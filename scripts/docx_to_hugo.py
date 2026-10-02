#!/usr/bin/env python3
"""
Update site pages from Word (.docx) files.

The DOCX files that colleagues edit are the source of truth for page text and
images; content/**/index.md is generated from them. This script converts each
DOCX to Hugo markdown and overwrites the page it is mapped to in
scripts/pages.csv. Everything else on the site is left alone.

Usage:
    python3 scripts/docx_to_hugo.py ~/Desktop/Week04_impuse_graphs.docx
    python3 scripts/docx_to_hugo.py ~/Downloads/updated-notes/     # a folder of .docx

Then review and publish:
    git diff content/        # check what changed
    hugo server              # look at it locally
    git commit ...           # discard instead with: git restore content/<page>

Requires pandoc (https://pandoc.org) on PATH. No Python packages needed.

How it works
------------
1. Look up the DOCX's filename in scripts/pages.csv to find its page folder.
   Unlisted files are skipped, with a suggested pages.csv line to add.
2. pandoc parses the DOCX into its document tree (JSON) and extracts images.
3. The tree is cleaned up in Python (see transform_blocks), which is far more
   reliable than search-and-replace on the markdown text:
     - Word "Title" style  -> page title (front matter)
     - "Reference: ..."    -> textbook_ref (front matter), if it is the first paragraph
     - Heading levels      -> shifted so the top level is ## (the title is the page's #)
     - YouTube link alone in a paragraph       -> {{< youtube >}}
     - "Simulation: <link>" alone in a paragraph -> {{< simulation >}}
     - Links to the live site / old DokuWiki   -> site-relative links
   (docs/editing-docx.md is the author-facing version of these rules.)
4. pandoc writes the tree back out as markdown, with $...$ math for KaTeX.
5. The page's index.md and media/ folder are replaced. Front matter the DOCX
   doesn't control (weight, anything added by hand) is kept.

Warnings are printed for things a person should check: images without alt
text, links to pages that don't exist, a missing Title, and so on.
"""

import csv
import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
PAGES_CSV = ROOT / "scripts" / "pages.csv"

# pandoc output: GitHub-flavored markdown, with math as $...$ / $$...$$
# (what KaTeX and Hugo's passthrough settings in hugo.toml expect) instead of
# GitHub's $`...`$ style.
MARKDOWN_FORMAT = "gfm-tex_math_gfm+tex_math_dollars"

REFERENCE_RE = re.compile(r"^\s*(?:textbook\s+)?references?\s*:\s*", re.IGNORECASE)
SIMULATION_RE = re.compile(r"^\s*(?:interactive\s+)?simulation\s*:", re.IGNORECASE)
VIDEO_CAPTION_RE = re.compile(r"^\s*video\s*:\s*(.*?)\s*[—–-]*\s*watch on youtube\s*$", re.IGNORECASE)
EXTERNAL_URL_RE = re.compile(r"^\s*\[External URL:\s*(\S+?)\s*\]\s*$")
YOUTUBE_RE = re.compile(
    r"^https?://(?:www\.|m\.)?(?:youtube\.com/(?:watch\?(?:.*&)?v=|embed/|shorts/)|youtu\.be/)([A-Za-z0-9_-]{11})"
)
LIVE_SITE_RE = re.compile(r"^https?://(?:www\.)?pcubed\.msuperl\.org(/[^\s]*)?$")
DOKUWIKI_RE = re.compile(r"doku\.php\?id=([\w:.-]+)(#\S*)?")
URL_RE = re.compile(r"^https?://\S+$")

# A "heading" this long is almost always a paragraph accidentally left in a
# Heading style in Word (it can be restyled to look normal on screen).
MAX_HEADING_CHARS = 100

# KaTeX doesn't support \mspace, which pandoc emits for spacing in Word equations.
MSPACE_RE = re.compile(r"\\mspace\{([^}]*)\}")


# --------------------------------------------------------------------------
# Finding pages
# --------------------------------------------------------------------------

def read_pages_csv() -> dict[str, Path]:
    """Lowercased DOCX filename -> page folder, from scripts/pages.csv."""
    lines = [line for line in PAGES_CSV.read_text().splitlines() if line.strip() and not line.startswith("#")]
    pages = {}
    for row in csv.DictReader(lines):
        pages[row["docx"].strip().lower()] = CONTENT / row["page"].strip().strip("/")
    return pages


def page_url(page_dir: Path) -> str:
    return "/" + page_dir.relative_to(CONTENT).as_posix() + "/"


def all_pages() -> dict[str, Path]:
    """Page folder name -> page folder, for every page on the site."""
    return {p.parent.name: p.parent for p in CONTENT.glob("**/index.md")}


def suggest_page(docx: Path) -> Path | None:
    """Best guess at an unlisted DOCX's page, so the error message can offer a
    ready-to-paste pages.csv line. Uses the old wiki page ID that many of the
    DOCX files still carry in File > Properties > Title (e.g.
    "183_notes:impulsegraphs"), then the filename minus a WeekNN_ prefix."""
    pages = all_pages()
    try:
        with zipfile.ZipFile(docx) as z:
            core = z.read("docProps/core.xml").decode("utf-8")
        m = re.search(r"<dc:title>[^<]*?([\w-]+)</dc:title>", core)
        if m and m.group(1) in pages:
            return pages[m.group(1)]
    except (KeyError, zipfile.BadZipFile):
        pass
    stem = re.sub(r"^(?:Weeks?[\d_-]*_|183_notes_(?:examples_)?)", "", docx.stem)
    return pages.get(stem)


# --------------------------------------------------------------------------
# pandoc
# --------------------------------------------------------------------------

def pandoc(args: list[str], stdin: str | None = None, cwd: Path | None = None) -> str:
    return subprocess.run(["pandoc", *args], input=stdin, cwd=cwd, capture_output=True,
                          text=True, check=True).stdout


def to_markdown(blocks: list, api_version: list) -> str:
    doc = {"pandoc-api-version": api_version, "meta": {}, "blocks": blocks}
    return pandoc(["-f", "json", "-t", MARKDOWN_FORMAT, "--wrap=none"], stdin=json.dumps(doc))


# --------------------------------------------------------------------------
# Working with pandoc's document tree
#
# pandoc's JSON is nested lists and {"t": type, "c": contents} dicts. The
# ones used here:
#   Para/Plain   {"t": "Para", "c": [inlines]}
#   Header       {"t": "Header", "c": [level, attr, [inlines]]}
#   Link/Image   {"t": "Link", "c": [attr, [inlines], [url, title]]}
#   Math         {"t": "Math", "c": [{"t": "InlineMath"|"DisplayMath"}, tex]}
#   Str          {"t": "Str", "c": "text"}
# --------------------------------------------------------------------------

SPACES = {"Space", "SoftBreak", "LineBreak"}
EMPHASIS = {"Emph", "Strong", "Underline", "Strikeout", "SmallCaps", "Superscript", "Subscript"}


def text_of(node, math_dollars: bool = False) -> str:
    """Plain text of a node or list of nodes (math optionally kept as $...$)."""
    if isinstance(node, list):
        return "".join(text_of(n, math_dollars) for n in node)
    t, c = node.get("t"), node.get("c")
    if t == "Str":
        return c
    if t in SPACES:
        return " "
    if t == "Math":
        return f"${c[1]}$" if math_dollars else c[1]
    if t in ("Code", "RawInline"):
        return c[1] if t == "Code" else ""
    if t == "Note":
        return ""
    if t in ("Link", "Image", "Span", "Quoted", "Cite"):
        inner = text_of(c[1], math_dollars)
        if t == "Quoted":
            return f"“{inner}”" if c[0]["t"] == "DoubleQuote" else f"‘{inner}’"
        return inner
    if isinstance(c, list):
        return text_of([x for x in c if isinstance(x, (dict, list))], math_dollars)
    return ""


def walk(node, fn):
    """Apply fn to every {"t": ...} node, bottom up. fn may return a list of
    nodes to splice in place of the node (used to unwrap emphasis)."""
    if isinstance(node, list):
        out = []
        for item in node:
            new = walk(item, fn)
            out.extend(new) if isinstance(new, list) and isinstance(item, dict) else out.append(new)
        return out
    if isinstance(node, dict):
        for key, value in node.items():
            node[key] = walk(value, fn)
        if "t" in node:
            return fn(node)
    return node


def lone_link(inlines: list) -> tuple[str, str] | None:
    """If a paragraph is just one link (or one typed URL), return (link text, url).
    A linked image (e.g. a video thumbnail) counts, with empty link text."""
    items = [x for x in inlines if x["t"] not in SPACES]
    if len(items) != 1:
        return None
    item = items[0]
    if item["t"] == "Link":
        has_image = any(x["t"] == "Image" for x in item["c"][1])
        return ("" if has_image else text_of(item["c"][1]).strip()), item["c"][2][0]
    if item["t"] == "Str" and URL_RE.match(item["c"]):
        return item["c"], item["c"]
    return None


def shortcode(name: str, **params) -> dict:
    args = " ".join(f'{k}="{v.replace(chr(34), "&quot;")}"' for k, v in params.items() if v)
    return {"t": "RawBlock", "c": ["html", f"{{{{< {name} {args} >}}}}"]}


# --------------------------------------------------------------------------
# Cleanup
# --------------------------------------------------------------------------

class ConversionError(Exception):
    """A DOCX that can't be converted; reported and skipped."""


class Page:
    def __init__(self, page_dir: Path):
        self.dir = page_dir
        self.warnings: list[str] = []

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def fix_inline(node: dict, page: Page, known: dict[str, Path]):
    t = node["t"]

    # Word sometimes italicizes/bolds a lone space or period between two
    # phrases. That's invisible in Word but becomes stray * in markdown.
    if t in EMPHASIS and not any(ch.isalnum() for ch in text_of(node["c"])):
        return node["c"]

    if t == "Math":
        node["c"][1] = MSPACE_RE.sub(r"\\mkern{\1}", node["c"][1])

    if t == "Link":
        url = node["c"][2][0]
        if m := LIVE_SITE_RE.match(url):
            url = m.group(1) or "/"
        elif m := DOKUWIKI_RE.search(url):
            slug = m.group(1).split(":")[-1]
            if slug in known:
                url = page_url(known[slug]) + (m.group(2) or "")
            else:
                page.warn(f"link to old wiki page with no match on this site: {url}")
        if url.startswith("/") and not url.startswith("//"):
            path = url.split("#")[0].split("?")[0].strip("/")
            if path and not ((CONTENT / path / "index.md").exists() or (CONTENT / path / "_index.md").exists()):
                page.warn(f"link to a page that doesn't exist: {url}")
        node["c"][2][0] = url

    return node


def transform_blocks(blocks: list, page: Page) -> tuple[list, str | None]:
    """Turn embed paragraphs into shortcodes, tidy headings, and pull out the
    textbook reference. Returns (blocks, textbook_ref)."""
    textbook_ref = None
    out: list = []

    for i, block in enumerate(blocks):
        t = block["t"]

        if t == "Header":
            text = text_of(block["c"][2]).strip()
            if not text:
                continue
            if len(text) > MAX_HEADING_CHARS:
                page.warn(f'paragraph in a Heading style turned back into text: "{text[:50]}..."')
                out.append({"t": "Para", "c": block["c"][2]})
                continue
            out.append(block)
            continue

        if t != "Para":
            out.append(block)
            continue

        inlines = block["c"]
        text = text_of(inlines).strip()

        # "Reference: Sections 2.1-2.4 in Matter and Interactions" as the first paragraph
        if not out and textbook_ref is None and REFERENCE_RE.match(text):
            textbook_ref = REFERENCE_RE.sub("", text_of(inlines, math_dollars=True)).strip()
            continue

        # YouTube link (or a linked video thumbnail) alone in a paragraph
        link = lone_link(inlines)
        if link and (vid := YOUTUBE_RE.match(link[1])):
            title = link[0] if link[0] and not URL_RE.match(link[0]) else ""
            out.append(("youtube", vid.group(1), title))
            continue

        # Older DOCX caption under a video: "Video: <title> — watch on YouTube"
        if (m := VIDEO_CAPTION_RE.match(text)) and out and isinstance(out[-1], tuple) and out[-1][0] == "youtube":
            out[-1] = ("youtube", out[-1][1], out[-1][2] or m.group(1).strip())
            continue

        # "Simulation: <linked title>" (or older "Interactive simulation: Title — <url>")
        if SIMULATION_RE.match(text):
            links = [x for x in inlines if x["t"] == "Link"]
            if len(links) == 1:
                url = links[0]["c"][2][0]
                title = text_of(links[0]["c"][1]).strip()
                if not title or URL_RE.match(title):
                    title = SIMULATION_RE.sub("", text.replace(url, "")).strip(" —–-:")
                if out and isinstance(out[-1], tuple) and out[-1][0] == "external-url" and out[-1][1] == url:
                    out.pop()  # older DOCX: "[External URL: ...]" placeholder just above it
                out.append(("simulation", url, title or "Interactive simulation"))
                continue
            page.warn(f'"Simulation:" paragraph needs exactly one link to become an embed: "{text[:60]}"')

        if m := EXTERNAL_URL_RE.match(text):
            out.append(("external-url", m.group(1), block))
            continue

        out.append(block)

    # Render the placeholders collected above
    blocks = []
    for item in out:
        if isinstance(item, tuple):
            kind = item[0]
            if kind == "youtube":
                blocks.append(shortcode("youtube", id=item[1], title=item[2]))
            elif kind == "simulation":
                blocks.append(shortcode("simulation", src=item[1], title=item[2]))
            else:
                page.warn(f"[External URL: {item[1]}] with no Simulation line under it; left as text")
                blocks.append(item[2])
        else:
            blocks.append(item)

    # The page title is the <h1>, so the document's top heading level becomes ##
    levels = [b["c"][0] for b in blocks if b["t"] == "Header"]
    if levels:
        shift = 2 - min(levels)
        for b in blocks:
            if b["t"] == "Header":
                b["c"][0] = min(6, b["c"][0] + shift)

    return blocks, textbook_ref


def check_images(blocks: list, page: Page) -> None:
    missing = 0

    def visit(node):
        nonlocal missing
        if node["t"] == "Image":
            alt = text_of(node["c"][1]).strip()
            if not alt or "ALT TEXT NEEDED" in alt:
                missing += 1
        return node

    walk(blocks, visit)
    if missing:
        page.warn(f"{missing} image(s) without alt text (in Word: right-click image > View Alt Text)")


# --------------------------------------------------------------------------
# Front matter
# --------------------------------------------------------------------------

def read_front_matter(index_md: Path) -> list[tuple[str, str]]:
    """Existing front matter as (key, raw lines) pairs, in order, so keys this
    script doesn't manage are written back exactly as they were."""
    if not index_md.exists():
        return []
    text = index_md.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return []
    entries: list[tuple[str, str]] = []
    for line in m.group(1).split("\n"):
        key = re.match(r"^([A-Za-z_][\w-]*):", line)
        if key:
            entries.append((key.group(1), line))
        elif entries:
            entries[-1] = (entries[-1][0], entries[-1][1] + "\n" + line)
    return entries


def front_matter_value(line: str) -> str:
    """The string value of a one-line `key: value` front matter entry."""
    value = line.split(":", 1)[-1].strip()
    if value.startswith('"'):
        return json.loads(value)
    if value.startswith("'"):
        return value[1:-1].replace("''", "'")
    return value


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)  # a JSON string is a valid YAML string


def next_weight(page_dir: Path) -> int:
    weights = [0]
    for sibling in page_dir.parent.glob("*/index.md"):
        for key, line in read_front_matter(sibling):
            if key == "weight" and (w := re.search(r"-?\d+", line)):
                weights.append(int(w.group()))
    return max(weights) + 1


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def convert(docx: Path, page_dir: Path, known: dict[str, Path]) -> Page:
    page = Page(page_dir)
    index_md = page_dir / "index.md"
    old_fm = read_front_matter(index_md)
    old = dict(old_fm)

    if not index_md.exists():
        if not (page_dir.parent / "_index.md").exists():
            raise ConversionError(f"{page_dir.parent.relative_to(ROOT)} isn't a section of the site; check pages.csv")
        page.warn("new page")

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        # Images land in tmp/media/ and are referenced as ./media/imageN.ext
        doc = json.loads(pandoc([str(docx.resolve()), "-t", "json", "--extract-media=."], cwd=tmp))

        meta_title = doc["meta"].get("title")
        title = text_of(meta_title["c"], math_dollars=True).strip() if meta_title else ""
        if not title:
            title = front_matter_value(old.get("title", ""))
            if not title:
                raise ConversionError("no paragraph in Word's \"Title\" style, and the page has no title yet")
            page.warn(f'no paragraph in Word\'s "Title" style; kept the current title "{title}"')

        blocks = walk(doc["blocks"], lambda n: fix_inline(n, page, known))
        blocks, textbook_ref = transform_blocks(blocks, page)
        check_images(blocks, page)
        if "textbook_ref" in old and not textbook_ref:
            page.warn('no "Reference:" first paragraph; textbook reference removed from the page')

        body = to_markdown(blocks, doc["pandoc-api-version"])

        # Front matter: title/textbook_ref come from the DOCX, the rest is kept
        fm = [f"title: {yaml_string(title)}"]
        fm += [line for key, line in old_fm if key not in ("title", "textbook_ref")]
        if "weight" not in old:
            fm.append(f"weight: {next_weight(page_dir)}")
        if textbook_ref:
            fm.append(f"textbook_ref: {yaml_string(textbook_ref)}")

        # Only touch the page once everything above has succeeded
        page_dir.mkdir(parents=True, exist_ok=True)
        shutil.rmtree(page_dir / "media", ignore_errors=True)
        for image in sorted((tmp / "media").glob("*")):
            if f"media/{image.name}" in body:  # skip e.g. video thumbnails replaced by embeds
                (page_dir / "media").mkdir(exist_ok=True)
                shutil.copy2(image, page_dir / "media")
        index_md.write_text("---\n" + "\n".join(fm) + "\n---\n\n" + body)

    return page


def main() -> None:
    args = [Path(a).expanduser() for a in sys.argv[1:]]
    if not args or any(a.name in ("-h", "--help") for a in args):
        sys.exit(__doc__.split("How it works")[0].strip())

    docx_files = []
    for arg in args:
        found = sorted(arg.glob("*.docx")) if arg.is_dir() else [arg]
        docx_files += [p for p in found if not p.name.startswith("~$")]  # skip Word lock files
    if not docx_files:
        sys.exit("No .docx files found.")

    pages = read_pages_csv()
    known = all_pages()
    failed = []

    for docx in docx_files:
        page_dir = pages.get(docx.name.lower())
        if page_dir is None:
            guess = suggest_page(docx)
            hint = f"{docx.name},{guess.relative_to(CONTENT).as_posix()}" if guess else f"{docx.name},notes/<week-folder>/<page-folder>"
            print(f"✗ {docx.name}: not listed in scripts/pages.csv. Add a line like:\n    {hint}")
            failed.append(docx.name)
            continue
        try:
            page = convert(docx, page_dir, known)
        except subprocess.CalledProcessError as e:
            print(f"✗ {docx.name}: pandoc failed:\n{e.stderr}")
            failed.append(docx.name)
            continue
        except ConversionError as e:
            print(f"✗ {docx.name}: {e}")
            failed.append(docx.name)
            continue
        print(f"✓ {docx.name} → {(page_dir / 'index.md').relative_to(ROOT)}")
        for w in page.warnings:
            print(f"    ! {w}")

    print(f"\n{len(docx_files) - len(failed)} updated, {len(failed)} skipped. Review with: git diff content/")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()

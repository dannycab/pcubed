#!/usr/bin/env python3
"""
Incrementally regenerate Hugo content pages from updated docx files.

The instructor's Word docs (kept in OneDrive) are the source of truth;
content/ is a generated copy. When a new batch of docx comes down (a folder
full of *.docx, e.g. a OneDrive download), this script matches each file to
its existing content bundle by slug and regenerates just that page -- text
and images -- leaving every other page untouched.

Matching: filenames have carried a few different prefixes over time
(`Week01_foo.docx`, `183_notes_foo.docx`, `183_notes_examples_foo.docx`, or
just `foo.docx`). Known prefixes are stripped and what's left is matched
against the slug of an existing content bundle (the page's own directory
name, e.g. content/notes/week-01-.../scalars_and_vectors/). A file that
doesn't match anything existing is reported, not guessed at -- a genuinely
new page still needs a human to decide where it belongs in content/.

Reuses the docx -> markdown cleanup helpers from migrate.py (the original
one-shot site migration): heading/title extraction, math delimiter
conversion, youtube/simulation shortcode detection, front matter quoting.
Two things migrate.py didn't need to handle, because they only showed up
once editors started working from the live site instead of the old wiki:
  - Links typed straight to the live site (https://pcubed.msuperl.org/...)
    are converted back to root-relative Hugo links.
  - A shortcode (youtube/simulation) only comes back if the docx still
    matches the exact convention migrate.py looks for (an embedded video
    thumbnail linked to a YouTube URL, or an "Interactive simulation:
    Title - <url>" line). If an editor rewrites that bit as plain prose,
    it comes through as a plain paragraph/link instead -- not a crash,
    just a plainer result.

Usage:
    python3 scripts/update_from_docx.py <folder-of-docx>

Requires: pandoc on PATH. No other dependencies. Changes land as normal
uncommitted edits under content/ -- review with `git diff content/` and
discard with `git checkout -- content/<path>` if something looks wrong.
"""

import html
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import migrate  # noqa: E402 (reuses split_title/demote_headings/convert_math/convert_youtube/convert_simulations/yaml_single_quote/LINK_MAP/link regexes)

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"
TODO_PATH = ROOT / "scripts" / "content-todo.txt"

WEIGHT_RE = re.compile(r"^weight:\s*(\S+)\s*$", re.MULTILINE)
PCUBED_LINK_RE = re.compile(r"https?://(?:www\.)?pcubed\.msuperl\.org(/[^\s)]*)")
EXAMPLES_WIKI_LINK_RE = re.compile(
    r"https?://(?:www\.)?msuperl\.org/wikis/pcubed/doku\.php\?id=183_notes:examples:([a-zA-Z0-9_-]+)(#[a-zA-Z0-9_]*)?"
)
KNOWN_PREFIXES = [
    re.compile(r"^183_notes_examples_"),
    re.compile(r"^183_notes_"),
    re.compile(r"^Weeks?[\d_-]*_"),
]

# A paragraph can carry Word's "Heading N" style while its runs override the
# font/size/color to look like normal body text -- so it looks fine on screen
# in Word but pandoc (which reads the style, not the on-screen appearance)
# still emits it as a heading. A heading that's empty or this long is almost
# certainly one of those, not a real section title, so it gets demoted back
# to a plain paragraph (or dropped, if empty) rather than shipped as-is.
HEADING_LINE_RE = re.compile(r"^(#{1,6})\s*(.*)$")
LONG_HEADING_CHARS = 100


def find_bundles() -> dict[str, tuple[Path, str]]:
    """slug -> (bundle_dir, content-todo.txt key), scanned from the *current*
    content tree so it reflects whatever pages actually exist today."""
    bundles: dict[str, tuple[Path, str]] = {}
    for index_md in CONTENT_DIR.glob("notes/*/*/index.md"):
        slug = index_md.parent.name
        todo_key = f"{index_md.parent.parent.name}/{slug}"
        bundles[slug] = (index_md.parent, todo_key)
    for index_md in CONTENT_DIR.glob("examples/*/index.md"):
        slug = index_md.parent.name
        bundles[slug] = (index_md.parent, f"examples/{slug}")
    return bundles


def slug_candidates(stem: str) -> list[str]:
    candidates = [stem]
    for prefix_re in KNOWN_PREFIXES:
        if prefix_re.match(stem):
            candidates.append(prefix_re.sub("", stem))
    return candidates


def match_bundle(docx_path: Path, bundles: dict[str, tuple[Path, str]]) -> tuple[Path, str] | None:
    for candidate in slug_candidates(docx_path.stem):
        if candidate in bundles:
            return bundles[candidate]
    return None


RUN_RE = re.compile(r"<w:r(?:\s[^>]*)?>.*?</w:r>", re.DOTALL)
RUN_TEXT_RE = re.compile(r"<w:t(?:\s[^>]*)?>(.*?)</w:t>", re.DOTALL)
EMPHASIS_TOGGLE_RE = re.compile(r"<w:(?:b|bCs|i|iCs)(?:\s[^>]*)?/>")


def clean_docx_for_pandoc(docx_path: Path, tmp_dir: Path) -> Path:
    """Word sometimes tags a run holding only whitespace/punctuation -- a
    lone space or a stray ".  " left over between two differently-styled
    phrases -- as bold/italic. It's invisible in Word (italics don't show on
    a space or a period), but pandoc has to represent it in markdown, and
    CommonMark forbids opening/closing emphasis next to such a boundary, so
    pandoc shoves the `*` onto the nearest word instead, producing stray
    literal asterisks in the rendered page. Clear bold/italic from any run
    that has no letters or digits at all before handing the docx to pandoc.

    This edits word/document.xml as plain text, not via an XML parser: Word
    documents wrap things like embedded images in mc:AlternateContent blocks
    that reference namespace prefixes (e.g. "wps") by their literal string,
    outside XML's own namespace mechanism. Round-tripping through
    xml.etree.ElementTree renames prefixes it didn't already know about
    (r -> ns3, wp -> ns4, ...), which silently breaks those references and
    makes pandoc drop the content entirely -- confirmed by testing a no-op
    ElementTree parse+reserialize, which lost embedded YouTube thumbnails
    with no error. A targeted string substitution leaves everything else in
    the file byte-for-byte untouched."""
    with zipfile.ZipFile(docx_path) as zin:
        document_xml = zin.read("word/document.xml").decode("utf-8")
        other_entries = [(item, zin.read(item.filename)) for item in zin.infolist() if item.filename != "word/document.xml"]

    changed = 0

    def clean_run(m: re.Match) -> str:
        nonlocal changed
        run = m.group(0)
        text = "".join(html.unescape(t) for t in RUN_TEXT_RE.findall(run))
        if text and not any(ch.isalnum() for ch in text):
            cleaned, n = EMPHASIS_TOGGLE_RE.subn("", run)
            if n:
                changed += n
                return cleaned
        return run

    fixed_xml = RUN_RE.sub(clean_run, document_xml)
    if not changed:
        return docx_path

    fixed_path = tmp_dir / docx_path.name
    with zipfile.ZipFile(fixed_path, "w", zipfile.ZIP_DEFLATED) as zout:
        zout.writestr("word/document.xml", fixed_xml.encode("utf-8"))
        for item, data in other_entries:
            zout.writestr(item, data)
    return fixed_path


def read_current_weight(bundle_dir: Path) -> str | None:
    match = WEIGHT_RE.search((bundle_dir / "index.md").read_text())
    return match.group(1) if match else None


def rewrite_links(body: str, examples_link_map: dict[str, str]) -> str:
    def examples_wiki_sub(m):
        slug, anchor = m.group(1), m.group(2) or ""
        return examples_link_map[slug] + anchor if slug in examples_link_map else m.group(0)

    body = EXAMPLES_WIKI_LINK_RE.sub(examples_wiki_sub, body)

    def notes_wiki_sub(m):
        slug, anchor = m.group(1), m.group(2) or ""
        return migrate.LINK_MAP[slug] + anchor if slug in migrate.LINK_MAP else m.group(0)

    body = migrate.WIKI_LINK_RE.sub(notes_wiki_sub, body)

    def other_wiki_sub(m):
        full_id = m.group(1)
        if ":" in full_id and full_id.split(":", 1)[0] == "183_notes":
            leaf = full_id.split(":")[-1]
            if leaf in migrate.LINK_MAP:
                return migrate.LINK_MAP[leaf]
        return "https://www.msuperl.org/wikis/pcubed/doku.php?id=" + full_id

    body = migrate.OTHER_WIKI_LINK_RE.sub(other_wiki_sub, body)
    body = PCUBED_LINK_RE.sub(lambda m: m.group(1), body)
    return body


def fix_mis_styled_headings(body: str) -> tuple[str, int]:
    in_fence = False
    out_lines = []
    fixed = 0
    for line in body.split("\n"):
        if line.startswith("```"):
            in_fence = not in_fence
            out_lines.append(line)
            continue
        if not in_fence:
            m = HEADING_LINE_RE.match(line)
            if m:
                text = m.group(2).strip()
                if not text or len(text) > LONG_HEADING_CHARS:
                    fixed += 1
                    if text:
                        out_lines.append(text)
                    continue
        out_lines.append(line)
    return "\n".join(out_lines), fixed


def process_bundle(docx_path: Path, bundle_dir: Path, examples_link_map: dict[str, str], tmp_dir: Path) -> list[str]:
    weight = read_current_weight(bundle_dir)

    media_dir = bundle_dir / "media"
    if media_dir.exists():
        shutil.rmtree(media_dir)

    cleaned_docx = clean_docx_for_pandoc(docx_path, tmp_dir)
    subprocess.run(
        ["pandoc", str(cleaned_docx), "-t", "gfm", "--wrap=none",
         "-o", "index.md", "--extract-media=."],
        cwd=bundle_dir, check=True,
    )
    if media_dir.exists() and not any(media_dir.iterdir()):
        media_dir.rmdir()

    raw = (bundle_dir / "index.md").read_text()
    title, textbook_ref, body = migrate.split_title(raw)
    title = migrate.convert_math(title)
    body = migrate.demote_headings(body)
    body = migrate.convert_math(body)
    body = migrate.convert_youtube(body)
    body = migrate.convert_simulations(body)
    body = rewrite_links(body, examples_link_map)
    body, fixed_headings = fix_mis_styled_headings(body)

    fm_lines = ["---", f"title: {migrate.yaml_single_quote(title)}"]
    if weight is not None:
        fm_lines.append(f"weight: {weight}")
    if textbook_ref:
        fm_lines.append(f"textbook_ref: {migrate.yaml_single_quote(textbook_ref)}")
    fm_lines.append("---\n")
    (bundle_dir / "index.md").write_text("\n".join(fm_lines) + "\n" + body)

    notes = []
    if "ALT TEXT NEEDED" in body:
        notes.append(f"{body.count('ALT TEXT NEEDED')} image(s) missing alt text")
    if "MANUAL REVIEW" in body:
        notes.append("embed/link flagged for manual review")
    if fixed_headings:
        notes.append(
            f"{fixed_headings} heading(s) demoted to plain text (empty, or over {LONG_HEADING_CHARS} chars "
            "-- likely a paragraph left in a Heading style in Word); double check nothing real got flattened"
        )
    return notes


def update_todo_file(todo_key: str, notes: list[str]) -> None:
    lines = TODO_PATH.read_text().splitlines() if TODO_PATH.exists() else []
    lines = [line for line in lines if not line.startswith(f"{todo_key}:")]
    if notes:
        lines.append(f"{todo_key}: " + "; ".join(notes))
    TODO_PATH.write_text("\n".join(lines) + ("\n" if lines else ""))


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 scripts/update_from_docx.py <folder-of-docx>")

    incoming_dir = Path(sys.argv[1]).expanduser()
    docx_files = sorted(p for p in incoming_dir.glob("*.docx") if not p.name.startswith("~$"))
    if not docx_files:
        sys.exit(f"No .docx files found in {incoming_dir}")

    bundles = find_bundles()
    examples_link_map = {
        slug: f"/examples/{slug}/" for slug, (_, todo_key) in bundles.items() if todo_key.startswith("examples/")
    }

    updated, unmatched = [], []
    with tempfile.TemporaryDirectory() as tmp_dir_name:
        tmp_dir = Path(tmp_dir_name)
        for docx_path in docx_files:
            match = match_bundle(docx_path, bundles)
            if match is None:
                unmatched.append(docx_path.name)
                continue
            bundle_dir, todo_key = match
            notes = process_bundle(docx_path, bundle_dir, examples_link_map, tmp_dir)
            update_todo_file(todo_key, notes)
            updated.append((docx_path.name, todo_key))
            flag = f"  [{'; '.join(notes)}]" if notes else ""
            print(f"  {docx_path.name} -> content/{'notes/' if not todo_key.startswith('examples/') else ''}{todo_key}/index.md{flag}")

    print(f"\nUpdated {len(updated)} page(s).")
    if unmatched:
        print(f"\n{len(unmatched)} file(s) didn't match an existing page (new page? needs a human to place it):")
        for name in unmatched:
            print(f"  - {name}")
    print("\nReview with: git diff content/")


if __name__ == "__main__":
    main()

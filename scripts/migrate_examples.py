#!/usr/bin/env python3
"""One-shot migration of docx examples -> Hugo content bundles. Not meant to
be re-run idempotently on hand-edited output. Sibling to migrate.py, reusing
its generic markdown-cleanup helpers; examples are a flat namespace (no
weeks) so they get their own top-level section instead of living under
content/notes."""
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import migrate  # noqa: E402  (reuses split_title/demote_headings/convert_math/convert_youtube/LINK_MAP)

DOCX_DIR = Path.home() / "Desktop/pcubed-solutions/docx/183_examples"
HTML_DIR = Path.home() / "Desktop/pcubed-solutions/html-complete/183_examples"
CONTENT_DIR = ROOT / "content" / "examples"

SLUGS = sorted(
    p.stem.removeprefix("183_notes_examples_") for p in DOCX_DIR.glob("183_notes_examples_*.docx")
)
assert len(SLUGS) == 52

EXAMPLES_LINK_MAP = {slug: f"/examples/{slug}/" for slug in SLUGS}
NOTES_LINK_MAP = migrate.LINK_MAP

EXAMPLES_WIKI_LINK_RE = re.compile(
    r"https?://(?:www\.)?msuperl\.org/wikis/pcubed/doku\.php\?id=183_notes:examples:([a-zA-Z0-9_-]+)(#[a-zA-Z0-9_]*)?"
)
NOTES_WIKI_LINK_RE = re.compile(
    r"https?://(?:www\.)?msuperl\.org/wikis/pcubed/doku\.php\?id=183_notes:([a-zA-Z0-9_]+)(#[a-zA-Z0-9_]*)?"
)


def convert_docx(slug: str, bundle_dir: Path):
    docx_path = DOCX_DIR / f"183_notes_examples_{slug}.docx"
    bundle_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["pandoc", str(docx_path), "-t", "gfm", "--wrap=none",
         "-o", "index.md", "--extract-media=."],
        cwd=bundle_dir, check=True,
    )
    media_dir = bundle_dir / "media"
    if media_dir.exists() and not any(media_dir.iterdir()):
        media_dir.rmdir()


def rewrite_links(body: str) -> str:
    def examples_sub(m):
        slug = m.group(1)
        anchor = m.group(2) or ""
        if slug in EXAMPLES_LINK_MAP:
            return EXAMPLES_LINK_MAP[slug] + anchor
        return m.group(0)

    body = EXAMPLES_WIKI_LINK_RE.sub(examples_sub, body)

    def notes_sub(m):
        slug = m.group(1)
        anchor = m.group(2) or ""
        if slug in NOTES_LINK_MAP:
            return NOTES_LINK_MAP[slug] + anchor
        return m.group(0)

    body = NOTES_WIKI_LINK_RE.sub(notes_sub, body)
    return body


def count_dropped_images(slug: str, body: str) -> int:
    """convert_to_docx.py silently decompose()s any content image it can't
    recover bytes for -- no placeholder, no marker -- so that loss is
    invisible in the migrated markdown unless we diff against the source
    HTML's image count ourselves."""
    matches = list(HTML_DIR.glob(f"183_notes_examples_{slug} *.html"))
    if not matches:
        return 0
    source_html = matches[0].read_text(encoding="utf-8", errors="replace")
    source_count = source_html.count('img-responsive')
    return max(0, source_count - body.count("<img"))


def process_page(slug: str):
    """Converts and cleans one example, returning its (title, body) without
    writing frontmatter yet -- final weight isn't known until all titles are
    collected and sorted."""
    bundle_dir = CONTENT_DIR / slug
    convert_docx(slug, bundle_dir)
    raw = (bundle_dir / "index.md").read_text()
    title, textbook_ref, body = migrate.split_title(raw)
    title = migrate.convert_math(title)
    body = migrate.demote_headings(body)
    body = migrate.convert_math(body)
    body = migrate.convert_youtube(body)
    body = rewrite_links(body)
    return bundle_dir, title, textbook_ref, body


def write_page(bundle_dir: Path, title: str, textbook_ref: str, body: str, weight: int):
    fm_lines = ["---", f"title: {migrate.yaml_single_quote(title)}", f"weight: {weight}"]
    if textbook_ref:
        fm_lines.append(f"textbook_ref: {migrate.yaml_single_quote(textbook_ref)}")
    fm_lines.append("---\n")
    (bundle_dir / "index.md").write_text("\n".join(fm_lines) + "\n" + body)


def write_examples_index():
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    (CONTENT_DIR / "_index.md").write_text(
        "\n".join(["---", 'title: "Examples"', "---", ""])
    )


def main():
    if CONTENT_DIR.exists():
        shutil.rmtree(CONTENT_DIR)
    write_examples_index()

    pages = []
    for slug in SLUGS:
        bundle_dir, title, textbook_ref, body = process_page(slug)
        pages.append((slug, bundle_dir, title, textbook_ref, body))
        print(f"ok: {slug}")

    pages.sort(key=lambda p: p[2].lower())

    alt_todo = []
    for weight, (slug, bundle_dir, title, textbook_ref, body) in enumerate(pages, start=1):
        write_page(bundle_dir, title, textbook_ref, body, weight)
        text = (bundle_dir / "index.md").read_text()
        notes = []
        if "ALT TEXT NEEDED" in text:
            notes.append(f"{text.count('ALT TEXT NEEDED')} image(s) missing alt text")
        if "MANUAL REVIEW" in text:
            notes.append("embed/link flagged for manual review")
        dropped = count_dropped_images(slug, body)
        if dropped:
            notes.append(f"{dropped} content image(s) dropped entirely (unrecoverable, no alt-text placeholder to find)")
        if notes:
            alt_todo.append(f"examples/{slug}: " + "; ".join(notes))

    existing_todo = ROOT / "scripts" / "content-todo.txt"
    prior = existing_todo.read_text() if existing_todo.exists() else ""
    prior = "\n".join(line for line in prior.splitlines() if not line.startswith("examples/"))
    combined = (prior + "\n" if prior else "") + "\n".join(alt_todo) + ("\n" if alt_todo else "")
    existing_todo.write_text(combined)
    print(f"\n{len(alt_todo)} example pages have pending content todos; see scripts/content-todo.txt")


if __name__ == "__main__":
    main()

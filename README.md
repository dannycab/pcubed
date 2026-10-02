# pcubed

Course notes and worked examples for Projects & Practices in Physics –
Mechanics, published at <https://pcubed.msuperl.org/>. It's a
[Hugo](https://gohugo.io) site, deployed to GitHub Pages on every push to
`main` (see `.github/workflows/hugo.yml`).

## Layout

```
content/notes/<week>/<page>/index.md   one page of notes (+ media/ for its images)
content/examples/<page>/index.md       one worked example
layouts/                               templates; shortcodes in layouts/shortcodes/
scripts/docx_to_hugo.py                DOCX -> page converter
scripts/pages.csv                      which DOCX updates which page
docs/editing-docx.md                   guide for colleagues editing the Word files
```

## Updating pages from Word files

The Word files colleagues edit are the source of truth. Each page's
`index.md` and `media/` are regenerated from its DOCX, so **edits made
directly to a page's markdown are lost the next time its DOCX comes in.**
Make content changes in the DOCX. (Front matter fields like `weight` are
kept.)

You need [pandoc](https://pandoc.org) (`brew install pandoc`) and
Hugo extended.

1. **Convert.** Pass one or more DOCX files, or a folder of them:

   ```sh
   python3 scripts/docx_to_hugo.py ~/Desktop/Week04_impuse_graphs.docx
   ```

   If a file isn't in `scripts/pages.csv`, it's skipped and the script
   prints a line to add, with a guess at the page when it can make one.
   For a new page, add a line with a folder that doesn't exist yet. The
   script creates the page at the end of that week.

2. **Read the warnings.** Lines marked `!` need a human: missing alt text,
   links to pages that don't exist, a missing Title paragraph, a
   "Simulation:" line without a link, and so on. Fix them in the DOCX (or
   ask the author) and re-run.

3. **Review.**

   ```sh
   git diff content/
   hugo server            # http://localhost:1313/
   ```

   To discard a page's changes: `git restore content/<path>/` (and
   `git clean -fd content/<path>/media` for new images).

4. **Publish.** Commit on `dev`, then merge to `main`.

### What the converter does

pandoc reads the DOCX into its document structure. `docx_to_hugo.py`
adjusts that structure, and pandoc writes markdown. The conventions,
documented for authors in `docs/editing-docx.md`:

| In the DOCX                                    | On the site                                   |
|------------------------------------------------|-----------------------------------------------|
| Paragraph in the **Title** style               | `title:` front matter (the page's `<h1>`)      |
| First paragraph starting `Reference:`          | `textbook_ref:` front matter                   |
| Heading 1 / Heading 2 / …                      | `##` / `###` / …                               |
| A YouTube link (or linked thumbnail) alone in a paragraph | `{{< youtube >}}`, link text as its title |
| `Simulation: <link>` alone in a paragraph      | `{{< simulation >}}`                           |
| Links to pcubed.msuperl.org or the old wiki    | site-relative links (`/notes/...`)             |
| Word equations                                 | `$...$` / `$$...$$`, rendered by KaTeX         |

It also absorbs older DOCX conventions (`Video: … — watch on YouTube`
captions and `[External URL: …]` lines above simulations) and cleans up
two Word quirks: bold/italic on stray spaces and punctuation, and long
paragraphs left in a Heading style.

To support a new convention, add a case to `transform_blocks()` in
`docx_to_hugo.py`. To see the structure pandoc gives a tricky DOCX, run
`pandoc file.docx -t native`.

## Open content work

- 77 pages have images with placeholder alt text:
  `grep -rl "ALT TEXT NEEDED" content`

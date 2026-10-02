# Editing the notes in Word

Each page on the site is built from one Word file (.docx). When you send an
updated file, it replaces that page's text and images. A few habits make
the conversion come out right without anyone having to fix it by hand.

## Before you send a file

- **Keep the filename the same.** The filename tells the site which page to
  update. Renaming `Week04_impulse_graphs.docx` to `impulse graphs v2.docx`
  means the site maintainer has to look up where it goes. For a brand-new
  page, say which week it belongs in.
- **Send the .docx itself**, not a PDF or a Google Doc link.

## Title and reference

- Put the page title in the first paragraph, in Word's **Title** style
  (Home tab > Styles > Title).
- If the page has a textbook reference, make it the next paragraph and start
  it with `Reference:`. For example:
  `Reference: Sections 2.1–2.4 in Matter and Interactions (4th edition)`
- Leave out anything you don't want on the page (notes to yourself, "DRAFT").

## Headings

- Use **Heading 1** for sections and **Heading 2** for subsections. Choose
  headings from the Styles menu; making text big and bold by hand doesn't
  count.
- A heading should be a short phrase. If you restyle a heading paragraph to
  look like normal text, change its style to **Normal** instead. Otherwise it
  still counts as a heading on the website.

## Videos and simulations

Put each one in **its own paragraph**:

| To get…                  | Type this, alone in a paragraph                                    |
|--------------------------|--------------------------------------------------------------------|
| A YouTube video          | The YouTube link: `https://www.youtube.com/watch?v=RXJ0XlcPBRg`. If you make descriptive text the link (e.g. "Lecture 4: Force vs. Time"), that text becomes the video's title for screen readers. |
| An interactive simulation | `Simulation: ` followed by the simulation's name, with the name linked to the simulation (Insert > Link). Example: Simulation: [Impulse Graph](https://demos.msuperl.org/interactive/mechanics/net_force_vs_time_discrete.html) |

A YouTube link inside a sentence stays an ordinary link. Pasting a video
thumbnail image that links to YouTube also works.

## Equations

- Use Word's equation editor (Insert > Equation, or Alt + =) for all math,
  including single variables like *x* in a sentence. Typing "Δp" as ordinary
  text works but won't look like the other equations.
- Avoid equations that are pictures (screenshots, or MathType objects shown
  as images). Screen readers can't read them and they can't be edited later.

## Images

- **Add alt text to every image.** Right-click the image > View Alt Text, and
  describe what a student needs to know from it, for example "Force vs. time
  graph: a positive rectangle from 0–2 s and a negative triangle from 2–4 s."
  Images without alt text are inaccessible, and the update gets flagged.
- Insert images **In Line with Text** (Picture Format > Wrap Text). Floating
  or text-wrapped images can end up in odd places on the web page.
- Use pictures (PNG/JPG). Diagrams drawn with Word's shapes or text boxes
  don't convert; take a screenshot of them, or save them as a picture first.

## Links

- To link to another page of the notes, copy its address from the live site
  (`https://pcubed.msuperl.org/notes/...`) and use Insert > Link. Links still
  pointing at the old wiki (`msuperl.org/wikis/...`) are converted
  automatically when possible.
- Link meaningful words ("the Momentum Principle"), not "click here".

## Things that don't come through

Word features without a web equivalent are dropped or flattened. These
include comments, tracked changes (accept or reject them first), text boxes,
columns, page breaks, headers and footers, colored or highlighted text,
and font choices. Bold, italics, lists, tables and footnotes all work.

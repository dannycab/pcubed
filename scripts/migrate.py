#!/usr/bin/env python3
"""One-shot migration of docx notes -> Hugo content bundles. Not meant to be re-run idempotently on hand-edited output."""
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCX_DIR = Path.home() / "Desktop/pcubed-solutions/docx/183_notes"
CONTENT_DIR = ROOT / "content" / "notes"

WEEKS = [
    ("week-01-modeling-motion-no-net-force", "Week 1: Modeling Motion with No Net Force", 1),
    ("week-02-modeling-motion-net-force", "Week 2: Modeling Motion with a Net Force", 2),
    ("week-03-newtonian-gravitation", "Week 3: Modeling Motion with Non-Constant Forces — Newtonian Gravitation", 3),
    ("week-04-05-springs-contact-interactions", "Weeks 4–5: Springs and Contact Interactions", 4),
    ("week-06-solids-curved-motion", "Week 6: Solids and Curved Motion", 5),
    ("week-07-energy-transfer", "Week 7: Energy Transfer in Single and Multi-Particle Systems", 6),
    ("week-08-potential-energy-applications", "Week 8: Potential Energy Applications", 7),
    ("week-10-internal-energy-heat", "Week 10: Internal Energy and Heat", 8),
    ("week-11-multi-particle-energy", "Week 11: Multi-Particle Energy Systems", 9),
    ("week-12-14-collisions-rotational-motion", "Weeks 12–14: Collisions and Rotational Motion", 10),
    ("week-15-core-principles", "Week 15: Core Principles", 11),
]

# slug -> (week_dir, weight within week)
PAGES = {
    "scalars_and_vectors": ("week-01-modeling-motion-no-net-force", 1),
    "displacement_and_velocity": ("week-01-modeling-motion-no-net-force", 2),
    "modeling_with_vpython": ("week-01-modeling-motion-no-net-force", 3),
    "relative_motion": ("week-01-modeling-motion-no-net-force", 4),
    "graphing_motion": ("week-01-modeling-motion-no-net-force", 5),

    "momentum": ("week-02-modeling-motion-net-force", 1),
    "momentum_principle": ("week-02-modeling-motion-net-force", 2),
    "acceleration": ("week-02-modeling-motion-net-force", 3),
    "motionpredict": ("week-02-modeling-motion-net-force", 4),
    "constantf": ("week-02-modeling-motion-net-force", 5),
    "localg": ("week-02-modeling-motion-net-force", 6),
    "iterativepredict": ("week-02-modeling-motion-net-force", 7),
    "drag": ("week-02-modeling-motion-net-force", 8),

    "gravitation": ("week-03-newtonian-gravitation", 1),
    "grav_accel": ("week-03-newtonian-gravitation", 2),
    "ucm": ("week-03-newtonian-gravitation", 3),

    "impulsegraphs": ("week-04-05-springs-contact-interactions", 1),
    "springmotion": ("week-04-05-springs-contact-interactions", 2),
    "freebodydiagrams": ("week-04-05-springs-contact-interactions", 3),
    "friction": ("week-04-05-springs-contact-interactions", 4),
    "mp_multi": ("week-04-05-springs-contact-interactions", 5),
    "collisions": ("week-04-05-springs-contact-interactions", 6),

    "model_of_solids": ("week-06-solids-curved-motion", 1),
    "model_of_a_wire": ("week-06-solids-curved-motion", 2),
    "youngs_modulus": ("week-06-solids-curved-motion", 3),
    "curving_motion": ("week-06-solids-curved-motion", 4),
    "center_of_mass": ("week-06-solids-curved-motion", 5),

    "define_energy": ("week-07-energy-transfer", 1),
    "point_particle": ("week-07-energy-transfer", 2),
    "work": ("week-07-energy-transfer", 3),
    "work_by_nc_forces": ("week-07-energy-transfer", 4),
    "potential_energy": ("week-07-energy-transfer", 5),
    "grav_and_spring_pe": ("week-07-energy-transfer", 6),
    "rest_mass": ("week-07-energy-transfer", 7),

    "spring_pe": ("week-08-potential-energy-applications", 1),
    "force_and_pe": ("week-08-potential-energy-applications", 2),
    "newton_grav_pe": ("week-08-potential-energy-applications", 3),
    "grav_pe_graphs": ("week-08-potential-energy-applications", 4),
    "escape_speed": ("week-08-potential-energy-applications", 5),
    "colliding_systems": ("week-08-potential-energy-applications", 6),

    "internal_energy": ("week-10-internal-energy-heat", 1),
    "heat": ("week-10-internal-energy-heat", 2),
    "power": ("week-10-internal-energy-heat", 3),
    "system_choice": ("week-10-internal-energy-heat", 4),
    "energy_dissipation": ("week-10-internal-energy-heat", 5),

    "energy_sep": ("week-11-multi-particle-energy", 1),
    "rot_ke": ("week-11-multi-particle-energy", 2),
    "pp_vs_real": ("week-11-multi-particle-energy", 3),
    "proof_of_pp": ("week-11-multi-particle-energy", 4),

    "discovery_of_the_nucleus": ("week-12-14-collisions-rotational-motion", 1),
    "angular_motivation": ("week-12-14-collisions-rotational-motion", 2),
    "torque": ("week-12-14-collisions-rotational-motion", 3),
    "static_eq": ("week-12-14-collisions-rotational-motion", 4),
    "torquediagram": ("week-12-14-collisions-rotational-motion", 5),
    "ang_momentum": ("week-12-14-collisions-rotational-motion", 6),
    "l_principle": ("week-12-14-collisions-rotational-motion", 7),
    "l_conservation": ("week-12-14-collisions-rotational-motion", 8),

    "fundamental_principles": ("week-15-core-principles", 1),
}

assert len(PAGES) == 58

LINK_MAP = {slug: f"/notes/{week_dir}/{slug}/" for slug, (week_dir, _) in PAGES.items()}

HEADING_RE = re.compile(r"^(#{1,2})\s+(.*)$")
WIKI_LINK_RE = re.compile(
    r"https?://(?:www\.)?msuperl\.org/wikis/pcubed/doku\.php\?id=183_notes:([a-zA-Z0-9_]+)(#[a-zA-Z0-9_]*)?"
)
OTHER_WIKI_LINK_RE = re.compile(
    r"https?://(?:www\.)?msuperl\.org/wikis/pcubed/doku\.php\?id=([a-zA-Z0-9_:]+)"
)
YOUTUBE_BLOCK_RE = re.compile(
    r"\[<img[^\n]*?/>\]\(https://www\.youtube\.com/watch\?v=([A-Za-z0-9_-]+)\)\n\n"
    r"Video:[^\n]*\[watch on YouTube\]\(https://www\.youtube\.com/watch\?v=\1\)\n?"
)
MATH_BLOCK_RE = re.compile(r"^``` math\n(.*?)\n```$", re.DOTALL | re.MULTILINE)
INLINE_MATH_RE = re.compile(r"\$`(.+?)`\$")


def convert_docx(slug: str, bundle_dir: Path):
    docx_path = DOCX_DIR / f"183_notes_{slug}.docx"
    bundle_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["pandoc", str(docx_path), "-t", "gfm", "--wrap=none",
         "-o", "index.md", "--extract-media=."],
        cwd=bundle_dir, check=True,
    )
    media_dir = bundle_dir / "media"
    if media_dir.exists() and not any(media_dir.iterdir()):
        media_dir.rmdir()


def split_title(text: str):
    lines = text.lstrip("\n").split("\n")
    idx = next((i for i, l in enumerate(lines) if HEADING_RE.match(l)), None)
    if idx is None:
        raise ValueError("no heading found")
    textbook_ref = " ".join(l.strip() for l in lines[:idx] if l.strip()) or None
    title = HEADING_RE.match(lines[idx]).group(2).strip()
    body = "\n".join(lines[idx + 1:]).lstrip("\n")
    return title, textbook_ref, body


def demote_headings(body: str) -> str:
    in_fence = False
    levels = []
    out_lines = []
    for line in body.split("\n"):
        if line.startswith("```"):
            in_fence = not in_fence
        elif not in_fence:
            m = re.match(r"^(#{1,6})\s", line)
            if m:
                levels.append(len(m.group(1)))
    if not levels:
        return body
    shift = min(levels) - 2
    if shift <= 0:
        return body
    in_fence = False
    for line in body.split("\n"):
        if line.startswith("```"):
            in_fence = not in_fence
            out_lines.append(line)
            continue
        if not in_fence:
            m = re.match(r"^(#{1,6})(\s.*)$", line)
            if m:
                new_level = max(2, len(m.group(1)) - shift)
                line = ("#" * new_level) + m.group(2)
        out_lines.append(line)
    return "\n".join(out_lines)


def convert_math(body: str) -> str:
    def block_sub(m):
        return f"$$\n{m.group(1)}\n$$"

    body = MATH_BLOCK_RE.sub(block_sub, body)

    out_lines = []
    for line in body.split("\n"):
        in_table_row = line.lstrip().startswith("|")

        def inline_sub(m, in_table_row=in_table_row):
            inner = m.group(1)
            if in_table_row:
                inner = inner.replace("|", "&#124;")
            return f"${inner}$"

        out_lines.append(INLINE_MATH_RE.sub(inline_sub, line))
    return "\n".join(out_lines)


def convert_youtube(body: str) -> str:
    return YOUTUBE_BLOCK_RE.sub(lambda m: f"{{{{< youtube {m.group(1)} >}}}}\n", body)


def rewrite_links(body: str) -> str:
    def wiki_sub(m):
        slug = m.group(1)
        anchor = m.group(2) or ""
        if slug in LINK_MAP:
            return LINK_MAP[slug] + anchor
        return m.group(0)

    body = WIKI_LINK_RE.sub(wiki_sub, body)

    def other_sub(m):
        full_id = m.group(1)
        if ":" in full_id and full_id.split(":", 1)[0] == "183_notes":
            leaf = full_id.split(":")[-1]
            if leaf in LINK_MAP:
                return LINK_MAP[leaf]
        return "https://www.msuperl.org/wikis/pcubed/doku.php?id=" + full_id

    body = OTHER_WIKI_LINK_RE.sub(other_sub, body)
    return body


def yaml_single_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def process_page(slug: str, week_dir: str, weight: int):
    bundle_dir = CONTENT_DIR / week_dir / slug
    convert_docx(slug, bundle_dir)
    raw = (bundle_dir / "index.md").read_text()
    title, textbook_ref, body = split_title(raw)
    title = convert_math(title)
    body = demote_headings(body)
    body = convert_math(body)
    body = convert_youtube(body)
    body = rewrite_links(body)

    fm_lines = ["---", f"title: {yaml_single_quote(title)}", f"weight: {weight}"]
    if textbook_ref:
        fm_lines.append(f"textbook_ref: {yaml_single_quote(textbook_ref)}")
    fm_lines.append("---\n")
    (bundle_dir / "index.md").write_text("\n".join(fm_lines) + "\n" + body)


def write_week_index(week_dir: str, title: str, weight: int):
    d = CONTENT_DIR / week_dir
    d.mkdir(parents=True, exist_ok=True)
    (d / "_index.md").write_text(
        "\n".join(["---", f'title: "{title}"', f"weight: {weight}", "---", ""])
    )


def write_notes_index():
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    (CONTENT_DIR / "_index.md").write_text(
        "\n".join(["---", 'title: "Notes"', "---", ""])
    )


def main():
    if CONTENT_DIR.exists():
        shutil.rmtree(CONTENT_DIR)
    write_notes_index()
    for week_dir, title, weight in WEEKS:
        write_week_index(week_dir, title, weight)
    alt_todo = []
    for slug, (week_dir, weight) in PAGES.items():
        process_page(slug, week_dir, weight)
        text = (CONTENT_DIR / week_dir / slug / "index.md").read_text()
        notes = []
        if "ALT TEXT NEEDED" in text:
            notes.append(f"{text.count('ALT TEXT NEEDED')} image(s) missing alt text")
        if "MANUAL REVIEW" in text:
            notes.append("embed/link flagged for manual review")
        if notes:
            alt_todo.append(f"{week_dir}/{slug}: " + "; ".join(notes))
        print(f"ok: {week_dir}/{slug}")
    (ROOT / "scripts" / "content-todo.txt").write_text("\n".join(alt_todo) + "\n")
    print(f"\n{len(alt_todo)} pages have pending content todos; see scripts/content-todo.txt")


if __name__ == "__main__":
    main()

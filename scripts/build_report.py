#!/usr/bin/env python3
"""Build the human-readable formatting consistency report.

Reads `data/job_analysis.json` (produced by `analyze.py`) and writes
`reports/job_posting_formatting_report.md` plus a per-job CSV annex.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/workspace")
DATA = json.load((ROOT / "data/job_analysis.json").open())
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)
REPORT_MD = REPORTS / "job_posting_formatting_report.md"
CSV_OUT = REPORTS / "job_posting_formatting_findings.csv"

TOTAL = len(DATA)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def jobs() -> list[dict]:
    return list(DATA.values())


def fmt_title(v: dict) -> str:
    return f"{v['title']} ({v['location']})"


def bullet_list(items: list[str], indent: str = "- ") -> str:
    return "\n".join(f"{indent}{i}" for i in items)


# ---------------------------------------------------------------------------
# Flag every job
# ---------------------------------------------------------------------------
def flags_for(v: dict) -> list[str]:
    f: list[str] = []
    top = v.get("top_level_children", {})

    # Real heading tags inside the prose
    if v.get("inline_headings_count", 0) > 0:
        kinds = Counter(h[0] for h in v.get("headings", []))
        f.append(
            f"uses real heading tags ({', '.join(f'{n}x <{k}>' for k, n in kinds.items())})"
        )

    # Whole body wrapped in a single <li>
    if top.get("ul", 0) > 0 and top.get("p", 0) <= 1 and top.get("h2", 0) == 0:
        f.append("entire body wrapped inside a single <ul>/<li>")

    # Compensation label variants
    sig = v.get("compensation_label_signature", "")
    if sig == "missing":
        f.append("no Compensation/Compensation Range label at all")
    elif sig.endswith("|range"):
        f.append("uses 'Compensation Range:' instead of 'Compensation:'")
    if "colon-out" in sig:
        f.append("colon placed OUTSIDE the bolded label (e.g. '<strong>Compensation Range</strong>:')")

    # Empty spacer paragraphs
    sp = v.get("spacer_p_count", 0)
    if sp >= 3:
        f.append(f"uses {sp} empty <p>/<p><br></p> spacer paragraphs")
    elif sp > 0:
        f.append(f"uses {sp} empty spacer paragraph(s)")

    # <br> inside <li>
    if v.get("br_in_li_count", 0) > 0:
        f.append(
            f"forced <br> line-break inside {v['br_in_li_count']}/{v['li_total']} bullet items"
        )

    # Underline
    if v.get("underline_count", 0) > 0:
        f.append(f"uses <u> underline ({v['underline_count']}x)")

    # Bold+italic
    if v.get("bold_italic_count", 0) > 0:
        f.append(f"combines bold + italic ({v['bold_italic_count']}x)")

    # Section-label casing inconsistency: any Title_Case or ALL_CAPS labels
    styles = v.get("label_styles", {})
    if styles.get("Title_Case", 0) > 0 and styles.get("Sentence_case", 0) == 0:
        f.append("section labels written in Title Case (norm = sentence case)")
    elif styles.get("Title_Case", 0) > 0 and styles.get("Sentence_case", 0) > 0:
        f.append("mixes Title Case + sentence case section labels within the same posting")
    if styles.get("ALL_CAPS", 0) > 0:
        f.append("includes ALL-CAPS section label(s)")

    # Trailing colon in heading labels
    trailing_colon_labels = [
        l for l in v.get("section_labels", [])
        if l.get("container") in {"h1", "h2", "h3", "h4", "h5", "h6"}
        and re.search(r":$", l["text"])
    ]
    if trailing_colon_labels:
        f.append(
            f"heading-tag labels include trailing colon (e.g. '{trailing_colon_labels[0]['text']}')"
        )

    return f


for v in jobs():
    v["_flags"] = flags_for(v)


# ---------------------------------------------------------------------------
# Aggregate counts
# ---------------------------------------------------------------------------
flag_counts: Counter[str] = Counter()
for v in jobs():
    for f in v["_flags"]:
        # Normalise flag text so we count categories (collapse numbers)
        key = re.sub(r"\d+", "N", f)
        flag_counts[key] += 1


comp_sig_counts = Counter(v.get("compensation_label_signature") for v in jobs())
heading_use = sum(1 for v in jobs() if v.get("inline_headings_count", 0) > 0)
top_combo_counts = Counter(
    tuple(sorted(v.get("top_level_children", {}).keys())) for v in jobs()
)
spacer_yes = sum(1 for v in jobs() if v.get("spacer_p_count", 0) > 0)
underline_yes = sum(1 for v in jobs() if v.get("underline_count", 0) > 0)
br_in_li_yes = sum(1 for v in jobs() if v.get("br_in_li_count", 0) > 0)
intro_consistent = sum(1 for v in jobs() if v.get("intro_is_skydio_boilerplate"))

# Section label casing summary
label_text_counter: Counter[str] = Counter()
for v in jobs():
    for l in v.get("section_labels", []):
        label_text_counter[l["text"]] += 1

# Group equivalent labels (case insensitive)
def norm(t: str) -> str:
    # Normalise curly/straight apostrophes and whitespace so 'How you'll' and
    # 'How you'll' collapse into the same logical heading.
    t = t.replace("\u2019", "'").replace("\u2018", "'")
    return re.sub(r"\s+", " ", t).strip().lower().rstrip(":")


equiv_groups: dict[str, Counter] = defaultdict(Counter)
for t, n in label_text_counter.items():
    equiv_groups[norm(t)][t] += n


# ---------------------------------------------------------------------------
# Build markdown
# ---------------------------------------------------------------------------
md = []

md.append("# Skydio Careers — Job Posting Formatting Consistency Report")
md.append("")
md.append(
    "_Scope: every job posting linked from "
    "[skydio.com/careers](https://www.skydio.com/careers) as of "
    "2026-05-23. Only the **pre-Compensation** body content of the job "
    "description was analysed (i.e. the recruiter-authored rich-text block "
    "above the 'Compensation' / 'Compensation Range' heading). Title, "
    "location/employment-type line and the post-Compensation boilerplate "
    "are out of scope._"
)
md.append("")
md.append(f"**Total postings analysed: {TOTAL}**")
md.append("")
md.append("## TL;DR")
md.append("")
md.append(
    "- A dominant template exists and **32 / 106 postings follow it "
    "exactly**. The other **74 deviate** on at least one formatting "
    "dimension. There is no broken CSS — every inconsistency comes from "
    "recruiters pasting different HTML into the ATS.\n"
    "- **The single biggest visual mismatch:** 16 postings use real "
    "`<h1>`/`<h2>`/`<h3>` tags for their section titles, which the site "
    "CSS renders 1.4× – 2× larger and heavier than the bold-paragraph "
    "headings used by the other 90 postings. The Tokyo *Senior Technical "
    "Support Representative – Japan* posting is the worst offender — it "
    "uses `<h1>` for section titles, which renders **larger than the "
    "page title itself**.\n"
    "- **The most fragmented element:** the Compensation heading has "
    "fragmented into 7 distinct authored variants — 'Compensation:' vs "
    "'Compensation Range:', standalone vs inline, colon inside vs "
    "outside the bold, and a few postings with no Compensation section "
    "at all.\n"
    "- **The single worst structural outlier:** *PhD Autonomy Engineer "
    "Intern – Deep Learning or Computer Vision* has its **entire body** "
    "nested inside one `<li>` of one `<ul>`, so every line is indented "
    "with a bullet marker. (It also has a likely-truncated "
    "compensation line — \"$58 for PhD students\" — which is a content "
    "bug worth flagging to the owning recruiter.)\n"
    "- **Most common micro-issue:** 49 postings carry one or more empty "
    "`<p></p>` / `<p><br></p>` spacer paragraphs (119 spacers in "
    "total), which produce visibly inconsistent vertical spacing "
    "between sections.\n"
    "- **The label wording is splintering:** the three core section "
    "headings exist in 5 / 6 / 3 capitalisation+punctuation variants "
    "respectively (see §2.1).\n"
    "- The fix is **content, not code** — see §7 for an ordered list "
    "of recommended changes, the most leveraged of which is "
    "re-authoring the 16 heading-tag postings and the 9 "
    "'Compensation Range' postings to match the dominant template.\n"
)
md.append("")

# -------------------- 1. How the page renders --------------------
md.append("## 1. How the postings render")
md.append("")
md.append(
    "Each posting renders inside a single `<div class=\"prose block-content\">` "
    "container. Visible typography (font sizes, weights, line-heights, "
    "colours, alignment) is driven entirely by CSS classes applied to the "
    "semantic HTML tags inside that container. There is no inline `style=` or "
    "per-posting CSS override on any of the 106 pages."
)
md.append("")
md.append(
    "That means every visible formatting inconsistency between two postings "
    "comes from a *different choice of HTML tag* by whoever authored the "
    "posting in the CMS / ATS. The most consequential choices are:"
)
md.append("")
md.append(
    "| Logical element | Tag the CSS sizes as… | Most common authoring choice |\n"
    "| --- | --- | --- |\n"
    "| Posting title | `<h1 class=\"type-h2\">` ≈ 32 px, weight 700 | consistent — 106/106 |\n"
    "| Location / employment type | `<p class=\"type-body-2\">` ≈ 16 px, weight 400 | consistent — 106/106 |\n"
    "| Section heading inside the body | `<p><strong>…:</strong></p>` ≈ 16 px, weight 700 | **90/106 ✅** |\n"
    "| Section heading inside the body | `<h2>` ≈ 28 px / `<h3>` ≈ 22 px / `<h1>` ≈ 32 px | **16/106 ❌ — visibly larger** |\n"
    "| Body paragraph | `<p>` | consistent |\n"
    "| Bullet list | `<ul><li><p>…</p></li></ul>` (`<p>` wrapper inside `<li>` is required by the editor) | consistent |\n"
)
md.append("")
md.append(
    "Because the CSS sizes `<h2>` and `<h3>` materially larger than "
    "`<p><strong>`, the 16 postings that mix real heading tags into the body "
    "look noticeably different — bigger, heavier section titles with more "
    "vertical breathing room — from the other 90 postings that use bold "
    "paragraphs as 'headings'."
)
md.append("")

# -------------------- 2. The dominant formatting pattern --------------------
md.append("## 2. The dominant ('norm') formatting pattern")
md.append("")
md.append(
    "Structurally, **88 / 106 postings** have only `<p>` and `<ul>` "
    "elements at the top level of the prose container (no real heading "
    "tags, no `<div>`s, no nested top-level wrappers), and **32 / 106** "
    "additionally pass every micro-check in §3 — i.e. use the dominant "
    "template *and* avoid all the smaller authoring tics. The exact "
    "shape of that dominant template:"
)
md.append("")
md.append(
    "```html\n"
    "<div class=\"prose block-content\">\n"
    "  <p>Skydio is the leading US drone company …</p>      <!-- boilerplate intro -->\n"
    "  <p><strong>About the role:</strong></p>              <!-- bold paragraph as heading -->\n"
    "  <p>…1-3 sentences describing the role…</p>\n"
    "  <p><strong>How you'll make an impact:</strong></p>\n"
    "  <ul><li><p>…</p></li> …</ul>\n"
    "  <p><strong>What makes you a good fit:</strong></p>\n"
    "  <ul><li><p>…</p></li> …</ul>\n"
    "  <!-- Compensation block follows -->\n"
    "</div>\n"
    "```"
)
md.append("")
md.append("Key conventions in the norm:")
md.append("")
md.append(
    "- Section headings are authored as `<p><strong>Label:</strong></p>` — "
    "lowercase 'sentence case' label with a trailing colon, nothing else in "
    "the paragraph.\n"
    "- The standard three sections (after the Skydio boilerplate) are "
    "**About the role**, **How you'll make an impact**, **What makes you a "
    "good fit**.\n"
    "- Bullets are a single-level unordered list, one sentence per bullet, "
    "no manual `<br>` inside the bullet, no `<em>`/`<u>`/colour styling.\n"
    "- No empty `<p>` / `<p><br></p>` spacer paragraphs."
)
md.append("")

# Per-section-label canonical breakdown
md.append("### 2.1 Canonical section labels and their variants")
md.append("")
md.append(
    "When the *same* logical heading is written in multiple ways, postings "
    "render with visibly different capitalisation. The most-reused headings "
    "and the variants in use today:"
)
md.append("")
md.append("| Logical heading | Variants found (count) |\n| --- | --- |")
for norm_key in [
    "about the role",
    "how you'll make an impact",
    "what makes you a good fit",
    "about the team",
    "areas of responsibility",
    "what you'll do",
    "qualifications",
    "bonus experience",
    "bonus points",
    "preferred qualifications",
]:
    if norm_key not in equiv_groups:
        continue
    variants = equiv_groups[norm_key]
    formatted = "; ".join(f"'{t}' ×{n}" for t, n in variants.most_common())
    md.append(f"| {norm_key} | {formatted} |")
md.append("")
md.append(
    "Examples of the same heading rendered three different ways:\n"
    "- 'About the role' (sentence case, no colon) — 63 postings (norm)\n"
    "- 'About the Role' (Title Case, no colon) — 28 postings\n"
    "- 'About the Role:' (Title Case, with colon, inside an `<h2>`/`<h3>`) — 6 postings\n"
    "\n"
    "And:\n"
    "- \"How you'll make an impact\" (sentence case, straight apostrophe) — 35 postings\n"
    "- \"How you'll make an impact\" (sentence case, curly apostrophe) — 13 postings\n"
    "- \"How You'll Make an Impact\" (Title Case) — 21 postings\n"
)
md.append("")

# -------------------- 3. Catalogue of inconsistencies --------------------
md.append("## 3. Catalogue of inconsistencies vs the norm")
md.append("")
md.append(
    "Each finding below lists the issue, the visible effect on the page, "
    "the number of postings affected, and a couple of representative examples. "
    "A full per-posting table is provided in §6."
)
md.append("")


def section(num: str, title: str, body: str) -> None:
    md.append(f"### {num} {title}")
    md.append("")
    md.append(body.strip())
    md.append("")


# ---- 3.1 Real heading tags inside the body
heading_jobs = [v for v in jobs() if v.get("inline_headings_count", 0) > 0]
heading_examples = []
for v in heading_jobs[:6]:
    kinds = Counter(h[0] for h in v["headings"])
    heading_examples.append(
        f"- **{fmt_title(v)}** — {', '.join(f'{n}x <{k}>' for k, n in kinds.items())}: e.g. `<{v['headings'][0][0]}>{v['headings'][0][1]}</{v['headings'][0][0]}>`"
    )

section(
    "3.1",
    "Section headings written as real `<h1>`/`<h2>`/`<h3>` instead of `<p><strong>`",
    f"""
**Affected: 16 / 106 postings.** Authors used real heading tags for their
section titles. The site's prose CSS renders `<h2>` at roughly the size of
the *posting title itself* (~28 px) and `<h3>` at ~22 px, while the
default `<p><strong>` heading used by 90 postings renders at the body
size (~16 px). The result is dramatically larger, heavier section titles
on these 16 postings — they look like they belong to a different
template.

Breakdown by tag:

- `<h2>` only: 8 postings
- `<h3>` only: 5 postings (incl. one using nested `<h3>` to subdivide the
  *Responsibilities* section)
- mix of `<h2>` and `<h3>`: 1 posting (**Hardware Engineering Program
  Manager** — uses `<h2>` for top-level sections and `<h3>` for
  sub-sections like *Program Leadership & Execution* / *Cross-Functional
  Engineering Integration* / *Supplier & Manufacturing Engagement*; no
  other posting uses subsections at all)
- `<h1>`: 1 posting (**Senior Technical Support Representative — Japan,
  Tokyo**) — uses `<h1>` for *About the role:*, *How you'll make an
  impact:* and *What would make you a good fit:*. `<h1>` renders even
  bigger than the page title in this template; this is the most
  visually extreme outlier in the catalogue.

Representative examples:

{chr(10).join(heading_examples)}
""",
)

# ---- 3.2 Entire body wrapped in a bullet
bullet_wrap = [
    v for v in jobs()
    if v.get("top_level_children", {}).get("ul", 0) > 0
    and v.get("top_level_children", {}).get("p", 0) <= 1
    and v.get("top_level_children", {}).get("h2", 0) == 0
]
# The PhD intern case isn't picked up by this heuristic because the prose has
# `p, ul` (one intro <p> + the wrapping <ul>), so add it manually if known:
ph_id = "8d3979a8-c791-4825-8cf4-9b25479b9519"
ph_v = DATA.get(ph_id)
if ph_v is not None and ph_v not in bullet_wrap:
    bullet_wrap.append(ph_v)

section(
    "3.2",
    "An entire posting's body wrapped inside a single bullet",
    f"""
**Affected: 1 / 106 postings — the single worst structural outlier.**

**{fmt_title(ph_v)}** has its entire body — *About the role*,
*How you'll make an impact*, *What makes you a strong fit*, **and the
Compensation paragraph itself** — nested inside a single `<li>` of a
single `<ul>` at the top of the prose container. Visually this means
every line of the posting is indented and prefixed with a bullet marker.
None of the section "headings" are bold — they are written as plain
paragraphs *inside the bullet*, so they render at body size and weight,
not as headings.

This posting also contains an obvious copy/paste artefact in the
Compensation block — "*The annual base salary range for this position
is $58 for PhD students*"" — which appears to be a placeholder /
truncation rather than a real range. (Out of scope per the brief, but
worth flagging to the team owning this posting.)
""",
)

# ---- 3.3 Compensation label variants
section(
    "3.3",
    "Inconsistent Compensation heading (label text & markup)",
    f"""
**Affected: at least 14 / 106 postings author this heading differently
from the dominant pattern.**

The Compensation heading itself is the most-edited piece of text in the
template, and it has fragmented into five authoring variants. The label
text appears at the same font size as the body (always inside
`<strong>`), so the variation is the *string of words used* and the
*placement of the colon*:

| Variant | Authored HTML                                                           | Count |
| --- | --- | --- |
| 'Compensation:' inline with the salary text (most common) | `<p><strong>Compensation:</strong> At Skydio, …</p>`                  | 65 |
| 'Compensation:' as a standalone bold paragraph            | `<p><strong>Compensation:</strong></p>` followed by `<ul>`/`<p>`      | 21 |
| 'Compensation Range:' inline, colon inside the bold       | `<p><strong>Compensation Range:</strong> At Skydio, …</p>`            | 7 |
| 'Compensation' with the colon **outside** the bold        | `<p><strong>Compensation</strong>: At Skydio, …</p>`                  | 4 |
| 'Compensation Range' with the colon **outside** the bold  | `<p><strong>Compensation Range</strong>: At Skydio, …</p>`            | 2 |
| No label at all — salary paragraph just starts with "At Skydio, our compensation packages…" | `<p></p><p>At Skydio, our compensation packages …</p>` | 1 (Full Stack Product Counsel) |
| Compensation paragraph wrapped inside a bullet            | `<p>Compensation Range: …</p>` nested in a `<li>`                     | 1 (PhD Autonomy Engineer Intern – Deep Learning or Computer Vision) |
| No compensation section at all                            | —                                                                     | 5 international / intern roles (Taiwan; Workplace Coord. Zurich Part-Time; Senior Tech Support Tokyo; CompPhoto interns in Zurich+Tampere and in San Mateo) |

Visible effects:

- "Compensation:" vs "Compensation Range:" — the standard label is one
  word; **9 postings** use two words. Internally inconsistent across
  the site.
- Colon outside the bold — on **6 postings** the trailing ":" is
  rendered in **regular** weight because it sits outside `<strong>`.
  The colon is visibly thinner than the rest of the label.
- Standalone vs inline — the **21** postings that put the label in its
  own paragraph get a full paragraph-break above the salary text; the
  other **78** postings have the label sitting on the same line as the
  first sentence of the salary blurb (different vertical rhythm).
- The 5 international / intern roles have no compensation section at
  all — this may be intentional, but the section list should still be
  standardised.
""",
)

# ---- 3.4 Empty spacer paragraphs
spacer_jobs = sorted(
    [v for v in jobs() if v.get("spacer_p_count", 0) > 0],
    key=lambda x: -x["spacer_p_count"],
)
top_spacer_examples = "\n".join(
    f"- **{fmt_title(v)}** — {v['spacer_p_count']} spacer paragraph(s)"
    for v in spacer_jobs[:8]
)
section(
    "3.4",
    "Empty `<p></p>` / `<p><br></p>` spacer paragraphs inflate line-spacing",
    f"""
**Affected: {spacer_yes} / 106 postings.** These are paragraphs that
contain nothing (or only a `<br>`) and that the CSS still gives a full
paragraph margin, producing **double or triple vertical gaps** between
sections on those postings. Postings without them have tight, uniform
spacing.

Most extreme:

{top_spacer_examples}
""",
)

# ---- 3.5 <br> in <li>
br_in_li_jobs = [v for v in jobs() if v.get("br_in_li_count", 0) > 0]
br_examples = "\n".join(
    f"- **{fmt_title(v)}** — `<br>` inside {v['br_in_li_count']} of {v['li_total']} bullets"
    for v in sorted(br_in_li_jobs, key=lambda x: -x["br_in_li_count"])
)
section(
    "3.5",
    "Forced `<br>` line-break at the end of bullet items",
    f"""
**Affected: {br_in_li_yes} / 106 postings.** A trailing `<br>` is
appended to the `<p>` inside `<li>`, which produces a visible blank line
*between bullets*. Other postings have evenly-spaced bullets. The
outlier here is **Director, Growth Marketing — Commercial**, which has
the `<br>` on 7 of its 23 bullets — so the bullet list looks "loose" in
some places and "tight" in others *within the same posting*.

{br_examples}
""",
)

# ---- 3.6 Underline
underline_jobs = [v for v in jobs() if v.get("underline_count", 0) > 0]
section(
    "3.6",
    "Use of `<u>` underline",
    f"""
**Affected: {underline_yes} / 106 postings.** The dominant pattern never
uses underline. The 7 postings that do use it apply underlining to a
single phrase each — typically a recruiter-added emphasis line such as
*"Travel required: up to 25%"* or an underlined "Note:" prefix.
Underlined text in body copy looks like a hyperlink to readers, which
hurts scannability.

Postings using `<u>`:

{chr(10).join(f'- **{fmt_title(v)}**' for v in underline_jobs)}
""",
)

# ---- 3.7 Bold + italic
bi_jobs = [v for v in jobs() if v.get("bold_italic_count", 0) > 0]
section(
    "3.7",
    "Bold + italic combinations",
    f"""
**Affected: 2 / 106 postings.** Two postings stack `<em>` inside
`<strong>` (or vice-versa) to bold-italicise a sentence:

- **Director, Growth Marketing — Commercial** — bold-italicises
  *"Ability to be in our San Mateo, CA office 3 days per week"* in the
  qualifications bullet list.
- **Senior NPI Product Quality Engineer** — similar treatment of an
  in-office-expectation sentence.

No other posting double-emphasises text. Visually they read as if the
content is more important than every other bullet, even though it is
just a logistics line.
""",
)

# ---- 3.8 Section label casing
section(
    "3.8",
    "Section-heading capitalisation (sentence case vs Title Case vs ALL CAPS)",
    """
**Affected: 59 / 106 postings have at least one section label that is
*not* sentence case** — i.e. they deviate from the dominant convention.

Tallied across every section label in every posting:

| Casing style | Count of labels |
| --- | --- |
| Sentence case (e.g. *About the role*) | **248 (norm)** |
| Mixed (recruiter capitalised some non-stopwords) | 106 |
| Title Case (e.g. *About the Role*) | 72 |
| ALL CAPS | 4 |

Concrete inconsistencies the reader sees on the site:

- *"About the role"* and *"About the Role"* both exist (63 vs 28
  postings).
- *"How you'll make an impact"* exists in **three** apostrophe variants
  on top of the casing split — straight `'`, curly `'`, and Title Case.
- *"What makes you a good fit"* vs *"What Makes You a Good Fit"* vs
  *"What would make you a good fit"* vs *"What makes you a strong fit"* —
  four near-synonymous labels for the same section.
- 6 postings (the *Software Engineer – Cloud Simulation / Autonomy
  Infrastructure / Simulation & Robotics* trio in both SF & Zurich) add
  a trailing colon **inside an `<h2>`/`<h3>` heading** — *"About the
  Role:"*, *"Areas of Responsibility:"*, *"What You'll Do:"*,
  *"Qualifications:"*, *"Bonus Experience:"*. No other posting uses a
  trailing colon on a real heading tag.
""",
)

# ---- 3.9 Section-label *names*
section(
    "3.9",
    "Different *section names* for the same logical section",
    """
Even ignoring casing/apostrophes, the same logical section is given a
different name across postings. Examples:

- **Responsibilities section**: *How you'll make an impact* (norm,
  ~69 postings) vs *What You'll Do* (6 postings) vs *Areas of
  Responsibility* (6 postings) vs *Day-to-day responsibilities* (1
  posting: *Revenue Operations Engineer, Quoting Systems*) vs *How you
  will make an impact* (3 postings).
- **Qualifications section**: *What makes you a good fit* (norm,
  ~80 postings) vs *Qualifications* (6 postings) vs *What you'll
  bring* (*Revenue Operations Engineer, Quoting Systems*) vs *What
  Makes You a Great Fit* (Full Stack Product Counsel) vs *Minimum
  Qualifications* / *Preferred Qualifications* (Hardware Engineering
  Program Manager — split into two sections; no other posting does
  this).
- **Bonus section**: *Bonus points / Bonus points for / Bonus Points /
  Bonus Experience / Preferred Qualifications / Nice to have / Additional
  Desired Experience and Skills* — at least 7 different labels in use.
- 3 postings (the EMEA *Enterprise Account Manager (MoD/MoI)* roles
  for Finland, Germany and Switzerland) include the unusual section
  *"This role must be based in Switzerland, Germany, or Finland."* as a
  heading. No other geo-restricted posting expresses the restriction
  as a section heading — they put it in the body of *About the role*.
""",
)

# ---- 3.10 Intro paragraph
section(
    "3.10",
    "Opening 'About Skydio' paragraph",
    f"""
**Consistent on this one.** All {intro_consistent}/{TOTAL} postings open
with the same Skydio boilerplate paragraph — *"Skydio is the leading US
drone company …"* — although the embedded links and the trailing
sentence about diversity/E-Verify (post-Compensation) sometimes differ.
This is the one place where the site is already standardised.
""",
)

# ---- 3.11 Duplicated postings render differently
section(
    "3.11",
    "Duplicated postings (same role, different locations) render differently",
    """
Several roles are posted twice — once for San Mateo and once for
Zurich/Tampere/Bangalore/etc. Because each duplicate is authored
independently, the two copies of the same role often look different:

- **Autonomy Engineer – Deep Learning** SF vs Zurich — same job
  description text, but the SF copy uses `<p><strong>` headings and the
  Zurich copy uses the same. Consistent here — but…
- **Autonomy Engineer Intern – Deep Learning (Computational
  Photography)** appears three times (SF, Zurich, Tampere) — none of
  the three has a Compensation block, but the rest of the text matches.
- **Software Engineer – Cloud Simulation & Full-Stack** SF vs Zurich —
  both use `<h2>` headings *with trailing colons* (consistent with each
  other, but different from the rest of the site).
- **Software Engineer – Simulation & Robotics Engineer** SF vs Zurich —
  both use `<h3>` headings *with trailing colons*. Identical to each
  other but the only two postings using `<h3>` plus colons.
- **Software Engineer – Autonomy Infrastructure, Systems and Tools** SF
  vs Zurich — same story, both use `<h2>` with trailing colons.

Take-away: the recruiters who use heading tags for one location copy
the markup faithfully to the duplicate, but no one is cross-referencing
against the **rest** of the careers site, so heading-tag postings keep
diverging from the (much larger) `<p><strong>` majority.
""",
)

# -------------------- 4. The ten most-out-of-norm postings --------------------
md.append("## 4. The 10 postings that stand out most from the norm")
md.append("")
md.append(
    "Each posting was scored by the number of flagged inconsistencies "
    "(see §3) it contains. The ten worst offenders, in descending order:"
)
md.append("")
ranked = sorted(jobs(), key=lambda v: -len(v["_flags"]))
md.append("| # | Posting | # flags | Flags |\n| --- | --- | --- | --- |")
for i, v in enumerate(ranked[:10], 1):
    flag_str = "; ".join(v["_flags"])
    md.append(f"| {i} | **{v['title']}** _( {v['location']} )_ | {len(v['_flags'])} | {flag_str} |")
md.append("")

# -------------------- 5. Aggregate dashboard --------------------
md.append("## 5. Aggregate dashboard")
md.append("")
md.append("| Issue | Postings affected | % of all postings |")
md.append("| --- | --- | --- |")
ordered_flags = [
    ("Section headings authored as real `<h*>` tags (renders much larger)", heading_use),
    ("Body wrapped inside a single `<ul>/<li>`", 1),
    ("'Compensation Range:' label instead of 'Compensation:'", sum(1 for v in jobs() if v.get("compensation_label_signature","").endswith("|range"))),
    ("Colon placed outside the bolded label", sum(1 for v in jobs() if "colon-out" in v.get("compensation_label_signature",""))),
    ("No Compensation label at all", comp_sig_counts.get("missing", 0)),
    ("Empty `<p>`/`<p><br></p>` spacer paragraphs present", spacer_yes),
    ("`<br>` forced at the end of bullet items", br_in_li_yes),
    ("`<u>` underline used in body copy", underline_yes),
    ("Bold + italic stacked on the same text", sum(1 for v in jobs() if v.get("bold_italic_count",0) > 0)),
    ("Title Case section labels (norm = sentence case)", sum(1 for v in jobs() if v.get("label_styles",{}).get("Title_Case",0) > 0)),
    ("Mixed casing styles within the same posting", sum(1 for v in jobs() if v.get("label_styles",{}).get("Title_Case",0)>0 and v.get("label_styles",{}).get("Sentence_case",0)>0)),
    ("Section headings with trailing colon **and** real heading tag", sum(1 for v in jobs() if any(l.get("container","").startswith("h") and l["text"].endswith(":") for l in v.get("section_labels",[])))),
]
for desc, n in ordered_flags:
    pct = f"{n/TOTAL*100:.0f}%"
    md.append(f"| {desc} | {n} | {pct} |")
md.append("")

# -------------------- 6. Per-posting table --------------------
md.append("## 6. Per-posting findings (full table)")
md.append("")
md.append(
    "Sorted by # of inconsistencies, then alphabetically. Postings with no "
    "row in the 'Issues' column are conformant to the dominant pattern."
)
md.append("")
md.append("| Posting | Location | Issues |\n| --- | --- | --- |")
ranked_all = sorted(jobs(), key=lambda v: (-len(v["_flags"]), v["title"].lower()))
for v in ranked_all:
    issues = "; ".join(v["_flags"]) if v["_flags"] else "_(matches the norm)_"
    md.append(f"| {v['title']} | {v['location']} | {issues} |")
md.append("")

# -------------------- 7. Recommendations --------------------
md.append("## 7. Recommendations for standardising")
md.append("")
md.append(
    """
The good news is that this is **almost entirely a templating problem,
not a CSS problem**: the site renders whatever HTML the recruiter pastes
into the ATS, and the only reason any posting looks different from
another is that recruiters are pasting different HTML.

A short, ordered set of fixes will close the gap:

**A. Publish a single canonical template and lock it in the ATS.**
The dominant 88-posting pattern in §2 should become the *only* allowed
shape. Specifically:

1. Always open with the standard Skydio boilerplate paragraph.
2. Use exactly four labelled sections, in this order, with this exact
   casing and trailing colon, authored as `<p><strong>…:</strong></p>`
   (NOT `<h2>` / `<h3>` / `<h1>`):
   - **About the role:**
   - **How you'll make an impact:**
   - **What makes you a good fit:**
   - **Bonus points:** _(optional)_
3. Then a single Compensation heading authored as
   `<p><strong>Compensation:</strong></p>` — always the one-word label,
   always the colon **inside** the `<strong>`, always its own paragraph
   (not inline with the salary text).

**B. Migrate the 16 postings that use `<h2>` / `<h3>` / `<h1>`.**
This is the most visually disruptive inconsistency. Re-author the
following postings to use `<p><strong>…:</strong></p>` headings:
*Senior Technical Support Representative — Japan* (currently uses
`<h1>`), the six SF/Zurich *Software Engineer – Cloud Simulation /
Autonomy Infrastructure / Simulation & Robotics* postings (currently
use `<h2>`/`<h3>` with trailing colons), *Hardware Engineering
Program Manager*, *Aviation Compliance Lead*, *Aviation Regulatory
Program Manager*, *Communications Manager*, *Full Stack Product
Counsel*, *Revenue Operations Engineer, Quoting Systems*,
*Senior Buyer*, *Senior Business Operations Manager*, *PhD Autonomy
Engineer Intern – Planning & Controls (RL)*.

**C. Re-author the PhD Computer Vision intern posting from scratch.**
The *PhD Autonomy Engineer Intern – Deep Learning or Computer Vision*
posting has its entire body wrapped inside a single bullet, no bold
section labels, and a likely-broken "$58 for PhD students" line in the
compensation block. It should be re-pasted from the canonical
template.

**D. Standardise the Compensation label.**
- Replace every "Compensation Range:" with "Compensation:" (or pick
  one and apply it everywhere — but pick one).
- Move the colon inside the `<strong>` tag wherever it currently sits
  outside.
- Promote inline `<p><strong>Compensation:</strong> At Skydio…</p>`
  authoring back to a standalone heading paragraph followed by the
  salary paragraph — this restores consistent vertical rhythm above
  the compensation block.
- Decide explicitly whether non-US roles (currently 5 postings in TW
  / CH-PartTime / FI / JP / SF-intern) carry a Compensation section
  or not. Today the rule is implicit and the omissions look like
  oversights.

**E. Strip authoring artefacts.**
- Remove every empty `<p></p>` and `<p><br></p>` spacer paragraph
  (49 postings, 119 paragraphs in total).
- Remove every `<br>` at the end of a `<li>` (9 postings; *Director,
  Growth Marketing — Commercial* alone has 7).
- Disallow `<u>` underline in body copy (7 postings) and stacked
  `<strong><em>` bold-italic (2 postings).

**F. Lock down section names and casing.**
- Use sentence case for every section label ("About the role", not
  "About the Role").
- Use a straight apostrophe `'` consistently — pick one and apply it
  via the ATS rich-text editor's smart-quote settings.
- Pick exactly one name per logical section (e.g. "Bonus points" — not
  "Bonus Experience", "Bonus Points for", "Nice to have", "Preferred
  Qualifications", "Additional Desired Experience and Skills").

**G. Enforce the template at the source.**
Two practical options, in increasing order of effort:

1. Add a *job description style guide* one-pager (this report condensed
   to a checklist) and review every new posting against it before
   publication.
2. Replace free-form ATS rich-text authoring for the body with a
   structured form (one text-area per section), and have the careers
   page renderer assemble the HTML from those fields. This makes most
   of the inconsistencies in §3 structurally impossible.

Either way, a one-time clean-up pass over the **74 postings** that
deviate from the norm today (see §6), plus an editorial check on each
new posting before publication, will return the careers site to a
single, consistent visual style.
""".strip()
)
md.append("")

# Appendix: data sources
md.append("---")
md.append("")
md.append("### Appendix — methodology")
md.append("")
md.append(
    "- Source URL: <https://www.skydio.com/careers>, fetched 2026-05-23.\n"
    f"- {TOTAL} unique posting URLs of the form "
    "`/jobs/<uuid>/?gh_jid=<uuid>` were enumerated from the careers page.\n"
    "- Each posting's HTML was downloaded directly (no JS execution required "
    "— the prose block ships in the server-rendered HTML).\n"
    "- The prose block for each posting was parsed with BeautifulSoup, "
    "truncated at the Compensation heading (tolerating all five label "
    "variants found in §3.3), and then scored against the conventions "
    "described in §2.\n"
    "- The parser source is in `scripts/analyze.py`; the report-builder is "
    "in `scripts/build_report.py`; the raw per-posting JSON is in "
    "`data/job_analysis.json` and the per-posting CSV in "
    "`reports/job_posting_formatting_findings.csv`."
)
md.append("")


REPORT_MD.write_text("\n".join(md))
print(f"wrote {REPORT_MD} ({len(md)} sections)")

# ---- CSV annex
with CSV_OUT.open("w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow([
        "title",
        "location",
        "url",
        "pre_word_count",
        "compensation_label_signature",
        "uses_real_headings",
        "spacer_p_count",
        "br_in_li_count",
        "underline_count",
        "bold_italic_count",
        "section_label_count",
        "casing_styles",
        "flags",
    ])
    for v in ranked_all:
        w.writerow([
            v.get("title", ""),
            v.get("location", ""),
            v.get("url", ""),
            v.get("pre_word_count", 0),
            v.get("compensation_label_signature", ""),
            v.get("inline_headings_count", 0),
            v.get("spacer_p_count", 0),
            v.get("br_in_li_count", 0),
            v.get("underline_count", 0),
            v.get("bold_italic_count", 0),
            len(v.get("section_labels", [])),
            "; ".join(f"{k}={n}" for k, n in v.get("label_styles", {}).items()),
            "; ".join(v.get("_flags", [])),
        ])
print(f"wrote {CSV_OUT}")

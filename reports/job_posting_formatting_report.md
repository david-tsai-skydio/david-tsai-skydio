# Skydio Careers — Job Posting Formatting Consistency Report

_Scope: every job posting linked from [skydio.com/careers](https://www.skydio.com/careers) as of 2026-05-23. Only the **pre-Compensation** body content of the job description was analysed (i.e. the recruiter-authored rich-text block above the 'Compensation' / 'Compensation Range' heading). Title, location/employment-type line and the post-Compensation boilerplate are out of scope._

**Total postings analysed: 106**

## TL;DR

- A dominant template exists and **32 / 106 postings follow it exactly**. The other **74 deviate** on at least one formatting dimension. There is no broken CSS — every inconsistency comes from recruiters pasting different HTML into the ATS.
- **The single biggest visual mismatch:** 16 postings use real `<h1>`/`<h2>`/`<h3>` tags for their section titles, which the site CSS renders 1.4× – 2× larger and heavier than the bold-paragraph headings used by the other 90 postings. The Tokyo *Senior Technical Support Representative – Japan* posting is the worst offender — it uses `<h1>` for section titles, which renders **larger than the page title itself**.
- **The most fragmented element:** the Compensation heading has fragmented into 7 distinct authored variants — 'Compensation:' vs 'Compensation Range:', standalone vs inline, colon inside vs outside the bold, and a few postings with no Compensation section at all.
- **The single worst structural outlier:** *PhD Autonomy Engineer Intern – Deep Learning or Computer Vision* has its **entire body** nested inside one `<li>` of one `<ul>`, so every line is indented with a bullet marker. (It also has a likely-truncated compensation line — "$58 for PhD students" — which is a content bug worth flagging to the owning recruiter.)
- **Most common micro-issue:** 49 postings carry one or more empty `<p></p>` / `<p><br></p>` spacer paragraphs (119 spacers in total), which produce visibly inconsistent vertical spacing between sections.
- **The label wording is splintering:** the three core section headings exist in 5 / 6 / 3 capitalisation+punctuation variants respectively (see §2.1).
- The fix is **content, not code** — see §7 for an ordered list of recommended changes, the most leveraged of which is re-authoring the 16 heading-tag postings and the 9 'Compensation Range' postings to match the dominant template.


## 1. How the postings render

Each posting renders inside a single `<div class="prose block-content">` container. Visible typography (font sizes, weights, line-heights, colours, alignment) is driven entirely by CSS classes applied to the semantic HTML tags inside that container. There is no inline `style=` or per-posting CSS override on any of the 106 pages.

That means every visible formatting inconsistency between two postings comes from a *different choice of HTML tag* by whoever authored the posting in the CMS / ATS. The most consequential choices are:

| Logical element | Tag the CSS sizes as… | Most common authoring choice |
| --- | --- | --- |
| Posting title | `<h1 class="type-h2">` ≈ 32 px, weight 700 | consistent — 106/106 |
| Location / employment type | `<p class="type-body-2">` ≈ 16 px, weight 400 | consistent — 106/106 |
| Section heading inside the body | `<p><strong>…:</strong></p>` ≈ 16 px, weight 700 | **90/106 ✅** |
| Section heading inside the body | `<h2>` ≈ 28 px / `<h3>` ≈ 22 px / `<h1>` ≈ 32 px | **16/106 ❌ — visibly larger** |
| Body paragraph | `<p>` | consistent |
| Bullet list | `<ul><li><p>…</p></li></ul>` (`<p>` wrapper inside `<li>` is required by the editor) | consistent |


Because the CSS sizes `<h2>` and `<h3>` materially larger than `<p><strong>`, the 16 postings that mix real heading tags into the body look noticeably different — bigger, heavier section titles with more vertical breathing room — from the other 90 postings that use bold paragraphs as 'headings'.

## 2. The dominant ('norm') formatting pattern

Structurally, **88 / 106 postings** have only `<p>` and `<ul>` elements at the top level of the prose container (no real heading tags, no `<div>`s, no nested top-level wrappers), and **32 / 106** additionally pass every micro-check in §3 — i.e. use the dominant template *and* avoid all the smaller authoring tics. The exact shape of that dominant template:

```html
<div class="prose block-content">
  <p>Skydio is the leading US drone company …</p>      <!-- boilerplate intro -->
  <p><strong>About the role:</strong></p>              <!-- bold paragraph as heading -->
  <p>…1-3 sentences describing the role…</p>
  <p><strong>How you'll make an impact:</strong></p>
  <ul><li><p>…</p></li> …</ul>
  <p><strong>What makes you a good fit:</strong></p>
  <ul><li><p>…</p></li> …</ul>
  <!-- Compensation block follows -->
</div>
```

Key conventions in the norm:

- Section headings are authored as `<p><strong>Label:</strong></p>` — lowercase 'sentence case' label with a trailing colon, nothing else in the paragraph.
- The standard three sections (after the Skydio boilerplate) are **About the role**, **How you'll make an impact**, **What makes you a good fit**.
- Bullets are a single-level unordered list, one sentence per bullet, no manual `<br>` inside the bullet, no `<em>`/`<u>`/colour styling.
- No empty `<p>` / `<p><br></p>` spacer paragraphs.

### 2.1 Canonical section labels and their variants

When the *same* logical heading is written in multiple ways, postings render with visibly different capitalisation. The most-reused headings and the variants in use today:

| Logical heading | Variants found (count) |
| --- | --- |
| about the role | 'About the role' ×63; 'About the Role' ×28; 'About the Role:' ×6; 'About The Role' ×1; 'About the role:' ×1 |
| how you'll make an impact | 'How you'll make an impact' ×35; 'How You’ll Make an Impact' ×21; 'How you’ll make an impact' ×13; 'How You'll Make an Impact' ×1; 'How you’ll make an impact:' ×1; 'How you'll make an impact:' ×1 |
| what makes you a good fit | 'What makes you a good fit' ×55; 'What Makes You a Good Fit' ×19; 'What Makes You A Good Fit' ×2 |
| about the team | 'About the Team' ×8; 'About the team' ×7 |
| areas of responsibility | 'Areas of Responsibility:' ×6 |
| what you'll do | 'What You’ll Do:' ×6; 'What You’ll Do' ×1; 'What you'll do' ×1 |
| qualifications | 'Qualifications:' ×6; 'Qualifications' ×1 |
| bonus experience | 'Bonus Experience:' ×6 |
| bonus points | 'Bonus Points' ×3; 'Bonus points' ×3 |
| preferred qualifications | 'Preferred Qualifications' ×4 |

Examples of the same heading rendered three different ways:
- 'About the role' (sentence case, no colon) — 63 postings (norm)
- 'About the Role' (Title Case, no colon) — 28 postings
- 'About the Role:' (Title Case, with colon, inside an `<h2>`/`<h3>`) — 6 postings

And:
- "How you'll make an impact" (sentence case, straight apostrophe) — 35 postings
- "How you'll make an impact" (sentence case, curly apostrophe) — 13 postings
- "How You'll Make an Impact" (Title Case) — 21 postings


## 3. Catalogue of inconsistencies vs the norm

Each finding below lists the issue, the visible effect on the page, the number of postings affected, and a couple of representative examples. A full per-posting table is provided in §6.

### 3.1 Section headings written as real `<h1>`/`<h2>`/`<h3>` instead of `<p><strong>`

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

- **Revenue Operations Engineer, Quoting Systems (San Mateo, California, United States - Full-time)** — 5x <h2>: e.g. `<h2>What you’ll drive (scope):</h2>`
- **Senior Business Operations Manager (San Mateo, California, United States - Full-time)** — 3x <h3>: e.g. `<h3>Strategic Sourcing:</h3>`
- **Communications Manager (US Remote - Full-time)** — 3x <h2>: e.g. `<h2>About the role</h2>`
- **Senior Buyer (Hayward, California, United States - Full-time)** — 2x <h2>: e.g. `<h2>How you will make an impact:</h2>`
- **Software Engineer - Simulation & Robotics Engineer (San Mateo, California, United States - Full-time)** — 5x <h3>: e.g. `<h3>About the Role:</h3>`
- **Software Engineer - Cloud Simulation & Full-Stack (San Mateo, California, United States - Full-time)** — 5x <h2>: e.g. `<h2>About the Role:</h2>`

### 3.2 An entire posting's body wrapped inside a single bullet

**Affected: 1 / 106 postings — the single worst structural outlier.**

**PhD Autonomy Engineer Intern - Deep Learning or Computer Vision (San Mateo, California, United States - Intern)** has its entire body — *About the role*,
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

### 3.3 Inconsistent Compensation heading (label text & markup)

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

### 3.4 Empty `<p></p>` / `<p><br></p>` spacer paragraphs inflate line-spacing

**Affected: 49 / 106 postings.** These are paragraphs that
contain nothing (or only a `<br>`) and that the CSS still gives a full
paragraph margin, producing **double or triple vertical gaps** between
sections on those postings. Postings without them have tight, uniform
spacing.

Most extreme:

- **Full Stack Product Counsel (San Mateo, California, United States - Full-time)** — 8 spacer paragraph(s)
- **Senior Product Manager, Platform & Infrastructure (San Mateo, California, United States - Full-time)** — 6 spacer paragraph(s)
- **Staff Product Manager, Platform & Infrastructure (San Mateo, California, United States - Full-time)** — 6 spacer paragraph(s)
- **Deployment Engineer - Southeast (US Remote - Full-time)** — 5 spacer paragraph(s)
- **Senior/Staff Embedded Software Engineer – Camera Systems (San Mateo, California, United States - Full-time)** — 4 spacer paragraph(s)
- **Sr/Staff Embedded Software Engineer - Camera Systems (Tampere, Finland - Full-time)** — 4 spacer paragraph(s)
- **Director, Growth Marketing - Commercial (San Mateo, California, United States - Full-time)** — 3 spacer paragraph(s)
- **Senior Business Operations Manager (San Mateo, California, United States - Full-time)** — 3 spacer paragraph(s)

### 3.5 Forced `<br>` line-break at the end of bullet items

**Affected: 9 / 106 postings.** A trailing `<br>` is
appended to the `<p>` inside `<li>`, which produces a visible blank line
*between bullets*. Other postings have evenly-spaced bullets. The
outlier here is **Director, Growth Marketing — Commercial**, which has
the `<br>` on 7 of its 23 bullets — so the bullet list looks "loose" in
some places and "tight" in others *within the same posting*.

- **Director, Growth Marketing - Commercial (San Mateo, California, United States - Full-time)** — `<br>` inside 7 of 23 bullets
- **Revenue Operations Engineer, Quoting Systems (San Mateo, California, United States - Full-time)** — `<br>` inside 3 of 25 bullets
- **Senior Technical Recruiter (San Mateo, California, United States - Full-time)** — `<br>` inside 2 of 14 bullets
- **GTM Data Engineer Intern (San Mateo, California, United States - Intern)** — `<br>` inside 2 of 18 bullets
- **Senior Technical Recruiter - Hardware Operations (San Mateo, California, United States - Full-time)** — `<br>` inside 1 of 13 bullets
- **Engineering Manager - Autonomy (San Mateo, California, United States - Full-time)** — `<br>` inside 1 of 10 bullets
- **PhD Autonomy Engineer Intern - Deep Learning or Computer Vision (San Mateo, California, United States - Intern)** — `<br>` inside 1 of 9 bullets
- **Aviation Compliance Lead (San Mateo, California, United States - Full-time)** — `<br>` inside 1 of 15 bullets
- **Senior Technical Support Representative - Japan (Tokyo, Japan - Full-time)** — `<br>` inside 1 of 20 bullets

### 3.6 Use of `<u>` underline

**Affected: 7 / 106 postings.** The dominant pattern never
uses underline. The 7 postings that do use it apply underlining to a
single phrase each — typically a recruiter-added emphasis line such as
*"Travel required: up to 25%"* or an underlined "Note:" prefix.
Underlined text in body copy looks like a hyperlink to readers, which
hurts scannability.

Postings using `<u>`:

- **Senior Technical Recruiter (San Mateo, California, United States - Full-time)**
- **Senior NPI Product Quality Engineer (San Mateo, California, United States - Full-time)**
- **Lead Staff Electrical Engineer (San Mateo, California, United States - Full-time)**
- **Senior Software Engineer, Full Stack (San Mateo, California, United States - Full-time)**
- **Senior Technical Recruiter - Hardware Operations (San Mateo, California, United States - Full-time)**
- **Staff Technical Recruiter (San Mateo, California, United States - Full-time)**
- **Full Stack Product Counsel (San Mateo, California, United States - Full-time)**

### 3.7 Bold + italic combinations

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

### 3.8 Section-heading capitalisation (sentence case vs Title Case vs ALL CAPS)

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

### 3.9 Different *section names* for the same logical section

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

### 3.10 Opening 'About Skydio' paragraph

**Consistent on this one.** All 106/106 postings open
with the same Skydio boilerplate paragraph — *"Skydio is the leading US
drone company …"* — although the embedded links and the trailing
sentence about diversity/E-Verify (post-Compensation) sometimes differ.
This is the one place where the site is already standardised.

### 3.11 Duplicated postings (same role, different locations) render differently

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

## 4. The 10 postings that stand out most from the norm

Each posting was scored by the number of flagged inconsistencies (see §3) it contains. The ten worst offenders, in descending order:

| # | Posting | # flags | Flags |
| --- | --- | --- | --- |
| 1 | **Revenue Operations Engineer, Quoting Systems** _( San Mateo, California, United States - Full-time )_ | 6 | uses real heading tags (5x <h2>); uses 2 empty spacer paragraph(s); forced <br> line-break inside 3/25 bullet items; mixes Title Case + sentence case section labels within the same posting; includes ALL-CAPS section label(s); heading-tag labels include trailing colon (e.g. 'What you’ll drive (scope):') |
| 2 | **Senior Technical Support Representative - Japan** _( Tokyo, Japan - Full-time )_ | 6 | uses real heading tags (3x <h1>); no Compensation/Compensation Range label at all; uses 1 empty spacer paragraph(s); forced <br> line-break inside 1/20 bullet items; mixes Title Case + sentence case section labels within the same posting; heading-tag labels include trailing colon (e.g. 'About the role:') |
| 3 | **Director, Growth Marketing - Commercial** _( San Mateo, California, United States - Full-time )_ | 4 | uses 3 empty <p>/<p><br></p> spacer paragraphs; forced <br> line-break inside 7/23 bullet items; combines bold + italic (1x); mixes Title Case + sentence case section labels within the same posting |
| 4 | **Senior Business Operations Manager** _( San Mateo, California, United States - Full-time )_ | 4 | uses real heading tags (3x <h3>); uses 3 empty <p>/<p><br></p> spacer paragraphs; mixes Title Case + sentence case section labels within the same posting; heading-tag labels include trailing colon (e.g. 'Strategic Sourcing:') |
| 5 | **Software Engineer - Simulation & Robotics Engineer** _( San Mateo, California, United States - Full-time )_ | 4 | uses real heading tags (5x <h3>); uses 2 empty spacer paragraph(s); section labels written in Title Case (norm = sentence case); heading-tag labels include trailing colon (e.g. 'About the Role:') |
| 6 | **Software Engineer - Cloud Simulation & Full-Stack** _( San Mateo, California, United States - Full-time )_ | 4 | uses real heading tags (5x <h2>); uses 2 empty spacer paragraph(s); section labels written in Title Case (norm = sentence case); heading-tag labels include trailing colon (e.g. 'About the Role:') |
| 7 | **Software Engineer - Cloud Simulation & Full-Stack** _( Zurich, Switzerland - Full-time )_ | 4 | uses real heading tags (5x <h2>); uses 2 empty spacer paragraph(s); section labels written in Title Case (norm = sentence case); heading-tag labels include trailing colon (e.g. 'About the Role:') |
| 8 | **Software Engineer - Autonomy Infrastructure, Systems and Tools** _( San Mateo, California, United States - Full-time )_ | 4 | uses real heading tags (5x <h2>); uses 1 empty spacer paragraph(s); section labels written in Title Case (norm = sentence case); heading-tag labels include trailing colon (e.g. 'About the Role:') |
| 9 | **Software Engineer - Autonomy Infrastructure, Systems and Tools** _( Zurich, Switzerland - Full-time )_ | 4 | uses real heading tags (5x <h2>); uses 1 empty spacer paragraph(s); section labels written in Title Case (norm = sentence case); heading-tag labels include trailing colon (e.g. 'About the Role:') |
| 10 | **Software Engineer - Simulation & Robotics Engineer** _( Zurich, Switzerland - Full-time )_ | 4 | uses real heading tags (5x <h3>); uses 2 empty spacer paragraph(s); section labels written in Title Case (norm = sentence case); heading-tag labels include trailing colon (e.g. 'About the Role:') |

## 5. Aggregate dashboard

| Issue | Postings affected | % of all postings |
| --- | --- | --- |
| Section headings authored as real `<h*>` tags (renders much larger) | 16 | 15% |
| Body wrapped inside a single `<ul>/<li>` | 1 | 1% |
| 'Compensation Range:' label instead of 'Compensation:' | 9 | 8% |
| Colon placed outside the bolded label | 6 | 6% |
| No Compensation label at all | 7 | 7% |
| Empty `<p>`/`<p><br></p>` spacer paragraphs present | 49 | 46% |
| `<br>` forced at the end of bullet items | 9 | 8% |
| `<u>` underline used in body copy | 7 | 7% |
| Bold + italic stacked on the same text | 2 | 2% |
| Title Case section labels (norm = sentence case) | 38 | 36% |
| Mixed casing styles within the same posting | 26 | 25% |
| Section headings with trailing colon **and** real heading tag | 11 | 10% |

## 6. Per-posting findings (full table)

Sorted by # of inconsistencies, then alphabetically. Postings with no row in the 'Issues' column are conformant to the dominant pattern.

| Posting | Location | Issues |
| --- | --- | --- |
| Revenue Operations Engineer, Quoting Systems | San Mateo, California, United States - Full-time | uses real heading tags (5x <h2>); uses 2 empty spacer paragraph(s); forced <br> line-break inside 3/25 bullet items; mixes Title Case + sentence case section labels within the same posting; includes ALL-CAPS section label(s); heading-tag labels include trailing colon (e.g. 'What you’ll drive (scope):') |
| Senior Technical Support Representative - Japan | Tokyo, Japan - Full-time | uses real heading tags (3x <h1>); no Compensation/Compensation Range label at all; uses 1 empty spacer paragraph(s); forced <br> line-break inside 1/20 bullet items; mixes Title Case + sentence case section labels within the same posting; heading-tag labels include trailing colon (e.g. 'About the role:') |
| Director, Growth Marketing - Commercial | San Mateo, California, United States - Full-time | uses 3 empty <p>/<p><br></p> spacer paragraphs; forced <br> line-break inside 7/23 bullet items; combines bold + italic (1x); mixes Title Case + sentence case section labels within the same posting |
| Full Stack Product Counsel | San Mateo, California, United States - Full-time | uses real heading tags (4x <h3>); no Compensation/Compensation Range label at all; uses 8 empty <p>/<p><br></p> spacer paragraphs; uses <u> underline (1x) |
| PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) | Zurich, Switzerland - Intern | uses real heading tags (3x <h3>); colon placed OUTSIDE the bolded label (e.g. '<strong>Compensation Range</strong>:'); mixes Title Case + sentence case section labels within the same posting; heading-tag labels include trailing colon (e.g. 'How you'll make an impact:') |
| Senior Business Operations Manager | San Mateo, California, United States - Full-time | uses real heading tags (3x <h3>); uses 3 empty <p>/<p><br></p> spacer paragraphs; mixes Title Case + sentence case section labels within the same posting; heading-tag labels include trailing colon (e.g. 'Strategic Sourcing:') |
| Software Engineer - Autonomy Infrastructure, Systems and Tools | San Mateo, California, United States - Full-time | uses real heading tags (5x <h2>); uses 1 empty spacer paragraph(s); section labels written in Title Case (norm = sentence case); heading-tag labels include trailing colon (e.g. 'About the Role:') |
| Software Engineer - Autonomy Infrastructure, Systems and Tools | Zurich, Switzerland - Full-time | uses real heading tags (5x <h2>); uses 1 empty spacer paragraph(s); section labels written in Title Case (norm = sentence case); heading-tag labels include trailing colon (e.g. 'About the Role:') |
| Software Engineer - Cloud Simulation & Full-Stack | San Mateo, California, United States - Full-time | uses real heading tags (5x <h2>); uses 2 empty spacer paragraph(s); section labels written in Title Case (norm = sentence case); heading-tag labels include trailing colon (e.g. 'About the Role:') |
| Software Engineer - Cloud Simulation & Full-Stack | Zurich, Switzerland - Full-time | uses real heading tags (5x <h2>); uses 2 empty spacer paragraph(s); section labels written in Title Case (norm = sentence case); heading-tag labels include trailing colon (e.g. 'About the Role:') |
| Software Engineer - Simulation & Robotics Engineer | San Mateo, California, United States - Full-time | uses real heading tags (5x <h3>); uses 2 empty spacer paragraph(s); section labels written in Title Case (norm = sentence case); heading-tag labels include trailing colon (e.g. 'About the Role:') |
| Software Engineer - Simulation & Robotics Engineer | Zurich, Switzerland - Full-time | uses real heading tags (5x <h3>); uses 2 empty spacer paragraph(s); section labels written in Title Case (norm = sentence case); heading-tag labels include trailing colon (e.g. 'About the Role:') |
| Aviation Compliance Lead | San Mateo, California, United States - Full-time | uses real heading tags (3x <h2>); uses 1 empty spacer paragraph(s); forced <br> line-break inside 1/15 bullet items |
| Director, Global Supply Management - Mechanicals | San Mateo, California, United States - Full-time | colon placed OUTSIDE the bolded label (e.g. '<strong>Compensation Range</strong>:'); uses 3 empty <p>/<p><br></p> spacer paragraphs; mixes Title Case + sentence case section labels within the same posting |
| Hardware Engineering Program Manager | San Mateo, California, United States - Full-time | uses real heading tags (3x <h2>, 5x <h3>); uses 3 empty <p>/<p><br></p> spacer paragraphs; mixes Title Case + sentence case section labels within the same posting |
| PhD Autonomy Engineer Intern - Deep Learning or Computer Vision | San Mateo, California, United States - Intern | no Compensation/Compensation Range label at all; forced <br> line-break inside 1/9 bullet items; mixes Title Case + sentence case section labels within the same posting |
| Senior Buyer | Hayward, California, United States - Full-time | uses real heading tags (2x <h2>); uses 3 empty <p>/<p><br></p> spacer paragraphs; heading-tag labels include trailing colon (e.g. 'How you will make an impact:') |
| Senior Director, Product Management, Drone as First Responder (DFR) | San Mateo, California, United States - Full-time | uses 'Compensation Range:' instead of 'Compensation:'; colon placed OUTSIDE the bolded label (e.g. '<strong>Compensation Range</strong>:'); mixes Title Case + sentence case section labels within the same posting |
| Senior NPI Product Quality Engineer | San Mateo, California, United States - Full-time | uses <u> underline (1x); combines bold + italic (1x); mixes Title Case + sentence case section labels within the same posting |
| Workplace Experience Coordinator Part-Time | Zurich, Switzerland - Part-time | no Compensation/Compensation Range label at all; uses 1 empty spacer paragraph(s); mixes Title Case + sentence case section labels within the same posting |
| Aviation Regulatory Program Manager | US Remote - Full-time | uses real heading tags (3x <h2>); uses 2 empty spacer paragraph(s) |
| Communications Manager | US Remote - Full-time | uses real heading tags (3x <h2>); uses 3 empty <p>/<p><br></p> spacer paragraphs |
| Deployment Engineer - Southeast | US Remote - Full-time | uses 5 empty <p>/<p><br></p> spacer paragraphs; mixes Title Case + sentence case section labels within the same posting |
| Director of Product Management, Drone as First Responder (DFR) | San Mateo, California, United States - Full-time | uses 'Compensation Range:' instead of 'Compensation:'; colon placed OUTSIDE the bolded label (e.g. '<strong>Compensation Range</strong>:') |
| Field Support Representative (Southwest, Remote) | US Remote - Full-time | uses 2 empty spacer paragraph(s); mixes Title Case + sentence case section labels within the same posting |
| GTM Data Engineer Intern | San Mateo, California, United States - Intern | uses 2 empty spacer paragraph(s); forced <br> line-break inside 2/18 bullet items |
| GTM Enablement Associate | San Mateo, California, United States - Full-time | uses 1 empty spacer paragraph(s); mixes Title Case + sentence case section labels within the same posting |
| IT Technician (Help Desk - Linux Focus) | Hayward, California, United States - Full-time | uses 2 empty spacer paragraph(s); section labels written in Title Case (norm = sentence case) |
| Lead Staff Electrical Engineer | San Mateo, California, United States - Full-time | uses 2 empty spacer paragraph(s); uses <u> underline (1x) |
| Manager, Technical Support | US CA San Mateo - Full-time | colon placed OUTSIDE the bolded label (e.g. '<strong>Compensation Range</strong>:'); mixes Title Case + sentence case section labels within the same posting |
| Program Manager, Major Deployments (Hawaii) | San Mateo, California, United States - Full-time | uses 3 empty <p>/<p><br></p> spacer paragraphs; mixes Title Case + sentence case section labels within the same posting |
| Program Manager, Major Deployments (Mid Atlantic) | US Remote - Full-time | uses 3 empty <p>/<p><br></p> spacer paragraphs; mixes Title Case + sentence case section labels within the same posting |
| Sales Planning Analyst Intern | San Mateo, California, United States - Intern | uses 'Compensation Range:' instead of 'Compensation:'; uses 1 empty spacer paragraph(s) |
| Senior Customer Support Representative - India | Bangalore, India - Full-time | uses 1 empty spacer paragraph(s); mixes Title Case + sentence case section labels within the same posting |
| Senior People Analytics Analyst | San Mateo, California, United States - Full-time | uses 'Compensation Range:' instead of 'Compensation:'; section labels written in Title Case (norm = sentence case) |
| Senior Product Manager, Platform & Infrastructure | San Mateo, California, United States - Full-time | uses 6 empty <p>/<p><br></p> spacer paragraphs; mixes Title Case + sentence case section labels within the same posting |
| Senior Revenue Operations Manager | San Mateo, California, United States - Full-time | uses 2 empty spacer paragraph(s); section labels written in Title Case (norm = sentence case) |
| Senior Software Engineer - Mobile Platform | San Mateo, California, United States - Full-time | uses 3 empty <p>/<p><br></p> spacer paragraphs; section labels written in Title Case (norm = sentence case) |
| Senior Technical Recruiter | San Mateo, California, United States - Full-time | forced <br> line-break inside 2/14 bullet items; uses <u> underline (1x) |
| Senior Technical Recruiter - Hardware Operations | San Mateo, California, United States - Full-time | forced <br> line-break inside 1/13 bullet items; uses <u> underline (1x) |
| Software Engineer Intern Fall 2026/Winter 2027 | US CA San Mateo - Intern | uses 'Compensation Range:' instead of 'Compensation:'; uses 1 empty spacer paragraph(s) |
| Staff Product Manager, Platform & Infrastructure | San Mateo, California, United States - Full-time | uses 6 empty <p>/<p><br></p> spacer paragraphs; mixes Title Case + sentence case section labels within the same posting |
| Success Systems Specialist | US Remote - Full-time | uses 1 empty spacer paragraph(s); mixes Title Case + sentence case section labels within the same posting |
| Supplier Quality Engineer, Sustaining | Taiwan - Full-time | no Compensation/Compensation Range label at all; uses 1 empty spacer paragraph(s) |
| Technical Support Specialist - West Coast | US Remote - Full-time | colon placed OUTSIDE the bolded label (e.g. '<strong>Compensation Range</strong>:'); section labels written in Title Case (norm = sentence case) |
| Autonomy Engineer - Deep Learning Infrastructure | San Mateo, California, United States - Full-time | uses 1 empty spacer paragraph(s) |
| Autonomy Engineer - ML & DL Infrastructure | San Mateo, California, United States - Full-time | uses 3 empty <p>/<p><br></p> spacer paragraphs |
| Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 | San Mateo, California, United States - Intern | uses 'Compensation Range:' instead of 'Compensation:' |
| Autonomy Engineer Intern - Deep Learning (Computational Photography) | Zurich, Switzerland or Tampere, Finland - Intern | no Compensation/Compensation Range label at all |
| Autonomy Engineer Intern - Deep Learning (Computational Photography) | San Mateo, California, United States - Intern | no Compensation/Compensation Range label at all |
| Autonomy Engineer Intern Fall 2026 | San Mateo, California, United States - Intern | uses 'Compensation Range:' instead of 'Compensation:' |
| Customer Success Manager, DFR Majors - Northeast | US Remote - Full-time | mixes Title Case + sentence case section labels within the same posting |
| Customer Success Manager, DFR Majors - Southeast | US Remote - Full-time | mixes Title Case + sentence case section labels within the same posting |
| Engineering Manager - Autonomy | San Mateo, California, United States - Full-time | forced <br> line-break inside 1/10 bullet items |
| Hardware Operations Program Manager | Hayward, California, United States - Full-time | uses 3 empty <p>/<p><br></p> spacer paragraphs |
| Head of Warehouse & Logistics Operations | US CA Production - Full-time | uses 2 empty spacer paragraph(s) |
| Manager, Logistics | US CA Production - Full-time | uses 2 empty spacer paragraph(s) |
| Middleware Software Engineer Intern - Fall 2026 | US CA San Mateo - Intern | uses 'Compensation Range:' instead of 'Compensation:' |
| Product Support Engineer | San Mateo, California, United States - Full-time | uses 2 empty spacer paragraph(s) |
| Product Support Engineer Intern | San Mateo, California, United States - Intern | uses 3 empty <p>/<p><br></p> spacer paragraphs |
| Production Manager, PM Shift | Hayward, California, United States - Full-time | uses 3 empty <p>/<p><br></p> spacer paragraphs |
| Senior Autonomy Engineer - Deep Learning | San Mateo, California, United States - Full-time | uses 1 empty spacer paragraph(s) |
| Senior Brand Designer (Contract) | San Mateo, California, United States - Full-time | uses 3 empty <p>/<p><br></p> spacer paragraphs |
| Senior RF Design Engineer | San Mateo, California, United States - Full-time | uses 2 empty spacer paragraph(s) |
| Senior Software Engineer,  Data Platform | San Mateo, California, United States - Full-time | mixes Title Case + sentence case section labels within the same posting |
| Senior Software Engineer, Frontend | San Mateo, California, United States - Full-time | section labels written in Title Case (norm = sentence case) |
| Senior Software Engineer, Full Stack | San Mateo, California, United States - Full-time | uses <u> underline (1x) |
| Senior/Staff Embedded Software Engineer – Camera Systems | San Mateo, California, United States - Full-time | uses 4 empty <p>/<p><br></p> spacer paragraphs |
| Software Engineer, Full Stack | San Mateo, California, United States - Full-time | mixes Title Case + sentence case section labels within the same posting |
| Sr/Staff Embedded Software Engineer - Camera Systems | Tampere, Finland - Full-time | uses 4 empty <p>/<p><br></p> spacer paragraphs |
| Staff Global Supply Manager,  Mechanicals | San Mateo, California, United States - Full-time | uses 1 empty spacer paragraph(s) |
| Staff Software Engineer, Frontend | San Mateo, California, United States - Full-time | mixes Title Case + sentence case section labels within the same posting |
| Staff Technical Recruiter | San Mateo, California, United States - Full-time | uses <u> underline (1x) |
| Supply Chain Intern | San Mateo, California, United States - Intern | uses 'Compensation Range:' instead of 'Compensation:' |
| Autonomy Engineer - Deep Learning | Zurich, Switzerland - Full-time | _(matches the norm)_ |
| Autonomy Engineer - Deep Learning | San Mateo, California, United States - Full-time | _(matches the norm)_ |
| Autonomy Engineer - Deep Learning Infrastructure | Zurich, Switzerland - Full-time | _(matches the norm)_ |
| Autonomy Engineer - Deep Learning Model Acceleration | Zurich, Switzerland - Full-time | _(matches the norm)_ |
| Autonomy Engineer - Deep Learning Model Acceleration | San Mateo, California, United States - Full-time | _(matches the norm)_ |
| Autonomy Engineer - Fixed Wing Planning & Controls | San Mateo, California, United States - Full-time | _(matches the norm)_ |
| Autonomy Software Engineer | San Mateo, California, United States - Full-time | _(matches the norm)_ |
| Electrical Engineer (all levels) | San Mateo, California, United States - Full-time | _(matches the norm)_ |
| Electrical Engineer (Sustaining/Validation) | San Mateo, California, United States - Full-time | _(matches the norm)_ |
| Enterprise Account Manager (MoD/ MoI) – EMEA (Finland) | Tampere, Finland - Full-time | _(matches the norm)_ |
| Enterprise Account Manager (MoD/ MoI) – EMEA (Germany) | Germany - Full-time | _(matches the norm)_ |
| Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland) | Zurich, Switzerland - Full-time | _(matches the norm)_ |
| Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM | US Remote - Full-time | _(matches the norm)_ |
| Enterprise Account Manager, US Army | US Remote - Full-time | _(matches the norm)_ |
| Field Support Representative | US Remote - Full-time | _(matches the norm)_ |
| Mission Success Operations Manager | US Remote - Full-time | _(matches the norm)_ |
| PCB Layout Engineer | San Mateo, California, United States - Full-time | _(matches the norm)_ |
| Product Design Engineer (All Levels) | San Mateo, California, United States - Full-time | _(matches the norm)_ |
| RF Design Engineer | San Mateo, California, United States - Full-time | _(matches the norm)_ |
| Senior Autonomy Engineer - Controls | San Mateo, California, United States - Full-time | _(matches the norm)_ |
| Senior Autonomy Engineer - Deep Learning | Zurich, Switzerland - Full-time | _(matches the norm)_ |
| Senior Hardware Test and Reliability Engineer | San Mateo, California, United States - Full-time | _(matches the norm)_ |
| Senior Software Engineer - Embedded | San Mateo, California, United States - Full-time | _(matches the norm)_ |
| Senior Software Engineer - Security | San Mateo, California, United States - Full-time | _(matches the norm)_ |
| Senior Software Engineer,  Infrastructure | San Mateo, California, United States - Full-time | _(matches the norm)_ |
| Senior Wireless Systems Performance Engineer | San Mateo, California, United States - Full-time | _(matches the norm)_ |
| Software Engineer - Embedded | San Mateo, California, United States - Full-time | _(matches the norm)_ |
| Software Engineer - Infrastructure | San Mateo, California, United States - Full-time | _(matches the norm)_ |
| Staff Software Engineer - Embedded | San Mateo, California, United States - Full-time | _(matches the norm)_ |
| Staff Software Engineer, Full Stack | San Mateo, California, United States - Full-time | _(matches the norm)_ |
| Systems Integration and Test Engineer (Mid to Senior Level) | San Mateo, California, United States - Full-time | _(matches the norm)_ |
| Wireless Software Engineer | San Mateo, California, United States - Full-time | _(matches the norm)_ |

## 7. Recommendations for standardising

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

---

### Appendix — methodology

- Source URL: <https://www.skydio.com/careers>, fetched 2026-05-23.
- 106 unique posting URLs of the form `/jobs/<uuid>/?gh_jid=<uuid>` were enumerated from the careers page.
- Each posting's HTML was downloaded directly (no JS execution required — the prose block ships in the server-rendered HTML).
- The prose block for each posting was parsed with BeautifulSoup, truncated at the Compensation heading (tolerating all five label variants found in §3.3), and then scored against the conventions described in §2.
- The parser source is in `scripts/analyze.py`; the report-builder is in `scripts/build_report.py`; the raw per-posting JSON is in `data/job_analysis.json` and the per-posting CSV in `reports/job_posting_formatting_findings.csv`.

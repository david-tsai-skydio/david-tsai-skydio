# Skydio Careers — Job Posting Formatting Consistency Report

**Scope:** All job postings currently published at
`https://www.skydio.com/careers` (linked through `/jobs/{uuid}/?gh_jid=…`).
Analysis was limited to the content that appears **above** the `Compensation:`
paragraph, as requested. The career landing page itself was not scored —
only the individual job-detail pages.

- Total open postings found on the careers page: **107**
- Pages successfully fetched & parsed: **107 / 107**
- Postings where a `Compensation` block could not be located in the
  pre-compensation content (flagged below): **6**
- Date of capture: 2026-05-19

> **What we measured.** Because the careers site renders the body of each
> posting from a shared CMS into a single `<div class="prose block-content">`
> wrapper, the *visual* font sizes, colors, line-heights and weights are
> driven by the global `prose` stylesheet. That means "different font size"
> on these pages can almost only be caused by editors using a different
> *HTML element* (e.g. `<h2>` vs `<p><strong>`) or a different *inline
> style*. Our analysis therefore concentrated on the HTML element used for
> each visual concept (section heading, body paragraph, list item, …),
> plus inline `style`/`class` attributes, plus the semantic naming and
> capitalization of section headings, since those are the controls editors
> actually have.

---

## TL;DR — top inconsistencies

| # | Inconsistency | Affected postings |
|---|---|---|
| 1 | Section headings rendered as `<p><strong>` (default) vs `<h2>` vs `<h3>` vs `<h1>` — visually different font sizes | **20 / 107** use a non-default element |
| 2 | Title-case vs sentence-case for the same heading ("About the Role:" vs "About the role:", "How You'll Make an Impact:" vs "How you'll make an impact:") | ~**45 / 107** |
| 3 | Straight `'` vs curly `'` apostrophe in the *same* heading text | mixed across postings |
| 4 | Trailing colon on section headings present in 287 occurrences, absent in 37, period in 3, question mark in 1 | ~**15 / 107** drop the colon |
| 5 | Inconsistent section *naming* (e.g. "What makes you a good fit" vs "Qualifications" vs "What we're looking for" vs "Areas of Responsibility") | **35 distinct unclassified headings** across postings |
| 6 | Empty `<p></p>` blocks creating extra vertical whitespace between sections | **46 / 107** (up to 6 empty paragraphs in one posting) |
| 7 | "About Skydio" intro paragraph diverges from the canonical wording | only **6 / 107** match the canonical block verbatim; **6 / 107** do not start with "Skydio…" at all |
| 8 | `Compensation:` block missing from the description body | **5 / 107** (legal/compliance risk for CA & similar jurisdictions) |
| 9 | Stray `#LI-XX1` LinkedIn source tag left in the visible body | **2+** |
| 10 | Typos / oddities in section heading text or job title (e.g. "What Makes Your a Good Fit:") | **1 confirmed** + 1 double-space title |

---

## 1. Method

1. Scraped `https://www.skydio.com/careers` and extracted all 107 unique
   `/jobs/{uuid}/?gh_jid=…` links plus their visible job titles.
2. Fetched each detail page server-side (no JS) and parsed the
   `<div class="prose block-content">` that holds the description body.
3. For each posting, kept every direct child element **up to (and not
   including)** the block whose `<strong>` text starts with
   `Compensation` (the few jobs where this could not be located are
   flagged separately).
4. For each retained block recorded: HTML tag, element classes, inline
   `style` attributes, presence of `<strong>`/`<em>`/`<u>`/`<br>`/`<a>`,
   whether the block is a section heading (defined as an `<h1–h6>` or a
   `<p>` whose entire visible text is wrapped in a single `<strong>`),
   the heading text, capitalization style and trailing punctuation.
5. Aggregated across the 107 postings to find the modal pattern and the
   deviations from it.

Raw artifacts produced during analysis (kept under `/tmp/jobs/` on the
agent's machine, not committed): per-job JSON in `results.json`, the
landing page snapshot `index.tsv`, the 107 individual HTML pages, and a
per-job table in `per_job_table.txt`. The full per-job table is
reproduced in section 8 of this report.

---

## 2. The "canonical" posting (what most postings look like)

Looking at the dominant pattern across the 107 postings, a Skydio job
description "should" look like this in HTML order, *above* the
Compensation block:

```html
<p>Skydio is the leading US drone company and the world leader in autonomous flight … [3-5 sentence "About Skydio" intro]</p>
<p><strong>About the role:</strong></p>
<p>[1–4 paragraphs describing the role]</p>
<p><strong>How you'll make an impact:</strong></p>
<ul><li><p>…</p></li>…</ul>
<p><strong>What makes you a good fit:</strong></p>
<ul><li><p>…</p></li>…</ul>
```

- **Heading style:** `<p><strong>{Sentence case heading}:</strong></p>`
- **Heading text:** sentence-case with a trailing colon
- **Lists:** `<ul>` with `<li><p>…</p></li>` items, no nested lists
- **Body paragraphs:** plain `<p>` with no inline styling

**87 / 107 (81 %)** postings use the `<p><strong>` heading style **for
every** section heading. The remaining **20 / 107 (19 %)** deviate.

---

## 3. Font-size / element inconsistencies

Visual font size on this site is determined by the element type. The
`prose` CSS gives `<p>` ≈ 16 px body, `<h2>` ≈ ~24–28 px, `<h3>` ≈ ~20 px,
`<h1>` ≈ ~32–40 px (depends on viewport). Because some editors used
heading elements while others used bolded paragraphs, the *same logical
section heading* is visually larger on some postings than on others.

| Heading element used | # postings | Effect |
|---|---:|---|
| `<p><strong>` only (canonical) | **87** | section headers same size as body text, just bold |
| `<h2>` only | **7** | section headers ~1.5×–1.75× body — visibly larger than peers |
| `<h2>` + `<p><strong>` mixed | **2** | inconsistent sizes **within the same posting** |
| `<h3>` only | **2** | section headers ~1.25× body |
| `<h3>` + `<p><strong>` mixed | **2** | inconsistent sizes within the same posting |
| `<h1>` only | **1** | section headers as large as the page title — clear outlier |
| No section headers detected | **6** | special / missing layout (see §6) |

### Postings that stand out because of heading element

**Use `<h2>` for sections (visually larger than peers):**
- Aviation Compliance Lead
- Aviation Regulatory Program Manager
- Communications Manager
- Senior Buyer *(mixed with `<p><strong>` for "About the role:")*
- Revenue Operations Engineer, Quoting Systems *(mixed)*
- Software Engineer – Cloud Simulation & Full-Stack (San Mateo)
- Software Engineer – Cloud Simulation & Full-Stack (Zurich)
- Software Engineer – Autonomy Infrastructure, Systems and Tools (San Mateo)
- Software Engineer – Autonomy Infrastructure, Systems and Tools (Zurich)

**Use `<h3>` for sections:**
- Software Engineer – Simulation & Robotics Engineer (San Mateo)
- Software Engineer – Simulation & Robotics Engineer (Zurich)
- Senior Business Operations Manager *(mixed — `<p><strong>` for "About the Role:" / "How you'll make an impact:" / "What makes you a good fit:" but `<h3>` for three internal sub-headings "Strategic Sourcing", "Cost Management", "Strategy & Operations")*
- PhD Autonomy Engineer Intern – Planning & Controls (Reinforcement Learning) *(mixed)*
- Full Stack Product Counsel — uses `<h3>` for "About the Team", "About the Role", "How You'll Make an Impact", "What Makes You a Great Fit"

**Uses `<h1>` for sections — the biggest visual outlier:**
- **Senior Technical Support Representative – Japan** — uses `<h1>About the role:</h1>`, `<h1>How you'll make an impact:</h1>`, `<h1>What would make you a good fit:</h1>`. These render at page-title size; they should be `<p><strong>` like its peers.

### Inline `style` attribute outlier

Only **one** posting in the entire set carries any inline `style`
attribute on body content:

- **Manager, Logistics** — a paragraph carries
  `style="min-height:1.2em;margin-top:0;margin-bottom:0"`. This is a
  leftover from a paste-from-Word import; it forces zero margins on that
  paragraph, producing tighter line spacing than every other posting.

No posting uses inline `color`, `background-color`, `font-family` or
`font-weight` overrides. Good — these would otherwise be the place to
look for hard-coded colour drift.

---

## 4. Heading-text inconsistencies (wording, case, punctuation)

The four most common heading concepts and the unique phrasings that show
up across postings:

### 4a. "About the role" (used by ~80 postings)

| Variant text | Count |
|---|---:|
| `About the role:` (sentence + colon) | **42** |
| `About the Role:` (title + colon) | **26** |
| `About the Team:` | 6 |
| `About the team:` | 5 |
| `About the Role` (no colon) | 3 |
| `About the role` (no colon) | 2 |
| `About The Role` (Title Case of all words) | 1 |
| `About the team` | 1 |

**Issues:** mixed sentence vs title case for the same heading; some keep
the trailing colon, some don't; "the Role" vs "the Team" used
interchangeably; the lone `About The Role` capitalises *every* word
including "The".

### 4b. "How you'll make an impact" (used by ~80 postings)

| Variant text | Count |
|---|---:|
| `How you'll make an impact:` (straight apostrophe, sentence case, colon) | **34** |
| `How You'll Make an Impact:` (curly apostrophe, title case, colon) | **18** |
| `How you'll make an impact:` (curly apostrophe, sentence case, colon) | **12** |
| `What You'll Do:` | 6 |
| `How you will make an impact:` (no contraction) | 4 |
| `How You'll Make an Impact` (no colon) | 2 |
| `Key Responsibilities:` | 1 |
| `How You'll Make an Impact:` (curly apostrophe **+** title case **+** colon) | 1 |
| `What You'll Do` (no colon) | 1 |
| `How you'll make an impact` (no colon) | 1 |
| `Areas of Responsibility:` (4 Cloud-Sim/Autonomy-Infra postings) | 6 |
| Other unique forms | several |

**Issues:** **three** different concepts ("impact", "what you'll do",
"areas of responsibility", "key responsibilities") all do the same job;
even within a single concept, six combinations of straight-vs-curly
apostrophe × sentence-vs-title case × colon-present-or-not appear.

### 4c. "What makes you a good fit" (used by ~80 postings)

| Variant text | Count |
|---|---:|
| `What makes you a good fit:` | **50** |
| `What Makes You a Good Fit:` | 16 |
| `Qualifications:` | 6 |
| `What makes you a good fit` (no colon) | 5 |
| `What Makes You A Good Fit:` (capital A) | 3 |
| `What Makes You a Good Fit` (no colon) | 3 |
| `What would make you a good fit:` | 5 |
| `What makes you a strong fit:` | 3 |
| `What makes this internship different:` | 1 |
| `What Makes You a Great Fit` *(Full Stack Product Counsel)* | 1 |
| `What Makes Your a Good Fit:` ⚠️ **typo** *(Senior People Analytics Analyst)* | 1 |

### 4d. "Nice to have / Bonus" (optional section)

| Variant text | Count |
|---|---:|
| `Bonus points:` | 3 |
| `Bonus Points:` | 3 |
| `Bonus Experience:` *(used by the 6 `<h2>`/`<h3>` Cloud-Sim/Autonomy-Infra postings)* | 6 |
| `Bonus points for:` | 4 |
| `Preferred Qualifications:` | 2 |
| `Nice to have:` | 2 |
| `Preferred Qualifications` (no colon) | 1 |
| `Nice to Have` (no colon) | 1 |
| `Nice To Haves:` | 1 |
| `Additional Desired Experience and Skills` (no colon) | 1 |

### 4e. Trailing punctuation across **all** section headings

| Trailing char | Count |
|---|---:|
| `:` | 287 |
| (none) | 37 |
| `.` | 3 |
| `?` | 1 |

Roughly **13 %** of section headings break the colon convention.

### 4f. Capitalization across **all** section headings

| Style | Count |
|---|---:|
| Sentence case ("About the role") | 187 |
| Title Case ("About the Role") | 109 |
| Mixed / inconsistent | 32 |

The two styles each have a strong following — neither is "wrong" in
isolation, but they are mixed *within* the corpus and sometimes *within*
the same posting.

---

## 5. "About Skydio" intro inconsistencies

The canonical "About Skydio" intro paragraph is:

> "Skydio is the leading US drone company and the world leader in
> autonomous flight, the key technology for the future of drones and
> aerial mobility. The Skydio team combines deep expertise in artificial
> intelligence, best-in-class hardware and software product development,
> operational excellence, and customer obsession to empower a broader,
> more diverse audience of drone users. From utility inspectors to first
> responders, soldiers in battlefield scenarios and beyond."

- **101 / 107** postings *start* with "Skydio is the leading US drone
  company…" — good.
- Only **6 / 107** contain this canonical paragraph *verbatim*. The
  other 95 have diverged through small edits, sentence reorders, and
  insertions over time.
- **6 / 107** postings do not contain a Skydio intro paragraph before
  the first section heading at all.
- **27 / 107** postings have **two or more** intro-style paragraphs
  before the first section header (typically a second "background on
  the team" paragraph). This is fine on its own but creates uneven
  density between postings — some openings are 1 paragraph long, others
  are 5.

**Block-count distribution** (number of pre-Compensation blocks per
posting): **min 5**, median ~9, max **28**. Outliers on the long side:

- 28 — IT Technician (Help Desk – Linux Focus)
- 26 — Director, Global Supply Management – Mechanicals
- 19 — Success Systems Specialist
- 16 — Staff Product Manager, Platform & Infrastructure
- 16 — Senior Product Manager, Platform & Infrastructure

Outliers on the short side (just the canonical intro + one bullet list,
no "fit" or "impact" header):

- Autonomy Engineer – Deep Learning Infrastructure (both postings)
- Autonomy Engineer – Deep Learning Model Acceleration (both postings)
- Autonomy Software Engineer
- PhD Autonomy Engineer Intern – Deep Learning or Computer Vision

---

## 6. Postings missing the Compensation block entirely

The following **5 postings** do not contain any `Compensation:` block in
the pre-Compensation portion of their description body. For the four US
postings this is a potential California pay-transparency issue and
should be added back:

1. **Autonomy Engineer Intern – Deep Learning (Computational Photography)** — San Mateo
2. **Autonomy Engineer Intern – Deep Learning (Computational Photography)** — Zurich (intern outside CA, lower legal risk but inconsistent with peers)
3. **Supplier Quality Engineer, Sustaining** — Taiwan
4. **Workplace Experience Coordinator Part-Time** — Zurich
5. **Senior Technical Support Representative – Japan** — Tokyo (this one *also* uses `<h1>` for section headings, see §3)

Additionally, **Full Stack Product Counsel** *has* a Compensation
paragraph but its leading text "At Skydio, our compensation packages…"
is **not** wrapped in `<strong>Compensation:</strong>` like the other
~100 postings. So the bold "Compensation:" label is silently missing on
that one posting.

---

## 7. Other formatting issues

### 7a. Empty paragraphs (extra vertical whitespace)

**46 / 107** postings contain at least one empty `<p></p>` block in the
pre-Compensation content, which renders as inconsistent vertical
spacing between sections. The worst offenders:

| Empty `<p>` blocks | Posting |
|---:|---|
| 6 | Staff Product Manager, Platform & Infrastructure |
| 6 | Senior Product Manager, Platform & Infrastructure |
| 3 | Sr/Staff Embedded Software Engineer – Camera Systems (Tampere) |
| 3 | Senior Software Engineer – Mobile Platform |
| 3 | Senior Buyer |
| 3 | Senior Brand Designer (Contract) |
| 3 | Program Manager, Major Deployments (South East) |
| 3 | Program Manager, Major Deployments (Mid Atlantic) |
| 3 | Product Support Engineer Intern |
| 3 | Director, Growth Marketing – Commercial |
| 3 | Senior Software Engineer – Mobile Platform |
| 3 | Director, Global Supply Management – Mechanicals |

The two `Platform & Infrastructure` PM postings have **six** blank
paragraphs each — that is a visible double-or-triple gap before the
next section.

### 7b. `<br>` for line breaks

**42 / 107** postings use `<br>` inside body paragraphs (often where a
section heading was typed on the same line as the following content),
while the other **65** do not. This results in slightly different
within-paragraph line spacing between postings, especially in the
"About the role" paragraph.

### 7c. `<em>` / italics

Only **3** postings use italics in pre-Compensation content:

- Director, Growth Marketing – Commercial
- Senior NPI Product Quality Engineer
- Electric Motor / Propulsion Engineer

If italics aren't part of the editorial style guide, these three should
be reviewed.

### 7d. Inline links

**59 / 107** postings contain at least one in-body hyperlink (e.g. links
to product pages, blog posts, customer stories). The other 48 contain
none. The link styling is consistent (driven by the global stylesheet)
but the *presence* of links is uneven — some postings act like a
landing page with multiple cross-links, others are link-free.

### 7e. "Orphan" inline bold (bold used mid-paragraph for emphasis)

**46 / 107** postings have at least one inline `<strong>` *within* a
paragraph (not as a section header). Examples include bolding location
requirements ("**Note:** this position is based in…"), bolding job
specifics, or bolding sub-section labels inside a paragraph. Used
inconsistently across postings.

### 7f. Stray internal recruiter tags in body

At least these postings ship the LinkedIn-source tag in the visible
body text (under the description, *near* the Compensation block in some
cases):

- Supplier Quality Engineer, Sustaining — `#LI-BJ1`
- (Several others have `#LI-…` after Compensation, but this one ships
  it inside the body because the Compensation block is missing — see §6.)

### 7g. Title-string oddities (on the careers landing page itself)

- "**What Makes Your a Good Fit:**" — typo in *Senior People Analytics
  Analyst* (should be "What Makes You a Good Fit").
- "**Staff Global Supply Manager,  Mechanicals**" — title contains two
  consecutive spaces after the comma; renders an extra-wide gap on the
  listing.
- "**Autonomy Engineer - ML & DL Infrastructure **" — trailing space
  after the title.
- Three of the EMEA "Enterprise Account Manager" postings (Finland /
  Germany / Switzerland) carry the line "**This role must be based in
  Switzerland, Germany, or Finland.**" wrapped in `<strong>` as if it
  were a section header — it isn't a section, it's a single-sentence
  callout, and it ends with a period instead of a colon.

---

## 8. Per-posting roll-up

Legend:
- `#blk` — number of HTML blocks above the Compensation block
- `#hdr` — number of section headings detected
- `styles` — heading element(s) used: `p>strong` (canonical), `h2`,
  `h3`, `h1`
- `intro` — `Y` if first paragraph starts with "Skydio…"
- `em` — has italics in pre-comp content
- `br` — uses `<br>` line breaks
- `a` — contains in-body hyperlinks
- `empty` — count of empty `<p>` blocks
- 🚩 — flagged for review (non-canonical heading element, missing
  comp, typo, inline style override, very long, etc.)

| Title | #blk | #hdr | styles | intro | em | br | a | empty | flags |
|---|---:|---:|---|:-:|:-:|:-:|:-:|---:|---|
| Autonomy Engineer - Deep Learning (San Mateo) | 8 | 3 | p>strong | Y |  |  | Y |  |  |
| Autonomy Engineer - Deep Learning (Zurich) | 8 | 3 | p>strong | Y |  |  |  |  |  |
| Autonomy Engineer - Deep Learning Infrastructure (San Mateo) | 5 | 1 | p>strong | Y |  | Y |  |  | 🚩 very short — no `fit` heading |
| Autonomy Engineer - Deep Learning Infrastructure (Zurich) | 6 | 1 | p>strong | Y |  | Y | Y | 1 | 🚩 very short — no `fit` heading |
| Autonomy Engineer - Deep Learning Model Acceleration (San Mateo) | 5 | 1 | p>strong | Y |  | Y |  |  | 🚩 very short |
| Autonomy Engineer - Deep Learning Model Acceleration (Zurich) | 5 | 1 | p>strong | Y |  | Y | Y |  | 🚩 very short |
| Autonomy Engineer - Fixed Wing Planning & Controls | 7 | 3 | p>strong | Y |  |  |  |  |  |
| Autonomy Engineer - ML & DL Infrastructure | 11 | 3 | p>strong | Y |  |  | Y | 2 | 🚩 trailing space in title |
| Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 | 9 | 3 | p>strong | Y |  | Y | Y |  |  |
| Autonomy Engineer Intern - Deep Learning (Computational Photography) (SMT) | n/a | n/a | n/a | Y |  |  |  |  | 🚩 **Compensation block missing** |
| Autonomy Engineer Intern - Deep Learning (Computational Photography) (Zurich) | n/a | n/a | n/a | Y |  |  |  |  | 🚩 **Compensation block missing** |
| Autonomy Engineer Intern - Deep Learning (Computational Photography) (Tampere) | 11 | 3 | p>strong | Y |  |  |  | 1 |  |
| Autonomy Engineer Intern Fall 2026 | 8 | 3 | p>strong | Y |  |  | Y |  |  |
| Autonomy Software Engineer | 5 | 1 | p>strong | Y |  | Y | Y |  | 🚩 very short |
| Aviation Compliance Lead | 10 | 3 | **h2** | Y |  | Y |  | 1 | 🚩 `<h2>` headings |
| Aviation Regulatory Program Manager | 13 | 3 | **h2** | Y |  |  |  | 2 | 🚩 `<h2>` headings |
| Communications Manager | 10 | 3 | **h2** | Y |  |  | Y | 2 | 🚩 `<h2>` headings |
| Customer Success Manager, DFR Majors - Northeast | 10 | 4 | p>strong | Y |  |  |  |  |  |
| Deployment Engineer - Southeast | 15 | 5 | p>strong | Y |  |  | Y | 3 | 🚩 many empty paragraphs |
| Director of Product Management, Drone as First Responder (DFR) | 7 | 2 | p>strong | Y |  | Y | Y |  | 🚩 no `fit` heading |
| Director, Global Supply Management - Mechanicals | 26 | 3 | p>strong | Y |  |  | Y | 3 | 🚩 very long, many empty paragraphs |
| Director, Growth Marketing - Commercial | 16 | 5 | p>strong | Y | Y | Y | Y | 3 | 🚩 italics + many empty paragraphs |
| Electric Motor / Propulsion Engineer | 7 | 2 | p>strong | Y | Y | Y | Y |  | 🚩 italics |
| Electrical Engineer (Sustaining/Validation) | 6 | 2 | p>strong | Y |  | Y | Y |  |  |
| Electrical Engineer (all levels) | 6 | 2 | p>strong | Y |  | Y | Y |  |  |
| Engineering Manager - Autonomy | 7 | 3 | p>strong | Y |  | Y | Y |  |  |
| Enterprise Account Manager (MoD/MoI) – EMEA (Finland) | 10 | 4 | p>strong | Y |  | Y |  |  | 🚩 4th "section" is a single-sentence period-terminated callout |
| Enterprise Account Manager (MoD/MoI) – EMEA (Germany) | 10 | 4 | p>strong | Y |  | Y |  |  | 🚩 same |
| Enterprise Account Manager (MoD/MoI) – EMEA (Switzerland) | 10 | 4 | p>strong | Y |  | Y |  |  | 🚩 same |
| Enterprise Account Manager, US Navy, US Marine Corps, and IC/SOCOM | 11 | 4 | p>strong | Y |  | Y | Y |  |  |
| Enterprise Account Manager, US Army | 11 | 4 | p>strong | Y |  | Y | Y |  |  |
| Field Support Representative | 10 | 4 | p>strong | Y |  | Y |  |  |  |
| Field Support Representative (Southwest, Remote) | 12 | 4 | p>strong | Y |  | Y |  | 2 |  |
| Full Stack Product Counsel | n/a | n/a | **h3** | Y |  |  | Y | several | 🚩 `<h3>` headings; "Compensation:" label not bolded; "What Makes You a **Great** Fit" wording |
| GTM Data Engineer Intern | 11 | 4 | p>strong | Y |  | Y |  | 2 |  |
| GTM Enablement Associate | 9 | 3 | p>strong | Y |  | Y |  | 1 |  |
| Hardware Operations Program Manager | 8 | 3 | p>strong | Y |  |  | Y | 1 |  |
| Hardware Technician | 11 | 4 | p>strong | Y |  | Y |  | 1 |  |
| Head of Warehouse & Logistics Operations | 13 | 4 | p>strong | Y |  |  | Y | 2 |  |
| IT Technician (Help Desk - Linux Focus) | **28** | 8 | p>strong | Y |  | Y |  | 2 | 🚩 longest posting (28 blocks); abnormally large pre-compensation body |
| Lead Staff Electrical Engineer (F10 Program) | 14 | 4 | p>strong | Y |  | Y | Y | 2 |  |
| Manager, Logistics | 11 | 4 | p>strong | Y |  |  | Y | 1 | 🚩 inline `style="min-height:1.2em;margin-top:0;margin-bottom:0"` overrides spacing |
| Manager, Technical Support | 11 | 3 | p>strong | Y |  |  |  |  |  |
| Manufacturing Quality Supervisor | 8 | 3 | p>strong | Y |  |  | Y | 1 |  |
| Mission Success Operations Manager | 12 | 4 | p>strong | Y |  |  |  |  |  |
| PCB Layout Engineer | 8 | 2 | p>strong | Y |  | Y | Y |  | 🚩 no `impact` heading |
| PhD Autonomy Engineer Intern - Deep Learning or Computer Vision | 5 | 1 | p>strong | Y |  | Y | Y |  | 🚩 very short |
| PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) | 11 | 4 | **h3 + p>strong** | Y |  |  | Y |  | 🚩 mixed heading styles within posting |
| Product Design Engineer (All Levels) | 11 | 3 | p>strong | Y |  | Y | Y |  |  |
| Product Support Engineer | 9 | 3 | p>strong | Y |  |  | Y | 2 |  |
| Product Support Engineer Intern | 13 | 3 | p>strong | Y |  |  | Y | 3 |  |
| Production Manager, PM Shift | 11 | 3 | p>strong | Y |  | Y |  | 1 |  |
| Production Supervisor | 8 | 2 | p>strong | Y |  | Y |  |  | 🚩 no `impact` heading |
| Program Manager, Major Deployments (Hawaii) | 12 | 4 | p>strong | Y |  |  | Y | 2 |  |
| Program Manager, Major Deployments (Mid Atlantic) | 13 | 4 | p>strong | Y |  |  | Y | 3 |  |
| Program Manager, Major Deployments (South East) | 13 | 4 | p>strong | Y |  |  | Y | 3 |  |
| RF Design Engineer | 10 | 4 | p>strong | Y |  | Y |  |  |  |
| Revenue Operations Engineer, Quoting Systems | 16 | 6 | **h2 + p>strong** | Y |  |  |  | 2 | 🚩 mixed heading styles within posting |
| Sales Planning Analyst Intern | 9 | 3 | p>strong | Y |  | Y |  | 1 |  |
| Senior Autonomy Engineer - Controls | 9 | 3 | p>strong | Y |  |  | Y |  |  |
| Senior Autonomy Engineer - Deep Learning (San Mateo) | 9 | 3 | p>strong | Y |  | Y | Y |  |  |
| Senior Autonomy Engineer - Deep Learning (Zurich) | 9 | 3 | p>strong | Y |  | Y | Y | 1 |  |
| Senior Brand Designer (Contract) | 14 | 5 | p>strong | Y |  |  | Y | 3 |  |
| Senior Business Operations Manager | 12 | 6 | **h3 + p>strong** | Y |  |  | Y |  | 🚩 mixed heading styles within posting |
| Senior Buyer | 14 | 3 | **h2 + p>strong** | Y |  |  |  | 3 | 🚩 mixed heading styles within posting; many empty paragraphs |
| Senior Customer Support Representative - India | 9 | 2 | p>strong | Y |  |  | Y | 1 | 🚩 no `fit` heading |
| Senior Director, Product Management, Drone as First Responder (DFR) | 8 | 2 | p>strong | Y |  |  | Y |  | 🚩 no `impact` heading |
| Senior Hardware Test and Reliability Engineer | 10 | 3 | p>strong | Y |  |  |  |  |  |
| Senior NPI Product Quality Engineer | 9 | 3 | p>strong | Y | Y |  | Y |  | 🚩 italics |
| Senior People Analytics Analyst | 14 | 4 | p>strong | Y |  |  |  | 2 | 🚩 **typo:** "What Makes Your a Good Fit:" |
| Senior Product Manager, Platform & Infrastructure | 16 | 5 | p>strong | Y |  |  |  | 6 | 🚩 **6** empty paragraphs |
| Senior Revenue Operations Manager | 10 | 4 | p>strong | Y |  |  |  | 2 |  |
| Senior Software Engineer - Embedded | 10 | 4 | p>strong | Y |  | Y |  |  |  |
| Senior Software Engineer - Mobile Platform | 13 | 4 | p>strong | Y |  |  |  | 3 |  |
| Senior Software Engineer - Security | 12 | 4 | p>strong | Y |  |  | Y |  |  |
| Senior Software Engineer, Data Platform | 9 | 2 | p>strong | Y |  | Y |  | 1 | 🚩 no `fit` heading |
| Senior Software Engineer, Frontend | 10 | 3 | p>strong | Y |  |  |  |  |  |
| Senior Software Engineer, Full Stack | 10 | 2 | p>strong | Y |  |  |  |  | 🚩 no `fit` heading |
| Senior Software Engineer,  Infrastructure | 11 | 3 | p>strong | Y |  | Y |  |  | 🚩 double space in title |
| Senior Technical Recruiter | 12 | 4 | p>strong | Y |  | Y |  | 1 |  |
| Senior Technical Recruiter - Hardware Operations | 12 | 3 | p>strong | Y |  | Y |  | 1 | 🚩 no `impact` heading |
| Senior Technical Support Representative - Japan | n/a | n/a | **h1** | Y |  |  | Y |  | 🚩 **uses `<h1>` for section headings; Compensation block missing** |
| Senior Wireless Systems Performance Engineer | 11 | 4 | p>strong | Y |  | Y |  |  |  |
| Senior/Staff Embedded Software Engineer – Camera Systems | 14 | 4 | p>strong | Y |  | Y | Y | 2 |  |
| Software Engineer - Autonomy Infrastructure, Systems and Tools (San Mateo) | 13 | 5 | **h2** | Y |  |  |  | 1 | 🚩 `<h2>` headings |
| Software Engineer - Autonomy Infrastructure, Systems and Tools (Zurich) | 13 | 5 | **h2** | Y |  |  |  | 1 | 🚩 `<h2>` headings |
| Software Engineer - Cloud Simulation & Full-Stack (San Mateo) | 12 | 5 | **h2** | Y |  |  |  | 2 | 🚩 `<h2>` headings |
| Software Engineer - Cloud Simulation & Full-Stack (Zurich) | 12 | 5 | **h2** | Y |  |  |  | 2 | 🚩 `<h2>` headings |
| Software Engineer - Embedded | 11 | 4 | p>strong | Y |  |  |  |  |  |
| Software Engineer - Infrastructure | 10 | 3 | p>strong | Y |  |  | Y |  |  |
| Software Engineer - Simulation & Robotics Engineer (San Mateo) | 12 | 5 | **h3** | Y |  |  |  | 2 | 🚩 `<h3>` headings |
| Software Engineer - Simulation & Robotics Engineer (Zurich) | 12 | 5 | **h3** | Y |  |  |  | 2 | 🚩 `<h3>` headings |
| Software Engineer Intern Fall 2026/Winter 2027 | 8 | 2 | p>strong | Y |  | Y |  | 1 | 🚩 no `impact` heading |
| Software Engineer, Full Stack | 10 | 3 | p>strong | Y |  |  |  |  |  |
| Sr/Staff Embedded Software Engineer - Camera Systems (Tampere) | 14 | 4 | p>strong | Y |  | Y | Y | 3 |  |
| Staff Global Supply Manager,  Mechanicals | 10 | 3 | p>strong | Y |  |  | Y | 1 | 🚩 double space in title |
| Staff Product Manager, Platform & Infrastructure | 16 | 5 | p>strong | Y |  |  |  | 6 | 🚩 **6** empty paragraphs |
| Staff Software Engineer - Embedded | 10 | 3 | p>strong | Y |  |  |  |  |  |
| Staff Software Engineer, Frontend | 10 | 3 | p>strong | Y |  |  |  |  |  |
| Staff Software Engineer, Full Stack | 10 | 2 | p>strong | Y |  |  |  |  | 🚩 no `fit` heading |
| Staff Technical Recruiter | 11 | 4 | p>strong | Y |  | Y |  |  |  |
| Success Systems Specialist | 19 | 5 | p>strong | Y |  |  | Y | 1 | 🚩 very long |
| Supplier Quality Engineer, Sustaining | n/a | n/a | p>strong | Y |  |  |  | 1 | 🚩 **Compensation block missing**; `#LI-BJ1` visible in body |
| Supply Chain Intern | 9 | 2 | p>strong | Y |  | Y | Y |  | 🚩 no `impact` heading |
| Systems Integration and Test Engineer (Mid to Senior Level) | 11 | 3 | p>strong | Y |  | Y |  |  | 🚩 no `fit` heading |
| Technical Support Specialist - West Coast | 10 | 3 | p>strong | Y |  | Y |  |  |  |
| Wireless Software Engineer | 11 | 4 | p>strong | Y |  | Y |  |  |  |
| Workplace Experience Coordinator Part-Time | n/a | n/a | p>strong | Y |  |  |  | 1 | 🚩 **Compensation block missing** |

(The 6 postings that surface as `n/a` use a non-canonical layout — either
missing the comp block entirely or styled with `<h1>`/`<h3>` such that
no canonical heading is detectable. They are all called out
individually elsewhere in this report.)

---

## 9. Recommendations — how to standardise

Ordered roughly by impact for editorial work; cheap wins first.

### A. Heading element & style guide (highest impact)

1. Decide on **one** heading element: recommend `<p><strong>{heading}:</strong></p>`
   (the existing dominant pattern in 87/107 postings). Update the 20
   deviating postings (`<h2>`, `<h3>`, `<h1>`) so all section headings
   render at the same font size and weight.
2. Decide on **one** case style for section headings: recommend
   **sentence case** (most common in the data) and stick to it.
3. Always end section headings with a colon ("**About the role:**",
   "**How you'll make an impact:**", "**What makes you a good fit:**").
4. Pick one apostrophe style (recommend a straight `'` since editors
   type that natively and copy/paste of the curly variant is the only
   way it leaks in). Most postings already use straight.
5. Lock down the canonical heading set:
   - About the role / About the team (when team-led)
   - How you'll make an impact (or What you'll do — pick one)
   - What makes you a good fit (or Qualifications — pick one)
   - (optional) Nice to have / Bonus points (pick one)
   - (optional) Location / Work Location, only when applicable
   …and retire the long tail of one-off variants ("Areas of
   Responsibility", "Bonus Experience", "What makes you a strong fit",
   "What makes this internship different", "Tech stack you'll work
   with", "Day-to-day responsibilities", etc.). At minimum, the
   "Cloud-Sim/Autonomy-Infra" cluster of six postings should be brought
   into line, since they share a non-standard `h2/h3` + "Areas of
   Responsibility / Bonus Experience" template.

### B. Body cleanup (low effort, high visible impact)

6. Strip empty `<p></p>` blocks from every posting (46 postings, up to
   6 empty paragraphs each). This is the single biggest source of
   uneven section spacing.
7. Remove the inline `style="min-height:1.2em;margin-top:0;margin-bottom:0"`
   on the *Manager, Logistics* paragraph and let the global stylesheet
   handle spacing.
8. Audit `<br>` usage. Replace within-paragraph `<br>` line breaks with
   real paragraph breaks where appropriate; the 42 postings that use
   `<br>` and the 65 that don't render with subtly different rhythms.
9. Replace italicized passages in *Director, Growth Marketing –
   Commercial*, *Senior NPI Product Quality Engineer*, and *Electric
   Motor / Propulsion Engineer* with regular paragraph styling unless
   italics are explicitly part of the style guide.

### C. Content/legal fixes (must-do)

10. Add a `Compensation:` block (with the `<strong>Compensation:</strong>`
    label) to the 5 postings that are missing it, plus standardise the
    *Full Stack Product Counsel* posting so "Compensation:" is bolded
    like everywhere else. CA-based postings missing comp are a pay
    transparency risk.
11. Remove the trailing `#LI-BJ1` internal recruiter source tag visible
    in the body of *Supplier Quality Engineer, Sustaining*. Several
    other postings carry these tags but they appear after the
    Compensation block (out of scope here); a quick scan for the
    pattern `#LI-` would be worth doing across the whole corpus.

### D. Title-bar cleanup

12. Fix the typo "**What Makes Your a Good Fit:**" → "What Makes You a
    Good Fit:" in *Senior People Analytics Analyst*.
13. Fix double-space titles:
    - "Staff Global Supply Manager,  Mechanicals" → "Staff Global Supply Manager, Mechanicals"
    - "Senior Software Engineer,  Infrastructure" → "Senior Software Engineer, Infrastructure"
14. Trim trailing whitespace in titles like "Autonomy Engineer - ML & DL Infrastructure ".
15. For the three EMEA "Enterprise Account Manager" postings, demote
    the bolded sentence "**This role must be based in Switzerland,
    Germany, or Finland.**" from looking like a section header to
    being plain body text (or move it into the body of *About the
    role*).

### E. "About Skydio" intro

16. Reset every posting's first paragraph to the canonical "About
    Skydio" boilerplate to give all postings the same opening rhythm.
    Only 6 / 107 currently match verbatim.
17. Decide whether postings should have **1** or **2** intro
    paragraphs before the first section header, and apply that uniformly.
    Currently it ranges from 0 to 5 intro paragraphs.

### F. Length normalisation

18. Audit the unusually long postings (28, 26, 19, 16, 16 pre-comp
    blocks — see §5) and decide whether their depth is justified or
    whether they can be trimmed to match the median ~9-block format.
19. Audit the unusually short postings (5 pre-comp blocks — typically
    just the intro plus one bullet list, missing the "fit" section).
    Several Autonomy Engineer postings are in this bucket and would
    benefit from a "What makes you a good fit" section like their
    peers.

### G. Process

20. Provide a single CMS template / Markdown snippet with the canonical
    structure and ask all recruiters to start from it. Move toward
    treating section headings as semantic constants (e.g. a "section
    heading" component in the CMS) so editors can't accidentally
    swap `<p><strong>` for `<h2>`.

---

## 10. Appendix — confidence & known caveats

- All measurements come from the server-rendered HTML of each detail
  page. The page does run client-side JavaScript on top, but
  spot-checking confirms the description body is rendered server-side
  and not mutated by JS, so the parsed DOM matches what the user sees.
- "Font size" and "line spacing" cannot be measured directly from
  static HTML without running a browser. They are inferred from the
  HTML element used (`<h2>` vs `<h3>` vs `<p><strong>` vs `<h1>`) and
  from inline `style` attributes; both are accurate proxies because
  the site uses a single global stylesheet driving the `prose` class.
- The classification of each section heading into role / impact / fit /
  nice categories uses a fixed synonym list; a handful of one-off
  headings ("Strategic Sourcing", "Tech stack you'll work with",
  "Reporting & Working Model", "What Success Looks Like", "Day-to-day
  responsibilities", etc.) are intentionally left in the "unclassified"
  bucket and flagged as outliers — they are exactly the kind of
  divergence the report is meant to surface.
- The 6 postings flagged as "no Compensation block parsed" are split
  into two groups: 5 are genuinely missing the block and 1 (Full Stack
  Product Counsel) has the block but not in the canonical `<strong>`
  form, so the automated detector missed it. Both groups are real
  inconsistencies and both are listed in §6.

# Skydio Careers — Job Posting Formatting Audit

**Scope:** All 114 jobs currently published on https://www.skydio.com/careers
**Section analyzed:** Everything in each posting from the company boilerplate
through the last bullet *before* the `Compensation:` block (compensation,
equity, EEO, E-Verify, and `#LI-*` tags are intentionally excluded).
**Source data:** Ashby Posting API
(`https://api.ashbyhq.com/posting-api/job-board/skydio?includeCompensation=true`)
— this is the same payload the careers page renders client-side, so what you
see here is exactly what the team is publishing.
**How to reproduce:** `python3 analyze.py` (writes `per_job_findings.csv`).

---

## TL;DR

> Skydio's job postings render in the same Ashby template, so **font family,
> base font size, color, and alignment are visually identical across all 114
> roles**. The real inconsistencies are structural — *which HTML elements* the
> writers chose for the same logical sections. Those choices change the
> rendered heading size, weight, spacing, and emphasis on a per-posting basis.

**Top issues, ranked by how often they show up:**

| # | Issue | Affected jobs |
|---|---|---|
| 1 | Section headings written 8 different ways (case, colon, wording) | 75 / 114 |
| 2 | Empty `<p></p>` used as a visual spacer between sections | 54 / 114 |
| 3 | `<br>` tags used for line breaks inside paragraphs | 48 / 114 |
| 4 | Straight `'` vs. curly `’` apostrophes inside section labels | mixed across postings |
| 5 | Section headings wrapped in `<h2>` or `<h3>` instead of bold `<p>` | 17 / 114 |
| 6 | Consecutive `<br><br>` (visible extra blank line) | 18 / 114 |
| 7 | `<u>` underlines used for `PLEASE NOTE:` callouts | 8 / 114 |
| 8 | `<em>` italics used for sub-headers / disclaimers | 3 / 114 |
| 9 | Job title strings with leading/trailing/double whitespace | 15 / 114 |
| 10 | `<h1>` used for section headers (one posting only) | 1 / 114 |
| 11 | Non-standard inline style (`min-height:1.2em;margin-top:0;margin-bottom:0`) | 1 / 114 |
| 12 | `<div>` wrapper inside the body (one posting only) | 1 / 114 |

The full per-job classification lives in
[`per_job_findings.csv`](./per_job_findings.csv).

---

## What's consistent (the baseline / "norm")

These behaviors hold for **100% of postings** and define what other postings
should match:

- **Font, color, weight, alignment, line-height** — fixed by the Ashby +
  Skydio CSS. No posting ever overrides them with inline `font-size`,
  `color`, or alignment styles (verified: 0 occurrences of `font-size:` or
  `color:` in any inline `style=` attribute).
- **Boilerplate intro paragraph** is byte-for-byte identical in all 114
  postings (`Skydio is the leading US drone company …`).
- **Every paragraph carries `style="min-height:1.5em"`** — *except* one
  outlier flagged below.
- **Lists are always `<ul><li><p style="min-height:1.5em">…</p></li></ul>`**
  (no `<ol>`, no nested lists).

So when this report talks about "font size" or "weight" issues, it means the
*element* changed (e.g. `<p>` → `<h2>`), which changes the rendered size
even though no one literally typed `font-size: 24px`.

---

## Issue 1 — Section heading **structure** (HTML element used)

Most postings have 3–5 section headings: *About the role*, *How you'll make
an impact*, *What makes you a good fit*. There are four different ways
postings author them today.

| Pattern | Count | Renders as |
|---|---|---|
| `<p><strong>About the role:</strong></p>` | **95 jobs** *(the norm)* | Body-size bold paragraph |
| `<h2>…</h2>` or `<h2><strong>…</strong></h2>` | 11 jobs | Large H2 (~1.5× body) |
| `<h3>…</h3>` or `<h3><strong>…</strong></h3>` | 6 jobs | Medium H3 (~1.2× body) |
| `<h1>…</h1>` | 1 job | Page-title size (~2× body) |
| Inline (no standalone section header at all — e.g. `<p><strong>About the role</strong>: text follows on the same line…</p>`) | 2 jobs | No visual section break |
| Mixed within the same posting (both `<h2>`/`<h3>` *and* `<p><strong>`) | 4 jobs | Two competing heading sizes in one posting |

**Specific outliers:**

- **`<h1>` outlier (renders much larger than every other posting):**
  - `Senior Technical Support Representative - Japan` *(Customer Support)*
- **`<h2>`-only postings (headings render visibly larger than 95 sibling postings):**
  - `Aviation Compliance Lead`, `Aviation Regulatory Program Manager`
    *(Policy & Regulatory Affairs)*
  - `Communications Manager` *(Marketing)*
  - `Revenue Operations Engineer, Quoting Systems` *(Sales)*
  - `Senior Buyer` *(Manufacturing)*
  - `Senior Wireless Software Engineer, National Security` *(Software, San Mateo + Boston)*
  - `Software Engineer - Autonomy Infrastructure, Systems and Tools` *(Autonomy, x2 locations)*
  - `Software Engineer - Cloud Simulation & Full-Stack` *(Autonomy, x2 locations)*
- **`<h3>`-only postings:**
  - `Full Stack Product Counsel` *(Legal)*
  - `Senior Business Operations Manager` *(Supply Chain & Logistics)*
  - `Software Engineer - Simulation & Robotics Engineer` *(Autonomy, x2)*
  - `PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning)`
    *(Autonomy)*
- **Mixed `<h2>` + `<h3>` within the same posting (two heading sizes):**
  - `Hardware Engineering Program Manager` *(Hardware)* uses `<h2>` for top
    sections and `<h3>` for sub-sections (Program Leadership / Cross-Functional
    / Supplier; Minimum / Preferred Qualifications) — this is the only posting
    that uses a true 2-level hierarchy.
- **Inline (no section headings at all):**
  - `Product Support Engineer`, `Product Support Engineer Intern`
    *(Customer Support)* — both write
    `<strong>About the role</strong>: …` on the same line as the description,
    so there is no visual heading break between the boilerplate and the role
    description.

**Bonus inconsistency:** even within the 17 heading-tag postings, some wrap
the heading text in `<strong>` and some don't:

- `<h2>What makes you a good fit</h2>` — no `<strong>` (renders bold via
  default browser styles)
- `<h2><strong>What you'll bring:</strong></h2>` — explicitly bolded
  (renders bold *and* bold-inside-bold; in some browsers this is identical,
  in others it's slightly heavier)

`Hardware Engineering Program Manager` is the only posting that does both in
the same document (`<h2><strong>About the role</strong></h2>` then
`<h2>How you'll make an impact</h2>`).

---

## Issue 2 — Section heading **text** (case, colon, wording)

For the *same logical section*, the literal text varies. Search counts across
the 114 postings:

**"About the role" variants:**

| Text | # of jobs |
|---|---|
| `About the role:` | 68 |
| `About the Role:` | 32 |
| `About the Role` *(no colon)* | 6 |
| `About the role` *(no colon)* | 5 |
| `About the Team:` | 8 |
| `About the team:` | 7 |
| `About the Team` / `About the team` | 1 / 1 |

That's **8 different spellings of one section title**.

**"How you'll make an impact" variants:**

| Text | # of jobs |
|---|---|
| `How you'll make an impact:` *(straight apostrophe, lowercase, colon)* | 37 |
| `How You'll Make an Impact:` *(title case, curly apostrophe)* | 20 |
| `How you'll make an impact:` *(curly apostrophe, lowercase)* | 15 |
| `How You'll Make an Impact` *(no colon)* | 3 |
| `How you will make an impact:` *("will" expanded)* | 4 |

**"What makes you a good fit" variants:**

| Text | # of jobs |
|---|---|
| `What makes you a good fit:` | 54 |
| `What Makes You a Good Fit:` | 17 |
| `What would make you a good fit:` | 7 |
| `What makes you a strong fit:` | 6 |
| `What makes you a good fit` *(no colon)* | 4 |
| `What Makes You a Good Fit` *(no colon)* | 3 |

**Apostrophe style:** 56 postings use the ASCII `'` and 30 use the
typographic `’` (a handful mix both in the same posting). This is invisible
in some fonts but causes copy-paste / search-grep mismatches.

---

## Issue 3 — Vertical spacing: empty paragraphs and `<br>` tags

The Ashby editor adds an empty `<p></p>` whenever an author hits *Enter*
twice. The canonical postings don't do this; 54 postings do, which produces
an extra blank line that's ~1× line-height taller than the equivalent gap
in the other 60 postings.

**`<br>` usage** is the larger spacing problem:

- 48 / 114 postings use one or more `<br>` tags inside paragraphs to force
  manual line breaks. The norm is to start a new `<p>`. Because Ashby gives
  `<p>` a `min-height:1.5em` and `<br>` doesn't, the two render different
  vertical rhythm even when they're visually similar.
- 18 of those postings have **consecutive `<br><br>`** which renders as an
  obvious extra-tall blank line:
  - `IT Technician (Help Desk - Linux Focus)` — 9 `<br>` tags total
  - `Autonomy Engineer - Deep Learning Infrastructure` — 8 (x2 locations)
  - `Director, Growth Marketing - Commercial` — 8
  - `Autonomy Engineer - Deep Learning Model Acceleration` — 6 (x2)
  - `GTM Engineer, Pre-Sales` — 6
  - `Director of Product Management, DFR` — 4
  - `Senior Technical Recruiter - Hardware Operations` — 4
  - `Autonomy Software Engineer` — 4
  - `Software Engineer Intern Fall 2026/Winter 2027` — 4
  - `Revenue Operations Engineer, Quoting Systems` — 4
  - `GTM Data Engineer Intern` — 3
  - `Senior Autonomy Engineer - Deep Learning` — 3 (one location), 2 (other)
  - plus several more with 1–2 `<br>` runs (see CSV)

---

## Issue 4 — Inline emphasis (underline / italic)

The canonical postings use **bold** (`<strong>`) for any in-paragraph
emphasis. A small number of postings reach for other tags and stand out
visually because of it.

**Underline (`<u>`) — 8 postings**, almost always for `PLEASE NOTE:`
disclaimers about hybrid / location requirements:

- `Staff Technical Recruiter`, `Senior Technical Recruiter`,
  `Senior Technical Recruiter - Hardware Operations` *(People & Recruiting)*
- `Senior Software Engineer, Full Stack` *(Software)*
- `Full Stack Product Counsel` *(Legal)*
- `Senior NPI Product Quality Engineer` *(Manufacturing)*
- `Lead Staff Electrical Engineer` *(Hardware)*
- `Public Safety Strategist` *(Sales)*

The other 106 postings either bold the same disclaimer or omit it. The
underline makes those 8 postings look like they have a hyperlink that
isn't clickable, which is a real accessibility issue.

**Italic (`<em>`) — 3 postings:**

- `GTM Engineer, Pre-Sales` *(Sales)* — uses italics as *sub-headers* inside
  bullet sections (e.g. *Find the right problems to solve*, *Build things that
  scale*, *Drive adoption, not just delivery*, *You understand how GTM teams
  work*, *You're a builder with AI fluency*, *You build for scale, not just
  for now*, *You've got the right instincts*). This gives the posting a
  three-level structural hierarchy (heading → italic sub-header → bullet)
  that no other posting has.
- `Director, Growth Marketing - Commercial` *(Marketing)* — 1 italic phrase.
- `Senior NPI Product Quality Engineer` *(Manufacturing)* — 1 italic phrase
  ("Obtaining FAA Part 107 certification within the first 60 days …").

---

## Issue 5 — One-off structural outliers

- **`Manager, Logistics` *(Manufacturing)*** is the only posting in the
  catalog with:
  1. A `<div>` wrapper inside the body (every other posting uses only
     `<p>`, `<ul>`, `<li>`, `<strong>`, `<a>`, `<u>`, `<em>`, `<h*>`, `<br>`).
  2. A paragraph carrying the non-standard inline style
     `min-height:1.2em;margin-top:0;margin-bottom:0` instead of the
     canonical `min-height:1.5em`. That paragraph renders ~20% tighter
     vertically than every other paragraph on the page.

- **`Senior Technical Support Representative - Japan`** is the only posting
  using `<h1>` for section headers. On the live site `<h1>` is reserved for
  the page title ("Senior Technical Support Representative - Japan"), so
  this posting renders three additional page-title-sized headings inside
  the body.

---

## Issue 6 — Job title strings (the listings index)

The role titles shown on the careers index have whitespace bugs in 15
listings. These render as visible extra spacing (or kerning oddities,
depending on the font) on the index page and inside the H1 of each
posting:

| Title (as published) | Team | Issue |
|---|---|---|
| `Electrical Engineer (all levels) ` | Hardware | trailing space |
| `Senior Software Engineer - Embedded ` | Software | trailing space |
| `Senior Software Engineer,  Data Platform ` | Software | double space + trailing |
| `Staff Global Supply Manager,  Mechanicals` | Supply Chain & Logistics | double space |
| `Autonomy Engineer - ML & DL Infrastructure ` *(both locations)* | Autonomy | trailing space |
| `Senior Autonomy Engineer - Controls ` | Autonomy | trailing space |
| ` Electrical Engineer (Sustaining/Validation)` | Hardware | leading space |
| ` Senior Software Engineer,  Infrastructure` | Software | leading space + double space |
| `Success Systems Specialist ` | Professional Services and Training | trailing space |
| `Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM` | Sales | double space |
| `Senior Software Engineer - Mobile Platform ` | Software | trailing space |
| ` Software Engineer - Infrastructure` | Software | leading space |
| `Field Support Representative ` | Customer Support | trailing space |
| `Manager, Logistics ` | Manufacturing | trailing space |

These are pre-compensation surface-level visual defects on the index page
and the posting `<h1>`.

---

## Per-posting outlier list (quick triage)

The 12 postings that depart from the norm in the most ways — these should
be reformatted first:

1. **`Hardware Engineering Program Manager` *(Hardware)*** — mixed `<h2>`
   + `<h3>` two-level hierarchy unique to this posting; `<h2>` heading
   text inconsistently wrapped in `<strong>` (one is, the other isn't).
2. **`Senior Technical Support Representative - Japan` *(Customer Support)*** —
   only posting that uses `<h1>`; also uses `<br>` for spacing.
3. **`GTM Engineer, Pre-Sales` *(Sales)*** — only posting using `<em>` as
   sub-headers (8 occurrences); also 6 `<br>` tags.
4. **`Manager, Logistics` *(Manufacturing)*** — only posting with a `<div>`
   and a non-standard paragraph inline style; also has a trailing-space
   title.
5. **`Full Stack Product Counsel` *(Legal)*** — `<h3>` instead of `<p><strong>`;
   uses Title Case section headers; uses `<u>`.
6. **`Senior NPI Product Quality Engineer` *(Manufacturing)*** — uses both
   `<u>` and `<em>` (other postings use neither).
7. **`Senior Wireless Software Engineer, National Security` *(Software, x2
   locations)*** — 6 `<h2>` headings, more than any other posting.
8. **`Director, Growth Marketing - Commercial` *(Marketing)*** — 8 `<br>`
   tags and an italic phrase.
9. **`IT Technician (Help Desk - Linux Focus)` *(IT)*** — 9 `<br>` tags
   (most in catalog) + Title Case section headers.
10. **`Software Engineer - Autonomy Infrastructure, Systems and Tools`** and
    **`Software Engineer - Cloud Simulation & Full-Stack`** *(Autonomy, x2
    locations each — 4 postings)* — all 4 use `<h2>` for sections and Title
    Case + colon section labels.
11. **`Product Support Engineer` / `Product Support Engineer Intern`
    *(Customer Support)*** — no standalone section headings at all
    (sections are run-on with descriptions on the same `<p>`).
12. **`Revenue Operations Engineer, Quoting Systems` *(Sales)*** — 5 `<h2>`
    section headers plus a leftover `<p><strong>About the Role:</strong></p>`
    above them (mixed mode).

---

## Recommendations for standardization

Concrete, ordered by impact / cost:

1. **Adopt a single canonical posting template** in Ashby. Based on what
   the majority already does:

   ```html
   <p style="min-height:1.5em">[Skydio boilerplate paragraph]</p>
   <p style="min-height:1.5em"><strong>About the role:</strong></p>
   <p style="min-height:1.5em">…</p>
   <p style="min-height:1.5em"><strong>How you'll make an impact:</strong></p>
   <ul style="min-height:1.5em"><li><p style="min-height:1.5em">…</p></li>…</ul>
   <p style="min-height:1.5em"><strong>What makes you a good fit:</strong></p>
   <ul style="min-height:1.5em"><li><p style="min-height:1.5em">…</p></li>…</ul>
   <p style="min-height:1.5em"><strong>Compensation:</strong> …</p>
   ```

   Specifically fix:
   - **Heading element** — always `<p><strong>…</strong></p>`. Do not use
     `<h1>`, `<h2>`, or `<h3>` in the posting body (reserve them for the
     page title and the Skydio site chrome).
   - **Heading text** — sentence case + trailing colon: `About the role:`,
     `How you'll make an impact:`, `What makes you a good fit:`.
   - **Apostrophe** — pick one and lint for it. Curly `’` matches the
     plurality of Skydio's marketing copy; straight `'` matches the
     plurality of the postings. Either is fine; pick one.

2. **Stop using `<br>` and empty `<p></p>` for spacing.** Vertical rhythm
   should come from `<p>` boundaries only. Recruiters typing into Ashby
   should be told: hit *Enter once* between paragraphs, never hit *Enter*
   twice and never use Shift-Enter.

3. **Replace `<u>` with `<strong>` for `PLEASE NOTE:` callouts.** Underline
   reads as a broken hyperlink and fails WCAG 1.4.1 (use of color/style
   alone). Bold matches every other location callout in the catalog.

4. **Decide whether sub-headers inside sections are allowed.** Today exactly
   two postings have them:
   - `Hardware Engineering Program Manager` does it with `<h3>`.
   - `GTM Engineer, Pre-Sales` does it with `<em>`.

   If long postings are allowed sub-headers, standardize on
   `<p><em>Sub-section name</em></p>` (or `<p><strong><em>…</em></strong></p>`)
   and document it. Otherwise, flatten those two postings into a single
   bullet list to match the norm.

5. **Fix the 15 title-whitespace bugs** as a one-time cleanup pass — they
   are 30-second edits per posting in Ashby.

6. **Rewrite the four "mixed" postings** to use a single heading style
   throughout, and the two "inline" postings (`Product Support Engineer`
   and `Product Support Engineer Intern`) so that "About the role:" sits
   on its own line above the description, like the rest of the catalog.

7. **Wire a lint into the publishing flow.** A 30-line script (see
   `analyze.py`) can fail the publish step whenever a posting:
   - contains `<h1>`/`<h2>`/`<h3>`/`<h4>`/`<div>` in the body,
   - contains a `style=` attribute other than `min-height:1.5em`,
   - contains `<u>`, `<em>`, or `<br>`,
   - contains an empty `<p></p>`,
   - has a title with leading, trailing, or double whitespace,
   - or uses a section-heading label not in the approved allow-list.

   With those checks in place the catalog stays consistent without
   requiring human review of every new posting.

---

## Appendix — Methodology notes

- "Norm" in this report = the modal pattern (most-common across 114 jobs).
  It's *not* a Skydio-blessed style guide; the team should treat the
  recommendations above as a *proposal* for what the norm should formally
  be.
- The Ashby API returns sanitized HTML produced by Ashby's WYSIWYG editor.
  The editor strips arbitrary CSS, which is why no posting ever has a
  hard-coded `color:` or `font-size:` value — the visual differences come
  from the *element* the author chose. This means standardization is a
  process / template question, not a CSS engineering question.
- Per-job machine-readable data: [`per_job_findings.csv`](./per_job_findings.csv).
- Re-run the audit: `python3 analyze.py` (no external dependencies; uses
  only the Python standard library).

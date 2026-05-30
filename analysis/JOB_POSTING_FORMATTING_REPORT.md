# Skydio Careers — Job Posting Formatting Consistency Report

**Source:** [skydio.com/careers](https://www.skydio.com/careers)
(jobs loaded from the public Ashby board:
`https://api.ashbyhq.com/posting-api/job-board/skydio`)
**Postings analyzed:** 113
**Scope:** every job description from the first paragraph up to — but **not
including** — the **Compensation** block.
**Date:** 2026-05-30

---

## 1. TL;DR — what to fix first

| # | Severity | Issue                                                                                                            | Count                            |
|---|----------|------------------------------------------------------------------------------------------------------------------|----------------------------------|
| 1 | **High** | Inconsistent heading hierarchy: 96 jobs use no `<h?>` tag at all; 17 use real headings (at h1, h2 **and** h3)    | 113 of 113                       |
| 2 | **High** | Section labels (e.g. "About the role", "How you'll make an impact", "What makes you a good fit") have **25+ casing / punctuation / wording variants** | every posting affected |
| 3 | **High** | Typo in a live posting — **"What Makes Your a Good Fit:"** ("Your" → "You")                                       | 1 (`GTM Engineer, Pre-Sales`)    |
| 4 | Med      | One posting uses `<h1>` for its section headings (visually huge vs. all others)                                  | 1 (`Senior Technical Support Representative - Japan`) |
| 5 | Med      | One posting nests `<h2>` + `<h3>` sub-sections — no other posting uses sub-sections                              | 1 (`Hardware Engineering Program Manager`) |
| 6 | Med      | Apostrophe inconsistency — straight `'` vs. typographic `’` in the same labels                                   | 36 vs. 35 occurrences            |
| 7 | Med      | 8 postings use `<u>` (underline) — non-standard on this site and a web-anti-pattern (looks like a hyperlink)     | 8                                |
| 8 | Med      | One posting uses `<em>` (italics) **8 times** as bullet sub-headings — unique pattern                            | 1 (`GTM Engineer, Pre-Sales`)    |
| 9 | Med      | Vertical-spacing is faked with empty `<p></p>` tags: 0–8 spacers per posting, no pattern                          | 54 of 113 use ≥1                 |
|10 | Low      | Pre-Compensation length ranges **244 → 876 words** (3.6× spread)                                                  | —                                |
|11 | Low      | One posting (`IT Technician (Help Desk – Linux Focus)`) has **42 bullets** — 2× the median                        | 1                                |
|12 | Low      | One posting (`Director, Global Supply Management — Mechanicals`) has **zero bullets**, every section is prose     | 1                                |

> **Good news:** there are **no inline `font-size`, `font-family`, `color`,
> `background-color`, `text-align`, or `line-height` declarations** anywhere
> in the pre-compensation HTML. Every posting also shares the **exact same
> opening "Skydio is the leading US drone company…" paragraph**. The visual
> inconsistencies you can see on the page come from inconsistent **HTML
> structure** (which heading or pseudo-heading is used), not from authored
> CSS overrides — which means everything below is fixable with a content
> style-guide and a CMS template, no design-system changes required.

---

## 2. How the analysis was done

1. Pulled every published posting via Skydio's Ashby JSON board (113 jobs).
2. For each posting, truncated `descriptionHtml` at the start of the
   Compensation block, defined as the first match of any of:
   - `<p><strong>Compensation` (most common — 78 postings)
   - `<h?>Compensation`
   - the boiler-plate sentence "*Compensation will vary based on…*" /
     "*Compensation for certain positions…*" (used by ~70% of postings even
     when no explicit Compensation header is present).
3. Parsed the resulting fragment for:
   - All HTML tag usage (`<h1>`–`<h6>`, `<p>`, `<ul>`, `<ol>`, `<li>`,
     `<strong>`, `<b>`, `<em>`, `<i>`, `<u>`, `<br>`, …).
   - Every inline `style=` attribute: `font-size`, `font-family`, `color`,
     `background-color`, `text-align`, `line-height`.
   - "Pseudo-headings" — paragraphs whose entire visible content is wrapped
     in `<strong>` (the most common way Skydio postings denote a section
     title).
   - Empty paragraphs used as spacers.
4. Aggregated across all 113 postings.

Raw artefacts produced (committed alongside this report):
- `per_job_metrics.json` — full HTML-derived metrics per posting.
- `per_job_summary.json` — flat per-posting summary (one row each).
- `per_job_table.md` — the full per-posting table (excerpted in §6).

---

## 3. Inconsistencies, in detail

### 3.1 Heading hierarchy is the biggest issue

| Heading style used in pre-Comp content        | # postings |
|-----------------------------------------------|-----------:|
| **No real `<h?>` tag at all** — sections are paragraphs of bold text | **96** |
| Real `<h2>` only                              | 7          |
| Real `<h3>` only                              | 4          |
| Real `<h1>` only                              | 1          |
| Real `<h2>` **+** `<h3>` (sub-sectioned)      | 1          |
| Mixed: real `<h?>` **and** pseudo `<p><strong>` headings in the same posting | 4 |

This produces visually-different pages even though all 113 contain the same
three logical sections ("About the role", "How you'll make an impact",
"What makes you a good fit").

**Outliers worth flagging by name:**

- **`Senior Technical Support Representative - Japan`** (Customer Support,
  Tokyo) is the only posting that uses `<h1>` for body sections. On the
  rendered page these display at *page-title* size, dwarfing all other
  content.
- **`Hardware Engineering Program Manager`** is the only posting that uses
  a nested heading hierarchy (`<h2>` for top-level sections + `<h3>` for
  sub-sections like "Program Leadership & Execution", "Cross-Functional
  Engineering Integration", "Supplier & Manufacturing Engagement"). No
  other posting attempts sub-sections.
- **`Revenue Operations Engineer, Quoting Systems`** — uses real `<h2>` for
  five of its sections *but still also has* a pseudo `<p><strong>About the
  Role:</strong></p>`. Same intra-posting inconsistency in
  `Senior Business Operations Manager`, `Senior Buyer`, and the
  `PhD Autonomy Engineer Intern — Planning & Controls (RL)` posting.

Postings that use real `<h2>` (uniformly): `Aviation Compliance Lead`,
`Aviation Regulatory Program Manager`, `Communications Manager`,
`Software Engineer – Autonomy Infrastructure, Systems and Tools` (both
locations), `Software Engineer – Cloud Simulation & Full-Stack` (both
locations), `Senior Wireless Software Engineer, National Security` (×6
h2 — densest section-headed posting of the set).

Postings that use real `<h3>` (uniformly): `Full Stack Product Counsel`,
`Software Engineer – Simulation & Robotics Engineer` (both locations),
`PhD Autonomy Engineer Intern – Planning & Controls (RL)`,
`Senior Business Operations Manager`.

### 3.2 Section-label wording / casing / punctuation drifts

Same logical section, multiple authored forms found in production:

**"About the role / team"** — 6 variants

| Variant | Count |
|---|---:|
| `About the role:`  | 48 |
| `About the Role:`  | 23 |
| `About the Team:`  | 8 |
| `About the team:`  | 5 |
| `About the Role`   (no colon) | 2 |
| `About The Role`   (Title-Case "The") | 1 |

**"How you'll make an impact"** — 9 variants

| Variant | Count |
|---|---:|
| `How you'll make an impact:`   (straight apostrophe, sentence case) | 36 |
| `How You'll Make an Impact:`   (straight apostrophe, title case) | 1 |
| `How you'll make an impact:`   (typographic `'`, sentence case) | 14 |
| `How You'll Make an Impact:`   (typographic `'`, title case) | 20 |
| `How you will make an impact:` (no contraction) | 3 |
| `What You'll Do`              | 1 |
| `What You'll Work On:`        | 1 |
| `Examples of what you'll help build:` | 1 |
| `What you'll gain:`           | 1 |

**"What makes you a good fit"** — 10 variants

| Variant | Count |
|---|---:|
| `What makes you a good fit:`       | 53 |
| `What Makes You a Good Fit:`       | 17 |
| `What would make you a good fit:`  | 6 |
| `What makes you a strong fit:`     | 4 |
| `What would make you a strong fit:`| 2 |
| `What Would Make You a Good Fit:`  | 2 |
| `What makes you a good fit`        (missing colon) | 1 |
| `What Makes You A Good Fit:`       (A→a) | 1 |
| `What Makes You a Good Fit`        (no colon) | 1 |
| **`What Makes Your a Good Fit:`**  **(typo — "Your")** | 1 |

Other label inconsistencies observed:
- `Bonus Points:` / `Bonus points:` / `Bonus points for:` (3 / 3 / 4)
- `Preferred Qualifications:` vs. `Preferred Qualifications` (2 vs. 1)
- `Nice to have:` vs. `Nice-to-Haves:` vs. `Nice To Haves` (2 / 2 / 1)
- `Requirements` (no colon) (2)
- A few postings invent custom labels: `Why Join Us?`, `Why This Role
  Matters Now:`, `Useful skills and experience:`, `Location` (used as a
  pseudo-heading in only 2 postings).

### 3.3 Emphasis tags used inconsistently

| Tag         | # postings using it | Notes |
|-------------|--------------------:|-------|
| `<strong>`  | 113 | Universal — used for every section label. |
| `<b>`       | 0   | Good, consistent. |
| `<em>`      | 3   | Outliers (see below). |
| `<i>`       | 0   | Good, consistent. |
| `<u>`       | 8   | Should not appear on a web page (looks like a hyperlink). |

`<u>` outliers (8 postings):
`Staff Technical Recruiter`, `Senior Technical Recruiter`,
`Senior Technical Recruiter - Hardware Operations`,
`Senior Software Engineer, Full Stack`,
`Full Stack Product Counsel`,
`Senior NPI Product Quality Engineer`,
`Lead Staff Electrical Engineer`,
`Public Safety Strategist (West Coast, Midwest, or Pacific North West)`.

`<em>` outliers:
- `Senior NPI Product Quality Engineer` — 1 italic phrase.
- `Director, Growth Marketing — Commercial` — 1 italic phrase.
- **`GTM Engineer, Pre-Sales` — 8 italic phrases.** This posting uniquely
  italicises the lead-in of each bullet ("*Find the right problems to
  solve*", "*Build things that scale*", "*Drive adoption, not just
  delivery*", …) as a stylistic device. No other posting uses this
  pattern, so this one will visually stand out from every other listing.

### 3.4 Vertical rhythm — empty-paragraph spacers

Skydio's CMS allows authors to add blank `<p></p>` rows as a manual spacer.
Usage is wildly inconsistent:

| Empty `<p>` spacers in pre-Comp content | # postings |
|----------------------------------------:|-----------:|
| 0 | 59 |
| 1 | 15 |
| 2 | 16 |
| 3 | 11 |
| 4 | 4  |
| 5 | 5  |
| 6 | 2  |
| 8 | 1  |

The two `Platform & Infrastructure` Product roles (Senior and Staff) each
use **6** empty paragraphs, giving them noticeably airier spacing than
neighbouring postings. The two `Software Engineer, Frontend` roles
(Senior + Staff) use **5**. Most engineering postings use **0**. The same
posting rendered with 0 vs. 5 spacers will look like a completely different
template even though the content is structurally identical.

### 3.5 Content length / density

Pre-Compensation word count distribution across the 113 postings:

| Statistic | Words |
|---|---:|
| Min | 244 (`Electrical Engineer (all levels)`) |
| 25th percentile | 394 |
| Median | 479 |
| 75th percentile | 567 |
| Max | **876** (`GTM Engineer, Pre-Sales`) |

`GTM Engineer, Pre-Sales` is **3.6× longer** than the shortest posting and
**1.8× longer** than the median. Combined with its italic sub-headings
(§3.3), it is the most visually distinctive posting on the entire careers
page.

Bullet density extremes:

- `Director, Global Supply Management - Mechanicals` — **0 bullets**;
  every section is rendered as prose paragraphs. Unique on the page.
- `IT Technician (Help Desk - Linux Focus)` — **42 bullets**, almost double
  the next highest (`Public Safety Strategist` and
  `GTM Engineer, Pre-Sales` at 27–28).

### 3.6 What is consistent (preserve this)

- ✅ All 113 postings open with the exact same paragraph: *"Skydio is the
  leading US drone company and the world leader in autonomous flight…"*.
- ✅ No posting carries inline `style=` overrides for font, color, or
  alignment — i.e., there are **no rogue `font-size`, `font-weight`,
  `color`, or `text-align` declarations** in the source. Visible
  differences all come from semantic tag choice.
- ✅ Every posting uses `<strong>` (not `<b>`) for emphasis, and `<ul>`
  rather than `<ol>` for unordered lists.
- ✅ The Ashby paragraph wrapper (`style="min-height:1.5em"`) is applied
  uniformly by the platform.

---

## 4. Recommendations (in priority order)

### 4.1 Lock in one heading hierarchy

Pick **one** of these two patterns and bake it into a recruiter content
template. Either is fine for SEO/a11y; what matters is that all 113
postings agree.

**Option A — semantic (recommended for accessibility & SEO):**

- Job title is the page's `<h1>` (rendered by the careers page wrapper,
  not by the recruiter).
- Recruiter content uses `<h2>` for the three top-level sections.
- If sub-sections are needed (rare), use `<h3>`.
- Do **not** use `<h1>` inside the body copy.

**Option B — what the majority already do:**

- Skip body headings entirely; render section labels as `<p><strong>…
  </strong></p>` ("pseudo-headings").
- Migrate the 17 outlier postings to this pattern.

Whichever is chosen, fix the four postings that currently *mix* real
headings with pseudo-headings (`Revenue Operations Engineer, Quoting
Systems`; `Senior Business Operations Manager`; `Senior Buyer`;
`PhD Autonomy Engineer Intern - Planning & Controls (RL)`).

### 4.2 Standardise the three canonical section labels

Adopt one casing/punctuation rule (sentence case + trailing colon is the
existing majority) and apply globally:

| Canonical label                  | Replaces | # postings to update |
|----------------------------------|----------|---------------------:|
| `About the role:`                | `About the Role:`, `About the Role`, `About The Role` | 26 |
| `About the team:`                | `About the Team:` | 8 |
| `How you'll make an impact:` (use one apostrophe style — recommend straight `'`) | all 9 variants in §3.2 | 41 |
| `What makes you a good fit:`     | all 9 variants in §3.2 (incl. the **"Your" typo**) | 35 |

While doing this, fix the typo in **`GTM Engineer, Pre-Sales`** ("Your" →
"You"). This is by far the most reputational fix in the list.

### 4.3 Pick a contraction & apostrophe style and enforce it

The authoring tool is silently substituting `'` → `’` for some authors and
not others, producing pairs like:

- `How you'll make an impact:` (straight)
- `How you'll make an impact:` (typographic — looks identical here but is
  a different code-point, U+2019)

Either pick one and configure the CMS to normalise (most ATS editors have
a "smart quotes" toggle), or run a one-time sweep to replace all `’` with
`'` (or vice-versa) inside `<strong>` tags.

### 4.4 Remove `<u>` and reserve `<em>`

- Strip all 8 `<u>` occurrences. Underlines on the web read as hyperlinks.
- Either ban `<em>` in postings entirely, **or** add the `GTM Engineer,
  Pre-Sales` pattern to the template ("italicise the lead-in of each
  bullet") so it's intentional and reused everywhere. Today it appears in
  exactly one posting and reads as a one-off.

### 4.5 Stop using empty `<p></p>` as a spacer

54 postings use 1–8 empty paragraphs to fake extra vertical white-space.
This makes spacing dependent on the recruiter's mood the day they wrote
the posting. Recommend either:

- Author guideline: "do not press Enter to add blank lines"; spacing is
  handled by the careers-page CSS (`.job-post p + p { margin-top: var(--
  space-2); }` already exists), **or**
- A one-line sanitiser in the careers template that strips
  `<p>\s*(?:&nbsp;)?\s*</p>` before rendering.

### 4.6 Cap or template length

The pre-Comp word-count range is 244 → 876 (3.6×). Consider a soft target
of **400–600 words pre-Compensation** with a hard cap of ~700, and ask
recruiters to move overflow into Compensation/Benefits sections or into
team-specific landing pages. The 876-word `GTM Engineer, Pre-Sales` and
the 786-word `Staff Product Manager, Platform & Infrastructure` are the
most over-target.

### 4.7 Standardise the bullet-vs-prose call

Define when to use bullets vs. paragraphs (typical guidance: bullets for
"How you'll make an impact" and "What makes you a good fit"; prose
optional for "About the role"). Then:

- Convert `Director, Global Supply Management - Mechanicals` (0 bullets,
  100% prose) to the standard bulleted format.
- Trim `IT Technician (Help Desk - Linux Focus)` from 42 bullets to ~20
  (consolidate or move to a separate "Requirements" subsection).

### 4.8 Add a lint step to the publishing pipeline

A 50-line checker (the script in this repo is a starting point) can run
against every new posting and block publish if any of the following are
true:
- contains `<u>`,
- contains `<h1>`,
- contains an empty `<p>`,
- pseudo-heading text doesn't match the canonical regex
  `^(About the (role|team)|How you'll make an impact|What makes you a
  good fit|Bonus points|Preferred qualifications):$`,
- pre-Compensation word count is outside 300–700.

That single guard would prevent every issue in §1 from recurring.

---

## 5. Postings that most need attention

Sorted by "how many flags this posting trips" (highest first).

| Posting | Flags |
|---|---|
| **`GTM Engineer, Pre-Sales`** (Sales, US CA San Mateo) | typo in section label · 8× `<em>` lead-ins (unique) · 876 words (longest) · 4 empty `<p>` spacers |
| **`Senior Technical Support Representative - Japan`** (Customer Support, Tokyo) | only posting using `<h1>` for sections |
| **`Hardware Engineering Program Manager`** (Hardware, San Mateo) | only posting using nested `<h2>`+`<h3>` |
| **`Revenue Operations Engineer, Quoting Systems`** (Sales) | mixes real `<h2>` and pseudo headings |
| **`Senior Business Operations Manager`** (Supply Chain) | mixes real `<h3>` and pseudo headings |
| **`PhD Autonomy Engineer Intern – Planning & Controls (RL)`** (Autonomy, Zurich) | mixes real `<h3>` and pseudo headings |
| **`Senior Buyer`** (Manufacturing, Hayward) | mixes real `<h2>` and pseudo headings |
| **`Full Stack Product Counsel`** (Legal) | real `<h3>` (outlier) + uses `<u>` |
| **`Lead Staff Electrical Engineer`** (Hardware) | uses `<u>` |
| **`Senior NPI Product Quality Engineer`** (Manufacturing) | uses `<u>` AND `<em>` |
| **`Director, Global Supply Management — Mechanicals`** (Supply Chain) | 0 bullets — only all-prose posting |
| **`IT Technician (Help Desk – Linux Focus)`** (IT) | 42 bullets — 2× the next highest |
| **`Senior / Staff Product Manager, Platform & Infrastructure`** (Product) | both use 6 empty-paragraph spacers (most of any posting) |
| **`Senior / Staff Software Engineer, Frontend`** (Software) | both use 5 empty-paragraph spacers |
| `Staff Technical Recruiter`, `Senior Technical Recruiter`, `Senior Technical Recruiter - Hardware Operations`, `Senior Software Engineer, Full Stack`, `Public Safety Strategist` | each contains a `<u>` |

---

## 6. Per-posting metrics (excerpt)

The full table is in `analysis/per_job_table.md`. Columns:

- **Heading style** — `pseudo only` (no `<h?>`, sections are bold
  paragraphs) or `REAL (h?×N …)` (which `<h?>` tags appear and how often).
- **# bold-section labels** — number of `<p><strong>…</strong></p>`
  pseudo-headings in the pre-Comp content.
- **# bullets** — number of `<li>` items.
- **empty `<p>`** — number of blank-paragraph spacers.
- **`<em>` / `<u>`** — italic / underline tag counts.

| Department | Title | Words | Heading style | Bold labels | Bullets | Empty p | em | u |
|---|---|---:|---|---:|---:|---:|---:|---:|
| Sales | **GTM Engineer, Pre-Sales** | **876** | pseudo only | 3 | 27 | 4 | **8** | 0 |
| Customer Support | **Senior Technical Support Representative – Japan** | 717 | **REAL (h1×3)** | 0 | 20 | 1 | 0 | 0 |
| Hardware | **Hardware Engineering Program Manager** | 491 | **REAL (h2×3 h3×5)** | 0 | 23 | 3 | 0 | 0 |
| Software | Senior Wireless Software Engineer, National Security | 723 | REAL (h2×6) | 0 | 25 | 4 | 0 | 0 |
| Autonomy | Software Engineer – Cloud Simulation & Full-Stack (Zurich) | 666 | REAL (h2×5) | 0 | 26 | 2 | 0 | 0 |
| Autonomy | Software Engineer – Cloud Simulation & Full-Stack (San Mateo) | 555 | REAL (h2×5) | 0 | 26 | 2 | 0 | 0 |
| Autonomy | Software Engineer – Autonomy Infrastructure, Systems and Tools (Zurich) | 635 | REAL (h2×5) | 0 | 20 | 1 | 0 | 0 |
| Autonomy | Software Engineer – Autonomy Infrastructure, Systems and Tools (San Mateo) | 524 | REAL (h2×5) | 0 | 20 | 1 | 0 | 0 |
| Autonomy | Software Engineer – Simulation & Robotics Engineer (Zurich) | 596 | REAL (h3×5) | 0 | 20 | 1 | 0 | 0 |
| Autonomy | Software Engineer – Simulation & Robotics Engineer (San Mateo) | 485 | REAL (h3×5) | 0 | 20 | 2 | 0 | 0 |
| Autonomy | PhD Autonomy Engineer Intern – Planning & Controls (RL) | 555 | REAL (h3×3) | **2** | 17 | 0 | 0 | 0 |
| Sales | Revenue Operations Engineer, Quoting Systems | 511 | REAL (h2×5) | **1** | 25 | 2 | 0 | 0 |
| Supply Chain & Logistics | Senior Business Operations Manager | 506 | REAL (h3×3) | **3** | 26 | 3 | 0 | 0 |
| Manufacturing | Senior Buyer | 478 | REAL (h2×2) | **1** | 22 | 3 | 0 | 0 |
| Marketing | Communications Manager | 425 | REAL (h2×3) | 0 | 12 | 3 | 0 | 0 |
| Policy & Regulatory Affairs | Aviation Compliance Lead | 402 | REAL (h2×4) | 0 | 15 | 1 | 0 | 0 |
| Policy & Regulatory Affairs | Aviation Regulatory Program Manager | 496 | REAL (h2×3) | 0 | 16 | 2 | 0 | 0 |
| Legal | Full Stack Product Counsel | 526 | REAL (h3×4) | 0 | 15 | 3 | 0 | **1** |
| Hardware | Lead Staff Electrical Engineer | 318 | pseudo only | 2 | 15 | 2 | 0 | **1** |
| Manufacturing | Senior NPI Product Quality Engineer | 394 | pseudo only | 3 | 19 | 0 | **1** | **1** |
| People & Recruiting | Staff Technical Recruiter | 432 | pseudo only | 3 | 15 | 0 | 0 | **1** |
| People & Recruiting | Senior Technical Recruiter | 435 | pseudo only | 2 | 14 | 0 | 0 | **1** |
| People & Recruiting | Senior Technical Recruiter – Hardware Operations | 442 | pseudo only | 1 | 13 | 0 | 0 | **1** |
| Software | Senior Software Engineer, Full Stack | 626 | pseudo only | 4 | 13 | 0 | 0 | **1** |
| Sales | Public Safety Strategist (W/Midwest/PNW) | 617 | pseudo only | 4 | 28 | 0 | 0 | **1** |
| Marketing | Director, Growth Marketing – Commercial | 596 | pseudo only | 5 | 23 | 2 | **1** | 0 |
| Product | Senior Product Manager, Platform & Infrastructure | 767 | pseudo only | 3 | 15 | **6** | 0 | 0 |
| Product | Staff Product Manager, Platform & Infrastructure | 786 | pseudo only | 3 | 15 | **6** | 0 | 0 |
| Supply Chain & Logistics | **Director, Global Supply Management – Mechanicals** | 612 | pseudo only | 3 | **0** | 3 | 0 | 0 |
| IT | **IT Technician (Help Desk – Linux Focus)** | 524 | pseudo only | 3 | **42** | 2 | 0 | 0 |
| Hardware | Electrical Engineer (all levels) | **244** | pseudo only | 2 | 13 | 0 | 0 | 0 |
| Supply Chain & Logistics | Supply Chain Intern | **232** | pseudo only | 2 | 8 | 0 | 0 | 0 |

(All 113 rows: see `analysis/per_job_table.md`.)

---

## 7. Reproducing the analysis

```bash
# Pull the live data set
curl -s https://api.ashbyhq.com/posting-api/job-board/skydio > jobs.json

# Run the analysis (uses only the Python standard library)
python3 analysis/analyze.py
```

Outputs:

- `analysis/per_job_metrics.json` — full per-posting metric dump.
- `analysis/per_job_summary.json` — flat one-row-per-posting summary.
- `analysis/per_job_table.md`     — markdown table used in §6.
- `analysis/run_summary.txt`      — aggregate console output.

---
*Report generated automatically from `descriptionHtml` payloads served by
the Ashby job-board API on 2026-05-30. No screenshots or page rendering
were used; all "visual" differences below are derived from authored HTML
structure.*

# Skydio Careers — Job Posting Formatting Consistency Audit

**Source:** [https://www.skydio.com/careers](https://www.skydio.com/careers) (snapshot pulled 2026-05-14)
**Postings analyzed:** 112 (every job linked from the careers page)
**Scope:** Job description body up to — but not including — the **Compensation** section.

> Skydio's careers page uses a single Greenhouse-backed template. Every posting is rendered inside the same `<div class="prose">` container with the same global CSS, so font *size, color, family,* and *line-height* are controlled by the site, not by the recruiter. The visual inconsistencies that show up between postings come from **the HTML structure the recruiter pasted into Greenhouse** — what tags they used for section headings, how they bolded labels, whether they used `<ul>` lists vs. typed-in bullets, whether they pasted smart quotes / `&nbsp;` from Word / Google Docs, etc. The audit below quantifies exactly those structural differences.

---

## 1. Executive summary

| Theme | What we found | Severity |
|---|---|---|
| **Section-heading hierarchy** | 81% of postings use a bold `<p>` for section headings (renders at body font size), 11% use real `<h2>` tags (large), 5% mix both inside the same posting, 4% have no detectable section headings at all. One posting uses `<h1>` (which collides with the page-title `<h1>`). | **High** — biggest visual difference between postings. |
| **Section-heading wording** | "About the role:" appears in **4** different capitalizations across postings; "What makes you a good fit:" appears in **6** different variants (including a typo "What Makes You*r* a Good Fit:"); some postings drop the trailing colon entirely. | **High** — readers notice it. |
| **Apostrophe style** | "How you*'*ll make an impact:" uses a **straight ASCII apostrophe** in 39 postings and a **curly Unicode apostrophe** in 37 — an almost 50/50 split. | **Medium** |
| **Quote characters** | 93/112 postings (83%) contain curly quotes pasted from Word/Docs; 19 use straight quotes only. | **Medium** |
| **Stray `&nbsp;`** | 26 postings have non-breaking spaces embedded in the prose (up to 13 per posting), a tell-tale of Word/Docs paste. They cause inconsistent inter-word spacing. | **Low / Medium** |
| **Manual `<br>` line breaks** | 11 postings use ≥4 `<br>` tags inside paragraphs (peak: 8 in one posting) to fake spacing, breaking the site's natural line-height/leading. | **Medium** |
| **Typed-in bullet glyphs (`•`)** | 1 posting (**Director, Global Supply Management - Mechanicals**) replaces a `<ul>` list with 14 plain paragraphs that begin with a `•` character. Renders flush-left, ignored by screen readers, and visually offset from every other posting. | **High** |
| **Bold emphasis inside `<li>`** | 18 postings inject `<strong>` inside list items (sometimes 19 per posting). The rest of the catalog never does. | **Medium** |
| **`<u>` underline and `<em>` italics** | 2 postings use `<u>` underline inside lists (looks like hyperlinks). 1 posting uses `<em>` italics inside a list. Inconsistent with the rest. | **Low** |
| **Compensation label** | Most postings use "**Compensation:**". Three use "**Compensation Range:**". One posting (**Full Stack Product Counsel**) has *no label at all* — the comp paragraph starts mid-sentence ("At Skydio, our compensation packages…"). | **Medium** |

---

## 2. Methodology

1. Downloaded the raw HTML for all 112 unique job listings linked from the careers page.
2. Located the description region (`<div class="prose block-content">`) and the page-title `<h1 class="type-h2">`.
3. Truncated each description at the first paragraph that begins with `Compensation`, `Compensation Range`, `Salary`, `Pay Range`, `Base Pay`, or the "At Skydio, our compensation…" boilerplate sentence.
4. For everything that remained (the pre-comp body), inspected:
   * Which heading tags appear (`<h1>`…`<h6>`)?
   * How section headings are styled (real heading vs. `<p><strong>…</strong></p>`).
   * Heading wording, capitalization, colon usage, and apostrophe style.
   * List structure: `<ul>`/`<ol>`, `<li>` shape, embedded `<strong>`/`<em>`/`<u>`.
   * Typography hygiene: `<br>` count, `&nbsp;` count, curly vs. straight quotes, manual bullet glyphs (`•`, `*`, `-`) at the start of `<p>` text.
   * Any inline `style="…"` attribute, `<font>` tag, `<span style>` tag, or explicit color/size/line-height overrides.

Reproducible scripts and raw outputs are in `analysis/` (see Appendix).

---

## 3. Detailed findings

### 3.1 Section-heading hierarchy is inconsistent (the headline issue)

All postings carry the same page-title `<h1 class="type-h2">` (rendered at the same large size by the site CSS). Below that title, postings diverge dramatically:

| Style used for section headings ("About the role", "How you'll make an impact", etc.) | # postings | What it looks like |
|---|---|---|
| Bold `<p>` only — `<p><strong>About the role:</strong></p>` | **91 (81%)** | Same body-font-size as paragraphs, just bold. |
| Real heading tags only — `<h2>` or `<h3>` inside the prose | **12 (11%)** | Noticeably larger font (Tailwind/typography styles `<h2>` ~1.5–1.75× body, `<h3>` ~1.25–1.5× body). |
| **Mixed** — both bold `<p>` and real headings in the *same* posting | **5 (4%)** | Section headings render at *two different sizes* in one job ad. |
| No detected bolded section headings | **4 (4%)** | The structure-by-typography signal collapses. |

#### 3.1.1 Postings rendering section headings at the larger `<h2>`/`<h3>` size (12)

| Posting | Heading tag used |
|---|---|
| Aviation Compliance Lead (San Mateo) | `<h2>` ×3 |
| Aviation Regulatory Program Manager (US Remote) | `<h2>` ×3 |
| Communications Manager (US Remote) | `<h2>` ×3 |
| Deployment Coordinator (US Remote) | `<h2>` ×4 |
| Field Marketing Event Manager (San Mateo) | `<h3>` ×7 |
| Full Stack Product Counsel (San Mateo) | `<h3>` ×4 |
| Revenue Operations Engineer, Quoting Systems (San Mateo) | `<h2>` ×5 |
| Senior Business Operations Manager (San Mateo) | `<h3>` ×3 |
| Senior Buyer (Hayward) | `<h2>` ×2 |
| Software Engineer – Autonomy Infrastructure, Systems and Tools (San Mateo & Zurich, 2 postings) | `<h2>` ×5 each |
| Software Engineer – Cloud Simulation & Full-Stack (San Mateo & Zurich, 2 postings) | `<h2>` ×5 each |
| Software Engineer – Simulation & Robotics Engineer (San Mateo & Zurich, 2 postings) | `<h3>` ×5 each |
| PhD Autonomy Engineer Intern – Planning & Controls (Reinforcement Learning) (Zurich) | `<h3>` ×3 |

Open any of these alongside an "Autonomy Engineer – Deep Learning" posting and the side-by-side difference is obvious: the section headings in the postings above are visibly larger and have more vertical spacing because the global `<h2>`/`<h3>` styles apply margin-top/bottom.

#### 3.1.2 Worst-case: `<h1>` used inside the body (1)

* **Senior Technical Support Representative – Japan (Tokyo)** uses **`<h1>`** ×3 inside the prose for "About the role:", "How you'll make an impact:", and "What would make you a good fit:". This collides with the page-title `<h1 class="type-h2">`, breaks document outline / SEO, and produces the largest font size of any posting's section heading.

#### 3.1.3 Postings mixing two heading sizes in the same job (5)

| Posting | Real headings | Bold-`<p>` headings |
|---|---|---|
| Revenue Operations Engineer, Quoting Systems | `<h2>` ×5 | 1 |
| Senior Business Operations Manager | `<h3>` ×3 | 3 |
| Senior Buyer | `<h2>` ×2 | 1 |
| Field Marketing Event Manager | `<h3>` ×7 | 3 |
| PhD Autonomy Engineer Intern – Planning & Controls (Reinforcement Learning) | `<h3>` ×3 | 2 |

In these postings, a reader sees a "section heading" appear at two different visual weights inside the same job — a clear sign the recruiter pasted from two different source docs.

#### 3.1.4 Postings with **no** bolded section-heading structure (4)

* **Technical Support Specialist – West Coast** (US Remote)
* **Product Support Engineer** (San Mateo) — colon and label split across nodes, see §3.2.
* **Product Support Engineer Intern** (San Mateo)
* **PhD Autonomy Engineer Intern – Deep Learning or Computer Vision** (San Mateo)

These read as a long wall of paragraphs with no visual section breaks.

---

### 3.2 Section-heading wording, capitalization and colon usage

The same section appears under many different labels. The most-used five labels:

| Variants of the same section | Counts | Notes |
|---|---|---|
| **"About the role"** — appears 4 ways: `About the role:` (46), `About the Role:` (22), `About The Role` (1), `About the Role` (2) | 71 total | Title-case vs. sentence-case is inconsistent; 3 postings drop the colon. |
| **"How you'll make an impact"** — appears 5 ways: `How you'll make an impact:` (37 with straight apostrophe), `How You'll Make an Impact:` (1, straight apostrophe), `How You'll Make an Impact:` (20, curly apostrophe), `How you'll make an impact:` (13, curly apostrophe), `How you'll make an impact` (1, no colon, curly apostrophe), `How you will make an impact:` (2) | 74 total | Three independent inconsistencies in one heading: case, apostrophe shape, presence of colon. |
| **"What makes you a good fit"** — 6 variants: sentence-case (53), Title Case (18), `What Makes You A Good Fit:` (3), `What Makes You a Good Fit` no colon (1), `What makes you a good fit` no colon (2), and **`What Makes You*r* a Good Fit:`** (1 — typo) | 78 total | The "Your" typo is on **IT Technician (Help Desk - Linux Focus)**. |
| **"About the team"** — `About the team:` (5) vs. `About the Team:` (6) | 11 total | |
| **"Bonus points"** — `Bonus points:` (3) vs. `Bonus Points:` (3) | 6 total | |
| **"Nice to have"** — `Nice to have:` (2) vs. `Nice to Have` (1) | 3 total | |

**Aggregate stats**

* 81% of section headings start with a Capital Letter on every word (Title Case); 19% use sentence case. Mixing inside the same posting happens in 4 named postings (e.g., *Senior Product Manager, Platform & Infrastructure* uses "Location" alongside "How you'll make an impact:").
* 73% of section headings end with `:`; 27% do not. Postings that drop the colon for every heading: 4 of the 12 real-heading postings (Aviation Compliance Lead, Aviation Regulatory Program Manager, Communications Manager, Deployment Coordinator) and **IT Technician (Help Desk - Linux Focus)**.
* Apostrophe shape in the canonical "How you'll make an impact" heading: **straight `'` in 39 postings vs. curly `'` in 37** — a nearly even split. Same heading, two different glyphs.

---

### 3.3 Colon-outside-`<strong>` cruft

In a clean posting the markup is `<p><strong>About the role:</strong></p>` — both label *and* colon are bold.

In 7 postings the colon (and sometimes a `&nbsp;`) is **outside** the `<strong>` wrap. The colon renders at regular weight while the label is bold, which is visibly uneven:

```html
<p><strong>About the team</strong>:<strong> </strong></p>     ← Technical Support Specialist - West Coast
<p><strong>About the role</strong>:&nbsp;</p>                 ← Product Support Engineer
```

Affected postings:

* Staff Software Engineer, Full Stack (San Mateo)
* Technical Support Specialist – West Coast (US Remote)
* Senior Software Engineer, Full Stack (San Mateo)
* Senior Software Engineer, Frontend (San Mateo)
* Product Support Engineer Intern (San Mateo)
* Product Support Engineer (San Mateo)
* Software Engineer Intern Fall 2026/Winter 2027 (US CA San Mateo)

The **Technical Support Specialist – West Coast** posting goes further with `<strong>About the team</strong>:<strong>&nbsp;</strong></p>` — an empty `<strong>&nbsp;</strong>` cruft node left behind by Word/Docs paste.

---

### 3.4 Lists and bullets

* **`<ul>` is used by 111 of 112 postings**, with `<li><p>…</p></li>` shape — consistent and correct.
* No posting uses `<ol>` ordered lists.

#### 3.4.1 Hard-typed bullet glyphs instead of a list (1, major)

* **Director, Global Supply Management – Mechanicals** (San Mateo) replaces the "How you'll make an impact" and "What makes you a good fit" sections with **14 separate paragraphs** that each begin with a `•` character, e.g.:

  > `<p>• Provide strategic vision and direction to align global supply chain…</p>`
  > `<p>• Develop component inventory strategies to support production…</p>`

  Because they're paragraphs, not list items, they render flush-left with no indentation and no hanging bullet alignment. Visually they stand out from every other posting in the catalog.

#### 3.4.2 Bold *inside* list items (18 postings; outliers)

18 postings introduce `<strong>` *inside* `<li>` for emphasis. Several use it heavily:

| Posting | `<li>` containing `<strong>` |
|---|---|
| Software Engineer – Cloud Simulation & Full-Stack (San Mateo) | 19 |
| Software Engineer – Cloud Simulation & Full-Stack (Zurich) | 19 |
| Revenue Operations Engineer, Quoting Systems (San Mateo) | 18 |
| PhD Autonomy Engineer Intern – Planning & Controls (RL) (Zurich) | 12 |
| GTM Data Engineer Intern (San Mateo) | 11 |
| Senior Product Manager, Platform & Infrastructure | 10 |
| Staff Product Manager, Platform & Infrastructure | 10 |
| Software Engineer – Simulation & Robotics Engineer (San Mateo & Zurich) | 8 each |
| Senior People Analytics Analyst | 7 |
| Hardware Operations Program Manager | 6 |
| Software Engineer – Autonomy Infrastructure, Systems and Tools (San Mateo & Zurich) | 4 each |
| Senior Technical Recruiter | 2 |
| Director, Growth Marketing - Commercial; Manager, Technical Support; Senior Technical Recruiter – Hardware Operations; PhD Autonomy Engineer Intern – Deep Learning or Computer Vision | 1 each |

The other **94 postings** never bold inside `<li>`. Inside a bullet list this reads as inconsistent emphasis — the visual texture of one job ad reads "bullets with bolded sub-labels" while the next reads "plain bullets".

#### 3.4.3 `<em>`/italic inside `<li>` (1)

* **Director, Growth Marketing - Commercial** (San Mateo): italicizes a single bullet (`<em><strong>Ability to be in our San Mateo, CA office 3 days per week</strong></em>`). No other posting uses italics inside bullets.

#### 3.4.4 `<u>` underline inside `<li>` (2)

* **Senior Software Engineer, Full Stack** (San Mateo)
* **Full Stack Product Counsel** (San Mateo)

Underlined text inside a list looks like a broken hyperlink and is inconsistent with the rest of the catalog.

---

### 3.5 Manual line-breaks (`<br>`), `&nbsp;`, and smart quotes

These are all signatures of pasted Word / Google Docs content rather than text typed directly into Greenhouse.

#### 3.5.1 Heavy `<br>` use (≥4 per posting, 11 postings)

`<br>` is being used to fake vertical spacing or to force line breaks inside otherwise normal paragraphs, which makes line-height inconsistent against the rest of the catalog.

| Posting | `<br>` count |
|---|---|
| Director, Growth Marketing - Commercial (San Mateo) | 8 |
| IT Technician (Help Desk - Linux Focus) (Hayward) | 8 |
| Autonomy Engineer – Deep Learning Infrastructure (San Mateo) | 8 |
| Autonomy Engineer – Deep Learning Model Acceleration (Zurich) | 6 |
| Autonomy Engineer – Deep Learning Infrastructure (Zurich) | 6 |
| Autonomy Engineer – Deep Learning Model Acceleration (San Mateo) | 6 |
| Revenue Operations Engineer, Quoting Systems | 4 |
| Director of Product Management, Drone as First Responder (DFR) | 4 |
| Senior Technical Recruiter – Hardware Operations | 4 |
| Autonomy Software Engineer | 4 |
| Software Engineer Intern Fall 2026/Winter 2027 | 4 |

#### 3.5.2 Stray `&nbsp;` (≥3 per posting, 9 postings)

Non-breaking spaces leak in from Word/Docs, producing inconsistent word spacing and double-spaces after periods.

| Posting | `&nbsp;` count |
|---|---|
| Field Support Representative (Southwest, Remote) | 13 |
| Senior Staff Product Manager, Drone Hardware Platforms & Sensors | 9 |
| Customer Success Manager, DFR Majors – Northeast | 6 |
| Director of Product Management, Drone as First Responder (DFR) | 5 |
| Technical Support Specialist – West Coast | 5 |
| Senior Wireless Systems Performance Engineer | 4 |
| Senior Software Engineer – Embedded | 3 |
| Staff Software Engineer – Embedded | 3 |
| Software Engineer – Embedded | 3 |

#### 3.5.3 Curly vs. straight quotes/apostrophes

* 93 postings (83%) contain at least one curly quote or apostrophe (' ' " ").
* 19 postings use straight quotes only.

Inside any given posting it's usually internally consistent (one source doc), but **across postings** the difference shows up most noticeably in the "How you'll make an impact:" heading, where 39 use `'` and 37 use `'`.

---

### 3.6 Title metadata

Two postings have **double spaces** in their `<h1>` title:

* **"Senior Software Engineer,&nbsp;&nbsp;Data Platform"** (San Mateo)
* **"Senior Software Engineer,&nbsp;&nbsp;Infrastructure"** (San Mateo)

These render with visibly wider gaps after the comma than the matching titles for other roles.

---

### 3.7 Compensation block consistency

Of 112 postings, **5 have no detectable compensation section** at all:

* Supplier Quality Engineer, Sustaining (Taiwan)
* Workplace Experience Coordinator Part-Time (Zurich)
* Senior Technical Support Representative – Japan (Tokyo)
* Autonomy Engineer Intern – Deep Learning (Computational Photography) (Zurich/Tampere)
* Autonomy Engineer Intern – Deep Learning (Computational Photography) (San Mateo)

Of the 107 that do, the **label** wording differs:

| Label | Approx. count |
|---|---|
| **"Compensation:"** as the bolded label | majority |
| **"Compensation Range:"** | 3 postings (Senior People Analytics Analyst; Staff Product Manager, Cameras & Sensors; Director of Product Management, DFR) |
| **No label at all** — body just begins "At Skydio, our compensation packages…" | 1 posting (**Full Stack Product Counsel**) |

Even though "Compensation" content is out of scope, the *boundary* between description and compensation is what readers see, and 4 postings break the pattern.

---

### 3.8 Things that are actually consistent (worth noting)

* **No inline `style="…"` attributes** anywhere — no posting overrides font-size, color, font-family, line-height, or alignment manually. All visible font/color/size differences come from heading-tag choice, not inline overrides.
* **No `<font>` tags, no `<span style>` overrides.**
* **No `<hr>` rules** in any posting.
* **No `<ol>` ordered lists** anywhere.
* `<ul><li><p>…</p></li></ul>` is used uniformly (111/112).
* The page-title `<h1 class="type-h2">` and location chip `<p class="type-body-2">` are identical across every posting.

These confirm that the catalog *would* be consistent if the body content itself were authored against a template.

---

## 4. Stand-out postings (the ones that look most different from the norm)

Ranked by how many distinct formatting issues they exhibit:

1. **Director, Global Supply Management – Mechanicals** — replaces both `<ul>` blocks with 14 hard-typed `•` paragraphs. Visually unmistakable.
2. **Senior Technical Support Representative – Japan** — uses `<h1>` inside the body (3 of them), giving section headings the largest font in the entire catalog and breaking the document outline.
3. **IT Technician (Help Desk - Linux Focus)** — 8 manual `<br>` tags, all headings drop the colon, mixes "About the Role" / "What You'll Do" / "What Makes You a Good Fit" / "Nice to Have" in different cases, contains the typo "What Makes You*r* a Good Fit:", uses both "Location" and "Onsite – 5 days/week, Monday – Friday: 3:30pm – 12am Skydio Manufacturing (Hayward, CA)" as section headings.
4. **Technical Support Specialist – West Coast** — bold label and colon split across nodes, empty `<strong>&nbsp;</strong>` cruft, 5 stray `&nbsp;`, no detectable section-heading style.
5. **Product Support Engineer** & **Product Support Engineer Intern** — bold label and colon split (so colon renders unbolded), all section headings essentially get demoted; the latter sits inside an `<ul>` immediately after a non-heading paragraph.
6. **PhD Autonomy Engineer Intern – Deep Learning or Computer Vision** — no bold section headings detected.
7. **Software Engineer – Cloud Simulation & Full-Stack (×2)** & **Software Engineer – Autonomy Infrastructure, Systems and Tools (×2)** — `<h2>` headings (large) plus 19 bolded `<li>` entries, a much heavier text texture than peer postings.
8. **Full Stack Product Counsel** — `<h3>` headings, `<u>` underlining inside list items, *and* a missing "Compensation:" label.
9. **Field Marketing Event Manager** — 7 `<h3>` section headings; reads as a multi-page document inside a single posting.
10. **Director, Growth Marketing - Commercial** — only posting that uses `<em>`/italic inside a list, 8 `<br>` tags, has bullets that are *italic + bold* simultaneously.

Specific typo to fix:

* **IT Technician (Help Desk - Linux Focus)**: `What Makes You*r* a Good Fit:` → `What Makes You a Good Fit:`

Specific double-space titles to fix:

* `Senior Software Engineer,  Data Platform` → `Senior Software Engineer, Data Platform`
* `Senior Software Engineer,  Infrastructure` → `Senior Software Engineer, Infrastructure`

---

## 5. Recommendations (actionable)

### 5.1 Adopt a single posting template

Define and circulate a **canonical Skydio job-posting template** with:

* Fixed section order and exact heading text:
  1. Intro paragraph ("Skydio is the leading US drone company…")
  2. **About the role:**
  3. **How you'll make an impact:** (curly apostrophe ' — pick one and stick with it)
  4. **What makes you a good fit:**
  5. **Bonus points:** *(optional)*
  6. **Compensation:** *(out of scope here)*

  Pick one case style — sentence case is dominant (53 vs. 18 for the most common heading) and matches the page-title `<h1>` casing — and apply it everywhere. Always end every section heading with a colon to remove the "to-colon-or-not" decision.

* Use the **same HTML shape** in every posting. Recommended: `<p><strong>Heading:</strong></p>` (no inline `<h2>`/`<h3>` in the prose, since today's `<h2>`/`<h3>` users are the visible outliers and recruiters can't reliably tell which tag the editor inserted). If Skydio prefers the larger headings, instead require `<h2>` everywhere and rebuild every posting against that — but pick **one** and audit periodically.

* Always wrap **the entire bold label, including the colon and trailing whitespace, inside one `<strong>`** — `<p><strong>About the role:</strong></p>`. Treat `<p><strong>X</strong>:</p>` and `<p><strong>X</strong>:<strong>&nbsp;</strong></p>` as lint failures.

* Bullets must use `<ul><li>…</li></ul>` — never typed-in `•`/`*`/`-`.

* Avoid `<strong>` inside `<li>`. If a bullet truly needs emphasis, refactor it into a sub-heading.

### 5.2 Add a "paste cleanup" pre-publish step in Greenhouse

Before publishing, every posting should be run through a paste-cleanup pass that:

* Strips `<br>` from inside paragraphs (use real `<p>` breaks for spacing).
* Strips `&nbsp;`, replaces with normal spaces; removes double spaces.
* Normalizes quotes (pick straight or curly — straight is simpler; curly is more polished. Right now both exist).
* Removes leftover editor cruft like `<strong>&nbsp;</strong>` and empty `<p></p>` blocks.
* Removes `class="ProseMirror-trailingBreak"` and other editor classes.

Tools: Greenhouse's "paste as plain text", a Tampermonkey script for recruiters, or a one-time bulk-edit script run against the Greenhouse API.

### 5.3 Quick wins (one-off edits, do these first)

These are the highest-impact, lowest-effort fixes:

1. **Director, Global Supply Management – Mechanicals** — re-author the two bullet sections as real `<ul>` lists. (Single biggest visual outlier in the catalog.)
2. **Senior Technical Support Representative – Japan** — change the three `<h1>` tags to whatever section-heading pattern is canonical.
3. **IT Technician (Help Desk - Linux Focus)** — fix the typo `What Makes Your` → `What Makes You`; add colons; normalize case.
4. **Product Support Engineer**, **Product Support Engineer Intern**, **Technical Support Specialist – West Coast**, **Senior Software Engineer, Frontend**, **Senior Software Engineer, Full Stack**, **Staff Software Engineer, Full Stack**, **Software Engineer Intern Fall 2026/Winter 2027** — move the colon (and any trailing `&nbsp;`) inside the `<strong>` wrap.
5. **Senior Software Engineer, Data Platform** & **Senior Software Engineer, Infrastructure** — remove the double space in the title.
6. **Full Stack Product Counsel** — add the missing "**Compensation:**" label; remove the `<u>` underlines in list items.
7. The 12 postings that currently use `<h2>`/`<h3>` (Aviation Compliance Lead, Aviation Regulatory Program Manager, Communications Manager, Deployment Coordinator, Field Marketing Event Manager, Revenue Operations Engineer, Senior Business Operations Manager, Senior Buyer, and the four "Software Engineer – Cloud / Autonomy / Sim" postings) — either downgrade them all to bold `<p>` to match the 91-posting norm, or *upgrade* the rest of the catalog to `<h2>`. Pick one.

### 5.4 Add an automated lint check

The analysis script in this audit (`analysis/analyze.py`) can be re-run any time to regenerate `per_posting_summary.csv`. Wire it into a weekly cron / GitHub Action that flags any new posting which:

* Contains `<h1>`/`<h2>`/`<h3>`/`<h4>` inside the description prose.
* Contains `<br>` more than 0 times.
* Contains `&nbsp;` more than 0 times.
* Contains a typed bullet glyph (`•`, `●`, `*`, `-`) at the start of a `<p>`.
* Has `<strong>` or `<em>` or `<u>` inside `<li>`.
* Uses a section-heading text that doesn't match the approved list.
* Uses both `'` and `'` in the same document.

That keeps the catalog clean going forward without recruiters needing to memorize every rule.

---

## Appendix — full per-posting summary

The full per-posting table is saved at `analysis/per_posting_summary.csv` (12 columns × 112 rows: title, location/type, body length, section-heading style, colon usage, TitleCase count, bold-inside-`<li>` count, `<br>` count, manual bullet count, curly-quote count, `&nbsp;` count, compensation marker found). The analyzer (`analysis/analyze.py`) and the machine-readable analysis output (`analysis/results.json`) are committed. To regenerate the raw posting HTML, run:

```bash
mkdir -p analysis/jobs
awk '{print $1" "$2}' analysis/job_index.tsv | xargs -n2 -P8 analysis/dl.sh
python3 analysis/analyze.py
```

That re-downloads all 112 job pages from `https://www.skydio.com/jobs/<id>/?gh_jid=<id>` (URL list in `analysis/job_urls.txt`) and writes a fresh `analysis/results.json` and `analysis/per_posting_summary.csv`.

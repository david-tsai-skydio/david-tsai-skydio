# Skydio Careers — Pre-Compensation Formatting Audit

**Audit date:** 2026-05-07  
**Source:** [https://www.skydio.com/careers](https://www.skydio.com/careers) and the 113 individual job-posting pages it links to (`/jobs/<id>`).  
**Scope:** All visible content from the job title down to (but not including) the `Compensation:` block.  
**Sample size:** **113 job postings** across 17 departments and 10+ locations.

---

## TL;DR

- **All 113 job postings share the same outer page chrome** (job title is `<h1 class="type-h2">`, location is `<p class="type-body-2">`). The job-title and location styling is consistent.
- **The body content is _not_ styled consistently.** Skydio's site CSS provides a single `.prose` typography system, but individual posting authors mix three different heading patterns inside it that produce dramatically different visual results. **94 of 113 postings (83%) deviate from the norm in at least one way; only 19 follow the standard pattern (17%).**
- **The single most impactful defect** is that 16 postings render section headings with real `<h1>`/`<h2>`/`<h3>` HTML tags, which display **2–3× larger** than the bold-paragraph headings used by the other 97 postings. One posting (Senior Technical Support Representative – Japan) renders its section headings _larger than the job title itself_.
- **The next most impactful defect** is heading capitalization drift — the same 5–6 logical sections are written 8+ different ways across postings (e.g. `About the role:` vs `About the Role:` vs `About The Role` vs missing entirely), which makes the postings look authored by different companies side-by-side.
- **Recommended fix:** standardize on a single Greenhouse/Sanity rich-text template (5 sections, sentence case, bold-paragraph headings, ASCII apostrophes, no empty paragraphs, no trailing `<br>`) and back-port it through every existing posting.

---

## How the audit was done

1. Fetched [https://www.skydio.com/careers](https://www.skydio.com/careers) and extracted the 113 unique posting URLs (`/jobs/<uuid>?gh_jid=<uuid>`).
2. Fetched each individual posting's static HTML.
3. For each posting, isolated the `<div class="prose block-content">…</div>` body, then truncated **before** the first `<strong>Compensation</strong>` block.
4. Computed an HTML "fingerprint" per posting: heading tags used, capitalization of canonical section labels, count of empty paragraphs, trailing `<br>`s, list-item structure, ALL-CAPS bolded segments, signoff markers, and word count.
5. Compared each posting against the modal pattern.

The full fingerprint dataset is in [`careers-audit/analysis.json`](./careers-audit/analysis.json); the per-posting issue list is in [`careers-audit/per_job_issues.csv`](./careers-audit/per_job_issues.csv); the analyzer script is [`careers-audit/analyze_jobs.py`](./careers-audit/analyze_jobs.py).

---

## What the "norm" looks like

Out of all 113 postings the most common pattern (used by ~57% of bodies) is:

```html
<p>Skydio is the leading US drone company and the world leader in autonomous flight…</p>

<p><strong>About the role:</strong></p>
<p>One paragraph describing the role…</p>
<p>Optional second paragraph…</p>

<p><strong>How you'll make an impact:</strong></p>
<ul>
  <li><p>Bullet 1</p></li>
  <li><p>Bullet 2</p></li>
  …
</ul>

<p><strong>What makes you a good fit:</strong></p>
<ul>
  <li><p>Bullet 1</p></li>
  …
</ul>
```

Resolved against the site's CSS variables, that produces:

| Element | CSS class / tag | Font size (mobile → desktop) | Weight |
|---|---|---|---|
| Job title | `<h1 class="type-h2">` | **22 px → 32 px** | 500 |
| Location | `<p class="type-body-2">` | 16 px → 18 px | 500 |
| Body paragraph | `<p>` (inherits `.prose` body) | **16 px → 18 px** | 400 |
| Section heading (norm) | `<p><strong>` | **16 px → 18 px** | 700 |
| List item | `<li><p>` | 16 px → 18 px | 400 |

Font sizes derive from the page CSS variables `--fs-body-2: clamp(1rem, .8977rem + .2841vw, 1.125rem)` and `--fs-h2: clamp(1.75rem, .7273rem + 2.8409vw, 3rem)` etc. and are confirmed in `.prose h1…h6` rules served on every posting page.

---

## Inconsistencies found

### 1. Section-heading **font size** (highest visual impact)

The Skydio template's `.prose` block applies real heading sizes when authors use real heading tags inside the body:

| Tag in body | Font size (per `.prose h*` rules in shipped CSS) |
|---|---|
| `<h1>` | clamp(1.75 rem, …, 3 rem) → **28 – 48 px** |
| `<h2>` | clamp(1.375 rem, …, 2 rem) → **22 – 32 px** |
| `<h3>` | clamp(1.125 rem, …, 1.75 rem) → **18 – 28 px** |
| `<h4>` | clamp(1.375 rem, …, 1.5 rem) → **22 – 24 px** |
| `<h5>` | clamp(1.125 rem, …, 1.375 rem) → **18 – 22 px** |
| `<h6>` | clamp(1 rem, …, 1.125 rem) → **16 – 18 px** |
| `<p><strong>` (norm) | inherits body — **16 – 18 px** |

Every posting that uses real `<h*>` tags renders **2–3× larger section headings** than its peers, and any posting that uses `<h1>` actually renders headings **larger than the job title itself** (the title is `class="type-h2"`).

#### Postings using real heading tags (16 total)

| Posting | Heading tag(s) | Visual effect |
|---|---|---|
| Senior Technical Support Representative - Japan | 3× `<h1>` | Section headings 28–48 px — **bigger than the job title** |
| Revenue Operations Engineer, Quoting Systems | 5× `<h2>` | Section headings 22–32 px — same size as the title |
| Software Engineer - Cloud Simulation & Full-Stack (San Mateo) | 5× `<h2>` | Same as above |
| Software Engineer - Cloud Simulation & Full-Stack (Zurich) | 5× `<h2>` | Same as above |
| Software Engineer - Autonomy Infrastructure, Systems and Tools (San Mateo) | 5× `<h2>` | Same |
| Software Engineer - Autonomy Infrastructure, Systems and Tools (Zurich) | 5× `<h2>` | Same |
| Aviation Compliance Lead | 3× `<h2>` | Same |
| Aviation Regulatory Program Manager | 3× `<h2>` | Same |
| Communications Manager | 3× `<h2>` | Same |
| Deployment Coordinator | 4× `<h2>` | Same |
| Senior Buyer | 2× `<h2>` | Same |
| Field Marketing Event Manager | 7× `<h3>` | Section headings 18–28 px — ~1.5× peers |
| Software Engineer - Simulation & Robotics Engineer (San Mateo) | 5× `<h3>` | Same |
| Software Engineer - Simulation & Robotics Engineer (Zurich) | 5× `<h3>` | Same |
| PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) | 3× `<h3>` | Same |
| Project Manager, Workplace | 2× `<h3>` | Same |

> **Concrete example:** `<h2><strong>What you'll drive (scope):</strong></h2>` in Revenue Operations Engineer, Quoting Systems vs. `<p><strong>How you'll make an impact:</strong></p>` in 97 other postings.  At desktop width those headings render at **32 px and 18 px respectively** — almost a 2× ratio.

> **Most extreme example:** Senior Technical Support Representative - Japan opens with `<h1>About the role:</h1>` — **48 px on desktop, larger than the 32 px job title above it**.

### 2. Section-heading **wording / capitalization**

The same 4–5 logical sections are written in 8+ different ways. Verbatim heading counts across all 113 postings:

| "About the role" section | Count |
|---|---|
| `About the role:` (sentence case + colon) | **47** ← _modal_ |
| `About the Role:` (Title Case + colon) | 23 |
| `About The Role` (Title Case, no colon) | 1 |
| `About the Role` (Title Case, no colon) | 1 |
| heading is run-on into the same `<p>` as the body (no colon-only "heading paragraph") | 17 |
| no `About the role` heading at all | 19 |
| missing colon variants | 4 |

| "How you'll make an impact" section | Count |
|---|---|
| `How you'll make an impact:` (sentence case, **straight apostrophe**) | **26** ← _modal_ |
| `How You'll Make an Impact:` (Title Case, straight apostrophe) | 17 |
| `How you'll make an impact:` (sentence case, **curly apostrophe** `'`) | 11 |
| `How You'll Make an Impact:` (Title Case, curly apostrophe) | smaller bucket |
| `How you'll make an impact` (no colon) | 1 |
| `How you will make an impact:` (different verb) | 2 |
| (omitted) | several |

| "What makes you a good fit" section | Count |
|---|---|
| `What makes you a good fit:` (sentence case + colon) | **51** ← _modal_ |
| `What Makes You a Good Fit:` (Title Case + colon) | 19 |
| `What Makes You A Good Fit:` (Title Case, capital "A") | 3 |
| `What Would Make You a Good Fit:` (different wording) | 2 |
| `What makes you a good fit` (no colon) | 2 |
| `What makes you a strong fit:` (different wording) | 2 |
| `What would make you a good fit:` (different wording) | 5 |
| `Useful skills and experience:` | 2 |
| `Preferred Qualifications:`, `Nice To Haves:`, `Nice to have:`, `Bonus Points:` | 1–2 each |

> Of all bold "section-heading" paragraphs found, **91 % end with `:` and 9 % do not** — even the colon punctuation is not consistent.

### 3. Section-heading **markup pattern** — three inconsistent approaches

The same logical heading is being written three structurally different ways across the corpus:

| Pattern | Example | Approx. count | Visual result |
|---|---|---|---|
| **A. Bold-paragraph (norm)** | `<p><strong>About the role:</strong></p>` followed by a separate `<p>` of body | 80 / 113 | 16–18 px bold inline-block heading with 12 px paragraph break |
| **B. Real heading tag** | `<h2><strong>What you'll drive (scope):</strong></h2>` | 16 / 113 | 22–48 px heading (see §1) |
| **C. Heading-glued-to-body** | `<p><strong>About the role: <br/></strong>As a Sales Planning Analyst Intern…</p>` *(heading and first paragraph in the same `<p>`, separated only by `<br>` or by nothing)* | 22 / 113 | Heading text rendered at body size with the body content immediately after, **no paragraph gap**. The heading visually disappears. |

#### Postings affected by Pattern C (heading run-on)

These 22 postings have at least one section heading "glued" into a paragraph instead of being its own block:

- Sales Planning Analyst Intern
- GTM Data Engineer Intern
- GTM Enablement Associate
- Hardware Technician
- Lead Staff Electrical Engineer (F10 Program)
- Senior Revenue Operations Manager
- Software Engineer Intern Fall 2026/Winter 2027
- Deployment Engineer - Southeast
- Director of Product Management, Drone as First Responder (DFR)
- Field Support Representative (Southwest, Remote)
- Program Leader, Law Enforcement & Public Safety Training
- Senior Autonomy Engineer - Deep Learning (San Mateo & Zurich)
- Senior Customer Support Representative - India
- Senior Product Manager, Platform & Infrastructure
- Senior Technical Recruiter - Hardware Operations
- Software Engineer - Infrastructure
- Staff Product Manager, Platform & Infrastructure
- Workplace Experience Coordinator Part-Time
- Autonomy Engineer - Deep Learning Infrastructure (Zurich)
- Autonomy Engineer - Deep Learning Model Acceleration (Zurich & San Mateo)
- Autonomy Software Engineer
- Customer Success Manager, DFR Majors - Northeast
- Electric Motor / Propulsion Engineer
- Product Design Engineer (All Levels)
- Senior Software Engineer, Infrastructure

> **Example HTML:** `<p><strong>About the Role:<br /></strong>As a Sales Planning Analyst Intern (SPA), you'll gain hands-on experience supporting…</p>`  
> Compare to the norm: `<p><strong>About the role:</strong></p><p>As a Sales Planning Analyst Intern (SPA), you'll gain hands-on experience supporting…</p>`

### 4. **Empty `<p></p>` filler paragraphs** (54 postings affected)

The Skydio CSS gives `<p>` a top margin and the empty paragraph injects **one extra ~12 px gap** between sections. Since only ~half the postings use them, vertical rhythm is uneven across postings.

Top offenders:

| Posting | Count of `<p></p>` |
|---|---:|
| Senior Product Manager, Platform & Infrastructure | 6 |
| Staff Product Manager, Platform & Infrastructure | 6 |
| Deployment Engineer - Southeast | 5 |
| Senior Autonomy Engineer - Data Curation | 4 |
| Deployment Coordinator | 4 |
| Senior/Staff Embedded Software Engineer – Camera Systems | 4 |
| Sr/Staff Embedded Software Engineer - Camera Systems | 4 |
| (… 47 more with 1–3 empty paragraphs) | |

### 5. **Trailing `<br>` inside `<p>`** (9 postings affected)

These postings end paragraphs with one or more `<br>` before the closing `</p>`, producing an extra blank line on top of the paragraph margin. Net effect: ~24 px of blank space below those paragraphs, vs. ~12 px below normal paragraphs.

| Posting | Count of trailing `<br>` |
|---|---:|
| **Director, Growth Marketing - Commercial** | **8** |
| Revenue Operations Engineer, Quoting Systems | 4 |
| GTM Data Engineer Intern | 2 |
| Lead Staff Electrical Engineer (F10 Program) | 1 |
| Senior Software Engineer, Full Stack | 1 |
| Engineering Manager - Autonomy | 1 |
| PhD Autonomy Engineer Intern - Deep Learning or Computer Vision | 1 |
| Aviation Compliance Lead | 1 |
| Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 | 1 |

### 6. **`#LI-*` LinkedIn signoffs leaking into pre-compensation content** (13 postings)

The `#LI-AY1`-style signoff is supposed to live at the very end of the description (inside or after the Compensation block). Several postings have it before the compensation block, where it shows up as a stray `#LI-AY1` line in the body. Postings affected include: Senior People Analytics Analyst, Senior Technical Support Representative - Japan, Sales Planning Analyst Intern, Hardware Test and Reliability Intern, Wireless Hardware Engineer Intern, Supply Chain Intern, Autonomy Engineer Intern Fall 2026, Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026, PhD Autonomy Engineer Intern - Deep Learning or Computer Vision, Director of Product Management, Drone as First Responder (DFR), Staff Product Manager, Cameras & Sensors, Supplier Quality Engineer, Sustaining, Software Engineer Intern Fall 2026/Winter 2027.

### 7. **ALL-CAPS bolded headings** (5 postings)

Five postings have one or more bolded paragraphs whose entire visible text is uppercase. These render as block-level headings even though they're really inline category labels. The most affected posting is Revenue Operations Engineer, Quoting Systems (`CRM/CPQ:`, `CLM:`, `ERP:`, `PLM:`).

| Posting | All-caps bold strings |
|---|---|
| Revenue Operations Engineer, Quoting Systems | `CRM/CPQ:`, `CLM:`, `ERP:`, `PLM:` |
| PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) | `RL`, `C++` |
| Software Engineer - Cloud Simulation & Full-Stack (San Mateo) | `AWS` |
| Software Engineer - Cloud Simulation & Full-Stack (Zurich) | `AWS` |
| Senior People Analytics Analyst | `R` |

### 8. **Body length** is not normalized

Pre-compensation word count ranges from **244 to 875 words** — a **3.6× spread**. Average is **478 words**.

- Shortest 5: Electrical Engineer (all levels) (244), Senior Autonomy Engineer - Controls (245), Software Engineer, Full Stack (254), Autonomy Engineer - Fixed Wing Planning & Controls (260), Electric Motor / Propulsion Engineer (284).
- Longest 5: Director of Product Management, DFR (875), Staff Product Manager, Platform & Infrastructure (786), Senior Product Manager, Platform & Infrastructure (767), Senior Software Engineer, Data Platform (731), Success Systems Specialist (729).

This is partly legitimate role-by-role variation, but the longest postings cross the threshold where applicants drop off — for example the Platform & Infrastructure PM postings dedicate 200+ words to a `Customer & sales engagement: …` "monolithic" responsibility paragraph that runs together (see Pattern C above).

### 9. Missing 'About the role' section entirely (19 postings)

These postings either replace it with `About the team:`, jump straight to `How you'll make an impact:`, or use real heading tags (covered above). Result: the candidate has no "what is this job" paragraph at the top.

Full list: Senior Technical Recruiter, Staff Product Manager, Cameras & Sensors, Staff Software Engineer, Full Stack, Technical Support Specialist - West Coast, Deployment Coordinator, Communications Manager, Software Engineer - Simulation & Robotics Engineer (×2), Product Support Engineer Intern, Software Engineer - Cloud Simulation & Full-Stack (×2), Software Engineer - Autonomy Infrastructure, Systems and Tools (×2), Product Support Engineer, Aviation Compliance Lead, Project Manager, Workplace, Aviation Regulatory Program Manager, Autonomy Engineer - Deep Learning Infrastructure, Senior Technical Support Representative - Japan.

### 10. Curly vs straight quotation marks

The body content contains **317 curly quotes** (`'`, `'`, `"`, `"`) and **104 straight quotes** mixed across postings. The same posting often contains both because text was pasted from multiple sources. While not a layout issue, it visibly varies typography and is worth normalizing alongside the other fixes.

### Things that are **consistent** across all 113 postings (good news)

- All titles are `<h1 class="type-h2">` (verified across all 113).
- All locations are `<p class="type-body-2">` (verified across all 113).
- **Zero** postings use inline `style="…"` attributes inside the body.
- **Zero** postings declare `font-family`, `font-size`, or `color` overrides.
- **Zero** postings use the deprecated `<b>` tag — bolding is uniformly via `<strong>`.
- All postings use `<ul>` (no `<ol>` numbered lists).
- All list items use the same `<li><p>…</p></li>` structure (no bare `<li>` anywhere in the corpus).
- All postings open with the same boilerplate paragraph beginning **"Skydio is the leading US drone company…"** (113/113).

So the inconsistency is **entirely in the body markup chosen by individual posting authors** — not in the page chrome, fonts, colors, or list styles.

---

## Standout outliers (worst formatters)

Sorted by total number of distinct issues found per posting:

1. **Revenue Operations Engineer, Quoting Systems** — uses 5× `<h2>` headings, 4 trailing `<br>` artifacts, 4 ALL-CAPS bold segments (`CRM/CPQ:`, `CLM:`, `ERP:`, `PLM:`), 2 empty `<p></p>`, Title-Case heading. Looks like a copy-paste from a Word doc.
2. **Senior Technical Support Representative - Japan** — uses 3× `<h1>` headings (the largest possible — 28–48 px) which are visually larger than the job title; missing `About the role` bold heading; `#LI-*` signoff in pre-comp; 1 empty `<p></p>`.
3. **Sales Planning Analyst Intern** — Heading run-on (heading inside same `<p>` as body via `<br>`); Title Case heading; `#LI-*` signoff in pre-comp; 1 empty `<p></p>`.
4. **Senior People Analytics Analyst** — 2 empty `<p></p>`, ALL-CAPS bold (`R` as in the language), 2 Title-Case headings, `#LI-*` signoff.
5. **Software Engineer - Cloud Simulation & Full-Stack** (×2 location variants — should have been one posting) — 5× `<h2>` headings, missing `About the role`, ALL-CAPS bold (`AWS`), 2 empty `<p></p>`.
6. **Software Engineer - Autonomy Infrastructure, Systems and Tools** (×2 location variants) — 5× `<h2>` headings, missing `About the role`.
7. **Director, Growth Marketing - Commercial** — 8 trailing `<br>` artifacts (worst in the corpus), 3 empty paragraphs, Title-Case heading.
8. **Aviation Compliance Lead / Aviation Regulatory Program Manager / Communications Manager / Deployment Coordinator** — same template variant: 3–4× `<h2>`, missing `About the role`, multiple empty paragraphs. Likely written by the same person/team.

The full ranked table (94 postings with at least one issue, plus the 19 clean postings) is in the **Appendix** below.

---

## Recommendations

### Recommendation 1 — Lock the body markup template

Publish a single canonical "Skydio role description" template in the Greenhouse / Sanity authoring tool and require all postings to use it. Recommended structure (in order):

1. **Standard intro paragraph** (no heading) — the existing "Skydio is the leading US drone company…" boilerplate.
2. `<p><strong>About the role:</strong></p>` (sentence case, ASCII apostrophe, trailing colon) — followed by 1–3 plain paragraphs.
3. *(Optional)* `<p><strong>Location:</strong> <inline text>.</p>` for hybrid/remote requirements that vary by role.
4. `<p><strong>How you'll make an impact:</strong></p>` followed by `<ul><li><p>…</p></li>…</ul>`.
5. `<p><strong>What makes you a good fit:</strong></p>` followed by a single `<ul>`.
6. *(Optional)* `<p><strong>Bonus points:</strong></p>` followed by a single `<ul>`.
7. `<p><strong>Compensation:</strong></p>` — boundary; everything below this is out of scope for this audit.

Section heading rules:
- **Use `<p><strong>` only.** Never `<h1>`–`<h6>` inside the body — those override the site's body type scale.
- **Sentence case**, with a trailing colon, **straight apostrophe** (`you'll`, not `you'll`).
- One section heading per topic; never glue a heading and a body paragraph into the same `<p>` (Pattern C above).

Bullet rules:
- Always `<ul><li><p>…</p></li>…</ul>` (matches the corpus norm — even the postings that look "clean" use this structure).
- No nested lists.
- No bullets inside the section-heading paragraph.

### Recommendation 2 — Run a one-time scrub script over existing postings

Use the same machine-readable rules to bulk-fix all 94 deviating postings:

| Issue | Auto-fix |
|---|---|
| Real `<h1>`/`<h2>`/`<h3>` heading tag | Replace with `<p><strong>…</strong></p>`; preserve text. |
| Title-Case heading (`About the Role:`, `What Makes You a Good Fit:`, etc.) | Lowercase to sentence case — match the canonical 5 wordings. |
| Curly apostrophe in canonical heading (`How you'll make an impact:`) | Normalize to ASCII `'`. |
| Heading-glued-to-body (`<p><strong>About the role:<br/></strong>Body…</p>`) | Split into two `<p>`s. |
| Empty `<p></p>` | Delete. |
| Trailing `<br>` inside `<p>` (`<br></p>`) | Strip the `<br>`. |
| ALL-CAPS bolded standalone segment that's actually a category label (`CRM/CPQ:`, `AWS`) | Move into running text or a definition list — do not let it be a top-level bold paragraph. |
| `#LI-AY1` style signoff appearing before the Compensation block | Move into the Compensation block (or remove if it's a duplicate). |
| Mixed straight/curly quotes in body | Normalize all quotes to the same style (curly is fine; just pick one). |

The analyzer included with this report (`careers-audit/analyze_jobs.py`) already produces the per-posting fingerprint and could be extended with a corresponding rewriter pass.

### Recommendation 3 — Publish an authoring guide for hiring managers / recruiters

Most defects look like Word/Google-Doc → Greenhouse paste artifacts (`<br>` instead of paragraph breaks, real `<h1>`/`<h2>`, curly quotes, ALL-CAPS labels, "Title Case" because the source doc capitalized everything). A 1-page authoring guide ("Paste as plain text. Use the Greenhouse heading button, not Bold-and-press-Enter") plus a Greenhouse template will prevent regressions.

### Recommendation 4 — Add a CI/lint check on the careers feed

The audit script in this repo (`careers-audit/analyze_jobs.py`) can run on every careers-page deploy and flag any posting that introduces:

- A real heading tag (`<h1>`–`<h6>`) inside `.prose`.
- An empty `<p></p>`.
- A trailing `<br>` before `</p>`.
- A heading paragraph with `<br>` immediately followed by non-empty text inside the same `<p>`.
- A canonical section heading whose wording or capitalization deviates from the approved list.
- `#LI-*` signoffs appearing before the `Compensation:` heading.

This catches drift before postings go live without requiring manual review.

### Recommendation 5 — De-duplicate postings that are role-identical across geos

The corpus contains several near-identical pairs / triples that differ only by location (e.g. Software Engineer - Simulation & Robotics Engineer in San Mateo and Zurich; Sr/Staff Embedded Software Engineer - Camera Systems in San Mateo and Tampere; Autonomy Engineer - Deep Learning in San Mateo and Zurich; the three EMEA Enterprise Account Manager postings). Today, formatting drift between these "twins" is locked in by hand-maintenance — for example one EMEA Account Manager posting uses Title Case headings and the other doesn't. Publishing each role once and letting candidates pick a location at apply-time would eliminate this entire class of drift.

---

## Appendix A — Per-posting issue table (94 postings with at least one issue)

| # | Job posting (location) | Words | Section heading tag | Issues found |
|---|------------------------|------:|---------------------|--------------|
| 1 | **Revenue Operations Engineer, Quoting Systems** (San Mateo, California, United States - Full-time) | 508 | `h2` | real heading tags: 5x `<h2>` (22-32px)<br>2 empty `<p></p>`<br>4 trailing `<br>` in `<p>`<br>4 ALL-CAPS bolded segment(s)<br>Title Case section heading(s) x1 |
| 2 | **Aviation Compliance Lead** (San Mateo, California, United States - Full-time) | 399 | `h2` | real heading tags: 3x `<h2>` (22-32px)<br>missing 'About the role' heading<br>1 empty `<p></p>`<br>1 trailing `<br>` in `<p>` |
| 3 | **Sales Planning Analyst Intern** (San Mateo, California, United States - Intern) | 596 | `<p><strong>` | heading run-on into body (1x)<br>1 empty `<p></p>`<br>Title Case section heading(s) x1<br>1 `#LI-*` signoff in pre-comp |
| 4 | **Senior People Analytics Analyst** (San Mateo, California, United States - Full-time) | 725 | `<p><strong>` | 2 empty `<p></p>`<br>1 ALL-CAPS bolded segment(s)<br>Title Case section heading(s) x2<br>1 `#LI-*` signoff in pre-comp |
| 5 | **Senior Technical Support Representative - Japan** (Tokyo, Japan - Full-time) | 717 | `h1` | real heading tags: 3x `<h1>` (28-48px)<br>missing 'About the role' heading<br>1 empty `<p></p>`<br>1 `#LI-*` signoff in pre-comp |
| 6 | **Software Engineer - Cloud Simulation & Full-Stack** (San Mateo, California, United States - Full-time) | 552 | `h2` | real heading tags: 5x `<h2>` (22-32px)<br>missing 'About the role' heading<br>2 empty `<p></p>`<br>1 ALL-CAPS bolded segment(s) |
| 7 | **Software Engineer - Cloud Simulation & Full-Stack** (Zurich, Switzerland - Full-time) | 552 | `h2` | real heading tags: 5x `<h2>` (22-32px)<br>missing 'About the role' heading<br>2 empty `<p></p>`<br>1 ALL-CAPS bolded segment(s) |
| 8 | **Aviation Regulatory Program Manager** (US Remote - Full-time) | 493 | `h2` | real heading tags: 3x `<h2>` (22-32px)<br>missing 'About the role' heading<br>2 empty `<p></p>` |
| 9 | **Communications Manager** (US Remote - Full-time) | 425 | `h2` | real heading tags: 3x `<h2>` (22-32px)<br>missing 'About the role' heading<br>3 empty `<p></p>` |
| 10 | **Deployment Coordinator** (US Remote - Full-time) | 422 | `h2` | real heading tags: 4x `<h2>` (22-32px)<br>missing 'About the role' heading<br>4 empty `<p></p>` |
| 11 | **Director, Growth Marketing - Commercial** (San Mateo, California, United States - Full-time) | 596 | `<p><strong>` | 3 empty `<p></p>`<br>8 trailing `<br>` in `<p>`<br>Title Case section heading(s) x1 |
| 12 | **GTM Data Engineer Intern** (San Mateo, California, United States - Intern) | 456 | `<p><strong>` | heading run-on into body (1x)<br>2 empty `<p></p>`<br>2 trailing `<br>` in `<p>` |
| 13 | **Hardware Technician** (San Mateo, California, United States - Full-time) | 376 | `<p><strong>` | heading run-on into body (1x)<br>3 empty `<p></p>`<br>Title Case section heading(s) x1 |
| 14 | **Lead Staff Electrical Engineer (F10 Program)** (San Mateo, California, United States - Full-time) | 318 | `<p><strong>` | heading run-on into body (1x)<br>2 empty `<p></p>`<br>1 trailing `<br>` in `<p>` |
| 15 | **Project Manager, Workplace** (San Mateo, California, United States - Full-time) | 491 | `h3` | real heading tags: 2x `<h3>` (18-28px)<br>missing 'About the role' heading<br>1 empty `<p></p>` |
| 16 | **Senior Revenue Operations Manager** (San Mateo, California, United States - Full-time) | 441 | `<p><strong>` | heading run-on into body (1x)<br>2 empty `<p></p>`<br>Title Case section heading(s) x2 |
| 17 | **Software Engineer - Autonomy Infrastructure, Systems and Tools** (San Mateo, California, United States - Full-time) | 521 | `h2` | real heading tags: 5x `<h2>` (22-32px)<br>missing 'About the role' heading<br>1 empty `<p></p>` |
| 18 | **Software Engineer - Autonomy Infrastructure, Systems and Tools** (Zurich, Switzerland - Full-time) | 521 | `h2` | real heading tags: 5x `<h2>` (22-32px)<br>missing 'About the role' heading<br>1 empty `<p></p>` |
| 19 | **Software Engineer - Simulation & Robotics Engineer** (San Mateo, California, United States - Full-time) | 482 | `h3` | real heading tags: 5x `<h3>` (18-28px)<br>missing 'About the role' heading<br>2 empty `<p></p>` |
| 20 | **Software Engineer - Simulation & Robotics Engineer** (Zurich, Switzerland - Full-time) | 482 | `h3` | real heading tags: 5x `<h3>` (18-28px)<br>missing 'About the role' heading<br>2 empty `<p></p>` |
| 21 | **Software Engineer Intern Fall 2026/Winter 2027** (US CA San Mateo - Intern) | 528 | `<p><strong>` | heading run-on into body (1x)<br>3 empty `<p></p>`<br>1 `#LI-*` signoff in pre-comp |
| 22 | **Autonomy Engineer - Deep Learning Infrastructure** (San Mateo, California, United States - Full-time) | 481 | `<p><strong>` | missing 'About the role' heading<br>1 empty `<p></p>` |
| 23 | **Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026** (San Mateo, California, United States - Intern) | 524 | `<p><strong>` | 1 trailing `<br>` in `<p>`<br>1 `#LI-*` signoff in pre-comp |
| 24 | **Deployment Engineer - Southeast** (US Remote - Full-time) | 595 | `<p><strong>` | heading run-on into body (1x)<br>5 empty `<p></p>` |
| 25 | **Director of Product Management, Drone as First Responder (DFR)** (San Mateo, California, United States - Full-time) | 875 | `<p><strong>` | heading run-on into body (1x)<br>1 `#LI-*` signoff in pre-comp |
| 26 | **Field Marketing Event Manager** (San Mateo, California, United States - Full-time) | 518 | `h3` | real heading tags: 7x `<h3>` (18-28px)<br>Title Case section heading(s) x3 |
| 27 | **Field Support Representative (Southwest, Remote)** (US Remote - Full-time) | 712 | `<p><strong>` | heading run-on into body (1x)<br>2 empty `<p></p>` |
| 28 | **GTM Enablement Associate** (San Mateo, California, United States - Full-time) | 374 | `<p><strong>` | heading run-on into body (1x)<br>1 empty `<p></p>` |
| 29 | **Hardware Test and Reliability Intern** (San Mateo, California, United States - Intern) | 565 | `<p><strong>` | 1 empty `<p></p>`<br>1 `#LI-*` signoff in pre-comp |
| 30 | **PhD Autonomy Engineer Intern - Deep Learning or Computer Vision** (San Mateo, California, United States - Intern) | 521 | `<p><strong>` | 1 trailing `<br>` in `<p>`<br>1 `#LI-*` signoff in pre-comp |
| 31 | **PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning)** (Zurich, Switzerland - Intern) | 442 | `h3` | real heading tags: 3x `<h3>` (18-28px)<br>2 ALL-CAPS bolded segment(s) |
| 32 | **Product Support Engineer** (San Mateo, California, United States - Full-time) | 581 | `<p><strong>` | missing 'About the role' heading<br>2 empty `<p></p>` |
| 33 | **Product Support Engineer Intern** (San Mateo, California, United States - Intern) | 441 | `<p><strong>` | missing 'About the role' heading<br>3 empty `<p></p>` |
| 34 | **Production Manager, PM Shift** (Hayward, California, United States - Full-time) | 295 | `<p><strong>` | 3 empty `<p></p>`<br>Title Case section heading(s) x3 |
| 35 | **Program Leader, Law Enforcement & Public Safety Training** (San Mateo, California, United States - Full-time) | 559 | `<p><strong>` | heading run-on into body (1x)<br>Title Case section heading(s) x2 |
| 36 | **Program Manager, Major Deployments (Hawaii)** (San Mateo, California, United States - Full-time) | 596 | `<p><strong>` | 3 empty `<p></p>`<br>Title Case section heading(s) x1 |
| 37 | **Program Manager, Major Deployments (Mid Atlantic)** (US Remote - Full-time) | 603 | `<p><strong>` | 3 empty `<p></p>`<br>Title Case section heading(s) x1 |
| 38 | **Program Manager, Major Deployments (South East)** (US Remote - Full-time) | 597 | `<p><strong>` | 3 empty `<p></p>`<br>Title Case section heading(s) x1 |
| 39 | **Senior Autonomy Engineer - Data Curation** (San Mateo, California, United States - Full-time) | 436 | `<p><strong>` | 4 empty `<p></p>`<br>Title Case section heading(s) x3 |
| 40 | **Senior Autonomy Engineer - Deep Learning** (San Mateo, California, United States - Full-time) | 314 | `<p><strong>` | heading run-on into body (1x)<br>1 empty `<p></p>` |
| 41 | **Senior Brand Designer (Contract)** (San Mateo, California, United States - Full-time) | 501 | `<p><strong>` | 3 empty `<p></p>`<br>Title Case section heading(s) x1 |
| 42 | **Senior Buyer** (Hayward, California, United States - Full-time) | 478 | `h2` | real heading tags: 2x `<h2>` (22-32px)<br>3 empty `<p></p>` |
| 43 | **Senior Customer Support Representative - India** (Bangalore, India - Full-time) | 611 | `<p><strong>` | heading run-on into body (1x)<br>1 empty `<p></p>` |
| 44 | **Senior Product Manager, Platform & Infrastructure** (San Mateo, California, United States - Full-time) | 767 | `<p><strong>` | heading run-on into body (1x)<br>6 empty `<p></p>` |
| 45 | **Senior Software Engineer - Mobile Platform** (San Mateo, California, United States - Full-time) | 530 | `<p><strong>` | 3 empty `<p></p>`<br>Title Case section heading(s) x3 |
| 46 | **Senior/Staff Embedded Software Engineer – Camera Systems** (San Mateo, California, United States - Full-time) | 394 | `<p><strong>` | 4 empty `<p></p>`<br>Title Case section heading(s) x3 |
| 47 | **Sr/Staff Embedded Software Engineer - Camera Systems** (Tampere, Finland - Full-time) | 394 | `<p><strong>` | 4 empty `<p></p>`<br>Title Case section heading(s) x3 |
| 48 | **Staff Product Manager, Cameras & Sensors** (San Mateo, California, United States - Full-time) | 713 | `<p><strong>` | missing 'About the role' heading<br>1 `#LI-*` signoff in pre-comp |
| 49 | **Staff Product Manager, Platform & Infrastructure** (San Mateo, California, United States - Full-time) | 786 | `<p><strong>` | heading run-on into body (1x)<br>6 empty `<p></p>` |
| 50 | **Success Systems Specialist** (US Remote - Full-time) | 729 | `<p><strong>` | 1 empty `<p></p>`<br>Title Case section heading(s) x2 |
| 51 | **Supplier Quality Engineer, Sustaining** (Taiwan - Full-time) | 566 | `<p><strong>` | 1 empty `<p></p>`<br>1 `#LI-*` signoff in pre-comp |
| 52 | **Technical FP&A Analyst** (San Mateo, California, United States - Full-time) | 359 | `<p><strong>` | 1 empty `<p></p>`<br>Title Case section heading(s) x1 |
| 53 | **Wireless Hardware Engineer Intern** (San Mateo, California, United States - Intern) | 551 | `<p><strong>` | 1 empty `<p></p>`<br>1 `#LI-*` signoff in pre-comp |
| 54 | **Workplace Experience Coordinator Part-Time** (Zurich, Switzerland - Part-time) | 486 | `<p><strong>` | heading run-on into body (1x)<br>1 empty `<p></p>` |
| 55 | **Autonomy Engineer - Deep Learning Infrastructure** (Zurich, Switzerland - Full-time) | 448 | `<p><strong>` | heading run-on into body (1x) |
| 56 | **Autonomy Engineer - Deep Learning Model Acceleration** (Zurich, Switzerland - Full-time) | 449 | `<p><strong>` | heading run-on into body (1x) |
| 57 | **Autonomy Engineer - Deep Learning Model Acceleration** (San Mateo, California, United States - Full-time) | 449 | `<p><strong>` | heading run-on into body (1x) |
| 58 | **Autonomy Engineer - Fixed Wing Planning & Controls** (San Mateo, California, United States - Full-time) | 260 | `<p><strong>` | Title Case section heading(s) x3 |
| 59 | **Autonomy Engineer Intern Fall 2026** (San Mateo, California, United States - Intern) | 434 | `<p><strong>` | 1 `#LI-*` signoff in pre-comp |
| 60 | **Autonomy Software Engineer** (San Mateo, California, United States - Full-time) | 392 | `<p><strong>` | heading run-on into body (1x) |
| 61 | **Customer Success Manager, DFR Majors - Northeast** (US Remote - Full-time) | 499 | `<p><strong>` | heading run-on into body (1x) |
| 62 | **Electric Motor / Propulsion Engineer** (San Mateo, California, United States - Full-time) | 284 | `<p><strong>` | heading run-on into body (1x) |
| 63 | **Engineering Manager - Autonomy** (San Mateo, California, United States - Full-time) | 338 | `<p><strong>` | 1 trailing `<br>` in `<p>` |
| 64 | **Enterprise Account Manager (MoD/ MoI) – EMEA (Finland)** (Tampere, Finland - Full-time) | 602 | `<p><strong>` | Title Case section heading(s) x3 |
| 65 | **Enterprise Account Manager (MoD/ MoI) – EMEA (Germany)** (Germany - Full-time) | 602 | `<p><strong>` | Title Case section heading(s) x3 |
| 66 | **Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland)** (Zurich, Switzerland - Full-time) | 602 | `<p><strong>` | Title Case section heading(s) x3 |
| 67 | **Enterprise Account Manager, US Army** (US Remote - Full-time) | 471 | `<p><strong>` | Title Case section heading(s) x3 |
| 68 | **Enterprise Account Manager, US Navy, US Marine Corps, and IC/SOCOM** (US Remote - Full-time) | 508 | `<p><strong>` | Title Case section heading(s) x3 |
| 69 | **Hardware Operations Program Manager** (Hayward, California, United States - Full-time) | 379 | `<p><strong>` | 3 empty `<p></p>` |
| 70 | **Head of Warehouse & Logistics Operations** (US CA Production - Full-time) | 447 | `<p><strong>` | 2 empty `<p></p>` |
| 71 | **Manufacturing Quality Supervisor** (Hayward, California, United States - Full-time) | 371 | `<p><strong>` | 1 empty `<p></p>` |
| 72 | **Product Design Engineer (All Levels)** (San Mateo, California, United States - Full-time) | 448 | `<p><strong>` | heading run-on into body (1x) |
| 73 | **Production Supervisor** (Hayward, California, United States - Full-time) | 294 | `<p><strong>` | 1 empty `<p></p>` |
| 74 | **RF Design Engineer** (San Mateo, California, United States - Full-time) | 391 | `<p><strong>` | Title Case section heading(s) x3 |
| 75 | **RMA & Repair Program Manager** (Hayward, California, United States - Full-time) | 422 | `<p><strong>` | 1 empty `<p></p>` |
| 76 | **Senior Autonomy Engineer - Controls** (San Mateo, California, United States - Full-time) | 245 | `<p><strong>` | Title Case section heading(s) x3 |
| 77 | **Senior Autonomy Engineer - Deep Learning** (Zurich, Switzerland - Full-time) | 314 | `<p><strong>` | heading run-on into body (1x) |
| 78 | **Senior Software Engineer - Security** (San Mateo, California, United States - Full-time) | 418 | `<p><strong>` | Title Case section heading(s) x1 |
| 79 | **Senior Software Engineer, Frontend** (San Mateo, California, United States - Full-time) | 350 | `<p><strong>` | Title Case section heading(s) x3 |
| 80 | **Senior Software Engineer, Full Stack** (San Mateo, California, United States - Full-time) | 623 | `<p><strong>` | 1 trailing `<br>` in `<p>` |
| 81 | **Senior Software Engineer, Infrastructure** (San Mateo, California, United States - Full-time) | 400 | `<p><strong>` | heading run-on into body (1x) |
| 82 | **Senior Staff Product Manager, Drone Hardware Platforms & Sensors** (San Mateo, California, United States - Full-time) | 508 | `<p><strong>` | Title Case section heading(s) x1 |
| 83 | **Senior Supplier Quality Engineer** (San Mateo, California, United States - Full-time) | 434 | `<p><strong>` | 1 empty `<p></p>` |
| 84 | **Senior Technical Recruiter** (San Mateo, California, United States - Full-time) | 433 | `<p><strong>` | missing 'About the role' heading |
| 85 | **Senior Technical Recruiter - Hardware Operations** (San Mateo, California, United States - Full-time) | 440 | `<p><strong>` | heading run-on into body (1x) |
| 86 | **Software Engineer - Infrastructure** (San Mateo, California, United States - Full-time) | 398 | `<p><strong>` | heading run-on into body (1x) |
| 87 | **Solutions Engineer - Public Safety - East North Central US** (US Remote - Full-time) | 440 | `<p><strong>` | Title Case section heading(s) x3 |
| 88 | **Staff Global Supply Manager, Mechanicals** (San Mateo, California, United States - Full-time) | 546 | `<p><strong>` | 1 empty `<p></p>` |
| 89 | **Staff Software Engineer, Full Stack** (San Mateo, California, United States - Full-time) | 613 | `<p><strong>` | missing 'About the role' heading |
| 90 | **Supply Chain Intern** (San Mateo, California, United States - Intern) | 416 | `<p><strong>` | 1 `#LI-*` signoff in pre-comp |
| 91 | **Technical Support Specialist - West Coast** (US Remote - Full-time) | 620 | `<p><strong>` | missing 'About the role' heading |

## Appendix B — Postings with no detected deviations from the norm

These **22 postings** (19% of the corpus) follow the standard pattern: sentence-case bold-paragraph headings, `<li><p>…</p></li>` lists, no real heading tags, no inline styles, no empty paragraphs, no trailing line breaks, no signoff leakage.

- Wireless Software Engineer (San Mateo)
- Senior NPI Product Quality Engineer (San Mateo)
- Mission Success Operations Manager (US Remote)
- Staff Software Engineer, Frontend (San Mateo)
- Autonomy Engineer Intern - Deep Learning (Computational Photography) (Zurich & Tampere)
- Autonomy Engineer Intern - Deep Learning (Computational Photography) (San Mateo)
- Senior Software Engineer - Embedded (San Mateo)
- Electrical Engineer (Sustaining/Validation) (San Mateo)
- Senior Business Recruiter (San Mateo)
- Systems Integration and Test Engineer (Mid to Senior Level) (San Mateo)
- Autonomy Engineer - Deep Learning (Zurich)
- Senior Software Engineer, Data Platform (San Mateo)
- Field Support Representative (US Remote)
- Staff Software Engineer - Embedded (San Mateo)
- Senior Hardware Test and Reliability Engineer (San Mateo)
- Staff Technical Recruiter (San Mateo)
- Autonomy Engineer - Deep Learning (San Mateo)
- PCB Layout Engineer (San Mateo)
- Software Engineer - Embedded (San Mateo)
- Software Engineer, Full Stack (San Mateo)
- Electrical Engineer (all levels) (San Mateo)
- Senior Wireless Systems Performance Engineer (San Mateo)

> Use any of these as the gold reference when re-templating the others.

---

## Appendix C — Tooling

- [`careers-audit/analyze_jobs.py`](./careers-audit/analyze_jobs.py) — analyzer that extracts pre-compensation HTML, fingerprints each posting, and prints the aggregate report on stdout.
- [`careers-audit/analysis.json`](./careers-audit/analysis.json) — full per-posting fingerprint dataset.
- [`careers-audit/per_job_issues.csv`](./careers-audit/per_job_issues.csv) — flat CSV of per-posting issues for spreadsheet review.
- [`careers-audit/job_links.txt`](./careers-audit/job_links.txt) — list of the 113 source URLs analyzed.

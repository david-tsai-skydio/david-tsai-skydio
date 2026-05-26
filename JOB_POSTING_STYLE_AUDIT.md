# Skydio Careers — Job Posting Style Consistency Audit

**Source:** [https://www.skydio.com/careers](https://www.skydio.com/careers)
**Audit date:** 2026-05-26
**Scope:** Visual formatting of the job description body **up to (and excluding) the "Compensation" block** on every individual posting page.
**Postings analyzed:** 106 live job postings (full list at the end of this document).

---

## TL;DR

> Skydio's `/careers` index page is visually consistent, but the **individual posting pages drift in five major ways**: section-header element type (and therefore size/weight), section-header label wording and capitalization, paragraph-vs-`<br>` separation, list-item wrapping (`<li><p>...</p></li>` vs bare `<li>`), and stray markup leaked in from external editors (e.g. Google Docs paste artefacts, underlines, italics, an inline `<div>` with an inline style).
>
> The single most disruptive outlier is **"Senior Technical Support Representative – Japan"**, which renders its section headers in `<h1>` (~48 px) instead of the inline body bold (~16 px) used by 88 of 106 postings — a ~3× size difference on the same page template. The Hardware Engineering Program Manager posting mixes `<h2>` and `<h3>` within the same posting. **18 postings use `<br><br>` instead of separate `<p>` blocks** (creating tighter vertical rhythm than the rest of the corpus), and **one posting (Manager, Logistics) contains a stray `<div style="min-height:1.2em;…">`** — a classic Google-Docs paste leftover.

---

## 1. How the page is rendered (font reference)

The careers site wraps every job description in `<div class="prose block-content">…</div>`. The `.prose` rule set provides the only font-sizing and weight in play; all visible inconsistencies are driven by **which HTML tag the recruiter chose to use** for headings and paragraph breaks. The relevant CSS values (extracted from the live page CSS) are:

| Element in `.prose` | Computed `font-size` (clamp range) | At desktop ≥1440 px | `font-weight` |
|---|---|---|---|
| `<h1>` | `clamp(1.75rem, .73rem + 2.84vw, 3rem)` | **~48 px** | 500 (medium) |
| `<h2>` | `clamp(1.375rem, .86rem + 1.42vw, 2rem)` | **~32 px** | 500 (medium) |
| `<h3>` | `clamp(1.125rem, .61rem + 1.42vw, 1.75rem)` | **~28 px** | 500 (medium) |
| `<h4>` | `clamp(1.375rem, 1.27rem + .28vw, 1.5rem)` | **~24 px** | 500 (medium) |
| `<h5>` | `clamp(1.125rem, .92rem + .57vw, 1.375rem)` | **~22 px** | 500 (medium) |
| `<h6>` | `clamp(1rem, .9rem + .28vw, 1.125rem)` | **~18 px** | 500 (medium) |
| `<p><strong>…</strong></p>` (body bold) | inherits body | **~16 px** | 700 (bold) |
| `<p>` body copy | inherits body | **~16 px** | 400 |

Practical consequence: a section title that one recruiter wrote as `<h2>` is rendered **2× larger and lighter-weight** than the same section title written by another recruiter as `<p><strong>`. The reader perceives the postings as belonging to different pages even though they sit under one URL pattern.

---

## 2. Findings (sorted by visual impact)

### 2.1 Section-header element is inconsistent across 106 postings  *(highest visual impact)*

| Header style used for section titles | # postings | % | Approx. rendered size & weight |
|---|---:|---:|---|
| `<p><strong>Section:</strong></p>` (body bold) | **88** | 83.0% | 16 px / weight 700 |
| `<h2>` | 9 | 8.5% | 32 px / weight 500 |
| `<h3>` | 5 | 4.7% | 28 px / weight 500 |
| `<h2>` **and** `<h3>` mixed in one posting | 1 | 0.9% | 32 px **and** 28 px |
| `<h1>` (entire posting) | 1 | 0.9% | **48 px** / weight 500 |
| No section headers at all (inline run-in bold) | 2 | 1.9% | 16 px / weight 700 |

#### The outliers (call out by name)

| Title | Location | Issue | Effect |
|---|---|---|---|
| **Senior Technical Support Representative – Japan** | Tokyo, Japan | Uses `<h1>` for **every** section ("About the role:", "How you'll make an impact:", "What would make you a good fit:") | Headers render at ~48 px — roughly **3× the size** of the same headers in 88 other postings |
| **Hardware Engineering Program Manager** | San Mateo, CA | Mixes `<h2>` (3×) **and** `<h3>` (5×) inside one posting | Two different "section-header" sizes within the same page (~32 px and ~28 px) — the reader can't tell which is the higher-level section |
| Software Engineer – Autonomy Infrastructure, Systems & Tools (SM **and** Zurich) | San Mateo / Zurich | `<h2>×5` each — section headers render at 32 px | Looks like a separate template; dwarfs the rest of the listing index |
| Software Engineer – Cloud Simulation & Full-Stack (SM **and** Zurich) | San Mateo / Zurich | `<h2>×5` each | Same as above |
| Aviation Compliance Lead | San Mateo, CA | `<h2>×3` | 32 px section headers |
| Aviation Regulatory Program Manager | US Remote | `<h2>×3` | 32 px section headers |
| Communications Manager | US Remote | `<h2>×3` | 32 px section headers |
| Senior Buyer | Hayward, CA | `<h2>×2` (but later sections fall back to `<p><strong>`) — **mixed in one posting** | Reader sees the first two sections "shout" then the rest go quiet |
| Revenue Operations Engineer, Quoting Systems | San Mateo, CA | `<h2>×5` **plus** `<br>×4` **plus** later `<p><strong>` sections — three different header styles in one posting | Worst single-posting inconsistency |
| Software Engineer – Simulation & Robotics Engineer (SM **and** Zurich) | San Mateo / Zurich | `<h3>×5` each | 28 px headers — quieter than `<h2>` postings, louder than the 88 `<p><strong>` postings |
| Full Stack Product Counsel | San Mateo, CA | `<h3>×4` **plus** an `<u>` underline | 28 px headers + non-link underlined text |
| PhD Autonomy Engineer Intern – Planning & Controls (RL) | Zurich | `<h3>×3` plus a 1,892-character bullet list wrapped in `<p><strong>` (the bullets were pasted with no line breaks — see §2.4) | Section header size mismatches and one giant bolded mega-paragraph |
| Senior Business Operations Manager | San Mateo, CA | `<h3>×3` mixed with `<p><strong>×3` | Mixed sizes within one posting |
| Product Support Engineer (full-time **and** intern) | San Mateo, CA | **No standalone section headers at all** — section labels are bolded run-in to the first sentence (e.g. `<strong>About the role</strong>: Skydio is looking for…`) | Visually flattens the posting; reader has no scannable anchors |

### 2.2 Section-header wording, capitalization, and apostrophes are all over the map

Every section header is written by hand in the recruiter's editor — there is no canonical phrasing or casing. Here are the live variants observed in pre-compensation content (counts are *occurrences* across all 106 postings):

| Canonical concept | Variants in use today | Counts |
|---|---|---|
| Intro to the role | `About the role`, `About the Role`, `About The Role` | **47 / 31 / 1** |
| Team intro | `About the team`, `About the Team` | 6 / 8 |
| Responsibilities header | `How you'll make an impact`<br>`How You'll Make an Impact`<br>`How you'll make an impact`<br>`How You'll Make an Impact`<br>`How you will make an impact`<br>(plus 1 case where the header text is concatenated to the *previous* paragraph with no break: `Location: SF/Bay area - hybrid 3 days in officeHow You'll Make an Impact`) | 27 / 19 / 9 / 1 / 4 / 1 |
| Qualifications header | `What makes you a good fit`<br>`What Makes You a Good Fit`<br>`What Makes You A Good Fit` ("A" capitalised)<br>`What would make you a good fit`<br>`What Would Make You a Good Fit`<br>`What makes you a strong fit`<br>`What Makes You a Great Fit`<br>`What makes this internship different`<br>`What Makes Your a Good Fit` (typo: "Your" instead of "You") | 49 / 19 / 2 / 6 / 1 / 4 / 1 / 1 / **1 (typo)** |
| "Nice to have" header | `Bonus Experience` / `Bonus Points` / `Bonus points` / `Bonus points for` / `Nice to have` / `Nice to Have` / `Nice To Haves` / `Nice-to-Haves` / `Additional Desired Experience and Skills` / `Preferred Qualifications` / `Useful skills and experience` | 6 / 3 / 2 / 4 / 2 / 1 / 1 / 1 / 1 / 3 / 2 |
| Generic qualifications | `Qualifications`, `Minimum Qualifications`, `Desired Qualifications`, `Requirements`, `Key Responsibilities`, `Areas of Responsibility` | 7 / 1 / 1 / 1 / 1 / 6 |

**~50 distinct section-name spellings are in production today.** The closest thing to a "standard" set is `About the role:` → `How you'll make an impact:` → `What makes you a good fit:` (~50% of postings), but even within that set roughly half use sentence case ("About the role") and half use title case ("About the Role").

Three smaller but real issues are bundled in here:
1. **Straight vs. curly apostrophes** are used interchangeably even for the same phrase ("How you'll" vs "How you'll" — 27 vs. 19+9 occurrences). This is a *visible* glyph difference, not just a code-point difference.
2. **Trailing-colon placement is inconsistent.** Most postings put the colon **inside** the `<strong>` (`<strong>About the role:</strong>`), but **2 postings** (Product Support Engineer + Product Support Engineer Intern) put the colon **outside**: `<strong>About the role</strong>:  Skydio is…`. **Technical Support Specialist – West Coast** has `<strong>About the role</strong>:&nbsp;` — colon outside *and* trailing non-breaking space. Also several postings (Software Engineer – Embedded, Senior Software Engineer – Embedded, Staff Software Engineer – Embedded, Director / Senior Director of PM DFR) use `<strong>About the role:&nbsp;</strong>` — non-breaking space inside the strong tag.
3. **Trailing whitespace inside `<strong>`** appears in 6 postings (e.g. `<strong>About the Role: </strong>` in Senior Business Operations Manager, Lead Staff Electrical Engineer, Software Engineer – Autonomy Infrastructure), which on some browsers produces a phantom underline gap if the strong is ever styled with `text-decoration`.

### 2.3 Two distinct opening paragraphs are in production

The "Skydio is the leading US drone company…" intro paragraph exists in **two visually different forms**:

| Variant | # postings | Visual effect |
|---|---:|---|
| **Plain text** ("…from utility inspectors to first responders, soldiers in battlefield scenarios and beyond.") | 41 | All black, single weight |
| **Hyperlinked** ("…from [utility inspectors](…) to [first responders](…), [soldiers in battlefield scenarios](…), and [beyond](…).") | 65 | Four blue underlined hyperlinks in the very first sentence |

There is no apparent pattern to the split (both versions appear across R&D, Sales, Operations, Marketing roles in the US and abroad), so this looks like a copy-paste accident rather than intentional segmentation.

### 2.4 Paragraph spacing is faked with `<br><br>` in 18 postings

Most postings use the standard pattern of separating intro paragraphs with `</p><p>` (which gives the spacing defined by the `.prose` rule for paragraph margins). **18 postings (17%) instead use one large `<p>` that contains `<br><br>` separators.** This renders with *less* vertical whitespace between visual paragraphs than the rest of the corpus.

| Posting | `<br>` count | Notes |
|---|---:|---|
| **IT Technician (Help Desk – Linux Focus)** | **9** | Worst offender — uses `<br>` repeatedly inside `<li>` content as well |
| Autonomy Engineer – Deep Learning Infrastructure (San Mateo) | 8 | Intro + section header all one `<p>` with `<br><br>` separators |
| Director, Growth Marketing – Commercial | 8 | Also contains the only `<em>` in this branch of the corpus |
| Autonomy Engineer – DL Infrastructure (Zurich) | 6 | Same template as San Mateo twin |
| Autonomy Engineer – DL Model Acceleration (Zurich & San Mateo) | 6 each | Same template |
| Autonomy Software Engineer (San Mateo) | 4 | |
| Director of Product Management, DFR | 4 | |
| Software Engineer Intern Fall 2026 / Winter 2027 | 4 | |
| Revenue Operations Engineer, Quoting Systems | 4 | Already flagged for `<h2>` mixing |
| Senior Technical Recruiter – Hardware Operations | 3 | Already flagged for `<u>` |
| GTM Data Engineer Intern | 3 | Bullets also pasted as one mega-paragraph (see below) |
| Senior Autonomy Engineer – Deep Learning (SM & Zurich) | 2 | |
| Senior Director PM DFR | 2 | |
| Senior Brand Designer (Contract) | 2 | |
| Product Support Engineer (full-time & intern) | 2 each | Already flagged in §2.1 |
| Senior Technical Support Representative – Japan | 2 | Already flagged for `<h1>` |
| Plus another ~7 postings with 1–2 `<br>` tags | — | |

### 2.5 "Bulleted lists pasted as a single bolded paragraph"

A close cousin of the `<br>` issue. In **6 postings**, the recruiter pasted a bulleted list from an external editor and the bullets collapsed into a single run-on paragraph wrapped in `<p><strong>…</strong></p>` (no line breaks, no `<ul>`/`<li>`). All bullets render as one giant bold paragraph at body-bold size, with the *next* section header concatenated to the end. Examples:

- **PhD Autonomy Engineer Intern – Planning & Controls (Reinforcement Learning)** — 1,892-character `<strong>` blob containing the entire "Responsibilities" *and* "What makes this internship different" *and* "What makes you a strong fit" sections.
- **Senior Product Manager, Platform & Infrastructure** — 2,064-character `<strong>` blob containing 7 bullet topics ("Customer & sales engagement", "Own the platform roadmap…", "Productize and deliver Skydio On-Prem", "Drive compliance and certification…", etc.).
- **Staff Product Manager, Platform & Infrastructure** — same 2,064-character blob.
- **Revenue Operations Engineer, Quoting Systems** — 1,115-character `<strong>` blob mashing the entire "Quoting & approvals / Amendments & changes / Catalog readiness / Order handoff / Channel & deal reg / Change management / Ownership boundaries" list together.
- **Hardware Operations Program Manager** — 1,264-character blob containing the responsibilities bullets.
- **GTM Data Engineer Intern** — three separate blobs (541, 966, 788 chars).

### 2.6 List-item structure is inconsistent

`<li>` content is wrapped in `<p>…</p>` in **1,751** of **1,755** list items (the `.prose` CSS gives `<li><p>` an extra top margin). The 4 postings that mix wrapped `<li><p>` with bare `<li>` get **two different bullet vertical spacings within the same posting**:

| Posting | `<li><p>` items | bare `<li>` items |
|---|---:|---:|
| Senior Technical Recruiter | 4 | 1 |
| Senior Technical Recruiter – Hardware Operations | 4 | 1 |
| Staff Technical Recruiter | 4 | 1 |
| Sales Planning Analyst Intern | 1 | 1 |

(All three Technical Recruiter postings share the same template — fixing one will likely fix all three.)

### 2.7 Stray inline styling

| Posting | Issue |
|---|---|
| **Manager, Logistics** (Hayward, CA) | Contains the corpus's **only inline `style` attribute**: `<div style="min-height:1.2em;margin-top:0;margin-bottom:0"> </div>`. This is a classic Google-Docs paste artefact. It also contains the corpus's only `<div>` inside the prose content. |

### 2.8 Underline (`<u>`) used as emphasis in 7 postings

Plain `<u>` tags render as underlines that look identical to hyperlinks, which is an accessibility/UX antipattern. Every other posting uses `<strong>` for emphasis.

| Posting | Where the `<u>` appears |
|---|---|
| Lead Staff Electrical Engineer | Underline used to emphasise an instruction line |
| Senior Software Engineer, Full Stack | Underlined phrase inside a bullet |
| Full Stack Product Counsel | Underline (also uses `<h3>` headings) |
| Senior NPI Product Quality Engineer | Underline **plus** the only other `<em>` in the corpus |
| Senior Technical Recruiter | Underline (template shared by the three recruiter postings) |
| Senior Technical Recruiter – Hardware Operations | Underline |
| Staff Technical Recruiter | Underline |

### 2.9 Italic (`<em>`) appears only twice

| Posting | Notes |
|---|---|
| Senior NPI Product Quality Engineer | Single `<em>` in pre-compensation content |
| Director, Growth Marketing – Commercial | Single `<em>` in pre-compensation content |

Both should either be normalised (drop the italic, or convert to `<strong>` like the rest of the corpus does for emphasis).

### 2.10 Heading on the post-compensation block: missing compensation in a US role

This sits just *after* the in-scope text but is worth mentioning because it's an obvious omission: **the US-based posting "Autonomy Engineer Intern – Deep Learning (Computational Photography), San Mateo, CA"** has no compensation block at all. The four other postings without a compensation block are all international (Zurich, Tokyo, Taiwan) where pay-disclosure laws differ — but the San Mateo intern role should match its US peers.

---

## 3. Per-posting summary table

Postings are sorted by *severity of formatting deviation from the corpus norm*. The "Header style" column shows which HTML element the posting uses for its section titles; the norm (used by 88/106 postings) is `P+STRONG (body)`.

| # | Title | Location | Header style | Notable formatting flags |
|---|---|---|---|---|
| 1 | Senior Technical Support Representative - Japan | Tokyo, Japan | H1 | h1, br×2, NO comp block |
| 2 | Hardware Engineering Program Manager | San Mateo, California, United States | H2+H3 mixed | h2×3, h3×5 |
| 3 | Aviation Compliance Lead | San Mateo, California, United States | H2 | h2×3 |
| 4 | Aviation Regulatory Program Manager | US Remote | H2 | h2×3 |
| 5 | Communications Manager | US Remote | H2 | h2×3 |
| 6 | Revenue Operations Engineer, Quoting Systems | San Mateo, California, United States | H2 | h2×5, br×4 |
| 7 | Senior Buyer | Hayward, California, United States | H2 | h2×2 |
| 8 | Software Engineer - Autonomy Infrastructure, Systems and Tools | San Mateo, California, United States | H2 | h2×5 |
| 9 | Software Engineer - Autonomy Infrastructure, Systems and Tools | Zurich, Switzerland | H2 | h2×5 |
| 10 | Software Engineer - Cloud Simulation &amp; Full-Stack | San Mateo, California, United States | H2 | h2×5 |
| 11 | Software Engineer - Cloud Simulation &amp; Full-Stack | Zurich, Switzerland | H2 | h2×5 |
| 12 | Full Stack Product Counsel | San Mateo, California, United States | H3 | h3×4, underline `<u>` |
| 13 | PhD Autonomy Engineer Intern - Planning &amp; Controls (Reinforcement Learning) | Zurich, Switzerland | H3 | h3×3 |
| 14 | Senior Business Operations Manager | San Mateo, California, United States | H3 | h3×3 |
| 15 | Software Engineer - Simulation &amp; Robotics Engineer | Zurich, Switzerland | H3 | h3×5 |
| 16 | Software Engineer - Simulation &amp; Robotics Engineer | San Mateo, California, United States | H3 | h3×5 |
| 17 | Autonomy Engineer - Deep Learning | San Mateo, California, United States | P+STRONG (body) |  |
| 18 | Autonomy Engineer - Deep Learning | Zurich, Switzerland | P+STRONG (body) |  |
| 19 | Autonomy Engineer - Deep Learning Infrastructure | Zurich, Switzerland | P+STRONG (body) | br×6 |
| 20 | Autonomy Engineer - Deep Learning Infrastructure | San Mateo, California, United States | P+STRONG (body) | br×8 |
| 21 | Autonomy Engineer - Deep Learning Model Acceleration | Zurich, Switzerland | P+STRONG (body) | br×6 |
| 22 | Autonomy Engineer - Deep Learning Model Acceleration | San Mateo, California, United States | P+STRONG (body) | br×6 |
| 23 | Autonomy Engineer - Fixed Wing Planning &amp; Controls | San Mateo, California, United States | P+STRONG (body) |  |
| 24 | Autonomy Engineer - ML &amp; DL Infrastructure | San Mateo, California, United States | P+STRONG (body) |  |
| 25 | Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 | San Mateo, California, United States | P+STRONG (body) |  |
| 26 | Autonomy Engineer Intern - Deep Learning (Computational Photography) | San Mateo, California, United States | P+STRONG (body) | NO comp block |
| 27 | Autonomy Engineer Intern - Deep Learning (Computational Photography) | Zurich, Switzerland | P+STRONG (body) | NO comp block |
| 28 | Autonomy Engineer Intern Fall 2026 | San Mateo, California, United States | P+STRONG (body) |  |
| 29 | Autonomy Software Engineer | San Mateo, California, United States | P+STRONG (body) | br×4 |
| 30 | Customer Success Manager, DFR Majors - Northeast | US Remote | P+STRONG (body) |  |
| 31 | Customer Success Manager, DFR Majors - Southeast | US Remote | P+STRONG (body) |  |
| 32 | Deployment Engineer - Southeast | US Remote | P+STRONG (body) |  |
| 33 | Director of Product Management, Drone as First Responder (DFR) | San Mateo, California, United States | P+STRONG (body) | br×4 |
| 34 | Director, Global Supply Management - Mechanicals | San Mateo, California, United States | P+STRONG (body) |  |
| 35 | Director, Growth Marketing - Commercial | San Mateo, California, United States | P+STRONG (body) | italic `<em>`, br×8 |
| 36 | Electrical Engineer (Sustaining/Validation) | San Mateo, California, United States | P+STRONG (body) |  |
| 37 | Electrical Engineer (all levels) | San Mateo, California, United States | P+STRONG (body) | br×2 |
| 38 | Engineering Manager - Autonomy | San Mateo, California, United States | P+STRONG (body) |  |
| 39 | Enterprise Account Manager (MoD/ MoI) – EMEA (Finland) | Tampere, Finland | P+STRONG (body) | br×2 |
| 40 | Enterprise Account Manager (MoD/ MoI) – EMEA (Germany) | Germany | P+STRONG (body) | br×2 |
| 41 | Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland) | Zurich, Switzerland | P+STRONG (body) | br×2 |
| 42 | Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM | US Remote | P+STRONG (body) |  |
| 43 | Enterprise Account Manager, US Army | US Remote | P+STRONG (body) |  |
| 44 | Field Support Representative | US Remote | P+STRONG (body) |  |
| 45 | Field Support Representative (Southwest, Remote) | US Remote | P+STRONG (body) |  |
| 46 | GTM Data Engineer Intern | San Mateo, California, United States | P+STRONG (body) | br×3 |
| 47 | GTM Enablement Associate | San Mateo, California, United States | P+STRONG (body) | br×2 |
| 48 | Hardware Operations Program Manager | Hayward, California, United States | P+STRONG (body) |  |
| 49 | Head of Warehouse &amp; Logistics Operations | Hayward, California, United States | P+STRONG (body) |  |
| 50 | IT Technician (Help Desk - Linux Focus) | Hayward, California, United States | P+STRONG (body) | br×9 |
| 51 | Lead Staff Electrical Engineer | San Mateo, California, United States | P+STRONG (body) | underline `<u>` |
| 52 | Manager, Logistics | Hayward, California, United States | P+STRONG (body) | stray `<div>`, inline-style |
| 53 | Manager, Technical Support | San Mateo, California, United States | P+STRONG (body) |  |
| 54 | Middleware Software Engineer Intern - Fall 2026 | San Mateo, California, United States | P+STRONG (body) |  |
| 55 | Mission Success Operations Manager | US Remote | P+STRONG (body) |  |
| 56 | PCB Layout Engineer | San Mateo, California, United States | P+STRONG (body) | br×2 |
| 57 | PhD Autonomy Engineer Intern - Deep Learning or Computer Vision | San Mateo, California, United States | P+STRONG (body) |  |
| 58 | Product Design Engineer (All Levels) | San Mateo, California, United States | P+STRONG (body) |  |
| 59 | Production Manager, PM Shift | Hayward, California, United States | P+STRONG (body) |  |
| 60 | Program Manager, Major Deployments (Hawaii) | San Mateo, California, United States | P+STRONG (body) |  |
| 61 | Program Manager, Major Deployments (Mid Atlantic) | US Remote | P+STRONG (body) |  |
| 62 | RF Design Engineer | San Mateo, California, United States | P+STRONG (body) |  |
| 63 | Sales Planning Analyst Intern | San Mateo, California, United States | P+STRONG (body) |  |
| 64 | Senior Autonomy Engineer - Controls | San Mateo, California, United States | P+STRONG (body) |  |
| 65 | Senior Autonomy Engineer - Deep Learning | Zurich, Switzerland | P+STRONG (body) | br×2 |
| 66 | Senior Autonomy Engineer - Deep Learning | San Mateo, California, United States | P+STRONG (body) | br×2 |
| 67 | Senior Brand Designer (Contract) | San Mateo, California, United States | P+STRONG (body) | br×2 |
| 68 | Senior Customer Support Representative - India | Bangalore, India | P+STRONG (body) |  |
| 69 | Senior Director, Product Management, Drone as First Responder (DFR) | San Mateo, California, United States | P+STRONG (body) | br×2 |
| 70 | Senior Hardware Test and Reliability Engineer | San Mateo, California, United States | P+STRONG (body) |  |
| 71 | Senior NPI Product Quality Engineer | San Mateo, California, United States | P+STRONG (body) | underline `<u>`, italic `<em>` |
| 72 | Senior People Analytics Analyst | San Mateo, California, United States | P+STRONG (body) |  |
| 73 | Senior Product Manager, Platform &amp; Infrastructure | San Mateo, California, United States | P+STRONG (body) |  |
| 74 | Senior RF Design Engineer | San Mateo, California, United States | P+STRONG (body) |  |
| 75 | Senior Revenue Operations Manager | San Mateo, California, United States | P+STRONG (body) |  |
| 76 | Senior Software Engineer - Embedded | San Mateo, California, United States | P+STRONG (body) |  |
| 77 | Senior Software Engineer - Mobile Platform | San Mateo, California, United States | P+STRONG (body) |  |
| 78 | Senior Software Engineer - Security | San Mateo, California, United States | P+STRONG (body) |  |
| 79 | Senior Software Engineer,  Data Platform | San Mateo, California, United States | P+STRONG (body) |  |
| 80 | Senior Software Engineer,  Infrastructure | San Mateo, California, United States | P+STRONG (body) |  |
| 81 | Senior Software Engineer, Frontend | San Mateo, California, United States | P+STRONG (body) |  |
| 82 | Senior Software Engineer, Full Stack | San Mateo, California, United States | P+STRONG (body) | underline `<u>` |
| 83 | Senior Technical Recruiter | San Mateo, California, United States | P+STRONG (body) | underline `<u>` |
| 84 | Senior Technical Recruiter - Hardware Operations | San Mateo, California, United States | P+STRONG (body) | underline `<u>`, br×3 |
| 85 | Senior Wireless Systems Performance Engineer | San Mateo, California, United States | P+STRONG (body) |  |
| 86 | Senior/Staff Embedded Software Engineer – Camera Systems | San Mateo, California, United States | P+STRONG (body) |  |
| 87 | Software Engineer - Embedded | San Mateo, California, United States | P+STRONG (body) |  |
| 88 | Software Engineer - Infrastructure | San Mateo, California, United States | P+STRONG (body) |  |
| 89 | Software Engineer Intern Fall 2026/Winter 2027 | San Mateo, California, United States | P+STRONG (body) | br×4 |
| 90 | Software Engineer, Full Stack | San Mateo, California, United States | P+STRONG (body) |  |
| 91 | Sr/Staff Embedded Software Engineer - Camera Systems | Tampere, Finland | P+STRONG (body) |  |
| 92 | Staff Global Supply Manager,  Mechanicals | San Mateo, California, United States | P+STRONG (body) |  |
| 93 | Staff Product Manager, Platform &amp; Infrastructure | San Mateo, California, United States | P+STRONG (body) |  |
| 94 | Staff Software Engineer - Embedded | San Mateo, California, United States | P+STRONG (body) |  |
| 95 | Staff Software Engineer, Frontend | San Mateo, California, United States | P+STRONG (body) |  |
| 96 | Staff Software Engineer, Full Stack | San Mateo, California, United States | P+STRONG (body) |  |
| 97 | Staff Technical Recruiter | San Mateo, California, United States | P+STRONG (body) | underline `<u>` |
| 98 | Success Systems Specialist | US Remote | P+STRONG (body) |  |
| 99 | Supplier Quality Engineer, Sustaining | Taiwan | P+STRONG (body) | NO comp block |
| 100 | Supply Chain Intern | San Mateo, California, United States | P+STRONG (body) | br×2 |
| 101 | Systems Integration and Test Engineer (Mid to Senior Level) | San Mateo, California, United States | P+STRONG (body) |  |
| 102 | Technical Support Specialist - West Coast | US Remote | P+STRONG (body) |  |
| 103 | Wireless Software Engineer | San Mateo, California, United States | P+STRONG (body) |  |
| 104 | Workplace Experience Coordinator Part-Time | Zurich, Switzerland | P+STRONG (body) | NO comp block |
| 105 | Product Support Engineer | San Mateo, California, United States | No headings | br×2 |
| 106 | Product Support Engineer Intern | San Mateo, California, United States | No headings | br×2 |


---

## 4. Recommendations for standardisation

The fixes group into two kinds: a one-time copy/markup cleanup of the 106 existing postings, and a forward-looking template that prevents the drift from coming back.

### 4.1 Adopt a single canonical posting skeleton

Pick **one** of the two style families currently in production and rewrite the rest to match. Recommendation: keep the **majority style** (`<p><strong>Section:</strong></p>`, 88/106 postings) as the canonical because it requires the fewest edits and matches the visual hierarchy the careers team already uses for body bold.

Canonical pre-compensation skeleton:

```html
<p>Skydio is the leading US drone company and the world leader in autonomous flight, the key technology for the future of drones and aerial mobility. The Skydio team combines deep expertise in artificial intelligence, best-in-class hardware and software product development, operational excellence, and customer obsession to empower a broader, more diverse audience of drone users. From utility inspectors to first responders, soldiers in battlefield scenarios and beyond.</p>

<p><strong>About the role:</strong></p>
<p>{1–2 paragraphs of context for the role.}</p>

<p><strong>How you'll make an impact:</strong></p>
<ul>
  <li><p>{Bullet.}</p></li>
  …
</ul>

<p><strong>What makes you a good fit:</strong></p>
<ul>
  <li><p>{Bullet.}</p></li>
  …
</ul>

<p><strong>Bonus points:</strong></p>          <!-- optional -->
<ul>…</ul>

<p><strong>Compensation:</strong> …</p>        <!-- everything below here is out of scope of this audit -->
```

### 4.2 Concrete style-guide rules to encode in the editor

1. **Section headers are `<p><strong>Header:</strong></p>` — never an `<h1>`/`<h2>`/`<h3>`.** Reason: the `.prose` CSS gives `<h2>` ~32 px / weight 500 and `<h1>` ~48 px / weight 500, which is louder than the surrounding card hierarchy on the listing page.
2. **Sentence case for every section header.** "About the role", not "About the Role" or "About The Role".
3. **Use a fixed set of 5 canonical section labels** (sentence case, trailing colon inside the `<strong>` tag, no trailing whitespace, single straight apostrophe `'`):
   - `About the role:`
   - `About the team:` (only when there's both an "About the role" and an "About the team")
   - `How you'll make an impact:`
   - `What makes you a good fit:`
   - `Bonus points:` (replaces today's "Bonus Experience", "Nice to have", "Nice-to-Haves", "Preferred Qualifications", "Useful skills and experience", "Additional Desired Experience and Skills")
4. **Always use straight `'`** in editor text. Decide once: either the rich-text editor automatically smart-quotes everything (in which case every "you'll" must be the curly version) or it never does (every "you'll" must be straight). The current 27 / 19 / 9 split between three glyphs is the worst case.
5. **Each visual paragraph is its own `<p>` tag — never `<br><br>`.** No `<br>` inside an `<li>` either.
6. **Each bullet is `<li><p>…</p></li>`** (not bare `<li>…</li>`). The `.prose` rule for `<li><p>` includes a top margin; bare `<li>`s render tight.
7. **Bold (`<strong>`) only.** No `<u>`, no `<b>`, no `<i>`, no `<em>`. The 7 underline and 2 italic usages today are all replaceable with `<strong>`.
8. **No inline `style` attributes; no `<div>`, `<span>`, `<font>` inside the prose block.** When pasting from Google Docs or Microsoft Word, paste via *Paste as plain text* (Cmd-Shift-V) and re-format inside the editor. (This will eliminate the Manager, Logistics anomaly.)
9. **Open-paragraph intro uses one consistent version.** Decide between the plain-text intro (41 postings today) and the four-link intro (65 postings today) — having both in production gives candidates two visibly different first impressions.
10. **US-based postings always include the Compensation block.** (Catches the missing-compensation US intern role.)
11. **The hidden LinkedIn tag (`#LI-AA1`, `#LI-PG1`, etc.)** sits just below the compensation block on most postings, but on a handful (e.g. Manager, Logistics; Senior Technical Support Representative – Japan) it's wrapped in the previous `<li>` or inside a stray `<div>`. Always wrap it in its own `<p>` and keep it directly after the EEO paragraph.

### 4.3 Suggested one-time cleanup work

In priority order (highest visual impact first):

1. **Senior Technical Support Representative – Japan** — change the three `<h1>` headers to `<p><strong>…:</strong></p>`. Single highest-impact fix in the corpus.
2. **The 15 postings using `<h2>` or `<h3>`** (see §2.1) — convert all section headers to `<p><strong>`. Special attention to Hardware Engineering Program Manager (mixes `<h2>` + `<h3>`), Senior Buyer (mixes `<h2>` + `<p><strong>`), and Revenue Operations Engineer Quoting Systems (mixes `<h2>` + `<br>` + `<p><strong>`).
3. **The 6 postings with mega-paragraph bullet blobs** (§2.5) — re-paste each bullet list as a proper `<ul><li><p>…</p></li>…</ul>`. These are the worst content-quality failures because a 2,000-character bold paragraph is essentially unreadable.
4. **The 18 postings using `<br><br>`** (§2.4) — split each into proper `<p>` elements.
5. **Manager, Logistics** — remove the `<div style="…">` artefact.
6. **The 7 underline (`<u>`) and 2 italic (`<em>`) postings** (§2.8–2.9) — replace with `<strong>` or remove.
7. **The 3 Technical Recruiter postings** — they share a template; rewriting one and re-cloning it will fix all three (`<u>`, mixed `<li><p>` vs bare `<li>`, plus `<br>`).
8. **Section-header casing pass** — convert all "About the Role" → "About the role"; "What Makes You a Good Fit" → "What makes you a good fit"; etc. A safe find-and-replace.
9. **Apostrophe pass** — normalise straight vs. curly across all "you'll", "you'd", "Skydio's".
10. **Fix the typo** `What Makes Your a Good Fit` → `What makes you a good fit` (Senior People Analytics Analyst).
11. **Add a Compensation block** to *Autonomy Engineer Intern – Deep Learning (Computational Photography), San Mateo* (the only US-based posting missing it).

### 4.4 Process recommendations

- Move section labels out of the free-text editor and into the posting template itself (i.e. pre-populate the five canonical labels in the ATS template so recruiters write the *body* of each section but never the *header* of it). This prevents 100% of the casing, apostrophe, and label-wording drift.
- Add a one-page "Skydio job posting style guide" (the 11 rules above) and link it from the ATS editor.
- Add a linter / Greenhouse webhook that scans each new posting on save and warns on any of: presence of `<h[1-6]>`, presence of `<br>`, presence of `<u>`/`<em>`/`<b>`/`<i>`/`<font>`, presence of `style="…"`, any `<div>` inside the description, any `<strong>` block longer than ~400 characters, missing "About the role:" / "How you'll make an impact:" / "What makes you a good fit:" / "Compensation:" markers in the right order.

---

## Appendix A — Methodology

1. Fetched `https://www.skydio.com/careers` and parsed out all 106 distinct posting URLs (the page lists 107 entries; "Senior Technical Recruiter" / "Staff Technical Recruiter" / "Senior Technical Recruiter – Hardware Operations" share an additional duplicate which was de-duplicated).
2. Downloaded each posting page and extracted the inner HTML of the `<div class="prose block-content">…</div>` block (this is the only content area on the page rendered with the careers `.prose` typography rule set).
3. Truncated each extracted block at the first occurrence of the word **"Compensation"** at the start of a block-level element (so all reported counts exclude the compensation paragraph, EEO statement, "#LI-…" recruiter tags, and the standard closing paragraphs).
4. Counted, per posting, every HTML tag, every inline `style` attribute, every section-header text (whether wrapped in an `<h*>` or in `<p><strong>`), and every paragraph-break pattern (`</p><p>` vs `<br><br>`).
5. Compared per-posting feature vectors against the modal corpus values to identify outliers, and confirmed each call-out by re-reading the source HTML.

The raw per-posting feature data and the source HTML are reproducible from the URLs above. No JavaScript execution was required — the prose block is fully server-rendered.


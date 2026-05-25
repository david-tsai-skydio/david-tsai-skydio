# Skydio Careers Page — Job Posting Formatting Audit
_Scope: 106 job postings reachable from [skydio.com/careers](https://www.skydio.com/careers), analyzing only the content **before** each posting's **Compensation** block._
## 1. Methodology
- Fetched every job posting linked from the careers page (106 listings).
- For each posting, located the `<div class="prose block-content">` body and sliced off everything from the **Compensation** paragraph onward (matched on `<p><strong>Compensation…</strong></p>`, `<h*>Compensation…`, or a bare `<strong>Compensation:</strong>`).
- The pre-compensation slice was inspected for HTML tag usage, inline styles, class attributes, list types, heading conventions, line-break / empty-paragraph usage, ALL-CAPS bold phrases, and length.
- Because every posting renders through Skydio's shared site stylesheet (`type-body-2`, `prose block-content`, etc.), absolute font sizes, colors, and line-heights are inherited from the same CSS for all postings. Differences are therefore driven entirely by the **semantic HTML the recruiter chose in Greenhouse** (e.g. `<p><strong>` vs `<h1>` vs `<h2>`, bullets vs prose, underline, italics, blank paragraphs, etc.). All deviations below originate in the source content, not in the page CSS.
## 2. Executive Summary — The Norm
A clear house-style emerges across the 106 postings. A "consistent" posting:

1. Opens with the standard Skydio company boilerplate paragraph that begins _"Skydio is the leading US drone company..."_. **All 106 postings comply.**
2. Uses `<p><strong>Section Label:</strong></p>` as the heading mechanism for sections such as **About the role**, **Responsibilities**, **Required qualifications**, etc. (166 occurrences across the corpus — the dominant convention).
3. Uses unordered `<ul>` bullet lists for responsibilities & qualifications (105 of 106 postings).
4. Contains no inline `style="…"` overrides, no inline color, no inline `font-size`, no inline `text-align`. **All 106 postings comply.**
5. Uses `<strong>` (never `<b>`) for emphasis. **All 106 postings comply.**
6. Avoids `<u>` underlines and `<em>/<i>` italics in the pre-compensation body.
7. Falls in the **~3,400 – 4,900 character / ~365 – 540 word** range (median ≈ 4,091 chars, 431 words).
## 3. Cross-Posting Formatting Inventory
| Feature | Postings following the norm | Postings deviating |
|---|---|---|
| Opens with standard Skydio intro paragraph | 106/106 | 0 |
| Uses `<p><strong>Label:</strong></p>` headings (with trailing colon) | 166 occurrences | 6 no-colon, 2 `<h1>`, 1 `<h2>` |
| Uses bullet (`<ul>`) lists | 105/106 | 1 use only prose |
| Uses `<strong>` (never `<b>`) | 106/106 | 0 |
| No `<u>` underlines | 99/106 | 7 use underline |
| No `<em>` / `<i>` italics | 104/106 | 2 use italics |
| No empty `<p></p>` spacers | 57/106 | 49 insert blank paragraphs |
| No `<br>` line-break shims | 64/106 | 42 use `<br>` inside prose |
| No ALL-CAPS bold phrases | 106/106 | 0 use SHOUTED headers |
| No inline `style=` overrides | 106/106 | 0 |
| No inline color / font-size / alignment | 106/106 | 0 |
## 4. Specific Inconsistencies Flagged
### 4.1 Heading hierarchy: `<h1>` / `<h2>` used inside the body
The dominant convention is to render section labels as a bold paragraph (`<p><strong>About the role:</strong></p>`), which inherits body styling and visually reads at body-text size. A small number of postings instead use **HTML headings** for those same labels, which Skydio's site CSS renders much larger (and `<h1>` competes with the actual job-title `<h1>` at the top of the page).
**`<h1>` headings used in body (visually equal to the job title):**
- _Senior Technical Support Representative - Japan_ — `<h1>About the role:</h1>`
- _Senior Technical Support Representative - Japan_ — `<h1>How you’ll make an impact:</h1>`

**`<h2>` headings used in body:**
- _Hardware Engineering Program Manager_ — `<h2>How you'll make an impact</h2>`

### 4.2 Bold section labels missing the trailing colon
The house pattern is `<strong>About the role:</strong>` (with colon). These postings drop the colon, making their labels look subtly different:
- _Customer Success Manager, DFR Majors - Southeast_ — `<strong>Requirements</strong>` (no colon)
- _IT Technician (Help Desk - Linux Focus)_ — `<strong>About the Role</strong>` (no colon)
- _IT Technician (Help Desk - Linux Focus)_ — `<strong>What You’ll Do</strong>` (no colon)
- _Senior People Analytics Analyst_ — `<strong>About The Role</strong>` (no colon)
- _Senior People Analytics Analyst_ — `<strong>Preferred Qualifications</strong>` (no colon)
- _Workplace Experience Coordinator Part-Time_ — `<strong>Qualifications</strong>` (no colon)

### 4.3 Underline (`<u>`) usage
`<u>` is not used anywhere else on the careers site. Underlined text visually mimics a hyperlink and should be avoided in static copy.
- Full Stack Product Counsel
- Lead Staff Electrical Engineer
- Senior NPI Product Quality Engineer
- Senior Software Engineer, Full Stack
- Senior Technical Recruiter
- Senior Technical Recruiter - Hardware Operations
- Staff Technical Recruiter

### 4.4 Italic (`<em>` / `<i>`) usage
Italics are absent from the rest of the corpus.
- Director, Growth Marketing - Commercial
- Senior NPI Product Quality Engineer

### 4.5 Empty-paragraph spacers (`<p></p>`, `<p>&nbsp;</p>`)
Empty paragraphs are used by some postings to add vertical whitespace. Because Skydio's `prose` CSS already applies a consistent paragraph rhythm, these blanks create unequal spacing between sections — visible as one posting having a noticeably larger gap before "Responsibilities" than another.
- _Staff Product Manager, Platform & Infrastructure_ — 6 blank paragraph(s)
- _Senior Product Manager, Platform & Infrastructure_ — 6 blank paragraph(s)
- _Deployment Engineer - Southeast_ — 5 blank paragraph(s)
- _Sr/Staff Embedded Software Engineer - Camera Systems_ — 4 blank paragraph(s)
- _Senior/Staff Embedded Software Engineer – Camera Systems_ — 4 blank paragraph(s)
- _Senior Software Engineer - Mobile Platform_ — 3 blank paragraph(s)
- _Senior Buyer_ — 3 blank paragraph(s)
- _Senior Business Operations Manager_ — 3 blank paragraph(s)
- _Senior Brand Designer (Contract)_ — 3 blank paragraph(s)
- _Program Manager, Major Deployments (Mid Atlantic)_ — 3 blank paragraph(s)
- _Program Manager, Major Deployments (Hawaii)_ — 3 blank paragraph(s)
- _Production Manager, PM Shift_ — 3 blank paragraph(s)
- _Product Support Engineer Intern_ — 3 blank paragraph(s)
- _Hardware Operations Program Manager_ — 3 blank paragraph(s)
- _Hardware Engineering Program Manager_ — 3 blank paragraph(s)
- _Full Stack Product Counsel_ — 3 blank paragraph(s)
- _Director, Growth Marketing - Commercial_ — 3 blank paragraph(s)
- _Director, Global Supply Management - Mechanicals_ — 3 blank paragraph(s)
- _Communications Manager_ — 3 blank paragraph(s)
- _Autonomy Engineer - ML & DL Infrastructure_ — 3 blank paragraph(s)
- _Software Engineer - Simulation & Robotics Engineer_ — 2 blank paragraph(s)
- _Software Engineer - Cloud Simulation & Full-Stack_ — 2 blank paragraph(s)
- _Senior Revenue Operations Manager_ — 2 blank paragraph(s)
- _Senior RF Design Engineer_ — 2 blank paragraph(s)
- _Revenue Operations Engineer, Quoting Systems_ — 2 blank paragraph(s)
- _Product Support Engineer_ — 2 blank paragraph(s)
- _Manager, Logistics_ — 2 blank paragraph(s)
- _Lead Staff Electrical Engineer_ — 2 blank paragraph(s)
- _IT Technician (Help Desk - Linux Focus)_ — 2 blank paragraph(s)
- _Head of Warehouse & Logistics Operations_ — 2 blank paragraph(s)
- _GTM Data Engineer Intern_ — 2 blank paragraph(s)
- _Field Support Representative (Southwest, Remote)_ — 2 blank paragraph(s)
- _Aviation Regulatory Program Manager_ — 2 blank paragraph(s)
- _Workplace Experience Coordinator Part-Time_ — 1 blank paragraph(s)
- _Supplier Quality Engineer, Sustaining_ — 1 blank paragraph(s)
- _Success Systems Specialist_ — 1 blank paragraph(s)
- _Staff Global Supply Manager,  Mechanicals_ — 1 blank paragraph(s)
- _Software Engineer Intern Fall 2026/Winter 2027_ — 1 blank paragraph(s)
- _Software Engineer - Autonomy Infrastructure, Systems and Tools_ — 1 blank paragraph(s)
- _Senior Technical Support Representative - Japan_ — 1 blank paragraph(s)
- _Senior Customer Support Representative - India_ — 1 blank paragraph(s)
- _Senior Autonomy Engineer - Deep Learning_ — 1 blank paragraph(s)
- _Sales Planning Analyst Intern_ — 1 blank paragraph(s)
- _GTM Enablement Associate_ — 1 blank paragraph(s)
- _Aviation Compliance Lead_ — 1 blank paragraph(s)
- _Autonomy Engineer - Deep Learning Infrastructure_ — 1 blank paragraph(s)

### 4.6 Inline `<br>` line-breaks
`<br>` shims inside paragraphs disrupt the consistent line-height that `<p>` siblings would produce. Sites typically prefer a new `<p>` or a list item instead.
- _IT Technician (Help Desk - Linux Focus)_ — 9 `<br>` tag(s)
- _Director, Growth Marketing - Commercial_ — 8 `<br>` tag(s)
- _Autonomy Engineer - Deep Learning Infrastructure_ — 8 `<br>` tag(s)
- _Autonomy Engineer - Deep Learning Model Acceleration_ — 6 `<br>` tag(s)
- _Autonomy Engineer - Deep Learning Infrastructure_ — 6 `<br>` tag(s)
- _Software Engineer Intern Fall 2026/Winter 2027_ — 4 `<br>` tag(s)
- _Senior Technical Recruiter - Hardware Operations_ — 4 `<br>` tag(s)
- _Revenue Operations Engineer, Quoting Systems_ — 4 `<br>` tag(s)
- _Director of Product Management, Drone as First Responder (DFR)_ — 4 `<br>` tag(s)
- _Autonomy Software Engineer_ — 4 `<br>` tag(s)
- _GTM Data Engineer Intern_ — 3 `<br>` tag(s)
- _Supply Chain Intern_ — 2 `<br>` tag(s)
- _Senior Technical Support Representative - Japan_ — 2 `<br>` tag(s)
- _Senior Technical Recruiter_ — 2 `<br>` tag(s)
- _Senior Director, Product Management, Drone as First Responder (DFR)_ — 2 `<br>` tag(s)
- _Senior Brand Designer (Contract)_ — 2 `<br>` tag(s)
- _Senior Autonomy Engineer - Deep Learning_ — 2 `<br>` tag(s)
- _Product Support Engineer Intern_ — 2 `<br>` tag(s)
- _Product Support Engineer_ — 2 `<br>` tag(s)
- _PCB Layout Engineer_ — 2 `<br>` tag(s)
- _GTM Enablement Associate_ — 2 `<br>` tag(s)
- _Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland)_ — 2 `<br>` tag(s)
- _Enterprise Account Manager (MoD/ MoI) – EMEA (Germany)_ — 2 `<br>` tag(s)

### 4.7 ALL-CAPS bold "headers" (e.g. `**ABOUT THE ROLE**`)
A small number of postings render section labels in ALL CAPS in addition to bolding, breaking sentence-case consistency with the rest of the corpus.
_None observed._

### 4.8 Postings without bulleted lists
105 of 106 postings break responsibilities and qualifications out into bulleted lists. The following posting renders everything as continuous prose paragraphs, which reads markedly differently:
- Director, Global Supply Management - Mechanicals

### 4.9 Length outliers (character count of pre-compensation body)
Distribution: min **1,880**, p25 **3,356**, median **4,081**, p75 **4,938**, max **6,788**.

**Substantially longer than the norm** (>1.5σ above median — these dominate visually compared to peer postings):
- _Staff Product Manager, Platform & Infrastructure_ — 6,788 chars
- _Senior Product Manager, Platform & Infrastructure_ — 6,677 chars
- _Manager, Technical Support_ — 6,363 chars
- _Success Systems Specialist_ — 6,168 chars
- _Senior Technical Support Representative - Japan_ — 6,134 chars
- _Senior Software Engineer,  Data Platform_ — 6,033 chars
- _Field Support Representative (Southwest, Remote)_ — 6,018 chars
- _Senior RF Design Engineer_ — 5,637 chars

**Substantially shorter than the norm** (<1.5σ below median — these look "thin" relative to peers):
- _Supply Chain Intern_ — 1,880 chars
- _Senior Autonomy Engineer - Controls_ — 1,950 chars
- _Autonomy Engineer - Fixed Wing Planning & Controls_ — 2,072 chars
- _Electrical Engineer (all levels)_ — 2,473 chars
- _Senior Autonomy Engineer - Deep Learning_ — 2,484 chars
- _Senior Autonomy Engineer - Deep Learning_ — 2,497 chars
- _PhD Autonomy Engineer Intern - Deep Learning or Computer Vision_ — 2,504 chars

### 4.10 Compensation-block labeling inconsistencies
Every US-located Skydio posting is expected to end with a clearly-labeled Compensation block (`<p><strong>Compensation:</strong> …</p>`). Two deviations show up:

**4.10a — Compensation paragraph present but with no bold "Compensation:" label** (the paragraph starts inline with "At Skydio, our compensation packages…"):
- Full Stack Product Counsel

**4.10b — No Compensation paragraph at all** (typically non-US roles where pay-range disclosure is not legally required, but worth confirming intentional):
- Autonomy Engineer Intern - Deep Learning (Computational Photography)
- Senior Technical Support Representative - Japan
- Supplier Quality Engineer, Sustaining
- Workplace Experience Coordinator Part-Time

**4.10c — Variant label "Compensation Range:" used instead of "Compensation:":**
- Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026
- Autonomy Engineer Intern Fall 2026
- Director of Product Management, Drone as First Responder (DFR)
- Middleware Software Engineer Intern - Fall 2026
- PhD Autonomy Engineer Intern - Deep Learning or Computer Vision
- Sales Planning Analyst Intern
- Senior Director, Product Management, Drone as First Responder (DFR)
- Senior People Analytics Analyst
- Software Engineer Intern Fall 2026/Winter 2027
- Supply Chain Intern

### 4.11 Postings missing the standard "Skydio is the leading..." intro
_None — every posting opens with the canonical company-intro paragraph._

### 4.12 Trailing punctuation inconsistencies in bold section labels
Most labels follow `**Label:**`. These postings use a period or other punctuation after the bold instead, breaking the pattern.
- _Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland)_ — 1 occurrence(s)
- _Enterprise Account Manager (MoD/ MoI) – EMEA (Germany)_ — 1 occurrence(s)
- _Enterprise Account Manager (MoD/ MoI) – EMEA (Finland)_ — 1 occurrence(s)
- _Communications Manager_ — 1 occurrence(s)

## 5. Per-Posting Formatting Characteristics
Columns: **len** (pre-compensation char count), **words**, **¶** (paragraph count), **·** (`<ul>` count), **#·** (list items), **H1/H2** (body headings used), **<u>** / **<em>** (underline / italic), **∅¶** (empty paragraphs), **<br>** (line breaks), **CAPS** (all-caps bold phrases). A blank cell = 0.
| Job title | Location | len | words | ¶ | · | #· | H1 | H2 | <u> | <em> | ∅¶ | <br> | CAPS |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Autonomy Engineer - Deep Learning | Zurich, Switzerland - Full-time | 3,376 | 346 | 20 | 2 | 14 |  |  |  |  |  |  |  |
| Autonomy Engineer - Deep Learning | San Mateo, California, United States - Full-time | 2,889 | 346 | 20 | 2 | 14 |  |  |  |  |  |  |  |
| Autonomy Engineer - Deep Learning Infrastructure | Zurich, Switzerland - Full-time | 3,594 | 426 | 20 | 2 | 17 |  |  |  |  |  | 6 |  |
| Autonomy Engineer - Deep Learning Infrastructure | San Mateo, California, United States - Full-time | 4,264 | 458 | 21 | 2 | 17 |  |  |  |  | 1 | 8 |  |
| Autonomy Engineer - Deep Learning Model Acceleration | Zurich, Switzerland - Full-time | 3,598 | 427 | 20 | 2 | 17 |  |  |  |  |  | 6 |  |
| Autonomy Engineer - Deep Learning Model Acceleration | San Mateo, California, United States - Full-time | 4,081 | 426 | 20 | 2 | 17 |  |  |  |  |  | 6 |  |
| Autonomy Engineer - Fixed Wing Planning & Controls | San Mateo, California, United States - Full-time | 2,072 | 246 | 17 | 2 | 12 |  |  |  |  |  |  |  |
| Autonomy Engineer - ML & DL Infrastructure | San Mateo, California, United States - Full-time | 3,960 | 433 | 22 | 3 | 13 |  |  |  |  | 3 |  |  |
| Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 | San Mateo, California, United States - Intern | 2,904 | 324 | 15 | 2 | 8 |  |  |  |  |  | 1 |  |
| Autonomy Engineer Intern - Deep Learning (Computational Photography) | Zurich, Switzerland or Tampere, Finland - Intern | 4,987 | 541 | 25 | 2 | 15 |  |  |  |  |  |  |  |
| Autonomy Engineer Intern - Deep Learning (Computational Photography) | San Mateo, California, United States - Intern | 4,987 | 541 | 25 | 2 | 15 |  |  |  |  |  |  |  |
| Autonomy Engineer Intern Fall 2026 | San Mateo, California, United States - Intern | 2,548 | 263 | 14 | 2 | 8 |  |  |  |  |  |  |  |
| Autonomy Software Engineer | San Mateo, California, United States - Full-time | 3,571 | 375 | 15 | 2 | 12 |  |  |  |  |  | 4 |  |
| Aviation Compliance Lead | San Mateo, California, United States - Full-time | 3,356 | 378 | 20 | 2 | 15 |  | 4 |  |  | 1 | 1 |  |
| Aviation Regulatory Program Manager | US Remote - Full-time | 3,921 | 469 | 24 | 2 | 16 |  | 3 |  |  | 2 |  |  |
| Communications Manager | US Remote - Full-time | 3,890 | 405 | 18 | 2 | 12 |  | 3 |  |  | 3 |  |  |
| Customer Success Manager, DFR Majors - Northeast | US Remote - Full-time | 3,912 | 478 | 27 | 2 | 19 |  |  |  |  |  |  |  |
| Customer Success Manager, DFR Majors - Southeast | US Remote - Full-time | 4,384 | 466 | 28 | 3 | 19 |  |  |  |  |  |  |  |
| Deployment Engineer - Southeast | US Remote - Full-time | 5,180 | 561 | 37 | 3 | 23 |  |  |  |  | 5 |  |  |
| Director of Product Management, Drone as First Responder (DFR) | San Mateo, California, United States - Full-time | 5,055 | 576 | 24 | 3 | 20 |  |  |  |  |  | 4 |  |
| Director, Global Supply Management - Mechanicals | San Mateo, California, United States - Full-time | 5,084 | 588 | 26 |  |  |  |  |  |  | 3 |  |  |
| Director, Growth Marketing - Commercial | San Mateo, California, United States - Full-time | 5,577 | 564 | 33 | 6 | 23 |  |  |  | 1 | 3 | 8 |  |
| Electrical Engineer (all levels) | San Mateo, California, United States - Full-time | 2,473 | 224 | 17 | 2 | 13 |  |  |  |  |  | 2 |  |
| Electrical Engineer (Sustaining/Validation) | San Mateo, California, United States - Full-time | 2,847 | 274 | 18 | 2 | 14 |  |  |  |  |  | 1 |  |
| Engineering Manager - Autonomy | San Mateo, California, United States - Full-time | 3,100 | 323 | 15 | 2 | 10 |  |  |  |  |  | 1 |  |
| Enterprise Account Manager (MoD/ MoI) – EMEA (Finland) | Tampere, Finland - Full-time | 5,248 | 573 | 30 | 2 | 22 |  |  |  |  |  | 2 |  |
| Enterprise Account Manager (MoD/ MoI) – EMEA (Germany) | Germany - Full-time | 5,248 | 573 | 30 | 2 | 22 |  |  |  |  |  | 2 |  |
| Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland) | Zurich, Switzerland - Full-time | 5,248 | 573 | 30 | 2 | 22 |  |  |  |  |  | 2 |  |
| Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM | US Remote - Full-time | 4,346 | 483 | 26 | 2 | 20 |  |  |  |  |  |  |  |
| Enterprise Account Manager, US Army | US Remote - Full-time | 4,339 | 446 | 26 | 2 | 20 |  |  |  |  |  |  |  |
| Field Support Representative | US Remote - Full-time | 4,584 | 486 | 25 | 2 | 18 |  |  |  |  |  |  |  |
| Field Support Representative (Southwest, Remote) | US Remote - Full-time | 6,018 | 687 | 30 | 4 | 22 |  |  |  |  | 2 |  |  |
| Full Stack Product Counsel | San Mateo, California, United States - Full-time | 4,385 | 477 | 22 | 2 | 15 |  |  | 1 |  | 3 |  |  |
| GTM Data Engineer Intern | San Mateo, California, United States - Intern | 3,861 | 433 | 26 | 4 | 18 |  |  |  |  | 2 | 3 |  |
| GTM Enablement Associate | San Mateo, California, United States - Full-time | 3,268 | 350 | 27 | 3 | 18 |  |  |  |  | 1 | 2 |  |
| Hardware Engineering Program Manager | San Mateo, California, United States - Full-time | 4,938 | 455 | 29 | 5 | 23 |  | 3 |  |  | 3 |  |  |
| Hardware Operations Program Manager | Hayward, California, United States - Full-time | 3,312 | 361 | 20 | 2 | 12 |  |  |  |  | 3 |  |  |
| Head of Warehouse & Logistics Operations | US CA Production - Full-time | 4,110 | 420 | 27 | 2 | 20 |  |  |  |  | 2 | 1 |  |
| IT Technician (Help Desk - Linux Focus) | Hayward, California, United States - Full-time | 5,315 | 460 | 60 | 14 | 42 |  |  |  |  | 2 | 9 |  |
| Lead Staff Electrical Engineer | San Mateo, California, United States - Full-time | 3,070 | 298 | 21 | 2 | 15 |  |  | 1 |  | 2 | 1 |  |
| Manager, Logistics | US CA Production - Full-time | 4,206 | 416 | 30 | 3 | 23 |  |  |  |  | 2 |  |  |
| Manager, Technical Support | US CA San Mateo - Full-time | 6,363 | 749 | 30 | 2 | 22 |  |  |  |  |  |  |  |
| Middleware Software Engineer Intern - Fall 2026 | US CA San Mateo - Intern | 3,005 | 316 | 17 | 2 | 11 |  |  |  |  |  |  |  |
| Mission Success Operations Manager | US Remote - Full-time | 3,430 | 429 | 24 | 4 | 17 |  |  |  |  |  |  |  |
| PCB Layout Engineer | San Mateo, California, United States - Full-time | 3,291 | 329 | 16 | 2 | 12 |  |  |  |  |  | 2 |  |
| PhD Autonomy Engineer Intern - Deep Learning or Computer Vision | San Mateo, California, United States - Intern | 2,504 | 328 | 15 | 3 | 9 |  |  |  |  |  | 1 |  |
| PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) | Zurich, Switzerland - Intern | 4,469 | 416 | 21 | 4 | 17 |  |  |  |  |  |  |  |
| Product Design Engineer (All Levels) | San Mateo, California, United States - Full-time | 3,913 | 427 | 20 | 2 | 16 |  |  |  |  |  | 1 |  |
| Product Support Engineer | San Mateo, California, United States - Full-time | 5,157 | 548 | 28 | 2 | 22 |  |  |  |  | 2 | 2 |  |
| Product Support Engineer Intern | San Mateo, California, United States - Intern | 3,985 | 415 | 22 | 2 | 15 |  |  |  |  | 3 | 2 |  |
| Production Manager, PM Shift | Hayward, California, United States - Full-time | 2,927 | 277 | 19 | 2 | 11 |  |  |  |  | 3 |  |  |
| Program Manager, Major Deployments (Hawaii) | San Mateo, California, United States - Full-time | 4,980 | 573 | 24 | 2 | 14 |  |  |  |  | 3 |  |  |
| Program Manager, Major Deployments (Mid Atlantic) | US Remote - Full-time | 4,597 | 582 | 25 | 2 | 15 |  |  |  |  | 3 |  |  |
| Revenue Operations Engineer, Quoting Systems | San Mateo, California, United States - Full-time | 4,951 | 470 | 31 | 5 | 25 |  | 5 |  |  | 2 | 4 |  |
| RF Design Engineer | San Mateo, California, United States - Full-time | 3,539 | 365 | 24 | 2 | 19 |  |  |  |  |  |  |  |
| Sales Planning Analyst Intern | San Mateo, California, United States - Intern | 3,302 | 385 | 25 | 2 | 18 |  |  |  |  | 1 | 1 |  |
| Senior Autonomy Engineer - Controls | San Mateo, California, United States - Full-time | 1,950 | 232 | 14 | 3 | 9 |  |  |  |  |  |  |  |
| Senior Autonomy Engineer - Deep Learning | San Mateo, California, United States - Full-time | 2,497 | 297 | 19 | 2 | 13 |  |  |  |  | 1 | 2 |  |
| Senior Autonomy Engineer - Deep Learning | Zurich, Switzerland - Full-time | 2,484 | 298 | 17 | 2 | 13 |  |  |  |  |  | 2 |  |
| Senior Brand Designer (Contract) | San Mateo, California, United States - Full-time | 4,125 | 471 | 33 | 4 | 22 |  |  |  |  | 3 | 2 |  |
| Senior Business Operations Manager | San Mateo, California, United States - Full-time | 4,798 | 471 | 34 | 4 | 26 |  |  |  |  | 3 |  |  |
| Senior Buyer | Hayward, California, United States - Full-time | 4,389 | 449 | 29 | 2 | 22 |  | 2 |  |  | 3 |  |  |
| Senior Customer Support Representative - India | Bangalore, India - Full-time | 5,345 | 584 | 29 | 3 | 22 |  |  |  |  | 1 |  |  |
| Senior Director, Product Management, Drone as First Responder (DFR) | San Mateo, California, United States - Full-time | 5,057 | 578 | 25 | 3 | 20 |  |  |  |  |  | 2 |  |
| Senior Hardware Test and Reliability Engineer | San Mateo, California, United States - Full-time | 4,202 | 521 | 19 | 2 | 12 |  |  |  |  |  |  |  |
| Senior NPI Product Quality Engineer | San Mateo, California, United States - Full-time | 3,245 | 367 | 25 | 2 | 19 |  |  | 1 | 1 |  |  |  |
| Senior People Analytics Analyst | San Mateo, California, United States - Full-time | 4,428 | 426 | 22 | 3 | 16 |  |  |  |  |  |  |  |
| Senior Product Manager, Platform & Infrastructure | San Mateo, California, United States - Full-time | 6,677 | 741 | 29 | 2 | 15 |  |  |  |  | 6 | 1 |  |
| Senior Revenue Operations Manager | San Mateo, California, United States - Full-time | 3,782 | 417 | 28 | 3 | 18 |  |  |  |  | 2 |  |  |
| Senior RF Design Engineer | San Mateo, California, United States - Full-time | 5,637 | 561 | 34 | 3 | 25 |  |  |  |  | 2 |  |  |
| Senior Software Engineer - Embedded | San Mateo, California, United States - Full-time | 3,278 | 333 | 23 | 3 | 17 |  |  |  |  |  |  |  |
| Senior Software Engineer - Mobile Platform | San Mateo, California, United States - Full-time | 4,595 | 502 | 29 | 3 | 18 |  |  |  |  | 3 |  |  |
| Senior Software Engineer - Security | San Mateo, California, United States - Full-time | 3,838 | 393 | 23 | 3 | 17 |  |  |  |  |  |  |  |
| Senior Software Engineer,  Data Platform | San Mateo, California, United States - Full-time | 6,033 | 699 | 30 | 3 | 20 |  |  |  |  |  | 1 |  |
| Senior Software Engineer,  Infrastructure | San Mateo, California, United States - Full-time | 3,481 | 379 | 19 | 3 | 13 |  |  |  |  |  |  |  |
| Senior Software Engineer, Frontend | San Mateo, California, United States - Full-time | 2,864 | 328 | 23 | 3 | 15 |  |  |  |  |  |  |  |
| Senior Software Engineer, Full Stack | San Mateo, California, United States - Full-time | 4,743 | 599 | 24 | 3 | 13 |  |  | 1 |  |  | 1 |  |
| Senior Technical Recruiter | San Mateo, California, United States - Full-time | 3,856 | 415 | 19 | 2 | 14 |  |  | 1 |  |  | 2 |  |
| Senior Technical Recruiter - Hardware Operations | San Mateo, California, United States - Full-time | 3,945 | 421 | 18 | 2 | 13 |  |  | 1 |  |  | 4 |  |
| Senior Technical Support Representative - Japan | Tokyo, Japan - Full-time | 6,134 | 685 | 28 | 2 | 20 | 3 |  |  |  | 1 | 2 |  |
| Senior Wireless Systems Performance Engineer | San Mateo, California, United States - Full-time | 3,525 | 363 | 21 | 2 | 16 |  |  |  |  |  |  |  |
| Senior/Staff Embedded Software Engineer – Camera Systems | San Mateo, California, United States - Full-time | 3,715 | 367 | 29 | 2 | 18 |  |  |  |  | 4 |  |  |
| Software Engineer - Autonomy Infrastructure, Systems and Tools | San Mateo, California, United States - Full-time | 4,519 | 493 | 24 | 4 | 20 |  | 5 |  |  | 1 |  |  |
| Software Engineer - Autonomy Infrastructure, Systems and Tools | Zurich, Switzerland - Full-time | 4,519 | 493 | 24 | 4 | 20 |  | 5 |  |  | 1 |  |  |
| Software Engineer - Cloud Simulation & Full-Stack | San Mateo, California, United States - Full-time | 5,103 | 507 | 31 | 4 | 26 |  | 5 |  |  | 2 |  |  |
| Software Engineer - Cloud Simulation & Full-Stack | Zurich, Switzerland - Full-time | 5,103 | 507 | 31 | 4 | 26 |  | 5 |  |  | 2 |  |  |
| Software Engineer - Embedded | San Mateo, California, United States - Full-time | 3,278 | 333 | 23 | 3 | 17 |  |  |  |  |  |  |  |
| Software Engineer - Infrastructure | San Mateo, California, United States - Full-time | 3,468 | 377 | 19 | 3 | 13 |  |  |  |  |  |  |  |
| Software Engineer - Simulation & Robotics Engineer | San Mateo, California, United States - Full-time | 4,102 | 446 | 26 | 4 | 20 |  |  |  |  | 2 |  |  |
| Software Engineer - Simulation & Robotics Engineer | Zurich, Switzerland - Full-time | 4,102 | 446 | 26 | 4 | 20 |  |  |  |  | 2 |  |  |
| Software Engineer Intern Fall 2026/Winter 2027 | US CA San Mateo - Intern | 3,366 | 347 | 19 | 3 | 12 |  |  |  |  | 1 | 4 |  |
| Software Engineer, Full Stack | San Mateo, California, United States - Full-time | 3,082 | 299 | 21 | 3 | 13 |  |  |  |  |  |  |  |
| Sr/Staff Embedded Software Engineer - Camera Systems | Tampere, Finland - Full-time | 3,715 | 367 | 29 | 2 | 18 |  |  |  |  | 4 |  |  |
| Staff Global Supply Manager,  Mechanicals | San Mateo, California, United States - Full-time | 4,513 | 524 | 24 | 2 | 17 |  |  |  |  | 1 | 1 |  |
| Staff Product Manager, Platform & Infrastructure | San Mateo, California, United States - Full-time | 6,788 | 760 | 29 | 2 | 15 |  |  |  |  | 6 | 1 |  |
| Staff Software Engineer - Embedded | San Mateo, California, United States - Full-time | 3,277 | 333 | 23 | 3 | 17 |  |  |  |  |  |  |  |
| Staff Software Engineer, Frontend | San Mateo, California, United States - Full-time | 2,827 | 328 | 22 | 3 | 15 |  |  |  |  |  |  |  |
| Staff Software Engineer, Full Stack | San Mateo, California, United States - Full-time | 4,763 | 588 | 25 | 3 | 16 |  |  |  |  |  |  |  |
| Staff Technical Recruiter | San Mateo, California, United States - Full-time | 3,827 | 410 | 21 | 2 | 15 |  |  | 1 |  |  |  |  |
| Success Systems Specialist | US Remote - Full-time | 6,168 | 690 | 41 | 6 | 28 |  |  |  |  | 1 |  |  |
| Supplier Quality Engineer, Sustaining | Taiwan - Full-time | 4,938 | 542 | 23 | 2 | 13 |  |  |  |  | 1 |  |  |
| Supply Chain Intern | San Mateo, California, United States - Intern | 1,880 | 217 | 12 | 2 | 8 |  |  |  |  |  | 2 |  |
| Systems Integration and Test Engineer (Mid to Senior Level) | San Mateo, California, United States - Full-time | 4,236 | 489 | 21 | 2 | 14 |  |  |  |  |  |  |  |
| Technical Support Specialist - West Coast | US Remote - Full-time | 4,742 | 592 | 28 | 2 | 19 |  |  |  |  |  |  |  |
| Wireless Software Engineer | San Mateo, California, United States - Full-time | 3,554 | 382 | 17 | 2 | 12 |  |  |  |  |  |  |  |
| Workplace Experience Coordinator Part-Time | Zurich, Switzerland - Part-time | 4,651 | 451 | 33 | 4 | 20 |  |  |  |  | 1 | 1 |  |

## 6. Recommendations for Standardization

The cleanest path to a uniformly styled careers feed is to lock the source HTML in
Greenhouse (or whatever editor recruiters use) to the existing house style. Concrete
guidelines below — listed in priority order.

### 6.1 Adopt a single section-header pattern
- **Use:** `<p><strong>About the role:</strong></p>`, `<p><strong>Responsibilities:</strong></p>`,
  `<p><strong>Required qualifications:</strong></p>`, etc.
- **Stop using:** `<h1>` or `<h2>` for body sections — they visually compete with the
  page-level job title and render at a much larger size due to the site's default
  heading CSS.
- **Stop using:** ALL-CAPS labels (`**ABOUT THE ROLE**`). Sentence case + colon
  matches the rest of the corpus.
- **Always include the trailing colon** on section labels.

### 6.2 Forbid ad-hoc inline styles
- No `<u>` underlines — they look like broken links.
- No `<em>` / `<i>` for emphasis; reserve `<strong>` for emphasis as the rest of the
  corpus does.
- No `<b>` (use `<strong>` consistently).
- No inline `style="..."` attributes (color, font-size, text-align) — none of the
  current postings need them, and Greenhouse should already be stripping them.

### 6.3 Use real lists, never line-break shims
- Convert any `<br>`-separated bullet lookalikes into proper `<ul><li>…</li></ul>`
  blocks. This keeps line-height consistent with the site's `.prose` styling.
- The one posting currently written as continuous prose should be re-flowed into
  the same Responsibilities / Qualifications bullet layout as every other role.

### 6.4 Remove blank paragraph spacers
- `<p></p>` and `<p>&nbsp;</p>` should be deleted. The site's `.prose` CSS already
  spaces sections evenly; manual spacers create uneven gaps that vary posting to
  posting.

### 6.5 Standardize the opening paragraph
- All 106 postings already open with the canonical _"Skydio is the leading US drone
  company..."_ paragraph. Lock that paragraph as a Greenhouse template snippet so
  recruiters can't accidentally tweak the wording.

### 6.6 Establish a length guardrail
- Pre-compensation body should target **350–550 words / 3,400–4,900 characters**
  (the current interquartile range). Postings above ~700 words are clearly the
  outliers and should be tightened; postings under ~250 words feel skeletal next to
  peers.

### 6.7 Add a CI/lint step
A 30-line script very similar to this audit can be wired into the careers-site
build (or run nightly) to flag new postings that violate any rule above. Suggested
checks:
1. `<h1>` / `<h2>` / `<h3>` inside `.prose.block-content` → fail.
2. `<u>`, `<b>`, `<em>`, `<i>` inside `.prose.block-content` → fail.
3. `style="..."` attribute inside `.prose.block-content` → fail.
4. Empty `<p></p>` or `<p>&nbsp;</p>` → fail.
5. `<br>` not inside a poem/address block → warn.
6. Section labels that don't match `<p><strong>[^<:]+:</strong></p>` → warn.
7. Pre-compensation word count outside 250 – 700 → warn.
8. Missing canonical intro paragraph → warn.
9. Missing `<strong>Compensation:</strong>` block → fail.

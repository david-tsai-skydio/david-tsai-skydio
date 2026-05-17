# Skydio Careers Page — Job-Posting Formatting Audit

_Source: `https://www.skydio.com/careers` (job content delivered by the Ashby ATS at `https://api.ashbyhq.com/posting-api/job-board/skydio`)._  
_Scope: every posting visible on the careers page, analyzed up to **— and not including —** the `Compensation` block (i.e. the salary section and everything that follows: standard benefits boilerplate, EEO notice, E-Verify, `#LI-…` requisition tag, etc.)._

**Postings analyzed:** 110

## How this audit was done

1. Pulled all live postings via the Ashby public job-board API and worked from the official `descriptionHtml` that Skydio publishes (the same HTML the careers page renders).
2. For each posting, found the first `Compensation` block (`<strong>Compensation`, `<u>Compensation`, `<h*>Compensation`, etc.) and **kept only the HTML before that point**.
3. Parsed the pre-compensation HTML with BeautifulSoup and recorded:
   - Tags used and their counts (`<p>`, `<h1>`–`<h6>`, `<ul>`/`<ol>`, `<li>`, `<strong>`, `<u>`, `<em>`, `<br>`, `<div>`, `<a>`).
   - All inline `style="…"` properties and their values (the only design tokens postings can override).
   - How section headers ("About the role", "How you'll make an impact", "What makes you a good fit", "PLEASE NOTE") are marked up.
   - List-item shape (`<li><p>…</p></li>` vs. `<li>…</li>`).
   - Boilerplate intro paragraph, link styling, empty/`<br>` spacing, `&nbsp;`/`'` vs `’` usage, and title whitespace.

> **Important note on "font sizes / colors / weights."** All postings are rendered server-side by the careers template — they do **not** ship any inline `font-size`, `color`, `font-weight`, or `text-align` styles. Visual differences therefore come from **structural** choices (which tags are used) rather than typographic overrides. That is the level at which the inconsistencies described below show up to a reader.

## The "normal" Skydio job posting

The modal posting (about 85 % of the board) is built from a very small set of building blocks:

| Block | Markup convention |
|---|---|
| Opening boilerplate paragraph | `<p style="min-height:1.5em">Skydio is the leading US drone company…</p>` — **identical** in all 110 postings |
| Section heading | `<p style="min-height:1.5em"><strong>About the role:</strong></p>` (i.e. a paragraph whose only content is a `<strong>` run) |
| Body copy | `<p style="min-height:1.5em">…</p>` |
| Bulleted list | `<ul style="min-height:1.5em"><li><p style="min-height:1.5em">…</p></li></ul>` |
| Inline emphasis | `<strong>` only |
| Links | `<a target="_blank" rel="noopener noreferrer nofollow" href="…">…</a>` |
| Compensation block (cut from this audit) | starts with `<p><strong>Compensation:</strong> At Skydio, …</p>` |

Every posting carries `style="min-height:1.5em"` on its block-level tags (a vestige of Ashby's editor); we treat that as the baseline, not a per-posting choice.

## Headline numbers

| Question | Answer |
|---|---|
| How many postings use the modal `<p><strong>` section-header pattern only? | **94 / 110** (85 %) |
| How many use real `<h1>`/`<h2>`/`<h3>` heading tags instead (or in addition)? | **16 / 110** |
| How many use `<u>` (underline) for a section header? | **3 / 110** |
| How many use any `<br>` tags? | **47 / 110** |
| How many use `<em>` (italic)? | **3 / 110** |
| How many have no `<ul>`/`<ol>` bullet list at all? | **1 / 110** |
| How many include custom inline CSS beyond `min-height:1.5em`? | **1 / 110** |
| How many do **not** include a `Compensation` block? | **6 / 110** |
| Posting titles with stray leading/trailing/double whitespace | **15 / 110** |
| Postings that mix `'` and `’` apostrophes in their pre-comp body | **46 / 110** |
| Postings that use the straight ASCII `'` only (no `’`) | **17 / 110** |

## Inconsistency 1 — Section headings are marked up three different ways

Across the board, the same kind of section heading ("About the Role", "How You'll Make an Impact", "What Makes You a Good Fit") is implemented three incompatible ways. Visually this shows up as headings that look bigger / heavier / underlined on some postings but not others.

**Style A — `<p><strong>` (the norm, ~94 postings).** Renders as a regular-size paragraph that's just bolded.

```html
<p style="min-height:1.5em"><strong>About the role:</strong></p>
```

**Style B — real heading tags `<h1>`, `<h2>`, `<h3>` (16 postings).** Renders **noticeably larger and heavier** than Style A.

| Posting | Department | Heading tags used |
|---|---|---|
| PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) | R&D | h3×3 |
| Full Stack Product Counsel | Operations | h3×4 |
| Field Marketing Event Manager | Operations | h3×7 |
| Senior Technical Support Representative - Japan | Operations | h1×3 |
| Revenue Operations Engineer, Quoting Systems | Operations | h2×5 |
| Senior Business Operations Manager | Operations | h3×3 |
| Aviation Compliance Lead | Operations | h2×4 |
| Software Engineer - Cloud Simulation & Full-Stack | R&D | h2×5 |
| Software Engineer - Simulation & Robotics Engineer | R&D | h3×5 |
| Software Engineer - Autonomy Infrastructure, Systems and Tools | R&D | h2×5 |
| Software Engineer - Autonomy Infrastructure, Systems and Tools | R&D | h2×5 |
| Software Engineer - Cloud Simulation & Full-Stack | R&D | h2×5 |
| Software Engineer - Simulation & Robotics Engineer | R&D | h3×5 |
| Aviation Regulatory Program Manager | Operations | h2×3 |
| Communications Manager | Operations | h2×3 |
| Senior Buyer | Operations | h2×2 |

Notes:
- *Field Marketing Event Manager* and *Software Engineer — Cloud Simulation & Full-Stack* (both SF and Zurich) push this furthest: they use `<h2>`/`<h3>` not only for section heads but also as **sub-sub-headings inside lists** (e.g. `<h3>Customer Summit Planning & Execution</h3>` above a `<ul>`). No other posting has nested headings.
- *Senior Technical Support Representative — Japan* uses `<h1>` three times, which on the public page renders the heading as large as the job title bar itself.
- *Software Engineer — Cloud Simulation & Full-Stack*, *Software Engineer — Simulation & Robotics Engineer*, and *Software Engineer — Autonomy Infrastructure, Systems and Tools* exist as **paired SF/Zurich postings using `<h2>`/`<h3>`**, while their sibling Autonomy roles (e.g. *Autonomy Engineer — Deep Learning*) use plain `<p><strong>`. Two postings sitting next to each other on the same page therefore look different.

**Style C — `<p><u>` (underline) (3 postings).** Three Recruiting postings underline the section labels (`PLEASE NOTE:`), which no other posting does.

- Staff Technical Recruiter
- Senior Technical Recruiter - Hardware Operations
- Senior Technical Recruiter

## Inconsistency 2 — Section heading **labels** are not standardized

Even when postings agree on the markup (Style A), the wording of the headings varies wildly. Casing, punctuation, and even apostrophe style differ for what is clearly meant to be the same heading.

| Concept | Variants found across postings |
|---|---|
| what makes you a good fit | `What makes you a good fit:` (54×) • `What Makes You a Good Fit:` (17×) • `What Makes You A Good Fit:` (3×) • `What makes you a good fit` (1×) • `What Makes You a Good Fit: ` (1×) • `What Makes You a Good Fit` (1×) |
| about the role | `About the role:` (45×) • `About the Role:` (21×) • `About the role: ` (3×) • `About the Role: ` (1×) • `About The Role` (1×) • `About the Role` (1×) |
| how you'll make an impact | `How you'll make an impact:` (33×) • `How You’ll Make an Impact:` (20×) • `How you’ll make an impact:` (13×) • `How You'll Make an Impact: ` (1×) |
| about the team | `About the Team:` (6×) • `About the team: ` (3×) • `About the team:` (2×) |
| what would make you a good fit | `What would make you a good fit:` (5×) • `What Would Make You a Good Fit:` (2×) |
| bonus points | `Bonus Points:` (3×) • `Bonus points:` (3×) |
| preferred qualifications | `Preferred Qualifications: ` (2×) • `Preferred Qualifications` (1×) |
| what you'll do | `What you'll do:` (1×) • `What You’ll Do` (1×) |
| nice to haves | `Nice To Haves: ` (1×) • `Nice To Haves:` (1×) |

Highlights:
- "About the Role" appears in **both** Title Case (`About the Role:`, 21×) and sentence case (`About the role:`, 45×) **and** a variant with a trailing `&nbsp;` (`About the role:&nbsp;`, 3×).
- "How You'll Make an Impact" appears with **three different apostrophes/casings**: `How you'll make an impact:` (33 straight-apostrophe sentence-case), `How you’ll make an impact:` (13 curly-apostrophe sentence-case), and `How You’ll Make an Impact:` (20 Title-case curly).
- "What Makes You a Good Fit" has four forms: `What makes you a good fit:` (54), `What Makes You a Good Fit:` (17), `What Makes You A Good Fit:` (3, every word capitalized), `What would make you a good fit:` (5).
- Five postings use a different label entirely (`Useful skills and experience:`, `What you'll do:`, `What would make you a strong fit:`, `Nice-to-Haves:`, etc.).

## Inconsistency 3 — "PLEASE NOTE" callouts use three different decorations

The `PLEASE NOTE` (in-office / location requirement) callout appears in 5 postings, decorated three different ways:

| Wrapping | Count | Example posting |
|---|---|---|
| `<u>` | 3 | Staff Technical Recruiter |
| `<em+strong>` | 1 | Electric Motor / Propulsion Engineer |
| `<strong+u>` | 1 | Senior NPI Product Quality Engineer |

Effect: the same paragraph reads as underlined-only in one posting, italic-bold in another, and bold-underline in a third.

## Inconsistency 4 — `<br>` line breaks appear in 47/110 postings, never in the others

Roughly 4 in 10 postings include manual `<br>` tags — used most often to add **a blank line between two paragraphs** (a workaround for visual spacing). The other ~60 % of postings achieve the same look with bare `<p>` paragraphs and never use `<br>`. So extra vertical whitespace is present in some postings, absent in others.

The worst offenders (8 `<br>` tags each in their pre-comp body):
- Autonomy Engineer - Deep Learning Infrastructure — 8 `<br>` tags
- Director, Growth Marketing - Commercial — 8 `<br>` tags
- IT Technician (Help Desk - Linux Focus) — 8 `<br>` tags
- Autonomy Engineer - Deep Learning Infrastructure — 6 `<br>` tags
- Autonomy Engineer - Deep Learning Model Acceleration — 6 `<br>` tags
- Autonomy Engineer - Deep Learning Model Acceleration — 6 `<br>` tags

## Inconsistency 5 — One posting has no bullet list at all

Every other posting uses an Ashby-flavored bullet list (`<ul><li><p>…</p></li></ul>`). Exactly one posting renders its responsibilities as a wall of consecutive `<p>` paragraphs:

- **Director, Global Supply Management - Mechanicals** (Operations) — 26 `<p>` paragraphs, **0** `<ul>`, **0** `<li>`.

This is the single largest individual outlier on the board: instead of scannable bullets, the reader sees ~7 dense paragraphs.

## Inconsistency 6 — One posting carries hand-written inline CSS

Only one posting overrides the default styling with hand-written CSS:

- **Manager, Logistics** — adds `margin-top:0` and `margin-bottom:0` to a `<div>` (the only `<div>` anywhere in the corpus). Style values: `{'margin-top': {'0': 1}, 'margin-bottom': {'0': 1}}`.

This will produce visibly tighter spacing in that one posting compared to its neighbors.

## Inconsistency 7 — Trailing `&nbsp;` and zero-width punctuation inside `<strong>` headers

7 section headers end with an extra `&nbsp;` (non-breaking space) **inside** the `<strong>` tag, e.g. `<strong>About the role:&nbsp;</strong>`. Browsers render this as a trailing bolded space, which can cause subtle visual misalignment with neighboring headers and an extra hidden character if a screen reader spells it out.

Where it occurs (sample):
- Senior Software Engineer - Embedded — `<strong>About the team:&nbsp;</strong>`
- Staff Software Engineer - Embedded — `<strong>About the team:&nbsp;</strong>`
- Director of Product Management, Drone as First Responder (DFR) — `<strong>About the role:&nbsp;</strong>`
- Software Engineer - Embedded — `<strong>About the team:&nbsp;</strong>`

## Inconsistency 8 — Apostrophe style is not standardized

- 46 postings mix curly `’` and straight `'` apostrophes in the **same** pre-comp body.
- 17 postings use only straight ASCII `'` (mostly the Embedded / Autonomy engineering family).
- The boilerplate Skydio intro uses `’` (curly); the modal section heading `How you'll make an impact` uses `'` (straight). Many postings therefore end up with both apostrophe styles within three lines of each other.

## Inconsistency 9 — 15 job titles have stray whitespace

Posting titles themselves (the `H1` on each posting page and the entry text on `/careers`) have leading spaces, trailing spaces, or doubled spaces. Examples:

- `'Electrical Engineer (all levels) '`
- `'Senior Software Engineer - Embedded '`
- `'Senior Software Engineer,  Data Platform '`
- `'Staff Global Supply Manager,  Mechanicals'`
- `'Autonomy Engineer - ML & DL Infrastructure '`
- `'Senior Autonomy Engineer - Data Curation '`
- `'Senior Autonomy Engineer - Controls '`
- `' Electrical Engineer (Sustaining/Validation)'`
- `' Senior Software Engineer,  Infrastructure'`
- `'Success Systems Specialist '`
- `'Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM'`
- `'Senior Software Engineer - Mobile Platform '`
- `' Software Engineer - Infrastructure'`
- `'Field Support Representative '`
- `'Manager, Logistics '`

These render as slightly off-aligned card titles in the careers grid and produce inconsistent URL slugs in Ashby.

## Inconsistency 10 — Paired SF/Zurich postings have drifted apart

Several roles exist as duplicate postings (same title, different location). In four of the eight paired roles the two copies differ in **length and content**:

| Title | Locations & pre-comp character counts |
|---|---|
| Autonomy Engineer - Deep Learning | San Mateo, California, United States — 3898 / Zurich, Switzerland — 3932 |
| Senior Autonomy Engineer - Deep Learning | San Mateo, California, United States — 3481 / Zurich, Switzerland — 3452 |
| Autonomy Engineer - Deep Learning Infrastructure | Zurich, Switzerland — 4603 / San Mateo, California, United States — 4811 |
| Autonomy Engineer - Deep Learning Model Acceleration | Zurich, Switzerland — 4607 / San Mateo, California, United States — 4603 |

Implication: a Zurich applicant and a San Mateo applicant looking at "the same" job today are reading different descriptions. (Some drift may be deliberate — local language about hybrid policy — but at minimum it deserves a sanity check.)

## Inconsistency 11 — 6 postings have no Compensation block at all

Most postings end with a `Compensation:` paragraph (US$ range, equity language, benefits boilerplate, EEO language). The following postings have **none** of that — i.e. the entire body is what this report analyses, and no salary information is published at all:

- Full Stack Product Counsel — San Mateo, California, United States
- Supplier Quality Engineer, Sustaining — Taiwan
- Senior Technical Support Representative - Japan — Tokyo, Japan
- Workplace Experience Coordinator Part-Time — Zurich, Switzerland
- Autonomy Engineer Intern - Deep Learning (Computational Photography) — Zurich, Switzerland
- Autonomy Engineer Intern - Deep Learning (Computational Photography) — San Mateo, California, United States

Most are international (Switzerland, Japan, Taiwan, Finland) where US pay-transparency law does not apply, but the *Full Stack Product Counsel* posting (San Mateo, CA) is missing a compensation block despite being a California role, which is worth checking against SB 1162.

---

## Appendix — Per-posting formatting inventory

Every posting, with its pre-compensation formatting fingerprint. "Section-header style" is what tag(s) the posting uses to mark sections like "About the Role"; "Anomaly flags" are deviations from the modal pattern.

| # | Posting | Department | Section-header style | `<h*>` | `<u>` | `<em>` | `<br>` | List | Anomaly flags |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Staff Technical Recruiter | Operations | <p><strong> + <p><u> | — | 1 | — | — | ul | underline section head |
| 2 | PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) | R&D | <h3> + <p><strong> | h3×3 | — | — | — | ul | uses heading tags |
| 3 | Wireless Hardware Engineer Intern | R&D | <p><strong> | — | — | — | 3 | ul | — |
| 4 | Electrical Engineer (all levels) | R&D | <p><strong> | — | — | — | 2 | ul | title whitespace |
| 5 | Senior Software Engineer - Embedded | R&D | <p><strong> | — | — | — | — | ul | title whitespace |
| 6 | Engineering Manager - Autonomy | R&D | <p><strong> | — | — | — | 1 | ul | — |
| 7 | Wireless Software Engineer | R&D | <p><strong> | — | — | — | — | ul | — |
| 8 | Senior Wireless Systems Performance Engineer | R&D | <p><strong> | — | — | — | — | ul | — |
| 9 | Staff Software Engineer, Frontend | R&D | <p><strong> | — | — | — | — | ul | — |
| 10 | Senior Technical Recruiter - Hardware Operations | Operations | <p><strong> + <p><u> | — | 1 | — | 4 | ul | underline section head; 4× `<br>` |
| 11 | Staff Software Engineer - Embedded | R&D | <p><strong> | — | — | — | — | ul | — |
| 12 | Technical Support Specialist - West Coast | Operations | <p><strong> | — | — | — | — | ul | — |
| 13 | Senior Technical Recruiter | Operations | <p><strong> + <p><u> | — | 1 | — | 2 | ul | underline section head |
| 14 | Director of Product Management, Drone as First Responder (DFR) | R&D | <p><strong> | — | — | — | 4 | ul | 4× `<br>` |
| 15 | Software Engineer - Embedded | R&D | <p><strong> | — | — | — | — | ul | — |
| 16 | Senior Software Engineer, Full Stack | R&D | <p><strong> | — | 1 | — | 1 | ul | — |
| 17 | Senior Software Engineer,  Data Platform | R&D | <p><strong> | — | — | — | 1 | ul | title whitespace |
| 18 | Electric Motor / Propulsion Engineer | R&D | <p><strong> | — | — | 1 | 1 | ul | italic |
| 19 | PhD Autonomy Engineer Intern - Deep Learning or Computer Vision | R&D | <p><strong> | — | — | — | 1 | ul | — |
| 20 | Customer Success Manager, DFR Majors - Northeast | Operations | <p><strong> | — | — | — | — | ul | — |
| 21 | Autonomy Engineer - Deep Learning | R&D | <p><strong> | — | — | — | — | ul | — |
| 22 | Senior Autonomy Engineer - Deep Learning | R&D | <p><strong> | — | — | — | 2 | ul | — |
| 23 | Senior Autonomy Engineer - Deep Learning | R&D | <p><strong> | — | — | — | 3 | ul | — |
| 24 | Autonomy Engineer - Deep Learning Infrastructure | R&D | <p><strong> | — | — | — | 6 | ul | 6× `<br>` |
| 25 | Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 | R&D | <p><strong> | — | — | — | 1 | ul | — |
| 26 | Autonomy Engineer - Deep Learning Model Acceleration | R&D | <p><strong> | — | — | — | 6 | ul | 6× `<br>` |
| 27 | Autonomy Engineer - Deep Learning Infrastructure | R&D | <p><strong> | — | — | — | 8 | ul | 8× `<br>` |
| 28 | Autonomy Software Engineer | R&D | <p><strong> | — | — | — | 4 | ul | 4× `<br>` |
| 29 | Autonomy Engineer - Deep Learning | R&D | <p><strong> | — | — | — | 1 | ul | — |
| 30 | Autonomy Engineer - Deep Learning Model Acceleration | R&D | <p><strong> | — | — | — | 6 | ul | 6× `<br>` |
| 31 | Autonomy Engineer Intern Fall 2026 | R&D | <p><strong> | — | — | — | — | ul | — |
| 32 | Systems Integration and Test Engineer (Mid to Senior Level) | R&D | <p><strong> | — | — | — | 1 | ul | — |
| 33 | Staff Global Supply Manager,  Mechanicals | Operations | <p><strong> | — | — | — | 1 | ul | title whitespace |
| 34 | Full Stack Product Counsel | Operations | <h3> | h3×4 | 1 | — | — | ul | uses heading tags; no compensation block |
| 35 | Senior Brand Designer (Contract) | Operations | <p><strong> | — | — | — | 2 | ul | — |
| 36 | Staff Product Manager, Platform & Infrastructure | R&D | <p><strong> | — | — | — | 1 | ul | — |
| 37 | Product Design Engineer (All Levels) | R&D | <p><strong> | — | — | — | 1 | ul | — |
| 38 | Supplier Quality Engineer, Sustaining | Operations | <p><strong> | — | — | — | — | ul | no compensation block |
| 39 | Staff Software Engineer, Full Stack | R&D | <p><strong> | — | — | — | — | ul | — |
| 40 | Field Marketing Event Manager | Operations | <h3> + <p><strong> | h3×7 | — | — | — | ul | uses heading tags |
| 41 | GTM Data Engineer Intern | Operations | <p><strong> | — | — | — | 3 | ul | — |
| 42 | Senior Customer Support Representative - India | Operations | <p><strong> | — | — | — | — | ul | — |
| 43 | Sales Planning Analyst Intern | Operations | <p><strong> | — | — | — | 1 | ul | — |
| 44 | Senior Supplier Quality Engineer | Operations | <p><strong> | — | — | — | 2 | ul | — |
| 45 | Enterprise Account Manager (MoD/ MoI) – EMEA (Germany) | Operations | <p><strong> | — | — | — | 2 | ul | — |
| 46 | Field Support Representative (Southwest, Remote) | Operations | <p><strong> | — | — | — | — | ul | — |
| 47 | Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland) | Operations | <p><strong> | — | — | — | 2 | ul | — |
| 48 | Enterprise Account Manager (MoD/ MoI) – EMEA (Finland) | Operations | <p><strong> | — | — | — | 2 | ul | — |
| 49 | Autonomy Engineer - ML & DL Infrastructure | R&D | <p><strong> | — | — | — | — | ul | title whitespace |
| 50 | Manufacturing Quality Supervisor | Operations | <p><strong> | — | — | — | — | ul | — |
| 51 | Senior Software Engineer, Frontend | R&D | <p><strong> | — | — | — | — | ul | — |
| 52 | Software Engineer, Full Stack | R&D | <p><strong> | — | — | — | — | ul | — |
| 53 | Product Support Engineer | Operations | <p><strong> | — | — | — | 2 | ul | — |
| 54 | Mission Success Operations Manager | Operations | <p><strong> | — | — | — | — | ul | — |
| 55 | Senior Technical Support Representative - Japan | Operations | <h1> | h1×3 | — | — | 2 | ul | uses heading tags; no compensation block |
| 56 | Revenue Operations Engineer, Quoting Systems | Operations | <p><strong> | h2×5 | — | — | 4 | ul | 4× `<br>` |
| 57 | Senior Business Operations Manager | Operations | <p><strong> | h3×3 | — | — | — | ul | — |
| 58 | Production Supervisor | Operations | <p><strong> | — | — | — | 2 | ul | — |
| 59 | Deployment Engineer - Southeast | Operations | <p><strong> | — | — | — | — | ul | — |
| 60 | Production Manager, PM Shift | Operations | <p><strong> | — | — | — | — | ul | — |
| 61 | Senior NPI Product Quality Engineer | Operations | <p><strong> | — | 1 | 1 | — | ul | italic |
| 62 | Hardware Operations Program Manager | Operations | <p><strong> | — | — | — | — | ul | — |
| 63 | Senior Hardware Test and Reliability Engineer | R&D | <p><strong> | — | — | — | — | ul | — |
| 64 | RF Design Engineer | R&D | <p><strong> | — | — | — | — | ul | — |
| 65 | Senior Autonomy Engineer - Data Curation | R&D | <p><strong> | — | — | — | — | ul | title whitespace |
| 66 | Senior Autonomy Engineer - Controls | R&D | <p><strong> | — | — | — | — | ul | title whitespace |
| 67 | Autonomy Engineer - Fixed Wing Planning & Controls | R&D | <p><strong> | — | — | — | — | ul | — |
| 68 | Senior People Analytics Analyst | Operations | <p><strong> | — | — | — | — | ul | — |
| 69 | Senior Software Engineer - Security | R&D | <p><strong> | — | — | — | — | ul | — |
| 70 | Aviation Compliance Lead | Operations | <h2> | h2×4 | — | — | 1 | ul | uses heading tags |
| 71 | Electrical Engineer (Sustaining/Validation) | R&D | <p><strong> | — | — | — | 1 | ul | title whitespace |
| 72 | Software Engineer - Cloud Simulation & Full-Stack | R&D | <h2> | h2×5 | — | — | — | ul | uses heading tags |
| 73 | Software Engineer - Simulation & Robotics Engineer | R&D | <h3> | h3×5 | — | — | — | ul | uses heading tags |
| 74 | Software Engineer - Autonomy Infrastructure, Systems and Tools | R&D | <h2> | h2×5 | — | — | — | ul | uses heading tags |
| 75 | Senior Software Engineer,  Infrastructure | R&D | <p><strong> | — | — | — | — | ul | title whitespace |
| 76 | Software Engineer - Autonomy Infrastructure, Systems and Tools | R&D | <h2> | h2×5 | — | — | — | ul | uses heading tags |
| 77 | Software Engineer - Cloud Simulation & Full-Stack | R&D | <h2> | h2×5 | — | — | — | ul | uses heading tags |
| 78 | Software Engineer - Simulation & Robotics Engineer | R&D | <h3> | h3×5 | — | — | — | ul | uses heading tags |
| 79 | Success Systems Specialist | Operations | <p><strong> | — | — | — | — | ul | title whitespace |
| 80 | Aviation Regulatory Program Manager | Operations | <h2> | h2×3 | — | — | — | ul | uses heading tags |
| 81 | PCB Layout Engineer | R&D | <p><strong> | — | — | — | 2 | ul | — |
| 82 | Program Manager, Major Deployments (South East) | Operations | <p><strong> | — | — | — | — | ul | — |
| 83 | Program Manager, Major Deployments (Mid Atlantic) | Operations | <p><strong> | — | — | — | — | ul | — |
| 84 | Senior Revenue Operations Manager | Operations | <p><strong> | — | — | — | — | ul | — |
| 85 | GTM Enablement Associate | Operations | <p><strong> | — | — | — | 2 | ul | — |
| 86 | Enterprise Account Manager, US Army | Operations | <p><strong> | — | — | — | — | ul | — |
| 87 | Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM | Operations | <p><strong> | — | — | — | — | ul | title whitespace |
| 88 | Communications Manager | Operations | <h2> | h2×3 | — | — | — | ul | uses heading tags |
| 89 | Supply Chain Intern | Operations | <p><strong> | — | — | — | 3 | ul | — |
| 90 | Senior Buyer | Operations | <p><strong> | h2×2 | — | — | — | ul | — |
| 91 | Workplace Experience Coordinator Part-Time | Operations | <p><strong> | — | — | — | 1 | ul | no compensation block |
| 92 | Senior Software Engineer - Mobile Platform | R&D | <p><strong> | — | — | — | — | ul | title whitespace |
| 93 | Senior Product Manager, Platform & Infrastructure | R&D | <p><strong> | — | — | — | 1 | ul | — |
| 94 | Director, Growth Marketing - Commercial | Operations | <p><strong> | — | — | 1 | 8 | ul | italic; 8× `<br>` |
| 95 | Program Manager, Major Deployments (Hawaii) | Operations | <p><strong> | — | — | — | — | ul | — |
| 96 | Product Support Engineer Intern | Operations | <p><strong> | — | — | — | 2 | ul | — |
| 97 | Hardware Technician | R&D | <p><strong> | — | — | — | — | ul | — |
| 98 | Software Engineer - Infrastructure | R&D | <p><strong> | — | — | — | — | ul | title whitespace |
| 99 | Field Support Representative | Operations | <p><strong> | — | — | — | — | ul | title whitespace |
| 100 | Autonomy Engineer Intern - Deep Learning (Computational Photography) | R&D | <p><strong> | — | — | — | — | ul | no compensation block |
| 101 | Autonomy Engineer Intern - Deep Learning (Computational Photography) | R&D | <p><strong> | — | — | — | — | ul | no compensation block |
| 102 | Lead Staff Electrical Engineer (F10 Program) | R&D | <p><strong> | — | 1 | — | 1 | ul | — |
| 103 | Senior/Staff Embedded Software Engineer – Camera Systems | R&D | <p><strong> | — | — | — | — | ul | — |
| 104 | Sr/Staff Embedded Software Engineer - Camera Systems | R&D | <p><strong> | — | — | — | — | ul | — |
| 105 | IT Technician (Help Desk - Linux Focus) | Operations | <p><strong> | — | — | — | 8 | ul | 8× `<br>` |
| 106 | Head of Warehouse & Logistics Operations | Operations | <p><strong> | — | — | — | 1 | ul | — |
| 107 | Software Engineer Intern Fall 2026/Winter 2027 | R&D | <p><strong> | — | — | — | 4 | ul | 4× `<br>` |
| 108 | Manager, Technical Support | Operations | <p><strong> | — | — | — | — | ul | — |
| 109 | Director, Global Supply Management - Mechanicals | Operations | <p><strong> | — | — | — | — | — | no bullet list |
| 110 | Manager, Logistics | Operations | <p><strong> | — | — | — | — | ul | custom inline CSS; title whitespace |

---

## Recommendations

Roughly in order of value-for-effort:

1. **Adopt a single section-header markup pattern and template the posting.** Either:
   - **Option A (preferred, matches the majority):** `<p><strong>Heading:</strong></p>`. Pros: no surprise large headings; consistent with 94/110 postings today; only requires fixing 16 outliers.
   - **Option B:** real `<h3>` heading tags everywhere. Pros: better semantics for SEO and screen readers. Cons: needs the Ashby template/CSS tuned so `<h3>` doesn't visually dwarf the rest of the body.
   Whichever is chosen, **stop mixing them.** Today the same template ships in three flavors on the same page.

2. **Adopt a single canonical wording for the three standard section labels** and add a copy-edit lint:
   - `About the role:` (sentence case, straight ASCII apostrophe disallowed)
   - `How you'll make an impact:`
   - `What makes you a good fit:`
   Pick one casing/apostrophe convention, then run a one-time sweep through the 110 postings — this single change normalizes ~110 visible deviations.

3. **Replace `<br><br>` spacing with semantic paragraphs.** The 47 postings that contain `<br>` tags are doing it to fake vertical spacing. The careers template already gives every `<p>` consistent vertical rhythm via `min-height:1.5em`; the `<br>` tags add **extra** space only on those postings.

4. **Standardize the "PLEASE NOTE" callout** to one decoration (`<p><strong>Please note:</strong> …</p>` is the cleanest, since it matches the section-header pattern). Eliminate the underline and italic variants.

5. **Add a bullet list to the *Director, Global Supply Management — Mechanicals* posting.** It is the only posting on the board with zero list items; converting its responsibilities to `<ul>` brings it in line with everything else.

6. **Strip the custom inline CSS** from the *Manager, Logistics* posting (`margin-top:0; margin-bottom:0` on a stray `<div>`). It produces tighter spacing than every other posting around it.

7. **Sanitize posting titles** — trim leading/trailing/double spaces in the 15 affected titles. This also fixes URL-slug drift in Ashby.

8. **Normalize apostrophes to curly `’`** (or to straight `'`, but curly matches the Skydio boilerplate intro). Do this in the same copy-edit pass as recommendation #2.

9. **Remove the trailing `&nbsp;` inside `<strong>` headers** in the ~7 postings that have them (`<strong>About the role:&nbsp;</strong>` → `<strong>About the role:</strong>`).

10. **Reconcile the paired SF/Zurich postings.** Decide whether the duplicates should remain word-for-word identical (and re-sync them) or formally split into "regional variant" postings with a documented diff. Right now the drift looks accidental.

11. **Decide whether internationally-located postings need a compensation block** (cheapest answer: a localized "we follow local market practice" paragraph) so all 110 postings end with the same final section type.

12. **Lock the format in tooling.** The cheapest way to keep this audit from being needed again: a small lint script (the one added in `tools/audit_postings.py` alongside this report — `python3 tools/audit_postings.py --check` exits non-zero if any posting violates the rules above) that runs nightly against the Ashby API and surfaces drift before the team has to do another audit pass.

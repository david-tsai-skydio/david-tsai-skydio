# Skydio Careers — Job Posting Formatting Consistency Audit

*Source:* `https://www.skydio.com/careers` (and every linked `/jobs/<id>` detail page)  
*Scope:* Pre-compensation content only — everything from the job title down to (but not including) the `Compensation:` section / `#LI-XX1` tag / EEO boilerplate.  
*Postings analysed:* **112** job detail pages.  

---

## 1. How the analysis was done

Every Skydio job detail page is built from the same Astro template, so the *base* typography is technically identical across postings — they share the same global CSS (`type-h2` for the title, `type-body-2` for the location/employment-type line, and a `prose block-content` container for the body).  The visual differences that show up on the page therefore come almost entirely from the **HTML the recruiting team enters in the CMS** for each job.

For each posting I:

1. Downloaded the rendered HTML.
2. Located the prose block (`<div class="prose block-content">`).
3. Cut at the first of these markers: a *Compensation* heading, a `#LI-XXn` line, or the *“At Skydio we believe that diversity drives innovation…”* EEO paragraph.
4. Classified every top-level element before that cut by tag, role (heading vs. paragraph vs. list), and markup pattern.

Inconsistencies fall into two buckets:

- **Structural** — the markup style of section headings, list items, blank paragraphs, the presence or absence of a *Compensation* block.
- **Textual** — capitalisation, smart-vs-straight quotes, presence/absence of trailing colons, duplicated paragraphs, whitespace bugs.

Because every posting inherits the same `.prose` styles, a markup difference like `<p><strong>` vs. `<h2>` renders as a real, visible difference in size, weight, vertical rhythm, and spacing on the page.

---

## 2. Headline findings

| Issue | Affected jobs | % |
|---|---:|---:|
| No `Compensation:` block before EEO boilerplate | 20 | 18% |
| Section headings use real `<h2>`/`<h3>` instead of the standard `<p><strong>` pattern | 18 | 16% |
| Mixed heading markup styles within the *same* posting | 7 | 6% |
| Company-intro paragraph ("Skydio is the leading US drone company…") appears more than once | 4 | 4% |
| One or more empty `<p></p>` paragraphs in the body (adds inconsistent vertical gaps) | 53 | 47% |
| Bullet lists with inconsistent `<li>`-vs-`<li><p>` markup (changes line-height in the same list) | 14 | 12% |
| Job title contains leading or trailing whitespace | 12 | 11% |
| Job title contains a double-space inside the text | 4 | 4% |

---

## 3. Heading markup — the single biggest visual inconsistency

Skydio's `.prose` stylesheet renders `<p><strong>…</strong></p>` headings at roughly **body text size, bold, with paragraph-style top margin**.  In contrast, native `<h2>` and `<h3>` elements render as **distinctly larger headings with extra top margin**.  Mixing these two markup styles across postings means readers see *very different* visual hierarchies depending on which job they open.

**Heading markup style mix across the 112 postings:**

| Heading markup used in posting | # of postings |
|---|---:|
| `p+strong` | 92 |
| `h2` | 7 |
| `h3` | 3 |
| `h2, h3` | 3 |
| `h2, p+strong` | 2 |
| `h3, p+strong` | 2 |
| `no section headings at all` | 2 |
| `h1` | 1 |

**Verdict:** The dominant pattern (82 % of postings) is `<p><strong>Heading:</strong></p>`.  The 18 postings that use real `<h2>`/`<h3>` tags will visibly *look* different — bigger, more spaced-out section labels — even though they describe the same role family.  The 7 postings that *mix* both styles within a single page are the most jarring: the first section heading is a large `<h2>`, the next is a small bold paragraph, etc.

### Postings that use HTML heading tags (visibly larger headings)

| Posting | Location | Heading tag(s) used |
|---|---|---|
| Revenue Operations Analyst, CPQ | San Mateo, California, United States - Full-time | `h2`, `p+strong` |
| PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) | Zurich, Switzerland - Intern | `h3`, `p+strong` |
| Senior Business Operations Manager | San Mateo, California, United States - Full-time | `h3`, `p+strong` |
| Software Engineer - Simulation & Robotics Engineer | Zurich, Switzerland - Full-time | `h3` |
| Software Engineer - Autonomy Infrastructure, Systems and Tools | Zurich, Switzerland - Full-time | `h2` |
| Communications Manager | US Remote - Full-time | `h2` |
| Software Engineer - Cloud Simulation & Full-Stack | Zurich, Switzerland - Full-time | `h2` |
| Senior Buyer | Hayward, California, United States - Full-time | `h2`, `p+strong` |
| Software Engineer - Simulation & Robotics Engineer | San Mateo, California, United States - Full-time | `h3` |
| Software Engineer - Cloud Simulation & Full-Stack | San Mateo, California, United States - Full-time | `h2` |
| Software Engineer - Autonomy Infrastructure, Systems and Tools | San Mateo, California, United States - Full-time | `h2` |
| Logistics Operations Specialist, HQ | San Mateo, California, United States - Full-time | `h2`, `h3` |
| Engineering Program Manager | San Mateo, California, United States - Full-time | `h2`, `h3` |
| Aviation Compliance Lead | San Mateo, California, United States - Full-time | `h2` |
| GTM Engineer, Pre-Sales | US CA San Mateo - Full-time | `h2`, `h3` |
| Full Stack Product Counsel | San Mateo, California, United States - Full-time | `h3` |
| Senior Wireless Software Engineer, National Security | San Mateo, California, United States or Boston, Massachusetts, United States - Full-time | `h2` |
| Senior Technical Support Representative - Japan | Tokyo, Japan - Full-time | `h1` |

### Postings that mix heading markup styles within one page

| Posting | Location | Markup styles used |
|---|---|---|
| Revenue Operations Analyst, CPQ | San Mateo, California, United States - Full-time | `h2`, `p+strong` |
| PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) | Zurich, Switzerland - Intern | `h3`, `p+strong` |
| Senior Business Operations Manager | San Mateo, California, United States - Full-time | `h3`, `p+strong` |
| Senior Buyer | Hayward, California, United States - Full-time | `h2`, `p+strong` |
| Logistics Operations Specialist, HQ | San Mateo, California, United States - Full-time | `h2`, `h3` |
| Engineering Program Manager | San Mateo, California, United States - Full-time | `h2`, `h3` |
| GTM Engineer, Pre-Sales | US CA San Mateo - Full-time | `h2`, `h3` |

---

## 4. Section name — wording, capitalisation, punctuation

Even where the structural markup is identical, the **text** of section headings varies widely.  Below is every distinct spelling of each canonical section, with a count of how many postings use it.  Smart vs. straight apostrophes (’ vs. ') and the presence of a trailing colon are the two most common drift sources.

**About the Role** — 4 distinct spellings observed:
- `About the role:` × 47 — sentence-case
- `About the Role:` × 29
- `About the Role` × 4 — no-colon
- `About the role` × 3 — no-colon, sentence-case

**About the Team** — 4 distinct spellings observed:
- `About the Team:` × 9
- `About the team:` × 5 — sentence-case
- `About the Team` × 1 — no-colon
- `About the team` × 1 — no-colon, sentence-case

**Bonus** — 3 distinct spellings observed:
- `Bonus Experience:` × 6
- `Bonus Points:` × 3
- `Bonus points:` × 3 — sentence-case

**How You'll Make an Impact** — 7 distinct spellings observed:
- `How you'll make an impact:` × 36 — straight-quote, sentence-case
- `How You’ll Make an Impact:` × 19 — smart-quote
- `How you’ll make an impact:` × 17 — smart-quote, sentence-case
- `How you'll make an impact` × 2 — straight-quote, no-colon, sentence-case
- `How You’ll Make an Impact` × 2 — smart-quote, no-colon
- `How You'll Make an Impact:` × 1 — straight-quote
- `How you’ll make an impact` × 1 — smart-quote, no-colon, sentence-case

**Key Responsibilities** — 2 distinct spellings observed:
- `Key Responsibilities:` × 1
- `Key Responsibilities` × 1 — no-colon

**Nice to Have** — 5 distinct spellings observed:
- `Nice to have:` × 4 — sentence-case
- `Nice-to-Haves:` × 1
- `Nice to Have` × 1 — no-colon
- `Nice To Haves` × 1 — no-colon
- `Nice To Haves:` × 1

**Preferred Qualifications** — 4 distinct spellings observed:
- `Preferred Qualifications:` × 3
- `Preferred Qualifications` × 2 — no-colon
- `Desired qualifications:` × 1 — sentence-case
- `Desired Qualifications:` × 1

**Qualifications** — 2 distinct spellings observed:
- `Qualifications:` × 6
- `Qualifications` × 1 — no-colon

**Requirements** — 2 distinct spellings observed:
- `Requirements` × 2 — no-colon
- `Requirements:` × 1

**What Makes You a Good Fit** — 8 distinct spellings observed:
- `What makes you a good fit:` × 52 — sentence-case
- `What Makes You a Good Fit:` × 19
- `What would make you a good fit:` × 7 — sentence-case
- `What makes you a good fit` × 5 — no-colon, sentence-case
- `What makes you a strong fit:` × 4 — sentence-case
- `What Would Make You a Good Fit:` × 2
- `What Makes You a Good Fit` × 2 — no-colon
- `What makes you a good fit :` × 1 — space-before-colon, sentence-case

**What You'll Do** — 2 distinct spellings observed:
- `What You’ll Do:` × 6 — smart-quote
- `What You’ll Do` × 1 — smart-quote, no-colon

**Work Location** — 2 distinct spellings observed:
- `Work Location :` × 3 — space-before-colon
- `Work location` × 1 — no-colon, sentence-case

**Specific micro-issues found in heading text:**
- `What makes you a good fit :` — has a stray space before the colon (1 posting).
- `Work Location :` — same issue, used by 3 postings, while a 4th writes `Work location` with no colon.
- `Nice To Haves` vs `Nice-to-Haves:` vs `Nice to have:` — three different ways of spelling the same idea.
- `Bonus Points:` vs `Bonus points:` vs `Bonus Experience:` — same concept, three different labels and capitalisations.
- `Desired qualifications:` vs `Desired Qualifications:` — sentence case vs title case.

---

## 5. Postings with no `Compensation:` block before the EEO boilerplate

Of 112 postings, **20** jump straight from the qualifications list to the `#LI-XXn` tracking tag or the *“At Skydio we believe that diversity drives innovation…”* paragraph, with no salary information at all.  This is almost certainly intentional for non-US roles (where pay-transparency rules differ), but it is still a visible inconsistency for candidates browsing the same template and worth flagging for the team to decide if it's the right policy.

| Posting | Location | Where the pre-comp body ends |
|---|---|---|
| Autonomy Engineer - Deep Learning Infrastructure | Zurich, Switzerland - Full-time | directly at `#LI-XXn` tag |
| Autonomy Engineer - Deep Learning Model Acceleration | Zurich, Switzerland - Full-time | directly at `#LI-XXn` tag |
| Autonomy Engineer - Deep Learning | Zurich, Switzerland - Full-time | directly at `#LI-XXn` tag |
| PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) | Zurich, Switzerland - Intern | directly at `#LI-XXn` tag |
| Software Engineer - Simulation & Robotics Engineer | Zurich, Switzerland - Full-time | directly at `#LI-XXn` tag |
| Software Engineer - Autonomy Infrastructure, Systems and Tools | Zurich, Switzerland - Full-time | directly at `#LI-XXn` tag |
| Supplier Quality Engineer, Sustaining | Taiwan - Full-time | directly at `#LI-XXn` tag |
| Senior Autonomy Engineer - Deep Learning | Zurich, Switzerland - Full-time | directly at `#LI-XXn` tag |
| Software Engineer - Cloud Simulation & Full-Stack | Zurich, Switzerland - Full-time | directly at `#LI-XXn` tag |
| Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 | Zurich, Switzerland - Intern | directly at `#LI-XXn` tag |
| Autonomy Engineer - ML & DL Infrastructure | Zurich, Switzerland - Full-time | directly at `#LI-XXn` tag |
| PhD Autonomy Engineer Intern - Deep Learning or Computer Vision | San Mateo, California, United States - Intern | directly at EEO paragraph |
| Autonomy Engineer Intern - Deep Learning (Computational Photography) | Zurich, Switzerland or Tampere, Finland - Intern | directly at EEO paragraph |
| Autonomy Engineer Intern Fall 2026 | Zurich, Switzerland - Intern | directly at `#LI-XXn` tag |
| PhD Autonomy Engineer Intern - Deep Learning or Computer Vision | Zurich, Switzerland - Intern | directly at EEO paragraph |
| Full Stack Product Counsel | San Mateo, California, United States - Full-time | directly at `#LI-XXn` tag |
| Workplace Experience Coordinator Part-Time | Zurich, Switzerland - Part-time | directly at EEO paragraph |
| Autonomy Engineer Intern - Deep Learning (Computational Photography) | San Mateo, California, United States - Intern | directly at EEO paragraph |
| Autonomy Engineer - Planning and Controls | Zurich, Switzerland - Full-time | directly at `#LI-XXn` tag |
| Senior Technical Support Representative - Japan | Tokyo, Japan - Full-time | directly at EEO paragraph |

---

## 6. Other structural drift

### 6.1 Bullet lists — `<li>x</li>` vs `<li><p>x</p></li>`

The `.prose` stylesheet adds extra vertical margin around `<p>` inside `<li>`, so a list that wraps its items in `<p>` is **noticeably more spaced out** than a list that doesn't.  Postings inconsistently mix these two patterns — sometimes even within the same list.

- Postings where at least one `<ul>` mixes wrapped and unwrapped items: **14**
- Some Zurich-authored postings drop the `<p>` wrapper entirely; the same role posted in San Mateo includes it, producing visibly tighter line-spacing in the EU listings.

### 6.2 Empty `<p></p>` paragraphs inserted as ad-hoc spacing

**53** postings contain at least one empty `<p></p>` element in the pre-compensation body.  These are invisible to authors in the CMS but render as a full empty paragraph height on the page, so two postings that look identical in markup will have **different gap sizes** between sections.

### 6.3 Duplicated company-intro paragraph

4 postings open with the standard *“Skydio is the leading US drone company…”* paragraph and then repeat the same paragraph (or a near-identical variant) inside *About the Role*.  Examples:

- Autonomy Engineer - ML & DL Infrastructure — Zurich, Switzerland - Full-time
- Autonomy Engineer - ML & DL Infrastructure — San Mateo, California, United States - Full-time
- Senior Hardware Test and Reliability Engineer — San Mateo, California, United States - Full-time
- Autonomy Engineer - Deep Learning Infrastructure — San Mateo, California, United States - Full-time

### 6.4 Title / location string hygiene

- **12** job titles contain trailing whitespace ("Foo " instead of "Foo").  This is invisible in most browsers but breaks anchor IDs, share-card snippets, and screen-reader pronunciation.

Titles with leading/trailing whitespace (the rendered title HTML contains literal spaces inside `<h1>`):

- `' Senior Software Engineer,  Infrastructure'`  →  expected `'Senior Software Engineer,  Infrastructure'`
- `'Senior Autonomy Engineer - Controls '`  →  expected `'Senior Autonomy Engineer - Controls'`
- `'Senior Software Engineer - Embedded '`  →  expected `'Senior Software Engineer - Embedded'`
- `'Autonomy Engineer - ML & DL Infrastructure '`  →  expected `'Autonomy Engineer - ML & DL Infrastructure'`
- `' Electrical Engineer (Sustaining/Validation)'`  →  expected `'Electrical Engineer (Sustaining/Validation)'`
- `'Senior Software Engineer,  Data Platform '`  →  expected `'Senior Software Engineer,  Data Platform'`
- `'Field Support Representative '`  →  expected `'Field Support Representative'`
- `'Autonomy Engineer - ML & DL Infrastructure '`  →  expected `'Autonomy Engineer - ML & DL Infrastructure'`
- `' Software Engineer - Infrastructure'`  →  expected `'Software Engineer - Infrastructure'`
- `'Senior Software Engineer - Mobile Platform '`  →  expected `'Senior Software Engineer - Mobile Platform'`
- `'Manager, Logistics '`  →  expected `'Manager, Logistics'`
- `'Electrical Engineer (all levels) '`  →  expected `'Electrical Engineer (all levels)'`

Titles with a double-space inside the text:

- `'Senior Software Engineer,  Infrastructure'`
- `'Staff Global Supply Manager,  Mechanicals'`
- `'Senior Software Engineer,  Data Platform'`
- `'Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM'`

Unusual location strings (anything other than `City, Region/Country - Job-type`):

- Autonomy Engineer Intern - Deep Learning (Computational Photography) — `Zurich, Switzerland or Tampere, Finland - Intern`
- Senior Wireless Software Engineer, National Security — `San Mateo, California, United States or Boston, Massachusetts, United States - Full-time`

---

## 7. Detailed per-posting findings

Each row shows: the title, location, heading-markup styles used, and a comma-separated list of flagged issues for that posting.  `—` means no issues detected.

| # | Title | Location | Heading markup | Flags |
|---:|---|---|---|---|
| 1 | Autonomy Engineer - Deep Learning | Zurich, Switzerland - Full-time | p+strong | NO-COMP(li_tag) |
| 2 | Autonomy Engineer - Deep Learning | San Mateo, California, United States - Full-time | p+strong | — |
| 3 | Autonomy Engineer - Deep Learning Infrastructure | Zurich, Switzerland - Full-time | p+strong | NO-COMP(li_tag) |
| 4 | Autonomy Engineer - Deep Learning Infrastructure | San Mateo, California, United States - Full-time | p+strong | dup-intro, 1-blank-p |
| 5 | Autonomy Engineer - Deep Learning Model Acceleration | Zurich, Switzerland - Full-time | p+strong | NO-COMP(li_tag) |
| 6 | Autonomy Engineer - Deep Learning Model Acceleration | San Mateo, California, United States - Full-time | p+strong | — |
| 7 | Autonomy Engineer - Fixed Wing Planning & Controls | San Mateo, California, United States - Full-time | p+strong | — |
| 8 | Autonomy Engineer - ML & DL Infrastructure | Zurich, Switzerland - Full-time | p+strong | NO-COMP(li_tag), dup-intro, 2-blank-p, title-whitespace |
| 9 | Autonomy Engineer - ML & DL Infrastructure | San Mateo, California, United States - Full-time | p+strong | dup-intro, 2-blank-p, title-whitespace |
| 10 | Autonomy Engineer - Planning and Controls | Zurich, Switzerland - Full-time | p+strong | NO-COMP(li_tag) |
| 11 | Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 | Zurich, Switzerland - Intern | p+strong | NO-COMP(li_tag) |
| 12 | Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 | San Mateo, California, United States - Intern | p+strong | — |
| 13 | Autonomy Engineer Intern - Deep Learning (Computational Photography) | Zurich, Switzerland or Tampere, Finland - Intern | p+strong | NO-COMP(diversity_boilerplate) |
| 14 | Autonomy Engineer Intern - Deep Learning (Computational Photography) | San Mateo, California, United States - Intern | p+strong | NO-COMP(diversity_boilerplate) |
| 15 | Autonomy Engineer Intern Fall 2026 | San Mateo, California, United States - Intern | p+strong | — |
| 16 | Autonomy Engineer Intern Fall 2026 | Zurich, Switzerland - Intern | p+strong | NO-COMP(li_tag) |
| 17 | Autonomy Software Engineer | San Mateo, California, United States - Full-time | p+strong | — |
| 18 | Aviation Compliance Lead | San Mateo, California, United States - Full-time | h2 | uses-h2/h3, 1-blank-p |
| 19 | Communications Manager | US Remote - Full-time | h2 | uses-h2/h3, 2-blank-p, inconsistent-li |
| 20 | CSM Manager - Public Safety (Major Markets) | US Remote - Full-time | p+strong | 4-blank-p |
| 21 | Customer Success Manager, Commercial | US Remote - Full-time | p+strong | 4-blank-p |
| 22 | Customer Success Manager, DFR Majors - Southeast | US Remote - Full-time | p+strong | — |
| 23 | Customer Success Manager, DFR Mid-Market - Northeast | US Remote - Full-time | p+strong | 5-blank-p |
| 24 | Deployment Engineer - Southeast | US Remote - Full-time | p+strong | 3-blank-p, inconsistent-li |
| 25 | Director of Product Management, Drone as First Responder (DFR) | San Mateo, California, United States - Full-time | p+strong | — |
| 26 | Director, Global Supply Management - Mechanicals | San Mateo, California, United States - Full-time | p+strong | 3-blank-p |
| 27 | Director, Growth Marketing - Commercial | San Mateo, California, United States - Full-time | p+strong | 3-blank-p |
| 28 | Electrical Engineer (all levels) | San Mateo, California, United States - Full-time | p+strong | title-whitespace |
| 29 | Electrical Engineer (Sustaining/Validation) | San Mateo, California, United States - Full-time | p+strong | title-whitespace |
| 30 | Engineering Manager - Autonomy | San Mateo, California, United States - Full-time | p+strong | — |
| 31 | Engineering Program Manager | San Mateo, California, United States - Full-time | h2, h3 | mixed-heading-markup, uses-h2/h3, 2-blank-p, inconsistent-li |
| 32 | Enterprise Account Manager (MoD/ MoI) – EMEA (Finland) | Tampere, Finland - Full-time | p+strong | — |
| 33 | Enterprise Account Manager (MoD/ MoI) – EMEA (Germany) | Germany - Full-time | p+strong | — |
| 34 | Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland) | Zurich, Switzerland - Full-time | p+strong | — |
| 35 | Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM | US Remote - Full-time | p+strong | title-double-space |
| 36 | Enterprise Account Manager, US Army | US Remote - Full-time | p+strong | — |
| 37 | Field Service Technician | US CA San Mateo - Full-time | p+strong | — |
| 38 | Field Support Representative | US Remote - Full-time | p+strong | title-whitespace |
| 39 | Field Support Representative (Southwest, Remote) | US Remote - Full-time | p+strong | 3-blank-p |
| 40 | Full Stack Product Counsel | San Mateo, California, United States - Full-time | h3 | NO-COMP(li_tag), uses-h2/h3, 6-blank-p |
| 41 | GTM Data Engineer Intern | San Mateo, California, United States - Intern | p+strong | 2-blank-p |
| 42 | GTM Enablement Associate | San Mateo, California, United States - Full-time | p+strong | 1-blank-p |
| 43 | GTM Engineer, Pre-Sales | US CA San Mateo - Full-time | h2, h3 | mixed-heading-markup, uses-h2/h3, 2-blank-p |
| 44 | Hardware Operations Program Manager | Hayward, California, United States - Full-time | p+strong | 1-blank-p, inconsistent-li |
| 45 | IT Technician (Help Desk - Linux Focus) | Hayward, California, United States - Full-time | p+strong | 2-blank-p, inconsistent-li |
| 46 | Lead Staff Electrical Engineer | San Mateo, California, United States - Full-time | p+strong | 2-blank-p |
| 47 | Logistics Operations Specialist, HQ | San Mateo, California, United States - Full-time | h2, h3 | mixed-heading-markup, uses-h2/h3, 4-blank-p |
| 48 | Manager, Logistics | Hayward, California, United States - Full-time | p+strong | 1-blank-p, inconsistent-li, title-whitespace |
| 49 | Manager, Technical Support | San Mateo, California, United States - Full-time | p+strong | — |
| 50 | Middleware Software Engineer Intern - Fall 2026 | San Mateo, California, United States - Intern | p+strong | — |
| 51 | Mission Success Operations Manager | US Remote - Full-time | p+strong | inconsistent-li |
| 52 | PCB Layout Engineer | San Mateo, California, United States - Full-time | p+strong | — |
| 53 | PhD Autonomy Engineer Intern - Deep Learning or Computer Vision | San Mateo, California, United States - Intern | — | NO-COMP(diversity_boilerplate) |
| 54 | PhD Autonomy Engineer Intern - Deep Learning or Computer Vision | Zurich, Switzerland - Intern | — | NO-COMP(diversity_boilerplate) |
| 55 | PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) | Zurich, Switzerland - Intern | h3, p+strong | NO-COMP(li_tag), mixed-heading-markup, uses-h2/h3 |
| 56 | Product Design Engineer (All Levels) | San Mateo, California, United States - Full-time | p+strong | — |
| 57 | Product Support Engineer | San Mateo, California, United States - Full-time | p+strong | 2-blank-p |
| 58 | Program Manager, Commercial Programs | US AR Remote - Full-time | p+strong | 5-blank-p |
| 59 | Public Safety Strategist (West Coast, Midwest, or Pacific North West) | US Remote - Full-time | p+strong | inconsistent-li |
| 60 | Revenue Operations Analyst, CPQ | San Mateo, California, United States - Full-time | h2, p+strong | mixed-heading-markup, uses-h2/h3, 2-blank-p |
| 61 | RF Design Engineer | San Mateo, California, United States - Full-time | p+strong | — |
| 62 | Sales Planning Analyst Intern | San Mateo, California, United States - Intern | p+strong | 1-blank-p |
| 63 | Senior Autonomy Engineer - Controls | San Mateo, California, United States - Full-time | p+strong | title-whitespace |
| 64 | Senior Autonomy Engineer - Deep Learning | Zurich, Switzerland - Full-time | p+strong | NO-COMP(li_tag) |
| 65 | Senior Autonomy Engineer - Deep Learning | San Mateo, California, United States - Full-time | p+strong | 1-blank-p |
| 66 | Senior Business Operations Manager | San Mateo, California, United States - Full-time | h3, p+strong | mixed-heading-markup, uses-h2/h3, 2-blank-p, inconsistent-li |
| 67 | Senior Buyer | Hayward, California, United States - Full-time | h2, p+strong | mixed-heading-markup, uses-h2/h3, 3-blank-p |
| 68 | Senior Customer Support Representative - India | Bangalore, India - Full-time | p+strong | 1-blank-p |
| 69 | Senior Director, Product Management, Drone as First Responder (DFR) | San Mateo, California, United States - Full-time | p+strong | — |
| 70 | Senior Engineering Manager, Infrastructure | San Mateo, California, United States - Full-time | p+strong | — |
| 71 | Senior Hardware Test and Reliability Engineer | San Mateo, California, United States - Full-time | p+strong | dup-intro |
| 72 | Senior Manager, Training | US Remote - Full-time | p+strong | 1-blank-p |
| 73 | Senior NPI Product Quality Engineer | San Mateo, California, United States - Full-time | p+strong | — |
| 74 | Senior Product Manager, Platform & Infrastructure | San Mateo, California, United States - Full-time | p+strong | 6-blank-p |
| 75 | Senior Revenue Operations Manager | San Mateo, California, United States - Full-time | p+strong | 2-blank-p |
| 76 | Senior RF Design Engineer | San Mateo, California, United States - Full-time | p+strong | 2-blank-p |
| 77 | Senior Software Engineer - Embedded | San Mateo, California, United States - Full-time | p+strong | title-whitespace |
| 78 | Senior Software Engineer - Mobile Platform | San Mateo, California, United States - Full-time | p+strong | 3-blank-p, title-whitespace |
| 79 | Senior Software Engineer - Security | San Mateo, California, United States - Full-time | p+strong | — |
| 80 | Senior Software Engineer,  Data Platform | San Mateo, California, United States - Full-time | p+strong | title-whitespace, title-double-space |
| 81 | Senior Software Engineer,  Infrastructure | San Mateo, California, United States - Full-time | p+strong | title-whitespace, title-double-space |
| 82 | Senior Software Engineer, Frontend | San Mateo, California, United States - Full-time | p+strong | 5-blank-p |
| 83 | Senior Software Engineer, Full Stack | San Mateo, California, United States - Full-time | p+strong | — |
| 84 | Senior Technical Recruiter | San Mateo, California, United States - Full-time | p+strong | — |
| 85 | Senior Technical Recruiter - Hardware Operations | San Mateo, California, United States - Full-time | p+strong | — |
| 86 | Senior Technical Support Representative - Japan | Tokyo, Japan - Full-time | h1 | NO-COMP(diversity_boilerplate), uses-h2/h3, 1-blank-p, inconsistent-li |
| 87 | Senior Wireless Software Engineer, National Security | San Mateo, California, United States or Boston, Massachusetts, United States - Full-time | h2 | uses-h2/h3, 3-blank-p, inconsistent-li |
| 88 | Senior Wireless Systems Performance Engineer | San Mateo, California, United States - Full-time | p+strong | — |
| 89 | Senior/Staff Embedded Software Engineer – Camera Systems | San Mateo, California, United States - Full-time | p+strong | 2-blank-p, inconsistent-li |
| 90 | Software Engineer - Autonomy Infrastructure, Systems and Tools | Zurich, Switzerland - Full-time | h2 | NO-COMP(li_tag), uses-h2/h3, 1-blank-p |
| 91 | Software Engineer - Autonomy Infrastructure, Systems and Tools | San Mateo, California, United States - Full-time | h2 | uses-h2/h3, 1-blank-p |
| 92 | Software Engineer - Cloud Simulation & Full-Stack | Zurich, Switzerland - Full-time | h2 | NO-COMP(li_tag), uses-h2/h3, 2-blank-p |
| 93 | Software Engineer - Cloud Simulation & Full-Stack | San Mateo, California, United States - Full-time | h2 | uses-h2/h3, 2-blank-p |
| 94 | Software Engineer - Embedded | San Mateo, California, United States - Full-time | p+strong | — |
| 95 | Software Engineer - Infrastructure | San Mateo, California, United States - Full-time | p+strong | title-whitespace |
| 96 | Software Engineer - Simulation & Robotics Engineer | Zurich, Switzerland - Full-time | h3 | NO-COMP(li_tag), uses-h2/h3, 1-blank-p |
| 97 | Software Engineer - Simulation & Robotics Engineer | San Mateo, California, United States - Full-time | h3 | uses-h2/h3, 2-blank-p |
| 98 | Software Engineer Intern Fall 2026/Winter 2027 | San Mateo, California, United States - Intern | p+strong | 1-blank-p |
| 99 | Software Engineer, Full Stack | San Mateo, California, United States - Full-time | p+strong | — |
| 100 | Sr/Staff Embedded Software Engineer - Camera Systems | Tampere, Finland - Full-time | p+strong | 3-blank-p, inconsistent-li |
| 101 | Staff Global Supply Manager,  Mechanicals | San Mateo, California, United States - Full-time | p+strong | 1-blank-p, title-double-space |
| 102 | Staff Product Manager, Platform & Infrastructure | San Mateo, California, United States - Full-time | p+strong | 6-blank-p |
| 103 | Staff Software Engineer - Embedded | San Mateo, California, United States - Full-time | p+strong | — |
| 104 | Staff Software Engineer - Security | San Mateo, California, United States - Full-time | p+strong | — |
| 105 | Staff Software Engineer, Frontend | San Mateo, California, United States - Full-time | p+strong | 5-blank-p |
| 106 | Staff Software Engineer, Full Stack | San Mateo, California, United States - Full-time | p+strong | — |
| 107 | Staff Technical Recruiter | San Mateo, California, United States - Full-time | p+strong | — |
| 108 | Supplier Quality Engineer, Sustaining | Taiwan - Full-time | p+strong | NO-COMP(li_tag), 1-blank-p |
| 109 | Supply Chain Intern | San Mateo, California, United States - Intern | p+strong | — |
| 110 | Systems Integration and Test Engineer (Mid to Senior Level) | San Mateo, California, United States - Full-time | p+strong | — |
| 111 | Wireless Software Engineer | San Mateo, California, United States - Full-time | p+strong | 2-blank-p, inconsistent-li |
| 112 | Workplace Experience Coordinator Part-Time | Zurich, Switzerland - Part-time | p+strong | NO-COMP(diversity_boilerplate), 1-blank-p |

---

## 8. Recommendations — standardising the formatting

Issues are listed in priority order; tackling 1 and 2 alone removes the great majority of the visible inconsistency.

1. **Settle on a single heading markup style and enforce it.**  Pick *one* of:
   - `<p><strong>Heading:</strong></p>` (the current majority — visually subtle, looks like emphasised body copy), **or**
   - `<h3>Heading</h3>` (semantic, larger, better for screen readers).

   Once chosen, convert the ~18 postings that use the other style.  This is the single biggest source of visual inconsistency across postings.

2. **Lock down a canonical section vocabulary and order.**  Recommended:
   1. *About the Role*
   2. *About the Team* (optional)
   3. *How You'll Make an Impact* — never *Areas of Responsibility* / *What You'll Do* in parallel
   4. *What Makes You a Good Fit* — never *Qualifications* / *Requirements* / *What Would Make You a Good Fit*
   5. *Nice to Have* (optional) — never *Bonus Points* / *Bonus Experience* / *Nice-to-Haves*
   6. *Compensation*

   Decide title-case vs sentence-case **once**, decide trailing-colon **once**, decide straight-apostrophe vs smart-apostrophe **once**, then bulk-edit every posting.  Today *About the Role* alone has 4 spellings, *How You'll Make an Impact* has 7, *What Makes You a Good Fit* has 6.

3. **Strip stray whitespace.**  Trim leading/trailing spaces from every job title and every section heading (e.g. `What makes you a good fit :`, `Work Location :`).

4. **Remove ad-hoc empty paragraphs.**  53 postings rely on empty `<p></p>` elements for spacing.  Spacing between sections should come from CSS, not from inserted blank paragraphs that vary by posting.

5. **Use a single bullet-list markup style.**  Either always wrap `<li>` content in `<p>`, or never do — but pick one.  The current mix produces visibly different line-spacing in postings that are otherwise identical.

6. **Don't repeat the company intro.**  4 postings paste *Skydio is the leading US drone company…* twice (once in the page intro, once at the top of *About the Role*).  Pick one location.

7. **Decide once whether non-US postings should include a Compensation section.**  20 postings (mostly Zurich/Tampere/Tokyo/Taiwan/India) omit it.  If this is policy, the EEO/legal page should document it; if not, add the missing compensation language to those 20 postings.

8. **Add a CMS lint step.**  Most issues above are detectable by a 50-line Python script (this report is its output).  Running such a linter on every CMS publish would catch new drift before it ships.

---

## 9. Appendix — index of all 112 postings analysed

| # | Job ID | Title | Location |
|---:|---|---|---|
| 1 | `1208ec60-0fb6-4e5d-bf1f-af1312139a84` | Autonomy Engineer - Deep Learning | Zurich, Switzerland - Full-time |
| 2 | `cc83824e-a1cd-4bc7-9206-7264da9fbd61` | Autonomy Engineer - Deep Learning | San Mateo, California, United States - Full-time |
| 3 | `06234e2e-6285-43ce-9ae5-417cbfb85436` | Autonomy Engineer - Deep Learning Infrastructure | Zurich, Switzerland - Full-time |
| 4 | `dcb04687-9b4f-425d-8c37-1111cf3ccf3d` | Autonomy Engineer - Deep Learning Infrastructure | San Mateo, California, United States - Full-time |
| 5 | `0aff9e3d-6c59-4463-845c-850b78b48172` | Autonomy Engineer - Deep Learning Model Acceleration | Zurich, Switzerland - Full-time |
| 6 | `cd6d8410-419b-4713-8d4d-7eb72b134d5a` | Autonomy Engineer - Deep Learning Model Acceleration | San Mateo, California, United States - Full-time |
| 7 | `20754382-05e7-4cb6-a0f9-0daf9338ba78` | Autonomy Engineer - Fixed Wing Planning & Controls | San Mateo, California, United States - Full-time |
| 8 | `7a611e90-4034-4e35-acce-388f48f7d3c0` | Autonomy Engineer - ML & DL Infrastructure | Zurich, Switzerland - Full-time |
| 9 | `b6be08f7-89c0-48dd-b427-f587f23dbf34` | Autonomy Engineer - ML & DL Infrastructure | San Mateo, California, United States - Full-time |
| 10 | `d5a3ac9c-7b50-4e51-9600-f3c3105652cd` | Autonomy Engineer - Planning and Controls | Zurich, Switzerland - Full-time |
| 11 | `611a7f87-bc4c-468f-976f-ecd33b731fa3` | Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 | Zurich, Switzerland - Intern |
| 12 | `c84945f0-b8e0-4272-b636-265d6611a8eb` | Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 | San Mateo, California, United States - Intern |
| 13 | `92a7a891-d332-459c-9aa8-e96afea4f2a4` | Autonomy Engineer Intern - Deep Learning (Computational Photography) | Zurich, Switzerland or Tampere, Finland - Intern |
| 14 | `d13e3179-e646-4873-84a6-d492a692bc25` | Autonomy Engineer Intern - Deep Learning (Computational Photography) | San Mateo, California, United States - Intern |
| 15 | `17f6173b-c96f-4b02-a6b5-da0a91ad95e5` | Autonomy Engineer Intern Fall 2026 | San Mateo, California, United States - Intern |
| 16 | `c48dabe8-cb67-4694-aacc-f9ef4d34ae50` | Autonomy Engineer Intern Fall 2026 | Zurich, Switzerland - Intern |
| 17 | `a48fe41b-030b-4f11-bf25-df7446151854` | Autonomy Software Engineer | San Mateo, California, United States - Full-time |
| 18 | `b9f9047b-1555-4978-9bff-70eae58a6b17` | Aviation Compliance Lead | San Mateo, California, United States - Full-time |
| 19 | `50567d8d-2903-494f-8e08-7c8ca734dc3a` | Communications Manager | US Remote - Full-time |
| 20 | `f749f019-6c19-44ee-be4e-8434d231b9bf` | CSM Manager - Public Safety (Major Markets) | US Remote - Full-time |
| 21 | `04384b35-fe97-46ea-9d5d-befed9bce9a0` | Customer Success Manager, Commercial | US Remote - Full-time |
| 22 | `3d4ac015-a6db-4a8d-9fec-557eb92eaf8d` | Customer Success Manager, DFR Majors - Southeast | US Remote - Full-time |
| 23 | `5c7a2b78-99d8-44f4-8c51-258c331a331d` | Customer Success Manager, DFR Mid-Market - Northeast | US Remote - Full-time |
| 24 | `6138ba1c-c048-407d-9ea2-7b51a3d38756` | Deployment Engineer - Southeast | US Remote - Full-time |
| 25 | `129a5bad-ca1d-4eda-843b-96f4581f3c43` | Director of Product Management, Drone as First Responder (DFR) | San Mateo, California, United States - Full-time |
| 26 | `eb7fbbdb-3346-4f7f-a202-8bfd3441217a` | Director, Global Supply Management - Mechanicals | San Mateo, California, United States - Full-time |
| 27 | `00d0bdc5-89ad-4182-8512-ab0a028953f6` | Director, Growth Marketing - Commercial | San Mateo, California, United States - Full-time |
| 28 | `f0c26a3c-d999-4dc2-8812-b3835f633ded` | Electrical Engineer (all levels) | San Mateo, California, United States - Full-time |
| 29 | `8e50c7da-2868-4383-af1f-920584d537fc` | Electrical Engineer (Sustaining/Validation) | San Mateo, California, United States - Full-time |
| 30 | `849ae77c-5ca2-42b5-812b-8b3ad4524a89` | Engineering Manager - Autonomy | San Mateo, California, United States - Full-time |
| 31 | `b49e6784-2183-4de4-a0a1-7661203c254a` | Engineering Program Manager | San Mateo, California, United States - Full-time |
| 32 | `d6f731e8-c530-4123-8b52-0e7cab164887` | Enterprise Account Manager (MoD/ MoI) – EMEA (Finland) | Tampere, Finland - Full-time |
| 33 | `12e9a494-9a89-457c-9dc7-2ef9ccdba17c` | Enterprise Account Manager (MoD/ MoI) – EMEA (Germany) | Germany - Full-time |
| 34 | `1d4977a2-c2e7-44ad-820b-253ff8355800` | Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland) | Zurich, Switzerland - Full-time |
| 35 | `e69362bc-5891-486e-be75-6bf25187ccf5` | Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM | US Remote - Full-time |
| 36 | `19559b4c-ed09-41eb-b1aa-f000a855b8fe` | Enterprise Account Manager, US Army | US Remote - Full-time |
| 37 | `0e503e13-efe0-4a33-a58d-8ce995e5f20e` | Field Service Technician | US CA San Mateo - Full-time |
| 38 | `b053b0e2-005c-4e77-95f3-26c7354e6095` | Field Support Representative | US Remote - Full-time |
| 39 | `9b93e7c2-e5d5-48b2-a2d2-8df71e0d8357` | Field Support Representative (Southwest, Remote) | US Remote - Full-time |
| 40 | `c9e40dab-ae7d-4034-a335-b3e05d419672` | Full Stack Product Counsel | San Mateo, California, United States - Full-time |
| 41 | `b90b9b3b-e326-4fb6-85bd-fe52bec5f180` | GTM Data Engineer Intern | San Mateo, California, United States - Intern |
| 42 | `2b3fea3b-e1b5-4497-9607-e9864019b0e7` | GTM Enablement Associate | San Mateo, California, United States - Full-time |
| 43 | `c0a67a10-0cda-4892-b9a5-8eadda765587` | GTM Engineer, Pre-Sales | US CA San Mateo - Full-time |
| 44 | `55b393cf-124c-46f8-bd83-8c62e3ce628b` | Hardware Operations Program Manager | Hayward, California, United States - Full-time |
| 45 | `28c865cf-6aa4-45d1-ae13-34bb8f6b776b` | IT Technician (Help Desk - Linux Focus) | Hayward, California, United States - Full-time |
| 46 | `1bbcf144-7057-4a6e-9d51-4924bfda52b9` | Lead Staff Electrical Engineer | San Mateo, California, United States - Full-time |
| 47 | `a769eb66-442c-4ea9-8d60-8fd9b6cffe26` | Logistics Operations Specialist, HQ | San Mateo, California, United States - Full-time |
| 48 | `eeb4b52f-d4e6-4823-9e4b-0ce75041d928` | Manager, Logistics | Hayward, California, United States - Full-time |
| 49 | `2b312ffb-26c3-4b7f-8904-acbc4e51934b` | Manager, Technical Support | San Mateo, California, United States - Full-time |
| 50 | `7d9dbb60-4ca1-4ba8-8bae-5ebfded4a915` | Middleware Software Engineer Intern - Fall 2026 | San Mateo, California, United States - Intern |
| 51 | `501a3067-e906-4354-b211-ac70db6accf4` | Mission Success Operations Manager | US Remote - Full-time |
| 52 | `eb2f4124-9bd6-49f9-9636-03152c573f7d` | PCB Layout Engineer | San Mateo, California, United States - Full-time |
| 53 | `8d3979a8-c791-4825-8cf4-9b25479b9519` | PhD Autonomy Engineer Intern - Deep Learning or Computer Vision | San Mateo, California, United States - Intern |
| 54 | `c783c8dd-f604-47d0-aae0-187af89c81b4` | PhD Autonomy Engineer Intern - Deep Learning or Computer Vision | Zurich, Switzerland - Intern |
| 55 | `12590806-3cf0-4bc3-930b-12b53e227a5c` | PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) | Zurich, Switzerland - Intern |
| 56 | `3f02ead1-8efe-4e3f-9c75-625e74ab57d1` | Product Design Engineer (All Levels) | San Mateo, California, United States - Full-time |
| 57 | `a4f131a0-4dde-46ce-85a1-c83fc3e0f21e` | Product Support Engineer | San Mateo, California, United States - Full-time |
| 58 | `29ee46f0-d9ea-4a59-a671-3bb024450d04` | Program Manager, Commercial Programs | US AR Remote - Full-time |
| 59 | `3a694691-50c2-43cf-b969-f40bad1d9e39` | Public Safety Strategist (West Coast, Midwest, or Pacific North West) | US Remote - Full-time |
| 60 | `02d54431-2747-417d-8234-e72c316fed87` | Revenue Operations Analyst, CPQ | San Mateo, California, United States - Full-time |
| 61 | `f72f1fa5-d3d6-459e-8722-a94ce92ad1c8` | RF Design Engineer | San Mateo, California, United States - Full-time |
| 62 | `712900e5-ff75-4e07-8f88-626d4f8ab653` | Sales Planning Analyst Intern | San Mateo, California, United States - Intern |
| 63 | `58b4cdf6-5630-4dd0-aab3-a1ed4d599466` | Senior Autonomy Engineer - Controls | San Mateo, California, United States - Full-time |
| 64 | `4ded3e5e-cdfe-4dc5-bbaf-0d3023521246` | Senior Autonomy Engineer - Deep Learning | Zurich, Switzerland - Full-time |
| 65 | `a6421d3e-fdd0-48d6-8d8f-3fd605cdf09f` | Senior Autonomy Engineer - Deep Learning | San Mateo, California, United States - Full-time |
| 66 | `17b9ecf9-7a47-4811-b035-e1b9a54966aa` | Senior Business Operations Manager | San Mateo, California, United States - Full-time |
| 67 | `5d32766d-990a-4c4c-a8c6-5e934dd8bd38` | Senior Buyer | Hayward, California, United States - Full-time |
| 68 | `bb7a9c5c-8dbb-4a2f-9d7d-db9ab1f707b0` | Senior Customer Support Representative - India | Bangalore, India - Full-time |
| 69 | `7ef6359b-6454-4f91-871f-b33961585086` | Senior Director, Product Management, Drone as First Responder (DFR) | San Mateo, California, United States - Full-time |
| 70 | `3e7fb209-7973-4b5e-bf3e-b9a8a1f390eb` | Senior Engineering Manager, Infrastructure | San Mateo, California, United States - Full-time |
| 71 | `c0e49670-51ca-461c-b0e2-4a06df01f692` | Senior Hardware Test and Reliability Engineer | San Mateo, California, United States - Full-time |
| 72 | `9c3a9c61-4057-4df6-a1dc-9903d7fbc984` | Senior Manager, Training | US Remote - Full-time |
| 73 | `178a7e84-562e-40db-9abd-94bbf29159ca` | Senior NPI Product Quality Engineer | San Mateo, California, United States - Full-time |
| 74 | `8d67884d-58f4-41a7-8740-ab65d3c03fa8` | Senior Product Manager, Platform & Infrastructure | San Mateo, California, United States - Full-time |
| 75 | `05e9f029-3a9d-4956-a4c8-e0bc786dd86a` | Senior Revenue Operations Manager | San Mateo, California, United States - Full-time |
| 76 | `7bd047de-b65b-42b2-a2bf-7d33ceabd083` | Senior RF Design Engineer | San Mateo, California, United States - Full-time |
| 77 | `67a7d89f-9c4e-4f60-bdf1-a60b8addd8ae` | Senior Software Engineer - Embedded | San Mateo, California, United States - Full-time |
| 78 | `e8cb16b0-d2f0-4cb4-a1a1-0f43d195cc9a` | Senior Software Engineer - Mobile Platform | San Mateo, California, United States - Full-time |
| 79 | `bcd3d614-178c-4349-afd4-76476211b7fe` | Senior Software Engineer - Security | San Mateo, California, United States - Full-time |
| 80 | `aeaa130d-3e8b-42c5-a805-46f056e62fda` | Senior Software Engineer,  Data Platform | San Mateo, California, United States - Full-time |
| 81 | `0f71bdbb-a645-49f6-8890-dd5c052772c3` | Senior Software Engineer,  Infrastructure | San Mateo, California, United States - Full-time |
| 82 | `86cfc7bb-001c-4c1c-b680-160265535a96` | Senior Software Engineer, Frontend | San Mateo, California, United States - Full-time |
| 83 | `5655fbe3-66b0-4951-afdc-3b67f71e6938` | Senior Software Engineer, Full Stack | San Mateo, California, United States - Full-time |
| 84 | `16b0647d-a470-4917-9bb9-a95967828edc` | Senior Technical Recruiter | San Mateo, California, United States - Full-time |
| 85 | `737c02d2-f03f-4716-a0c8-e14a0307f8cb` | Senior Technical Recruiter - Hardware Operations | San Mateo, California, United States - Full-time |
| 86 | `f714e85f-31df-494e-bac4-1dd61d4d6066` | Senior Technical Support Representative - Japan | Tokyo, Japan - Full-time |
| 87 | `e49983b2-2323-48ea-bf1d-270f9f037457` | Senior Wireless Software Engineer, National Security | San Mateo, California, United States or Boston, Massachusetts, United States - Full-time |
| 88 | `f1ecf164-714c-4f1a-b672-d763f5724c03` | Senior Wireless Systems Performance Engineer | San Mateo, California, United States - Full-time |
| 89 | `71033170-d9d0-474b-b712-a11e4f11c146` | Senior/Staff Embedded Software Engineer – Camera Systems | San Mateo, California, United States - Full-time |
| 90 | `49da6783-223e-4b2c-81f6-3b47de1c52e7` | Software Engineer - Autonomy Infrastructure, Systems and Tools | Zurich, Switzerland - Full-time |
| 91 | `9e42a7af-6369-4036-ae6f-6626ee3a4fb3` | Software Engineer - Autonomy Infrastructure, Systems and Tools | San Mateo, California, United States - Full-time |
| 92 | `50dad059-b43b-4be1-84ab-2c350a68848f` | Software Engineer - Cloud Simulation & Full-Stack | Zurich, Switzerland - Full-time |
| 93 | `7d7dfadc-c6fd-4958-8d59-004a91bff55e` | Software Engineer - Cloud Simulation & Full-Stack | San Mateo, California, United States - Full-time |
| 94 | `ef9f7dd2-5a88-49b4-a507-d5fc9cad565a` | Software Engineer - Embedded | San Mateo, California, United States - Full-time |
| 95 | `cb958101-ede8-4f50-bf30-b3272d33f25f` | Software Engineer - Infrastructure | San Mateo, California, United States - Full-time |
| 96 | `3193c6ab-27d2-4558-8ad8-1d3a1512ab72` | Software Engineer - Simulation & Robotics Engineer | Zurich, Switzerland - Full-time |
| 97 | `7a8f3e6c-d576-41af-a81e-bf4fe20da12a` | Software Engineer - Simulation & Robotics Engineer | San Mateo, California, United States - Full-time |
| 98 | `f6320e9b-4eed-408d-8d37-d509fb0406ee` | Software Engineer Intern Fall 2026/Winter 2027 | San Mateo, California, United States - Intern |
| 99 | `067e1f47-9fba-4abf-b986-874d4d569706` | Software Engineer, Full Stack | San Mateo, California, United States - Full-time |
| 100 | `898a9c77-cc20-4ed6-a050-f68e5c15d5c8` | Sr/Staff Embedded Software Engineer - Camera Systems | Tampere, Finland - Full-time |
| 101 | `2ffe6453-4a2f-4dfb-94f8-882f731a11ae` | Staff Global Supply Manager,  Mechanicals | San Mateo, California, United States - Full-time |
| 102 | `dbd737b2-beed-4917-9948-dde4250929a8` | Staff Product Manager, Platform & Infrastructure | San Mateo, California, United States - Full-time |
| 103 | `b3b2dea9-63bb-4adb-ba29-69bd8f7a18eb` | Staff Software Engineer - Embedded | San Mateo, California, United States - Full-time |
| 104 | `417e884e-6760-41c6-ada4-db09dd7fd1c2` | Staff Software Engineer - Security | San Mateo, California, United States - Full-time |
| 105 | `54654035-a78a-4e5b-9ebf-ae4067e5a246` | Staff Software Engineer, Frontend | San Mateo, California, United States - Full-time |
| 106 | `379b23ea-14ff-4602-9b79-52d00bb96fda` | Staff Software Engineer, Full Stack | San Mateo, California, United States - Full-time |
| 107 | `c3a4256a-4525-443c-81d0-6f69e7c24805` | Staff Technical Recruiter | San Mateo, California, United States - Full-time |
| 108 | `4c4874bf-02da-4ccc-8918-2cca08feaf21` | Supplier Quality Engineer, Sustaining | Taiwan - Full-time |
| 109 | `2d21f482-3224-4906-a1bb-6a64436774cb` | Supply Chain Intern | San Mateo, California, United States - Intern |
| 110 | `a1a60b27-53a8-455e-b467-712e01c532dc` | Systems Integration and Test Engineer (Mid to Senior Level) | San Mateo, California, United States - Full-time |
| 111 | `c0c38168-badc-4dd7-96ed-99deb22149fc` | Wireless Software Engineer | San Mateo, California, United States - Full-time |
| 112 | `d023afe5-f19f-42f7-a1dd-aa94a361b86f` | Workplace Experience Coordinator Part-Time | Zurich, Switzerland - Part-time |

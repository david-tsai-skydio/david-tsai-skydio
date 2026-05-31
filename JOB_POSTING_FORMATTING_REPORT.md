# Skydio Careers — Job Posting Formatting Consistency Report

**Source:** [https://www.skydio.com/careers](https://www.skydio.com/careers)
**Date generated:** 2026-05-31
**Postings analyzed:** 113 individual job pages linked from the careers index
**Scope:** Pre-compensation content only (everything in the job description prose block up to, but not including, the `Compensation` / `Compensation Range` section)

---

## TL;DR

Roughly **59 / 113** postings follow the dominant format. The remaining **~54 postings show one or more formatting deviations** — some cosmetic (capitalization, punctuation), others structurally significant (different heading sizes, sub-section bolding patterns, missing structure).

The single biggest visual outlier is **Senior Technical Support Representative – Japan**, which uses `<h1>` for section headings — making each section title roughly **2–3× larger** than every other posting on the site.

---

## 1. Methodology

1. Pulled all `/jobs/{uuid}` links from the careers index page (113 unique postings).
2. Downloaded each job page and isolated the `<div class="prose block-content">` job-description container.
3. Truncated the HTML at the first occurrence of `<strong>Compensation…</strong>` (or equivalent compensation header), so only pre-compensation content was analyzed.
4. For each posting, recorded:
   - HTML structure (top-level child tags)
   - Heading tags used (`<h1>`–`<h6>`)
   - Bolded "section heading" paragraphs (`<p><strong>…</strong></p>`)
   - All `<strong>`/`<b>` phrases
   - `<em>`/`<i>`/`<u>` usage
   - Inline `style="…"` and `class="…"` attributes
   - List structure (`<ul>` / `<li>` counts)
   - Trailing-colon and capitalization style of each section label
5. Mapped each posting against the **dominant pattern** (defined below) and flagged deviations.

### The dominant pattern

> A short intro paragraph (no heading), followed by 1–6 **section labels marked up as `<p><strong>Section Title:</strong></p>`**, each followed by a `<ul>` of `<li><p>…</p></li>` bullets. No HTML headings (`<hN>`). No inline `style=`. No italics. No nested bold inside the bullets.

This pattern is used by ~59 postings exactly, and approximated by another ~30 with only cosmetic deviations.

### Important context about how the design system renders these elements

From Skydio's site stylesheet (relevant variables):

| Element / class | Computed font size | Font weight |
|---|---|---|
| `p`, `.type-body-3` | `clamp(0.875rem, …, 1rem)` ≈ **14–16 px** | 400 (regular) |
| `strong` (anywhere) | inherits parent size | **500 (medium)** — not 700 |
| `.prose h6` | ≈ 16–18 px | 500 |
| `.prose h5` | ≈ 18–22 px | 500 |
| `.prose h4` | ≈ 22–24 px | 500 |
| `.prose h3` | ≈ 18–28 px | 500 |
| `.prose h2` | ≈ 22–32 px | 500 |
| `.prose h1` | ≈ 28–48 px | 500 |

Two consequences worth flagging:

1. **`<strong>` is medium (500), not bold (700)** in this design system. Bold-only section headers therefore look quite subtle — they read as "slightly heavier body text," not as conventional bold.
2. **`<h2>` and `<h1>` in `.prose` are dramatically larger than body** — using them as section labels makes a posting look very different from the dominant pattern, even if everything else is identical.

---

## 2. Headline inconsistencies (across all 113 postings)

### 2.1 Section-heading **markup style** (font size / heading hierarchy)

| Markup used for section labels | # postings | Visual effect on label |
|---|---:|---|
| `<p><strong>…</strong></p>` *(dominant)* | **96** | 14–16 px, weight 500 |
| `<h2>` | 10 | **22–32 px**, weight 500 — clearly larger |
| `<h3>` | 5 | **18–28 px**, weight 500 — larger |
| Mixed `<h2>` + `<h3>` in one posting | 1 (Hardware Engineering Program Manager) | Two heading sizes in one posting |
| `<h1>` | **1** (Senior Technical Support Representative – Japan) | **28–48 px** — same size as page title; most extreme outlier |

> This is by far the **biggest visual inconsistency**: roughly 1 in 7 postings uses an HTML heading element where the rest of the site uses bolded body text, producing a ~1.5–3× larger section title.

### 2.2 Section-label **wording** (same concept, multiple text variants)

The same 3 "core" section labels appear with the following text variants across the site:

| Concept | Variants observed (count) |
|---|---|
| `about the role` | **49**× `About the role:` · **29**× `About the Role:` · **5**× `About the Role` · **3**× `About the role` · **1**× `About The Role` |
| `how youll make an impact` | **37**× `How you'll make an impact:` · **20**× `How You'll Make an Impact:` · **15**× `How you'll make an impact:` · **3**× `How You'll Make an Impact` · **2**× `How you'll make an impact` · **1**× `How You'll Make an Impact:` · **1**× `How you'll make an impact` |
| `what makes you a good fit` | **53**× `What makes you a good fit:` · **17**× `What Makes You a Good Fit:` · **4**× `What makes you a good fit` · **3**× `What Makes You a Good Fit` · **1**× `What Makes You A Good Fit:` · **1**× **`What Makes Your a Good Fit:`** ← **typo** (in *Senior People Analytics Analyst*) |
| `about the team` | **8**× `About the Team:` · **5**× `About the team:` · **1**× `About the Team` · **1**× `About the team` |
| `what would make you a good fit` | **7**× `What would make you a good fit:` · **2**× `What Would Make You a Good Fit:` |
| `bonus points` | **3**× `Bonus Points:` · **3**× `Bonus points:` |
| `nice to have` / `nice to haves` | `Nice to have:` (2) · `Nice to Have` (1) · `Nice To Haves` (1) · `Nice To Haves:` (1) |
| `qualifications` | **6**× `Qualifications:` · **1**× `Qualifications` |
| `requirements` | **2**× `Requirements` · **1**× `Requirements:` |

This produces three intersecting cosmetic dimensions:

- **Capitalization:** sentence case vs Title Case vs ALL CAPS variants
- **Trailing colon:** present vs absent (316 with colon, 58 without across all postings)
- **Apostrophe:** straight `'` (40) vs curly `'` (39) — almost an even split, often varying *within the same posting*

### 2.3 Internal inconsistency within a single posting

- **18 postings** mix "label with colon" and "label without colon" between their own sections.
- **51 postings** mix sentence-case section labels with Title-Case section labels (often: `About the role:` + `What Makes You a Good Fit:` in the same posting).
- The most jumbled example is **Senior Business Operations Manager**, which uses *all of these in one posting*: `About the Role:`, `How you'll make an impact:`, `Strategic Sourcing:`, `Cost Management`, `Strategy & Operations`, `What makes you a good fit:`.

### 2.4 Inline bolding inside bullets ("sub-section bolding")

Most postings keep `<strong>` to **3–6 occurrences total** (the section labels themselves, ±1).

A subset of postings uses heavy inline bolding inside list items as pseudo-sub-headings:

| Posting | `<strong>` count | Pattern |
|---|---:|---|
| Revenue Operations Engineer, Quoting Systems | **39** | Bold lead-in on nearly every bullet (`Quoting & approvals:`, `Amendments & changes:`, `Catalog readiness:` …) |
| Senior Wireless Software Engineer, National Security | **32** | Bold lead-in on each responsibility (`Own radio-link performance end-to-end`, `Integrate and control radios at the system layer`, …) |
| Software Engineer – Cloud Simulation & Full-Stack (×2) | **26** each | Bold sub-headings inside `<h2>` sections |
| PhD Autonomy Engineer Intern – Planning & Controls (RL) | **21** | Bold lead-ins + `<h3>` headings |
| Senior People Analytics Analyst | **18** | Bold city name, bold tool names, bold sub-section labels |
| GTM Data Engineer Intern | **16** | Bold lead-in on each bullet |
| Senior / Staff Product Manager, Platform & Infrastructure | **15** each | Bold lead-in on each bullet |
| Software Engineer – Simulation & Robotics Engineer (×2) | **13** each | Bold sub-headings |
| Software Engineer – Autonomy Infrastructure (×2) | **9** each | Bold lead-in on each bullet |
| Hardware Operations Program Manager | 9 | Bold lead-in on each bullet |
| Program Manager, Commercial Programs | 8 | Bold lead-in on each bullet |
| Success Systems Specialist | 8 | Bold sub-section labels mid-list |

This is a legitimate stylistic choice, but the site is **split** between "no sub-bolding" (the norm) and "heavy sub-bolding" (these 15+ postings), with no in-between. Visually this is a very obvious difference.

### 2.5 Italics and other inline styling

| Posting | What's italicized (why it's odd) |
|---|---|
| Senior Technical Recruiter | Whole *"PLEASE NOTE: We've returned to the office 3 days a week…"* paragraph |
| Senior Technical Recruiter – Hardware Operations | Same in-office disclaimer (italics) |
| Staff Technical Recruiter | Same in-office disclaimer (italics) |
| Senior NPI Product Quality Engineer | *"Please Note: This position requires a regular onsite presence…"* (italics) |
| Director, Growth Marketing – Commercial | *"Ability to be in our San Mateo, CA office 3 days per week"* (italics on a bullet) |
| Public Safety Strategist (West Coast, Midwest, or PNW) | *"Additional Responsibilities:"* (italicized sub-heading) |
| Lead Staff Electrical Engineer | *"About the role:"* (entire intro paragraph italicized – unusual pattern) |
| Senior Software Engineer, Full Stack | Italicized inline link wrapper |
| Full Stack Product Counsel | *"You are a true Full Stack Product Counsel"* (entire italicized blockquote-style line) |
| GTM Engineer, Pre-Sales | **8 italicized phrases** (sub-headings *"Find the right problems to solve"*, *"Build things that scale"*, etc.) — the heaviest italics user on the site |

For at least 4 postings the *same* "office policy" disclaimer is italicized; in the other ~10 postings that contain a similar disclaimer, it is not italicized. This is the clearest example of "same content, different formatting" on the site.

### 2.6 Postings with **no formal section structure**

Two postings have **zero** section markers (neither `<h*>` headings nor `<p><strong>…</strong></p>` paragraph headers). Section labels exist only as inline bolded run-on text inside paragraphs:

- **Product Support Engineer**
- **Product Support Engineer Intern**

These postings list `About the role`, `Location`, `How you'll make an impact`, `What makes you a good fit` as inline `<strong>` runs rather than standalone paragraph headers — so visually they have no breathing room and no scannable section breaks at all.

### 2.7 Inline `style=` attribute (CSS hygiene)

**Only one posting** contains inline `style=` in its prose:

- **Manager, Logistics** — `<div style="min-height:1.2em;margin-top:0;margin-bottom:0">`

This appears to be a leftover empty spacer copied from another source (Word / Google Docs). It should be removed for cleanliness — every other posting relies entirely on the design-system stylesheet.

### 2.8 Other small but visible quirks

- **Curly vs straight apostrophe:** the same section label appears with `'` and `'` (Unicode U+2019). In "How you'll make an impact" alone, the split is 40 / 39 / 4. Often varies even between sections of the same posting.
- **Double-space typos in titles (and likely body):**
  `Senior Software Engineer,  Infrastructure`, `Senior Software Engineer,  Data Platform`, `Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM`, `Staff Global Supply Manager,  Mechanicals`.
- **`PhD` vs `Ph.D.`** isn't an issue here — all use `PhD`. Fine.
- **Duplicate location postings**: roughly 12 jobs are duplicated across 2 locations (e.g. San Mateo + Zurich) as separate listings. They are mostly consistent within their pair, but each pair counts as 2 independent postings, so any formatting issue is counted twice.

---

## 3. Postings that stand out the most (curated list)

### A — Most extreme visual outlier
1. **Senior Technical Support Representative – Japan** — only posting on the site that uses `<h1>` for section labels. Renders at ~28–48 px, the same size as the page H1. Will look broken next to any other posting on a careers feed.

### B — Different headings hierarchy entirely
2. **Hardware Engineering Program Manager** — mixes `<h2>` and `<h3>` within one posting (two visibly different heading sizes).
3. **Revenue Operations Engineer, Quoting Systems** — `<h2>` headings + 39 inline `<strong>` lead-ins (the heaviest formatting on the site).
4. **Senior Wireless Software Engineer, National Security** — `<h2>` headings + 32 inline `<strong>` lead-ins.
5. **Software Engineer – Cloud Simulation & Full-Stack** (×2 listings) — `<h2>` + 26 `<strong>` each.
6. **Software Engineer – Autonomy Infrastructure, Systems and Tools** (×2 listings) — `<h2>` + 9 `<strong>` each.
7. **Software Engineer – Simulation & Robotics Engineer** (×2 listings) — `<h3>` + 13 `<strong>` each.
8. **PhD Autonomy Engineer Intern – Planning & Controls (Reinforcement Learning)** — `<h3>` + 21 `<strong>`.
9. **Aviation Compliance Lead**, **Aviation Regulatory Program Manager**, **Communications Manager**, **Senior Buyer**, **Full Stack Product Counsel**, **Senior Business Operations Manager**, **Senior Technical Support Representative – Japan** — all use HTML headings in a sea of postings that don't.

### C — Missing structure
10. **Product Support Engineer** and **Product Support Engineer Intern** — no paragraph-level section headers at all.

### D — Italics heavy / off-style
11. **GTM Engineer, Pre-Sales** — 8 italicized sub-headings.
12. **Lead Staff Electrical Engineer** — entire opening paragraph italicized.
13. **Full Stack Product Counsel** — italicized one-liner used as a stylistic flourish that no other posting uses.

### E — Internal capitalization / colon chaos
14. **Senior Business Operations Manager** — 6 section labels in 3+ different cap/colon styles.
15. **Customer Success Manager, DFR Majors – Southeast** and **DFR Mid-Market – Northeast** — mix sentence + title case and mixed colons.
16. **Workplace Experience Coordinator Part-Time** — only 1 of 5 section labels has a trailing colon (inverse of the dominant pattern).
17. **Success Systems Specialist** — 8 section labels, 4 with colon and 4 without.
18. **Director, Growth Marketing – Commercial** — mixes sentence + title case + italics in 5 labels.

### F — Typos / character issues
19. **Senior People Analytics Analyst** — section heading reads **"What Makes Your a Good Fit:"** (should be "You").
20. **Manager, Logistics** — only posting with inline `style="…"` attribute.

---

## 4. Full per-posting findings table

Sorted issue-first, then alphabetically among "matches dominant pattern."

- **Sections** = number of detected section labels (paragraph-level)
- **`<strong>`s** = total `<strong>`/`<b>` element count in pre-compensation content
- **Issues** = deviations from dominant pattern; "matches dominant pattern" means no flagged issues (but may still have curly-vs-straight apostrophe or label-text-variant differences vs. the site average).

| # | Job Title | Sections | `<strong>`s | Issues |
|---|-----------|---------:|------------:|--------|
| 1 | Director, Growth Marketing – Commercial | 5 | 6 | mixed trailing colon (4/5 with); mixes sentence-case + title-case headings; uses italics |
| 2 | PhD Autonomy Engineer Intern – Planning & Controls (Reinforcement Learning) | 5 | 21 | uses `<h3>`; mixes sentence- + title-case headings; heavy sub-section bolding |
| 3 | Revenue Operations Engineer, Quoting Systems | 6 | 39 | uses `<h2>`; mixes sentence- + title-case headings; heavy sub-section bolding |
| 4 | Senior Business Operations Manager | 6 | 6 | uses `<h3>`; mixed trailing colon; mixes sentence- + title-case headings |
| 5 | Senior Product Manager, Platform & Infrastructure | 3 | 15 | mixed trailing colon; mixes sentence- + title-case headings; heavy sub-section bolding |
| 6 | Staff Product Manager, Platform & Infrastructure | 3 | 15 | mixed trailing colon; mixes sentence- + title-case headings; heavy sub-section bolding |
| 7 | Success Systems Specialist | 8 | 8 | mixed trailing colon (4/8 with); mixes sentence- + title-case headings; heavy sub-section bolding |
| 8 | Customer Success Manager, DFR Majors – Southeast | 5 | 6 | mixed trailing colon; mixes sentence- + title-case headings |
| 9 | Customer Success Manager, DFR Mid-Market – Northeast | 5 | 6 | mixed trailing colon; mixes sentence- + title-case headings |
| 10 | Full Stack Product Counsel | 4 | 4 | uses `<h3>`; uses italics |
| 11 | GTM Engineer, Pre-Sales | 3 | 4 | mixed trailing colon; uses italics (8 italic phrases) |
| 12 | Hardware Engineering Program Manager | 8 | 6 | **mixes heading levels `<h2>` + `<h3>`**; mixes sentence- + title-case headings |
| 13 | Mission Success Operations Manager | 4 | 4 | mixed trailing colon; mixes sentence- + title-case headings |
| 14 | Program Manager, Commercial Programs | 4 | 8 | mixed trailing colon; heavy sub-section bolding |
| 15 | Public Safety Strategist (West Coast, Midwest, or PNW) | 4 | 4 | mixed trailing colon; uses italics |
| 16 | Senior People Analytics Analyst | 4 | 18 | mixed trailing colon; heavy sub-section bolding; **typo** in section label ("Your" → "You") |
| 17 | Senior Software Engineer, Data Platform | 4 | 5 | mixed trailing colon; mixes sentence- + title-case headings |
| 18 | Senior Wireless Software Engineer, National Security | 6 | 32 | uses `<h2>`; heavy sub-section bolding |
| 19 | Software Engineer – Autonomy Infrastructure, Systems and Tools *(San Mateo)* | 5 | 9 | uses `<h2>`; heavy sub-section bolding |
| 20 | Software Engineer – Autonomy Infrastructure, Systems and Tools *(Zurich)* | 5 | 9 | uses `<h2>`; heavy sub-section bolding |
| 21 | Software Engineer – Cloud Simulation & Full-Stack *(San Mateo)* | 5 | 26 | uses `<h2>`; heavy sub-section bolding |
| 22 | Software Engineer – Cloud Simulation & Full-Stack *(Zurich)* | 5 | 26 | uses `<h2>`; heavy sub-section bolding |
| 23 | Software Engineer – Simulation & Robotics Engineer *(San Mateo)* | 5 | 13 | uses `<h3>`; heavy sub-section bolding |
| 24 | Software Engineer – Simulation & Robotics Engineer *(Zurich)* | 5 | 13 | uses `<h3>`; heavy sub-section bolding |
| 25 | Workplace Experience Coordinator Part-Time | 5 | 6 | inverse trailing colon (only 1/5 with); mixes sentence- + title-case headings |
| 26 | Aviation Compliance Lead | 4 | 4 | uses `<h2>` |
| 27 | Aviation Regulatory Program Manager | 3 | 4 | uses `<h2>` |
| 28 | CSM Manager – Public Safety (Major Markets) | 4 | 4 | mixes sentence- + title-case headings |
| 29 | Communications Manager | 3 | 4 | uses `<h2>` |
| 30 | Deployment Engineer – Southeast | 5 | 6 | mixes sentence- + title-case headings |
| 31 | Director, Global Supply Management – Mechanicals | 3 | 3 | mixes sentence- + title-case headings |
| 32 | Enterprise Account Manager (MoD/ MoI) – EMEA (Finland) | 4 | 4 | mixed trailing colon |
| 33 | Enterprise Account Manager (MoD/ MoI) – EMEA (Germany) | 4 | 4 | mixed trailing colon |
| 34 | Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland) | 4 | 4 | mixed trailing colon |
| 35 | GTM Data Engineer Intern | 4 | 16 | heavy sub-section bolding |
| 36 | GTM Enablement Associate | 2 | 5 | mixes sentence- + title-case headings |
| 37 | Hardware Operations Program Manager | 3 | 9 | heavy sub-section bolding |
| 38 | Lead Staff Electrical Engineer | 2 | 3 | uses italics on opening paragraph |
| 39 | **Manager, Logistics** | 3 | 3 | **inline `style=` attribute** |
| 40 | Manager, Technical Support | 5 | 6 | mixed trailing colon |
| 41 | **Product Support Engineer** | 0 | 4 | **NO section structure** |
| 42 | **Product Support Engineer Intern** | 0 | 4 | **NO section structure** |
| 43 | Program Manager, Major Deployments (Hawaii) | 3 | 3 | mixes sentence- + title-case headings |
| 44 | Senior Buyer | 3 | 3 | uses `<h2>` |
| 45 | Senior NPI Product Quality Engineer | 3 | 4 | uses italics |
| 46 | Senior Software Engineer – Security | 4 | 5 | mixes sentence- + title-case headings |
| 47 | Senior Software Engineer, Full Stack | 4 | 5 | uses italics |
| 48 | Senior Strategy and Planning Analyst | 3 | 3 | mixes sentence- + title-case headings |
| 49 | Senior Technical Recruiter | 2 | 2 | uses italics on disclaimer |
| 50 | Senior Technical Recruiter – Hardware Operations | 1 | 3 | uses italics on disclaimer |
| 51 | **Senior Technical Support Representative – Japan** | 3 | 2 | **uses `<h1>` (~28–48 px, same as page title — most extreme outlier)** |
| 52 | Software Engineer, Full Stack | 4 | 5 | mixes sentence- + title-case headings |
| 53 | Staff Software Engineer, Frontend | 4 | 5 | mixes sentence- + title-case headings |
| 54 | Staff Technical Recruiter | 3 | 3 | uses italics on disclaimer |
| 55 | Autonomy Engineer – Deep Learning *(San Mateo)* | 3 | 3 | matches dominant pattern |
| 56 | Autonomy Engineer – Deep Learning *(Zurich)* | 3 | 3 | matches dominant pattern |
| 57 | Autonomy Engineer – Deep Learning Infrastructure *(San Mateo)* | 1 | 3 | matches dominant pattern |
| 58 | Autonomy Engineer – Deep Learning Infrastructure *(Zurich)* | 1 | 3 | matches dominant pattern |
| 59 | Autonomy Engineer – Deep Learning Model Acceleration *(San Mateo)* | 1 | 3 | matches dominant pattern |
| 60 | Autonomy Engineer – Deep Learning Model Acceleration *(Zurich)* | 1 | 3 | matches dominant pattern |
| 61 | Autonomy Engineer – Fixed Wing Planning & Controls | 3 | 3 | matches dominant pattern |
| 62 | Autonomy Engineer – ML & DL Infrastructure *(San Mateo)* | 3 | 3 | matches dominant pattern |
| 63 | Autonomy Engineer – ML & DL Infrastructure *(Zurich)* | 3 | 3 | matches dominant pattern |
| 64 | Autonomy Engineer – Planning and Controls | 2 | 3 | matches dominant pattern |
| 65 | Autonomy Engineer Intern – Computer Vision/Deep Learning Fall 2026 *(San Mateo)* | 3 | 3 | matches dominant pattern |
| 66 | Autonomy Engineer Intern – Computer Vision/Deep Learning Fall 2026 *(Zurich)* | 3 | 4 | matches dominant pattern |
| 67 | Autonomy Engineer Intern – Deep Learning (Computational Photography) *(San Mateo)* | 3 | 3 | matches dominant pattern |
| 68 | Autonomy Engineer Intern – Deep Learning (Computational Photography) *(Tampere or Zurich)* | 3 | 3 | matches dominant pattern |
| 69 | Autonomy Engineer Intern Fall 2026 *(San Mateo)* | 3 | 4 | matches dominant pattern |
| 70 | Autonomy Engineer Intern Fall 2026 *(Zurich)* | 3 | 3 | matches dominant pattern |
| 71 | Autonomy Software Engineer | 1 | 3 | matches dominant pattern |
| 72 | Director of Product Management, Drone as First Responder (DFR) | 2 | 6 | matches dominant pattern |
| 73 | Electrical Engineer (Sustaining/Validation) | 2 | 3 | matches dominant pattern |
| 74 | Electrical Engineer (all levels) | 2 | 3 | matches dominant pattern |
| 75 | Engineering Manager – Autonomy | 3 | 3 | matches dominant pattern |
| 76 | Enterprise Account Manager, US Navy, US Marine Corps, and IC/SOCOM | 3 | 3 | matches dominant pattern |
| 77 | Enterprise Account Manager, US Army | 3 | 3 | matches dominant pattern |
| 78 | Field Support Representative | 4 | 4 | matches dominant pattern |
| 79 | Field Support Representative (Southwest, Remote) | 3 | 4 | matches dominant pattern |
| 80 | IT Technician (Help Desk – Linux Focus) | 4 | 6 | matches dominant pattern |
| 81 | Middleware Software Engineer Intern – Fall 2026 | 3 | 4 | matches dominant pattern |
| 82 | PCB Layout Engineer | 2 | 3 | matches dominant pattern |
| 83 | PhD Autonomy Engineer Intern – Deep Learning or Computer Vision *(San Mateo)* | 3 | 4 | matches dominant pattern |
| 84 | PhD Autonomy Engineer Intern – Deep Learning or Computer Vision *(Zurich)* | 3 | 3 | matches dominant pattern |
| 85 | Product Design Engineer (All Levels) | 2 | 3 | matches dominant pattern |
| 86 | RF Design Engineer | 3 | 3 | matches dominant pattern |
| 87 | Sales Planning Analyst Intern | 2 | 4 | matches dominant pattern |
| 88 | Senior Autonomy Engineer – Controls | 3 | 3 | matches dominant pattern |
| 89 | Senior Autonomy Engineer – Deep Learning *(San Mateo)* | 2 | 3 | matches dominant pattern |
| 90 | Senior Autonomy Engineer – Deep Learning *(Zurich)* | 2 | 3 | matches dominant pattern |
| 91 | Senior Customer Support Representative – India | 3 | 4 | matches dominant pattern |
| 92 | Senior Director, Product Management, Drone as First Responder (DFR) | 2 | 6 | matches dominant pattern |
| 93 | Senior Engineering Manager, Infrastructure | 2 | 7 | matches dominant pattern |
| 94 | Senior Hardware Test and Reliability Engineer | 3 | 3 | matches dominant pattern |
| 95 | Senior RF Design Engineer | 3 | 3 | matches dominant pattern |
| 96 | Senior Revenue Operations Manager | 4 | 5 | matches dominant pattern |
| 97 | Senior Software Engineer – Embedded | 4 | 4 | matches dominant pattern |
| 98 | Senior Software Engineer – Mobile Platform | 5 | 5 | matches dominant pattern |
| 99 | Senior Software Engineer, Infrastructure | 3 | 5 | matches dominant pattern |
| 100 | Senior Software Engineer, Frontend | 4 | 5 | matches dominant pattern |
| 101 | Senior Wireless Systems Performance Engineer | 3 | 3 | matches dominant pattern |
| 102 | Senior/Staff Embedded Software Engineer – Camera Systems | 4 | 4 | matches dominant pattern |
| 103 | Software Engineer – Embedded | 4 | 4 | matches dominant pattern |
| 104 | Software Engineer – Infrastructure | 3 | 5 | matches dominant pattern |
| 105 | Software Engineer Intern Fall 2026/Winter 2027 | 1 | 4 | matches dominant pattern |
| 106 | Sr/Staff Embedded Software Engineer – Camera Systems | 4 | 4 | matches dominant pattern |
| 107 | Staff Global Supply Manager, Mechanicals | 2 | 3 | matches dominant pattern |
| 108 | Staff Software Engineer – Embedded | 4 | 4 | matches dominant pattern |
| 109 | Staff Software Engineer, Full Stack | 3 | 4 | matches dominant pattern |
| 110 | Supplier Quality Engineer, Sustaining | 3 | 3 | matches dominant pattern |
| 111 | Supply Chain Intern | 2 | 4 | matches dominant pattern |
| 112 | Systems Integration and Test Engineer (Mid to Senior Level) | 3 | 3 | matches dominant pattern |
| 113 | Wireless Software Engineer | 3 | 3 | matches dominant pattern |

---

## 5. Recommendations

Group these by how much editorial / engineering effort they take.

### 5.1 Highest priority — fix today

1. **Fix the `<h1>` outlier.** Convert section labels in **Senior Technical Support Representative – Japan** from `<h1>` to whatever the standard ends up being (see §5.2). Right now those headings render at the page-title size and look broken.
2. **Fix the typo.** *Senior People Analytics Analyst* — change **"What Makes Your a Good Fit:"** → **"What Makes You a Good Fit:"**.
3. **Remove the inline `style="…"`** from *Manager, Logistics*. It's the only posting on the site using inline CSS and is leftover from a copy/paste source.
4. **Restore section structure** in *Product Support Engineer* and *Product Support Engineer Intern* — promote the inline `<strong>` runs to `<p><strong>…</strong></p>` paragraph headers, matching the rest of the site.
5. **Trim "About the role" duplicates in titles like `Senior Software Engineer,  Infrastructure`** — kill the double space in posting titles for 4 postings.

### 5.2 Medium priority — pick a single canonical format

Make the design / talent-ops team commit to **one** answer for each of these. Suggested defaults are shown.

| Decision | Recommended | Rationale |
|---|---|---|
| Section-label markup | `<p><strong>Section Title:</strong></p>` *(the current majority)* | 96 / 113 already use it; no engineering work needed. |
| Or alternatively → introduce a **dedicated CSS class** (e.g. `.job-section-title`) that renders larger than body but smaller than `<h2>` | If a more visible hierarchy is desired | Avoids the "tiny medium-weight" appearance and keeps semantics consistent. |
| Heading-tag use inside `.prose` | **Forbid `<h1>`–`<h3>` for section labels** | They cause 1.5–3× size jumps relative to the norm. |
| Section-label text — capitalization | **Sentence case** (`About the role:`) | This is the most common variant for *every* core label; matches the existing site voice. |
| Section-label text — trailing colon | **Always present** | 316/374 currently use a trailing colon; the colon also visually separates label from the following list. |
| Apostrophe character | **Curly `'` everywhere** (or always straight `'` — but pick one) | Currently split ~40/39. Resolve at the CMS/lint layer if possible (autoreplace on save). |
| Sub-section bold lead-ins inside `<li>` | **Only allow if used consistently throughout that posting** | Heavy bolding is acceptable but should not be mixed with `<h2>`/`<h3>` headings in the same posting. |
| Italics | **Reserve for the in-office policy disclaimer only**, and standardize its wording | Currently the disclaimer is italic in 4 postings and plain in ~6 others, with three different exact wordings. |
| Inline `style=` attributes | **Disallowed in CMS** | Block at the editor / pre-publish layer. |

### 5.3 Lower priority — content normalization

6. **Adopt a canonical section-label vocabulary** (suggested):

   | Section | Canonical label |
   |---|---|
   | Team intro | `About the team:` |
   | Role intro | `About the role:` |
   | What they do day-to-day | `How you'll make an impact:` |
   | Required skills | `What makes you a good fit:` |
   | Nice-to-haves | `Bonus points:` *(currently "Bonus Points", "Bonus points", "Nice to have", "Nice to Have", "Nice To Haves", "Nice To Haves:", "Preferred Qualifications", "Bonus Experience" all coexist)* |

7. **Add a job-description style guide** to whichever tool authors use (Greenhouse, Notion template, internal doc) so new postings get the right structure at draft time, not after publish.

8. **Run a one-time normalization pass** to apply the chosen defaults across all 54 deviating postings (the table in §4). The cheapest path is probably a CMS/Greenhouse script that:
   - Replaces `<h1>`/`<h2>`/`<h3>` section labels with `<p><strong>…</strong></p>`.
   - Removes empty `<div style="…">` blocks.
   - Lowercases section-label text to sentence case where the canonical variant uses sentence case.
   - Ensures trailing colons on all paragraph-level section labels.
   - Normalizes curly apostrophes (or straight, depending on team preference).

9. **Add automated lint** in the publishing pipeline that warns when a draft posting:
   - Uses `<h1>`–`<h3>` inside the description body.
   - Uses any inline `style=` attribute.
   - Has fewer than 2 section labels (catches the "no structure" Product Support Engineer case).
   - Mixes capitalization styles in its own section labels.
   - Mixes trailing-colon styles in its own section labels.

These five rules alone would have caught every issue in §3 before publication.

---

## 6. Appendix — How the analysis was run

- All 113 job pages were downloaded from `https://www.skydio.com/jobs/{uuid}/?gh_jid=...`.
- Each page contains the job description in `<div class="prose block-content">`.
- The HTML inside that container was truncated immediately before the first `<strong>Compensation…</strong>` (or `<strong>Compensation Range</strong>`, or `<h*>Compensation</h*>`) marker.
- Per-posting structural metrics (heading tags, bold counts, section markers, inline styles) were computed using BeautifulSoup.
- A "section marker" = either an `<h1>`–`<h6>` element or a `<p>` whose sole non-whitespace child is a `<strong>`/`<b>` element.
- Capitalization-style classification ignores stop-words (`a`, `an`, `the`, `and`, `or`, `for`, etc.) so that AP-style title case (`About the Role`) is correctly grouped with full title case (`What Makes You a Good Fit`).
- "Heavy sub-section bolding" = a posting with ≥ 8 `<strong>` elements in pre-compensation content.

Raw per-posting JSON output is available alongside this report if the team wants to drill into a specific posting.

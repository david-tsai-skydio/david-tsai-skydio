# Skydio Careers — Job Posting Formatting Audit

**Source:** https://www.skydio.com/careers
**Date captured:** 2026-06-08
**Scope:** All **120** live job postings, body content **up to (and not including) the `Compensation:` block** (i.e. the role description, "How you'll make an impact" / responsibilities, and "What makes you a good fit" / qualifications sections).
**Method:** Each posting page was fetched and the HTML inside `<div class="prose block-content">…</div>` was parsed and split at the first `<strong>Compensation:</strong>` marker. Structural, class, and inline-styling attributes were then compared across the corpus.

---

## 1. Executive summary

The Skydio careers site renders every posting through one Astro/Ashby template, so the *outer chrome* (page title, location subline, body font, background, line-height) is identical across all 120 jobs. The visible inconsistencies all come from **content authored in the Ashby CMS** and fall into seven recurring patterns:

| # | Issue | Postings affected | Severity |
|---|---|---:|---|
| 1 | Section headings rendered as `<h2>`/`<h3>` (≈ **24 px / 20 px**) instead of the standard bold paragraph (**16 px**) | **18 / 120** | High |
| 2 | "Run-on" headings (bold label glued to body copy with no paragraph break, producing a 200–2,000-char "heading") | **28 / 120** | High |
| 3 | Heading text varies in **casing**, **punctuation**, and **apostrophe style** for the same three logical sections | **~95 / 120** | Medium |
| 4 | Section headings missing the trailing colon | **21 / 120** (39 individual headings) | Medium |
| 5 | Underline `<u>` used for emphasis (visually competes with hyperlinks) | **9 / 120** | Medium |
| 6 | Inline CSS `style="…"` carried in from a pasted source | **2 / 120** | Low |
| 7 | Posting omits the "Compensation:" block entirely | **30 / 120** | Out of scope (flagged for context) |

The base template itself is **visually consistent** — same `type-h2` for the role title and same `type-body-2` for the location subline on every page. All deviations are CMS-content artifacts, which means they can be fixed without code changes by editing the source markdown in Ashby.

---

## 2. Baseline template (the "norm")

The 80-odd well-formatted postings share this exact structure:

```html
<h1 class="type-h2">{Role title}</h1>
<p class="type-body-2">{City, Country} - {Employment type}</p>

<div class="prose block-content">
  <p>Skydio is the leading US drone company …  [boilerplate intro, identical on every page]</p>
  <p><strong>About the role:</strong></p>
  <p>{1-3 paragraphs of narrative}</p>
  <p><strong>How you'll make an impact:</strong></p>
  <ul><li><p>Bullet</p></li> … </ul>
  <p><strong>What makes you a good fit:</strong></p>
  <ul><li><p>Bullet</p></li> … </ul>
  <p><strong>Compensation:</strong> …</p>
  …
</div>
```

Visual properties (from `prose` + design-system tokens):

- **Body text:** 16 px, regular weight, ~1.6 line-height, dark-grey on white.
- **Section heading:** the same 16 px body run rendered **bold** (no size change, no margin change beyond the standard `<p>` margin).
- **Role title (`<h1 class="type-h2">`):** the design system's `type-h2` token — substantially larger than body (≈ 32 px on desktop), regular tracking.
- **Location subline (`<p class="type-body-2">`):** the design system's `type-body-2` token — small/muted.
- **Bullets:** `<ul><li><p>…</p></li></ul>` — every posting uses this exact pattern (118/120; the remaining 2 have no list at all).

`<h1 class>`, `<p class>`, and the bullet pattern were **100 % consistent** across the 120 postings. Every formatting issue below lives **inside** the `prose` body.

---

## 3. Inconsistencies — detailed findings

### 3.1 Mixed heading "weights" (`<h2>`/`<h3>` vs `<p><strong>`) — **High severity**

102 postings use `<p><strong>About the role:</strong></p>` (renders at body size, **16 px bold**). **18 postings** render the same labels as real `<h2>` or `<h3>` headings, which inherit the Tailwind/`prose` typography scale and visually pop out at roughly **24 px / 20 px**. On the same job board, "About the Role:" appears in three different sizes depending on which posting you open.

**Affected postings (count of heading-tagged sections per posting):**

| Posting | Heading tag(s) used | Count |
|---|---|---:|
| Aviation Compliance Lead | h2 | 4 |
| Communications Manager | h2 | 3 |
| Engineering Program Manager | h2, h3 | 8 |
| Full Stack Product Counsel | h3 | 4 |
| GTM Engineer, Pre-Sales | h2, h3 | 11 |
| Logistics Operations Specialist, HQ | h2, h3 | 6 |
| PhD Autonomy Engineer Intern – Planning & Controls (RL) | h3 | 3 |
| Revenue Operations Analyst, CPQ | h2 | 5 |
| Senior Business Operations Manager | h3 | 3 |
| Senior Buyer | h2 | 2 |
| Senior Technical Support Representative – Japan | **h1** | 3 |
| Senior Wireless Software Engineer, National Security | h2 | 6 |
| Software Engineer – Autonomy Infrastructure, Systems and Tools (×2 listings) | h2 | 5 each |
| Software Engineer – Cloud Simulation & Full-Stack (×2 listings) | h2 | 5 each |
| Software Engineer – Simulation & Robotics Engineer (×2 listings) | h3 | 5 each |

The **Senior Technical Support Representative – Japan** posting is the worst offender: it uses **`<h1>`** for its section headings, which renders larger than the role title itself, breaking the heading hierarchy (the page now has two competing top-level headings).

### 3.2 Run-on / merged headings — **High severity**

The label and the first paragraph of the section were pasted as one block, producing a single "bold" run that is actually 200–2,000 characters long. Visually this renders as a giant bold paragraph that swallows the rest of the section.

**28 postings affected.** Worst examples:

| Posting | Length of run-on "heading" | First ~120 chars |
|---|---:|---|
| Staff Product Manager, Platform & Infrastructure | **2,064 chars** | `Customer & sales engagement: Run discovery with government and commercial customers…` |
| Senior Product Manager, Platform & Infrastructure | **2,064 chars** | (same as above) |
| PhD Autonomy Engineer Intern – Planning & Controls (RL) | **1,892 chars** | `Navigation & avoidance in the wild: Train policies that adapt online to cluttered 3D scenes…` |
| Software Engineer Intern Fall 2026/Winter 2027 | **1,607 chars** | `About the role:With best-in-class autonomy and real-time cloud connectivity…` |
| Senior Engineering Manager, Infrastructure | **1,534 chars** | `About the role: Skydio is building a secure, globally distributed drone platform…` |
| Field Service Technician | **1,513 chars** | `About the role:A Skydio Field Service Technician (FST) is responsible for…` |
| Senior Wireless Software Engineer, National Security | **1,381 chars** | `About the Role:We deliver life-saving information as fast as possible…` |
| Hardware Operations Program Manager | **1,264 chars** | `Collaborate cross-functionally with product, engineering, reliability…` |
| Revenue Operations Analyst, CPQ | **1,115 chars** | `Quoting & approvals: Own the end-to-end quoting experience…` |
| Senior Software Engineer, Infrastructure | **1,019 chars** | `About the team: Skydio's Cloud infrastructure team is here to ensure…` |
| Software Engineer – Infrastructure | **1,007 chars** | (duplicate of above) |
| Senior Technical Recruiter – Hardware Operations | **992 chars** | `About the role:We are seeking a proven Senior Technical Recruiter…` |
| Senior Director, Product Management, DFR | **917 chars** | `About the role: As the Senior Director of Product Management for Skydio's DFR…` |
| Director of Product Management, DFR | **910 chars** | (very similar to above) |
| Autonomy Engineer – Deep Learning Infrastructure (×2) | **831/831 chars** | `About the role:Learning a semantic and geometric understanding of the world…` |
| Autonomy Engineer – Deep Learning Model Acceleration (×2) | **835/831 chars** | (same boilerplate) |
| GTM Enablement Associate | 728 chars | `About the role:We're looking for a GTM Enablement Associate…` |
| Senior Autonomy Engineer – Deep Learning (×2) | 528–529 chars | `About the role:Learning a semantic…` |
| Autonomy Software Engineer | 580 chars | `About the role:As an Autonomy Engineer, your primary goal…` |
| Workplace Experience Coordinator Part-Time | 557 chars | `About the RoleWe are looking for a proactive and detail-oriented…` |
| Product Design Engineer (All Levels) | 410 chars | `About the role:Skydio's mechanical systems are the backbone…` |
| Lead Staff Electrical Engineer | 393 chars | `About the role: We are looking for a Lead Electrical Engineer…` |
| Field Support Representative – New York | 393 chars | `Location: New York — Hudson Valley / Greater NYC Region Preferred…` |
| Manager, Technical Support | 220 chars | `Location: This is an office or remote-based position…` |
| Deployment Engineer – Southeast | 214 chars | `Location Preference: Candidates must be based in the Southeast…` |

Many of these are obvious copy-paste artifacts (note the duplicated Deep-Learning boilerplate appearing identically across 4–6 postings).

### 3.3 Heading text variation — **Medium severity**

The same three logical sections are written **17 different ways**.

**"About the role"** — 4 variants observed:

| Count | Variant |
|---:|---|
| 51 | `About the role:` *(canonical, most common)* |
| 33 | `About the Role:` |
| 5 | `About the Role` *(no colon)* |
| 3 | `About the role` *(no colon)* |

Plus **15** postings using `About the team:` and **2** postings using `About the team` (no colon).

**"How you'll make an impact"** — 7 variants, including a curly-vs-straight apostrophe split:

| Count | Variant |
|---:|---|
| 32 | `How you'll make an impact:` *(canonical)* |
| 19 | `How You'll Make an Impact:` *(curly apostrophe)* |
| 12 | `How you'll make an impact:` *(curly apostrophe)* |
| 3 | `How You'll Make an Impact` *(no colon, curly)* |
| 2 | `How you'll make an impact` *(no colon, straight)* |
| 1 | `How You'll Make an Impact:` *(Title case, straight)* |
| 1 | `How you'll make an impact` *(curly, no colon)* |
| 4 | `How you will make an impact:` *(separate phrasing)* |

Apostrophe split overall: **49 straight (`'`)** vs **44 curly (`'`)**.

**"What makes you a good fit"** — 5 variants for the same heading, plus 3 sibling variants:

| Count | Variant |
|---:|---|
| 52 | `What makes you a good fit:` *(canonical)* |
| 21 | `What Makes You a Good Fit:` |
| 5 | `What makes you a good fit` *(no colon)* |
| 2 | `What Makes You a Good Fit` *(no colon)* |
| 1 | `What Makes You A Good Fit:` *(all-Title-Case)* |
| 8 | `What would make you a good fit:` |
| 6 | `What makes you a strong fit:` |
| 1 | `What makes you a great fit:` |

A handful of postings use a **completely different framework** ("Areas of Responsibility:" / "What You'll Do:" / "Qualifications:" / "Bonus Experience:") instead of the Skydio-standard trio — see §3.5.

### 3.4 Headings missing the trailing colon — **Medium severity**

In the canonical template every bold section heading ends in `:`. **21 postings** have at least one heading without the colon (39 total occurrences). Highlights:

- **Communications Manager** — *all three* headings lack the colon: `About the role`, `How you'll make an impact`, `What makes you a good fit`.
- **Aviation Compliance Lead** — all three section headings lack the colon (and are rendered as `<h2>` — see §3.1).
- **Full Stack Product Counsel** — `About the Team`, `About the Role`, `How You'll Make an Impact`, `What Makes You a Great Fit` — all without colons (and `<h3>`-tagged).
- **IT Technician (Help Desk – Linux Focus)** — `About the Role`, `Location`, `What Makes You a Good Fit`, `Nice to Have` — all without colons.
- **Engineering Program Manager** — 8 separate headings, all without colons (and all rendered as `<h2>`/`<h3>`).
- **GTM Engineer, Pre-Sales** — 8 headings missing colons; also uses h2/h3.

### 3.5 Postings using a *different* section framework — **Medium severity**

A small cluster of postings ignores the Skydio "About / How you'll make an impact / What makes you a good fit" template and uses an alternate framework. These are all in the Autonomy or PM cluster, suggesting one team copied another team's template:

| Posting | Heading framework |
|---|---|
| Software Engineer – Simulation & Robotics Engineer (×2) | About the Role · Areas of Responsibility · What You'll Do · Qualifications · Bonus Experience |
| Software Engineer – Autonomy Infrastructure, Systems and Tools (×2) | (same) |
| Software Engineer – Cloud Simulation & Full-Stack (×2) | (same) |
| Revenue Operations Analyst, CPQ | What you'll drive (scope) · Day-to-day responsibilities · Tech stack you'll work with · What you'll bring · Reporting & Working Model |
| Equipment and Inventory Specialist (Part Time) | Position Overview · Key Responsibilities · Preferred Qualifications · Ideal Candidate |
| Logistics Operations Specialist, HQ | Key Responsibilities · `1. Logistics Operations & Shipping (≈60%)` · `2. Logistics Coordination & Process Improvement (≈25%)` · `3. Workplace Operations Support (≈15%)` · Required Qualifications · Preferred Qualifications |
| Workplace Experience Coordinator Part-Time | Workplace Experience & Office Operations · People Operations & HR Coordination · Qualifications · Work Environment |
| Inside Sales Solutions Engineer – Public Safety | About the Role · How You'll Make an Impact · Preferred Skills and Qualifications · What Is Required |
| Director, Global Supply Management – Mechanicals | About the role: · What you will do: · Desired qualifications: |

**Logistics Operations Specialist, HQ** is uniquely the only posting that **numbers** its subsections (`1. … 2. … 3. …`) — no other posting uses numbered list-style headings.

### 3.6 Inline emphasis: `<u>` underline and `<em>` italics — **Medium severity**

The base template uses **bold** for emphasis. **9 postings** introduce `<u>` (underline) — which on the web reads as a hyperlink and is the WCAG-discouraged style for emphasis. **2 postings** introduce `<em>` italics. No posting uses `<s>`/`<strike>`/`<del>`, and no posting uses `<span>` (good).

| Posting | Tag | Example string |
|---|---|---|
| Director, Growth Marketing – Commercial | `<em>` | *"Ability to be in our San Mateo, CA office 3 days per week"* |
| Senior NPI Product Quality Engineer | `<em>` + `<u>` | "Please Note:" |
| Field Service Technician | `<u>` | "Based out of Denver, Las Vegas, Dallas and Chicago, Phoenix, Baltimore, Nashville, or Orlando" |
| Senior Technical Recruiter | `<u>` | "PLEASE NOTE:" |
| Senior Technical Recruiter – Hardware Operations | `<u>` | "PLEASE NOTE:" |
| Staff Technical Recruiter | `<u>` | "PLEASE NOTE:" |
| Manufacturing Execution System Analyst | `<u>` | "PLEASE NOTE:" |
| Lead Staff Electrical Engineer | `<u>` | "Skydio F10 Program" |
| Public Safety Strategist (West / Midwest / PNW) | `<u>` | An entire bullet underlined: "Champion Skydio's innovative drone and DFR technology, demonstrating public safety value to key decision-makers …" |
| Senior Software Engineer, Full Stack | `<u>` | An entire bullet underlined: "Continually design and expand Skydio Cloud's core data model and API for drones/docks …" |
| Full Stack Product Counsel | `<u>` | "Develop, execute, and own product legal strategy across all products …" |

### 3.7 Inline CSS `style="…"` — **Low severity**

Two postings carry pasted-in inline styles that the CMS did not strip:

- **Manager, Logistics** — `style="min-height:1.2em;margin-top:0;margin-bottom:0"`
- **Manufacturing Execution System Analyst** — `style="min-height:1.2em;margin-top:0;margin-bottom:0"`

These are residue from Google Docs / Word paste. They tighten line spacing on those two postings in a way no other posting does (no margin between paragraphs), producing visibly cramped copy.

### 3.8 Excess `<br>` tags instead of paragraphs — **Low severity**

46 postings contain at least one literal `<br>` tag. The base template separates paragraphs with `<p>` blocks (which gives consistent vertical rhythm); `<br>` collapses spacing to a single line break. Worst offenders:

| Posting | `<br>` count |
|---:|---|
| IT Technician (Help Desk – Linux Focus) | 9 |
| Director, Growth Marketing – Commercial | 8 |
| Autonomy Engineer – Deep Learning Infrastructure | 8 |
| Field Service Technician | 6 |
| Autonomy Engineer – Deep Learning Model Acceleration (×2) | 6 each |
| Director of Product Management, DFR | 6 |
| Systems Integration and Test Engineer (Mid to Senior Level) | 5 |
| IT Technician (Help Desk – Linux Focus) | 5 |

### 3.9 Postings without a `Compensation:` block (informational only)

The task scoped this audit to "pre-compensation" content, but it is worth noting that **30/120 postings have no `Compensation:` block at all** — for those postings the "pre-compensation" content *is* the whole posting body. The two notable groups are:

- **All ex-US engineering roles** (Zurich, Tampere, Tokyo, Bangalore, Taiwan, Germany).
- **All Autonomy intern roles** (Fall 2026, PhD, Computational Photography, etc.).

A few US-based postings also lack one — e.g. Director of Product Management DFR (San Mateo), Senior Director PM DFR (San Mateo), Manager Logistics (Hayward), Manufacturing Execution System Analyst (Hayward), Aviation Compliance Lead (San Mateo), Full Stack Product Counsel (San Mateo) — which is probably an oversight given that other San Mateo full-time roles do include one.

---

## 4. Postings that **most stand out** as visually different

Ranked by the cumulative number of formatting deviations:

1. **Senior Technical Support Representative – Japan** — uses `<h1>` for section headings, making them larger than the role title itself. Also 2 `<br>` tags. Most jarring single page.
2. **Engineering Program Manager** — 8 headings, all rendered as `<h2>`/`<h3>` and all missing the trailing colon. Completely different visual rhythm from neighbouring engineering postings.
3. **GTM Engineer, Pre-Sales** — 11 sections rendered as `<h2>`/`<h3>`, 8 headings without colons, plus 3 `<br>` tags.
4. **Revenue Operations Analyst, CPQ** — `<h2>` headings, plus a **1,115-character "heading"** that is actually 9 paragraphs of run-on text in one bold block.
5. **Staff Product Manager, Platform & Infrastructure** and **Senior Product Manager, Platform & Infrastructure** — both contain the same 2,064-char bold run-on block.
6. **Software Engineer – Simulation & Robotics Engineer / Autonomy Infra / Cloud Simulation (3 duplicated pairs = 6 postings)** — all use the alternate "Areas of Responsibility / What You'll Do / Qualifications / Bonus Experience" framework rendered as `<h2>` or `<h3>` headings.
7. **Field Service Technician** — 1,513-char run-on heading, `<u>` underline misuse, 6 `<br>` tags, 4 missing-colon headings.
8. **IT Technician (Help Desk – Linux Focus)** — 9 `<br>` tags, 5 missing-colon headings, run-on `What You'll Do` section.
9. **Logistics Operations Specialist, HQ** — only posting in the corpus to number its sections (`1.`, `2.`, `3.`) and the only one to put percentages in headings (`≈60%`). 6 sections rendered as `<h2>`/`<h3>`.
10. **Communications Manager**, **Full Stack Product Counsel**, **Aviation Compliance Lead** — uniformly use `<h2>`/`<h3>` headings without colons.
11. **Manager, Logistics** and **Manufacturing Execution System Analyst** — inherit Google-Docs paste residue (`style="min-height:1.2em;margin-top:0;margin-bottom:0"`), producing cramped paragraph spacing not seen anywhere else.

---

## 5. Per-posting formatting matrix

Columns:
- **RH** = number of real heading tags (`h1`/`h2`/`h3`) used inside the prose body (should be **0**)
- **IS** = number of inline `style="…"` attributes (should be **0**)
- **U** = uses `<u>` underline (should be **0**)
- **EM** = uses `<em>` italics (should be **0**)
- **BR** = count of `<br>` tags (should be **0**)
- **NC** = number of section headings missing trailing colon
- **RO** = number of run-on headings (length > 200 chars)
- **Cmp** = has a `Compensation:` block (Y/N)

|Title|RH|IS|U|EM|BR|NC|RO|Cmp|
|-|-|-|-|-|-|-|-|-|
|Autonomy Engineer - Deep Learning|0|0|0|0|1|0|0|N|
|Autonomy Engineer - Deep Learning|0|0|0|0|0|0|0|Y|
|Autonomy Engineer - Deep Learning Infrastructure|0|0|0|0|6|0|1|N|
|Autonomy Engineer - Deep Learning Infrastructure|0|0|0|0|8|0|0|Y|
|Autonomy Engineer - Deep Learning Model Acceleration|0|0|0|0|6|0|1|N|
|Autonomy Engineer - Deep Learning Model Acceleration|0|0|0|0|6|0|1|Y|
|Autonomy Engineer - Fixed Wing Planning & Controls|0|0|0|0|0|0|0|Y|
|Autonomy Engineer - ML & DL Infrastructure|0|0|0|0|0|0|0|N|
|Autonomy Engineer - ML & DL Infrastructure|0|0|0|0|0|0|0|Y|
|Autonomy Engineer - Planning and Controls|0|0|0|0|2|0|0|N|
|Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026|0|0|0|0|1|0|0|N|
|Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026|0|0|0|0|1|0|0|N|
|Autonomy Engineer Intern - Deep Learning (Computational Photography)|0|0|0|0|0|0|0|N|
|Autonomy Engineer Intern - Deep Learning (Computational Photography)|0|0|0|0|0|0|0|N|
|Autonomy Engineer Intern Fall 2026|0|0|0|0|0|0|0|N|
|Autonomy Engineer Intern Fall 2026|0|0|0|0|0|0|0|N|
|Autonomy Software Engineer|0|0|0|0|4|0|1|Y|
|Aviation Compliance Lead|4|0|0|0|1|0|0|N|
|Communications Manager|3|0|0|0|0|0|0|Y|
|CSM Manager - Public Safety (Major Markets)|0|0|0|0|0|0|0|Y|
|Customer Success Manager, Commercial|0|0|0|0|0|1|0|Y|
|Customer Success Manager, DFR Majors - Southeast|0|0|0|0|0|1|0|Y|
|Customer Success Manager, DFR Mid-Market - Northeast|0|0|0|0|0|2|0|Y|
|Deployment Engineer - Southeast|0|0|0|0|0|0|1|Y|
|Director of Product Management, Drone as First Responder (DFR)|0|0|0|0|6|0|1|N|
|Director, Global Supply Management - Mechanicals|0|0|0|0|0|0|0|Y|
|Director, Growth Marketing - Commercial|0|0|0|1|8|1|0|Y|
|Electrical Engineer (all levels)|0|0|0|0|2|0|0|Y|
|Electrical Engineer (Sustaining/Validation)|0|0|0|0|1|0|0|Y|
|Engineering Manager - Autonomy|0|0|0|0|1|0|0|Y|
|Engineering Program Manager|8|0|0|0|0|0|0|Y|
|Enterprise Account Manager (MoD/ MoI) – EMEA (Finland)|0|0|0|0|2|1|0|Y|
|Enterprise Account Manager (MoD/ MoI) – EMEA (Germany)|0|0|0|0|2|1|0|Y|
|Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland)|0|0|0|0|2|1|0|Y|
|Enterprise Account Manager, US Army|0|0|0|0|0|0|0|Y|
|Enterprise Account Manager, US Navy, US Marine Corps, and IC/SOCOM|0|0|0|0|0|0|0|Y|
|Equipment and Inventory Specialist (Part Time)|0|0|0|0|0|4|0|Y|
|Field Service Technician|0|0|1|0|6|4|1|Y|
|Field Support Representative|0|0|0|0|0|0|0|Y|
|Field Support Representative (Southwest, Remote)|0|0|0|0|0|0|0|Y|
|Field Support Representative - New York|0|0|0|0|0|0|1|Y|
|Full Stack Product Counsel|4|0|1|0|0|0|0|N|
|GTM Enablement Associate|0|0|0|0|2|0|1|Y|
|GTM Engineer, Pre-Sales|11|0|0|0|3|0|0|Y|
|Hardware Operations Program Manager|0|0|0|0|0|0|1|Y|
|Inside Sales Solutions Engineer – Public Safety|0|0|0|0|0|4|0|Y|
|IT Technician (Help Desk - Linux Focus)|0|0|0|0|9|5|0|Y|
|Lead Staff Electrical Engineer|0|0|1|0|1|0|1|Y|
|Logistics Operations Specialist, HQ|6|0|0|0|0|0|0|Y|
|Manager, Logistics|0|1|0|0|0|0|0|N|
|Manager, Technical Support|0|0|0|0|0|1|1|Y|
|Manufacturing Execution System Analyst|0|1|1|0|0|0|0|N|
|Middleware Software Engineer Intern - Fall 2026|0|0|0|0|0|0|0|N|
|Mission Success Operations Manager|0|0|0|0|0|1|0|Y|
|Order Management Analyst|0|0|0|0|0|0|0|Y|
|PCB Layout Engineer|0|0|0|0|2|0|0|Y|
|PhD Autonomy Engineer Intern - Deep Learning or Computer Vision|0|0|0|0|1|0|0|N|
|PhD Autonomy Engineer Intern - Deep Learning or Computer Vision|0|0|0|0|1|0|0|N|
|PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning)|3|0|0|0|0|0|1|N|
|Product Design Engineer (All Levels)|0|0|0|0|1|0|1|Y|
|Product Support Engineer|0|0|0|0|2|0|0|Y|
|Production Planner, Nightshift|0|0|0|0|0|0|0|Y|
|Program Manager, Commercial Programs|0|0|0|0|0|2|0|Y|
|Program Manager, DFR|0|0|0|0|0|1|0|Y|
|Public Safety Strategist (West Coast, Midwest, or Pacific North West)|0|0|1|0|0|1|0|Y|
|Revenue Operations Analyst, CPQ|5|0|0|0|4|1|1|Y|
|RF Design Engineer|0|0|0|0|0|0|0|Y|
|Senior Autonomy Engineer - Controls|0|0|0|0|0|0|0|Y|
|Senior Autonomy Engineer - Deep Learning|0|0|0|0|3|0|1|N|
|Senior Autonomy Engineer - Deep Learning|0|0|0|0|2|0|1|Y|
|Senior Autonomy Engineer, Data Curation|0|0|0|0|0|0|0|Y|
|Senior Business Operations Manager|3|0|0|0|0|0|0|Y|
|Senior Buyer|2|0|0|0|0|0|0|Y|
|Senior Customer Support Representative - India|0|0|0|0|0|0|0|Y|
|Senior Director, Product Management, Drone as First Responder (DFR)|0|0|0|0|4|0|1|N|
|Senior Engineering Manager, Infrastructure|0|0|0|0|0|0|1|Y|
|Senior Hardware Test and Reliability Engineer|0|0|0|0|0|0|0|Y|
|Senior Manager, Training|0|0|0|0|2|0|0|Y|
|Senior Materials Program Manager|0|0|0|0|0|0|0|Y|
|Senior NPI Product Quality Engineer|0|0|1|1|0|0|0|Y|
|Senior Product Manager, Platform & Infrastructure|0|0|0|0|1|1|2|Y|
|Senior Revenue Operations Manager|0|0|0|0|0|0|0|Y|
|Senior RF Design Engineer|0|0|0|0|0|0|0|Y|
|Senior Software Engineer - Embedded|0|0|0|0|0|0|0|Y|
|Senior Software Engineer - Mobile Platform|0|0|0|0|0|0|0|Y|
|Senior Software Engineer - Security|0|0|0|0|0|0|0|Y|
|Senior Software Engineer, Data Platform|0|0|0|0|1|1|0|Y|
|Senior Software Engineer, Frontend|0|0|0|0|0|0|0|Y|
|Senior Software Engineer, Full Stack|0|0|1|0|1|0|0|Y|
|Senior Software Engineer, Infrastructure|0|0|0|0|0|0|1|Y|
|Senior Solutions Engineer - North East|0|0|0|0|1|0|0|Y|
|Senior Technical Recruiter|0|0|1|0|2|0|0|Y|
|Senior Technical Recruiter - Hardware Operations|0|0|1|0|4|0|1|Y|
|Senior Technical Support Representative - Japan|3|0|0|0|2|0|0|N|
|Senior Wireless Software Engineer, National Security|6|0|0|0|2|0|0|Y|
|Senior Wireless Systems Performance Engineer|0|0|0|0|0|0|0|Y|
|Senior/Staff Embedded Software Engineer – Camera Systems|0|0|0|0|0|0|0|Y|
|Software Engineer - Autonomy Infrastructure, Systems and Tools|5|0|0|0|0|0|0|N|
|Software Engineer - Autonomy Infrastructure, Systems and Tools|5|0|0|0|0|0|0|Y|
|Software Engineer - Cloud Simulation & Full-Stack|5|0|0|0|0|0|0|N|
|Software Engineer - Cloud Simulation & Full-Stack|5|0|0|0|0|0|0|Y|
|Software Engineer - Embedded|0|0|0|0|0|0|0|Y|
|Software Engineer - Infrastructure|0|0|0|0|0|0|1|Y|
|Software Engineer - Simulation & Robotics Engineer|5|0|0|0|0|0|0|N|
|Software Engineer - Simulation & Robotics Engineer|5|0|0|0|0|0|0|Y|
|Software Engineer Intern Fall 2026/Winter 2027|0|0|0|0|4|0|1|N|
|Software Engineer, Full Stack|0|0|0|0|0|0|0|Y|
|Sr/Staff Embedded Software Engineer - Camera Systems|0|0|0|0|0|0|0|Y|
|Staff Global Supply Manager, Mechanicals|0|0|0|0|1|0|0|Y|
|Staff Product Manager, Platform & Infrastructure|0|0|0|0|1|1|2|Y|
|Staff Software Engineer - Embedded|0|0|0|0|0|0|0|Y|
|Staff Software Engineer - Security|0|0|0|0|0|0|0|Y|
|Staff Software Engineer, Frontend|0|0|0|0|0|0|0|Y|
|Staff Software Engineer, Full Stack|0|0|0|0|0|0|0|Y|
|Staff Technical Recruiter|0|0|1|0|0|0|0|Y|
|Supplier Quality Engineer, Sustaining|0|0|0|0|0|0|0|N|
|Systems Integration and Test Engineer (Mid to Senior Level)|0|0|0|0|5|0|0|N|
|Technical Support Specialist|0|0|0|0|0|0|0|Y|
|Wireless Software Engineer|0|0|0|0|0|0|0|Y|
|Workplace Experience Coordinator Part-Time|0|0|0|0|1|4|1|N|

A "clean" posting has all zeros in RH/IS/U/EM/BR/NC/RO **and** a `Y` in Cmp. By that bar, **~55 / 120 (46%)** of the postings are fully compliant today.

---

## 6. Recommendations

### 6.1 Adopt and publish a single canonical posting template

Lock in **exactly one** structure for the pre-compensation body and put it in the Ashby template / hiring manager handbook:

```
Skydio is the leading US drone company …  [the existing boilerplate intro — leave untouched]

**About the role:**
{1–3 plain paragraphs}

**How you'll make an impact:**
• Bullet
• Bullet

**What makes you a good fit:**
• Bullet
• Bullet

**Compensation:** …
```

Specify in writing:
- **All section labels are bold body text (`<p><strong>…</strong></p>`), not `<h1>/<h2>/<h3>`.** This single rule fixes the largest visible inconsistency (issue 3.1).
- Three canonical section labels: **"About the role:"**, **"How you'll make an impact:"**, **"What makes you a good fit:"** — sentence-case, straight apostrophe, **always end with a colon**.
- Allowed alternate label set when the role is on a brand-new team: **"About the team:"** (added before "About the role:") — same casing/punctuation rules.
- Bullet lists only via `<ul><li>…</li></ul>`; one idea per bullet; no numbered subsections inside a section.

### 6.2 Source content from the CMS, not from Google Docs / Word

Most of the inline `style="…"`, `<u>`, `<em>`, and stray `<br>` tags trace back to pasting from Google Docs or Word. Either:
- Add a paste-as-plain-text step to the recruiter workflow, or
- Wire an HTML sanitizer into the Ashby content pipeline (or into Skydio's careers page renderer) that strips `style`, `class`, `<u>`, `<em>`, `<span>`, and converts `<br><br>` runs into `<p>` boundaries.

### 6.3 Run a one-time content fix-up pass

Use the matrix in §5 as the punch-list. The 28 postings flagged in §3.2 (run-on headings) and the 18 postings flagged in §3.1 (real heading tags) deliver the biggest visual improvement per fix:

1. **Round 1 — High severity:** Fix the run-on headings on the 28 postings, and re-tag the 18 postings that use `<h1>/<h2>/<h3>` in the prose body.
2. **Round 2 — Medium severity:** Normalise heading casing/punctuation across all 95 postings that diverge from sentence-case + trailing colon. Replace curly apostrophes in headings with straight `'`. Replace `<u>` and `<em>` with `<strong>` (or remove the emphasis entirely for full underlined bullets).
3. **Round 3 — Low severity:** Strip the two inline `style="…"` attributes (Manager Logistics, Manufacturing Execution System Analyst). Convert excessive `<br>` runs to `<p>` boundaries on the 46 affected postings.
4. **Round 4 — Add missing compensation blocks** for the 6–10 US-based postings that are missing one (Director / Sr Director PM DFR, Manager Logistics, Manufacturing Execution System Analyst, Aviation Compliance Lead, Full Stack Product Counsel).

### 6.4 Add an automated lint to keep it clean

The same script that produced this audit can be wired into CI (or run nightly against the live site) to catch regressions. The minimum rule set:

- The body of a `<div class="prose block-content">…</div>` must contain **no** `<h1>`, `<h2>`, `<h3>`, `<u>`, `<em>`, `<span>`, or `style=` attributes.
- Every `<strong>` that is the entire content of its parent `<p>` (i.e. is a section heading) must match one of `~5` allowed labels and end with `:`.
- No `<strong>` may be longer than 80 characters (catches run-on headings).
- Posting must contain exactly one `<strong>Compensation:</strong>` block (configurable to optional for ex-US / intern roles).

A nightly job + Slack alert against this lint would prevent the slow drift that produced today's state.

---

*Audit produced by automated comparison of all 120 `/jobs/<uuid>/` pages on www.skydio.com on 2026-06-08. Raw per-posting data is in the analysis JSON used to generate §5.*

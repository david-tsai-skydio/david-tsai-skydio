# Skydio Careers — Job Posting Formatting Consistency Report

**Source:** [`https://www.skydio.com/careers`](https://www.skydio.com/careers)
**Date generated:** 2026-06-03
**Scope:** All 112 unique open job postings linked from the careers page, analyzed
from the start of the job description through (but **not** including) the
`Compensation:` block.
**Method:** Each individual job page (`/jobs/<uuid>`) was fetched and the body
inside `<div class="prose block-content">` was parsed structurally. The 112 bodies
were then compared element-by-element to identify formatting drift.

---

## 1. Executive summary

Of the **112 postings** analyzed, **91 (81%) contain at least one formatting
inconsistency** relative to the dominant pattern; only **21 postings (19%) are
fully clean**.

Skydio's careers site renders the body of every posting through a single CSS
container (`.prose.block-content`), so visible differences are driven almost
entirely by the **HTML elements the recruiter pasted into the ATS**. The most
visible inconsistencies on the rendered page are:

| Inconsistency | Postings affected | Visible effect |
|---|---|---|
| Headings authored as `<p><strong>X:</strong></p>` vs. real `<h2>`/`<h3>` | 19 / 112 use `<h*>`, 93 use `<p><strong>` | Section titles render at body-text size (~16 px) on most pages, but at heading size (~28–32 px / 22–24 px) on a handful — large visual jump between roles |
| Sentence case vs. Title Case in standard headings (e.g. "About the role" vs "About the Role") | 26 | Subtle, but clearly different across the same template heading |
| Stray `<br>` tags used as visual spacers inside / between paragraphs | 48 | Uneven vertical rhythm; some bullets/headings have extra whitespace |
| Section heading missing the trailing colon | 17 | Inconsistent typographic ending — `About the role:` vs. `About the Role` |
| `<u>`-underlined text (used for "PLEASE NOTE" callouts and link text) | 8 | Words appear underlined; on links it duplicates the existing link styling |
| Body-internal `<h1>` (should never appear, breaks page outline) | 1 | "Senior Technical Support Representative – Japan" |
| No section headings at all (single wall of text + bullets) | 2 | Significantly harder to scan than peer postings |
| Mixed semantic-heading + `<p><strong>` headings within the same posting | 4 | Two heading styles visible side-by-side |
| Anchor link styling (`class="c-link c-link--underline"` vs. plain `<a>`) | 10 (~40 anchors) | Some links underlined, others rely on default styling |
| Inline `style="…"` attribute on a `<div>` | 1 | Authoring artifact; visible blank gap |
| Italic `<em>` used inside a heading | 2 | One-off italicized callout |
| Job-title double space (`,  US Navy` etc.) | 4 | Visible double-space in the H1 |

> **Takeaway for the team:** the careers page CSS is consistent — the drift is
> in *how recruiters write the source*. A short authoring guide + a one-time
> cleanup pass will resolve almost all of the issues below.

---

## 2. Inventory

* Postings analyzed: **112** (all listings on the page)
* Departments represented: **16**
  * Autonomy (30), Software (18), Sales (12), Hardware (9), Professional Services & Training (9), Customer Support (6), Supply Chain & Logistics (6), People & Recruiting (5), Product (4), Connectivity (3), Manufacturing (3), Security (2), Marketing (2), IT (1), Legal (1), Policy & Regulatory Affairs (1)
* Locations represented: **11** — San Mateo (70), Zurich (16), US Remote (14), Hayward (4), Tampere (2), Boston, Bangalore, Tokyo, Germany, Taiwan, US AR Remote, "US CA San Mateo" (1 each — note: one location string is "US CA San Mateo" and another is "San Mateo, California, United States", which is itself a location-label inconsistency)
* Body-content size range: **254 → 1,019 words** (median ≈ 510 words). Largest outliers include "Manager, Technical Support" (1,019 words) and "GTM Engineer, Pre-Sales" (927 words); shortest outliers are several hardware roles (~250–325 words).
* Boilerplate intro (`Skydio is the leading US drone company…`): **present in 100% of postings.** ✅

---

## 3. Detailed findings

### 3.1 Heading hierarchy — the largest source of visible drift

Most postings encode section headings as **bolded paragraphs**, e.g.

```html
<p><strong>About the role:</strong></p>
```

…which render at body-text size (~16 px, 700 weight). A minority use real
semantic elements, e.g.

```html
<h2>About the Role</h2>
<h3>What you'll do</h3>
```

…which the global stylesheet renders at ~28–32 px (h2) / ~22–24 px (h3),
producing **dramatically larger headings** than the rest of the careers index.

**Distribution across postings:**

| Heading approach | # postings |
|---|---:|
| Only `<p><strong>X:</strong></p>` | **93** |
| Only semantic `<h2>` / `<h3>` | 13 |
| Mixes both within same posting | 4 |
| No headings of any kind | 2 |

**Postings using semantic `<h2>` (will look noticeably "bigger"):**
Aviation Compliance Lead · Communications Manager · Engineering Program Manager · GTM Engineer, Pre-Sales · Logistics Operations Specialist, HQ · Revenue Operations Engineer, Quoting Systems · Senior Buyer · Senior Wireless Software Engineer, National Security · Software Engineer - Autonomy Infrastructure, Systems and Tools (×2) · Software Engineer - Cloud Simulation & Full-Stack (×2)

**Postings additionally introducing `<h3>` sub-headings:**
Engineering Program Manager · Full Stack Product Counsel · GTM Engineer, Pre-Sales · Logistics Operations Specialist, HQ · PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) · Senior Business Operations Manager · Software Engineer - Simulation & Robotics Engineer (×2)

**Postings that mix `<h*>` and `<p><strong>` in the same posting (most jarring):**
PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) · Revenue Operations Engineer, Quoting Systems · Senior Business Operations Manager · Senior Buyer

**Postings with NO section headings at all (single wall of text):**
* Product Support Engineer
* Senior Technical Support Representative - Japan

**Postings with `<h1>` *inside* the body (semantically wrong; only one allowed per page):**
* Senior Technical Support Representative - Japan — uses `<h1>About the role:</h1>` and `<h1>How you'll make an impact:</h1>` inside the body, in addition to the page's own `<h1>` for the title. This breaks the page outline and renders the section titles at title size.

### 3.2 Heading capitalization drift

The same standard headings appear with two different capitalization conventions:

| Canonical heading | Variant 1 (sentence case) | Variant 2 (Title Case) | Other variants |
|---|---:|---:|---|
| About the role | **"About the role" — 51** | "About the Role" — 34 | — |
| How you'll make an impact | **"How you'll make an impact" — 36** + "How you'll make an impact" (curly apostrophe) — 17 | "How You'll Make an Impact" — 22 + 1 | "How you will make an impact" — 3 |
| What makes you a good fit | **"What makes you a good fit" — 58** | "What Makes You a Good Fit" — 21 | "What would make you a good fit" — 7; "What makes you a strong fit" — 4 |
| About the team | "About the team" — 6 | **"About the Team" — 10** | — |

**Note:** The **dominant convention is sentence case**, but ~30% of postings
slipped into Title Case. The straight (`'`) vs. curly (`'`) apostrophe also
varies between postings.

26 postings have at least one heading that drifts from the dominant case
convention. Notable concentrations are in the Sales department (all four
"Enterprise Account Manager" postings use Title Case throughout) and
"IT Technician (Help Desk - Linux Focus)".

### 3.3 Trailing-colon inconsistency

The standard pattern is `<strong>About the role:</strong>` — colon included.
17 postings break this in at least one heading, mixing colon and no-colon
within the same posting.

Examples of headings *missing* a trailing colon (verbatim):

* "About the Role" — IT Technician (Help Desk - Linux Focus); Program Manager, Commercial Programs
* "What You'll Do" / "What Makes You a Good Fit" — IT Technician (Help Desk - Linux Focus)
* "Why Join Us?" — Senior Software Engineer, Data Platform *(also note the `?` instead of `:`)*
* "Location" — Senior Product Manager, Platform & Infrastructure; Staff Product Manager, Platform & Infrastructure
* "Requirements" — Customer Success Manager, DFR Majors – Southeast; Customer Success Manager, DFR Mid-Market – Northeast
* "Experience & Skills" — Customer Success Manager, DFR Mid-Market – Northeast
* "Workplace Experience & Office Operations", "People Operations & HR Coordination", "Qualifications", "Work Environment" — Workplace Experience Coordinator Part-Time
* "Additional Desired Experience and Skills" — Director, Growth Marketing – Commercial
* "What makes you a good fit" (no colon, lower-case) — Customer Success Manager, Commercial; Mission Success Operations Manager
* "Build Automation & Intelligence into Mission Success", "Customer Digital Experience", "Cross-Functional Architecture & Governance", "Scalability & Cost Avoidance" — Success Systems Specialist
* "This role must be based in Switzerland, Germany, or Finland." — *all three* Enterprise Account Manager (MoD/ MoI) – EMEA postings (this is a **full sentence bolded as a heading** — see §3.4)

### 3.4 Bolded sentences masquerading as headings

In 4 postings, full sentences (≥ 8 words) are wrapped in `<p><strong>…</strong></p>`,
which the renderer treats as a section heading even though the content is a
sentence:

* **Manager, Technical Support** — "Willingness to work extended hours, weekends, holidays and on-call support as needed."
* **Enterprise Account Manager (MoD/ MoI) – EMEA (Finland / Germany / Switzerland)** — "This role must be based in Switzerland, Germany, or Finland." (×3 — appears across three sibling postings)

These look visually like headings but read like body text.

### 3.5 Stray `<br>` tags used as spacers — 48 postings (43%)

Many postings contain hand-typed line breaks that the rich-text editor
preserved. They produce uneven vertical spacing, especially around bullet lists
and trailing paragraphs.

| `<br>` count | # postings |
|---:|---:|
| 0 | 64 |
| 1–2 | 30 |
| 3–5 | 11 |
| 6+ | **7** |

Worst offenders:

| `<br>` count | Posting |
|---:|---|
| 9 | IT Technician (Help Desk - Linux Focus) |
| 8 | Autonomy Engineer - Deep Learning Infrastructure (San Mateo) |
| 8 | Director, Growth Marketing – Commercial |
| 6 | Autonomy Engineer - Deep Learning Infrastructure (Zurich) |
| 6 | Autonomy Engineer - Deep Learning Model Acceleration (×2) |
| 6 | Director of Product Management, Drone as First Responder (DFR) |
| 5 | Systems Integration and Test Engineer (Mid to Senior Level) |

### 3.6 `<u>` underlines — 8 postings

`<u>` is used inconsistently:

* As a faux-heading callout: "**PLEASE NOTE:**" with the words underlined — Senior Technical Recruiter, Senior Technical Recruiter - Hardware Operations, Staff Technical Recruiter
* Inside link text (redundant with link styling) — Lead Staff Electrical Engineer, Senior Software Engineer, Full Stack, Full Stack Product Counsel
* As a sub-heading separator: "Additional Responsibilities:" underlined — Public Safety Strategist (West Coast, Midwest, or Pacific North West)
* In an italic-strong-underline sandwich: `<em><strong><u>Please Note:</u></strong></em>` — Senior NPI Product Quality Engineer

Because `<u>` is rare, the underlined text visibly stands out against every
other posting's typography.

### 3.7 `<em>` italics — 2 postings

* **Senior NPI Product Quality Engineer** — "*Please Note:*" rendered italic-bold-underlined
* **Director, Growth Marketing – Commercial** — single italicized fragment

No other posting uses italics, so these two are the only ones with italic text
in their pre-compensation body.

### 3.8 Inline `style="…"` attribute — 1 posting

* **Manager, Logistics** — contains `<div style="min-height:1.2em;margin-top:0;margin-bottom:0">` between the qualifications list and the next section. This is editor cruft and produces a visible empty band that no other posting has.

### 3.9 Anchor (link) styling drift — 10 postings (~40 anchors)

Most postings use plain `<a href="…">` and rely on `.prose` to style links
(331 plain anchors total across all 112 postings). However, 10 postings emit
`class="c-link c-link--underline"` on their anchors (40 anchors total), which
applies a different underline / hover style.

Affected postings (each contains class-styled links mixed with plain links in
the same posting):

* Autonomy Engineer - Deep Learning Infrastructure
* Autonomy Engineer - Deep Learning Model Acceleration
* Autonomy Software Engineer
* Engineering Manager - Autonomy
* Senior Software Engineer - Embedded
* Senior Technical Recruiter
* Senior Technical Recruiter - Hardware Operations
* Software Engineer - Embedded
* Staff Software Engineer - Embedded
* Staff Technical Recruiter

### 3.10 List-item structure — consistent ✅

All 111 postings that use bullet lists wrap each `<li>` around a `<p>` (i.e.
`<li><p>…</p></li>`). No posting uses bare `<li>…</li>`. This is the one
formatting decision that is uniform across the entire site, so vertical bullet
spacing is consistent. **Keep this convention.**

### 3.11 Job-title typography (the `<h1>` itself)

Four postings have a **double space** baked into the title, which is visible in
the page's `<h1>`:

* Enterprise Account Manager,&nbsp;&nbsp;US Navy, US Marine Corps, and IC/SOCOM
* Senior Software Engineer,&nbsp;&nbsp;Data Platform
* Senior Software Engineer,&nbsp;&nbsp;Infrastructure
* Staff Global Supply Manager,&nbsp;&nbsp;Mechanicals

### 3.12 Boilerplate intro — consistent ✅

Every one of the 112 postings opens with the standard `Skydio is the leading US
drone company…` paragraph. This is one of the strongest consistency wins.
There are still 5–6 small **wording variants** of the boilerplate (some say
"the world leader in autonomous flight, the key technology for the future of
drones and aerial mobility"; others stop at "world leader in autonomous flight.
We leverage breakthrough AI…"), but the typography is uniform.

---

## 4. Postings that stand out the most (ranked by issue count)

These are the postings most worth a hands-on edit pass. (Issue counts cover
only the categories above; a posting can score 1 even when it is otherwise
clean — e.g. a single capitalization drift.)

| Issues | Department | Posting | Headline problem |
|---:|---|---|---|
| 4 | Sales | **Revenue Operations Engineer, Quoting Systems** | 5 `<h2>` headings + mixes `<p><strong>` headings + 4 `<br>` + `About the Role` Title Case |
| 3 | Customer Support | **Senior Technical Support Representative – Japan** | 3 `<h1>` tags inside the body **and** has zero "section" headings (because the H1s are the sections) + 2 `<br>` |
| 3 | IT | **IT Technician (Help Desk - Linux Focus)** | 9 `<br>` (most of any posting); 3 headings missing colon; Title Case drift |
| 3 | Software | **Senior Software Engineer, Data Platform** | Title has double space; "Why Join Us?" heading uses `?` not `:`; 1 `<br>` |
| 3 | Marketing | **Director, Growth Marketing – Commercial** | 8 `<br>`; italics; heading missing colon |
| 3 | People & Recruiting | **Senior Technical Recruiter** | Mixed link classes; `<u>` callout; `<br>` |
| 3 | People & Recruiting | **Senior Technical Recruiter – Hardware Operations** | Same pattern as above + 4 `<br>` |
| 3 | People & Recruiting | **Staff Technical Recruiter** | `<u>` callout; mixed link classes |
| 3 | Sales | **Enterprise Account Manager (MoD/MoI) – EMEA (Finland / Germany / Switzerland)** | Three sibling postings, all Title Case throughout; "This role must be based…" sentence used as a heading; `<br>` |
| 3 | Sales | **GTM Engineer, Pre-Sales** | 4 `<h2>` + 7 `<h3>` (heaviest semantic-heading user); 3 `<br>` |
| 3 | Sales | **Public Safety Strategist (West Coast, Midwest, or Pacific North West)** | `<u>` callout; Title Case drift; heading missing colon |
| 3 | Supply Chain & Logistics | **Senior Business Operations Manager** | 3 `<h3>` mixed with `<p><strong>`; Title Case |

The **Sales** department has the largest concentration of drift — 8 of the 12
Sales postings appear in this top list. The **Customer Support** posting from
**Tokyo** is the most structurally broken (body `<h1>`s).

---

## 5. Recommendations

### Quick wins (one-time content cleanup)

1. **Standardize section-heading element.** Pick one. Recommendation:
   continue using `<p><strong>About the role:</strong></p>` since 93/112
   already follow this pattern, **or** migrate everything to semantic
   `<h2>` / `<h3>` and tune `.prose h2/h3` CSS to produce a moderate visual
   step (today, real `<h2>` is ~30 px which is too large vs. the 16 px most
   postings use). Migrating to semantic headings is the better long-term
   choice (accessibility / SEO), but pick *one* and apply it everywhere.
2. **Lock in heading text + capitalization.** Adopt a single canonical set:
   * `About the role:`
   * `How you'll make an impact:`
   * `What makes you a good fit:`
   * `About the team:` *(only when present)*
   * `Bonus points:` *(when present)*
   Use **sentence case + curly apostrophe + trailing colon** (the dominant convention).
3. **Strip `<br>`, `<u>`, `<em>`, inline `style="…"`, and `class="c-link…"`
   from all 48 + 8 + 2 + 1 + 10 affected postings.** These are paste artifacts
   from Word / Google Docs / older Greenhouse imports and add no semantic
   value.
4. **Fix the four titles with double spaces** ("Senior Software Engineer,&nbsp;&nbsp;Data Platform" etc.).
5. **Replace the body-internal `<h1>` tags** in *Senior Technical Support
   Representative – Japan* with the canonical `<p><strong>X:</strong></p>` (or
   `<h2>`) and add the missing section structure to *Product Support Engineer*
   (currently a wall of text).
6. **Remove the 4 sentence-as-heading cases** so they read as normal paragraphs:
   * Manager, Technical Support — "Willingness to work extended hours…"
   * Enterprise Account Manager (MoD/ MoI) – EMEA (×3) — "This role must be based in Switzerland, Germany, or Finland."

### Process changes (prevent regression)

7. **Author postings in the rich-text editor's "Code/Plain" view first.**
   Pasting from Word/Docs is the source of nearly every issue above.
8. **Provide a Greenhouse / ATS template** with the canonical heading set
   already included — recruiters fill in the body, never re-type the headings.
9. **Add a CI lint** on the careers data (the postings come from a Greenhouse
   feed — a quick script can flag any of: `<h1>`/`<h2>`/`<br>`/`<u>`/`<em>`/
   inline-`style`/class-attribute/double-space-in-title/sentence-as-strong) on
   every publish.
10. **Pick one location-label format.** Today the same place is rendered as
    "San Mateo, California, United States" (70 postings) and "US CA San
    Mateo" (1 posting — *GTM Engineer, Pre-Sales*).
11. **Consolidate the 5–6 boilerplate intro variants** to a single approved
    paragraph, owned by the recruiting-content team.

### Optional polish

12. The 13 postings already using semantic `<h2>` are a good template for what
    the future state should look like *if* you choose route 1's "migrate to
    semantic" option — they happen to also be among the most carefully
    structured postings overall.

---

## 6. Appendix — full per-posting issue list

The complete machine-generated drift table (one row per posting, sorted by
issue count) is available in the repository at
`reports/per_job_issues.json` for ATS-side cleanup or scripted fixes.

Categorical totals from that file:

| Category | # postings |
|---|---:|
| Stray `<br>` tag(s) | 48 |
| Heading capitalization drift | 26 |
| Section heading missing trailing colon | 17 |
| Use semantic `<h2>` (vs. dominant `<p><strong>`) | 12 |
| Anchor `class="c-link c-link--underline"` mixed with plain links | 10 |
| `<u>` underline tag(s) | 8 |
| Use semantic `<h3>` sub-headings | 8 |
| Title contains a double space | 4 |
| Mixes semantic `<h*>` and `<p><strong>` headings | 4 |
| `<em>`/`<i>` italic tag(s) | 2 |
| No section headings at all | 2 |
| Body-internal `<h1>` | 1 |
| Inline `style="…"` attribute | 1 |
| **Postings with at least one issue** | **91 / 112 (81%)** |
| **Postings with zero issues** | **21 / 112 (19%)** |


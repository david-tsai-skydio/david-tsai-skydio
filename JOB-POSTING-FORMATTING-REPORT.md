# Skydio Careers — Job Posting Formatting Consistency Report

**Source:** https://www.skydio.com/careers
**Postings analyzed:** 113 unique job pages (all "View & Apply" links from the careers listing)
**Scope:** Body content from the start of the role description up to — but not including — the "Compensation" block. The header (job title + location subtitle) and the global page chrome were also excluded because they are template-rendered identically for every posting.
**Date of capture:** 2026-06-01
**Method:** Programmatic fetch of each posting's HTML and structural inspection of the `<div class="prose block-content">` body. Because every posting is rendered with the same global CSS, all observed visual inconsistencies come from differences in the underlying HTML/markup that each hiring manager (or the source ATS) supplies. Differences in markup translate directly to differences in rendered font size, weight, spacing, and hierarchy. Supporting data:
- `job-posting-formatting-summary.csv` — one row per posting with the key formatting signals
- `job-posting-formatting-analysis.json` — full structural fingerprint per posting

---

## 1. Executive summary

| Inconsistency | Severity | # affected of 113 |
|---|---|---|
| Section headers rendered at different visual sizes (`<h1>` / `<h2>` / `<h3>` vs. `<p><strong>`) | **High** | 18 |
| Section label wording — sentence case vs. Title Case (e.g., "About the role" vs. "About the Role") | **High** | ~45 (Title-Case variants) |
| Section label wording — semantic variants (`What makes you a good fit` vs `What would make you a good fit` vs `Requirements` vs `Useful skills and experience`) | High | ~25 |
| Smart vs. straight apostrophes within the same section labels (`you'll` vs `you'll`) | Medium | 7 jobs use both within the same posting; 41 vs 52 split overall |
| Punctuation drift — colon, no colon, space-before-colon | Medium | ~30 |
| Empty `<p></p>` paragraphs that add a visible blank line | Medium | 54 |
| `<br>` line breaks instead of structural separators | Medium | 48 (1–9 per posting) |
| Inline `style="…"` overriding the site's stylesheet | Low (but visible) | 1 |
| `<em>` / `<i>` italic usage | Low | 2 |
| Job uses prose with no bullet list at all | Medium | 1 |
| Section body collapsed into a single inline paragraph (no breaks between bolded sub-headers) | Medium | 3 |
| Title-string typo / double space ("Senior Software Engineer,  Infrastructure") | Low | 4 |
| Body typo in label ("What Makes Your a Good Fit") | Low | 1 |
| Location requirement inserted as an ad-hoc inline label rather than a dedicated component | Medium | 12 |
| `<h2>` followed by `<h3>` sub-sections (creates a 3-tier visual stack other postings don't have) | Medium | 2 |

The biggest issue is **inconsistent heading hierarchy**: 95 of 113 postings render every section header as a bold body paragraph, while the remaining 18 inject real `<h1>`–`<h3>` elements. On a Skydio job page, the body paragraph headers render at ~16 px / 700 weight, whereas `<h2>` and `<h3>` from the site's typography scale render substantially larger (roughly 28 px / 24 px in the same `prose` block). The result is that those 18 postings look visibly "louder" — and they're located disproportionately in newer Operations / Aviation / Software-Eng-Cloud roles, which makes them stand out from the engineering bulk of the listing.

The second-biggest issue is **label drift**: there are at least six different ways to write "About the role" and eight different ways to write "What makes you a good fit," with no apparent pattern other than which manager or which template was used to author the role. This is the most visible inconsistency for any visitor that browses 2+ postings.

---

## 2. The baseline (the format ~84% of postings follow)

The canonical Skydio job posting has the following pre-compensation structure (used by 95 of 113):

```12:32:job-posting-formatting-summary.csv
Autonomy Engineer - Deep Learning,"San Mateo, California, United States - Full-time",https://www.skydio.com/jobs/cc83824e-a1cd-4bc7-9206-7264da9fbd61/?gh_jid=cc83824e-a1cd-4bc7-9206-7264da9fbd61,p>strong,About the role,How you'll make an impact,What makes you a good fit,365,14,2,0,0,0,0,True
```

In HTML terms:

```html
<p>Skydio is the leading US drone company …</p>             <!-- preamble (113/113) -->
<p><strong>About the role:</strong></p>                      <!-- section header  -->
<p>… role narrative …</p>
<p><strong>How you'll make an impact:</strong></p>
<ul>
  <li><p>Bullet item 1</p></li>
  <li><p>Bullet item 2</p></li>
</ul>
<p><strong>What makes you a good fit:</strong></p>
<ul>
  <li><p>Bullet item</p></li>
</ul>
<p><strong>Compensation:</strong> …</p>                      <!-- (out of scope) -->
```

Specifically:
- Section headers are `<p><strong>Label:</strong></p>` — they render at body size, just bolded.
- All bullet content is wrapped in `<li><p>…</p></li>` (112 of 113 — confirmed consistent).
- No `<br>` tags, no empty `<p>` paragraphs, no inline styles, no `<em>`/`<i>`.
- The three canonical section labels are:
  1. **"About the role"** (sentence case, no colon when standalone, colon when inline)
  2. **"How you'll make an impact"** (sentence case, ASCII apostrophe)
  3. **"What makes you a good fit"** (sentence case)
- Bullet list is the only list type used (no `<ol>` anywhere in the dataset).

Every deviation called out below is measured against this baseline.

---

## 3. Detailed inconsistencies

### 3.1 Section header markup — 18 postings render headers at a different visual size

The site's `prose` typography ramps for headings. `<h2>` and `<h3>` are visibly larger than the body-bold pattern that the rest of the listing uses, so these 18 postings have section titles that "shout" relative to the other 95.

**Postings that use semantic `<h1>` (renders as the largest heading on the page — competes with the actual job title `<h1>`):**

| Title | Heading levels used |
|---|---|
| Senior Technical Support Representative - Japan (Tokyo) | `<h1>` |

**Postings that use `<h2>` (renders much larger than body bold):**

| Title | Heading levels used |
|---|---|
| Software Engineer - Autonomy Infrastructure, Systems and Tools (San Mateo) | `<h2>` only |
| Software Engineer - Autonomy Infrastructure, Systems and Tools (Zurich) | `<h2>` only |
| Software Engineer - Cloud Simulation & Full-Stack (San Mateo) | `<h2>` only |
| Software Engineer - Cloud Simulation & Full-Stack (Zurich) | `<h2>` only |
| Senior Wireless Software Engineer, National Security (San Mateo) | `<h2>` only |
| Senior Buyer (Hayward) | `<h2>` only |
| Communications Manager (US Remote) | `<h2>` only |
| Aviation Compliance Lead (San Mateo) | `<h2>` only |
| Aviation Regulatory Program Manager (US Remote) | `<h2>` only |
| Revenue Operations Engineer, Quoting Systems (San Mateo) | `<h2>` only |

**Postings that use `<h3>`:**

| Title | Heading levels used |
|---|---|
| PhD Autonomy Engineer Intern - Planning & Controls (RL) (Zurich) | `<h3>` only |
| Software Engineer - Simulation & Robotics Engineer (San Mateo) | `<h3>` only |
| Software Engineer - Simulation & Robotics Engineer (Zurich) | `<h3>` only |
| Full Stack Product Counsel (San Mateo) | `<h3>` only |
| Senior Business Operations Manager (San Mateo) | `<h3>` only |

**Postings that use *both* `<h2>` and `<h3>` (3-tier visual stack the rest of the listing doesn't have):**

| Title | Heading levels used |
|---|---|
| Hardware Engineering Program Manager (San Mateo) | `<h2>` for top-level, `<h3>` for sub-sections |
| GTM Engineer, Pre-Sales (US CA San Mateo) | `<h2>` for top-level, `<h3>` for sub-sections |

> **Specific example of the visual mismatch:** *Software Engineer - Autonomy Infrastructure, Systems and Tools* uses `<h2>About the Role:</h2>` whereas the otherwise-identical *Autonomy Software Engineer* role next to it uses `<p><strong>About the role:</strong></p>`. The two `About the role` headings end up at noticeably different point sizes despite being adjacent in the listing.

### 3.2 Section label wording — at least 24 distinct strings cover three concepts

#### "About …" — the role-narrative header

| Variant | Count |
|---|---|
| About the role | 38 |
| About the Role | 24 |
| About the team | 5 |
| About the Team | 5 |
| About The Role | 1 |
| About the role : (extra space before colon) | 2 |

Among these, sentence-case ("About the role") is most common but Title-Case ("About the Role") is used by 24 postings — a quarter of the listing. Mixed casing creates a visible inconsistency for any visitor browsing more than one role.

#### "How you'll make an impact" — the responsibilities header

| Variant | Count |
|---|---|
| How you'll make an impact (sentence + ASCII `'`) | 25 |
| How You'll Make an Impact (Title + smart `'`) | 17 |
| How you'll make an impact (sentence + smart `'`) | 9 |
| How you will make an impact (no contraction) | 3 |
| How You'll Make an Impact (Title + ASCII `'`) | 1 |
| Key Responsibilities | 1 |
| What you will do / What You'll Do / What You'll Work On / Areas of Responsibility | 6 (split across 4 spellings) |
| Examples of what you'll help build / Project Examples | 2 |

7 postings use **both** the curly `'` and the ASCII `'` in different headings within the same posting — these will read as visually mismatched even on a single page.

#### "What makes you a good fit" — the requirements header

| Variant | Count |
|---|---|
| What makes you a good fit | 49 |
| What Makes You a Good Fit | 18 |
| What would make you a good fit | 6 |
| What makes you a strong fit | 4 |
| What Makes You a Strong Fit | 1 |
| What Would Make You a Good Fit | 1 |
| What Makes Your a Good Fit | 1  ← **typo** |
| What Makes You A Good Fit | 1 |
| Qualifications | 4 |
| Requirements | 3 |
| Preferred Qualifications | 3 |
| Useful skills and experience | 2 |
| Desired Qualifications | 1 |

The typo `"What Makes Your a Good Fit"` is in **Senior People Analytics Analyst** (San Mateo).

### 3.3 Trailing-section names — "bonus" requirements have eight names

These are all the trailing-skills sections used after the primary requirements:

| Variant | Count |
|---|---|
| Bonus points for | 8 |
| Bonus points | 6 |
| Bonus Points | 6 |
| Preferred Qualifications | 6 |
| Useful skills and experience | 4 |
| Nice to have | 4 |
| Nice-to-Haves | 2 |
| Nice To Haves | 2 |
| Desired Qualifications | 2 |
| Nice to Have | 1 |
| Additional Desired Experience and Skills | 1 |
| Certifications preferred | 1 |
| Even better | 1 |
| Bonus Experience: | 4 (the Sim/Cloud cluster) |

Same concept ("things that would help but aren't required"), 14 different surface forms.

### 3.4 Punctuation drift on section labels

- **Trailing colon present** (e.g. `<strong>About the role:</strong>`) is the dominant convention, but ~20 postings drop the colon entirely (`About the Role`, `About the role`, `About the team`).
- **Space before colon** — `About the role :` and `Location :` — present in **Product Support Engineer** (San Mateo) and **Product Support Engineer Intern** (San Mateo). Renders as a stray gap inside the bold label.
- **Inline label vs standalone label** — Most postings put the label in its own paragraph (`<p><strong>X:</strong></p>` followed by content `<p>…</p>`). Several put the label and the first sentence in the same paragraph (`<p><strong>X:</strong> Content…</p>`). This changes whether the label sits on its own line or wraps inline with the body copy.

### 3.5 Whitespace artifacts — empty `<p></p>` paragraphs

54 of 113 postings contain at least one empty paragraph, which renders as a visible blank line that other postings don't have. The worst offenders:

| Empty `<p>` count | Title |
|---|---|
| 6 | Senior Product Manager, Platform & Infrastructure |
| 6 | Staff Product Manager, Platform & Infrastructure |
| 5 | Senior Software Engineer, Frontend |
| 5 | Staff Software Engineer, Frontend |
| 5 | Customer Success Manager, DFR Mid-Market - Northeast |
| 5 | Deployment Engineer - Southeast |
| 5 | Program Manager, Commercial Programs |
| 4 | Senior Wireless Software Engineer, National Security |
| 4 | Senior/Staff Embedded Software Engineer – Camera Systems |
| 4 | Sr/Staff Embedded Software Engineer - Camera Systems |
| 4 | CSM Manager - Public Safety (Major Markets) |

### 3.6 `<br>` line breaks instead of structural breaks

48 postings use `<br>` tags inside `<p>` or `<li><p>` content, which forces a soft line break that the body copy elsewhere doesn't have. Top offenders:

| `<br>` count | Title |
|---|---|
| 9 | IT Technician (Help Desk - Linux Focus) |
| 8 | Autonomy Engineer - Deep Learning Infrastructure (San Mateo) |
| 8 | Director, Growth Marketing - Commercial |
| 6 | Autonomy Engineer - Deep Learning Infrastructure (Zurich) |
| 6 | Autonomy Engineer - Deep Learning Model Acceleration (Zurich) |
| 6 | Autonomy Engineer - Deep Learning Model Acceleration (San Mateo) |
| 4 | Autonomy Software Engineer |
| 4 | Director of Product Management, Drone as First Responder (DFR) |
| 4 | Software Engineer Intern Fall 2026/Winter 2027 |
| 4 | Senior Technical Recruiter - Hardware Operations |
| 4 | Revenue Operations Engineer, Quoting Systems |

The pattern most commonly is `…<br/></p></li>` inside bullets — a trailing line break at the end of the last bullet, which adds a half-empty line below the list.

### 3.7 Inline `style` attribute

**One** posting overrides the site stylesheet with an inline style:

- **Manager, Logistics** (Hayward) contains `<div style="min-height:1.2em;margin-top:0;margin-bottom:0"></div>`. This forces a 1.2 em (≈ one line-height) blank block that other postings don't have, and bypasses the site's spacing tokens.

### 3.8 Italic text (`<em>` / `<i>`)

**Two** postings use italics where the rest of the listing uses none:

- **Senior NPI Product Quality Engineer** (San Mateo) — 1 `<em>`
- **Director, Growth Marketing - Commercial** (San Mateo) — 1 `<em>`

In a listing that is otherwise emphasis-free, even one italic phrase visually pops.

### 3.9 Job uses no bullet list at all

- **Director, Global Supply Management - Mechanicals** (San Mateo) — Has no `<ul>` and therefore no bullets in its pre-compensation body. Everything is prose paragraphs, which reads very differently from the rest of the listing where bullets are universal.

### 3.10 "Wall of bold" — labels collapsed into a single inline paragraph

Three postings collapse what should be multiple labeled sections into one long paragraph by using inline `<strong>label:</strong>` markers without paragraph breaks between them:

- **Senior Product Manager, Platform & Infrastructure** (San Mateo) — 6 sub-section labels packed into a single paragraph (`Customer & sales engagement: … Productize and deliver Skydio On-Prem: … Drive compliance and certification programs (FedRAMP, CJIS, and other regulatory frameworks): … Release & expectation management: … Compliance enablement: … Evangelize & enable: …`). Reads as a wall of bolded labels with no whitespace between sub-topics.
- **Staff Product Manager, Platform & Infrastructure** (San Mateo) — Same authoring pattern as above (and same content). Both also have 6 empty paragraphs, which makes the spacing erratic.
- **Senior Engineering Manager, Infrastructure** (San Mateo) — Inline `<strong>` labels inside a single bullet preface (`Site-Reliability Engineering:`, `Observability:`, `Software Deployment Lifecycle:`, `Cloud-to-Drone Infrastructure:`) where elsewhere each would be its own section header.

### 3.11 `Location` callout — 12 postings, 4 spellings, ad-hoc placement

Some postings have an explicit Location section because the role has special location requirements. There is no standard convention:

| Label | Postings |
|---|---|
| Location | Sr Director PM DFR; Field Support Rep (Southwest); Manager, Technical Support; CSM, DFR Majors - Southeast; Program Manager, Commercial Programs; GTM Enablement Associate; Senior RevOps Manager |
| Location Preference | Sr Customer Support Rep - India; Sr Tech Support Rep - Japan; CSM, DFR Mid-Market - Northeast; Deployment Engineer - Southeast |
| Work Location | Staff Software Engineer, Frontend |
| Work location | (`<h2>` variant inside Sr Wireless SW Eng — different than Frontend's Title Case) |

In addition, **Field Support Representative** has its Location section inline in the body text rather than as a separate labeled paragraph — same role, two different presentations.

### 3.12 Job-title field formatting (rendered in the page subtitle)

Four titles have a double space after a comma in the title itself, which is visible on the page subtitle:

- "Senior Software Engineer,  Infrastructure" (San Mateo)
- "Senior Software Engineer,  Data Platform" (San Mateo)
- "Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM" (US Remote)
- "Staff Global Supply Manager,  Mechanicals" (San Mateo)

The other 109 titles use single-space commas.

### 3.13 Preamble (Skydio elevator pitch)

**Consistent across all 113 postings.** Every job opens with a paragraph beginning *"Skydio is the leading US drone company …"*. Different roles use one of two slight variants but always lead with this preamble paragraph.

---

## 4. Postings that stand out as different from the norm

If a reader were to skim the listing, these postings would visually catch the eye for the wrong reasons. Listed in rough order of how strongly they deviate from the baseline:

| # | Posting | Why it stands out |
|---|---|---|
| 1 | **Senior Technical Support Representative - Japan** (Tokyo) | Uses `<h1>` for every section header, which renders at approximately the same size as the job title itself — the largest visual deviation in the listing. |
| 2 | **Hardware Engineering Program Manager** (San Mateo) | Mixes `<h2>` top-level with `<h3>` sub-headings, creating a 3-tier visual hierarchy other postings don't have. |
| 3 | **GTM Engineer, Pre-Sales** (US CA San Mateo) | Same `<h2>`+`<h3>` mix as Hardware Eng PM; also the longest pre-comp body in the listing (876 words). |
| 4 | **Senior Product Manager / Staff Product Manager, Platform & Infrastructure** (San Mateo) | Body collapsed into a long single-paragraph wall of inline `<strong>` labels, plus 6 empty paragraphs each. Heaviest spacing irregularity in the listing. |
| 5 | **Software Engineer - Autonomy Infrastructure / Cloud Simulation / Simulation & Robotics** (4 postings) | Use Title-Case section labels ("About the Role:", "Areas of Responsibility:", "What You'll Do:", "Qualifications:", "Bonus Experience:") rendered as semantic `<h2>` or `<h3>`. They look like a *different template* from the other Autonomy postings they appear next to in the listing. |
| 6 | **Director, Global Supply Management - Mechanicals** (San Mateo) | No bullet list anywhere in the pre-comp body — only prose paragraphs. Reads as plain text vs the bulleted norm. |
| 7 | **Manager, Logistics** (Hayward) | Only posting with an inline `style="…"` override (`min-height:1.2em`) — inserts an extra hard-coded vertical gap. |
| 8 | **Revenue Operations Engineer, Quoting Systems** (San Mateo) | Mixes `<h2>` section headers with all-caps acronym `<strong>` labels (`CRM/CPQ:`, `CLM:`, `ERP:`, `PLM:`), plus uses `Tech stack you'll work with:` and `Reporting & Working Model:` headers found nowhere else in the listing. |
| 9 | **Senior Engineering Manager, Infrastructure** (San Mateo) | Inline `<strong>Site-Reliability Engineering:</strong>`, `<strong>Observability:</strong>`, etc. labels packed into one paragraph rather than separated headers. |
| 10 | **IT Technician (Help Desk - Linux Focus)** (Hayward) | 9 `<br>` tags in the pre-comp body — by far the most line-break-driven layout. |
| 11 | **Director, Growth Marketing - Commercial** (San Mateo) | 8 `<br>` tags plus the only `<em>` italic in the body. |
| 12 | **Senior People Analytics Analyst** (San Mateo) | Body typo "What Makes Your a Good Fit" (should be "You"). |
| 13 | **Product Support Engineer / Product Support Engineer Intern** (San Mateo) | Both use `About the role :` and `Location :` with a stray space before the colon. |
| 14 | **Senior NPI Product Quality Engineer** (San Mateo) | Only italic outside of Director Growth Marketing. |
| 15 | **Field Support Representative (Southwest, Remote)** | Embeds the Location requirement inline in the impact-section header rather than its own section, breaking the section-label convention. |

---

## 5. Recommendations — how to standardize

These are ordered from highest impact / lowest cost to highest cost.

1. **Lock the section-header markup to `<p><strong>Label:</strong></p>`.** Strip any `<h1>`–`<h6>` from job postings before they go live, or rewrite the Skydio careers template's `prose` CSS so `<h2>`/`<h3>` inside `.block-content` collapse to the same body-bold treatment. This single change fixes the visual size mismatch on the 18 postings that currently jump out, including the Tokyo posting that uses `<h1>`.

2. **Adopt one canonical wording per section, in sentence case, with a trailing colon, and ASCII apostrophes.** Recommended labels:
   - `About the role:` (use `About the team:` only when there is a *separate* team section in addition to the role)
   - `How you'll make an impact:`
   - `What makes you a good fit:`
   - `Bonus points:` (retire all 13 trailing-skills variants — pick one)
   - `Location:` (retire `Location Preference`, `Work Location`, `Work location`)

   Build a templated, validated authoring form in the ATS so a recruiter physically cannot save a draft until the three required section labels match the canonical strings.

3. **Reject empty `<p></p>` paragraphs and trailing `<br>` tags at ingest.** A simple HTML-sanitization pass in the careers ingest pipeline can remove `<p>(\s|&nbsp;)*</p>` and `<br>\s*</p>` patterns. This alone normalizes spacing on ~70 postings.

4. **Strip inline `style="…"` attributes.** Only one posting has one today, but allowing them means the site's spacing tokens can be silently overridden. The sanitization pass should drop `style` attributes on every element inside `.block-content`.

5. **Disallow inline section labels.** Any `<strong>X:</strong>` followed by sentence text in the same `<p>` should be promoted to its own `<p><strong>X:</strong></p>` line. This fixes the "wall of bold" rendering on the two Platform & Infrastructure PM postings and on the Sr Engineering Manager (Infrastructure) posting.

6. **Require a bullet list under each "How you'll make an impact" and "What makes you a good fit" section.** Director, Global Supply Management - Mechanicals is the only role with no bullets — bringing it inline with the rest of the listing is a content fix, not a CSS fix.

7. **Standardize the trailing-bonus section name to one term and one HTML pattern.** Today there are 14 surface forms ("Bonus points for", "Nice-to-Haves", "Useful skills and experience", etc.). Pick one — recommend `Bonus points:` for sentence-case, body-bold paragraph — and migrate.

8. **Trim double spaces in the job-title field.** The 4 postings with "`, `" → "`,  `" double spaces should be cleaned. This is one regex sweep.

9. **Fix the typo "What Makes Your a Good Fit" → "What Makes You a Good Fit"** in *Senior People Analytics Analyst*.

10. **Avoid `<em>` / `<i>` italic in the role body** (or define and stylize one use-case for italics so the team knows when it's allowed). Today only 2 postings use italics, and both feel accidental.

11. **Add a single linter rule for apostrophes.** Replace smart `'` with ASCII `'` (or vice-versa — pick one) globally inside `.block-content`. This eliminates the 7 postings that mix both within the same page.

12. **Consider promoting "Location" to a structured field** on the page (rendered by the template, like the location subtitle is) instead of an authored section. That gives every location-special role the same look and removes the 4-way Location/Work Location/Location Preference label drift.

---

## 6. Quick-win checklist (a single sanitization pass would fix the bulk)

A one-time HTML cleanup pass run against every existing posting would resolve roughly 80% of the inconsistencies catalogued here without manual rewrites. Suggested transforms:

```text
1.  Replace <h1>…</h1>, <h2>…</h2>, <h3>…</h3> inside .block-content
    with <p><strong>…</strong></p>.
2.  Strip <p></p> and <p>&nbsp;</p>.
3.  Strip trailing <br/> immediately before </p> and </li>.
4.  Strip style="…" on any element under .block-content.
5.  Normalize apostrophes: '   → '   (or vice versa).
6.  Normalize section labels (regex-replace common variants):
       "About the Role" → "About the role"
       "How You'll Make an Impact" / "How You'll Make an Impact"
           / "How you will make an impact" → "How you'll make an impact"
       "What Makes You a Good Fit" / "What Would Make You a Good Fit"
           / "What makes you a strong fit" / "Requirements"
           / "Useful skills and experience" → "What makes you a good fit"
7.  Ensure every section label ends with ":" and has no whitespace before
    the colon.
8.  Collapse runs of 2+ spaces inside the title and body to a single space.
```

The remaining residue (Director GSM Mechanicals' missing bullet list, the two PMP&I postings' wall-of-bold, the Senior People Analytics typo, the few inline-label postings) needs manual content edits and should be triaged to the role owners.

---

## Appendix A — How to reproduce

```bash
# 1. Dump the careers index
curl -sL -A "Mozilla/5.0" https://www.skydio.com/careers -o careers.html

# 2. Extract job URLs (links of form /jobs/<uuid>/?gh_jid=<uuid>)
#    See repo: build jobs.json from anchors with class context "job-listings__title".

# 3. Fetch every posting (113 unique URLs)
#    curl -sL <url> -o jobs/<uuid>.html for each

# 4. For each posting, isolate the body:
#    <div class="prose block-content"> … </div> </stack-l>
#    and truncate at the first <strong>Compensation</strong> match.

# 5. Inspect:
#    - tag counts (h1..h6, p, li, br, strong, em, span)
#    - section-marker text (text inside <p><strong>X</strong></p>)
#    - inline style attributes
#    - empty <p> elements
#    - bullet wrapper pattern (<li><p>...</p></li> vs <li>...</li>)
```

The two supporting data files in this repo capture the result of those steps:

```1:5:job-posting-formatting-summary.csv
title,location,url,section_header_style,about_label,impact_label,fit_label,word_count,li_total,ul_count,empty_paragraphs,br_tags,inline_styles,em_or_i_count,preamble_present
```

`job-posting-formatting-analysis.json` contains the full structural fingerprint per posting (tag counts, all section markers, headings list, inline styles, etc.) for any deeper drill-downs the team needs.

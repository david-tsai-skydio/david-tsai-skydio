# Skydio Careers — Job Posting Formatting Audit

**Source:** <https://www.skydio.com/careers> (and the linked `/jobs/<id>/`
detail pages)
**Snapshot date:** 2026-05-13 (UTC)
**Postings analyzed:** 112 unique job postings (the careers page lists 113
tiles; one role appears twice with two locations but resolves to the same
job ID, so de-duped count is 112)
**Scope of analysis:** body text from the start of the posting up to (but
not including) the **Compensation:** block. The compensation paragraph,
EEO/diversity boilerplate, E‑Verify line, and `#LI-…` tag are excluded.

---

## 1. How the page is built (so we know where formatting comes from)

Every `/jobs/<id>/` page renders the body inside a single container:

```
<div class="prose block-content"> … posting markup … </div>
```

`prose` is a Tailwind‑style typography preset, so **font size, font
family, color, line‑height, and paragraph spacing are applied uniformly
by CSS** to every posting. There are **no inline `style="…"` attributes,
no inline `color:`, `font-size:`, or `font-family:` declarations**, and
no `<hr>` or layout overrides anywhere in the 112 bodies.

> Implication: any visual inconsistency a reader sees on the live site
> is driven by **which HTML tags the writer used**, not by stray inline
> CSS. Standardizing the tag set will fix the visual differences.

The remainder of this report inventories the markup choices each writer
made and flags the ones that drift from the dominant pattern.

---

## 2. Headline findings

| # | Issue | Affected postings | Severity |
|---|---|---|---|
| 1 | Section headers built with **`<h2>` / `<h3>`** instead of the dominant `<p><strong>…</strong></p>` style — these render visibly larger and break the visual rhythm | **16 / 112 (14 %)** | High |
| 2 | Section header **wording, casing, colon, and apostrophe style** are all over the map — the canonical trio "About the role / How you'll make an impact / What makes you a good fit" appears in **>30 distinct surface forms** | **~95 / 112 (85 %)** | High |
| 3 | Stray **`<br>` line breaks** scattered through paragraphs (most likely pasted from Word/Docs) | 44 / 112 | Medium |
| 4 | Empty `<p></p>` and `<p>&nbsp;</p>` paragraphs creating extra vertical whitespace | 43 / 112 | Medium |
| 5 | Hard‑coded **non‑breaking spaces (`&nbsp;`)** inside body copy, up to 13 per posting | 26 / 112 | Medium |
| 6 | Mixed **straight (`'`) vs curly (`'`) apostrophes** — sometimes within the same posting | 44 / 112 mixed; 17 straight‑only; 49 smart‑only | Low‑Medium |
| 7 | **Trailing whitespace inside the `<h1>` job title** | 9 / 112 | Low |
| 8 | One posting has a **double space in the title** (`"Senior Software Engineer,&nbsp;&nbsp;Data Platform"`) | 1 / 112 | Low |
| 9 | One US‑based posting has **no Compensation block at all** (likely missing required CA pay‑range disclosure) | 1 / 112 | High (legal) |
| 10 | A few postings use a **bolded "lead‑in" pattern inside bullets** (`<li><strong>Action verb</strong> rest of sentence</li>`) that nobody else uses | 15 / 112 | Low |

The rest of this report explains each item with concrete examples and
the postings that exhibit it.

---

## 3. The "norm" — what the typical Skydio posting looks like

After scanning all 112 postings, the dominant template is:

1. **Title** in `<h1 class="type-h2">` — e.g. `"Autonomy Engineer - Deep Learning"`.
2. **Location/employment line** in `<p class="type-body-2">` — e.g.
   `"San Mateo, California, United States - Full-time"`.
3. **Boilerplate Skydio intro paragraph** opening with
   `"Skydio is the leading US drone company and the world leader in
   autonomous flight…"` — present in **112/112** postings (perfect
   compliance).
4. Three section headers, each rendered as `<p><strong>…</strong></p>`:
   - `About the role:`
   - `How you'll make an impact:`
   - `What makes you a good fit:`
5. Bullets rendered as `<ul><li><p>…</p></li></ul>` (every one of the
   1,816 bullet items in the corpus uses this nested structure — 0 use
   the plain `<li>…</li>` form, which is excellent consistency).
6. **Compensation:** block, then the EEO + E‑Verify boilerplate.

99/112 postings use the `<p><strong>…</strong></p>` header style.
99/112 postings use `<li><p>…</p></li>` for bullets. So the structural
"chassis" is in great shape — the inconsistencies are on top of it.

Body length is also fairly tight: median **3,190 characters** of plain
text in the pre‑compensation block (p25 = 2,588; p75 = 3,893; full range
1,539 – 5,713).

---

## 4. Issue #1 — `<h2>`/`<h3>` headers in 16 postings (HIGH)

These postings use real heading tags inside the rich‑text body, which
the `prose` CSS renders **substantially larger and bolder** than the
`<p><strong>` headers used in the other 96. Several of them also **mix
both styles within the same posting**, so a reader sees two distinct
header sizes side by side.

| Posting | Style | Headers found |
|---|---|---|
| Software Engineer - Autonomy Infrastructure, Systems and Tools (San Mateo) | `<h2>` × 5 | About the Role: / Areas of Responsibility: / What You'll Do: / Qualifications: / Bonus Experience: |
| Software Engineer - Autonomy Infrastructure, Systems and Tools (Zurich) | `<h2>` × 5 | (same as above) |
| Software Engineer - Cloud Simulation & Full-Stack (San Mateo) | `<h2>` × 5 | (same as above) |
| Software Engineer - Cloud Simulation & Full-Stack (Zurich) | `<h2>` × 5 | (same as above) |
| Software Engineer - Simulation & Robotics Engineer (San Mateo) | `<h3>` × 5 | (same as above) |
| Software Engineer - Simulation & Robotics Engineer (Zurich) | `<h3>` × 5 | (same as above) |
| Communications Manager (US Remote) | `<h2>` × 3 | About the role / How you'll make an impact / What makes you a good fit |
| Aviation Compliance Lead (San Mateo) | `<h2>` × 3 | About the Role / How You'll Make an Impact / What Makes You a Good Fit |
| Aviation Regulatory Program Manager (US Remote) | `<h2>` × 3 | About the Role / How You'll Make an Impact / What Makes You a Good Fit |
| Deployment Coordinator (US Remote) | `<h2>` × 4 | About the Role / How You'll Make an Impact / What Makes You a Good Fit / Why This Role is Unique |
| Senior Buyer (Hayward) | **mixed** `<p><strong>` × 1 + `<h2>` × 2 | About the role: / How you will make an impact: / What makes you a strong fit: |
| Project Manager, Workplace (San Mateo) | **mixed** `<p><strong>` × 6 + `<h3>` × 2 | About the Role / You will be part of: / 4 sub‑sections |
| Field Marketing Event Manager (San Mateo) | **mixed** `<p><strong>` × 3 + `<h3>` × 7 | About the Role: / How You'll Make an Impact: / 3 sub‑sections / What Makes You a Good Fit: |
| Revenue Operations Engineer, Quoting Systems (San Mateo) | **mixed** `<p><strong>` × 1 + `<h2>` × 5 | About the Role: / What you'll drive (scope): / Day-to-day responsibilities: / Tech stack you'll work with: / What you'll bring: / Reporting & Working Model: |
| Senior Business Operations Manager (San Mateo) | **mixed** `<p><strong>` × 3 + `<h3>` × 3 | About the Role: / How you'll make an impact: / 3 sub‑sections / What makes you a good fit: |
| PhD Autonomy Engineer Intern - Planning & Controls (RL) (Zurich) | **mixed** `<p><strong>` × 2 + `<h3>` × 3 | About the role: / How you'll make an impact: / What makes this internship different: / What makes you a strong fit: / Nice-to-Haves: |

**Why it matters:** on the rendered page these `<h2>` headers look like
mini‑titles (close in weight to the job title itself) while every other
posting's section headers look like normal bolded body text. Readers
moving from one posting to the next perceive Skydio as visually
inconsistent.

**Fix:** convert all 16 of these to the dominant
`<p><strong>Header:</strong></p>` form (or, alternatively, migrate
*every* posting to `<h2>` — but doing it on the 16 outliers is
cheaper).

---

## 5. Issue #2 — Section header wording, casing, colons, and apostrophes (HIGH)

The "About the role / How you'll make an impact / What makes you a good
fit" trio is the de‑facto template. It exists in many surface forms.

### 5a. Most common headers across all 112 postings

| Count | Header text |
|---|---|
| 52 | `What makes you a good fit:` |
| 46 | `About the role:` |
| 35 | `How you'll make an impact:` (straight apostrophe) |
| 29 | `About the Role:` |
| 20 | `How You'll Make an Impact:` (Title Case, smart apostrophe) |
| 19 | `What Makes You a Good Fit:` |
| 12 | `How you'll make an impact:` (lowercase, smart apostrophe) |
|  6 | `About the Role` (Title Case, **no colon**) |
|  6 | `About the Team:` |
|  6 | `Areas of Responsibility:` (only used by the 4 SWE Autonomy/Cloud postings) |
|  6 | `What You'll Do:` (only used by those same 4 SWE postings) |
|  6 | `Qualifications:` (only used by those same 4 SWE postings) |
|  6 | `Bonus Experience:` (only used by those same 4 SWE postings) |
|  5 | `About the team:` |
|  5 | `What would make you a good fit:` |
|  4 | `What makes you a strong fit:` |
|  4 | `Bonus points for:` |
|  4 | `What Makes You a Good Fit` (no colon) |
|  3 | `How you will make an impact:` (no contraction) |
|  3 | `Bonus Points:` |
|  3 | `Bonus points:` |
|  3 | `What Makes You A Good Fit:` ("A" capitalized) |
|  3 | `How You'll Make an Impact` (no colon) |

### 5b. Specific inconsistencies extracted from the data

- **Sentence case vs. Title Case** — both are widespread:
  - `About the role:` (46) vs `About the Role:` (29) vs `About the Role` (6)
  - `How you'll make an impact:` (47 lower) vs `How You'll Make an Impact:` (20 Title) vs 3 with no colon
  - `What makes you a good fit:` (52) vs `What Makes You a Good Fit:` (19)
- **Trailing colon present in 308 headers but missing in 55** (the
  no‑colon variant is concentrated in 21 postings, mostly the
  `<h2>`‑style postings listed in §4 plus a handful of others such as
  `Project Manager, Workplace` and `Communications Manager`).
- **Apostrophe glyph in "How you'll make an impact" / "What you'll
  drive" headers** — straight `'` in **39** headers, smart `'` in
  **50**, none/dropped in **3**. Some postings even contain *both*
  glyphs in the same body (44 postings have mixed apostrophes).
- **"Good fit" vs "Strong fit" vs "Would make you a good fit"** —
  three different phrasings for the same section (4 + 3 + 5 + 3 = 15
  postings using a non‑canonical phrasing).
- **"Bonus / Nice‑to‑Have" header** — 8 distinct variants in just 22
  postings: `Bonus Experience:` (6), `Bonus points for:` (4), `Bonus
  Points:` (3), `Bonus points:` (3), `Nice To Haves:` (2), `Nice to
  have:` (2), `Nice-to-Haves:` (1), `Nice to Have` (1).
- Only **16 of 112 postings** match the strict template
  `{About the role: / How you'll make an impact: / What makes you a
  good fit:}` exactly (sentence case + colons + straight apostrophe).
  Another 16 match the strict Title‑Case smart‑apostrophe variant.

**Fix:** pick *one* canonical surface form per header and run a
find‑and‑replace across the source CMS (Greenhouse → Skydio site syncs
through Sanity). My recommendation is **sentence case + trailing colon
+ straight apostrophe**, because that's already the single most
frequent variant and matches the "About the role:" majority.

---

## 6. Issue #3 — Stray `<br>` tags (MEDIUM)

113 stray `<br>` tags appear inside paragraphs of 44 postings. These
typically come from a Word/Google Docs paste and create irregular
in‑paragraph line breaks that don't appear in the surrounding 68
postings.

Worst offenders:

| `<br>` count | Posting |
|---|---|
| 8 | Autonomy Engineer - Deep Learning Infrastructure (San Mateo) |
| 8 | IT Technician (Help Desk - Linux Focus) |
| 8 | Director, Growth Marketing - Commercial |
| 6 | Autonomy Engineer - Deep Learning Infrastructure (Zurich) |
| 6 | Autonomy Engineer - Deep Learning Model Acceleration (Zurich) |
| 6 | Autonomy Engineer - Deep Learning Model Acceleration (San Mateo) |
| 4 | Autonomy Software Engineer |
| 4 | Director of Product Management, DFR |
| 4 | Software Engineer Intern Fall 2026/Winter 2027 |
| 4 | Revenue Operations Engineer, Quoting Systems |

**Fix:** delete `<br>` tags inside `<p>`; keep only the paragraph
breaks the writer intended.

---

## 7. Issue #4 — Empty paragraphs (MEDIUM)

43 postings contain at least one `<p></p>` or `<p>&nbsp;</p>`. They
read as a single extra blank line on the rendered page, making those
postings look more loosely spaced than the rest.

Worst offenders:

| Empty `<p>` | Posting |
|---|---|
| 5 | Senior Product Manager, Platform & Infrastructure |
| 5 | Staff Product Manager, Platform & Infrastructure |
| 4 | Deployment Engineer - Southeast |
| 3 | Senior Autonomy Engineer - Data Curation |
| 3 | Senior Software Engineer - Mobile Platform |
| 3 | Senior/Staff Embedded Software Engineer – Camera Systems |
| 3 | Sr/Staff Embedded Software Engineer - Camera Systems |
| 3 | Deployment Coordinator |

(Note also the **dash inconsistency** between the two embedded camera
roles: one uses an em‑dash `–` and the other uses a hyphen `-` in the
same job title.)

**Fix:** strip empty paragraphs in the CMS save filter.

---

## 8. Issue #5 — Hard‑coded `&nbsp;` (MEDIUM)

70 non‑breaking spaces appear in 26 postings. Most are inside body
copy where a regular space would be correct; they tend to ride along
with `<br>` as Word‑paste residue.

Worst offenders:

| `&nbsp;` count | Posting |
|---|---|
| 13 | Field Support Representative (Southwest, Remote) |
|  9 | Senior Staff Product Manager, Drone Hardware Platforms & Sensors |
|  6 | Customer Success Manager, DFR Majors - Northeast |
|  5 | Director of Product Management, DFR |
|  5 | Technical Support Specialist - West Coast |
|  4 | Senior Wireless Systems Performance Engineer |
|  3 | Senior Software Engineer - Embedded |
|  3 | Software Engineer - Embedded |
|  3 | Staff Software Engineer - Embedded |

**Fix:** replace `&nbsp;` with regular spaces in the CMS save filter
unless the writer deliberately wanted a non‑breaking pair (rare in
prose).

---

## 9. Issue #6 — Mixed straight vs curly apostrophes (LOW‑MEDIUM)

Of the 112 postings:

- **49** use only smart quotes (`' '`)
- **17** use only straight quotes (`' '`)
- **44** **mix both within the same posting**
- 2 contain neither

This is the source of the "you'll" vs "you'll" inconsistency in
section headers (§5b).

**Fix:** decide on a house style (smart quotes are typographically
preferred for body copy) and run a one‑shot conversion. The CMS save
filter can then auto‑smart‑quote on save.

---

## 10. Issue #7 — Trailing whitespace inside `<h1>` titles (LOW)

Nine postings have a stray space at the end of the `<h1>` text node.
It does not produce a visible character, but it can leak into
breadcrumbs, browser tabs, OG/Twitter previews, ATS exports, and
underline/hover decorations.

| Posting (raw `<h1>` content) |
|---|
| `Autonomy Engineer - ML & DL Infrastructure ` |
| `Senior Autonomy Engineer - Controls ` |
| `Senior Autonomy Engineer - Data Curation ` |
| `Electrical Engineer (all levels) ` |
| `Senior Software Engineer - Embedded ` |
| `Senior Software Engineer - Mobile Platform ` |
| `Senior Software Engineer,  Data Platform ` |
| `Field Support Representative ` |
| `Success Systems Specialist ` |

**Bonus catch:** `Senior Software Engineer,  Data Platform` has a
**double space after the comma** in addition to the trailing space.

**Fix:** trim title strings on save.

---

## 11. Issue #8 — One US posting is missing the Compensation block (HIGH / legal)

The compensation paragraph (and the legally required California pay
range) is present on **107 / 112** postings. Of the 5 missing it:

| Posting | Location | Why it matters |
|---|---|---|
| Autonomy Engineer Intern - Deep Learning (Computational Photography) | **San Mateo, CA — Intern** | **California‑based role with no pay range — likely a CA SB 1162 disclosure miss.** |
| Autonomy Engineer Intern - Deep Learning (Computational Photography) | Zurich, Switzerland — Intern | Non‑US, expected |
| Senior Technical Support Representative - Japan | Tokyo, Japan | Non‑US, expected |
| Workplace Experience Coordinator Part-Time | Zurich, Switzerland | Non‑US, expected |
| Supplier Quality Engineer, Sustaining | Taiwan | Non‑US, expected |

**Fix (urgent):** add a compensation block with the pay range to the
San Mateo intern posting before the next refresh.

---

## 12. Issue #9 — Postings with no detected section headers (LOW)

Three postings render as walls of paragraphs with no bolded section
headers at all (no `<p><strong>…</strong></p>`, no `<h*>`):

- Product Support Engineer (San Mateo)
- Product Support Engineer Intern (San Mateo)
- Senior Technical Support Representative - Japan (Tokyo)

These postings have plain‑text labels like `About the Role:` typed
*inline* in regular paragraph text instead of being bolded. On the
live site they read as one undifferentiated block of body copy.

**Fix:** wrap the in‑text labels in `<p><strong>…</strong></p>` to
match every other posting.

---

## 13. Issue #10 — Bolded "lead‑in" pattern inside bullets (LOW)

15 postings use a stylistic pattern where each bullet starts with a
bolded action phrase, for example:

> *<li><p><strong>Design and build robust replay and analysis
> systems</strong> that enable engineers to inspect and reproduce
> recorded autonomy behavior…</p></li>*

The other 97 postings do not bold the lead‑in. This is not wrong, but
it makes those 15 postings look stylistically distinct (and is heavily
correlated with the same 15 postings that also use `<h2>`/`<h3>`
section headers — see §4).

Worst offenders:

| Bolded lead‑ins | Posting |
|---|---|
| 16 | Revenue Operations Engineer, Quoting Systems |
| 11 | GTM Data Engineer Intern |
| 10 | Project Manager, Workplace |
|  9 | Senior Product Manager, Platform & Infrastructure |
|  9 | Staff Product Manager, Platform & Infrastructure |
|  8 | PhD Autonomy Engineer Intern - Planning & Controls (RL) |
|  6 | Software Engineer - Simulation & Robotics Engineer (San Mateo) |
|  6 | Software Engineer - Simulation & Robotics Engineer (Zurich) |
|  6 | Senior People Analytics Analyst |
|  6 | Hardware Operations Program Manager |

**Decision required:** either adopt the bolded‑lead‑in pattern across
all postings (it does aid scannability) or remove it from these 15.

---

## 14. Recommendations (prioritized for implementation)

### A. Standardize the markup chassis (quick wins)

These are mechanical edits that can be done in one pass over the
Greenhouse/Sanity content:

1. **Convert `<h2>` and `<h3>` section headers to
   `<p><strong>Header:</strong></p>`** in the 16 postings listed in §4.
   Single biggest visual win.
2. **Strip `<br>` inside `<p>`** across all 44 affected postings (§6).
3. **Remove `<p></p>` and `<p>&nbsp;</p>`** across all 43 affected
   postings (§7).
4. **Replace `&nbsp;` with a normal space** in body copy (§8).
5. **Trim trailing whitespace and collapse double spaces in
   `<h1>` titles** (§10).
6. **Add the missing Compensation block** to *Autonomy Engineer Intern -
   Deep Learning (Computational Photography) — San Mateo* (§11) —
   urgent for CA SB 1162 compliance.
7. **Wrap inline section labels in `<p><strong>…</strong></p>`** for
   the three Customer‑Support postings in §12.

All seven items can be enforced going forward by a CMS save filter
(strip `<br>` inside `<p>`, drop empty `<p>`, normalize `&nbsp;`,
trim/collapse whitespace in `<h1>`).

### B. Standardize wording (style guide)

Adopt one canonical surface form for each section header and update
the recruiter content templates accordingly. Suggested house style
(matches the most common variant):

| Use | Don't use |
|---|---|
| `About the role:` | `About the Role:` / `About the Role` / `About the Team:` (use only if literally about the team) |
| `How you'll make an impact:` (straight apostrophe, sentence case, colon) | `How You'll Make an Impact` / `How you will make an impact:` |
| `What makes you a good fit:` | `What Makes You a Good Fit` / `What makes you a strong fit:` / `What would make you a good fit:` |
| `Bonus points:` | `Bonus Experience:` / `Nice-to-Haves:` / `Nice To Haves:` / `Nice to have:` |

Pick a single apostrophe glyph (smart `'` is the more typographically
correct default but straight `'` is currently the more common one in
this corpus — either is fine, just pick one) and apply it consistently
in headers and body copy.

### C. Decide on the bullet "lead‑in" pattern (§13)

Either:
- adopt `<p><strong>Action verb …</strong> rest of sentence</p>` as
  the standard for every bullet under "How you'll make an impact:"
  (good for scannability), **or**
- remove the bolded lead‑in from the 15 postings that currently use
  it.

Consistency matters more than which option you pick.

### D. Add a recruiter template + lint check

Most of these issues can be eliminated upstream:

- Provide recruiters a Google Doc / Greenhouse template with the
  canonical section headers pre‑filled.
- Add a pre‑publish lint script (the analyzer used to produce this
  report — `analyze.py` in this directory — does most of what's
  needed) that flags any posting with `<h2>`/`<h3>` body headers,
  stray `<br>`, empty `<p>`, missing compensation block, or trailing
  title whitespace before it goes live.

---

## 15. Reproducibility

The data and the analyzer used to produce this report are checked in
alongside it:

- `analyze.py` — extracts the pre‑compensation body from each posting
  and tabulates the formatting features.
- `data/index.json` — the 112 unique postings (UUID, title, location)
  scraped from <https://www.skydio.com/careers> on 2026‑05‑13.
- `data/analysis.json` — full per‑job feature dump.
- `data/per_job.csv` — flat, spreadsheet‑friendly per‑job table
  (columns: `title, loc, header_style, header_count, has_h_tag,
  mixes_header_styles, br, nbsp, empty_p, li_bold_leadin, pre_chars,
  title_trailing_ws, has_comp_block, headers, uuid`). Open in Sheets
  to filter and sort the outliers.

To re‑run on a fresh snapshot:

```bash
mkdir -p /tmp/jobs/raw && cd /tmp/jobs
curl -sL https://www.skydio.com/careers -o careers.html
# then extract /jobs/<uuid>/ links from careers.html, fetch each,
# and run: python3 analyze.py
```

---

## 16. Appendix — full per‑job feature table

See `data/per_job.csv` for all 112 rows. The columns most useful for
a quick scan:

- `header_style` — `p_strong` (norm), `h2`, `h3`, or `NONE`.
- `mixes_header_styles` — `True` if the posting contains both
  `<p><strong>` and `<h*>` headers (the worst kind of inconsistency
  because it's visible **within a single posting**).
- `br`, `nbsp`, `empty_p` — counts of stray legacy markup.
- `li_bold_leadin` — bullets that start with a `<strong>` lead‑in.
- `headers` — pipe‑separated list of section headers in document
  order, useful for spotting wording drift at a glance.

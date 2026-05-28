# Skydio Careers – Job Posting Formatting Audit

**Source:** https://www.skydio.com/careers (live, fetched 2026-05-28)
**Scope:** 113 active job postings.  Each posting was analyzed from the start
of its job-description body up to (and **not** including) the "Compensation
Range" block. The closing EEO boilerplate and `#LI-XXX` LinkedIn slugs were
also excluded so that every posting is compared on apples-to-apples
pre-compensation content.

**Method.** The careers landing page references each posting as
`/jobs/<uuid>`. All 113 detail pages were fetched and parsed. The visible job
body lives in a single container (`<div class="prose block-content">`), which
inherits site typography from the global "prose" stylesheet. That means there
are no per-job inline font-size, font-family or color overrides in the body
itself — instead, visual inconsistency comes from **structural HTML
differences** (which tag the page uses for headings, lists, line breaks,
etc.). The audit below enumerates those structural choices, since they are
exactly what produces the different rendered sizes, weights, spacing and
hierarchies the team is seeing.

Tooling and raw data ship alongside this report:

- `scripts/fetch_jobs.sh` – download all 113 postings
- `scripts/analyze_jobs.py` – parse + extract formatting signals
- `scripts/summarize.py`, `scripts/extra_checks.py` – aggregate analyses
- `data/job-formatting-by-posting.csv` – one row per posting, all key
  formatting attributes (sortable in Sheets/Excel)
- `data/job-formatting-analysis.json` – the full structured analysis

---

## 1. TL;DR — the inconsistencies that matter most

| # | Issue | Affected | Severity |
|---|-------|----------|----------|
| 1 | **Two completely different heading systems** in use across the site: 96 postings use bold paragraphs as pseudo-headings, 13 use real `<h2>`/`<h3>` tags, 4 use **both**, 4 use **neither** | 113 / 113 | Critical |
| 2 | **22 postings (19.5%) have no compensation block at all** | 22 / 113 | Critical (legal / pay-transparency) |
| 3 | **One posting uses `<h1>` three times inside the body** (collides with the page title `<h1>`) | 1 / 113 | High (a11y) |
| 4 | Section labels (e.g. "About the role") appear in **at least 4 capitalization variants** including one typo (`What Makes Your a Good Fit`) | ~70 / 113 | High |
| 5 | **Heading colon style is mixed** – 81 jobs always use a trailing colon, 1 never does, **14 mix both within the same posting** | 14 / 113 | High |
| 6 | **49 postings (43%) use `<br>` tags** to fake vertical spacing — produces uneven gaps between paragraphs and bullets | 49 / 113 | High |
| 7 | **Apostrophe character is inconsistent** – 37 postings use ASCII `'`, 35 use the curly `’`, and 2 mix both inside the same posting | 74 / 113 | Medium |
| 8 | **`c-link c-link--underline` link class is applied unevenly** – 10 postings have it on every link, 73 have unstyled links, 30 have no links at all → underlined-vs-plain links render differently | 83 / 113 | Medium |
| 9 | **4 job titles contain double-space typos** (e.g. `Senior Software Engineer,  Infrastructure`) | 4 / 113 | Low (but visible on cards) |
| 10 | **8 postings use `<u>` underline**, 3 use `<em>`/`<i>` italic, 1 has a stray inline `style=""` attribute, 1 posting (Director, Global Supply Management – Mechanicals) has **no bullet lists at all** | up to 13 / 113 | Low–Medium |

Word-count range across pre-comp content: **229 → 871 words** (≈ 3.8× spread),
with no clear correlation to seniority. Section counts range from 0 → 8.

---

## 2. Why postings *look* different (the root cause)

Every page wraps the job description in `<div class="prose block-content">`,
which means the visible **font family, base font size, base line-height and
color are inherited globally** from the `.prose` stylesheet. We did **not**
find any per-job inline `font-size`, `font-family` or `color` overrides in the
body (only one stray `style="min-height:1.2em;margin-top:0;margin-bottom:0"`
on the *Manager, Logistics* posting).

So when the team sees "this one has a bigger heading" or "this one's text is
spaced differently," it's not coming from CSS overrides — it's coming from
**which HTML tag is rendering the content**:

| What you see | What's in the HTML |
|---|---|
| A clearly larger / bolder section heading | A real `<h2>` or `<h3>` tag (13 jobs do this) |
| A subtle bold line that sits flush with paragraph text | A `<p><strong>…</strong></p>` "pseudo-heading" (96 jobs do this) |
| Bullets with extra vertical padding | `<li><p>…</p></li>` (every posting uses this Greenhouse pattern — at least it's consistent) |
| Random tall gaps between paragraphs | Stray `<br>` tags (49 jobs have between 1 and 9 each) |
| Underlined links | The `c-link c-link--underline` class is present (10 jobs) |
| Plain links | No class, just bare `<a>` (73 jobs) |
| A heading that's a different size from the others on the *same* page | The posting mixes `<h2>` with `<p><strong>` (4 jobs) |

Because `<h2>`/`<h3>` and `<p><strong>` are styled completely differently by
the `.prose` rules, side-by-side postings can read like they came from two
different brands.

---

## 3. Heading hierarchy — the biggest source of visual inconsistency

### 3a. Four different heading strategies are in use

| Strategy | Count | Behavior |
|---|---:|---|
| Only `<p><strong>…</strong></p>` pseudo-headings | **92** | Subtle bold lines that look like regular text |
| Only real `<h2>` and/or `<h3>` | **13** | Properly large, bold, visually distinct headings |
| **Both** real `<h*>` and pseudo-headings in the same posting | **4** | Two heading sizes inside one job → visually broken |
| **Neither** (no headings of any kind) | **4** | A wall of paragraphs/bullets with no section breaks |

The 13 postings that use **real heading tags** look noticeably "bigger and
bolder" than the rest of the site:

- Aviation Compliance Lead (`h2 × 4`)
- Aviation Regulatory Program Manager (`h2 × 3`)
- Communications Manager (`h2 × 3`)
- Full Stack Product Counsel (`h3 × 4`)
- Hardware Engineering Program Manager (`h2 × 3, h3 × 5`)
- Senior Wireless Software Engineer, National Security (`h2 × 6`)
- Senior Technical Support Representative – Japan (`h1 × 3`  ← see §3c)
- Software Engineer – Autonomy Infrastructure, Systems and Tools (`h2 × 5`, two listings)
- Software Engineer – Cloud Simulation & Full-Stack (`h2 × 5`, two listings)
- Software Engineer – Simulation & Robotics Engineer (`h3 × 5`, two listings)

The 4 postings that **mix** both heading styles in one body are the most
jarring (one heading suddenly twice the size of the next):

- Revenue Operations Engineer, Quoting Systems – `h2 × 5` + 1 bold-pseudo
- PhD Autonomy Engineer Intern – Planning & Controls (RL) – `h3 × 3` + 2 bold-pseudo
- Senior Business Operations Manager – `h3 × 3` + 3 bold-pseudo
- Senior Buyer – `h2 × 2` + 1 bold-pseudo

The 4 postings with **no headings at all** read as one long block:

- Product Support Engineer
- Product Support Engineer Intern
- PhD Autonomy Engineer Intern – Deep Learning or Computer Vision (San Mateo)
- PhD Autonomy Engineer Intern – Deep Learning or Computer Vision (Zurich)

### 3b. Section-label wording is fragmented

Even within the dominant "bold pseudo-heading" group, the *exact same* section
appears under many different labels.

`About the role` variants:

| Variant | Count |
|---|---:|
| `About the role:` | 47 |
| `About the Role:` | 23 |
| `About the Role` (no colon) | 1 |
| `About The Role` (Title Case, no colon) | 1 |

`How you'll make an impact` variants:

| Variant | Count |
|---|---:|
| `How you'll make an impact:` (ASCII apostrophe) | 38 |
| `How You’ll Make an Impact:` (Title Case, curly `’`) | 20 |
| `How you’ll make an impact:` (sentence case, curly `’`) | 14 |
| `How you will make an impact:` (spelled out) | 3 |
| `How You'll Make an Impact:` (Title Case, ASCII `'`) | 1 |

`What makes you a good fit` variants:

| Variant | Count |
|---|---:|
| `What makes you a good fit:` | 54 |
| `What Makes You a Good Fit:` | 17 |
| `What would make you a good fit:` | 6 |
| `What Would Make You a Good Fit:` | 2 |
| `What makes you a strong fit:` | 2 |
| `What would make you a strong fit:` | 2 |
| **`What Makes Your a Good Fit:`** *(typo — "Your" should be "You")* | **1** |
| `What Makes You a Good Fit` (no colon) | 1 |
| `What makes you a good fit` (no colon) | 1 |
| `What Makes You A Good Fit:` (every-word caps) | 1 |

`Nice to have` variants (5 spellings across 6 jobs):

| Variant | Count |
|---|---:|
| `Nice to have:` | 2 |
| `Nice-to-Haves:` | 1 |
| `Nice to Have` (no colon) | 1 |
| `Nice To Haves` (Title Case, no colon) | 1 |
| `Nice To Haves:` | 1 |

`Bonus points` variants (3 spellings across 10 jobs):

| Variant | Count |
|---|---:|
| `Bonus points for:` | 4 |
| `Bonus Points:` | 3 |
| `Bonus points:` | 3 |

### 3c. Outlier: `<h1>` used inside the job body

**Senior Technical Support Representative – Japan** is the only posting that
uses **`<h1>` three times** inside the body content. The page already has its
own `<h1>` for the job title in the page header, so this posting renders with
4 H1s in the document outline – an accessibility and SEO problem (and visually
this posting's section headings will be noticeably larger than every other
posting on the site).

### 3d. Colon style is mixed inside individual postings

81 jobs always end pseudo-headings with `:`. 1 job (`What Makes You a Good
Fit`) never does. **14 jobs mix both styles** inside the same posting, e.g.:

- *Senior People Analytics Analyst* – colon: `How You’ll Make an Impact:` / no-colon: `About The Role`, `Preferred Qualifications`
- *Customer Success Manager, DFR Mid-Market – Northeast* – colon: `About the Team:` / no-colon: `Requirements`, `Experience & Skills`
- *Success Systems Specialist* – the most extreme: 3 colon headings followed by 3 no-colon headings (`Build Automation & Intelligence into Mission Success`, `Customer Digital Experience`, `Cross-Functional Architecture & Governance`)

### 3e. One-off / outlier section labels

23 section labels appear in only **one** posting and aren't part of the shared
vocabulary. The notable ones:

- `additional desired experience and skills` (Director, Growth Marketing)
- `examples of what you’ll help build` (Senior Software Engineer, Data Platform)
- `experience & skills` (Customer Success Manager, DFR Mid-Market)
- `key responsibilities` (Director, Growth Marketing)
- `nice-to-haves` (one posting only — the rest use 4 other spellings)
- `qualifications` (Workplace Experience Coordinator)
- `scalability & cost avoidance` (Senior Product Manager, Platform & Infrastructure)
- `what success looks like` (Director, Growth Marketing)
- `why join us?` (Senior Software Engineer, Data Platform)
- `why this role matters now` (Success Systems Specialist)
- `work environment` (Senior Wireless Software Engineer, National Security)
- `work location` (Communications Manager)
- **`onsite - 5 days/week, monday - friday: 3:30pm - 12am skydio manufacturing (hayward, ca)`** *(IT Technician (Help Desk – Linux Focus) is using a bold paragraph for a schedule note, treating it as a section heading)*
- The 3 EMEA Enterprise Account Manager postings render the legal location requirement (`This role must be based in Switzerland, Germany, or Finland.`) as a bold-paragraph "heading" instead of body text.

---

## 4. Compensation block: 22 postings have none

Per California / Washington / Colorado / NYC pay-transparency laws, every
posting should disclose a compensation range. **19.5% of the corpus does not.**
Full list:

| Posting | URL |
|---|---|
| Autonomy Engineer - Deep Learning Infrastructure | https://www.skydio.com/jobs/06234e2e-6285-43ce-9ae5-417cbfb85436 |
| Autonomy Engineer - Deep Learning Model Acceleration | https://www.skydio.com/jobs/0aff9e3d-6c59-4463-845c-850b78b48172 |
| Autonomy Engineer - Deep Learning | https://www.skydio.com/jobs/1208ec60-0fb6-4e5d-bf1f-af1312139a84 |
| PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) | https://www.skydio.com/jobs/12590806-3cf0-4bc3-930b-12b53e227a5c |
| Software Engineer - Simulation & Robotics Engineer | https://www.skydio.com/jobs/3193c6ab-27d2-4558-8ad8-1d3a1512ab72 |
| Software Engineer - Autonomy Infrastructure, Systems and Tools | https://www.skydio.com/jobs/49da6783-223e-4b2c-81f6-3b47de1c52e7 |
| Supplier Quality Engineer, Sustaining | https://www.skydio.com/jobs/4c4874bf-02da-4ccc-8918-2cca08feaf21 |
| Senior Autonomy Engineer - Deep Learning | https://www.skydio.com/jobs/4ded3e5e-cdfe-4dc5-bbaf-0d3023521246 |
| Software Engineer - Cloud Simulation & Full-Stack | https://www.skydio.com/jobs/50dad059-b43b-4be1-84ab-2c350a68848f |
| Staff Software Engineer, Frontend | https://www.skydio.com/jobs/54654035-a78a-4e5b-9ebf-ae4067e5a246 |
| Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 | https://www.skydio.com/jobs/611a7f87-bc4c-468f-976f-ecd33b731fa3 |
| Autonomy Engineer - ML & DL Infrastructure | https://www.skydio.com/jobs/7a611e90-4034-4e35-acce-388f48f7d3c0 |
| Autonomy Engineer Intern - Deep Learning (Computational Photography) | https://www.skydio.com/jobs/92a7a891-d332-459c-9aa8-e96afea4f2a4 |
| Systems Integration and Test Engineer (Mid to Senior Level) | https://www.skydio.com/jobs/a1a60b27-53a8-455e-b467-712e01c532dc |
| Aviation Compliance Lead | https://www.skydio.com/jobs/b9f9047b-1555-4978-9bff-70eae58a6b17 |
| Autonomy Engineer Intern Fall 2026 | https://www.skydio.com/jobs/c48dabe8-cb67-4694-aacc-f9ef4d34ae50 |
| PhD Autonomy Engineer Intern - Deep Learning or Computer Vision | https://www.skydio.com/jobs/c783c8dd-f604-47d0-aae0-187af89c81b4 |
| Full Stack Product Counsel | https://www.skydio.com/jobs/c9e40dab-ae7d-4034-a335-b3e05d419672 |
| Workplace Experience Coordinator Part-Time | https://www.skydio.com/jobs/d023afe5-f19f-42f7-a1dd-aa94a361b86f |
| Autonomy Engineer Intern - Deep Learning (Computational Photography) | https://www.skydio.com/jobs/d13e3179-e646-4873-84a6-d492a692bc25 |
| Autonomy Engineer - Planning and Controls | https://www.skydio.com/jobs/d5a3ac9c-7b50-4e51-9600-f3c3105652cd |
| Senior Technical Support Representative - Japan | https://www.skydio.com/jobs/f714e85f-31df-494e-bac4-1dd61d4d6066 |

Pattern: the Zurich/Tampere/Switzerland/Finland-located autonomy roles and
several internship postings consistently omit compensation; a handful of US
roles (e.g. *Aviation Compliance Lead*, *Staff Software Engineer, Frontend*,
*Senior Autonomy Engineer – Deep Learning*) also omit it, which is the
higher-risk subset.

---

## 5. Inline spacing: `<br>` tags faking vertical rhythm

Forty-nine postings (43%) inject one or more `<br>` tags into the
pre-compensation body. Because the `.prose` paragraph styles already give
paragraphs vertical margin, an extra `<br>` produces visibly inconsistent gaps.
The worst offenders:

| `<br>` count | Posting |
|---:|---|
| 9 | IT Technician (Help Desk – Linux Focus) |
| 8 | Director, Growth Marketing – Commercial |
| 8 | Autonomy Engineer – Deep Learning Infrastructure |
| 6 | GTM Engineer, Pre-Sales |
| 6 × 2 | Autonomy Engineer – Deep Learning Model Acceleration (both listings) |
| 6 | Autonomy Engineer – Deep Learning Infrastructure (second listing) |
| 5 | Systems Integration and Test Engineer (Mid to Senior Level) |
| 4 | Software Engineer Intern Fall 2026/Winter 2027 |
| 4 | Senior Technical Recruiter – Hardware Operations |
| 4 | Revenue Operations Engineer, Quoting Systems |
| 4 | Director of Product Management, DFR |
| 4 | Autonomy Software Engineer |

By comparison, the remaining ~64 postings have zero `<br>` and read with the
intended consistent rhythm.

---

## 6. Inline character & style outliers

### 6a. Italic and underline
Italic and underline are not standard for these postings, but appear sporadically:

- **Italic (`<em>` / `<i>`)** – Director, Growth Marketing – Commercial (1×); Senior NPI Product Quality Engineer (1×); **GTM Engineer, Pre-Sales (8×)** ← outlier
- **Underline (`<u>`)** – 8 postings each use it exactly once: Senior Technical Recruiter, Senior NPI Product Quality Engineer, Lead Staff Electrical Engineer, Public Safety Strategist, Senior Software Engineer Full Stack, Senior Technical Recruiter – Hardware Operations, Staff Technical Recruiter, Full Stack Product Counsel.

### 6b. Apostrophe character
Pseudo-headings split almost evenly between ASCII `'` (37 jobs) and curly `’`
(35 jobs). Two postings actually **mix both** in their own headings:

- Senior Software Engineer, Data Platform
- GTM Data Engineer Intern

### 6c. Link styling
`<a>` tags appear in 83 postings. **Ten** of those wrap links in
`<a class="c-link c-link--underline">…`, which renders them underlined; the
other **73** use plain `<a>` tags which inherit only the prose anchor color.
This means clickable text styling is visibly different from posting to
posting.

### 6d. Stray inline style
One posting (`Manager, Logistics`) has a literal
`style="min-height:1.2em;margin-top:0;margin-bottom:0"` attribute on a node —
a pasted-in fragment from Word/Google Docs. No other posting has any inline
`style=""`.

### 6e. List structure
112 of 113 postings use the consistent Greenhouse-style
`<ul><li><p>…</p></li></ul>` pattern. One posting (`Director, Global Supply
Management – Mechanicals`) has **no bullet lists at all** and lists
responsibilities/requirements as run-on paragraphs.

No posting uses an ordered list (`<ol>`). No posting uses emoji, images
(`<img>`) or horizontal rules (`<hr>`) inside the body.

---

## 7. Length variance

| Metric | Min | Median | Max |
|---|---:|---:|---:|
| Word count (pre-compensation) | 229 | ~430 | 871 |

Shortest: *Supply Chain Intern* (229), *Autonomy Engineer – Planning and
Controls* (230), *Electrical Engineer (all levels)* (244). Longest: *GTM
Engineer, Pre-Sales* (871), *Staff Product Manager, Platform & Infrastructure*
(786), *Manager, Technical Support* (780). A ~4× spread is fine across roles
of different complexity, but the **<250-word postings feel "incomplete"** next
to siblings in the same job family — e.g. *Senior Autonomy Engineer – Controls*
(245 words) sits next to *Senior Autonomy Engineer – Deep Learning* (314 / 317
words) and *Engineering Manager – Autonomy* (~530 words).

---

## 8. Title-card typos

The careers landing page renders titles verbatim. Four postings have
**double-space typos** that are visible on the cards:

- `Senior Software Engineer,  Infrastructure`
- `Staff Global Supply Manager,  Mechanicals`
- `Senior Software Engineer,  Data Platform`
- `Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM`

And the title-cased typo on *Senior People Analytics Analyst* should be fixed:
`What Makes Your a Good Fit:` → `What Makes You a Good Fit:`.

---

## 9. Postings that stand out as different from the norm

Ranking the most visually divergent postings (most independent-issue flags
first):

1. **Senior Technical Support Representative – Japan** – the *only* posting
   that injects `<h1>` tags into the body; also missing compensation block.
2. **GTM Engineer, Pre-Sales** – heaviest italic use (8×), 6 `<br>` tags,
   mixes colon and no-colon headings, has the longest body (871 words).
3. **IT Technician (Help Desk – Linux Focus)** – 9 `<br>` tags (most in the
   corpus), uses a bold paragraph for a schedule string as if it were a
   section heading, no-colon variants for `About the Role` and `Nice to Have`.
4. **Director, Growth Marketing – Commercial** – mixes Title-Case and
   sentence-case headings, mixes colon styles, uses italics + 8 `<br>` tags,
   introduces 3 one-off section labels.
5. **Senior People Analytics Analyst** – contains the `What Makes Your a Good
   Fit:` typo, mixes colon styles (`About The Role` no colon, others colon).
6. **Success Systems Specialist** – 3 colon headings followed by 3 no-colon
   headings of completely different wording style.
7. **Senior Wireless Software Engineer, National Security** – uses `<h2> × 6`,
   making it look much "bigger" than nearly every other posting.
8. **Software Engineer – Cloud Simulation & Full-Stack / Simulation &
   Robotics Engineer / Autonomy Infrastructure** (each ×2 locations) – use
   real `<h2>`/`<h3>` instead of pseudo-headings; the corresponding sibling
   Autonomy roles use bold pseudo-headings, so the *same hiring team's*
   postings render differently next to each other.
9. **Director, Global Supply Management – Mechanicals** – the only posting
   without any bullet lists.
10. **Manager, Logistics** – the only posting with a stray inline `style=""`.
11. **The 4 EMEA Autonomy roles in Zurich/Tampere/etc.** – clustered in the
    "no compensation block" outlier group.

---

## 10. Recommendations (in priority order)

### Tier 1 — fix immediately
1. **Pick ONE heading element and standardize.** The 13 jobs using real
   `<h2>`/`<h3>` produce headings ~1.5–2× larger than the 96 jobs using
   `<p><strong>`. Decide whether section headings should be `<h3>` (semantic
   + accessible) or a pseudo-heading, then re-format every posting to match.
   *If you keep `<p><strong>`*, add a Greenhouse linter/save-time check that
   blocks `<h1>`–`<h6>` in the body.
   *If you switch to `<h3>`*, run a one-time pass converting bold-only
   paragraphs to `<h3>` and remove the now-redundant trailing colon.
2. **Eliminate the 14 mixed-colon postings** by removing or adding the
   trailing colon on every bold pseudo-heading so the convention is one or
   the other.
3. **Adopt a fixed section vocabulary** and use it verbatim everywhere.
   Suggested canonical set (sentence case + trailing colon, ASCII apostrophe):
   - `About the role:`
   - `About the team:` (optional)
   - `How you'll make an impact:`
   - `What makes you a good fit:`
   - `Nice to have:` (one and only one spelling)
   - `Bonus points:` (one and only one spelling)
   Find-and-replace the 4 capitalization variants of `About the role`, the 5
   variants of `How you('|’)ll make an impact`, the 10 variants of `What
   makes you a good fit`, the 5 spellings of `Nice to have`, and the 3
   spellings of `Bonus points`.
4. **Fix the typo:** `What Makes Your a Good Fit:` → `What Makes You a Good
   Fit:` (Senior People Analytics Analyst).
5. **Fix the 4 double-space title typos** in Greenhouse:
   `Senior Software Engineer,  Infrastructure`,
   `Senior Software Engineer,  Data Platform`,
   `Staff Global Supply Manager,  Mechanicals`,
   `Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM`.
6. **Add a compensation block to the 22 postings missing one** (full list in
   §4). Pay-transparency exposure for the US-located roles in that group
   (e.g. *Staff Software Engineer, Frontend* – San Mateo; *Aviation
   Compliance Lead* – San Mateo) is material.

### Tier 2 — clean up presentation
7. **Strip every `<br>` from the body.** The `.prose` paragraph margin gives
   correct spacing; `<br>` produces irregular gaps. Highest priority: the 13
   postings with 4+ `<br>` listed in §5.
8. **Remove ad-hoc underline (`<u>`) and italic (`<em>` / `<i>`)** unless
   strictly required (e.g. legal disclosures). Eight underline and three
   italic uses are inconsistent with the rest of the corpus. Pull GTM
   Engineer, Pre-Sales (8 italics) into the style guide review.
9. **Normalize link markup.** Either always apply `c-link c-link--underline`
   to every `<a>` in the body, or remove it from the 10 postings where it
   currently exists. Inconsistent link styling on otherwise-identical body
   copy is visible to candidates.
10. **Standardize the apostrophe character.** ASCII `'` is safest for
    copy/paste and search; convert the 35 postings using `’` (and the 2
    that mix both inside their own headings) when running the heading
    rewrite.
11. **Add bullet lists to the one posting that has none** (*Director, Global
    Supply Management – Mechanicals*) and strip the stray
    `style="min-height:1.2em;…"` on *Manager, Logistics*.

### Tier 3 — process / prevention
12. **Add a Greenhouse template** that pre-fills the canonical section
    headings (`About the role:`, `How you'll make an impact:`, `What makes
    you a good fit:`, `Nice to have:` (optional), `Compensation:`) so future
    postings start from a consistent skeleton.
13. **Add a linter / CI check** that crawls `/careers` and fails the build
    when a posting:
    - has `<h1>`–`<h6>` inside the body (or, conversely, uses anything other
      than `<h3>` if you go the semantic-heading route)
    - mixes colon and no-colon pseudo-headings
    - contains `<br>`, `<u>`, or `<style>`/`style=""` attributes
    - has no `Compensation` section
    - has a section label not in the canonical allow-list
    The `scripts/analyze_jobs.py` in this repo already extracts every signal
    needed and writes JSON/CSV — wiring it into a nightly check is a small
    additional step.
14. **Document a Job-Posting Style Guide** (one page) that codifies tone,
    casing, heading vocabulary, list usage, link styling, and required
    compensation block, and link it from the Greenhouse template description.

---

## Appendix: how to reproduce this audit

```bash
# 1. Pull the live data (downloads ~54MB into /tmp/skydio_jobs)
./scripts/fetch_jobs.sh

# 2. Parse + analyze
python3 scripts/analyze_jobs.py     # writes data/job-formatting-analysis.json
python3 scripts/make_csv.py         # writes data/job-formatting-by-posting.csv

# 3. Print the aggregate summaries used in this report
python3 scripts/summarize.py
python3 scripts/extra_checks.py
```

The CSV at `data/job-formatting-by-posting.csv` is the easiest way to share
findings with the team — open it in Sheets/Excel, filter by
`uses_real_headings = TRUE`, `heading_colon_style = mixed`, `br_count > 0`,
or `found_compensation_block = FALSE` to triage in priority order.

# Skydio Careers — Pre-Compensation Formatting Audit

_Source: `https://api.ashbyhq.com/posting-api/job-board/Skydio?includeCompensation=true` (Ashby job board), pulled live. All listed postings analyzed up to (and not including) the "Compensation" block._

**Postings analyzed:** 110  
**Postings with a detectable Compensation block:** 104 / 110  
**Postings flagged with at least one inconsistency:** 105 (95%)  
**Postings with no detected formatting issues:** 5

**Contents**

1. [Executive summary](#1-executive-summary)
2. [Distribution of section-label styles across postings](#2-distribution-of-section-label-styles-across-postings)
3. [Distribution of list-item structure](#3-distribution-of-list-item-structure)
4. [Flagged postings (pre-compensation content only)](#4-flagged-postings-pre-compensation-content-only)
5. [Postings with no detected issues](#5-postings-with-no-detected-issues)
6. [Recommendations for standardizing pre-compensation content](#6-recommendations-for-standardizing-pre-compensation-content)

## 1. Executive summary

Every posting on `skydio.com/careers` is rendered from HTML stored in Ashby. The Skydio site's CSS gives **all** of these a single uniform look — body text inherits the page font, size, weight, line height, and color from the careers stylesheet. So the only places real visual inconsistencies can creep in are the **HTML structure** of each posting (which tags are used) and any **inline `style=` overrides** writers add inside Ashby's editor.

**The page-wide conventions** (what most postings do):

- **Section labels** are rendered as `<p><strong>Label:</strong></p>` in **85%** of postings (dominant style: `P+STRONG`).
- **Label casing**: **sentencecase** in ~67% of postings.
- **Label colon**: labels end **with** a colon in ~93% of postings.
- **Bulleted list items**: **p-wrapped** (`<li><p>…</p></li>`) in ~97% of postings.
- Every block carries the inline style `style="min-height:1.5em"` (this is Ashby's default and is consistent — not an issue).
- **Standard intro paragraph** ("Skydio is the leading…") opens ~100% of postings.

**Where postings drift from the norm** (most common issues):

- 52× — Contains N empty paragraph(s) (extra vertical gap).
- 45× — Contains N `<br>` tag(s) (line-break instead of paragraph break).
- 28× — Inconsistent label capitalization within the posting (titlecase=N, sentencecase=N).
- 26× — Contains N non-breaking space(s) — likely pasted from a word processor.
- 20× — Section labels use **titlecase** while N% of postings use **sentencecase**.
- 17× — Contains N run(s) of double spaces in body text.
- 16× — Uses real heading tags inside the body (hN=N); the page-wide convention is `<p><strong>` for section labels.
- 15× — Section labels primarily styled as **HN** while N% of postings use **P+STRONG**.
- 13× — Inconsistent label punctuation: N end with `:` and N do not.
- 7× — Uses `<u>` underline (rare across postings; only appears in 'PLEASE NOTE' callouts).
- 5× — Section labels without colons, while N% of postings use labels with colons.
- 4× — Mixes section-label styles within the posting (HN=N, P+STRONG=N).

**Bonus — title-string hygiene** (visible in the careers index):

- `"Electrical Engineer (all levels) "` — leading/trailing whitespace or double space.
- `"Senior Software Engineer - Embedded "` — leading/trailing whitespace or double space.
- `"Senior Software Engineer,  Data Platform "` — leading/trailing whitespace or double space.
- `"Staff Global Supply Manager,  Mechanicals"` — leading/trailing whitespace or double space.
- `"Autonomy Engineer - ML & DL Infrastructure "` — leading/trailing whitespace or double space.
- `"Senior Autonomy Engineer - Data Curation "` — leading/trailing whitespace or double space.
- `"Senior Autonomy Engineer - Controls "` — leading/trailing whitespace or double space.
- `" Electrical Engineer (Sustaining/Validation)"` — leading/trailing whitespace or double space.
- `" Senior Software Engineer,  Infrastructure"` — leading/trailing whitespace or double space.
- `"Success Systems Specialist "` — leading/trailing whitespace or double space.
- `"Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM"` — leading/trailing whitespace or double space.
- `"Senior Software Engineer - Mobile Platform "` — leading/trailing whitespace or double space.
- `" Software Engineer - Infrastructure"` — leading/trailing whitespace or double space.
- `"Field Support Representative "` — leading/trailing whitespace or double space.
- `"Manager, Logistics "` — leading/trailing whitespace or double space.

## 2. Distribution of section-label styles across postings

| Style used for section labels (e.g. "About the role") | Postings |
|---|---|
| `P+STRONG` | 90 |
| `H2` | 7 |
| `mixed within posting` | 5 |
| `(none — flat prose)` | 4 |
| `H3` | 3 |
| `H1` | 1 |

## 3. Distribution of list-item structure

| List-item structure | Postings (with lists) |
|---|---|
| `p-wrapped` | 106 |
| `mixed` | 3 |

_Why this matters visually: a `<li>` whose text is wrapped in `<p>` renders with the page's standard paragraph spacing above and below; a bare `<li>` does not. Mixing these in one page produces visibly uneven gaps between bullets._

## 4. Flagged postings (pre-compensation content only)

Each entry below lists the issues detected in that posting's pre-compensation HTML, with quotes anchored to specific elements where possible.

### Operations

#### Aviation Compliance Lead
_Policy & Regulatory Affairs · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/b9f9047b-1555-4978-9bff-70eae58a6b17)_

- Section-label styles: `H2`=3  
- Heading tags inside body: `h2`=3  
- Lists: 2 `<ul>`, 0 `<ol>`, 15 items  
- Pre-compensation length: 2990 chars across 10 top-level blocks
- Actual labels: `H2` "About the Role", `H2` "How You’ll Make an Impact", `H2` "What Makes You a Good Fit"

**Issues:**

- Section labels primarily styled as **H2** while 85% of postings use **P+STRONG**.
- Uses real heading tags inside the body (h2=3); the page-wide convention is `<p><strong>` for section labels.
- Contains 1 empty paragraph(s) (extra vertical gap).
- Contains 1 `<br>` tag(s) (line-break instead of paragraph break).
- Section labels without colons, while 93% of postings use labels with colons.
- Section labels use **titlecase** while 67% of postings use **sentencecase**.

#### Aviation Regulatory Program Manager
_Policy & Regulatory Affairs · US Remote · [posting](https://jobs.ashbyhq.com/Skydio/d73ae64d-5877-4ab6-ad42-0224702f3fba)_

- Section-label styles: `H2`=3  
- Heading tags inside body: `h2`=3  
- Lists: 2 `<ul>`, 0 `<ol>`, 16 items  
- Pre-compensation length: 3531 chars across 13 top-level blocks
- Actual labels: `H2` "About the Role", `H2` "How You’ll Make an Impact", `H2` "What Makes You a Good Fit"

**Issues:**

- Section labels primarily styled as **H2** while 85% of postings use **P+STRONG**.
- Uses real heading tags inside the body (h2=3); the page-wide convention is `<p><strong>` for section labels.
- Contains 2 empty paragraph(s) (extra vertical gap).
- Section labels without colons, while 93% of postings use labels with colons.
- Section labels use **titlecase** while 67% of postings use **sentencecase**.

#### Communications Manager
_Marketing · US Remote · [posting](https://jobs.ashbyhq.com/Skydio/50567d8d-2903-494f-8e08-7c8ca734dc3a)_

- Section-label styles: `H2`=3  
- Heading tags inside body: `h2`=3  
- Lists: 2 `<ul>`, 0 `<ol>`, 12 items  
- Pre-compensation length: 3112 chars across 10 top-level blocks
- Actual labels: `H2` "About the role", `H2` "How you'll make an impact", `H2` "What makes you a good fit"

**Issues:**

- Section labels primarily styled as **H2** while 85% of postings use **P+STRONG**.
- Uses real heading tags inside the body (h2=3); the page-wide convention is `<p><strong>` for section labels.
- Contains 2 empty paragraph(s) (extra vertical gap).
- Section labels without colons, while 93% of postings use labels with colons.

#### Customer Success Manager, DFR Majors - Northeast
_Professional Services and Training · US Remote · [posting](https://jobs.ashbyhq.com/Skydio/23721f25-7d5f-45fa-a5fe-d58f9680e1ef)_

- Section-label styles: `P+STRONG`=4  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 19 items  
- Pre-compensation length: 3486 chars across 10 top-level blocks
- Actual labels: `P+STRONG` "About the Team:", `P+STRONG` "About the role:", `P+STRONG` "How you’ll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 6 non-breaking space(s) — likely pasted from a word processor.
- Inconsistent label capitalization within the posting (titlecase=1, sentencecase=3).

#### Deployment Engineer - Southeast
_Professional Services and Training · US Remote · [posting](https://jobs.ashbyhq.com/Skydio/6138ba1c-c048-407d-9ea2-7b51a3d38756)_

- Section-label styles: `P+STRONG`=5  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 23 items  
- Pre-compensation length: 4167 chars across 15 top-level blocks
- Actual labels: `P+STRONG` "About the Team:", `P+STRONG` "About the role:", `P+STRONG` "How you’ll make an impact:", `P+STRONG` "What makes you a good fit:", `P+STRONG` "Nice to have:"

**Issues:**

- Contains 3 empty paragraph(s) (extra vertical gap).
- Inconsistent label capitalization within the posting (titlecase=1, sentencecase=4).

#### Director, Global Supply Management - Mechanicals
_Supply Chain & Logistics · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/eb7fbbdb-3346-4f7f-a202-8bfd3441217a)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 0 `<ul>`, 0 `<ol>`, 0 items  
- Pre-compensation length: 4423 chars across 26 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "What you will do:", `P+STRONG` "Desired Qualifications:"

**Issues:**

- Contains 3 empty paragraph(s) (extra vertical gap).
- Contains 4 run(s) of double spaces in body text.
- Inconsistent label capitalization within the posting (titlecase=1, sentencecase=2).

#### Director, Growth Marketing - Commercial
_Marketing · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/00d0bdc5-89ad-4182-8512-ab0a028953f6)_

- Section-label styles: `P+STRONG`=5  
- Heading tags inside body: _(none)_  
- Lists: 6 `<ul>`, 0 `<ol>`, 23 items  
- Pre-compensation length: 4505 chars across 16 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "Key Responsibilities:", `P+STRONG` "What Success Looks Like:", `P+STRONG` "What Would Make You a Good Fit:", `P+STRONG` "Additional Desired Experience and Skills"

**Issues:**

- Contains 3 empty paragraph(s) (extra vertical gap).
- Contains 8 `<br>` tag(s) (line-break instead of paragraph break).
- Contains 1 run(s) of double spaces in body text.
- Inconsistent label punctuation: 4 end with `:` and 1 do not.
- Inconsistent label capitalization within the posting (titlecase=4, sentencecase=1).

#### Enterprise Account Manager (MoD/ MoI) – EMEA (Finland)
_Sales · Tampere, Finland · [posting](https://jobs.ashbyhq.com/Skydio/d6f731e8-c530-4123-8b52-0e7cab164887)_

- Section-label styles: `P+STRONG`=4  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 22 items  
- Pre-compensation length: 4780 chars across 10 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `P+STRONG` "This role must be based in Switzerland, Germany, or Finland.", `P+STRONG` "How You’ll Make an Impact:", `P+STRONG` "What Makes You a Good Fit:"

**Issues:**

- Contains 2 `<br>` tag(s) (line-break instead of paragraph break).
- Inconsistent label punctuation: 3 end with `:` and 1 do not.
- Inconsistent label capitalization within the posting (titlecase=3, sentencecase=1).

#### Enterprise Account Manager (MoD/ MoI) – EMEA (Germany)
_Sales · Germany · [posting](https://jobs.ashbyhq.com/Skydio/12e9a494-9a89-457c-9dc7-2ef9ccdba17c)_

- Section-label styles: `P+STRONG`=4  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 22 items  
- Pre-compensation length: 4780 chars across 10 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `P+STRONG` "This role must be based in Switzerland, Germany, or Finland.", `P+STRONG` "How You’ll Make an Impact:", `P+STRONG` "What Makes You a Good Fit:"

**Issues:**

- Contains 2 `<br>` tag(s) (line-break instead of paragraph break).
- Inconsistent label punctuation: 3 end with `:` and 1 do not.
- Inconsistent label capitalization within the posting (titlecase=3, sentencecase=1).

#### Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland)
_Sales · Zurich, Switzerland · [posting](https://jobs.ashbyhq.com/Skydio/1d4977a2-c2e7-44ad-820b-253ff8355800)_

- Section-label styles: `P+STRONG`=4  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 22 items  
- Pre-compensation length: 4780 chars across 10 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `P+STRONG` "This role must be based in Switzerland, Germany, or Finland.", `P+STRONG` "How You’ll Make an Impact:", `P+STRONG` "What Makes You a Good Fit:"

**Issues:**

- Contains 2 `<br>` tag(s) (line-break instead of paragraph break).
- Inconsistent label punctuation: 3 end with `:` and 1 do not.
- Inconsistent label capitalization within the posting (titlecase=3, sentencecase=1).

#### Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM
_Sales · US Remote · [posting](https://jobs.ashbyhq.com/Skydio/e69362bc-5891-486e-be75-6bf25187ccf5)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 20 items  
- Pre-compensation length: 3949 chars across 8 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `P+STRONG` "How You’ll Make an Impact:", `P+STRONG` "What Makes You a Good Fit:"

**Issues:**

- Section labels use **titlecase** while 67% of postings use **sentencecase**.

#### Enterprise Account Manager, US Army
_Sales · US Remote · [posting](https://jobs.ashbyhq.com/Skydio/19559b4c-ed09-41eb-b1aa-f000a855b8fe)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 20 items  
- Pre-compensation length: 3483 chars across 8 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `P+STRONG` "How You’ll Make an Impact:", `P+STRONG` "What Makes You a Good Fit:"

**Issues:**

- Section labels use **titlecase** while 67% of postings use **sentencecase**.

#### Field Marketing Event Manager
_Marketing · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/6451be14-d388-4ad1-a4ce-97c36d130c71)_

- Section-label styles: `H3`=7, `P+STRONG`=3  
- Heading tags inside body: `h3`=7  
- Lists: 8 `<ul>`, 0 `<ol>`, 27 items  
- Pre-compensation length: 3917 chars across 21 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `P+STRONG` "How You’ll Make an Impact:", `H3` "Customer Summit Planning & Execution", `H3` "Field Marketing & Trade Show Support", `H3` "Relationship Building & Internal Collaboration", `P+STRONG` "What Makes You a Good Fit:", `H3` "Required Experience", `H3` "Preferred Skills & Experience", … (+2 more)

**Issues:**

- Section labels primarily styled as **H3** while 85% of postings use **P+STRONG**.
- Mixes section-label styles within the posting (H3=7, P+STRONG=3).
- Uses real heading tags inside the body (h3=7); the page-wide convention is `<p><strong>` for section labels.
- Inconsistent label punctuation: 3 end with `:` and 7 do not.
- Section labels use **titlecase** while 67% of postings use **sentencecase**.

#### Field Support Representative (Southwest, Remote)
_Customer Support · US Remote · [posting](https://jobs.ashbyhq.com/Skydio/9b93e7c2-e5d5-48b2-a2d2-8df71e0d8357)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 4 `<ul>`, 0 `<ol>`, 22 items  
- Pre-compensation length: 5086 chars across 12 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 2 empty paragraph(s) (extra vertical gap).
- Contains 13 non-breaking space(s) — likely pasted from a word processor.

#### Full Stack Product Counsel
_Legal · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/c9e40dab-ae7d-4034-a335-b3e05d419672)_

- Section-label styles: `H3`=4  
- Heading tags inside body: `h3`=4  
- Lists: 2 `<ul>`, 0 `<ol>`, 15 items  
- Pre-compensation length: 3376 chars across 13 top-level blocks
- Actual labels: `H3` "About the Team", `H3` "About the Role", `H3` "How You’ll Make an Impact", `H3` "What Makes You a Great Fit"

**Issues:**

- Section labels primarily styled as **H3** while 85% of postings use **P+STRONG**.
- Uses real heading tags inside the body (h3=4); the page-wide convention is `<p><strong>` for section labels.
- Uses `<u>` underline (rare across postings; only appears in 'PLEASE NOTE' callouts).
- Contains 3 empty paragraph(s) (extra vertical gap).
- Section labels without colons, while 93% of postings use labels with colons.
- Section labels use **titlecase** while 67% of postings use **sentencecase**.

#### GTM Data Engineer Intern
_Sales · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/b90b9b3b-e326-4fb6-85bd-fe52bec5f180)_

- Section-label styles: `P+STRONG`=4  
- Heading tags inside body: _(none)_  
- Lists: 4 `<ul>`, 0 `<ol>`, 18 items  
- Pre-compensation length: 3235 chars across 12 top-level blocks
- Actual labels: `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:", `P+STRONG` "Bonus points:", `P+STRONG` "What you’ll gain:"

**Issues:**

- Contains 2 empty paragraph(s) (extra vertical gap).
- Contains 3 `<br>` tag(s) (line-break instead of paragraph break).
- Contains 1 run(s) of double spaces in body text.

#### GTM Enablement Associate
_Sales · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/2b3fea3b-e1b5-4497-9607-e9864019b0e7)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 18 items  
- Pre-compensation length: 2829 chars across 12 top-level blocks
- Actual labels: `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:", `P+STRONG` "Preferred Qualifications:"

**Issues:**

- Contains 1 empty paragraph(s) (extra vertical gap).
- Contains 2 `<br>` tag(s) (line-break instead of paragraph break).
- Contains 1 non-breaking space(s) — likely pasted from a word processor.
- Inconsistent label capitalization within the posting (titlecase=1, sentencecase=2).

#### Hardware Operations Program Manager
_Supply Chain & Logistics · Hayward, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/55b393cf-124c-46f8-bd83-8c62e3ce628b)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 12 items  
- Pre-compensation length: 2924 chars across 8 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 1 empty paragraph(s) (extra vertical gap).

#### Head of Warehouse & Logistics Operations
_Manufacturing · Hayward, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/0c1e9360-09dc-4c73-85bc-51aa72afd3ad)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 20 items  
- Pre-compensation length: 3240 chars across 9 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 2 empty paragraph(s) (extra vertical gap).
- Contains 1 `<br>` tag(s) (line-break instead of paragraph break).

#### IT Technician (Help Desk - Linux Focus)
_IT · Hayward, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/28c865cf-6aa4-45d1-ae13-34bb8f6b776b)_

- Section-label styles: `P+STRONG`=5  
- Heading tags inside body: _(none)_  
- Lists: 14 `<ul>`, 0 `<ol>`, 42 items  
- Pre-compensation length: 3846 chars across 28 top-level blocks
- Actual labels: `P+STRONG` "About the Role", `P+STRONG` "Location", `P+STRONG` "What You’ll Do", `P+STRONG` "What Makes You a Good Fit", `P+STRONG` "Nice to Have"

**Issues:**

- Contains 2 empty paragraph(s) (extra vertical gap).
- Contains 8 `<br>` tag(s) (line-break instead of paragraph break).
- Section labels without colons, while 93% of postings use labels with colons.
- Inconsistent label capitalization within the posting (titlecase=4, sentencecase=1).
- Mixes list-item structures (`<li><p>…</p></li>` and `<li>…</li>` in the same posting) — this produces uneven bullet spacing.

#### Manager, Logistics 
_Manufacturing · US CA Production · [posting](https://jobs.ashbyhq.com/Skydio/eeb4b52f-d4e6-4823-9e4b-0ce75041d928)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 23 items  
- Pre-compensation length: 3222 chars across 10 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you will make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 1 empty paragraph(s) (extra vertical gap).
- Contains 1 non-breaking space(s) — likely pasted from a word processor.
- Non-standard inline styles detected: <div> min-height:1.2em; margin-top:0; margin-bottom:0

#### Manager, Technical Support
_Customer Support · US CA San Mateo · [posting](https://jobs.ashbyhq.com/Skydio/2b312ffb-26c3-4b7f-8904-acbc4e51934b)_

- Section-label styles: `P+STRONG`=4  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 22 items  
- Pre-compensation length: 5416 chars across 10 top-level blocks
- Actual labels: `P+STRONG` "About the team:", `P+STRONG` "About the role:", `P+STRONG` "How you’ll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 6 run(s) of double spaces in body text.

#### Manufacturing Quality Supervisor
_Manufacturing · Hayward, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/e0c94b6c-e08e-499b-aa62-b010993a9200)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 23 items  
- Pre-compensation length: 2848 chars across 8 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you’ll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 1 empty paragraph(s) (extra vertical gap).

#### Mission Success Operations Manager
_Professional Services and Training · US Remote · [posting](https://jobs.ashbyhq.com/Skydio/501a3067-e906-4354-b211-ac70db6accf4)_

- Section-label styles: `P+STRONG`=4  
- Heading tags inside body: _(none)_  
- Lists: 4 `<ul>`, 0 `<ol>`, 17 items  
- Pre-compensation length: 3037 chars across 10 top-level blocks
- Actual labels: `P+STRONG` "About the Team:", `P+STRONG` "About the role:", `P+STRONG` "How you’ll make an impact:", `P+STRONG` "What makes you a good fit"

**Issues:**

- Inconsistent label punctuation: 3 end with `:` and 1 do not.
- Inconsistent label capitalization within the posting (titlecase=1, sentencecase=3).
- Mixes list-item structures (`<li><p>…</p></li>` and `<li>…</li>` in the same posting) — this produces uneven bullet spacing.

#### Product Support Engineer
_Customer Support · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/a4f131a0-4dde-46ce-85a1-c83fc3e0f21e)_

- Section-label styles: _(none)_  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 22 items  
- Pre-compensation length: 4245 chars across 8 top-level blocks

**Issues:**

- No detectable section labels (flat prose).
- Contains 2 empty paragraph(s) (extra vertical gap).
- Contains 2 `<br>` tag(s) (line-break instead of paragraph break).
- Contains 3 run(s) of double spaces in body text.

#### Product Support Engineer Intern
_Customer Support · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/8df0689e-a489-4c72-a1f7-09dfe59745b8)_

- Section-label styles: _(none)_  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 15 items  
- Pre-compensation length: 3171 chars across 9 top-level blocks

**Issues:**

- No detectable section labels (flat prose).
- Contains 3 empty paragraph(s) (extra vertical gap).
- Contains 2 `<br>` tag(s) (line-break instead of paragraph break).
- Contains 4 run(s) of double spaces in body text.

#### Production Manager, PM Shift
_Manufacturing · Hayward, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/7836de07-b630-438b-8db5-37a9ee618009)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 11 items  
- Pre-compensation length: 2191 chars across 8 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `P+STRONG` "How You’ll Make an Impact:", `P+STRONG` "What Makes You a Good Fit:"

**Issues:**

- Contains 1 empty paragraph(s) (extra vertical gap).
- Section labels use **titlecase** while 67% of postings use **sentencecase**.

#### Production Supervisor
_Manufacturing · Hayward, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/90771bb1-f860-4b49-90ef-3a15bcd1fada)_

- Section-label styles: `P+STRONG`=2  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 11 items  
- Pre-compensation length: 2034 chars across 6 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 2 `<br>` tag(s) (line-break instead of paragraph break).

#### Program Manager, Major Deployments (Hawaii)
_Professional Services and Training · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/b194dcda-7ff0-4d44-9785-16895a44727f)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 14 items  
- Pre-compensation length: 4187 chars across 11 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What Makes You A Good Fit:"

**Issues:**

- Contains 2 empty paragraph(s) (extra vertical gap).
- Contains 1 run(s) of double spaces in body text.
- Inconsistent label capitalization within the posting (titlecase=1, sentencecase=2).

#### Program Manager, Major Deployments (Mid Atlantic)
_Professional Services and Training · US Remote · [posting](https://jobs.ashbyhq.com/Skydio/c2651b2d-14c5-4bf7-9a35-90b3c939af10)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 15 items  
- Pre-compensation length: 4248 chars across 12 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What Makes You A Good Fit:"

**Issues:**

- Contains 3 empty paragraph(s) (extra vertical gap).
- Contains 1 run(s) of double spaces in body text.
- Inconsistent label capitalization within the posting (titlecase=1, sentencecase=2).

#### Program Manager, Major Deployments (South East)
_Professional Services and Training · US Remote · [posting](https://jobs.ashbyhq.com/Skydio/28bb232f-54c4-486b-9bdb-c7855d04661d)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 14 items  
- Pre-compensation length: 4211 chars across 12 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What Makes You A Good Fit:"

**Issues:**

- Contains 3 empty paragraph(s) (extra vertical gap).
- Contains 1 run(s) of double spaces in body text.
- Inconsistent label capitalization within the posting (titlecase=1, sentencecase=2).

#### Revenue Operations Engineer, Quoting Systems
_Sales · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/02d54431-2747-417d-8234-e72c316fed87)_

- Section-label styles: `H2`=5, `P+STRONG`=1  
- Heading tags inside body: `h2`=5  
- Lists: 5 `<ul>`, 0 `<ol>`, 25 items  
- Pre-compensation length: 3822 chars across 16 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `H2` "What you’ll drive (scope):", `H2` "Day-to-day responsibilities:", `H2` "Tech stack you’ll work with:", `H2` "What you’ll bring:", `H2` "Reporting & Working Model:"

**Issues:**

- Section labels primarily styled as **H2** while 85% of postings use **P+STRONG**.
- Mixes section-label styles within the posting (H2=5, P+STRONG=1).
- Uses real heading tags inside the body (h2=5); the page-wide convention is `<p><strong>` for section labels.
- Contains 2 empty paragraph(s) (extra vertical gap).
- Contains 4 `<br>` tag(s) (line-break instead of paragraph break).
- Inconsistent label capitalization within the posting (titlecase=2, sentencecase=4).

#### Sales Planning Analyst Intern
_Sales · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/712900e5-ff75-4e07-8f88-626d4f8ab653)_

- Section-label styles: `P+STRONG`=2  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 18 items  
- Pre-compensation length: 2923 chars across 9 top-level blocks
- Actual labels: `P+STRONG` "How You’ll Make an Impact:", `P+STRONG` "What Would Make You a Good Fit:"

**Issues:**

- Contains 1 empty paragraph(s) (extra vertical gap).
- Contains 1 `<br>` tag(s) (line-break instead of paragraph break).
- Section labels use **titlecase** while 67% of postings use **sentencecase**.

#### Senior Brand Designer (Contract)
_Marketing · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/5ae7e25f-7da3-4523-a8be-8866aa89e8df)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 4 `<ul>`, 0 `<ol>`, 22 items  
- Pre-compensation length: 3619 chars across 15 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `P+STRONG` "What you'll do:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 3 empty paragraph(s) (extra vertical gap).
- Contains 2 `<br>` tag(s) (line-break instead of paragraph break).
- Inconsistent label capitalization within the posting (titlecase=1, sentencecase=2).

#### Senior Business Operations Manager
_Supply Chain & Logistics · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/17b9ecf9-7a47-4811-b035-e1b9a54966aa)_

- Section-label styles: `P+STRONG`=3, `H3`=3  
- Heading tags inside body: `h3`=3  
- Lists: 4 `<ul>`, 0 `<ol>`, 26 items  
- Pre-compensation length: 3744 chars across 14 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `P+STRONG` "How you'll make an impact:", `H3` "Strategic Sourcing:", `H3` "Cost Management", `H3` "Strategy & Operations", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Mixes section-label styles within the posting (P+STRONG=3, H3=3).
- Uses real heading tags inside the body (h3=3); the page-wide convention is `<p><strong>` for section labels.
- Contains 2 empty paragraph(s) (extra vertical gap).
- Inconsistent label punctuation: 4 end with `:` and 2 do not.
- Inconsistent label capitalization within the posting (titlecase=4, sentencecase=2).

#### Senior Buyer
_Manufacturing · Hayward, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/5d32766d-990a-4c4c-a8c6-5e934dd8bd38)_

- Section-label styles: `H2`=2, `P+STRONG`=1  
- Heading tags inside body: `h2`=2  
- Lists: 2 `<ul>`, 0 `<ol>`, 22 items  
- Pre-compensation length: 3478 chars across 11 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `H2` "How you will make an impact:", `H2` "What makes you a strong fit:"

**Issues:**

- Section labels primarily styled as **H2** while 85% of postings use **P+STRONG**.
- Mixes section-label styles within the posting (H2=2, P+STRONG=1).
- Uses real heading tags inside the body (h2=2); the page-wide convention is `<p><strong>` for section labels.
- Contains 3 empty paragraph(s) (extra vertical gap).
- Contains 2 run(s) of double spaces in body text.

#### Senior Customer Support Representative - India
_Customer Support · Bangalore, India · [posting](https://jobs.ashbyhq.com/Skydio/bb7a9c5c-8dbb-4a2f-9d7d-db9ab1f707b0)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 22 items  
- Pre-compensation length: 4427 chars across 10 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you’ll make an impact:", `P+STRONG` "What would make you a good fit:"

**Issues:**

- Contains 1 empty paragraph(s) (extra vertical gap).
- Contains 2 run(s) of double spaces in body text.

#### Senior NPI Product Quality Engineer
_Manufacturing · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/178a7e84-562e-40db-9abd-94bbf29159ca)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 19 items  
- Pre-compensation length: 2831 chars across 8 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Uses `<u>` underline (rare across postings; only appears in 'PLEASE NOTE' callouts).

#### Senior People Analytics Analyst
_People & Recruiting · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/0703aaa0-9fcb-4b22-ad8c-b53e74151a72)_

- Section-label styles: `P+STRONG`=4  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 16 items  
- Pre-compensation length: 3405 chars across 9 top-level blocks
- Actual labels: `P+STRONG` "About The Role", `P+STRONG` "How You’ll Make an Impact:", `P+STRONG` "What Makes Your a Good Fit:", `P+STRONG` "Preferred Qualifications"

**Issues:**

- Inconsistent label punctuation: 2 end with `:` and 2 do not.
- Section labels use **titlecase** while 67% of postings use **sentencecase**.

#### Senior Revenue Operations Manager
_Sales · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/05e9f029-3a9d-4956-a4c8-e0bc786dd86a)_

- Section-label styles: `P+STRONG`=4  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 18 items  
- Pre-compensation length: 3347 chars across 13 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `P+STRONG` "How You’ll Make an Impact:", `P+STRONG` "What Makes You a Good Fit:", `P+STRONG` "Preferred Qualifications:"

**Issues:**

- Contains 2 empty paragraph(s) (extra vertical gap).
- Section labels use **titlecase** while 67% of postings use **sentencecase**.

#### Senior Supplier Quality Engineer
_Supply Chain & Logistics · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/b0fb285d-0619-42ee-ad24-d549479deb84)_

- Section-label styles: `P+STRONG`=2  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 12 items  
- Pre-compensation length: 3098 chars across 7 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 1 empty paragraph(s) (extra vertical gap).
- Contains 2 `<br>` tag(s) (line-break instead of paragraph break).

#### Senior Technical Recruiter
_People & Recruiting · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/16b0647d-a470-4917-9bb9-a95967828edc)_

- Section-label styles: `P+STRONG`=2  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 14 items  
- Pre-compensation length: 3033 chars across 7 top-level blocks
- Actual labels: `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Uses `<u>` underline (rare across postings; only appears in 'PLEASE NOTE' callouts).
- Contains 2 `<br>` tag(s) (line-break instead of paragraph break).
- Contains 1 non-breaking space(s) — likely pasted from a word processor.

#### Senior Technical Recruiter - Hardware Operations
_People & Recruiting · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/737c02d2-f03f-4716-a0c8-e14a0307f8cb)_

- Section-label styles: `P+STRONG`=1  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 13 items  
- Pre-compensation length: 3110 chars across 7 top-level blocks
- Actual labels: `P+STRONG` "What makes you a good fit:"

**Issues:**

- Uses `<u>` underline (rare across postings; only appears in 'PLEASE NOTE' callouts).
- Contains 4 `<br>` tag(s) (line-break instead of paragraph break).
- Contains 1 non-breaking space(s) — likely pasted from a word processor.

#### Senior Technical Support Representative - Japan
_Customer Support · Tokyo, Japan · [posting](https://jobs.ashbyhq.com/Skydio/f714e85f-31df-494e-bac4-1dd61d4d6066)_

- Section-label styles: `H1`=3  
- Heading tags inside body: `h1`=3  
- Lists: 2 `<ul>`, 0 `<ol>`, 20 items  
- Pre-compensation length: 4331 chars across 9 top-level blocks
- Actual labels: `H1` "About the role:", `H1` "How you’ll make an impact:", `H1` "What would make you a good fit:"

**Issues:**

- Section labels primarily styled as **H1** while 85% of postings use **P+STRONG**.
- Uses real heading tags inside the body (h1=3); the page-wide convention is `<p><strong>` for section labels.
- Contains 1 empty paragraph(s) (extra vertical gap).
- Contains 2 `<br>` tag(s) (line-break instead of paragraph break).
- Contains 1 run(s) of double spaces in body text.

#### Staff Global Supply Manager,  Mechanicals
_Supply Chain & Logistics · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/2ffe6453-4a2f-4dfb-94f8-882f731a11ae)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 17 items  
- Pre-compensation length: 4148 chars across 9 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 1 empty paragraph(s) (extra vertical gap).
- Contains 1 `<br>` tag(s) (line-break instead of paragraph break).

#### Staff Technical Recruiter
_People & Recruiting · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/c3a4256a-4525-443c-81d0-6f69e7c24805)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 15 items  
- Pre-compensation length: 3012 chars across 8 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you’ll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Uses `<u>` underline (rare across postings; only appears in 'PLEASE NOTE' callouts).
- Contains 1 non-breaking space(s) — likely pasted from a word processor.

#### Success Systems Specialist 
_Professional Services and Training · US Remote · [posting](https://jobs.ashbyhq.com/Skydio/8de95d05-a601-47e2-8a13-5ba4d7ad428a)_

- Section-label styles: `P+STRONG`=8  
- Heading tags inside body: _(none)_  
- Lists: 6 `<ul>`, 0 `<ol>`, 28 items  
- Pre-compensation length: 5487 chars across 19 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `P+STRONG` "Why This Role Matters Now:", `P+STRONG` "How You’ll Make an Impact:", `P+STRONG` "Build Automation & Intelligence into Mission Success", `P+STRONG` "Customer Digital Experience", `P+STRONG` "Cross-Functional Architecture & Governance", `P+STRONG` "Scalability & Cost Avoidance", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 1 empty paragraph(s) (extra vertical gap).
- Inconsistent label punctuation: 4 end with `:` and 4 do not.
- Inconsistent label capitalization within the posting (titlecase=7, sentencecase=1).

#### Supplier Quality Engineer, Sustaining
_Supply Chain & Logistics · Taiwan · [posting](https://jobs.ashbyhq.com/Skydio/4c4874bf-02da-4ccc-8918-2cca08feaf21)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 13 items  
- Pre-compensation length: 3243 chars across 9 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 1 empty paragraph(s) (extra vertical gap).

#### Supply Chain Intern
_Supply Chain & Logistics · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/2d21f482-3224-4906-a1bb-6a64436774cb)_

- Section-label styles: `P+STRONG`=2  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 8 items  
- Pre-compensation length: 1664 chars across 6 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 2 `<br>` tag(s) (line-break instead of paragraph break).

#### Technical Support Specialist - West Coast
_Customer Support · US Remote · [posting](https://jobs.ashbyhq.com/Skydio/3ac81a34-b7fe-4142-9d29-12bcc1376182)_

- Section-label styles: _(none)_  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 19 items  
- Pre-compensation length: 4281 chars across 11 top-level blocks

**Issues:**

- No detectable section labels (flat prose).
- Contains 5 non-breaking space(s) — likely pasted from a word processor.

#### Workplace Experience Coordinator Part-Time
_People & Recruiting · Zurich, Switzerland · [posting](https://jobs.ashbyhq.com/Skydio/d023afe5-f19f-42f7-a1dd-aa94a361b86f)_

- Section-label styles: `P+STRONG`=5  
- Heading tags inside body: _(none)_  
- Lists: 4 `<ul>`, 0 `<ol>`, 20 items  
- Pre-compensation length: 2759 chars across 14 top-level blocks
- Actual labels: `P+STRONG` "How you’ll make an impact:", `P+STRONG` "Workplace Experience & Office Operations", `P+STRONG` "People Operations & HR Coordination", `P+STRONG` "Qualifications", `P+STRONG` "Work Environment"

**Issues:**

- Contains 1 empty paragraph(s) (extra vertical gap).
- Contains 1 `<br>` tag(s) (line-break instead of paragraph break).
- Inconsistent label punctuation: 1 end with `:` and 4 do not.
- Inconsistent label capitalization within the posting (titlecase=3, sentencecase=2).

### R&D

####  Electrical Engineer (Sustaining/Validation)
_Hardware · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/8e50c7da-2868-4383-af1f-920584d537fc)_

- Section-label styles: `P+STRONG`=2  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 14 items  
- Pre-compensation length: 2088 chars across 6 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 1 `<br>` tag(s) (line-break instead of paragraph break).

####  Senior Software Engineer,  Infrastructure
_Software · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/0f71bdbb-a645-49f6-8890-dd5c052772c3)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 13 items  
- Pre-compensation length: 2689 chars across 9 top-level blocks
- Actual labels: `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:", `P+STRONG` "Bonus points:"

**Issues:**

- Contains 1 run(s) of double spaces in body text.

#### Autonomy Engineer - Deep Learning
_Autonomy · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/cc83824e-a1cd-4bc7-9206-7264da9fbd61)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 14 items  
- Pre-compensation length: 2582 chars across 8 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 1 non-breaking space(s) — likely pasted from a word processor.

#### Autonomy Engineer - Deep Learning
_Autonomy · Zurich, Switzerland · [posting](https://jobs.ashbyhq.com/Skydio/ae12de71-0010-49d3-b171-c0b257e3b6c1)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 14 items  
- Pre-compensation length: 2582 chars across 8 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 1 non-breaking space(s) — likely pasted from a word processor.

#### Autonomy Engineer - Deep Learning Infrastructure
_Autonomy · Zurich, Switzerland · [posting](https://jobs.ashbyhq.com/Skydio/c051266c-3e00-4906-abd0-21f18db56b3f)_

- Section-label styles: `P+STRONG`=1  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 17 items  
- Pre-compensation length: 3227 chars across 5 top-level blocks
- Actual labels: `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 6 `<br>` tag(s) (line-break instead of paragraph break).

#### Autonomy Engineer - Deep Learning Infrastructure
_Autonomy · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/dcb04687-9b4f-425d-8c37-1111cf3ccf3d)_

- Section-label styles: `P+STRONG`=1  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 17 items  
- Pre-compensation length: 3392 chars across 6 top-level blocks
- Actual labels: `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 1 empty paragraph(s) (extra vertical gap).
- Contains 8 `<br>` tag(s) (line-break instead of paragraph break).
- Contains 2 non-breaking space(s) — likely pasted from a word processor.

#### Autonomy Engineer - Deep Learning Model Acceleration
_Autonomy · Zurich, Switzerland · [posting](https://jobs.ashbyhq.com/Skydio/5892ea83-ad5a-480a-bd9f-2409bb0b644e)_

- Section-label styles: `P+STRONG`=1  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 17 items  
- Pre-compensation length: 3231 chars across 5 top-level blocks
- Actual labels: `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 6 `<br>` tag(s) (line-break instead of paragraph break).

#### Autonomy Engineer - Deep Learning Model Acceleration
_Autonomy · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/cd6d8410-419b-4713-8d4d-7eb72b134d5a)_

- Section-label styles: `P+STRONG`=1  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 17 items  
- Pre-compensation length: 3227 chars across 5 top-level blocks
- Actual labels: `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 6 `<br>` tag(s) (line-break instead of paragraph break).

#### Autonomy Engineer - Fixed Wing Planning & Controls
_Autonomy · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/20754382-05e7-4cb6-a0f9-0daf9338ba78)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 12 items  
- Pre-compensation length: 1801 chars across 7 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `P+STRONG` "How You'll Make an Impact:", `P+STRONG` "What Makes You a Good Fit:"

**Issues:**

- Contains 1 run(s) of double spaces in body text.
- Section labels use **titlecase** while 67% of postings use **sentencecase**.

#### Autonomy Engineer - ML & DL Infrastructure 
_Autonomy · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/b6be08f7-89c0-48dd-b427-f587f23dbf34)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 13 items  
- Pre-compensation length: 3179 chars across 11 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `P+STRONG` "How You’ll Make an Impact:", `P+STRONG` "What Makes You a Good Fit:"

**Issues:**

- Contains 2 empty paragraph(s) (extra vertical gap).
- Section labels use **titlecase** while 67% of postings use **sentencecase**.

#### Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026
_Autonomy · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/c84945f0-b8e0-4272-b636-265d6611a8eb)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 8 items  
- Pre-compensation length: 2216 chars across 9 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a strong fit:"

**Issues:**

- Contains 1 `<br>` tag(s) (line-break instead of paragraph break).
- Contains 1 non-breaking space(s) — likely pasted from a word processor.

#### Autonomy Engineer Intern - Deep Learning (Computational Photography)
_Autonomy · Zurich, Switzerland · [posting](https://jobs.ashbyhq.com/Skydio/6280ab1d-147d-4f39-8618-a216c18ce0f9)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 15 items  
- Pre-compensation length: 3263 chars across 9 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 3 run(s) of double spaces in body text.

#### Autonomy Engineer Intern - Deep Learning (Computational Photography)
_Autonomy · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/d13e3179-e646-4873-84a6-d492a692bc25)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 15 items  
- Pre-compensation length: 3263 chars across 9 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 3 run(s) of double spaces in body text.

#### Autonomy Engineer Intern Fall 2026
_Autonomy · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/17f6173b-c96f-4b02-a6b5-da0a91ad95e5)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 8 items  
- Pre-compensation length: 1872 chars across 8 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 1 non-breaking space(s) — likely pasted from a word processor.

#### Autonomy Software Engineer
_Autonomy · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/a48fe41b-030b-4f11-bf25-df7446151854)_

- Section-label styles: `P+STRONG`=1  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 12 items  
- Pre-compensation length: 2803 chars across 5 top-level blocks
- Actual labels: `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 4 `<br>` tag(s) (line-break instead of paragraph break).

#### Director of Product Management, Drone as First Responder (DFR)
_Product · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/129a5bad-ca1d-4eda-843b-96f4581f3c43)_

- Section-label styles: `P+STRONG`=2  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 20 items  
- Pre-compensation length: 4148 chars across 7 top-level blocks
- Actual labels: `P+STRONG` "What makes you a good fit:", `P+STRONG` "Bonus points for:"

**Issues:**

- Contains 4 `<br>` tag(s) (line-break instead of paragraph break).
- Contains 5 non-breaking space(s) — likely pasted from a word processor.

#### Electric Motor / Propulsion Engineer
_Hardware · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/847c1abe-b3b6-4e97-bc0e-e3f46437287a)_

- Section-label styles: `P+STRONG`=2  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 14 items  
- Pre-compensation length: 1921 chars across 7 top-level blocks
- Actual labels: `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 1 `<br>` tag(s) (line-break instead of paragraph break).

#### Electrical Engineer (all levels) 
_Hardware · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/f0c26a3c-d999-4dc2-8812-b3835f633ded)_

- Section-label styles: `P+STRONG`=2  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 13 items  
- Pre-compensation length: 1723 chars across 6 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 2 `<br>` tag(s) (line-break instead of paragraph break).

#### Engineering Manager - Autonomy
_Autonomy · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/849ae77c-5ca2-42b5-812b-8b3ad4524a89)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 10 items  
- Pre-compensation length: 2366 chars across 7 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 1 `<br>` tag(s) (line-break instead of paragraph break).

#### Hardware Technician
_Hardware · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/6d5e666b-a0b7-45d4-a4de-45aef141ce10)_

- Section-label styles: `P+STRONG`=2  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 18 items  
- Pre-compensation length: 2646 chars across 7 top-level blocks
- Actual labels: `P+STRONG` "How You’ll Make an Impact:", `P+STRONG` "What Makes You a Good Fit:"

**Issues:**

- Contains 1 empty paragraph(s) (extra vertical gap).
- Section labels use **titlecase** while 67% of postings use **sentencecase**.

#### Lead Staff Electrical Engineer (F10 Program)
_Hardware · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/1bbcf144-7057-4a6e-9d51-4924bfda52b9)_

- Section-label styles: `P+STRONG`=2  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 15 items  
- Pre-compensation length: 2194 chars across 8 top-level blocks
- Actual labels: `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Uses `<u>` underline (rare across postings; only appears in 'PLEASE NOTE' callouts).
- Contains 2 empty paragraph(s) (extra vertical gap).
- Contains 1 `<br>` tag(s) (line-break instead of paragraph break).
- Contains 2 non-breaking space(s) — likely pasted from a word processor.

#### PCB Layout Engineer
_Hardware · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/eb2f4124-9bd6-49f9-9636-03152c573f7d)_

- Section-label styles: `P+STRONG`=2  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 12 items  
- Pre-compensation length: 2556 chars across 6 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 2 `<br>` tag(s) (line-break instead of paragraph break).
- Contains 2 non-breaking space(s) — likely pasted from a word processor.

#### PhD Autonomy Engineer Intern - Deep Learning or Computer Vision
_Autonomy · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/8d3979a8-c791-4825-8cf4-9b25479b9519)_

- Section-label styles: _(none)_  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 9 items  
- Pre-compensation length: 2733 chars across 2 top-level blocks

**Issues:**

- No detectable section labels (flat prose).
- Contains 1 `<br>` tag(s) (line-break instead of paragraph break).
- Contains 1 non-breaking space(s) — likely pasted from a word processor.
- Mixes list-item structures (`<li><p>…</p></li>` and `<li>…</li>` in the same posting) — this produces uneven bullet spacing.

#### PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning)
_Autonomy · Zurich, Switzerland · [posting](https://jobs.ashbyhq.com/Skydio/f8225008-00b5-415e-9a48-c9b6eba9363c)_

- Section-label styles: `H3`=3, `P+STRONG`=2  
- Heading tags inside body: `h3`=3  
- Lists: 4 `<ul>`, 0 `<ol>`, 17 items  
- Pre-compensation length: 3318 chars across 11 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `H3` "How you'll make an impact:", `H3` "What makes this internship different:", `H3` "What makes you a strong fit:", `P+STRONG` "Nice-to-Haves:"

**Issues:**

- Section labels primarily styled as **H3** while 85% of postings use **P+STRONG**.
- Mixes section-label styles within the posting (H3=3, P+STRONG=2).
- Uses real heading tags inside the body (h3=3); the page-wide convention is `<p><strong>` for section labels.
- Contains 1 non-breaking space(s) — likely pasted from a word processor.

#### Product Design Engineer (All Levels)
_Hardware · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/3f02ead1-8efe-4e3f-9c75-625e74ab57d1)_

- Section-label styles: `P+STRONG`=2  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 16 items  
- Pre-compensation length: 3124 chars across 6 top-level blocks
- Actual labels: `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 1 `<br>` tag(s) (line-break instead of paragraph break).
- Contains 1 non-breaking space(s) — likely pasted from a word processor.

#### RF Design Engineer
_Connectivity · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/f72f1fa5-d3d6-459e-8722-a94ce92ad1c8)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 19 items  
- Pre-compensation length: 2704 chars across 7 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `P+STRONG` "How You’ll Make an Impact:", `P+STRONG` "What Makes You a Good Fit:"

**Issues:**

- Section labels use **titlecase** while 67% of postings use **sentencecase**.

#### Senior Autonomy Engineer - Controls 
_Autonomy · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/58b4cdf6-5630-4dd0-aab3-a1ed4d599466)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 9 items  
- Pre-compensation length: 1715 chars across 8 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `P+STRONG` "How You’ll Make an Impact:", `P+STRONG` "What Makes You a Good Fit:"

**Issues:**

- Contains 1 run(s) of double spaces in body text.
- Section labels use **titlecase** while 67% of postings use **sentencecase**.

#### Senior Autonomy Engineer - Data Curation 
_Autonomy · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/562c2e8f-c366-4149-945e-0f42f4264b5f)_

- Section-label styles: `P+STRONG`=5  
- Heading tags inside body: _(none)_  
- Lists: 4 `<ul>`, 0 `<ol>`, 19 items  
- Pre-compensation length: 3170 chars across 16 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `P+STRONG` "How You’ll Make an Impact:", `P+STRONG` "What Makes You a Good Fit:", `P+STRONG` "Nice To Haves:", `P+STRONG` "Working Style:"

**Issues:**

- Contains 4 empty paragraph(s) (extra vertical gap).
- Section labels use **titlecase** while 67% of postings use **sentencecase**.

#### Senior Autonomy Engineer - Deep Learning
_Autonomy · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/a6421d3e-fdd0-48d6-8d8f-3fd605cdf09f)_

- Section-label styles: `P+STRONG`=2  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 13 items  
- Pre-compensation length: 2193 chars across 8 top-level blocks
- Actual labels: `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 1 empty paragraph(s) (extra vertical gap).
- Contains 2 `<br>` tag(s) (line-break instead of paragraph break).
- Contains 1 non-breaking space(s) — likely pasted from a word processor.

#### Senior Autonomy Engineer - Deep Learning
_Autonomy · Zurich, Switzerland · [posting](https://jobs.ashbyhq.com/Skydio/a6973c57-132a-4a0d-b130-02d2bdaecd2a)_

- Section-label styles: `P+STRONG`=2  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 13 items  
- Pre-compensation length: 2193 chars across 6 top-level blocks
- Actual labels: `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 2 `<br>` tag(s) (line-break instead of paragraph break).
- Contains 1 non-breaking space(s) — likely pasted from a word processor.

#### Senior Product Manager, Platform & Infrastructure
_Product · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/8d67884d-58f4-41a7-8740-ab65d3c03fa8)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 15 items  
- Pre-compensation length: 5646 chars across 16 top-level blocks
- Actual labels: `P+STRONG` "Location", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What would make you a strong fit:"

**Issues:**

- Contains 6 empty paragraph(s) (extra vertical gap).
- Contains 1 `<br>` tag(s) (line-break instead of paragraph break).
- Inconsistent label punctuation: 2 end with `:` and 1 do not.

#### Senior Software Engineer - Embedded 
_Software · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/67a7d89f-9c4e-4f60-bdf1-a60b8addd8ae)_

- Section-label styles: `P+STRONG`=4  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 17 items  
- Pre-compensation length: 2413 chars across 9 top-level blocks
- Actual labels: `P+STRONG` "About the team:", `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 3 non-breaking space(s) — likely pasted from a word processor.

#### Senior Software Engineer - Mobile Platform 
_Software · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/e8cb16b0-d2f0-4cb4-a1a1-0f43d195cc9a)_

- Section-label styles: `P+STRONG`=5  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 18 items  
- Pre-compensation length: 3693 chars across 14 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `P+STRONG` "About the Team:", `P+STRONG` "How You’ll Make an Impact:", `P+STRONG` "What Makes You a Good Fit:", `P+STRONG` "Nice To Haves:"

**Issues:**

- Contains 3 empty paragraph(s) (extra vertical gap).
- Section labels use **titlecase** while 67% of postings use **sentencecase**.

#### Senior Software Engineer - Security
_Security · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/bcd3d614-178c-4349-afd4-76476211b7fe)_

- Section-label styles: `P+STRONG`=4  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 17 items  
- Pre-compensation length: 2986 chars across 9 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `P+STRONG` "How you’ll make an impact:", `P+STRONG` "What makes you a good fit:", `P+STRONG` "Nice to have:"

**Issues:**

- Inconsistent label capitalization within the posting (titlecase=1, sentencecase=3).

#### Senior Software Engineer,  Data Platform 
_Software · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/aeaa130d-3e8b-42c5-a805-46f056e62fda)_

- Section-label styles: `P+STRONG`=5  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 20 items  
- Pre-compensation length: 5104 chars across 13 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "Examples of what you’ll help build:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What would make you a good fit:", `P+STRONG` "Why Join Us?"

**Issues:**

- Contains 1 `<br>` tag(s) (line-break instead of paragraph break).
- Inconsistent label punctuation: 4 end with `:` and 1 do not.
- Inconsistent label capitalization within the posting (titlecase=1, sentencecase=4).

#### Senior Software Engineer, Frontend
_Software · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/86cfc7bb-001c-4c1c-b680-160265535a96)_

- Section-label styles: `P+STRONG`=4  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 15 items  
- Pre-compensation length: 2488 chars across 11 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `P+STRONG` "How You’ll Make an Impact:", `P+STRONG` "What Makes You a Good Fit:", `P+STRONG` "Bonus Points:"

**Issues:**

- Section labels use **titlecase** while 67% of postings use **sentencecase**.

#### Senior Software Engineer, Full Stack
_Software · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/5655fbe3-66b0-4951-afdc-3b67f71e6938)_

- Section-label styles: `P+STRONG`=4  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 13 items  
- Pre-compensation length: 4254 chars across 14 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you’ll make an impact:", `P+STRONG` "What would make you a good fit:", `P+STRONG` "Bonus points for:"

**Issues:**

- Uses `<u>` underline (rare across postings; only appears in 'PLEASE NOTE' callouts).
- Contains 1 `<br>` tag(s) (line-break instead of paragraph break).

#### Senior Wireless Systems Performance Engineer
_Connectivity · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/f1ecf164-714c-4f1a-b672-d763f5724c03)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 16 items  
- Pre-compensation length: 2735 chars across 7 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 4 non-breaking space(s) — likely pasted from a word processor.

#### Senior/Staff Embedded Software Engineer – Camera Systems
_Software · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/71033170-d9d0-474b-b712-a11e4f11c146)_

- Section-label styles: `P+STRONG`=4  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 18 items  
- Pre-compensation length: 2838 chars across 11 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `P+STRONG` "About the Team:", `P+STRONG` "How You’ll Make an Impact:", `P+STRONG` "What Makes You a Good Fit:"

**Issues:**

- Contains 2 empty paragraph(s) (extra vertical gap).
- Section labels use **titlecase** while 67% of postings use **sentencecase**.

#### Software Engineer - Autonomy Infrastructure, Systems and Tools
_Autonomy · Zurich, Switzerland · [posting](https://jobs.ashbyhq.com/Skydio/9fc135c5-7a87-410d-8323-e0f918585ebc)_

- Section-label styles: `H2`=5  
- Heading tags inside body: `h2`=5  
- Lists: 4 `<ul>`, 0 `<ol>`, 20 items  
- Pre-compensation length: 3977 chars across 13 top-level blocks
- Actual labels: `H2` "About the Role:", `H2` "Areas of Responsibility:", `H2` "What You’ll Do:", `H2` "Qualifications:", `H2` "Bonus Experience:"

**Issues:**

- Section labels primarily styled as **H2** while 85% of postings use **P+STRONG**.
- Uses real heading tags inside the body (h2=5); the page-wide convention is `<p><strong>` for section labels.
- Contains 1 empty paragraph(s) (extra vertical gap).
- Inconsistent label capitalization within the posting (titlecase=4, sentencecase=1).

#### Software Engineer - Autonomy Infrastructure, Systems and Tools
_Autonomy · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/9e42a7af-6369-4036-ae6f-6626ee3a4fb3)_

- Section-label styles: `H2`=5  
- Heading tags inside body: `h2`=5  
- Lists: 4 `<ul>`, 0 `<ol>`, 20 items  
- Pre-compensation length: 3977 chars across 13 top-level blocks
- Actual labels: `H2` "About the Role:", `H2` "Areas of Responsibility:", `H2` "What You’ll Do:", `H2` "Qualifications:", `H2` "Bonus Experience:"

**Issues:**

- Section labels primarily styled as **H2** while 85% of postings use **P+STRONG**.
- Uses real heading tags inside the body (h2=5); the page-wide convention is `<p><strong>` for section labels.
- Contains 1 empty paragraph(s) (extra vertical gap).
- Inconsistent label capitalization within the posting (titlecase=4, sentencecase=1).

#### Software Engineer - Cloud Simulation & Full-Stack
_Autonomy · Zurich, Switzerland · [posting](https://jobs.ashbyhq.com/Skydio/948bddb5-4679-4c7c-bf57-960a0fd1a7ed)_

- Section-label styles: `H2`=5  
- Heading tags inside body: `h2`=5  
- Lists: 4 `<ul>`, 0 `<ol>`, 26 items  
- Pre-compensation length: 4208 chars across 14 top-level blocks
- Actual labels: `H2` "About the Role:", `H2` "Areas of Responsibility:", `H2` "What You’ll Do:", `H2` "Qualifications:", `H2` "Bonus Experience:"

**Issues:**

- Section labels primarily styled as **H2** while 85% of postings use **P+STRONG**.
- Uses real heading tags inside the body (h2=5); the page-wide convention is `<p><strong>` for section labels.
- Contains 2 empty paragraph(s) (extra vertical gap).
- Inconsistent label capitalization within the posting (titlecase=4, sentencecase=1).

#### Software Engineer - Cloud Simulation & Full-Stack
_Autonomy · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/7d7dfadc-c6fd-4958-8d59-004a91bff55e)_

- Section-label styles: `H2`=5  
- Heading tags inside body: `h2`=5  
- Lists: 4 `<ul>`, 0 `<ol>`, 26 items  
- Pre-compensation length: 4208 chars across 14 top-level blocks
- Actual labels: `H2` "About the Role:", `H2` "Areas of Responsibility:", `H2` "What You’ll Do:", `H2` "Qualifications:", `H2` "Bonus Experience:"

**Issues:**

- Section labels primarily styled as **H2** while 85% of postings use **P+STRONG**.
- Uses real heading tags inside the body (h2=5); the page-wide convention is `<p><strong>` for section labels.
- Contains 2 empty paragraph(s) (extra vertical gap).
- Inconsistent label capitalization within the posting (titlecase=4, sentencecase=1).

#### Software Engineer - Embedded
_Software · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/ef9f7dd2-5a88-49b4-a507-d5fc9cad565a)_

- Section-label styles: `P+STRONG`=4  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 17 items  
- Pre-compensation length: 2413 chars across 9 top-level blocks
- Actual labels: `P+STRONG` "About the team:", `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 3 non-breaking space(s) — likely pasted from a word processor.

#### Software Engineer - Simulation & Robotics Engineer
_Autonomy · Zurich, Switzerland · [posting](https://jobs.ashbyhq.com/Skydio/abd4addb-2d11-4207-b3a2-446a09121e39)_

- Section-label styles: `H3`=5  
- Heading tags inside body: `h3`=5  
- Lists: 4 `<ul>`, 0 `<ol>`, 20 items  
- Pre-compensation length: 3485 chars across 15 top-level blocks
- Actual labels: `H3` "About the Role:", `H3` "Areas of Responsibility:", `H3` "What You’ll Do:", `H3` "Qualifications:", `H3` "Bonus Experience:"

**Issues:**

- Section labels primarily styled as **H3** while 85% of postings use **P+STRONG**.
- Uses real heading tags inside the body (h3=5); the page-wide convention is `<p><strong>` for section labels.
- Contains 2 empty paragraph(s) (extra vertical gap).
- Inconsistent label capitalization within the posting (titlecase=4, sentencecase=1).

#### Software Engineer - Simulation & Robotics Engineer
_Autonomy · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/7a8f3e6c-d576-41af-a81e-bf4fe20da12a)_

- Section-label styles: `H3`=5  
- Heading tags inside body: `h3`=5  
- Lists: 4 `<ul>`, 0 `<ol>`, 20 items  
- Pre-compensation length: 3485 chars across 15 top-level blocks
- Actual labels: `H3` "About the Role:", `H3` "Areas of Responsibility:", `H3` "What You’ll Do:", `H3` "Qualifications:", `H3` "Bonus Experience:"

**Issues:**

- Section labels primarily styled as **H3** while 85% of postings use **P+STRONG**.
- Uses real heading tags inside the body (h3=5); the page-wide convention is `<p><strong>` for section labels.
- Contains 2 empty paragraph(s) (extra vertical gap).
- Inconsistent label capitalization within the posting (titlecase=4, sentencecase=1).

#### Software Engineer Intern Fall 2026/Winter 2027
_Software · US CA San Mateo · [posting](https://jobs.ashbyhq.com/Skydio/f6320e9b-4eed-408d-8d37-d509fb0406ee)_

- Section-label styles: `P+STRONG`=1  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 12 items  
- Pre-compensation length: 2593 chars across 10 top-level blocks
- Actual labels: `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 1 empty paragraph(s) (extra vertical gap).
- Contains 4 `<br>` tag(s) (line-break instead of paragraph break).

#### Software Engineer, Full Stack
_Software · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/f0020863-db72-480f-916d-375986f86031)_

- Section-label styles: `P+STRONG`=4  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 13 items  
- Pre-compensation length: 1935 chars across 9 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you’ll make an impact:", `P+STRONG` "What would make you a good fit:", `P+STRONG` "Bonus Points:"

**Issues:**

- Inconsistent label capitalization within the posting (titlecase=1, sentencecase=3).

#### Sr/Staff Embedded Software Engineer - Camera Systems
_Software · Tampere, Finland · [posting](https://jobs.ashbyhq.com/Skydio/898a9c77-cc20-4ed6-a050-f68e5c15d5c8)_

- Section-label styles: `P+STRONG`=4  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 18 items  
- Pre-compensation length: 2838 chars across 12 top-level blocks
- Actual labels: `P+STRONG` "About the Role:", `P+STRONG` "About the Team:", `P+STRONG` "How You’ll Make an Impact:", `P+STRONG` "What Makes You a Good Fit:"

**Issues:**

- Contains 3 empty paragraph(s) (extra vertical gap).
- Section labels use **titlecase** while 67% of postings use **sentencecase**.

#### Staff Product Manager, Platform & Infrastructure
_Product · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/dbd737b2-beed-4917-9948-dde4250929a8)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 15 items  
- Pre-compensation length: 5757 chars across 16 top-level blocks
- Actual labels: `P+STRONG` "Location", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What would make you a strong fit:"

**Issues:**

- Contains 6 empty paragraph(s) (extra vertical gap).
- Contains 1 `<br>` tag(s) (line-break instead of paragraph break).
- Inconsistent label punctuation: 2 end with `:` and 1 do not.

#### Staff Software Engineer - Embedded
_Software · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/b3b2dea9-63bb-4adb-ba29-69bd8f7a18eb)_

- Section-label styles: `P+STRONG`=4  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 17 items  
- Pre-compensation length: 2412 chars across 9 top-level blocks
- Actual labels: `P+STRONG` "About the team:", `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 3 non-breaking space(s) — likely pasted from a word processor.

#### Staff Software Engineer, Frontend
_Software · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/54654035-a78a-4e5b-9ebf-ae4067e5a246)_

- Section-label styles: `P+STRONG`=4  
- Heading tags inside body: _(none)_  
- Lists: 3 `<ul>`, 0 `<ol>`, 15 items  
- Pre-compensation length: 2457 chars across 10 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:", `P+STRONG` "Bonus Points:"

**Issues:**

- Inconsistent label capitalization within the posting (titlecase=1, sentencecase=3).

#### Wireless Hardware Engineer Intern
_Connectivity · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/5e1057a4-214f-4783-b676-c1315cfa81ea)_

- Section-label styles: `P+STRONG`=2  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 14 items  
- Pre-compensation length: 2616 chars across 7 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 2 `<br>` tag(s) (line-break instead of paragraph break).

#### Wireless Software Engineer
_Connectivity · San Mateo, California, United States · [posting](https://jobs.ashbyhq.com/Skydio/04fde92b-6a2b-4638-adc2-e8fa91cc1a49)_

- Section-label styles: `P+STRONG`=3  
- Heading tags inside body: _(none)_  
- Lists: 2 `<ul>`, 0 `<ol>`, 12 items  
- Pre-compensation length: 2824 chars across 7 top-level blocks
- Actual labels: `P+STRONG` "About the role:", `P+STRONG` "How you'll make an impact:", `P+STRONG` "What makes you a good fit:"

**Issues:**

- Contains 1 non-breaking space(s) — likely pasted from a word processor.

## 5. Postings with no detected issues

- ** Software Engineer - Infrastructure** — Software · San Mateo, California, United States
- **Field Support Representative ** — Customer Support · US Remote
- **Senior Hardware Test and Reliability Engineer** — Hardware · San Mateo, California, United States
- **Staff Software Engineer, Full Stack** — Software · San Mateo, California, United States
- **Systems Integration and Test Engineer (Mid to Senior Level)** — Hardware · San Mateo, California, United States

## 6. Recommendations for standardizing pre-compensation content

These are concrete, do-this-not-that fixes the recruiting/marketing team can apply directly in Ashby's editor.

**A. Lock the section-label style.**  
Use `<p><strong>Label:</strong></p>` for every section header (About the role, How you'll make an impact, What makes you a good fit, About Skydio, etc.). Do **not** use `<h1>`–`<h6>` inside the body — those tags pick up the page's display-heading CSS and render dramatically larger than the rest of the posting. (66 stray heading tag(s) found across 16 posting(s).)

**B. Pick one capitalization style for labels and use it everywhere.**  
Today the corpus mixes Title Case ("How You'll Make an Impact"), Sentence case ("What makes you a good fit"), and a few all-caps callouts. Recommend Sentence case + trailing colon (the majority pattern), e.g. "About the role:", "How you'll make an impact:", "What makes you a good fit:".

**C. Pick one bullet structure.**  
Standardize on `<li><p>…</p></li>` (the dominant pattern). When writers paste from Google Docs, Ashby sometimes produces bare `<li>…</li>` — visually those bullets render closer together than the rest of the page. After pasting, click into each bullet and press Enter/Backspace once to force the editor to wrap text in `<p>`.

**D. Strip inline `style=` attributes other than the default.**  
Anything other than `min-height:1.5em` (Ashby's default) is a smell: `color:`, `font-family:`, `font-size:`, `text-align:`, `<font>`, etc. These come from pasted Google Docs / Word content and override the site's typography. Use Ashby's "Clear formatting" before saving.

**E. Reserve `<u>` underline for the "PLEASE NOTE" callout only.**  
Underlines are easy to confuse with hyperlinks. Today underline is used inconsistently — only keep it for the standard hybrid-policy PLEASE NOTE block (or replace that block with bold text).

**F. Remove empty paragraphs, stray `<br>`, and non-breaking spaces.**  
Empty `<p></p>` blocks add an extra blank line that's visually double-spaced; `<br>` makes a soft line-break that looks tighter than a real paragraph break; non-breaking spaces (`\xa0`) are an artifact of pasted Word/Docs content and have no place here.

**G. Standardize the opening paragraph.**  
Today 100% of postings start with the canonical "Skydio is the leading US drone company…" boilerplate. Make this a required opening (Ashby template) so every posting shares the same first paragraph.

**H. Single source of truth: a posting template in Ashby.**  
Build a template containing the standard intro, the standard PLEASE NOTE block, and the standard section labels (About the role, How you'll make an impact, What makes you a good fit). Recruiters should fork this template instead of copy-pasting from existing postings, which is how drift compounds.

**I. Add a CI/lint pass.**  
The script that produced this report (`scripts/analyze_skydio_jobs.py`) can be run on a schedule against the Ashby API. Treat any non-zero issue count as a posting that needs a quick editor pass before it hits production.

---

_Generated by `scripts/analyze_skydio_jobs.py`. Re-run any time to refresh the audit._

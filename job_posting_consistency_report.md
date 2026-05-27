# Skydio Careers — Job-Posting Formatting Consistency Report

**Source:** [skydio.com/careers](https://www.skydio.com/careers)  
**Postings analyzed:** 104 (all live openings)  
**Scope:** the *Job Description* body of each posting (the content inside `<div class="prose block-content">`) **up to but not including the `Compensation:` block**. Boilerplate that always follows the compensation block (EEO statement, E-Verify, etc.) was excluded.  
**Generated:** 2026-05-27 16:10 UTC  
**Method:** Each posting was downloaded, the pre-compensation HTML was extracted, and the resulting markup was inspected for heading tags, inline styles, list/break usage, casing, punctuation, and link density. Visual rendering is governed by the site stylesheet, so this report focuses on *the markup the postings emit* — that is what produces the visual differences a reader sees on the page.

---

## 1. TL;DR — the biggest visual inconsistencies

| # | Inconsistency | How many postings | Why it matters |
|---|---------------|-------------------|----------------|
| 1 | **Section headings use two different HTML mechanisms.** Most postings render headings as a bold paragraph (`<p><strong>About the role</strong></p>`); 16 emit real `<h2>`/`<h3>`/`<h1>` headings instead. | 88 bold-paragraph style, **16 use real headings** | Bold-paragraph headings inherit body text size/weight; real headings inherit a much larger and bolder typographic scale. Side-by-side they look noticeably different. |
| 2 | **Heading-level chaos.** Among the 16 postings that use real headings: 1 uses `<h1>`, 9 use `<h2>`, 6 use `<h3>`, and 1 mixes `<h2>`+`<h3>`. | 16 postings, **4 different level patterns** | The same section ("About the Role") renders in 3+ different font sizes depending on which posting you opened. |
| 3 | **Casing of section labels is not standardized.** "About the role" appears as `About the role` (43×), `About the Role` (22×), `About The Role` (1×). | Affects most common sections | The page-to-page reading experience flickers between sentence case and title case. |
| 4 | **Trailing colon usage is mixed** — some postings end headings with `:` ("About the role:"), others don't ("About the role"). | 6 postings even mix both styles **within a single posting** | Inconsistent terminal punctuation at the section level. |
| 5 | **Intro paragraph hyperlinking is inconsistent.** All 104 postings use the *same* opening "Skydio is the leading US drone company…" paragraph, but 38 render it as **plain text** while 66 render it with 4 in-text hyperlinks to product/solutions pages. | 38 plain / 66 linked | Same words, different blue underlined links — visibly different on the page, and it splits SEO equity. |
| 6 | **`<br>` tags scattered in bullets.** 43 postings contain stray `<br>` line breaks (often at the end of `<li>` items: 13 postings); the rest don't. | 43 of 104 | Adds extra vertical whitespace below random bullets — looks like a copy/paste artefact. |
| 7 | **Empty `<p></p>` paragraphs.** 42 postings contain one or more empty paragraphs, producing an inconsistent vertical gap before the *Compensation:* block. | 42 of 104 | Same content, different vertical rhythm. |
| 8 | **Italic-bold mixing.** 2 postings put requirements lines inside `<em><strong>…</strong></em>` (italic-bold); no other posting does. | 2 postings | A handful of bullets visually shout in italic-bold. |
| 9 | **Underline styling.** 7 postings include `<u>` tags (mostly recruiter/legal/EE roles); the rest never use underline. | 7 postings | Underlined text on a web page typically signals a link — using it as emphasis is jarring. |
| 10 | **6 postings have NO compensation block at all** (whereas the other 98 do). | 6 postings | A consistency *and* legal/transparency issue. |

---

## 2. The two formatting "templates" in use

Across the 104 postings I can see **two distinct authoring templates** plus several one-off variants:

| Template | Count | How it marks up section headings | How it marks up sub-points |
|---|---:|---|---|
| **Template A — "bold paragraph"** (most common) | 88 | `<p><strong>Section Name:</strong></p>` — renders at body font size, only the *weight* changes | `<ul><li><p>…</p></li></ul>` |
| **Template B — "real headings"** | 12 | `<h2>` (9×), `<h3>` (6×), `<h1>` (1×) — renders at the site's heading typographic scale | `<ul><li><p>…</p></li></ul>` (same) |
| **Template C — mixed** (real headings *and* bold-paragraph headings in the same posting) | 4 | Both, inconsistently | Same |

A simple way to test this yourself: open any two postings from the lists below side-by-side and look at the font size of "About the role" — postings in Template A render it the same size as the body paragraph; postings in Template B render it noticeably larger and bolder.

### Postings using Template B (real headings) — visually larger section labels
| Title | Heading levels used | Heading texts |
|---|---|---|
| [Aviation Compliance Lead](https://www.skydio.com/jobs/b9f9047b-1555-4978-9bff-70eae58a6b17/?gh_jid=b9f9047b-1555-4978-9bff-70eae58a6b17) | `<h2>`×3 | `About the Role` · `How You’ll Make an Impact` · `What Makes You a Good Fit` |
| [Aviation Regulatory Program Manager](https://www.skydio.com/jobs/d73ae64d-5877-4ab6-ad42-0224702f3fba/?gh_jid=d73ae64d-5877-4ab6-ad42-0224702f3fba) | `<h2>`×3 | `About the Role` · `How You’ll Make an Impact` · `What Makes You a Good Fit` |
| [Communications Manager](https://www.skydio.com/jobs/50567d8d-2903-494f-8e08-7c8ca734dc3a/?gh_jid=50567d8d-2903-494f-8e08-7c8ca734dc3a) | `<h2>`×3 | `About the role` · `How you'll make an impact` · `What makes you a good fit` |
| [Full Stack Product Counsel](https://www.skydio.com/jobs/c9e40dab-ae7d-4034-a335-b3e05d419672/?gh_jid=c9e40dab-ae7d-4034-a335-b3e05d419672) | `<h3>`×4 | `About the Team` · `About the Role` · `How You’ll Make an Impact` · `What Makes You a Great Fit` |
| [Hardware Engineering Program Manager](https://www.skydio.com/jobs/b49e6784-2183-4de4-a0a1-7661203c254a/?gh_jid=b49e6784-2183-4de4-a0a1-7661203c254a) | `<h2>`×3, `<h3>`×5 | `About the role` · `How you'll make an impact` · `Program Leadership & Execution` · `Cross-Functional Engineering Integration` · `Supplier & Manufacturing Engagement` · `What makes you a good fit` |
| [PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning)](https://www.skydio.com/jobs/f8225008-00b5-415e-9a48-c9b6eba9363c/?gh_jid=f8225008-00b5-415e-9a48-c9b6eba9363c) | `<h3>`×3 | `How you'll make an impact:` · `What makes this internship different:` · `What makes you a strong fit:` |
| [Revenue Operations Engineer, Quoting Systems](https://www.skydio.com/jobs/02d54431-2747-417d-8234-e72c316fed87/?gh_jid=02d54431-2747-417d-8234-e72c316fed87) | `<h2>`×5 | `What you’ll drive (scope):` · `Day-to-day responsibilities:` · `Tech stack you’ll work with:` · `What you’ll bring:` · `Reporting & Working Model:` |
| [Senior Business Operations Manager](https://www.skydio.com/jobs/17b9ecf9-7a47-4811-b035-e1b9a54966aa/?gh_jid=17b9ecf9-7a47-4811-b035-e1b9a54966aa) | `<h3>`×3 | `Strategic Sourcing:` · `Cost Management` · `Strategy & Operations` |
| [Senior Buyer](https://www.skydio.com/jobs/5d32766d-990a-4c4c-a8c6-5e934dd8bd38/?gh_jid=5d32766d-990a-4c4c-a8c6-5e934dd8bd38) | `<h2>`×2 | `How you will make an impact:` · `What makes you a strong fit:` |
| [Senior Technical Support Representative - Japan](https://www.skydio.com/jobs/f714e85f-31df-494e-bac4-1dd61d4d6066/?gh_jid=f714e85f-31df-494e-bac4-1dd61d4d6066) | `<h1>`×3 | `About the role:` · `How you’ll make an impact:` · `What would make you a good fit:` |
| [Software Engineer - Autonomy Infrastructure, Systems and Tools](https://www.skydio.com/jobs/9e42a7af-6369-4036-ae6f-6626ee3a4fb3/?gh_jid=9e42a7af-6369-4036-ae6f-6626ee3a4fb3) | `<h2>`×5 | `About the Role:` · `Areas of Responsibility:` · `What You’ll Do:` · `Qualifications:` · `Bonus Experience:` |
| [Software Engineer - Autonomy Infrastructure, Systems and Tools](https://www.skydio.com/jobs/9fc135c5-7a87-410d-8323-e0f918585ebc/?gh_jid=9fc135c5-7a87-410d-8323-e0f918585ebc) | `<h2>`×5 | `About the Role:` · `Areas of Responsibility:` · `What You’ll Do:` · `Qualifications:` · `Bonus Experience:` |
| [Software Engineer - Cloud Simulation & Full-Stack](https://www.skydio.com/jobs/7d7dfadc-c6fd-4958-8d59-004a91bff55e/?gh_jid=7d7dfadc-c6fd-4958-8d59-004a91bff55e) | `<h2>`×5 | `About the Role:` · `Areas of Responsibility:` · `What You’ll Do:` · `Qualifications:` · `Bonus Experience:` |
| [Software Engineer - Cloud Simulation & Full-Stack](https://www.skydio.com/jobs/948bddb5-4679-4c7c-bf57-960a0fd1a7ed/?gh_jid=948bddb5-4679-4c7c-bf57-960a0fd1a7ed) | `<h2>`×5 | `About the Role:` · `Areas of Responsibility:` · `What You’ll Do:` · `Qualifications:` · `Bonus Experience:` |
| [Software Engineer - Simulation & Robotics Engineer](https://www.skydio.com/jobs/7a8f3e6c-d576-41af-a81e-bf4fe20da12a/?gh_jid=7a8f3e6c-d576-41af-a81e-bf4fe20da12a) | `<h3>`×5 | `About the Role:` · `Areas of Responsibility:` · `What You’ll Do:` · `Qualifications:` · `Bonus Experience:` |
| [Software Engineer - Simulation & Robotics Engineer](https://www.skydio.com/jobs/abd4addb-2d11-4207-b3a2-446a09121e39/?gh_jid=abd4addb-2d11-4207-b3a2-446a09121e39) | `<h3>`×5 | `About the Role:` · `Areas of Responsibility:` · `What You’ll Do:` · `Qualifications:` · `Bonus Experience:` |

---

## 3. Inconsistencies in section-heading **text**

Same conceptual section, multiple spellings/casings used across the postings:

| Canonical section | Variants observed (count × exact text) |
|---|---|
| *what makes you a good fit* | **50×** `What makes you a good fit` · **16×** `What Makes You a Good Fit` · **1×** `What Makes You A Good Fit` |
| *about the role* | **43×** `About the role` · **22×** `About the Role` · **1×** `About The Role` |
| *how you'll make an impact* | **23×** `How you'll make an impact` · **1×** `How You'll Make an Impact` |
| *how you’ll make an impact* | **15×** `How You’ll Make an Impact` · **8×** `How you’ll make an impact` |
| *about the team* | **7×** `About the Team` · **5×** `About the team` |
| *what would make you a good fit* | **6×** `What would make you a good fit` · **2×** `What Would Make You a Good Fit` |
| *bonus points* | **3×** `Bonus Points` · **2×** `Bonus points` |
| *nice to have* | **2×** `Nice to have` · **1×** `Nice to Have` |

**Trailing-colon usage:** 87 postings have at least one section heading ending in `:`; 8 have at least one without `:`. **6 postings mix both styles in the same posting.**

Hybrid-colon postings (mix `Heading:` with `Heading` in the same body):
- [Director, Growth Marketing - Commercial](https://www.skydio.com/jobs/00d0bdc5-89ad-4182-8512-ab0a028953f6/?gh_jid=00d0bdc5-89ad-4182-8512-ab0a028953f6)
- [Senior People Analytics Analyst](https://www.skydio.com/jobs/0703aaa0-9fcb-4b22-ad8c-b53e74151a72/?gh_jid=0703aaa0-9fcb-4b22-ad8c-b53e74151a72)
- [Customer Success Manager, DFR Majors - Southeast](https://www.skydio.com/jobs/3d4ac015-a6db-4a8d-9fec-557eb92eaf8d/?gh_jid=3d4ac015-a6db-4a8d-9fec-557eb92eaf8d)
- [Mission Success Operations Manager](https://www.skydio.com/jobs/501a3067-e906-4354-b211-ac70db6accf4/?gh_jid=501a3067-e906-4354-b211-ac70db6accf4)
- [Success Systems Specialist ](https://www.skydio.com/jobs/8de95d05-a601-47e2-8a13-5ba4d7ad428a/?gh_jid=8de95d05-a601-47e2-8a13-5ba4d7ad428a)
- [Senior Software Engineer,  Data Platform ](https://www.skydio.com/jobs/aeaa130d-3e8b-42c5-a805-46f056e62fda/?gh_jid=aeaa130d-3e8b-42c5-a805-46f056e62fda)

### Most common section labels (across all 104 postings)
| Count | Section name |
|---:|---|
| 50 | `What makes you a good fit` |
| 43 | `About the role` |
| 23 | `How you'll make an impact` |
| 22 | `About the Role` |
| 16 | `What Makes You a Good Fit` |
| 15 | `How You’ll Make an Impact` |
| 8 | `How you’ll make an impact` |
| 7 | `About the Team` |
| 6 | `What would make you a good fit` |
| 5 | `About the team` |
| 4 | `Bonus points for` |
| 3 | `Bonus Points` |
| 3 | `How you will make an impact` |
| 2 | `What Would Make You a Good Fit` |
| 2 | `Preferred Qualifications` |

---

## 4. Intro-paragraph hyperlinking is inconsistent

Every posting begins with **exactly the same** intro paragraph:

> *"Skydio is the leading US drone company and the world leader in autonomous flight, the key technology for the future of drones and aerial mobility. The Skydio team combines deep expertise in artificial intelligence, best-in-class hardware and software product development, operational excellence, and customer obsession to empower a broader, more diverse audience of drone users, from utility inspectors to first responders, soldiers in battlefield scenarios, and beyond."*

However, the markup differs:

- **66 postings** wrap "utility inspectors", "first responders", "soldiers in battlefield scenarios", "beyond" (and sometimes more) as inline hyperlinks to `/solutions/*` URLs.
- **38 postings** render the same sentence as plain text with no links at all.

Link-count distribution across pre-comp bodies: 
`0 links`: 38 jobs  · `1 links`: 1 jobs  · `4 links`: 58 jobs  · `5 links`: 6 jobs  · `6 links`: 1 jobs

**Most-affected: jobs with zero hyperlinks** (sample of the 38):
- [Revenue Operations Engineer, Quoting Systems](https://www.skydio.com/jobs/02d54431-2747-417d-8234-e72c316fed87/?gh_jid=02d54431-2747-417d-8234-e72c316fed87)
- [Senior Revenue Operations Manager](https://www.skydio.com/jobs/05e9f029-3a9d-4956-a4c8-e0bc786dd86a/?gh_jid=05e9f029-3a9d-4956-a4c8-e0bc786dd86a)
- [Enterprise Account Manager (MoD/ MoI) – EMEA (Germany)](https://www.skydio.com/jobs/12e9a494-9a89-457c-9dc7-2ef9ccdba17c/?gh_jid=12e9a494-9a89-457c-9dc7-2ef9ccdba17c)
- [Senior NPI Product Quality Engineer](https://www.skydio.com/jobs/178a7e84-562e-40db-9abd-94bbf29159ca/?gh_jid=178a7e84-562e-40db-9abd-94bbf29159ca)
- [Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland)](https://www.skydio.com/jobs/1d4977a2-c2e7-44ad-820b-253ff8355800/?gh_jid=1d4977a2-c2e7-44ad-820b-253ff8355800)
- [Autonomy Engineer - Fixed Wing Planning & Controls](https://www.skydio.com/jobs/20754382-05e7-4cb6-a0f9-0daf9338ba78/?gh_jid=20754382-05e7-4cb6-a0f9-0daf9338ba78)
- [Customer Success Manager, DFR Majors - Northeast](https://www.skydio.com/jobs/23721f25-7d5f-45fa-a5fe-d58f9680e1ef/?gh_jid=23721f25-7d5f-45fa-a5fe-d58f9680e1ef)
- [GTM Enablement Associate](https://www.skydio.com/jobs/2b3fea3b-e1b5-4497-9607-e9864019b0e7/?gh_jid=2b3fea3b-e1b5-4497-9607-e9864019b0e7)
- [Supply Chain Intern](https://www.skydio.com/jobs/2d21f482-3224-4906-a1bb-6a64436774cb/?gh_jid=2d21f482-3224-4906-a1bb-6a64436774cb)
- [Staff Global Supply Manager,  Mechanicals](https://www.skydio.com/jobs/2ffe6453-4a2f-4dfb-94f8-882f731a11ae/?gh_jid=2ffe6453-4a2f-4dfb-94f8-882f731a11ae)
- [Staff Software Engineer, Full Stack](https://www.skydio.com/jobs/379b23ea-14ff-4602-9b79-52d00bb96fda/?gh_jid=379b23ea-14ff-4602-9b79-52d00bb96fda)
- [Mission Success Operations Manager](https://www.skydio.com/jobs/501a3067-e906-4354-b211-ac70db6accf4/?gh_jid=501a3067-e906-4354-b211-ac70db6accf4)
- [Staff Software Engineer, Frontend](https://www.skydio.com/jobs/54654035-a78a-4e5b-9ebf-ae4067e5a246/?gh_jid=54654035-a78a-4e5b-9ebf-ae4067e5a246)
- [Hardware Operations Program Manager](https://www.skydio.com/jobs/55b393cf-124c-46f8-bd83-8c62e3ce628b/?gh_jid=55b393cf-124c-46f8-bd83-8c62e3ce628b)
- [Autonomy Engineer - Deep Learning Model Acceleration](https://www.skydio.com/jobs/5892ea83-ad5a-480a-bd9f-2409bb0b644e/?gh_jid=5892ea83-ad5a-480a-bd9f-2409bb0b644e)
- [Senior Autonomy Engineer - Controls ](https://www.skydio.com/jobs/58b4cdf6-5630-4dd0-aab3-a1ed4d599466/?gh_jid=58b4cdf6-5630-4dd0-aab3-a1ed4d599466)
- [Senior Brand Designer (Contract)](https://www.skydio.com/jobs/5ae7e25f-7da3-4523-a8be-8866aa89e8df/?gh_jid=5ae7e25f-7da3-4523-a8be-8866aa89e8df)
- [Sales Planning Analyst Intern](https://www.skydio.com/jobs/712900e5-ff75-4e07-8f88-626d4f8ab653/?gh_jid=712900e5-ff75-4e07-8f88-626d4f8ab653)
- [Software Engineer - Simulation & Robotics Engineer](https://www.skydio.com/jobs/7a8f3e6c-d576-41af-a81e-bf4fe20da12a/?gh_jid=7a8f3e6c-d576-41af-a81e-bf4fe20da12a)
- [Software Engineer - Cloud Simulation & Full-Stack](https://www.skydio.com/jobs/7d7dfadc-c6fd-4958-8d59-004a91bff55e/?gh_jid=7d7dfadc-c6fd-4958-8d59-004a91bff55e)
- …and 18 more

---

## 5. List & line-break inconsistencies

**`<br>` tags inside the body** — 43 of 104 postings include at least one `<br>` tag in the pre-compensation content; the other 61 have none. The most common pattern is a trailing `<br />` at the *end* of `<li>` bullets (13 postings), which inserts a blank line under those bullets while neighbouring bullets sit flush.

Distribution of `<br>` counts per posting (excluding zero): `1`×16, `2`×15, `3`×1, `4`×5, `6`×3, `8`×2, `9`×1

Worst offenders (most `<br>` tags):
- [IT Technician (Help Desk - Linux Focus)](https://www.skydio.com/jobs/28c865cf-6aa4-45d1-ae13-34bb8f6b776b/?gh_jid=28c865cf-6aa4-45d1-ae13-34bb8f6b776b) — 9 `<br>` tag(s)
- [Director, Growth Marketing - Commercial](https://www.skydio.com/jobs/00d0bdc5-89ad-4182-8512-ab0a028953f6/?gh_jid=00d0bdc5-89ad-4182-8512-ab0a028953f6) — 8 `<br>` tag(s)
- [Autonomy Engineer - Deep Learning Infrastructure](https://www.skydio.com/jobs/dcb04687-9b4f-425d-8c37-1111cf3ccf3d/?gh_jid=dcb04687-9b4f-425d-8c37-1111cf3ccf3d) — 8 `<br>` tag(s)
- [Autonomy Engineer - Deep Learning Model Acceleration](https://www.skydio.com/jobs/5892ea83-ad5a-480a-bd9f-2409bb0b644e/?gh_jid=5892ea83-ad5a-480a-bd9f-2409bb0b644e) — 6 `<br>` tag(s)
- [Autonomy Engineer - Deep Learning Infrastructure](https://www.skydio.com/jobs/c051266c-3e00-4906-abd0-21f18db56b3f/?gh_jid=c051266c-3e00-4906-abd0-21f18db56b3f) — 6 `<br>` tag(s)
- [Autonomy Engineer - Deep Learning Model Acceleration](https://www.skydio.com/jobs/cd6d8410-419b-4713-8d4d-7eb72b134d5a/?gh_jid=cd6d8410-419b-4713-8d4d-7eb72b134d5a) — 6 `<br>` tag(s)
- [Revenue Operations Engineer, Quoting Systems](https://www.skydio.com/jobs/02d54431-2747-417d-8234-e72c316fed87/?gh_jid=02d54431-2747-417d-8234-e72c316fed87) — 4 `<br>` tag(s)
- [Director of Product Management, Drone as First Responder (DFR)](https://www.skydio.com/jobs/129a5bad-ca1d-4eda-843b-96f4581f3c43/?gh_jid=129a5bad-ca1d-4eda-843b-96f4581f3c43) — 4 `<br>` tag(s)
- [Senior Technical Recruiter - Hardware Operations](https://www.skydio.com/jobs/737c02d2-f03f-4716-a0c8-e14a0307f8cb/?gh_jid=737c02d2-f03f-4716-a0c8-e14a0307f8cb) — 4 `<br>` tag(s)
- [Autonomy Software Engineer](https://www.skydio.com/jobs/a48fe41b-030b-4f11-bf25-df7446151854/?gh_jid=a48fe41b-030b-4f11-bf25-df7446151854) — 4 `<br>` tag(s)

**Empty paragraphs** — 42 postings contain `<p></p>` (or `<p><br></p>`) blocks. These typically appear immediately above a section heading, creating a double-gap.
Worst offenders:
- [Full Stack Product Counsel](https://www.skydio.com/jobs/c9e40dab-ae7d-4034-a335-b3e05d419672/?gh_jid=c9e40dab-ae7d-4034-a335-b3e05d419672) — 8 empty paragraph(s)
- [Senior Product Manager, Platform & Infrastructure](https://www.skydio.com/jobs/8d67884d-58f4-41a7-8740-ab65d3c03fa8/?gh_jid=8d67884d-58f4-41a7-8740-ab65d3c03fa8) — 5 empty paragraph(s)
- [Staff Product Manager, Platform & Infrastructure](https://www.skydio.com/jobs/dbd737b2-beed-4917-9948-dde4250929a8/?gh_jid=dbd737b2-beed-4917-9948-dde4250929a8) — 5 empty paragraph(s)
- [Deployment Engineer - Southeast](https://www.skydio.com/jobs/6138ba1c-c048-407d-9ea2-7b51a3d38756/?gh_jid=6138ba1c-c048-407d-9ea2-7b51a3d38756) — 4 empty paragraph(s)
- [Director, Growth Marketing - Commercial](https://www.skydio.com/jobs/00d0bdc5-89ad-4182-8512-ab0a028953f6/?gh_jid=00d0bdc5-89ad-4182-8512-ab0a028953f6) — 3 empty paragraph(s)
- [Senior/Staff Embedded Software Engineer – Camera Systems](https://www.skydio.com/jobs/71033170-d9d0-474b-b712-a11e4f11c146/?gh_jid=71033170-d9d0-474b-b712-a11e4f11c146) — 3 empty paragraph(s)
- [Sr/Staff Embedded Software Engineer - Camera Systems](https://www.skydio.com/jobs/898a9c77-cc20-4ed6-a050-f68e5c15d5c8/?gh_jid=898a9c77-cc20-4ed6-a050-f68e5c15d5c8) — 3 empty paragraph(s)
- [Senior Software Engineer - Mobile Platform ](https://www.skydio.com/jobs/e8cb16b0-d2f0-4cb4-a1a1-0f43d195cc9a/?gh_jid=e8cb16b0-d2f0-4cb4-a1a1-0f43d195cc9a) — 3 empty paragraph(s)
- [Senior Revenue Operations Manager](https://www.skydio.com/jobs/05e9f029-3a9d-4956-a4c8-e0bc786dd86a/?gh_jid=05e9f029-3a9d-4956-a4c8-e0bc786dd86a) — 2 empty paragraph(s)
- [Senior Business Operations Manager](https://www.skydio.com/jobs/17b9ecf9-7a47-4811-b035-e1b9a54966aa/?gh_jid=17b9ecf9-7a47-4811-b035-e1b9a54966aa) — 2 empty paragraph(s)

**Ordered vs unordered lists:** 100% of postings use `<ul>`; no posting uses `<ol>`. ✅

---

## 6. Emphasis & font-style inconsistencies

**Italic-bold (`<em><strong>…</strong></em>`)** — used by **2 posting(s)** only. The italic-bold bullet appears to be emphasising the in-office attendance requirement (e.g. "*Ability to be in our San Mateo, CA office 3 days per week*") — no other posting visually emphasises that line, even when the requirement is included:
- [Director, Growth Marketing - Commercial](https://www.skydio.com/jobs/00d0bdc5-89ad-4182-8512-ab0a028953f6/?gh_jid=00d0bdc5-89ad-4182-8512-ab0a028953f6)
- [Senior NPI Product Quality Engineer](https://www.skydio.com/jobs/178a7e84-562e-40db-9abd-94bbf29159ca/?gh_jid=178a7e84-562e-40db-9abd-94bbf29159ca)

**Underline (`<u>`)** — used by **7 posting(s)**; every other posting avoids `<u>` entirely:
- [Senior Technical Recruiter](https://www.skydio.com/jobs/16b0647d-a470-4917-9bb9-a95967828edc/?gh_jid=16b0647d-a470-4917-9bb9-a95967828edc)
- [Senior NPI Product Quality Engineer](https://www.skydio.com/jobs/178a7e84-562e-40db-9abd-94bbf29159ca/?gh_jid=178a7e84-562e-40db-9abd-94bbf29159ca)
- [Lead Staff Electrical Engineer](https://www.skydio.com/jobs/1bbcf144-7057-4a6e-9d51-4924bfda52b9/?gh_jid=1bbcf144-7057-4a6e-9d51-4924bfda52b9)
- [Senior Software Engineer, Full Stack](https://www.skydio.com/jobs/5655fbe3-66b0-4951-afdc-3b67f71e6938/?gh_jid=5655fbe3-66b0-4951-afdc-3b67f71e6938)
- [Senior Technical Recruiter - Hardware Operations](https://www.skydio.com/jobs/737c02d2-f03f-4716-a0c8-e14a0307f8cb/?gh_jid=737c02d2-f03f-4716-a0c8-e14a0307f8cb)
- [Staff Technical Recruiter](https://www.skydio.com/jobs/c3a4256a-4525-443c-81d0-6f69e7c24805/?gh_jid=c3a4256a-4525-443c-81d0-6f69e7c24805)
- [Full Stack Product Counsel](https://www.skydio.com/jobs/c9e40dab-ae7d-4034-a335-b3e05d419672/?gh_jid=c9e40dab-ae7d-4034-a335-b3e05d419672)
Underlined text on the web typically signals a link. Using it as emphasis is jarring and reduces accessibility.

**Inline `style="…"` attributes** — used by **1 posting(s)**:
- [Manager, Logistics ](https://www.skydio.com/jobs/eeb4b52f-d4e6-4823-9e4b-0ce75041d928/?gh_jid=eeb4b52f-d4e6-4823-9e4b-0ce75041d928)
No posting overrides `font-size`, `font-weight`, or `color` via inline CSS — colour, weight, and size differences come entirely from the *choice of HTML element* (bold-paragraph vs. real heading, plain text vs. `<u>`, etc.).

---

## 7. Missing compensation block (postings that *omit* the entire compensation section)

6 of 104 postings have **no compensation block** anywhere in the body — meaning everything up to the end of the description was scanned and no `Compensation:` paragraph or heading was found. This is both a visual *and* a transparency/compliance inconsistency:

| Title | Location & type | Link |
|---|---|---|
| Supplier Quality Engineer, Sustaining | Taiwan - Full-time | [view](https://www.skydio.com/jobs/4c4874bf-02da-4ccc-8918-2cca08feaf21/?gh_jid=4c4874bf-02da-4ccc-8918-2cca08feaf21) |
| Autonomy Engineer Intern - Deep Learning (Computational Photography) | Zurich, Switzerland or Tampere, Finland - Intern | [view](https://www.skydio.com/jobs/6280ab1d-147d-4f39-8618-a216c18ce0f9/?gh_jid=6280ab1d-147d-4f39-8618-a216c18ce0f9) |
| Full Stack Product Counsel | San Mateo, California, United States - Full-time | [view](https://www.skydio.com/jobs/c9e40dab-ae7d-4034-a335-b3e05d419672/?gh_jid=c9e40dab-ae7d-4034-a335-b3e05d419672) |
| Workplace Experience Coordinator Part-Time | Zurich, Switzerland - Part-time | [view](https://www.skydio.com/jobs/d023afe5-f19f-42f7-a1dd-aa94a361b86f/?gh_jid=d023afe5-f19f-42f7-a1dd-aa94a361b86f) |
| Autonomy Engineer Intern - Deep Learning (Computational Photography) | San Mateo, California, United States - Intern | [view](https://www.skydio.com/jobs/d13e3179-e646-4873-84a6-d492a692bc25/?gh_jid=d13e3179-e646-4873-84a6-d492a692bc25) |
| Senior Technical Support Representative - Japan | Tokyo, Japan - Full-time | [view](https://www.skydio.com/jobs/f714e85f-31df-494e-bac4-1dd61d4d6066/?gh_jid=f714e85f-31df-494e-bac4-1dd61d4d6066) |

---

## 8. Postings that stand out the most from the norm

Synthesising the above, these are the postings that diverge most strongly from the "typical" Skydio posting (Template A, bold-paragraph headings, hyperlinked intro, ~350 words, no `<br>`/`<u>`/`<em><strong>`, with a compensation block):

| Score | Title | Why it stands out |
|---:|---|---|
| 10 | [Full Stack Product Counsel](https://www.skydio.com/jobs/c9e40dab-ae7d-4034-a335-b3e05d419672/?gh_jid=c9e40dab-ae7d-4034-a335-b3e05d419672) | uses real `<h3>` headings (4×); contains 8 empty paragraph(s); uses underline (`<u>`); **no compensation block at all** |
| 8 | [Revenue Operations Engineer, Quoting Systems](https://www.skydio.com/jobs/02d54431-2747-417d-8234-e72c316fed87/?gh_jid=02d54431-2747-417d-8234-e72c316fed87) | uses real `<h2>` headings (5×); mixes bold-paragraph **and** HTML headings; intro paragraph has 0 hyperlinks; contains 4 stray `<br>` tags |
| 8 | [Senior Technical Support Representative - Japan](https://www.skydio.com/jobs/f714e85f-31df-494e-bac4-1dd61d4d6066/?gh_jid=f714e85f-31df-494e-bac4-1dd61d4d6066) | uses real `<h1>` headings (3×); contains 2 stray `<br>` tag(s); **no compensation block at all** |
| 6 | [Senior Business Operations Manager](https://www.skydio.com/jobs/17b9ecf9-7a47-4811-b035-e1b9a54966aa/?gh_jid=17b9ecf9-7a47-4811-b035-e1b9a54966aa) | uses real `<h3>` headings (3×); mixes bold-paragraph **and** HTML headings; contains 2 empty paragraph(s) |
| 6 | [Senior Buyer](https://www.skydio.com/jobs/5d32766d-990a-4c4c-a8c6-5e934dd8bd38/?gh_jid=5d32766d-990a-4c4c-a8c6-5e934dd8bd38) | uses real `<h2>` headings (2×); mixes bold-paragraph **and** HTML headings; contains 2 empty paragraph(s) |
| 5 | [Director, Growth Marketing - Commercial](https://www.skydio.com/jobs/00d0bdc5-89ad-4182-8512-ab0a028953f6/?gh_jid=00d0bdc5-89ad-4182-8512-ab0a028953f6) | contains 8 stray `<br>` tags; contains 3 empty paragraph(s); uses italic-bold (`<em><strong>`) |
| 5 | [Senior NPI Product Quality Engineer](https://www.skydio.com/jobs/178a7e84-562e-40db-9abd-94bbf29159ca/?gh_jid=178a7e84-562e-40db-9abd-94bbf29159ca) | intro paragraph has 0 hyperlinks; uses italic-bold (`<em><strong>`); uses underline (`<u>`) |
| 5 | [Aviation Compliance Lead](https://www.skydio.com/jobs/b9f9047b-1555-4978-9bff-70eae58a6b17/?gh_jid=b9f9047b-1555-4978-9bff-70eae58a6b17) | uses real `<h2>` headings (3×); intro paragraph has 0 hyperlinks; contains 1 stray `<br>` tag(s) |
| 5 | [Workplace Experience Coordinator Part-Time](https://www.skydio.com/jobs/d023afe5-f19f-42f7-a1dd-aa94a361b86f/?gh_jid=d023afe5-f19f-42f7-a1dd-aa94a361b86f) | contains 1 stray `<br>` tag(s); **no compensation block at all** |
| 5 | [PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning)](https://www.skydio.com/jobs/f8225008-00b5-415e-9a48-c9b6eba9363c/?gh_jid=f8225008-00b5-415e-9a48-c9b6eba9363c) | uses real `<h3>` headings (3×); mixes bold-paragraph **and** HTML headings |
| 4 | [Supplier Quality Engineer, Sustaining](https://www.skydio.com/jobs/4c4874bf-02da-4ccc-8918-2cca08feaf21/?gh_jid=4c4874bf-02da-4ccc-8918-2cca08feaf21) | **no compensation block at all** |
| 4 | [Communications Manager](https://www.skydio.com/jobs/50567d8d-2903-494f-8e08-7c8ca734dc3a/?gh_jid=50567d8d-2903-494f-8e08-7c8ca734dc3a) | uses real `<h2>` headings (3×); contains 2 empty paragraph(s) |
| 4 | [Autonomy Engineer Intern - Deep Learning (Computational Photography)](https://www.skydio.com/jobs/6280ab1d-147d-4f39-8618-a216c18ce0f9/?gh_jid=6280ab1d-147d-4f39-8618-a216c18ce0f9) | **no compensation block at all** |
| 4 | [Senior Technical Recruiter - Hardware Operations](https://www.skydio.com/jobs/737c02d2-f03f-4716-a0c8-e14a0307f8cb/?gh_jid=737c02d2-f03f-4716-a0c8-e14a0307f8cb) | contains 4 stray `<br>` tags; uses underline (`<u>`) |
| 4 | [Software Engineer - Simulation & Robotics Engineer](https://www.skydio.com/jobs/7a8f3e6c-d576-41af-a81e-bf4fe20da12a/?gh_jid=7a8f3e6c-d576-41af-a81e-bf4fe20da12a) | uses real `<h3>` headings (5×); intro paragraph has 0 hyperlinks |
| 4 | [Software Engineer - Cloud Simulation & Full-Stack](https://www.skydio.com/jobs/7d7dfadc-c6fd-4958-8d59-004a91bff55e/?gh_jid=7d7dfadc-c6fd-4958-8d59-004a91bff55e) | uses real `<h2>` headings (5×); intro paragraph has 0 hyperlinks |
| 4 | [Software Engineer - Cloud Simulation & Full-Stack](https://www.skydio.com/jobs/948bddb5-4679-4c7c-bf57-960a0fd1a7ed/?gh_jid=948bddb5-4679-4c7c-bf57-960a0fd1a7ed) | uses real `<h2>` headings (5×); intro paragraph has 0 hyperlinks |
| 4 | [Software Engineer - Autonomy Infrastructure, Systems and Tools](https://www.skydio.com/jobs/9e42a7af-6369-4036-ae6f-6626ee3a4fb3/?gh_jid=9e42a7af-6369-4036-ae6f-6626ee3a4fb3) | uses real `<h2>` headings (5×); intro paragraph has 0 hyperlinks |
| 4 | [Software Engineer - Autonomy Infrastructure, Systems and Tools](https://www.skydio.com/jobs/9fc135c5-7a87-410d-8323-e0f918585ebc/?gh_jid=9fc135c5-7a87-410d-8323-e0f918585ebc) | uses real `<h2>` headings (5×); intro paragraph has 0 hyperlinks |
| 4 | [Software Engineer - Simulation & Robotics Engineer](https://www.skydio.com/jobs/abd4addb-2d11-4207-b3a2-446a09121e39/?gh_jid=abd4addb-2d11-4207-b3a2-446a09121e39) | uses real `<h3>` headings (5×); intro paragraph has 0 hyperlinks |
| 4 | [Hardware Engineering Program Manager](https://www.skydio.com/jobs/b49e6784-2183-4de4-a0a1-7661203c254a/?gh_jid=b49e6784-2183-4de4-a0a1-7661203c254a) | uses real `<h2/h3>` headings (8×); contains 2 empty paragraph(s) |
| 4 | [Autonomy Engineer Intern - Deep Learning (Computational Photography)](https://www.skydio.com/jobs/d13e3179-e646-4873-84a6-d492a692bc25/?gh_jid=d13e3179-e646-4873-84a6-d492a692bc25) | **no compensation block at all** |
| 4 | [Aviation Regulatory Program Manager](https://www.skydio.com/jobs/d73ae64d-5877-4ab6-ad42-0224702f3fba/?gh_jid=d73ae64d-5877-4ab6-ad42-0224702f3fba) | uses real `<h2>` headings (3×); intro paragraph has 0 hyperlinks |
| 3 | [Senior Technical Recruiter](https://www.skydio.com/jobs/16b0647d-a470-4917-9bb9-a95967828edc/?gh_jid=16b0647d-a470-4917-9bb9-a95967828edc) | contains 2 stray `<br>` tag(s); uses underline (`<u>`) |
| 3 | [Lead Staff Electrical Engineer](https://www.skydio.com/jobs/1bbcf144-7057-4a6e-9d51-4924bfda52b9/?gh_jid=1bbcf144-7057-4a6e-9d51-4924bfda52b9) | contains 1 stray `<br>` tag(s); uses underline (`<u>`) |

---

## 9. Quality issues that aren't strictly visual but worth flagging

### Job title whitespace (14 affected)
These titles have leading/trailing whitespace or double spaces, which makes them render inconsistently in listings and browser tabs:

- [` Senior Software Engineer,  Infrastructure`](https://www.skydio.com/jobs/0f71bdbb-a645-49f6-8890-dd5c052772c3/?gh_jid=0f71bdbb-a645-49f6-8890-dd5c052772c3)
- [`Staff Global Supply Manager,  Mechanicals`](https://www.skydio.com/jobs/2ffe6453-4a2f-4dfb-94f8-882f731a11ae/?gh_jid=2ffe6453-4a2f-4dfb-94f8-882f731a11ae)
- [`Senior Autonomy Engineer - Controls `](https://www.skydio.com/jobs/58b4cdf6-5630-4dd0-aab3-a1ed4d599466/?gh_jid=58b4cdf6-5630-4dd0-aab3-a1ed4d599466)
- [`Senior Software Engineer - Embedded `](https://www.skydio.com/jobs/67a7d89f-9c4e-4f60-bdf1-a60b8addd8ae/?gh_jid=67a7d89f-9c4e-4f60-bdf1-a60b8addd8ae)
- [`Success Systems Specialist `](https://www.skydio.com/jobs/8de95d05-a601-47e2-8a13-5ba4d7ad428a/?gh_jid=8de95d05-a601-47e2-8a13-5ba4d7ad428a)
- [` Electrical Engineer (Sustaining/Validation)`](https://www.skydio.com/jobs/8e50c7da-2868-4383-af1f-920584d537fc/?gh_jid=8e50c7da-2868-4383-af1f-920584d537fc)
- [`Senior Software Engineer,  Data Platform `](https://www.skydio.com/jobs/aeaa130d-3e8b-42c5-a805-46f056e62fda/?gh_jid=aeaa130d-3e8b-42c5-a805-46f056e62fda)
- [`Field Support Representative `](https://www.skydio.com/jobs/b053b0e2-005c-4e77-95f3-26c7354e6095/?gh_jid=b053b0e2-005c-4e77-95f3-26c7354e6095)
- [`Autonomy Engineer - ML & DL Infrastructure `](https://www.skydio.com/jobs/b6be08f7-89c0-48dd-b427-f587f23dbf34/?gh_jid=b6be08f7-89c0-48dd-b427-f587f23dbf34)
- [` Software Engineer - Infrastructure`](https://www.skydio.com/jobs/cb958101-ede8-4f50-bf30-b3272d33f25f/?gh_jid=cb958101-ede8-4f50-bf30-b3272d33f25f)
- [`Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM`](https://www.skydio.com/jobs/e69362bc-5891-486e-be75-6bf25187ccf5/?gh_jid=e69362bc-5891-486e-be75-6bf25187ccf5)
- [`Senior Software Engineer - Mobile Platform `](https://www.skydio.com/jobs/e8cb16b0-d2f0-4cb4-a1a1-0f43d195cc9a/?gh_jid=e8cb16b0-d2f0-4cb4-a1a1-0f43d195cc9a)
- [`Manager, Logistics `](https://www.skydio.com/jobs/eeb4b52f-d4e6-4823-9e4b-0ce75041d928/?gh_jid=eeb4b52f-d4e6-4823-9e4b-0ce75041d928)
- [`Electrical Engineer (all levels) `](https://www.skydio.com/jobs/f0c26a3c-d999-4dc2-8812-b3835f633ded/?gh_jid=f0c26a3c-d999-4dc2-8812-b3835f633ded)

### Same role, two postings — but the *body content differs*
Several roles are duplicated (one posting per location). Most duplicates have *identical* body markup, but four pairs **diverge**:

| Title | Differences |
|---|---|
| Autonomy Engineer - Deep Learning Model Acceleration | link count 0 vs 4; 427 vs 426 words |
| Senior Autonomy Engineer - Deep Learning | 297 vs 298 words |
| Autonomy Engineer - Deep Learning | link count 4 vs 0 |
| Autonomy Engineer - Deep Learning Infrastructure | link count 0 vs 4; 426 vs 458 words; 2 vs 1 bold headings |

### Length disparity
Pre-compensation word count varies from 217 to 760 words — almost a 4× range:

| Shortest 5 | Words | Longest 5 | Words |
|---|---:|---|---:|
| [Supply Chain Intern](https://www.skydio.com/jobs/2d21f482-3224-4906-a1bb-6a64436774cb/?gh_jid=2d21f482-3224-4906-a1bb-6a64436774cb) | 217 | [Senior Software Engineer,  Data Platform ](https://www.skydio.com/jobs/aeaa130d-3e8b-42c5-a805-46f056e62fda/?gh_jid=aeaa130d-3e8b-42c5-a805-46f056e62fda) | 699 |
| [Electrical Engineer (all levels) ](https://www.skydio.com/jobs/f0c26a3c-d999-4dc2-8812-b3835f633ded/?gh_jid=f0c26a3c-d999-4dc2-8812-b3835f633ded) | 224 | [Senior Product Manager, Platform & Infrastructure](https://www.skydio.com/jobs/8d67884d-58f4-41a7-8740-ab65d3c03fa8/?gh_jid=8d67884d-58f4-41a7-8740-ab65d3c03fa8) | 741 |
| [Senior Autonomy Engineer - Controls ](https://www.skydio.com/jobs/58b4cdf6-5630-4dd0-aab3-a1ed4d599466/?gh_jid=58b4cdf6-5630-4dd0-aab3-a1ed4d599466) | 232 | [Full Stack Product Counsel](https://www.skydio.com/jobs/c9e40dab-ae7d-4034-a335-b3e05d419672/?gh_jid=c9e40dab-ae7d-4034-a335-b3e05d419672) | 742 |
| [Autonomy Engineer - Fixed Wing Planning & Controls](https://www.skydio.com/jobs/20754382-05e7-4cb6-a0f9-0daf9338ba78/?gh_jid=20754382-05e7-4cb6-a0f9-0daf9338ba78) | 246 | [Manager, Technical Support](https://www.skydio.com/jobs/2b312ffb-26c3-4b7f-8904-acbc4e51934b/?gh_jid=2b312ffb-26c3-4b7f-8904-acbc4e51934b) | 749 |
| [Autonomy Engineer Intern Fall 2026](https://www.skydio.com/jobs/17f6173b-c96f-4b02-a6b5-da0a91ad95e5/?gh_jid=17f6173b-c96f-4b02-a6b5-da0a91ad95e5) | 263 | [Staff Product Manager, Platform & Infrastructure](https://www.skydio.com/jobs/dbd737b2-beed-4917-9948-dde4250929a8/?gh_jid=dbd737b2-beed-4917-9948-dde4250929a8) | 760 |

---

## 10. Recommendations — how to standardise

### Must-fix (visible, high-impact)

1. **Pick one heading mechanism for section labels and apply it everywhere.** Recommended: use a single real heading element (e.g. `<h3>`) for every section label in every posting. This:

   - Gives the same visual weight/size to "About the Role", "How You'll Make an Impact", "What Makes You a Good Fit", and "Compensation" across all 104 postings.
   - Improves accessibility (screen-readers, ARIA outline) and SEO.
   - Eliminates the bold-paragraph-vs-`<h2>`-vs-`<h3>`-vs-`<h1>` inconsistency in one move.

2. **Standardise the canonical section labels and their order.** Suggested canonical set:

   1. *About the Role*  
   2. *How You'll Make an Impact*  
   3. *What Makes You a Good Fit*  
   4. *Bonus Points* (optional)  
   5. *Compensation* (required)  

   Lock the casing (Title Case is recommended for parity with the rest of skydio.com), pick **one** punctuation rule (recommendation: **no trailing colon** when the label is a real heading), and enforce it in a CMS validator.

3. **Remove stray `<br>` tags from the end of `<li>` items.** They originate from a CMS paste — most likely from a Word/Google-Docs source. A find-and-replace on `<br/></p></li>` → `</p></li>` will fix all 43 affected postings.

4. **Strip empty `<p></p>` / `<p><br></p>` blocks** (42 postings affected). These produce inconsistent vertical rhythm above the *Compensation* block.

5. **Add a compensation block to the 6 postings missing one.** This is a fairness/transparency issue for candidates and may be a legal requirement in some of these jurisdictions.

6. **Either link or do not link the intro paragraph — choose one.** Either *all* postings inline-link the words "utility inspectors" / "first responders" / etc., or *none* of them do. Recommend **linking all** (current majority style) so the SEO equity is consistent.

### Should-fix (medium impact)

7. **Stop using `<u>` for emphasis.** Replace the 7 underline instances with `<strong>` or remove altogether — underlines look like broken links.

8. **Stop using `<em><strong>` italic-bold combos.** Pick one (recommend plain `<strong>`) and apply uniformly. Affects 2 postings today; could spread.

9. **Reorder paragraphs in the "Aviation Compliance Lead" posting** — it's the only posting that emits `<h2><strong>Compensation:</strong></h2>` instead of the plain `<p><strong>Compensation:</strong></p>` used everywhere else, which causes its compensation header to render *visibly larger* than every other posting's.

### Nice-to-have (polish)

10. **Trim job titles** — 14 titles have leading/trailing whitespace or double spaces (`"Manager, Logistics "`, `" Software Engineer - Infrastructure"`, etc.).

11. **Reconcile the 4 duplicate-role pairs whose body content has drifted apart** (different word counts, different link counts, different heading set). Treat one location as the canonical source and re-sync the other.

12. **Cap pre-compensation length to a target band** (e.g. 300–600 words). Right now it spans **217–760 words** (3.5× variance). The shortest postings (Supply Chain Intern, Electrical Engineer (all levels), Senior Autonomy Engineer - Controls) feel sparse next to the 700-word postings.

### Process / tooling suggestions

- Add a **CMS-side validator** (or a CI check on the static export) that flags any `prose block-content` body containing: `<br>` tags, empty paragraphs, `<u>` tags, `<em><strong>`, inline `style=` attributes, or a mix of bold-paragraph and real-heading section labels.

- Add a **lint rule** for the canonical section label spellings (case-insensitive match into one of the 4–5 approved labels) and reject anything else.

- Provide authors with a **single Markdown/CMS template** so new postings can't drift visually. Today the divergence suggests at least two different authoring paths (probably Greenhouse-imported HTML vs. hand-edited CMS) are reaching the live page without normalisation.

---

## Appendix A — Per-posting classification (all 104)

Sorted alphabetically. *Style* = bold-paragraph / real-heading template; *Hdrs* = real heading tags in body; *Bold*= bold-paragraph section markers; *Links/Br/E∅/U/EmSt* = link count / `<br>` count / empty `<p>` count / `<u>` count / italic-bold count; *Cmp* = has compensation block.

| Title | Style | Hdrs | Bold | Words | Links | Br | E∅ | U | EmSt | Cmp |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| [ Electrical Engineer (Sustaining/Validation)](https://www.skydio.com/jobs/8e50c7da-2868-4383-af1f-920584d537fc/?gh_jid=8e50c7da-2868-4383-af1f-920584d537fc) | bold-p | — | 2 | 274 | 4 | 1 | 0 | 0 | 0 | yes |
| [ Senior Software Engineer,  Infrastructure](https://www.skydio.com/jobs/0f71bdbb-a645-49f6-8890-dd5c052772c3/?gh_jid=0f71bdbb-a645-49f6-8890-dd5c052772c3) | bold-p | — | 2 | 379 | 4 | 0 | 0 | 0 | 0 | yes |
| [ Software Engineer - Infrastructure](https://www.skydio.com/jobs/cb958101-ede8-4f50-bf30-b3272d33f25f/?gh_jid=cb958101-ede8-4f50-bf30-b3272d33f25f) | bold-p | — | 2 | 377 | 4 | 0 | 0 | 0 | 0 | yes |
| [Autonomy Engineer - Deep Learning](https://www.skydio.com/jobs/ae12de71-0010-49d3-b171-c0b257e3b6c1/?gh_jid=ae12de71-0010-49d3-b171-c0b257e3b6c1) | bold-p | — | 3 | 346 | 4 | 0 | 0 | 0 | 0 | yes |
| [Autonomy Engineer - Deep Learning](https://www.skydio.com/jobs/cc83824e-a1cd-4bc7-9206-7264da9fbd61/?gh_jid=cc83824e-a1cd-4bc7-9206-7264da9fbd61) | bold-p | — | 3 | 346 | 0 | 0 | 0 | 0 | 0 | yes |
| [Autonomy Engineer - Deep Learning Infrastructure](https://www.skydio.com/jobs/c051266c-3e00-4906-abd0-21f18db56b3f/?gh_jid=c051266c-3e00-4906-abd0-21f18db56b3f) | bold-p | — | 1 | 426 | 0 | 6 | 0 | 0 | 0 | yes |
| [Autonomy Engineer - Deep Learning Infrastructure](https://www.skydio.com/jobs/dcb04687-9b4f-425d-8c37-1111cf3ccf3d/?gh_jid=dcb04687-9b4f-425d-8c37-1111cf3ccf3d) | bold-p | — | 1 | 458 | 4 | 8 | 0 | 0 | 0 | yes |
| [Autonomy Engineer - Deep Learning Model Acceleration](https://www.skydio.com/jobs/5892ea83-ad5a-480a-bd9f-2409bb0b644e/?gh_jid=5892ea83-ad5a-480a-bd9f-2409bb0b644e) | bold-p | — | 1 | 427 | 0 | 6 | 0 | 0 | 0 | yes |
| [Autonomy Engineer - Deep Learning Model Acceleration](https://www.skydio.com/jobs/cd6d8410-419b-4713-8d4d-7eb72b134d5a/?gh_jid=cd6d8410-419b-4713-8d4d-7eb72b134d5a) | bold-p | — | 1 | 426 | 4 | 6 | 0 | 0 | 0 | yes |
| [Autonomy Engineer - Fixed Wing Planning & Controls](https://www.skydio.com/jobs/20754382-05e7-4cb6-a0f9-0daf9338ba78/?gh_jid=20754382-05e7-4cb6-a0f9-0daf9338ba78) | bold-p | — | 3 | 246 | 0 | 0 | 0 | 0 | 0 | yes |
| [Autonomy Engineer - ML & DL Infrastructure ](https://www.skydio.com/jobs/b6be08f7-89c0-48dd-b427-f587f23dbf34/?gh_jid=b6be08f7-89c0-48dd-b427-f587f23dbf34) | bold-p | — | 3 | 433 | 4 | 0 | 2 | 0 | 0 | yes |
| [Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026](https://www.skydio.com/jobs/c84945f0-b8e0-4272-b636-265d6611a8eb/?gh_jid=c84945f0-b8e0-4272-b636-265d6611a8eb) | bold-p | — | 3 | 324 | 4 | 1 | 0 | 0 | 0 | yes |
| [Autonomy Engineer Intern - Deep Learning (Computational Photography)](https://www.skydio.com/jobs/6280ab1d-147d-4f39-8618-a216c18ce0f9/?gh_jid=6280ab1d-147d-4f39-8618-a216c18ce0f9) | bold-p | — | 3 | 541 | 5 | 0 | 0 | 0 | 0 | **NO** |
| [Autonomy Engineer Intern - Deep Learning (Computational Photography)](https://www.skydio.com/jobs/d13e3179-e646-4873-84a6-d492a692bc25/?gh_jid=d13e3179-e646-4873-84a6-d492a692bc25) | bold-p | — | 3 | 541 | 5 | 0 | 0 | 0 | 0 | **NO** |
| [Autonomy Engineer Intern Fall 2026](https://www.skydio.com/jobs/17f6173b-c96f-4b02-a6b5-da0a91ad95e5/?gh_jid=17f6173b-c96f-4b02-a6b5-da0a91ad95e5) | bold-p | — | 3 | 263 | 4 | 0 | 0 | 0 | 0 | yes |
| [Autonomy Software Engineer](https://www.skydio.com/jobs/a48fe41b-030b-4f11-bf25-df7446151854/?gh_jid=a48fe41b-030b-4f11-bf25-df7446151854) | bold-p | — | 1 | 375 | 4 | 4 | 0 | 0 | 0 | yes |
| [Aviation Compliance Lead](https://www.skydio.com/jobs/b9f9047b-1555-4978-9bff-70eae58a6b17/?gh_jid=b9f9047b-1555-4978-9bff-70eae58a6b17) | h2 | h2×3 | 0 | 378 | 0 | 1 | 1 | 0 | 0 | yes |
| [Aviation Regulatory Program Manager](https://www.skydio.com/jobs/d73ae64d-5877-4ab6-ad42-0224702f3fba/?gh_jid=d73ae64d-5877-4ab6-ad42-0224702f3fba) | h2 | h2×3 | 0 | 469 | 0 | 0 | 1 | 0 | 0 | yes |
| [Communications Manager](https://www.skydio.com/jobs/50567d8d-2903-494f-8e08-7c8ca734dc3a/?gh_jid=50567d8d-2903-494f-8e08-7c8ca734dc3a) | h2 | h2×3 | 0 | 405 | 4 | 0 | 2 | 0 | 0 | yes |
| [Customer Success Manager, DFR Majors - Northeast](https://www.skydio.com/jobs/23721f25-7d5f-45fa-a5fe-d58f9680e1ef/?gh_jid=23721f25-7d5f-45fa-a5fe-d58f9680e1ef) | bold-p | — | 3 | 478 | 0 | 0 | 0 | 0 | 0 | yes |
| [Customer Success Manager, DFR Majors - Southeast](https://www.skydio.com/jobs/3d4ac015-a6db-4a8d-9fec-557eb92eaf8d/?gh_jid=3d4ac015-a6db-4a8d-9fec-557eb92eaf8d) | bold-p | — | 4 | 466 | 4 | 0 | 0 | 0 | 0 | yes |
| [Deployment Engineer - Southeast](https://www.skydio.com/jobs/6138ba1c-c048-407d-9ea2-7b51a3d38756/?gh_jid=6138ba1c-c048-407d-9ea2-7b51a3d38756) | bold-p | — | 4 | 561 | 4 | 0 | 4 | 0 | 0 | yes |
| [Director of Product Management, Drone as First Responder (DFR)](https://www.skydio.com/jobs/129a5bad-ca1d-4eda-843b-96f4581f3c43/?gh_jid=129a5bad-ca1d-4eda-843b-96f4581f3c43) | bold-p | — | 2 | 576 | 4 | 4 | 0 | 0 | 0 | yes |
| [Director, Global Supply Management - Mechanicals](https://www.skydio.com/jobs/eb7fbbdb-3346-4f7f-a202-8bfd3441217a/?gh_jid=eb7fbbdb-3346-4f7f-a202-8bfd3441217a) | bold-p | — | 3 | 588 | 4 | 0 | 2 | 0 | 0 | yes |
| [Director, Growth Marketing - Commercial](https://www.skydio.com/jobs/00d0bdc5-89ad-4182-8512-ab0a028953f6/?gh_jid=00d0bdc5-89ad-4182-8512-ab0a028953f6) | bold-p | — | 6 | 564 | 4 | 8 | 3 | 0 | 1 | yes |
| [Electrical Engineer (all levels) ](https://www.skydio.com/jobs/f0c26a3c-d999-4dc2-8812-b3835f633ded/?gh_jid=f0c26a3c-d999-4dc2-8812-b3835f633ded) | bold-p | — | 2 | 224 | 4 | 2 | 0 | 0 | 0 | yes |
| [Engineering Manager - Autonomy](https://www.skydio.com/jobs/849ae77c-5ca2-42b5-812b-8b3ad4524a89/?gh_jid=849ae77c-5ca2-42b5-812b-8b3ad4524a89) | bold-p | — | 3 | 323 | 4 | 1 | 0 | 0 | 0 | yes |
| [Enterprise Account Manager (MoD/ MoI) – EMEA (Finland)](https://www.skydio.com/jobs/d6f731e8-c530-4123-8b52-0e7cab164887/?gh_jid=d6f731e8-c530-4123-8b52-0e7cab164887) | bold-p | — | 3 | 573 | 0 | 2 | 0 | 0 | 0 | yes |
| [Enterprise Account Manager (MoD/ MoI) – EMEA (Germany)](https://www.skydio.com/jobs/12e9a494-9a89-457c-9dc7-2ef9ccdba17c/?gh_jid=12e9a494-9a89-457c-9dc7-2ef9ccdba17c) | bold-p | — | 3 | 573 | 0 | 2 | 0 | 0 | 0 | yes |
| [Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland)](https://www.skydio.com/jobs/1d4977a2-c2e7-44ad-820b-253ff8355800/?gh_jid=1d4977a2-c2e7-44ad-820b-253ff8355800) | bold-p | — | 3 | 573 | 0 | 2 | 0 | 0 | 0 | yes |
| [Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM](https://www.skydio.com/jobs/e69362bc-5891-486e-be75-6bf25187ccf5/?gh_jid=e69362bc-5891-486e-be75-6bf25187ccf5) | bold-p | — | 3 | 483 | 0 | 0 | 0 | 0 | 0 | yes |
| [Enterprise Account Manager, US Army](https://www.skydio.com/jobs/19559b4c-ed09-41eb-b1aa-f000a855b8fe/?gh_jid=19559b4c-ed09-41eb-b1aa-f000a855b8fe) | bold-p | — | 3 | 446 | 4 | 0 | 0 | 0 | 0 | yes |
| [Field Support Representative ](https://www.skydio.com/jobs/b053b0e2-005c-4e77-95f3-26c7354e6095/?gh_jid=b053b0e2-005c-4e77-95f3-26c7354e6095) | bold-p | — | 4 | 486 | 4 | 0 | 0 | 0 | 0 | yes |
| [Field Support Representative (Southwest, Remote)](https://www.skydio.com/jobs/9b93e7c2-e5d5-48b2-a2d2-8df71e0d8357/?gh_jid=9b93e7c2-e5d5-48b2-a2d2-8df71e0d8357) | bold-p | — | 2 | 687 | 4 | 0 | 2 | 0 | 0 | yes |
| [Full Stack Product Counsel](https://www.skydio.com/jobs/c9e40dab-ae7d-4034-a335-b3e05d419672/?gh_jid=c9e40dab-ae7d-4034-a335-b3e05d419672) | h3 | h3×4 | 0 | 742 | 6 | 0 | 8 | 1 | 0 | **NO** |
| [GTM Data Engineer Intern](https://www.skydio.com/jobs/b90b9b3b-e326-4fb6-85bd-fe52bec5f180/?gh_jid=b90b9b3b-e326-4fb6-85bd-fe52bec5f180) | bold-p | — | 1 | 433 | 0 | 3 | 1 | 0 | 0 | yes |
| [GTM Enablement Associate](https://www.skydio.com/jobs/2b3fea3b-e1b5-4497-9607-e9864019b0e7/?gh_jid=2b3fea3b-e1b5-4497-9607-e9864019b0e7) | bold-p | — | 2 | 350 | 0 | 2 | 1 | 0 | 0 | yes |
| [Hardware Engineering Program Manager](https://www.skydio.com/jobs/b49e6784-2183-4de4-a0a1-7661203c254a/?gh_jid=b49e6784-2183-4de4-a0a1-7661203c254a) | h2+h3 | h2×3,h3×5 | 0 | 455 | 4 | 0 | 2 | 0 | 0 | yes |
| [Hardware Operations Program Manager](https://www.skydio.com/jobs/55b393cf-124c-46f8-bd83-8c62e3ce628b/?gh_jid=55b393cf-124c-46f8-bd83-8c62e3ce628b) | bold-p | — | 2 | 361 | 0 | 0 | 2 | 0 | 0 | yes |
| [Head of Warehouse & Logistics Operations](https://www.skydio.com/jobs/0c1e9360-09dc-4c73-85bc-51aa72afd3ad/?gh_jid=0c1e9360-09dc-4c73-85bc-51aa72afd3ad) | bold-p | — | 2 | 420 | 4 | 1 | 1 | 0 | 0 | yes |
| [IT Technician (Help Desk - Linux Focus)](https://www.skydio.com/jobs/28c865cf-6aa4-45d1-ae13-34bb8f6b776b/?gh_jid=28c865cf-6aa4-45d1-ae13-34bb8f6b776b) | bold-p | — | 3 | 460 | 4 | 9 | 2 | 0 | 0 | yes |
| [Lead Staff Electrical Engineer](https://www.skydio.com/jobs/1bbcf144-7057-4a6e-9d51-4924bfda52b9/?gh_jid=1bbcf144-7057-4a6e-9d51-4924bfda52b9) | bold-p | — | 1 | 298 | 5 | 1 | 1 | 1 | 0 | yes |
| [Manager, Logistics ](https://www.skydio.com/jobs/eeb4b52f-d4e6-4823-9e4b-0ce75041d928/?gh_jid=eeb4b52f-d4e6-4823-9e4b-0ce75041d928) | bold-p | — | 3 | 416 | 4 | 0 | 2 | 0 | 0 | yes |
| [Manager, Technical Support](https://www.skydio.com/jobs/2b312ffb-26c3-4b7f-8904-acbc4e51934b/?gh_jid=2b312ffb-26c3-4b7f-8904-acbc4e51934b) | bold-p | — | 3 | 749 | 4 | 0 | 0 | 0 | 0 | yes |
| [Middleware Software Engineer Intern - Fall 2026](https://www.skydio.com/jobs/7d9dbb60-4ca1-4ba8-8bae-5ebfded4a915/?gh_jid=7d9dbb60-4ca1-4ba8-8bae-5ebfded4a915) | bold-p | — | 3 | 316 | 4 | 0 | 0 | 0 | 0 | yes |
| [Mission Success Operations Manager](https://www.skydio.com/jobs/501a3067-e906-4354-b211-ac70db6accf4/?gh_jid=501a3067-e906-4354-b211-ac70db6accf4) | bold-p | — | 4 | 429 | 0 | 0 | 0 | 0 | 0 | yes |
| [PCB Layout Engineer](https://www.skydio.com/jobs/eb2f4124-9bd6-49f9-9636-03152c573f7d/?gh_jid=eb2f4124-9bd6-49f9-9636-03152c573f7d) | bold-p | — | 2 | 329 | 4 | 2 | 0 | 0 | 0 | yes |
| [PhD Autonomy Engineer Intern - Deep Learning or Computer Vision](https://www.skydio.com/jobs/8d3979a8-c791-4825-8cf4-9b25479b9519/?gh_jid=8d3979a8-c791-4825-8cf4-9b25479b9519) | bold-p | — | 3 | 328 | 0 | 1 | 0 | 0 | 0 | yes |
| [PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning)](https://www.skydio.com/jobs/f8225008-00b5-415e-9a48-c9b6eba9363c/?gh_jid=f8225008-00b5-415e-9a48-c9b6eba9363c) | MIXED | h3×3 | 1 | 416 | 4 | 0 | 0 | 0 | 0 | yes |
| [Product Design Engineer (All Levels)](https://www.skydio.com/jobs/3f02ead1-8efe-4e3f-9c75-625e74ab57d1/?gh_jid=3f02ead1-8efe-4e3f-9c75-625e74ab57d1) | bold-p | — | 1 | 427 | 4 | 1 | 0 | 0 | 0 | yes |
| [Product Support Engineer](https://www.skydio.com/jobs/a4f131a0-4dde-46ce-85a1-c83fc3e0f21e/?gh_jid=a4f131a0-4dde-46ce-85a1-c83fc3e0f21e) | bold-p | — | 0 | 548 | 4 | 2 | 1 | 0 | 0 | yes |
| [Product Support Engineer Intern](https://www.skydio.com/jobs/8df0689e-a489-4c72-a1f7-09dfe59745b8/?gh_jid=8df0689e-a489-4c72-a1f7-09dfe59745b8) | bold-p | — | 0 | 415 | 4 | 2 | 2 | 0 | 0 | yes |
| [Program Manager, Major Deployments (Hawaii)](https://www.skydio.com/jobs/b194dcda-7ff0-4d44-9785-16895a44727f/?gh_jid=b194dcda-7ff0-4d44-9785-16895a44727f) | bold-p | — | 3 | 573 | 4 | 0 | 2 | 0 | 0 | yes |
| [Revenue Operations Engineer, Quoting Systems](https://www.skydio.com/jobs/02d54431-2747-417d-8234-e72c316fed87/?gh_jid=02d54431-2747-417d-8234-e72c316fed87) | MIXED | h2×5 | 1 | 470 | 0 | 4 | 1 | 0 | 0 | yes |
| [RF Design Engineer](https://www.skydio.com/jobs/f72f1fa5-d3d6-459e-8722-a94ce92ad1c8/?gh_jid=f72f1fa5-d3d6-459e-8722-a94ce92ad1c8) | bold-p | — | 3 | 365 | 4 | 0 | 0 | 0 | 0 | yes |
| [Sales Planning Analyst Intern](https://www.skydio.com/jobs/712900e5-ff75-4e07-8f88-626d4f8ab653/?gh_jid=712900e5-ff75-4e07-8f88-626d4f8ab653) | bold-p | — | 1 | 385 | 0 | 1 | 0 | 0 | 0 | yes |
| [Senior Autonomy Engineer - Controls ](https://www.skydio.com/jobs/58b4cdf6-5630-4dd0-aab3-a1ed4d599466/?gh_jid=58b4cdf6-5630-4dd0-aab3-a1ed4d599466) | bold-p | — | 3 | 232 | 0 | 0 | 0 | 0 | 0 | yes |
| [Senior Autonomy Engineer - Deep Learning](https://www.skydio.com/jobs/a6421d3e-fdd0-48d6-8d8f-3fd605cdf09f/?gh_jid=a6421d3e-fdd0-48d6-8d8f-3fd605cdf09f) | bold-p | — | 1 | 297 | 0 | 2 | 0 | 0 | 0 | yes |
| [Senior Autonomy Engineer - Deep Learning](https://www.skydio.com/jobs/a6973c57-132a-4a0d-b130-02d2bdaecd2a/?gh_jid=a6973c57-132a-4a0d-b130-02d2bdaecd2a) | bold-p | — | 1 | 298 | 0 | 2 | 0 | 0 | 0 | yes |
| [Senior Brand Designer (Contract)](https://www.skydio.com/jobs/5ae7e25f-7da3-4523-a8be-8866aa89e8df/?gh_jid=5ae7e25f-7da3-4523-a8be-8866aa89e8df) | bold-p | — | 3 | 471 | 0 | 2 | 2 | 0 | 0 | yes |
| [Senior Business Operations Manager](https://www.skydio.com/jobs/17b9ecf9-7a47-4811-b035-e1b9a54966aa/?gh_jid=17b9ecf9-7a47-4811-b035-e1b9a54966aa) | MIXED | h3×3 | 3 | 471 | 4 | 0 | 2 | 0 | 0 | yes |
| [Senior Buyer](https://www.skydio.com/jobs/5d32766d-990a-4c4c-a8c6-5e934dd8bd38/?gh_jid=5d32766d-990a-4c4c-a8c6-5e934dd8bd38) | MIXED | h2×2 | 1 | 449 | 4 | 0 | 2 | 0 | 0 | yes |
| [Senior Customer Support Representative - India](https://www.skydio.com/jobs/bb7a9c5c-8dbb-4a2f-9d7d-db9ab1f707b0/?gh_jid=bb7a9c5c-8dbb-4a2f-9d7d-db9ab1f707b0) | bold-p | — | 2 | 584 | 4 | 0 | 0 | 0 | 0 | yes |
| [Senior Director, Product Management, Drone as First Responder (DFR)](https://www.skydio.com/jobs/7ef6359b-6454-4f91-871f-b33961585086/?gh_jid=7ef6359b-6454-4f91-871f-b33961585086) | bold-p | — | 2 | 578 | 4 | 2 | 0 | 0 | 0 | yes |
| [Senior Hardware Test and Reliability Engineer](https://www.skydio.com/jobs/c0e49670-51ca-461c-b0e2-4a06df01f692/?gh_jid=c0e49670-51ca-461c-b0e2-4a06df01f692) | bold-p | — | 3 | 521 | 0 | 0 | 0 | 0 | 0 | yes |
| [Senior NPI Product Quality Engineer](https://www.skydio.com/jobs/178a7e84-562e-40db-9abd-94bbf29159ca/?gh_jid=178a7e84-562e-40db-9abd-94bbf29159ca) | bold-p | — | 2 | 367 | 0 | 0 | 0 | 1 | 1 | yes |
| [Senior People Analytics Analyst](https://www.skydio.com/jobs/0703aaa0-9fcb-4b22-ad8c-b53e74151a72/?gh_jid=0703aaa0-9fcb-4b22-ad8c-b53e74151a72) | bold-p | — | 2 | 426 | 4 | 0 | 0 | 0 | 0 | yes |
| [Senior Product Manager, Platform & Infrastructure](https://www.skydio.com/jobs/8d67884d-58f4-41a7-8740-ab65d3c03fa8/?gh_jid=8d67884d-58f4-41a7-8740-ab65d3c03fa8) | bold-p | — | 1 | 741 | 4 | 1 | 5 | 0 | 0 | yes |
| [Senior Revenue Operations Manager](https://www.skydio.com/jobs/05e9f029-3a9d-4956-a4c8-e0bc786dd86a/?gh_jid=05e9f029-3a9d-4956-a4c8-e0bc786dd86a) | bold-p | — | 3 | 417 | 0 | 0 | 2 | 0 | 0 | yes |
| [Senior RF Design Engineer](https://www.skydio.com/jobs/7bd047de-b65b-42b2-a2bf-7d33ceabd083/?gh_jid=7bd047de-b65b-42b2-a2bf-7d33ceabd083) | bold-p | — | 3 | 561 | 4 | 0 | 2 | 0 | 0 | yes |
| [Senior Software Engineer - Embedded ](https://www.skydio.com/jobs/67a7d89f-9c4e-4f60-bdf1-a60b8addd8ae/?gh_jid=67a7d89f-9c4e-4f60-bdf1-a60b8addd8ae) | bold-p | — | 4 | 333 | 4 | 0 | 0 | 0 | 0 | yes |
| [Senior Software Engineer - Mobile Platform ](https://www.skydio.com/jobs/e8cb16b0-d2f0-4cb4-a1a1-0f43d195cc9a/?gh_jid=e8cb16b0-d2f0-4cb4-a1a1-0f43d195cc9a) | bold-p | — | 5 | 502 | 4 | 0 | 3 | 0 | 0 | yes |
| [Senior Software Engineer - Security](https://www.skydio.com/jobs/bcd3d614-178c-4349-afd4-76476211b7fe/?gh_jid=bcd3d614-178c-4349-afd4-76476211b7fe) | bold-p | — | 4 | 393 | 4 | 0 | 0 | 0 | 0 | yes |
| [Senior Software Engineer,  Data Platform ](https://www.skydio.com/jobs/aeaa130d-3e8b-42c5-a805-46f056e62fda/?gh_jid=aeaa130d-3e8b-42c5-a805-46f056e62fda) | bold-p | — | 4 | 699 | 4 | 1 | 0 | 0 | 0 | yes |
| [Senior Software Engineer, Frontend](https://www.skydio.com/jobs/86cfc7bb-001c-4c1c-b680-160265535a96/?gh_jid=86cfc7bb-001c-4c1c-b680-160265535a96) | bold-p | — | 4 | 328 | 0 | 0 | 0 | 0 | 0 | yes |
| [Senior Software Engineer, Full Stack](https://www.skydio.com/jobs/5655fbe3-66b0-4951-afdc-3b67f71e6938/?gh_jid=5655fbe3-66b0-4951-afdc-3b67f71e6938) | bold-p | — | 4 | 599 | 1 | 1 | 0 | 1 | 0 | yes |
| [Senior Strategy and Planning Analyst](https://www.skydio.com/jobs/8b96b4ed-04cf-4451-89bc-0db79a01d64d/?gh_jid=8b96b4ed-04cf-4451-89bc-0db79a01d64d) | bold-p | — | 3 | 574 | 4 | 1 | 1 | 0 | 0 | yes |
| [Senior Technical Recruiter](https://www.skydio.com/jobs/16b0647d-a470-4917-9bb9-a95967828edc/?gh_jid=16b0647d-a470-4917-9bb9-a95967828edc) | bold-p | — | 2 | 415 | 4 | 2 | 0 | 1 | 0 | yes |
| [Senior Technical Recruiter - Hardware Operations](https://www.skydio.com/jobs/737c02d2-f03f-4716-a0c8-e14a0307f8cb/?gh_jid=737c02d2-f03f-4716-a0c8-e14a0307f8cb) | bold-p | — | 1 | 421 | 4 | 4 | 0 | 1 | 0 | yes |
| [Senior Technical Support Representative - Japan](https://www.skydio.com/jobs/f714e85f-31df-494e-bac4-1dd61d4d6066/?gh_jid=f714e85f-31df-494e-bac4-1dd61d4d6066) | h1 | h1×3 | 0 | 685 | 5 | 2 | 1 | 0 | 0 | **NO** |
| [Senior Wireless Systems Performance Engineer](https://www.skydio.com/jobs/f1ecf164-714c-4f1a-b672-d763f5724c03/?gh_jid=f1ecf164-714c-4f1a-b672-d763f5724c03) | bold-p | — | 3 | 363 | 4 | 0 | 0 | 0 | 0 | yes |
| [Senior/Staff Embedded Software Engineer – Camera Systems](https://www.skydio.com/jobs/71033170-d9d0-474b-b712-a11e4f11c146/?gh_jid=71033170-d9d0-474b-b712-a11e4f11c146) | bold-p | — | 4 | 367 | 4 | 0 | 3 | 0 | 0 | yes |
| [Software Engineer - Autonomy Infrastructure, Systems and Tools](https://www.skydio.com/jobs/9e42a7af-6369-4036-ae6f-6626ee3a4fb3/?gh_jid=9e42a7af-6369-4036-ae6f-6626ee3a4fb3) | h2 | h2×5 | 0 | 493 | 0 | 0 | 1 | 0 | 0 | yes |
| [Software Engineer - Autonomy Infrastructure, Systems and Tools](https://www.skydio.com/jobs/9fc135c5-7a87-410d-8323-e0f918585ebc/?gh_jid=9fc135c5-7a87-410d-8323-e0f918585ebc) | h2 | h2×5 | 0 | 493 | 0 | 0 | 1 | 0 | 0 | yes |
| [Software Engineer - Cloud Simulation & Full-Stack](https://www.skydio.com/jobs/7d7dfadc-c6fd-4958-8d59-004a91bff55e/?gh_jid=7d7dfadc-c6fd-4958-8d59-004a91bff55e) | h2 | h2×5 | 0 | 507 | 0 | 0 | 1 | 0 | 0 | yes |
| [Software Engineer - Cloud Simulation & Full-Stack](https://www.skydio.com/jobs/948bddb5-4679-4c7c-bf57-960a0fd1a7ed/?gh_jid=948bddb5-4679-4c7c-bf57-960a0fd1a7ed) | h2 | h2×5 | 0 | 507 | 0 | 0 | 1 | 0 | 0 | yes |
| [Software Engineer - Embedded](https://www.skydio.com/jobs/ef9f7dd2-5a88-49b4-a507-d5fc9cad565a/?gh_jid=ef9f7dd2-5a88-49b4-a507-d5fc9cad565a) | bold-p | — | 4 | 333 | 4 | 0 | 0 | 0 | 0 | yes |
| [Software Engineer - Simulation & Robotics Engineer](https://www.skydio.com/jobs/7a8f3e6c-d576-41af-a81e-bf4fe20da12a/?gh_jid=7a8f3e6c-d576-41af-a81e-bf4fe20da12a) | h3 | h3×5 | 0 | 446 | 0 | 0 | 1 | 0 | 0 | yes |
| [Software Engineer - Simulation & Robotics Engineer](https://www.skydio.com/jobs/abd4addb-2d11-4207-b3a2-446a09121e39/?gh_jid=abd4addb-2d11-4207-b3a2-446a09121e39) | h3 | h3×5 | 0 | 446 | 0 | 0 | 1 | 0 | 0 | yes |
| [Software Engineer Intern Fall 2026/Winter 2027](https://www.skydio.com/jobs/f6320e9b-4eed-408d-8d37-d509fb0406ee/?gh_jid=f6320e9b-4eed-408d-8d37-d509fb0406ee) | bold-p | — | 0 | 347 | 4 | 4 | 1 | 0 | 0 | yes |
| [Software Engineer, Full Stack](https://www.skydio.com/jobs/067e1f47-9fba-4abf-b986-874d4d569706/?gh_jid=067e1f47-9fba-4abf-b986-874d4d569706) | bold-p | — | 4 | 299 | 4 | 0 | 0 | 0 | 0 | yes |
| [Sr/Staff Embedded Software Engineer - Camera Systems](https://www.skydio.com/jobs/898a9c77-cc20-4ed6-a050-f68e5c15d5c8/?gh_jid=898a9c77-cc20-4ed6-a050-f68e5c15d5c8) | bold-p | — | 4 | 367 | 4 | 0 | 3 | 0 | 0 | yes |
| [Staff Global Supply Manager,  Mechanicals](https://www.skydio.com/jobs/2ffe6453-4a2f-4dfb-94f8-882f731a11ae/?gh_jid=2ffe6453-4a2f-4dfb-94f8-882f731a11ae) | bold-p | — | 2 | 524 | 0 | 1 | 0 | 0 | 0 | yes |
| [Staff Product Manager, Platform & Infrastructure](https://www.skydio.com/jobs/dbd737b2-beed-4917-9948-dde4250929a8/?gh_jid=dbd737b2-beed-4917-9948-dde4250929a8) | bold-p | — | 1 | 760 | 4 | 1 | 5 | 0 | 0 | yes |
| [Staff Software Engineer - Embedded](https://www.skydio.com/jobs/b3b2dea9-63bb-4adb-ba29-69bd8f7a18eb/?gh_jid=b3b2dea9-63bb-4adb-ba29-69bd8f7a18eb) | bold-p | — | 4 | 333 | 4 | 0 | 0 | 0 | 0 | yes |
| [Staff Software Engineer, Frontend](https://www.skydio.com/jobs/54654035-a78a-4e5b-9ebf-ae4067e5a246/?gh_jid=54654035-a78a-4e5b-9ebf-ae4067e5a246) | bold-p | — | 4 | 328 | 0 | 0 | 0 | 0 | 0 | yes |
| [Staff Software Engineer, Full Stack](https://www.skydio.com/jobs/379b23ea-14ff-4602-9b79-52d00bb96fda/?gh_jid=379b23ea-14ff-4602-9b79-52d00bb96fda) | bold-p | — | 3 | 588 | 0 | 0 | 0 | 0 | 0 | yes |
| [Staff Technical Recruiter](https://www.skydio.com/jobs/c3a4256a-4525-443c-81d0-6f69e7c24805/?gh_jid=c3a4256a-4525-443c-81d0-6f69e7c24805) | bold-p | — | 3 | 410 | 4 | 0 | 0 | 1 | 0 | yes |
| [Success Systems Specialist ](https://www.skydio.com/jobs/8de95d05-a601-47e2-8a13-5ba4d7ad428a/?gh_jid=8de95d05-a601-47e2-8a13-5ba4d7ad428a) | bold-p | — | 8 | 690 | 0 | 0 | 0 | 0 | 0 | yes |
| [Supplier Quality Engineer, Sustaining](https://www.skydio.com/jobs/4c4874bf-02da-4ccc-8918-2cca08feaf21/?gh_jid=4c4874bf-02da-4ccc-8918-2cca08feaf21) | bold-p | — | 3 | 542 | 5 | 0 | 1 | 0 | 0 | **NO** |
| [Supply Chain Intern](https://www.skydio.com/jobs/2d21f482-3224-4906-a1bb-6a64436774cb/?gh_jid=2d21f482-3224-4906-a1bb-6a64436774cb) | bold-p | — | 2 | 217 | 0 | 2 | 0 | 0 | 0 | yes |
| [Systems Integration and Test Engineer (Mid to Senior Level)](https://www.skydio.com/jobs/a1a60b27-53a8-455e-b467-712e01c532dc/?gh_jid=a1a60b27-53a8-455e-b467-712e01c532dc) | bold-p | — | 3 | 489 | 0 | 0 | 0 | 0 | 0 | yes |
| [Wireless Software Engineer](https://www.skydio.com/jobs/04fde92b-6a2b-4638-adc2-e8fa91cc1a49/?gh_jid=04fde92b-6a2b-4638-adc2-e8fa91cc1a49) | bold-p | — | 3 | 382 | 4 | 0 | 0 | 0 | 0 | yes |
| [Workplace Experience Coordinator Part-Time](https://www.skydio.com/jobs/d023afe5-f19f-42f7-a1dd-aa94a361b86f/?gh_jid=d023afe5-f19f-42f7-a1dd-aa94a361b86f) | bold-p | — | 4 | 451 | 5 | 1 | 1 | 0 | 0 | **NO** |

---

*This report was generated by automated analysis of the live HTML of each posting under `/jobs/<id>`. Visual rendering is driven by the site stylesheet; this report therefore characterises the *markup-level* differences that cause the visible inconsistencies a reader observes. A spot-check by opening any two postings side-by-side in a browser confirms each of the issues listed above is visually noticeable.*

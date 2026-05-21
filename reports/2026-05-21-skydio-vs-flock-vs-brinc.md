🌐 last30days v3.3.0 · synced 2026-05-21

# Skydio vs Flock Safety vs Brinc: What the Community Says (/last30days)

Run via the [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) engine (`scripts/last30days.py`, comparison/competitors mode) plus Hacker News Algolia and post-engine web supplements. Engine sources active this run: Reddit (blocked by 403 from this VM's IP), Hacker News, GitHub, Polymarket. X, YouTube, TikTok, and Instagram were not available (no keys/cookies in this environment).

## Quick Verdict

- **Skydio** owns the "American-made autonomous DFR drone" lane right now. The last 30 days are a steady drumbeat of new city pilots and a 25,000-mission milestone at the flagship Chula Vista deployment - operational receipts, not announcements.
- **Flock Safety** is the dominant story of the month, but for bad reasons. Hacker News is alight with stories of vandalized cameras, demo-room privacy scandals, false-warrant matches, ICE data-sharing accusations, and the first towns banning Flock outright. Their Aerodome-powered drone push barely registers in community discussion next to the surveillance backlash.
- **Brinc** is quiet in social/HN signal but loud in trade press: it is using the BRINC + National League of Cities DFR partnership and an AirData integration to position the Lemur 2 / Responder line as the indoor-tactical + outdoor-911 complement to a Skydio-style platform, with concrete municipal wins (e.g. Victorville's $832K three-year contract).

If Skydio is the autonomous outdoor DFR aircraft, Flock is the surveillance fabric (ALPR + cameras + Aerodome drones) that ties it all together, and Brinc is the indoor / tactical drone plus a growing DFR pitch of its own. The community treats Skydio as a credible technology story, Brinc as a niche success story, and Flock as the surveillance-state lightning rod.

## Skydio

The last-30-days picture for Skydio is operational, not promotional. Five public-safety deployments crossed the news cycle:

- **[Chula Vista PD's DFR program crossed 25,000 missions](https://dronexl.co/2026/05/15/chula-vista-pd-dfr-drone-program-25000/)** as of May 8, 2026. The drone arrived first on 17,170 calls with a 96.98s average response time, contributed to 4,138 arrests, and cleared 4,629 calls without dispatching ground officers. That "~1 in 5 calls resolved without a cop physically rolling" stat is the real selling line for Skydio's enterprise pitch.
- **[Fresno's Skydio X10 drones caught Dick's Sporting Goods thieves](https://dronexl.co/2026/05/14/fresno-skydio-x10-drones-thieves/)**. Their program (launched March 23, 2026; 3 rooftop docks; two units funded by California's Organized Retail Theft grants) had run ~275 calls and cleared roughly 20% without an officer responding.
- **[Leander, TX](https://dronexl.co/2026/05/06/leander-skydio-drones-911/)** ran a two-week X10 DFR pilot on live 911 calls May 4-15.
- **[Bloomington, MN](https://dronexl.co/2026/05/19/bloomington-skydio-x10-dfr-drones-response/)** kicked off a two-week X10 DFR pilot the week of May 18, joining Edina and Minnetonka in Minneapolis-area DFR experimentation.
- **[Skydio CEO Adam Bry attended](https://dronexl.co/2026/04/22/skydio-ceo-ramapo-police-dfr/)** Ramapo PD's DFR demo for Rockland County (NY) supervisors in late April - executive selling at the county-procurement level.

On Hacker News, Skydio itself produced zero front-page items in the last 30 days. The Skydio GitHub org's most notable activity is a feature PR on their internal stacked-diff tool [`Skydio/revup`](https://github.com/Skydio/revup/pull/241) (May 7, 4 comments) - infrastructure, not product. There was no fresh Reddit signal accessible from this run (Reddit returned 403 for all r/skydio, r/drones, r/protectandserve, r/Multicopter, and r/publicsafety queries from this IP).

Read together: Skydio's last 30 days look like a company executing in market - city pilots stacking up, the flagship deployment hitting a vanity milestone, the CEO doing in-person procurement work - rather than making news with launches or controversies.

## Flock Safety

Flock dominated the last 30 days of social signal, and almost entirely as the subject of backlash. The Hacker News front page carried at least seven distinct Flock-related stories totaling 1,400+ points and 800+ comments:

- **[At least 25 Flock cameras have been destroyed in five states since April 2025](https://stateofsurveillance.org/news/flock-cameras-destroyed-nationwide-ice-backlash-2026/)** (May 17, 443 pts, 322 comments). HN reframed it as community-led pushback after the ICE-cooperation reporting earlier in the month.
- **[City Learns Flock Accessed Cameras in Children's Gymnastics Room as a Sales Demo](https://www.404media.co/city-learns-flock-accessed-cameras-in-childrens-gymnastics-room-as-a-sales-pitch-demo-renews-contract-anyway/)** (404 Media, May 1, 478 pts, 122 comments). The town renewed the contract anyway, which is the part the comment section can't get over.
- **[Flock cameras keep telling police a man who doesn't have a warrant has a warrant](https://www.youtube.com/watch?v=nHwxV0Sd9V8)** (May 1, 192 pts, 145 comments) - false-positive ALPR matches that led to repeated stops.
- **[Authorities say Flock cameras' data allegedly used for immigration enforcement](https://www.ohio.news/stories/dayton-authorities-say-that-flock-cameras-data-allegedly-used-for-immigration-enforcement/)** (May 7, 94 pts, 51 comments).
- **[After Town Bans Flock, Councilmember Crashes Out, Proposes Internet, Phone Ban](https://www.404media.co/after-town-bans-flock-councilmember-crashes-out-proposes-internet-and-phone-ban/)** (May 20, 118 pts, 108 comments). A town actually banning Flock is a 2026 first; that it produced an immediate proposal to also ban "the internet and phones" is what drove the comment volume.
- **[AI license plate cameras tore this town apart and led to a state of emergency](https://hn.algolia.com/?q=AI+license+plate+cameras+tore+this+town+apart)** (May 17).
- **[City and Flock Manipulate Security Scores](https://ipvm.com/reports/flock-review-dunwoody)** (IPVM, May 14) and the related ["The Link Between Flock Safety, Dunwoody, and Attorney General Chris Carr"](https://jasonhunyar.substack.com/p/inside-the-belly-of-the-beast-the) (May 15) - reporting that Dunwoody, GA and Flock allegedly massaged "before/after" crime stats used to sell the system to other cities.

In parallel, the developer/hobbyist response is hardening into actual tooling. The GitHub side of last-30-days has [`none-below/sm-alpr`](https://github.com/none-below/sm-alpr) running automated hourly refreshes of Flock's "transparency portal" data (PRs [#368](https://github.com/none-below/sm-alpr/pull/368), [#365](https://github.com/none-below/sm-alpr/pull/365), [#426](https://github.com/none-below/sm-alpr/pull/426)) so anyone can track which agencies use Flock and what they share. [`yattsu/biscuit`](https://github.com/yattsu/biscuit/pull/1) just ported a passive Flock camera detector ("Flock-You") that fingerprints camera networks by their 31 known wireless OUIs. That's an organized counter-surveillance ecosystem forming around Flock the way it once did around Ring.

The under-discussed thing in this stream: Flock's actual drone strategy. The Aerodome acquisition (Oct 2024, $300M+, founded by ex-cop Rahul Sidhu, also a16z-backed) is what makes Flock a direct Skydio competitor - it pairs Aerodome's automated battery-swap docks, detect-and-avoid, and BVLOS-without-visual-observers capability with Flock's existing ALPR + gunshot-detection + Real-Time Crime Center stack, and Flock has been hiring ~100 engineers and committed to shipping a suite of NDAA-compliant American-made drones over the following 12 months. None of that surfaced on Hacker News this month. Community discussion is 100% surveillance ethics, 0% product roadmap.

## Brinc

Brinc has the thinnest social-media footprint of the three (HN: zero hits this window; Reddit: blocked; GitHub: no signal), but the trade-press story is coherent and incremental:

- **[BRINC and the National League of Cities launched a national DFR program](https://dronelife.com/2026/03/17/brinc-nlc-drone-as-first-responder-program/)** in March 2026 - a policy-and-education channel to help cities stand up DFR programs, with Brinc's hardware as the implicit reference platform.
- **[BRINC drones land in Victorville for an $832K DFR rollout](https://dronexl.co/2026/04/27/brinc-drones-victorville-832k/)** (late April). The contract is $832K over three years (~$277K/yr) funded through California AB 3229 Supplemental Law Enforcement Services Funds - real money, not a pilot.
- **[AirData integrated with BRINC](https://dronedj.com/2026/04/23/brinc-drone-airdata-lemur-responder/)** (April 22-23) to auto-capture flight logs from the Lemur 2 and Responder lines. The Lemur 2 is positioned as the indoor / tactical drone for clearing buildings, which is a different mission set than Skydio's outdoor X10 - that distinction is the core of Brinc's pitch.
- Brinc's own [DFR 3.0 framing](https://brincdrones.com/news/dfr-3-0-the-next-step-in-the-evolution-of-drone-as-first-responder/) names a "next evolution" of DFR. Marketing copy, but it shows where they want the conversation to go.

The macro number that keeps recurring across both Brinc and Skydio coverage: 1,500+ US law-enforcement agencies now operate drone programs, and DFR programs are reporting 20-25% of 911 calls resolved without sending a ground officer. That's the TAM line the whole sector is fighting over.

## Head-to-Head

| Dimension | Skydio | Flock Safety | Brinc |
|---|---|---|---|
| What it is | Autonomous outdoor public-safety drones (X10) and software for DFR | Surveillance platform (ALPR cameras, gunshot detection, RTCC) + drones via Aerodome | Indoor-tactical and first-responder drones (Lemur 2, Responder), DFR program |
| Flagship product | Skydio X10 + rooftop dock + DFR Command | Flock cameras + Falcon ALPR + Aerodome drones | Lemur 2 (indoor) + Responder line, BRINC LiveOps |
| Origin story | Computer-vision autonomy spin-out, ex-MIT/Google | LPR cameras for HOAs, scaled into police contracts | Indoor breaching/tactical drones for SWAT and crisis response |
| US-made / NDAA | NDAA-compliant, American-made | Building NDAA-compliant drone line through Aerodome | NDAA-compliant, American-made |
| 30-day signal | 5+ city pilots/expansions, Chula Vista at 25K missions | Mostly negative HN coverage: vandalism, ICE data, demo-room scandal, town bans | Niche but positive: NLC partnership, Victorville $832K rollout, AirData integration |
| Dominant narrative | Execution and adoption | Surveillance backlash and trust crisis | Quiet adoption, indoor-tactical differentiation |
| Headline risk | Low this month | Very high: organized counter-surveillance tooling and the first municipal bans | Low |
| Best for | Outdoor DFR, autonomous flight to incidents | Cities that already use Flock ALPR and want drones in the same stack | Indoor / tactical missions, smaller agencies, AB 3229-funded California PDs |

## The Bottom Line

- **Choose Skydio if** you are buying a single best-of-breed autonomous outdoor DFR aircraft and an extensible software stack, and you want the deployment with the most operational receipts (Chula Vista's 25K-mission numbers are the reference deployment everyone else gets compared to).
- **Choose Flock if** you have already standardized on Flock ALPR / RTCC / gunshot detection and you want drones (via Aerodome) inside that same vendor relationship - but understand you are also buying their PR risk profile. The community noise around Flock in May 2026 is loud enough that procurement teams will be asked about it in council meetings.
- **Choose Brinc if** the mission is indoor entries / hostage / building clears, or if you're a smaller agency using California AB 3229 or similar grant funding and want a turnkey program-management partner (the NLC partnership is doing real work here).

The emerging stack: an agency probably ends up with Skydio (or Aerodome, if Flock-aligned) outdoors, Brinc indoors, and Flock or a competing ALPR layer underneath. The three are less a head-to-head and more a Pokémon-style type triangle: Skydio = open-air autonomy, Brinc = indoor / tactical, Flock = the surveillance fabric that ties detection to dispatch. Where they actually collide is **Aerodome vs Skydio X10 vs Brinc Responder** for the outdoor 911-dispatch drone, and that head-to-head is still being decided one city-council vote at a time.

---

## Engine footer

```
✅ All agents reported back!
├─ 🟡 HN: 4 storys │ 1,207 points │ 640 comments (Skydio pass)
├─ 🟡 HN: 12 storys │ 1,679 points │ 1,015 comments (Flock Safety pass)
├─ 🐙 GitHub: 1 + 7 + 1 = 9 items (Skydio / Flock / Brinc)
├─ 🟢 Polymarket: 0 markets matched
├─ 🔴 Reddit: 0 threads (HTTP 403 from this VM IP across r/skydio, r/drones, r/protectandserve, r/Multicopter, r/publicsafety)
└─ 📎 Raw results: reports/raw/{skydio,flock-safety,brinc}-raw-v3.md
```

## How this was generated

- Engine: `mvanhorn/last30days-skill` v3.3.0 (cloned from <https://github.com/mvanhorn/last30days-skill>), invoked as `python3 scripts/last30days.py "Skydio vs Flock Safety vs Brinc" --emit=compact --plan plan.json --x-handle=SkydioHQ --x-related=flock_safety,brincdrones --subreddits=skydio,drones,protectandserve,Multicopter,publicsafety`. The engine's vs-mode fan-out produced one raw file per entity (saved under `reports/raw/`).
- HN supplements: direct queries against `hn.algolia.com/api/v1/search_by_date` for `skydio`, `flock safety`, `brinc`, `drone first responder`, `DFR police drone` over the last 30 days.
- Post-engine web supplements (per the skill's Step 2 contract): WebSearch for "Skydio X10 DFR police 2026", "Brinc Lemur 2 first responder funding 2026", "Flock Safety Aerodome drone acquisition 2026".
- Environment limitations: Reddit's public JSON endpoint returned `403 forbidden` for every query from this VM's IP, so the rich Reddit/r/protectandserve discussion the skill normally surfaces is missing here. X/Twitter, YouTube transcripts, TikTok, and Instagram were not available (no AUTH_TOKEN/CT0, no yt-dlp, no ScrapeCreators key). Polymarket had no matching markets.

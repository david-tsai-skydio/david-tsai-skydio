## Skydio vs Flock vs Brinc - Last 30 Days

Generated 2026-06-04 using the [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) research engine (Reddit + Hacker News + GitHub + Polymarket) and supplemental web search. Date range: 2026-05-05 to 2026-06-04.

> **Source availability note.** The engine ran without paid API keys, so X/Twitter, YouTube, TikTok, and Instagram were not available; Reddit's public search returned 403s on several pump queries and the keyless RSS tier carried the rest. Findings below combine the engine output (saved under `research/*-raw-v3.md`) with four targeted web searches covering recent news for each company and the head-to-head DFR market.

### Quick verdict

The three companies sell into the same buyer (US public safety agencies) but with very different shapes, and the last 30 days widened the gap between them.

- **Skydio** is the runaway DFR (Drone as First Responder) incumbent and is now repositioning as "America's drone prime." It announced a $3.5B, five-year US manufacturing push (SkyForge) plus a $110M Series F at a $4.4B valuation, and its X10D was named to the US Army's Short-Range Reconnaissance program of record alongside Teal's Black Widow.
- **Brinc** is attacking Skydio from the "capability" angle - tactical indoor flight (LEMUR 2) plus the new Guardian DFR drone with 90-second battery swap, marketed explicitly as "DFR 3.0" against Skydio's 35-minute X10 recharge. It is the upstart with the freshest hardware story.
- **Flock Safety** moved into drones via its 2024 Aerodome acquisition (now sold as **Flock Alpha** / Flock Aerodome) and is the software-forward play with ALPR + gunshot + DFR fused, but the last-30-days narrative around Flock is dominated by surveillance backlash, not product launches.

### Skydio

**The big-money story.** On April 24, 2026 Skydio announced a $3.5B, five-year commitment to expand US manufacturing and a $110M Series F at a $4.4B valuation, framed as "America's drone prime" positioning ([Skydio blog](https://www.skydio.com/blog/skydio-commits-usd3-5-billion-to-expand-u-s-manufacturing-and-secure-american-drone-leadership), [Sourcery VC](https://www.sourcery.vc/p/breaking-skydio-commits-35b-to-us)). The plan includes SkyForge - a supplier co-location program directing $1B+ to domestic suppliers - a US factory 5x larger than today's footprint, 2,000+ new Skydio jobs, and 3,000+ supply-chain roles. Industrial Sage explicitly ties the timing to the [FCC's December 2025 decision adding foreign-made drones to the national security Covered List](https://www.industrialsage.com/skydio-us-drone-manufacturing-skyforge/), which effectively blocks new DJI imports.

**Operational scale at the same time.** Per a long-form interview with CEO Adam Bry ([shriftman.substack.com](https://shriftman.substack.com/p/skydio-is-americas-drone-prime-a)) and a competitive analysis on robotics.press, Skydio's [DFR Command platform has processed 10M+ calls for service](https://robotics.press/news/skydio-dfr-1200-public-safety-agencies/) across 1,200+ public safety agencies, with 60,000 drones shipped to 3,800+ customers. Headline metrics: drones arrive first 71% of the time (92% at Jefferson Parish) and ~25% of calls resolve without dispatching a patrol unit (40% at the high end). San Francisco reports a 42% drop in auto theft since launching its program. Many contracts are 10-year subscriptions.

**Defense traction.** The engine surfaced one strong piece of evidence on the defense side: the Army's [Short-Range Reconnaissance program of record selected the Skydio X10D](https://www.reddit.com/r/RedCatHoldings/comments/1t8sn5n/us_army_small_uncrewed_aircraft_systems_programs/) along with Teal's Black Widow (per a thread in r/RedCatHoldings on 2026-05-10). Independent verification from a GitHub PR adding 20 deep-research-verified UAV entries to a defense database lists the [Skydio X10D as a $52M Army award covering 2500+ units](https://github.com/royconstantymartin-hub/defense-dashboard/pull/378). This is part of a broader sector run discussed in [r/IonQStock](https://www.reddit.com/r/IonQStock/comments/1ts9614/ionq_did_you_know/) on 2026-05-30, where investors tied a sector rally (UMAC +37%, ONDS +10.5%, RCAT +8%) to a WSJ scoop on Trump's Office of Strategic Capital backing critical supply chains.

**Public safety expansion.** Skydio launched a Drone-as-First-Responder program in Dallas during May; the [Nashville MNPD DFR program also kicked off on 2026-05-26](https://www.reddit.com/r/nashville/comments/1tojgig/drone_as_first_responder_program_starting_in/), and an open-source GitHub project mapping [Nashville MNPD DFR launch radii and council district overlays](https://github.com/clovenbradshaw-ctrl/DFR/pull/5) was being actively worked on (PR opened 2026-05-28). The [Minneapolis DFR pilot evaluation](https://dronexl.co/2026/05/31/minneapolis-dfr-pilot-north-minneapolis/) named Skydio as MPD's chosen platform - and called the X10 the "safe pick, the most-deployed American platform, the option that draws the least political fire."

**Brand pull on Reddit.** A Skydio-vs-DIY thread in r/drone_done on 2026-05-28 conceded that "[the Skydio's tracking is genuinely magic, no contest there](https://www.reddit.com/r/drone_done/comments/1tpnl3a/lmost_bought_a_skydio_2_instead/)" - the autonomy moat that investors and agencies keep paying for. Separately, OUST and AXON investor communities are starting to triangulate that [Skydio supplies drones to Axon's airframe lineup](https://www.reddit.com/r/OUST/comments/1tgvb1f/did_anyone_else_notice_this_bullish_news_about/) (2026-05-18, r/OUST), tying Ouster lidar + Axon RTCC + Skydio drone into one stack.

**The early civil-liberties flag.** A resident in r/Humboldt posted a [drive-by sighting of a Skydio brand drone dock atop a shipping container](https://www.reddit.com/r/Humboldt/comments/1top2zl/mobile_drone_dock_outside_blue_lake/) outside Blue Lake, CA (2026-05-27), citing a recent ICE contract with Skydio. This is the first organic Reddit chatter that puts Skydio in the same "where is this being pointed?" frame that has already swallowed Flock - worth watching.

### Brinc

**Positioning has gotten much sharper.** Brinc's pitch this month is **DFR 3.0** - explicitly named against Skydio's "DFR 2.0" docks-and-automation generation. Their public [DFR 3.0 post](https://brincdrones.com/news/dfr-3-0-the-next-step-in-the-evolution-of-drone-as-first-responder/) calls out the Skydio X10 by name: "a contact-charging platform such as the Skydio X10 requires 35 minutes to recharge from 15% to 95%. In contrast, Guardian's automated battery swap takes 90 seconds, assuming a charged battery is staged in the dock." That is the most direct comparative attack between any two of these three companies right now.

**The dual-drone capability differentiator.** Brinc is the only one of the three with a purpose-built indoor tactical drone, the [LEMUR 2](https://brincdrones.com/lemur-2/) - LiDAR-generated 2D floor plans pushed live to operators, a glass breaker attachment for tempered/automotive/residential glass, two-way comms, FLIR thermal, night vision, 20+ minute flight, IP24, AES-256 encryption, NDAA-compliant, made in Seattle. The combination of the outdoor **Responder** dock + indoor LEMUR 2 handoff is what the [Minneapolis DFR analysis](https://dronexl.co/2026/05/31/minneapolis-dfr-pilot-north-minneapolis/) explicitly cites as "the capability pick - the option that builds in an indoor tactical option the city will eventually want." Skydio cannot match it inside a single procurement.

**Scale.** Brinc reports 900+ public safety agencies and 20%+ of US SWAT teams as customers; revenue tripled in 2025. The company opened a new Seattle factory and raised $75M earlier in the year ([DRONELIFE](https://dronelife.com/2026/03/24/brinc-us-drone-manufacturing-public-safety-guardian/)). The footprint is roughly 1/4 to 1/3 of Skydio's agency count but with a defensible tactical niche.

**Last-30-days social signal is genuinely thin.** This is the most important honest caveat in this report: the engine's Reddit results for the keyword "Brinc" got dominated by Better Call Saul fan content (r/okbuddychicanery's "Brince"), and a targeted re-run on `Brinc Drones LEMUR` returned no actual Brinc Drones content from the last 30 days on Reddit or Hacker News - just r/ProtectAndServe ambient posts. Brinc is shipping aggressively and getting press coverage, but it is not generating organic Reddit or HN discussion the way Skydio and Flock are.

### Flock Safety

**The product surface keeps growing.** Following the [October 2024 Aerodome acquisition](https://www.flocksafety.com/blog/flock-safety-expands-into-drones-for-law-enforcement-with-acquisition-of-aerodome), the drone arm is now branded as [Flock Aerodome](https://www.flocksafety.com/products/flock-dfr), with the **Flock Alpha** drone as the DFR hardware - 60 mph cruise speed, license plate reads from 2,000 feet, four independent cellular modems for connectivity redundancy, automated docking and battery swap, BVLOS-capable software. On paper Flock is competitive with Skydio and Brinc on DFR.

**But the actual last-30-days story is backlash.** This is by far the strongest signal across the engine output - Flock dominates Hacker News and the privacy-focused subs in a way Skydio and Brinc do not:

- [Cities Are Covering Flock Cameras with Trash Bags](https://www.404media.co/cities-are-covering-flock-cameras-with-trash-bags/) - 404 Media, surfaced on HN (40pts, 17cmt) and cross-posted to r/technology and r/politics on 2026-05-28. The piece reports that cities locked into contracts are physically obscuring the cameras because they cannot exit the deal.
- [Bipartisan federal legislation that would have effectively banned police LPR (including Flock) was killed](https://ipvm.com/reports/bipartisan-alpr-amendment-killed) - HN 119pts, 74cmt, 2026-05-28. Surveillance-policy fight is now national.
- [After Town Bans Flock, Councilmember Crashes Out, Proposes Internet, Phone Ban](https://www.404media.co/after-town-bans-flock-councilmember-crashes-out-proposes-internet-and-phone-ban/) - HN 120pts, 109cmt, 2026-05-20.
- [At least 25 Flock cameras have been destroyed in five states since April 2025](https://stateofsurveillance.org/news/flock-cameras-destroyed-nationwide-ice-backlash-2026/) - HN 443pts, 326cmt, 2026-05-17. This is one of the biggest HN threads in the corpus.
- [Dayton suspends Flock contract, says data used for immigration enforcement](https://www.ohio.news/stories/dayton-authorities-say-that-flock-cameras-data-allegedly-used-for-immigration-enforcement/) - HN 94pts, 51cmt, 2026-05-07. The ICE-data narrative is the policy axis driving this.
- [Flock CEO calls Deflock a "terroristic organization"](https://www.reddit.com/r/FlockSurveillance/comments/1tvphvj/deflock_called_terroristic_organization_by_flock/) - r/FlockSurveillance, 2026-06-03. Tone has escalated.
- An entire subreddit, [r/FlockSurveillance](https://www.reddit.com/r/FlockSurveillance/), exists solely to track and oppose Flock. Multiple top threads in the last 30 days: [I sent an email regarding Flock cameras to my local police department](https://www.reddit.com/r/FlockSurveillance/comments/1tv7uwm/i_sent_an_email_regarding_flock_cameras_to_my/), [Flock around and find out](https://www.reddit.com/r/FlockSurveillance/comments/1trrx4c/flock_around_and_find_out/) (visible sabotage), [The Guardrail Guy documenting illegal installs](https://www.reddit.com/r/FlockSurveillance/comments/1tqzghh/the_guardrail_guy_a_dad_who_turned_his_daughters/) without required breakaway bases.
- [Flipper Zero can now detect Flock cameras](https://old.reddit.com/r/TikTokCringe/comments/1to4xfh/dystopia_speed_run/) - HN cross-post, 2026-05-26.
- [Editing PBF files to avoid Flock cameras with Android Auto](https://pickpj.github.io/Mapping/FIock/bigbrouter.html) - HN, 2026-05-20. The community is now building avoidance tooling.

The throughline: Flock Aerodome's drone story is technically credible, but every recent news cycle is consumed by ALPR backlash, immigration-data scandals, and physical sabotage. That makes Flock the company most exposed to political risk going into procurement decisions even as the actual hardware ships.

### Head-to-head

| Dimension | Skydio | Flock Safety (Aerodome) | Brinc |
|---|---|---|---|
| Core hardware | X10 / X10D (DFR + Army SRR) | Flock Alpha (DFR drone, LPR-from-air) | Guardian (DFR), LEMUR 2 (indoor tactical) |
| Public safety reach | 1,200+ agencies, 60K drones shipped | ALPR in thousands of cities; drones rolling out | 900+ agencies, 20%+ of US SWAT teams |
| Manufacturing | $3.5B / 5yr US build, SkyForge | US-made under NDAA | Seattle factory, vertically integrated |
| Funding (latest) | $110M Series F at $4.4B (Apr 2026) | Privately held, $7B+ valuation prior | $75M raise (Mar 2026) |
| Defense work | Army SRR program of record ($52M, 2500+ units) | None disclosed | None disclosed |
| Partnership stack | Axon RTCC + Ouster lidar | Owns ALPR + gunshot + DFR end-to-end | Motorola Solutions DFR partner |
| Last-30-days narrative | Manufacturing push + DFR scale | Surveillance backlash + sabotage + ICE data | DFR 3.0 messaging vs Skydio X10 |
| Positioning | "Safe pick" - most-deployed, longest reps | Software-forward platform (LPR + drone) | "Capability pick" - dual outdoor/indoor |
| Civil-liberties exposure | Emerging (one ICE-contract sighting in Humboldt) | Severe and ongoing | Low (purpose-built for tactical/SWAT) |

### Bottom line

The three companies are functionally non-overlapping today even though they will eventually compete head-to-head for the same DFR budget at the same agencies.

- **Choose Skydio if** you are an agency or investor optimizing for least-risk procurement, longest operational reps, deepest software/data moat, and a defense option. The $3.5B US manufacturing pledge is the strongest signal Skydio has ever sent that it intends to be a long-cycle prime, not a Silicon Valley quarterly story.
- **Choose Brinc if** the mission needs the **indoor + outdoor** package - SWAT entries, active-shooter response, hostage scenarios. Brinc owns the only credible US tactical drone today (LEMUR 2), and Guardian's 90-second battery swap is a genuine spec advantage over Skydio's X10 contact-charging for high-volume DFR queues.
- **Choose Flock if** you are already buying ALPR + gunshot detection from them and want the drone overlay on a single pane of glass. Just understand that you are buying into the most politically volatile brand of the three; Hacker News and at least one new dedicated subreddit are organized against the product.

The macro tailwind for all three is the same: the FCC's December 2025 Covered List essentially excluded DJI from US public-safety procurement, and the Office of Strategic Capital is now financing domestic drone supply chains. That is what is funding Skydio's $3.5B, Brinc's Seattle expansion, and Flock's drone push simultaneously - and it is why the [EFF flagged DFR program proliferation as the surveillance story of the year](https://www.eff.org/deeplinks/2025/12/drone-first-responder-programs-2025-review).

### Sources & raw artifacts

The engine's per-entity raw dumps are saved in this repo under `research/`:
- `research/skydio-raw-v3.md` (15 Reddit threads, 12 HN stories, 3 GitHub items)
- `research/flock-raw-v3.md` (rich Reddit + HN signal, see file for 30+ items)
- `research/brinc-raw-v3.md` and `research/brinc-drones-raw-brinc-targeted.md` (thin - see caveat above)
- `research/engine-output.log` and `research/brinc-targeted.log` (full engine traces)

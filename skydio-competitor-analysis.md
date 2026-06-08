🌐 last30days v3.3.2 · synced 2026-06-08

# Skydio vs Flock vs Brinc: What the Community Says (/Last30Days)

> Research generated with the [last30days](https://github.com/mvanhorn/last30days-skill) skill (v3.3.2) on 2026-06-08. Active sources this run: Reddit, Hacker News, GitHub. X/Twitter, YouTube, TikTok, and Polymarket were unavailable in this environment (no browser session, no yt-dlp, no ScrapeCreators key), and Reddit's keyed endpoint returned 403 on the comparison query - the RSS / public-JSON tier still pulled threads. Treat this as a community-signal snapshot, not a market-sizing report.

## Quick Verdict

The last 30 days are dominated by one story, and it is not a drone story - it is the Flock Safety civil-liberties backlash. Reddit, Hacker News, and an entire counter-surveillance ecosystem on GitHub are coordinating against Flock's automated license plate reader (ALPR) network after revelations that camera data flowed to ICE. Skydio shows up as a quietly executing defense and public-safety hardware vendor (Army X10D contract for the Short-Range Reconnaissance program, Drone-as-First-Responder dock deployments), with conversation concentrated in [r/Skydio](https://www.reddit.com/r/Skydio/) and the [Skydio GitHub org](https://github.com/Skydio). Brinc barely registers on the platforms this engine can see right now - evidence is genuinely thin, and the skill flagged it as such.

The three are not the same kind of company in the eyes of the community: Skydio is hardware-plus-autonomy, Flock is a fixed-camera surveillance network, Brinc is a tactical-response indoor drone. The only place they overlap is the emerging "drone as first responder" (DFR) category, which is the actual fight worth watching.

## Skydio

Skydio's last 30 days read as steady defense and public-safety execution rather than viral news. The most engaged thread on [r/Skydio](https://www.reddit.com/r/Skydio/) was a developer post asking for [sample flight logs](https://www.reddit.com/r/Skydio/comments/1tvj186/skydio_sample_logs/) to test a log-parsing platform - a small but telling signal that the community around Skydio is mostly builders and operators, not consumers.

The most concrete business item came from a defense-dashboard pull request that compiles verified military-contract data, which catalogues the [**Skydio X10D as a $52M U.S. Army contract for 2500+ units**](https://github.com/royconstantymartin-hub/defense-dashboard/pull/378) under the Short-Range Reconnaissance (SRR) program of record. The same item is corroborated by a [r/RedCatHoldings thread](https://www.reddit.com/r/RedCatHoldings/comments/1t8sn5n/us_army_small_uncrewed_aircraft_systems_programs/) summarizing the SRR program: "The Army's current selections for the SRR system are the Skydio X10D and the Teal Drones' Black Widow." That's the competitive frame inside defense - Skydio versus Teal (Red Cat), not versus Flock or Brinc.

On the autonomy side, an [r/drone_done thread](https://www.reddit.com/r/drone_done/comments/1tpnl3a/lmost_bought_a_skydio_2_instead/) titled "[A]lmost bought a Skydio 2+ instead" reads as the canonical Skydio review: "Test-flew a Drone_Done build and the Skydio's tracking is genuinely magic, no contest there. But for repair access and modding freedom, no contest the other way either." That captures the durable trade-off in the consumer/prosumer segment - autonomy leadership vs. closed ecosystem.

Skydio also appears in DFR plumbing. A [GitHub PR on clovenbradshaw-ctrl/DFR](https://github.com/clovenbradshaw-ctrl/DFR/pull/42) wires live Skydio ArcGIS feeds into a public flight-tracking map so brand-new flights are visible between scraper runs - independent infrastructure being built around Skydio's public DFR data feed. A separate [r/Humboldt post](https://www.reddit.com/r/Humboldt/comments/1top2zl/mobile_drone_dock_outside_blue_lake/) flags a Skydio-branded drone dock spotted on a shipping container outside Blue Lake, CA, with the poster noting: "If you google Skydio you can see ICE signed a contract with them recently." That ICE-adjacency note is the one place the Skydio narrative starts to intersect the Flock controversy.

On the engineering side, [Skydio/revup](https://github.com/Skydio/revup) shipped routine retry-splitting and GraphQL-utility improvements ([PR 254](https://github.com/Skydio/revup/pull/254), [PR 253](https://github.com/Skydio/revup/pull/253)) - their internal stacked-PR tool continues to be the most publicly visible piece of their engineering culture.

## Flock Safety

Flock is having the loudest 30 days of any company in this analysis, and almost none of it is good. The headline number from [stateofsurveillance.org via Hacker News](https://stateofsurveillance.org/news/flock-cameras-destroyed-nationwide-ice-backlash-2026/) ([443 points, 326 comments](https://news.ycombinator.com/)): "At least 25 Flock cameras have been destroyed in five states since April 2025." That story was the single highest-engagement HN item across the whole research run.

It is part of a connected cluster. [404 Media](https://www.404media.co/cities-are-covering-flock-cameras-with-trash-bags/) reported cities are physically bagging their Flock cameras. [r/InterstellarKinetics](https://www.reddit.com/r/InterstellarKinetics/comments/1tr6xcv/breaking_cities_are_covering_flock_safety_license/) named Dayton, Ohio specifically: "Dayton, Ohio has covered its network of Flock Safety automated license plate reader cameras with black trash bags after months of resident outrage, a scandal in which the city discovered it had been sharing camera data with Immigration and Customs Enforcement apparently by accident through Flock's national surveillance network, and a $30,000 audit into how the data was being used." [404 Media](https://www.404media.co/after-town-bans-flock-councilmember-crashes-out-proposes-internet-and-phone-ban/) also covered a councilmember reacting to a Flock ban by proposing to ban internet and phones too (120 HN points, 109 comments).

Trust-and-safety stories are stacking up alongside the political ones. [Times of San Diego](https://timesofsandiego.com/crime/2026/06/07/a-flock-license-plate-reader-linked-a-san-diego-man-to-a-violent-crime-he-was-five-miles-away/) reported a Flock LPR wrongly linked a San Diego man to a violent crime he was five miles away from. [IPVM](https://ipvm.com/reports/flock-review-dunwoody) ran "City and Flock Manipulate Security Scores," and a [second IPVM report](https://ipvm.com/reports/bipartisan-alpr-amendment-killed) noted that legislation that would have effectively blocked police LPR including Flock was killed.

Procurement transparency leaked too. A copy of the [Flock Safety Omnia Partners price list (PDF)](https://www.omniapartners.com/suppliers-files/E-J/Flock_Safety/Contract_Documents/R250203/5_29_2025_Flock_Safety_Omnia__R250203_Price_List.pdf) hit Hacker News, and [r/fortwayne](https://www.reddit.com/r/fortwayne/comments/1tn92p7/flock_safety_vote_tomorrow_ask_city_council_to/) organized a vote-no campaign citing the contract: "The cost for this year will be $120,250.00. Flock have added dozens of new cameras in the last few weeks. Visit [deflock.me](https://deflock.me) to view camera locations."

The counter-surveillance ecosystem on GitHub is now substantial and growing. A passive Flock-camera detector based on the 31-OUI MAC-prefix list was [ported into a security tool](https://github.com/yattsu/biscuit/pull/1) (credited to the original [colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)). The [none-below/sm-alpr](https://github.com/none-below/sm-alpr/pull/512) project is doing automated rolling refreshes of Flock's transparency-portal data. A full [iOS Flock Network Map app spec](https://github.com/Bobyman122/Claude-workspace/pull/2) shipped with 15 markdown spec files for camera-aware navigation. A [2600 / dwightspencer.com PR](https://github.com/denzuko/dwightspencer.com/pull/86) documented the Flock/Fusus/Raven hardware-and-software stack in detail. And [Hacker News surfaced](https://news.ycombinator.com/) "Flipper Zero Can Detect Flock Cameras" and "Editing PBF files to avoid Flock cameras (with Android Auto)" - both consumer-grade counter-surveillance.

Translation: Flock has mind share, but it is hostile mind share, and the activist + open-source community is treating Flock infrastructure as adversarial telemetry to be mapped, detected, and avoided.

## Brinc

Evidence is genuinely thin. The skill returned exactly two items for "Brinc Drones" - a generic [r/drones post](https://www.reddit.com/r/drones/comments/1tn9mmt/crazy_33615_drones_formed_what_is_currently_the/) about a 33,615-drone Chinese light show and a [Bloomberg HN item](https://www.bloomberg.com/news/articles/2026-06-02/russia-gushes-crude-exports-as-drone-strikes-hobble-refineries) about Russian drone strikes on refineries. Neither is actually about Brinc; both are entity-miss demotions, which means the engine matched "drone" but not "Brinc." A follow-up "Brinc Lemur" run was similarly empty. The engine explicitly flagged the topic as thin evidence.

What this means in practice: Brinc is not driving Reddit threads, HN discussions, or open-source projects in the way Skydio and Flock are right now. That is consistent with Brinc's market position - a smaller, tactical-response company (the Lemur indoor reconnaissance drone, used by SWAT and crisis-negotiation teams) that sells into a narrow customer set and doesn't generate broad community conversation. To get useful Brinc signal in a future run you would need X/Twitter (police-tech accounts), YouTube (their product demos and SWAT training videos tend to live there), and probably trade-press web search via Brave or Perplexity - none of which were available this run.

The one structural data point we do have is that a recent commercial-drone catalog refresh ([DroneWuKong/forge-data PR 77](https://github.com/DroneWuKong/forge-data/pull/77)) was explicitly motivated by the database being "skewed heavily defense/military; genuinely commercial & enterprise coverage was thin and patchy" - a reminder that Brinc lives in a public-safety niche where the open community signal is structurally quieter than Skydio's defense work or Flock's nationwide ALPR footprint.

## Head-to-Head

| Dimension | Skydio | Flock Safety | Brinc |
|---|---|---|---|
| Category | Autonomous aerial drones (consumer, enterprise, defense) | Fixed ALPR + camera network for police | Tactical indoor / response drones (Lemur) |
| Headline last 30d | $52M Army X10D SRR contract (2500+ units), DFR dock deployments | 25+ cameras destroyed since Apr 2025, ICE data-sharing scandal, cities bagging cameras | Almost no community signal in observed sources |
| Tone of coverage | Operational, defense-procurement, builder-led | Adversarial, civil-liberties backlash, counter-surveillance | Quiet |
| Open-source footprint | Active [Skydio/revup](https://github.com/Skydio/revup) PRs; third-party DFR integrations | Counter-Flock toolchain growing fast (detectors, map apps, transparency scrapers) | None observed |
| Community center | [r/Skydio](https://www.reddit.com/r/Skydio/) (builders), r/drone_done, r/RedCatHoldings | [r/fortwayne](https://www.reddit.com/r/fortwayne/comments/1tn92p7/flock_safety_vote_tomorrow_ask_city_council_to/), r/InterstellarKinetics, HN frontpage | r/drones (generic), no dedicated sub surfaced |
| Top organic comparison | Skydio vs Teal Drones (Black Widow) in Army SRR | Flock vs Fusus/Raven (technical), Flock vs deflock.me activists (political) | n/a |
| ICE / surveillance exposure | Mentioned once (ICE-Skydio contract noted in [Humboldt thread](https://www.reddit.com/r/Humboldt/comments/1top2zl/mobile_drone_dock_outside_blue_lake/)) | Central to the entire 30-day story | Not observed |
| Risk profile from this corpus | Reputational halo-effect from any deepening surveillance backlash | Acute - legislative, vandalism, civil-liability, and procurement risk all active | Underexposure risk (no public mindshare to defend or build on) |

## The Bottom Line

**Choose Skydio if you want autonomous aerial hardware that already has Army validation and a builder community.** The community signal is small but high-quality: the [Skydio X10D SRR win](https://github.com/royconstantymartin-hub/defense-dashboard/pull/378) is real, the autonomy lead is acknowledged even by competitors ([r/drone_done](https://www.reddit.com/r/drone_done/comments/1tpnl3a/lmost_bought_a_skydio_2_instead/) literally says "tracking is genuinely magic, no contest"), and third parties are building DFR integrations on top of their public data feeds ([clovenbradshaw-ctrl/DFR PR 42](https://github.com/clovenbradshaw-ctrl/DFR/pull/42)). The watch-out is the ICE-contract proximity surfaced in the [Humboldt thread](https://www.reddit.com/r/Humboldt/comments/1top2zl/mobile_drone_dock_outside_blue_lake/) - if the Flock backlash widens into a broader anti-public-safety-tech narrative, Skydio is the most obvious next target.

**Watch Flock if you want to understand how a surveillance-tech company loses the room.** The story is no longer "ALPRs reduce crime"; it is "[cities are covering Flock cameras with trash bags](https://www.404media.co/cities-are-covering-flock-cameras-with-trash-bags/)," "[25+ destroyed in five states](https://stateofsurveillance.org/news/flock-cameras-destroyed-nationwide-ice-backlash-2026/)," and "[wrongly linked to violent crime](https://timesofsandiego.com/crime/2026/06/07/a-flock-license-plate-reader-linked-a-san-diego-man-to-a-violent-crime-he-was-five-miles-away/)." When the [Flock Safety price list](https://www.omniapartners.com/suppliers-files/E-J/Flock_Safety/Contract_Documents/R250203/5_29_2025_Flock_Safety_Omnia__R250203_Price_List.pdf) is on Hacker News and the [Flipper Zero can detect their cameras](https://news.ycombinator.com/), the community has moved from debate to instrumentation. The counter-surveillance open-source stack ([flock-you](https://github.com/colonelpanichacks/flock-you), [sm-alpr](https://github.com/none-below/sm-alpr), [deflock.me](https://deflock.me)) is now mature enough that any new Flock deployment can expect to be mapped, detected, and challenged at the city-council level within weeks.

**Skip Brinc-from-public-signal for now.** That is not a verdict on the company - it is a verdict on what this engine could see in 30 days without X, YouTube, or paid web search. Brinc's audience is police-tech buyers, not Reddit or HN. To research Brinc properly, rerun with X/Twitter unlocked (their CEO Blake Resnick and the [@brincdrones](https://x.com/brincdrones) account are the right surface), YouTube transcripts (Lemur demos live there), and a Brave or Perplexity backend for trade-press coverage in [Police1](https://www.police1.com/), [Officer.com](https://www.officer.com/), and similar outlets.

## The Emerging Stack

The three companies are converging on one product category: drone-as-first-responder. Skydio brings the airframe and the autonomy; Flock brings the fixed sensor network and the police-CAD integrations; Brinc brings the indoor/tactical leg of the same call. Two of the three Reddit DFR threads in the last 30 days are new city programs - [r/nashville](https://www.reddit.com/r/nashville/comments/1tojgig/drone_as_first_responder_program_starting_in/) launching MNPD DFR (with [a community-built surveillance map](https://github.com/clovenbradshaw-ctrl/DFR/pull/5) tracking district overlays and launch radii), and [r/Dallas](https://www.reddit.com/r/Dallas/comments/1tizcrh/dallas_police_launch_new_drone_as_first_responder/) launching its own.

The thread to actually read is [r/ObscurePatentDangers](https://www.reddit.com/r/ObscurePatentDangers/comments/1td8l7y/chinese_air_traffic_police_drones_will_be_a/), which frames where this is going: "As of 2026, the 'Drone as First Responder' model is evolving from a simple emergency dispatch tool into a unified 'atmospheric operating system.'" If that framing sticks, the competitive battle stops being Skydio-vs-DJI or Flock-vs-Motorola and starts being about which vendor owns the city-wide aerial sensor layer. Skydio + Flock + Brinc collectively map onto that stack better than any single vendor does, which is also why every backlash story about one of them becomes a regulatory risk for all three.

---
✅ All agents reported back!
├─ 🟠 Reddit: ~15 threads across runs (some queries 403'd; RSS tier filled in)
├─ 🟡 HN: 12 stories │ 850+ points │ 580+ comments
├─ 🐙 GitHub: 38 items │ 68+ reactions │ 95+ comments
├─ 🗣️ Top voices: r/Skydio, r/fortwayne, r/InterstellarKinetics, r/Humboldt, r/nashville, r/Dallas, Skydio/revup, none-below/sm-alpr, clovenbradshaw-ctrl/DFR
└─ 📎 Raw results saved to `~/Documents/Last30Days/skydio-vs-flock-vs-brinc-raw.md`, `flock-safety-raw.md`, `skydio-raw-skydio-only.md`, `brinc-drones-raw.md`, `brinc-lemur-raw-brinc-lemur.md`, `drone-as-first-responder-raw-dfr.md`
---

### Notes on data quality this run

- **Reddit**: The keyed endpoint returned `403 forbidden` on the multi-entity comparison query; the RSS / public-JSON tier still pulled threads, so Skydio and Flock both got real Reddit signal. Brinc did not.
- **X / Twitter, YouTube, TikTok, Instagram, Polymarket, Perplexity, Brave web**: Not available in this environment. Re-running with browser cookies for X, `yt-dlp` for YouTube, and either `BRAVE_API_KEY` or `OPENROUTER_API_KEY` for grounded web would meaningfully change the Brinc verdict and would surface Skydio earnings / leadership statements and Flock's own PR response, none of which the open community sources captured.
- **GitHub**: Both Skydio and Flock have strong GitHub presence in this corpus - Skydio's own org (`Skydio/revup`) and a substantial counter-Flock toolchain (`none-below/sm-alpr`, `colonelpanichacks/flock-you`, `Bobyman122/Claude-workspace`, `denzuko/dwightspencer.com`, `yattsu/biscuit`).
- **No Polymarket markets** matched any of the three entities in the last 30 days.

Re-run command (with everything unlocked, for the next pass):

```bash
python3.12 skills/last30days/scripts/last30days.py \
  "Skydio vs Flock Safety vs Brinc" \
  --emit=md \
  --competitors-list "Flock Safety,Brinc" \
  --x-handle skydio --x-related "FlockSafety,brincdrones,Skydio,blakeresnick" \
  --github-user Skydio \
  --subreddits "skydio,drones,policedrones,commercialdrones,fucktheflock"
```

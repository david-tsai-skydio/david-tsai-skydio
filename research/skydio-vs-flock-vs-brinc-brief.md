# Skydio vs Flock vs Brinc: What the Community Says (/Last30Days)

> Generated 2026-06-06 using the [last30days-skill](https://github.com/mvanhorn/last30days-skill) engine
> (Reddit + Hacker News + GitHub sources active in this sandbox; X / YouTube / TikTok / Polymarket /
> Perplexity not available without their respective API keys / browser tokens).
> Engine date range: 2026-05-07 to 2026-06-06. Web supplement used to fill thin-evidence gaps on Brinc.

## Quick Verdict

Three U.S. drone makers, three different last-30-day stories.

- **Skydio** is the boring-but-winning incumbent. Quiet on social, loud on contracts: the X10D is now the U.S. Army's program-of-record quadcopter (alongside Teal's Black Widow), an ICE contract is up in the wild (mobile dock spotted in Humboldt County, CA), and city-scale Drone-as-First-Responder (DFR) wins keep landing through the Axon Air channel - Dallas just deployed 8 X10s on 911 calls, Orlando approved a $6.83M / 11-drone DFR program after a trial drone arrived before officers on 33% of calls.
- **Flock** is the company everyone is *fighting about*. The last 30 days are dominated by a backlash cycle: 25+ Flock LPR cameras physically destroyed across five states since April 2025 (443 pts on HN), cities literally putting trash bags over their own cameras, multiple state-level bills to ban Flock LPRs, Dayton suspending its Flock contract over immigration-enforcement data sharing, and Flock's CEO calling the DeFlock project a "terroristic organization." Its drone bet runs through the Aerodome acquisition (>$300M, Oct 2024), not anything that surfaced in this 30-day window.
- **Brinc** is the under-the-radar capability story. Almost no Reddit / HN chatter this window (the skill explicitly warned "evidence is thin"), but the trade press shows real momentum: the Lemur 2 indoor tactical drone, the new Guardian DFR platform with Starlink on every unit and 60+ mph vehicle-pursuit speed, a Motorola Solutions alliance for CAD / dispatch integration, and a joint Skydio+Brinc+Spot deployment in two Louisiana parishes.

If you wanted a one-liner: **Skydio = the safe, most-deployed picks; Flock = the political lightning rod that owns LPR and is buying its way into drones; Brinc = the purpose-built public-safety specialist that wins on indoor + autonomy + DFR feature depth, not on volume.**

## Skydio

What surfaced in the last 30 days:

- **U.S. Army SRR (Short-Range Reconnaissance) program of record.** A 2026-05-10 r/RedCatHoldings thread quotes the official program description: "The Army's current selections for the SRR system are the Skydio X10D and the Teal Drones' Black Widow." Skydio X10D is also tagged in a defense-dashboard GitHub PR as **"$52M Army, 2500+ units"** ([royconstantymartin-hub/defense-dashboard PR #378](https://github.com/royconstantymartin-hub/defense-dashboard/pull/378), 2026-05-31).
- **ICE / immigration enforcement footprint.** r/Humboldt user [reports](https://www.reddit.com/r/Humboldt/comments/1top2zl/mobile_drone_dock_outside_blue_lake/) a shipping container with a Skydio-branded drone dock and ring cameras on a perimeter east of Blue Lake, CA, noting "ICE signed a contract with them recently." This is the same line that runs through the Flock controversy (immigration data sharing) but for hardware rather than LPR data.
- **City DFR wins keep landing through Axon.** Web supplement (not in the engine's 30-day pull but adjacent): Dallas PD launched its DFR program 2026-05-20 with **8 Skydio aircraft from fire stations, 2-mile radius each, run from the Real Time Crime Center** ([dronexl.co](https://dronexl.co/2026/05/25/skydio-drones-dallas-911-calls/)); Orlando approved $6.83M / 11-drone DFR after the pilot showed **drones arriving before officers on 33% of calls and delivering useful info on 97%** ([dronexl.co](https://dronexl.co/2026/02/25/orlando-skydio-drone-program/)). Orlando's chief explicitly said Brinc "could not match" Axon-Skydio's body-cam and 911 integration, and Flock "failed to provide us with a product to evaluate."
- **The community comparison.** r/drone_done's ["lmost bought a Skydio 2+ instead"](https://www.reddit.com/r/drone_done/comments/1tpnl3a/lmost_bought_a_skydio_2_instead/) (score 29, 2026-05-28) gives you the prosumer take in one quote: "the Skydio's tracking is genuinely magic, no contest there. But for repair access and modding freedom, no contest the other way." Autonomy is still the moat. Repairability is still the weakness.
- **GitHub signal.** Most of the Skydio-tagged GitHub traffic is internal: PRs against [Skydio/revup](https://github.com/Skydio/revup) (Skydio's open-source stacked-PR tool for GitHub) plus a kevin-pan-skydio PR into [grpc/grpc](https://github.com/grpc/grpc/pull/42577). r/Skydio itself is small ([r/Skydio Sample Logs](https://www.reddit.com/r/Skydio/comments/1tvj186/skydio_sample_logs/), score 32) - this is a B2G/B2B company, not a Reddit-forward consumer brand.

The picture: **Skydio is winning the procurement war while keeping a low Reddit / X profile.** That's the opposite of Flock's posture this month.

## Flock

This is the story of the window. Flock dominates Hacker News and r/FlockSurveillance, and the energy is almost entirely negative:

- **Physical resistance.** "[At least 25 Flock cameras have been destroyed in five states since April 2025](https://stateofsurveillance.org/news/flock-cameras-destroyed-nationwide-ice-backlash-2026/)" landed **443 points / 326 comments on HN** (2026-05-17). "[Cities Are Covering Flock Cameras With Trash Bags](https://www.404media.co/cities-are-covering-flock-cameras-with-trash-bags/)" hit HN (40 pts / 17 cmt), r/technology, and r/politics in the same week - the framing in r/technology is on the nose: "Regretful cities aren't sure how to cancel their surveillance contracts, so they are literally covering their cameras."
- **Legislative backlash.** A 2026-05-28 IPVM report, "[Legislation Killed Would Have Effectively Blocked Police LPR, Including Flock](https://ipvm.com/reports/bipartisan-alpr-amendment-killed)" pulled **119 pts / 74 cmt on HN**. "[After Town Bans Flock, Councilmember Crashes Out, Proposes Internet, Phone Ban](https://www.404media.co/after-town-bans-flock-councilmember-crashes-out-proposes-internet-and-phone-ban/)" hit **120 pts / 109 cmt**. A 2026-06-04 r/Maine post details a state bill from Rep. David Boyer (R-Poland) to "ban almost all of the controversial automatic license plate readers popping up around the state."
- **Immigration-enforcement scandal.** "[Authorities say Flock cameras' data allegedly used for immigration enforcement](https://www.ohio.news/stories/dayton-authorities-say-that-flock-cameras-data-allegedly-used-for-immigration-enforcement/)" was the top story on 2026-05-07 (94 pts / 51 cmt), and Dayton suspended its Flock contract the same day. This is the same political risk vector now circling Skydio's ICE work but with a year-long head start.
- **CEO escalation, community fights back.** A 2026-06-03 r/FlockSurveillance post titled "[Deflock called 'terroristic organization' by Flock CEO](https://www.reddit.com/r/FlockSurveillance/comments/1tvphvj/deflock_called_terroristic_organization_by_flock/)" frames it. So does "[I got perma banned from my local area sub Reddit because I brought up my concerns with flock](https://www.reddit.com/r/FlockSurveillance/comments/1touhgi/i_got_perma_banned_from_my_local_area_sub_reddit/)" (2026-05-27). Counter-projects: [DeFlock](https://deflock.me) crowdsources camera locations, the Flipper Zero detection trick ([HN](https://old.reddit.com/r/TikTokCringe/comments/1to4xfh/dystopia_speed_run/), 2026-05-26), and [PBF-editing tutorials](https://pickpj.github.io/Mapping/FIock/bigbrouter.html) so Android Auto can route you around the cameras.
- **Drone bet, off-window but central.** Flock's drone strategy is the **$300M+ October 2024 acquisition of Aerodome** ([TechCrunch](https://techcrunch.com/2024/10/23/flock-safety-paid-over-300-million-for-17-month-old-drone-startup-aerodome/)) plus the [Aerodome-Flock partnership](https://www.flocksafety.com/blog/aerodome-and-flock-safety-forge-strategic-partnership-to-expand-drone-as-first-responder-technology-for-public-safety-agencies) that wires Falcon LPR / Raven gunshot detection into auto-dispatched DFR drones. Orlando this year reported Flock "failed to provide us with a product to evaluate," so the integration is still ahead of the hardware in some markets.

The picture: **Flock has the brand, the AI-trigger story, and the political problem.** This is the only one of the three companies whose name comes up unprompted across r/politics, r/technology, and HN front page in the same week, and it's almost never positive.

## Brinc

The skill explicitly warned "evidence is thin for this topic" on Brinc - the Reddit corpus on "Brinc" gets polluted by `r/okbuddychicanery` ("Brince"), r/Monopoly_GO ("brinc"-fragment matches), and gluten-free teacher posts. That itself is a finding: **Brinc is not a Reddit / HN protagonist this month.** It is a trade-press and procurement story.

What was real, from web supplement:

- **Product line.** **Lemur 2** (indoor tactical, ~20-min flight, LiDAR-driven autonomy in GPS-denied / dark spaces, self-rights, glass-breaker payload, 4K + FLIR thermal, 1-lb payload for Narcan / phones / medical supplies, two-way audio); **Brinc Ball** (throwable); **Responder** (dock-based outdoor DFR aircraft); **Guardian** (the new flagship - announced March 2026 - **Starlink on every unit**, **60+ mph top speed**, **1+ hr flight time**, automated battery swap in ~1 minute, payloads include floatation device, AED, EpiPens, Narcan). Quote of the launch from founder Blake Resnick on [Ars Technica](https://arstechnica.com/gadgets/2026/03/brincs-new-police-drone-uses-starlink-carries-narcan-chases-vehicles-at-60mph/): "Guardian is more of a direct police helicopter competitor than the drone industry has produced to date." Critic counterpoint in the same piece: an EFF source called it "an incremental improvement over other comparable drone platforms."
- **Customers and capital.** **Over 900 American cities** using Brinc hardware (Laredo, Chattanooga, Redmond WA, etc.). Around **$82M raised** from backers including Peter Thiel and Sam Altman ([dronexl.co](https://dronexl.co/2026/05/28/skydio-brinc-robot-dog-louisiana/)).
- **Co-deployment, not just competition.** A May 2026 Louisiana DA-funded program splits the buy: **West Baton Rouge SO gets four Skydio X10s + a Boston Dynamics Spot**, **Iberville Parish SO gets three Brinc drones, one a dedicated DFR aircraft in a hangar**. Both procurements skipped DJI entirely. Same article: "BRINC has carved out the DFR niche fast."
- **Where Brinc wins vs Skydio.** The cleanest framing was in the Minneapolis DFR analysis: Skydio X10 is "the safe pick, the most-deployed American platform, the option that draws the least political fire and the most operational reps." Brinc Responder + Lemur 2 is "the capability pick" because it adds **indoor tactical entry** (glass-break, GPS-denied autonomy, throwable, self-righting) **in the same product family**. Cost-per-unit is higher, operational maturity is less.
- **What Reddit *did* surface that's adjacent.** [r/RedCatHoldings on the U.S. Army SRR program](https://www.reddit.com/r/RedCatHoldings/comments/1t8sn5n/us_army_small_uncrewed_aircraft_systems_programs/) - Brinc is NOT named in the Army SRR selection (Skydio X10D and Teal Black Widow are). Brinc's lane is municipal public safety, not DoD platoon recon. That's a clean wedge between the two.

The picture: **Brinc is the specialist.** Best-in-class indoor tactical drone in the U.S. market, a fresh DFR flagship (Guardian) that goes vertically against Skydio + Aerodome, and a procurement story that's growing fast but doesn't have the social-media surface area of either rival.

## Head-to-Head

| Dimension | Skydio | Flock | Brinc |
|---|---|---|---|
| What it is | Autonomous outdoor drone maker, DFR + DoD | Surveillance platform (LPR / audio / cameras) + drones via Aerodome acquisition | Purpose-built public-safety drones, indoor + DFR |
| Hero product (last 30d) | X10 / X10D | Falcon LPR + Aerodome DFR | Lemur 2 (indoor) + Guardian (DFR, Starlink, 60+ mph) |
| Government wins | U.S. Army SRR program of record; ICE contract; Dallas, Orlando, hundreds of PDs via Axon | ~5,000 communities on LPR; trying to enter DFR | 900+ U.S. cities; Louisiana parish DFR + tactical |
| Channel | Axon Air (bundled with body cams + evidence mgmt) | Direct sales; LPR network effect | Direct sales; Motorola Solutions alliance |
| Backers | Andreessen Horowitz, public via DoD contracts | Andreessen Horowitz, late-stage growth | Peter Thiel, Sam Altman, ~$82M raised |
| Last-30d Reddit / HN energy | Quiet (12 Reddit, 12 GitHub items, small r/Skydio) | Loud and negative (multiple front-page HN, r/politics, r/technology, r/FlockSurveillance very active) | Effectively silent on social (engine warned "thin evidence") |
| Biggest 30d risk | ICE contract starting to attract the same political attention Flock already has | Camera destruction, state-level bans, immigration-enforcement scandal | Operational maturity vs Skydio; higher per-unit cost |
| Biggest 30d tailwind | Army program of record + Axon channel + Dallas / Orlando DFR | None visible in this window; the news cycle is uniformly bad | Guardian launch press; Louisiana joint deployment; Motorola CAD integration |
| Best for | Departments that want the most-deployed, Axon-integrated DFR with a track record | Departments already on Flock LPR / Raven who want auto-triggered DFR | Departments that need indoor tactical + DFR in one vendor, can pay a premium |

## The Bottom Line

- **Pick Skydio if** your buyers are procurement officers comparing operational track record, your channel partner is Axon, or you have DoD adjacency. The political downside is real (ICE contract is now in the wild on Reddit) but the upside - the Army SRR pick, the Dallas / Orlando DFR launches - is bigger than anyone else's this month.
- **Pick Flock if** you already run their LPR / audio network and want the DFR layer to auto-dispatch off existing sensor triggers. Just know that "Flock" is currently the most controversial brand name in U.S. local-government surveillance, the cameras are being physically attacked in five states, multiple state bills are pending, and Orlando publicly said they couldn't get a drone product to evaluate. The integration story is real; the political and supply-execution story is not yet.
- **Pick Brinc if** you specifically need indoor tactical capability (glass-break, GPS-denied, throwable, self-righting) in the same vendor as your outdoor DFR drone, and you have the budget for the per-unit premium. Guardian is the most aggressive new DFR spec sheet in the U.S. (Starlink, 60+ mph, 1+ hr) and Motorola CAD integration is closing the dispatch-software gap that Axon-Skydio currently owns.

## The emerging stack

The 30-day pattern across all three is that **the DJI ban is now a foregone conclusion in U.S. public-safety procurement**, and the question is not "American or Chinese" but "which American stack." Three stacks are visible:

1. **Axon + Skydio** (body cam + evidence + DFR aircraft + Dedrone counter-drone, one procurement relationship). Most-deployed, lowest political surface area in the air; growing political surface area on the ground because of ICE contract optics. Vendor lock-in is a feature for the buyer and an explicit Dallas talking point.
2. **Flock + Aerodome** (LPR + audio + auto-triggered DFR). Strongest sensor-fusion story in theory; weakest community-reception story in practice. Anywhere the Flock political fight matters, the integration advantage doesn't.
3. **Brinc + Motorola** (DFR aircraft + indoor tactical drone + CAD/dispatch integration). The capability ceiling pick. Lower deployment volume than Skydio, but the feature roadmap (Guardian + Lemur 2 in one vendor + Motorola CAD) is the closest thing to a Skydio-Axon alternative.

The cities are picking sides. Louisiana DA Tony Clayton's program funded **both** Skydio and Brinc, which is the new normal: agencies buying DFR aircraft from Skydio for outdoor 911 response and Brinc Lemur 2s for indoor entry, because no single vendor yet covers the full call mix.

---

## Engine footer (sources, /last30days raw output)

```
✅ All agents reported back!
├─ 🟠 Reddit: 12 threads (Skydio) + 12 threads (Flock) + 12 threads (Brinc, mostly off-topic noise)
├─ 🐙 GitHub: 12 items (Skydio) + ~10 items (Flock) + 1 item (Brinc)
├─ 🟢 Hacker News: 0 (Skydio) + ~10 items (Flock, multiple 100+ point threads) + 0 (Brinc)
├─ 🗣️ Top voices: r/Skydio, r/FlockSurveillance, r/drone_done, r/Humboldt, HN front page, Skydio/revup
└─ 📎 Raw results saved to research/skydio-last30days-raw.md, flock-last30days-raw.md, brinc-last30days-raw.md, brinc-lemur-targeted-raw.md
```

## Caveats

- The /last30days engine in this sandbox had **4 of 13 possible sources** active (Reddit, Hacker News, GitHub, Polymarket). X / Twitter, YouTube, TikTok, Instagram, Threads, Bluesky, Pinterest, Perplexity, and the Brave web backend were not configured (no `SCRAPECREATORS_API_KEY`, no Bird X auth, no `OPENROUTER_API_KEY`, no `BRAVE_API_KEY`). With those wired up, the Brinc thinness almost certainly fills in (Brinc is more visible on YouTube police-tech channels and X than on Reddit), and Skydio's X presence would carry the founder / DoD signal that doesn't make it to r/Skydio.
- The 2026-05-28 Louisiana, 2026-05-20 Dallas, and 2026-02-25 Orlando city-DFR launches were filled in via WebSearch supplementing the engine's raw evidence, since the engine's Reddit/HN/GitHub corpus didn't surface them organically in the 30-day window.
- Polymarket: no live markets on Skydio / Flock / Brinc surfaced. (There were noisy "Apple"-style false positives demoted by the engine's common-word disambiguation.)
- Brinc's Reddit footprint is genuinely small and dominated by namespace collisions ("Brince" the Breaking-Bad/Better-Call-Saul character, "brinc" fragment in Monopoly GO posts). The targeted re-run with a forced `--plan` (pinning r/BRINC, r/police, r/publicsafety, etc.) returned only one off-topic HN item ("Russia ships oil"). This is a real signal, not a tooling failure: the Brinc community lives in trade press and on LinkedIn / X, not Reddit.

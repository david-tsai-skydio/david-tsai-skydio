# Skydio vs Flock Safety vs Brinc: What the Last 30 Days Say (May 2026)

> Research compiled with the [`last30days`](https://github.com/mvanhorn/last30days-skill) skill (v3.3.1) plus targeted web search, covering 2026-05-01 to 2026-05-31. Skill ran with Reddit, Hacker News, and GitHub as active sources (no X, TikTok, or paid web backend keys configured); the noisy Brinc Reddit hits (r/okbuddychicanery, r/glutenfree, r/HazbinHotel, r/Monopoly_GO) were filtered out as `entity-miss demotions` and the synthesis below leans on the web-search supplement to fill the gap for that entity.

## Quick Verdict

The three companies are no longer in the same market - they are converging on the same customer (US public safety agencies and federal buyers) from three different starting positions, and the last 30 days made those positions sharper, not blurrier.

- **[Skydio](https://www.skydio.com/)** is the outdoor-autonomy + defense-procurement category leader. It hit a $4.4B valuation on a deliberately small $110M Series F, committed $3.5B to US manufacturing, and is putting X10 fleets on city rooftops through Axon as the distribution channel. Risk surface: a real cloud outage on May 6-7 and political exposure on an ICE contract.
- **[Flock Safety](https://www.flocksafety.com/)** is the surveillance-ecosystem play. ALPR + gunshot detectors + [Flock Alpha](https://www.flocksafety.com/products/flock-dfr) DFR (post-Aerodome) + [FlockOS](https://www.flocksafety.com/) RTCC. The platform story is the strongest of the three. The trust story is the weakest: cities cancelling contracts, cameras being physically destroyed, and an [FBI move](https://www.404media.co/) toward a $36M national LPR contract that scares city councils.
- **[Brinc](https://brincdrones.com/)** owns the tactical / medical-payload niche and is the upstart with the most surprising hardware. The March-2026 [Guardian](https://brincdrones.com/news/brinc-unveils-guardian-launching-the-next-era-of-drone-as-first-responder/) launch (satellite-connected, robotic 40-second battery swap) plus the Motorola exclusive reseller agreement gives it a credible second public-safety stack opposite Axon/Skydio.

## Skydio

**Financials and posture.** Skydio raised [$110M Series F at a $4.4B post-money valuation on April 23, 2026](https://www.cbinsights.com/company/skydio/financials), led by existing investors. CEO Adam Bry framed the round on [Skydio's blog](https://www.skydio.com/blog/skydio-series-f) as "the most significant fact is how little we are raising" - the company is funding most of its operations from a core business doing hundreds of millions in annual revenue with strong unit economics, hypergrowth, and ~60,000 drones shipped to ~4,000 enterprise/government customers. Per [Sourcery's interview with Bry](https://www.sourcery.vc/p/breaking-skydio-hits-44b-with-110m), production is tripling in 2026 and "the number one constraint is building more drones faster." On May 4, Skydio announced a [$3.5B, five-year US manufacturing expansion](https://www.police1.com/police-products/Police-Drones/skydio-to-invest-3-5b-in-u-s-drone-manufacturing-expansion) including a new facility five times larger than its current Bay Area footprint - explicitly framed as a response to being cut off from Chinese batteries by Beijing in October 2025.

**Defense pipeline.** The [robotics.press deep dive](https://robotics.press/news/skydio-deep-dive/) catalogs a $52M+ X10D order from the US Army (largest single-vendor tactical sUAS contract in Army history) and selection for the Missile Defense Agency's $151B SHIELD vehicle. The r/RedCatHoldings thread ["U.S. Army Small Uncrewed Aircraft Systems Programs"](https://www.reddit.com/r/RedCatHoldings/comments/1t8sn5n/us_army_small_uncrewed_aircraft_systems_programs/) (score 29) corroborates: the Army's Short-Range Reconnaissance (SRR) program of record - first quadcopter program of record for Army platoons - is the X10D and Teal Drones' Black Widow.

**Public safety - Drone as First Responder.** Dallas went live May 20 with eight Skydio X10 aircraft on Dallas Fire-Rescue rooftops through a [$120.6M Axon contract amendment](https://dronexl.co/2026/05/25/skydio-drones-dallas-911-calls/); first operational use removed a man from Interstate 45 the next day. Nashville started a [45-day pilot with three loaner Skydio aircraft on May 26](https://dronexl.co/2026/05/27/nashville-police-45-day-skydio-dfr/), kicking the tires before committing. Louisiana DA Tony Clayton is funding [4 X10s for the West Baton Rouge Sheriff's Office](https://dronexl.co/2026/05/28/skydio-brinc-robot-dog-louisiana/) alongside Boston Dynamics' Spot.

**Risk surface visible in last30days.** Two:
1. **Cloud incident.** Skydio's [own post-incident review](https://www.skydio.com/blog/post-incident-review-for-degraded-connectivity-may-2026) details a May 6-7 connectivity degradation: a timer-overflow bug in Skydio Cloud after long uptime caused video throttling from 3-5 Mbps to 0.5 Mbps for X10 Dock customers, preventing missions. A pure software issue, but a credibility-relevant one for a vendor pitching 99.9% mission completion.
2. **Civil-liberties exposure.** A [r/Humboldt thread](https://www.reddit.com/r/Humboldt/comments/1top2zl/mobile_drone_dock_outside_blue_lake/) (score 31) about a Skydio-branded mobile drone dock outside Blue Lake, CA, surfaced the same week as reporting that ICE signed a contract with Skydio. That is the kind of single-thread signal that compounds into the political headwind Flock is already living inside.

## Flock Safety

**Strategy.** Flock has spent the last year welding three businesses into one platform: ALPR cameras (the core 12,000+ customer base per [a16z's portfolio piece](https://www.a16z.news/p/flock-and-the-future-of-safety-in)), gunshot/HD/PTZ situational-awareness cameras, and - since the [Aerodome acquisition](https://www.policemag.com/news/flock-safety-expands-into-drones-for-law-enforcement-with-acquisition-of-aerodome) - Drone as First Responder via the [Flock Alpha aircraft and Flock Aerodome software](https://www.flocksafety.com/products/flock-dfr). The pitch is single-vendor: an ALPR hit, a gunshot detection, or a 911 call automatically launches a drone that arrives in ~86 seconds with full chain-of-custody video into FlockOS. The Aerodome deal also commits Flock to "a suite of American-made, NDAA-compliant drones over the next 12 months," produced at a 97,000-sq-ft factory near Atlanta. On February 10 Flock extended this into the private sector with [Flock DAS (Drone as Automated Security)](https://www.flocksafety.com/blog/flock-safety-launches-flock-aerodome-drone-as-automated-security), targeting warehouses, rail yards, hospital campuses, ports, malls, and business parks with 3.5-mile-radius coverage per dock.

**The trust crisis is the story.** This is the dimension where the last 30 days punished Flock the hardest. From Hacker News alone:
- ["At least 25 Flock cameras have been destroyed in five states since April 2025"](https://stateofsurveillance.org/news/flock-cameras-destroyed-nationwide-ice-backlash-2026/) - 443 points, 326 comments. The vandalism framing is explicitly "ICE backlash."
- ["After Town Bans Flock, Councilmember Crashes Out, Proposes Internet, Phone Ban"](https://www.404media.co/after-town-bans-flock-councilmember-crashes-out-proposes-internet-and-phone-ban/) - 120 points, 109 comments.
- ["Cities Are Covering Flock Cameras with Trash Bags"](https://www.404media.co/cities-are-covering-flock-cameras-with-trash-bags/) - 40 points, 17 comments.
- ["Legislation Killed Would Have Effectively Blocked Police LPR, Including Flock"](https://ipvm.com/reports/bipartisan-alpr-amendment-killed) - 119 points, 74 comments.

City-level: [Edmonds, WA cancelled its Flock contract on May 27](https://www.heraldnet.com/2026/05/27/edmonds-becomes-3rd-city-in-the-county-to-cancel-flock-safety-contract/) - the third Snohomish County city to do so. Mayor Mike Rosen cited [404 Media's May 18 report](https://www.404media.co/) that the FBI is seeking up to $36M for warrantless access to a nationwide LPR network - a market only Flock and Motorola Solutions can serve. [Reddit r/fortwayne](https://www.reddit.com/r/fortwayne/comments/1tn92p7/flock_safety_vote_tomorrow_ask_city_council_to/) (score 37) organized a "VOTE NO" campaign against renewing a $120,250 contract; [r/ObscurePatentDangers](https://www.reddit.com/r/ObscurePatentDangers/comments/1t7e92t/privacy_vs_protection_it_expert_leads_deflock/) (score 30) profiled "Deflock Corona," an IT-network-architect-led local repeal effort.

**The hostility shows up in code, too.** Three GitHub artifacts surfaced in the last 30 days that have no parallel on the Skydio or Brinc side:
- [`none-below/sm-alpr`](https://github.com/none-below/sm-alpr/pull/512) - an automated rolling refresh of "Flock Safety transparency portal data" diffing departmental ALPR SOPs over time (scores 39 and 35 on two PRs).
- [`denzuko/dwightspencer.com#86`](https://github.com/denzuko/dwightspencer.com/pull/86) - "ALPR infrastructure stack - what Flock Safety actually is" - a 2600-magazine piece reverse-engineering Falcon camera hardware, NVLS database, hot-list system, retention defaults, and Flock+Fusus+Raven integration (score 34).
- [`yattsu/biscuit#1`](https://github.com/yattsu/biscuit/pull/1) - "Flock-You passive Flock Safety camera detector," a port of `colonelpanichacks/flock-you` with a 31-OUI detection list to passively spot Flock devices on the network (score 31).

You can build a thriving ALPR business with that much organized opposition. But the cost-of-customer-acquisition slope is bending against Flock in a way it isn't against the other two.

**Pro side, for balance.** The [a16z piece](https://www.a16z.news/p/flock-and-the-future-of-safety-in) cites San Francisco - 400 LPRs + 80 drones deployed in 2024, major crimes down 44%, car thefts down 54% from 2023-2025, SFPD spokesperson Evan Sernoffsky crediting the tooling. Elk Grove, CA hits 911 calls in 68 seconds (vs 7.5-minute baseline). Operationally the product works; politically the product is contested.

## Brinc

**Profile.** Per the [Louisiana DA deal coverage](https://dronexl.co/2026/05/28/skydio-brinc-robot-dog-louisiana/), Brinc was founded by Blake Resnick in 2019 (Seattle), has raised ~$82M from backers including Peter Thiel and Sam Altman, and runs equipment at "over 20 percent of U.S. SWAT teams" and 900+ public safety agencies. The product line splits into three jobs: the **Lemur 2** for indoor tactical entry (LiDAR autonomy, no-GPS no-light hover, glass-breaking, 1 lb payload like a Narcan kit, two-way de-escalation speaker/microphone), the **Responder** for outdoor DFR (42-minute flight, IPX4, thermal + loudspeaker), and the brand-new **Guardian**.

**Guardian launch (March 24, 2026) reshaped the conversation in May.** [Brinc's announcement](https://brincdrones.com/news/brinc-unveils-guardian-launching-the-next-era-of-drone-as-first-responder/) and the follow-up [TechBullion piece](https://techbullion.com/brinc-drones-guardian-built-around-the-charging-problem-that-has-kept-emergency-drones-grounded/) frame Guardian as "the world's first satellite-connected drone" with a robotic Guardian Station that physically swaps batteries and reloads payloads in under 40 seconds (vs the 25+ minute contact-charging baseline that has kept DFR drones grounded between calls). The payload bay holds 10 lbs across 20 climate-controlled slots: defibrillators, Narcan, EpiPens, flotation devices, trauma kits, and for tactical deployments Motorola radios, hazmat sensors, and comms gear. The hardware story is purpose-built for two trends: FAA cutting DFR waiver approval from 11 months to roughly one week in 2025 (410 authorizations in the first two months - nearly a third of all DFR waivers ever granted), and the Motorola Solutions exclusive North American reseller alliance feeding 911 keyword detection (Assist AI on CommandCentral Aware) into automatic Guardian dispatch.

**May procurement wins.** [St. Louis Board of Police Commissioners approved six BRINC Responder DFR drones on May 27](https://dronexl.co/2026/05/28/st-louis-six-brinc-drones/), two each across north, south, and central patrol areas, with Mayor Cara Spencer publicly calling the vote "rushed" - the funding deadline plus the city's 2028 LA Games Olympic-soccer hosting created the urgency. The same week, the Iberville Parish Sheriff (LA) added three BRINC drones - one Responder DFR in a hangar near Plaquemine, two Lemur 2s for tactical entry - paid for by [DA Tony Clayton's cooperative endeavor](https://www.theadvocate.com/baton_rouge/news/crime_police/west-baton-rouge-iberville-tony-clayton/article_c422a8ce-5463-4f68-9da4-97fbc4adda59.html) alongside the Skydio order for the West Baton Rouge Sheriff next door.

**Brinc engine signal note.** The last30days engine on a 4-letter keyword like "Brinc" pulled in heavy false-positive Reddit noise (r/okbuddychicanery, r/glutenfree, r/Monopoly_GO, r/HazbinHotel) - all demoted to score 0 with `entity-miss demotion`. The fix going forward is `--polymarket-keywords` and a tighter handle-resolution plan; for now the WebSearch supplement carries the load for Brinc.

## Head-to-Head

| Dimension | Skydio | Flock Safety | Brinc |
|---|---|---|---|
| Origin story | 2014, autonomous flight first - Bay Area | 2017 ALPR cameras - Atlanta | 2019 tactical drones - Seattle |
| Flagship aircraft | X10 / X10D | Flock Alpha (ex-Aerodome) | Lemur 2 (indoor), Responder (DFR), Guardian (satellite + auto-battery-swap) |
| Strongest job | Outdoor DFR + defense-grade ISR | Surveillance ecosystem - drones bolted onto ALPR + gunshot + RTCC | Indoor tactical entry + medical-payload delivery, now 24/7 DFR via Guardian |
| Public-safety stack partner | Axon (body cams, evidence.com, RTCC) | First-party FlockOS | Motorola Solutions (CommandCentral Aware, APX NEXT radios) |
| Defense / federal traction | Army SRR program of record, $52M X10D order, MDA SHIELD, US AFCENT airbase Docks | Limited - DFR + ALPR are city/private | None disclosed in last 30 days |
| Latest funding | $110M Series F @ $4.4B (Apr 2026) | a16z portfolio, ~$1B+ raised historically | ~$82M total per Forbes (Thiel, Altman) |
| Customers (claimed) | ~4,000 enterprise + government, 1,200+ public safety agencies, every DoD branch, 29 allied nations | 12,000+ across LE and private | 900+ public safety agencies, 20%+ of US SWAT teams |
| US-manufacturing posture | $3.5B/5-yr expansion; 5x current Bay Area space; explicit Chinese-supply-chain hedge | 97,000-sq-ft Atlanta drone factory; NDAA-compliant suite "in next 12 months" | Seattle-based; promotes "American-made" |
| Visible May 2026 wins | Dallas DFR (8x X10 via Axon), Nashville pilot, West Baton Rouge LA | University of St. Thomas connected-campus program (May 7) | St. Louis (6x Responder), Iberville Parish LA (3x) |
| Visible May 2026 risk | Cloud outage May 6-7 (timer overflow); ICE contract scrutiny | Cities cancelling contracts, 25+ cameras destroyed since Apr 2025, FBI $36M LPR procurement triggering blowback | Lower public profile; 4-letter brand name creates monitoring noise |

## The Bottom Line

**Choose Skydio if** the buyer is a defense agency, a major-metro PD that has already bought into the Axon ecosystem, or any operator who weights autonomous outdoor mission-completion above everything else. The DJI ban plus the Beijing battery cutoff have given Skydio the closest thing to a regulatory moat any US drone OEM has ever held, and the Series F structure (deliberately small, oversubscribed) suggests a company approaching profitability rather than chasing it. The May cloud outage is a real but bounded incident that does not change the trajectory.

**Choose Flock Safety if** the buyer wants one vendor for cameras, drones, and the RTCC software that ties them together, and is operating in a jurisdiction where the privacy debate has already been litigated and resolved in favor of deployment. Operationally the product is strong (San Francisco's crime drop is a real datapoint). Reputationally the company has the hardest political ground of the three to defend, and the last 30 days made it harder, not easier.

**Choose Brinc if** the mission profile is tactical entry, indoor mapping, or medical-payload delivery, or if the buyer wants a public-safety stack outside the Axon orbit. Guardian's robotic battery/payload swap is the single most interesting hardware artifact across all three companies' May 2026 surface area; if the FAA waiver backlog really has cleared and 24/7 DFR is the next category, Brinc + Motorola is set up to ride it harder than the other two.

## The Emerging Stack

US public safety drones have stratified into two procurement super-stacks plus a contested middle.

- **Axon + Skydio** is the outdoor-DFR and evidence-management stack. Body cameras feed dispatch, dispatch summons drones, drone video lands on evidence.com next to body-camera video, and the same procurement contract buys counter-drone sensors for major events (Dallas explicitly bundled both into the same $120.6M amendment in anticipation of World Cup and LA Games hosting). Switching cost is rising fast.
- **Motorola Solutions + Brinc** is the 911-dispatch + tactical / medical-payload stack. Assist AI watches calls for keywords like "heart attack" or "allergic reaction" and tees up the right Guardian payload before the dispatcher even speaks; the APX NEXT smart-radio panic button can launch a drone toward an officer in distress. This stack is younger but it does not compete head-on with Axon on the same workflows.
- **Flock Safety** is the third pole, trying to be a stack by itself (FlockOS + ALPR + Aerodome drones). The integration story is real and the customer count is the largest of the three. The political ceiling on ALPR is also the lowest of the three, and several mid-sized US cities just put a number on it.

The dimension to watch over the next 30-90 days is whether Flock's NDAA-compliant US-made drone suite ships on schedule (the 12-month clock from the Aerodome announcement is well underway), and whether the cloud-reliability concern Skydio surfaced on May 6-7 leaks into any agency pause or pilot conversion. On Brinc, the metric is conversion rate of "Guardian launched March 24" announcements into named municipal procurements by Q3.

---

✅ All agents reported back!  
├─ 🟠 Reddit: 13 threads (Skydio 4 high-signal; Flock 2 + ALPR transparency PRs; Brinc keyword-trap noise demoted)  
├─ 🐙 GitHub: 1 high-signal item (Flock transparency / detector tooling) + 4 comments  
├─ 📰 HN: 12 items, 5 directly on Flock (4 of 5 critical), 1,062 combined points across the cluster  
├─ 🌐 Web supplement: dronexl.co, police1.com, 404media.co, robotics.press, sourcery.vc, a16z.news, flocksafety.com, brincdrones.com, theadvocate.com  
└─ 📎 Raw engine output: `/tmp/l30/skydio-raw.md`, `/tmp/l30/flock-safety-raw.md`, `/tmp/l30/brinc-raw.md` (not committed; reproducible via the skill)

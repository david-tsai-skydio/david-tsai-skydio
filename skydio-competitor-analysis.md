# Skydio vs Flock Safety vs Brinc: What the Last 30 Days Say

_Generated 2026-05-29 using the [`/last30days`](https://github.com/mvanhorn/last30days-skill) skill (v3.3.0). Engine ran in 3-way comparison mode (`--competitors-list "Flock Safety,Brinc Drones"`) against GitHub, Hacker News, Polymarket, and supplemented with WebSearch (Reddit returned 403 from this VM's IP, X/YouTube/TikTok require keys not configured here)._

## Quick Verdict

The American Drone-as-First-Responder (DFR) market is now a three-horse race - and all three have done something newsworthy in the last 30-60 days:

- **[Skydio](https://www.skydio.com/)** is the autonomy/defense incumbent. Closed a **$110M Series F at a $4.4B valuation** and announced **SkyForge - a $3.5B, 5-year U.S. manufacturing commitment** ([DRONELIFE, Apr 28](https://dronelife.com/2026/04/28/skydio-series-f-110m-funding-us-manufacturing/), [ASDNews, May 26](https://www.asdnews.com/news/defense/2026/05/26/skydio-commits-35-bn-expand-us-manufacturing-secure-american-drone-leadership)). Dallas PD went live on **8 X10 drones for 911** on May 20 ([dronexl, May 25](https://dronexl.co/2026/05/25/skydio-drones-dallas-911-calls/)).
- **[Flock Safety](https://www.flocksafety.com/)** is the surveillance-platform play. Pushing the **Flock Alpha DFR drone** (60 mph, ALPR-from-the-air) and tying it into its 12,000-customer ALPR + camera network ([a16z](https://www.a16z.news/p/flock-and-the-future-of-safety-in), [Flock](https://www.flocksafety.com/products/flock-dfr)). Also took the month's worst PR hit: Cleveland audit logs showed **163 immigration-related searches** hitting the city's Flock network despite a "no ICE" filter ([Gadget Review](https://www.gadgetreview.com/cleveland-flock-surveillance-network-used-for-immigration-searches-despite-safeguards)).
- **[Brinc](https://brincdrones.com/)** is the tactical/indoor specialist. Launched the **Guardian** - the world's first Starlink-connected DFR drone, ~8-mile range, automated battery-swap dock - from a new Seattle factory ([GeekWire, Mar 24](https://www.geekwire.com/2026/brinc-unveils-guardian-a-starlink-connected-drone-that-could-replace-the-police-helicopter/), [DroneXL](https://dronexl.co/2026/03/24/brinc-guardian-drone-starlink-911-response/)). $157M total funding; exclusive North American reseller is **Motorola Solutions**.

The macro tailwind for all three: **the FCC's December 2025 decision adding DJI to the Covered List** effectively bans the dominant Chinese drones from U.S. public-safety procurement, projected to remove **$1.5B in 2026 sales** from DJI's pipeline ([robotics.press](https://robotics.press/news/skydio-deep-dive/), [Industrial Sage](https://www.industrialsage.com/skydio-us-drone-manufacturing-skyforge/)). Skydio, Flock, and Brinc are the three NDAA-compliant U.S. companies positioned to absorb that vacuum.

---

## Skydio - the autonomy + defense incumbent

**The headline of the last 30 days is capital discipline + manufacturing scale.** CEO Adam Bry framed the [$110M Series F](https://dronelife.com/2026/04/28/skydio-series-f-110m-funding-us-manufacturing/) explicitly as "the most significant fact is how little we are raising," with investors wanting to put in substantially more. The valuation **doubled to $4.4B** anyway. The same week, Skydio committed **$3.5B over five years** to a new U.S. factory **5x larger** than its current footprint, $1B+ to domestic component suppliers, and a co-location program called **SkyForge** that invites suppliers to physically build alongside Skydio ([ASDNews](https://www.asdnews.com/news/defense/2026/05/26/skydio-commits-35-bn-expand-us-manufacturing-secure-american-drone-leadership)).

**Defense procurement is now a fixture, not an aspiration.** A **$52M+ U.S. Army order for X10D drones** (the largest single-vendor tactical sUAS order in Army history), selection for the **Missile Defense Agency's $151B SHIELD vehicle**, and follow-on USAF X10D EOD awards are all on the public record per [robotics.press](https://robotics.press/news/skydio-deep-dive/). Ahead of the FIFA World Cup, Spokane PD added Skydio drones for security; Skydio also crossed **1,000+ public safety agencies deployed**.

**The Axon channel is the de facto distribution moat.** A **$120.6M Dallas contract amendment via Axon** bundles eight Skydio X10s, integration with the Real-Time Crime Center, and a $10.3M counter-drone addition. Orlando PD signed a **$6.83M, 11-drone, 9-dock** Skydio program through Axon. Dallas's launch went live May 20 with the [first operational use the next day](https://dronexl.co/2026/05/25/skydio-drones-dallas-911-calls/) - a freeway extraction on I-45. Two-minute arrival from a fire-station roof rooftop is now the operational benchmark.

**Hardware:** X10 (~40 min flight, ~45 mph, 360° obstacle avoidance, integrated FLIR Boson+, -4°F to 113°F), R10 for indoor manual flight that hands off to a remote pilot, and the upcoming **F10** that "extends DFR coverage to dozens of miles" ([Skydio DFR](https://www.skydio.com/solutions/dfr)). The only meaningful GitHub signal in the last 30 days was a single PR on [Skydio/revup](https://github.com/Skydio/revup/pull/241) - Skydio's open-source git stacking tool - the company doesn't ship its drone autonomy stack publicly.

---

## Flock Safety - the surveillance platform

**Strategy is the inverse of Skydio's.** Flock isn't selling the best autonomous flyer; it's selling **integration into the 12,000-customer ALPR + camera + gunshot-detection mesh** that Flock has spent five years building ([a16z](https://www.a16z.news/p/flock-and-the-future-of-safety-in)). The drone (Flock Alpha, 60 mph, license-plate reading from up to 2,000 ft) is the **fourth payload** on top of license plate readers, situational-awareness cameras, and gunshot detectors. FlockOS is the unifying real-time intelligence layer.

**The product pitch is automation, not autonomy.** Flock's DFR launches drones automatically when **a 911 call is received, an LPR hit fires, or a gunshot detector triggers** - what Flock markets as "**Flock911 for Aerodome**," which it claims is the first U.S. system to launch a drone before a 911 call is even logged into dispatch ([Police and Security News](https://policeandsecuritynews.com/2025/06/13/emergency-response-reinvented-the-growing-role-of-drones-as-first-responders/)). 85-90 second arrival, four independent cellular modems for redundancy. SF deployed 400 LPRs + 80 drones in 2024 and major crimes fell 44%, car thefts 54%, per a16z's case study.

**The PR overhang is real and getting worse.** The biggest story of the month was [Cleveland's audit logs revealing 163 immigration-related searches](https://www.gadgetreview.com/cleveland-flock-surveillance-network-used-for-immigration-searches-despite-safeguards) hitting city cameras between Dec 28 and Jan 27, despite an activated "immigration filter." Texas and Florida agencies (some with ICE ties) had remote access. Cleveland blamed **Flock vendor error**; Flock has not publicly confirmed the explanation. Cleveland's contract expires June 28 and Mayor Bibb sent renewal to City Council rather than approving administratively.

The [EFF's December 2025 DFR retrospective](https://www.eff.org/deeplinks/2025/12/drone-first-responder-programs-2025-review) flagged Flock specifically for adding ALPR to the drone itself - so the drone is now a **flying license-plate reader**, with Flock's VP of Aviation Rahul Sidhu confirming this on calls to law-enforcement prospects ([EFF](https://www.eff.org/deeplinks/2025/09/drone-sky-could-be-tracking-your-car)). Some agencies (e.g., Redondo Beach PD) plan to activate the ALPR-on-drone feature soon.

**GitHub signal is the most active of the three** - and almost all of it is **adversarial / activist tooling**, which is itself a competitive signal:

- [the-machine-herald/machineherald.io#1513](https://github.com/the-machine-herald/machineherald.io/pull/1513) - submission summarizing the EFF's analysis of millions of Flock ALPR searches and mission-creep findings.
- [none-below/sm-alpr#477](https://github.com/none-below/sm-alpr/pull/477) - automated rolling refresh of Flock's transparency portal data.
- [denzuko/dwightspencer.com#86](https://github.com/denzuko/dwightspencer.com/pull/86) - a 2600-style technical writeup of "what Flock Safety actually is" (Falcon camera, NVLS database, Fusus integration, retention defaults).
- [yattsu/biscuit#1](https://github.com/yattsu/biscuit/pull/1) - **Flock-You**, a passive Flock camera detector ported from [colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you) using a 31-OUI detection list.

When civic hackers are shipping passive detectors for your hardware, that's the brand-risk axis Skydio doesn't have.

---

## Brinc - the tactical & indoor specialist

**The big launch was [Guardian on March 24](https://dronexl.co/2026/03/24/brinc-guardian-drone-starlink-911-response/)** - "the world's first Starlink-connected drone built for 911 response." Reach is **~8 miles** (more than 2x current non-DJI DFR ceilings of ~3 miles) thanks to a Starlink panel on top, plus a **Guardian Station** dock that **automatically swaps batteries and reloads payloads** between missions - eliminating the 25-min charge gap every other DFR platform has. CEO Blake Resnick told [GeekWire](https://www.geekwire.com/2026/brinc-unveils-guardian-a-starlink-connected-drone-that-could-replace-the-police-helicopter/) the pitch is "replace the **$4M police helicopter**" with a $100K rooftop drone + dock.

**The wedge is indoor and tactical, not patrol.** The flagship Lemur 2 is built **for getting inside a structure**: 20+ min flight, LiDAR autonomy that maps a room in 3D with no GPS and no light, **self-rights if it flips**, can break tempered/residential glass to gain entry, smoke-piercing FLIR, two-way speaker/mic for de-escalation, drops a 1-lb payload like a Narcan kit ([dronexl Louisiana case study](https://dronexl.co/2026/05/28/skydio-brinc-robot-dog-louisiana/)). 20%+ of U.S. SWAT teams now run BRINC. ~900 public safety agencies on the platform.

**Distribution is a Motorola lock.** The April 2025 [$75M raise](https://brincdrones.com/news/brinc-secures-75-million-forms-strategic-alliance-with-motorola-solutions-to-scale-production-and-use-of-911-response-drones/) (Index Ventures led, Motorola Solutions joined as strategic, plus Mike Volpi and Dylan Field) made **Motorola Solutions the exclusive North American reseller**. That's the same dynamic as Skydio + Axon - a public-safety-stack partner doing the channel motion - but Motorola has the *radio* footprint, not the body-cam one. **Total funding is now ~$157M** ([Forge](https://forgeglobal.com/brinc_stock/), [Tracxn](https://tracxn.com/d/companies/brincdrones/__FBTekRz_-AiCXshQW01oL3EtzDKaQUldxlxjkdZchMU)). Tripled revenue, 5x monthly production capacity in 2025, new factory in Seattle's Queen Anne neighborhood.

**Last 30 days news flow:** Iberville Parish (Louisiana) added 3 BRINC drones via a DA-funded program; Newport Beach committed $2.17M for a BRINC DFR network earlier in 2025. The HN/web signal Brinc picked up in raw research is mostly Ukraine-war drone-warfare context (slaughterbots, hypersonic strikes) rather than direct Brinc coverage - that's noise from the engine's keyword fallback, not real signal about the company.

---

## Head-to-Head

| Dimension | Skydio | Flock Safety | Brinc |
|---|---|---|---|
| **Founded / HQ** | 2014 / Hayward, CA | 2017 / Atlanta, GA | 2017 / Seattle, WA |
| **Latest valuation / funding** | $4.4B post-money, $110M Series F (Apr 2026) | Private; 12,000+ customers | ~$157M total; $75M Series C (Apr 2025) |
| **Distribution channel** | **Axon** (body-cam, RTCC, evidence) | Direct + own ALPR/camera mesh (FlockOS) | **Motorola Solutions** (exclusive NA reseller) |
| **Flagship hardware** | X10 / X10D / R10 (indoor); F10 coming | Flock Alpha DFR drone (+ ALPR cameras) | Guardian (Starlink, ~8mi); Lemur 2 (indoor) |
| **Best at** | Outdoor autonomy, defense, RTCC integration | **Pre-call** automated launches via 911/ALPR/gunshot triggers | Indoor entry, payload delivery, tactical/SWAT |
| **Range** | ~2 mi from base (X10) | 60 mph fast pursuit; 85-90s arrival | **~8 miles** with Starlink (Guardian) |
| **Standout feature** | $52M Army X10D order; SHIELD MDA vehicle | Drone-based ALPR (license-plate read at 2,000 ft) | **Auto battery swap** dock; 24/7 readiness |
| **Public-safety footprint** | 1,000+ agencies; Dallas, Orlando, Spokane, Nashville | 12,000 customers across LE + private | 900+ agencies; 20%+ of U.S. SWAT |
| **Manufacturing posture** | $3.5B SkyForge, 5x facility, $1B+ to domestic suppliers | 97,000 sq-ft drone factory near Atlanta | New Queen Anne, Seattle factory; 5x production capacity in 2025 |
| **Brand risk axis** | Defense / surveillance ethics, but lower-profile | **High** - civil-liberties orgs (EFF, Flock No coalition), Cleveland ICE-search story, civic hacker detection tooling | Modest - tactical-policing critique only |
| **DJI ban beneficiary?** | Yes - largest single beneficiary | Yes - DFR + ALPR | Yes - especially in tactical niche |

---

## The Bottom Line

- **Choose Skydio if** you're a federal agency, large municipal PD running an Axon stack, or a defense/critical-infrastructure customer. The autonomy is best-in-class and the procurement story (NDAA, U.S.-made, MDA SHIELD eligibility, $52M Army contract precedent) is the cleanest of the three.
- **Choose Flock if** you already have Flock LPR cameras and want **automated, intelligence-led dispatch** before a 911 call is even logged. Be prepared for civil-liberties scrutiny - Cleveland-style audit-log incidents are now a recurring news beat, and your contract may end up at City Council, not the city manager's desk.
- **Choose Brinc if** the mission profile is **indoor entry, hostage/barricade, payload delivery, or long-range rural** (Starlink Guardian's ~8-mile reach is a real moat over the 3-mile non-DJI DFR ceiling). Motorola Solutions' channel is the right fit if your radios are already Motorola.

## The Emerging Stack

The notable shift in the last 30-60 days is that **none of the three are competing as standalone drone vendors anymore.** Each one is now **a hardware layer inside a public-safety platform**:

- **Skydio + Axon** = drone + body-cam + evidence + RTCC.
- **Flock** = drone + ALPR + cameras + gunshot detection + dispatch automation, all under FlockOS.
- **Brinc + Motorola** = drone + radio + dispatch.

That's what Dallas, Orlando, Cleveland, and Iberville Parish all just bought. The **vendor-lock dynamic** that the [DroneXL Dallas piece](https://dronexl.co/2026/05/25/skydio-drones-dallas-911-calls/) called out - "a single procurement relationship now supplies body cameras, evidence management, the DFR aircraft channel, and the counter-drone World Cup posture" - is the ground truth for U.S. municipal drone procurement in 2026. The DJI ban created the demand vacuum; **the platform plays - not the drone specs - are how that vacuum gets filled.**

---

✅ All agents reported back!
- 🐙 GitHub: 6 items / 4 enriched comments (Flock-related civic-hacker tooling dominates)
- 🟠 Hacker News: 4 items (mostly Ukraine-war drone-warfare context, low signal for these vendors)
- 📊 Polymarket: 0 markets matched
- 🔴 Reddit: blocked (403 from this IP - normally a strong source)
- 🌐 Web: 16+ articles across DroneLife, DroneXL, GeekWire, Robotics.press, EFF, a16z, ASDNews, Industrial Sage, Police & Security News
- 📎 Raw engine output saved to `/tmp/l30d-out/{skydio,flock-safety,brinc-drones}-raw.md`

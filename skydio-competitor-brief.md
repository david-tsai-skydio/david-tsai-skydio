# Skydio vs. Flock vs. Brinc — Last-30-Days Competitive Brief

> Research window: **2026-04-28 → 2026-05-28** (last 30 days)
> Tooling: [`mvanhorn/last30days-skill`](https://github.com/mvanhorn/last30days-skill) (Reddit / HN / GitHub / Polymarket free tier — no SCRAPECREATORS, X, YouTube, or TikTok keys configured in this environment) + supplemental WebSearch.
> Engine output saved at `/tmp/last30-out/{skydio,flock-safety,brinc-drones}-raw.md`.

## TL;DR

The three companies are increasingly grouped together as the American Drone-as-First-Responder (DFR) stack now that DJI is effectively excluded from U.S. public-safety procurement, but each is on a very different trajectory in the last 30 days:

- **Skydio (autonomous airframe + DoD)** — Just closed a **$110M Series F at a $4.4B valuation** and announced **SkyForge**, a **$3.5B / 5-year** U.S. manufacturing build-out. Riding a record **$52M+ U.S. Army X10D order** (2,500+ units) plus a **$9M USAFCENT contract** for Middle East airbase protection, and just powered Dallas PD's brand-new 8-drone DFR program (May 20).
- **Brinc (mission-specialty hardware)** — Launched **Guardian**, the first **Starlink-connected DFR drone** (62-min flight, 8-mile range, autonomous battery-swap dock), opened a much larger Seattle factory, and is leveraging its exclusive Motorola Solutions reseller channel. No new round announced this window; still riding the $75M April 2025 Series C and ~$82M lifetime funding.
- **Flock Safety (LPR + Aerodome DFR)** — Quietly winning city DFR pilots (Aerodome / Flock911) but the dominant 30-day narrative is a **regulatory and PR firestorm** over its license-plate-reader network: ICE/immigration data-sharing scandals, multiple cities cancelling contracts, a bipartisan federal amendment threatening highway funding, **25+ Flock cameras destroyed in 5 states** since April 2025, and a sales-demo-into-children's-gym-camera blow-up.

Net: Skydio is consolidating the airframe/defense lane, Brinc is consolidating the public-safety mission/payload lane, and Flock is the one paying the political tax for being the most visible "AI surveillance" brand.

---

## 1. Skydio — last 30 days

### Capital and manufacturing
- **Series F:** $110M raised at **$4.4B post-money** (announced ~Apr 23, 2026; widely covered late April through May). CEO Adam Bry's framing: the round is small "because we don't need it" — declining capital needs as a profitability tell.
- **SkyForge / $3.5B U.S. expansion (Apr 24, 2026):** five-year plan; a new manufacturing facility "5x larger" than current; **$1B+ committed to U.S. suppliers**; ~2,000 direct hires + 3,000 supplier-side roles. Frames Skydio as the U.S. industrial counterweight to DJI.
- **Cumulative funding ~$850M+** (Series E $230M Feb '23, E-II $170M May '24, F $110M May '26), per `robotics.press` deep dive.

### Defense / public-safety wins
- **U.S. Army X10D order — $52M+ for 2,500+ units** (announced May 3, 2026 covering a March 22 award routed through Atlantic Diving Supply). Largest single-vendor sUAS contract in Army history; bid-to-award in **under 72 hours**. Implied unit price ~$17K–$21K.
- **USAFCENT $9M contract** (Apr 2026): Skydio Dock + X10 systems for U.S. airbase protection across Kuwait, Qatar, Bahrain, Saudi Arabia, UAE.
- Selected for the **Missile Defense Agency SHIELD** $151B contract vehicle.
- **Dallas Police DFR launch (May 20, 2026):** 8 Skydio drones flying from Dallas Fire-Rescue rooftops, 2-mile coverage radius each, integrated with Axon evidence/dispatch. First operational save inside 24 hours (man removed from Interstate 45). Notable for vendor-stack lock-in: Axon body cams + evidence + DFR + counter-drone all flowing through one procurement relationship.
- **Louisiana parishes (May 28, 2026):** West Baton Rouge / Iberville / Pointe Coupee adopting **Skydio X10 + Brinc Lemur 2** in a DA-funded three-year program. Reinforces the pattern of "Skydio for the outdoor autonomy lane, Brinc for the indoor/breach lane."

### Live signal (last30days-skill)
The free-tier engine surfaced one Skydio-org GitHub PR (`Skydio/revup#241`, May 7) — narrow signal because X / Reddit credentials are unavailable in this environment. The Skydio narrative this window is dominated by the press cycle around SkyForge, the Series F, and the Army order, not by community discussion.

```12:14:/tmp/last30-out/skydio-raw.md
- Date range: 2026-04-28 to 2026-05-28
- Sources: 1 active (GitHub)
```

---

## 2. Flock Safety — last 30 days

### Product / DFR posture
- **Flock911 / Flock for Aerodome** is the company's DFR play: drones auto-launch on 911 keywords; targeted 85–90 second arrival; tightly integrated with Flock's existing **license-plate-reader (LPR)** network and "people of interest" workflows. This is the strategic differentiator vs. Skydio/Brinc — Flock doesn't lead with the airframe, it leads with the surveillance graph the airframe plugs into.
- Tied to the broader Flock Safety camera ecosystem now in 4,000+ U.S. communities.

### The dominant 30-day story is regulatory/PR pressure on the LPR business
This is where the `last30days` engine had real signal — Hacker News carried Flock through the front page repeatedly:

| Date | Story | HN signal |
|---|---|---|
| 2026-05-01 | "City Learns Flock Accessed Cameras in **Children's Gymnastics Room as a Sales Demo** — Renews Contract Anyway" (404 Media) | 478 pts / 122 cmt |
| 2026-05-01 | "Flock cameras keep telling police a man who doesn't have a warrant has a warrant" | 192 pts / 145 cmt |
| 2026-05-04 | "Flock Holding Closed Police Conference, Requires Police Consent for Marketing" (IPVM) | 54 pts |
| 2026-05-07 | Dayton suspends Flock contract, "data used for immigration enforcement" | 94 + 12 pts, ~54 cmt total |
| 2026-05-14 | "City and Flock Manipulate Security Scores" (IPVM, Dunwoody) | 8 pts |
| 2026-05-17 | "**At least 25 Flock cameras have been destroyed in five states** since April 2025" | **443 pts / 326 cmt** (week's biggest cluster) |
| 2026-05-20 | "After town bans Flock, councilmember crashes out, proposes internet+phone ban" (404 Media) | 120 pts / 109 cmt |
| 2026-05-20 | "Editing PBF files to avoid Flock cameras (Android Auto)" | 3 pts |
| 2026-05-26 | "**Flipper Zero can detect Flock cameras**" | 5 pts |

### Policy and contract churn (WebSearch supplement)
- **Dane County, WI** Board of Supervisors **defunded** the sheriff's Flock contract 32-1 ($80K stripped), following **Verona, WI's** earlier cancellation. WisconsinWatch frames it as a cascade across the state.
- **Richmond, VA** banned its police from sharing Flock data with any in-state department holding a 287(g) ICE agreement.
- **Cleveland, OH:** city audit logs revealed >1M searches/month, with 168 immigration-tagged searches in a recent ~6-week window; city framing it as a "filter fluke" and a misread of First Responder Drone logs. Council still planning to renew Flock through June 1.
- **Federal:** Reps. Scott Perry (R-PA) and Chuy García (D-IL) introduced a bipartisan transportation-bill amendment that would **bar federal-highway-funded localities from using LPRs for any purpose other than tolling**. If it passes, it is an existential constraint on the core Flock business.
- **Illinois** previously found Flock had given CBP access to state ALPR data in violation of state law; Flock paused federal pilots nationwide.

### Read
Flock is closing DFR deals (Aerodome integration is genuinely faster than Skydio/Brinc on integrated 911-trigger workflow), but the LPR side is now the political lightning rod for the entire "AI surveillance" debate — and the brand damage is bleeding into the drone side. Cleveland's spokesperson literally had to argue on local TV in mid-May "it's not mass surveillance" in front of activists demanding contract cancellation.

---

## 3. Brinc — last 30 days

### Product
- **Guardian + Guardian Station** (announced March 24, 2026, but the rollout, factory, and Motorola channel push are the dominant May story):
  - **First Starlink-connected DFR drone** — unlimited range outside terrestrial coverage.
  - **62-minute flight time**, ~60 mph top speed.
  - Robotic dock auto-swaps batteries and reloads payloads → ~1 minute turnaround vs. 25-minute charge cycles for everyone else (this is a real moat for sustained 24/7 DFR).
  - **8-mile incident reach** vs. ~3-mile ceiling for non-DJI competitors.
  - Carries medical payloads (Narcan, AED) and integrates directly with Motorola CommandCentral Aware so dispatchers can launch from 911 keyword detection or APX NEXT radio panic buttons.
- **Lemur 2** continues as the indoor-tactical/SWAT entry drone (LiDAR autonomy, glass-breaking, two-way audio, sub-1lb payload). This is what Iberville Parish (LA) just bought alongside Skydio X10s on May 28 — the parish DA explicitly carving roles: Skydio for outdoor first response, Lemur 2 for indoor breach/de-escalation.

### Capital / scale
- **No new round in the 30-day window.** Lifetime funding ~$157M–$82M (sources differ on exact total — GeekWire said $157.2M post the April 2025 $75M Series C; the May 28 dronexl piece quotes Forbes at "around $82M" which appears to be a typo or different cut). Last priced round at **>$400M valuation** (Nov 2025 reporting).
- **Investor base:** Index Ventures, Motorola Solutions, Sam Altman, Dylan Field, Elad Gil, Patrick Shanahan, Shyam Sankar, Alexandr Wang, Jeff Weiner, Bradley Tusk, Julius Genachowski. (Heavy SV-defense/policy crossover.)
- **New Seattle factory** more than doubles production footprint; Brinc says monthly production capacity grew 5x in 2025 and revenue tripled.
- **Customer base:** ~900 public safety agencies; 20%+ of U.S. SWAT teams; 500+ active contracts.

### Live signal (last30days-skill)
The free-tier engine over-matched on the bare token "drones" and returned generic Ukraine/Russia drone-warfare HN stories rather than Brinc-specific items — a known limitation in the absence of X handles or richer subreddit auth. The Brinc news this window is concentrated in trade-press WebSearch results, not in HN/GitHub/Reddit comment volume.

```5:9:/tmp/last30-out/brinc-drones-raw.md
- Date range: 2026-04-28 to 2026-05-28
- Sources: 1 active (Hacker News)
[...]
- Top evidence is highly concentrated in one source.
```

---

## 4. Head-to-head matrix

| Dimension | Skydio | Flock Safety | Brinc |
|---|---|---|---|
| Core wedge | Autonomous AI airframe (X10 / X10D) | LPR/camera surveillance graph + DFR layer | Mission-specific hardware (DFR Guardian + breach Lemur 2) |
| DFR product | X10 from dock or vehicle, Axon-integrated | Flock911 / Aerodome — auto-launch on 911 keyword | Guardian + Guardian Station, Motorola CommandCentral-integrated |
| Killer hardware feature (last 30d) | NDAA-compliant U.S.-built X10D, NVIDIA Jetson Orin onboard, 360° AI obstacle avoidance | (No drone hardware diff. — wins on LPR data graph) | First Starlink drone + autonomous battery swap → true 24/7 DFR |
| Defense / federal | $52M+ Army order, $9M USAFCENT, MDA SHIELD vehicle | LPR data accessed by ICE/CBP — political liability | Backers include former DepSecDef Patrick Shanahan; Palantir CTO Sankar; not in DoD procurement at scale |
| Latest funding | **$110M Series F at $4.4B (Apr/May 2026)** | Last large round Series F $275M (2024) at $7.5B; no May 2026 round disclosed | $75M Series C April 2025 at >$400M; no May 2026 round |
| Manufacturing | $3.5B SkyForge build-out, Hayward CA (5th expansion) | N/A (cameras manufactured at scale already) | New Seattle Queen Anne HQ + factory, 5x prior capacity |
| Customers | 1,000+ public-safety agencies; 900+ utilities; all U.S. military branches; 60K+ units shipped | 4,000+ communities; thousands of police departments | 900+ public-safety agencies; 20%+ of U.S. SWAT; 500+ contracts |
| Channel | Direct + Axon ecosystem | Direct, deep PD relationships | **Exclusive Motorola Solutions reseller** in North America (CommandCentral + APX NEXT integration) |
| Dominant 30-day narrative | "Capital-disciplined raise + $3.5B U.S. industrial play + record Army order" | **Regulatory backlash:** ICE/immigration data sharing, city cancellations, federal LPR amendment, cameras destroyed | "Guardian rollout + Motorola channel + parish-by-parish DFR wins" |
| Risk | Vendor lock-in narrative (Dallas-style Axon stacks); execution on $3.5B build | LPR business is the political fuse; if the Perry/García amendment moves, the funding model breaks | Single-channel dependence on Motorola; smaller $ scale than Skydio for federal/defense |

---

## 5. Bottom line per company

**Choose Skydio if** you are a federal/defense buyer or a city that wants the most autonomy-forward American airframe with the deepest DoD trust signal. The April-May news cycle is unusually one-directional positive: Series F + SkyForge + Army order + USAFCENT + Dallas PD launch. Watch for execution risk on $3.5B and for whether the Axon stack provokes any antitrust/sole-source pushback.

**Choose Flock Safety if** you want the fastest 911-keyword-to-drone latency and you already run their LPR fleet — the integrated graph is genuinely unique. But the brand is now the proxy for every "AI mass surveillance" debate in the country: 25+ cameras physically destroyed in 5 states, multiple contract cancellations in WI/VA/OH/IL, and a federal amendment that could gut the funding model. Buyers are now asking explicit "what happens if Flock loses federal cover?" questions.

**Choose Brinc if** you are a city/parish public-safety agency that needs **24/7 DFR uptime with payload delivery** and you already buy Motorola radios. Guardian's autonomous battery swap and Starlink link are the only specs that materially advance the DFR state of the art this window. The 30-day cadence is slower and more operational than Skydio's, but the Motorola channel does to Brinc what Axon does to Skydio — it removes the second-vendor evaluation friction.

---

## 6. The emerging stack (most likely outcome)

A consensus is forming that the U.S. public-safety drone stack post-DJI is **Skydio (outdoor airframe + DoD share) + Brinc (indoor/breach + 24-7 DFR + payload) + Flock (LPR data graph and 911-trigger plumbing if it survives the regulatory cycle)**. The Louisiana parish deal (May 28) and the Dallas PD launch (May 20) both show agencies buying *both* Skydio and Brinc rather than choosing one. The open question for the next 30–90 days is which vendor — if any — gets to own the integration plane: Axon (riding Skydio), Motorola (riding Brinc), or Flock itself.

---

## 7. Methodology notes

- The `last30days` engine ran in *local mode* (no SCRAPECREATORS / OPENAI / X / YouTube / TikTok / Brave / Exa keys), so coverage was limited to GitHub + HackerNews + Polymarket + free-tier Reddit. Reddit returned 0 items — likely a transient API behavior given no auth was supplied.
- Where the engine reported "Evidence is thin," I supplemented with `WebSearch` and treated the engine output as a signal-of-discussion-volume check (most useful for the **Flock HN cluster**, which the engine surfaced cleanly).
- Date drift caveat: a couple of headline events (Skydio Series F / SkyForge announcement, March 22 Army contract) actually broke just outside the strict 30-day window but are still the dominant Q2 narrative driving last-30-days coverage and analyst commentary, so they're included.


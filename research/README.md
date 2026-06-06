# Skydio competitor research (last 30 days)

Generated 2026-06-06 using the [last30days-skill](https://github.com/mvanhorn/last30days-skill)
research engine (v3.3.1), running locally against the free-tier sources
(Reddit, Hacker News, GitHub, Polymarket) with WebSearch as a supplement
for Brinc, where the engine reported "evidence is thin."

## Files

- **`skydio-vs-flock-vs-brinc-brief.md`** - synthesized comparison brief
  covering market positioning, last-30-day signal, head-to-head table, and
  bottom-line recommendations.
- `skydio-last30days-raw.md` - raw `--emit=md` output for the Skydio leg
  of the `Skydio vs Flock vs Brinc` engine run (24 items, Reddit + GitHub).
- `flock-last30days-raw.md` - raw output for the Flock leg of the same
  run (Reddit + Hacker News + GitHub; dominant HN cycle on Flock backlash).
- `brinc-last30days-raw.md` - raw output for the Brinc leg (mostly
  off-topic noise, engine flagged thin-evidence warning).
- `brinc-lemur-targeted-raw.md` - second, focused engine run for
  `BRINC Lemur drone` with an explicit `--plan` JSON pinning the right
  subreddits (`r/BRINC`, `r/police`, `r/publicsafety`, `r/drones`,
  `r/Multicopter`, `r/ProtectAndServe`) and ranking keywords. Confirmed
  the thin-evidence finding for Brinc on Reddit / HN.

## How to reproduce

The skill is open source under MIT license. Clone it and run with the same
free-tier sources used here:

```bash
git clone --depth 1 https://github.com/mvanhorn/last30days-skill.git
cd last30days-skill/skills/last30days

# Three-way comparison (writes one raw file per entity into /tmp/l30/):
python3 scripts/last30days.py "Skydio vs Flock vs Brinc" \
  --emit=md --save-dir /tmp/l30 --save-suffix skydio-vs

# Targeted Brinc re-run (fills in the thin-evidence gap):
cat > /tmp/brinc_plan.json <<'EOF'
{
  "topic": "BRINC Lemur drone public safety",
  "search_queries": ["BRINC Lemur", "BRINC drone", "Brinc public safety drone",
                     "Blake Resnick", "BRINC Drones", "DFR drone first responder"],
  "subreddits": ["BRINC", "police", "drones", "publicsafety", "Multicopter",
                 "ProtectAndServe"],
  "x_handles": ["BRINCDrones", "blakeresnick"],
  "ranking_keywords": ["BRINC", "Lemur", "Resnick", "police drone",
                       "public safety", "tactical", "first responder", "DFR"]
}
EOF
python3 scripts/last30days.py "BRINC Lemur drone" \
  --plan /tmp/brinc_plan.json --emit=md \
  --save-dir /tmp/l30 --save-suffix brinc-lemur --deep
```

For richer coverage (X / YouTube / TikTok / Instagram / Polymarket / Perplexity)
add the optional API keys / browser tokens listed in the skill's
[CONFIGURATION.md](https://github.com/mvanhorn/last30days-skill/blob/main/CONFIGURATION.md).

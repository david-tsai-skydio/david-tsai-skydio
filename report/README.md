# Skydio Careers — Formatting Consistency Audit

This folder contains the output of a formatting-consistency audit of every
open job posting at <https://www.skydio.com/careers>.

## Files

| File | Purpose |
| --- | --- |
| `REPORT.md` | **The main report**, written for the careers/recruiting team. Lists every formatting inconsistency we found, which postings are affected, and how to fix them. |
| `findings.json` | A machine-readable summary of the same findings (used to drive the markdown report, and convenient if someone wants to script follow-up checks). |
| `jobs_index.json` | The 118 open job postings extracted from the careers landing page (title, location, employment type, department, URL, internal job ID). |
| `jobs_formatting.json` | Per-posting formatting fingerprint — block-tag sequence, section labels and the markup used for each, counts of bold/italic/heading/list/`<br>`/empty-paragraph/inline-style/etc. elements found in the pre-compensation body. |

## How the report was generated

The end-to-end pipeline lives in `../scripts/`:

1. `extract_jobs.py` — parses the cached `/careers` HTML and writes `jobs_index.json`.
2. `download_jobs.py` — fetches `https://www.skydio.com/jobs/<id>/?gh_jid=<id>` for each posting and stores the raw HTML in `../job_pages/` (gitignored — ~57 MB).
3. `analyze_jobs.py` — for every downloaded posting, isolates the body inside `<div class="prose block-content">`, splits at the `Compensation:` paragraph, and records the formatting fingerprint into `jobs_formatting.json`.
4. `build_report.py` — turns the fingerprints into `REPORT.md` and `findings.json`.

To regenerate from scratch:

```bash
# 1) Make sure /tmp/careers.html is fresh:
curl -sL "https://www.skydio.com/careers" \
    -A "Mozilla/5.0" -o /tmp/careers.html

# 2) Run the pipeline:
cd /workspace
python3 scripts/extract_jobs.py
python3 scripts/download_jobs.py        # cached; re-uses existing files
python3 scripts/analyze_jobs.py
python3 scripts/build_report.py
```

## Scope reminder

Only the **pre-compensation** portion of each posting body was analyzed — everything inside the `prose` content container up to (but not including) the paragraph that starts with `Compensation:`. The compensation and equal-opportunity boilerplate that follow are intentionally excluded.

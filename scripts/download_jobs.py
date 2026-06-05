"""Download every individual job posting HTML page (cached)."""
import json
import time
from pathlib import Path

import requests

INDEX = Path("/workspace/report/jobs_index.json")
OUT_DIR = Path("/workspace/job_pages")
OUT_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


def main() -> None:
    jobs = json.loads(INDEX.read_text())
    session = requests.Session()
    session.headers.update(HEADERS)

    downloaded = 0
    skipped = 0
    failed = 0
    for j in jobs:
        path = OUT_DIR / f"{j['job_id']}.html"
        if path.exists() and path.stat().st_size > 5000:
            skipped += 1
            continue
        url = j["url"]
        try:
            r = session.get(url, timeout=30)
            r.raise_for_status()
            path.write_text(r.text, encoding="utf-8")
            downloaded += 1
            print(f"[{downloaded:3d}] {len(r.text):>8} bytes  {j['title']}")
        except Exception as e:
            failed += 1
            print(f"FAILED {url}: {e}")
        time.sleep(0.3)

    print(f"Done. downloaded={downloaded} skipped={skipped} failed={failed}")


if __name__ == "__main__":
    main()

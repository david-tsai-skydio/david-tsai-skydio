"""Extract job listings from the cached careers page and write a JSON index."""
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

CAREERS_HTML = Path("/tmp/careers.html")
OUT = Path("/workspace/report/jobs_index.json")
OUT.parent.mkdir(parents=True, exist_ok=True)


def main() -> None:
    soup = BeautifulSoup(CAREERS_HTML.read_text(encoding="utf-8"), "lxml")

    # Job postings are wrapped in <a href="/jobs/<id>/?gh_jid=<id>"> elements
    # In Skydio's markup, each posting appears inside a department section.
    jobs = []
    seen = set()

    # Each job posting in the careers page is a card containing
    #   <h5 class="job-listings__title">TITLE</h5>
    # and an <a href="/jobs/<id>/?gh_jid=<id>"> (the "View & Apply" link).
    # We iterate over the title elements and look forward to the next anchor.
    for title_el in soup.find_all("h5", class_="job-listings__title"):
        title = title_el.get_text(" ", strip=True)

        # Find the next sibling anchor pointing to /jobs/...
        a = title_el.find_next("a", href=re.compile(r"^/jobs/[a-f0-9-]+/\?gh_jid="))
        if a is None:
            continue
        href = a["href"]
        m = re.search(r"gh_jid=([a-f0-9-]+)", href)
        if not m:
            continue
        job_id = m.group(1)
        if job_id in seen:
            continue
        seen.add(job_id)

        # Meta text (location + employment type) sits in a sibling <p> after the title
        meta_el = title_el.find_next(
            string=re.compile(
                r"(Full-time|Intern|Part-time|Contract|Remote)"
            )
        )
        meta_text = (meta_el.strip() if meta_el else "")

        # Department: nearest preceding h4 heading
        dept = None
        node = title_el
        while node is not None and dept is None:
            node = node.find_previous("h4")
            if node is None:
                break
            t = node.get_text(" ", strip=True)
            if t and len(t) < 60:
                dept = t

        jobs.append({
            "job_id": job_id,
            "title": title,
            "meta": meta_text,
            "department": dept,
            "url": f"https://www.skydio.com{href}",
        })

    OUT.write_text(json.dumps(jobs, indent=2))
    print(f"Wrote {len(jobs)} jobs to {OUT}")
    # Print first few for sanity check
    for j in jobs[:5]:
        print(j)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Refresh content/ from vascue.io's public Markdown twins.

Reads the sitemap, downloads each page's .md twin (frontmatter carries the
canonical URL and title), plus the claims-automation brief. Public content
only; run before cutting a release so the bundled snapshot is current.
"""
from __future__ import annotations

import pathlib
import re
import sys
import urllib.request

SITE = "https://www.vascue.io"
CONTENT = pathlib.Path(__file__).resolve().parent.parent / "content"


def get(url: str) -> str | None:
    request = urllib.request.Request(url, headers={"User-Agent": "vascue-content-sync"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            if response.status != 200:
                return None
            return response.read().decode("utf-8")
    except OSError as error:
        print(f"  skip {url}: {error}", file=sys.stderr)
        return None


def main() -> int:
    sitemap = get(f"{SITE}/sitemap.xml")
    if not sitemap:
        print("could not fetch sitemap", file=sys.stderr)
        return 1
    paths = sorted(
        {re.sub(r"^https://www\.vascue\.io", "", loc) or "/" for loc in re.findall(r"<loc>([^<]+)</loc>", sitemap)}
    )
    CONTENT.mkdir(exist_ok=True)
    for stale in CONTENT.glob("*.md"):
        stale.unlink()
    saved = 0
    markdown_paths = ["/index.md" if p == "/" else f"{p}.md" for p in paths] + ["/claims-automation.md"]
    for md_path in markdown_paths:
        body = get(f"{SITE}{md_path}")
        if body is None:
            continue
        slug = md_path.strip("/").removesuffix(".md").replace("/", "--")
        (CONTENT / f"{slug}.md").write_text(body, encoding="utf-8")
        saved += 1
    print(f"saved {saved}/{len(markdown_paths)} pages into {CONTENT}")
    return 0 if saved else 1


if __name__ == "__main__":
    raise SystemExit(main())

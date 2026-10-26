#!/usr/bin/env python3
"""Report Markdown pages whose 'Last reviewed' / 'Last verified' date is past its review window.

Tool guides: 6 months. Everything else: 12 months.
Prints a GitHub Actions warning for each stale page. Exits 0, since stale pages
are flagged for maintainers rather than blocking contributions.
"""
from __future__ import annotations

import datetime as dt
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PATTERN = re.compile(r"Last (?:reviewed|verified):\**\s*(\d{4})-(\d{2})")


def months_between(year: int, month: int, today: dt.date) -> int:
    return (today.year - year) * 12 + (today.month - month)


def main() -> int:
    today = dt.date.today()
    stale = 0
    missing = []
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith((".github/", "node_modules/")) or path.name in {
            "LICENSE.md", "CODE_OF_CONDUCT.md", "CONTRIBUTING.md"
        }:
            continue
        text = path.read_text(encoding="utf-8")
        match = PATTERN.search(text)
        if not match:
            if rel.startswith("docs/"):
                missing.append(rel)
            continue
        limit = 6 if "/tool-guides/" in rel and not path.name.startswith("_") else 12
        age = months_between(int(match.group(1)), int(match.group(2)), today)
        if age > limit:
            stale += 1
            print(f"::warning file={rel}::Last reviewed {age} months ago (window {limit} months)")
    for rel in missing:
        print(f"::notice file={rel}::No 'Last reviewed' date found")
    print(f"{stale} stale page(s); {len(missing)} docs page(s) without a review date.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# Generate books/index.json by scanning books/*/book.json
# Usage: python3 tools/generate_index.py

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOKS = ROOT / "books"
OUT = BOOKS / "index.json"

KEEP = ["id", "series", "title_ua", "title_en", "level", "durationMin", "cover"]

items = []
for d in sorted(BOOKS.iterdir()):
    if not d.is_dir():
        continue
    bj = d / "book.json"
    if not bj.exists():
        continue
    try:
        data = json.loads(bj.read_text(encoding="utf-8"))
    except Exception:
        continue
    if not data.get("id"):
        data["id"] = d.name
    item = {k: data.get(k) for k in KEEP if data.get(k) not in (None, "", [])}
    items.append(item)

items.sort(key=lambda x: (str(x.get("series","")).lower(),
                         str(x.get("title_en","")).lower(),
                         str(x.get("id","")).lower()))

OUT.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"✅ Wrote {OUT} ({len(items)} books)")

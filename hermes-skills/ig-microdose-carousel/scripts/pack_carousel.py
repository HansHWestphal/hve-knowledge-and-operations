#!/usr/bin/env python3
"""Copy a finished work dir into the Syncthing outbox with caption files."""
from __future__ import annotations

import argparse
import json
import shutil
from datetime import date
from pathlib import Path


README = """Publish from Instagram iOS only.

Order:
1. 01-cover.mp4
2. 02.png
3. 03.png
4. 04.png
5. 05.png
6. 06.png
7. 07.png
8. 08.png

Do not tap Add music. The MP4 already carries the bed.
Paste caption.txt. After publish, first comment is FIRST_COMMENT.txt.
"""


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--work", required=True)
    p.add_argument("--outbox", required=True)
    args = p.parse_args()
    work = Path(args.work)
    slides = work / "slides"
    out = Path(args.outbox)
    out.mkdir(parents=True, exist_ok=True)
    script = json.loads((work / "script.json").read_text())

    shutil.copy2(slides / "01-cover.mp4", out / "01-cover.mp4")
    for n in range(2, 9):
        shutil.copy2(slides / f"{n:02d}.png", out / f"{n:02d}.png")

    hook = script["slides"][0]
    body = script["slides"][2]
    caption = (
        f"{hook}\n\n{body}\n\n"
        "Save this for the moment the grip comes back.\n"
        "What are you still making too important?\n"
    )
    (out / "caption.txt").write_text(caption)
    (out / "FIRST_COMMENT.txt").write_text(script["keyword"].strip() + "\n")
    (out / "README.txt").write_text(README)

    factory = out.parent.parent
    ledger = factory / "ledger.jsonl"
    row = {
        "date": date.today().isoformat(),
        "slug": out.name,
        "series": script.get("series"),
        "keyword": script.get("keyword"),
        "source": script.get("source_url"),
    }
    with ledger.open("a") as fh:
        fh.write(json.dumps(row) + "\n")
    print(out)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Crop a photo to 1080x1350 (4:5), face-high, lower third relatively empty."""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def crop_45(im: Image.Image) -> Image.Image:
    w, h = im.size
    target = 1080 / 1350
    src = w / h
    if src > target:
        new_w = int(h * target)
        left = (w - new_w) // 2
        im = im.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / target)
        top = max(0, int((h - new_h) * 0.18))
        im = im.crop((0, top, w, min(h, top + new_h)))
    return im.resize((1080, 1350), Image.Resampling.LANCZOS)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--in", dest="src", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()
    src = Path(args.src)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src) as im:
        crop_45(im.convert("RGB")).save(out, "PNG", optimize=True)
    print(out)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Render the 8-slide micro-dose pack as 1080x1350 PNGs."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
BG = (17, 17, 17)
CREAM = (243, 237, 224)
GOLD = (196, 165, 116)
MUTE = (138, 133, 128)


def font_path(name_guess: list[str]) -> str:
    roots = [
        Path(__file__).resolve().parent.parent / "assets" / "fonts",
        Path("/usr/share/fonts/truetype/dejavu"),
        Path("/usr/share/fonts/truetype/liberation"),
    ]
    for root in roots:
        if not root.exists():
            continue
        for g in name_guess:
            hit = list(root.rglob(g))
            if hit:
                return str(hit[0])
    return "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    if bold:
        path = font_path(["*Serif*Bold*.ttf", "DejaVuSans-Bold.ttf", "*.ttf"])
    else:
        path = font_path(["*Serif*.ttf", "DejaVuSans.ttf", "*.ttf"])
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


def wrap(draw: ImageDraw.ImageDraw, text: str, font, max_w: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    cur = ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines or [""]


def base() -> tuple[Image.Image, ImageDraw.ImageDraw]:
    im = Image.new("RGB", (W, H), BG)
    dr = ImageDraw.Draw(im)
    foot = load_font(22)
    dr.text((80, 1268), "KNOW THYSELF", font=foot, fill=MUTE)
    return im, dr


def draw_block(dr, text: str, y: int, size: int, fill, max_w: int = 920, bold: bool = False) -> int:
    font = load_font(size, bold=bold)
    lines = wrap(dr, text, font, max_w)
    for line in lines:
        dr.text((80, y), line, font=font, fill=fill)
        y += int(size * 1.28)
    return y


def photo_underlay(path: str | None) -> Image.Image:
    im, dr = base()
    if path and Path(path).exists():
        ph = Image.open(path).convert("RGB").resize((W, H), Image.Resampling.LANCZOS)
        im.paste(ph)
        dr = ImageDraw.Draw(im)
        dr.rectangle((0, 980, W, H), fill=(0, 0, 0))
        foot = load_font(22)
        dr.text((80, 1268), "KNOW THYSELF", font=foot, fill=MUTE)
    return im


def render(script: dict, out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    slides = script["slides"]
    cover = script.get("cover")
    proof = script.get("proof")
    close = script.get("close")

    im = photo_underlay(cover)
    dr = ImageDraw.Draw(im)
    draw_block(dr, slides[0], 1020, 48, CREAM, bold=True)
    swipe = load_font(28)
    dr.text((820, 1220), "Swipe →", font=swipe, fill=GOLD)
    im.save(out / "01-cover.png")

    jobs = [
        (2, slides[1], GOLD),
        (3, slides[2], CREAM),
        (4, slides[3], CREAM),
        (5, slides[4], CREAM),
        (6, slides[5], CREAM),
    ]
    for n, text, color in jobs:
        im, dr = base()
        label = load_font(22)
        labels = {2: "SOURCE", 3: "TRANSLATION", 4: "TRAP", 5: "MECHANISM", 6: "TODAY"}
        dr.text((80, 140), labels[n], font=label, fill=GOLD)
        draw_block(dr, text, 240, 52, color)
        im.save(out / f"{n:02d}.png")

    im = photo_underlay(proof) if proof else base()[0]
    dr = ImageDraw.Draw(im)
    if not proof:
        draw_block(dr, slides[6], 240, 48, CREAM)
    else:
        draw_block(dr, slides[6], 1100, 32, CREAM)
    im.save(out / "07.png")

    im = photo_underlay(close) if close else base()[0]
    dr = ImageDraw.Draw(im)
    y = 1040 if close else 240
    draw_block(dr, slides[7], y, 44, CREAM, bold=True)
    im.save(out / "08.png")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--script", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()
    script = json.loads(Path(args.script).read_text())
    render(script, Path(args.out))
    print(args.out)


if __name__ == "__main__":
    main()

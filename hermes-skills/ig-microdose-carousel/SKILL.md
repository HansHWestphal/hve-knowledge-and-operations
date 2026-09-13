---
name: ig-microdose-carousel
description: Build Instagram carousels on the NVIDIA Spark from Hans X micro-doses using only local open-source tools. Trigger on Spark carousel, Hermes carousel skill, micro-dose to slides, bake local audio cover, FOSS Instagram factory, or replace Canva CapCut.
license: MIT
metadata:
  type: workflow
  version: "1.0"
  runtime: spark-hermes
---

# IG micro-dose carousel (Spark / Hermes)

Run this factory on the DGX Spark through Hermes. Do not use Canva, CapCut, Photoshop, or Instagram Add music. Render slides with Python/Pillow. Bake the local audio bed with ffmpeg. Park a phone-ready pack in `outbox/` for Syncthing.

## When to use

User wants a carousel from an authored X micro-dose or a cluster of cousin notes. Last-year @HansHWestphal posts plus daily micro-doses only. No LinkedIn, no Substack, no new doctrine.

## Stack (FOSS only)

| Job | Tool |
|---|---|
| Script the 8 lines | Local LLM already on Spark (Ollama / Hermes trio) |
| Still slides | Python 3, Pillow, DejaVu or OFL fonts in `assets/fonts/` |
| Cover video + bed | ffmpeg + ffprobe |
| Photo prep | ImageMagick `magick` or ffmpeg scale/crop |
| Catalog | JSONL at `$FACTORY/ledger.jsonl` |
| Sync to phone | Syncthing folder `$FACTORY/outbox/` |
| Publish | Human taps Share in Instagram iOS (no FOSS IG publisher) |

System packages on Spark. `sudo apt install python3-pil ffmpeg imagemagick fonts-dejavu-core syncthing` if missing. Do not introduce closed SaaS.

Default factory root (override with `$HVE_IG_FACTORY`):

```
/data/hve/ig-factory/
  inbox/microdoses/
  photos/cover|proof|close|texture|kill/
  audio/transurfing-bed.mp3
  audio/russell-bed.mp3
  work/<slug>/
  outbox/<slug>/
  ledger.jsonl
```

If `/data/hve` does not exist, use `$HOME/hve/ig-factory`.

## 8-slide contract

1 Cover photo + hook (max 10 words) + Swipe
2 Source quote
3 Translation
4 Trap
5 Mechanism
6 Today’s move
7 Proof photo, almost no type
8 Close portrait + Save this. Comment KEYWORD.

Slides 2–6 are type on `#111111`. Never put a portrait under the paragraph. Shirt text and teaching line do not stack.

Canvas always 1080x1350. First asset in the Instagram picker must be `01-cover.mp4` so the post carries original audio.

## Hermes procedure

### 1. Ingest

Read the micro-dose text. If a cluster, fuse 2–3 cousin notes into one teaching arc. Refuse off-corpus sources.

Write `work/<slug>/script.json` with keys title, source_url, date, series (transurfing|russell), slides (8 strings), keyword, cover, proof, close, bed.

Series picker. Transurfing if the note is Zeland, pendulums, intention, mirror, inversion, will to have. Russell if interchange, wave, genius, prayer-with, meditation, light-wave.

### 2. Pick photos

From `photos/cover`, `photos/proof`, `photos/close`. Reuse rotation. Do not invent stock. Crop to 4:5 with `scripts/prep_photo.py` (face high, lower third empty on covers).

### 3. Render stills

```
python3 scripts/render_slides.py --script work/<slug>/script.json --out work/<slug>/slides
```

Produces `01-cover.png` plus `02.png` through `08.png`.

### 4. Bake cover

```
python3 scripts/bake_cover.py --image work/<slug>/slides/01-cover.png --audio $FACTORY/audio/<series>-bed.mp3 --out work/<slug>/slides/01-cover.mp4
```

6 to 8 seconds, 1080x1350, yuv420p + aac, zoom 1.00 to 1.08. Probe after write.

### 5. Pack

```
python3 scripts/pack_carousel.py --work work/<slug> --outbox $FACTORY/outbox/<slug>
```

Copies `01-cover.mp4`, `02.png`–`08.png`, `caption.txt`, `FIRST_COMMENT.txt`, `README.txt`. Append a ledger row. Syncthing ships `outbox/<slug>` to the phone.

### 6. Human last mile

On the phone, Instagram + → Post → multi-select in README order. Do not tap Add music. Paste caption.txt. After publish, first comment is FIRST_COMMENT.txt.

## Script voice

Keep the authored line. Expand only into the 8 jobs. Hook is a fragment of the note, not a new slogan. Keyword is one token such as LETTERBOX, PROCESS, MIRROR, ALLOW, INTERCHANGE.

## Quality gate

- Every still is 1080x1350
- `01-cover.mp4` has an audio stream
- Slides 2–6 have no full-body portrait
- Caption starts with the hook
- Ledger has the slug before you tell the user it is done

## References

- `references/oss-bom.md` — packages and why each exists
- `references/layout.md` — type sizes, colors, safe zones
- `scripts/` — render, bake, pack, prep

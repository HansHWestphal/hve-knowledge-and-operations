#!/usr/bin/env python3
"""6-8s 4:5 cover with slow zoom and original audio bed. FOSS ffmpeg only."""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def run(cmd: list[str]) -> None:
    subprocess.check_call(cmd)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--image", required=True)
    p.add_argument("--audio", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--seconds", type=float, default=7.0)
    args = p.parse_args()
    image = Path(args.image)
    audio = Path(args.audio)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_suffix(".tmp.mp4")

    filt = (
        f"scale=1166:1458,zoompan=z='min(1.08,1+0.08*on/{args.seconds*30})'"
        f":d={int(args.seconds*30)}:s=1080x1350:fps=30"
    )
    run(
        [
            "ffmpeg",
            "-y",
            "-loop",
            "1",
            "-i",
            str(image),
            "-i",
            str(audio),
            "-filter_complex",
            filt,
            "-t",
            str(args.seconds),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-shortest",
            str(tmp),
        ]
    )
    run(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "a:0",
            "-show_entries",
            "stream=codec_type",
            "-of",
            "csv=p=0",
            str(tmp),
        ]
    )
    tmp.replace(out)
    print(out)


if __name__ == "__main__":
    main()

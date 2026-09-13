# FOSS bill of materials (Spark)

Closed tools this stack replaces — Canva, CapCut, Photos albums as the system of record, Instagram Add music, Later/Metricool as publisher.

| Package | Role | Spark install |
|---|---|---|
| python3 | glue | distro |
| python3-pil (Pillow) | draw 1080x1350 slides | `apt install python3-pil` |
| ffmpeg / ffprobe | crop, zoom, mux bed AAC | `apt install ffmpeg` |
| ImageMagick 7 | batch 4:5 crops if preferred | `apt install imagemagick` |
| fonts-dejavu-core | default type | `apt install fonts-dejavu-core` |
| Syncthing | outbox → iPhone | `apt install syncthing` |
| Ollama + Hermes | micro-dose → 8-line script | already on Spark |
| ACE-Step 1.5 | local instrumental beds (Apache 2.0) | separate install; not called from v1 scripts |
| jq | inspect script.json | optional |
| git | skill + factory versioned | already |

Optional OFL faces in `assets/fonts/` — Source Serif 4, Source Sans 3, or IBM Plex. If present, `render_slides.py` prefers them over DejaVu.

Do not call Suno from Hermes. Drop an approved WAV/MP3 at `audio/transurfing-bed.mp3` or generate it on Spark with ACE-Step. MusicGen and YuE2 weights are typically non-commercial; do not use them on the HVE grid.

Instagram’s app is the only non-FOSS hop, because there is no trustworthy open publisher for mixed photo/video carousels with original audio. Do not add instagrapi or unofficial private APIs to this skill.

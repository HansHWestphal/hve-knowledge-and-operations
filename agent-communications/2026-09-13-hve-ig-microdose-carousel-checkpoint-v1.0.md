# HVE IG Microdose Carousel Factory — Checkpoint

**Date:** 2026-09-13  
**Project:** Issue #24 — `ig-microdose-carousel`  
**Status:** Ready to resume

## Confirmed decisions

- Runtime root: `/home/hans/hve/ig-factory/`
- Git checkout remains `/home/hans/humanvalueexchange/`
- Runtime media, model weights, generated audio, work files, and phone outbox stay outside Git.
- Tool split:
  - ImageMagick for asset preparation and batch transforms
  - Pillow for deterministic slide composition and text layout
  - FFmpeg/ffprobe for cover video, audio muxing, and validation
  - ACE-Step 1.5 for required local MP3 generation
- Approved fonts: IBM Plex primary, with Noto and DejaVu available for fallback.

## Spark foundation

- Ubuntu 24.04.4 LTS
- ARM64/aarch64
- 20 Cortex-X925 CPU cores
- NVIDIA GB10, driver 580.159.03
- 121 GiB unified memory
- Approximately 2.8 TB available storage

## Runtime setup

- Factory venv: `/home/hans/hve/ig-factory/runtime/factory-venv/`
- ACE-Step venv: `/home/hans/hve/ig-factory/runtime/ace-step-venv/`
- ACE-Step source: `/home/hans/hve/ig-factory/runtime/ACE-Step-1.5/`
- Model root: `/home/hans/hve/ig-factory/models/`
- UV cache: `/home/hans/hve/ig-factory/cache/uv/`

## ACE-Step status

ACE-Step 1.5 is installed and the LM-enabled Gradio UI has started successfully on the Spark. Confirmed versions include:

- ACE-Step 1.5.0
- PyTorch 2.10.0+cu130
- torchaudio 2.10.0+cu130
- torchvision 0.25.0+cu130
- Transformers 4.57.6

CUDA detects the NVIDIA GB10 and a real FP16 CUDA matmul passed. The PyTorch wheel reports a warning because it lists compiled architectures through `sm_120` while the GB10 reports `sm_121`; this remains a compatibility and performance caveat.

## Next step

Resume with the first real ACE-Step output validation:

1. Generate a short instrumental MP3 in the UI.
2. Save it under `/home/hans/hve/ig-factory/audio/generated/`.
3. Validate the file with `ffprobe`.
4. Record the active model, backend, duration, prompt, and output hash.
5. Only then proceed to the carousel asset inventory and first `LETTERBOX` pack.

No Instagram publication is authorized by this checkpoint.

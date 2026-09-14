# HVE Spark Sound Studio Capability Specification

**Date:** 2026-09-14  
**Status:** Enhancement proposal; deferred for operating-stack configuration later this week  
**Owner:** Hans Westphal, with Luna coordinating architecture  
**Related capability:** `ig-microdose-carousel` and HVE content operations  
**Runtime target:** DGX Spark, local-only production workflow

## Purpose

Human Value Exchange needs a sovereign local sound-production capability on the
DGX Spark. The capability should let HVE content creators make, adapt, catalog,
and reuse original music and sound beds for carousels, short videos, explainers,
podcasts, courses, launches, and internal communications without sending
creative source material to a closed generation service.

This proposal names the capability **Sound Studio**. Sound Studio is a local
creative production system, not a public music service, a streaming platform,
or an automatic social-media publisher.

The final ACE-Step operating configuration is intentionally deferred. The
current installation and model inventory prove that the technical foundation
exists, but they do not yet constitute the approved 24/7 Spark operating stack.

## Current evidence

The following is already present on the Spark:

- ACE-Step 1.5 source under
  `/home/hans/hve/ig-factory/runtime/ACE-Step-1.5/`
- Dedicated ACE-Step environment under
  `/home/hans/hve/ig-factory/runtime/ace-step-venv/`
- ACE-Step 1.5, PyTorch 2.10.0+cu130, torchaudio, torchvision, and
  Transformers installed
- NVIDIA GB10 CUDA detection and a passing FP16 CUDA smoke test
- ACE-Step Gradio UI startup with the 5Hz language model enabled
- Downloaded language models:
  - `acestep-5Hz-lm-0.6B`
  - `acestep-5Hz-lm-1.7B`
  - `acestep-5Hz-lm-4B`
- Downloaded core assets:
  - `acestep-v15-turbo`
  - `Qwen3-Embedding-0.6B`
  - `vae`

One unresolved technical caveat remains: the installed PyTorch wheel reports
compiled architectures through `sm_120`, while the GB10 reports `sm_121`.
Basic CUDA execution works, but model-generation validation and performance
acceptance are still required.

## Sound Studio capability map

### 1. Original music generation

Sound Studio should generate short and long-form music from a structured brief:

- purpose and publishing surface
- emotional direction
- series or campaign
- instrumentation
- tempo and duration
- key or scale where relevant
- vocal, instrumental, or background-only requirement
- energy curve and ending behavior
- content restrictions and exclusions

The output should include the audio file, generation prompt, model, seed or
other reproducibility parameters where supported, duration, sample rate,
format, and a content record.

### 2. Reusable audio beds

The system should create reusable beds for recurring HVE content families:

- Transurfing and stance-oriented microdose content
- Russell and wave-oriented microdose content
- Five Wealth educational content
- Human Life Operating System explainers
- launch and announcement content
- calm reflection, work, focus, and transition beds

Reuse is a creative choice, not a restriction. A creator may reuse a proven bed,
create a variation, or generate a new bed for a particular post. The inventory
must distinguish original generation, approved master, derivative edit, and
published use.

### 3. Editing and repainting

The studio should support controlled revision of local audio:

- shorten or extend a bed
- change the ending
- create an intro, loop, or outro
- repaint a selected section
- alter instrumentation or energy
- create alternate mixes for different durations
- produce a clean instrumental version
- normalize loudness without destroying dynamics

Every derivative should preserve a link to its source asset and record the
change requested.

### 4. Cover and reference-audio workflows

Where the tool supports it, creators should be able to provide reference audio
to guide a new version or cover. This must be governed by provenance:

- use HVE-owned or properly licensed reference material
- record the reference asset and permission status
- do not treat a generated similarity as proof of ownership
- obtain human approval before publication

### 5. Vocal-to-background-music workflows

Sound Studio should support turning an approved vocal, spoken-word, or
instructional recording into a suitable background bed. This is useful for:

- Hans narration over a restrained musical bed
- Five Wealth lessons
- Human Life Operating System walkthroughs
- founder messages
- course and podcast segments

The workflow must preserve the original voice recording, create a separate
music derivative, and never overwrite the source.

### 6. Track and stem separation

Where supported and legally appropriate, creators should be able to separate
or export stems for:

- drums and percussion
- bass
- harmonic instruments
- melodic elements
- vocals
- ambience and effects

Stem operations enable quieter voice-over mixes, alternate edits, and
accessibility versions. Stem separation is a transformation of an approved
source, not permission to use third-party material.

### 7. Multi-track and layered production

The longer-term studio should support assembling layers such as:

- voice-over
- generated bed
- approved sound effect
- transition or riser
- silence and breathing room
- end card or call-to-action cue

The first production path may remain file-based and deterministic. A full
timeline editor is not required before the underlying asset and render
contracts are stable.

### 8. Metadata and reproducibility

Every generated or edited asset should have a sidecar record containing, where
available:

- asset identifier and title
- source and derivative relationships
- creator and approver
- prompt or brief
- model and model revision
- seed and generation parameters
- duration, sample rate, channels, and codec
- loudness analysis
- creation date and tool version
- license and provenance notes
- intended series, campaign, or content surface
- publication status
- SHA-256 hash

The goal is to make a useful sound library rather than a directory of anonymous
MP3 files.

### 9. LRC and timed-text support

Where the model or workflow produces lyrics or timed text, Sound Studio should
retain LRC or equivalent timing data. This can support:

- lyric or quote overlays
- accessible captions
- spoken-word alignment
- editing reference points
- future video and reel workflows

Timed text must remain separate from the authoritative written content unless a
human approves the final wording.

### 10. Quality scoring and review

Automated checks should flag, not silently approve:

- clipping
- silence or near-silence
- unexpected duration
- loudness outside the intended range
- malformed audio
- missing channels
- excessive noise or artifacts
- abrupt endings
- prompt or provenance omissions

Human review remains required for creative fit, rights, voice, brand alignment,
and publication approval.

## How HVE content creators use Sound Studio

### Microdose carousel

The creator selects a microdose and chooses a series, such as Transurfing or
Russell. Sound Studio either reuses an approved bed or generates a short
instrumental. The carousel factory muxes the selected audio into the cover
video and records the bed in the carousel ledger.

### Five Wealth education

A creator briefs a calm, intelligible bed for a lesson on Time, Physical,
Mental, Social, or Financial wealth. The same master may produce a short social
cut, a longer lesson cut, and a low-energy background version.

### Human Life Operating System explainer

The creator supplies a narration outline or approved voice recording. Sound
Studio generates or selects an unobtrusive bed, creates an alternate without
voice, and preserves both the source narration and the final mix.

### Launch and announcement

The team creates a recognizable sonic treatment for a launch, event, product
explanation, or company announcement. The asset record links the master,
short sting, transition, and social cut so the identity can be reused
consistently.

### Founder and team communications

Hans or a future content creator can produce a reflective or instructional
voice-over with a controlled bed, without outsourcing private drafts or source
recordings. The final asset remains reviewable and editable locally.

### Localization and accessibility

A master bed can support multiple language voice-overs or captioned versions.
The music, narration, timed text, and final mix remain separate so one approved
change does not require regenerating the entire production.

## Proposed Spark architecture

Sound Studio should remain isolated from the existing Hermes, Ollama, and other
agent runtimes:

```text
/home/hans/hve/ig-factory/
├── audio/
│   ├── originals/
│   ├── generated/
│   ├── approved/
│   ├── derivatives/
│   ├── stems/
│   └── manifests/
├── models/
│   └── checkpoints/
├── runtime/
│   ├── ace-step-venv/
│   └── ACE-Step-1.5/
├── work/
│   └── <project-slug>/
├── outbox/
└── ledger.jsonl
```

The final directory layout may be reconciled with the carousel asset
inventory, but media and model weights must remain outside GitHub.

The operating stack should provide:

- one controlled ACE-Step runtime
- one documented model/cache policy
- explicit CPU/GPU resource controls
- repeatable generation commands
- local UI for creators
- a later API or script interface for governed automation
- logs and output manifests
- no public Gradio share links
- no automatic Instagram publishing

## Operating and governance requirements

Before Sound Studio becomes a standing Spark service, the team must decide:

1. The approved ACE-Step model and backend for routine production.
2. Whether the 0.6B, 1.7B, and 4B LMs are all retained resident or loaded on
   demand.
3. The acceptable concurrency with Hermes and other HVE workloads.
4. The approved output formats, loudness targets, and duration limits.
5. The asset approval and rights-review workflow.
6. The model and prompt provenance retention period.
7. The service boundary: UI only, CLI, API, or all three.
8. Whether ACE-Step should run on demand or under a managed systemd service.
9. How backups protect original audio, masters, manifests, and inventory.
10. The acceptance test for GB10 `sm_121` behavior and performance.

No decision in this document authorizes public publishing, third-party
distribution, or automatic social posting.

## Deferred work

- Complete model-load and short-MP3 generation tests for all three LMs.
- Resolve or formally accept the `sm_121` PyTorch warning.
- Select production model/backend defaults.
- Define asset inventory and audio manifest schemas.
- Build deterministic render and loudness-validation helpers.
- Decide whether to add local image enhancement to the broader content factory.
- Configure Syncthing only after the outbox and approval boundary are stable.
- Produce the first approved `LETTERBOX` carousel pack.

## Intended outcome

Sound Studio should make local music creation a governed, reusable HVE content
capability. It should reduce dependence on closed creative services while
increasing provenance, reuse, consistency, and editorial control. The success
measure is not the number of generated songs; it is whether HVE creators can
reliably turn an approved brief into publication-ready audio that fits the
content, can be reproduced or revised, and remains under HVE control.

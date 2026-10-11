# HVE Hermes Runtime Update Pipeline - Step 6 Activation Record

- **Date:** 2026-10-11
- **Version:** 1.1
- **Prepared by:** Luna, HVE CTO / Head Architect
- **Decision authority:** Hans Westphal, CEO
- **Status:** v0.21.6 promoted; daily stable-update timer enabled

## Scope and approval

This version updates the Step 6 implementation record in
[`2026-10-11-hve-hermes-runtime-update-pipeline-v1.0.md`](2026-10-11-hve-hermes-runtime-update-pipeline-v1.0.md).
Hans explicitly approved production activation through the interactive
`approve_activation` confirmation on 2026-10-11. The approval covered arming the
selector, promoting Hermes `v0.21.6` with its four-service restart, and
enabling scheduled automatic updates. The selector still requires current
unit bindings to match the activation marker before an automatic promotion
can occur.

- **Owner:** Hans Westphal, CEO.
- **Rationale:** Adopt upstream Hermes stable improvements through isolated
  validation and selector-managed rollback instead of an unsafe in-place
  update.
- **Effective date:** 2026-10-11, when `v0.21.6` was promoted.
- **Review date:** 2026-10-12, after the first scheduled run at 03:45 EDT. This
  is a verification checkpoint, not an additional approval.

## Rollback baseline reconciliation

The Step 5 record initially treated `legacy-d54e5b4...` as the rollback
baseline. That release points to a separate dirty checkout and is not the
source imported by the live services. The existing
`/home/hans/.hermes/current` pointer resolved to deployed commit
`45b7b962f6a5e10bc807a243e2544f22c5bcb652`, paired with the existing Hermes
Python 3.11.15 environment.

That exact deployed source and environment were registered as
`legacy-45b7b962f6a5e10bc807a243e2544f22c5bcb652`, checked against the
deployment manifest, smoke-validated, and seeded as the selector's initial
known-good release. The original `/home/hans/.hermes/current` pointer was not
changed. The corrected Step 5 evidence distinguishes the old checkout from the
actual live rollback baseline.

## Stable update path

- `hermes-runtime-deploy.py update` routes to the selector instead of an
  in-place `origin/main` update.
- Discovery uses GitHub's published latest-stable-release endpoint and
  cross-checks the release tag against the official remote's tag target,
  including peeled commits for annotated tags.
- The promoted release is `v0.21.6` at
  `818c13be1dc4fd28987e1e881a9408224afd4535`, using Python 3.14.7 and
  `httpx 0.28.1`. The tag is unsigned; its target was verified against the
  official remote.
- The focused Hermes smoke gate checked version, CLI import, and isolated
  `hermes status`. The full upstream suite was not run, consistent with the
  user-approved minimal acceptance gate.
- Candidate creation follows Hermes' PM-managed runtime setup and fails closed
  for unsupported non-PM layouts.
- The update service invokes the HVE-CFO wrapper with `--automatic`. Each
  scheduled run stages and validates the latest stable release before
  promotion; automatic promotion requires the activation marker and matching
  effective unit bindings.

The earlier mixed-tag ordering attempt selected the older `v2026.9.24`
(`0.21.5`) release and left a private, unregistered partial candidate. It was
not selected or used and remains untouched. Stable discovery was corrected to
use GitHub's latest published stable release metadata.

## Service wiring and activation

- COS gateway, Librarian gateway, and coder worker use the selector's paired
  current source and virtual environment.
- The coder worker continues to resolve its existing pinned
  `/home/hans/.local/bin/hermes-coder` adapter.
- Proton remains on its HVE-Librarian interpreter and `PYTHONPATH`; it is
  included in the four-service restart and active-state check.
- Effective bindings passed for all four consumer services and the update
  service before activation. The activation marker is
  `/home/hans/.local/state/hve-hermes-runtime/activation-armed.json`, owned by
  Hans and mode `0600`.
- The selector runtime root and candidate-store parent are mode `0700`.
- On 2026-10-11 at 22:21:28 UTC, the selector atomically promoted
  `v0.21.6` from rollback baseline
  `legacy-45b7b962f6a5e10bc807a243e2544f22c5bcb652`. The previous baseline
  remains in the known-good set for rollback.
- The selector restarted the COS gateway, Librarian gateway, coder worker,
  and Proton worker. All four reported active afterward. A subsequent
  `journalctl --user -p err` query for those units returned no entries since
  the restart window.

## Scheduled update policy and current state

- `hermes-runtime-update.timer` is enabled and active.
- It runs daily at **03:45 local time** (`OnCalendar=*-*-* 03:45:00`,
  `Persistent=false`). The next scheduled run is 2026-10-12 at 03:45 EDT.
  Because persistence is disabled, a missed run is not replayed at login.
- At the time of this record, the one-shot update service was inactive and the
  timer had not triggered. No second promotion was started by enabling the
  timer.
- The selector's current release is `v0.21.6`; the prior verified live
  baseline remains available for rollback. The private pre-activation Step 6
  evidence record is preserved unchanged.
- **Review checkpoint:** verify the first scheduled run on 2026-10-12 after
  03:45 EDT; that run had not occurred when this record was prepared.

The selector's restart check confirms systemd active state, supplemented here
by the empty error-priority journal query; it is not an application-level
end-to-end health measurement.

## Evidence

The private post-activation evidence is stored mode `0600` at
`/home/hans/.local/state/hve-hermes-updates/evidence/step6-production-activation-20261011T182210-0400.json`.
Its SHA-256 is
`a4d3ef4d50c945e7d86e2f66f0acd7a378fdf73a7b3485c86017f0f9548225c1`.

Selector regression tests passed (**17 passed, 0 failed**); both Python updater
files parsed successfully. Step 4's Hermes smoke evidence remains at
`/home/hans/.local/state/hve-hermes-updates/evidence/step4-minimal-smoke-20261011T172458-0400.json`
with SHA-256
`67c704f80ba50084372285927839fc940945213cb02a1e84ac4357e5cee61116`.

# HVE Hermes Runtime Update Pipeline - Step 6 Implementation Record

- **Date:** 2026-10-11
- **Version:** 1.0
- **Prepared by:** Luna, HVE CTO / Head Architect
- **Decision authority:** Hans Westphal, CEO
- **Status:** Step 6 wiring and validation complete; production activation remains gated

## Scope and approval

Hans approved implementation of the six-step Hermes update plan and directed
completion through Step 6. This record documents the selector, updater, and
service wiring only. It does **not** authorize promotion of the staged release,
service restarts, activation arming, or enabling the update timer.

## Rollback baseline reconciliation

The Step 5 record initially treated `legacy-d54e5b4...` as the rollback
baseline. That release points to a separate dirty checkout and is not the
source imported by the live services. The existing
`/home/hans/.hermes/current` pointer resolved to deployed commit
`45b7b962f6a5e10bc807a243e2544f22c5bcb652`, paired with the existing Hermes
Python 3.11.15 environment.

That exact deployed source and environment were registered as
`legacy-45b7b962f6a5e10bc807a243e2544f22c5bcb652`, checked against the
deployment manifest, smoke-validated, and seeded as the selector's current
known-good release. The original `/home/hans/.hermes/current` pointer was not
changed. The Step 5 evidence was corrected to distinguish the old checkout
from the real live rollback baseline.

## Stable update path

- `hermes-runtime-deploy.py update` now forwards to the selector instead of
  running the unsafe in-place `origin/main` updater.
- Discovery uses GitHub's published latest-stable-release endpoint and
  cross-checks the release tag against the official remote's tag target,
  including peeled commits for annotated tags.
- As of this record, the official latest stable release was `v0.21.6` at
  `818c13be1dc4fd28987e1e881a9408224afd4535`. Its existing Step 4 candidate
  passed the focused version, CLI import, and isolated `hermes status` smoke
  gate with Python 3.14.7 and `httpx 0.28.1`.
- Candidate creation follows Hermes' PM-managed runtime setup and refuses an
  unsupported non-PM layout rather than leaving a checkout-local venv in a
  release source tree.
- `update --automatic` stages and validates while activation is unarmed; it
  promotes only when the activation marker is present and still matches the
  effective service bindings.

During implementation, an initial numeric ordering of mixed calendar and
semantic-version tags selected the older `v2026.9.24` release (`0.21.5`). Its
setup attempt left a private, unregistered partial candidate. That candidate
was not selected or used, and was left untouched. Discovery was corrected to
use GitHub's latest stable release metadata, which identifies `v0.21.6`.

## Service wiring

- The COS gateway, Librarian gateway, and coder worker now reference the
  selector's paired `current/source` and `current/venv` paths.
- The coder worker still resolves its existing pinned
  `/home/hans/.local/bin/hermes-coder` adapter. Proton remains on its existing
  HVE-Librarian interpreter and `PYTHONPATH`; it remains in the four-service
  restart and health-check scope.
- The Hermes update service passes `--automatic`. The arming check also
  verifies this updater entrypoint and records its effective binding.
- systemd unit definitions were reloaded, but no service was restarted.
  All four Hermes consumer services remained active.

## Validation and current state

- Selector regression tests: **17 passed**; both Python updater scripts parsed
  successfully.
- The deployed rollback baseline and the latest stable candidate both passed
  the selector smoke validation.
- Effective bindings passed for all four Hermes consumer units and the update
  service. The wrapper returned `staged_validation_passed` and
  `promotion_blocked: activation is not armed`.
- The selector currently points to the validated `legacy-45b7...` baseline.
  Candidate `v0.21.6` is staged and validated, but is **not live**.
- The activation marker is absent. `hermes-runtime-update.timer` remains
  inactive and disabled. No Hermes consumer service was restarted or promoted.
- The candidate-store parent permissions were tightened from `0775` to
  `0700`; existing candidate contents were preserved.

Production activation remains a separate gate. It requires explicit approval
before arming the selector, promoting `v0.21.6` (which restarts the four
Hermes consumers), or enabling scheduled automatic updates.

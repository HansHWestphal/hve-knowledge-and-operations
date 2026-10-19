# HVE Spark-Local Agent Delegation Platform — Major Implementation Update

**Date:** 2026-09-11
**Status:** Phase 6 pilot evidence passed; telemetry capture is now active
**Owner:** Luna, HVE CTO / Head Architect
**Decision authority:** Hans Westphal, CEO
**Related issue:** [#21](https://github.com/HansHWestphal/hve-knowledge-and-operations/issues/21)
**Supersedes:** The implementation status recorded in the original Issue #21
description and prior Phase 6 evidence

## Executive update

The Spark-local Hermes-Coder delegation platform now has working queue
lifecycle controls, worker recovery, workspace and safety preflight, readiness
policy, cohort-aware pilot evaluation, and runtime telemetry capture.

The first live pilot attempt was correctly stopped before execution because its
workspace was outside the worker's approved root. That failed attempt remains
preserved as `phase6-pilot-20260911-r1` evidence. A corrected ten-task cohort
was then run under the approved HVE workspace root:

`phase6-pilot-20260911-r2`

The corrected cohort produced:

| Measure | Result |
|---|---:|
| Qualified tasks | 10 |
| Completed tasks | 10 |
| Safety pass rate | 100% |
| Review pass rate | 100% |
| Intervention rate | 0% |
| Recovery rate | 0% |
| Pilot decision | `PILOT_PASS` |

The failed and successful cohorts are isolated by `pilot_id`; no historical
pilot evidence was deleted or merged.

## Telemetry enhancement

The queue and metrics layer now records:

- `pilot_id` for cohort-level comparison;
- `execution_mode` as `pilot` or `live`;
- model and provider;
- input, output, and cache token counts;
- turns/API calls;
- tool-call count;
- wall-clock duration;
- telemetry completeness and parser errors;
- estimated local cost;
- pricing status, source, version, and fetch timestamp as a pricing snapshot.

The worker consumes Hermes-Coder's authoritative `--usage-file` JSON report
instead of scraping human-readable output. The parser is strict: missing or
invalid fields are recorded as `partial` or `unavailable`, never silently
invented.

A bounded telemetry smoke task completed with complete telemetry:

| Field | Captured value |
|---|---:|
| Job | `5fa1a61fce72` |
| Cohort | `telemetry-smoke-20260911-r3` |
| Model | `qwen3.8-hermes:27b-128k` |
| Input tokens | 41,832 |
| Output tokens | 2,166 |
| Turns | 3 |
| Tool calls | 2 |
| Wall-clock time | 160.75 seconds |
| Estimated local cost | `$0.00` |
| Telemetry status | `complete` |

The local Qwen model currently has no pricing catalog entry. The system
therefore records pricing status `unknown` and source `none` rather than
claiming a false cost estimate. The schema and capture path are ready for a
pricing entry to be added later.

## Phase 6 status

**Phase 6 implementation and controlled pilot gate: PASS.** The ten-task
cohort met the defined safety, review, intervention, and recovery thresholds.
The telemetry smoke also proves that runtime model, token, turn, tool-call, and
pricing-snapshot fields can be captured end to end.

**Phase 6 is not authorization to make local execution universally default.**
The successful ten-task pilot predates complete runtime telemetry capture, and
the telemetry smoke task reached the existing review boundary without a
reviewable unstaged diff. Before changing operating defaults, Luna should run a
small reviewable cohort with complete telemetry on every task and obtain Hans's
explicit operating decision.

Issue #19 remains paused. No production defaults, COS/Librarian/CFO behavior,
deployment, commit, push, or issue closure was changed.

## Rollback and validation evidence

Focused temporary-database validation remains green:

`13 tests OK`

The final verified rollback bundle is:

`/home/hans/.hermes/backups/hermes-coder-telemetry-final-20260911T214420Z/`

The Hermes-Coder worker is active with exactly one worker process. Disposable
smoke workspaces were removed after validation. The host-local implementation
remains subject to the approved bootstrap exception; normal bounded
implementation work returns to Hermes-Coder after the remaining operating
decision and reviewable telemetry cohort are complete.

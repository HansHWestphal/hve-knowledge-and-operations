# HVE Chief of Staff Completion Evidence — Gate 2 Preparation

**Date:** 2026-09-20  
**Owner:** Luna, HVE CTO / Head Architect  
**Status:** Gate 2 staged locally; controlled cutover blocked pending owning-runtime publication  
**Primary tracker:** [HVE knowledge-and-operations #40](https://github.com/HansHWestphal/hve-knowledge-and-operations/issues/40)  
**Prior evidence:** [Gate 1 reconciliation v1.2](https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/main/agent-communications/2026-09-20-hve-chief-of-staff-completion-evidence-v1.2.md)

## Shared runtime candidate

The minimal runtime candidate was built in a clean worktree from the live
runtime base:

- Base: `861ca0cc7274a1efc1c2324e15b5f49f74a81db7`
- Candidate: `45b7b962f6a5e10bc807a243e2544f22c5bcb652`
- Change source: upstream lifecycle commit `c230d04d8317f97f7a4df4539bf85a5f05ed09f0`
- Runtime worktree: `/tmp/hermes-agent-gate2-minimal`
- Staged release: `/home/hans/.hermes/releases/45b7b962f6a5e10bc807a243e2544f22c5bcb652`

The candidate changes only:

- `tools/code_kernel.py`
- `tests/tools/test_code_kernel.py`

The implementation adds a low-frequency background idle-kernel reaper,
attached-cell protection, and stale kernel staging-directory cleanup. The
conflicting follow-up commit `31d237c...` was intentionally excluded because
it depends on unrelated later runtime lineage and does not apply cleanly to
the pinned live base.

## Validation and preflight

- Complete `tests/tools/test_code_kernel.py`: **27 passed**
- Candidate diff check: passed
- Tracked-file parity from clean worktree to staged release: passed
- Staged deployment manifest JSON: passed
- Runtime selector remains unchanged at:
  `/home/hans/.hermes/releases/861ca0cc7274a1efc1c2324e15b5f49f74a81db7`
- `hermes-gateway-hve-chief-of-staff.service`: active
- Gateway main PID remains `1512544`
- No selector change, service restart, or production cutover occurred

The staged manifest records COS revision
`1c72fb6dd7c6b6f46ce14ae34b2468fba34343c9`, restart-required behavior, and
rollback to the live `861ca0cc...` release.

## Publication blocker

The exact candidate was not publishable to the owning runtime repository from
this environment. The attempted publication to
`https://github.com/NousResearch/hermes-agent.git` was rejected with:

`Permission to NousResearch/hermes-agent.git denied to HansHWestphal (403)`

No fork was available at `HansHWestphal/hermes-agent`. The clean local
candidate and staged release are preserved for review, but the runtime fix is
not yet an externally published owning-repository revision. Therefore Gate 2
is **not ready for controlled cutover** and the live selector must remain
unchanged.

## Required next gate

An authorized owner must publish or otherwise approve the exact runtime
candidate in the owning Hermes runtime repository. After that publication,
reconcile the published commit against the staged release, review the
combined COS/runtime manifest, and obtain cutover approval before switching
the selector and restarting only the COS gateway. Then perform the lifecycle,
gateway, WhatsApp, scheduler, watchdog, memory-maintenance, x333, rollback,
and observation checks.

No predecessor reactivation, LifeOS migration, automatic replay, database
deletion, credential movement, or unrelated service change was performed.

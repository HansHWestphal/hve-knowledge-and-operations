# HVE Chief of Staff Completion Evidence — Runtime Boundary Correction

**Date:** 2026-09-20  
**Owner:** Luna, HVE CTO / Head Architect  
**Status:** Corrected Gate 2 preparation record  
**Primary tracker:** [HVE knowledge-and-operations #40](https://github.com/HansHWestphal/hve-knowledge-and-operations/issues/40)  
**Supersedes:** [Gate 2 preparation v1.3](https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/main/agent-communications/2026-09-20-hve-chief-of-staff-completion-evidence-v1.3.md)

## Boundary correction

The previous record incorrectly treated publication to the upstream
`NousResearch/hermes-agent` repository as a Gate 2 prerequisite and incorrectly
described the generic runtime change as an HVE adapter violation.

The authoritative HVE runtime boundary says that Hermes owns execution,
conversation/session state, and runtime lifecycle. The HVE adapter owns
organization identity, policy, data roots, channels, credentials, and approval
sinks. The candidate lifecycle change is generic Hermes behavior: it contains
no HVE, COS, organization, profile, or adapter coupling.

Therefore:

- Hermes remains pure with respect to HVE-specific behavior.
- No COS-specific runtime logic belongs in the adapter for this defect.
- No fork or upstream publication is required for the local immutable runtime
  deployment path.
- The earlier upstream push attempt and fork lookup were unnecessary and are
  not part of the deployment path.

## Correct runtime candidate

- Live base: `861ca0cc7274a1efc1c2324e15b5f49f74a81db7`
- Local candidate: `45b7b962f6a5e10bc807a243e2544f22c5bcb652`
- Clean source worktree: `/tmp/hermes-agent-gate2-minimal`
- Staged release:
  `/home/hans/.hermes/releases/45b7b962f6a5e10bc807a243e2544f22c5bcb652`
- Changed files: `tools/code_kernel.py` and
  `tests/tools/test_code_kernel.py`

The candidate adds the generic proactive idle-kernel reaper, attached-cell
protection, and stale staging-directory cleanup. The runtime test module
passed **27 tests**. The staged release remains inactive.

## Current gate state

The runtime selector remains on the live release
`861ca0cc7274a1efc1c2324e15b5f49f74a81db7`; the COS gateway remains active
with main PID `1512544`. No service restart or production cutover occurred.

Gate 2 is no longer blocked by external repository publication. It remains
pending the controlled cutover approval and the final lifecycle, gateway,
WhatsApp, scheduler, watchdog, memory-maintenance, x333, rollback, and
observation checks.

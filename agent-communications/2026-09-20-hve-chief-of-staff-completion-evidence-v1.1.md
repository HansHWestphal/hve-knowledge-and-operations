# HVE Chief of Staff Completion Evidence — Gate 1 Plan

**Date:** 2026-09-20  
**Owner:** Luna, HVE CTO / Head Architect  
**Status:** Gate 1 implementation plan  
**Primary tracker:** [HVE knowledge-and-operations #40](https://github.com/HansHWestphal/hve-knowledge-and-operations/issues/40)  
**Prior evidence:** [v1.0](https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/main/agent-communications/2026-09-20-hve-chief-of-staff-completion-evidence-v1.0.md)

## Gate 1 objective

Reconcile the live profile at
`/home/hans/.hermes/profiles/hve-chief-of-staff` to one exact,
repository-owned COS source revision without replacing or deleting mutable
runtime state, restarting services prematurely, or reactivating predecessor
paths.

## Implementation plan

1. **Freeze the target revision.** Resolve the current provenance mismatch:
   the pushed COS repository is at
   `eb505ba01c5ba1e464f71118b31732286f43ea96`, while the release metadata
   currently identifies `4f60f1abce5f24536ed4af19dcb98663c242f006` as the
   source revision. Select one exact approved commit and make `RELEASE.yaml`,
   `provenance.yaml`, the staged deployment manifest, and issue evidence
   agree.

2. **Create a read-only live inventory.** Record hashes and paths for
   repository-owned files currently present in the live profile, including
   configuration, scripts, skills, schedules, watchdog, reliability review,
   memory maintenance, and channel configuration.

3. **Classify every profile item.**
   - Regenerate from Git: identity, instructions, skills, scripts, adapters,
     schedules, deployment configuration, and validation assets.
   - Preserve in place: databases, WAL/SHM files, credentials, environment
     files, WhatsApp session data, logs, caches, locks, generated reports,
     backups, and historical evidence.
   - Reject: predecessor paths or symlinks into `hanshermesagent`,
     `hermes-v2`, or retired session state.

4. **Stage the repository revision outside the live profile.** Run the
   immutable staging tool against the selected commit, validate the clean
   checkout, verify checksums, and write the deployment manifest. No live
   files or services change during staging.

5. **Reconcile only repository-owned live files.** Perform a controlled,
   reviewable migration into the profile. Do not wholesale-copy the
   repository over the existing profile and do not delete runtime state.

6. **Verify runtime ownership.** Confirm the active profile path, profile-local
   WhatsApp session, COS-owned schedules, COS memory-maintenance path, and
   absence of active `hanshermesagent` or `hermes-v2` dependencies. Record
   shared Hermes runtime provenance separately from COS source provenance.

7. **Run offline and shadow checks.** Validate profile loading, source/runtime
   boundaries, schedule definitions, watchdog, memory maintenance, delivery
   outcomes, weekly reliability review, x333 authorization refusal, and
   rollback without replaying missed jobs.

8. **Preserve rollback.** Retain the existing known-good profile state and
   deployment reference as the rollback target. Do not delete historical
   backups, databases, sessions, or logs.

9. **Request controlled cutover.** Only after the diff and evidence are
   reviewed should the staged revision be activated, only the COS gateway be
   restarted, and the gateway, channel, scheduler, memory, and observation
   window be verified.

## Gate 1 safety boundary

No live profile change, service restart, job replay, predecessor reactivation,
database deletion, credential movement, or LifeOS migration is included in
this gate. The current gateway remains active and the observed idle kernel
remains preserved until the controlled lifecycle and cutover evidence is
ready.

Gate 1 is not complete until the selected exact revision is internally
consistent across source metadata, staged manifest, live provenance, and issue
#40 evidence.

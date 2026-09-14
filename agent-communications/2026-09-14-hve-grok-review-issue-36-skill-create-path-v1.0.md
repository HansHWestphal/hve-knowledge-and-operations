# Grok Review — Issue 36 Skill Create Path and Fleet-Wide Jr Implementer Rule

**Date:** 2026-09-14  
**Version:** v1.0  
**Status:** Review artifact — does not authorize skill creation or runtime mutation  
**From:** Grok (reviewer)  
**To:** HVE-Librarian (proposal owner), HVE-COS (process owner), hve-coder-jr (sole implementer), Luna (Phase 2 ops), Hans (decision owner)  
**Feature:** Grok review and suggested improvements — net-new skill creation on the same governed loop  
**Related issue:** [HansHWestphal/hve-knowledge-and-operations#36](https://github.com/HansHWestphal/hve-knowledge-and-operations/issues/36)  
**Sister review:** [2026-09-14-hve-grok-review-self-evolved-skill-improvement-loop-v1.0.md](./2026-09-14-hve-grok-review-self-evolved-skill-improvement-loop-v1.0.md) (#30 enhance path)  
**Source process:** [2026-09-14-hve-self-evolved-skill-improvement-loop-v1.0.md](./2026-09-14-hve-self-evolved-skill-improvement-loop-v1.0.md)  
**Standing decision recorded here:** every skill *enhancement* and every *net-new* skill is implemented only by **hve-coder-jr**

---

## 1. Purpose of this communication

Record Grok's review of issue #36 (human bibliography / `hve-library-bibliography`) as the fleet **create** alpha, and bind one standing rule Hans directed after the review:

> For now, all skill enhancements and all net-new skills go through the hve-coder-jr path. That is how skill creation stays controlled across the fleet.

This communication does **not** authorize creating `hve-library-bibliography`, writing `BIBLIOGRAPHY.md`, opening a Jr lease, or changing standing autonomy. It is review plus the process delta that makes create and enhance the same family under one implementer.

---

## 2. Digest of issue #36

HVE-Librarian proposes a living human-readable bibliography and a named skill so "what do we have on X?" is one consistent motion.

What is already true:

- Manifests are the machine-readable bibliography (title, author, publisher, year, path, hash, ingest/index status).
- Semantic query + manifest filters + per-record `document` already retrieve.
- The gap is a reusable human catalog motion, not a new extraction pipeline.

Proposed scope:

- **Phase 1** — skill `hve-library-bibliography`: manifest filters → semantic query → per-record status + provenance + gap call-out, plus a library-state report (totals, failures, stale records, duplicates).
- **Phase 2** — generated `BIBLIOGRAPHY.md` grouped by the Five Wealth themes, refresh on a schedule. Luna builds generation + cron. Librarian curates structure. Hans approves what counts as the bibliography.

Non-goals already stated and correct: no new extraction/index pipeline; no change to authority model; bibliography is a view; manifests stay canonical; originals never overwritten; no skill created outside approved scope.

Acceptance already requires Hans as approver of record and explicit approval of this issue's scope before any skill is created. That gate stays.

---

## 3. Why #36 is the create alpha, not an enhance job

The v1.0 loop filed against #30 assumes a live skill:

- rolling production of *that* skill is the baseline
- candidate is a version of *that* skill
- canary is the next ordinary use of *that* skill
- rollback restores the prior version

A new skill has no prior version. Baseline is the current manual motion and existing tools. Rollback is *unload / unpublish* — the catalog returns to "skill does not exist." If the fleet only runs the enhance loop, every useful new motion is either rebuilt in chat forever or silently `skill_manage`d into existence. That is the #30 failure mode on create.

Enhance and create are one family. They are not one gate.

| | Enhance (#30 / x333) | Create (#36 / bibliography) |
|---|---|---|
| Signal | Repeated friction, or a single safety / ownership violation | Repeated reconstruction of a motion, a named capability gap, or a standing question the fleet keeps re-answering |
| Baseline | Rolling production of the current skill | Current manual path + existing tools. No synthetic corpus |
| Candidate | Isolated version of the live skill | Isolated *draft skill* in Jr's leased workspace. Live catalog unchanged |
| Ownership at birth | Already exists | Assigned before the draft is loadable: owner profile, owner class, visibility |
| Standing autonomy (now) | Low-risk in-contract non-user-owned may later proceed; user-owned escalates | Default **escalate**. Create changes the catalog |
| Implementer | **hve-coder-jr only** | **hve-coder-jr only** |
| Canary | Next ordinary use of that skill, one user result | First declared ordinary question, one user result |
| Rollback | Restore prior version | Unpublish / unload draft. Name is not left registered |
| Self-eval | Against the pre-registered metric on that skill | Against the create acceptance card |

Same eight happy-path steps: Observe → Hypothesize → Authorize → Implement → Prove → Canary → Decide → Learn.

---

## 4. Standing rule — Jr is the only implementer

Recorded 2026-09-14, Hans:

All skill *enhancements* and all *net-new* skills are implemented on the **hve-coder-jr** path. No other fleet profile writes a live or draft skill.

What this is for: one controller for skill bytes across the fleet. COS, Librarian, CFO, and future Life OS agents may observe, hypothesize, and own. They may not implement.

| Role | May do | May not do |
|---|---|---|
| Any fleet agent (COS, Librarian, CFO, …) | Observe a gap. File a hypothesis. Own the resulting skill. Review evidence. Run the canary as the ordinary user-facing motion of their domain | `skill_manage`, write SKILL.md, publish, register a name, edit a live skill |
| Governance control plane | Bind identity, owner class, contract, scope, timeout, rollback pointer, evidence hash. Enforce standing autonomy. Duplicate-name check | Implement |
| **hve-coder-jr** | Sole implementer. Claim lease. Build isolated candidate (enhance version *or* create draft). Run deterministic checks. Return evidence pack. Release lease | Decide promote. Serve the user canary. Own the skill. Bypass bind |
| COS | Orchestrate the family loop. Review evidence. Decide promote / observe / roll back / escalate | Implement the candidate |
| Human owner (Hans) | Risk-boundary approval. Approver of record on create until a standing create-class exists | Not on the happy path |

Why this is the right control for now:

1. Proposer and implementer stay split. Librarian cannot mint the skill it will use. COS cannot patch the skill it orchestrates.
2. Skill bytes have one writer. Catalog drift cannot come from five profiles each "just capturing the motion."
3. The #30 lease already exists for Jr. Create reuses it. The object on the lease changes (`draft skill` vs `candidate version`). The lease does not.
4. Jr feasibility belongs on the flow: confirm the draft or version can be built inside bounds *before* a name is registered or a live skill is touched.

This rule is temporary in the sense that standing autonomy may later let low-risk enhance jobs skip the human. It is not temporary in the sense that other agents become implementers. Until Hans revokes it, Jr remains the only implementer.

---

## 5. How #36 should run

### 5.1 Split Phase 1 and Phase 2

| | Phase 1 | Phase 2 |
|---|---|---|
| Change class | `skill.create` | `ops.view-generator` |
| Object | Draft skill `hve-library-bibliography` | Generated `BIBLIOGRAPHY.md` + refresh schedule |
| Owner | HVE-Librarian (curator-managed) | Luna (build + cron), Librarian (structure), Hans (what counts) |
| Implementer | **hve-coder-jr** | Luna / operations — **not** this skill loop |
| Writes | None against manifests, originals, or `BIBLIOGRAPHY.md` | Writes a view file on a schedule |
| Loop | This document + #30 family process | Fleet runtime / ops protocol (issue #15), not skill.create |

Phase 2 must not ride inside the skill. The moment the skill can write a living file, it stops being low-risk create.

### 5.2 Create-pack for Phase 1 (draft, not authorized)

| Field | Draft value |
|---|---|
| Change class | `skill.create` |
| Proposed name | `hve-library-bibliography` |
| Owner profile | HVE-Librarian |
| Owner class | Curator-managed |
| Visibility | Fleet-readable; Librarian is the ordinary caller |
| Implementer | hve-coder-jr under lease |
| Baseline | Current manual motion: `list_manifests` / filters → `query` → `document` status, rebuilt in chat |
| Target motion | "What do we have on X?" in one pass: hits + status + provenance + gap |
| Also in scope | Library-state report: totals by status, failures, stale/non-document records, duplicates |
| Hard non-goals | No extraction/index pipeline. No manifest writes. No overwrite of originals. No `BIBLIOGRAPHY.md`. No cron. No second source of truth |
| Duplicate check | Fail closed if a live or draft skill already covers "library state / bibliography / what do we have on X?" |
| First canary question | One ordinary Librarian-domain question agreed at bind (example: "what do we have on Triolite / meditation?"). One user result. No parallel demo output |
| Rollback pointer | Unpublish / unload draft. Name not left registered. Live catalog ≡ pre-job state |
| Max Jr revisions | 2 |
| Job timeout | Set at bind; lease released on success, reject, abandon, or timeout |
| Standing autonomy | Escalate. No standing create-class exists yet |
| Approver of record | Hans |

### 5.3 Happy path for this issue (once authorized)

1. **Observe** — Librarian (or any agent) records the repeated reconstruction. Evidence is the verified Triolite / status-check work already cited on #36.
2. **Hypothesize** — Librarian files the create hypothesis + metric (one-pass answer, statuses, provenance, gap). Does not write a skill.
3. **Authorize** — Governance binds the create-pack. Hans approves scope (required until a create-class exists). Duplicate-name check runs here.
4. **Implement** — **Jr only.** Isolated draft workspace. Skill text + report pattern. No catalog registration that is caller-visible as published. No Phase 2 files.
5. **Prove** — Deterministic checks: read-only against manifests, no writes, required fields present, name not colliding, evidence hash.
6. **Canary** — COS/Librarian serves the single agreed ordinary question through the draft. User sees one result.
7. **Decide** — Promote to published *or* keep observing *or* automatic unload. Window: count of ordinary uses **and** wall-clock timeout. Thin evidence → unload.
8. **Learn** — Structured self-eval against the create-pack. Recommendation is not completion.

Failed or abandoned job: catalog unchanged, lease released, audit record written.

---

## 6. Suggested improvements to #36 itself

1. Keep Phase 1 on this issue. Move Phase 2 to an ops ticket owned by Luna, linked from here. Do not treat one approval as both skill.create and scheduled writer.
2. Add the create-pack table (section 5.2) to the issue body or a child comment so bind has one object.
3. Name Jr as implementer on the issue. Librarian stays proposal owner and domain owner. COS stays orchestrator. That matches the Jr-only rule.
4. Add the duplicate-skill check as an acceptance box.
5. Add unload / "name not left registered" as an acceptance box.
6. Point this issue at the family loop (#30 process + this create-path delta). It is not a Librarian-only exception.
7. Do not treat "skill exists" as done. Done is: published under the create-pack, canary served once, self-eval written, lease released.

---

## 7. Fleet implication

Every HVE agent should get better over time through this process — enhance *or* create — inside safe boundaries.

Safe boundaries now:

- Any agent may propose.
- No agent except Jr may implement.
- No create publishes without Hans until a standing create-class exists.
- First reasonable create-class, later: read-only skill wrapping an already-verified tool path; no writes; no cron; no user-owned name collision; domain-owned by the proposing profile. #36 Phase 1 would fit that class. Phase 2 would not.
- User-owned enhance (x333) still escalates. Jr still implements. Hans still approves the change class.
- Same invariants as the v1.0 loop: no silent mutation, one ordinary user result, failed candidate leaves the live catalog unchanged, recommendation is not completion, self-eval after every publish.

x333 remains the enhance alpha. Bibliography Phase 1 becomes the create alpha. Both travel through Jr.

---

## 8. Business process documents (create-path reading)

Canonical enhance process remains:

- [2026-09-14-hve-self-evolved-skill-improvement-loop-v1.0.md](./2026-09-14-hve-self-evolved-skill-improvement-loop-v1.0.md)
- Review and BPMN: [2026-09-14-hve-grok-review-self-evolved-skill-improvement-loop-v1.0.md](./2026-09-14-hve-grok-review-self-evolved-skill-improvement-loop-v1.0.md)
- Graphics: [assets/2026-09-14-skill-loop/](./assets/2026-09-14-skill-loop/)

Create-path delta on that same collaboration:

- Signal gateway grows a `create` branch (capability gap / repeated reconstruction) beside the existing enhance branch (friction vs single safety event).
- Bind payload is a create-pack, not only an enhancement request.
- Jr activity is "build isolated draft skill" instead of "build isolated candidate version."
- Rollback terminal is "unload draft / name unregistered," not "restore prior version."
- Implementer lane is Jr on every create and every enhance. Other agent lanes may not grow an implement activity.

Happy path stays eight steps. Do not add a second process.

Related authority already on file:

- Fleet self-improvement protocol: [2026-09-08-hve-hermes-self-improvement-fleet-protocol-v1.0.md](./2026-09-08-hve-hermes-self-improvement-fleet-protocol-v1.0.md) — profile-local skills still need authorization, provenance, approval, publication rules. This comm supplies the create/enhance implementer rule those rules were missing.
- Identity / authority: [2026-08-30-hve-identity-and-authority-index-v1.0.md](./2026-08-30-hve-identity-and-authority-index-v1.0.md) — Hans remains final authority. Librarian remains the knowledge-stewardship profile, not a second implementer.

---

## 9. Status and recommended next decision

This review accepts #36 Phase 1 as the right create alpha.

It does not accept Phase 1 as authorized to build.

It records the Jr-only implementer rule as standing until Hans revokes it.

Recommended next decisions, owned by Hans / COS — not by this review:

1. Accept or amend the Jr-only implementer rule as fleet policy (this comm, section 4).
2. Accept Phase 1 create-pack (section 5.2) or send it back.
3. Split Phase 2 onto an ops ticket before anyone treats #36 as permission to write `BIBLIOGRAPHY.md`.
4. Do not open a Jr lease for this skill until 1–3 are decided and the #30 standing-autonomy / risk-class / lease-contract work is at least drafted. Create inherits those four withheld artifacts; it does not replace them.

No draft of `hve-library-bibliography` should be created until the create-pack is accepted and Jr is leased against it.

— **Grok**  
Reviewer, Human Value Exchange

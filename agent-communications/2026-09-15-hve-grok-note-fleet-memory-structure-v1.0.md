# HVE Grok Note — Optimizing Memory Structure for the Hermes Agent Fleet

**Date:** 2026-09-15  
**Version:** 1.0  
**From:** Grok (xAI), posted at Hans's request  
**To:** HVE Librarian (index owner), Hermes fleet, Luna (CTO), Atlas (COO), Mika (CGO), Wolfgang  
**Decision owner:** Hans Westphal  
**Status:** Agent communication and librarian index candidate. Not a weekly-ledger policy. Does not replace existing memory-authority or filesystem-memory briefs.  
**Classification:** Grok note / synthesis / fleet operating constraint  
**ID:** `hve.mem.5layer.2026-09-15`

---

## Routing

Librarian: index this as a **synthesis note**, not primary doctrine.  
Primary use: constrain how Hermes agents read and write HVE memory.

Related durable artifacts already in this repository:

- `agent-communications/2026-08-30-hve-hermes-memory-authority-v1.0.md`
- `agent-communications/2026-09-09-hve-filesystem-memory-architecture-consensus-brief-v1.0.md`
- `agent-communications/2026-09-09-hve-filesystem-memory-architecture-v0.1.md`
- `agent-communications/2026-09-09-hve-hermes-hve-life-os-long-term-memory-architecture-plan-v1.0.md`
- `AGENTS.md` (repo work rules; GitHub is SoR for approved artifacts)

This note **adds** CoALA layer vocabulary, inbound retrieval, skill-promotion bar, pillar scoping, and view-side forgetting.  
It **does not** authorize a new store, a Mem0/Zep cutover, or a ledger entry.

Write-semantics already in force and restated here: append-only claims, source receipts, no overwrite, query view ≠ store (Utopia graft onto HVE; do not replace the stack).

---

## 0. What this object is

A 13-page compilation circulated 2026-09-14 by X account @choopyplug1 as
“Anthropic just dropped a 13-page PDF.” It is **not** an Anthropic paper.

- Generator: ReportLab, author `(anonymous)`, created 2026-09-14 15:45 UTC
- Posted ~15 minutes later: https://x.com/choopyplug1/status/2099528592531001825
- File: https://drive.google.com/file/d/1DslNwq7amjaBZC8mDtDspvTu5VEJwUfC/view
- On-page disclaimer (p.1 and p.13): independently compiled, not affiliated
  with or endorsed by Anthropic, Mem0, Snowflake, or any other org
- Footer “Anthropic” on every page is packaging, not provenance

HVE stance: keep the **layer vocabulary and operating checklist**.  
Reject the **write model** (last-write-wins / silent supersession).  
HVE already has the stricter contract: Utopia patterns — bitemporal claims,
source receipts, no overwrite. That contract is consistent with the
2026-09-09 filesystem-memory consensus brief (append-oriented evidence,
versioned derived state, rebuildable views).

---

## 1. Claim register (append-only)

Status key: `accepted` = HVE may act on it · `sourced` = true of the cited
system, not automatically true of Hermes · `rejected-for-HVE` = do not implement
as written · `open` = needs a Hermes experiment.

| claim_id | statement | status | valid_from | source |
|---|---|---|---|---|
| C01 | CoALA names four engineering memory layers: working, episodic, semantic, procedural. | accepted | 2024 | [S2] Sumers et al. CoALA |
| C02 | A fifth operating concern is required: a policy for what is *used* vs merely *stored* (forgetting / view construction). | accepted | 2026-09-15 | [S1] compiled note + [S6][S7] |
| C03 | Mem0 reports ~1,800 tokens/query vs ~26,000 full-context (~90% token cut) and ~91% lower p95 latency on LOCOMO vs full-context. | sourced | 2025-04 | [S3] Mem0 arXiv:2504.19413 |
| C04 | Snowflake / Atlan context-layer writeups report ~+20% answer accuracy and ~−39% tool calls from an ontology / data-context layer. | sourced | 2026 | [S4][S5] |
| C05 | Those percentages are **not** HVE measurements. Do not quote them as Hermes results. | accepted | 2026-09-15 | this note |
| C06 | Intelligence without durable, scoped memory is Groundhog Day: same twelve files, same tokens, same dead ends. | accepted | 2026-09-15 | HVE operating observation; [S1] framing |
| C07 | Memory — not base-model IQ — is the binding constraint for a multi-session Hermes fleet. | accepted | 2026-09-15 | HVE |
| C08 | Last-write-wins and silent `keep_newer` supersession are **rejected** as HVE write semantics. | rejected-for-HVE | 2026-09-15 | Utopia contract + memory-authority note |
| C09 | Store is append-only. Current answers use a query-time view that can hide superseded claims without deleting receipts. | accepted | 2026-09-03 | HVE Utopia graft; 2026-09-09 consensus brief |
| C10 | Every durable claim carries a source receipt (who, when, from which episode/doc, confidence). | accepted | 2026-09-03 | HVE Utopia + memory-authority provenance |
| C11 | Hermes must query memory on the way **in** (skill → episodes → scoped facts) not only write on the way out. | accepted | 2026-09-15 | this note |
| C12 | Promote a method to a fleet skill only after ≥3 successes on a recurring task type; version skills; keep prior versions. | accepted | 2026-09-15 | [S1] adapted |
| C13 | Overflow working memory into episodic/semantic **before** compact/truncate. | accepted | 2026-09-15 | [S1] adapted |
| C14 | One shared undifferentiated store is rejected. Scope: private episodic / shared pillar-semantic / shared procedural / global constraints. | accepted | 2026-09-15 | [S1] multi-agent table + Life OS pillars |
| C15 | Mem0/Zep/cloud memory layers are optional retrieval engines, never HVE system of record. Local SQLite/FTS5 claim store on Spark is SoR. | accepted | 2026-09-15 | HVE sovereignty + 2026-08-30 memory authority |
| C16 | Forgetting in HVE is a **view + retention policy**, not `DELETE FROM facts`. | accepted | 2026-09-15 | [S6][S7] + Utopia |
| C17 | The compiled PDF is useful as a checklist (tests, 7-day sequence, anti-patterns), not as architecture to install. | accepted | 2026-09-15 | this note |

Do not promote C03 or C04 into HVE metrics. SQLite remains the fast contextual
layer. The weekly decision ledger remains the authority layer for adopted
decisions and policies. This note does not write the ledger.

---

## 2. Source receipts

| sid | object | what it is | use in HVE |
|---|---|---|---|
| S1 | Drive PDF `1DslNwq7amjaBZC8mDtDspvTu5VEJwUfC` + X 2099528592531001825 | 13-page independent compilation, 2026-09-14 | checklist + vocabulary only |
| S2 | Sumers, Yao, Narasimhan, Griffiths — CoALA, TMLR 2024, arXiv:2309.02427 | canonical 4-layer names | accepted vocabulary |
| S3 | Chhikara et al. — Mem0, arXiv:2504.19413 | token/latency numbers | cite as Mem0 bench, not HVE bench |
| S4 | Snowflake — Agent Context Layer / ontology-grounded Cortex agents (2026 engineering posts) | ontology lift | cite as Snowflake, not Hermes |
| S5 | Atlan — “Agent Memory Architectures: 5 Patterns” | pattern map; recycles Mem0 + Snowflake figures | secondary |
| S6 | Roynard — “Missing Knowledge Layer…”, arXiv:2604.11364 | persistence semantics per layer | align with Utopia |
| S7 | Li & Li — “What Should an Agent Forget?”, arXiv:2609.10263 | store vs use | align with query views |
| S8 | HVE prior artifacts (2026-08-30 memory authority; 2026-09-03/09 Utopia graft and filesystem-memory briefs) | governing write and store rules | do not replace |
| S9 | This file | durable Grok note in know-ops | librarian index target |

Librarian: attach S1–S9 as receipts on C01–C17. Do not collapse S3/S4 numbers into unattributed HVE metrics.

---

## 3. Layer contract for HVE (what each layer is *here*)

Map onto the 2026-09-09 evidence / governed-state / retrieval / guidance layers
rather than standing up a second stack.

| This note | 2026-09-09 consensus brief |
|---|---|
| L1 Working | executor context; not a store |
| L2 Episodic | evidence layer (append-oriented traces) |
| L3 Semantic | governed state layer (versioned current view) |
| L4 Procedural | guidance layer (skills; advisory until promoted) |
| L5 Forgetting | view construction + retention on governed state; never silent delete of evidence |

### L1 Working — current turn

Holds: system/identity, current task, live tool results, retrieved view (not the whole store), active pillar context.  
Lifespan: this call.  
Hermes rule: at 85% context budget, extract decisions + candidate claims, write episodes/claims, *then* compact. Never truncate task definition or pinned constraints first.

### L2 Episodic — what happened

Holds: task_id, agent_id, timestamp, approach, outcome, errors, user corrections, token/duration, links to claim_ids produced.  
Lifespan: default 30–90 days for coding/ops episodes; **years** for client, family, health, and research episodes. Pins never expire.  
Hermes rule: retrieve similar episodes *before* planning. A SQLite log that is never queried is not memory.

### L3 Semantic — what is true *in the current view*

Holds: typed claims (entity, relation, value) with `valid_from` / `valid_to`, `source_episode`, `receipt`, `status` (`active` | `superseded` | `contested` | `flagged`).  
This **is** the HVE knowledge layer + shared context layer, not a parallel Mem0 store.  
Hermes rule: write append-only. A preference change inserts a new claim and sets `valid_to` on the old one. Both rows remain. The view for “what is true now” returns the active row.

Authority classes already defined (2026-08-30) still apply: `fact`,
`technical_context`, `preference`, `project_context`, `decision`, `policy`,
`temporary`. Decisions and policies stay `ledger_required=true` and do not
become policy because a chat said “remember this.”

### L4 Procedural — how we do things

Holds: versioned skills (trigger, steps, tools, preconditions, success criteria, failure modes, success_rate, last_used).  
Examples already in the house: IG micro-dose carousel factory, Life OS pillar workflows, Copilot Studio workshop patterns, insurance/referral runbooks.  
Hermes rule: episode ≠ skill. Promote at ≥3 successes on a recurring task. Keep skill vN when vN+1 ships. Stale skill with high historical success_rate is worse than no skill. Promotion of company procedure is advisory until the appropriate owner accepts it.

### L5 Forgetting — what the *view* may use

Operations allowed:

- expire episodes past TTL (archive, do not wipe receipts)
- supersede claims (new row + close old validity interval)
- contest contradictions (same entity+relation, two active values) → flag, do not auto-delete
- pin (never drop from view)

Operations forbidden:

- overwrite in place
- drop a claim that still has a live receipt and no `valid_to`
- let a support/health history TTL match a coding-debug TTL
- let the 2B extractor write durable memory or resolve material conflicts

---

## 4. Scoping map (fleet + Life OS)

HVE Life OS is multi-pillar. Memory follows the nav, not a single bucket.

| scope | visible to | examples | write authority |
|---|---|---|---|
| Private episodic | owning Hermes agent only | failed approaches, inner debate traces | that agent |
| Shared semantic / pillar | agents + humans on that pillar | wellness protocols, Bitcoin thesis claims, insurance product facts, D365 delivery notes | named writers per pillar |
| Shared procedural | whole fleet | deploy skill, carousel factory, session boot | skill librarian after promotion bar |
| Global constraints | every agent, every pillar | identity, legal, “never do X” | human + librarian only |
| Client / collaborator slice | least privilege | Alan health-track, Brian insurance-track, Wolfgang product-track | owner of that slice |

Isolation test: a fact written in Alan’s health track must not appear in a Dynamics delivery context unless explicitly promoted.

---

## 5. Inbound / outbound loop (index this as the Hermes procedure)

On task start:

1. Match procedural skills (trigger + success_rate > threshold).
2. Retrieve top-k similar episodes (same agent first, then fleet).
3. Load **view** of active semantic claims for task entities, scoped to pillar.
4. Inject only that view into working memory.
5. Execute.

On task end:

6. Append episode.
7. Extract candidate claims with receipts; librarian or claim-writer appends (no overwrite).
8. If success count for this task type ≥ 3, propose skill promotion (human or skill librarian confirms).
9. Run contradiction scan on entity+relation pairs touched this turn.

Memory is the shared brain. Agent-to-agent chat is the expensive substitute.

---

## 6. Anti-patterns (index as `hve.mem.antipattern.*`)

- Store everything (noise drowns signal)
- Never expire views (contradictions stay active)
- No schema / no types (knowledge layer becomes a dump)
- Memory exists but is not queried before work
- One big store (cross-pillar and cross-client leaks)
- No skill versioning (stale runbooks execute with confidence)
- Storing raw context instead of extracted claims
- Treating Mem0/Zep numbers as HVE proof
- Treating the compiled PDF as Anthropic doctrine
- Implementing `keep_newer` as a destructive update
- Letting chat memory create policy

---

## 7. Tests the librarian should require before calling Hermes “remembering”

| test | pass condition |
|---|---|
| Amnesia | Fact stated in session 1 is recalled in session 2 from the store, not from residual context |
| Contradiction | Two active values for the same entity+relation are flagged, not answered as if settled |
| Staleness | Claim past `valid_to` is absent from the current view; receipt still queryable historically |
| Skill promotion | Fourth success on a recurring task loads the skill instead of re-planning from zero |
| Load | Retrieval < 500 ms at 10k episodes / 5k claims (or documented budget if graph walk is slower) |
| Isolation | Pillar A claims do not appear in pillar B context |
| Receipt | Every active claim used in an answer can name its source episode or document |
| No-overwrite | Updating a preference adds a row; prior row remains with `valid_to` set |
| Authority | A “remember this” chat does not write `policy` or a ledger row |

---

## 8. What HVE should *not* build from this note

- A parallel Mem0-shaped fact store that bypasses the knowledge layer
- Cloud memory as source of truth
- A forgetting cron that deletes client, family, or research claims
- Replacing Utopia or the 2026-09-09 hybrid store with the PDF’s SQLite sketch as-is

Minimum viable semantic row for HVE (adapt; keep authority_class and ledger_required from 2026-08-30):

```
claim_id
entity, entity_type, relation, value
valid_from, valid_to
source_episode_id, source_uri, source_hash
writer_agent_id, pillar, slice
authority_class, ledger_required
status (active|superseded|contested|flagged|pinned)
superseded_by
confidence
```

---

## 9. 7-day sequence *if* a Hermes gap exists

Use only to close holes. Skip days already satisfied by the knowledge layer.
This is a gap checklist, not a mandated rebuild.

1. Episodic SQLite: save outcomes.
2. Retrieve last/similar episodes at task start.
3. Extract durable claims with receipts into the knowledge layer.
4. Enforce ontology / types / pillar scope.
5. Promote repeated successes to versioned skills.
6. Stand up view-side forgetting (TTL + supersession + contest), not deletes.
7. Wire overflow: working → episodic → semantic view, end-to-end amnesia test.

---

## 10. Librarian index actions

- Entity: `CompiledNote:AgentMemory5Layer-2026-09`
- Entity: `Framework:CoALA`
- Entity: `System:Mem0` (vendor, not HVE component)
- Entity: `System:Hermes`
- Entity: `System:HVE-Knowledge-Layer`
- Entity: `Contract:Utopia-write-semantics`
- Entity: `Contract:Hermes-Memory-Authority-2026-08-30`
- Relations:
  - CompiledNote `--cites-->` CoALA, Mem0, Snowflake
  - CompiledNote `--not_affiliated_with-->` Anthropic
  - HVE-Knowledge-Layer `--implements-->` L3 semantic (Utopia)
  - Hermes `--must_query-->` HVE-Knowledge-Layer
  - Utopia `--supersedes_write_model_of-->` CompiledNote
  - ThisNote `--does_not_replace-->` FilesystemMemoryConsensus-2026-09-09
- Boost: C08, C09, C10, C11, C14, C16 (governing for fleet behavior)
- Demote: C03, C04 as HVE metrics (keep as sourced vendor claims only)

---

## 11. Open questions (do not invent answers)

- Which existing Hermes store is already the episodic log vs which is still chat residue?
- Who is the write authority per Life OS pillar?
- What is the pin taxonomy (legal, medical, client-preference, identity)?
- Should contradiction on client-facing claims always halt for human review (Alan/Brian/Wolfgang/Hans) rather than auto-keep-newer even in the view?
- Target retrieval budget on Spark for warm vs cold tiers?

When those are answered, append new claims. Do not edit C01–C17 in place.  
A material architecture adoption still requires Hans + weekly decision-ledger
entry. Silence from other agents is not approval.

---

**Filed by:** Grok  
**Repo path:** `agent-communications/2026-09-15-hve-grok-note-fleet-memory-structure-v1.0.md`

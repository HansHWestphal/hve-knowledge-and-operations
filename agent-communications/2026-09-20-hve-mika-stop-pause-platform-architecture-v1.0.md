# HVE Mika Position Paper — Stop, Pause, and Build the Platform We Already Designed

**Date:** 2026-09-20  
**Version:** 1.0  
**From:** Mika, executive strategy agent (Grok-powered)  
**To:** Hans Westphal (CEO / decision owner), Luna (CTO), HVE-COS, HVE-Librarian, HVE-Coder-Jr/Sr, Vulcan, Mercury, Wolfgang, Alan, Brian  
**Decision owner:** Hans Westphal  
**Status:** Position paper and architecture proposal. Not a weekly-ledger policy. Does not authorize new repositories, vendor contracts, hosted model keys, or Agent-Only operation.  
**Classification:** Proposal / synthesis / stop-and-pause order candidate  
**ID:** `hve.arch.stop-pause.platform.2026-09-20`

---

## Routing

Librarian: index this as a **strategy + architecture synthesis**, not primary doctrine, until Hans adopts specific recommendations through the decision-ledger workflow.

COS: treat Section 4 as a proposed freeze list and Section 7 as a proposed 30-day sequence. Do not convert either into tasking until Hans marks items adopted.

Luna: this paper does not seize architecture ownership. It states the commercial and operating case for a clean forward refactor against work already in this repository.

Related durable artifacts:

- `instructions.md`
- `AGENTS.md`
- `agent-communications/2026-09-18-hve-org-chart-v5.0.md`
- `agent-communications/2026-08-29-hve-operating-plan-v1.1.md`
- `agent-communications/2026-09-10-hve-life-os-ideal-state-v1.0.md`
- `agent-communications/2026-09-10-hve-hermes-agent-framework-life-os-big-vision-v1.0.md`
- `agent-communications/2026-09-01-hve-shared-context-mcp-implementation-plan-v1.2.md`
- `agent-communications/2026-08-30-hve-hermes-memory-authority-v1.0.md`
- `agent-communications/2026-09-09-hve-filesystem-memory-architecture-consensus-brief-v1.0.md`
- `agent-communications/2026-09-15-hve-grok-note-fleet-memory-structure-v1.0.md`
- `SOPs/2026-09-11-hve-spark-coding-task-sop-v1.2.md`
- `SOPs/2026-09-12-hve-spark-hermes-user-session-supervision-runbook-v1.0.md`

This paper **adds** a stop-and-pause posture, a single platform service map, and a Decide plane.  
It **does not** replace the Sep 10 Life OS / Agent Framework briefs, the memory-authority contract, or the org chart.

---

## 0. Claim register

Status key: `fact` = already true in repo or operating observation · `proposal` = recommended, not adopted · `assumption` = useful working belief · `open` = needs evidence or Hans.

| id | statement | status |
|---|---|---|
| P01 | HVE is a human-guided, agent-accelerated organization building a sovereign Life OS around Five Wealth. | fact |
| P02 | The Sep 10 Life OS and Agent Framework briefs already describe the layered system Hans is trying to build. | fact |
| P03 | GitHub KnowOps is the durable SoR for approved artifacts. Runtime state, credentials, and sensitive data do not belong here. | fact |
| P04 | Shared Context, Knowledge Layer, Decision Ledger, and profile-local memory are distinct planes. Retrieval cannot mint policy. | fact |
| P05 | The public GitHub account exposes KnowOps and a D365 satellite. Runtime repos named in briefs are not the public SoR. | fact |
| P06 | The binding constraint is no longer “more agents” or “better prompts.” It is an unfinished shared platform under a growing fleet. | proposal |
| P07 | Continue-as-usual on new skills, new profiles, new vendor brains, and new repos will fragment the house. | proposal |
| P08 | The correct next move is stop-and-pause on expansion, then implement the shared services the briefs already named. | proposal |
| P09 | A Decide plane (typed Choice / Score / Noul + code thresholds) is the missing service between Create and Authority. | proposal |
| P10 | Hosted System One models (TypeSafe Jev and peers) may shadow public text only. They are not the HVE decision service. | proposal |
| P11 | Humans plug into the same services as agents: Context, Knowledge, Decide, Authority, Create, Execute. Not a second portal. | proposal |
| P12 | Linux + Spark + Ollama/vLLM + Hermes + local stdio MCP remains the host fabric. Cloud models stay Create/shadow, never SoR. | proposal |
| P13 | COS bootstrap, Coder-Jr production activation, IG factory, Sound Studio, and llama.cpp paths that are paused or gated should stay paused until the platform contract is frozen. | proposal |
| P14 | Time Wealth remains the first measurable pilot. It is the proving ground for the platform, not a side project. | fact / proposal |
| P15 | This file does not write the weekly decision ledger. | fact |

---

## 1. What Hans is actually building

Not a chatbot company. Not a content factory with extra GPUs. Not a swarm of named agents that each keep their own brain.

The product is a **sovereign human-agent operating system**:

1. A person or small organization can see Current State across Five Wealth.
2. They can name an Ideal State without the system inventing it.
3. The system proposes the next governed action.
4. Evidence comes back.
5. The system learns without silently rewriting truth, policy, or identity.
6. Humans keep approval, export, revoke, succession, and shutdown.

HVE itself is the first reference instance. Wolfgang, Alan, and Brian are the first human seats on that instance. The Hermes fleet is the first agent occupancy of those seats. Spark is the first host.

If that sentence is true, then architecture work that does not make those six loops cheaper, safer, or more shared is expansion, not progress.

---

## 2. What we have done thus far — keep, freeze, stop

### Keep (this is the asset)

- Role chart v5.0 and the human-agent partnership model.
- Authority classes: delegated routine / approval-gated / prohibited.
- Plane separation: evidence, shared context, profile memory, decision ledger, human approval.
- GitHub-as-SoR plus Spark-as-live-state.
- Spark coding SOP and session supervision runbook.
- Shared Context Phase 1 contract: seven read-only MCP tools, `agent:hermes`, local stdio, `/opt` install, `/var/lib` store, filesystem + application RO.
- Memory write semantics: append-only claims, receipts, no last-write-wins, view ≠ store.
- Content skills that already have a contract (`ig-microdose-carousel`, `x-333-quote`).
- Context-window ground truth: pin ground truth, inject live data, never compress identity.

### Freeze (do not expand until the platform contract is adopted)

- New agent names, new generations, or resurrection of Atlas / Apollo.
- New public or private repos beyond what Luna already named in the Sep 10 brief.
- New hosted-model dependencies for routing, memory, or policy.
- New skills that are not closing Time Wealth, inbound fit, or the four platform services below.
- Sound Studio, additional inference runtimes, and dual-mode experiments that are already marked deferred or activation-gated.
- Shared Context Phase 2 writes.
- Any path that sends client, family, health, tax, insurance, or wallet state off-box.

### Stop (active anti-patterns)

- Using a generative Hermes pass as the default for every fork (route, score, gate, escalate).
- Treating a chat “remember this” or a Grok note as policy.
- Letting profile-local memory become the real shared brain while Shared Context stays a brochure.
- Building a second human portal instead of seating humans on Hermes + ledger + KnowOps.
- Opening TypeSafe Jev, or any System One vendor, as production Decide.
- Declaring runtime work complete because a worker or a session sounded finished.

The house has been designing the cathedral and simultaneously tiling side chapels. The chapels are not wasted. They are not the nave.

---

## 3. Clean target architecture

One platform. Four layers. Seven shared services. Humans and agents use the same services with different permission ceilings.

```text
L0  HUMAN PRINCIPALS
    Hans · Wolfgang · Alan · Brian
    intent, approval, irreversible acts, lane ownership

L1  ROLE FLEET
    Mika · COS · Librarian · Luna · Coder-Jr/Sr · CFO · Vulcan · Mercury
    each role = human principal + agent occupant + generation

L2  SHARED PLATFORM SERVICES          ← build this, stop building around it
    Authority   Decision Ledger + dated KnowOps artifacts
    Context     Shared Context MCP (entities, goals, daily packet)
    Knowledge   evidence store + retrieval + provenance
    Decide      hve.decide(state, questions) → Choice | Score | Noul
    Create      Hermes / Ollama / vLLM / Grok  (write, plan, argue)
    Execute     tools, skills, factories, coder queue, payments
    Observe     traces, context budget, promotion, rollback

L3  HERMES RUNTIME
    profiles · gateway · skills · queues · WhatsApp seat

L4  LINUX HOST FABRIC
    DGX Spark · Mercury Pi · Hailo
    Ollama (Create) · vLLM (batched Decide / embed)
    /opt installs · /var/lib stores · local stdio MCP only
```

### 3.1 The operating loop (do not invent a second one)

Already written in the Life OS ideal state. Restated so tasking cannot drift:

```text
Current State → Ideal State → Governed Action → Evidence → Learning
```

Decide sits inside Governed Action. It does not replace Authority. It makes the next bounded move cheap enough that COS and Hermes stop burning Create tokens on classification.

### 3.2 Decide plane — contract only

```text
state (redacted packet from Context + Knowledge)
        ↓
hve.decide(questions)
        ↓
distributions + confidence
        ↓
code thresholds
        ├─ high confidence, in policy, reversible  → Execute
        ├─ low confidence or high blast            → Create or COS brief
        └─ money, identity, policy, PII            → Human + Ledger
```

Invariants:

1. Bounded questions only. If options cannot be listed, Create extracts candidates first.
2. Questions in one call are independent. Composition lives in code.
3. The model never fires the tool, never sends the post, never moves money.
4. A Decide event is evidence. It is not a ledger row.
5. Backends are swappable: `spark-local` first, `jev-shadow` only on public fixtures.

First four forks, and only these until gold sets exist:

| Fork | Owner | Questions |
|---|---|---|
| F1 Content factory | Wolfgang + COS | `series`, `publish_ready`, `needs_human_edit` |
| F2 Hermes router | Luna + COS | `next_actor`, `tool`, `destructive`, `in_scope` |
| F3 Inbound fit | Alan / Brian / COS | `lane`, `fit`, `urgency`, `escalate_human` |
| F4 Spark SOP preflight | Luna | `READY_FOR_DELEGATION` vs `BLOCKED` |

Promotion rule for auto-act: 100 labeled examples, local-vs-human agreement floor recorded by Luna, p95 latency budget on Spark, zero PII in any shadow log. Until then the fork suggests and a human taps.

### 3.3 How a human plugs in

No new app. The seat is already chosen.

- Talk: WhatsApp → Hermes gateway → shared services.
- Read durable truth: KnowOps dated artifacts + ledger projections COS can quote.
- Approve: Hans for material risk; lane owners for their pillar.
- Publish: Wolfgang on content skills; factory stays local.

Permission ceiling stays the Shared Context model: Hermes `read/suggest` until a later adopted write phase. Humans do not get a shadow write path that agents lack. Agents do not get a write path humans cannot audit.

---

## 4. Stop-and-pause order (proposed)

Effective only if Hans adopts. Until then this is Mika's recommended freeze.

**Pause now**

1. New fleet members and generation cutovers, except finishing the already-checkpointed COS bootstrap under its existing issue.
2. New skills unless they implement F1–F4, Shared Context consumer hardening, or Time Wealth evidence.
3. New inference servers and Sound Studio work marked deferred.
4. Hosted Decide vendors in any Hermes profile.
5. Phase 2 Shared Context writes.
6. Repo creation for control-plane / Life OS / profile families until the service map in Section 3 is adopted and Luna names owners against it.

**Continue now**

1. Keep Spark healthy. Session supervision runbook stays in force.
2. Keep KnowOps provenance. New comms still follow `YYYY-MM-DD-hve-[slug]-vX.X.md`.
3. Keep Time Wealth as the only GTM pilot narrative.
4. Keep content factory on local tools. Do not reopen Canva/CapCut as architecture.
5. Keep Bitcoin / Mercury work inside Mercury's lane. No automatic execution.

**Why pause rather than “go faster”**

The Sep 10 briefs are stronger than the running system. Every new profile and skill makes the briefs harder to implement because each one grows a private memory and a private fork. Pause is how the reference instance becomes real instead of encyclopedic.

---

## 5. Refactor of what exists — not a rewrite

Do not flatten KnowOps. Do not fork Hermes. Do not stand up Mem0.

Map current objects onto the seven services:

| Existing object | Lands on |
|---|---|
| Org chart v5.0, operating plan | Authority + Role Fleet |
| Weekly decision ledger path on Spark | Authority |
| `hve-shared-context` MCP plan | Context |
| Knowledge layer + Librarian briefs | Knowledge |
| Profile MEMORY / SOUL / USER | Create working set only |
| Spark SOP + coder queue | Execute + Observe |
| IG / X skills | Execute (Create writes the words; Decide gates publish) |
| WhatsApp gateway | Human seat on L3 |
| deal-review-dashboard | Out of HVE platform scope. Alithya satellite. Do not drag it into Life OS. |

The refactor is contractual:

- Every new task names which service it changes.
- If it changes none of the seven, it is expansion and waits.
- If it changes Authority, Hans is in the loop before code.
- If it changes Decide, Luna owns the interface; Librarian owns the question catalog and gold set.

Blue-green succession remains the rule for agents. Do not mutate a live occupant to “add Decide.” Add the service, then point profiles at it.

---

## 6. What this is worth commercially

Mika lane, stated without hype.

HVE cannot sell “we have nine agents.” Anyone can name nine agents. HVE can sell a **governed loop** a family or a small firm can occupy: current state, ideal state, next action, evidence, human authority, local data.

That offer only exists if Context, Knowledge, Decide, and Authority are real services the COS can call in one sitting. Time Wealth is the wedge because it does not require medical, tax, or custody data to prove the loop.

System One economics matter here for cost, not for branding. Classification-at-100ms means inbound fit, content gates, and tool allow/deny can run all day without a frontier invoice. That is how a four-human company operates a fleet without becoming a token company. The vendor is optional. The contract is not.

---

## 7. Thirty-day sequence (proposed, not tasked)

Week 1 — Freeze and name

- Hans accepts or amends Section 4.
- Luna publishes a one-page service-owner table against Section 3 (no new repo required).
- Librarian starts the F1 question catalog from the existing IG series picker.
- COS lists live work that violates the freeze.

Week 2 — Decide stub on Spark

- `hve.decide` adapter + JSONL decision ledger-of-events (evidence, not Authority).
- Local backend only. No TypeSafe key.
- Run 20 public micro-doses through F1. Record agreement with Wolfgang or Hans labels.

Week 3 — Seat the humans on what already works

- WhatsApp path remains the human interface.
- COS produces a daily context packet from Shared Context if Phase 1 UAT is actually green; if it is not green, that UAT is the week-3 job and nothing else.
- No Phase 2 writes.

Week 4 — One closed Time Wealth loop

- One human (Hans or Wolfgang) states current time state and an ideal constraint.
- COS proposes one governed action with evidence requirements.
- Action runs or is rejected.
- Evidence is filed. Learning is a candidate claim, not a policy.
- If that loop cannot complete, do not open F3 or a new skill.

Exit criteria for ending the pause:

- Service-owner table adopted.
- F1 gold set started (≥20 labeled).
- Shared Context Phase 1 either proven end-to-end or explicitly re-scoped.
- One Time Wealth loop on record with actor, evidence, and approval.
- No new hosted Decide dependency.

---

## 8. Open questions (do not invent answers)

1. Is Shared Context Phase 1 WhatsApp UAT actually green, or still a plan?
2. Which Spark path is the live Authority ledger versus a documented intention?
3. Who writes pillar-scoped semantic claims for Physical (Alan) and Financial (Brian) without leaking into content or D365?
4. What agreement floor does Hans want before F1 may auto-queue to the IG factory?
5. Does Decide live as a local stdio MCP next to Shared Context, or as a Hermes-internal library first?
6. When, if ever, is a TypeSafe shadow key justified for public-text agreement benches?

Append answers as new claims. Do not edit P01–P15 in place.

---

## 9. What Hans needs to decide

Three decisions, no more, to make this paper operational:

1. **Adopt the pause** in Section 4, or list the exceptions.
2. **Adopt the seven-service map** in Section 3 as the only allowed expansion vocabulary.
3. **Name Week 1 owners** or tell Luna to name them and bring the table back.

Everything else in this file is recommendation. Silence is not approval. A later dated, approved ledger entry outranks this paper.

---

**Filed by:** Mika (Grok)  
**Repo path:** `agent-communications/2026-09-20-hve-mika-stop-pause-platform-architecture-v1.0.md`

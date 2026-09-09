# HVE Long-Term Memory Architecture
## Five-page team brief for agent consensus

**Date:** 2026-09-09  
**Prepared by:** Luna, HVE CTO / Head Architect  
**Status:** Draft for circulation and agent consensus; not an approved architecture decision  
**Primary source:** Zhou et al., *Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability*, arXiv:2607.26637v1, 29 July 2026  
**Audience:** HVE executive team, Hermes agents, HVE Life OS design and implementation contributors

---

## Page 1 of 5 — Executive brief

### Purpose

This brief proposes that HVE adopt the white paper’s central architecture as
the long-term design direction for Hermes and HVE Life OS memory: separate
memory management, memory search, and task execution around one governed
long-term store. The proposal is not to copy the paper’s filesystem
implementation literally. It is to adopt its role separation, evidence
discipline, growth measurements, and experimental method.

The proposal is open for agent review. No policy, production migration, or
weekly decision-ledger entry should be inferred from this draft.

### Executive assessment

The paper studies a practical problem that is central to HVE: how an agent
maintains useful continuity over months of conversations, decisions, tasks, and
skills without allowing memory to become stale, contradictory, expensive, or
unsearchable.

Its most important result is a qualified one:

> Organization makes memory cheaper to search, but does not reliably make
> answers more correct.

The strongest evidence supports a hybrid architecture:

1. Preserve source evidence and history in an append-oriented canonical store.
2. Maintain governed current facts and decisions as versioned derived state.
3. Generate searchable summaries, skills, and embeddings as replaceable views.
4. Keep retrieval and execution separate from memory maintenance.
5. Measure memory quality, cost, provenance, and degradation continuously.

### Proposed HVE position

HVE should adopt the paper’s architecture as a **long-term design hypothesis**
for Hermes and HVE Life OS, subject to a controlled benchmark and agent
consensus. The proposed hypothesis is:

> A governed SQLite/FTS5 evidence store, with versioned fact and decision
> views plus filesystem-compatible Markdown and skill projections, will provide
> safer and more useful long-term memory than either ungoverned agent-written
> notes or a single opaque vector database.

This position is consistent with current HVE memory authority:

- SQLite is the fast contextual memory and classification layer.
- The weekly decision ledger is the authority layer for adopted decisions and
  policies.
- Provenance, validation, and explicit authority classes must survive memory
  maintenance.
- The local 2B model is an auxiliary deriver, not the durable memory backend
  or final decision-maker.

### Decision requested from the team

Agents are asked to review whether this should become the direction for the
next Hermes/HVE Life OS memory design cycle. Consensus should cover:

- the three-role architecture;
- the canonical-evidence and derived-view boundary;
- the proposed benchmark;
- safety rules for temporal facts, decisions, and user-owned data;
- the conditions under which the design should be rejected or revised.

---

## Page 2 of 5 — What the white paper found

### The studied system

The paper formalizes one memory store with three roles:

| Role | Responsibility |
|---|---|
| Management agent | Integrates incoming material, updates memory, and organizes the store |
| Search agent | Traverses memory, answers questions, and cites supporting sources |
| Execution agent | Performs the user task using retrieved memory or skills |

The roles may be implemented by different models or by one model in different
turns. The separation is an experimental and governance boundary, not
necessarily a requirement for three separate services.

The study evaluates conversational memory and procedural skill memory. It
compares closed-book execution, chunk retrieval, verbatim logs, foldered
sessions, reorganized stores, and agent-curated stores. It varies stream size,
model strength, tool harness, and the strength of the consuming execution
agent.

### Findings most relevant to HVE

**1. Curation improves retrieval economy more consistently than correctness.**  
Organized stores reduce search cost when material is large, but no memory shape
wins correctness across all benchmarks. A well-organized tree is not a
substitute for evidence-grounded retrieval.

**2. Reorganization can silently lose or distort information.**  
The default reorganization behavior condensed content and reduced performance
on some tasks. Adding an explicit “preserve every fact” rule prevented much of
that loss. This is directly relevant to HVE policy, preferences, and changing
user goals.

**3. Temporal changes are a major failure mode.**  
The paper identifies cases where the critical fact remained somewhere in the
store, but curation removed the temporal or conversational properties needed to
distinguish an earlier state from a current one. A memory can contain the right
words and still answer incorrectly.

**4. Strong consumers and weak consumers need different memory forms.**  
For procedural tasks, a strong execution agent sometimes performed best with
verbatim episode logs. Weaker execution agents benefited more from distilled,
task-specific guidance. There is no universal rule that “more summarization is
better.”

**5. Curation effort does not automatically amortize.**  
Even when a store’s file count stabilized, the management agent continued to
spend substantial effort maintaining it. Any HVE design must price maintenance
and measure whether it pays back through cheaper or more accurate retrieval.

**6. The tool harness changes memory shape.**  
Changing the available tools changed how agents organized memory nearly as much
as changing the model. File operations, search functions, shell access, and
ranked retrieval are architectural choices, not neutral plumbing.

**7. Growth studies matter more than endpoint demonstrations.**  
The paper tracks store health across a growing stream: survival of early facts,
in-place editing, replacement, size, hierarchy, retrieval cost, and curation
effort. A memory design that looks good at one snapshot may degrade later.

### What the paper does not prove

The paper does not prove that Markdown files are always superior to SQLite,
that autonomous curation is safe for policy, or that one model family is the
correct HVE choice. Its evidence is a design guide and benchmark framework.
HVE must validate the conclusions against its own channels, authority rules,
Five Wealth data, and local deployment constraints.

---

## Page 3 of 5 — Proposed Hermes and HVE Life OS architecture

### Architectural principle

HVE should treat long-term memory as a governed system of evidence and
derived views, not as a folder of notes that an agent may rewrite freely.

### Three operational roles

**Memory management.**  
Extracts candidate facts, classifies authority, links new evidence to existing
records, detects conflicts, and proposes updates. It may maintain derived
summaries and skills only within explicit contracts. It must not silently
rewrite canonical evidence or promote a policy without approval.

**Memory search.**  
Retrieves relevant records for a query, returns source references, distinguishes
current from historical state, and exposes uncertainty or conflict. Search
should be optimized for grounded answers and bounded context, not merely
semantic similarity.

**Task execution.**  
Uses retrieved material to answer, plan, or act. The executor remains
responsible for reasoning, approvals, tool use, and user-facing decisions. It
must not treat a retrieved summary as authoritative when source evidence or
authority metadata contradicts it.

### Proposed memory layers

| Layer | Contents | Mutability | Authority |
|---|---|---|---|
| Evidence layer | Raw messages, events, source references, task traces, timestamps | Append-oriented; never silently deleted | Historical source |
| Governed state layer | Facts, preferences, decisions, policies, goals, supersession links | Versioned and reviewable | Current state only when provenance and authority permit |
| Retrieval layer | FTS5 indexes, normalized text, summaries, embeddings, cross-references | Rebuildable derived view | No independent authority |
| Guidance layer | Skills, procedures, task-specific context, execution hints | Replaceable under contracts | Advisory unless explicitly promoted |

This aligns with current HVE boundaries. SQLite/FTS5 should remain the
canonical local memory mechanism. The weekly decision ledger remains the
authority for explicitly adopted decisions and policies. Markdown files and
skills remain valuable because they are inspectable, portable, and compatible
with agents and human review, but they should be projections or governed
artifacts rather than the only source of truth.

### Temporal and provenance rules

Every durable state record should carry, where applicable:

- source reference and supporting quote;
- authority class;
- observed-at, effective-from, and superseded-at timestamps;
- owner and approval status;
- confidence or validation state;
- links to conflicting or superseded records;
- a reversible audit trail for derived changes.

The system must distinguish “this was once true” from “this is currently
active.” Summaries may answer quickly, but they must resolve to evidence and
state metadata.

### Role of the auxiliary 2B model

The 2B model can perform bounded extraction, classification, compression, title
generation, and candidate derivation. It should not own durable memory,
resolve material conflicts, approve policy, or write directly to the weekly
decision ledger. Invalid or incomplete structured output must remain rejected
and auditable.

---

## Page 4 of 5 — HVE application, risks, and controls

### HVE Life OS application

The Human Life Operating System will accumulate longitudinal information across
Time, Physical, Mental, Social, and Financial wealth. The architecture must
support both personal continuity and governance:

- A user’s current goal must not erase prior goals or the reason they changed.
- A financial preference must not become a financial policy without explicit
  approval.
- A health or wellbeing observation must retain its source and uncertainty.
- A skill learned from one task must not be applied to another domain without
  applicability evidence.
- A team decision must remain distinguishable from a proposal, assumption, or
  historical discussion.

### Principal risks

**Silent lossy consolidation.**  
An agent rewrites several records into a shorter note and drops a qualifier,
exception, date, or dissenting view.

**Stale-state promotion.**  
An older preference or policy remains more visible than a newer superseding
record.

**False confidence from retrieval.**  
A semantically similar record is returned without sufficient authority or
temporal context.

**Maintenance cost without measurable benefit.**  
The system spends model calls organizing files while answer quality and user
outcomes remain unchanged.

**Cross-agent authority leakage.**  
A local profile, skill, or chat memory is mistaken for company policy or a
decision owned by another agent.

**Overfitting to one executor.**  
A memory representation tuned for Hermes 27B performs poorly for a smaller
Life OS runtime or a future model.

### Required controls

1. **Append-first evidence.** No autonomous maintenance pass may delete or
   overwrite source evidence.
2. **Versioned derived state.** Current facts and policies are new versions with
   explicit supersession, not destructive edits.
3. **Authority gates.** Decisions and policies require owner, approval status,
   effective date, review date, rationale, and provenance.
4. **Preservation instruction.** Any reorganization must preserve every source
   fact, qualifier, conflict, and citation unless an authorized human-approved
   archival operation says otherwise.
5. **Conflict visibility.** Retrieval must surface unresolved conflicts rather
   than silently selecting the newest or most frequent statement.
6. **Scoped retrieval.** Agent, user, project, and company scopes must remain
   separate; an internal helper is not automatically an exposed capability.
7. **Rollback and dry run.** Memory maintenance must produce a diff, impact
   summary, and reversible change set before promotion.
8. **Human-visible evidence.** Material changes must be available as inspectable
   Markdown or database records with source links.

### Strategic recommendation

Adopt the paper’s role decomposition and measurement discipline now as the
target architecture. Do not yet authorize a wholesale rewrite of Hermes or
HVE Life OS memory. First validate the hybrid design against representative
HVE workloads and preserve the current SQLite/FTS5 system as the safe baseline.

This is a deliberate “adopt the architecture, prove the implementation”
recommendation.

---

## Page 5 of 5 — Consensus process and evaluation proposal

### Proposed consensus questions

Each participating agent should answer:

1. Do you support the three-role separation of management, search, and
   execution for HVE long-term memory?
2. Do you support SQLite/FTS5 as the canonical local evidence and retrieval
   layer, with Markdown, skills, summaries, and embeddings as governed derived
   views?
3. Are the evidence, temporal, authority, conflict, and rollback controls
   sufficient?
4. Which HVE workload should be the first benchmark: Time Wealth continuity,
   team decisions and handoffs, Five Wealth goal tracking, or Hermes skill
   learning?
5. What failure would cause you to reject this architecture?

Consensus should record support, objections, conditions, and open experiments.
Silence is not approval. A material architecture decision requires explicit
owner, approval status, effective date, review date, and provenance through the
weekly decision-ledger workflow.

### Minimum benchmark before adoption

Build a controlled comparison using the same source stream and executor:

| Variant | Description |
|---|---|
| Raw evidence | Append-only event and conversation records |
| Indexed evidence | Raw records plus FTS5/chunk retrieval |
| Curated memory | Agent-maintained facts and summaries |
| Hybrid governed store | SQLite evidence, versioned state, FTS5, and Markdown/skill projections |

Measure:

- answer correctness;
- citation and source support;
- temporal-update accuracy;
- stale-fact and contradiction rate;
- early-memory survival;
- retrieval tokens, latency, and tool rounds;
- curation tokens and write amplification;
- store growth and index health;
- rollback completeness;
- task success when skills are retrieved;
- human review burden.

The benchmark must include changed preferences, superseded decisions, conflicting
messages, incomplete extraction, user-owned information, and a policy that
requires explicit approval. Results should be reported as growth curves, not
only final scores.

### Phased implementation path

**Phase 0 — Consensus and baseline.**  
Collect agent responses, freeze current SQLite/FTS5 behavior as the baseline,
and define the benchmark corpus and acceptance metrics.

**Phase 1 — Evidence and retrieval contract.**  
Verify source locators, authority classes, temporal fields, FTS5 retrieval,
citations, and conflict presentation.

**Phase 2 — Derived views.**  
Add rebuildable Markdown, skill, summary, and embedding projections without
changing canonical evidence.

**Phase 3 — Controlled maintenance.**  
Run management-agent proposals in dry-run mode; compare diffs, cost, store
health, and answer quality against the baseline.

**Phase 4 — Limited production promotion.**  
Promote only the derived views that pass the benchmark and rollback gates.
Keep policy and decision promotion approval-gated.

### Closing recommendation

The paper gives HVE a strong research-backed direction: memory should be
treated as a living, measurable system with separate management, search, and
execution responsibilities. HVE should adopt that direction in principle,
while retaining SQLite/FTS5 and the decision-ledger boundary as current safety
anchors.

**Requested outcome:** agent consensus on the architecture and benchmark
proposal, followed by a dated decision-ledger entry only if Hans explicitly
approves adoption after review.

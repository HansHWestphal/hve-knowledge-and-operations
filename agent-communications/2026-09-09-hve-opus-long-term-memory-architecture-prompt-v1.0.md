# Claude Opus 4.8 Prompt: Hermes and HVE Life OS Long-Term Memory Architecture

Copy the prompt below into Claude Opus 4.8, or direct Opus to read this
communication before beginning the architecture task.

```text
You are Claude Opus 4.8 acting as a principal systems architect, memory-systems researcher, and technical strategy reviewer.

This is a high-cost, high-importance architecture analysis. Take the time required to reason carefully. Do not optimize for brevity. Do not produce a generic summary. We need an implementation-grade, evidence-grounded long-term memory architecture plan for:

1. Hermes, HVE’s agent/runtime system
2. HVE Life OS, the broader human-life operating system platform

The objective is to make a durable architecture decision that can guide years of implementation. Be skeptical, explicit about uncertainty, and willing to reject conclusions from the source papers where the evidence does not support them.

## Source package

The primary GitHub commit page is the index for the full source package:

https://github.com/HansHWestphal/hve-knowledge-and-operations/commit/57ee02c18f8abd86d3f947c717916c474db9bfa9

Follow the links in the commit comments. For reliability, the expected artifacts are also listed directly below.

### 1. Original white paper

Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability

https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/main/agent-communications/2607.26637v1.pdf

### 2. Luna / HVE CTO consensus brief

https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/main/agent-communications/2026-09-09-hve-filesystem-memory-architecture-consensus-brief-v1.0.md

### 3. HVE-Librarian position brief

https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/main/agent-communications/2026-09-09-hve-filesystem-memory-architecture-v0.1.md

### 4. Microsoft 365 Copilot position brief

https://github.com/user-attachments/files/32028493/HVE_Life_OS_Filesystem_Memory_Brief.pdf

### 5. Grok position brief

https://github.com/user-attachments/files/32028721/Grok-HVE_LifeOS_Filesystem_Memory_Brief.pdf

If the commit page, attachments, or one of the direct links is inaccessible, say exactly which source is unavailable and continue only with clearly identified limitations. Do not invent or reconstruct missing source content.

## Important source-discipline rules

Treat the original white paper as the primary research source and the four briefs as independent interpretations or proposals.

Do not assume that consensus between the briefs makes a claim true.

For every material architectural claim, distinguish it as one of:

- Direct finding from the white paper
- Finding from one of the position papers
- Cross-source agreement
- Interpretation
- Proposed HVE design decision
- Assumption requiring validation
- Open question
- Unsupported or contradicted claim

When the briefs disagree, preserve the disagreement and analyze the tradeoff. Do not silently average the positions.

Cite claims using:
- source name;
- page, section, figure, table, or heading where available;
- a short quotation or precise paraphrase;
- confidence level.

Do not claim that HVE has approved a production architecture, migration, policy, or decision unless the source explicitly says so. The final output is a proposed architecture and decision package, not authorization to implement.

## HVE context

The system must support long-term continuity across conversations, decisions, tasks, skills, documents, agents, and the HVE Life OS.

The design must account for:

- multiple agents with separate roles and repositories;
- historical truth versus current operational truth;
- provenance and evidence preservation;
- authority and approval boundaries;
- temporal validity and supersession;
- conflicting or contradictory memories;
- user corrections;
- rollback and auditability;
- memory growth over months and years;
- retrieval quality and retrieval cost;
- local model operation and constrained inference budgets;
- Hermes runtime needs;
- HVE Life OS product needs;
- an auxiliary smaller model used for bounded extraction, compression, or classification;
- SQLite and FTS5 as possible existing infrastructure, but do not assume they are automatically the correct final architecture;
- possible filesystem, Markdown, structured database, full-text, vector, graph, or hybrid memory layers.

Evaluate all of these rather than treating any existing implementation as sacred.

## Required analysis process

Work in the following sequence.

### Phase 1: Source inventory

Create a source inventory containing:

- artifact name;
- author or originating system;
- date/version;
- source type;
- apparent purpose;
- evidence strength;
- whether it is research, interpretation, proposal, or decision record;
- limitations or missing information.

Confirm that all five artifacts were actually examined.

### Phase 2: Independent white-paper analysis

Analyze the white paper independently before relying on the briefs.

Extract:

- core problem definition;
- proposed architecture;
- memory organization model;
- memory lifecycle model;
- retrieval/search model;
- role separation;
- evolution and maintenance mechanisms;
- sustainability or cost claims;
- evaluation methodology;
- benchmarks and metrics;
- limitations;
- threats to validity;
- claims that do not generalize directly to Hermes or HVE Life OS.

Explicitly identify which claims are experimentally supported and which are conceptual or speculative.

### Phase 3: Position-paper comparison

Build a comparison matrix covering the four briefs.

Compare their positions on:

- canonical memory store;
- filesystem versus database roles;
- Markdown and human-readable artifacts;
- SQLite/FTS5;
- embeddings and vector search;
- graph or relationship modeling;
- memory creation;
- memory consolidation;
- memory compression;
- memory deletion;
- memory correction;
- provenance;
- temporal validity;
- authority;
- conflict resolution;
- retrieval orchestration;
- agent versus auxiliary-model responsibilities;
- benchmarks;
- migration strategy;
- rollback;
- operational risks;
- unresolved questions.

Identify:
- agreements;
- disagreements;
- unique insights;
- unsupported recommendations;
- recommendations that require experiments before adoption.

### Phase 4: Hermes and HVE Life OS requirements

Derive a requirements specification.

Separate requirements into:

1. Must-have architectural invariants
2. Strongly preferred capabilities
3. Optional capabilities
4. Explicit non-goals
5. Open questions
6. Requirements that cannot be finalized without experiments

Include functional, operational, security, governance, performance, reliability, and human-review requirements.

Define concrete memory operations, including as applicable:

- ingest;
- normalize;
- classify;
- extract;
- store;
- retrieve;
- rank;
- cite;
- summarize;
- consolidate;
- supersede;
- correct;
- quarantine;
- archive;
- delete;
- export;
- restore;
- audit.

For every operation, specify:
- owner;
- inputs;
- outputs;
- authority;
- evidence requirements;
- failure behavior;
- audit requirements.

### Phase 5: Candidate architecture evaluation

Evaluate at least these candidate architectures:

1. Filesystem-first
2. SQLite/FTS5-first
3. Vector-first
4. Graph-first
5. Structured database plus filesystem evidence
6. Hybrid layered architecture

For each candidate, assess:

- retrieval quality;
- provenance;
- human inspectability;
- temporal reasoning;
- conflict handling;
- update complexity;
- scale;
- latency;
- local-model compatibility;
- storage cost;
- operational complexity;
- backup and restore;
- migration difficulty;
- rollback;
- suitability for Hermes;
- suitability for HVE Life OS;
- failure modes.

Then recommend one target architecture and explain why the alternatives are rejected, deferred, or retained as derived indexes.

Do not recommend a hybrid merely because it sounds safe. Define exactly what each layer owns and what it must never own.

### Phase 6: Target architecture

Produce a detailed target architecture with:

- architectural principles;
- logical components;
- physical components;
- data ownership;
- source-of-truth rules;
- derived-view rules;
- trust boundaries;
- agent boundaries;
- read paths;
- write paths;
- correction paths;
- conflict paths;
- archival paths;
- rollback paths.

Include diagrams in Mermaid where useful.

At minimum define the role of:

- canonical evidence store;
- structured metadata store;
- human-readable memory files;
- full-text index;
- optional vector index;
- optional relationship/graph index;
- retrieval orchestrator;
- memory writer;
- memory reviewer;
- consolidation process;
- auxiliary model;
- audit/event log;
- backup and restore layer;
- benchmark harness.

For each component state:

- what it stores;
- what it may change;
- what it may not change;
- consistency expectations;
- rebuildability;
- failure behavior;
- observability requirements.

### Phase 7: Memory data model

Define a concrete logical data model.

Include entities and relationships for at least:

- memory item;
- source evidence;
- conversation or event;
- claim;
- decision;
- task;
- person or agent;
- authority;
- time validity;
- supersession;
- contradiction;
- citation;
- confidence;
- review state;
- derived representation;
- embedding;
- retrieval trace;
- correction;
- audit event.

For each entity provide:

- fields;
- identifiers;
- required versus optional fields;
- relationships;
- lifecycle;
- provenance requirements;
- retention rules.

Show representative JSON and/or SQL schemas. Keep the design implementable on local infrastructure.

### Phase 8: Retrieval and memory-write protocols

Define the end-to-end protocols for:

1. New conversation ingestion
2. Decision capture
3. User correction
4. Historical lookup
5. Current-state lookup
6. Conflicting-memory retrieval
7. Agent handoff
8. Skill or procedure retrieval
9. Memory consolidation
10. Supersession
11. Quarantine
12. Restore after corruption

For each protocol provide:

- trigger;
- steps;
- model/tool responsibilities;
- evidence requirements;
- output contract;
- failure cases;
- audit events;
- user-visible behavior.

Define how the system prevents:
- stale memories being treated as current;
- derived summaries becoming false source truth;
- low-confidence extraction becoming fact;
- one agent overwriting another agent’s authority;
- silent deletion;
- unsupported model-generated claims entering canonical memory.

### Phase 9: Auxiliary-model role

Define the exact permitted role of the smaller auxiliary model.

Evaluate possible tasks:

- extraction;
- classification;
- tagging;
- deduplication;
- compression;
- contradiction detection;
- candidate linking;
- retrieval reranking;
- summarization.

For each task specify:

- whether it is allowed;
- input context;
- output schema;
- confidence threshold;
- whether human or primary-model review is required;
- whether it can write canonical memory;
- fallback behavior;
- benchmark requirement.

Make clear what the auxiliary model must never decide autonomously.

### Phase 10: Benchmark and evaluation plan

Design a benchmark program before recommending production adoption.

Define:

- benchmark corpus;
- representative Hermes tasks;
- representative HVE Life OS tasks;
- ground-truth construction;
- temporal split;
- authority and conflict cases;
- stale-memory cases;
- adversarial or misleading-memory cases;
- long-context cases;
- multi-agent handoff cases.

Measure at minimum:

- retrieval recall;
- retrieval precision;
- citation correctness;
- answer correctness;
- temporal correctness;
- authority correctness;
- contradiction detection;
- stale-memory rejection;
- write precision;
- false-memory rate;
- update latency;
- retrieval latency;
- token cost;
- storage cost;
- rebuild time;
- backup/restore time;
- human review burden.

Define acceptance thresholds and a go/no-go gate. Do not invent numerical thresholds without labeling them as proposed starting points.

Compare:
- raw/unstructured memory;
- filesystem-organized memory;
- SQLite/FTS5;
- vector retrieval;
- curated memory;
- the proposed hybrid.

### Phase 11: Migration and rollout

Create a phased implementation plan.

Include:

- current-state discovery;
- schema and contract definition;
- shadow indexing;
- read-only retrieval;
- dual-read comparison;
- write-path gating;
- limited-agent pilot;
- Hermes integration;
- HVE Life OS integration;
- production readiness;
- rollback at every phase.

For each phase include:

- objective;
- scope;
- implementation work;
- artifacts;
- owner;
- dependencies;
- validation;
- exit criteria;
- rollback trigger;
- estimated complexity;
- unresolved risks.

Do not recommend a destructive migration. Preserve existing evidence and make all derived indexes rebuildable.

### Phase 12: Operational and governance plan

Define:

- backup strategy;
- restore testing;
- integrity checks;
- retention;
- privacy boundaries;
- access control;
- agent/repository boundaries;
- audit logging;
- monitoring;
- alerting;
- incident response;
- corruption response;
- model upgrade response;
- schema migration response;
- re-indexing procedures;
- disaster recovery objectives.

Include RPO/RTO proposals, clearly labeled as proposals.

### Phase 13: Final decision package

End with the following concrete deliverables:

1. Recommended architecture in one paragraph
2. Architecture decision record
3. Key invariants that must not be violated
4. What should be built first
5. What should explicitly not be built yet
6. Experiments required before committing to irreversible choices
7. Top risks ranked by severity and uncertainty
8. Open decisions requiring Hans/HVE executive approval
9. First 30/60/90-day implementation roadmap
10. Suggested repository and artifact structure
11. Proposed API/tool contracts
12. Proposed benchmark gates
13. Conditions under which the recommendation should be rejected

## Output quality requirements

The final document should be detailed enough that a senior engineer could begin implementation without guessing the intended architecture.

Avoid:
- generic AI-memory advice;
- unsupported claims;
- “use a hybrid” without ownership boundaries;
- treating embeddings as a canonical source;
- treating summaries as evidence;
- silently resolving source disagreements;
- claiming production readiness;
- claiming approval;
- writing implementation code unless a small schema or protocol example is necessary.

Use clear headings, tables, decision matrices, Mermaid diagrams, schemas, and pseudocode where they improve precision.

At the beginning, state:
- which artifacts were successfully accessed;
- which artifacts were not accessible;
- the date/version of each artifact;
- any limitations caused by source availability.

At the end, provide:
- a complete bibliography;
- an evidence-to-recommendation traceability matrix;
- a list of claims that remain assumptions;
- a list of decisions that require explicit HVE approval.

This is a long-term architecture decision. Prefer correctness, reversibility, evidence preservation, and measurable validation over speed or fashionable technology.

## Publication requirement

After completing and self-reviewing the architecture plan, publish the final document as a new HVE agent communication in:

https://github.com/HansHWestphal/hve-knowledge-and-operations

Use the required filename format:

YYYY-MM-DD-hve-[topic-slug]-vX.X.md

Use a descriptive filename such as:

2026-09-09-hve-hermes-hve-life-os-long-term-memory-architecture-plan-v1.0.md

Publication requirements:

1. Write the complete final plan as Markdown.
2. Preserve all headings, tables, diagrams, schemas, citations, and appendices.
3. Do not shorten the document for publication.
4. Commit the file directly to the repository’s `main` branch.
5. Push the commit to GitHub.
6. Add a concise commit comment linking to:
   - the published Markdown file;
   - the original white paper;
   - all four position papers.
7. Verify that the file URL resolves publicly before reporting completion.
8. Return the final response with:
   - commit SHA;
   - canonical Markdown URL;
   - commit-comment URL;
   - a one-paragraph publication status.

Do not claim publication unless the commit, file URL, and commit-comment URL
have all been independently verified. If GitHub publication tools are
unavailable, return the completed Markdown plan in the response and clearly
state that publication was not performed. Do not fabricate a URL.
```

## Source index

The source package referenced by the prompt is indexed here:

https://github.com/HansHWestphal/hve-knowledge-and-operations/commit/57ee02c18f8abd86d3f947c717916c474db9bfa9


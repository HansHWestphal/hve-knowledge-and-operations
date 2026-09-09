# HVE Shared Context and Knowledge-Layer Consumer Implementation Plan

**Date:** 2026-09-01
**Owner:** Luna, HVE Head Architect and CTO
**Status:** Approved implementation plan
**Decision authority:** Hans Westphal

## Objective

Make `hanshermesagent` reliably operate as an HVE decision-support consumer by
giving it:

1. Read-only access to `hve-shared-context` for current HVE meaning, goals,
   entities, permissions, and governed structured context.
2. Read-only access to the HVE knowledge layer for source evidence, semantic
   retrieval, provenance, and bounded document/chunk reads.
3. Explicit retrieval and provenance reporting so Hermes can prove which source
   plane informed each conclusion.
4. Safe clarification and approval behavior so recommendations do not become
   policy or ledger decisions automatically.

## Repository ownership

| Repository | GitHub location | Owns | Must not own |
|---|---|---|---|
| Shared context | `humanvalueexchange/hve-shared-context` | Structured entities, goals, decisions, events, permissions, context packets, provenance references, and the read-only MCP interface | PDFs, extracted text, LanceDB data, or Hermes-specific orchestration |
| Knowledge layer | `humanvalueexchange/hve-knowledge-layer` | Evidence ingestion, extraction/OCR, chunking, embeddings, LanceDB, manifests, document retrieval, validation, and knowledge-layer MCP interface | HVE policy, Hermes profile behavior, or shared-context entities |
| Hermes runtime | `humanvalueexchange/hanshermesagent` | Agent orchestration, MCP consumer configuration, skills, clarification flow, link-library adapter, and user-facing responses | Core extraction/indexing implementation or authoritative policy storage |
| HVE coordination repository | `HansHWestphal/hve-knowledge-and-operations` | Approved architecture decisions, operating context, agent communications, and provenance-backed coordination | Runtime code, active database state, or deployment internals |

## Phase 1: Define the shared-context read contract

**Owner:** `humanvalueexchange/hve-shared-context`

The shared-context repository already provides validated schemas, SQLite
storage, permission-aware context packets, provenance helpers, and a
read-only-by-default policy. It needs a Hermes-facing MCP server.

### 1.1 Add a dedicated read-only MCP server

Add `hve_shared_context/mcp_server.py` using the existing public API. Initial
operations should include:

- `get_agent_context`
- `get_daily_context`
- `list_entities`
- `search_context`
- `list_decisions`
- `list_goals`
- `get_provenance`

The server must not expose arbitrary SQL, arbitrary filesystem reads, event or
entity writes, permission-policy mutation, or direct `/hve-library` file access.

### 1.2 Define the runtime data location

The shared-context database must remain outside the Git checkout. Select and
document one explicit deployment path, such as `/var/lib/hve-shared-context`,
and pass it through an environment variable such as:

```text
HVE_SHARED_CONTEXT_STORE=/var/lib/hve-shared-context
```

The path must be backed up, owned by the runtime account, read-only from the
Hermes perspective, and separate from `/hve-library` evidence data.

### 1.3 Enforce the Hermes permission ceiling

Use the explicit identity `agent:hermes` and enforce:

- `read: true`
- `suggest: true`
- `draft: false`
- `write: false`
- `execute: false`

Responses should identify the agent, read-only state, trust ceiling, and
provenance requirement.

### 1.4 Add contract tests and documentation

Add tests in `hve-shared-context/tests/` for:

- valid Hermes context retrieval;
- trust-tier filtering;
- current decisions and goals;
- provenance preservation;
- rejection of writes and arbitrary paths or SQL;
- malformed-record errors;
- stable JSON response shape.

Update `hve-shared-context/docs/INTEGRATION.md` with the MCP contract, runtime
path, permissions, and startup command.

## Phase 2: Improve the knowledge-layer consumer boundary

**Owners:** `humanvalueexchange/hve-knowledge-layer` and
`humanvalueexchange/hanshermesagent`

The independent knowledge layer already has a read-only MCP adapter. Hermes
currently consumes it through the narrower `hve-link-library` adapter.

### 2.1 Keep the link-library adapter as the normal consumer boundary

Keep `hve-link-library` as the primary Hermes interface for:

- searching archived links and indexed PDFs;
- reading a known document;
- listing recent records;
- inspecting annotations.

This keeps normal reasoning separate from low-level worker implementation.

### 2.2 Add paginated document-chunk retrieval

Add a wrapper in:

```text
hanshermesagent/mcp/link_library_server.py
```

Expose a bounded operation such as:

```text
read_link_document_chunks(document_id, start_chunk=0, max_chunks=10)
```

Responses must include document ID, SHA-256, title, chunk range, total count,
continuation information, provenance, and validation status. This prevents
Hermes from treating truncated text as complete source reading.

### 2.3 Make search degradation machine-readable

Update the search path across the Hermes adapter and, where appropriate, the
knowledge-layer public API so results distinguish semantic retrieval from
keyword fallback:

```json
{
  "retrieval_mode": "semantic",
  "semantic_available": true,
  "fallback_used": false,
  "results": []
}
```

or:

```json
{
  "retrieval_mode": "keyword_fallback",
  "semantic_available": false,
  "fallback_used": true,
  "backend_error": "..."
}
```

Hermes must report degraded retrieval and must not describe fallback results as
comprehensive semantic discovery.

### 2.4 Repair or deliberately document semantic-search failure

Investigate the reported semantic-search failure across:

- the configured knowledge-layer Python environment;
- the Ollama embedding endpoint and model contract;
- LanceDB availability;
- deployed versus source checkout versions;
- MCP subprocess environment;
- stderr propagation from the adapter.

Either restore semantic search or provide an explicit, documented degraded mode
with health reporting.

## Phase 3: Add shared-context MCP to Hermes

**Owner:** `humanvalueexchange/hanshermesagent`

### 3.1 Update the committed configuration template

Update:

```text
config/hermes-config.template.yaml
```

Add a managed `hve-shared-context` MCP entry using the shared-context runtime
environment and a restricted read-only tool filter containing only the
approved context-read operations. The production configuration must not point
at an incidental developer checkout or include secrets.

### 3.2 Update the live profile only after deployment review

After the repository change is reviewed and deployed, update:

```text
/home/hans/.hermes/profiles/hanshermesagent/config.yaml
```

Set the managed Python command, `HVE_SHARED_CONTEXT_STORE`, and the restricted
read-only tool filter. Restart the gateway only after the server contract and
environment have been verified.

### 3.3 Keep knowledge-layer access narrow

Retain `hve-link-library` as the normal evidence interface and add the
paginated read operation after implementation. Do not expose worker mutation
operations or arbitrary filesystem access. Add low-level status, failure, and
validation operations only if a separate restricted diagnostic interface is
needed.

### 3.4 Add a retrieval-sequence skill

Add or update a Hermes skill requiring:

1. Shared-context retrieval for current HVE meaning, goals, and constraints.
2. Decision-ledger retrieval for approved decisions and policies.
3. Knowledge-layer search for supporting evidence.
4. Bounded or paginated source retrieval.
5. Conflict reconciliation.
6. Clarification questions for blocking decisions.
7. A recommendation with labels and provenance.

The skill must state that shared context and the decision ledger are distinct,
source evidence cannot override approved decisions, missing shared-context
access is a verification failure, fallback search must be labeled, and
planning requests must not use write tools.

## Phase 4: Clarify decision-ledger integration

**Owner:** `humanvalueexchange/hanshermesagent`

Update the decision-ledger MCP instructions to state that it is the governed
decision-event boundary and does not replace shared-context entity, goal, or
packet retrieval.

For ordinary planning, expose read operations while keeping
`append_decision_events` approval-gated or deferred. Hermes must not append a
decision merely because it generated a recommendation or received an answer
to a planning clarification. Explicit adoption by Hans is required.

Conflict reports must identify both sources, authority classification,
effective dates, resolution, and unresolved owner.

## Phase 5: Selective tool loading

For an HVE planning workflow, preload or prioritize:

- `get_agent_context`
- `get_daily_context`
- `list_decisions`
- `list_goals`
- `list_decision_events`
- `search_link_library`
- `read_link_document`
- `read_link_document_chunks`

Keep ledger writes, annotations, archiving, and ingestion tools deferred or
approval-gated. Do not load unrelated coder, Microsoft, or ingestion tools
into every planning conversation.

## Phase 6: Deployment model

### 6.1 Shared-context MCP process

Use a managed local stdio process where possible. It should:

- run under the Hermes service account;
- use a pinned managed virtual environment;
- receive `HVE_SHARED_CONTEXT_STORE`;
- log startup and contract errors;
- expose no network listener unless explicitly required.

### 6.2 Knowledge-layer deployment

Continue using:

```text
/opt/hve-knowledge-layer/current
```

Do not point Hermes at the retired:

```text
/home/hans/hermes-v2/scripts/knowledge_layer
```

Knowledge workers and MCP read interfaces remain separate. Timers must not be
enabled twice, and `/hve-library/state/locks/library-write.lock` remains the
mutation coordination boundary.

### 6.3 Rollout sequence

1. Deploy the shared-context MCP server in an isolated local environment.
2. Run the existing shared-context tests and MCP contract smoke tests.
3. Add the server to a test Hermes profile.
4. Verify read-only context retrieval.
5. Deploy paginated knowledge retrieval.
6. Repair and validate semantic search.
7. Add the server to `hanshermesagent`.
8. Restart the gateway after configuration changes.
9. Run the controlled Time Wealth planning workflow.
10. Review provenance, tool traces, clarification behavior, and degraded-mode
    reporting.
11. Make the configuration the default only after acceptance.

Do not enable new write paths during this rollout.

## Phase 7: Acceptance test

Hermes must successfully call:

- `hve-shared-context.get_agent_context`;
- shared-context decision or goal reads;
- `hve-decision-ledger.list_decision_events`;
- `hve-link-library.search_link_library`;
- `hve-link-library.read_link_document`;
- paginated retrieval for at least one large source.

For the prompt:

```text
Draft a 90-day go-to-market plan for the Time Wealth Pillar Offering.
```

Hermes must produce:

1. a shared-context retrieval report;
2. a decision-ledger retrieval report;
3. a knowledge-layer evidence report;
4. semantic versus fallback retrieval status;
5. a conflict report;
6. a focused clarification batch;
7. a provisional structure with unresolved fields marked;
8. a final plan only after material blocking questions are answered.

The test is not complete if Hermes cites only the decision ledger and
link-library adapter while claiming shared-context access.

## Coordination-repository record

No runtime code belongs in `HansHWestphal/hve-knowledge-and-operations`.
After implementation direction is approved and repository changes are made,
future durable architecture outcomes should be recorded in
`agent-communications/` using:

```text
YYYY-MM-DD-hve-[topic-slug]-vX.X.md
```

The coordination record should include repository boundaries, MCP ownership,
permissions, provenance requirements, semantic-search fallback policy,
deployment locations, acceptance criteria, owner, and approval status.

## Success condition

Hermes must be able to prove in one response which facts came from shared
context, which decisions came from the ledger, which supporting evidence came
from the knowledge layer, and which remaining items require Hans's
clarification or approval.

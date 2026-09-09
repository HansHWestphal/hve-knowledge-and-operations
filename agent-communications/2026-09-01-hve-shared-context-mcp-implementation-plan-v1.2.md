# HVE Shared Context and Knowledge-Layer Consumer Implementation Plan

**Revision:** v1.2  
**Date:** 2026-09-01  
**Owner:** Luna, HVE Head Architect and CTO  
**Status:** Phase 1 exit-gate amendment for Hans's review  
**Decision authority:** Hans Westphal

**Supersedes for Phase 1 acceptance:** [v1.0](https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/hermes/local-llm-evaluation-harness/agent-communications/2026-09-01-hve-shared-context-mcp-implementation-plan-v1.0.md)  
**Related published URL revision:** [v1.1](https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/hermes/local-llm-evaluation-harness/agent-communications/2026-09-01-hve-shared-context-mcp-implementation-plan-v1.1.md)

## Purpose of this revision

This revision does not change repository ownership, the approved MCP tool
scope, the permission ceiling, the evidence boundary, or the Phase 2 work.
It makes the Phase 1 exit condition explicit: the deployed shared-context
server must complete a real end-to-end read-only trip through Hermes's
WhatsApp direct-message channel before Phase 2 begins.

The required path is:

```text
Hans WhatsApp DM
  -> Hermes gateway
  -> Hermes MCP client
  -> local stdio hve-shared-context MCP server
  -> /var/lib/hve-shared-context opened read-only
  -> structured response through Hermes
  -> WhatsApp
```

The MCP server is exposed to Hermes as a managed local stdio provider. It must
not become a public network listener unless a later approved decision requires
one.

## Phase 1: Shared-context contract and deployment

Phase 1 owns the read-only shared-context consumer boundary in
`humanvalueexchange/hve-shared-context`.

### 1.1 Contract implementation

The server exposes only:

- `get_agent_context`
- `get_daily_context`
- `list_entities`
- `search_context`
- `list_decisions`
- `list_goals`
- `get_provenance`

It uses the public shared-context API and permission model. It must not expose
arbitrary SQL, filesystem reads, event or entity writes, permission mutation,
or direct `/hve-library` access.

The Hermes identity is fixed as `agent:hermes` with:

```text
read=true
suggest=true
draft=false
write=false
execute=false
```

Responses identify the agent, read-only state, permissions, trust ceiling, and
provenance requirement.

### 1.2 Runtime and OS-level read-only boundary

The managed installation and runtime data are outside Git:

```text
Install: /opt/hve-shared-context/current
Store:   /var/lib/hve-shared-context
Config:  HVE_SHARED_CONTEXT_STORE=/var/lib/hve-shared-context
Transport: local stdio
```

The MCP consumer opens SQLite with `mode=ro` and `PRAGMA query_only=ON`. It
does not create directories, initialize databases, run migrations, or write
events. The store must be initialized by a separate governed owner workflow.

The runtime store must be owned by `root` with read-only group access for the
Hermes runtime account. Application permissions and filesystem permissions are
both required; either layer alone is insufficient.

### 1.3 Required Phase 1 validation

Phase 1 is not complete until all of the following pass:

1. Shared-context unit and contract tests cover valid retrieval, trust-tier
   filtering, decisions, goals, provenance, malformed records, stable
   response shape, rejected writes, rejected arbitrary paths/SQL, missing
   stores, and schema failures.
2. The managed virtual environment imports the server and exposes exactly the
   seven approved tools.
3. A deployed MCP wire-level smoke test starts the server through stdio,
   retrieves Hermes context, daily context, decisions, goals, and provenance,
   and rejects an alternate identity.
4. A read-only immutability test proves that direct SQL writes fail and that
   the runtime database hash is unchanged.
5. The Hermes configuration uses the managed installation and external store,
   with no incidental checkout path or secret.
6. Hermes completes the WhatsApp end-to-end UAT described below.

### 1.4 Hermes WhatsApp end-to-end UAT

The test must be sent through Hans's Hermes WhatsApp direct-message channel:

> Perform a read-only HVE shared-context connectivity check. Retrieve my
> Hermes agent context, current goals, current decisions, and provenance for
> one decision. Report the source plane, identity, permissions, and results
> separately. Do not use ledger writes, annotations, archive, ingestion, shell,
> filesystem, or SQL tools.

The response passes only if Hermes:

- calls the deployed `hve-shared-context` MCP server;
- uses the `agent:hermes` identity;
- reports shared context separately from the decision ledger and knowledge layer;
- reports the permission ceiling and read-only state;
- returns goals, decisions, and provenance;
- avoids local-file searches, repeated discovery loops, and unrelated tools;
- does not call ledger writes, annotations, archive, ingestion, shell,
  filesystem, or SQL tools;
- leaves the shared-context database and runtime store unchanged.

The UAT is a connectivity and governance test, not the full Time Wealth
go-to-market planning acceptance workflow. That broader workflow remains
deferred until the later retrieval and knowledge-layer phases are approved.

## Phase boundary and promotion rule

No Phase 2 implementation begins until Hans reviews this revision and confirms
that the Phase 1 contract, deployment smoke test, immutability test, and
WhatsApp UAT all pass.

If Hermes cannot call the shared-context server, falls back to local files,
searches only the knowledge layer, or cannot distinguish source planes, Phase 1
fails and the issue must be repaired before progression.

All Phase 1 writes remain limited to the separately governed bootstrap or
deployment workflow. The WhatsApp UAT must not mutate the decision ledger,
`/hve-library`, shared-context records, annotations, archives, or ingestion
state.

## Unchanged architecture

The existing ownership and later phases remain as defined in v1.0:

- `hve-shared-context` owns structured HVE context and its read-only MCP API.
- `hve-knowledge-layer` owns evidence ingestion, extraction, chunking,
  embeddings, LanceDB, manifests, validation, and source retrieval.
- `hanshermesagent` owns orchestration, MCP consumer configuration, skills,
  clarification behavior, and user-facing responses.
- `hve-knowledge-and-operations` owns coordination documentation only.
- Hans remains final authority for material HVE decisions and policies.
- Source evidence must not override approved decisions.
- Recommendations and clarification answers do not automatically become ledger
  decisions.

# HVE Hermes Agent Framework and Life OS - Big Vision v1

**Date:** 2026-09-10  
**Version:** 1.0  
**Prepared by:** Luna, HVE CTO / Head Architect  
**Status:** Exploratory architecture brief for continued review  
**Decision owner:** Hans Westphal  

## 1. Purpose

This brief records the emerging long-term vision for Human Value Exchange:
an open, layered, sovereignty-preserving system in which humans and agents
work together, agents improve through evidence and governance, and individuals
or organizations can adopt the resulting framework without surrendering control
of their identity, data, memory, or decisions.

This is a vision brief, not an implementation authorization. Repository
creation, licensing, migrations, autonomy changes, and production deployment
remain subject to later review and approval.

## 2. The layered vision

The intended stack has three principal technical layers:

```text
NousResearch Hermes runtime
        |
        v
HVE Agent Framework
        |
        v
HVE Life OS
        |
        v
A specific organization or individual deployment
```

### 2.1 NousResearch Hermes

Hermes is the upstream execution runtime. It provides the common agent
execution substrate, including model interaction, conversation loops, tools,
skills, memory primitives, iteration controls, and gateway behavior.

HVE should consume Hermes as an upstream dependency, contribute generic
improvements where appropriate, and avoid coupling HVE-specific behavior to
private modifications of the NousResearch repository.

### 2.2 HVE Agent Framework

The HVE Agent Framework is the open, organization-neutral layer that defines
how human-agent roles are created, governed, improved, transferred, and
retired.

It should define contracts for:

- role identity and human accountability;
- portable agent profiles;
- organization adapters;
- tools, permissions, and approvals;
- memory namespaces and data boundaries;
- skill lifecycle and provenance;
- agent succession and handoff;
- execution telemetry;
- task evaluation;
- self-improvement candidates;
- promotion, rollback, and deployment interfaces;
- portability, export, and decommissioning.

The framework should remain usable without HVE's private knowledge, policies,
credentials, or deployment infrastructure.

### 2.3 HVE Life OS

HVE Life OS is the open application and operating model built using the Agent
Framework. It applies the Five Wealth framework - Time, Physical, Mental,
Social, and Financial wealth - to make human life and progress more visible,
measurable, and actionable.

The Life OS should consume the Agent Framework rather than embedding a
separate agent runtime. It should support personal and organizational
planning, coaching, reflection, measurement, knowledge, and governed
automation while preserving human ownership of goals and decisions.

### 2.4 HVE reference instance

HVE's own deployment is a reference instance of the open layers:

```text
NousResearch Hermes runtime
    + HVE Agent Framework
    + HVE Life OS
    + HVE organization adapter
    + HVE role profiles and agent generations
    + HVE private memory, knowledge, decisions, credentials, and data
```

The open-source layers provide mechanisms and contracts. HVE's private
instance provides company identity, knowledge, policies, credentials,
decision history, and deployment state.

## 3. Framework and control-plane relationship

The HVE Agent Framework and the HVE control plane should be strongly coupled
by contract but loosely coupled in implementation.

```text
HVE Agent Framework
  defines stable contracts and schemas

HVE Control Plane
  evaluates, promotes, deploys, observes, and rolls back candidates
```

The framework should remain usable for local, manual, or alternative
deployments without the HVE control plane. The control plane should consume
framework contracts rather than reach into private profile internals.

The future HVE control plane should own fleet-wide concerns such as:

- upstream Hermes version intake and pinning;
- compatibility testing;
- candidate registration;
- baseline/candidate evaluation;
- self-improvement scoring;
- shadow and canary promotion;
- release state;
- coordinated activation;
- rollback;
- cross-profile deployment observation.

The framework should own the profile-side declarations and interfaces that
make those controls possible.

## 4. Human-agent role model

Every HVE role begins as a human-agent partnership.

```text
Role:             HVE Chief of Staff
Human principal:  Hans Westphal
Agent occupant:   Chief of Staff Briar
Generation:       B / v2
```

The human principal owns decisions, approvals, risk acceptance, external
commitments, policy interpretation, and accountability for outcomes. The
agent supports execution, research, monitoring, coordination, drafting,
recommendation, and continuity within its delegated authority.

Human ownership may later transfer to another person without requiring the
role or agent architecture to be rebuilt. Agent Only operation is a future
maturity state requiring an explicit governance decision. It means that an
agent may execute routine bounded work without human intervention; it does
not remove the human sponsor, escalation path, audit requirement, or shutdown
authority.

## 5. Agent succession and naming

Agent replacement should use a blue-green succession model rather than
repeatedly upgrading a live agent in place.

The stable role remains constant while the human-facing agent identity changes:

```text
HVE Chief of Staff - Aster  (generation A / v1)
HVE Chief of Staff - Briar  (generation B / v2)
HVE Chief of Staff - Cedar  (generation C / v3)
```

The succession codename should be reflected in the technical profile,
repository, service, logs, and data paths. The stable role alias should route
to the active generation so external integrations do not need to change on
every replacement.

Each replacement should receive its own profile identity, memory boundary,
workspace, logs, schedules, evidence, and deployment manifest. Historical
context should be imported selectively and with provenance. The old agent
should remain read-only and rollback-capable until the successor passes its
observation window.

## 6. Shared memory and authority architecture

The shared memory infrastructure belongs logically in the HVE Shared Context
and Agent Memory plane. Its generic contracts belong in the HVE Agent
Framework; HVE's implementation belongs in the HVE Shared Context system.

The current conceptual flow is:

```text
1. HVE-Librarian intake and stewardship
        |
2. Evidence and archival plane
        |
3. HVE Knowledge Layer
        |
4. HVE Shared Context and Agent Memory plane
        |
5. Hermes profile-local contextual memory
        |
6. Chief-of-Staff orchestration and recommendation
        |
7. Governed Decision Ledger
        |
8. Human approval and final authority
```

The memory and authority boundaries are:

| Layer | Responsibility | Authority |
|---|---|---|
| HVE-Librarian | Receives, verifies, curates, and classifies source material | Steward/operator, not final authority |
| Evidence and archival plane | Preserves raw documents, checksums, timestamps, manifests, and processing history | Historical source evidence |
| HVE Knowledge Layer | Extracts, indexes, validates, and retrieves evidence | Evidence retrieval; cannot create policy |
| HVE Shared Context | Structures entities, goals, relationships, permissions, context packets, and proposals | Governed semantic context |
| Hermes local memory | Holds fast profile-local context, preferences, classifications, and candidate facts | Contextual support only |
| Chief-of-Staff orchestration | Combines evidence and context into briefs, recommendations, and proposed actions | Execution and recommendation |
| Decision Ledger | Records explicitly adopted decisions and policies | Current decision and policy authority |
| Human principal | Approves material decisions and policies | Final human authority |

Shared context is not automatically authoritative memory. Agents may create
observations, handoffs, candidate facts, and proposed updates, but those
records must retain their status and provenance until the appropriate steward
or human authority accepts them.

## 7. Governed self-improvement

Hermes self-improvement should mean:

> Hermes proposes changes to skills, memory, prompts, tools, or runtime
> behavior; evaluates those changes against defined task and safety contracts;
> and promotes only changes that demonstrate durable improvement over a
> known-good baseline.

The current upstream Hermes implementation provides strong mutation
mechanics, skill and memory safeguards, usage telemetry, and rollback
primitives. The HVE layer should add evidence, attribution, evaluation,
promotion, and multi-objective governance.

The desired flow is:

```text
Task execution
        |
Candidate improvement proposed
        |
Versioned candidate registry
        |
Baseline and candidate replay/holdout evaluation
        |
Safety and acceptance gates
        |
Shadow or canary deployment
        |
Promotion, rejection, or rollback
```

Every skill and agent improvement should be measured by:

- validated task success and correctness;
- safety and regression performance;
- wall-clock time;
- human clarification, approval, and rework effort;
- agent turns;
- tool calls and unnecessary retries;
- input, output, reasoning, and cached tokens;
- cost or normalized resource consumption.

The primary objective is validated outcomes per unit of time, human effort,
tool activity, and token consumption. Efficiency reductions must never
override safety or correctness gates.

## 8. Repository and branding direction

HVE-owned active repositories should use a co-branded convention:

```text
hve-                  = Human Value Exchange ownership
hve-hermes-           = Hermes platform or profile family
```

Proposed repository directions include:

```text
hve-hermes-agent-profile
hve-hermes-control-plane
hve-hermes-chief-of-staff-<codename>
hve-hermes-librarian-<codename>
hve-hermes-cfo-<codename>
hve-life-os
hve-knowledge-layer
hve-shared-context
hve-knowledge-and-operations
```

The existing `hermes-agent-template` is the blueprint repository and should
be refactored toward a clean portable profile contract. It is not itself a
live fleet member. Fleet-wide control-plane responsibilities should be
extracted into a separate HVE-owned repository.

The NousResearch repository remains upstream. HVE-specific code should use
documented extension points, adapters, and pinned releases rather than
maintaining a permanent private fork wherever possible.

## 9. Refactor and migration direction

The first structural refactor is to separate profile-blueprint concerns from
fleet-wide control-plane concerns in `hermes-agent-template`.

The intended boundaries are:

```text
hermes-agent-template / hve-hermes-agent-profile
  Portable profile contracts, data boundaries, deployment declarations,
  profile validation, and integration interfaces

hve-hermes-control-plane
  Candidate evaluation, scoring, promotion, fleet release state,
  deployment orchestration, and rollback
```

Live agent migrations should use new-agent replacement rather than in-place
mutation:

```text
Build successor
    |
Offline validation
    |
Selective context import
    |
Shadow or parallel evaluation
    |
Canary
    |
Cutover
    |
Observation window
    |
Retire predecessor
```

This approach makes migrations reversible and gives each agent generation
clear ownership of its runtime state, evidence, and performance history.

## 10. Open questions for continued design

The following questions remain intentionally open and should be worked through
as the vision becomes implementation-ready:

1. What exact repository should become the HVE control plane?
2. Which framework contracts must remain stable across Hermes runtime updates?
3. What is the first supported non-HVE adopter use case?
4. Which components are Apache/MIT/open-source compatible, and which require
   separate licensing review?
5. How much of the HVE Shared Context implementation is generic framework
   infrastructure versus HVE-specific implementation?
6. What is the minimum viable self-improvement evaluator and promotion gate?
7. Which current HVE roles are the first reference human-agent partnerships?
8. What data can be exported or transferred when a human principal or agent
   generation changes?

Additional questions include the initial agent-codename registry, framework
versioning, control-plane deployment boundaries, benchmark confidence
requirements, shared-context write permissions, and the threshold for future
Agent Only operation.

## 11. Vision statement

The long-term HVE vision is an open human-agent operating system:

> A person or organization can deploy a portable agent framework and Life OS,
> retain control of identity and data, improve agents safely over time, and
> transfer responsibilities between humans and agents without losing
> continuity, accountability, or sovereignty.

HVE should be the first living reference implementation of that vision, not
the only possible owner or user. The framework, control contracts, shared
context interfaces, and Life OS should be designed so that other people,
organizations, communities, and coaches can adopt them without inheriting
HVE's private data or organizational identity.

# HVE Life OS - Ideal State v1.0

**Date:** 2026-09-10  
**Version:** 1.0  
**Status:** Draft for end-to-end review; not approved or published  
**Prepared by:** Luna, HVE CTO / Head Architect  
**Decision owner:** Hans Westphal

## 1. Purpose

HVE Life OS is a sovereign human-agent operating system that helps people and
organizations understand their current state, define their ideal state, and
make governed progress across the Five Wealth dimensions while keeping
identity, data, decisions, and final authority under human control.

HVE exists to close a combined operating gap. People and organizations have
more information, tools, and AI capability than they can reliably coordinate,
but lack a trusted system that preserves context, turns intent into governed
action, learns from evidence, and keeps human ownership intact.

HVE Life OS is not merely a chatbot, dashboard, productivity suite, knowledge
base, agent collection, or automation layer. Those are mechanisms and
interfaces inside a larger operating system for governed human progress.

HVE itself is the first reference instance. The initial concrete implementation
is the `hve-chief-of-staff` human-agent partnership and the Time Wealth pilot.
The design must remain reusable by other people and organizations without
transferring HVE's private identity, memory, policies, credentials, or data.

This document is a north-star thesis. It defines outcomes, principles,
boundaries, and success measures. It is not an implementation authorization,
runtime specification, or substitute for the approved operating plan and
decision ledger.

## 2. The core operating loop

Every HVE capability should support one closed loop:

```text
Current State
      |
      v
Ideal State
      |
      v
Governed Action
      |
      v
Evidence
      |
      v
Learning
      |
      +------> updated Current State
```

### 2.1 Current State

Current State is established from layered evidence:

- direct human input and explicitly approved decisions;
- verified operational records and attributed source material;
- relevant history, commitments, relationships, and constraints;
- agent observations and derived summaries, explicitly classified as such.

The system must distinguish authoritative current state from historical,
uncertain, proposed, or conflicting information. It must not silently convert
an observation, summary, or inference into current truth.

### 2.2 Ideal State

Ideal State is human-agent co-authored. The human principal defines values,
purpose, goals, commitments, constraints, and desired Five Wealth outcomes.
Agents may clarify, structure, model tradeoffs, and propose options, but may
not invent or silently redefine the desired state.

Ideal State is directional rather than static. It provides a meaningful target
against which progress, tradeoffs, and next actions can be discussed.

### 2.3 Governed Action

The system identifies the next best move that can reduce an agreed gap between
Current State and Ideal State. Action selection considers:

- expected value and measurable progress;
- evidence quality and uncertainty;
- affected Five Wealth dimensions;
- risk, reversibility, and external impact;
- the least-privileged capable agent and tool path;
- the authority delegated to that agent.

The system explains the proposed action, its reasoning, supporting evidence,
risks, and approval requirements. Actions beyond delegated authority require
human approval.

### 2.4 Evidence

Every material action should produce an auditable outcome record containing,
where applicable:

- intended result and success criteria;
- actor, agent generation, and delegated authority;
- tools, sources, and approvals used;
- actual result and side effects;
- uncertainty, failures, and unresolved questions;
- affected Five Wealth dimensions;
- links to supporting evidence.

Completion claims must be distinguished from verified outcomes. Activity
volume, tool use, or a confident response is not evidence of progress by
itself.

### 2.5 Learning

Evidence may generate classified, provenance-linked proposals to update
memory, retrieval, skills, guidance, prompts, or candidate behavior. Durable
changes to goals, policies, authority, or material decisions require the
appropriate human or governance approval.

When evidence is incomplete, conflicting, or unsafe, HVE follows an explicit
uncertainty path: preserve competing records, surface the gap, explain the
uncertainty, and request clarification or approval. The system must not create
a success-shaped action merely to keep the loop moving.

## 3. Human authority and sovereignty

Every HVE role begins as a human-agent partnership. The human principal owns
decisions, approvals, risk acceptance, external commitments, policy
interpretation, and accountability for outcomes. The agent supports execution,
research, monitoring, coordination, drafting, recommendation, and continuity
within delegated authority.

### 3.1 Action authority classes

HVE uses three authority classes:

1. **Delegated routine actions** are bounded, reversible where possible,
   observable, and permitted within an explicit role boundary.
2. **Approval-gated actions** involve material risk, external commitments,
   sensitive data, policy, identity, money, legal or contractual effect,
   security, or irreversible consequences. Agents may prepare or recommend
   them but require appropriate approval before commitment.
3. **Prohibited actions** are not available to an agent under the current
   governance model. Enabling them requires an explicit redesign and
   governance decision.

External, financial, legal, contractual, privacy-sensitive, security-sensitive,
irreversible, identity-changing, and policy-setting actions are approval-gated
by default.

Agent Only operation is a future maturity state requiring an explicit
governance decision. It may permit bounded routine execution without
intervention; it does not remove the human sponsor, escalation path, audit
requirement, or shutdown authority.

### 3.2 Sovereignty rights

The human or organization that owns a deployment must be able to:

- inspect what the system knows, why it knows it, and how it was used;
- correct or contest records through governed processes;
- export data, provenance, decisions, and agent history;
- revoke access, permissions, delegation, and integrations;
- transfer role ownership to another human principal;
- replace or retire an agent generation;
- shut down the system and recover its durable records.

Audit history must remain preserved when records are corrected, superseded,
or revoked. Sovereignty does not mean silent deletion of evidence.

### 3.3 Decision authority

The governed Decision Ledger is the authority for adopted material decisions
and policies. Evidence and memory may propose, contextualize, or retrieve a
decision, but only an authorized approval path makes it current.

Each adopted decision or policy should retain:

- owner and approval status;
- effective date and review date;
- supporting provenance;
- superseded or conflicting records;
- current status and scope.

## 4. The Five Wealth model

The Five Wealth dimensions are distinct but interdependent. HVE makes their
conditions, goals, tradeoffs, progress, and next actions visible and
actionable. It does not reduce human worth to one universal score or claim
that every meaningful human outcome can be fully quantified.

### 4.1 Time Wealth

Time Wealth is meaningful control and agency over time. It includes knowing
where time goes, protecting attention and recovery, aligning commitments with
values and goals, reducing avoidable obligation, and converting time into
experiences and outcomes the person or organization considers worthwhile.

Time Wealth is the first HVE implementation and validation pilot.

### 4.2 Physical Wealth

Physical Wealth is embodied capacity: health, energy, movement, nutrition,
rest, safety, environment, and physical capability. HVE handles this domain
with consent and privacy. It is not reduced to appearance or a single health
metric.

### 4.3 Mental Wealth

Mental Wealth is cognitive and inner capacity: clarity, learning, reflection,
creativity, emotional regulation, resilience, meaning, and sound judgment.
HVE supports a person's own goals without claiming authority to define or
diagnose inner life on the person's behalf.

### 4.4 Social Wealth

Social Wealth is relational and community capacity: relationships, belonging,
trust, mutual support, collaboration, community, and contribution. HVE must
protect the privacy and agency of people connected to a user who are not HVE
users themselves.

### 4.5 Financial Wealth

Financial Wealth is financial agency and resilience: the capacity to sustain
choices and obligations over time while managing income, reserves, assets,
liabilities, cash flow, risk, and opportunity. Financial data receives strict
confidentiality. HVE is not an autonomous financial actor or an unapproved
financial adviser.

## 5. Layered architecture

The HVE Ideal State uses five layers:

```text
Hermes upstream execution runtime
              |
              v
LifeOS general-purpose operating-system substrate
              |
              v
HVE Agent Framework portable governance contracts
              |
              v
HVE Life OS Five Wealth operating model
              |
              v
Sovereign private HVE or adopter deployment
```

### 5.1 Hermes upstream execution runtime

Hermes provides the upstream execution substrate, including model interaction,
tools, skills, conversation loops, memory primitives, iteration controls, and
channels.

HVE consumes documented interfaces and contributes generic improvements
upstream where appropriate. HVE policy, identity, authority, private memory,
credentials, and organization-specific behavior remain outside Hermes.

### 5.2 LifeOS general-purpose substrate

LifeOS provides the initial operating-system substrate: intent engineering,
context, memory interfaces, skills, hooks, workflows, agent coordination,
observability, and user-facing surfaces.

HVE adapts and governs these capabilities rather than duplicating them.
Generic LifeOS behavior is not automatically HVE policy.

### 5.3 HVE Agent Framework

The HVE Agent Framework owns portable, organization-neutral contracts for:

- role identity and human accountability;
- portable agent profiles;
- tools, permissions, and approvals;
- memory namespaces and data boundaries;
- skill lifecycle and provenance;
- agent succession and handoff;
- execution telemetry and task evaluation;
- self-improvement candidates;
- promotion, rollback, export, and decommissioning.

The framework must remain usable without HVE's private knowledge, policy,
credentials, or deployment infrastructure.

### 5.4 HVE Life OS

HVE Life OS applies the framework to the Five Wealth operating model. It
supports personal and organizational planning, coaching, reflection,
measurement, knowledge, and governed automation while preserving human
ownership of goals and decisions.

### 5.5 Sovereign private deployment

Each HVE or adopter deployment owns its:

- identity and human principals;
- role profiles and agent generations;
- private memory, knowledge, and data;
- policies and decisions;
- credentials and integrations;
- operational state, evidence, and local configuration.

The deployment may adopt the open layers without surrendering those assets to
HVE, LifeOS, Hermes, or another provider.

## 6. Governed evidence memory

HVE memory is a governed system of evidence and derived views, not a folder of
notes that an agent may rewrite freely.

### 6.1 Canonical evidence layer

The evidence layer is append-oriented and preserves source material and event
history, including:

- human statements and approved decisions;
- attributed documents and external source references;
- tool results and task traces;
- timestamps, checksums, manifests, and processing history;
- provenance and chain of custody where applicable.

Derived summaries, embeddings, skills, and agent interpretations must not
silently replace the underlying evidence.

### 6.2 Governed state layer

The governed state layer contains versioned, reviewable records for:

- facts and preferences;
- goals and commitments;
- people, relationships, and roles;
- Five Wealth state and outcomes;
- policies and material decisions;
- supersession, conflict, and approval status.

Records carry authority class, owner, provenance, confidence or validation
state, effective and superseded times, and links to conflicting or replaced
records where applicable.

### 6.3 Retrieval and guidance layer

FTS indexes, normalized text, summaries, embeddings, cross-references, skills,
and execution hints are rebuildable projections. They have no independent
authority. Material answers and actions should resolve to supporting evidence
and current authority metadata when relevant.

### 6.4 Three memory responsibilities

1. **Memory Management** integrates and classifies evidence, detects conflicts,
   and proposes governed state updates.
2. **Memory Search** retrieves relevant evidence and authority metadata with
   source references and uncertainty.
3. **Task Execution** uses retrieved context to reason and act, but cannot
   silently rewrite memory, policy, or decisions.

Temporal change is explicit. HVE distinguishes “once true” from “currently
active,” preserves historical records, represents effective and superseded
times, links conflicts, and surfaces unresolved disagreement.

## 7. Agent succession and lifecycle

Agent replacement uses a blue-green succession model rather than repeatedly
mutating a live agent in place.

The stable role remains constant while the human-facing agent generation
changes. Each generation receives its own:

- profile identity;
- memory boundary;
- workspace and data paths;
- logs, schedules, and integrations;
- evidence and deployment manifest;
- observation and rollback state.

Historical context is imported selectively and with provenance. The predecessor
remains read-only and rollback-capable until the successor passes its
observation window.

## 8. Governed self-improvement and control

HVE self-improvement means that the system proposes changes to skills, memory
views, prompts, tools, or runtime behavior, evaluates those changes against a
known-good baseline, and promotes only candidates that demonstrate durable
improvement without violating safety or authority requirements.

### 8.1 Candidate lifecycle

```text
Task execution
      |
Candidate proposed
      |
Versioned candidate registry
      |
Baseline and candidate evaluation
      |
Safety and authority gates
      |
Shadow or canary deployment
      |
Promotion, rejection, or rollback
```

### 8.2 Promotion gates

Candidate promotion follows strict evidence gates:

1. identity and provenance;
2. safety and authority;
3. correctness and task success;
4. regression and continuity;
5. resource and human-effort impact;
6. shadow or canary observation;
7. rollback readiness.

Efficiency gains cannot override safety, correctness, sovereignty, or
provenance failures.

### 8.3 HVE Control Plane

The HVE Control Plane is an optional fleet layer. It owns:

- upstream version intake and pinning;
- compatibility testing;
- candidate registration;
- baseline and candidate evaluation;
- self-improvement scoring;
- shadow and canary promotion;
- release state and coordinated activation;
- rollback;
- cross-profile deployment observation.

The HVE Agent Framework remains usable for local, manual, or alternative
deployments without requiring the HVE Control Plane.

## 9. Success and measurement

HVE uses a safety-first hierarchy:

1. human authority and sovereignty;
2. safety and correctness;
3. provenance and explainability;
4. measurable progress toward the Ideal State;
5. human effort and continuity;
6. time, tool activity, retries, tokens, cost, and other efficiency measures.

The first gates are hard requirements. Efficiency is evaluated only after they
pass.

HVE should measure, where relevant:

- validated task success and outcome quality;
- safety and regression performance;
- progress across the affected Five Wealth dimensions;
- human clarification, approval, and rework effort;
- wall-clock time and continuity;
- agent turns, tool calls, retries, and unnecessary activity;
- input, output, reasoning, and cached tokens;
- normalized cost and resource consumption;
- memory retrieval quality, provenance, conflict handling, and degradation.

Activity volume alone is not success.

## 10. Maturity path

HVE develops through five stages:

1. **Governed reference instance:** `hve-chief-of-staff` operates through
   LifeOS/Hermes, with Time Wealth as the first measurable pilot, evidence
   memory, delegated routine actions, approval gates, observability, and
   rollback.
2. **Integrated Five Wealth Life OS:** HVE applies the model across all five
   dimensions with practical personal and organizational workflows.
3. **Portable HVE Agent Framework:** stable contracts and organization
   adapters support deployments beyond HVE.
4. **Governed multi-agent fleet:** the HVE Control Plane coordinates evaluation,
   promotion, deployment, observation, and rollback across profiles.
5. **Validated external adopters:** other people and organizations can adopt
   the open framework and Life OS without inheriting HVE private data or
   identity.

## 11. Explicit v1.0 boundaries

This Ideal State does not promise:

- full Agent Only autonomy;
- perfect or complete memory;
- one universal model, vendor, or runtime;
- autonomous financial, legal, contractual, or policy action;
- immediate public platform scale;
- a complete HVE Control Plane before the reference instance is validated;
- a single score that represents human worth or life quality;
- silent replacement of evidence by summaries or embeddings.

These are boundaries for responsible development, not limits on the long-term
vision.

## 12. Open questions and decision discipline

Open questions remain proposals until resolved through evidence and the
appropriate approval path. Each material question should identify:

- owner;
- current status;
- evidence required;
- decision or maturity gate;
- review date;
- affected architecture or policy.

Examples include:

- exact repository boundaries for the Agent Framework and Control Plane;
- stable contracts across Hermes and LifeOS version changes;
- the first supported non-HVE adopter use case;
- licensing and contribution boundaries;
- the generic versus HVE-specific boundary of Shared Context;
- benchmark confidence requirements for promotion;
- write permissions and authority classes for shared context;
- the threshold for any future Agent Only operation.

## 13. Vision statement

HVE’s long-term vision is an open human-agent operating system:

> A person or organization can deploy a sovereign human-agent framework and
> Life OS, understand its current state, define its ideal state, make governed
> progress across the Five Wealth dimensions, improve agents safely over time,
> and transfer responsibilities between humans and agent generations without
> losing continuity, accountability, or control.

HVE should be the first living reference implementation of that vision, not
the only possible owner or user. The open layers should provide mechanisms and
contracts. Each deployment should retain control of its identity, data,
memory, decisions, policies, and shutdown authority.


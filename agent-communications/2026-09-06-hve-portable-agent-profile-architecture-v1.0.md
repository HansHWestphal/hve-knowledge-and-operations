# HVE Portable Agent Profile Architecture

**Date:** 2026-09-06  
**Prepared by:** Luna, HVE CTO / Head Architect  
**Status:** Architecture direction recorded for future refactors  
**Scope:** Hermes profile independence, portability, and HVE integration boundaries

## Executive decision

Each true HVE executive profile must be independently deployable and portable.
An agent should be able to leave HVE, receive a different organization adapter,
and continue functioning without depending on another HVE profile, repository,
private filesystem path, gateway, credential, or shared mutable state.

The profile should be portable by construction and HVE-specialized by
configuration.

This means the objective is not merely one Git repository per profile. The
actual target is:

> One profile, one bounded runtime contract, one owned data boundary, one
> portable deployment unit, and one portable export.

## Architectural separation

The system should be organized into two explicit layers.

### Hermes runtime and portable profile stack

Hermes supplies the common execution framework. Each profile owns its complete
profile-level operating contract:

- identity and mission;
- `SOUL.md` and behavioral rules;
- profile configuration;
- memory and conversation history;
- skills and prompts;
- MCP and tool registry;
- permission policy;
- schedules and recurring workflows;
- logs, audit trail, and evidence store;
- model and provider configuration;
- deployment manifests and health checks;
- backup, export, and import procedures;
- tests proving tool and permission boundaries.

### Organization adapter

HVE-specific information must remain an explicit adapter layer rather than
being hidden inside a portable profile:

- HVE mission and Five Wealth taxonomy;
- HVE company knowledge and source documents;
- HVE policies and approval rules;
- HVE branding and operating language;
- HVE-specific MCP integrations;
- HVE-specific truth-layer and shared-context connections.

The adapter can be replaced when the profile operates for another
organization. HVE proprietary knowledge and restricted data do not become
portable profile state automatically.

## Independence requirements

A portable profile must not depend on:

- another profile's repository;
- another profile's private filesystem paths;
- another profile's gateway or worker;
- HVE-only credentials;
- HVE-only MCP servers without an adapter boundary;
- HVE-specific assumptions embedded in core logic;
- a global unnamed Hermes runtime;
- shared mutable state that cannot be exported or reconstructed.

Shared infrastructure is allowed only when it behaves as a replaceable
platform dependency with a stable contract. Examples include Hermes core,
Ollama, browser services, or a knowledge engine. A profile may use those
services, but it must not reach into another profile's private files or
implicitly inherit that profile's lifecycle.

## Portability standard

A profile is portable when the following procedure succeeds:

1. Clone the profile repository.
2. Install the profile stack.
3. Provide a new organization adapter, or run in generic mode.
4. Restore an authorized memory export.
5. Configure new credentials.
6. Start the profile without any other HVE profile.
7. Pass health, permission, tool-surface, and isolation tests.

If the process requires `HansHermesAgent`, `HVE-CFO`, an HVE-private path, or a
hidden systemd unit, the profile is still an HVE deployment component rather
than an independent agent.

## Ownership boundaries

The HVE executive fleet should use the following ownership model:

| Profile | Portable responsibility | HVE specialization |
|---|---|---|
| HansHermesAgent | Executive chief-of-staff behavior, continuity, coordination, commitments | HVE executive context and company decisions |
| HVE-CTO | Chief Time Officer capabilities | HVE Time Wealth model and records |
| HVE-CPO | Chief Physical Officer capabilities | HVE Physical Wealth model and records |
| HVE-CMO | Chief Mental Officer capabilities | HVE Mental Wealth model and records |
| HVE-CSO | Chief Social Officer capabilities | HVE Social Wealth model and records |
| HVE-CFO | Chief Financial Officer capabilities | HVE Financial Wealth model and records |
| HVE-Librarian | Knowledge curation, provenance, and source verification | HVE truth layer and institutional memory |

The HVE-specific adapter must not be confused with the profile's core identity.
For example, a portable financial profile can become HVE-CFO when loaded with
the HVE financial adapter, while remaining a general financial advisor in
another organization.

## Current Spark implication

The current Spark refactor has established several repository and identity
boundaries, but it has not yet reached this standard. The remaining work must
remove cross-profile executable paths, assign ownership to shared services,
separate scheduler state, and provide independent profile deployment and
isolation validation.

The refactor should therefore be judged against profile portability rather than
only repository separation.

## Required future contract

Every true profile repository should eventually contain or reference:

- `PROFILE.yaml` with stable identity and ownership;
- portable runtime configuration;
- profile-owned skills and prompts;
- profile-owned MCP/tool declarations;
- permission and approval policy;
- scheduler definitions;
- service and deployment manifests;
- memory schema and export/import tooling;
- health, isolation, and capability tests;
- organization-adapter interface;
- rollback and decommission procedures.

Every live deployment should be traceable back to those artifacts. Host-level
cron, systemd units, timers, environment files, data roots, and service
dependencies must be included in the deployment manifest or validated against
it.

## Architectural principle

Build every true executive profile as a portable autonomous product, then
assemble those products into HVE through explicit adapters and governance.
This preserves sovereignty, prevents profile coupling, and allows profiles,
models, hosts, and organizational contexts to change without invalidating the
whole system.

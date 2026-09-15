# HVE Chief of Staff Bootstrap Handoff and Checkpoint

**Date:** 2026-09-15  
**Owner:** Luna, HVE head architect and CTO  
**Human:** Hans Westphal  
**Status:** Step 2 complete; paused before Step 3  
**Primary tracker:** HVE knowledge-and-operations issue #40

## Objective

Create the canonical `hve-chief-of-staff` agent instance from
`hermes-agent-template`, preserve the existing Chief of Staff capabilities,
separate source from live runtime state, and remove active dependencies on
retired or predecessor codebases.

The approved fleet order remains:

1. `hve-chief-of-staff`
2. `hve-librarian`
3. `hve-coder-jr`

## Completed steps

### Step 1 — Freeze and classify

Completed non-destructively against:

```text
/home/hans/.hermes/profiles/hve-chief-of-staff
```

No profile files, services, schedules, databases, credentials, or runtime state
were changed. The profile was inventoried as a mixed live runtime directory of
approximately 150 MB containing source candidates, generated configuration,
mutable databases, credentials, logs, caches, sessions, backups, bundled
dependencies, and temporary state.

Confirmed boundary findings:

- The profile has no Git repository.
- `whatsapp/session` is a symlink into
  `/home/hans/.hermes/profiles/hanshermesagent/whatsapp/session`.
- Chief of Staff configuration and skills reference
  `/home/hans/hve-life-os-alpha`; this must be classified as an approved
  platform dependency or replaced with a repository-owned interface.
- Mutable databases, `.env` files, `auth.json`, logs, caches, locks, sessions,
  and generated artifacts must remain outside the source repository.
- The active Proton worker remains under `/home/hans/hanshermesagent`; this is
  primarily Librarian migration residue and must be resolved in the Librarian
  phase.

### Step 2 — Bootstrap repository

Created the private canonical repository:

```text
https://github.com/humanvalueexchange/hve-chief-of-staff
```

It was bootstrapped from the exact approved template baseline:

```text
humanvalueexchange/hermes-agent-template@37f9f4e4ff5cbfe0d9c1d3e318329ade6c1539e3
```

Remote baseline:

- Branch: `main`
- Commit: `37f9f4e4ff5cbfe0d9c1d3e318329ade6c1539e3`
- Visibility: private

The repository contains the pinned template contract, including
`AGENT_CARD.md`, `PROFILE.yaml`, `RELEASE.yaml`, README, identity, charter,
permissions, tools, deployment documentation, and validation suites.

The clean bootstrap checkout passed:

- profile contract checks;
- memory checks;
- isolation checks;
- portability checks;
- rollback contract checks;
- v0.6.1 release gates;
- full template suite: **167 tests passed**.

The bootstrap intentionally retains the validated generic template identity.
Chief of Staff specialization is deferred to Step 3 so the initial repository
remains a clean, independently validated template baseline.

## Step 3 starting boundary

Step 3 is the controlled source/runtime reconciliation. It must:

1. Select repository-owned identity, scripts, skills, schedules, configuration
   templates, deployment manifests, tests, and documentation from the frozen
   profile inventory.
2. Keep databases, locks, logs, caches, credentials, sessions, generated
   reports, backups, and historical evidence outside Git.
3. Adapt the template identity to `hve-chief-of-staff` while preserving the
   template validation contract.
4. Add HVE-specific adapter and profile configuration without embedding secrets
   or private runtime state.
5. Resolve or explicitly approve the `hve-life-os-alpha` dependency.
6. Remove the WhatsApp symlink dependency on `hanshermesagent` through a
   reversible migration path.
7. Add deployment provenance tying the live profile to an exact repository
   commit and rollback commit.
8. Validate from a clean checkout before any live profile reconciliation.

No live cutover, destructive cleanup, predecessor-state deletion, or service
restart is authorized by this checkpoint.

## Traceability

- Fleet completion issue: #40
- Approved completion path:
  `agent-communications/2026-09-15-hve-chief-of-staff-fleet-instance-completion-path-v1.0.md`
- Chief of Staff migration issue: #16
- LifeOS/Hermes architecture issue: #18
- Repository: `humanvalueexchange/hve-chief-of-staff`
- Bootstrap commit:
  `37f9f4e4ff5cbfe0d9c1d3e318329ade6c1539e3`

## Resume instruction

When resuming, read issue #40 and this checkpoint first. Do not repeat Steps 1
or 2 unless remote verification shows the repository or evidence is missing.
Begin with Step 3 source/runtime reconciliation from the frozen inventory.

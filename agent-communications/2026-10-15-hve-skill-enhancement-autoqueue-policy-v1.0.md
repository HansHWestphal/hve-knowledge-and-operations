# HVE Skill-Enhancement Auto-Queue Policy

- **Date:** 2026-10-15
- **Version:** 1.0
- **Status:** Approved
- **Decision owner:** Hans Westphal, CEO
- **Approval:** Hans explicitly approved this bounded policy on 2026-10-15.
- **Effective date:** 2026-10-15
- **Review date:** 2026-10-19
- **Implementer:** HVE-Coder-Jr

## Decision

HVE-COS and HVE-Librarian may submit eligible skill enhancements directly to
HVE-Coder-Jr's shared queue. The Jr gateway policy-authorizes and queues each
eligible request without a separate per-job human approval. This is a bounded
execution authorization, not approval to adopt or publish the resulting skill.

The policy applies only to profile-bound callers:

| Caller | Canonical repository |
|---|---|
| `hve-chief-of-staff` | `humanvalueexchange/hve-chief-of-staff` |
| `hve-librarian` | `humanvalueexchange/hve-librarian` |

## Eligibility and safeguards

Every request must:

- be `skill.enhance` for the caller's registered repository;
- target only the exact allowlisted `skills/*/SKILL.md` paths;
- include a non-empty purpose, task, and acceptance criteria;
- include a `candidate_contract` whose file set exactly matches the allowlist;
- pass read-only contract preflight against the staged repository baseline
  before queue creation; and
- be limited to one isolated attempt.

The queue atomically records `candidate` → `approved` → `queued`. Its approval
event records the policy ID and version, policy actor, approval reference,
authorization time, candidate-contract SHA-256, and preflight summary. Missing
staged repositories, stale baselines, malformed contracts, and failed
preflight reject the request before it is queued.

## Promotion boundary

HVE-Coder-Jr may return an isolated candidate and validation evidence only.
This policy does not authorize commit, push, publication, adoption, deployment,
or writes to a live profile. Those actions remain separately human-gated.
Nightly generation, automatic retries beyond the single attempt, and automatic
promotion are excluded.

## First application

Apply this policy once to the already-submitted HVE-COS request
`hve-chief-of-staff-x333-insight-math-candidate-v1.1-2026-10-15-0001` after
verifying its current queue record, caller, repository, path, contract, and
lifecycle state. The prior submission report stated `proposal` / `candidate`,
attempt `0` of `1`; that report is historical until the live queue is checked.
Do not resubmit the request or apply the policy to any other existing
candidate.

This artifact records the explicit CEO approval and policy scope; it does not
claim that the first candidate has been queued or executed.

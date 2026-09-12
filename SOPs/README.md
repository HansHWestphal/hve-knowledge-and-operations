# HVE Standard Operating Procedures

This is the GitHub landing page and index for approved HVE operating
procedures. Use this directory as the canonical, easy-to-find home for SOPs
that govern repeatable work across HVE and the DGX Spark.

## SOPs

| SOP | Owner | Effective | Status |
|---|---|---:|---|
| [HVE Spark Coding Task SOP v1.1](./2026-09-11-hve-spark-coding-task-sop-v1.1.md) | Luna, CTO | 2026-09-11 | Adopted |
| [HVE Spark Coding Task SOP v1.0](./2026-09-11-hve-spark-coding-task-sop-v1.0.md) | Luna, CTO | 2026-09-11 | Superseded |

## How to add a future SOP

1. Draft the SOP as a dated, versioned Markdown document in this directory.
2. Use the filename pattern:
   `YYYY-MM-DD-hve-[topic-slug]-sop-vX.X.md`
3. Include owner, decision authority, status, effective date, scope, approval
   gates, evidence requirements, and change-control rules.
4. Obtain the required owner or Hans approval before describing the SOP as
   adopted.
5. Add the approved document to the table above in the same commit.
6. Preserve prior versions for provenance; publish revisions as new versioned
   documents rather than silently overwriting history.

Drafts remain clearly marked as proposed and must not be presented as active
policy. GitHub is the system of record for adopted SOPs.

Version 1.1 adds a mandatory safe-pause and resume protocol for live tasks,
dirty user changes, uncertain repository ownership, and unclear rollback
authority. It is the active version.

## Related operating records

Historical planning notes and agent communications remain in
[`agent-communications/`](../agent-communications/). The canonical current
SOP is the document linked above; the communications directory contains the
historical publication context and decision trail.

## Runbooks

| Runbook | Owner | Status |
|---|---|---|
| [HVE Spark Hermes User-Session Supervision Runbook v1.0](./2026-09-12-hve-spark-hermes-user-session-supervision-runbook-v1.0.md) | Luna, CTO | Approved for operational use |

Runbooks document concrete operational procedures for the Spark Hermes
infrastructure. Use the same dated, versioned Markdown convention as SOPs,
preserve prior versions, and publish approved changes to GitHub as the system
of record.

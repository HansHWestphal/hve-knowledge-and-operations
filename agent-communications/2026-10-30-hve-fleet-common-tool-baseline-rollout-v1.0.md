# HVE Fleet Common Tool Baseline — Rollout Plan

- **Date:** 2026-10-30
- **Version:** v1.0
- **Status:** Approved implementation plan; pending PR review and merge
- **Decision owner:** Hans Westphal, CEO
- **Implementation owner:** Luna, CTO / Head Architect
- **Pilot cohort:** `hve-chief-of-staff`, `hve-librarian`, `hve-cfo`
- **Classification:** Internal operational design; no credentials, private data, or runtime state

## 1. Purpose

Establish one governed common non-channel tool baseline for HVE-COS,
HVE-Librarian, and HVE-CFO while preserving profile-specific authority,
channel, data-root, privacy, financial, and approval boundaries.

This document governs the rollout. It does not itself modify Hermes profiles,
install plugins, change live services, or declare deployment complete.
Implementation changes belong in the owning Hermes/profile repositories and
must be validated there before production activation.

## 2. Common baseline

The pilot profiles should expose the same approved baseline of registered
non-channel capabilities:

| Capability group | Baseline scope |
|---|---|
| Filesystem | Read, write, search, and bounded file-management operations |
| Execution | Terminal/command execution and process management |
| Editing | Patch and bounded file-edit operations |
| Web and UI | Browser and computer-use operations |
| Operations | Kanban and task-management operations |
| Documents and data | Registered PDF, DOCX, XLSX, CSV, and related MCP tools |

`delegate_task` is excluded from this baseline because the current fleet
availability record explicitly states that it was not present in the observed
common schema. New tools require separate catalog registration and validation.

## 3. Non-negotiable boundaries

- Tool availability does not grant action authority.
- Communication-channel access remains profile-governed.
- HVE-CFO retains its financial execution, filing, ledger-posting, private-data
  egress, and cross-profile restrictions.
- HVE-Librarian retains knowledge, provenance, and publication ownership.
- HVE-COS retains coordination, review, and decision-preparation ownership.
- Profile data roots and private runtime state remain isolated.
- Office Desk remains a separate proposed pilot and is not part of this rollout.
- No production deployment is claimed until the owning repositories and live
  profile state have independently passed validation.

## 4. Implementation sequence

### Phase 0 — Catalog and inventory

1. Define the canonical tool catalog entries, schemas, versions, owners, and
   risk classification.
2. Capture the current declared tool surface and `tool_filter` for each pilot
   profile.
3. Produce a gap matrix for missing, duplicate, stale, or over-permissive
   tools.
4. Record the rollback configuration for each profile before editing it.

**Gate:** the catalog and gap matrix are complete, and no profile-specific
   restriction is lost in the proposed filters.

### Phase 1 — Shared registration

1. Register or normalize common tools once in the shared fleet catalog or
   established adapter layer.
2. Keep implementation changes in the owning Hermes/profile repositories;
   this KnowOps repository records the contract and evidence only.
3. Pin tool definitions and versions for the pilot validation window.

**Gate:** each tool has one canonical registration and an identified owner.

### Phase 2 — Profile enablement

Enable the common baseline in this order:

1. `hve-chief-of-staff`
2. `hve-librarian`
3. `hve-cfo`

Apply the profile-specific allowlists after the common set is present. Do not
enable communication channels or authority beyond the existing profile policy.

**Gate:** each profile declares the expected common surface and retains its
   restricted operations.

### Phase 3 — Acceptance validation

For each profile, run and record:

- tool-schema and startup validation;
- successful filesystem, terminal, patch, process, browser/UI, Kanban, and
  registered document-tool smoke tests;
- denied cross-profile path and private-state access;
- denied restricted financial, channel, and authority actions;
- egress and credential-boundary checks;
- audit/receipt and error-reporting checks;
- rollback test or verified rollback readiness.

Any failed gate stops the fan-out and triggers rollback or a documented gap.

### Phase 4 — Promotion

After all three profiles pass:

1. Publish the evidence manifest and exact catalog revision.
2. Update the versioned fleet baseline reference.
3. Open separate follow-up work for any remaining fleet profiles.
4. Treat future tool additions as catalog changes requiring focused regression
   validation.

## 5. Acceptance criteria

The rollout is ready for Hans's deployment approval only when:

- all three profiles expose the same common baseline;
- profile-specific restrictions remain enforced;
- no cross-profile data access is possible through the common tools;
- no unapproved channel or external egress capability is introduced;
- all smoke, denial, isolation, and rollback checks have evidence;
- owning-repository changes are linked to the rollout issue and this artifact;
- the final live state is independently rechecked after activation.

## 6. Ownership and evidence

| Work | Owner |
|---|---|
| Baseline architecture and acceptance design | Luna |
| Profile implementation | Owning Hermes/profile repository maintainers |
| Knowledge/provenance review | HVE-Librarian |
| Coordination and decision-record linkage | HVE-COS |
| CFO boundary review | HVE-CFO owner, with Hans's approval |
| Final approval and production activation | Hans |

The 2026-10-25 fleet tool-availability policy is the governing input for this
plan. This rollout plan is an implementation artifact, not a replacement for
that policy or for the current approved decision ledger.

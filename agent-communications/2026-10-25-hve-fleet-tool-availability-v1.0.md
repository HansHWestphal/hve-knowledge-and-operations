# HVE Fleet Tool Availability Policy

- **Date:** 2026-10-25
- **Status:** Approved
- **Decision owner:** Hans Westphal, CEO
- **Recorded by:** Luna, HVE CTO / Head Architect

## Decision

Hans approved all currently registered **non-channel tools** in the shared HVE
fleet tool catalog as available to every HVE agent profile. This includes
general file tools, terminal, patch and process-management tools, browser and
computer-use tools, Kanban tools, and profile-specific tools when registered.

Communication-channel access and use remain governed separately by each
profile's channel policy. This decision does not enable a channel for a profile
whose policy disables it.

Tool availability is not authority to take an action. Existing role ownership,
data-root and cross-profile boundaries, privacy and egress rules, financial
action limits, approval requirements, and source-file protections remain in
force. Profile owners must make these boundaries clear even when a tool could
technically perform an out-of-scope action.

## Evidence and scope

On 2026-10-25, Hans reported the live HVE-CFO session's declared schema as 68
tools. The report included generic `read_file`, `write_file`, and `search_files`
tools, as well as terminal, patch, process-management, browser, computer-use,
and Kanban tools. It did not include `delegate_task`. This is evidence of the
session's declared schema, not independent functional or isolation validation.
Unregistered capabilities remain unavailable until implemented and registered.

## Supersession

This decision supersedes current fleet-level assumptions that generic
non-channel tools must be absent or denied by default. Historical decisions
and activation records are preserved for provenance; this approval does not
rewrite their record of the policy that applied when they were made.

For HVE-CFO, external channels remain disabled under its existing profile
policy. Financial execution, filing, ledger posting, private-data egress, and
cross-profile access remain outside this tool-availability decision.

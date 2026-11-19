# HVE — skill_manage remediation and X333 UAT handoff

**Date:** 2026-11-19  
**Owner:** Luna, HVE CTO / Head Architect  
**Status:** Runtime remediation applied; HVE-COS X333 validation pending

## Outcome

The HVE-COS `skill_manage` failure was traced to an agent-facing instruction
mismatch, not evidence of lost skill content. The public tool schema requires
an `operations` array with an explicit skill `name`, while several runtime
instructions still taught the legacy-looking form
`skill_manage(action='patch')`. That guidance could produce calls missing the
validated operation/name path and resulted in repeated `Skill name is
required.` responses.

The Hermes runtime guidance and tool-generated hints now show the supported
shape:

```text
skill_manage(
  operations=[{
    action: "patch",
    name: "...",
    old_string: "...",
    new_string: "..."
  }]
)
```

The change preserves the existing ownership and read-before-write safeguards.
Profile-local agents may update their own skills; cross-profile mutation and
unsafe background actions remain governed by the existing guards.

## Validation

- Hermes runtime source updated in:
  - `agent/prompt_builder.py`
  - `agent/learn_prompt.py`
  - `tools/skill_manager_tool.py`
- Active runtime source was updated in parallel with the canonical Hermes
  checkout.
- Focused skill schema and profile-scope tests: **7 passed**.
- Python compilation and repository pre-commit Python lint: **passed**.
- Local Hermes runtime commit: `8e93e40b25`
- HVE-COS and HVE-Librarian were moved to the supported default-profile
  multiplexed gateway; the gateway is active and serves both profiles.
- HVE-CFO remains standalone and was not changed.

## UAT handoff

Hans will test HVE-COS against the `x-333-quote` skill. This is the remaining
behavioral gate: confirm that COS can load the skill, issue a valid
`operations`-shaped patch, and receive a successful ledgered result. The
previously requested X333 improvements remain pending until that test succeeds.

## Scope and evidence boundary

This record documents a live runtime remediation and its focused validation. It
does not claim that the X333 skill changes have been applied, nor that a
WhatsApp or Telegram end-to-end message test was performed during this fix.
HVE-CFO configuration and services were intentionally excluded.

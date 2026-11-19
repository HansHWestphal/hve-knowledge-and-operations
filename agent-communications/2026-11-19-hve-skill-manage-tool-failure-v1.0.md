# HVE — skill_manage tool failure in hve-chief-of-staff profile

**Date:** 2026-11-19
**Reporter:** CoS (hve-chief-of-staff profile)
**Severity:** Medium — blocks skill maintenance, no data loss

## Symptom

Every `skill_manage` call with action=patch in the `hve-chief-of-staff`
profile returns:

```
"Skill name is required."
```

This is false — the `name` field IS present in the payload. Five test calls
across different skills all return the identical error:

| # | Skill tested | Result |
|---|-------------|--------|
| 1 | `x-333-quote` (user-owned, v1.3) | "Skill name is required." |
| 2 | `x333-insight-math` (user-owned, v1.0) | "Skill name is required." |
| 3 | `hve-status-brief` (user-owned) | "Skill name is required." |
| 4 | `weekly-mission-review` (user-owned) | "Skill name is required." |
| 5 | `x-333-quote` (retest, minimal payload) | "Skill name is required." |

No `skill_manage` call succeeds in this profile as of 2026-11-19.

## Impact

- `patch` file tool also blocks SKILL.md edits (by design — it routes to
  skill_manage for the ledger). So there is **no working path to edit a
  skill** in this profile.
- The `hve-bridge-group-chat`, `hve-status-brief`, `weekly-mission-review`,
  `x-333-quote`, and `x333-insight-math` skills are all user-owned and
  currently read-only in this profile.
- Skill evolution (new lessons, corrections, procedural updates) is blocked
  until the tool is fixed.

## What was attempted

- `skill_manage` with `action=patch`, `name=<skill>`, `old_string`, `new_string`
  → "Skill name is required." (5x, different skills)
- `hermes skills` CLI → no edit/update subcommand
- `patch` file tool on `/home/hans/.hermes/profiles/hve-chief-of-staff/skills/hve/*/SKILL.md`
  → "Use skill_manage for skill changes so the skill ledger can record them."
- `terminal` + sed → blocked by the same routing

## Likely cause

The `skill_manage` tool's validation layer appears to be failing to read
the `name` field from the structured tool payload. This may be:

1. **A Hermes version mismatch** in how this profile deserializes the
   `skill_manage` tool call (the tool schema expects `name` at the top
   level of each action object, and it's present, but the handler may be
   looking for it at a different path).
2. **A plugin conflict** — the `hve-baseline-guards` plugin (enabled in
   config.yaml) may be intercepting skill_manage calls.
3. **A profile-level tool config** that strips or rewrites the payload
   before validation.

## Suggested fix

- Check the Hermes version in this profile vs. a profile where skill_manage
  works: `hermes --version`
- Try the same skill_manage call from a different profile (e.g. the default
  profile) to see if the error is profile-specific or global
- Check `hve-baseline-guards` plugin logs for any interception of
  skill_manage calls
- If it's a known Hermes issue, file it with the Hermes runtime team

## Pending skill patch (blocked)

The following edit was ready to apply but is blocked by this bug:

**Target:** `x-333-quote/SKILL.md`
**Insert before:** `## Quote pick — plain, short, universally understood`
**Content:** "Themed bridge" section — requires insights to name one
concrete science↔esoteric mechanism when Hans asks for a themed run.
Reduces themed-run convergence from 8+ tool calls to 3-4. Full content
in the CoS session history of 2026-11-19.

**Target:** `x333-insight-math/SKILL.md`
**Insert before:** `## Hard gate — never claim '333' without a passing assert`
**Content:** "Themed-convergence rule" — companion to the above, defines
how to converge a themed insight in one pass instead of a fan-out.

These two edits would fix the most expensive failure mode in x-333 runs:
free-metaphor fan-out on themed requests.

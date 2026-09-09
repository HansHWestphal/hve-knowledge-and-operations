# HVE Daily Skill Recommendation Cron - Reasoning and Timeout Update

**Date:** 2026-08-30
**Owner:** Hermes-coder
**Status:** Completed

## Issue

The `hve-daily-skill-recommendation` Cron job
(`c6895f6b9552`) failed after the local Qwen provider timed out twice and
Hermes fell back to Copilot. The live profile supplied `reasoning_effort:
minimal`, which is not supported by the fallback GPT-5 models.

The repository template already specified `low`; the live profile had drifted
to `minimal`. The skill prompt and research workflow were not the direct cause.

## Fix

- Restored the global `hanshermesagent` reasoning setting to `low`.
- Pinned the daily skill recommendation job to `reasoning_effort: high`.
- Set the gateway Cron and API stale budgets to 600 seconds.
- Restarted the gateway with the updated runtime environment.

The higher effort is intentionally limited to this overnight research job so
normal Hermes conversations and other scheduled jobs retain the lower default.

## Verification

- Gateway restarted and remained active.
- The target job completed successfully when triggered manually.
- The job used the configured local `qwen3.8-hermes:27b-128k` model.
- The generated WhatsApp-ready recommendation was saved and delivered.
- The job failure streak returned to zero.
- The next scheduled run remains 03:00 America/Toronto.

## Runtime boundary

The live Hermes profile and systemd override are operational files outside this
repository. This record documents the approved runtime change and outcome;
secrets and live configuration are not committed here.

# HVE Event Monitoring and Triage Plan

**Date:** 2026-09-03  
**Owner:** Luna, HVE head architect and CTO  
**Status:** Proposed for Hans review  
**Scope:** Spark health watcher findings and related Hermes platform reliability events

## Purpose

Record a proposed change to operational alert handling: retain all useful
health-watcher evidence in a local SQLite reliability store, while reserving
WhatsApp for sustained user-impacting incidents. This plan is not yet an
approved policy and does not authorize implementation or runtime changes.

## Problem

Short-lived Telegram reconnects, stale gateway metadata, and similar warnings
can self-heal without affecting service delivery. Sending each event to Hans
through WhatsApp creates alert fatigue and makes genuinely urgent incidents
harder to identify. Discarding the events would lose the evidence needed to
diagnose recurring reliability patterns.

## Proposed routing model

| Event class | SQLite | WhatsApp |
|---|---:|---:|
| Self-healing advisory | Record and increment | No |
| Repeated but recovered | Record and trend | Weekly review digest only |
| Sustained user-impacting failure | Record and escalate | Immediate alert |
| Recovery from sustained failure | Update and close | Recovery notice |

The current Librarian Telegram `httpx.ReadError` and fallback-path warnings
would initially be recorded as monitoring events when recovery completes within
the retry window. They would be promoted only after configurable thresholds
such as repeated occurrences, excessive recovery duration, repeated failed
watcher cycles, failed outbound delivery, or a channel remaining disconnected
beyond its service threshold.

## Proposed event record

Each normalized event would use a stable fingerprint and retain:

- event identifier, fingerprint, profile, and subsystem;
- first seen, last seen, occurrence count, and recovery duration;
- severity, operational impact, and lifecycle state;
- sanitized exception class and diagnostic detail;
- protocol, remote address, interface, and connection age when available;
- owner, review status, rationale, and next review date.

Credentials, tokens, message bodies, runtime secrets, and unbounded raw logs
must not be written to the database.

## Ingestion contract

The watcher would update SQLite transactionally:

1. Create a new fingerprint record or increment an existing one.
2. Append a bounded occurrence record for trend analysis.
3. Record recovery when an active event disappears.
4. Commit the evidence before attempting notification.

A database write failure must remain visible as a watcher failure; it must not
fall back silently to a healthy result. Runtime database and evidence files
remain outside this knowledge repository.

## Weekly review

A separate Hermes no-agent weekly cron job would review events opened or
updated since the prior review. It would group events by fingerprint, profile,
subsystem, severity, frequency, duration, and recovery rate, then produce a
short decision queue:

- continue monitoring;
- investigate;
- escalate;
- resolved; or
- won't fix.

The review would write a durable decision record containing reviewer, date,
rationale, owner, and next review date. WhatsApp would be used only for a
material decision or escalation, not as a transcript of every warning.

## Rollout gates

1. **Shadow mode:** write and classify events while preserving current alerts.
2. **Measurement:** compare event volume, duplicates, recovery timing, and
   missed escalations.
3. **Routing cutover:** suppress short-lived advisory WhatsApp alerts.
4. **Weekly review activation:** publish the review queue and decisions.
5. **Threshold tuning:** adjust from observed evidence over several weeks.
6. **Documentation:** record schema, retention, thresholds, cron ownership,
   escalation rules, and rollback procedure.

## Review request

Hans review is requested before implementation begins, especially for:

- the immediate-alert and promotion thresholds;
- weekly review timing and recipient;
- SQLite location and retention period;
- event ownership and escalation responsibility; and
- whether the initial rollout should cover only the Spark watcher or all
  Hermes platform reliability events.


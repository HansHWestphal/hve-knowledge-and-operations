# HVE Event Monitoring and Triage - Active Operating Process

**Date:** 2026-09-03  
**Owner:** Luna, HVE head architect and CTO  
**Status:** Approved and operational  
**Supersedes:** `2026-09-03-hve-event-monitoring-triage-v1.0.md`

## Operating decision

The Spark health watcher continues to run every 30 minutes and evaluates all
declared health surfaces. Findings are retained in evidence and the local
SQLite reliability store, but WhatsApp is now reserved for events requiring
Hans's attention.

Routine advisories, repeated self-healing warnings, stale metadata, and
non-critical scheduler findings do not interrupt WhatsApp. Required-channel
disconnects, failed outbound delivery, sustained failures, and promoted
actionable events do. Recovery notices are sent only for incidents that were
previously escalated.

The active Hans route is:

`whatsapp:98938950533173@lid`

## Monday weekly event review

The no-agent review runs every Monday at **07:15 America/Toronto time** from
the prior Monday-Sunday period. It reads the reliability database and records
review decisions without restarting services or changing production
configuration.

The review should accomplish the following:

1. Confirm the review period, database integrity, watcher execution continuity,
   and any ingestion failures.
2. Rank event families by user impact first, then severity, frequency, duration,
   recurrence trend, and recovery behavior.
3. Separate true service incidents from self-healing transport noise,
   observability freshness issues, and known/non-actionable warnings.
4. Review open `escalated` and `monitoring` events, including owners and next
   review dates.
5. Decide each material event as `investigate`, `escalate`, `resolved`,
   `continue monitoring`, or `won't fix`.
6. Record rationale, evidence boundaries, owner, and follow-up date in the
   review ledger.
7. Send a bounded WhatsApp report only when the review produces material
   `investigate` or `escalate` decisions.

## Expected weekly report

When material findings exist, the WhatsApp report should contain:

- review period and database status;
- count of event families and occurrences;
- top material findings ranked by impact;
- recurring advisory trends retained for monitoring;
- decisions, owners, and next actions;
- recovery or closure items; and
- exact evidence/database references when useful.

When no material findings exist, the review remains recorded in SQLite and
WhatsApp remains silent.

## Current first-week focus

The first review should pay particular attention to:

- Librarian Telegram reconnect frequency and recovery duration;
- repeated `httpx.ReadError`, fallback-path, and polling warnings;
- stale gateway metadata age and whether it reflects an observability gap;
- non-critical cron failure streaks and whether they affect required work; and
- any required-channel or outbound-delivery failures.

The review must not treat a warning as an outage when live service, process,
channel, and delivery checks pass. It should promote an event only when the
stored evidence demonstrates sustained or user-visible impact.

## Evidence and authority

The operational implementation is maintained in the `hanshermesagent`
repository. Runtime database, credentials, session state, and raw evidence
remain host-local and are not committed to the knowledge repository. This
communication records the approved operating process; future threshold or
ownership changes require an updated versioned communication.


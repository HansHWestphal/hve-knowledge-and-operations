# Event Monitoring and Triage

**Status:** Proposed design - implementation requires Hans review  
**Owner:** HVE head architect and CTO  
**Related communication:** `agent-communications/2026-09-03-hve-event-monitoring-triage-v1.0.md`

## Operating objective

Keep operational evidence durable without turning every recoverable warning
into a WhatsApp interruption. The watcher remains responsible for collecting
read-only health evidence; SQLite becomes the reliability review queue; Hermes
WhatsApp remains the escalation path for sustained user impact.

## Event lifecycle

Normalized findings use stable fingerprints and move through these states:

```text
new -> monitoring -> escalated -> resolved
                    \-> wont_fix
```

An event can remain in `monitoring` while it recurs and self-heals. A recovery
must be recorded rather than deleting the event. Severity changes, sustained
impact, and failed delivery can promote an event to `escalated`.

## Minimum data model

The implementation should provide an event summary table, an occurrence table,
and a review ledger.

### Event summary

```text
fingerprint
event_type
profile
subsystem
first_seen
last_seen
occurrence_count
severity
impact
state
recovery_duration_seconds
owner
next_review_at
```

### Occurrence

```text
fingerprint
observed_at
sanitized_detail
exception_class
protocol
remote_ip
interface
connection_age_seconds
recovered_at
```

### Review ledger

```text
fingerprint
reviewed_at
reviewer
decision
rationale
owner
next_review_at
```

Secrets, credentials, message bodies, and unrestricted raw log content are
excluded. Database integrity checks, bounded occurrence retention, and explicit
write-error reporting are required.

## Routing rules

| Condition | Action |
|---|---|
| One short-lived, self-healed warning | Store; no WhatsApp |
| Repeated recovered warnings | Store and aggregate for weekly review |
| Failure beyond the configured impact window | Store and alert WhatsApp |
| Failed delivery or disconnected required channel | Store and alert WhatsApp |
| Recovery after an escalated incident | Close and send recovery notice |

Thresholds must be configuration, not undocumented constants. The first
implementation should use conservative defaults and support later tuning from
review evidence.

## Weekly review job

The weekly job should be a separate Hermes no-agent cron entry. It must:

1. Read events opened or updated since the previous review.
2. Group and rank them by impact, severity, frequency, and duration.
3. Present a bounded decision queue.
4. Write review decisions and next-review dates.
5. Send WhatsApp only for material escalations or decisions.

It must not restart gateways, alter network configuration, or mutate
production services. Its writes are limited to the reliability database and
review ledger.

## Rollout and rollback

Deploy in shadow mode first, measure false suppression and missed escalation,
then enable advisory suppression. Rollback must be a configuration change that
restores the previous WhatsApp routing while retaining all SQLite evidence.

This document remains a proposal until the associated Agent Communications post
is reviewed and approved. No runtime database, cron entry, or threshold change
has been created by documenting this plan.

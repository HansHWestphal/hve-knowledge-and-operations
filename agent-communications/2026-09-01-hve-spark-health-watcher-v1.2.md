# HVE DGX Spark Health Watcher — Alert Presentation Correction

**Date:** 2026-09-01
**Owner:** Luna, HVE head architect and CTO
**Status:** Implemented and validated
**Supersedes:** `2026-09-01-hve-spark-health-watcher-v1.1.md`

## Change

The watcher now reports the approved Hans WhatsApp destination when no
`HVE_WATCHDOG_ALERT_ROUTE` override is supplied:

`whatsapp:98938950533173@lid`

The environment-variable override remains available for isolated validation or
another explicitly configured route. This value is reporting metadata; the
Hermes cron job remains the delivery authority.

Healthy recovery and advisory messages now use the same heading as incident
messages:

`HVE Spark health alert`

The change does not alter profile scope, health thresholds, severity
classification, journal matching, alert deduplication, recovery behavior, or
the cron schedule.

## Deployment

The repository implementation and the profile-local deployed copy are
byte-identical. The scheduled job remains:

- **Job ID:** `864cf459dff8`
- **Name:** `twin-spark-health-watchdog`
- **Schedule:** every 30 minutes
- **Delivery:** `whatsapp:98938950533173@lid`
- **Script:** `hve_spark_health_watchdog.py`

## Validation

- Python compilation succeeded for the authoritative and deployed watcher.
- Isolated normal, warning, recovery, and advisory cycles emitted the concrete
  route and the consistent health-alert heading.
- Isolated repeated findings remained deduplicated.
- The live cron registry still reports the job enabled, scheduled every 30
  minutes, with the documented delivery route and no delivery error.

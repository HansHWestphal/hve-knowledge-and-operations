# HVE DGX Spark Health Watcher - Deployment Copy Clarification

**Date:** 2026-09-03
**Owner:** Luna, HVE head architect and CTO
**Status:** Confirmed operational state
**Supersedes:** `2026-09-01-hve-spark-health-watcher-v1.2.md`

## Finding

The apparent watcher deployment mismatch was investigated against the live
Hermes cron registry and all three known script copies.

The repository implementation and the active profile-local deployment are
byte-identical:

```text
SHA-256: d1a826714a11003b08f7fe490bf6ed65cea0b50a05b2c8511bed1fef5d8daec4
```

The active cron job is:

- **Job ID:** `864cf459dff8`
- **Name:** `twin-spark-health-watchdog`
- **Schedule:** every 30 minutes
- **Workdir:** `/home/hans/.hermes/profiles/hanshermesagent`
- **Script:** `hve_spark_health_watchdog.py`
- **Delivery:** `whatsapp:98938950533173@lid`

Hermes resolves the script basename from the profile workdir, so the live
deployment is:

```text
/home/hans/.hermes/profiles/hanshermesagent/scripts/hve_spark_health_watchdog.py
```

The job is enabled, on time, and completing successfully.

## Legacy shared copy

The following older copy remains on the host:

```text
/home/hans/.hermes/scripts/hve_spark_health_watchdog.py
```

Its SHA-256 is:

```text
958f4a694d90e088d0d7f330c2b72a963772a092850ff94bcc82d42c22b5847c
```

This copy predates the profile-local deployment corrections and is not
referenced by the active cron job. It is a stale legacy artifact, not a second
active watcher. It should not be used as a deployment source.

## Operational decision

No runtime repair or cron change is required. The repository artifact and the
profile-local deployed copy are aligned, and the active job remains the
deployment authority.

Optional cleanup of the unused shared copy requires a separate, explicit
host-side operation. Until then, it remains preserved for provenance and must
not be mistaken for the active implementation.

## Evidence

- Live cron registry inspection on 2026-09-03.
- Successful recent executions of job `864cf459dff8`.
- SHA-256 comparison of repository, shared, and profile-local copies.
- Confirmed active workdir and Hermes profile-local script resolution.

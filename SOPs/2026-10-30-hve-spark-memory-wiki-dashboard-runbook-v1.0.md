# HVE Spark Memory Wiki Dashboard Runbook

- **Date:** 2026-10-30
- **Version:** 1.0
- **Status:** Deployed and enabled; host-reboot behavior not yet tested
- **Owner:** Luna, HVE CTO / Head Architect
- **Decision authority:** Hans Westphal, CEO
- **Host:** `spark-5054`

## Purpose and scope

Keep the existing local Hermes Memory Wiki dashboard available through a
systemd user service instead of an open shell command. The service uses the
HVE-CFO profile to host the already-approved Memory Wiki installation. The
dashboard intentionally presents the all-profile selector; that does not
mean non-CFO session histories were inspected or that other profiles were
changed.

The Memory Wiki backend is read-only. This service does not install or enable
the plugin in COS, Librarian, or any other profile, and it does not modify
profile databases. Keep the dashboard bound to loopback; do not expose it on
the LAN or public network.

## Deployed service

- **Unit:** `hermes-memory-wiki.service`
- **Unit file:** `/home/hans/.config/systemd/user/hermes-memory-wiki.service`
- **Profile:** `hve-cfo`
- **Plugin:** `hermes-memory-wiki` v1.1.0, catalog commit
  `54afaf5014db23346148436c4883eb64095e8060` (per the 2026-10-28 UAT record)
- **Working directory:** `/home/hans/humanvalueexchange`
- **Listener:** `127.0.0.1:9119`
- **Wiki URL:** `http://127.0.0.1:9119/memory-wiki`
- **Dashboard auth gate:** unauthenticated Memory Wiki API requests return
  HTTP 401.
- **Startup:** enabled under the per-user `default.target`; user lingering is
  enabled so the user manager can run without an interactive login.
- **Restart policy:** `on-failure`, with a five-second delay and systemd start
  rate limiting.
- **Logs:** systemd user journal.

The launch command is:

```bash
/home/hans/.local/bin/hermes --profile hve-cfo dashboard \
  --host 127.0.0.1 --port 9119 --isolated --no-open
```

This preserves the current HVE-CFO profile context, local bind, port, and
dashboard mode. The service runs as the `hans` user, not as root.

## Health checks

Check that systemd owns an enabled, active unit:

```bash
systemctl --user status hermes-memory-wiki.service --no-pager
systemctl --user is-enabled hermes-memory-wiki.service
```

These commands verify service state and whether it is configured to start with
the user manager.

Check that the only listener is loopback:

```bash
ss -ltnp 'sport = :9119'
```

The local address must be `127.0.0.1:9119`, not `0.0.0.0` or a LAN address.

Check the Wiki page and unauthenticated API gate:

```bash
curl --max-time 5 -sS -o /dev/null -w 'HTTP %{http_code}\n' \
  http://127.0.0.1:9119/memory-wiki
curl --max-time 5 -sS -o /dev/null -w 'HTTP %{http_code}\n' \
  http://127.0.0.1:9119/api/memory-wiki
```

The page should return HTTP 200; an unauthenticated API request should return
HTTP 401. Do not weaken the authentication gate to make a client connect.

Restart the dashboard service after an approved local configuration change:

```bash
systemctl --user restart hermes-memory-wiki.service
```

Afterward, repeat the unit, listener, page, and API checks above. A successful
service restart was verified on 2026-10-30; the Spark itself was not rebooted
for this deployment.

Inspect service-only logs when troubleshooting:

```bash
journalctl --user -u hermes-memory-wiki.service -n 100 --no-pager
```

Review logs for operational errors only. Do not copy session contents or
financial details into an incident report; the deployment check observed
startup/readiness messages only, not a full log-retention audit.

## Access and evidence boundaries

- The all-profile selector is intentional for this Memory Wiki installation,
  per the 2026-10-28 HVE-CFO UAT record.
- The UAT verified HVE-CFO history visibility and profile-list visibility.
  Non-CFO history contents were not opened or tested.
- The plugin is installed under HVE-CFO. Do not infer that other agents have
  the plugin enabled or that their memory access has been validated.
- The read-only plugin and the loopback/auth checks do not prove complete
  profile database isolation, retention safety, or fleet readiness.
- The dashboard is local to the Spark. Remote access is out of scope; if later
  approved, use a separately reviewed access design rather than a public bind.

## Rollback

Stop and disable only this user service:

```bash
systemctl --user disable --now hermes-memory-wiki.service
```

This stops the managed dashboard and removes its automatic-start link without
disabling the Memory Wiki plugin or changing any profile database.

If temporary dashboard access is still required, confirm port 9119 is free and
run the same launch command from the `hans` account:

```bash
/home/hans/.local/bin/hermes --profile hve-cfo dashboard \
  --host 127.0.0.1 --port 9119 --isolated --no-open
```

This restores the prior shell-owned mode. Do not use the global
`hermes dashboard --stop` command for rollback because it can stop other
Hermes dashboard processes.

Do not delete or restore `state.db`, memory files, snapshots, or plugin files
as part of service rollback. Plugin disablement or removal requires separate
approval.

## Deployment evidence

On 2026-10-30, the service was enabled and started under the user manager.
The listener was verified on `127.0.0.1:9119`, the Wiki page returned HTTP 200,
the unauthenticated API returned HTTP 401, and a controlled systemd restart
returned to active service state. `loginctl` reported `Linger=yes`. No
non-CFO history was opened, and no profile database contents were inspected.

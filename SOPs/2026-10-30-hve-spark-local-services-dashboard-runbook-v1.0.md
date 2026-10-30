# HVE Spark Local Services and Dashboard Runbook

- **Date:** 2026-10-30
- **Version:** 1.0
- **Status:** Live inventory snapshot; recheck before operational action
- **Owner:** Luna, HVE CTO / Head Architect
- **Decision authority:** Hans Westphal, CEO
- **Host checked:** `spark-5054`
- **Inventory time:** 2026-10-30

## Purpose and scope

This runbook records the Spark-local web applications, useful service
endpoints, active application services, and network bindings observed during
the read-only inventory on 2026-10-30. It is a dated snapshot, not a live
health monitor. Verify service state and access controls before relying on any
entry.

The static HVE-branded launcher is
[`../operational-artifacts/spark-landing-dashboard.html`](../operational-artifacts/spark-landing-dashboard.html).
Open it in a browser running on the Spark. Links using `127.0.0.1` refer to
the computer running that browser, not a remote workstation.

No service, firewall, Tailscale, systemd, or application configuration was
changed during this inventory.

## Host identity and network

- **Host:** `spark-5054`
- **OS / architecture:** Ubuntu 24.04.5 LTS, `aarch64`
- **GPU:** NVIDIA GB10; driver `580.178.04`
- **LAN address:** `192.168.1.10/24`
- **Tailscale address:** `100.85.145.63`
- **Default gateway:** `192.168.1.1`

The router page `http://192.168.1.1/start.html` is a separate network
appliance, not a Spark-hosted application. It was not opened or independently
checked.

## Application services observed active

### System services

| Unit | Function |
|---|---|
| `dgx-dashboard.service` | NVIDIA DGX Dashboard |
| `dgx-dashboard-admin.service` | NVIDIA DGX Dashboard administration component |
| `nginx.service` | Web server and reverse proxy |
| `tailscaled.service` | Tailscale network and Serve/Funnel |
| `open-webui.service` | Open WebUI |
| `ollama.service` | Ollama inference API |
| `hve-coder-runtime.service` | Shared vLLM inference runtime |
| `btcpayserver.service` | BTCPay Server |
| `hve-bitcoind.service` | Bitcoin node |
| `nbxplorer.service` | NBXplorer API |
| `lnd.service` | Lightning Network Daemon |
| `rtl.service` | Ride The Lightning |
| `hve-cfo-camofox.service` | HVE-CFO browser automation service |

### User services

The following user services were active: `hermes-memory-wiki.service`,
`hermes-gateway-hve-cfo.service`, `hermes-gateway-hve-chief-of-staff.service`,
`hermes-gateway-hve-librarian.service`, `hermes-coder-worker.service`,
`hermes-proton-worker.service`, `hve-coder-jr.service`, and
`hermes-browser.service`. These are agent, worker, or browser-support
components; their internal listeners are not separate dashboard pages.

The Docker daemon is active, but `docker ps` reported no running containers.

## Human-facing web applications

| Application | Address | Observed state and binding |
|---|---|---|
| NVIDIA DGX Dashboard | `http://127.0.0.1:11000/` | HTTP 200; loopback-only |
| Open WebUI | `http://192.168.1.10:8080/` | HTTP 200; listens on `0.0.0.0:8080`, so it may be reachable from the LAN subject to firewall and authentication |
| Hermes Memory Wiki | `http://127.0.0.1:9119/memory-wiki` | HTTP 200; loopback-only; unauthenticated plugin API returned HTTP 401 |
| Ride The Lightning | `http://127.0.0.1:3010/` | HTTP 200; loopback-only |
| BTCPay Server | `https://spark-5054-1.tail3b0306.ts.net:8443/` | Nginx listens on the Spark's Tailscale address and proxies to `127.0.0.1:23000`; backend root redirected to the login page |
| Nginx default page | `http://192.168.1.10/` | HTTP 200, but serves the default “Welcome to nginx!” page; not an HVE dashboard |

Open WebUI's bind allows connections on all IPv4 interfaces; actual
reachability and authentication were not tested from another device. Do not
change its binding or infer its access policy from this inventory.

## Service APIs and non-dashboard endpoints

| Service | Address | Classification |
|---|---|---|
| Ollama | `http://127.0.0.1:11434/` | Local inference API; root returned HTTP 200 |
| Shared vLLM | `http://127.0.0.1:11435/` | Local inference API; root returned HTTP 404 JSON |
| NBXplorer | `http://127.0.0.1:24444/` | API; response identified as NBXplorer |
| BTCPay backend | `http://127.0.0.1:23000/` | Loopback backend proxied by Nginx on the Tailscale interface |
| Hermes COS child endpoint | `http://127.0.0.1:3000/` | HTTP 404; process belongs to the COS gateway unit, not a human-facing dashboard |
| Unidentified local HTTP endpoint | `http://127.0.0.1:8081/` | Returned HTTP 400; service identity was not established |
| Unidentified local JSON endpoint | `http://127.0.0.1:9377/` | Returned JSON; socket ownership was not established, so it is not linked as a dashboard |
| Local data services | `127.0.0.1:6379`, `127.0.0.1:5432` | Redis and PostgreSQL; not browser dashboards |
| Hermes and model-worker listeners | Various loopback ports | Internal service endpoints; several are dynamic and must not be treated as stable web links |

Bitcoin, Lightning, SSH, DNS, printing, and other system sockets are also
present. They are not dashboard links. During this check port `8333` listened
on all IPv4 interfaces and `8332` was loopback-bound; the non-HTTP response
did not establish socket ownership. Confirm port ownership and firewall
policy before changing or documenting external exposure.

## External and network links

These are navigation links, not Spark-hosted services:

- HVE website: `https://humanvalueexchange.com/`
- HVE blog: `https://humanvalueexchange.blog/`
- Grok: `https://grok.com/`
- X: `https://x.com/`
- Microsoft Office: `https://office.com/`
- Brave API Dashboard: `https://api-dashboard.search.brave.com/app/dashboard`
- GitHub: `https://github.com/`
- HVE x402 Watch: `https://hanshwestphal.github.io/x402-watch/`
- HVE Maps: `https://hanshwestphal.github.io/HVE-maps/`
- Amboss Magma: `https://magma.amboss.tech/buy`
- Amboss subscriptions: `https://account.amboss.tech/subscriptions`
- Starlink: `https://starlink.com/`
- Tailscale Admin Console: `https://login.tailscale.com/admin/machines`
- Router administration page: `http://192.168.1.1/start.html` (LAN gateway;
  not checked during the Spark inventory)

### Tailscale-hosted services

Tailscale was active during the inventory. BTCPay Server is available through
Nginx bound to the Spark's Tailscale address at
`https://spark-5054-1.tail3b0306.ts.net:8443/`; this requires an authorized
Tailscale connection. Its backend remains loopback-bound at
`http://127.0.0.1:23000/`.

Tailscale also reports Funnel enabled at
`https://spark-5054-1.tail3b0306.ts.net/`, proxying to
`http://127.0.0.1:3001`. Port `3001` had no listener during the inventory, so
this is not listed as an available dashboard destination. The public endpoint
was not tested.

## Exposure and verification caveats

- The Funnel mapping and missing local port `3001` listener are detailed in
  the Tailscale section above. Do not rely on the public URL until its target
  and access boundary have been reverified.
- The Spark's LAN interface had listeners on ports `22`, `80`, `8080`, and
  `8333`. This is socket-binding evidence only; firewall rules and reachability
  from another device were not tested.
- Systemd warned that on-disk unit definitions for the DGX Dashboard,
  dashboard admin, Nginx, Open WebUI, Ollama, and shared vLLM differed from
  the manager's loaded definitions. No `daemon-reload`, restart, or service
  change was performed. Reconcile this before future service maintenance.
- The user dashboard page is static: it does not probe health, authenticate,
  proxy requests, or change network access. Localhost links work only when
  opened in a browser on the Spark.

## Read-only recheck commands

Check active application units:

```bash
systemctl --no-pager --type=service --state=running
systemctl --user --no-pager --type=service --state=running
```

Check socket bindings:

```bash
ss -ltnp
```

Check the primary human-facing pages without displaying response bodies:

```bash
curl --max-time 5 -sS -o /dev/null -w 'DGX Dashboard HTTP %{http_code}\n' \
  http://127.0.0.1:11000/
curl --max-time 5 -sS -o /dev/null -w 'Open WebUI HTTP %{http_code}\n' \
  http://127.0.0.1:8080/
curl --max-time 5 -sS -o /dev/null -w 'Memory Wiki HTTP %{http_code}\n' \
  http://127.0.0.1:9119/memory-wiki
curl --max-time 5 -sS -o /dev/null -w 'RTL HTTP %{http_code}\n' \
  http://127.0.0.1:3010/
```

Repeat the bind, auth, and network-scope checks before describing an
application as secure or reachable. Do not restart services as part of a
read-only inventory.

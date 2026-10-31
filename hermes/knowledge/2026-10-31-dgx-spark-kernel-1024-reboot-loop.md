# DGX Spark: reboot loop with a monitor attached on kernel 7.0.0-1024-nvidia

**Type:** Hermes knowledge note (draft, for later placement at `hermes/knowledge/`)
**Prepared by:** HVE Knowledge Ops, for Hans Westphal and Luna (on-prem infrastructure)
**Research date:** 2026-10-31, about 8:50 AM EDT (Toronto)
**Status:** DRAFT, not committed. Not yet checked against the live Spark.
**Labels used:** FACT (an official NVIDIA or Canonical source, checked) · REPORTED (community forum post, not confirmed by NVIDIA) · UNVERIFIED (searched for and not found) · PROPOSAL (HVE recommendation) · ASSUMPTION

> Scope: This note covers the reboot and hard-reset reports that began on 2026-10-30, after the DGX Dashboard or apt upgraded DGX Spark systems from kernel 7.0.0-1019-nvidia to 7.0.0-1024-nvidia. Nothing here has been run on HVE's Spark yet. Its current kernel and state are unknown to this note.

## 1. Status as of 2026-10-31

| # | Claim | Label | Evidence |
|---|---|---|---|
| 1 | NVIDIA's current DGX Spark software table lists **DGX OS 7.6.0, GPU driver 580.178.04, kernel 7.0.0-1019**, UEFI 1.111.17, EC 3.13.7, SoC 2.158.15. It does **not** list 1024. | FACT | [DGX Spark Release Notes](https://docs.nvidia.com/dgx/dgx-spark/release-notes.html) |
| 2 | Canonical's `linux-nvidia-7.0` **7.0.0-1024.25~24.04.1** entered noble-proposed on 2026-10-23 and was published to **noble-updates on 2026-10-30 at 00:43 UTC (Oct 29, 8:43 PM EDT)**. No newer build (1025 or later) exists in proposed or updates. 1019 (`7.0.0-1019.19~24.04.2`) is in noble-security from 2026-09-15. | FACT | [Launchpad: linux-nvidia-7.0](https://launchpad.net/ubuntu/+source/linux-nvidia-7.0), Launchpad API `getPublishedSources` |
| 3 | An NVIDIA forum moderator replied "We will look into this kernel issue" (2026-10-30, 16:35 UTC) and asked for `nvidia-bug-report` output. A second thread was closed with "We are investigating this issue" and merged into the main thread. | FACT (NVIDIA staff post) | [Main thread #387397](https://forums.developer.nvidia.com/t/dgx-spark-repeatedly-rebooting-after-most-recent-update/387397), [idle-reset thread #387401](https://forums.developer.nvidia.com/t/dgx-spark-resetting-at-idle-after-latest-dgx-dashboard-update-kernel-7-0-0-1024/387401) |
| 4 | There is **no official fix, bug ID, known-issues entry or advisory** yet. The Known Issues page (updated Oct 21) does not mention it. | UNVERIFIED (searched, not found) | [Known Issues](https://docs.nvidia.com/dgx/dgx-spark/known-issues.html) |
| 5 | Driver **580.178.04 did not change** in the upgrade. Only the kernel and its rebuilt module packages changed. `dgx-dashboard` went from 0.39.3-4 to 0.39.3-5. | REPORTED (several users, with package versions) | #387397 posts 4, 16 |
| 6 | The symptom is a reboot or hard reset about every 30 seconds to 5 minutes with a monitor attached. It is **stable headless** for hours. | REPORTED (Founders Edition, Gigabyte, ASUS GX10, Dell Pro Max GB10) | #387397 posts 1, 8, 10 |
| 7 | Which port triggers it **varies**. One ASUS GX10 owner gets a hard reset only on HDMI (TMDS), at boot or on hot-plug, while USB-C/DP works. Another user resets on either HDMI or DP. A third was stable on HDMI only, then reset again later. | REPORTED | [#387456](https://forums.developer.nvidia.com/t/any-use-of-the-hdmi-tmds-output-causes-a-hard-reset-on-kernel-7-0-0-1024-nvidia/387456), #387397 posts 8, 14 |
| 8 | One user sees no panic or Xid. On shutdown they see "watchdog0: watchdog did not stop!", and the SBSA hardware watchdog resets the host. Others report Xid 13/154 (GSP "Reset Required"), SLUB corruption Oops, or idle resets. | REPORTED | #387397 posts 4, 16, 18; [#387497](https://forums.developer.nvidia.com/t/system-gets-frozen-from-time-to-time/387497); #387401 |
| 9 | **Booting 7.0.0-1019-nvidia resolves it** on every unit that tried. | REPORTED (≥6 users) | #387397 posts 4, 17, 23, 24; #387456 post 4; #387497 post 2 |
| 10 | The claim "DGX OS 7.6.0, driver 580.178.04" matches both the official table and the user reports. "October 2026 release" is the official release name, but that release ships kernel **1019**. 1024 arrived afterward, as an Ubuntu kernel update delivered through the Dashboard's system upgrade and apt. | FACT + REPORTED | Release notes; #387397 post 4 |
| 11 | An NVIDIA employee said running `apt upgrade` without `dist-upgrade` can leave the GPU driver unloaded. The reporter then showed that `dist-upgrade` with 580.178.04 loaded still resets, so this does not explain the issue. | REPORTED (staff post, refuted by reporter) | #387456 posts 2, 5 |
| 12 | A moderator stated that driver **595 is not supported on DGX Spark** (Sept 2026). Some users on this issue installed 595 through `ubuntu-drivers`. | FACT (staff post) | [#383563](https://forums.developer.nvidia.com/t/dgx-spark-regression-after-updating-to-kernel-7-0-0-1019-nvidia-gdm-no-longer-boots-correctly-fixed/383563) post 2 |
| 13 | During a `fwupdmgr` firmware upgrade, systems can be offline for about 10 minutes (staff: "a couple of minutes" is normal). One user lost fan control (`nvidia-ffa-ec` already bound) on 1024. | REPORTED | #387397 posts 21–23 |
| 14 | Reddit, GitHub issues and Launchpad bugs: no matching report found. Reddit blocked automated fetches (HTTP 403), so it was only checked through the search index. | UNVERIFIED | — |

**Bottom line:** NVIDIA is investigating, and there is no fix. 1024 is not the kernel NVIDIA documents for Spark. The community workaround is to boot and pin 1019, or run headless.

## 2. Practical impact for Hermes (PROPOSAL)

- **PROPOSAL:** Keep the Spark on **7.0.0-1019-nvidia** until NVIDIA documents a newer kernel in the Spark release notes or confirms a fix in thread #387397.
- **ASSUMPTION:** The Spark mainly runs headless as the Hermes host. If so, it may be stable even on 1024. But the idle resets and the GPU "Reset Required" faults reported on 1024 (rows 8, 13) are a risk for long-running agents. Prefer 1019 either way.
- Hermes gateways are **`systemctl --user`** services (see `SOPs/2026-09-12-hve-spark-hermes-user-session-supervision-runbook-v1.0.md`). A headless reboot starts them only if **user lingering** is enabled for the `hans` account. Check this before relying on headless reboots.
- FACT: In the October release, NVIDIA fixed "fans stop responding in headless mode" and added Dynamic Display Reserved Memory (headless can drop to a 512 MB carveout). Headless operation is supported.
- Do **not** run `ubuntu-drivers install`/`autoinstall` (it pulls the unsupported 595 driver). Do not run firmware upgrades during this incident.

## 3. Runbook for Hans or Luna (run on the Spark)

Legend: 🟢 read-only · 🔴 **CHANGES THE SYSTEM** (needs Hans's OK under the Luna autonomy grant)

### 3.1 Diagnose 🟢
```bash
uname -a                                   # running kernel; 1024 shows "#25~24.04.1 ... Oct 22"
dpkg -l | grep -E 'linux-(image|modules|headers)-7\.0\.0-10(19|24)|nvidia-hwe-24.04'
apt-mark showhold
sudo apt update && apt list --upgradable 2>/dev/null | grep -Ei 'linux|nvidia|dgx'   # apt update refreshes lists only
fwupdmgr get-updates                       # read-only; do NOT run fwupdmgr upgrade now
nvidia-smi                                 # expect Driver 580.178.04, CUDA 13.0
journalctl --list-boots | tail -n 10       # many short boots = loop
journalctl -b -1 -k --no-pager | tail -n 80     # kernel log of previous boot
journalctl -b -1 --no-pager | grep -Ei 'watchdog|Xid|NVRM|Oops|panic|BERT|hardware error' | tail -n 40
last -x | head -n 20                       # crash = 'reboot' without a matching 'shutdown'
ls /sys/fs/pstore/ 2>/dev/null             # panic dumps, if any
```
If the loop is too fast to log in locally, unplug all monitors and use SSH.

### 3.2 Boot 1019 once 🔴 (temporary, one boot)
At the GRUB menu, choose **Advanced options for DGX OS → … with Linux 7.0.0-1019-nvidia** (REPORTED menu title). If the menu is hidden, see 3.3. The `/etc/default/grub.d/*.cfg` files override `/etc/default/grub`.

### 3.3 Make 1019 the default 🔴
```bash
# show exact menu entry IDs (read-only)
sudo grep -E "submenu|menuentry " /boot/grub/grub.cfg | grep -oE "(gnulinux-[^']+)" | sort -u

# override file sorts last, so it wins over no-grubmenu.cfg (REPORTED behaviour)
sudo tee /etc/default/grub.d/zz-hve-kernel-pin.cfg >/dev/null <<'CFG'
GRUB_DEFAULT=saved
GRUB_TIMEOUT_STYLE=menu
GRUB_TIMEOUT=10
CFG
sudo update-grub
# use the submenu id + '>' + the 1019 entry id from the grep above
sudo grub-set-default 'gnulinux-advanced-<UUID>>gnulinux-7.0.0-1019-nvidia-advanced-<UUID>'
sudo grub-editenv list        # verify saved_entry (read-only)
sudo reboot
uname -r                      # expect 7.0.0-1019-nvidia
```

### 3.4 Stop the upgrade coming back 🔴
```bash
sudo apt-mark hold linux-nvidia-hwe-24.04 linux-image-nvidia-hwe-24.04 \
  linux-headers-nvidia-hwe-24.04 linux-tools-nvidia-hwe-24.04 \
  linux-modules-nvidia-580-open-nvidia-hwe-24.04 linux-modules-nvidia-fs-nvidia-hwe-24.04
apt-mark showhold
```
- These are the metapackage names from the community post. First check the names on our unit with `dpkg -l | grep nvidia-hwe-24.04` and hold only the ones that exist.
- Holding the metapackages blocks *future* kernels too, including a fix. Un-pin deliberately (3.7).
- Do **not** run `apt autoremove` or purge 1019. Leave 1024 installed for later re-testing.
- Avoid one-click "Update" in the DGX Dashboard while pinned. **ASSUMPTION:** the Dashboard's upgrade respects apt holds. Verify that with `apt-mark showhold` after any Dashboard run.

### 3.5 Run headless with remote access meanwhile 🟢/🔴
- Disconnect HDMI and USB-C displays. Do not hot-plug HDMI while on 1024 (REPORTED instant reset).
- Access options: SSH over LAN; Tailscale if already installed (`tailscale status`); [NVIDIA Sync](https://docs.nvidia.com/dgx/dgx-spark/nvidia-sync.html) (official, SSH-based) from a laptop; the DGX Dashboard through Sync.
- Make sure Hermes comes up without a desktop login:
```bash
loginctl show-user hans -p Linger            # 🟢 want Linger=yes
sudo loginctl enable-linger hans             # 🔴 only if Linger=no
systemctl --user is-enabled hermes-gateway-hve-chief-of-staff.service hermes-gateway-hve-librarian.service hermes-coder-worker.service   # 🟢
systemctl is-enabled ollama 2>/dev/null; systemctl --user is-enabled ollama 2>/dev/null   # 🟢 Ollama is system or user, whichever exists
```
- After any reboot, check: `systemctl --user is-active` (as in the supervision runbook), `curl -s localhost:11434/api/tags | head` (Ollama), and confirm that the model preload (`hermes/scripts/hermes-preload-models.sh`) ran. Check that the COS cron jobs (3:00 AM daily, 6:10 AM brief, Sunday 6 PM pack) did not miss a run.

### 3.6 Optional, only if idle resets continue on 1019 (REPORTED, not NVIDIA-endorsed) 🔴
A separate Oct 21 report ([#386469](https://forums.developer.nvidia.com/t/dgx-spark-repeated-hard-resets-sbsa-generic-watchdog-timeout-cpu-6-hangs-gone-for-10-days-when-deep-cpuidle-states-are-disabled/386469)) found that disabling deep CPU idle states stopped SBSA-watchdog resets. The setting does not survive a reboot, and it costs idle power. Treat it as a diagnostic, not a fix:
`echo 1 | sudo tee /sys/devices/system/cpu/cpu*/cpuidle/state{1,2,3}/disable`

### 3.7 Un-pin when a fix ships 🔴
Wait for **both** of these: (a) the Spark release notes list a kernel newer than 1019, or NVIDIA posts a fix in #387397; **and** (b) at least two other users confirm it is stable with a monitor attached.
```bash
sudo apt-mark unhold linux-nvidia-hwe-24.04 linux-image-nvidia-hwe-24.04 linux-headers-nvidia-hwe-24.04 \
  linux-tools-nvidia-hwe-24.04 linux-modules-nvidia-580-open-nvidia-hwe-24.04 linux-modules-nvidia-fs-nvidia-hwe-24.04
sudo apt update && sudo apt dist-upgrade      # official manual path also includes fwupdmgr refresh/upgrade
sudo grub-set-default 0 && sudo update-grub   # or keep 'saved' and select the new kernel id
sudo reboot
```
Test headless first, then with one monitor, during a maintenance window. Keep 1019 installed until the new kernel has run for 72 hours. Rollback is 3.2–3.4.

## 4. Daily monitor checklist (PROPOSAL)

Check once a day. Every 6 hours is optional while the thread is active.

1. `https://forums.developer.nvidia.com/t/387397.json`: new posts, and especially posts from users with `staff: true` or `moderator: true`. Same for `/t/387456.json` and `/t/387497.json`.
2. `https://forums.developer.nvidia.com/search.json?q=1024%20kernel%20order:latest` and `?q=spark%20kernel%20order:latest`: new threads, and any mention of 1025 or higher.
3. `https://docs.nvidia.com/dgx/dgx-spark/release-notes.html`: does the "Canonical Kernel" row change from 7.0.0-1019? Is there a new release section or a fixed-issue entry?
4. `https://docs.nvidia.com/dgx/dgx-spark/known-issues.html`: is a reboot or display entry added?
5. Launchpad API: `https://api.launchpad.net/devel/ubuntu/+archive/primary?ws.op=getPublishedSources&source_name=linux-nvidia-7.0&exact_match=true&ws.size=5`. Is there a version above 7.0.0-1024.25 in Proposed or Updates?
6. Launchpad bugs: `https://api.launchpad.net/devel/ubuntu/+source/linux-nvidia-7.0?ws.op=searchTasks` and `.../linux-nvidia?ws.op=searchTasks` for new bugs mentioning GB10, Spark or HDMI.
7. Web search: "DGX Spark 7.0.0-1024", "DGX Spark kernel 1025", "GB10 HDMI reset kernel" (covers Reddit, which blocks direct fetches).

**What counts as a material change** (report to Hans the same day): an NVIDIA staff reply with a root cause, fix, bug ID or new guidance; a kernel newer than 1024 in noble-proposed or noble-updates; the Spark release notes kernel row changing; a Known Issues entry; a driver or firmware update tied to the fix; a new widely confirmed workaround, or a reversal of the current one (for example, 1019 also failing). Everything else is "no change", which gets a one-line note or silence, depending on the routine's settings.

## 5. Sources checked on 2026-10-31 (HTTP 200 unless noted)
- https://forums.developer.nvidia.com/t/dgx-spark-repeatedly-rebooting-after-most-recent-update/387397
- https://forums.developer.nvidia.com/t/any-use-of-the-hdmi-tmds-output-causes-a-hard-reset-on-kernel-7-0-0-1024-nvidia/387456
- https://forums.developer.nvidia.com/t/dgx-spark-resetting-at-idle-after-latest-dgx-dashboard-update-kernel-7-0-0-1024/387401
- https://forums.developer.nvidia.com/t/system-gets-frozen-from-time-to-time/387497
- https://forums.developer.nvidia.com/t/dgx-spark-repeated-hard-resets-sbsa-generic-watchdog-timeout-cpu-6-hangs-gone-for-10-days-when-deep-cpuidle-states-are-disabled/386469
- https://forums.developer.nvidia.com/t/dgx-spark-regression-after-updating-to-kernel-7-0-0-1019-nvidia-gdm-no-longer-boots-correctly-fixed/383563
- https://docs.nvidia.com/dgx/dgx-spark/release-notes.html
- https://docs.nvidia.com/dgx/dgx-spark/known-issues.html
- https://docs.nvidia.com/dgx/dgx-spark/os-and-component-update.html
- https://docs.nvidia.com/dgx/dgx-spark/nvidia-sync.html
- https://docs.nvidia.com/dgx/dgx-os-7-user-guide/release_notes.html: this is the DGX *server* OS 7 table (driver 580.196.07, Oct 27). It is **not** the Spark stack, so do not apply it to Spark.
- https://launchpad.net/ubuntu/+source/linux-nvidia-7.0
- Reddit r/LocalLLaMA and r/nvidia returned HTTP 403 (blocked). GitHub issue search found no matching issue.

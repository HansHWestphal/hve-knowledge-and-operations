# HVE Agent Comms: DGX Spark kernel pin after the 7.0.0-1024 reboot loop (v1.0)

**From:** HVE Knowledge Ops, on behalf of Hans
**To:** Luna (on-prem infrastructure owner)
**Date:** 2026-10-31 (Toronto time)
**Status:** For awareness and ownership. The change is already applied on the Spark by Hans.

## 1. Summary
On Saturday morning (Oct 31) the DGX Spark (`spark-5054`) was in a reboot loop on kernel `7.0.0-1024-nvidia`. Hans recovered it from the console and pinned it to the previous kernel, `7.0.0-1019-nvidia`. The Spark is now stable on 1019 with a monitor attached. Kernel updates are held until NVIDIA ships a fix.

## 2. What happened (FACT unless marked)
- FACT: `linux-nvidia-7.0` 7.0.0-1024.25~24.04.1 was published to noble-updates on 2026-10-29 at 8:43 PM EDT and arrived through the Dashboard and apt upgrade path. The driver (580.178.04) did not change.
- FACT: NVIDIA's DGX Spark release notes still list kernel 7.0.0-1019 for DGX OS 7.6.0. 1024 is not in them.
- FACT: An NVIDIA moderator acknowledged the issue in forum thread 387397 ("We will look into this kernel issue"). As of Oct 31 at 9:05 AM there is no fix, no bug ID, no Known Issues entry and no kernel newer than 1024.
- REPORTED (community): hard resets every 30 seconds to 5 minutes with a display attached (HDMI, and on some units USB-C/DP too). Units are stable headless or on 1019. Founders Edition, ASUS, Gigabyte and Dell units are affected.
- FACT (our Spark): the loop matched the reports; it happened with a monitor attached on 1024.

## 3. Changes made on the Spark (FACT, applied by Hans, confirmed)
1. `/etc/default/grub`: `GRUB_DEFAULT=saved`, then `update-grub`.
2. `grub-set-default "1>2"`. The saved entry is Advanced options, item 2, which is `7.0.0-1019-nvidia` (non-recovery). `grub-editenv list` shows `saved_entry=1>2`.
3. `/etc/default/grub.d/zz-menu.cfg` was added with `GRUB_TIMEOUT_STYLE=menu` and `GRUB_TIMEOUT=15`, so the GRUB menu shows for 15 seconds at every boot.
4. `apt-mark hold` is set on the five kernel metapackages:
   - `linux-headers-nvidia-hwe-24.04`
   - `linux-image-nvidia-hwe-24.04`
   - `linux-modules-nvidia-580-open-nvidia-hwe-24.04`
   - `linux-nvidia-hwe-24.04`
   - `linux-tools-nvidia-hwe-24.04`
5. A test reboot came up on `7.0.0-1019-nvidia`, confirmed by Hans with `uname -r`.

Installed kernels still on disk: 7.0.0-1024, 7.0.0-1019, 6.17.0-1021 and 6.17.0-1018. Nothing was removed.

Note: in Hans's BIOS (AMI Aptio, Boot tab), the "boot to Grub menu" option may have been switched to Enabled during recovery. ASSUMPTION: it is harmless, but please check it and record its state.

## 4. Asks for Luna (PROPOSAL, within your on-prem autonomy grant)
1. **Verify** on the Spark: `uname -r` shows 1019, `apt-mark showhold` lists the five packages, and `sudo grub-editenv list` shows `saved_entry=1>2`.
2. **Hermes health after the reboots:** check that the gateways, Ollama and the model preload are up. Check that `loginctl show-user hans` reports `Linger=yes`, so the user services start headless after any future reboot. Check whether the COS cron jobs missed any runs on Oct 31 (03:00 daily, 06:10 morning brief) and backfill or note them.
3. **During this incident, avoid** `apt autoremove` (it could remove 1019), `ubuntu-drivers install`, `fwupdmgr upgrade`, and Dashboard "Update" actions. Driver 595 is not supported on Spark, per an NVIDIA moderator.
4. **Sunday decision pack job:** the install and dry run from the Oct 30 handoff still apply. Please do them on the stable 1019 kernel, and confirm `next_run_at` = 2026-11-01T18:00:00-05:00.
5. **Note the pinned state** in your on-prem runbook or inventory.

## 5. How to unpin later (PROPOSAL, do not run until a fix is confirmed)
Trigger: NVIDIA documents a kernel newer than 1024 that fixes this, or a staff post confirms a fix, and at least two users report it stable. HVE Knowledge Ops runs a twice-daily watch, at about 9 AM and 5 PM Toronto time, and will tell Hans when this happens.
1. `sudo apt-mark unhold` the same five packages.
2. `sudo apt update && sudo apt full-upgrade`.
3. Set `GRUB_DEFAULT=0` in `/etc/default/grub` (or run `grub-set-default 0`), then `update-grub`.
4. Reboot headless first, then attach a monitor and watch for 30 minutes or more.
5. Keep 1019 installed as a fallback for at least 72 hours. Optionally remove `zz-menu.cfg` afterwards.

Rollback: boot Advanced options and 1019 from the 15-second GRUB menu, then `grub-set-default "1>2"` again.

## 6. Decision and money notes
- No money decisions are involved.
- This change is an on-prem configuration action, within Luna's domain autonomy (Q4). It should be recorded by COS as an informational entry once the action-to-COS path exists.

## 7. Sources
- NVIDIA forum, main thread: https://forums.developer.nvidia.com/t/dgx-spark-repeatedly-rebooting-after-most-recent-update/387397
- NVIDIA forum, HDMI reset thread: https://forums.developer.nvidia.com/t/any-use-of-the-hdmi-tmds-output-causes-a-hard-reset-on-kernel-7-0-0-1024-nvidia/387456
- DGX Spark release notes: https://docs.nvidia.com/dgx/dgx-spark/release-notes.html
- DGX Spark Known Issues: https://docs.nvidia.com/dgx/dgx-spark/known-issues.html
- Full research note (draft): `hermes/knowledge/2026-10-31-dgx-spark-kernel-1024-reboot-loop.md` (pending Hans's approval to commit)

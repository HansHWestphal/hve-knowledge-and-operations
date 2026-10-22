# Kitchen Satellite iMac — Omarchy Mac-Clone Spec

**Date:** 2026-10-21  
**Status:** Draft for review  
**Machine:** iMac 21.5-inch (Mid 2011) — Model A1311, EMC 2428, iMac12,1  
**Role:** Home lab kitchen satellite — wife photos, recipes, light daily use  
**Owner:** Hans Westphal / HVE  

## 1. Purpose

This machine was slated for disposal. It is now being recovered as a clean, self-contained kitchen satellite node:

- Primary user: spouse (Mac-familiar, non-technical)
- Workloads: photo viewing, recipe browsing, light web, occasional local AI / agent tasks
- Data model: OS + apps only on internal drive; all bulk data (photos, recipes, documents, media) on NAS
- Aesthetic / UX goal: Omarchy (Arch Linux + Hyprland) configured as a close Mac clone experience that passes the “wife test” (floating windows, dock, familiar shortcuts, polished theme)

## 2. Hardware Baseline

| Component | Spec | Notes |
|-----------|------|-------|
| Model | iMac 21.5" Mid 2011 (A1311 / EMC 2428) | High Sierra-era Intel |
| CPU | Quad-core Core i5 (2.5/2.7 GHz) or Core i7 (2.8 GHz) | Sandy Bridge |
| RAM | 4 GB stock → target 32 GB | Easy bottom-door upgrade; 4 × 8 GB DDR3-1333 SO-DIMM |
| Storage | Stock 500 GB or 1 TB 7200-rpm 3.5" HDD | Keep as-is for this path |
| GPU | AMD Radeon HD 6750M / 6770M (512 MB) | Sufficient for Hyprland floating mode |
| Ports | Thunderbolt, FireWire 800, USB 2.0 ×4, SDXC, Gigabit Ethernet | |
| Max official macOS | High Sierra 10.13.6 | Not used; Omarchy replaces it |

## 3. Upgrade Path (Current Plan)

### Phase 1 — Immediate (no disassembly)
- Upgrade RAM to 32 GB via bottom access panel (highest ROI, lowest risk).
- Wipe internal drive and install Omarchy cleanly from USB.
- Configure floating workspaces + Mac theme / dock / Command-Tab behavior.
- Mount NAS shares (NFS or SMB) for all non-system data.

### Phase 2 — Optional later (if needed)
- Internal SSD swap (main bay or secondary 2.5" bay) only if stock HDD feels too slow after real use.
- Requires screen removal + OWC In-line Digital Thermal Sensor for main-bay SSD.
- Not required for initial kitchen satellite role.

**Decision:** Skip internal SSD for now. Keep stock HDD for OS + apps only. All else on NAS.

## 4. Software Stack — Omarchy Mac Clone

- Base: Omarchy (Arch + Hyprland + Quickshell)
- UX targets for wife test:
  - Floating workspaces (not pure tiling)
  - Magnification dock or equivalent
  - Cupertino / Mac Starter theme (frosted glass, titlebars, rounding)
  - Command-Tab / Mission Control style switching
  - Familiar keyboard shortcuts where possible
- Agent / HVE integration:
  - Local agent access (Hermes or lightweight client) for kitchen-relevant tasks
  - Read-only or carefully scoped access to HVE knowledge / recipe / photo indexes on NAS
  - No heavy local model hosting required (32 GB is comfortable but not a GPU box)

## 5. Data & NAS Strategy

- Internal drive: Omarchy + packages + daily apps only.
- NAS: primary store for photos, recipes, documents, backups.
- Mount points: standard user directories symlinked or bind-mounted to NAS shares.
- Network: Prefer wired Ethernet; solid Wi-Fi acceptable for kitchen use.
- Backup: NAS itself is the durable store; internal drive is disposable system volume.

## 6. Wife-Test Criteria

- Looks and feels like a familiar Mac (dock, floating windows, theme).
- Photos and recipes open without friction.
- No unexpected terminal or tiling surprises in normal use.
- Stable, quiet, and low-maintenance.
- Passes casual daily use without support requests.

## 7. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Stock HDD age / speed | Accept for Phase 1; SSD is optional Phase 2. Monitor SMART. |
| Fan noise if later SSD | Use proper thermal sensor cable if main-bay SSD is ever installed. |
| Network dependency | Ensure reliable NAS connectivity; local cache for critical recipes if needed. |
| Theme drift | Pin floating mode + Mac theme in Omarchy config; document exact settings. |

## 8. Next Actions

1. Confirm exact CPU (i5 2.5 / 2.7 or i7 2.8) once powered on.
2. Order 32 GB RAM kit (4 × 8 GB DDR3-1333).
3. Prepare Omarchy USB installer.
4. Define NAS share layout for photos + recipes.
5. Document final floating-mode + theme config after first boot.

## 9. Agent Notes

- This node is a lightweight edge satellite, not a primary compute or training machine.
- Preferred agent interaction: thin client or local lightweight agent talking to central HVE systems.
- Keep configuration reproducible and documented in this repo.

---

**Filed by:** Grok (on behalf of Hans)  
**Classification:** Operational hardware spec — kitchen satellite  
**Review requested:** Yes

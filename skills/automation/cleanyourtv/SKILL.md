---
name: cleanyourtv
description: >
  Smart TV Debloater & Ad-Removal: Connects to Android TV or Google TV over Wi-Fi
  via ADB to safely disable manufacturer ad packages, purge telemetry, and replace
  cluttered home screens with a clean Apple TV-style launcher.
argument-hint: "[connect|disable|restore|check|theme]"
license: MIT
---

# CleanYourTV: Smart TV Debloater & Ad-Remover

CleanYourTV connects your AI coding assistant to your Android TV / Google TV (Sony, TCL, Xiaomi, Hisense, Nvidia Shield, etc.) over Wi-Fi ADB. It guides the agent through safely disabling ad-serving services, telemetry tracking, and sponsored rows without rooting or flashing.

## Core Rules & Non-Negotiables

1. **Disable, Never Uninstall:** Always use `pm disable-user --user 0`, one package at a time. Never run destructive uninstalls.
2. **Safe Backups First:** All active packages, disabled lists, and system settings are archived before any modifications begin.
3. **Instant Rollback:** Every single action can be reversed via `tools/restore.ps1` or `tools/restore.sh`.
4. **Visual Verification:** Pull screenshots over ADB after each step to confirm that the TV's display is responsive and functioning properly.

## Quick Commands

```powershell
# Check TV connection status over Wi-Fi
python tools/check.py <TV_IP_ADDRESS>

# Disable ad and telemetry packages safely
./tools/disable.ps1 -Target <TV_IP_ADDRESS>

# Revert and restore all original packages
./tools/restore.ps1 -Target <TV_IP_ADDRESS>
```

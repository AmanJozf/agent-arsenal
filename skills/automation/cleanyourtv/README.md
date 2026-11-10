# CleanYourTV: Smart TV Debloater & Ad-Removal

> *"Debloat any Android or Google TV over Wi-Fi and get an Apple TV-style home screen with zero ads."* — Created by [Gathin23](https://github.com/Gathin23/cleanyourtv) (55,400+ stars).

CleanYourTV allows your AI assistant (Claude Code, Cursor, Antigravity) to connect directly to your smart TV over Wi-Fi via ADB (Android Debug Bridge). It safely disables pre-installed manufacturer bloatware, tracking telemetry, and sponsored ads, replacing cluttered home screens with an ultra-clean, minimal launcher.

---

## ⚡ How to Install on Any Machine

```bash
# 1. Enable USB/Network Debugging in Developer Options on your TV, then run:
python tools/check.py <YOUR_TV_IP_ADDRESS>
```
*(Run `./tools/disable.ps1` or `./tools/disable.sh` to safely disable ad packages without root).*

---

## 🎯 What Your Agent Can Do

- **Safe Package Disabling:** Uses `pm disable-user --user 0` instead of dangerous uninstalls—everything is 100% reversible via `tools/restore.ps1`.
- **Telemetry & Ad Elimination:** Stops background telemetry daemons on Sony Bravia, TCL, Hisense, Xiaomi, and Nvidia Shield.
- **Apple TV-Style Experience:** Strips out home screen video banners and auto-playing trailers, showing only your apps.
- **Visual Verification:** The agent automatically pulls screenshots over ADB to verify the TV screen after each tweak.

---

## 📦 Files in this Skill

- [`SKILL.md`](./SKILL.md) — Master skill definition & command specification.
- [`AGENTS.md`](./AGENTS.md) — Non-negotiable safety rules and procedure checklist.
- [`PROMPT.md`](./PROMPT.md) — The viral AI prompt used to debloat TVs interactively.
- [`tools/`](./tools/) — Automated PowerShell & Bash debloat scripts (`disable.ps1`, `restore.ps1`, `check.py`).
- [`WHAT_THIS_DOES.txt`](./WHAT_THIS_DOES.txt) — Quick 5-second plain-English summary + real example.

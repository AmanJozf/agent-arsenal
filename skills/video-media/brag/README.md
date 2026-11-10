# Brag: Automated Launch Video Generator for AI Agents

> *"You built it. Now brag. Turn the project you just created into a short, shareable launch demo video with one command."* — Created by [latent-spaces/brag](https://github.com/latent-spaces/brag) (20,850+ stars).

Brag inspects the source code, routes, and UI of your current project and automatically writes, composes, and renders a sleek, animated product launch video using **HyperFrames**. No screen recording or live URL required.

---

## ⚡ How to Install on Any Machine

```bash
# 1. In Claude Code, install the official plugin from marketplace:
/plugin marketplace add latent-spaces/brag && /plugin install brag@brag
```
*(Or in Cursor / Codex / Antigravity, add [`SKILL.md`](./SKILL.md) to your agent skills directory).*

---

## 🎯 What Brag Does

- **Codebase-to-Video:** Reads your frontend components and routes directly from disk—no need to deploy or record your screen.
- **Storyboarding & Pacing:** Automatically constructs an engaging hook, problem breakdown, feature highlights, and call-to-action slide.
- **Audio & Music Alignment:** Generates beat-synced motion and optional AI voiceover narration (`--voice`).
- **HyperFrames Engine:** Uses HyperFrames underneath to deterministically compile HTML/CSS/GSAP animations into crisp MP4 launch videos.

---

## 🛠️ Usage Examples

```text
/brag                        # Generates standard launch video for current repo
/brag --voice                # Adds AI voiceover narration
/brag --title "My App v2"    # Custom title and branding
/brag --no-music             # Disables background audio tracks
```

---

## 📦 Files in this Skill

- [`SKILL.md`](./SKILL.md) — Master skill definition & prompt workflow.
- [`slim.md`](./slim.md) — Fast single-pass execution mode for advanced reasoning models.
- [`references/`](./references/) — Detailed multi-step pipeline (`step-1-inspect.md`, `step-2-plan.md`, `step-3-compose.md`, `tones.md`).
- [`WHAT_THIS_DOES.txt`](./WHAT_THIS_DOES.txt) — Quick 5-second plain-English summary + real example.

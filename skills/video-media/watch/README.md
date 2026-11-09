# Watch: Video Understanding for AI Coding Agents

> *"Give Claude the ability to watch any video. /watch downloads, extracts frames, transcribes, and hands it all to Claude."* — Created by [bradautomates/claude-video](https://github.com/bradautomates/claude-video) (20,300+ stars).

Watch turns video evidence (a YouTube URL, Loom link, or local MP4 recording) into timestamped visual frames and synchronized audio transcripts. It allows AI coding agents to visually inspect UI recordings, reproduce bugs, and code frontend interfaces directly from video references.

---

## ⚡ How to Install on Any Machine

```bash
# 1. In Claude Code, install the official plugin from marketplace:
/plugin marketplace add bradautomates/claude-video && /plugin install watch@claude-video
```
*(Or in Codex / Cursor / Antigravity, ask your agent: `Use $skill-installer to install the watch skill from https://github.com/bradautomates/claude-video/tree/main/skills/watch`)*

---

## 🎯 What Watch Does

- **Scene-Change Keyframe Extraction:** Uses `ffmpeg` to detect visual scene transitions and pull high-resolution frames with exact timestamps.
- **Transcript Synchronization:** Automatically downloads native subtitles or runs transcription (via local WhisperX or cloud Whisper / Groq API).
- **Agentic Video Analysis:** When configured with a `GEMINI_API_KEY`, leverages Google's multimodal video models to analyze the raw stream directly.
- **UI Recreation from Video:** Point your agent at a 30-second screen capture of any website or animation and say: *"Recreate this UI in React + Tailwind."*

---

## 🛠️ Usage Examples

```text
/watch https://www.youtube.com/watch?v=dQw4w9WgXcQ
/watch path/to/ui-demo.mp4 "What animations and CSS layout are used here?"
/watch https://loom.com/share/abc123xyz "Find the exact line where the bug occurs in this reproduction"
```

---

## 📦 Files in this Skill

- [`SKILL.md`](./SKILL.md) — Main skill definition & Python runtime invocation rules.
- [`AGENTS.md`](./AGENTS.md) — Operational guidelines for video-evidence analysis.
- [`CLAUDE.md`](./CLAUDE.md) — Plugin commands and configuration rules.
- [`scripts/`](./scripts/) — Full bundled Python pipeline (`watch.py`, `frames.py`, `download.py`, `transcribe.py`, `gemini.py`, `setup.py`).

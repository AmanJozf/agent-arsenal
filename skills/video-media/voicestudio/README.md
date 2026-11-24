# VoiceStudio: Open-Source AI Voice Workstation

> *"A local-first, zero-subscription desktop voice studio and ElevenLabs alternative."* — Created by [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) on GitHub.

VoiceStudio is a complete local speech synthesis and audio production suite. It allows developers, creators, and AI agents to clone voices, generate character dialogue, dub videos across hundreds of languages, and transcribe audio completely offline on personal hardware.

---

## ⚡ Quick Start

### 1. Installation
```bash
# macOS & Linux one-line installer:
curl -fsSL https://voicestudio.sh/install | sh

# Or run headless server via Docker:
docker run -d -p 8000:8000 --gpus all ghcr.io/debpalash/voicestudio:latest
```

### 2. Using with AI Coding Agents
VoiceStudio includes a local OpenAI-compatible endpoint at `http://localhost:8000/v1` and an MCP server:

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="local")

response = client.audio.speech.create(
    model="omni-voice-v1",
    voice="cloned_voice_id",
    input="This entire sentence was synthesized locally without any cloud API fees."
)
response.stream_to_file("output.mp3")
```

---

## 🎯 Key Features

- **Instant Voice Cloning:** High-fidelity voice matching from a 5–15 second clean sample.
- **Voice Design:** Create unique, synthetic personas from text prompts (pitch, tone, accent, age).
- **Multi-Speaker Audiobooks:** Visual script editor to orchestrate conversations with multiple voices.
- **Video Dubbing:** Timed translation and voice-preserving dubbing across 600+ languages.
- **Whisper Transcription:** Local offline speech-to-text with timestamping.
- **MCP Integration:** Native Model Context Protocol support for agent-driven voice generation.

---

## 📦 Files in this Skill

- [`SKILL.md`](./SKILL.md) — Comprehensive agent prompts, triggers, and configuration reference.
- [`AGENTS.md`](./AGENTS.md) — Operational rules and quality requirements for agents.
- [`WHAT_THIS_DOES.txt`](./WHAT_THIS_DOES.txt) — 1-sentence quick summary and copy-paste prompt example.

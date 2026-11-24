---
name: voicestudio
description: Local-first AI voice studio and open-source ElevenLabs alternative. Clone voices from audio clips, generate high-fidelity speech (TTS), dub videos across 600+ languages, transcribe audio with Whisper, and integrate with MCP agents or local OpenAI-compatible endpoints.
---

# VoiceStudio

> A local-first, zero-cost desktop studio and AI agent voice engine designed as an open-source alternative to ElevenLabs. Created by [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio).

VoiceStudio enables high-fidelity voice cloning, text-to-speech (TTS), multi-character audiobook creation, video dubbing, and Whisper speech-to-text running completely offline on your local GPU/CPU hardware.

---

## ⚡ Core Capabilities

1. **Instant Voice Cloning (Zero-Shot / Few-Shot):**
   - Provide a 5–15 second clean reference audio clip (`.wav`, `.mp3`, `.m4a`).
   - Extract voice timbre, accent, pitch, and cadence without fine-tuning.
   - Generate speech in the cloned voice with emotional inflection control.

2. **Custom Voice Design:**
   - Synthesize unique voices by specifying gender, age, vocal warmth, energy, and accent parameters.
   - Save custom voice profiles locally for reuse across projects.

3. **Multi-Character Audiobook & Script Editor:**
   - Write or paste full scripts with multi-speaker dialogue blocks.
   - Assign distinct voice profiles to each character or narrator.
   - Export unified audio with automatic pause/pacing adjustments.

4. **Video Dubbing & Translation:**
   - Time-aligned speech translation across 600+ languages.
   - Voice preservation: dub into target languages while retaining the speaker's original vocal tone.

5. **Transcription & Dictation (Whisper-Powered):**
   - Local, fast, privacy-preserving speech-to-text.
   - Floating widget support for system-wide voice dictation.

6. **Agent & MCP Interoperability:**
   - Built-in **Model Context Protocol (MCP)** server for AI coding agents.
   - OpenAI-compatible `/v1/audio/speech` and `/v1/audio/transcriptions` REST endpoints.
   - Agent-specific client mapping (`X-OmniVoice-Client-Id`) to assign unique voices to different AI personas.

---

## 🚀 Installation & Setup

### Option 1: One-Line Installer (macOS & Linux)
```bash
curl -fsSL https://voicestudio.sh/install | sh
```

### Option 2: Windows Setup
1. Download the latest installer `.exe` from the [Releases page](https://github.com/debpalash/VoiceStudio/releases).
2. Run the installer (ships with bundled GPU/CUDA acceleration detection).

### Option 3: Docker (Headless / Server Mode)
```bash
docker run -d -p 8000:8000 --gpus all ghcr.io/debpalash/voicestudio:latest
```

---

## 🤖 AI Agent & MCP Integration

VoiceStudio exposes a native MCP server so that Antigravity, Claude Code, Cursor, and Codex can synthesize speech and clone voices programmatically.

### Running the Local MCP Server
```bash
# Start backend with MCP enabled
python -m backend.mcp_server --port 8000
```

### Connecting to Antigravity / Claude Code MCP
Add to your MCP configuration:
```json
{
  "mcpServers": {
    "voicestudio": {
      "command": "python",
      "args": ["-m", "backend.mcp_server"],
      "env": {
        "VOICESTUDIO_API_URL": "http://127.0.0.1:8000",
        "VOICESTUDIO_CLIENT_ID": "antigravity-agent"
      }
    }
  }
}
```

### Using the OpenAI-Compatible API in Python
VoiceStudio runs a local `/v1` server, allowing you to use the standard `openai` SDK with zero subscription cost:

```python
from openai import OpenAI

# Point to your local VoiceStudio instance
client = OpenAI(
    base_url="http://127.0.0.1:8000/v1",
    api_key="local"  # Dummy key for local offline server
)

# 1. Text-to-Speech (TTS)
response = client.audio.speech.create(
    model="omni-voice-v1",
    voice="cloned-speaker-id",  # Or built-in voice preset
    input="Welcome to our project. Let me show you what we built today."
)
response.stream_to_file("output.mp3")

# 2. Audio Transcription (STT)
with open("recording.mp3", "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        model="whisper-base",
        file=audio_file
    )
    print(transcription.text)
```

---

## 🛠️ Prompt Trigger Recipes

Agents should activate this skill when the user asks for:
* "Clone this voice from `<sample.wav>`"
* "Generate a voiceover for this video script without paying ElevenLabs"
* "Dub this video into German while keeping the original speaker's voice"
* "Create an audiobook / dialogue with two different narrator voices"
* "Set up a local text-to-speech engine with OpenAI compatibility"

---

## 💡 Production Best Practices

1. **Audio Sample Quality for Cloning:**
   - Use 5–15 seconds of clean, dry speech (no background music, no reverb, no mouth clicks).
   - Ensure consistent volume and normal speaking cadence.
2. **GPU Acceleration:**
   - Windows/Linux: NVIDIA GPU with CUDA 11.8+ or 12.x provides real-time streaming (<200ms latency).
   - macOS: Apple Silicon (M1/M2/M3/M4) leverages Metal Performance Shaders (MPS) natively.
3. **Pacing in Scripts:**
   - Use punctuation (`...`, `,`, `—`) to guide the engine's natural breathing pauses and cadence.

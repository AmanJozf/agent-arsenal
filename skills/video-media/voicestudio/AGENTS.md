# VoiceStudio: Operational Rules for AI Agents

When interacting with voice tasks, speech synthesis, and voice cloning using VoiceStudio:

## 1. Safety & Privacy First
- Never clone voices without user authorization or clear ownership of the reference audio sample.
- Run locally by default to ensure no audio samples or synthesized outputs leave the user's machine.

## 2. Audio Processing Standards
- Reference samples should be converted to 24kHz or 48kHz mono WAV/FLAC for maximum fidelity before cloning.
- Strip silence and background noise if the user provides raw audio with hum or hiss.
- For long narration scripts (>500 words), split text into logical paragraph chunks to prevent memory spikes and ensure consistent prosody.

## 3. Integration Patterns
- Prefer the local OpenAI-compatible `/v1/audio/speech` endpoint (`base_url="http://127.0.0.1:8000/v1"`) for simple script execution.
- Use the MCP server interface for direct agent-to-tool orchestration.

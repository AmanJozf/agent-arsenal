---
name: freellmapi
description: >
  Free LLM Gateway: route coding agents and LLM applications through 34 free providers
  and 635 free model endpoints (7.4 billion tokens/month pooled capacity) via a single
  OpenAI-compatible /v1 endpoint. Features smart routing, automatic failover, and one-line
  CLI generators for Claude Code, Codex, Cursor, Cline, OpenCode, and Aider.
argument-hint: "[setup|serve|models|launch|keys]"
license: MIT
---

# FreeLLMAPI: Multi-Provider Free AI Gateway

FreeLLMAPI consolidates 34 free LLM providers and 635 free model endpoints behind a single unified `/v1` endpoint. It eliminates rate limits and subscription barriers by intelligently load-balancing and failing over across free tiers.

## Core Capabilities

1. **Massive Free Tier Capacity:** Aggregates 7.4B tokens/month across providers like Groq, Cerebras, SambaNova, Cloudflare Workers AI, GitHub Models, Hugging Face, Cohere, and more.
2. **Universal Wire Support:**
   - OpenAI Chat (`/v1/chat/completions`)
   - Anthropic Messages API (`/v1/messages`)
   - Codex Responses Wire API
   - Native Gemini and Ollama endpoints
3. **Agent Auto-Configurators:** Built-in `npx freellmapi setup-<tool>` automatically generates perfectly matched configuration files for all major coding tools.
4. **Credential-Free In-Memory Launch:** `launch` and `launch-codex` inject credentials directly into child processes without saving API keys in plain text to disk.

## Agent Usage & Configuration

- **Default Endpoint:** `http://localhost:3001/v1`
- **Dashboard & Keys:** `http://localhost:3001`
- **Model Aliases:**
  - `freellmapi/auto`: Automatically routes to the highest-performing available free endpoint
  - `freellmapi/fast`: Lowest latency provider (e.g. Groq, Cerebras)
  - `freellmapi/code`: Highest-rated coding benchmark model available in pool

## Quick Commands

```bash
# Start via Docker
docker run -d -p 3001:3001 -v ~/freellmapi:/app/data freellmapi/freellmapi:latest

# Auto-configure your coding agent
npx freellmapi setup-claude --url http://localhost:3001 --api-key <unified-key>
npx freellmapi setup-cursor --url http://localhost:3001 --api-key <unified-key>
npx freellmapi setup-codex --url http://localhost:3001 --api-key <unified-key>
npx freellmapi setup-opencode --url http://localhost:3001 --api-key <unified-key>
```

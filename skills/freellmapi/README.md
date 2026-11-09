# FreeLLMAPI: Multi-Provider Free AI Gateway

> *"7.4 billion tokens per month. 34 free LLM providers. 635 free model endpoints. All behind one unified endpoint."*

FreeLLMAPI consolidates dozens of free LLM tiers (Groq, Cerebras, SambaNova, Cloudflare Workers AI, GitHub Models, Hugging Face, Cohere, etc.) into a single OpenAI-compatible `/v1` endpoint. It eliminates rate-limit bottlenecks with smart routing, automatic failover, and automated CLI configuration generators.

---

## ⚡ How to Install on Any Machine

```bash
# 1. Run the one-line installer (Docker required; or download Windows desktop .exe):
curl -fsSL https://freellmapi.co/install.sh | bash
```
*(Dashboard opens at `http://localhost:3001` — add your provider keys and grab your unified API key from the header! On Windows, an `.exe` installer is also available via Releases).*

---

## 🎯 Key Capabilities

- **Pooled Free Capacity:** Aggregates 7.4 billion tokens per month across 34 providers and 635 model endpoints.
- **Smart Routing & Failover:** Catches provider rate limits (`429`) or errors and instantly routes requests to the next active provider in your fallback chain.
- **Universal Wire Protocol:** Supports OpenAI Chat (`/v1/chat/completions`), Anthropic Messages (`/v1/messages`), Codex Responses API, and native Gemini endpoints.
- **One-Command Agent Generators:** Automated `npx freellmapi setup-<tool>` scripts write exact configurations for Claude Code, Cursor, Codex, OpenCode, Cline, Continue, and Aider.
- **Encrypted & Private:** All provider keys are stored locally and AES-encrypted on disk at `~/freellmapi/.env`.

---

## 🛠️ Instant Agent Setup

Run any of the built-in generators to configure your tools in seconds:

```bash
# Claude Code
npx freellmapi setup-claude --url http://localhost:3001 --api-key <unified-key>

# Cursor
npx freellmapi setup-cursor --url http://localhost:3001 --api-key <unified-key>

# Codex CLI
npx freellmapi setup-codex --url http://localhost:3001 --api-key <unified-key>

# OpenCode
npx freellmapi setup-opencode --url http://localhost:3001 --api-key <unified-key>
```

---

## 📦 Files in this Skill

- [`SKILL.md`](./SKILL.md) - Skill definition & CLI invocation commands.
- [`AGENTS.md`](./AGENTS.md) - Operational guidelines & rules for agent integration.
- [`agent-setup-guide.md`](./agent-setup-guide.md) - Complete reference for all 20+ supported agent setup generators.

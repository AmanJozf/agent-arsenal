# OmniRoute: Multi-Provider AI Gateway & Router

> *"Never stop coding. Free MIT AI gateway: one endpoint, 375 providers (150+ free), 1,400+ models."*

OmniRoute connects AI coding assistants and agents (Claude Code, Cursor, Codex, OpenCode, Cline, Antigravity) to 375+ LLM providers and 1,400+ models through a single local or self-hosted OpenAI-compatible endpoint.

---

## ⚡ How to Install on Any Machine

```bash
# 1. Install & launch the OmniRoute gateway (Node 18+ required):
npm install -g omniroute && omniroute serve --daemon
```
*(Or test instantly without global install: `npx omniroute serve` — opens dashboard at `http://localhost:20128`)*

---

## 🎯 Key Features

- **375+ Providers & 1,400+ Models:** Seamlessly access Claude, GPT, Gemini, Kimi, GLM, DeepSeek, MiniMax, Ollama, and local runtimes.
- **Quota-Aware Auto-Fallback:** When one provider hits a rate limit (429) or outage, requests instantly reroute to alternative providers without aborting your session.
- **RTK + Caveman Token Compression:** Saves 15% to 95% of prompt tokens using intelligent context filtering and noise stripping.
- **Automated Skill Collector:** Scans your machine for installed coding CLI tools (Claude Code, Cursor, Copilot, Cline) and provisions relevant agent skills from GitHub.
- **MCP & A2A Native:** Includes 110+ Model Context Protocol tools and JSON-RPC 2.0 Agent-to-Agent protocols.

---

## 🛠️ Configuring Your Agents to Use OmniRoute

### 1. Claude Code
Point Claude Code to OmniRoute's local endpoint in your environment:
```bash
export ANTHROPIC_BASE_URL="http://localhost:20128"
export ANTHROPIC_API_KEY="your-omniroute-key"
```

### 2. Cursor / Windsurf / VS Code Extensions
Set OpenAI Base URL in settings:
- **Base URL:** `http://localhost:20128/v1`
- **API Key:** `your-omniroute-key` (or local token)

### 3. Codex CLI
Use the built-in configuration helper:
```bash
omniroute config set codex
```

### 4. Antigravity / OpenCode
Add OmniRoute as a custom OpenAI-compatible provider:
```json
{
  "apiBase": "http://localhost:20128/v1",
  "apiKey": "your-omniroute-key"
}
```

---

## 📦 Files in this Skill

- [`SKILL.md`](./SKILL.md) - Master gateway invocation skill.
- [`AGENTS.md`](./AGENTS.md) - Full official OmniRoute agent guide (single source of truth for all coding agents).
- [`CLAUDE.md`](./CLAUDE.md) - Full Claude Code agent directives and instructions.
- [`GEMINI.md`](./GEMINI.md) - Full Gemini CLI agent directives and instructions.
- [`SKILLS_CATALOG.md`](./SKILLS_CATALOG.md) - Full catalog of all 46 drop-in REST & CLI sub-skills.
- [`skills/`](./skills/) - Complete collection of all 46 official, un-truncated `SKILL.md` sub-skill definitions (authentication, routing, compression, resilience, MCP tools, A2A protocol, skill collector, etc.).

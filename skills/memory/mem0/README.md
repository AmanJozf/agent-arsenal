# Mem0: Persistent Memory Layer for AI Agents

> *"The Memory Layer for AI Agents — Context that persists across sessions and projects."* — Created by [mem0ai](https://github.com/mem0ai/mem0) (68,700+ stars).

Mem0 provides intelligent, persistent memory infrastructure for AI coding assistants (Claude Code, Cursor, Codex, Antigravity). It solves "context drift" and conversation fading by automatically storing your coding habits, tech preferences, and formatting rules, re-injecting them dynamically into every prompt turn.

---

## ⚡ How to Install on Any Machine

```bash
# 1. Run the official Mem0 MCP server (requires free API key from mem0.ai or local config):
npx -y @mem0/mcp
```
*(Or install locally via Python: `pip install mem0ai`)*

---

## 🔌 MCP Server Configuration

Add to your tool's `mcpServers` configuration (`claude_desktop_config.json`, `.cursor/mcp.json`, or Antigravity):

```json
{
  "mcpServers": {
    "mem0": {
      "command": "npx",
      "args": ["-y", "@mem0/mcp"],
      "env": {
        "MEM0_API_KEY": "YOUR_MEM0_API_KEY"
      }
    }
  }
}
```

*(For completely local, self-hosted memory without external cloud APIs, configure Mem0 with local SQLite or Qdrant).*

---

## 🎯 What Your Agent Remembers

- **Personal Preferences:** Preferred package managers (`pnpm`, `bun`), styling frameworks, indentation rules, and commit message formats.
- **Architectural Rules:** Which libraries are strictly forbidden in your repo, API design patterns, and deployment guidelines.
- **Cross-Chat Memory:** Start a fresh chat tomorrow or open a new terminal on your work laptop—your agent instantly knows your preferences without re-prompting.

---

## 📦 Files in this Skill

- [`SKILL.md`](./SKILL.md) — Master skill definition & memory tools reference.
- [`AGENTS.md`](./AGENTS.md) — Operational guidelines for memory extraction and retrieval.
- [`WHAT_THIS_DOES.txt`](./WHAT_THIS_DOES.txt) — Quick 5-second plain-English summary and example.

# Microsoft Playwright MCP: Browser Automation for AI Agents

> *"Control browsers, click, fill forms, and take screenshots directly from your AI agent."* — Created by [Microsoft](https://github.com/microsoft/playwright-mcp) (39,300+ stars).

Microsoft Playwright MCP connects AI coding assistants (Claude Code, Cursor, Codex, Antigravity) to real Chromium, Firefox, and WebKit browsers. It allows agents to interact with web pages, fill out complex forms, test frontend apps, and capture visual screenshots.

---

## ⚡ How to Install on Any Machine

```bash
# 1. Run the official Microsoft Playwright MCP server with npx (Node 18+ required):
npx -y @playwright/mcp@latest
```
*(Or add the configuration block below to your client's MCP configuration).*

---

## 🔌 MCP Server Configuration

Add to your tool's `mcpServers` configuration (`claude_desktop_config.json`, `.cursor/mcp.json`, or Antigravity):

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    }
  }
}
```

---

## 🎯 What Your Agent Can Do

- **Autonomous Web Browsing:** Agents can visit live websites, follow pagination, and extract structured data.
- **Local Dev Server Verification:** Instruct your agent: *"Open http://localhost:3000, fill out the signup form, click Submit, and take a screenshot of the dashboard."*
- **End-to-End Regression Testing:** Verifies responsive design, mobile viewports, and interactive animations.

---

## 📦 Files in this Skill

- [`SKILL.md`](./SKILL.md) — Master skill definition & available browser tools list.

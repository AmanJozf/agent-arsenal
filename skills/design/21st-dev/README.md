# 21st.dev: Design Engineer & UI Component Generator for AI Agents

> *"It's like v0, but running directly inside your Cursor, Claude Code, or Antigravity workspace."* — Created by [21st.dev](https://21st.dev) (6,400+ stars).

21st.dev gives AI coding assistants direct access to a marketplace of over 10,000+ production-ready React, Tailwind CSS, Framer Motion, and shadcn-compatible components, plus on-demand AI UI generation and brand SVG logo search.

---

## ⚡ How to Install on Any Machine

```bash
# 1. Initialize the 21st MCP server for your client (Cursor, Claude, VS Code, or Codex):
npx @21st-dev/cli@latest init --client cursor   # replace 'cursor' with 'claude' or 'vscode'
```
*(Grab a free API key at [21st.dev/mcp](https://21st.dev/mcp) — or add the MCP configuration JSON manually below).*

---

## 🔌 MCP Server Configuration

Add to your tool's `mcpServers` configuration (`claude_desktop_config.json`, `.cursor/mcp.json`, or Antigravity settings):

```json
{
  "mcpServers": {
    "21st": {
      "url": "https://21st.dev/api/mcp",
      "headers": {
        "x-api-key": "YOUR_21ST_API_KEY"
      }
    }
  }
}
```

---

## 🎯 What Your Agent Can Do with 21st.dev

- **Search Existing Components:** `search "animated pricing card"` — instantly finds polished, responsive components with dark mode and Tailwind styling.
- **Generate Custom UI:** `generate "minimalist fintech onboarding flow with step progress"` — creates production JSX/TSX on the fly.
- **Fetch Brand Logos:** `search_logo "Stripe"` — pulls crisp, official SVG/React logo components into your project.
- **Inspect Design Inspiration:** `get_inspiration` — returns trending, community-vetted design patterns for any page block.

---

## 📦 Files in this Skill

- [`SKILL.md`](./SKILL.md) — Master 21st UI skill definition.
- [`llms-install.md`](./llms-install.md) — Agent-specific setup guide across all major IDEs.
- [`server.json`](./server.json) — MCP server definition schema.
- [`skills/`](./skills/) — Sub-skills collection (`21st-ui-build`, `21st-ui-explore`, `21st-ui-review`, `21st-design-sync`, `21st-registry`).

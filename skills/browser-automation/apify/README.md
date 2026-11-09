# Apify MCP Server: Web Scraping & Cloud Automation

> *"Extract data from any website, search Google, and run 1,500+ cloud scrapers directly from your AI agent."* — Created by [Apify](https://github.com/apify/apify-mcp-server) (15,400+ stars).

Apify MCP server connects AI coding assistants (Claude Code, Cursor, Codex, Antigravity) to Apify's cloud platform. It enables agents to bypass anti-bot protections, extract clean markdown/JSON from websites, search Google in real-time, and scrape social networks without writing complex scraping logic from scratch.

---

## ⚡ How to Install on Any Machine

```bash
# 1. Run the Apify MCP server via npx (requires free API token from apify.com):
npx -y @apify/actors-mcp-server
```
*(Add your `APIFY_TOKEN` into your environment or client configuration below).*

---

## 🔌 MCP Server Configuration

Add to your tool's `mcpServers` configuration (`claude_desktop_config.json`, `.cursor/mcp.json`, or Antigravity):

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": ["-y", "@apify/actors-mcp-server"],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_API_TOKEN"
      }
    }
  }
}
```

---

## 🎯 Popular Agent Use Cases

- **Real-Time Google Search:** Query Google via official Apify actors to ground agent reasoning with fresh web results.
- **Social Media Extraction:** Scrape trending YouTube video transcripts, Twitter/X posts, and Reddit discussions.
- **LLM-Ready Web Crawling:** Crawl documentation sites and convert all nested pages into clean markdown for embeddings or context loading.

---

## 📦 Files in this Skill

- [`SKILL.md`](./SKILL.md) — Master skill definition & actor execution guidelines.
- [`AGENTS.md`](./AGENTS.md) — Operational rules and output format constraints.

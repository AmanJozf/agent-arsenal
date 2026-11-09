# FreeLLMAPI: Coding Agent Setup Guide

FreeLLMAPI includes built-in generator commands that inspect the models your local gateway is serving and automatically write the exact configuration files expected by each coding assistant.

---

## ⚡ The Setup Generators

Instead of manually crafting JSON/TOML configuration files, run the generator for your tool:

```bash
# General Syntax
npx freellmapi setup-<tool> --url http://localhost:3001 --api-key <unified-key>
```

Add `--dry-run` to preview the configuration diff before writing to disk.

---

## 🛠️ Tool-by-Tool Commands

### 1. Claude Code
Configures Claude Code to route through FreeLLMAPI's Anthropic Messages wire endpoint:
```bash
npx freellmapi setup-claude --url http://localhost:3001 --api-key <unified-key>
```
*Tip: To run Claude Code without saving plain-text API keys to disk, use the in-memory runner:*
```bash
npx freellmapi launch --url http://localhost:3001 --api-key <unified-key>
```

### 2. Cursor
Configures Cursor's OpenAI-compatible base URL and models:
```bash
npx freellmapi setup-cursor --url http://localhost:3001 --api-key <unified-key>
```

### 3. Codex CLI
Configures OpenAI Codex CLI with the Responses wire API:
```bash
npx freellmapi setup-codex --url http://localhost:3001 --api-key <unified-key>
# Or run with in-memory credentials:
npx freellmapi launch-codex --url http://localhost:3001 --api-key <unified-key>
```

### 4. OpenCode / Kilo Code
Generates or updates `opencode.json`:
```bash
npx freellmapi setup-opencode --url http://localhost:3001 --api-key <unified-key>
```

### 5. Cline / Roo Code (VS Code)
```bash
npx freellmapi setup-cline --url http://localhost:3001 --api-key <unified-key>
npx freellmapi setup-roo --url http://localhost:3001 --api-key <unified-key>
```

### 6. Aider
```bash
npx freellmapi setup-aider --url http://localhost:3001 --api-key <unified-key>
```

### 7. Continue (VS Code & JetBrains Autocomplete)
```bash
npx freellmapi setup-continue --url http://localhost:3001 --api-key <unified-key>
```

### 8. Antigravity & Generic OpenAI Clients
Point your custom client to:
- **Base URL:** `http://localhost:3001/v1`
- **API Key:** `<your-unified-key>`
- **Model:** `freellmapi/auto` or any specific model from `http://localhost:3001/v1/models`

---

## 🔑 Useful Flags

| Flag | Description |
|---|---|
| `--dry-run` | Prints the configuration diff without modifying any files. |
| `--profile <name>` | Writes a named profile rather than overwriting the default profile. |
| `--url <url>` | FreeLLMAPI server URL (defaults to `http://localhost:3001`). |
| `--api-key <key>` | Unified API key from your FreeLLMAPI dashboard. |

# OmniRoute Drop-in Agent Skills Reference

OmniRoute exposes 45 specialized sub-skills divided into API skills (REST) and CLI management skills.

## Core API Skills

- **`omni-auth`**: API key authentication, Bearer tokens, and session management.
- **`omni-providers`**: Manage 375+ provider connections, API keys, and connection testing.
- **`omni-models`**: Query available models and resolve cross-provider model aliases.
- **`omni-combos-routing`**: Create and tune routing strategies (priority, weighted, round-robin, Auto-combo).
- **`omni-compression`**: RTK, Caveman, and stacked token compression (15-95% reduction).
- **`omni-resilience`**: Circuit breakers, p50/p95/p99 latency tracking, and budget guards.
- **`omni-mcp`**: 110+ MCP tools across 33 scopes over SSE, stdio, and Streamable HTTP.
- **`omni-agents-a2a`**: 6 A2A autonomous agent coordination skills via JSON-RPC 2.0.

## Core CLI Skills

- **`cli-serve`**: Daemon lifecycle, port settings, system tray, and auto-recovery.
- **`cli-skill-collector`**: Auto-detect installed agent CLI tools and install matching skills from GitHub.
- **`cli-compression`**: Test and preview compression efficiency on real prompts.
- **`cli-cost-usage`**: Cost breakdown, token expenditure, and connection audits.
- **`config-codex-cli`**: Automated configuration script for Codex CLI backends.

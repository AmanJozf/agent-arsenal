---
name: omniroute
description: >
  AI Gateway & Model Router: route any coding agent (Claude Code, Cursor, Codex,
  OpenCode, Cline, Antigravity) through 375+ LLM providers (150+ free) and 1,400+ models
  via a unified OpenAI-compatible endpoint. Features quota-aware auto-fallback,
  RTK + Caveman prompt compression (15-95% token savings), and MCP/A2A agent protocol.
argument-hint: "[serve|status|compress|models|fallback]"
license: MIT
---

# OmniRoute: AI Gateway & Smart Agent Router

OmniRoute connects AI coding assistants and agents to over 375 providers and 1,400+ models through a single local or self-hosted endpoint, ensuring developers never hit rate limits, quotas, or context window limits.

## Core Capabilities

1. **Unified Endpoint:** Standard OpenAI/Anthropic-compatible proxy running at `http://localhost:20128`.
2. **Quota-Aware Fallbacks:** Automatically routes requests to backup providers when primary models rate-limit or fail.
3. **Prompt Compression:** Integrated RTK + Caveman engines compress prompts by 15% to 95% without loss of reasoning accuracy.
4. **Agent-to-Agent (A2A) & MCP:** Exposes 110+ MCP tools and JSON-RPC 2.0 A2A protocols for autonomous coordination.
5. **Skill Collector:** Automatically scans and provisions agent skills into detected coding CLI environments.

## Agent Usage Instructions

When interacting with or configuring OmniRoute for coding agents:
- **Default Endpoint:** `http://localhost:20128/v1`
- **API Key:** Use the local master key configured during `omniroute setup` (or default local bearer token).
- **Model Aliases:**
  - `auto`: Best available model using smart-routing score
  - `cheap`: Lowest-cost model capable of completing the task
  - `fast`: Lowest-latency p50/p95 provider
  - Provider-specific: e.g. `claude-3-7-sonnet`, `gemini-2.5-pro`, `deepseek-v3`, `gpt-4o`

## Quick Commands

- Start gateway server: `omniroute serve --daemon`
- Check provider & gateway health: `omniroute health`
- Test prompt compression: `omniroute compression test --preset high`
- Scan & install CLI agent skills: `omniroute skills scan --auto-install`

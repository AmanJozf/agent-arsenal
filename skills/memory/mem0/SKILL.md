---
name: mem0
description: >
  The Memory Layer for AI Agents: provides persistent, adaptive long-term memory
  across chat sessions and projects. Remembers user preferences, coding styles,
  conventions, and project context so the agent never forgets past instructions.
argument-hint: "[recall|store|search|forget]"
license: Apache-2.0
---

# Mem0: Persistent Memory Layer for AI Agents

Mem0 gives AI coding agents long-term, cross-session memory. Instead of re-explaining your coding conventions, preferred packages, architecture styles, or output preferences in every chat, Mem0 stores them in an adaptive vector graph and injects relevant context automatically on every turn.

## Core Capabilities

1. **Preference Persistence:** Automatically captures user preferences (e.g. "I prefer pnpm over npm", "Always write short commit messages", "Use Tailwind v4 syntax").
2. **Context Continuity:** Carries critical architectural decisions and bug history from yesterday's session into today's session.
3. **Adaptive Graph Memory:** Connects related entities (projects, repositories, libraries, developers) for associative retrieval.
4. **Universal Client Support:** Runs via MCP server (`@mem0/mcp`), local Python/TypeScript SDK, or self-hosted Qdrant/SQLite storage.

## Agent Memory Operations

- `search_memory` — Search stored user memories for relevant preferences before answering.
- `add_memory` — Store a new user preference, convention, or project fact permanently.
- `update_memory` — Update an existing memory when the user's preferences change.
- `delete_memory` — Forget outdated or deprecated guidelines.

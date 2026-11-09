# Mem0 Agent Operational Guidelines

When working as an AI assistant integrated with Mem0, follow these memory governance rules.

## Autonomous Memory Lifecycle

1. **Passive Retrieval (Start of Task):**
   At the beginning of any non-trivial coding task, query memory for:
   - User style preferences (`commit style`, `package manager`, `testing library`).
   - Project constraints (`Node version`, `forbidden dependencies`, `formatting rules`).

2. **Explicit Storage (When User Corrects or Instructs):**
   Whenever the user corrects your behavior or expresses an enduring preference (e.g., *"Don't use classes here, I prefer functional components"* or *"Always format commit messages in lowercase"*):
   - Automatically save that fact via `add_memory`.
   - Acknowledge that the rule has been committed to long-term memory.

3. **Noise Filtering:**
   Do NOT store temporary, transient task data (e.g. "User is fixing line 42 of index.ts"). Only store enduring preferences and architectural decisions.

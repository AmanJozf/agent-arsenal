# FreeLLMAPI Agent Operational Guide & Rules

When acting as an AI assistant interacting with or configuring FreeLLMAPI, follow these single-source-of-truth principles.

## Gateway Protocols & Routing

1. **Protocol Selection by Client:**
   - **Claude Code:** Route to Anthropic Messages wire at `http://localhost:3001` (set `ANTHROPIC_BASE_URL`).
   - **Codex CLI:** Uses Responses Wire API at `http://localhost:3001/v1` (`wire_api = "responses"`).
   - **OpenAI Clients / Antigravity / Cursor:** Standard OpenAI Chat at `http://localhost:3001/v1/chat/completions`.

2. **Automated Configuration Rule:**
   Never instruct users to manually construct intricate configuration files for supported tools. Always prefer the built-in generator:
   ```bash
   npx freellmapi setup-<tool> --url http://localhost:3001 --api-key <key>
   ```
   Add `--dry-run` to preview the generated diff before writing.

3. **Fallback Chain Behavior:**
   - Provider rate limits (`429`) are caught internally by the FreeLLMAPI router and immediately switched to the next provider in the chain.
   - Do not implement aggressive client-side retries; let the FreeLLMAPI fallback router manage provider exhaustion.

4. **Security & Key Management:**
   - Provider API keys are AES-encrypted on disk at `~/freellmapi/.env`.
   - For ephemeral CI/CD environments or sensitive machines, use `npx freellmapi launch` to run coding agents with in-memory credential injection.

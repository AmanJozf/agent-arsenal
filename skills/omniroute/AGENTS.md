# OmniRoute Agent Guide & Operational Rules

When operating as an agent working with or configuring OmniRoute, follow these single-source-of-truth guidelines.

## Architecture & Integration Principles

1. **Proxy Endpoint Protocol:**
   OmniRoute serves an OpenAI/Anthropic compatible gateway.
   - Base URL: `http://localhost:20128/v1` (or configured port)
   - Header: `Authorization: Bearer <omniroute-api-key>`

2. **Routing & Combos:**
   - Always prefer defined routing combos over hardcoding single upstream providers.
   - For coding agents requiring long contexts, enable RTK context compression (`--compress rtk`).
   - For high-reliability background jobs, enable session affinity (`sessionAffinityTtlMs > 0`) to preserve KV-cache prompt continuity.

3. **Fallback Chains:**
   When primary endpoints return `429 (Rate Limit)` or `503 (Unavailable)`, OmniRoute transparently steps through fallback chains without dropping the client stream.
   Do not retry client-side immediately; allow OmniRoute's internal circuit breakers and backoff levels to manage provider switching.

4. **Token Conservation:**
   - Use Caveman compression mode for verbose diagnostic logs and long bash outputs.
   - Strip redundant markdown decorative noise before sending large multi-file diffs.

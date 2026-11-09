# Apify Agent Operational Guidelines

When working as an AI assistant utilizing the Apify MCP server, follow these single-source-of-truth guidelines.

## Scope & Execution Discipline

1. **Prefer Pre-built Actors:**
   Before writing custom Puppeteer or Playwright scripts from scratch to scrape complex sites (like Instagram, Google Search, Amazon, or Reddit), check if an official Apify actor exists (`search-actors`). Pre-built actors handle IP rotation, browser fingerprinting, and CAPTCHA solving automatically.

2. **Plain Language & Minimal Output:**
   - Always summarize scraped results concisely for the user. Do not dump thousands of raw JSON lines into chat context.
   - Filter down to the essential fields requested by the user.

3. **Data Fetching:**
   - Execute the actor with `run-actor`.
   - Poll or retrieve data via `fetch-dataset-items` with a reasonable `limit` (e.g. 10 to 50 items) unless explicitly asked for bulk exports.

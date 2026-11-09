---
name: apify
description: >
  Apify MCP Server: Web scraping, crawling, and cloud actors. Allows AI agents
  to extract data from any website, search Google, scrape social media (X, YouTube,
  Instagram, LinkedIn), and run 1,500+ pre-built web scrapers via MCP.
argument-hint: "[scrape|search|crawl|actor]"
license: Apache-2.0
---

# Apify MCP Server: Web Scraping & Cloud Actors

This skill connects AI coding assistants and agents to Apify's cloud ecosystem of over 1,500+ specialized web scrapers and automation Actors via the Model Context Protocol (MCP).

## Core Capabilities

1. **Website Content Scraping:** Extract structured markdown, text, and tables from any public URL without getting blocked by anti-bot protections.
2. **Search Engine & Social Scraping:** Direct access to Google Search results, YouTube transcripts, Reddit threads, Twitter/X posts, and LinkedIn profiles.
3. **Actor Discovery & Execution:** Search the Apify store for dedicated scrapers, execute them with custom parameters, and fetch JSON datasets in seconds.
4. **Resilient Data Pipelines:** Offload long-running web crawling jobs to cloud infrastructure without burdening local machine bandwidth.

## Key Available Tools

- `search-actors` — Search Apify Store for scrapers matching any target website or domain.
- `run-actor` — Execute a specific Apify actor with input parameters.
- `fetch-dataset-items` — Retrieve structured JSON rows from an executed scraping run.
- `rag-web-browser` — Scrape and convert web pages directly into clean LLM-ready markdown.

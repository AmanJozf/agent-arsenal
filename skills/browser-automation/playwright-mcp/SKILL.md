---
name: playwright-mcp
description: >
  Browser automation and web testing with Microsoft Playwright. Allows AI agents
  to navigate web pages, click elements, fill forms, scroll, take screenshots,
  and inspect accessibility trees using structured snapshots.
argument-hint: "[navigate|click|snapshot|screenshot|fill]"
license: Apache-2.0
---

# Microsoft Playwright MCP: Agent Browser Automation

This skill connects AI coding assistants and agents to Microsoft Playwright via the Model Context Protocol (MCP). It enables agents to browse the live web, test local web applications, click buttons, fill forms, and take high-resolution screenshots.

## Core Capabilities

1. **Accessibility Snapshot Navigation:** Instead of relying on slow vision models, inspects the page via fast semantic accessibility snapshots.
2. **Interactive Controls:** Click, type, press keyboard shortcuts, hover, drag, and scroll through complex interactive single-page apps.
3. **Deterministic Testing:** Run automated end-to-end verification tests against local dev servers (`localhost:3000`, `localhost:5173`, etc.).
4. **Visual Evidence:** Capture full-page or element-specific PNG screenshots for visual bug reports.

## Available Agent Tools

- `browser_navigate` — Navigate to any URL.
- `browser_snapshot` — Return a text snapshot of the page's accessibility tree.
- `browser_click` — Click a button, link, or DOM element.
- `browser_type` / `browser_fill` — Type text into an input or textarea.
- `browser_press_key` — Press keyboard keys (Enter, Escape, Tab, etc.).
- `browser_hover` — Hover over an element to trigger dropdowns or tooltips.
- `browser_scroll` — Scroll up or down by pixel offset.
- `browser_screenshot` — Capture a visual screenshot of the current page.

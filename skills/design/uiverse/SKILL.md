---
name: uiverse
description: Access 3,000+ open-source CSS & Tailwind UI micro-components (buttons, loaders, toggles, cards, inputs) with zero npm bloat.
tools:
  - component_fetcher
  - css_generator
---

# Uiverse Galaxy Skill

This skill equips your AI coding agent with the 3,000+ element open-source collection from [uiverse.io](https://uiverse.io) and `uiverse-io/galaxy` (14,000+ GitHub stars).

## Capabilities
- **Zero-Dependency Micro-Components:** Buttons, switches, loaders, inputs, and cards built with pure CSS & Tailwind.
- **Instant Search & Fetch:** Query the live Uiverse open-source repository directly via `scripts/fetch_element.py`.
- **Pre-Curated Top Patterns:** Built-in templates in `components/` for buttons, cards, loaders, switches, and inputs.

## Usage
Ask your agent to generate or drop in a Uiverse element:
```text
/uiverse Add a futuristic cyber button to the header
```
Or use the CLI fetcher:
```bash
python scripts/fetch_element.py list --category loaders
python scripts/fetch_element.py fetch --category loaders --name "0xnihilism_brown-puma-30.html" -o spinner.html
```

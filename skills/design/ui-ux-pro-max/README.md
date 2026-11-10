# 🌟 UI/UX Pro Max: Design Intelligence for AI Agents

> Based on the #1 design intelligence repository by [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (147,000+ stars).

An AI skill that provides searchable design intelligence—including product-specific color palettes, font pairings, UI aesthetics, chart guidelines, and UX anti-pattern checklists—across 7 modular sub-skills.

---

## ⚡ How to Install on Any Machine (2-Line Guide)

```bash
# Copy universal UI/UX Pro Max rules into your project
curl -fsSL https://raw.githubusercontent.com/AmanJozf/agent-arsenal/main/skills/design/ui-ux-pro-max/AGENTS.md -o AGENTS.md
```

---

## 💡 What This Does

* **Searchable Design Intelligence:** Query hundreds of battle-tested design tokens by domain:
  ```bash
  python src/ui-ux-pro-max/scripts/search.py "fintech" --domain color
  python src/ui-ux-pro-max/scripts/search.py "modern clean" --domain typography
  ```
* **7 Modular Sub-Skills:**
  - `ui-ux-pro-max/`: Search engine & core directives
  - `design-system/`: Component guidelines & token contracts
  - `ui-styling/`: CSS & Tailwind micro-styling
  - `design/`: Layout hierarchy & responsiveness
  - `brand/`: Color palettes & visual identity
  - `banner-design/`: High-impact hero graphics
  - `slides/`: Presentation deck systems
* **Prevents AI Slop:** Hard guardrails stopping generic purple blobs, bad mobile contrast, and awkward nested cards.

---

## 🚀 How to Use

Instruct your AI agent:
```text
Apply UI/UX Pro Max: build a dashboard overview using the modern clean typography scale and a high-contrast dark theme.
```

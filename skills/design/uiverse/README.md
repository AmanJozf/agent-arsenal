# 🌌 Uiverse Galaxy: Open-Source CSS & Tailwind Micro-Components

> Based on the 14,000+ star open-source repository by [uiverse-io/galaxy](https://github.com/uiverse-io/galaxy).

A curated universe of over 3,000+ community-built UI micro-components—including neon buttons, 3D hover cards, animated toggle switches, smooth loaders, and stylish inputs—using pure CSS and Tailwind with **zero external npm dependencies**.

---

## ⚡ How to Install on Any Machine (2-Line Guide)

```bash
# Copy the universal agent instructions into your target project
curl -fsSL https://raw.githubusercontent.com/AmanJozf/agent-arsenal/main/skills/design/uiverse/AGENTS.md -o AGENTS.md
```

---

## 💡 What This Does

* **Zero External Dependencies:** Every component runs on pure HTML and CSS/Tailwind. No heavy UI framework installations needed.
* **Pre-Curated Top Patterns:** Includes ready-to-use templates in `components/`:
  - `components/buttons/`: Neon glow and 3D cyber buttons
  - `components/loaders/`: High-aesthetic animated spinners and orbital loaders
  - `components/cards/`: Glassmorphic and 3D tilt cards
  - `components/switches/`: Smooth pill toggles and cyber switches
  - `components/inputs/`: Floating glow and neon border inputs
* **Interactive Fetcher:** Includes `scripts/fetch_element.py` to query and download any of the 3,000+ elements from the Galaxy repo on demand.

---

## 🚀 How to Use

### 1. In Your Agent Prompt
Ask your agent to use Uiverse:
```text
Add an animated Uiverse loading spinner and a 3D glassmorphism card to this dashboard in pure CSS.
```

### 2. Using the CLI Component Fetcher
List elements from any category:
```bash
python scripts/fetch_element.py list --category loaders --limit 5
```

Download a specific element into your project:
```bash
python scripts/fetch_element.py fetch --category loaders --name "0xnihilism_brown-puma-30.html" -o src/components/Loader.html
```

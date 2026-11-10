# 📸 Screenshot to Code: Visual Frontend Generation

> Based on the viral 65,000+ star open-source project by [abi/screenshot-to-code](https://github.com/abi/screenshot-to-code).

Converts any UI screenshot, Figma mockup, or whiteboard wireframe into clean, responsive HTML, React, or Vue code using Tailwind CSS.

---

## ⚡ How to Install on Any Machine (2-Line Guide)

```bash
# Copy the universal agent vision rules into your target project
curl -fsSL https://raw.githubusercontent.com/AmanJozf/agent-arsenal/main/skills/design/screenshot-to-code/AGENTS.md -o AGENTS.md
```

---

## 💡 What This Does

* **Exact Visual Matching:** Analyzes colors, typography, paddings, borders, shadows, and grids from any uploaded image.
* **Component Extraction:** Recreates buttons, cards, navigation headers, forms, and pricing matrices with semantic elements.
* **Responsive by Default:** Automatically structures the layout using Tailwind Flexbox and Grid (`col-span`, `gap`, `sm:`, `md:`, `lg:`).
* **Multi-Framework:** Generates single-file HTML, modern React (Next.js / Vite), or Vue components.

---

## 🚀 How to Use

### In Any AI Assistant (Cursor, Antigravity, Claude Code, Windsurf)
1. Paste or attach your screenshot into the chat window.
2. Provide this simple prompt:
   ```text
   Recreate this UI screenshot in React + Tailwind CSS. Follow the rules in AGENTS.md.
   ```
3. The assistant will inspect the image and output the matching component code.

### Running the Full Local Server
If you want to run the full original local web UI with Docker:
```bash
git clone https://github.com/abi/screenshot-to-code.git
cd screenshot-to-code
docker compose up -d --build
# Open http://localhost:5173
```

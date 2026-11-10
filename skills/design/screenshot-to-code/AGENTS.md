# Screenshot to Code: Universal Agent Instructions

These instructions guide any AI coding agent (Claude Code, Cursor, Antigravity, OpenCode, Codex) to convert visual screenshots, design mockups, and wireframes into pixel-perfect frontend code.

---

## 🎯 Role & Objective
You are an expert senior frontend engineer and design technologist. When given an image (screenshot, Figma export, wireframe, or photo of a whiteboard UI):
1. Analyze the layout grid, responsive containers, and visual hierarchy.
2. Extract exact copy, labels, icons, and button states.
3. Match font sizes, weights, line heights, colors, padding, borders, and shadows.
4. Output clean, responsive code using **Tailwind CSS** and semantic HTML or React JSX.

---

## 🛠️ Replication Rules

### 1. Typography & Hierarchy
- Identify primary headings (`h1`, `h2`), body copy, metadata captions, and microcopy.
- Match font scale (`text-xs` through `text-5xl`) and weights (`font-normal`, `font-medium`, `font-semibold`, `font-bold`).
- Ensure contrast ratios meet WCAG AA standards.

### 2. Spacing & Layout
- Use modern Flexbox and CSS Grid layouts (`grid grid-cols-1 md:grid-cols-3 gap-6`).
- Maintain exact visual padding (`p-4`, `p-6`, `p-8`) and margins matching the screenshot.
- Keep components centered with standard containers (`max-w-7xl mx-auto px-4 sm:px-6 lg:px-8`).

### 3. Colors & Theme
- Extract exact brand hex codes or map to the nearest standard Tailwind colors (e.g. `indigo-600`, `zinc-900`, `slate-100`).
- If dark mode is shown, apply clean dark-mode classes (`bg-zinc-950 text-zinc-100 border-zinc-800`).

### 4. Icons & Assets
- Use inline SVGs or standard icon names from **Lucide** / **Heroicons** / **FontAwesome**.
- For images, use high-quality Unsplash image URLs with descriptive terms (e.g. `https://images.unsplash.com/photo-...?auto=format&fit=crop&w=800&q=80`).

### 5. Interactivity
- Add hover, focus, and active states (`hover:bg-indigo-700 transition-colors duration-150`).
- Add accessible focus rings (`focus:outline-none focus:ring-2 focus:ring-indigo-500`).

---

## ⚡ Direct Prompt Template

When feeding a screenshot to your agent, use this prompt:

```text
Look at this screenshot and write clean, responsive [HTML + Tailwind CSS / React + Tailwind CSS] that matches it 1:1.
Replicate all sections: navigation, hero, cards, typography, colors, and button states.
Ensure the layout is mobile-responsive and self-contained.
```

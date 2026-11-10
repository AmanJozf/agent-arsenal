# Uiverse: Universal Agent Instructions

These instructions guide any AI coding agent (Claude Code, Cursor, Antigravity, OpenCode, Codex) to integrate community-crafted CSS and Tailwind UI micro-components from Uiverse into modern web applications without installing heavy external npm libraries.

---

## 🎯 Role & Objective
You are an expert design engineer. When asked to add creative buttons, loading states, animated switches, glassmorphic cards, or form inputs:
1. Prefer lightweight, pure CSS or Tailwind solutions over bulky third-party component libraries.
2. Leverage the Uiverse component patterns (in `components/` and `scripts/fetch_element.py`).
3. Ensure all micro-interactions are smooth (60fps GPU-accelerated transforms and opacity).
4. Maintain accessibility: preserve focus rings, aria attributes, keyboard navigation, and semantic tags (`<button>`, `<input>`, `<label>`).

---

## 🛠️ Integration Patterns

### 1. React / Next.js Integration
When porting a Uiverse `.html` snippet into a React component:
- Convert inline `style` tags into CSS Modules (`Component.module.css`), styled-jsx, or Tailwind utility classes.
- Ensure `class` attributes become `className`.
- Replace `for` in `<label>` with `htmlFor`.

### 2. Pure Tailwind CSS Porting
Many Uiverse elements use raw CSS keyframes. When embedding into a Tailwind project:
- Put custom `@keyframes` into `tailwind.config.js` or `globals.css`.
- Map colors to the project's CSS variables (`hsl(var(--primary))`).

### 3. Loading Spinners & Indicators
- Always include an accessible label: `aria-label="Loading..."` and `role="status"`.
- Provide smooth enter/exit transitions so loaders do not pop abruptly.

---

## ⚡ Direct Prompt Template

When asking an assistant to add a Uiverse component:

```text
Add a modern Uiverse-style [neon button / glassmorphism card / smooth pill toggle / animated loader].
Keep it completely self-contained in pure CSS / Tailwind with zero external npm dependencies.
```

# Image-First Website Design to Code: Agent Instructions

These instructions guide any AI coding agent (Claude Code, Cursor, Antigravity, OpenCode, Codex) to follow an image-first web design methodology.

---

## 🎯 Directives: Image-First Art Direction

Before rushing into code, visually ambitious websites require an image-first strategy:
1. **Analyze Reference Mockups:** Inspect the layout, spacing, negative space, and visual rhythm.
2. **Avoid "Cards-Inside-Cards":** Do not wrap every element in nested borders or gray boxes. Let typography, whitespace, and layout breathe.
3. **Keep the Hero Spacious:** On laptop screens (1366x768 / 1440x900), ensure the hero headline, subhead, and CTA are instantly visible without scrolling.
4. **Section-by-Section Fidelity:** Build sections independently with high attention to detail rather than generating a generic full-page skeleton all at once.

---

## 🛠️ Stack Rules
- **Tailwind CSS:** For typography scales, flexbox, CSS grid, and responsive modifiers (`sm:`, `md:`, `lg:`).
- **Semantics:** Use standard HTML5 elements (`<nav>`, `<header>`, `<main>`, `<section>`, `<footer>`).
- **Assets:** Use crisp SVG icons and real high-resolution imagery.

---

## ⚡ Direct Prompt Template

```text
Follow the image-to-code art direction rules: inspect this UI mockup, plan the section hierarchy,
avoid cards-inside-cards, and write clean, responsive Tailwind code that matches the visual weight.
```

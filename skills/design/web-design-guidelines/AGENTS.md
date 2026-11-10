# Vercel Web Interface Guidelines: Universal Agent Instructions

These instructions guide any AI coding agent (Claude Code, Cursor, Antigravity, OpenCode, Codex) to audit and write UI code matching Vercel's official Web Interface Guidelines.

---

## 🎯 Role & Objective
You are a senior frontend engineer enforcing the official Vercel Web Interface Guidelines.
When asked to review, write, or polish web UI code, check against these core rules:

### 1. Accessibility (a11y)
- **Buttons & Links:** Use `<button>` for actions, `<a>`/`<Link>` for navigation. Never `<div onClick>`.
- **Labels:** Icon-only buttons must have `aria-label`. Form controls must have `<label>` or `aria-label`.
- **Keyboard Navigation:** All interactive elements must have keyboard handlers (`onKeyDown`/`onKeyUp`) and visible focus states (`focus-visible:ring-2`).
- **Live Regions:** Dynamic status changes and toasts must use `aria-live="polite"`.
- **Images:** All `<img>` tags must include meaningful `alt` text (or `alt=""` if decorative).

### 2. Layout, Typography & Whitespace
- **Hierarchy:** Strict hierarchical headings (`<h1>` through `<h6>`).
- **Scroll Anchors:** Add `scroll-margin-top` to headings targeted by anchor links so fixed headers don't overlap content.
- **Responsive Overflow:** Never allow accidental horizontal scrolling on mobile viewports (`overflow-x-hidden`).
- **Touch Targets:** Minimum 44x44px touch targets for mobile interactive elements.

### 3. Performance & Animation
- **Transforms & Opacity:** Animate only `transform` and `opacity` to avoid GPU-expensive layout thrashing.
- **Prefers Reduced Motion:** Respect user preferences via `motion-reduce:transition-none`.
- **Image Sizing:** Always set explicit `width` and `height` or `aspect-ratio` to avoid Cumulative Layout Shift (CLS).

---

## ⚡ Direct Review Prompt

```text
Review this UI file against Vercel Web Interface Guidelines:
Check accessibility, keyboard navigation, touch targets, layout shifts, and semantic HTML.
Output findings in concise `file:line - issue - fix` format.
```

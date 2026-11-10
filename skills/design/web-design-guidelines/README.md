# 📐 Vercel Web Interface Guidelines

> Based on the official [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) repository and [web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines).

Enforces Vercel's production standards for web application design, frontend architecture, accessibility (WCAG AA), responsive touch targets, and layout performance.

---

## ⚡ How to Install on Any Machine (2-Line Guide)

```bash
# Copy the universal Vercel Web Design Guidelines into your project
curl -fsSL https://raw.githubusercontent.com/AmanJozf/agent-arsenal/main/skills/design/web-design-guidelines/AGENTS.md -o AGENTS.md
```

---

## 💡 What This Does

* **Accessibility & Semantics:** Eliminates `<div onClick>` antipatterns, mandates `<button>`/`<Link>` tags, enforces keyboard navigation, and ensures ARIA live regions for async states.
* **Layout Shift Prevention:** Enforces explicit aspect ratios, safe scroll-margins on heading anchors, and mobile viewport containment.
* **Terse Audit Reporting:** Outputs findings in clean `file:line - problem - recommended fix` syntax for instant remediation.

---

## 🚀 How to Use

Run an audit with your AI agent:
```text
Review src/components/Header.tsx for compliance with Vercel Web Interface Guidelines.
```

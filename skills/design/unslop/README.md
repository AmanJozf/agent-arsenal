# 🧼 Unslop: Turn Vibecoded UI into Crafted Product Design

> Created by **Damir Sokolovsky** ([@heydamir](https://x.com/heydamir) · [heydamir.design/unslop](https://heydamir.design/unslop)).  
> Original repository: [heydamir/unslop](https://github.com/heydamir/unslop) (Licensed under CC-BY-4.0).

**Unslop** is an agent skill for AI coding assistants (Claude Code, Antigravity, Cursor, Codex) that targets and eliminates the formulaic "AI aesthetic" from generated code, transforming generic screens into distinct, human-crafted interfaces.

---

## ⚡ Quick Install (2-Line Guide)

Drop the universal Unslop rules directly into any project workspace:

```bash
curl -fsSL https://raw.githubusercontent.com/AmanJozf/agent-arsenal/main/skills/design/unslop/AGENTS.md -o AGENTS.md
```

Or install natively via package runners:
```bash
npx skills add heydamir/unslop
```

---

## 💡 What This Does

Standard LLM code generation suffers from repetitive design habits:
* Purple/indigo gradients on dark backdrops
* Glowing neon cards and gradient text
* Gratuitous emoji prefixes on buttons and tags (🚀, ✨, ⚡)
* Overused uppercase tracked labels (`TRACKED OVERVIEW`)
* Cards nested inside cards with uniform 16px/24px padding

**Unslop conducts a structured redline review in 9 strict passes:**
1. **Spacing:** Fix margins, rhythm, and section padding.
2. **Color:** Neutralize chrome; define 1 tinted neutral and 1 accent.
3. **Icons:** Remove spam emojis; unify stroke weights.
4. **Copy:** Rewrite formulaic marketing hype into clear, grounded language.
5. **Type:** Establish high-contrast optical hierarchy.
6. **Layout:** Simplify card-in-card nesting and structure page flow.
7. **Details:** Hairline borders and soft ambient lighting.
8. **Visuals:** Anchor with one hero moment (rendered object, realistic preview, or custom chart).
9. **Motion:** Snappy 150–200ms transitions without perpetual pulsing effects.

---

## 📂 Included References & Scripts

* `references/signs.md`: Comprehensive catalog of AI slop tells to audit.
* `references/visuals.md`: Recommended art direction styles and failure modes.
* `references/effects.md`: Code recipes and modern frontend treatments.
* `references/rtl.md`: Bidirectional layout rules for Arabic, Persian, Urdu, and Hebrew.
* `references/refs/`: High-resolution visual benchmarks of finished, unslopped screens.
* `scripts/snapshot.mjs`: Utility script to snapshot live URLs or local files for audit.
* `scripts/story.mjs`: Script to generate progress before/after stories.

---

## 🚀 How to Prompt Your Agent

```text
Unslop this screen. Run an audit against references/signs.md, propose a clear 
design direction, and execute the 9 redline passes in order.
```

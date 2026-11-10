# Awesome Design MD: Universal Agent Instructions

These instructions guide any AI coding agent (Claude Code, Cursor, Antigravity, OpenCode, Codex) to build websites matching the exact visual style, color tokens, typography scales, and motion curves of 84+ world-class tech companies and consumer brands.

---

## 🎯 Role & Objective
You are an expert brand technologist. When asked to design or style a page like an iconic company (Stripe, Linear, Apple, Vercel, Supabase, Tesla, Notion, Raycast, etc.):
1. Inspect the target company's `DESIGN.md` in `design-md/<company>/DESIGN.md`.
2. Extract the exact color hex codes (`primary`, `canvas`, `ink`, `hairline`, `accents`).
3. Match font scales, weights, and tracking.
4. Replicate characteristic design signatures (e.g. Stripe's upper gradient mesh, Linear's subtle 1px border glow, Apple's high-contrast typography, Vercel's stark monochrome minimalism).

---

## 📂 Available Brand Systems (84 Total)
Included directly in `design-md/`:
- **Tech & Dev Tools:** `stripe`, `linear.app`, `vercel`, `supabase`, `raycast`, `cursor`, `figma`, `framer`, `posthog`, `resend`, `hashicorp`, `sentry`, `mongodb`, `clickhouse`
- **Consumer & Hardware:** `apple`, `tesla`, `nike`, `spotify`, `airbnb`, `notion`, `intercom`, `mercury`, `revolut`, `wise`, `dji`, `bmw`, `ferrari`
- **AI & Cloud:** `claude`, `x.ai`, `together.ai`, `minimax`, `elevenlabs`, `cohere`, `replicate`, `mistral.ai`

---

## ⚡ Direct Prompt Template

```text
Build a landing page for my product using the [Stripe / Linear / Vercel / Apple] design system.
Read the exact tokens from `design-md/<company>/DESIGN.md` and match its typography, colors, and layout rhythm.
```

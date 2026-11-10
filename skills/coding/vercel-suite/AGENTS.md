# Vercel Labs Agent Skills Suite: Universal Agent Instructions

These instructions guide any AI coding agent (Claude Code, Cursor, Antigravity, OpenCode, Codex) to build, optimize, and deploy high-performance React and Next.js applications according to official Vercel Labs engineering standards.

---

## 🎯 Role & Objective
You are a senior frontend infrastructure engineer following Vercel Labs production best practices across:
1. **React 19 & Next.js Performance (`react-best-practices`):**
   - Use React Server Components (RSC) by default; add `"use client"` only when interactivity, hooks, or browser APIs are required.
   - Stream content with `<Suspense>` boundaries to optimize Time to First Byte (TTFB).
   - Keep client bundles minimal by avoiding heavy third-party packages in client components.
2. **View Transitions (`react-view-transitions`):**
   - Use Next.js View Transitions API for zero-layout-jump page transitions.
3. **Compound Components (`composition-patterns`):**
   - Write composable UI components using slot and render-prop patterns instead of prop-drilling booleans.
4. **Autonomous Deployment (`deploy-to-vercel`):**
   - Configure project environments, build outputs, and trigger preview deployments.

---

## 🛠️ Sub-Skills Included
- `react-best-practices/`: 45 rules for high-performance React architecture
- `react-view-transitions/`: Smooth page transitions via View Transitions API
- `composition-patterns/`: Clean component composition & slots
- `deploy-to-vercel/`: Autonomous deployment to Vercel
- `vercel-optimize/`: Core Web Vitals audit & tuning
- `vercel-cli-with-tokens/`: Automated CLI workflows

---

## ⚡ Direct Prompt Template

```text
Optimize this Next.js app using the Vercel Suite:
Apply react-best-practices to eliminate client bundle bloat, add Suspense streaming,
and implement react-view-transitions for smooth page navigation.
```

# Production-Grade Engineering Skills (by Addy Osmani)

> *"Production-grade engineering skills for AI coding agents."* — Created by [Addy Osmani](https://github.com/addyosmani), Lead Engineer at Google Chrome.

A comprehensive collection of 25 battle-tested engineering skills designed to make AI coding agents (Claude Code, Cursor, Codex, OpenCode, Antigravity) think, plan, and execute like senior software engineers.

---

## ⚡ How to Install on Any Machine

```bash
# 1. In Claude Code, install the official plugin from marketplace:
/plugin marketplace add addyosmani/agent-skills && /plugin install agent-skills@agent-skills
```
*(Or for any other agent like Cursor, Codex, or Antigravity, copy [`AGENTS.md`](./AGENTS.md) and the desired skills from [`skills/`](./skills/) into your workspace).*

---

## 🧭 The 25 Production Engineering Skills

| Category | Skill | Purpose & Trigger |
|---|---|---|
| **Architecture & Design** | [`api-and-interface-design`](./skills/api-and-interface-design/SKILL.md) | Designs robust, ergonomic APIs, function signatures, and interface contracts. |
| | [`spec-driven-development`](./skills/spec-driven-development/SKILL.md) | Drafts rigorous engineering specifications before writing code. |
| | [`constraint-driven-development`](./skills/constraint-driven-development/SKILL.md) | Enforces hard performance, dependency, and architecture boundaries. |
| | [`documentation-and-adrs`](./skills/documentation-and-adrs/SKILL.md) | Generates clear documentation and Architectural Decision Records. |
| | [`deprecation-and-migration`](./skills/deprecation-and-migration/SKILL.md) | Manages graceful legacy code retirement and safe migration pathways. |
| **Planning & Execution** | [`planning-and-task-breakdown`](./skills/planning-and-task-breakdown/SKILL.md) | Breaks large features into ordered, verifiable, bite-sized tasks. |
| | [`incremental-implementation`](./skills/incremental-implementation/SKILL.md) | Ships changes in small, verifiable steps without breaking the build. |
| | [`test-driven-development`](./skills/test-driven-development/SKILL.md) | Writes failing tests first, then minimal code to make them pass (Red-Green-Refactor). |
| | [`git-workflow-and-versioning`](./skills/git-workflow-and-versioning/SKILL.md) | Enforces clean Git hygiene, branch strategies, and semantic versioning. |
| **Quality & Debugging** | [`code-review-and-quality`](./skills/code-review-and-quality/SKILL.md) | Conducts senior-level reviews focusing on edge cases, safety, and correctness. |
| | [`code-simplification`](./skills/code-simplification/SKILL.md) | Refactors messy code into clear, maintainable, idiomatic implementations. |
| | [`debugging-and-error-recovery`](./skills/debugging-and-error-recovery/SKILL.md) | Systematically isolates bugs, traces root causes, and fixes regressions. |
| | [`doubt-driven-development`](./skills/doubt-driven-development/SKILL.md) | Pressure-tests assumptions, edge cases, and failure modes under stress. |
| **Security & Performance** | [`security-and-hardening`](./skills/security-and-hardening/SKILL.md) | Audits and fixes vulnerabilities, injection risks, auth flaws, and data leaks. |
| | [`performance-optimization`](./skills/performance-optimization/SKILL.md) | Diagnoses bottlenecks, optimizes hot paths, memory allocations, and network I/O. |
| | [`observability-and-instrumentation`](./skills/observability-and-instrumentation/SKILL.md) | Implements telemetry, logging, metrics, and distributed tracing. |
| **Frontend & Browser** | [`frontend-ui-engineering`](./skills/frontend-ui-engineering/SKILL.md) | Builds responsive, accessible (a11y), performant web interfaces. |
| | [`browser-testing-with-devtools`](./skills/browser-testing-with-devtools/SKILL.md) | Drives headless browser debugging and automated UI testing via DevTools. |
| **Workflow & Discovery** | [`interview-me`](./skills/interview-me/SKILL.md) | Interviews the developer interactively to clarify ambiguous requirements. |
| | [`idea-refine`](./skills/idea-refine/SKILL.md) | Refines raw concepts and feature ideas into structured engineering proposals. |
| | [`context-engineering`](./skills/context-engineering/SKILL.md) | Curates and packages optimal context windows for downstream agent sessions. |
| | [`source-driven-development`](./skills/source-driven-development/SKILL.md) | Anchors all architectural decisions against verified upstream source code. |
| | [`ci-cd-and-automation`](./skills/ci-cd-and-automation/SKILL.md) | Automates CI/CD pipelines, lint gates, and release automation. |
| | [`shipping-and-launch`](./skills/shipping-and-launch/SKILL.md) | Pre-flight checklists, release verification, and zero-downtime deploy procedures. |
| | [`using-agent-skills`](./skills/using-agent-skills/SKILL.md) | Guides agents on how to discover and activate the right skill for any prompt. |

---

## 🛠️ Usage Across AI Assistants

### 1. Claude Code
Install via marketplace:
```bash
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@agent-skills
```

### 2. Antigravity / Cursor / Windsurf / OpenCode
Link or copy [`AGENTS.md`](./AGENTS.md) and any individual skill from [`skills/`](./skills/) into your project root. The agent will automatically map prompts (e.g. "review this PR" or "write a spec") to the matching skill.

---

## 📦 Files in this Skill Bundle

- [`AGENTS.md`](./AGENTS.md) — Intent-to-skill mapping rules for AI agents.
- [`CLAUDE.md`](./CLAUDE.md) — Claude Code environment and plugin rules.
- [`plugin.json`](./plugin.json) — Official plugin manifest.
- [`skills/`](./skills/) — All 25 complete, unmodified skills, scripts, and references.

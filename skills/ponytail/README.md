# Ponytail: Lazy Senior Dev Mode

> *"He says nothing. He writes one line. It works."*

Ponytail puts a seasoned, pragmatic senior developer into your AI coding assistant. It focuses on the **smallest complete change** that solves the whole task without over-engineering, while never cutting security, accessibility, validation, or tests on critical logic.

---

## ⚡ How to Install on Any Machine

```bash
# 1. Copy the universal rules into your project root:
curl -fsSL https://raw.githubusercontent.com/AmanJozf/agent-arsenal/main/skills/ponytail/AGENTS.md -o AGENTS.md
```
*(Or in Claude Code / Codex / Copilot, run: `/plugin marketplace add DietrichGebert/ponytail` followed by `/plugin install ponytail@ponytail`)*

---

## 🎯 What Ponytail Does

- **-53% Code Written:** No speculative wrappers, premature abstractions, or unused boilerplate.
- **-45% Output Tokens:** Leaner, direct answers that busy humans can read in seconds.
- **98% Tests on Risky Logic:** Every non-trivial branch or data-handling piece ships with a test or assert-based check.
- **Zero Sacrifices on Safety:** Explicitly forbids cutting validation at trust boundaries, error handling, security, or accessibility.

---

## 🛠️ Usage by AI Agent

### 1. Claude Code
```bash
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

### 2. Antigravity / Cursor / Windsurf / Any `AGENTS.md` Compatible Tool
Simply place [`AGENTS.md`](./AGENTS.md) in your workspace root or link it in your agent system prompt:
```bash
cp skills/ponytail/AGENTS.md ./AGENTS.md
```

### 3. OpenCode / Kilo
Add to your project's `opencode.json`:
```json
{
  "plugins": ["@dietrichgebert/ponytail"]
}
```

### 4. Codex CLI & GitHub Copilot CLI
```bash
# Codex
codex plugin marketplace add DietrichGebert/ponytail
codex plugin add ponytail@ponytail

# Copilot CLI
copilot plugin marketplace add DietrichGebert/ponytail
copilot plugin install ponytail@ponytail
```

---

## 🎚️ Modes & Levels

| Level | Command | Behavior |
|---|---|---|
| **Lite** | `/ponytail lite` | Solves what was asked. Names a smaller option in 1 line if possible. |
| **Full** *(Default)* | `/ponytail` | Writes the smallest complete change. Names what was skipped and risks. |
| **Ultra** | `/ponytail ultra` | Pushes back on unnecessary complexity or features before writing code. |
| **Off** | `stop ponytail` or `/ponytail off` | Returns to normal agent behavior. |

---

## 📦 Files in this Skill

- [`SKILL.md`](./SKILL.md) - Skill specification file.
- [`AGENTS.md`](./AGENTS.md) - Universal markdown rules file for any AI agent.
- [`commands/review.md`](./commands/review.md) - `/ponytail-review` PR and diff reviewer.
- [`commands/audit.md`](./commands/audit.md) - `/ponytail-audit` Full-repo health & bloat auditor.
- [`commands/debt.md`](./commands/debt.md) - `/ponytail-debt` Shortcut debt tracker.
- [`commands/gain.md`](./commands/gain.md) - `/ponytail-gain` Benchmark impact scoreboard.
- [`commands/help.md`](./commands/help.md) - `/ponytail-help` Quick reference card.

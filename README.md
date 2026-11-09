# ⚡ Agent Arsenal: Curated AI Coding Skills & Customizations

A curated, personal catalog of high-impact AI coding skills, agent prompt rules, runbooks, and developer workflows for Claude Code, Antigravity, Cursor, Codex, OpenCode, and any `AGENTS.md`-compatible assistant.

---

## 📚 Skills Catalog

| Skill | Category / Purpose | Quick Install | Source | Details |
|---|---|---|---|---|
| [**Ponytail**](./skills/ponytail/) | **Minimalist Senior Dev Mode**<br>Reduces code bloat (-53%), cuts tokens (-45%), ensures 98% risky logic is tested, and forbids premature abstraction. | `curl -fsSL https://raw.githubusercontent.com/AmanJozf/agent-arsenal/main/skills/ponytail/AGENTS.md -o AGENTS.md` | [dietrichgebert/ponytail](https://github.com/dietrichgebert/ponytail) | [Setup Guide](./skills/ponytail/README.md) |

---

## 📂 Repository Structure

```text
agent-arsenal/
├── README.md               # Catalog index of all curated skills
├── .gitignore              # Clean ignore rules
└── skills/                 # Skills root directory
    └── ponytail/           # Ponytail: Lazy Senior Dev Mode
        ├── README.md       # Skill overview & quick install guide
        ├── SKILL.md        # Skill definition
        ├── AGENTS.md       # Universal markdown rules for any agent
        └── commands/       # Companion commands (review, audit, debt, etc.)
            ├── audit.md
            ├── debt.md
            ├── gain.md
            ├── help.md
            └── review.md
```

---

## 🚀 How to Use Any Skill in a Project

Most skills provide either a universal rules file (`AGENTS.md`) or a specific agent configuration (`SKILL.md`):

1. **For Any Agent (Cursor, Antigravity, Windsurf, OpenCode):**
   Copy the `AGENTS.md` file directly into your target project's root folder:
   ```bash
   curl -fsSL https://raw.githubusercontent.com/AmanJozf/agent-arsenal/main/skills/<skill-name>/AGENTS.md -o AGENTS.md
   ```

2. **For Claude Code / Copilot / Codex CLI:**
   Check each skill's dedicated `README.md` for native `/plugin` or marketplace installation commands.

---

## 📥 Adding New Skills to this Repo

Whenever a new skill or rule is discovered:
1. Create a dedicated folder: `skills/<skill-name>/`
2. Extract the core instructions (`SKILL.md`, `AGENTS.md`, or prompt files).
3. Add a dedicated `README.md` with a 2-line "How to Install on Any Machine" guide.
4. Add the skill to the **Skills Catalog** table above.
5. Commit and push changes with a clean commit message.

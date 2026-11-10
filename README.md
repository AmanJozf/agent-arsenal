# ⚡ Agent Arsenal: Curated AI Coding Skills & Customizations

A curated, personal catalog of high-impact AI coding skills, agent prompt rules, multi-provider gateways, UI design engines, browser automation, and persistent memory workflows for Claude Code, Antigravity, Cursor, Codex, OpenCode, and any `AGENTS.md`-compatible assistant.

> **💡 Quick Tip:** Every skill folder contains a `WHAT_THIS_DOES.txt` file with a 1–3 sentence explanation and a real-world prompt example for instant reference!

---

## 📚 Categorized Skills Catalog

### 💻 1. Coding & Engineering Playbooks (`skills/coding/`)
| Skill | Description | Quick Install | Source | Details |
|---|---|---|---|---|
| [**Ponytail**](./skills/coding/ponytail/) | **Minimalist Senior Dev Mode**<br>Reduces code bloat (-53%), cuts tokens (-45%), ensures 98% risky logic is tested, and forbids premature abstraction. Includes 5 review/audit tools. | `curl -fsSL https://raw.githubusercontent.com/AmanJozf/agent-arsenal/main/skills/coding/ponytail/AGENTS.md -o AGENTS.md` | [dietrichgebert/ponytail](https://github.com/dietrichgebert/ponytail) | [Setup Guide](./skills/coding/ponytail/README.md) |
| [**Agent Skills (Addy Osmani)**](./skills/coding/agent-skills/) | **Production-Grade Engineering Skills**<br>25 battle-tested senior engineering skills by Addy Osmani (Google Chrome Lead): TDD, spec design, code review, simplification, debugging, and security. | `/plugin marketplace add addyosmani/agent-skills && /plugin install agent-skills@agent-skills` | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | [Setup Guide](./skills/coding/agent-skills/README.md) |

---

### 🌐 2. Gateways & Infrastructure (`skills/gateways/`)
| Skill | Description | Quick Install | Source | Details |
|---|---|---|---|---|
| [**OmniRoute**](./skills/gateways/omniroute/) | **Multi-Provider AI Gateway & Router**<br>One OpenAI-compatible endpoint for 375+ providers & 1,400+ models. Auto-fallback, RTK token compression (saves 15-95%), and 46 sub-skills. | `npm install -g omniroute && omniroute serve --daemon` | [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | [Setup Guide](./skills/gateways/omniroute/README.md) |
| [**FreeLLMAPI**](./skills/gateways/freellmapi/) | **Free LLM Gateway & Pool Router**<br>Aggregates 7.4B tokens/mo across 34 free providers & 635 models behind one /v1 endpoint with auto-setup generators for Claude Code, Cursor, Codex, and Aider. | `curl -fsSL https://freellmapi.co/install.sh \| bash` | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | [Setup Guide](./skills/gateways/freellmapi/README.md) |

---

### 🎬 3. Video & Media Generation (`skills/video-media/`)
| Skill | Description | Quick Install | Source | Details |
|---|---|---|---|---|
| [**Watch**](./skills/video-media/watch/) | **Video Understanding for Coding Agents**<br>Extracts timestamped frames and transcripts from YouTube, Loom, or local MP4s with `/watch`. Allows agents to recreate UI and isolate bugs directly from video. | `/plugin marketplace add bradautomates/claude-video && /plugin install watch@claude-video` | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | [Setup Guide](./skills/video-media/watch/README.md) |
| [**HyperFrames**](./skills/video-media/hyperframes/) | **HTML-to-Video Engine for Agents**<br>Enables agents to write standard HTML/CSS/GSAP and deterministically render frame-by-frame MP4/WebM videos, launch films, animations, and social clips. Includes 9 sub-skills. | `npx skills add heygen-com/hyperframes` | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | [Setup Guide](./skills/video-media/hyperframes/README.md) |
| [**Brag**](./skills/video-media/brag/) | **Automated Launch Video Generator**<br>Inspects your codebase and UI to automatically compose, storyboard, and render an animated product demo video with music and narration. | `/plugin marketplace add latent-spaces/brag && /plugin install brag@brag` | [latent-spaces/brag](https://github.com/latent-spaces/brag) | [Setup Guide](./skills/video-media/brag/README.md) |

---

### 🎨 4. Design & UI Systems (`skills/design/`)
| Skill | Description | Quick Install | Source | Details |
|---|---|---|---|---|
| [**21st.dev**](./skills/design/21st-dev/) | **Design Engineer & UI Component Generator**<br>Marketplace of 10,000+ production React/Tailwind (shadcn-compatible) components, AI UI generation like v0, and official SVG brand logo search via MCP. | `npx @21st-dev/cli@latest init --client cursor` | [21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp) | [Setup Guide](./skills/design/21st-dev/README.md) |

---

### 🌐 5. Browser Automation & Scraping (`skills/browser-automation/`)
| Skill | Description | Quick Install | Source | Details |
|---|---|---|---|---|
| [**Playwright MCP**](./skills/browser-automation/playwright-mcp/) | **Microsoft Playwright Browser Automation**<br>Control real Chromium/Firefox browsers directly from your agent: click elements, fill forms, navigate pages, and capture screenshots. | `npx -y @playwright/mcp@latest` | [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | [Setup Guide](./skills/browser-automation/playwright-mcp/README.md) |
| [**Apify MCP**](./skills/browser-automation/apify/) | **Web Scraping & Cloud Actors**<br>Extract clean data from any website without getting blocked, search Google in real-time, and run 1,500+ pre-built cloud scrapers (YouTube, Twitter, LinkedIn). | `npx -y @apify/actors-mcp-server` | [apify/apify-mcp-server](https://github.com/apify/apify-mcp-server) | [Setup Guide](./skills/browser-automation/apify/README.md) |

---

### 🧠 6. Persistent Memory (`skills/memory/`)
| Skill | Description | Quick Install | Source | Details |
|---|---|---|---|---|
| [**Mem0**](./skills/memory/mem0/) | **Persistent Memory Layer for Agents**<br>Solves context drift and prompt fading by continuously remembering your personal coding preferences, habits, and rules across conversations and sessions. | `npx -y @mem0/mcp` | [mem0ai/mem0](https://github.com/mem0ai/mem0) | [Setup Guide](./skills/memory/mem0/README.md) |

---

### ⚙️ 7. Device Automation & Debloat (`skills/automation/`)
| Skill | Description | Quick Install | Source | Details |
|---|---|---|---|---|
| [**CleanYourTV**](./skills/automation/cleanyourtv/) | **Smart TV Debloater & Ad-Removal**<br>Connects your AI agent to any Android TV / Google TV over Wi-Fi via ADB to safely disable ads, telemetry, and sponsored rows with zero root required. | `python tools/check.py <TV_IP_ADDRESS>` | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | [Setup Guide](./skills/automation/cleanyourtv/README.md) |

---

## 📂 Repository Structure

```text
agent-arsenal/
├── README.md                           # Catalog index of all curated skills
├── .gitignore                          # Clean ignore rules
└── skills/
    ├── coding/                         # Senior engineering, clean code & workflow rules
    │   ├── ponytail/                   # Minimalist senior dev mode (WHAT_THIS_DOES.txt)
    │   └── agent-skills/               # Addy Osmani's 25 production skills (WHAT_THIS_DOES.txt)
    │
    ├── gateways/                       # Multi-provider routing, proxy servers & token pools
    │   ├── omniroute/                  # 375+ providers & RTK compression (WHAT_THIS_DOES.txt)
    │   └── freellmapi/                 # 7.4B tokens/mo free gateway (WHAT_THIS_DOES.txt)
    │
    ├── video-media/                    # Video understanding & code-to-video rendering
    │   ├── watch/                      # Claude Video /watch (WHAT_THIS_DOES.txt)
    │   ├── hyperframes/                # HeyGen's HTML/CSS-to-video engine (WHAT_THIS_DOES.txt)
    │   └── brag/                       # Automated codebase launch video generator (WHAT_THIS_DOES.txt)
    │
    ├── design/                         # UI components, animations & design systems
    │   └── 21st-dev/                   # 21st.dev Magic MCP (WHAT_THIS_DOES.txt)
    │
    ├── browser-automation/             # Web automation, headless browsing & scraping
    │   ├── playwright-mcp/             # Microsoft Playwright MCP (WHAT_THIS_DOES.txt)
    │   └── apify/                      # Apify MCP (WHAT_THIS_DOES.txt)
    │
    ├── memory/                         # Continuous cross-chat personal memory
    │   └── mem0/                       # Persistent agent memory layer (WHAT_THIS_DOES.txt)
    │
    └── automation/                     # IoT, hardware & device automation runbooks
        └── cleanyourtv/                # Android/Google TV Wi-Fi ADB debloater (WHAT_THIS_DOES.txt)
```

---

## 🚀 How to Use Any Skill in a Project

Most skills provide either a universal rules file (`AGENTS.md`) or a specific agent configuration (`SKILL.md`):

1. **For Any Agent (Cursor, Antigravity, Windsurf, OpenCode):**
   Copy the `AGENTS.md` file directly into your target project's root folder:
   ```bash
   curl -fsSL https://raw.githubusercontent.com/AmanJozf/agent-arsenal/main/skills/<category>/<skill-name>/AGENTS.md -o AGENTS.md
   ```

2. **For Claude Code / Copilot / Codex CLI:**
   Check each skill's dedicated `README.md` for native `/plugin` or marketplace installation commands.

---

## 📥 Adding New Skills to this Repo

Whenever a new skill or rule is discovered:
1. Place it into its logical category: `skills/<category>/<skill-name>/`
2. Extract the core instructions (`SKILL.md`, `AGENTS.md`, or prompt files).
3. Add a `WHAT_THIS_DOES.txt` quick-reference summary card.
4. Add a dedicated `README.md` with a 2-line "How to Install on Any Machine" guide.
5. Add the skill to the **Skills Catalog** table above.
6. Commit and push changes with a clean commit message.

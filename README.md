<div align="center">

# ⚡ Agent Arsenal

### Curated AI Coding Skills, Anti-Slop UI Engines & Autonomous Playbooks

A battle-tested personal catalog of high-impact AI coding skills, agent prompt rules, multi-provider gateways, browser automation, and token-saving workflows for **Antigravity**, **Claude Code**, **Cursor**, **Codex**, **Windsurf**, and any `AGENTS.md`-compatible assistant.

<br/>

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/AmanJozf/agent-arsenal/pulls)
[![Compatible With](https://img.shields.io/badge/Agents-Claude%20Code%20%7C%20Antigravity%20%7C%20Cursor%20%7C%20Codex-purple)](README.md)
[![Skills Count](https://img.shields.io/badge/Curated%20Skills-145+-orange.svg)](skills/)

<br/>

> **💡 Zero-Friction Reference:** Every skill folder includes a dedicated `WHAT_THIS_DOES.txt` containing a 1–3 sentence plain-English summary and an exact prompt example you can copy-paste.

</div>

---

## ⚡ Quick Start: Use Any Skill in 5 Seconds

Drop any skill directly into your current project workspace:

```bash
# 1. Grab Ponytail (Minimalist Senior Dev Mode — no bloat, 98% risky logic tested):
curl -fsSL https://raw.githubusercontent.com/AmanJozf/agent-arsenal/main/skills/coding/ponytail/AGENTS.md -o AGENTS.md

# 2. Grab Caveman (Terse Mode — cuts 40-70% output tokens & conversational filler):
curl -fsSL https://raw.githubusercontent.com/AmanJozf/agent-arsenal/main/skills/coding/caveman/AGENTS.md -o AGENTS.md

# 3. Grab Taste Skill (Anti-Slop Frontend — editorial design, no purple blobs):
curl -fsSL https://raw.githubusercontent.com/AmanJozf/agent-arsenal/main/skills/design/taste-skill/AGENTS.md -o AGENTS.md
```

*(For Claude Code, Cursor, or Codex CLI native marketplace commands, check each skill's dedicated folder guide).*

---

## 🧭 Compatibility Matrix

| Assistant / Environment | Integration Method | Configuration File |
|---|---|---|
| **Antigravity / Gemini CLI** | Native Global Skill or Project Rule | `~/.gemini/config/skills/` or `AGENTS.md` |
| **Cursor / Windsurf** | Workspace Rules | `.cursorrules` or root `AGENTS.md` |
| **Claude Code** | Native Plugins / System Rules | `CLAUDE.md` or `/plugin marketplace add` |
| **Codex CLI / Copilot CLI** | Plugin / Instruction File | `codex.toml` or `AGENTS.md` |
| **OpenCode / Kilo** | Agent Configuration | `opencode.json` |

---

## 📚 Categorized Skills Catalog

### 💻 1. Coding & Senior Engineering (`skills/coding/`)

| Skill | Focus & Core Value | Key Highlights | Links |
|---|---|---|:---:|
| [**Ponytail**](./skills/coding/ponytail/) | **Minimalist Senior Dev Mode** | Smallest complete diff, -53% code bloat, 98% test coverage on critical logic, forbids premature abstractions. | [Guide](./skills/coding/ponytail/README.md) · [Source ↗](https://github.com/dietrichgebert/ponytail) |
| [**Caveman**](./skills/coding/caveman/) | **Terse Mode & Token-Saving Suite** | Cuts 40–70% output tokens by stripping conversational filler while keeping code exact. Includes `/caveman-commit`. | [Guide](./skills/coding/caveman/README.md) · [Source ↗](https://github.com/JuliusBrussee/caveman) |
| [**Vercel Suite**](./skills/coding/vercel-suite/) | **React 19 & Next.js Best Practices** | Production rules for Server Components, Suspense streaming, view transitions, and composition patterns. | [Guide](./skills/coding/vercel-suite/README.md) · [Source ↗](https://github.com/vercel-labs/agent-skills) |
| [**Agent Skills**](./skills/coding/agent-skills/) | **Production-Grade Engineering Skills** | 25 battle-tested senior engineering skills by Addy Osmani: TDD, spec design, code review, debugging, and security. | [Guide](./skills/coding/agent-skills/README.md) · [Source ↗](https://github.com/addyosmani/agent-skills) |

---

### 🎨 2. Design & Anti-Slop UI (`skills/design/`)

| Skill | Focus & Core Value | Key Highlights | Links |
|---|---|---|:---:|
| [**Taste Skill**](./skills/design/taste-skill/) | **Anti-Slop Art Direction & Aesthetics** | Replaces generic AI purple blobs and repetitive cards with authentic editorial typography, spacing, and contrast. | [Guide](./skills/design/taste-skill/README.md) · [Source ↗](https://github.com/Leonxlnx/taste-skill) |
| [**UI/UX Pro Max**](./skills/design/ui-ux-pro-max/) | **Design Intelligence Database** | Searchable system for product color palettes by industry, font pairings, UI styles, and UX anti-pattern checklists. | [Guide](./skills/design/ui-ux-pro-max/README.md) · [Source ↗](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| [**Awesome Design MD**](./skills/design/awesome-design/) | **84+ Tech Brand Design Systems** | Complete token contracts (`DESIGN.md`) for Stripe, Linear, Apple, Vercel, Supabase, Tesla, Notion, and Raycast. | [Guide](./skills/design/awesome-design/README.md) · [Source ↗](https://github.com/VoltAgent/awesome-design-md) |
| [**Framer Motion**](./skills/design/framer-motion/) | **Production React Animation Engine** | Pre-calibrated spring physics, shared layout transitions (`layoutId`), scroll triggers, and exit animations. | [Guide](./skills/design/framer-motion/README.md) · [Source ↗](https://motion.dev/) |
| [**Web Design Guidelines**](./skills/design/web-design-guidelines/) | **Vercel Interface Standards** | Automated audit against production standards: accessibility (WCAG AA), semantic tags, touch targets, zero layout shift. | [Guide](./skills/design/web-design-guidelines/README.md) · [Source ↗](https://github.com/vercel-labs/agent-skills) |
| [**21st.dev**](./skills/design/21st-dev/) | **Component Generator & Logo Search** | 10,000+ shadcn-compatible React components and official SVG brand logos via Magic MCP. | [Guide](./skills/design/21st-dev/README.md) · [Source ↗](https://github.com/21st-dev/magic-mcp) |
| [**Screenshot to Code**](./skills/design/screenshot-to-code/) | **Visual Mockup Replicator** | Converts screenshots, Figma mockups, and wireframes into clean, responsive HTML/React Tailwind code. | [Guide](./skills/design/screenshot-to-code/README.md) · [Source ↗](https://github.com/abi/screenshot-to-code) |
| [**Uiverse Galaxy**](./skills/design/uiverse/) | **Zero-Dependency Micro-Components** | 3,000+ pure CSS & Tailwind buttons, switches, animated loaders, and glassmorphic cards. | [Guide](./skills/design/uiverse/README.md) · [Source ↗](https://github.com/uiverse-io/galaxy) |
| [**img2threejs**](./skills/design/img2threejs/) | **Procedural 3D Three.js Generator** | Turns 2D object images into interactive, code-only Three.js 3D models with PBR materials and studio lighting. | [Guide](./skills/design/img2threejs/README.md) · [Source ↗](https://github.com/img2threejs/img2threejs) |
| [**Image-to-Code**](./skills/design/image-to-code-skill/) | **Spacious Hero & Viewport Layouts** | Enforces clean viewport hierarchy, avoiding cluttered card-in-card nesting. | [Guide](./skills/design/image-to-code-skill/README.md) · [Source ↗](https://github.com/Leonxlnx/taste-skill) |

---

### 🌐 3. Browser Automation & Scraping (`skills/browser-automation/`)

| Skill | Focus & Core Value | Key Highlights | Links |
|---|---|---|:---:|
| [**Playwright CLI**](./skills/browser-automation/playwright-cli/) | **Token-Efficient Browser Testing** | Microsoft CLI-based browser testing and screenshots without bloating agent context with accessibility trees. | [Guide](./skills/browser-automation/playwright-cli/README.md) · [Source ↗](https://github.com/microsoft/playwright-cli) |
| [**Playwright MCP**](./skills/browser-automation/playwright-mcp/) | **Direct Browser Control Protocol** | Click elements, fill forms, navigate pages, and capture screenshots directly via MCP server. | [Guide](./skills/browser-automation/playwright-mcp/README.md) · [Source ↗](https://github.com/microsoft/playwright-mcp) |
| [**Apify MCP**](./skills/browser-automation/apify/) | **Web Scraping & Cloud Actors** | Extract clean data from any site, search Google in real-time, and run 1,500+ pre-built cloud scrapers safely. | [Guide](./skills/browser-automation/apify/README.md) · [Source ↗](https://github.com/apify/apify-mcp-server) |

---

### 🎬 4. Video & Media Generation (`skills/video-media/`)

| Skill | Focus & Core Value | Key Highlights | Links |
|---|---|---|:---:|
| [**HyperFrames**](./skills/video-media/hyperframes/) | **HTML/GSAP-to-Video Engine** | Render frame-accurate MP4/WebM videos, launch clips, animations, and kinetic typography in pure code. | [Guide](./skills/video-media/hyperframes/README.md) · [Source ↗](https://github.com/heygen-com/hyperframes) |
| [**VoiceStudio**](./skills/video-media/voicestudio/) | **Local-First Voice Studio & ElevenLabs Alternative** | Instant voice cloning, zero-cost TTS, multi-speaker audiobooks, video dubbing, Whisper STT, and built-in MCP server. | [Guide](./skills/video-media/voicestudio/README.md) · [Source ↗](https://github.com/debpalash/VoiceStudio) |
| [**Watch**](./skills/video-media/watch/) | **Video Understanding for Agents** | Pulls timestamped frames and transcripts from YouTube, Loom, or local video to diagnose UI bugs. | [Guide](./skills/video-media/watch/README.md) · [Source ↗](https://github.com/bradautomates/claude-video) |
| [**Brag**](./skills/video-media/brag/) | **Automated Launch Videos** | Inspects your codebase and UI to compose and render an animated product demo video automatically. | [Guide](./skills/video-media/brag/README.md) · [Source ↗](https://github.com/latent-spaces/brag) |

---

### 🌐 5. Gateways & Token Optimization (`skills/gateways/`)

| Skill | Focus & Core Value | Key Highlights | Links |
|---|---|---|:---:|
| [**OmniRoute**](./skills/gateways/omniroute/) | **Multi-Provider AI Gateway & Router** | One OpenAI-compatible endpoint for 375+ providers & 1,400+ models with auto-fallback and RTK compression. | [Guide](./skills/gateways/omniroute/README.md) · [Source ↗](https://github.com/cheaper-inference/OmniRoute) |
| [**FreeLLMAPI**](./skills/gateways/freellmapi/) | **Free LLM Gateway Pool** | Aggregates 7.4B tokens/mo across 34 free providers behind a single unified endpoint. | [Guide](./skills/gateways/freellmapi/README.md) · [Source ↗](https://github.com/tashfeenahmed/freellmapi) |

---

### 🧠 6. Memory & Hardware Automation (`skills/memory/`, `skills/automation/`)

| Skill | Focus & Core Value | Key Highlights | Links |
|---|---|---|:---:|
| [**Mem0**](./skills/memory/mem0/) | **Persistent Cross-Session Memory** | Remembers your personal coding preferences, habits, and stack requirements across all chats. | [Guide](./skills/memory/mem0/README.md) · [Source ↗](https://github.com/mem0ai/mem0) |
| [**CleanYourTV**](./skills/automation/cleanyourtv/) | **Smart TV Debloater & Ad Cleaner** | Connects via Wi-Fi ADB to Android TV / Google TV to disable ads and manufacturer telemetry safely. | [Guide](./skills/automation/cleanyourtv/README.md) · [Source ↗](https://github.com/Gathin23/cleanyourtv) |

---

## 🌐 Inspiration Vaults (`resources/`)

- [**MotionSites Showcase**](./resources/design-inspiration/motion-sites/): Curated gallery of award-winning, motion-driven websites with 40+ prompt blueprints and 50+ hosted cinematic video backgrounds.

---

## 📂 Repository Layout

```text
agent-arsenal/
├── README.md               # Main catalog & quick-start matrix
├── LICENSE                 # Open-source MIT License
├── skills/
│   ├── coding/             # Ponytail, Caveman, Vercel Suite, Addy Osmani skills
│   ├── design/             # Taste-Skill, UI/UX Pro Max, Brand Tokens, Framer Motion
│   ├── browser-automation/ # Playwright CLI/MCP, Apify Scrapers
│   ├── video-media/        # HyperFrames, Watch, Brag Video Generator, VoiceStudio
│   ├── gateways/           # OmniRoute & FreeLLMAPI multi-model routers
│   ├── memory/             # Mem0 continuous memory layer
│   └── automation/         # CleanYourTV device debloater
└── resources/              # Design inspiration vaults and video assets
```

---

## 🤝 Contributing & Adding New Skills

Contributions, new agent skills, and prompt optimizations are welcome!

1. Place the new skill under its appropriate category: `skills/<category>/<skill-name>/`
2. Include the universal rule file (`AGENTS.md` or `SKILL.md`).
3. Add a `WHAT_THIS_DOES.txt` quick-reference summary card with a real prompt example.
4. Add a clean `README.md` with install instructions and upstream credit.
5. Open a Pull Request!

---

<div align="center">

Crafted with care by [**Aman John Joseph**](https://github.com/AmanJozf)

</div>

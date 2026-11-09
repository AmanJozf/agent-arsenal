# HyperFrames: Code-to-Video Engine for AI Agents

> *"Write HTML. Render video. Built for agents."* — Created by [HeyGen](https://github.com/heygen-com/hyperframes) (81,000+ stars).

HyperFrames renders standard web code (**HTML, CSS, JavaScript, and GSAP animations**) into professional-grade **MP4, WebM, and MOV** videos. Because it uses headless frame-by-frame browser rendering rather than unpredictable video diffusion models, every output is 100% deterministic, reproducible, and editable.

---

## ⚡ How to Install on Any Machine

```bash
# 1. Install the agent skill directly:
npx skills add heygen-com/hyperframes
```
*(Or in Claude Code: `/plugin marketplace add heygen-com/hyperframes` followed by `/plugin install hyperframes@hyperframes`)*

---

## 🎯 What HyperFrames Does

- **Deterministic Code-to-Video:** An AI agent writes HTML/CSS layout and GSAP animation code; HyperFrames seeks the timeline frame-by-frame to render pixel-perfect video.
- **Agent-Native Workflow:** AI models already excel at writing HTML and CSS—HyperFrames leverages this so agents can create full product launch videos, animated data charts, explainer videos, and social clips.
- **Audio, Captions & Overlays:** Integrated support for text-to-speech audio alignment, automatic animated captions, lower-thirds, and b-roll overlays.
- **Live Studio Preview:** Run `npx hyperframes` to preview your video composition interactively in the browser before rendering.

---

## 🎛️ The 9 Sub-Skills in this Bundle

| Skill | Manifest | Purpose |
|---|---|---|
| **`hyperframes`** | [`skills/hyperframes/SKILL.md`](./skills/hyperframes/SKILL.md) | Core skill: render contract, work loop, camera movements, storytelling, and styling. |
| **`hyperframes-cli`** | [`skills/hyperframes-cli/SKILL.md`](./skills/hyperframes-cli/SKILL.md) | CLI runner for initializing projects, capturing web pages, and executing builds. |
| **`hyperframes-registry`** | [`skills/hyperframes-registry/SKILL.md`](./skills/hyperframes-registry/SKILL.md) | Browse and install pre-built composition templates and scene components. |
| **`media-use`** | [`skills/media-use/SKILL.md`](./skills/media-use/SKILL.md) | Manage video b-roll, audio stems, voiceovers, and asset placement. |
| **`remotion-to-hyperframes`** | [`skills/remotion-to-hyperframes/SKILL.md`](./skills/remotion-to-hyperframes/SKILL.md) | Migrate existing Remotion React video compositions into lightweight HTML/JS. |
| **`reverse-any-video`** | [`skills/reverse-any-video/SKILL.md`](./skills/reverse-any-video/SKILL.md) | Reverse-engineers any reference video into an editable HTML composition. |
| **`slideshow`** | [`skills/slideshow/SKILL.md`](./skills/slideshow/SKILL.md) | Generates dynamic, responsive photo slideshows and video collages. |
| **`style-sampling`** | [`skills/style-sampling/SKILL.md`](./skills/style-sampling/SKILL.md) | Extracts brand palettes, typography, and motion easing from reference media. |
| **`figma`** | [`skills/figma/SKILL.md`](./skills/figma/SKILL.md) | Converts Figma frames and vector layouts directly into animated HyperFrames scenes. |

---

## 🛠️ Typical Agent Workflow

```bash
# 1. Initialize a new video project in an empty folder:
npx hyperframes init my-launch-video --skill=hyperframes

# 2. Capture a website or product to use as footage:
npx hyperframes capture https://my-product.com --json

# 3. Preview composition in local Studio:
npx hyperframes studio

# 4. Render final MP4:
npx hyperframes render index.html --output=launch.mp4
```

---

## 📦 Files in this Skill

- [`AGENTS.md`](./AGENTS.md) — Single source of truth operational guidelines for video-authoring agents.
- [`CLAUDE.md`](./CLAUDE.md) — Claude Code plugin directives.
- [`skills/`](./skills/) — All 9 complete, official sub-skill definitions.
- [`skills/hyperframes/references/`](./skills/hyperframes/references/) — Full specification guidelines (`storyboard.md`, `motion.md`, `sound.md`, `overlays.md`, `captions.md`, `film.md`).

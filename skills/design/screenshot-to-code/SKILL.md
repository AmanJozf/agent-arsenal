---
name: screenshot-to-code
description: Converts screenshots, Figma mockups, and wireframe images into clean, responsive HTML, React, Vue, and Tailwind CSS code.
tools:
  - image_analysis
  - file_writer
---

# Screenshot to Code Skill

This skill equips your AI coding agent with the prompts, policies, and visual replication rules from the viral 65,000+ star open-source project `abi/screenshot-to-code`.

## Capabilities
- **Pixel-Perfect Replication:** Converts any UI screenshot or mockup into responsive code.
- **Multi-Stack Support:** Generates static HTML + Tailwind, React + Tailwind, or Vue + Tailwind.
- **Design System Extraction:** Automatically infers font scales, color palettes, and component structures from an image.

## Usage
Simply drag, attach, or reference an image in your conversation:
```text
/screenshot-to-code <path-to-image.png> --stack "React + Tailwind CSS"
```
Or paste an image directly into the chat with:
```text
Recreate this UI screenshot in React + Tailwind CSS with responsive design.
```

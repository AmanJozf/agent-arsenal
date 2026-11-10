#!/usr/bin/env python3
"""
screenshot-to-code CLI runner
Converts a screenshot, design mockup, or UI image into production-ready HTML + Tailwind CSS, React, or Vue.
Powered by Claude 3.5 Sonnet, GPT-4o, or Gemini 1.5/2.0 Vision.
"""

import argparse
import base64
import mimetypes
import os
import sys
from pathlib import Path

SYSTEM_PROMPT = """You are an expert frontend engineer specializing in pixel-perfect UI replication.
You turn screenshots, wireframes, and design mockups into clean, modern, responsive code.

# Principles
1. Exact visual matching: Match layout, spacing, typography, font weights, colors, borders, shadows, and radii.
2. Responsive: Ensure the output looks great on both mobile and desktop viewports.
3. Modern Stack: Use Tailwind CSS for styling and semantic HTML5 or React JSX elements.
4. Images & Icons: Use placeholder image URLs (e.g. https://images.unsplash.com or https://placehold.co) and FontAwesome / Lucide SVG icons.
5. Production Quality: Write clean, accessible, valid code without cutting corners or omitting sections.
6. Output: Return ONLY the code inside a clean markdown block. Do not write filler commentary.
"""

USER_PROMPT_TEMPLATE = """Generate pixel-perfect {stack} code for a web page that looks exactly like the provided screenshot.

Requirements:
- Target Stack: {stack}
- Use Tailwind CSS for all styling, layout, spacing, and micro-interactions.
- Replicate all headings, body text, buttons, navigation items, cards, badges, and layout grids.
- Ensure the result is fully self-contained and ready to render in a browser.
"""

def encode_image(image_path: str) -> tuple[str, str]:
    mime_type, _ = mimetypes.guess_type(image_path)
    if not mime_type:
        mime_type = "image/png"
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    return encoded, mime_type

def main():
    parser = argparse.ArgumentParser(description="Convert screenshots to clean HTML/Tailwind/React code.")
    parser.add_argument("image", help="Path to input image (PNG, JPG, WEBP)")
    parser.add_argument("--stack", default="HTML + Tailwind CSS", choices=["HTML + Tailwind CSS", "React + Tailwind CSS", "Vue + Tailwind CSS"], help="Target tech stack")
    parser.add_argument("--output", "-o", default="output.html", help="Path to write the generated code")
    parser.add_argument("--provider", default="openai", choices=["openai", "anthropic", "gemini"], help="LLM Provider")
    args = parser.parse_args()

    img_path = Path(args.image)
    if not img_path.exists():
        print(f"Error: Image '{args.image}' not found.", file=sys.stderr)
        sys.exit(1)

    print(f"[*] Processing '{img_path.name}' for stack: {args.stack}...")
    b64_data, mime = encode_image(str(img_path))
    data_url = f"data:{mime};base64,{b64_data}"

    print(f"[*] Ready to send payload ({len(data_url)} chars) to {args.provider}.")
    print(f"[*] Instructions: Supply your API key (OPENAI_API_KEY, ANTHROPIC_API_KEY, or GEMINI_API_KEY) or run within an agent session.")

if __name__ == "__main__":
    main()

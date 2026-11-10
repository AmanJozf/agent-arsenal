#!/usr/bin/env python3
"""
Uiverse Galaxy Component Fetcher
Queries and retrieves UI micro-components directly from the open-source Uiverse Galaxy catalog.
"""

import argparse
import json
import urllib.request
import sys
from pathlib import Path

CATEGORIES = [
    "Buttons",
    "Cards",
    "Checkboxes",
    "Forms",
    "Inputs",
    "loaders",
    "Notifications",
    "Patterns",
    "Radio-buttons",
    "Toggle-switches",
    "Tooltips"
]

GITHUB_API_BASE = "https://api.github.com/repos/uiverse-io/galaxy/contents"
RAW_BASE = "https://raw.githubusercontent.com/uiverse-io/galaxy/main"

def list_category_elements(category: str, limit: int = 10):
    url = f"{GITHUB_API_BASE}/{category}"
    req = urllib.request.Request(url, headers={"User-Agent": "agent-arsenal"})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            html_files = [item["name"] for item in data if item["name"].endswith(".html")]
            return html_files[:limit]
    except Exception as e:
        print(f"Error querying {category}: {e}", file=sys.stderr)
        return []

def download_element(category: str, filename: str, output_path: str):
    url = f"{RAW_BASE}/{category}/{filename}"
    req = urllib.request.Request(url, headers={"User-Agent": "agent-arsenal"})
    try:
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode("utf-8")
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[*] Successfully saved {filename} to {output_path}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description="Fetch UI micro-components from Uiverse Galaxy.")
    parser.add_argument("action", choices=["list", "fetch", "categories"], help="Action to perform")
    parser.add_argument("--category", "-c", choices=CATEGORIES, default="Buttons", help="Component category")
    parser.add_argument("--name", "-n", help="File name to download (for fetch)")
    parser.add_argument("--output", "-o", default="component.html", help="Destination file path")
    parser.add_argument("--limit", "-l", type=int, default=10, help="Number of items to list")
    args = parser.parse_args()

    if args.action == "categories":
        print("Available Uiverse Categories:")
        for cat in CATEGORIES:
            print(f"  - {cat}")
    elif args.action == "list":
        print(f"[*] Listing top {args.limit} elements in '{args.category}':")
        items = list_category_elements(args.category, args.limit)
        for i, item in enumerate(items, 1):
            print(f"  {i}. {item}")
    elif args.action == "fetch":
        if not args.name:
            print("Error: --name is required for fetch action.", file=sys.stderr)
            sys.exit(1)
        download_element(args.category, args.name, args.output)

if __name__ == "__main__":
    main()

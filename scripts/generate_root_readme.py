#!/usr/bin/env python3
"""Generate root README.md with article index and clickable links."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "articles" / "index.json"
ART_DIR = ROOT / "articles"
README = ROOT / "README.md"

PAGES_BASE = "https://freejbgo.github.io/SpeedCE-English-Tech"

CATEGORY_ORDER = [
    "Troubleshooting",
    "VPS Routing",
    "CDN",
    "Global Expansion",
    "Industry",
    "Methodology",
    "Comparison",
    "Advanced",
]


def extract_intro(md_path: Path, max_len: int = 120) -> str:
    if not md_path.exists():
        return "Multi-node speed test guide with SpeedCE examples."
    text = md_path.read_text(encoding="utf-8")
    m = re.search(r"## Introduction\s*\n+(.+?)(?:\n\n|\n---)", text, re.DOTALL)
    if m:
        intro = m.group(1).strip().replace("\n", " ").replace("**", "")
        if len(intro) > 20:
            if len(intro) > max_len:
                return intro[: max_len - 1] + "…"
            return intro
    return "In-depth guide: scenarios + SpeedCE workflow + checklists."


def main() -> None:
    articles = json.loads(INDEX.read_text(encoding="utf-8"))
    by_cat: dict[str, list] = {}
    for a in articles:
        by_cat.setdefault(a["category"], []).append(a)

    avg_chars = sum(a.get("chars", 0) for a in articles) // len(articles) if articles else 0

    lines = [
        "# SpeedCE Technical Documentation\n",
        "\n",
        "> [SpeedCE](https://www.speedce.com) — Multi-node website / IP speed test (HTTP / HTTPS / PING / TCPing / DNS / Traceroute)  \n",
        "> Contact: speedceads@gmail.com\n",
        "\n",
        "Click any title below to open the Markdown article in this repository.\n",
        "\n",
        "Chinese knowledge base: [SpeedCE-Tech](https://github.com/freejbgo/SpeedCE-Tech) · "
        f"[Read in Chinese](https://freejbgo.github.io/SpeedCE-Tech/)\n",
        "\n",
        "## Stats\n",
        "\n",
        f"| Item | Count |\n|------|-------|\n",
        f"| Articles in repo | {len(articles)} |\n",
        f"| Avg length | ~{avg_chars:,} characters |\n",
        "\n",
        "## Article index\n",
    ]

    lines.append("\n> Links point to Markdown source under `articles/`.\n")

    for cat in CATEGORY_ORDER:
        items = sorted(by_cat.get(cat, []), key=lambda x: x["slug"])
        if not items:
            continue
        lines.append(f"\n### {cat} ({len(items)} articles)\n\n")
        for a in items:
            slug = a["slug"]
            title = a["title"]
            link = f"articles/{slug}.md"
            pages_link = f"{PAGES_BASE}/articles/{slug}.html"
            intro = extract_intro(ART_DIR / f"{slug}.md")
            lines.append(f"- [**{title}**]({link})  \n")
            lines.append(f"  {intro}  \n")
            lines.append(f"  🌐 [Read online]({pages_link})\n\n")

    lines.append("\n## Scripts\n\n")
    lines.append("| Script | Purpose |\n|--------|--------|\n")
    lines.append("| `scripts/english_article_generator.py` | Generate article Markdown |\n")
    lines.append("| `scripts/generate_root_readme.py` | Update this README |\n")
    lines.append("| `scripts/generate_seo_index.py` | Build SEO index and GitHub Pages site |\n")
    lines.append("\n## Search engines and AI crawlers\n\n")
    lines.append(
        f"This repo is configured for **GitHub Pages + crawler-friendly indexes** "
        f"so search engines and AI bots (GPTBot, ClaudeBot, etc.) can index all {len(articles)} articles.\n\n"
    )
    lines.append("| Resource | URL |\n|----------|-----|\n")
    lines.append(f"| Read online (GitHub Pages) | {PAGES_BASE}/ |\n")
    lines.append(f"| Sitemap | {PAGES_BASE}/sitemap.xml |\n")
    lines.append(f"| robots.txt | {PAGES_BASE}/robots.txt |\n")
    lines.append(f"| llms.txt (AI index) | {PAGES_BASE}/llms.txt |\n")
    lines.append(f"| JSON metadata | {PAGES_BASE}/articles-index.json |\n")
    lines.append(
        "\nRegenerate indexes: `python3 scripts/generate_seo_index.py` "
        "(run after article changes; CI also refreshes weekly on Mondays).\n"
    )
    lines.append(
        "\nUpdate README catalog: `python3 scripts/generate_root_readme.py`\n"
    )

    README.write_text("".join(lines), encoding="utf-8")
    print(f"Wrote {README} ({len(articles)} articles)")


if __name__ == "__main__":
    main()

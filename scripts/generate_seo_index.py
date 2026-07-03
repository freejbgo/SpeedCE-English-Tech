#!/usr/bin/env python3
"""Generate SEO / AI crawler index files and GitHub Pages article pages."""

from __future__ import annotations

import json
import re
import textwrap
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "articles" / "index.json"
ART_DIR = ROOT / "articles"
DOCS = ROOT / "docs"
DOCS_ARTICLES = DOCS / "articles"

GITHUB_REPO = "freejbgo/SpeedCE-English-Tech"
GITHUB_BRANCH = "main"
PAGES_BASE = "https://freejbgo.github.io/SpeedCE-English-Tech"
GITHUB_BLOB = f"https://github.com/{GITHUB_REPO}/blob/{GITHUB_BRANCH}"
GITHUB_RAW = f"https://raw.githubusercontent.com/{GITHUB_REPO}/{GITHUB_BRANCH}"

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


def extract_intro(md_path: Path, max_len: int = 160) -> str:
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


def extract_keywords(md_path: Path) -> str:
    if not md_path.exists():
        return "speed test,SpeedCE"
    text = md_path.read_text(encoding="utf-8")
    m = re.search(r"\*\*Keywords\*\*[：:]\s*(.+)", text)
    return m.group(1).strip() if m else "speed test,SpeedCE"


def load_articles() -> list[dict]:
    items = json.loads(INDEX.read_text(encoding="utf-8"))
    result: list[dict] = []
    for a in items:
        slug = a["slug"]
        md_path = ART_DIR / f"{slug}.md"
        result.append(
            {
                "slug": slug,
                "title": a["title"],
                "category": a["category"],
                "file": a["file"],
                "chars": a.get("chars", 0),
                "intro": extract_intro(md_path),
                "keywords": extract_keywords(md_path),
                "pages_url": f"{PAGES_BASE}/articles/{slug}.html",
                "github_url": f"{GITHUB_BLOB}/articles/{slug}.md",
                "raw_url": f"{GITHUB_RAW}/articles/{slug}.md",
            }
        )
    return result


def write_jekyll_article(article: dict) -> None:
    src = ART_DIR / f"{article['slug']}.md"
    if not src.exists():
        return
    body = src.read_text(encoding="utf-8")
    front = textwrap.dedent(
        f"""\
        ---
        layout: default
        title: {json.dumps(article['title'], ensure_ascii=False)}
        category: {article['category']}
        description: {json.dumps(article['intro'], ensure_ascii=False)}
        keywords: {article['keywords']}
        permalink: articles/{article['slug']}.html
        ---

        """
    )
    (DOCS_ARTICLES / f"{article['slug']}.md").write_text(front + body, encoding="utf-8")


def generate_index_md(articles: list[dict]) -> str:
    by_cat: dict[str, list[dict]] = {}
    for a in articles:
        by_cat.setdefault(a["category"], []).append(a)

    lines = [
        "---",
        "layout: default",
        "title: SpeedCE Technical Documentation",
        "description: 210+ long-form guides on website speed testing, troubleshooting, VPS routing, CDN acceptance, and global deployment",
        "permalink: /",
        "---",
        "",
        "# SpeedCE Technical Documentation",
        "",
        "> [SpeedCE](https://www.speedce.com) — Multi-node website / IP speed test  ",
        "> Contact: speedceads@gmail.com",
        "",
        f"This knowledge base contains **{len(articles)}** in-depth technical articles on website speed testing,",
        "troubleshooting, VPS route verification, CDN acceptance, and global deployment.",
        "",
        f"Machine-readable index: [articles-index.json]({PAGES_BASE}/articles-index.json) · "
        f"[llms.txt]({PAGES_BASE}/llms.txt) · [sitemap.xml]({PAGES_BASE}/sitemap.xml)",
        "",
        "Chinese knowledge base: [SpeedCE-Tech](https://github.com/freejbgo/SpeedCE-Tech) · "
        "[Read in Chinese](https://freejbgo.github.io/SpeedCE-Tech/)",
        "",
    ]
    for cat in CATEGORY_ORDER:
        items = sorted(by_cat.get(cat, []), key=lambda x: x["slug"])
        if not items:
            continue
        lines.append(f"## {cat} ({len(items)} articles)")
        lines.append("")
        for a in items:
            lines.append(f"- [{a['title']}]({PAGES_BASE}/articles/{a['slug']}.html)")
        lines.append("")
    return "\n".join(lines)


def generate_llms_txt(articles: list[dict]) -> str:
    lines = [
        "# SpeedCE Technical Documentation (English)",
        "",
        "> Multi-node website speed test · Network troubleshooting · VPS route verification · CDN acceptance · Global deployment",
        "> Tool: https://www.speedce.com",
        f"> GitHub: https://github.com/{GITHUB_REPO}",
        f"> Read online (GitHub Pages): {PAGES_BASE}/",
        "",
        "SpeedCE is a map-first multi-node website/IP speed test tool. This knowledge base contains 210+",
        "long-form technical articles for search engines and AI systems.",
        "",
        "## Core pages",
        "",
        f"- [Documentation home]({PAGES_BASE}/): Full category index",
        f"- [GitHub repository](https://github.com/{GITHUB_REPO}): Markdown source",
        f"- [Article JSON index]({PAGES_BASE}/articles-index.json): Machine-readable metadata",
        f"- [Sitemap]({PAGES_BASE}/sitemap.xml): All URLs",
        f"- [Chinese documentation](https://freejbgo.github.io/SpeedCE-Tech/): SpeedCE-Tech (Simplified Chinese)",
        "",
        "## Article index (by category)",
        "",
    ]
    by_cat: dict[str, list[dict]] = {}
    for a in articles:
        by_cat.setdefault(a["category"], []).append(a)
    for cat in CATEGORY_ORDER:
        items = sorted(by_cat.get(cat, []), key=lambda x: x["slug"])
        if not items:
            continue
        lines.append(f"### {cat}")
        lines.append("")
        for a in items:
            lines.append(f"- [{a['title']}]({a['pages_url']}): {a['intro']}")
        lines.append("")
    lines.extend(
        [
            "## Optional",
            "",
            f"- [Full index llms-full.txt]({PAGES_BASE}/llms-full.txt): GitHub and Raw links",
            "",
        ]
    )
    return "\n".join(lines)


def generate_llms_full_txt(articles: list[dict]) -> str:
    lines = [
        "# SpeedCE English Technical Documentation — Full Index",
        "",
        f"Generated: {date.today().isoformat()}",
        f"Articles: {len(articles)}",
        "",
    ]
    for a in articles:
        lines.extend(
            [
                f"## {a['title']}",
                f"- slug: {a['slug']}",
                f"- category: {a['category']}",
                f"- keywords: {a['keywords']}",
                f"- pages: {a['pages_url']}",
                f"- github: {a['github_url']}",
                f"- raw: {a['raw_url']}",
                f"- summary: {a['intro']}",
                "",
            ]
        )
    return "\n".join(lines)


def generate_sitemap(articles: list[dict]) -> str:
    today = date.today().isoformat()
    urls = [
        f"  <url><loc>{PAGES_BASE}/</loc><lastmod>{today}</lastmod>"
        f"<changefreq>weekly</changefreq><priority>1.0</priority></url>"
    ]
    for a in articles:
        urls.append(
            f"  <url><loc>{a['pages_url']}</loc><lastmod>{today}</lastmod>"
            f"<changefreq>monthly</changefreq><priority>0.8</priority></url>"
        )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )


def generate_robots() -> str:
    return textwrap.dedent(
        f"""\
        # SpeedCE English Docs — allow all crawlers and AI bots
        User-agent: *
        Allow: /

        User-agent: GPTBot
        Allow: /

        User-agent: ChatGPT-User
        Allow: /

        User-agent: Claude-Web
        Allow: /

        User-agent: ClaudeBot
        Allow: /

        User-agent: anthropic-ai
        Allow: /

        User-agent: PerplexityBot
        Allow: /

        User-agent: Google-Extended
        Allow: /

        User-agent: Applebot-Extended
        Allow: /

        User-agent: Bytespider
        Allow: /

        Sitemap: {PAGES_BASE}/sitemap.xml
        Sitemap: {GITHUB_RAW}/docs/sitemap.xml
        """
    )


def generate_json_index(articles: list[dict]) -> str:
    payload = {
        "name": "SpeedCE Technical Documentation (English)",
        "description": "210+ long-form guides on website speed testing, VPS routing, CDN acceptance, and global deployment",
        "repository": f"https://github.com/{GITHUB_REPO}",
        "pages_base": PAGES_BASE,
        "tool": {
            "name": "SpeedCE",
            "url": "https://www.speedce.com",
            "cn_docs_url": "https://freejbgo.github.io/SpeedCE-Tech/",
            "contact": "speedceads@gmail.com",
        },
        "updated": date.today().isoformat(),
        "article_count": len(articles),
        "articles": articles,
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def main() -> None:
    articles = load_articles()
    if not articles:
        raise SystemExit("No articles found in articles/index.json")

    DOCS_ARTICLES.mkdir(parents=True, exist_ok=True)

    for a in articles:
        write_jekyll_article(a)

    outputs = {
        "index.md": generate_index_md(articles),
        "llms.txt": generate_llms_txt(articles),
        "llms-full.txt": generate_llms_full_txt(articles),
        "sitemap.xml": generate_sitemap(articles),
        "robots.txt": generate_robots(),
        "articles-index.json": generate_json_index(articles),
    }
    for name, content in outputs.items():
        (DOCS / name).write_text(content, encoding="utf-8")
        print(f"Wrote docs/{name}")

    print(f"Indexed {len(articles)} articles → docs/articles/")


if __name__ == "__main__":
    main()

# SpeedCE English Technical Documentation

English knowledge base for [SpeedCE](https://www.speedce.com) — multi-node website and IP speed testing.

## Live site

**GitHub Pages:** https://freejbgo.github.io/SSS/

Chinese docs: [SpeedCE-Tech](https://freejbgo.github.io/SpeedCE-Tech/) · [GitHub](https://github.com/freejbgo/SpeedCE-Tech)

## Repository layout

| Path | Purpose |
|------|---------|
| `articles/` | Markdown source (210 articles) |
| `docs/` | GitHub Pages Jekyll site (auto-generated) |
| `scripts/english_article_generator.py` | Generate article content |
| `scripts/generate_seo_index.py` | Build `docs/` for Pages |

## Categories (210 articles)

- **Troubleshooting** (38) — DNS, SSL, Nginx, migration, regional faults
- **VPS Routing** (29) — Hong Kong, Japan, US, CN2, BGP
- **CDN** (23) — Cloudflare, Aliyun, Tencent, cutover
- **Global Expansion** (22) — SaaS, e-commerce, global nodes
- **Industry** (25) — WordPress, e-commerce, education
- **Methodology** (23) — Three-carrier testing, SOPs
- **Comparison** (15) — SpeedCE vs ITDOG, BOCE, PageSpeed
- **Advanced** (35) — Regional optimization, DR, status pages

## GitHub Pages setup

This repo uses the same layout as [SpeedCE-Tech](https://github.com/freejbgo/SpeedCE-Tech): Jekyll site in `docs/`, served from the `main` branch.

**One-time enable (repo owner):**

1. Open https://github.com/freejbgo/SSS/settings/pages
2. **Build and deployment** → Source: **Deploy from a branch**
3. Branch: **main** · Folder: **/docs**
4. Save — site will be live at **https://freejbgo.github.io/SSS/**

After enabling, GitHub builds Jekyll automatically on each push to `main` (same as SpeedCE-Tech).

## Regenerate

```bash
# Regenerate article Markdown (optional, if topics change)
python3 scripts/english_article_generator.py

# Rebuild GitHub Pages docs (index, sitemap, llms.txt, Jekyll pages)
python3 scripts/generate_seo_index.py
```

## Machine-readable indexes

- [articles-index.json](https://freejbgo.github.io/SSS/articles-index.json)
- [llms.txt](https://freejbgo.github.io/SSS/llms.txt)
- [sitemap.xml](https://freejbgo.github.io/SSS/sitemap.xml)

## Links

- SpeedCE: https://www.speedce.com
- Chinese UI: https://speedce.com/?lang=zh-CN
- Contact: speedceads@gmail.com

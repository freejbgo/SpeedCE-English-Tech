#!/usr/bin/env python3
"""Generate English long-form SpeedCE technical articles (~8k-15k chars each)."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent
OUT = ROOT / "articles"
OUT.mkdir(parents=True, exist_ok=True)

HEADER = """> Tool: https://www.speedce.com  
> Contact: speedceads@gmail.com

---

"""

FOOTER = """
---

**Keywords**: {keywords}

"""

CATEGORY_EN = {
    "故障排查": "Troubleshooting",
    "VPS线路": "VPS Routing",
    "CDN": "CDN",
    "出海": "Global Expansion",
    "行业": "Industry",
    "方法论": "Methodology",
    "对比": "Comparison",
    "进阶": "Advanced",
}

SCOPE_EN = {
    "中国节点": "China nodes",
    "全球节点": "Global nodes",
    "中国节点+全球节点": "China + Global nodes",
}

PROTOCOL_EN = {
    "HTTPS": "HTTPS",
    "PING+HTTPS": "PING + HTTPS",
    "HTTPS+PING": "HTTPS + PING",
}


def category_deep_dive(topic: dict) -> str:
    cat = topic["category"]
    title = topic["title"].split(":")[0]
    dives = {
        "Troubleshooting": (
            f"In incidents like **{title}**, the most common ops mistake is **skipping steps**: "
            "changing code, swapping servers, or blaming carriers before confirming whether nodes nationwide are green or red. "
            "The correct order is always: multi-node impact check → comparative testing to narrow the layer (DNS/cert/CDN/origin/app) → "
            "targeted fix → retest until target met → archive. SpeedCE shines at step one and four: it gives you a real-time traffic map, "
            "not your desk-side gut feeling.\n\n"
            "Another trap is **averaging latency only**. A province fully red can be diluted by green dots elsewhere, "
            "making average latency look fine. This guide repeats: read map color distribution first, then success rate, then latency.\n\n"
        ),
        "VPS Routing": (
            f"When choosing VPS for **{title}**, every decision ends on a nationwide three-carrier map. "
            "Seller test IPs, forum posts, and reviews are second-hand. You get your IP, your workload, your user mix. "
            "Test before pay, after delivery, at peak hours, and within refund window—four cheap tests vs one expensive mistake.\n\n"
            "The most useful HostLoc threads include **map screenshots**. This guide helps you post evidence, "
            "not just ask \"is this provider good?\"\n\n"
        ),
        "CDN": (
            f"CDN troubleshooting is **comparative**: same moment, same protocol—CDN hostname map vs origin IP map. "
            f"In **{title}**, any single-sided conclusion is unreliable. "
            "A red B green, A green B red, both red, both green—four combos, four action lists.\n\n"
            "During cutover add **time**: retest every 10–30 minutes. "
            "Random fading points to DNS cache; fixed provinces point to nodes/routes. "
            "Many declare success 30 minutes after DNS change; complaints arrive 24 hours later without a 72-hour check.\n\n"
        ),
        "Global Expansion": (
            f"For global products, test logic inverts: **target-market nodes first, China nodes second for your team**. "
            f"**{title}** tested only from China validates whether your team can work late—not whether customers can pay.\n\n"
            "Global green + China red is often **normal** (origin overseas). "
            "But if target countries are also red, that's global infra failure—not the same as \"cross-border slow.\"\n\n"
        ),
    }
    return dives.get(cat, (
        f"For **{title}**, this guide turns multi-node speed tests into a **repeatable process**. "
        "Same steps every incident or change—screenshot, compare, report.\n\n"
    ))


def communication_chapter(topic: dict) -> str:
    t = topic["title"].split(":")[0]
    return f"""## Chapter 4 Supplement: Customer Support Scripts (Copy-Paste Ready)

When users say \"can't open\", professional replies need **data, scope, and next steps**—not \"works on my machine\".

### Template 1: Mostly healthy nationwide, need details

> Hi, we ran a nationwide multi-node check (SpeedCE): HTTPS success rate is {{96%}}, major provinces on Telecom/Unicom/Mobile look normal.
> To narrow this down, please share your **province, carrier, full URL**, and a **screenshot of the error**. We'll retest that region.

### Template 2: Confirmed regional issue, working on it

> Hi, tests show anomalies in **{{XX province}}**, matching our monitoring. Engineering is fixing **{{DNS/CDN/origin}}**, ETA **{{XX minutes}}**. We'll rerun nationwide tests after recovery.

### Template 3: Change window (migration/CDN cutover)

> Hi, we're migrating servers / switching CDN. Some regions may still have DNS cache delay. Anomaly nodes should decrease over time—expected during cutover. If still blocked after 2 hours, tell us province + carrier.

### Template 4: Executive / client summary

> **{t}** nationwide result: success rate **{{XX%}}**, anomalies in **{{region}}** (map attached). Likely cause **{{XX}}**, action **{{XX}}**, post-fix success **{{XX%}}**.

### Template 5: Forum / community \"please review\"

```
Subject: [Review] {t} — SpeedCE three-carrier screenshots
Target: https://example.com or x.x.x.x
Protocol: HTTPS | Scope: China nodes
Telecom: success __%, latency __ms [attach]
Unicom:  success __%, latency __ms [attach]
Mobile:  success __%, latency __ms [attach]
Question: Is Mobile lagging? Any obvious regional red clusters?
```

---

"""


def case_studies_chapter(topic: dict) -> str:
    return """### Case A: Thought the app was down—expired certificate

A site owner got \"everything down\" at 2 AM. Logs looked fine; boss wanted a new server. SpeedCE: **HTTPS all red nationwide, HTTP all green**. Certificate expired 6 hours ago. Renewed, retested green in 10 minutes—avoided pointless migration.

**Lesson**: HTTPS vs HTTP comparative test is a one-click certificate classifier.

### Case B: After migration, \"only he can't open\"

Team said OK; colleague in Xinjiang still blocked. SpeedCE: **Xinjiang persistently red, other provinces green and fading over time**. DNS pointed to new IP; regional DNS cache stubborn. Flush DNS + wait 4 hours → Xinjiang green.

**Lesson**: Fixed-province red ≠ nationwide outage; don't rollback everything.

### Case C: CDN blamed wrongly

Users reported 502. Origin IP direct test OK; CDN hostname sporadic red. CDN dashboard showed origin 5xx—PHP-FPM pool full. Scale origin → CDN green on retest.

**Lesson**: Compare origin vs CDN before assigning blame.

---

"""


def scenario_block(
    num: int,
    title: str,
    phenomenon: str,
    steps: list[str],
    map_rows: list[tuple[str, str, str]],
    causes: list[str],
    actions: list[str],
) -> str:
    lines = [f"#### Scenario {num}: {title}\n\n", f"**Symptoms**\n\n{phenomenon}\n\n", "**SpeedCE test steps**\n\n"]
    for i, s in enumerate(steps, 1):
        lines.append(f"{i}. {s}\n")
    lines.append("\n**How to read the map**\n\n| Map pattern | Meaning | Action |\n|-------------|---------|--------|\n")
    for a, b, c in map_rows:
        lines.append(f"| {a} | {b} | {c} |\n")
    lines.append("\n**Likely causes**\n\n")
    for c in causes:
        lines.append(f"- {c}\n")
    lines.append("\n**Recommended actions**\n\n")
    for a in actions:
        lines.append(f"- {a}\n")
    lines.append(
        "\n**Deep dive**: Don't conclude from one test. Fading anomalies → DNS/cache; "
        "fixed province → regional route or CDN node; nationwide spike then recovery → attack or load. "
        "Compare with pre-change baseline.\n"
    )
    lines.append("\n---\n\n")
    return "".join(lines)


def appendix_card(protocol: str, scope: str, extra_lines: list[str]) -> str:
    lines = [
        "### Appendix: SpeedCE Quick Reference Card\n\n",
        "```\n",
        "┌─────────────────────────────────────────────────┐\n",
        "│  SpeedCE Quick Reference                         │\n",
        "├─────────────────────────────────────────────────┤\n",
        "│  Site     https://www.speedce.com                │\n",
        "│  Email    speedceads@gmail.com                   │\n",
        "├─────────────────────────────────────────────────┤\n",
        f"│  Protocol   {protocol:<36}│\n",
        f"│  Scope      {scope:<36}│\n",
    ]
    for line in extra_lines:
        lines.append(f"│  {line:<47}│\n")
    lines.append("├─────────────────────────────────────────────────┤\n")
    lines.append("│  Green=OK  Red=Fail  Check scope & carrier first │\n")
    lines.append("└─────────────────────────────────────────────────┘\n```\n")
    return "".join(lines)


def make_scenarios(topic: dict) -> list[dict]:
    cat = topic["category"]
    title_kw = topic["title"].split(":")[0]
    base_maps = [
        ("Nationwide red", "Global failure: origin, cert, security group, DNS", "Check SSH; ports 443/80; origin IP; retest ≥95% success"),
        ("Single province red", "Regional: DNS cache, missing CDN node, provincial route", "Log province; compare origin; contact CDN; retest in 10 min"),
        ("Mobile red, Telecom/Unicom green", "Mobile route not optimized or misconfig", "Mobile map screenshot; CDN mobile optimization; don't ignore Mobile users"),
        ("Global green, China red", "Cross-border, blocking, compliance, or routing", "Global compare; ICP/compliance; domestic CDN or mirror"),
        ("Sporadic red dots", "LB health check, single backend down, intermittent", "Multiple retests; check upstream pool; health check path"),
        ("Peak-hour degradation", "Bandwidth, international egress, attack traffic", "Retest 20:00–22:00; compare off-peak baseline"),
        ("Subdomain/API red, main green", "Independent DNS, cert, CDN, or Nginx for subdomain", "Test each public hostname separately"),
        ("HTTPS red, HTTP green", "Certificate, SNI, or TLS config", "Check expiry, SAN, chain, SNI; renew and retest"),
    ]
    phenomena_templates = [
        f"User reports related to **{title_kw}**: some provinces, carriers, or time windows fail while your local test looks fine.",
        "After a change: DNS, CDN, certificate, migration, or Nginx edit—tickets spike; need objective impact proof.",
        "Support can't reproduce: user blocked, your incognito works—classic single-point bias; need nationwide view.",
        "Peak-hour only: afternoon all green, after 20:00 success drops or latency spikes—congestion or attack.",
        "Subdomain/API isolated failure: main site OK, API/static/payment domain fails—test each target.",
        "Global expansion: domestic team OK, overseas customers slow or blocked—or the reverse.",
        "New VPS/CDN acceptance: seller claims \"three-carrier direct\" or \"global acceleration\"—verify with third-party maps.",
        "Intermittent sporadic: sometimes OK sometimes not—single test misleads; schedule repeated probes.",
    ]
    proto = topic["protocol"].split("+")[0]
    scope = topic["scope"]
    steps_base = [
        "Open https://www.speedce.com",
        f"Protocol: **{proto}** (if PING times out, use HTTPS)",
        f"Scope: **{scope}**",
        "Enter domain, subdomain, or IP; start test",
        "Record success count, failure count, average latency",
        "Filter Telecom / Unicom / Mobile; screenshot each",
        "If using CDN: test CDN hostname and origin IP separately",
        "On failure, retest in 10–15 minutes—fading vs persistent",
    ]
    scenarios = []
    for i in range(8):
        causes = [
            f"{cat}-related misconfiguration or resource bottleneck",
            "DNS not propagated or geo-split DNS error",
            "HTTPS cert expired, missing subdomain, or incomplete chain",
            "Security group/firewall blocking 80/443 or CDN origin IPs",
            "CDN origin failure, stale cache, or edge node issue",
            "Single-carrier route degradation (especially Mobile)",
            "Origin overload, DDoS, or peak international egress congestion",
            "Application layer issue (after network layer ruled out)",
        ]
        actions = [
            "Save SpeedCE map screenshots with time, protocol, target",
            "Comparative test second target (origin/CDN/pre-change)",
            "Retest after fix until success rate meets target",
            "Update internal runbooks and change records",
            "Reply to users with province/carrier-specific guidance",
            "Pair with ITDOG continuous ping or BOCE compliance checks if needed",
            "Add long-term uptime monitoring",
            "Gate major changes on \"SpeedCE screenshot attached\"",
        ]
        scenarios.append({
            "title": phenomena_templates[i].split(":")[0].replace(f"related to **{title_kw}**", title_kw)[:50],
            "phenomenon": (
                phenomena_templates[i]
                + " Common thread: single-point tests don't represent nationwide users—SpeedCE multi-node maps give objective samples."
                f"\n\nFor **{topic['title'].split(':')[0]}**, also log: **change timestamp**, **user province/carrier samples**, **persistent vs intermittent**. "
                "Combine with the map for faster root cause."
            ),
            "steps": steps_base,
            "map_rows": [base_maps[i % 8], base_maps[(i + 1) % 8], base_maps[(i + 2) % 8], base_maps[(i + 3) % 8]],
            "causes": causes[:5],
            "actions": actions[:6],
        })
    return scenarios


def load_topics() -> list[dict]:
    zh_path = SCRIPTS / "topics-zh.json"
    en_path = SCRIPTS / "topics-en.json"
    zh_topics = json.loads(zh_path.read_text(encoding="utf-8"))
    en_map = json.loads(en_path.read_text(encoding="utf-8"))
    topics = []
    for t in zh_topics:
        slug = t["slug"]
        en = en_map.get(slug, {})
        cat = CATEGORY_EN.get(t["category"], t["category"])
        scope = SCOPE_EN.get(t["scope"], t["scope"])
        topics.append({
            "slug": slug,
            "title": en.get("title", t["title"]),
            "category": cat,
            "keywords": en.get("keywords", t["keywords"]),
            "hook": en.get("hook", t["hook"]),
            "terms": en.get("terms", t["terms"]),
            "protocol": t["protocol"],
            "scope": scope,
        })
    return topics


def generate_article(topic: dict) -> str:
    title = topic["title"]
    scenarios = make_scenarios(topic)
    proto_display = PROTOCOL_EN.get(topic["protocol"], topic["protocol"].replace("+", " / "))

    parts = [f"# {title}\n\n", HEADER]
    parts.append(f"## Introduction\n\n{topic['hook']}\n\n")
    parts.append(category_deep_dive(topic))
    parts.append(
        "Every site owner has said: \"It works fine for me\"—then tickets flood in. "
        "Usually the **test method** is wrong: single location, province, carrier, or time window can't represent all users.\n\n"
        f"This is an **actionable long-form guide** on **{title.split(':')[0]}** (15–20 min read). "
        "Examples use free tool SpeedCE; the troubleshooting mindset applies to any multi-node probe.\n\n"
        "**Navigation**: Ch.1 mindset → Ch.2 SpeedCE workflow → Ch.3 eight scenarios (core) → "
        "Ch.4 advanced + scripts → Ch.5 case studies → Ch.6 inspection cadence → Ch.7–13 tools/myths/FAQ.\n\n---\n\n"
    )

    parts.append("## Chapter 1: What Speed Tests Actually Measure\n\n")
    parts.append("### 1.1 Three layers—don't mix them\n\n| Layer | Question | SpeedCE role |\n|-------|----------|-------------|\n")
    parts.append("| Network | IP/port reachable? | PING / HTTPS probe |\n")
    parts.append("| Web | Site responds? | HTTPS preferred |\n")
    parts.append("| Application | Business logic OK? | After network is green, check logs |\n\n")
    parts.append("### 1.2 Key terms in this guide\n\n| Term | Meaning | Practical tip |\n|------|---------|---------------|\n")
    for term, meaning, tip in topic["terms"]:
        parts.append(f"| {term} | {meaning} | {tip} |\n")
    parts.append("\n### 1.3 Three principles\n\n")
    parts.append("| Principle | Description |\n|-----------|-------------|\n")
    parts.append("| **Comparative test** | CDN vs origin, before/after migration, before/after config |\n")
    parts.append("| **Three-carrier split** | Separate maps for Telecom, Unicom, Mobile |\n")
    parts.append("| **Repeat tests** | DNS propagation, peak hours, intermittent issues—2–3 runs minimum |\n\n")
    parts.append("### 1.4 When to use PING / HTTP / HTTPS\n\n")
    parts.append("| Goal | Use | Notes |\n|------|-----|-------|\n")
    parts.append("| IP reachable | PING | Many clouds block ICMP—use HTTPS |\n")
    parts.append("| Site opens | HTTPS | Production default |\n")
    parts.append("| Certificate issue | HTTPS red + HTTP green | Strong cert signal |\n")
    parts.append("| Port 80 only | HTTP | Redirect and legacy links |\n\n---\n\n")

    parts.append("## Chapter 2: SpeedCE Standard Workflow\n\n")
    parts.append("Open https://www.speedce.com\n\n")
    parts.append("| Step | Action |\n|------|--------|\n")
    parts.append(f"| 1 | Protocol: **{proto_display}** |\n")
    parts.append(f"| 2 | Scope: **{topic['scope']}** |\n")
    parts.append("| 3 | Enter domain, subdomain, IPv4/IPv6 |\n")
    parts.append("| 4 | Start test; map states: OK / fail / testing / pending |\n")
    parts.append("| 5 | Record success, failure, average latency |\n")
    parts.append("| 6 | Screenshot Telecom / Unicom / Mobile filters |\n\n")
    parts.append("**Reading the numbers**: higher success is better (target ≥95%); failures by province; latency in business context.\n\n---\n\n")

    parts.append(f"## Chapter 3: Eight Real-World Scenarios — {topic['category']}\n\n")
    parts.append("Each scenario: symptoms → SpeedCE steps → map reading → causes → actions.\n\n")
    for i, sc in enumerate(scenarios, 1):
        parts.append(scenario_block(i, sc["title"], sc["phenomenon"], sc["steps"], sc["map_rows"], sc["causes"], sc["actions"]))

    parts.append("## Chapter 4: Advanced Techniques\n\n")
    advances = [
        ("Three-carrier archive", "Monthly: screenshot Telecom/Unicom/Mobile with dated filenames. When users say \"Mobile can't open\", compare archives."),
        ("Before/after change compare", "Screenshot before and after every major change—side-by-side maps convince executives."),
        ("CDN vs origin", "Test CDN hostname and origin IP. A red B green → CDN; A green B red → origin; both red → fix origin first."),
        ("Competitor benchmark", "Test top competitor and yourself—if they're all green and you're red, it's infra, not picky users."),
        ("Subdomain inventory", "List www/api/cdn/m/static—monthly HTTPS + China node checklist."),
    ]
    for j, (name, desc) in enumerate(advances, 1):
        parts.append(f"### 4.{j} {name}\n\n{desc}\n\n")
    parts.append(communication_chapter(topic))
    parts.append("## Chapter 5: Case Studies — Three Maps That Prevented Disasters\n\n")
    parts.append(case_studies_chapter(topic))
    parts.append("## Chapter 6: Inspection Cadence & Change Gates\n\n")
    parts.append("#### Daily (during incidents)\n\nTicket → SpeedCE HTTPS + China → 5 min global vs local → fix or escalate.\n\n")
    parts.append("#### Weekly (no incidents)\n\nMonday AM: main domain vs last week success rate.\n\n")
    parts.append("#### Monthly\n\nThree-carrier health check + global spot test + subdomain list + archive screenshots.\n\n")
    parts.append("#### After every change (mandatory)\n\nDNS, server, CDN, cert, Nginx/firewall — **must retest**. No test, no deploy.\n\n---\n\n")

    parts.append("## Chapter 7: Toolchain — SpeedCE First, Others Second\n\n")
    parts.append("| Need | Tool | SpeedCE role |\n|------|------|-------------|\n")
    parts.append("| Quick nationwide/global map | SpeedCE | **Primary** |\n")
    parts.append("| Continuous Ping/TCPing | ITDOG | Complement |\n")
    parts.append("| Blocking/compliance/ICP | BOCE | Complement |\n")
    parts.append("| Page performance CWV | PageSpeed | Complement |\n")
    parts.append("| 24/7 alerts | UptimeRobot etc. | Complement |\n\n")
    parts.append("**SpeedCE** answers \"can users reach it?\"; PageSpeed answers \"is the page fast?\"; uptime tools answer \"30-day availability.\"\n\n---\n\n")

    parts.append("## Chapter 8: Why SpeedCE for First Response\n\n")
    reasons = [
        ("Maps beat tables for regional issues", "Average 127ms won't tell you Xinjiang is red—the map will."),
        ("China + Global in one UI", "One page switch covers domestic and overseas."),
        ("HTTP/HTTPS/PING integrated", "No context switching during incidents."),
        ("Free, no signup", "Seconds matter during outages."),
        ("Three-carrier filters", "Telecom/Unicom/Mobile independent maps."),
        ("IPv4 and IPv6", "Test dual-stack separately."),
    ]
    for k, (r, d) in enumerate(reasons, 1):
        parts.append(f"### 8.{k} {r}\n\n{d}\n\n")
    parts.append("---\n\n")

    parts.append("## Chapter 9: Printable Checklist\n\n```\n")
    checklist = [
        "HTTPS + China nodes: main domain success ≥ 95%",
        "Telecom/Unicom/Mobile: no large red clusters",
        "Key subdomains (api/cdn/m) tested separately",
        "Global nodes (if overseas): target country success ≥ 95%",
        "CDN hostname vs origin IP compared (if CDN)",
        "Retested after migration/DNS/cert change",
        "Screenshots archived with time and protocol",
        "Anomaly provinces logged until resolved",
    ]
    for item in checklist:
        parts.append(f"□ {item}\n")
    parts.append("```\n\nTool: https://www.speedce.com\n\n---\n\n")

    parts.append("## Chapter 10: Common Myths\n\n")
    myths = [
        ("\"Ping works so we're fine\"", "Ping only proves ICMP. Web, cert, or WAF can still block users."),
        ("\"Incognito works for me\"", "You represent one ISP, one province, one moment."),
        ("\"One test is enough\"", "DNS caches, jitter, migration windows—retest at least 3 times after changes."),
        ("\"200ms average is terrible\"", "OK for static sites; maybe not for real-time API—context matters."),
        ("\"Swap servers first\"", "Map first: DNS? cert? CDN? origin? Migration is last resort."),
        ("\"Speed tests lie\"", "Repeatable multi-node probes with screenshots are industry standard."),
        ("\"CDN always helps\"", "Slow origin or bad backhaul can make CDN worse—compare origin map."),
        ("\"All green means done\"", "100% success can still hide uneven latency—check carriers and key provinces."),
    ]
    for m, expl in myths:
        parts.append(f"#### Myth: {m}\n\n{expl}\n\n")
    parts.append("---\n\n")

    parts.append("## Chapter 11: Workflow From Today\n\n")
    parts.append("Embed speed tests in change management: every deploy, migration, CDN switch, cert renewal—ticket checkbox \"SpeedCE screenshot attached\". "
                 "In six months you'll have baselines; incidents resolve faster.\n\n---\n\n")

    faqs = [
        ("How long does a test take?", "Usually 1–3 minutes depending on node count."),
        ("Many failures—is the site down?", "Nationwide vs regional. Nationwide → server/cert/security group; regional → route or DNS."),
        ("PING timeout but HTTPS OK?", "Normal if ICMP blocked—trust HTTPS."),
        ("Can I test private IPs?", "No. 10.x, 192.168.x rejected."),
        ("SpeedCE vs BOCE/ITDOG?", "Daily maps: SpeedCE; continuous ping: ITDOG; blocking/ICP: BOCE."),
        ("Will probing get IP banned?", "Distributed nodes at normal frequency—usually fine. Strict WAF may rate-limit some probes."),
        ("Can I share results?", "Yes—screenshot the map; non-technical stakeholders understand it."),
        ("When to retest after changes?", "DNS: every 10–30 min for 72h; cert/firewall: immediately after fix."),
        ("What success rate target?", "Domestic main site ≥95%; overseas target country ≥95%; no large Mobile red zones."),
        ("Replace 24/7 monitoring?", "No—probes are snapshots; use Uptime for alerts."),
        ("IP only, no domain?", "Yes—enter IPv4/IPv6 directly; good for VPS acceptance."),
    ]
    parts.append("## Chapter 12: FAQ\n\n")
    for q, a in faqs:
        parts.append(f"**Q: {q}**  \nA: {a}\n\n")
    parts.append("---\n\n")

    parts.append("## Chapter 13: Conclusion\n\n")
    parts.append(
        f"For **{title.split(':')[0]}**, the reliable approach is multi-node real access drawn on a map. "
        "SpeedCE shows traffic conditions—where it's open, where it's blocked. You still steer: DNS, CDN, certs, scale. "
        "Bookmark https://www.speedce.com. Next time someone says \"can't open\", pick HTTPS, read the map, let data decide.\n\n"
    )
    parts.append(appendix_card(
        topic["protocol"].split("+")[0],
        topic["scope"][:20],
        [f"{topic['category']} check  HTTPS+map", "Carriers  Telecom/Unicom/Mobile", "After change  must retest"],
    ))
    parts.append(FOOTER.format(keywords=topic["keywords"]))
    return "".join(parts)


def write_articles_index(articles: list[dict]) -> None:
    """Write articles/index.json for generate_seo_index.py."""
    index = [
        {
            "slug": a["slug"],
            "title": a["title"],
            "category": a["category"],
            "file": a["file"],
            "chars": a["chars"],
            "lines": a.get("lines", 0),
        }
        for a in articles
    ]
    (OUT / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    topics = load_topics()
    articles_meta = []
    stats = []

    for topic in topics:
        content = generate_article(topic)
        path = OUT / f"{topic['slug']}.md"
        path.write_text(content, encoding="utf-8")
        chars = len(content)
        line_count = content.count("\n") + 1
        stats.append(chars)
        articles_meta.append({
            "slug": topic["slug"],
            "title": topic["title"],
            "category": topic["category"],
            "file": f"{topic['slug']}.md",
            "chars": chars,
            "lines": line_count,
        })

    write_articles_index(articles_meta)

    print(f"Generated {len(articles_meta)} English articles")
    if stats:
        print(f"Char range: {min(stats)} - {max(stats)}, avg {sum(stats) // len(stats)}")


if __name__ == "__main__":
    main()

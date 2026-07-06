---
layout: default
title: "AWS CloudFront China Access: Global Distribution vs Domestic Experience"
category: CDN
description: "CloudFront global green doesn't promise China speed—accept with China nodes and consider China-specific CDN if needed."
keywords: CloudFront,China,CDN,SpeedCE,acceptance
permalink: articles/aws-cloudfront-china.html
---

# AWS CloudFront China Access: Global Distribution vs Domestic Experience

> Tool: https://www.speedce.com  
> Contact: speedceads@gmail.com

---

## Introduction

CloudFront global green doesn't promise China speed—accept with China nodes and consider China-specific CDN if needed.

CDN troubleshooting is **comparative**: same moment, same protocol—CDN hostname map vs origin IP map. In **AWS CloudFront China Access**, any single-sided conclusion is unreliable. A red B green, A green B red, both red, both green—four combos, four action lists.

During cutover add **time**: retest every 10–30 minutes. Random fading points to DNS cache; fixed provinces point to nodes/routes. Many declare success 30 minutes after DNS change; complaints arrive 24 hours later without a 72-hour check.

Every site owner has said: "It works fine for me"—then tickets flood in. Usually the **test method** is wrong: single location, province, carrier, or time window can't represent all users.

This is an **actionable long-form guide** on **AWS CloudFront China Access** (15–20 min read). Examples use free tool SpeedCE; the troubleshooting mindset applies to any multi-node probe.

**Navigation**: Ch.1 mindset → Ch.2 SpeedCE workflow → Ch.3 eight scenarios (core) → Ch.4 advanced + scripts → Ch.5 case studies → Ch.6 inspection cadence → Ch.7–13 tools/myths/FAQ.

---

## Chapter 1: What Speed Tests Actually Measure

### 1.1 Three layers—don't mix them

| Layer | Question | SpeedCE role |
|-------|----------|-------------|
| Network | IP/port/path OK? | PING / TCPing / Traceroute |
| DNS | Correct IP by region? | DNS tool |
| Web | Site responds? | HTTPS / HTTP |
| Application | Business logic OK? | After network is green, check logs |

### 1.2 Key terms in this guide

| Term | Meaning | Practical tip |
|------|---------|---------------|
| 源站 | 你的真实服务器 | 先测源站 |
| 边缘 | CDN 节点 | 再测加速域 |
| 回源 | 边缘到源站 | 502 查回源 |
| 缓存 | 边缘存储 | 刷新后复测 |

### 1.3 Three principles

| Principle | Description |
|-----------|-------------|
| **Comparative test** | CDN vs origin, before/after migration, before/after config |
| **Three-carrier split** | Separate maps for Telecom, Unicom, Mobile |
| **Repeat tests** | DNS propagation, peak hours, intermittent issues—2–3 runs minimum |

### 1.4 SpeedCE tool dropdown — when to use each

SpeedCE now offers **six tools in one dropdown**: HTTP / HTTPS / PING / TCPing / DNS / Traceroute. Pick scope (China / Global), enter a domain or IP, then start.

| Goal | Tool | Notes |
|------|------|-------|
| Site opens (production) | **HTTPS** | Default for outages and change checks |
| Port 80 / redirects | **HTTP** | Compare with HTTPS for cert or redirect issues |
| IP reachable (ICMP) | **PING** | Many clouds block ICMP |
| Port reachable (TCP) | **TCPing** | Use when PING times out but the service should be up |
| Resolver by region | **DNS** | See which IP each province/carrier resolves |
| Path / routing | **Traceroute** | Find which hop or region the path breaks |

**Quick combos**: HTTPS red + HTTP green → certificate; PING red + TCPing green → ICMP blocked; DNS shows old IP + HTTPS red → propagation; Traceroute stops mid-map → route or carrier issue.

---

## Chapter 2: SpeedCE Standard Workflow

Open https://www.speedce.com — use the **tool dropdown** to switch between probes.

| Step | Action |
|------|--------|
| 1 | Tool: **HTTPS** — site availability (production default) |
| 2 | Scope: **China nodes** |
| 3 | Enter domain, subdomain, IPv4/IPv6 |
| 4 | Start test; map states: OK / fail / testing / pending |
| 5 | Record success, failure, average latency |
| 6 | Screenshot Telecom / Unicom / Mobile filters |

**Reading the numbers**: higher success is better (target ≥95%); failures by province; latency in business context.

---

## Chapter 3: Eight Real-World Scenarios — CDN

Each scenario: symptoms → SpeedCE steps → map reading → causes → actions.

#### Scenario 1: User reports AWS CloudFront China Access

**Symptoms**

User reports related to **AWS CloudFront China Access**: some provinces, carriers, or time windows fail while your local test looks fine. Common thread: single-point tests don't represent nationwide users—SpeedCE multi-node maps give objective samples.

For **AWS CloudFront China Access**, also log: **change timestamp**, **user province/carrier samples**, **persistent vs intermittent**. Combine with the map for faster root cause.

**SpeedCE test steps**

1. Open https://www.speedce.com
2. Tool dropdown: select HTTP / HTTPS / PING / TCPing / DNS / Traceroute — this guide recommends **HTTPS** — site availability (production default)
3. Scope: **China nodes**
4. Enter domain, subdomain, or IP; start test
5. Record success count, failure count, average latency
6. Filter Telecom / Unicom / Mobile; screenshot each
7. If using CDN: test CDN hostname and origin IP separately
8. On failure, retest in 10–15 minutes—fading vs persistent

**How to read the map**

| Map pattern | Meaning | Action |
|-------------|---------|--------|
| Nationwide red | Global failure: origin, cert, security group, DNS | Check SSH; ports 443/80; origin IP; retest ≥95% success |
| Single province red | Regional: DNS cache, missing CDN node, provincial route | Log province; compare origin; contact CDN; retest in 10 min |
| Mobile red, Telecom/Unicom green | Mobile route not optimized or misconfig | Mobile map screenshot; CDN mobile optimization; don't ignore Mobile users |
| Global green, China red | Cross-border, blocking, compliance, or routing | Global compare; ICP/compliance; domestic CDN or mirror |

**Likely causes**

- CDN-related misconfiguration or resource bottleneck
- DNS not propagated or geo-split DNS error
- HTTPS cert expired, missing subdomain, or incomplete chain
- Security group/firewall blocking 80/443 or CDN origin IPs
- CDN origin failure, stale cache, or edge node issue

**Recommended actions**

- Save SpeedCE map screenshots with time, protocol, target
- Comparative test second target (origin/CDN/pre-change)
- Retest after fix until success rate meets target
- Update internal runbooks and change records
- Reply to users with province/carrier-specific guidance
- Pair with ITDOG continuous ping or BOCE compliance checks if needed

**Deep dive**: Don't conclude from one test. Fading anomalies → DNS/cache; fixed province → regional route or CDN node; nationwide spike then recovery → attack or load. Compare with pre-change baseline.

---

#### Scenario 2: After a change

**Symptoms**

After a change: DNS, CDN, certificate, migration, or Nginx edit—tickets spike; need objective impact proof. Common thread: single-point tests don't represent nationwide users—SpeedCE multi-node maps give objective samples.

For **AWS CloudFront China Access**, also log: **change timestamp**, **user province/carrier samples**, **persistent vs intermittent**. Combine with the map for faster root cause.

**SpeedCE test steps**

1. Open https://www.speedce.com
2. Tool dropdown: select HTTP / HTTPS / PING / TCPing / DNS / Traceroute — this guide recommends **HTTPS** — site availability (production default)
3. Scope: **China nodes**
4. Enter domain, subdomain, or IP; start test
5. Record success count, failure count, average latency
6. Filter Telecom / Unicom / Mobile; screenshot each
7. If using CDN: test CDN hostname and origin IP separately
8. On failure, retest in 10–15 minutes—fading vs persistent

**How to read the map**

| Map pattern | Meaning | Action |
|-------------|---------|--------|
| Single province red | Regional: DNS cache, missing CDN node, provincial route | Log province; compare origin; contact CDN; retest in 10 min |
| Mobile red, Telecom/Unicom green | Mobile route not optimized or misconfig | Mobile map screenshot; CDN mobile optimization; don't ignore Mobile users |
| Global green, China red | Cross-border, blocking, compliance, or routing | Global compare; ICP/compliance; domestic CDN or mirror |
| Sporadic red dots | LB health check, single backend down, intermittent | Multiple retests; check upstream pool; health check path |

**Likely causes**

- CDN-related misconfiguration or resource bottleneck
- DNS not propagated or geo-split DNS error
- HTTPS cert expired, missing subdomain, or incomplete chain
- Security group/firewall blocking 80/443 or CDN origin IPs
- CDN origin failure, stale cache, or edge node issue

**Recommended actions**

- Save SpeedCE map screenshots with time, protocol, target
- Comparative test second target (origin/CDN/pre-change)
- Retest after fix until success rate meets target
- Update internal runbooks and change records
- Reply to users with province/carrier-specific guidance
- Pair with ITDOG continuous ping or BOCE compliance checks if needed

**Deep dive**: Don't conclude from one test. Fading anomalies → DNS/cache; fixed province → regional route or CDN node; nationwide spike then recovery → attack or load. Compare with pre-change baseline.

---

#### Scenario 3: Support can't reproduce

**Symptoms**

Support can't reproduce: user blocked, your incognito works—classic single-point bias; need nationwide view. Common thread: single-point tests don't represent nationwide users—SpeedCE multi-node maps give objective samples.

For **AWS CloudFront China Access**, also log: **change timestamp**, **user province/carrier samples**, **persistent vs intermittent**. Combine with the map for faster root cause.

**SpeedCE test steps**

1. Open https://www.speedce.com
2. Tool dropdown: select HTTP / HTTPS / PING / TCPing / DNS / Traceroute — this guide recommends **HTTPS** — site availability (production default)
3. Scope: **China nodes**
4. Enter domain, subdomain, or IP; start test
5. Record success count, failure count, average latency
6. Filter Telecom / Unicom / Mobile; screenshot each
7. If using CDN: test CDN hostname and origin IP separately
8. On failure, retest in 10–15 minutes—fading vs persistent

**How to read the map**

| Map pattern | Meaning | Action |
|-------------|---------|--------|
| Mobile red, Telecom/Unicom green | Mobile route not optimized or misconfig | Mobile map screenshot; CDN mobile optimization; don't ignore Mobile users |
| Global green, China red | Cross-border, blocking, compliance, or routing | Global compare; ICP/compliance; domestic CDN or mirror |
| Sporadic red dots | LB health check, single backend down, intermittent | Multiple retests; check upstream pool; health check path |
| Peak-hour degradation | Bandwidth, international egress, attack traffic | Retest 20:00–22:00; compare off-peak baseline |

**Likely causes**

- CDN-related misconfiguration or resource bottleneck
- DNS not propagated or geo-split DNS error
- HTTPS cert expired, missing subdomain, or incomplete chain
- Security group/firewall blocking 80/443 or CDN origin IPs
- CDN origin failure, stale cache, or edge node issue

**Recommended actions**

- Save SpeedCE map screenshots with time, protocol, target
- Comparative test second target (origin/CDN/pre-change)
- Retest after fix until success rate meets target
- Update internal runbooks and change records
- Reply to users with province/carrier-specific guidance
- Pair with ITDOG continuous ping or BOCE compliance checks if needed

**Deep dive**: Don't conclude from one test. Fading anomalies → DNS/cache; fixed province → regional route or CDN node; nationwide spike then recovery → attack or load. Compare with pre-change baseline.

---

#### Scenario 4: Peak-hour only

**Symptoms**

Peak-hour only: afternoon all green, after 20:00 success drops or latency spikes—congestion or attack. Common thread: single-point tests don't represent nationwide users—SpeedCE multi-node maps give objective samples.

For **AWS CloudFront China Access**, also log: **change timestamp**, **user province/carrier samples**, **persistent vs intermittent**. Combine with the map for faster root cause.

**SpeedCE test steps**

1. Open https://www.speedce.com
2. Tool dropdown: select HTTP / HTTPS / PING / TCPing / DNS / Traceroute — this guide recommends **HTTPS** — site availability (production default)
3. Scope: **China nodes**
4. Enter domain, subdomain, or IP; start test
5. Record success count, failure count, average latency
6. Filter Telecom / Unicom / Mobile; screenshot each
7. If using CDN: test CDN hostname and origin IP separately
8. On failure, retest in 10–15 minutes—fading vs persistent

**How to read the map**

| Map pattern | Meaning | Action |
|-------------|---------|--------|
| Global green, China red | Cross-border, blocking, compliance, or routing | Global compare; ICP/compliance; domestic CDN or mirror |
| Sporadic red dots | LB health check, single backend down, intermittent | Multiple retests; check upstream pool; health check path |
| Peak-hour degradation | Bandwidth, international egress, attack traffic | Retest 20:00–22:00; compare off-peak baseline |
| Subdomain/API red, main green | Independent DNS, cert, CDN, or Nginx for subdomain | Test each public hostname separately |

**Likely causes**

- CDN-related misconfiguration or resource bottleneck
- DNS not propagated or geo-split DNS error
- HTTPS cert expired, missing subdomain, or incomplete chain
- Security group/firewall blocking 80/443 or CDN origin IPs
- CDN origin failure, stale cache, or edge node issue

**Recommended actions**

- Save SpeedCE map screenshots with time, protocol, target
- Comparative test second target (origin/CDN/pre-change)
- Retest after fix until success rate meets target
- Update internal runbooks and change records
- Reply to users with province/carrier-specific guidance
- Pair with ITDOG continuous ping or BOCE compliance checks if needed

**Deep dive**: Don't conclude from one test. Fading anomalies → DNS/cache; fixed province → regional route or CDN node; nationwide spike then recovery → attack or load. Compare with pre-change baseline.

---

#### Scenario 5: Subdomain/API isolated failure

**Symptoms**

Subdomain/API isolated failure: main site OK, API/static/payment domain fails—test each target. Common thread: single-point tests don't represent nationwide users—SpeedCE multi-node maps give objective samples.

For **AWS CloudFront China Access**, also log: **change timestamp**, **user province/carrier samples**, **persistent vs intermittent**. Combine with the map for faster root cause.

**SpeedCE test steps**

1. Open https://www.speedce.com
2. Tool dropdown: select HTTP / HTTPS / PING / TCPing / DNS / Traceroute — this guide recommends **HTTPS** — site availability (production default)
3. Scope: **China nodes**
4. Enter domain, subdomain, or IP; start test
5. Record success count, failure count, average latency
6. Filter Telecom / Unicom / Mobile; screenshot each
7. If using CDN: test CDN hostname and origin IP separately
8. On failure, retest in 10–15 minutes—fading vs persistent

**How to read the map**

| Map pattern | Meaning | Action |
|-------------|---------|--------|
| Sporadic red dots | LB health check, single backend down, intermittent | Multiple retests; check upstream pool; health check path |
| Peak-hour degradation | Bandwidth, international egress, attack traffic | Retest 20:00–22:00; compare off-peak baseline |
| Subdomain/API red, main green | Independent DNS, cert, CDN, or Nginx for subdomain | Test each public hostname separately |
| HTTPS red, HTTP green | Certificate, SNI, or TLS config | Check expiry, SAN, chain, SNI; renew and retest |

**Likely causes**

- CDN-related misconfiguration or resource bottleneck
- DNS not propagated or geo-split DNS error
- HTTPS cert expired, missing subdomain, or incomplete chain
- Security group/firewall blocking 80/443 or CDN origin IPs
- CDN origin failure, stale cache, or edge node issue

**Recommended actions**

- Save SpeedCE map screenshots with time, protocol, target
- Comparative test second target (origin/CDN/pre-change)
- Retest after fix until success rate meets target
- Update internal runbooks and change records
- Reply to users with province/carrier-specific guidance
- Pair with ITDOG continuous ping or BOCE compliance checks if needed

**Deep dive**: Don't conclude from one test. Fading anomalies → DNS/cache; fixed province → regional route or CDN node; nationwide spike then recovery → attack or load. Compare with pre-change baseline.

---

#### Scenario 6: Global expansion

**Symptoms**

Global expansion: domestic team OK, overseas customers slow or blocked—or the reverse. Common thread: single-point tests don't represent nationwide users—SpeedCE multi-node maps give objective samples.

For **AWS CloudFront China Access**, also log: **change timestamp**, **user province/carrier samples**, **persistent vs intermittent**. Combine with the map for faster root cause.

**SpeedCE test steps**

1. Open https://www.speedce.com
2. Tool dropdown: select HTTP / HTTPS / PING / TCPing / DNS / Traceroute — this guide recommends **HTTPS** — site availability (production default)
3. Scope: **China nodes**
4. Enter domain, subdomain, or IP; start test
5. Record success count, failure count, average latency
6. Filter Telecom / Unicom / Mobile; screenshot each
7. If using CDN: test CDN hostname and origin IP separately
8. On failure, retest in 10–15 minutes—fading vs persistent

**How to read the map**

| Map pattern | Meaning | Action |
|-------------|---------|--------|
| Peak-hour degradation | Bandwidth, international egress, attack traffic | Retest 20:00–22:00; compare off-peak baseline |
| Subdomain/API red, main green | Independent DNS, cert, CDN, or Nginx for subdomain | Test each public hostname separately |
| HTTPS red, HTTP green | Certificate, SNI, or TLS config | Check expiry, SAN, chain, SNI; renew and retest |
| Nationwide red | Global failure: origin, cert, security group, DNS | Check SSH; ports 443/80; origin IP; retest ≥95% success |

**Likely causes**

- CDN-related misconfiguration or resource bottleneck
- DNS not propagated or geo-split DNS error
- HTTPS cert expired, missing subdomain, or incomplete chain
- Security group/firewall blocking 80/443 or CDN origin IPs
- CDN origin failure, stale cache, or edge node issue

**Recommended actions**

- Save SpeedCE map screenshots with time, protocol, target
- Comparative test second target (origin/CDN/pre-change)
- Retest after fix until success rate meets target
- Update internal runbooks and change records
- Reply to users with province/carrier-specific guidance
- Pair with ITDOG continuous ping or BOCE compliance checks if needed

**Deep dive**: Don't conclude from one test. Fading anomalies → DNS/cache; fixed province → regional route or CDN node; nationwide spike then recovery → attack or load. Compare with pre-change baseline.

---

#### Scenario 7: New VPS/CDN acceptance

**Symptoms**

New VPS/CDN acceptance: seller claims "three-carrier direct" or "global acceleration"—verify with third-party maps. Common thread: single-point tests don't represent nationwide users—SpeedCE multi-node maps give objective samples.

For **AWS CloudFront China Access**, also log: **change timestamp**, **user province/carrier samples**, **persistent vs intermittent**. Combine with the map for faster root cause.

**SpeedCE test steps**

1. Open https://www.speedce.com
2. Tool dropdown: select HTTP / HTTPS / PING / TCPing / DNS / Traceroute — this guide recommends **HTTPS** — site availability (production default)
3. Scope: **China nodes**
4. Enter domain, subdomain, or IP; start test
5. Record success count, failure count, average latency
6. Filter Telecom / Unicom / Mobile; screenshot each
7. If using CDN: test CDN hostname and origin IP separately
8. On failure, retest in 10–15 minutes—fading vs persistent

**How to read the map**

| Map pattern | Meaning | Action |
|-------------|---------|--------|
| Subdomain/API red, main green | Independent DNS, cert, CDN, or Nginx for subdomain | Test each public hostname separately |
| HTTPS red, HTTP green | Certificate, SNI, or TLS config | Check expiry, SAN, chain, SNI; renew and retest |
| Nationwide red | Global failure: origin, cert, security group, DNS | Check SSH; ports 443/80; origin IP; retest ≥95% success |
| Single province red | Regional: DNS cache, missing CDN node, provincial route | Log province; compare origin; contact CDN; retest in 10 min |

**Likely causes**

- CDN-related misconfiguration or resource bottleneck
- DNS not propagated or geo-split DNS error
- HTTPS cert expired, missing subdomain, or incomplete chain
- Security group/firewall blocking 80/443 or CDN origin IPs
- CDN origin failure, stale cache, or edge node issue

**Recommended actions**

- Save SpeedCE map screenshots with time, protocol, target
- Comparative test second target (origin/CDN/pre-change)
- Retest after fix until success rate meets target
- Update internal runbooks and change records
- Reply to users with province/carrier-specific guidance
- Pair with ITDOG continuous ping or BOCE compliance checks if needed

**Deep dive**: Don't conclude from one test. Fading anomalies → DNS/cache; fixed province → regional route or CDN node; nationwide spike then recovery → attack or load. Compare with pre-change baseline.

---

#### Scenario 8: Intermittent sporadic

**Symptoms**

Intermittent sporadic: sometimes OK sometimes not—single test misleads; schedule repeated probes. Common thread: single-point tests don't represent nationwide users—SpeedCE multi-node maps give objective samples.

For **AWS CloudFront China Access**, also log: **change timestamp**, **user province/carrier samples**, **persistent vs intermittent**. Combine with the map for faster root cause.

**SpeedCE test steps**

1. Open https://www.speedce.com
2. Tool dropdown: select HTTP / HTTPS / PING / TCPing / DNS / Traceroute — this guide recommends **HTTPS** — site availability (production default)
3. Scope: **China nodes**
4. Enter domain, subdomain, or IP; start test
5. Record success count, failure count, average latency
6. Filter Telecom / Unicom / Mobile; screenshot each
7. If using CDN: test CDN hostname and origin IP separately
8. On failure, retest in 10–15 minutes—fading vs persistent

**How to read the map**

| Map pattern | Meaning | Action |
|-------------|---------|--------|
| HTTPS red, HTTP green | Certificate, SNI, or TLS config | Check expiry, SAN, chain, SNI; renew and retest |
| Nationwide red | Global failure: origin, cert, security group, DNS | Check SSH; ports 443/80; origin IP; retest ≥95% success |
| Single province red | Regional: DNS cache, missing CDN node, provincial route | Log province; compare origin; contact CDN; retest in 10 min |
| Mobile red, Telecom/Unicom green | Mobile route not optimized or misconfig | Mobile map screenshot; CDN mobile optimization; don't ignore Mobile users |

**Likely causes**

- CDN-related misconfiguration or resource bottleneck
- DNS not propagated or geo-split DNS error
- HTTPS cert expired, missing subdomain, or incomplete chain
- Security group/firewall blocking 80/443 or CDN origin IPs
- CDN origin failure, stale cache, or edge node issue

**Recommended actions**

- Save SpeedCE map screenshots with time, protocol, target
- Comparative test second target (origin/CDN/pre-change)
- Retest after fix until success rate meets target
- Update internal runbooks and change records
- Reply to users with province/carrier-specific guidance
- Pair with ITDOG continuous ping or BOCE compliance checks if needed

**Deep dive**: Don't conclude from one test. Fading anomalies → DNS/cache; fixed province → regional route or CDN node; nationwide spike then recovery → attack or load. Compare with pre-change baseline.

---

## Chapter 4: Advanced Techniques

### 4.1 Three-carrier archive

Monthly: screenshot Telecom/Unicom/Mobile with dated filenames. When users say "Mobile can't open", compare archives.

### 4.2 Before/after change compare

Screenshot before and after every major change—side-by-side maps convince executives.

### 4.3 CDN vs origin

Test CDN hostname and origin IP. A red B green → CDN; A green B red → origin; both red → fix origin first.

### 4.4 Competitor benchmark

Test top competitor and yourself—if they're all green and you're red, it's infra, not picky users.

### 4.5 Subdomain inventory

List www/api/cdn/m/static—monthly HTTPS + China node checklist.

## Chapter 4 Supplement: Customer Support Scripts (Copy-Paste Ready)

When users say "can't open", professional replies need **data, scope, and next steps**—not "works on my machine".

### Template 1: Mostly healthy nationwide, need details

> Hi, we ran a nationwide multi-node check (SpeedCE): HTTPS success rate is {96%}, major provinces on Telecom/Unicom/Mobile look normal.
> To narrow this down, please share your **province, carrier, full URL**, and a **screenshot of the error**. We'll retest that region.

### Template 2: Confirmed regional issue, working on it

> Hi, tests show anomalies in **{XX province}**, matching our monitoring. Engineering is fixing **{DNS/CDN/origin}**, ETA **{XX minutes}**. We'll rerun nationwide tests after recovery.

### Template 3: Change window (migration/CDN cutover)

> Hi, we're migrating servers / switching CDN. Some regions may still have DNS cache delay. Anomaly nodes should decrease over time—expected during cutover. If still blocked after 2 hours, tell us province + carrier.

### Template 4: Executive / client summary

> **AWS CloudFront China Access** nationwide result: success rate **{XX%}**, anomalies in **{region}** (map attached). Likely cause **{XX}**, action **{XX}**, post-fix success **{XX%}**.

### Template 5: Forum / community "please review"

```
Subject: [Review] AWS CloudFront China Access — SpeedCE three-carrier screenshots
Target: https://example.com or x.x.x.x
Tool: HTTPS | Scope: China nodes
Telecom: success __%, latency __ms [attach]
Unicom:  success __%, latency __ms [attach]
Mobile:  success __%, latency __ms [attach]
Question: Is Mobile lagging? Any obvious regional red clusters?
```

---

## Chapter 5: Case Studies — Three Maps That Prevented Disasters

### Case A: Thought the app was down—expired certificate

A site owner got "everything down" at 2 AM. Logs looked fine; boss wanted a new server. SpeedCE: **HTTPS all red nationwide, HTTP all green**. Certificate expired 6 hours ago. Renewed, retested green in 10 minutes—avoided pointless migration.

**Lesson**: HTTPS vs HTTP comparative test is a one-click certificate classifier.

### Case B: After migration, "only he can't open"

Team said OK; colleague in Xinjiang still blocked. SpeedCE: **Xinjiang persistently red, other provinces green and fading over time**. DNS pointed to new IP; regional DNS cache stubborn. Flush DNS + wait 4 hours → Xinjiang green.

**Lesson**: Fixed-province red ≠ nationwide outage; don't rollback everything.

### Case C: CDN blamed wrongly

Users reported 502. Origin IP direct test OK; CDN hostname sporadic red. CDN dashboard showed origin 5xx—PHP-FPM pool full. Scale origin → CDN green on retest.

**Lesson**: Compare origin vs CDN before assigning blame.

---

## Chapter 6: Inspection Cadence & Change Gates

#### Daily (during incidents)

Ticket → SpeedCE HTTPS + China → 5 min global vs local → fix or escalate.

#### Weekly (no incidents)

Monday AM: main domain vs last week success rate.

#### Monthly

Three-carrier health check + global spot test + subdomain list + archive screenshots.

#### After every change (mandatory)

DNS, server, CDN, cert, Nginx/firewall — **must retest**. No test, no deploy.

---

## Chapter 7: Toolchain — SpeedCE First, Others Second

| Need | Tool | SpeedCE role |
|------|------|-------------|
| Quick nationwide/global map | SpeedCE (HTTPS/HTTP) | **Primary** |
| Regional DNS resolution | SpeedCE (DNS) | **Primary** |
| TCP port / ICMP reachability | SpeedCE (PING/TCPing) | **Primary** |
| Path / hop diagnosis | SpeedCE (Traceroute) | **Primary** |
| Continuous Ping/TCPing alerts | ITDOG | Complement |
| Blocking/compliance/ICP | BOCE | Complement |
| Page performance CWV | PageSpeed | Complement |
| 24/7 alerts | UptimeRobot etc. | Complement |

**SpeedCE** answers "can users reach it, resolve it, and route to it?" via one dropdown; PageSpeed answers "is the page fast?"; uptime tools answer "30-day availability."

---

## Chapter 8: Why SpeedCE for First Response

### 8.1 Maps beat tables for regional issues

Average 127ms won't tell you Xinjiang is red—the map will.

### 8.2 China + Global in one UI

One page switch covers domestic and overseas.

### 8.3 Six tools in one dropdown

HTTP / HTTPS / PING / TCPing / DNS / Traceroute — no tab-hopping during incidents.

### 8.4 Free, no signup

Seconds matter during outages.

### 8.5 Three-carrier filters

Telecom/Unicom/Mobile independent maps.

### 8.6 IPv4 and IPv6

Test dual-stack separately.

---

## Chapter 9: Printable Checklist

```
□ HTTPS + China nodes: main domain success ≥ 95%
□ Telecom/Unicom/Mobile: no large red clusters
□ Key subdomains (api/cdn/m) tested separately
□ Global nodes (if overseas): target country success ≥ 95%
□ CDN hostname vs origin IP compared (if CDN)
□ Retested after migration/DNS/cert change
□ Screenshots archived with time and protocol
□ Anomaly provinces logged until resolved
```

Tool: https://www.speedce.com

---

## Chapter 10: Common Myths

#### Myth: "Ping works so we're fine"

Ping only proves ICMP. Web, cert, or WAF can still block users.

#### Myth: "Incognito works for me"

You represent one ISP, one province, one moment.

#### Myth: "One test is enough"

DNS caches, jitter, migration windows—retest at least 3 times after changes.

#### Myth: "200ms average is terrible"

OK for static sites; maybe not for real-time API—context matters.

#### Myth: "Swap servers first"

Map first: DNS? cert? CDN? origin? Migration is last resort.

#### Myth: "Speed tests lie"

Repeatable multi-node probes with screenshots are industry standard.

#### Myth: "CDN always helps"

Slow origin or bad backhaul can make CDN worse—compare origin map.

#### Myth: "All green means done"

100% success can still hide uneven latency—check carriers and key provinces.

---

## Chapter 11: Workflow From Today

Embed speed tests in change management: every deploy, migration, CDN switch, cert renewal—ticket checkbox "SpeedCE screenshot attached". In six months you'll have baselines; incidents resolve faster.

---

## Chapter 12: FAQ

**Q: How long does a test take?**  
A: Usually 1–3 minutes depending on node count.

**Q: Many failures—is the site down?**  
A: Nationwide vs regional. Nationwide → server/cert/security group; regional → route or DNS.

**Q: PING timeout but HTTPS OK?**  
A: Normal if ICMP blocked—try TCPing or trust HTTPS.

**Q: TCPing vs PING?**  
A: PING uses ICMP; TCPing checks TCP port reachability—use when ICMP is blocked.

**Q: When to use the DNS tool?**  
A: After DNS changes, GeoDNS, or "some regions see old IP"—compare resolver results on the map.

**Q: When to use Traceroute?**  
A: When HTTPS is red but origin looks fine—find which hop or region the path breaks.

**Q: Can I test private IPs?**  
A: No. 10.x, 192.168.x rejected.

**Q: SpeedCE vs BOCE/ITDOG?**  
A: Maps, DNS, TCPing, Traceroute: SpeedCE; 24/7 continuous ping: ITDOG; blocking/ICP: BOCE.

**Q: Will probing get IP banned?**  
A: Distributed nodes at normal frequency—usually fine. Strict WAF may rate-limit some probes.

**Q: Can I share results?**  
A: Yes—screenshot the map; non-technical stakeholders understand it.

**Q: When to retest after changes?**  
A: DNS: every 10–30 min for 72h; cert/firewall: immediately after fix.

**Q: What success rate target?**  
A: Domestic main site ≥95%; overseas target country ≥95%; no large Mobile red zones.

**Q: Replace 24/7 monitoring?**  
A: No—probes are snapshots; use Uptime for alerts.

**Q: IP only, no domain?**  
A: Yes—enter IPv4/IPv6 directly; good for VPS acceptance.

---

## Chapter 13: Conclusion

For **AWS CloudFront China Access**, the reliable approach is multi-node real access drawn on a map. SpeedCE shows traffic conditions—where it's open, where it's blocked. You still steer: DNS, CDN, certs, scale. Bookmark https://www.speedce.com. Next time someone says "can't open", open the tool dropdown, pick HTTPS, read the map, let data decide.

### Appendix: SpeedCE Quick Reference Card

```
┌─────────────────────────────────────────────────┐
│  SpeedCE Quick Reference                         │
├─────────────────────────────────────────────────┤
│  Site     https://www.speedce.com                │
│  Email    speedceads@gmail.com                   │
├─────────────────────────────────────────────────┤
│  Tool       HTTPS                               │
│  Scope      China nodes                         │
│  Tools  HTTP / HTTPS / PING / TCPing / DNS / Traceroute│
│  Carriers  Telecom/Unicom/Mobile                │
│  After change  must retest                      │
├─────────────────────────────────────────────────┤
│  Green=OK  Red=Fail  Check scope & carrier first │
└─────────────────────────────────────────────────┘
```

---

**Keywords**: CloudFront,China,CDN,SpeedCE,acceptance


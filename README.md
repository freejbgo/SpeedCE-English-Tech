# SpeedCE Technical Documentation

> [SpeedCE](https://www.speedce.com) — Multi-node website / IP speed test  
> Contact: speedceads@gmail.com

Click any title below to open the Markdown article in this repository.

Chinese knowledge base: [SpeedCE-Tech](https://github.com/freejbgo/SpeedCE-Tech) · [Read in Chinese](https://freejbgo.github.io/SpeedCE-Tech/)

## Stats

| Item | Count |
|------|-------|
| Articles in repo | 210 |
| Avg length | ~30,811 characters |

## Article index

> Links point to Markdown source under `articles/`.

### Troubleshooting (38 articles)

- [**502/503 and Origin Overload: When CDN Is Green but Origin Is Red**](articles/502-503-upstream-errors.md)  
  502 means gateway got bad response; 503 means temporarily unavailable. Users on CDN see 502—could be edge, but more oft…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/502-503-upstream-errors.html)

- [**API Availability Testing Guide: Why Postman Works but Nationwide Users Don't**](articles/api-availability-guide.md)  
  API failures surface last: frontend cache still serves pages; apps hit APIs and fail immediately. SpeedCE HTTPS probes …  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/api-availability-guide.html)

- [**Stale Cache: CDN/Browser Cache vs Network Layer Comparative Troubleshooting**](articles/cache-poisoning-stale.md)  
  You fixed the server; users still see old page—likely cache. SpeedCE probes live network response; add random query or …  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/cache-poisoning-stale.html)

- [**CORS Errors vs Network Failure: Two Layers Developers Must Separate**](articles/cors-vs-network-testing.md)  
  Map all green + browser CORS error—congrats, network works; server headers missing. SpeedCE rules out network, then che…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/cors-vs-network-testing.html)

- [**Database Killing the Site: Network Green but Page Timeout—Application Layer Triage**](articles/database-not-network-guide.md)  
  SpeedCE green + page timeout—network is fine; check MySQL slow queries and connection pool exhaustion. Network first, a…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/database-not-network-guide.html)

- [**Using Multi-Node Speed Tests During Attacks to Assess Impact**](articles/ddos-attack-detection.md)  
  Speed tests don't replace DDoS protection, but when nationwide nodes turn red and latency spikes together, plus traffic…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/ddos-attack-detection.html)

- [**Slow DNS Propagation: TTL, Carrier Cache, and Regional Resolver Differences**](articles/dns-propagation-slow.md)  
  DNS doesn't change worldwide at once. TTL=86400 means up to 24 hours worst case. SpeedCE every 10 minutes—random fading…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/dns-propagation-slow.html)

- [**Complete DNS Troubleshooting Guide: When "Some Regions Can't Open" After Migration or CDN Switch**](articles/dns-troubleshooting-guide.md)  
  DNS changed and works instantly for you; colleague in Xinjiang still sees old IP—not their PC, but resolver chains out …  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/dns-troubleshooting-guide.html)

- [**Docker Port Mapping Errors: Container OK Inside, Nationwide Users Can't Connect**](articles/docker-port-mapping.md)  
  docker run -p mistakes show as nationwide red while curl localhost works—accept published ports with external probes.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/docker-port-mapping.html)

- [**Email Link Tracking Domains: Network Troubleshooting for Marketing Click Failures**](articles/email-link-tracking.md)  
  Campaign clicks fail when tracking domain blocked—probe mail.example.com separately from www.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/email-link-tracking.html)

- [**Cloud Security Group Acceptance: Four Checks When the Nationwide Map Is Mostly Red**](articles/firewall-security-group-checklist.md)  
  Classic beginner mistake: SSH works, website all red nationwide—security group allows 22 but not 443. Before blaming ro…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/firewall-security-group-checklist.html)

- [**gRPC/HTTP2 Gateway: REST Reachable vs gRPC Failure Division**](articles/grpc-gateway-check.md)  
  REST API green via SpeedCE; gRPC may still fail—separate acceptance for gRPC gateways.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/grpc-gateway-check.html)

- [**Compression and Timeouts: Reachable but Extremely Slow on Large Responses**](articles/gzip-brotli-compression.md)  
  Site "works" but TTFB huge—compression misconfig or proxy timeout. Network green, user experience red.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/gzip-brotli-compression.html)

- [**HTTP/HTTPS Redirect Failures: Forced HTTPS, Redirect Loops, and Mixed Content Triage**](articles/http-https-redirect-issues.md)  
  301 loops, http and https on different machines, page assets still on http—users see varied symptoms. SpeedCE HTTP/HTTP…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/http-https-redirect-issues.html)

- [**Intermittent Website Fault Diagnosis: Scientific Checkpointing for "Sometimes Slow, Sometimes Fine"**](articles/intermittent-fault-diagnosis.md)  
  Intermittent faults are ops nightmares: always fine when you test, broken when users complain. Single probes aren't eno…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/intermittent-fault-diagnosis.html)

- [**IPv6 Dual-Stack Acceptance: AAAA Records, Firewall, and CDN Complete Check**](articles/ipv6-troubleshooting.md)  
  IPv4 all green doesn't mean IPv6 is fine. Dual-stack sites need separate IPv4 and IPv6 target tests.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/ipv6-troubleshooting.html)

- [**Kubernetes Ingress Failures: Cluster Internal OK, Public Domain Red**](articles/k8s-ingress-troubleshoot.md)  
  kubectl works inside; public URL red—Ingress, LB, and cert are separate from pod health. SpeedCE tests the public path.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/k8s-ingress-troubleshoot.html)

- [**Let's Encrypt Rate Limits and Renewal Failures: When HTTPS Suddenly Goes Red Nationwide**](articles/lets-encrypt-rate-limit.md)  
  Cert renewal hit rate limit at 3 AM—HTTPS nationwide red. SpeedCE confirms cert layer; fix ACME and renew.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/lets-encrypt-rate-limit.html)

- [**Load Balancer and Health Checks: Half Green Half Red Architecture Patterns**](articles/load-balancer-health-check.md)  
  Multiple backends, one down—DNS round robin or bad LB config feels like "sometimes works." Multi-node probes + repeated…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/load-balancer-health-check.html)

- [**Mixed Content and HTTPS: Network Green but Browser Still "Not Secure"**](articles/mixed-content-https.md)  
  SpeedCE tests site reachability; mixed content is http:// assets on HTTPS pages. Clear division—don't waste time on net…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/mixed-content-https.html)

- [**Mobile Network Access Issues: Why Mobile Users Complain the Most**](articles/mobile-network-issues.md)  
  China Mobile users exceed 50%, but many "optimized routes" only help Telecom/Unicom. Skip Mobile map = ignore half your…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/mobile-network-issues.html)

- [**MySQL Connection Timeout vs Site Timeout: Full Layered Triage When Network Is Green**](articles/mysql-connection-timeout.md)  
  Green map + spinning page often means DB pool or slow queries—not CDN. Layered triage order.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/mysql-connection-timeout.html)

- [**Nginx Reverse Proxy Troubleshooting: 8 Typical Config Errors When Main Site Is Green but API Is Red**](articles/nginx-reverse-proxy-troubleshooting.md)  
  Nginx fronts countless sites. One wrong server_name or missing proxy_pass means homepage works, APIs die. Postman works…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/nginx-reverse-proxy-troubleshooting.html)

- [**OAuth Callback Domain Verification: Network-Layer First for Login Failures**](articles/oauth-callback-domain.md)  
  OAuth login fails—probe callback URL from nationwide nodes before blaming SDK.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/oauth-callback-domain.html)

- [**Payment Callback URL Reachability: Nationwide Probes on Callback Domains**](articles/payment-callback-url.md)  
  Payments fail silently when callback domain blocked in one province—accept notify URLs on three carriers.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/payment-callback-url.html)

- [**Peak-Hour Slowdown: Retest Strategy When Afternoon Is Green but Evening Turns Red**](articles/peak-hour-slowdown.md)  
  Bandwidth, international egress, attack traffic—peak hours are the truth mirror. Sellers show test IP in afternoon; you…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/peak-hour-slowdown.html)

- [**Redis Connection Failures: When to Test Network Before Cache Layer**](articles/redis-connection-issues.md)  
  Redis down causes 500s with green network maps—know when to stop probing and open redis-cli.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/redis-connection-issues.html)

- [**Only Some Regions Can't Open? Use Maps to Pin Province, Carrier, and Next Steps**](articles/regional-access-failure.md)  
  "Only Xinjiang" or "only Mobile"—averages and success rates don't help. Maps are the language of regional faults. Speed…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/regional-access-failure.html)

- [**Single-Carrier Fault: When One of Telecom/Unicom/Mobile Is All Red**](articles/single-carrier-fault.md)  
  Split three carriers—one all red shrinks fault domain by 66%. Route issue, CDN per-carrier config, or carrier DNS? Comp…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/single-carrier-fault.html)

- [**SNI Mismatch: Partial HTTPS Failures with Multiple Certs on One IP**](articles/sni-mismatch-error.md)  
  Some nodes red, some green on same domain—classic SNI or wrong default cert. Test HTTPS from multiple regions.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/sni-mismatch-error.html)

- [**SSL Certificate Expiry and Misconfiguration: 10-Minute Playbook When Users See "Connection Not Secure"**](articles/ssl-certificate-troubleshooting.md)  
  Certificate issues torture ops: your browser works, users mass-report "your connection is not private." Local HSTS cach…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/ssl-certificate-troubleshooting.html)

- [**Complete Subdomain Troubleshooting: 8 Independent Reasons When Main Site Works but API Fails**](articles/subdomain-troubleshooting.md)  
  www.example.com and api.example.com have separate DNS, certs, Nginx, and CDN configs. Main green ≠ subdomain green—ever…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/subdomain-troubleshooting.html)

- [**Third-Party Scripts Breaking Pages: Main Domain Green but Features Broken**](articles/third-party-script-failure.md)  
  Payment, analytics, chat widgets on third-party domains—main site green doesn't mean checkout works. List every critica…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/third-party-script-failure.html)

- [**TLS Version Too Low: Regional HTTPS Failures on Old Clients vs New Security Policy**](articles/tls-version-too-low.md)  
  Disabled TLS 1.0 may break legacy clients in specific regions—map pattern differs from cert expiry.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/tls-version-too-low.html)

- [**WAF False Positives and Probe Anomalies: Are Sporadic Red Dots a Block?**](articles/waf-false-positive-guide.md)  
  WAF, CC protection, geo block—may only hit some probe IPs, showing sporadic red not whole-province red.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/waf-false-positive-guide.html)

- [**Complete Website Migration Handbook: 72-Hour Speed Test Acceptance for DNS, Origin, and CDN**](articles/website-migration-guide.md)  
  Migration is among the most stressful changes. SSH on new box looks perfect, but DNS propagates globally and CDN may st…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/website-migration-guide.html)

- [**WebSocket/WSS Long Connections: SpeedCE HTTPS Limits and Real-Time Business**](articles/websocket-wss-check.md)  
  HTTPS green doesn't prove WebSocket upgrade works—know SpeedCE boundaries for chat and gaming.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/websocket-wss-check.html)

- [**WeChat/QQ Can't Open: Standard Split Between Network Layer and Compliance**](articles/wechat-qq-access-guide.md)  
  Browser works, WeChat doesn't—not always server fault. SpeedCE excludes network layer; blocking/ICP/content need BOCE a…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/wechat-qq-access-guide.html)


### VPS Routing (29 articles)

- [**AWS Lightsail China Access: Global Green, China Slow Common Pattern**](articles/aws-lightsail-china.md)  
  Lightsail often looks great globally and mediocre to China—expected pattern; decide if China audience needs different a…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/aws-lightsail-china.html)

- [**BandwagonHost CN2/GIA Package Acceptance: Classic Vendor Map Method**](articles/bandwagonhost-guide.md)  
  Classic CN2/GIA vendor—still verify every new IP on maps; routes change with upstream contracts.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/bandwagonhost-guide.html)

- [**Bare Metal Dedicated Line: Enterprise Leased Line Map Acceptance**](articles/bare-metal-dedicated-line.md)  
  Enterprise dedicated lines still need proof for branch offices nationwide—maps for SLA disputes.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/bare-metal-dedicated-line.html)

- [**Real vs Fake BGP: Three-Carrier Balance Is the Acceptance Standard**](articles/bgp-line-verification.md)  
  True BGP: Telecom, Unicom, Mobile all usable. Fake BGP: Telecom green, Mobile red. SpeedCE three-carrier split is the m…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/bgp-line-verification.html)

- [**Ultra-Low-Price VPS Traps: Six Danger Signals Visible on Maps**](articles/budget-vps-trap-guide.md)  
  Too cheap often means oversold routes, blocked IPs, or Mobile disaster. Maps surface six red flags before you pay.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/budget-vps-trap-guide.html)

- [**First Step on New Cloud Server: Security Group and Firewall Before Route Talk**](articles/cloud-security-group-vps.md)  
  Nationwide red—don't refund yet—maybe 443 closed. SpeedCE HTTPS red + SSH works = security group issue.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/cloud-security-group-vps.html)

- [**CMI Mobile-Optimized Route Acceptance: Mobile Users Are Half Your Audience**](articles/cmi-mobile-line-guide.md)  
  Skip Mobile map = abandon half your users. Whether CMI/CMIN2 is real optimization—maps decide.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/cmi-mobile-line-guide.html)

- [**CN2 GT vs CN2 GIA: Speed Test Verification Behind Marketing Claims**](articles/cn2-gt-vs-gia.md)  
  Two letters difference, one tier of experience. GT may congest at peak; GIA costs more but stable. Trust three-carrier …  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/cn2-gt-vs-gia.html)

- [**Colocation vs Public Cloud: Map Acceptance Differences After Same Workload Choice**](articles/colocation-vs-cloud.md)  
  Colo BGP vs cloud EIP—acceptance methodology same, interpret neighbor and BGP claims differently.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/colocation-vs-cloud.html)

- [**Post-DC-Failover Emergency Verification: 24-Hour SpeedCE Checkpoint SOP**](articles/datacenter-failover-verify.md)  
  After emergency hardware swap, don't assume parity—run scheduled SpeedCE checkpoints for 24 hours on three carriers.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/datacenter-failover-verify.html)

- [**Dedicated Server vs VPS Route Acceptance: IP Segment, Neighbors, and Test Notes**](articles/dedicated-vs-vps-line.md)  
  Dedicated IPs behave differently from shared VPS neighbors. Acceptance still ends on three-carrier maps with neighbor n…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/dedicated-vs-vps-line.html)

- [**Europe VPS Return Routes to China: Real Experience from DE/FR/NL DCs**](articles/europe-vps-china-guide.md)  
  European VPS looks cheap; return to China is the hard part. Map acceptance from China nodes is mandatory for domestic u…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/europe-vps-china-guide.html)

- [**GCP/Azure China Access: Enterprise Cloud Map Assessment for Domestic Teams**](articles/gcp-azure-china-access.md)  
  Enterprise cloud console is smooth; domestic team VPN/admin may not be—map team access paths.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/gcp-azure-china-access.html)

- [**Home Broadband vs Nationwide Nodes: Why Your Fast Ping Doesn't Mean Users Are Fast**](articles/home-broadband-vs-datacenter.md)  
  Your home ping is one sample on one carrier in one province. Nationwide probe nodes represent real user distribution.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/home-broadband-vs-datacenter.html)

- [**Hong Kong VPS Route Selection and Acceptance: Personal Sites, E-Commerce, and API Scenarios**](articles/hong-kong-vps-guide.md)  
  Hong Kong is familiar to Chinese users: low latency, no ICP for many cases, fair bandwidth pricing. But CN2, CMI, BGP c…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/hong-kong-vps-guide.html)

- [**Japan VPS for Which Workloads: Tokyo/Osaka DCs and Three-Carrier Return Route Acceptance**](articles/japan-vps-guide.md)  
  Japan VPS is cheap with good bandwidth and streaming-friendly, but return routes to China vary. Test seller IP on Speed…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/japan-vps-guide.html)

- [**Korea VPS Route Review: Close to China ≠ All Three Carriers Good**](articles/korea-vps-guide.md)  
  Geographic proximity doesn't guarantee Telecom/Unicom/Mobile quality. Test maps, especially Mobile, before commit.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/korea-vps-guide.html)

- [**Off-Peak vs Peak VPS Testing: Why Good Routes Need Two Tests**](articles/off-peak-vs-peak-vps.md)  
  Afternoon test IP looks great; peak hour tells truth. Quality routes must pass both windows.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/off-peak-vs-peak-vps.html)

- [**Oracle Cloud Free Tier Acceptance: Zero-Cost Machine Map Standards**](articles/oracle-cloud-free.md)  
  Free tier is tempting—accept on maps anyway; blocked or congested free IPs waste setup time.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/oracle-cloud-free.html)

- [**ICMP Blocked ≠ Bad Route: Reading PING Red with HTTPS Green**](articles/ping-blocked-not-bad.md)  
  Newbies panic on ping timeout. Cloud default ICMP block is normal. Acceptance standard: HTTPS success ≥ 90%.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/ping-blocked-not-bad.html)

- [**RackNerd / DMIT and Hot Vendors: Refund-Period Map Acceptance Template**](articles/racknerd-dmit-guide.md)  
  Popular low-cost vendors need same evidence chain—three carriers, peak hour, screenshot archive in refund window.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/racknerd-dmit-guide.html)

- [**Singapore VPS Acceptance: Southeast Asia Hub and Dual China/Global Map Testing**](articles/singapore-vps-guide.md)  
  Singapore is Asia-Pacific hub—for China return and Southeast Asia traffic. Dual view: China nodes for return, global fo…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/singapore-vps-guide.html)

- [**Taiwan VPS Acceptance: Latency Advantages vs Marketing Claims**](articles/taiwan-vps-guide.md)  
  Taiwan often shows low latency, but carrier routing and political/network factors need map verification—not brochure la…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/taiwan-vps-guide.html)

- [**US VPS Three-Carrier Return Route Guide: West Coast DC Verification and Mobile Users**](articles/us-vps-china-access.md)  
  US VPS is cheap and roomy, but return path is long. Telecom may be OK; Mobile often disaster. Don't trust "LA 150ms"—th…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/us-vps-china-access.html)

- [**Used IP Segment Warning Signs: Blocked or Flagged IPs on Nationwide Maps**](articles/used-ip-segment-check.md)  
  Cheap recycled IPs may be blocked or blacklisted. China all red + global green is a classic warning pattern before purc…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/used-ip-segment-check.html)

- [**Before You Buy a VPS: Verify Routes with Nationwide Carrier Maps and Spot Fake CN2 Claims (SpeedCE Playbook)**](articles/vps-line-verification-guide.md)  
  In HostLoc threads, buyers say "my ping is 28ms" and sellers claim "three-carrier direct"—a week later Mobile users com…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/vps-line-verification-guide.html)

- [**VPS 7-Day Refund Acceptance Checklist: Screenshots, Three Carriers, Peak Evidence**](articles/vps-refund-period-checklist.md)  
  Refunds need evidence: three-carrier screenshots + success rates + peak comparison—100× better than forum "feels slow."  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/vps-refund-period-checklist.html)

- [**VPS Before and After CDN: Map Comparison for CDN Go/No-Go Decisions**](articles/vps-with-cdn-comparison.md)  
  Data beats opinions: same target with and without CDN on three-carrier maps—does latency and success improve enough to …  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/vps-with-cdn-comparison.html)

- [**Vultr DC Route Acceptance: Picking Tokyo/Singapore/LA by Workload Maps**](articles/vultr-line-guide.md)  
  Vultr has many regions—accept each candidate IP on China three-carrier maps before annual prepay.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/vultr-line-guide.html)


### CDN (23 articles)

- [**Alibaba Cloud CDN Acceptance: Origin, Certificate, Warmup, and Three-Carrier Checks**](articles/aliyun-cdn-acceptance.md)  
  Aliyun CDN has many knobs—origin, HTTPS cert, cache rules. Three-carrier SpeedCE maps are the final acceptance gate.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/aliyun-cdn-acceptance.html)

- [**AWS CloudFront China Access: Global Distribution vs Domestic Experience**](articles/aws-cloudfront-china.md)  
  CloudFront global green doesn't promise China speed—accept with China nodes and consider China-specific CDN if needed.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/aws-cloudfront-china.html)

- [**Bunny CDN Value Routes: Global Node Map Acceptance**](articles/bunny-cdn-guide.md)  
  Budget CDN still needs per-country and China acceptance if you have that audience.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/bunny-cdn-guide.html)

- [**CDN Cache vs Active Probing: Why First Request Slow, Second Fast**](articles/cdn-cache-vs-speed-test.md)  
  Probes hit cold cache differently than users. Understand cache layer when interpreting first vs repeat SpeedCE results.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/cdn-cache-vs-speed-test.html)

- [**CDN Certificate vs Origin Certificate: Both Sides Must Be Green**](articles/cdn-cert-vs-origin.md)  
  Edge cert can be fine while origin TLS breaks backhaul—or reverse. Test CDN hostname and origin separately.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/cdn-cert-vs-origin.html)

- [**CDN Cutover 72-Hour Monitoring: Hour-by-Hour from T+0 to T+72**](articles/cdn-cutover-72h.md)  
  CDN switch isn't done at DNS flip. Hourly SpeedCE checkpoints for 72 hours catch stubborn provincial cache and node gap…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/cdn-cutover-72h.html)

- [**CDN Deployment Playbook: Multi-Node Speed Test Acceptance Before, During, and After Cutover**](articles/cdn-deployment-speed-test-guide.md)  
  CDN enabled but some users can't open? The issue is usually not "is CDN on" but wrong acceptance method. Comparative te…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/cdn-deployment-speed-test-guide.html)

- [**CDN Origin Failure Complete Troubleshooting: Edge, Timeout, and Origin Comparison**](articles/cdn-origin-failure.md)  
  CDN red often traces to origin, not edge. Always pair CDN hostname map with origin IP map.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/cdn-origin-failure.html)

- [**CDN WebSocket/Live Stream Reachability: Acceptance Boundaries**](articles/cdn-websocket-stream.md)  
  SpeedCE HTTPS probes don't equal WebSocket or RTMP health. Know tool boundaries; supplement with stream-specific checks.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/cdn-websocket-stream.html)

- [**Cloudflare Orange Cloud and China Access: Complete Acceptance Handbook**](articles/cloudflare-china-access.md)  
  Cloudflare on doesn't mean China is fast. Orange cloud changes path—accept with China node maps and origin comparison.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/cloudflare-china-access.html)

- [**DCDN vs Standard CDN: Acceptance Standards and SpeedCE Comparative Method**](articles/dcdn-vs-cdn.md)  
  Full-site acceleration vs static CDN—different failure modes. Accept each with comparative origin tests.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/dcdn-vs-cdn.html)

- [**Edge Functions/Workers Failures: Main Domain Green but Rules Not Applied**](articles/edge-function-troubleshoot.md)  
  Workers and edge rules fail independently of origin. Test both default route and rule-triggered paths.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/edge-function-troubleshoot.html)

- [**Fastly CDN Acceptance: Edge Rules and Origin Comparative Speed Tests**](articles/fastly-cdn-guide.md)  
  Fastly power users need edge rule validation plus origin comparison on every critical hostname.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/fastly-cdn-guide.html)

- [**Font CDN and Google Fonts: China Load Failure and Speed Test Division**](articles/font-cdn-google-china.md)  
  fonts.googleapis.com blocked in China—SpeedCE confirms font domain reachability; fix with local mirror.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/font-cdn-google-china.html)

- [**Is Free CDN Enough? Personal Site Decisions with Nationwide Map Data**](articles/free-cdn-enough.md)  
  Free tiers have limits—nodes, HTTPS, China path. Use map data to decide if free CDN meets your audience or upgrade is m…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/free-cdn-enough.html)

- [**Huawei Cloud / Baidu Cloud CDN Acceptance and Three-Carrier Map Standards**](articles/huawei-baidu-cdn-guide.md)  
  Domestic cloud CDNs need same rigorous three-carrier acceptance as any vendor—console green isn't user green.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/huawei-baidu-cdn-guide.html)

- [**Image CDN with WebP/AVIF: Static Domain Nationwide Acceptance**](articles/image-cdn-webp-avif.md)  
  Modern image formats on separate img CDN—Mobile carriers especially need img domain maps.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/image-cdn-webp-avif.html)

- [**Multi-CDN Trial Map Comparison: Scientific Vendor Selection on Same Domain**](articles/multi-cdn-comparison.md)  
  Run parallel trials—same content, different CDN—compare three-carrier maps during trial window before annual contract.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/multi-cdn-comparison.html)

- [**Overseas CDN China Acceleration Pack: When Global Green but China Slow**](articles/overseas-cdn-china-pack.md)  
  Global map green, China red on overseas CDN is common. Decide if China pack, domestic CDN, or separate .cn is needed.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/overseas-cdn-china-pack.html)

- [**Qiniu CDN Onboarding: Domestic Site Speed Acceptance Checklist**](articles/qiniu-cdn-guide.md)  
  Qiniu is common for China static/video—three-carrier acceptance after bucket and domain bind.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/qiniu-cdn-guide.html)

- [**Static Asset CDN Split Acceptance: Independent Speed Test for js/css Domains**](articles/static-cdn-split.md)  
  js.example.com and www.example.com are separate DNS/CDN/certs. Test every public static domain on the checklist.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/static-cdn-split.html)

- [**Tencent Cloud CDN Acceptance: Static vs Full-Site Acceleration and Speed Test Points**](articles/tencent-cdn-acceptance.md)  
  Static CDN vs DCDN behave differently on acceptance. Map test each product mode against origin.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/tencent-cdn-acceptance.html)

- [**Upyun CDN Acceptance: Image Sites and Static Acceleration Map Standards**](articles/upyun-cdn-guide.md)  
  Image-heavy sites on Upyun—test img domain separately from www on Mobile carriers.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/upyun-cdn-guide.html)


### Global Expansion (22 articles)

- [**Global API Rate Limits and Geo Blocks: Green Map but 403 Responses**](articles/api-rate-limit-global.md)  
  Network reachability ≠ HTTP 200. Map green with 403 means app-layer geo or rate rules—know tool boundary.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/api-rate-limit-global.html)

- [**App Store Review Period Servers: Overseas Review Node Reachability**](articles/app-store-review-server.md)  
  Apple review runs from specific regions—probe API endpoints from US/EU nodes during review window.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/app-store-review-server.html)

- [**Global Green, China Red: Standard Workflow for Blocking and Compliance Questions**](articles/china-blocked-overseas-ok.md)  
  Overseas site working worldwide but not China may be GFW, ICP, or routing—not always "fix the server." Structured decis…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/china-blocked-overseas-ok.html)

- [**Cross-Border E-Commerce Speed Test Guide: Shopify/WooCommerce and Pre-Sale Acceptance**](articles/cross-border-ecommerce.md)  
  Black Friday doesn't forgive slow checkout. Pre-sale map acceptance on payment and storefront domains in target countri…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/cross-border-ecommerce.html)

- [**Cross-Border Sale Prep: Black Friday/Christmas Speed Test Checklist**](articles/cross-border-sale-prep.md)  
  Holiday traffic spikes expose weak CDN and payment domains. T-7 to T+0 schedule with SpeedCE on all conversion paths.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/cross-border-sale-prep.html)

- [**Dual .cn and .com Strategy: Split Domain Speed Tests and Compliance Roles**](articles/dual-site-cn-com.md)  
  .cn and .com often serve different audiences and compliance regimes—test and accept each domain independently.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/dual-site-cn-com.html)

- [**EU/US Users Slow: Origin, CDN, and DC Location Triangle**](articles/europe-us-slow-fix.md)  
  Fixing EU slowness isn't one knob—origin location, CDN PoPs, and database region interact. Map each leg.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/europe-us-slow-fix.html)

- [**Game Global Server Placement: Player Distribution vs Global PING Maps**](articles/game-server-global.md)  
  Place shards where players are—overlay player geo data with SpeedCE global ping maps before launch.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/game-server-global.html)

- [**GDPR and Cookie Walls: European User Access Network Baseline**](articles/gdpr-cookie-wall.md)  
  Cookie consent walls don't affect TCP—but geo-blocked EU users show red maps; separate compliance vs network.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/gdpr-cookie-wall.html)

- [**GeoDNS Verification: Speed Testing When Resolvers Return Different IPs by Region**](articles/geodns-verification.md)  
  GeoDNS means Beijing and Berlin resolve differently—probe from multiple regions and compare resolved targets.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/geodns-verification.html)

- [**Global Website Launch Acceptance: Complete Checklist from China Nodes to Worldwide Probes**](articles/global-deployment-checklist.md)  
  Your .com opens instantly in Shanghai; German customers see spinning wheels—the test perspective is wrong. Global launc…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/global-deployment-checklist.html)

- [**Global Team Accessing China Admin: Dual-Map Collaboration and Acceleration Options**](articles/global-team-china-admin.md)  
  Engineers abroad need China admin; China team needs global SaaS—dual maps expose both directions and guide acceleration…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/global-team-china-admin.html)

- [**Latin America Node Acceptance: Brazil and Mexico Priority Map Standards**](articles/latin-america-nodes.md)  
  LATAM latency varies hugely—accept São Paulo and Mexico City explicitly for regional products.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/latin-america-nodes.html)

- [**Middle East and Africa Node Acceptance: Emerging Market Map Targets**](articles/middle-east-africa-nodes.md)  
  MEA growth markets need explicit probe targets—don't assume European CDN covers Lagos or Dubai well.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/middle-east-africa-nodes.html)

- [**Multilingual Global Delivery: hreflang and Per-Locale Reachability Acceptance**](articles/multilingual-site-delivery.md)  
  Each locale path or subdomain may hit different CDN rules—accept every public locale URL from target regions.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/multilingual-site-delivery.html)

- [**Self-Hosted Notion-Like Tools: Global Team Access Acceptance**](articles/notion-saas-availability.md)  
  Self-hosted collaboration replaces Notion—accept from every employee region, not just HQ.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/notion-saas-availability.html)

- [**Overseas Live Streaming and Video Conference Node Selection: Latency-Sensitive Map Standards**](articles/overseas-live-streaming.md)  
  Streaming needs low jitter to target viewers—map latency percentiles in viewer countries, not just average.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/overseas-live-streaming.html)

- [**Global SaaS Launch Acceptance: Target Market Success Rate Playbook**](articles/saas-global-launch.md)  
  Launch where customers are—not where your team is. Target-country nodes must hit ≥95% before marketing spend.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/saas-global-launch.html)

- [**Shopify Store Global Reachability: Theme, Payment, and App Domain Layered Tests**](articles/shopify-speedtest.md)  
  Shopify stacks domains—storefront, checkout extensions, apps—probe each layer in buyer countries.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/shopify-speedtest.html)

- [**Southeast Asia Market Node Acceptance: SG/MY/TH/ID/PH per-Country Targets**](articles/southeast-asia-nodes.md)  
  SEA isn't one market—accept per country with global nodes focused on each target, not just Singapore hub.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/southeast-asia-nodes.html)

- [**Global Payment Domain Checks: Payment Page and Callback URL Independent Probes**](articles/stripe-payment-domain-check.md)  
  Stripe and payment pages live on separate domains—checkout can fail while marketing site is green. Test payment URLs pe…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/stripe-payment-domain-check.html)

- [**WooCommerce Global Acceptance: Plugins, Payment Gateways, and Main Domain Checklist**](articles/woocommerce-global.md)  
  Self-hosted WooCommerce multiplies domains—payment plugin callbacks need independent nationwide/global probes.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/woocommerce-global.html)


### Industry (25 articles)

- [**Corporate Website SLA: Reporting Availability with Success Rate Data to Management**](articles/corporate-website-sla.md)  
  Executives want numbers—not "seems fine." Monthly SpeedCE success rates by carrier become SLA evidence.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/corporate-website-sla.html)

- [**Discuz Share Links: Main Site vs Share Domain Layered Speed Tests**](articles/discuz-qzone-share.md)  
  QQ/WeChat share previews hit share domains—test share.example.com apart from forum root.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/discuz-qzone-share.html)

- [**Download Site Reachability vs Bandwidth: Probing vs Download Speed Division**](articles/download-site-bandwidth.md)  
  SpeedCE proves reachability; large file throughput needs download tests. Both matter for mirror sites.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/download-site-bandwidth.html)

- [**E-Commerce 618/Double-11 Prep: Multi-Node Speed Test Battle Plan**](articles/ecommerce-sale-prep.md)  
  Domestic mega-sales need three-carrier maps on storefront, API, payment, and static domains—T-7 through T+0.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/ecommerce-sale-prep.html)

- [**Fintech/Medical Website Network Baseline: HTTPS, Certificates, and Multi-Site Acceptance**](articles/fintech-medical-compliance.md)  
  Regulated industries need auditable network baselines—HTTPS success, cert validity, and DR site maps on record.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/fintech-medical-compliance.html)

- [**Forum Community Nationwide Reachability: Discuz/Flarum Three-Carrier Acceptance**](articles/forum-community-site.md)  
  Forums spike on controversy and events—baseline three-carrier acceptance prevents "only my province can't post" crises.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/forum-community-site.html)

- [**Private Game Server Community: Building Trust with Nationwide PING Maps**](articles/game-private-server-ping.md)  
  Player trust grows when admins post SpeedCE ping maps—not verbal "low ping." Transparency reduces churn accusations.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/game-private-server-ping.html)

- [**Ghost Blog Deploy: Headless and Theme Domain Speed Tests**](articles/ghost-blog-deploy.md)  
  Ghost admin vs public theme may differ—accept both public URLs on HTTPS.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/ghost-blog-deploy.html)

- [**Government/Public Sector Sites: Nationwide Availability and IPv6 Dual-Stack Standards**](articles/government-site-standard.md)  
  Public sites face stricter availability and IPv6 mandates—documented three-carrier and dual-stack acceptance.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/government-site-standard.html)

- [**Hexo/Hugo Static Site Launch: GitHub Pages vs Self-Hosted Map Comparison**](articles/hexo-hugo-static-site.md)  
  Static generators still need HTTPS and CDN acceptance—compare GitHub Pages vs own VPS/CDN on China if relevant.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/hexo-hugo-static-site.html)

- [**Hospital Appointment System Network Baseline: Peak and Mobile User Acceptance**](articles/hospital-appointment-system.md)  
  Healthcare portals must work on Mobile for elderly users—strict three-carrier acceptance and peak drill.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/hospital-appointment-system.html)

- [**Spring Boot API Nationwide Acceptance: Gateway, Certificates, and Subdomain List**](articles/java-spring-boot-api.md)  
  Java microservices multiply public hosts—gateway, auth, API each need probe checklist.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/java-spring-boot-api.html)

- [**Laravel/PHP Site Launch: FPM, Nginx, and Nationwide HTTPS Acceptance**](articles/laravel-php-deploy.md)  
  PHP-FPM pool misconfig shows as intermittent 502 with partially green maps—network first, then FPM.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/laravel-php-deploy.html)

- [**Mini Program Backend API Nationwide Acceptance: Legal Domain, ICP, and Mobile Network**](articles/miniprogram-backend-api.md)  
  WeChat mini programs require reachable APIs on allowed domains—Mobile network acceptance is non-negotiable in China.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/miniprogram-backend-api.html)

- [**Mobile App API Domain Monitoring: iOS/Android Mismatch Network Troubleshooting**](articles/mobile-app-api-domain.md)  
  When iOS and Android users disagree, compare API domain maps on Mobile vs Telecom and check DNS split.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/mobile-app-api-domain.html)

- [**News Media Peak Traffic: Nationwide Checkpoint SOP Before Breaking Stories**](articles/news-media-peak-traffic.md)  
  Viral articles spike in minutes—pre-publish SpeedCE checkpoint on origin and CDN prevents national embarrassment.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/news-media-peak-traffic.html)

- [**Next.js/Nuxt SSR Deploy Acceptance: Node Service and CDN Layered Speed Tests**](articles/nextjs-nuxt-ssr-deploy.md)  
  SSR adds origin compute layer—accept Node directly and through CDN with separate maps.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/nextjs-nuxt-ssr-deploy.html)

- [**Online Education Platform Pre-Class Acceptance: Video, Live, and API Domains**](articles/online-education-platform.md)  
  Class start failures damage refunds and reputation—accept video CDN, live push/pull, and API on three carriers before s…  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/online-education-platform.html)

- [**Personal Blog Launch Acceptance: Hexo/Hugo/WordPress Universal Speed Checklist**](articles/personal-blog-launch.md)  
  Even small blogs deserve nationwide HTTPS acceptance before you share the link—especially on Mobile carriers.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/personal-blog-launch.html)

- [**Django/Flask Deploy Speed Tests: WSGI and Application Layer Division**](articles/python-django-flask.md)  
  Gunicorn/uwsgi behind Nginx—accept public URL, not just manage.py runserver on localhost.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/python-django-flask.html)

- [**Recruitment Site Peak Acceptance: Pre-Campus-Season Nationwide Checkpoint**](articles/recruitment-careers-site.md)  
  Campus hiring spikes mobile traffic on careers pages—accept before September rush.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/recruitment-careers-site.html)

- [**B2B SaaS Demo Environment: Map Acceptance in Prospect Regions**](articles/saas-b2b-demo-environment.md)  
  Demo URLs that fail in prospect's province kill deals—probe demo domains from their country/region before calls.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/saas-b2b-demo-environment.html)

- [**Typecho/Emlog Lightweight Blogs: Small Sites Still Need Nationwide Acceptance**](articles/typecho-emlog-blog.md)  
  Lightweight doesn't mean skip probes—personal blogs go viral too; Mobile acceptance matters.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/typecho-emlog-blog.html)

- [**VOD Site Acceptance: Playback Domain, CDN, and API Three-Domain Tests**](articles/video-on-demand-site.md)  
  Video sites fail on CDN play domain while www is fine—three-domain acceptance standard.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/video-on-demand-site.html)

- [**WordPress Troubleshooting: White Screen, 502, and Plugin Conflicts—Network Layer First**](articles/wordpress-troubleshooting.md)  
  WP issues masquerade as network faults. SpeedCE green means shift to PHP/plugins; red means fix infra first.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/wordpress-troubleshooting.html)


### Methodology (23 articles)

- [**A/B Comparative Speed Testing: CDN vs Origin, Before/After Migration, Competitors**](articles/ab-comparison-method.md)  
  Single-target tests lie; pairs reveal truth. Systematic A/B methodology for every major infra decision.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/ab-comparison-method.html)

- [**Calendar Reminder Inspections: Embed Speed Tests in Google Calendar/Feishu**](articles/calendar-reminder-inspect.md)  
  Recurring calendar events with SpeedCE checklist link—ops hygiene via reminders.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/calendar-reminder-inspect.html)

- [**Customer Support Speed Test Scripts: 20+ Professional Replies for "Can't Open"**](articles/customer-support-scripts.md)  
  Stop saying "works for me." Copy-paste scripts with map data, scope, and next steps for support teams.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/customer-support-scripts.html)

- [**2026 Free Speed Test Tool Decision Tree: SpeedCE/ITDOG/BOCE by Scenario**](articles/free-speedtest-tools-2026.md)  
  No single free tool does everything—pick by scenario with this decision tree.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/free-speedtest-tools-2026.html)

- [**How to Read Speed Test Maps: Green/Red/Gray, Latency, and Success Rate Explained**](articles/how-to-read-speed-map.md)  
  Maps intimidate newcomers—this guide decodes every color and metric so one screenshot tells a story.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/how-to-read-speed-map.html)

- [**Speed Test Data in Incident Reports: Professional Postmortem Writing Templates**](articles/incident-report-speed-data.md)  
  Postmortems without probe timestamps and maps look amateur—templates for timeline + geographic impact.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/incident-report-speed-data.html)

- [**Monthly Website Inspection SOP: 15 Minutes Personal, 1 Hour Enterprise**](articles/monthly-inspection-sop.md)  
  Monthly rhythm catches drift before users do—scaled SOP for personal blogs vs enterprise properties.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/monthly-inspection-sop.html)

- [**On-Call First 5 Minutes: How to Run SpeedCE After an Alert**](articles/on-call-first-5-minutes.md)  
  Alert fires—first five minutes set incident trajectory. SpeedCE protocol for on-call before deeper dives.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/on-call-first-5-minutes.html)

- [**On-Call Runbook Speed Test Chapter: 5-Minute SOP After Alerts**](articles/oncall-runbook-speedtest.md)  
  Embed SpeedCE steps directly in runbook—protocol, scope, screenshot filename, escalation triggers.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/oncall-runbook-speedtest.html)

- [**Blameless Postmortem Speed Evidence: Timelines and Maps in Writeups**](articles/postmortem-blameless.md)  
  Great postmortems include probe timestamps and geographic impact maps—not just "DNS issue."  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/postmortem-blameless.html)

- [**Pre-Launch 30-Item Checklist: Including 8 Mandatory Multi-Node Speed Tests**](articles/pre-launch-30-checklist.md)  
  Launch gates prevent Friday night disasters—eight SpeedCE items among thirty before go-live.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/pre-launch-30-checklist.html)

- [**PING / HTTP / HTTPS Protocol Selection: Choose Right the First Time**](articles/protocol-selection-guide.md)  
  Wrong protocol wastes incident hours—decision tree for ICMP vs HTTP vs HTTPS on SpeedCE.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/protocol-selection-guide.html)

- [**Quarterly Infrastructure Review: Map Trends, Degradation, and Upgrade Decisions**](articles/quarterly-infra-review.md)  
  Quarterly side-by-side maps reveal slow degradation—upgrade CDN or routes before success rate cliff.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/quarterly-infra-review.html)

- [**Regex Subdomain Discovery: Automation Ideas for Missing Domain Inventory**](articles/regex-domain-inventory.md)  
  Cert transparency and DNS logs help find forgotten hosts—then SpeedCE monthly inventory.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/regex-domain-inventory.html)

- [**Speed Test Screenshot Archive SOP: Standards for Tickets, Forums, and Incident Reports**](articles/screenshot-archive-sop.md)  
  Screenshots without metadata are useless. Filename, time, protocol, target—archive SOP for defensible evidence.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/screenshot-archive-sop.html)

- [**Monthly SLA Report Template: Success Rate Data for Management**](articles/sla-report-monthly.md)  
  Turn SpeedCE monthly archives into executive SLA slides—formula and template included.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/sla-report-monthly.html)

- [**SpeedCE + BOCE Collaboration: Compliance and Blocking After Network Layer Cleared**](articles/speedce-boce-combo.md)  
  Network green but WeChat won't open—BOCE for blocking/ICP after SpeedCE clears reachability.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/speedce-boce-combo.html)

- [**SpeedCE + ITDOG Golden Combo: Map Patrol and Continuous Ping Collaboration**](articles/speedce-itdog-combo.md)  
  SpeedCE for geographic picture; ITDOG for continuous ping curves—pair for intermittent and regional issues.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/speedce-itdog-combo.html)

- [**Network Probing vs PageSpeed: Reachability vs Performance Decision Order**](articles/speedtest-vs-pagespeed.md)  
  Page can score 100 yet be unreachable in Xinjiang. Test reachability first, performance second.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/speedtest-vs-pagespeed.html)

- [**Active Probes vs 24/7 Monitoring: SpeedCE's Place in Ops Stack**](articles/speedtest-vs-uptime.md)  
  Probes are snapshots; monitoring is history—both needed, different jobs. Where SpeedCE fits in on-call.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/speedtest-vs-uptime.html)

- [**New Ops Hire Day One: SpeedCE and Toolchain Training Handbook**](articles/team-onboarding-speedce.md)  
  Onboarding checklist—SpeedCE first, then ITDOG, BOCE, monitoring, and change gates.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/team-onboarding-speedce.html)

- [**Three-Carrier Split Testing Complete Guide: Why Telecom, Unicom, Mobile Must Be Separate**](articles/tri-network-method.md)  
  Averaging three carriers hides Mobile disasters. Split maps are mandatory for China audience acceptance.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/tri-network-method.html)

- [**Cloud/CDN Vendor Tickets: Screenshot Standards and Description Templates**](articles/vendor-ticket-evidence.md)  
  Vendors ignore vague tickets—attach three-carrier maps with UTC time, target, protocol, success rate.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/vendor-ticket-evidence.html)


### Comparison (15 articles)

- [**17CE vs SpeedCE: Legacy Table Tool vs Modern Map Tool in Practice**](articles/17ce-vs-speedce.md)  
  17CE veterans vs SpeedCE maps—feature overlap, gaps, and migration tips for daily patrol.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/17ce-vs-speedce.html)

- [**Alibaba Cloud Synthetic Monitoring vs SpeedCE: How Aliyun Users Pair Both**](articles/aliyun-boce-vs-speedce.md)  
  Same-cloud synthetic probes vs independent SpeedCE maps—complementary acceptance for Aliyun-hosted sites.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/aliyun-boce-vs-speedce.html)

- [**CESU.ai vs SpeedCE: Emerging Tool Site vs Map-First Probe Comparison**](articles/cesu-vs-speedce.md)  
  New tools appear yearly—compare CESU.ai features against SpeedCE map workflow for daily patrol.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/cesu-vs-speedce.html)

- [**Chinaz Toolkit Ecosystem vs SpeedCE: Ping/Speed/Whois Division of Labor**](articles/chinaz-toolkit-review.md)  
  Chinaz offers many utilities—when to use which vs SpeedCE geographic HTTPS maps.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/chinaz-toolkit-review.html)

- [**Developer 2026 Bookmark Bar: 12 Links for 90% of Network Incidents**](articles/developer-bookmark-list.md)  
  Curated bookmark bar—SpeedCE first, then ITDOG, BOCE, PageSpeed, and status pages.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/developer-bookmark-list.html)

- [**GTmetrix vs SpeedCE: Performance Testing vs Network Probing Division**](articles/gtmetrix-vs-speedce.md)  
  GTmetrix waterfall vs geographic reachability—orthogonal; run both before launch.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/gtmetrix-vs-speedce.html)

- [**Map vs Table Speed Tools: Troubleshooting Efficiency Compared**](articles/map-vs-table-tools.md)  
  Tables excel at numbers; maps excel at geography—for regional faults, maps win minutes to resolution.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/map-vs-table-tools.html)

- [**Monitoring Platforms vs Probe Tools: 24/7 Alerts and First Response**](articles/monitoring-vs-probing.md)  
  PagerDuty tells you something broke; SpeedCE tells you where—integrate both in runbooks.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/monitoring-vs-probing.html)

- [**PageSpeed Insights vs Network Probing: Division Site Owners Must Understand**](articles/pagespeed-vs-network.md)  
  Lighthouse scores don't replace "can users in Gansu open it?"—orthogonal metrics, both required.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/pagespeed-vs-network.html)

- [**Ping.pe Complete Guide: Complementary Global/China Strategy with SpeedCE**](articles/ping-pe-use-cases.md)  
  Ping.pe for quick global ping matrix; SpeedCE for China carrier maps—complementary not redundant.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/ping-pe-use-cases.html)

- [**SpeedCE vs BOCE Complete Comparison: Lightweight Maps vs Full Ops Toolkit**](articles/speedce-vs-boce.md)  
  BOCE does more than reachability; SpeedCE focuses on geographic HTTPS maps—know the boundary.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/speedce-vs-boce.html)

- [**SpeedCE vs ITDOG Complete Comparison: Scenarios, Pros/Cons, and Pairing**](articles/speedce-vs-itdog.md)  
  Map-first vs table/ping-first—when to open which tab and how to combine without duplicate work.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/speedce-vs-itdog.html)

- [**2026 Top 5 Free Speed Test Tools for Site Owners: Deep Review and Bookmark Picks**](articles/top5-free-speedtest-2026.md)  
  Curated stack for solo site owners—what to bookmark and when to use each in 2026.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/top5-free-speedtest-2026.html)

- [**VSPING vs SpeedCE: Pollution Detection and Reachability Together**](articles/vsping-vs-speedce.md)  
  VSPING for pollution/GFW signals; SpeedCE for nationwide HTTPS maps—use in sequence.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/vsping-vs-speedce.html)

- [**WebPageTest vs SpeedCE: When to Use Which Tool**](articles/webpagetest-vs-speedce.md)  
  Filmstrip debugging vs China carrier maps—pick tool by question type.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/webpagetest-vs-speedce.html)


### Advanced (35 articles)

- [**A/B Test Traffic Split Domains: Independent Map Acceptance per Experiment Arm**](articles/ab-test-traffic-split.md)  
  Experiment subdomain must accept independently—don't assume control map applies to variant.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/ab-test-traffic-split.html)

- [**Acquisition Tech Due Diligence: Quick Nationwide Reachability Assessment**](articles/acquisition-due-diligence.md)  
  M&A technical DD—SpeedCE snapshot of target's main domains in 30 minutes.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/acquisition-due-diligence.html)

- [**Affiliate Tracking Domains: Nationwide Reachability Impact on Conversion Chain**](articles/affiliate-tracking-domain.md)  
  Affiliate click blocked in one province loses commission—probe tracking domains on three carriers.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/affiliate-tracking-domain.html)

- [**News Release Peak Traffic: 30-Minute Pre-Publish Checkpoint**](articles/cctv-news-peak.md)  
  State media and viral news—half-hour SpeedCE gate before publish button.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/cctv-news-peak.html)

- [**Change Management Speed Test Gate: Mandatory Probe After DNS/Cert/Nginx Changes**](articles/change-management-speedtest.md)  
  Institutionalize "no SpeedCE screenshot, no change close"—reduces rollback incidents.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/change-management-speedtest.html)

- [**Quarterly Client Reports with Maps: B2B Provider Speed Test Reporting Template**](articles/client-report-quarterly.md)  
  Agencies retain clients with quarterly map reports—white-label template structure.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/client-report-quarterly.html)

- [**Competitor Benchmark Speed Tests: Same-Niche Map Comparison to Convince Leadership**](articles/competitor-benchmark.md)  
  Leadership ignores latency complaints until competitor map is all green and yours isn't—data-driven upgrade requests.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/competitor-benchmark.html)

- [**Disaster Recovery Drill: Nationwide SpeedCE Checkpoint After DR Failover**](articles/disaster-recovery-drill.md)  
  DR drill isn't done until DR site maps match primary acceptance thresholds.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/disaster-recovery-drill.html)

- [**Double-11/618 Sale Speed Test Timeline: T-7 to T+0 Complete Rhythm**](articles/double11-618-prep.md)  
  Domestic mega-sales timeline with SpeedCE gates at T-7, T-3, T-1, and hourly T+0.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/double11-618-prep.html)

- [**Guangdong/Zhejiang/Shanghai/Beijing Baseline Latency: Map Targets for Coastal Economies**](articles/guangdong-zhejiang-baseline.md)  
  Coastal economic hubs expect lower latency—use as baseline when accepting CDN and origin upgrades.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/guangdong-zhejiang-baseline.html)

- [**Hainan Free Trade Zone Sites: Island Geography and Access Traits**](articles/hainan-special-zone.md)  
  Island province routing differs from mainland—dedicated map acceptance for Hainan-focused services.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/hainan-special-zone.html)

- [**Post-ICP Filing Nationwide Reachability Acceptance: DNS, Certs, and Compliance**](articles/icp-filing-launch-check.md)  
  ICP approved doesn't mean nationwide green—accept parsing, HTTPS, and compliance probes after filing goes live.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/icp-filing-launch-check.html)

- [**Inner Mongolia/Northeast: Cold-Region Routes and Winter Peak Traffic**](articles/inner-mongolia-northeast.md)  
  Winter heating season shifts traffic patterns—retest northeast maps in January peak.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/inner-mongolia-northeast.html)

- [**Ad Landing Pages: 10-Minute Nationwide Checkpoint Before Campaign Launch**](articles/landing-page-campaign.md)  
  Paid traffic to slow landing pages burns budget—SpeedCE gate before ad account goes live.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/landing-page-campaign.html)

- [**Migration Before/After Report Template: Dual-Map Slides for Executives and Clients**](articles/migration-before-after-report.md)  
  Side-by-side maps in PPT close migration projects professionally—template structure included.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/migration-before-after-report.html)

- [**Ops Handover Speed Baselines: Map Archive Required Before Departure**](articles/multi-team-handover.md)  
  Leaving ops without baseline maps strands the team—handover package template.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/multi-team-handover.html)

- [**National Holiday Golden Week: Pre-Surge Mobile User Checkpoint**](articles/national-holiday-golden-week.md)  
  Golden week mobile travel surge—three-carrier checkpoint one week before holiday.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/national-holiday-golden-week.html)

- [**New Domain Cold Start 72 Hours: Registration, DNS, Certs, and Map Acceptance Rhythm**](articles/new-domain-cold-start.md)  
  New domains propagate unevenly—72-hour SpeedCE rhythm from registration through first marketing push.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/new-domain-cold-start.html)

- [**Northeast China Access Quality: Cold-Region Routes and CDN Node Coverage**](articles/northeast-china-access-guide.md)  
  Heilongjiang/Jilin/Liaoning have unique long-haul paths—accept with regional map focus.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/northeast-china-access-guide.html)

- [**Pre-Pentest External Attack Surface: Public Domain Speed Test Inventory**](articles/penetration-test-prep.md)  
  Before pentest, inventory all public hosts with probes—find orphan domains attackers will too.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/penetration-test-prep.html)

- [**Fujian/Guangdong Taiwan-Trade Sites: Southeast Coastal Map Acceptance**](articles/province-fujian-taiwan-trade.md)  
  Cross-strait trade sites need coastal map baselines and Mobile emphasis.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/province-fujian-taiwan-trade.html)

- [**Henan/Hubei Central China Access Optimization: Map Patterns and CDN Strategy**](articles/province-henan-hubei.md)  
  Central provinces bridge north-south routes—recognize map signatures and CDN node placement.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/province-henan-hubei.html)

- [**Beijing-Tianjin-Hebei/Shandong Baseline: North China Map Targets**](articles/province-shandong-hebei.md)  
  North China dense population—use as reference baseline for CDN PoP effectiveness.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/province-shandong-hebei.html)

- [**Sichuan/Chongqing Access Acceptance: Southwest Nodes and Route Traits**](articles/province-sichuan-chongqing.md)  
  Southwest basin geography affects routes—accept with province-focused maps.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/province-sichuan-chongqing.html)

- [**Yunnan/Guizhou Access: Southwest Frontier Maps and Mobile Network**](articles/province-yunnan-guizhou.md)  
  Southwest frontier provinces often show higher latency—set realistic targets and CDN strategy.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/province-yunnan-guizhou.html)

- [**September School Season: Education Site Traffic Assurance Speed Tests**](articles/school-start-september.md)  
  September enrollment spikes—education platforms run T-14 SpeedCE schedule.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/school-start-september.html)

- [**Baidu/Google Crawlers and Site Reachability: SEO Angle on Speed Tests**](articles/seo-crawl-baidu-google.md)  
  Crawlers hit from specific networks—reachability supports SEO; SpeedCE complements Search Console.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/seo-crawl-baidu-google.html)

- [**Short Link Domain Acceptance: Nationwide Node Tests on Redirect Chains**](articles/short-link-domain-check.md)  
  t.co style short domains redirect—probe short URL and final landing separately.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/short-link-domain-check.html)

- [**Spring Festival Traffic Assurance: Three-Carrier Checkpoint Before Mobile Surge**](articles/spring-festival-traffic.md)  
  Holiday mobile usage spikes—pre-festival three-carrier maps on all conversion domains.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/spring-festival-traffic.html)

- [**Status Page Setup: How Probe Data Supports Public Status Pages**](articles/status-page-setup.md)  
  Status pages need honest geographic impact—integrate probe summaries subscribers understand.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/status-page-setup.html)

- [**Subdomain Inventory Patrol: One Spreadsheet for Monthly Speed Tests of All Public Domains**](articles/subdomain-inventory-method.md)  
  Forgotten api-staging.example.com causes incidents—inventory method ensures no public host skips monthly probe.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/subdomain-inventory-method.html)

- [**2026 Ultimate Site Owner Browser Toolbar: Speed, Monitor, Performance 12 Links**](articles/ultimate-toolbar-2026.md)  
  One toolbar row for daily ops—SpeedCE, uptime, PageSpeed, DNS, SSL expiry, and vendor consoles.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/ultimate-toolbar-2026.html)

- [**Xinjiang/Tibet/Northwest Access Optimization: Map Acceptance and CDN Strategy**](articles/xinjiang-tibet-access-guide.md)  
  Northwest provinces show distinct map patterns—don't treat as generic "China slow"; targeted CDN and DNS strategy.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/xinjiang-tibet-access-guide.html)

- [**Year-End Infrastructure Report: Summarizing 12 Months of Map Archives**](articles/year-end-summary-report.md)  
  December is time to aggregate monthly screenshots into annual availability narrative.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/year-end-summary-report.html)

- [**Zero-Downtime Deploy: Blue/Green and Canary Map Comparison**](articles/zero-downtime-deploy.md)  
  Canary slice still needs geographic probe on canary hostname—compare blue vs green maps.  
  🌐 [Read online](https://freejbgo.github.io/SpeedCE-English-Tech/articles/zero-downtime-deploy.html)


## Scripts

| Script | Purpose |
|--------|--------|
| `scripts/english_article_generator.py` | Generate article Markdown |
| `scripts/generate_root_readme.py` | Update this README |
| `scripts/generate_seo_index.py` | Build SEO index and GitHub Pages site |

## Search engines and AI crawlers

This repo is configured for **GitHub Pages + crawler-friendly indexes** so search engines and AI bots (GPTBot, ClaudeBot, etc.) can index all 210 articles.

| Resource | URL |
|----------|-----|
| Read online (GitHub Pages) | https://freejbgo.github.io/SpeedCE-English-Tech/ |
| Sitemap | https://freejbgo.github.io/SpeedCE-English-Tech/sitemap.xml |
| robots.txt | https://freejbgo.github.io/SpeedCE-English-Tech/robots.txt |
| llms.txt (AI index) | https://freejbgo.github.io/SpeedCE-English-Tech/llms.txt |
| JSON metadata | https://freejbgo.github.io/SpeedCE-English-Tech/articles-index.json |

Regenerate indexes: `python3 scripts/generate_seo_index.py` (run after article changes; CI also refreshes weekly on Mondays).

Update README catalog: `python3 scripts/generate_root_readme.py`

<p align="center">
  <img src="https://hack23.com/icon-192.png" alt="Hack23 Logo" width="192" height="192">
</p>

<h1 align="center">🔚 Hack23 Homepage — End-of-Life Strategy</h1>

<p align="center">
  <strong>🛡️ Proactive Technology Lifecycle Management for a Static Corporate Website</strong><br>
  <em>📦 Web-Standards Stack • 🔄 Node.js Build Tooling Lifecycle • ☁️ AWS Service Continuity</em>
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Owner-CEO-0A66C2?style=for-the-badge" alt="Owner"/></a>
  <a href="#"><img src="https://img.shields.io/badge/Version-1.0-555?style=for-the-badge" alt="Version"/></a>
  <a href="#"><img src="https://img.shields.io/badge/Effective-2026--04--21-success?style=for-the-badge" alt="Effective Date"/></a>
  <a href="#"><img src="https://img.shields.io/badge/Review-Annual-orange?style=for-the-badge" alt="Review Cycle"/></a>
</p>

![License](https://img.shields.io/github/license/Hack23/homepage)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/Hack23/homepage/badge)](https://scorecard.dev/viewer/?uri=github.com/Hack23/homepage)

**📋 Document Owner:** CEO | **📄 Version:** 1.0 | **📅 Last Updated:** 2026-04-21 (UTC)
**🔄 Review Cycle:** Annual | **⏰ Next Review:** 2027-04-21
**🏷️ Classification:** [![Public](https://img.shields.io/badge/C-Public-lightgrey?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#confidentiality-levels) [![Low](https://img.shields.io/badge/I-Low-lightgreen?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#integrity-levels) [![Standard](https://img.shields.io/badge/A-Standard-lightgreen?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#availability-levels)

**🔐 ISMS Alignment:** This document fulfils the Business Continuity & Lifecycle documentation requirements set out in the [Hack23 Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md).

---

## 📚 Related Documentation

| Document | Focus | Description |
|----------|-------|-------------|
| **[🏛️ Architecture](ARCHITECTURE.md)** | C4 Model | System structure |
| **[🛡️ Security Architecture](SECURITY_ARCHITECTURE.md)** | Security | Defense-in-depth controls |
| **[🎯 Threat Model](THREAT_MODEL.md)** | Threats | STRIDE / MITRE ATT&CK analysis |
| **[🔄 Workflows](WORKFLOWS.md)** | CI/CD | GitHub Actions pipeline |
| **[🔄 BCP Plan](BCPPlan.md)** | Resilience | Business continuity & recovery |
| **[💰 Financial & Security Plan](FinancialSecurityPlan.md)** | Cost | TCO and security investment |
| **[🛡️ CRA Assessment](CRA-ASSESSMENT.md)** | Compliance | EU Cyber Resilience Act conformity |

---

## 🎯 EOL Strategy Overview

### **📋 Strategic Objective**

The Hack23 Homepage (`hack23.com`) is a **static HTML5/CSS3 corporate website** with **no server-side runtime**, **no database**, **no user data processing**, and **only build-time tooling**. As such it is intentionally one of the most lifecycle-resilient assets in the Hack23 portfolio: there is no application runtime to deprecate.

The site will continue to operate against current web standards indefinitely. EOL planning therefore focuses on three layered concerns:

1. **🌐 Web platform standards** — HTML5, CSS3, ECMAScript baseline, Schema.org, OpenGraph (effectively perpetual)
2. **🔨 Build & validation tooling** — Node.js, npm, GitHub Actions, OWASP ZAP, Lighthouse CI, HTMLHint, html5validator
3. **☁️ Hosting & delivery infrastructure** — AWS S3, CloudFront, Route53, ACM, GitHub Pages (DR)

This strategy aligns with the **"Living on the Edge"** philosophy of the [Hack23 Vulnerability Management Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Vulnerability_Management.md): keep tooling on the latest stable line, with comprehensive automated testing and SLSA Level 3 attestation gating each release.

### **🏷️ Business Impact Classification**

Per [Hack23 Classification Framework](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md):

| Security Dimension | Level | EOL Impact | Business Rationale |
|--------------------|-------|------------|--------------------|
| **🔐 Confidentiality** | [![Public](https://img.shields.io/badge/C-Public-lightgrey?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#confidentiality-levels) | Very Low | All website content is public corporate marketing material |
| **🔒 Integrity** | [![Low](https://img.shields.io/badge/I-Low-lightgreen?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#integrity-levels) | Low | Content accuracy matters for reputation but tolerates brief defacement |
| **⚡ Availability** | [![Standard](https://img.shields.io/badge/A-Standard-lightgreen?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#availability-levels) | Low | 99% SLA target; CloudFront + GitHub Pages DR provides ample resilience |

**🎯 RTO / RPO Alignment:** RTO Standard (>72 h), RPO Extended (>24 h) — daily Git commits and S3 versioning are sufficient.

---

## 📦 Current Technology Stack Inventory

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#e8f5e9", "primaryTextColor": "#2e7d32", "lineColor": "#4caf50", "secondaryColor": "#fff3e0", "tertiaryColor": "#e3f2fd"}}}%%
mindmap
  root)🌐 Hack23 Homepage Stack(
    (📄 Web Platform)
      🌐 HTML5
        ⏰ EOL: None (W3C living standard)
      🎨 CSS3
        ⏰ EOL: None (W3C living standard)
      📋 Schema.org JSON-LD
        ⏰ EOL: None (community standard)
      🔤 Google Fonts
        ⏰ EOL: External CDN; SRI planned
    (☁️ Hosting & Delivery)
      📦 AWS S3
        ⏰ EOL: AWS GA service; no announced EOL
      🌍 AWS CloudFront
        ⏰ EOL: AWS GA service; no announced EOL
      🔗 AWS Route53
        ⏰ EOL: AWS GA service; no announced EOL
      🔒 AWS ACM (TLS 1.3)
        ⏰ EOL: Tied to TLS protocol lifecycle
      🏠 GitHub Pages (DR)
        ⏰ EOL: GitHub-managed
    (🔨 Build & Validation Tooling)
      ☕ Node.js (LTS baseline + current-version compatibility testing)
        ⏰ Lifecycle: Node release schedule
        🔄 LTS rotation tracked annually; selected workflows may also use newer major releases (e.g., v24/v25) for forward-compatibility validation
      📦 npm + npx
        ⏰ Bundled with Node.js
      ⚙️ GitHub Actions
        ⏰ EOL: GitHub-managed; SHA-pinned actions
      🛡️ StepSecurity Harden Runner
        ⏰ EOL: Active OSS, monthly releases
      🔍 OWASP ZAP
        ⏰ EOL: Active OSS, semi-annual major releases
      💡 Lighthouse CI
        ⏰ EOL: Google-maintained
      ✅ HTMLHint, html5validator, Linkinator
        ⏰ EOL: Active OSS
      🗜️ dra1ex/minify-action
        ⏰ EOL: SHA-pinned action
      📋 Anchore Syft (SBOM)
        ⏰ EOL: Anchore-maintained OSS
    (🤖 AI & DevSecOps Tooling)
      🤖 GitHub Copilot
        ⏰ EOL: GitHub-managed product
      📚 58 Copilot Skills
        ⏰ EOL: Repo-managed
      🤝 8 Custom Agents
        ⏰ EOL: Repo-managed
      🔌 MCP Servers (github, filesystem, git, memory, sequential-thinking, playwright, brave-search, aws-knowledge)
        ⏰ EOL: Per-server upstream lifecycle
```

---

## 📅 Lifecycle Tracking Matrix

### Web Platform (Source Content)

| Component | Current | EOL Risk | Mitigation |
|-----------|---------|----------|------------|
| HTML5 | Living standard | None | W3C HTML Living Standard is perpetually maintained |
| CSS3 / CSS Modules | Living standard | None | W3C CSS WG; we use widely-supported, baseline features |
| ECMAScript (used in inline scripts) | Baseline (ES2015+) | None | Minimal JS; conservative feature set |
| Schema.org JSON-LD | Living vocabulary | None | Community-maintained; backward-compatible |
| OpenGraph / Twitter Cards | De facto standard | None | Stable for >10 years |
| RTL CSS for `_ar`, `_he` | Baseline support | None | All evergreen browsers support `dir="rtl"` |

### Build & Validation Tooling

| Component | Current Version Source | LTS Strategy | EOL Trigger | Action Plan |
|-----------|------------------------|--------------|-------------|-------------|
| **Node.js** | `.github/workflows/copilot-setup-steps.yml` + `actions/setup-node@v6.4.0` | Active LTS | Active LTS goes EOL per [nodejs.org/en/about/previous-releases](https://nodejs.org/en/about/previous-releases) | Bump to next LTS within 60 days of new LTS GA; test all workflows on PR |
| **GitHub Actions runners** | `ubuntu-26.04` | GitHub-managed | GitHub deprecation notice | Track GitHub Actions changelog; upgrade to next Ubuntu LTS when released |
| **StepSecurity Harden Runner** | SHA-pinned (`v2.19.0` as of 2026-04) | Latest stable | Project EOL | Dependabot tracks; review monthly |
| **OWASP ZAP (`ghcr.io/zaproxy/zaproxy:stable`)** | `:stable` tag | Stable channel | OWASP ZAP project EOL | Migrate to successor scanner if announced |
| **Lighthouse CI** | `treosh/lighthouse-ci-action` | Latest stable | Action archived | Pin to last working SHA; evaluate alternatives (e.g., `chrome-launcher` direct) |
| **HTMLHint** | npm latest | Latest stable | Project archived | Replace with `htmlvalidate` or custom validator |
| **html5validator** | PyPI | Latest stable | Project archived | Switch to W3C Validator API directly |
| **Linkinator** | npm latest | Latest stable | Project archived | Replace with `lychee` or `markdown-link-check` |
| **Minify Action (`dra1ex/minify-action`)** | SHA-pinned | Latest stable | Action archived | Pin to last good SHA; replace with `htmlnano` + `cssnano` script |
| **anchore/sbom-action (Syft)** | SHA-pinned | Latest stable | Project EOL | Anchore Syft is actively maintained; track Anchore announcements |
| **actions/attest-build-provenance, attest-sbom** | SHA-pinned | GitHub-maintained | GitHub deprecation | Track GitHub Actions security blog |

### Hosting & Delivery (AWS + GitHub)

| Component | Current | EOL Risk | Action Plan |
|-----------|---------|----------|-------------|
| **AWS S3** (private bucket, versioning, OAC) | GA service | Very Low | AWS GA services have no published EOL; monitor AWS What's New |
| **AWS CloudFront** (TLS 1.3, security-headers policy, AWS Shield Standard) | GA service | Very Low | Migrate cache policy if AWS deprecates legacy config formats |
| **AWS Route53** (hosted zone, health-checks, DR failover) | GA service | Very Low | None required |
| **AWS Certificate Manager** (TLS certs auto-renewed) | GA service | Tied to TLS | Move to TLS 1.3-only when CloudFront drops TLS 1.2 baseline |
| **GitHub Pages** (DR origin) | GA product | Low | Keep gh-pages branch in sync via release.yml |
| **Google Fonts CDN** | External CDN | Medium | Plan B: self-host fonts under `/fonts/` with SRI hashes |

### AI / DevSecOps Tooling

| Component | EOL Risk | Action Plan |
|-----------|----------|-------------|
| GitHub Copilot + Coding Agent | Product change | Track GitHub Copilot changelog; documentation in repo decoupled from product |
| 58 Skills in `.github/skills/` | None (repo-owned) | Skill index reviewed quarterly |
| 8 Custom Agents in `.github/agents/` | None (repo-owned) | Agent definitions reviewed quarterly |
| MCP servers | Per-server upstream | `.github/copilot-mcp.json` SHA-pin where supported; replace if upstream goes silent |

---

## 🚦 EOL Decision Triggers

A formal EOL review is triggered by **any** of the following:

| Trigger | Detected By | Response Time | Action |
|---------|-------------|---------------|--------|
| Node.js LTS reaches end of "Active LTS" phase | Dependabot / CI failure | Within 60 days | Bump to next LTS in `setup-node@vX` action `node-version` input |
| GitHub Action archived/deprecated | Dependabot alert | Within 30 days | Replace with maintained equivalent; SHA-pin |
| AWS service deprecation notice | AWS Health Dashboard | Per AWS deadline | Migrate per AWS guidance; rehearse in staging |
| Critical CVE (CVSS ≥ 9.0) in build tooling | OpenSSF Scorecard / Dependabot | Within 7 days (per Vulnerability Management SLA) | Patch, regenerate SLSA attestation, redeploy |
| Browser baseline drops critical CSS feature | Lighthouse / manual audit | Within 90 days | Refactor `styles.css`; bump version |
| Web standard officially deprecated (e.g., OpenGraph successor) | W3C / industry signal | Per spec timeline | Add successor metadata alongside legacy |
| GitHub Pages discontinued (DR origin) | GitHub announcement | Within 30 days | Switch DR to AWS S3 second region (e.g., eu-west-1) |
| Hack23 brand or product strategy change | Internal decision | Per change-management process | Re-architect or sunset; see Sunset Procedure below |

---

## 🔚 Sunset Procedure (If Project is Retired)

In the unlikely event the corporate website is retired (e.g., company dissolution or full migration to a new platform), the following steps are executed:

1. **🗓️ Pre-announcement (90 days)** — Update homepage banner; notify partners and clients via `info@hack23.com`
2. **🗃️ Archive (60 days)** — Snapshot of repository tagged `archive/final`; release `vN.0.0-final` with full SLSA Level 3 attestation; publish final SBOM
3. **🌐 DNS migration (30 days)** — Either redirect `hack23.com` to successor URL or set Route53 to a static "Retired" page
4. **☁️ Infrastructure decommission (Day 0)** — Disable CloudFront distribution (keep config exportable); empty and version-lock S3 bucket; archive CloudTrail logs to Glacier per [Backup & Recovery Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Backup_Recovery_Policy.md)
5. **📂 GitHub repo archival** — Mark repository read-only / archived on GitHub; preserve issues, PRs, and release artefacts indefinitely (public good)
6. **📋 Compliance closure** — Update [Risk Register](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Risk_Register.md), [Compliance Checklist](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Compliance_Checklist.md); file final CRA conformity statement

---

## 🛡️ Migration Strategy (If Stack Evolves)

If the website outgrows the static-only model (e.g., interactive client area, dynamic dashboards), evolution paths and EOL implications are pre-planned:

| Evolution Scenario | New Components | EOL Implications | Migration Window |
|--------------------|----------------|------------------|------------------|
| **+ Contact form (server-less)** | API Gateway + Lambda + SES | Lambda runtime (Node.js) lifecycle now in scope | Plan in line with Node LTS schedule |
| **+ Newsletter / CMS** | DynamoDB / S3 + Lambda | Add data classification & retention | Update [DATA_MODEL.md](DATA_MODEL.md), [BCPPlan.md](BCPPlan.md) |
| **+ Search** | OpenSearch Serverless or Algolia | Vendor lock-in risk | Document exit plan |
| **+ Authentication (client area)** | AWS Cognito or Auth0 | Federation lifecycle | Add to [Access Control Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Access_Control_Policy.md) review |
| **+ Internationalisation framework** | Static-site generator (Astro / Eleventy / Hugo) | Adds toolchain EOL surface | Pilot in branch; budget refactor |

Each evolution requires updates to: ARCHITECTURE.md, SECURITY_ARCHITECTURE.md, THREAT_MODEL.md, BCPPlan.md, FinancialSecurityPlan.md, and this document.

---

## 📋 Lifecycle Governance

| Activity | Cadence | Owner | Evidence |
|----------|---------|-------|----------|
| **Dependency / Action review** | Weekly (Dependabot) | CEO | Dependabot PRs |
| **Stack EOL review** | Quarterly | CEO | Updated tables in this document |
| **Node LTS bump** | At each new LTS | CEO | `setup-node` action input bumped, CI green |
| **AWS deprecation watch** | Continuous (AWS Health) | CEO | AWS Health Dashboard subscription |
| **Browser baseline review** | Annual | CEO | Lighthouse + caniuse audit |
| **Sunset rehearsal** | Documented; not rehearsed (low value) | CEO | This document |

---

## 📋 ISMS Policy Alignment

| ISMS Policy | Relevance |
|-------------|-----------|
| **[Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md)** | Lifecycle documentation requirement |
| **[Vulnerability Management](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Vulnerability_Management.md)** | "Living on the Edge" patch strategy; CVSS-driven SLAs |
| **[Open Source Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Open_Source_Policy.md)** | Action and dependency licensing & maintenance |
| **[Change Management](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Change_Management.md)** | Tooling upgrade and migration procedure |
| **[Backup & Recovery Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Backup_Recovery_Policy.md)** | Sunset archival and Git-based perpetual backup |
| **[Business Continuity Plan](BCPPlan.md)** | DR fallback during migration / sunset |

---

<div align="center">

## 📋 Document Control

**✅ Approved by:** James Pether Sörling, CEO, Hack23 AB
**📤 Distribution:** Public
**🏷️ Classification:** [![Confidentiality: Public](https://img.shields.io/badge/C-Public-lightgrey?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#confidentiality-levels) [![Integrity: Low](https://img.shields.io/badge/I-Low-lightgreen?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#integrity-levels) [![Availability: Standard](https://img.shields.io/badge/A-Standard-lightgreen?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#availability-levels)
**📅 Effective Date:** 2026-04-21
**⏰ Next Review:** 2027-04-21

[![ISO 27001:2022](https://img.shields.io/badge/ISO_27001-2022-blue?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Compliance_Checklist.md)
[![NIST CSF 2.0](https://img.shields.io/badge/NIST_CSF-2.0-purple?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Compliance_Checklist.md)
[![CIS Controls v8.1](https://img.shields.io/badge/CIS_Controls-v8.1-orange?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Compliance_Checklist.md)

</div>

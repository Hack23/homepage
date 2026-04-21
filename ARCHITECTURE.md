<p align="center">
  <img src="https://hack23.com/icon-192.png" alt="Hack23 Logo" width="192" height="192">
</p>

<h1 align="center">🏛️ Hack23 Homepage — Architecture</h1>

<p align="center">
  <strong>C4 Architecture Model: Static Website on AWS S3 + CloudFront</strong><br>
  <em>Corporate Cybersecurity Consulting Website — hack23.com</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Owner-CEO-0A66C2?style=for-the-badge" alt="Owner"/>
  <img src="https://img.shields.io/badge/Version-1.1-555?style=for-the-badge" alt="Version"/>
  <img src="https://img.shields.io/badge/Status-Current-success?style=for-the-badge" alt="Status"/>
  <img src="https://img.shields.io/badge/Review-Quarterly-orange?style=for-the-badge" alt="Review Cycle"/>
</p>

![License](https://img.shields.io/github/license/Hack23/homepage)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/Hack23/homepage/badge)](https://scorecard.dev/viewer/?uri=github.com/Hack23/homepage)
[![Verify and Deploy](https://github.com/Hack23/homepage/actions/workflows/main.yml/badge.svg)](https://github.com/Hack23/homepage/actions/workflows/main.yml)
[![SLSA 3](https://slsa.dev/images/gh-badge-level3.svg)](https://slsa.dev/spec/v1.0/levels)

**📋 Document Owner:** CEO | **📄 Version:** 1.1 | **📅 Last Updated:** 2026-04-21 (UTC)
**🔄 Review Cycle:** Quarterly | **⏰ Next Review:** 2026-07-21
**🏷️ Classification:** [![Public](https://img.shields.io/badge/C-Public-lightgrey?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#confidentiality-levels) [![Low](https://img.shields.io/badge/I-Low-lightgreen?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#integrity-levels) [![Standard](https://img.shields.io/badge/A-Standard-lightgreen?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#availability-levels)

---

## 📚 Architecture Documentation Map

| Document | Focus | Description |
|----------|-------|-------------|
| **[🏛️ Architecture](ARCHITECTURE.md)** | C4 Model | C4 model showing system structure (this document) |
| **[🛡️ Security Architecture](SECURITY_ARCHITECTURE.md)** | Security | Security controls and infrastructure |
| **[📊 Data Model](DATA_MODEL.md)** | Data | Content model and data structures |
| **[🔄 Flowchart](FLOWCHART.md)** | Processes | CI/CD and content workflows |
| **[📈 State Diagram](STATEDIAGRAM.md)** | States | Deployment and content lifecycle states |
| **[🧠 Mindmap](MINDMAP.md)** | Concepts | System conceptual relationships |
| **[💼 SWOT](SWOT.md)** | Strategy | Strategic analysis and positioning |
| **[🔄 Workflows](WORKFLOWS.md)** | CI/CD | GitHub Actions workflow documentation |
| **[🎯 Threat Model](THREAT_MODEL.md)** | Threats | STRIDE threat analysis |
| **[🛡️ CRA Assessment](CRA-ASSESSMENT.md)** | Compliance | EU Cyber Resilience Act conformity |
| **[🔄 BCP Plan](BCPPlan.md)** | Resilience | Business continuity & recovery |
| **[💰 Financial & Security Plan](FinancialSecurityPlan.md)** | Cost | Infrastructure cost & security investment |
| **[🔚 End-of-Life Strategy](End-of-Life-Strategy.md)** | Lifecycle | Technology lifecycle management |
| **[🏷️ Classification](CLASSIFICATION.md)** | Data | Security classification framework |
| **[🚀 Future Architecture](FUTURE_ARCHITECTURE.md)** | Roadmap | Architectural evolution plans |

---

## 📑 Table of Contents

- [🌐 System Context](#-system-context)
- [🏢 Container View](#-container-view)
- [🧩 Component View](#-component-view)
- [📁 File Structure](#-file-structure)
- [⚙️ Technology Stack](#-technology-stack)
- [🔄 Deployment Architecture](#-deployment-architecture)
- [📋 ISMS Compliance](#-isms-compliance)

---

## 🌐 System Context

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2196F3", "primaryTextColor": "#ffffff", "lineColor": "#455A64", "secondaryColor": "#4CAF50", "tertiaryColor": "#FF9800", "primaryBorderColor": "#1565C0"}}}%%
C4Context
    title System Context - Hack23 Homepage (hack23.com)

    Person(visitor, "🧑 Website Visitor", "Potential clients, partners, developers exploring Hack23's cybersecurity services")
    Person(admin, "👤 Content Admin", "CEO/developer maintaining website content")

    System(homepage, "🌐 Hack23 Homepage", "Static HTML/CSS corporate website showcasing cybersecurity consulting services, open-source projects, and ISMS transparency")

    System_Ext(cloudfront, "☁️ AWS CloudFront", "Global CDN with 400+ edge locations, DDoS protection, HTTPS termination")
    System_Ext(s3, "💾 AWS S3", "Static website hosting with versioning and encryption")
    System_Ext(github, "🔧 GitHub", "Source control, CI/CD, security scanning")
    System_Ext(ghpages, "📄 GitHub Pages", "DR hosting fallback")

    Rel(visitor, cloudfront, "Views website", "HTTPS/TLS 1.3")
    Rel(cloudfront, s3, "Serves content", "HTTPS")
    Rel(admin, github, "Pushes content changes", "HTTPS/SSH")
    Rel(github, s3, "Deploys via CI/CD", "AWS OIDC")
    Rel(visitor, ghpages, "DR fallback", "HTTPS")
```

---

## 🏢 Container View

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2196F3", "primaryTextColor": "#ffffff", "lineColor": "#455A64", "secondaryColor": "#4CAF50", "tertiaryColor": "#FF9800", "primaryBorderColor": "#1565C0"}}}%%
C4Container
    title Container View - Hack23 Homepage

    Person(visitor, "Website Visitor", "Browser user")

    System_Boundary(website, "Hack23 Homepage") {
        Container(html, "📄 HTML Pages", "HTML5", "1,353 pages — 105 English source pages × 14 languages: project showcases, blog posts, services, ISMS docs, sitemaps")
        Container(css, "🎨 Stylesheet", "CSS3", "Single styles.css with responsive design, CSS custom properties, dark theme")
        Container(sitemap, "🗺️ Sitemap", "XML", "SEO sitemap with hreflang tags for 14 languages")
        Container(robots, "🤖 Robots.txt", "Text", "Search engine crawling directives")
        Container(schema, "📋 Schema.org", "JSON-LD", "Structured data for SEO: Organization, WebPage, FAQPage, BreadcrumbList, Service")
    }

    System_Boundary(infra, "AWS Infrastructure") {
        Container(cf, "☁️ CloudFront", "CDN", "Global edge delivery, HTTPS, caching, security headers")
        Container(s3bucket, "💾 S3 Bucket", "Storage", "Static content with versioning, AES-256 encryption at rest")
        Container(route53, "🌍 Route53", "DNS", "Domain management with health checks")
        Container(acm, "🔒 ACM", "TLS", "SSL/TLS certificate management")
    }

    System_Boundary(cicd, "CI/CD Pipeline") {
        Container(actions, "⚙️ GitHub Actions", "CI/CD", "Build, validate, scan, deploy workflows")
        Container(scanning, "🔍 Security Scanning", "Tools", "CodeQL, ZAP, Scorecard, Dependency Review")
    }

    Rel(visitor, cf, "HTTPS requests", "TLS 1.3")
    Rel(cf, s3bucket, "Origin fetch", "HTTPS")
    Rel(actions, s3bucket, "Deploy content", "AWS OIDC")
    Rel(actions, scanning, "Security checks", "API")
```

---

## 🧩 Component View

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2196F3", "primaryTextColor": "#ffffff", "lineColor": "#455A64", "secondaryColor": "#4CAF50", "tertiaryColor": "#FF9800", "primaryBorderColor": "#1565C0"}}}%%
C4Component
    title Component View - Hack23 Homepage Content

    Container_Boundary(content, "Website Content") {
        Component(index, "🏠 Homepage", "HTML", "Main landing page with services overview")
        Component(projects, "📦 Project Pages", "HTML", "7 product portfolio: CIA, CIA Compliance Manager, Black Trigram, EU Parliament MCP Server, Riksdagsmonitor, EU Parliament Monitor, Homepage")
        Component(docs, "📚 Documentation Pages", "HTML", "Project documentation pages with ISMS cards")
        Component(features, "⭐ Feature Pages", "HTML", "Project feature showcase pages")
        Component(blog, "📝 Blog Posts", "HTML", "26 English blog articles on security, compliance, AI, Discordian framework")
        Component(services, "💼 Services", "HTML", "Consulting services and offerings")
        Component(i18n, "🌍 Translations", "HTML", "13 language variants × 96 pages each (sv, ko, ar, zh, de, fi, fr, es, ja, he, nl, da, no)")
    }

    Container_Boundary(seo, "SEO & Metadata") {
        Component(meta, "🏷️ Meta Tags", "HTML", "Open Graph, Twitter Cards, hreflang")
        Component(schemaorg, "📋 Schema.org", "JSON-LD", "Structured data markup")
        Component(breadcrumbs, "🍞 Breadcrumbs", "HTML", "Navigation with Schema.org BreadcrumbList")
    }

    Container_Boundary(style, "Styling") {
        Component(stylesheet, "🎨 styles.css", "CSS3", "Single CSS file with custom properties and responsive grid")
    }
```

---

## 📁 File Structure

```
hack23-homepage/
├── 📄 index.html                    # Main landing page (and 12 lang variants)
├── 📄 *-project.html / *.html       # 7 product overview pages (CIA, CIA Compliance Manager,
│                                    # Black Trigram, EU Parliament MCP Server, Riksdagsmonitor,
│                                    # EU Parliament Monitor, Hack23 Homepage)
├── 📄 *-features.html               # Project feature pages
├── 📄 *-docs.html                   # Project documentation pages
├── 📄 blog-*.html                   # 26 English blog articles (+ translations)
├── 📄 services.html                 # Services page
├── 📄 why-hack23.html               # About / differentiators
├── 📄 *_{lang}.html                 # Translated pages — 13 languages × 96 pages
│                                    # (sv, ko, ar, zh, de, fi, fr, es, ja, he, nl, da, no)
├── 🎨 styles.css                    # Single stylesheet (responsive, dark theme)
├── 🗺️ sitemap.xml                   # XML sitemap with hreflang
├── 📄 sitemap_*.html                # HTML sitemaps per language
├── 🤖 robots.txt                    # Crawling directives
├── 📄 budget.json                   # Lighthouse performance budgets
├── 📄 .htmlhintrc                   # HTML linting configuration
├── 📁 screenshots/                  # Visual assets and product screenshots
├── 📁 docs/                         # Auto-generated release docs (Lighthouse, a11y, security reports)
├── 📁 .github/
│   ├── 📁 workflows/                # 10 CI/CD workflow files
│   ├── 📁 skills/                   # 58 Copilot skills (12 categories)
│   ├── 📁 agents/                   # 8 custom Copilot agents
│   ├── 📁 aw/                       # Agentic workflow shared prompts
│   └── 📄 copilot-mcp.json          # MCP server configuration
├── 📄 ARCHITECTURE.md               # C4 architecture (this file)
├── 📄 SECURITY_ARCHITECTURE.md      # Security design
├── 📄 THREAT_MODEL.md               # STRIDE / MITRE ATT&CK threat analysis
├── 📄 CRA-ASSESSMENT.md             # EU Cyber Resilience Act conformity
├── 📄 BCPPlan.md                    # Business Continuity Plan
├── 📄 FinancialSecurityPlan.md      # Cost & security investment
├── 📄 End-of-Life-Strategy.md       # Technology lifecycle
├── 📄 DATA_MODEL.md                 # Content & data model
├── 📄 FLOWCHART.md                  # Process flows
├── 📄 STATEDIAGRAM.md               # Lifecycle states
├── 📄 MINDMAP.md                    # Conceptual relationships
├── 📄 SWOT.md                       # Strategic analysis
├── 📄 WORKFLOWS.md                  # CI/CD documentation
├── 📄 FUTURE_ARCHITECTURE.md        # Architectural roadmap
├── 📄 FUTURE_SECURITY_ARCHITECTURE.md # Security enhancement roadmap
├── 📄 FUTURE_WORKFLOWS.md           # CI/CD evolution
├── 📄 CLASSIFICATION.md             # Data classification per ISMS
├── 📄 ISMS_REFERENCE_GUIDE.md       # Blog-to-policy mapping
├── 📄 SECURITY.md                   # Vulnerability disclosure policy
└── 📄 README.md                     # Project overview
```

---

## ⚙️ Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Content** | HTML5 | Semantic markup with Schema.org structured data |
| **Styling** | CSS3 | Responsive design with custom properties; single `styles.css` |
| **Hosting** | AWS S3 (private bucket) | Static website hosting with versioning + AES-256 encryption |
| **CDN** | AWS CloudFront | Global edge delivery (450+ PoPs) with HTTPS, security headers, OAC |
| **DNS** | AWS Route53 | Domain management with health-check based DR failover |
| **TLS** | AWS ACM | Certificate management (TLS 1.3) |
| **DR Hosting** | GitHub Pages | Free fallback origin via Route53 health-check failover |
| **CI/CD** | GitHub Actions (10 workflows) | Automated build, validate, scan, deploy, release pipeline |
| **Security Scanning** | CodeQL, OWASP ZAP, OpenSSF Scorecard, Dependency Review | Multi-layer security scanning |
| **Quality** | HTMLHint, Lighthouse CI, html5validator, Linkinator | Content validation and performance |
| **Build Hardening** | StepSecurity Harden Runner | Runtime egress filtering and process monitoring |
| **Supply Chain** | SLSA Build Level 3, Anchore Syft (SBOM), GitHub Attestations | Build provenance, SBOM, signed releases |
| **Build Tooling** | Node.js (LTS), `dra1ex/minify-action` | HTML/CSS/JS minification |
| **AI Tooling** | GitHub Copilot, 58 skills, 8 custom agents, MCP servers | DevSecOps assistance |

---

## 🔄 Deployment Architecture

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2196F3", "primaryTextColor": "#1a1a2e", "lineColor": "#455A64", "secondaryColor": "#e8f5e9", "tertiaryColor": "#fff8e1", "primaryBorderColor": "#1565C0"}}}%%
flowchart LR
    subgraph GitHub["🔧 GitHub"]
        repo[Repository] --> actions[GitHub Actions]
        actions --> validate[Validate HTML/CSS]
        validate --> scan[Security Scan]
        scan --> build[Minify & Build]
    end

    subgraph AWS["☁️ AWS"]
        build --> s3[S3 Bucket]
        s3 --> cf[CloudFront CDN]
        cf --> edge[Edge Locations]
    end

    edge --> visitor[🧑 Visitor]

    classDef default fill:#e3f2fd,stroke:#1565C0,stroke-width:2px,color:#1a1a2e
    classDef primary fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#ffffff
    classDef success fill:#4CAF50,stroke:#2E7D32,stroke-width:2px,color:#ffffff
    classDef warning fill:#FF9800,stroke:#F57C00,stroke-width:2px,color:#ffffff
    classDef danger fill:#D32F2F,stroke:#B71C1C,stroke-width:2px,color:#ffffff
    classDef info fill:#455A64,stroke:#263238,stroke-width:2px,color:#ffffff
```

---

## 📋 ISMS Compliance

This architecture aligns with the following ISMS frameworks:

| Framework | Controls | Status |
|-----------|----------|--------|
| **[ISO 27001:2022](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Compliance_Checklist.md)** | A.8.9 Configuration Management, A.8.25 Secure Development | ✅ Implemented |
| **[NIST CSF 2.0](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Compliance_Checklist.md)** | PR.DS-1 Data-at-Rest Protection, PR.IP-1 Configuration Baseline | ✅ Implemented |
| **[CIS Controls v8.1](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Compliance_Checklist.md)** | CIS 2 Software Inventory, CIS 16 Application Software Security | ✅ Implemented |

### Related ISMS Policies

- 🔗 **[Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md)** — Development lifecycle requirements
- 🔗 **[Network Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Network_Security_Policy.md)** — CDN and network architecture
- 🔗 **[Cryptography Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Cryptography_Policy.md)** — TLS and encryption standards
- 🔗 **[Access Control Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Access_Control_Policy.md)** — AWS IAM and OIDC
- 🔗 **[Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)** — Overall security governance

<p align="center">
  <img src="https://hack23.com/icon-192.png" alt="Hack23 Logo" width="192" height="192">
</p>

<h1 align="center">🧠 Hack23 Homepage — Concept Map</h1>

<p align="center">
  <strong>System Conceptual Relationships and Overview</strong><br>
  <em>Mindmap Documentation for hack23.com</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Owner-CEO-0A66C2?style=for-the-badge" alt="Owner"/>
  <img src="https://img.shields.io/badge/Version-1.1-555?style=for-the-badge" alt="Version"/>
  <img src="https://img.shields.io/badge/Status-Current-success?style=for-the-badge" alt="Status"/>
  <img src="https://img.shields.io/badge/Review-Quarterly-orange?style=for-the-badge" alt="Review Cycle"/>
</p>

![License](https://img.shields.io/github/license/Hack23/homepage)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/Hack23/homepage/badge)](https://scorecard.dev/viewer/?uri=github.com/Hack23/homepage)

**📋 Document Owner:** CEO | **📄 Version:** 1.1 | **📅 Last Updated:** 2026-04-21 (UTC)
**🔄 Review Cycle:** Quarterly | **⏰ Next Review:** 2026-07-21
**🏷️ Classification:** [![Public](https://img.shields.io/badge/C-Public-lightgrey?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#confidentiality-levels) [![Low](https://img.shields.io/badge/I-Low-lightgreen?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#integrity-levels) [![Standard](https://img.shields.io/badge/A-Standard-lightgreen?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#availability-levels)

---

## 📚 Related Documentation

| Document | Focus | Description |
|----------|-------|-------------|
| **[🏛️ Architecture](ARCHITECTURE.md)** | C4 Model | System structure and containers |
| **[📊 Data Model](DATA_MODEL.md)** | Data | Content model and data structures |
| **[🔄 Flowchart](FLOWCHART.md)** | Processes | CI/CD and content workflows |
| **[📈 State Diagram](STATEDIAGRAM.md)** | States | Deployment and content lifecycle |
| **[🛡️ Security Architecture](SECURITY_ARCHITECTURE.md)** | Security | Defense-in-depth controls |
| **[🎯 Threat Model](THREAT_MODEL.md)** | Threats | STRIDE / MITRE ATT&CK analysis |
| **[💼 SWOT](SWOT.md)** | Strategy | Strategic analysis |
| **[🔄 BCP Plan](BCPPlan.md)** | Resilience | Business continuity & recovery |
| **[💰 Financial & Security Plan](FinancialSecurityPlan.md)** | Cost | TCO and security investment |
| **[🔚 End-of-Life Strategy](End-of-Life-Strategy.md)** | Lifecycle | Technology lifecycle |
| **[🛡️ CRA Assessment](CRA-ASSESSMENT.md)** | Compliance | EU Cyber Resilience Act conformity |
| **[🚀 Future Mindmap](FUTURE_MINDMAP.md)** | Roadmap | Capability expansion plans |

---

## 🌐 Hack23 Homepage Overview

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2196F3", "primaryTextColor": "#1a1a2e", "lineColor": "#455A64", "secondaryColor": "#4CAF50", "tertiaryColor": "#FF9800"}}}%%
mindmap
  root((hack23.com<br/>Cybersecurity<br/>Consulting))
    🏢 Company
      Hack23 AB
        Swedish Company
        Cybersecurity Focus
        Open Source Advocate
        ISMS Transparency
      Services
        Security Consulting
        Compliance Advisory
        Architecture Review
        Threat Modeling
      Values
        Transparency
        Open Source Security
        Practical Solutions
        Innovation
    🌐 Website
      Static HTML5 CSS3
        1353 HTML Files Total
        105 English Source Pages
        96 Pages Per Language
        Responsive Design
        WCAG 2.1 AA
        Dark Theme
      14 Languages
        English Primary
        Swedish Korean Arabic RTL
        Chinese German Finnish
        French Spanish Japanese
        Hebrew RTL Dutch
        Danish Norwegian
      SEO Optimized
        Schema.org JSON LD
        Open Graph
        Hreflang Tags
        Sitemap XML
    📦 Open Source Projects (7)
      CIA
        Political Intelligence
        Swedish Parliament
        Java Spring Boot AWS
      CIA Compliance Manager
        Security Assessment
        Compliance Tool
        React TypeScript Supabase
      Black Trigram
        Korean Combat Sim
        Three.js WebGL R3F
        Educational Gaming
      EU Parliament MCP Server
        Model Context Protocol
        European Parliament Open Data
        TypeScript
      Riksdagsmonitor
        Swedish Parliament
        AI News Generation
        Static Site
      EU Parliament Monitor
        European Parliament
        Intelligence Platform
        Multi Language
      Hack23 Homepage
        This Repository
        Static HTML CSS Marketing Site
        ISMS Transparency
    ☁️ Infrastructure
      AWS
        S3 Static Hosting
        CloudFront CDN
        Route53 DNS
        ACM TLS Certificates
      GitHub
        Source Control
        Actions CI CD
        Security Scanning
        Copilot Agents
      Security
        SLSA Build Level 3
        OpenSSF Scorecard
        CodeQL Analysis
        ZAP Full Scan
    🛡️ ISMS Framework
      ISO 27001 2022
        Annex A Controls
        Risk Management
        Continuous Improvement
      NIST CSF 2.0
        Govern
        Identify
        Protect
        Detect
        Respond
        Recover
      CIS Controls v8.1
        Implementation Groups
        Security Baselines
        Best Practices
      Compliance
        GDPR
        NIS2
        EU CRA
```

---

## 🔧 Technical Architecture Concepts

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2196F3", "primaryTextColor": "#1a1a2e", "lineColor": "#455A64", "secondaryColor": "#4CAF50", "tertiaryColor": "#FF9800"}}}%%
mindmap
  root((Technical Stack))
    Frontend
      HTML5
        Semantic Elements
        Schema.org Markup
        Accessibility ARIA
        Breadcrumb Navigation
      CSS3
        Custom Properties
        Responsive Grid
        Dark Theme
        Print Styles
      Content
        Blog Posts
        Project Pages
        Service Descriptions
        ISMS Documentation
    CI CD Pipeline (10 Workflows)
      GitHub Actions
        main.yml Verify and Deploy
        pullrequest.yml PR Verification
        quality-checks.yml Continuous Quality
        scorecards.yml Supply Chain Security
        dependency-review.yml SCA
        release.yml SLSA Level 3 Release
        copilot-setup-steps.yml Copilot Env
        labeler.yml PR Auto Labelling
        setup-labels.yml Repo Label Baseline
        compile-agentic-workflows.yml Agentic Compile
      Validation
        HTMLHint Linting
        HTML5 W3C Validator
        Linkinator Links
        Lighthouse Audits Perf 90 plus A11y 100 SEO 100
      Security
        CodeQL SAST
        ZAP DAST Baseline
        Scorecard Supply Chain
        Dependency Review
        StepSecurity Harden Runner Egress Allowlist
      Build
        HTML CSS JS Minification
        SLSA Level 3 Build Provenance
        SBOM Anchore Syft SPDX 2.3
        SBOM Attestation
        Release Drafting
    Deployment
      AWS S3
        Static Hosting
        Versioning
        AES 256 Encryption
        OIDC Authentication
      CloudFront
        Global CDN
        TLS 1.3
        Security Headers
        Cache Management
      DR Strategy
        GitHub Pages Fallback
        Route53 Health Checks
        Multi Region Backup
    Automation
      8 Copilot Agents
        Task Agent
        UI Specialist
        Marketing Specialist
        Security Architect
      58 Skills Library
        Security Skills
        Quality Skills
        Compliance Skills
        Architecture Skills
```

---

## 📝 Content Structure Concepts

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2196F3", "primaryTextColor": "#1a1a2e", "lineColor": "#455A64", "secondaryColor": "#4CAF50", "tertiaryColor": "#FF9800"}}}%%
mindmap
  root((Content Model))
    Page Types
      Homepage
        Landing Page
        Service Overview
        Project Showcase
      Project Pages
        Overview Page
        Features Page
        Documentation Page
      Blog Posts
        Security Topics
        Compliance Guides
        Discordian Framework
      Service Pages
        Consulting
        Advisory
        Architecture
    Internationalization
      14 Languages
        EN Primary
        SV Swedish
        KO Korean
        AR Arabic RTL
        DA Danish
        DE German
        ES Spanish
        FI Finnish
        FR French
        HE Hebrew RTL
        JA Japanese
        NL Dutch
        NO Norwegian
        ZH Chinese
      Translation Process
        Content Creation EN
        Translation Review
        Quality Check
        Deploy All Variants
    SEO Strategy
      Technical SEO
        Sitemap XML
        Robots txt
        Canonical URLs
        Hreflang Tags
      Structured Data
        Organization
        WebPage
        FAQPage
        BreadcrumbList
      Performance
        Lighthouse Scores
        Core Web Vitals
        Image Optimization
        Minification
```

---

## 📋 ISMS Compliance

This mindmap aligns with:

- 🔗 **[Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md)** — Development practices
- 🔗 **[Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)** — Security governance
- 🔗 **[Compliance Checklist](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Compliance_Checklist.md)** — Framework alignment

<p align="center">
  <img src="https://hack23.com/icon-192.png" alt="Hack23 Logo" width="192" height="192">
</p>

<h1 align="center">📊 Hack23 Homepage — Data Model</h1>

<p align="center">
  <strong>Content Model: Static HTML/CSS Website</strong><br>
  <em>Corporate Website Content Structure and Relationships</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Owner-CEO-0A66C2?style=for-the-badge" alt="Owner"/>
  <img src="https://img.shields.io/badge/Version-1.0-555?style=for-the-badge" alt="Version"/>
  <img src="https://img.shields.io/badge/Status-Current-success?style=for-the-badge" alt="Status"/>
  <img src="https://img.shields.io/badge/Review-Quarterly-orange?style=for-the-badge" alt="Review Cycle"/>
</p>

![License](https://img.shields.io/github/license/Hack23/homepage)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/Hack23/homepage/badge)](https://scorecard.dev/viewer/?uri=github.com/Hack23/homepage)

**📋 Document Owner:** CEO | **📄 Version:** 1.0 | **📅 Last Updated:** 2026-02-20 (UTC)
**🔄 Review Cycle:** Quarterly | **⏰ Next Review:** 2026-05-20
**🏷️ Classification:** [![Public](https://img.shields.io/badge/C-Public-lightgrey?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#confidentiality-levels) [![Low](https://img.shields.io/badge/I-Low-lightgreen?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#integrity-levels) [![Standard](https://img.shields.io/badge/A-Standard-lightgreen?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#availability-levels)

---

## 📚 Related Documentation

| Document | Focus | Description |
|----------|-------|-------------|
| **[🏛️ Architecture](ARCHITECTURE.md)** | C4 Model | System structure and containers |
| **[📊 Data Model](DATA_MODEL.md)** | Data | Content model (this document) |
| **[🔄 Flowchart](FLOWCHART.md)** | Processes | Content and deployment workflows |
| **[📈 State Diagram](STATEDIAGRAM.md)** | States | Content and deployment lifecycle |
| **[🛡️ Security Architecture](SECURITY_ARCHITECTURE.md)** | Security | Security controls |
| **[🛡️ CRA Assessment](CRA-ASSESSMENT.md)** | Compliance | EU Cyber Resilience Act conformity |
| **[🚀 Future Data Model](FUTURE_DATA_MODEL.md)** | Roadmap | Planned content model enhancements |

---

## 🎯 Overview

The Hack23 homepage is a static HTML/CSS website with no backend database. The "data model" represents the content structure, page relationships, metadata schema, and SEO structured data that form the information architecture of hack23.com.

### Content Architecture Principles

- ✅ **Static-First**: All content is pre-rendered HTML — no dynamic data loading
- ✅ **Multilingual**: 14 language variants with consistent structure
- ✅ **SEO-Optimized**: Schema.org structured data on every page
- ✅ **Accessible**: WCAG 2.1 AA compliant content structure
- ✅ **Security-Transparent**: Public ISMS documentation integrated into site

---

## 📐 Content Entity Model

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#e3f2fd", "primaryTextColor": "#01579b", "lineColor": "#0288d1", "secondaryColor": "#f1f8e9", "tertiaryColor": "#fff8e1"}}}%%
erDiagram
    WEBSITE ||--o{ PAGE : contains
    PAGE ||--o{ TRANSLATION : "has_variants"
    PAGE ||--o{ META_TAG : "has_metadata"
    PAGE ||--o{ BREADCRUMB : "has_navigation"
    PAGE ||--o{ SCHEMA_ORG : "has_structured_data"

    PROJECT ||--|{ PROJECT_PAGE : "has_overview"
    PROJECT ||--|{ FEATURES_PAGE : "has_features"
    PROJECT ||--|{ DOCS_PAGE : "has_documentation"

    BLOG_POST ||--|| PAGE : "is_a"
    SERVICE_PAGE ||--|| PAGE : "is_a"

    WEBSITE {
        string domain "hack23.com"
        string hosting "AWS S3 + CloudFront"
        int pageCount "74+"
        int languageCount "14"
    }

    PAGE {
        string filename PK
        string title
        string description
        string lang
        string type "page|blog|project|docs|features"
        string canonical_url
    }

    TRANSLATION {
        string filename PK
        string lang "en|sv|ko|ar|da|de|es|fi|fr|he|ja|nl|no|zh"
        string suffix "_sv|_ko|_ar|..."
        string original_page FK
    }

    PROJECT {
        string name PK
        string repo_url
        string description
        string tech_stack
    }

    META_TAG {
        string property
        string content
        string type "og|twitter|standard"
    }

    SCHEMA_ORG {
        string type "Organization|WebPage|FAQPage|BreadcrumbList"
        string json_ld
    }
```

---

## 📄 Page Types

### Page Hierarchy

| Type | Count | Pattern | Description |
|------|-------|---------|-------------|
| **Homepage** | 1 | `index.html` | Main landing page |
| **Project Overview** | 6 | `{project}.html` | Project showcase pages |
| **Project Features** | 6 | `{project}-features.html` | Feature detail pages |
| **Project Docs** | 6 | `{project}-docs.html` | Documentation with ISMS cards |
| **Blog Posts** | 20+ | `blog-{topic}.html` | Security and compliance articles |
| **Service Pages** | 3 | `services.html`, etc. | Consulting offerings |
| **Translations** | 50+ | `*_{lang}.html` | Localized page variants |
| **Sitemaps** | 14 | `sitemap_{lang}.html` | Per-language HTML sitemaps |
| **Utility** | 5 | `404.html`, etc. | Error pages, robots.txt |

### Project Page Structure

Each open-source project follows a three-page pattern:

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2196F3", "primaryTextColor": "#1a1a2e", "lineColor": "#455A64", "secondaryColor": "#e8f5e9", "tertiaryColor": "#fff8e1", "primaryBorderColor": "#1565C0"}}}%%
graph TD
    P[Project Overview<br/>project.html] --> F[Features Page<br/>project-features.html]
    P --> D[Documentation Page<br/>project-docs.html]
    D --> ISMS[ISMS Documentation Cards<br/>Links to GitHub repo docs]

    style P fill:#2979FF,stroke:#0D47A1,color:#fff
    style F fill:#00C853,stroke:#00796B,color:#fff
    style D fill:#FFD600,stroke:#F57F17,color:#000
```

### Projects Documented

| Project | Overview | Features | Docs |
|---------|----------|----------|------|
| **CIA** | `cia-project.html` | `cia-features.html` | `cia-docs.html` |
| **CIA Compliance Manager** | `compliance-manager.html` | `cia-compliance-manager-features.html` | `cia-compliance-manager-docs.html` |
| **Black Trigram** | `black-trigram.html` | `black-trigram-features.html` | `black-trigram-docs.html` |
| **EU Parliament MCP** | `european-parliament-mcp.html` | `european-parliament-mcp-features.html` | `european-parliament-mcp-docs.html` |
| **Riksdagsmonitor** | `riksdagsmonitor.html` | `riksdagsmonitor-features.html` | `riksdagsmonitor-docs.html` |
| **EU Parliament Monitor** | `euparliamentmonitor.html` | `euparliamentmonitor-features.html` | `euparliamentmonitor-docs.html` |

---

## 🌍 Internationalization Model

### Language Support Matrix

| Language | Code | Suffix | Status |
|----------|------|--------|--------|
| English | en | (none) | ✅ Primary |
| Swedish | sv | `_sv` | ✅ Complete |
| Korean | ko | `_ko` | ✅ Complete |
| Arabic | ar | `_ar` | ✅ Complete (RTL) |
| Danish | da | `_da` | ✅ Complete |
| German | de | `_de` | ✅ Complete |
| Spanish | es | `_es` | ✅ Complete |
| Finnish | fi | `_fi` | ✅ Complete |
| French | fr | `_fr` | ✅ Complete |
| Hebrew | he | `_he` | ✅ Complete (RTL) |
| Japanese | ja | `_ja` | ✅ Complete |
| Dutch | nl | `_nl` | ✅ Complete |
| Norwegian | no | `_no` | ✅ Complete |
| Chinese | zh | `_zh` | ✅ Complete |

---

## 📋 SEO Structured Data Model

### Schema.org Types Used

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2196F3", "primaryTextColor": "#1a1a2e", "lineColor": "#455A64", "secondaryColor": "#e8f5e9", "tertiaryColor": "#fff8e1", "primaryBorderColor": "#1565C0"}}}%%
graph TD
    Org[Organization<br/>hack23.com] --> WP[WebPage<br/>Every page]
    WP --> BL[BreadcrumbList<br/>Navigation path]
    WP --> FAQ[FAQPage<br/>FAQ sections]
    Org --> WS[WebSite<br/>Site metadata]

    style Org fill:#2979FF,stroke:#0D47A1,color:#fff
    style WP fill:#00C853,stroke:#00796B,color:#fff
    style FAQ fill:#FFD600,stroke:#F57F17,color:#000
```

---

## 🔒 Data Security

### Classification per ISMS

| Data Type | Confidentiality | Integrity | Availability |
|-----------|----------------|-----------|--------------|
| **Website Content** | Public | Low | Standard |
| **Blog Posts** | Public | Low | Standard |
| **ISMS Documentation** | Public | Medium | Standard |
| **Configuration** | Internal | Medium | High |
| **Deployment Secrets** | Confidential | High | High |

All data classification follows the **[Hack23 Classification Framework](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md)**.

### Related ISMS Policies

- 🔗 **[Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md)** — Content development standards
- 🔗 **[Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)** — Data handling requirements
- 🔗 **[Cryptography Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Cryptography_Policy.md)** — Encryption standards for data at rest

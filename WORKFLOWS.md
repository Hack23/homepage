<p align="center">
  <img src="https://hack23.com/icon-192.png" alt="Hack23 Logo" width="192" height="192">
</p>

<h1 align="center">🔄 Hack23 Homepage — CI/CD Workflows</h1>

<p align="center">
  <strong>GitHub Actions Pipeline: Build, Validate, Scan, Deploy</strong><br>
  <em>DevSecOps Workflow Documentation for hack23.com</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Owner-CEO-0A66C2?style=for-the-badge" alt="Owner"/>
  <img src="https://img.shields.io/badge/Version-1.2-555?style=for-the-badge" alt="Version"/>
  <img src="https://img.shields.io/badge/Status-Current-success?style=for-the-badge" alt="Status"/>
  <img src="https://img.shields.io/badge/Review-Quarterly-orange?style=for-the-badge" alt="Review Cycle"/>
</p>

![License](https://img.shields.io/github/license/Hack23/homepage)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/Hack23/homepage/badge)](https://scorecard.dev/viewer/?uri=github.com/Hack23/homepage)
[![Verify and Deploy](https://github.com/Hack23/homepage/actions/workflows/main.yml/badge.svg)](https://github.com/Hack23/homepage/actions/workflows/main.yml)
[![SLSA 3](https://slsa.dev/images/gh-badge-level3.svg)](https://slsa.dev/spec/v1.0/levels)

**📋 Document Owner:** CEO | **📄 Version:** 1.2 | **📅 Last Updated:** 2026-04-21 (UTC)
**🔄 Review Cycle:** Quarterly | **⏰ Next Review:** 2026-07-21
**🏷️ Classification:** [![Public](https://img.shields.io/badge/C-Public-lightgrey?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#confidentiality-levels) [![Low](https://img.shields.io/badge/I-Low-lightgreen?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#integrity-levels) [![Standard](https://img.shields.io/badge/A-Standard-lightgreen?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#availability-levels)

---

## 📚 Related Architecture Documentation

| Document | Focus | Description |
|----------|-------|-------------|
| **[🏛️ Architecture](ARCHITECTURE.md)** | C4 Model | System structure and deployment |
| **[🛡️ Security Architecture](SECURITY_ARCHITECTURE.md)** | Security | Defense-in-depth security controls |
| **[🎯 Threat Model](THREAT_MODEL.md)** | Threats | STRIDE/MITRE ATT&CK threat analysis |
| **[🔄 Flowchart](FLOWCHART.md)** | Processes | CI/CD and content workflows |
| **[📈 State Diagram](STATEDIAGRAM.md)** | States | Deployment and content lifecycle |
| **[🔄 BCP Plan](BCPPlan.md)** | Resilience | Business continuity & recovery |
| **[💰 Financial & Security Plan](FinancialSecurityPlan.md)** | Cost | Infrastructure cost & security investment |
| **[🔚 End-of-Life Strategy](End-of-Life-Strategy.md)** | Lifecycle | Technology lifecycle management |
| **[🛡️ CRA Assessment](CRA-ASSESSMENT.md)** | Compliance | EU Cyber Resilience Act conformity |
| **[🚀 Future Workflows](FUTURE_WORKFLOWS.md)** | Roadmap | Planned workflow improvements |

---

## Table of Contents

- [Overview](#overview)
- [CI/CD Pipeline Architecture](#cicd-pipeline-architecture)
- [Workflow Catalog](#workflow-catalog)
  - [1. Verify and Deploy (main.yml)](#1-verify-and-deploy-mainyml)
  - [2. Quality Checks (quality-checks.yml)](#2-quality-checks-quality-checksyml)
  - [3. Verify Pull Request (pullrequest.yml)](#3-verify-pull-request-pullrequestyml)
  - [4. Scorecard Supply-Chain Security (scorecards.yml)](#4-scorecard-supply-chain-security-scorecardsyml)
  - [5. Dependency Review (dependency-review.yml)](#5-dependency-review-dependency-reviewyml)
  - [6. Copilot Setup Steps (copilot-setup-steps.yml)](#6-copilot-setup-steps-copilot-setup-stepsyml)
  - [7. Build, Attest and Release (release.yml)](#7-build-attest-and-release-releaseyml)
  - [8. Pull Request Automatic Labeler (labeler.yml)](#8-pull-request-automatic-labeler-labeleryml)
  - [9. Setup Repository Labels (setup-labels.yml)](#9-setup-repository-labels-setup-labelsyml)
  - [10. Compile Agentic Workflows (compile-agentic-workflows.yml)](#10-compile-agentic-workflows-compile-agentic-workflowsyml)
- [Security Controls](#security-controls)
- [Performance Optimization](#performance-optimization)
- [Monitoring and Observability](#monitoring-and-observability)
- [ISMS Compliance Mapping](#isms-compliance-mapping)

---

## Overview

The Hack23 homepage repository implements a comprehensive CI/CD pipeline using **10 GitHub Actions workflows** to ensure secure, high-quality deployments of the static website to AWS S3 + CloudFront. The pipeline integrates multiple security scanning tools, quality checks, and automated deployment processes aligned with the [Hack23 Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md).

### Key Objectives

- **Security-First**: Multiple security scanning layers (ZAP, CodeQL, Scorecard, Dependency Review)
- **Quality Assurance**: Automated HTML validation, link checking, and performance audits
- **Continuous Deployment**: Automated deployment to AWS S3 + CloudFront with cache invalidation
- **Supply Chain Security**: SLSA-inspired practices with action pinning and security hardening
- **Performance**: Comprehensive caching strategy for faster builds and reduced costs

### Technology Stack

- **Platform**: GitHub Actions
- **Deployment**: AWS S3, CloudFront, AWS IAM (OIDC)
- **Security**: StepSecurity Harden Runner, ZAP, CodeQL, OpenSSF Scorecard
- **Quality**: HTMLHint, Linkinator, Lighthouse CI, HTML5 Validator
- **Optimization**: Minify Action, GitHub Actions Cache

---

## CI/CD Pipeline Architecture

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2196F3", "primaryTextColor": "#1a1a2e", "lineColor": "#455A64", "secondaryColor": "#e8f5e9", "tertiaryColor": "#fff8e1", "primaryBorderColor": "#1565C0"}}}%%
graph TB
    subgraph "Development Phase"
        A[Developer Push] --> B{Branch?}
        B -->|Feature Branch| C[PR Created]
        B -->|Master Branch| D[Main Pipeline]
    end
    
    subgraph "Pull Request Pipeline"
        C --> E[Harden Runner]
        E --> F[HTML Validation]
        F --> G[Link Checking]
        G --> H[Test Minification]
        H --> I[CodeQL Analysis]
        I --> J{All Checks Pass?}
        J -->|No| K[Block Merge]
        J -->|Yes| L[Allow Merge]
    end
    
    subgraph "Main Deployment Pipeline"
        D --> M[Harden Runner]
        M --> N[Checkout & Cache]
        N --> O[AWS OIDC Auth]
        O --> P[Minify Assets]
        P --> Q[Deploy to S3]
        Q --> R[Set Cache Headers]
        R --> S[Invalidate CloudFront]
        S --> T[Lighthouse Audit]
        T --> U[ZAP Security Scan]
        U --> V{Deployment Success?}
        V -->|Yes| W[Production Live]
        V -->|No| X[Rollback/Alert]
    end
    
    subgraph "Continuous Monitoring"
        Y[Scheduled: Weekly] --> Z[Scorecard Analysis]
        Z --> AA[SARIF Upload]
        AA --> AB[Security Dashboard]
        
        AC[PR Events] --> AD[Dependency Review]
        AD --> AE[Vulnerability Check]
        AE --> AF{Vulnerabilities?}
        AF -->|Yes| AG[Block PR]
        AF -->|No| AH[Continue]
    end
    
    subgraph "Quality Assurance"
        AI[Every Push] --> AJ[HTML Validation]
        AJ --> AK[Link Checker]
        AK --> AL[Quality Reports]
        AL --> AM[Artifacts Stored]
    end

    classDef default fill:#e3f2fd,stroke:#1565C0,stroke-width:2px,color:#1a1a2e
    classDef primary fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#ffffff
    classDef success fill:#4CAF50,stroke:#2E7D32,stroke-width:2px,color:#ffffff
    classDef warning fill:#FF9800,stroke:#F57C00,stroke-width:2px,color:#ffffff
    classDef danger fill:#D32F2F,stroke:#B71C1C,stroke-width:2px,color:#ffffff
    classDef info fill:#455A64,stroke:#263238,stroke-width:2px,color:#ffffff
    class K danger
    class Q success
    class W success
    class X danger
    class AG danger
```

### Pipeline Flow

1. **Pre-Deployment Checks**: Security hardening, dependency caching
2. **Build Phase**: Minification of HTML, CSS, JS
3. **Deployment Phase**: S3 sync, cache header configuration, CloudFront invalidation
4. **Post-Deployment**: Lighthouse performance audit, ZAP security scan
5. **Continuous**: Scorecard analysis, dependency review, quality checks

---

## Workflow Catalog

### 1. Verify and Deploy (main.yml)

**Trigger**: Push to `master` branch  
**Purpose**: Production deployment with security and performance validation  
**Permissions**: `write-all` (deployment requires AWS and GitHub write access)

#### Workflow Steps

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2196F3", "primaryTextColor": "#1a1a2e", "lineColor": "#455A64", "secondaryColor": "#e8f5e9", "tertiaryColor": "#fff8e1", "primaryBorderColor": "#1565C0"}}}%%
graph LR
    A[Checkout] --> B[Cache Setup]
    B --> C[AWS OIDC Auth]
    C --> D[Minify Assets]
    D --> E[S3 Sync]
    E --> F[Cache Headers]
    F --> G[CloudFront Invalidation]
    G --> H[Lighthouse Audit]
    H --> I[ZAP Scan]

    classDef default fill:#e3f2fd,stroke:#1565C0,stroke-width:2px,color:#1a1a2e
    classDef primary fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#ffffff
    classDef success fill:#4CAF50,stroke:#2E7D32,stroke-width:2px,color:#ffffff
    classDef warning fill:#FF9800,stroke:#F57C00,stroke-width:2px,color:#ffffff
    classDef danger fill:#D32F2F,stroke:#B71C1C,stroke-width:2px,color:#ffffff
    classDef info fill:#455A64,stroke:#263238,stroke-width:2px,color:#ffffff
```

#### Key Features

**1. Security Hardening**
- **StepSecurity Harden Runner** (v2.14.0): Network egress policy enforcement
- **Allowed Endpoints**: Strict allowlist of 40+ required domains
- **Blocks**: All unauthorized network traffic

**2. AWS Deployment**
- **OIDC Authentication**: No long-lived credentials (IAM role assumption)
- **Role**: `arn:aws:iam::172017021075:role/GithubWorkFlowRole`
- **Region**: `us-east-1`
- **S3 Bucket**: `amazon-cloudfront-secure-static-site-s3bucketroot-14oliw5cmta06`

**3. Asset Optimization**
- **Minification**: HTML, CSS, JS using `dra1ex/minify-action@v1.0.3`
- **Cache Headers**: Optimized TTL per asset type
  - CSS/JS/Images: 1 year (`max-age=31536000, immutable`)
  - HTML: 1 hour (`max-age=3600, must-revalidate`)
  - Metadata: 1 day (`max-age=86400`)
  - Fonts: 1 year (`max-age=31536000, immutable`)

**4. CloudFront Management**
- **Discovery**: Automatic distribution ID lookup from CloudFormation stack
- **Invalidation**: Full cache invalidation (`/*`) after deployment
- **Fallback**: Direct CloudFront API query if stack lookup fails

**5. Performance Auditing**
- **Lighthouse CI**: Performance, accessibility, SEO, best practices
- **Budget Enforcement**: `budget.json` thresholds
- **Artifacts**: Reports uploaded and publicly accessible

**6. Security Scanning**
- **ZAP Full Scan**: OWASP Top 10 vulnerability detection
- **Target**: `https://hack23.com/`
- **Docker Image**: `ghcr.io/zaproxy/zaproxy:stable`

#### Caching Strategy

Three-layer caching approach (see [WORKFLOW_CACHING_GUIDE.md](WORKFLOW_CACHING_GUIDE.md)):

1. **APT Packages**: `/var/cache/apt/archives`
2. **NPM Dependencies**: `~/.npm` (minify tools)
3. **Docker Layers**: `/tmp/.buildx-cache` (ZAP image)

**Expected Performance**: 20-40% faster builds, 10-20% cost reduction

#### Security Controls Mapping

| Control | Implementation | ISMS Reference |
|---------|----------------|----------------|
| SC-7 (Boundary Protection) | Harden Runner egress policy | [Network Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Network_Security_Policy.md) |
| IA-2 (Authentication) | AWS OIDC with IAM roles | [Access Control Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Access_Control_Policy.md) |
| CM-3 (Change Control) | Automated deployment gates | [Change Management](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Change_Management.md) |
| RA-5 (Vulnerability Scanning) | ZAP security scan | [Vulnerability Management](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Vulnerability_Management.md) |
| SC-13 (Cryptography) | TLS 1.3 via CloudFront | [Cryptography Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Cryptography_Policy.md) |

---

### 2. Quality Checks (quality-checks.yml)

**Trigger**: Push to `master` or pull request to `master`  
**Purpose**: Continuous quality assurance for HTML and links  
**Permissions**: `contents: read`

#### Workflow Architecture

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2196F3", "primaryTextColor": "#1a1a2e", "lineColor": "#455A64", "secondaryColor": "#e8f5e9", "tertiaryColor": "#fff8e1", "primaryBorderColor": "#1565C0"}}}%%
graph TB
    subgraph "Job 1: HTML Validation"
        A1[Checkout] --> A2[Setup Node.js 24]
        A2 --> A3[Cache NPM]
        A3 --> A4[Install HTMLHint]
        A4 --> A5[Validate 74 HTML Files]
        A5 --> A6[Upload Report]
    end
    
    subgraph "Job 2: Link Checking"
        B1[Checkout] --> B2[Setup Node.js 24]
        B2 --> B3[Cache NPM & APT]
        B3 --> B4[Install Linkinator v6]
        B4 --> B5[Install jq]
        B5 --> B6[Start HTTP Server]
        B6 --> B7[Check Internal Links]
        B7 --> B8[Check External Links]
        B8 --> B9[Upload Reports]
    end
    
    subgraph "Job 3: Summary"
        C1[Wait for Jobs] --> C2[Display Summary]
        C2 --> C3[List Artifacts]
    end
    
    A6 --> C1
    B9 --> C1

    classDef default fill:#e3f2fd,stroke:#1565C0,stroke-width:2px,color:#1a1a2e
    classDef primary fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#ffffff
    classDef success fill:#4CAF50,stroke:#2E7D32,stroke-width:2px,color:#ffffff
    classDef warning fill:#FF9800,stroke:#F57C00,stroke-width:2px,color:#ffffff
    classDef danger fill:#D32F2F,stroke:#B71C1C,stroke-width:2px,color:#ffffff
    classDef info fill:#455A64,stroke:#263238,stroke-width:2px,color:#ffffff
```

#### Job 1: HTML Validation

**Technology**: HTMLHint (global npm installation)  
**Scope**: All 74 HTML files in repository root  
**Configuration**: `.htmlhintrc`

**Validation Rules**:
- DOCTYPE presence
- Tag naming conventions
- Attribute formatting
- Proper nesting
- Accessibility hints

**Artifacts**: `htmlhint-report.txt` (30-day retention)

#### Job 2: Link Checking

**Technology**: Linkinator v6 (v7.5.2 has module resolution bug)  
**Scope**: Internal and external links

**Internal Links**:
- Local HTTP server on port 8080
- Recursive crawling of all pages
- Skip external domains
- Timeout: 30s, Concurrency: 25

**External Links** (Sample):
- Target: `https://hack23.com/`
- Skip: Google Fonts, GitHub (rate limiting)
- Timeout: 30s

**Artifacts**: 
- `internal-links-report.json`
- `external-links-report.json`

#### Job 3: Summary

Consolidates results from both jobs and lists available artifacts.

---

### 3. Verify Pull Request (pullrequest.yml)

**Trigger**: Push to any branch  
**Purpose**: Pre-merge validation with strict quality gates  
**Permissions**: `checks: write`, `security-events: write`, `pull-requests: read`

#### Workflow Steps

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2196F3", "primaryTextColor": "#1a1a2e", "lineColor": "#455A64", "secondaryColor": "#e8f5e9", "tertiaryColor": "#fff8e1", "primaryBorderColor": "#1565C0"}}}%%
graph LR
    A[Harden Runner] --> B[HTML5 Validation]
    B --> C[Link Checking]
    C --> D[Test Minification]
    D --> E[Verify Results]
    E --> F[CodeQL Init]
    F --> G[CodeQL Analysis]
    G --> H{All Pass?}
    H -->|Yes| I[Allow Merge]
    H -->|No| J[Block Merge]

    classDef default fill:#e3f2fd,stroke:#1565C0,stroke-width:2px,color:#1a1a2e
    classDef primary fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#ffffff
    classDef success fill:#4CAF50,stroke:#2E7D32,stroke-width:2px,color:#ffffff
    classDef warning fill:#FF9800,stroke:#F57C00,stroke-width:2px,color:#ffffff
    classDef danger fill:#D32F2F,stroke:#B71C1C,stroke-width:2px,color:#ffffff
    classDef info fill:#455A64,stroke:#263238,stroke-width:2px,color:#ffffff
    class J danger
```

#### Key Features

**1. Strict Security**
- **Harden Runner**: `egress-policy: block` with strict endpoint allowlist
- **Disable sudo**: Prevents privilege escalation
- **Minimal endpoints**: Only required services (GitHub, npm, validator.nu)

**2. HTML5 Validation**
- **Tool**: `Cyb3r-Jak3/html5validator-action@v8.0.0`
- **Standard**: W3C HTML5 specification
- **Scope**: All HTML files
- **CSS Validation**: Disabled (false flag)

**3. Link Verification**
- **Linkinator v6**: Same as quality-checks.yml
- **Failure Mode**: **Hard fail on broken internal links**
- **Exit Code**: 1 if any broken links detected

**4. Minification Testing**
- **Pre-flight Check**: Verify minify-action works before deployment
- **Validation**: Ensure `index.html` and `styles.css` exist post-minification
- **File Count**: Verify all HTML/CSS files survive minification

**5. Static Analysis**
- **CodeQL**: JavaScript security analysis
- **Language**: JavaScript (for any inline scripts)
- **SARIF Upload**: Results to GitHub Security Dashboard

#### Quality Gates

| Gate | Failure Impact | Bypass |
|------|----------------|--------|
| HTML5 Validation | **Blocks merge** | None |
| Internal Links | **Blocks merge** | None |
| Minification | **Blocks merge** | None |
| CodeQL | Warning only | Non-blocking |

---

### 4. Scorecard Supply-Chain Security (scorecards.yml)

**Trigger**: Weekly (Tuesday 07:20 UTC), push to `master`, branch protection changes  
**Purpose**: OpenSSF Scorecard analysis for supply-chain security  
**Permissions**: `security-events: write`, `id-token: write`, `contents: read`, `actions: read`

#### Workflow Architecture

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2196F3", "primaryTextColor": "#1a1a2e", "lineColor": "#455A64", "secondaryColor": "#e8f5e9", "tertiaryColor": "#fff8e1", "primaryBorderColor": "#1565C0"}}}%%
graph TB
    A[Scheduled/Triggered] --> B[Harden Runner]
    B --> C[Checkout]
    C --> D[Cache APT]
    D --> E[Run Scorecard Analysis]
    E --> F[Generate SARIF]
    F --> G[Upload Artifact]
    G --> H[Upload to Security Dashboard]
    H --> I[Publish to OpenSSF API]

    classDef default fill:#e3f2fd,stroke:#1565C0,stroke-width:2px,color:#1a1a2e
    classDef primary fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#ffffff
    classDef success fill:#4CAF50,stroke:#2E7D32,stroke-width:2px,color:#ffffff
    classDef warning fill:#FF9800,stroke:#F57C00,stroke-width:2px,color:#ffffff
    classDef danger fill:#D32F2F,stroke:#B71C1C,stroke-width:2px,color:#ffffff
    classDef info fill:#455A64,stroke:#263238,stroke-width:2px,color:#ffffff
```

#### Scorecard Checks

The OpenSSF Scorecard evaluates **18 security checks**:

| Check Category | Checks | Score Impact |
|----------------|--------|--------------|
| **Code Quality** | Code-Review, Maintained | Repository activity |
| **Supply Chain** | Pinned-Dependencies, Dependency-Update-Tool | Action/dependency security |
| **Vulnerability Management** | Vulnerabilities, Security-Policy | CVE disclosure |
| **Build Security** | Signed-Releases, Token-Permissions | Release integrity |
| **Branch Protection** | Branch-Protection | Protected branches |
| **Security Tooling** | SAST, Dangerous-Workflow | Security automation |

**Current Badge**: [![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/Hack23/homepage/badge)](https://scorecard.dev/viewer/?uri=github.com/Hack23/homepage)

#### Outputs

1. **SARIF Artifact**: `results.sarif` (5-day retention)
2. **Security Dashboard**: GitHub Code Scanning alerts
3. **OpenSSF Badge**: Public scorecard at api.securityscorecards.dev

#### ISMS Alignment

| ISO 27001 Control | Implementation |
|-------------------|----------------|
| A.8.30 (Outsourcing) | Scorecard validates third-party actions |
| A.8.8 (Secure Coding) | SAST and dependency checks |
| A.8.32 (Change Management) | Branch protection validation |

---

### 5. Dependency Review (dependency-review.yml)

**Trigger**: Pull request to any branch  
**Purpose**: Detect vulnerable dependencies before merge  
**Permissions**: `contents: read`

#### Workflow Steps

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2196F3", "primaryTextColor": "#1a1a2e", "lineColor": "#455A64", "secondaryColor": "#e8f5e9", "tertiaryColor": "#fff8e1", "primaryBorderColor": "#1565C0"}}}%%
graph LR
    A[PR Opened] --> B[Harden Runner]
    B --> C[Checkout]
    C --> D[Cache APT]
    D --> E[Dependency Review]
    E --> F{Vulnerabilities?}
    F -->|Yes| G[Comment in PR + Block]
    F -->|No| H[Allow Merge]

    classDef default fill:#e3f2fd,stroke:#1565C0,stroke-width:2px,color:#1a1a2e
    classDef primary fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#ffffff
    classDef success fill:#4CAF50,stroke:#2E7D32,stroke-width:2px,color:#ffffff
    classDef warning fill:#FF9800,stroke:#F57C00,stroke-width:2px,color:#ffffff
    classDef danger fill:#D32F2F,stroke:#B71C1C,stroke-width:2px,color:#ffffff
    classDef info fill:#455A64,stroke:#263238,stroke-width:2px,color:#ffffff
    class G danger
```

#### Key Features

**1. Automated Scanning**
- **Action**: `actions/dependency-review-action@v4.8.2`
- **Scope**: All manifest changes in PR
- **Databases**: GitHub Advisory Database, npm audit

**2. PR Integration**
- **Comment Summary**: Always posts findings in PR
- **Blocking**: Required check prevents merging vulnerable dependencies
- **Severity Filter**: Configurable thresholds

**3. Vulnerability Sources**
- GitHub Advisory Database
- npm Security Advisories
- NVD/CVE Database

#### Sample Output

```markdown
### Dependency Review Summary

⚠️ 2 vulnerabilities detected:

| Package | Version | Severity | Advisory |
|---------|---------|----------|----------|
| lodash | 4.17.19 | High | GHSA-xxx |
| axios | 0.19.2 | Moderate | CVE-2020-xxx |

**Recommendation**: Update to lodash@4.17.21 and axios@0.21.1
```

---

### 6. Copilot Setup Steps (copilot-setup-steps.yml)

**Trigger**: Manual (`workflow_dispatch`), changes to workflow file  
**Purpose**: Setup environment for GitHub Copilot agents  
**Permissions**: Comprehensive read access, write to issues/PRs

#### Workflow Configuration

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2196F3", "primaryTextColor": "#1a1a2e", "lineColor": "#455A64", "secondaryColor": "#e8f5e9", "tertiaryColor": "#fff8e1", "primaryBorderColor": "#1565C0"}}}%%
graph LR
    A[Workflow Dispatch] --> B[Checkout]
    B --> C[Setup Environment]
    C --> D[Copilot Agent Ready]

    classDef default fill:#e3f2fd,stroke:#1565C0,stroke-width:2px,color:#1a1a2e
    classDef primary fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#ffffff
    classDef success fill:#4CAF50,stroke:#2E7D32,stroke-width:2px,color:#ffffff
    classDef warning fill:#FF9800,stroke:#F57C00,stroke-width:2px,color:#ffffff
    classDef danger fill:#D32F2F,stroke:#B71C1C,stroke-width:2px,color:#ffffff
    classDef info fill:#455A64,stroke:#263238,stroke-width:2px,color:#ffffff
```

#### Key Features

**1. Secret Management**
- **PAT Token**: `COPILOT_MCP_GITHUB_PERSONAL_ACCESS_TOKEN`
- **Environment Variables**: `GITHUB_TOKEN`, `GITHUB_PERSONAL_ACCESS_TOKEN`
- **MCP Server**: GitHub MCP with organization-wide access

**2. Permissions**
Balanced permissions for Copilot operations:
- **Read**: contents, actions, checks, deployments, security-events
- **Write**: issues, pull-requests

**3. MCP Integration**
Enables Copilot access to:
- All Hack23 repositories (via PAT)
- ISMS policies from Hack23/ISMS-PUBLIC
- Cross-repository code search
- Security documentation references

---

### 7. Build, Attest and Release (release.yml)

**Trigger**: Tag push (`v*`), manual (`workflow_dispatch`)  
**Purpose**: Automated release with SLSA Build Level 3 attestations and documentation as code  
**Permissions**: Minimal per job (read-all default)

#### Workflow Architecture

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2196F3", "primaryTextColor": "#1a1a2e", "lineColor": "#455A64", "secondaryColor": "#e8f5e9", "tertiaryColor": "#fff8e1", "primaryBorderColor": "#1565C0"}}}%%
graph TB
    subgraph "Job 1: Prepare"
        A[Checkout default branch] --> B[Generate Documentation]
        B --> C[HTML Validation]
        C --> D[Lighthouse Audits]
        D --> E[Accessibility Reports]
        E --> F[Commit to docs/]
    end
    
    subgraph "Job 2: Build"
        G[Minify Assets] --> H[Create ZIP]
        H --> I[Generate SBOM]
        I --> J[Build Provenance]
        J --> K[SBOM Attestation]
    end
    
    subgraph "Job 3: Release"
        L[Create GitHub Release] --> M[Attach Artifacts]
        M --> N[Deploy to gh-pages]
    end
    
    F --> G
    K --> L

    classDef default fill:#e3f2fd,stroke:#1565C0,stroke-width:2px,color:#1a1a2e
    classDef primary fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#ffffff
    classDef success fill:#4CAF50,stroke:#2E7D32,stroke-width:2px,color:#ffffff
    classDef warning fill:#FF9800,stroke:#F57C00,stroke-width:2px,color:#ffffff
    classDef danger fill:#D32F2F,stroke:#B71C1C,stroke-width:2px,color:#ffffff
    classDef info fill:#455A64,stroke:#263238,stroke-width:2px,color:#ffffff
    class N success
```

#### Key Features

**1. Documentation as Code**
- **HTML Validation**: All pages validated with html-validate
- **Lighthouse Audits**: Performance, accessibility, SEO reports for each page
- **WCAG 2.1 AA Compliance**: Automated accessibility verification
- **Security Reports**: OWASP ZAP baseline scan summaries
- **Auto-Commit**: All reports committed to `docs/` directory

**Artifacts Generated**:
- `docs/html-validation.txt` - W3C standards compliance
- `docs/lighthouse-*.html` - Individual page audits
- `docs/lighthouse-summary.html` - Aggregated performance metrics
- `docs/accessibility-report.html` - WCAG compliance summary
- `docs/security-report.html` - Security posture
- `docs/RELEASE_SUMMARY.md` - Release metadata
- `docs/VERSION.txt` - Version tracking

**2. SLSA Build Level 3 Attestations**
- **Build Provenance**: Cryptographic attestation of build process
  - File: `homepage-vX.Y.Z.zip.intoto.jsonl`
  - Signed with GitHub OIDC (non-falsifiable)
  - Includes: Builder identity, build parameters, dependencies
  
- **SBOM Attestation**: Software Bill of Materials
  - File: `homepage-vX.Y.Z.spdx.json.intoto.jsonl`
  - Format: SPDX 2.3
  - Generator: Anchore Syft (v0.22.2)
  - Contains: All dependencies, licenses, relationships

**Verification**:
```bash
# Verify build provenance
gh attestation verify homepage-v1.0.0.zip --owner Hack23

# View SBOM
cat homepage-v1.0.0.spdx.json | jq '.packages[] | {name, version, licenses}'
```

**3. Release Automation**
- **Release Drafter**: Automated changelog generation
  - Categorizes PRs: features, bugs, docs, security, etc.
  - Semantic versioning: major/minor/patch detection
  - Quality metrics: Test coverage, Lighthouse scores
  
- **Asset Publishing**:
  - Release ZIP: Minified static site
  - SBOM: `homepage-vX.Y.Z.spdx.json`
  - Attestations: Build provenance + SBOM attestation
  
- **Dual Deployment**:
  - **GitHub Pages**: Backup deployment at `hack23.github.io/homepage`
  - **S3/CloudFront**: Primary deployment via `main.yml` on master

**4. Security Hardening**
- **Minimal Permissions**: Read-all default, write only where needed
- **SHA-Pinned Actions**: All actions use commit SHAs
- **Harden Runner**: Network egress auditing on all jobs
- **Pre-release Detection**: Auto-detects pre-release from tag name

#### Job Details

**Job 1: Prepare (Runs ~5-10 minutes)**
- Checks out default branch (not detached HEAD)
- Generates comprehensive documentation reports
- Commits reports to `docs/` directory
- Sets up outputs for downstream jobs

**Job 2: Build (Runs ~2-3 minutes)**
- Minifies HTML/CSS/JS assets
- Creates release ZIP artifact
- Generates SBOM using Anchore SBOM Action
- Creates attestations using GitHub's attest actions

**Job 3: Release (Runs ~2-3 minutes)**
- Creates GitHub Release with Release Drafter
- Attaches ZIP, SBOM, and attestation files
- Deploys minified artifact to GitHub Pages
- Generates release summary

#### Security Controls Mapping

| Control | Implementation | ISMS Reference |
|---------|----------------|----------------|
| SC-28 (Data Integrity) | SLSA Build Level 3 attestations | [Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md) |
| CM-3 (Change Control) | Release workflow with approval gates | [Change Management](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Change_Management.md) |
| SA-15 (Development Process) | Documentation as code, SBOM | [Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md) |
| SR-4 (Provenance) | Cryptographic build provenance | [Supply Chain Security](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md#supply-chain-security) |
| SA-10 (Developer Testing) | Automated quality reports | [Change Management](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Change_Management.md) |

#### Documentation References

- **[docs/WORKFLOW_DOCUMENTATION.md](docs/WORKFLOW_DOCUMENTATION.md)** - Complete workflow usage guide
- **[RELEASE_WORKFLOW_IMPLEMENTATION.md](RELEASE_WORKFLOW_IMPLEMENTATION.md)** - Implementation details
- **[QUICKSTART_RELEASE.md](QUICKSTART_RELEASE.md)** - Quick start guide
- **[docs/index.html](docs/index.html)** - Documentation viewer UI

**Related Workflows**:
- **main.yml**: Deploys to S3/CloudFront after release tag merged to master
- **quality-checks.yml**: Validates quality before release
- **scorecards.yml**: Verifies supply-chain security posture

---

### 8. Pull Request Automatic Labeler (labeler.yml)

**Trigger**: `pull_request_target` (`opened`, `synchronize`, `reopened`, `edited`)
**Purpose**: Automatically apply category labels to pull requests based on changed file paths defined in `.github/labeler.yml`
**Permissions**: Default `read-all`; per-job `pull-requests: write`, `issues: write`, `contents: read` (least privilege)

#### Workflow Steps

1. **Harden the runner** (StepSecurity) — egress audit
2. **Checkout repository** (`actions/checkout` SHA-pinned) with `persist-credentials: false`
3. **Check if required labels exist** — verifies the label palette seeded by `setup-labels.yml` before attempting to apply
4. **Apply labels** using a SHA-pinned `actions/labeler` action driven by `.github/labeler.yml` (changed-path globs)
5. **Summary output** — prints a summary of label-existence checks and labels applied for visibility

#### Security Controls

- ✅ Uses `pull_request_target` only for label management; no untrusted code is checked out at write privilege
- ✅ SHA-pinned actions to defeat tag-hijacking
- ✅ Step-level `permissions:` block (no inherited write tokens)
- ✅ Egress audit logs outbound network access for visibility and review

#### ISMS Mapping

- [Change Management](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Change_Management.md) — consistent triage labelling for changes
- [Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md) — workflow least-privilege

---

### 9. Setup Repository Labels (setup-labels.yml)

**Trigger**: `workflow_dispatch` (manual; with optional `recreate_all` boolean)
**Purpose**: One-shot / on-demand reconciliation of the repository's standard label palette so triage automation (`labeler.yml`, Copilot agent triage) operates against a known schema
**Permissions**: `contents: read`, `issues: write` (least privilege)

#### Workflow Steps

1. **Harden Runner** — egress audit
2. **Checkout repository**
3. **Apply label set** from the label definitions currently maintained inline in the workflow's shell logic (`create_or_update_label` function); `recreate_all=true` deletes and recreates each label

#### Security Controls

- ✅ Manual-only trigger eliminates automation-induced label churn
- ✅ Minimal permissions (no `contents: write`, no `pull-requests: write`)
- ✅ Idempotent by default; destructive mode is opt-in

#### ISMS Mapping

- [Change Management](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Change_Management.md) — controlled metadata baseline
- [Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md) — repository governance hygiene

---

### 10. Compile Agentic Workflows (compile-agentic-workflows.yml)

**Trigger**: `workflow_dispatch` (manual)
**Purpose**: Compile `.md` agentic workflow definitions in `.github/aw/` and `.github/workflows/*.md` into executable `.lock.yml` artefacts using the `gh aw` CLI, then commit the generated artefacts back to the repository
**Permissions**: `contents: write`, `actions: write` (required for committing compiled artefacts and re-registering workflows)

#### Workflow Steps

1. **Harden Runner** — egress audit
2. **Checkout repository** with a write-enabled token (`secrets.COPILOT_MCP_GITHUB_PERSONAL_ACCESS_TOKEN` when available, otherwise the workflow `GITHUB_TOKEN`) to allow commit-back
3. **Install `gh aw` CLI** (version-pinned to `v0.68.7`)
4. **Delete existing `.lock.yml` files** then **run `gh aw compile`** — converts agentic Markdown workflow definitions into deterministic `.lock.yml` files (note: `SHARED_PROMPT_PATTERNS.md` lives in `.github/aw/` rather than `.github/workflows/` so the bare command needs no exclusions)
5. **Commit & push** generated `.lock.yml` files (and `.github/aw/actions-lock.json`) directly to the triggering branch when they differ from committed versions

#### Security Controls

- ✅ Manual-only trigger (`workflow_dispatch`); cannot be poisoned by external PRs
- ✅ Egress audit logs outbound network access for visibility and review
- ✅ Commit-back uses a GitHub credential with auditability; depending on secret availability this may be `secrets.COPILOT_MCP_GITHUB_PERSONAL_ACCESS_TOKEN` or the workflow `GITHUB_TOKEN` (both are captured in the GitHub audit log)
- ✅ `gh aw` CLI is version-pinned (`v0.68.7`) to defeat upstream regressions
- ⚠️ Generated `.lock.yml` files are deterministic and visible in repository history, but this workflow pushes changes directly to the triggering branch, so PR review is **not** inherently enforced by the compile path — reviewers must inspect the resulting commit post-hoc

#### ISMS Mapping

- [Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md) — code-as-config integrity
- [AI Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/AI_Policy.md) — agentic workflow lifecycle and approval

---

## Security Controls

### Network Security

**Harden Runner Configuration**:
- **Egress Policy**: Block unauthorized traffic
- **Allowed Endpoints**: Strict allowlist (40+ domains)
- **Monitoring**: All network calls audited

**Key Allowed Endpoints**:
- AWS: cloudfront.amazonaws.com, s3.us-east-1.amazonaws.com
- GitHub: github.com, api.github.com, ghcr.io
- Security: api.securityscorecards.dev, bestpractices.coreinfrastructure.org
- CDN: fonts.googleapis.com, cloudflare.docker.com

### Authentication

**AWS OIDC**:
- No long-lived credentials stored
- Short-lived tokens from IAM role assumption
- Scoped to specific S3 bucket and CloudFront distribution

**GitHub Token**:
- Automatic GITHUB_TOKEN with minimal permissions
- PAT only for Copilot MCP (cross-repo access)

### Action Security

**SHA Pinning**:
All actions pinned to specific commit SHAs:
```yaml
uses: step-security/harden-runner@20cf305ff2073D973412fa9b1e3a4f227bda3c76 # v2.14.0
uses: actions/checkout@8e8c483db84b4bee98b60c0593521ed34d9990e8 # v6.0.1
uses: actions/cache@9255dc7a253b0ccc959486e2bca901246202afeb # v5.0.1
```

**Benefits**:
- Prevents supply-chain attacks
- Ensures reproducible builds
- Aligns with SLSA Level 3 requirements

### Vulnerability Scanning

Multi-layer scanning approach:

1. **ZAP (DAST)**: Runtime web application scanning
2. **CodeQL (SAST)**: Static JavaScript analysis
3. **Scorecard**: Supply-chain security posture
4. **Dependency Review**: Vulnerable dependency detection

---

## Performance Optimization

### Caching Strategy

Comprehensive three-tier caching (see [WORKFLOW_CACHING_GUIDE.md](WORKFLOW_CACHING_GUIDE.md)):

**1. APT Packages**
```yaml
path: /var/cache/apt/archives
key: ${{ runner.os }}-apt-${{ hashFiles('**/.github/workflows/main.yml') }}
```

**2. NPM Dependencies**
```yaml
path: ~/.npm
key: ${{ runner.os }}-npm-htmlhint-${{ hashFiles('**/package-lock.json') }}
```

**3. Docker Layers**
```yaml
path: /tmp/.buildx-cache
key: ${{ runner.os }}-docker-${{ github.sha }}
```

### Cache Performance

| Metric | Without Cache | With Cache | Improvement |
|--------|---------------|------------|-------------|
| npm install | 15-30s | 1-2s | **85-90%** |
| apt-get install | 10-20s | 1-2s | **80-90%** |
| Docker pull | 30-60s | 5-10s | **75-80%** |
| **Total Workflow** | ~5 min | ~3 min | **40%** |

### CloudFront Optimization

**Cache Headers by Asset Type**:
- Static assets (CSS/JS/images): 1 year immutable
- Dynamic content (HTML): 1 hour with revalidation
- Metadata (XML/JSON): 1 day
- Fonts: 1 year immutable

**Benefits**:
- Reduced origin requests to S3
- Faster page loads (browser caching)
- Lower CloudFront costs

---

## Monitoring and Observability

### Workflow Metrics

**Available in GitHub Actions**:
- Workflow run duration
- Success/failure rates
- Cache hit rates
- Step-level timing

### Security Dashboard

**GitHub Security Tab**:
- CodeQL findings (JavaScript)
- Scorecard SARIF results
- Dependabot alerts
- Secret scanning alerts

### Artifacts

Stored reports with 30-day retention:

| Artifact | Workflow | Content |
|----------|----------|---------|
| htmlhint-report | quality-checks.yml | HTML validation results |
| link-checker-reports | quality-checks.yml | Internal/external link status |
| SARIF file | scorecards.yml | Scorecard security analysis |
| link-checker-report | pullrequest.yml | PR link verification |
| Release documentation | release.yml | HTML validation, Lighthouse, accessibility reports (committed to docs/) |
| SBOM | release.yml | Software Bill of Materials (SPDX format) |
| Build provenance | release.yml | SLSA Build Level 3 attestation |
| Release ZIP | release.yml | Minified static site bundle |

### External Monitoring

**OpenSSF Scorecard Badge**:
```markdown
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/Hack23/homepage/badge)](https://scorecard.dev/viewer/?uri=github.com/Hack23/homepage)
```

**Lighthouse CI**:
- Performance scores
- Accessibility audit
- SEO recommendations
- Best practices validation

---

## ISMS Compliance Mapping

### Secure Development Policy Alignment

| Requirement | Implementation | Evidence |
|-------------|----------------|----------|
| **Automated Testing** | HTML validation, link checking | quality-checks.yml, pullrequest.yml |
| **Security Scanning** | ZAP, CodeQL, Scorecard | main.yml, pullrequest.yml, scorecards.yml |
| **Dependency Management** | Dependency Review, Scorecard, SBOM | dependency-review.yml, release.yml |
| **Change Control** | PR validation, quality gates, release workflow | pullrequest.yml, release.yml |
| **Infrastructure as Code** | CloudFormation for AWS resources | main.yml (stack-based CloudFront discovery) |
| **Least Privilege** | OIDC IAM roles, minimal permissions | All workflows |
| **Supply Chain Security** | SHA-pinned actions, Harden Runner, SLSA attestations | All workflows, release.yml |
| **Documentation as Code** | Automated documentation generation | release.yml (docs/ directory) |
| **Build Provenance** | SLSA Build Level 3 attestations | release.yml |
| **SBOM Generation** | Automated Software Bill of Materials | release.yml (SPDX format) |

### NIST CSF 2.0 Mapping

| Function | Category | Control | Workflow |
|----------|----------|---------|----------|
| **IDENTIFY** | AM-2 (Asset Inventory) | S3/CloudFront tracking | main.yml |
| **PROTECT** | PR.DS-6 (Integrity) | Minification verification | pullrequest.yml |
| **DETECT** | DE.CM-4 (Detection) | ZAP security scan | main.yml |
| **DETECT** | DE.CM-8 (Vulnerability Scans) | CodeQL, Dependency Review | pullrequest.yml, dependency-review.yml |
| **RESPOND** | RS.AN-3 (Analysis) | Scorecard SARIF reporting | scorecards.yml |

### ISO 27001:2022 Controls

| Control | Description | Implementation |
|---------|-------------|----------------|
| **A.8.8** | Secure Coding | CodeQL SAST analysis |
| **A.8.9** | Security Testing | ZAP DAST scanning |
| **A.8.25** | SDLC Security | PR validation gates |
| **A.8.30** | Outsourced Development | Scorecard supply-chain checks |
| **A.8.32** | Change Management | Automated deployment with gates |

### CIS Controls v8.1

| Control | Sub-Control | Implementation |
|---------|-------------|----------------|
| **4.1** | Secure Configuration | CloudFront cache headers |
| **10.1** | Deploy Anti-Malware | Dependency Review |
| **16.1** | Network Monitoring | Harden Runner egress audit |
| **16.6** | Vulnerability Scanning | ZAP, CodeQL, Scorecard |

---

## Related Documentation

- **[FUTURE_WORKFLOWS.md](FUTURE_WORKFLOWS.md)** - Planned improvements and roadmap
- **[WORKFLOW_CACHING_GUIDE.md](WORKFLOW_CACHING_GUIDE.md)** - Caching strategy deep-dive
- **[SECURITY_ARCHITECTURE.md](SECURITY_ARCHITECTURE.md)** - Overall security architecture
- **[THREAT_MODEL.md](THREAT_MODEL.md)** - Threat analysis and mitigations
- **[Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md)** - ISMS development requirements

---

## Changelog

### 2026-04-21: Workflow Catalog Completion
- Added documentation for `labeler.yml`, `setup-labels.yml`, and `compile-agentic-workflows.yml`
- Catalog now reflects all **10** GitHub Actions workflow files in `.github/workflows/`
- Refreshed action SHA references and document control dates
- Cross-referenced new ISMS lifecycle docs (BCPPlan, FinancialSecurityPlan, End-of-Life-Strategy)

### 2026-02-18: Release Workflow Addition
- Added comprehensive release workflow with SLSA Build Level 3 attestations
- Documented SBOM generation and build provenance
- Added documentation as code section
- Updated artifacts and ISMS compliance mappings
- Cross-referenced release documentation in docs/ directory

### 2026-01-11: Initial Documentation
- Comprehensive documentation of all 6 workflows
- Mermaid diagrams for visualization
- Security controls mapping
- Performance optimization details
- ISMS compliance mapping to ISO 27001, NIST CSF, CIS Controls

---

**🔒 This documentation is part of Hack23 AB's commitment to transparency and security excellence.**

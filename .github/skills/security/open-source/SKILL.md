---
name: open-source
description: 🔓 Open source governance demonstrating security excellence through transparent practices following Hack23 Open Source Policy
license: Apache-2.0
---

# 🔓 Open Source Policy Skill

## 🎯 Purpose

This skill ensures all open source activities demonstrate **security excellence through transparency** as defined in the [Hack23 Open Source Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Open_Source_Policy.md). It applies to all Hack23-owned repositories, external contributions, and third-party open source usage.

**Core principle:** Open source transparency creates competitive advantage through systematic security excellence and publicly verifiable governance.

## 📋 Rules

### 🎖️ Security Posture Evidence (Required Badges)

**MUST display these security badges in README.md:**

#### **🏆 Security Assessment Badges**
- **OpenSSF Scorecard:** Supply chain security assessment ≥7.0 score
- **CII Best Practices:** At least "Passing" level
- **SLSA Level 3:** Build provenance and integrity attestation
- **Quality Gate:** SonarCloud or equivalent showing "Passed" status

#### **📊 License Compliance Badges**
- **FOSSA Status:** License scanning and compliance verification
- **REUSE Compliant:** Clear licensing information for all files
- **License Badge:** Clear display of repository license

**MUST NOT:**
- Release repositories without security badges configured
- Display badges that show "failing" status without remediation plan
- Use placeholder badges with no actual integration

### 📜 Approved Open Source Licenses

**✅ APPROVED for Hack23 projects:**

#### **🟢 Permissive Licenses (Preferred)**
- **Apache-2.0** ⭐ (Hack23 standard) - Patent grant, commercial-friendly
- **MIT** - Simple and permissive
- **BSD-3-Clause** - Minimal restrictions
- **ISC** - Functionally identical to MIT

#### **🟡 Copyleft Licenses (Conditional)**
- **GPL-3.0** - Strong copyleft, requires CEO approval
- **LGPL-3.0** - Library copyleft, requires CEO approval
- **AGPL-3.0** - Network copyleft, internal use only with CEO approval
- **MPL-2.0** - File-level copyleft, automatic approval

**❌ PROHIBITED:**
- Proprietary licenses without legal review
- CC-BY-NC (Non-Commercial)
- SSPL, BSL, PolyForm (source-available, not OSS)
- JSON License ("Good not Evil" clause)
- Unlicensed code

**MUST:**
- Use Apache-2.0 for all new Hack23 projects
- Include SPDX license identifier in all source files
- Verify license compatibility before adding dependencies
- Obtain CEO approval for copyleft licenses

### 🔍 Dependency Management

**MUST:**
- Generate SBOM (Software Bill of Materials) in CycloneDX or SPDX format
- Enable Dependabot or Renovate for automated updates
- Merge security updates within 7 days (Critical) or 30 days (High)
- Use package lock files (package-lock.json, Pipfile.lock, go.sum)
- Scan dependencies with FOSSA or equivalent

**MUST NOT:**
- Add dependencies without license verification
- Use dependencies with known critical vulnerabilities
- Ignore Dependabot alerts

### 🤝 Community Standards

**MUST include in repository:**
- **CONTRIBUTING.md** - Contribution guidelines, DCO/CLA requirements
- **CODE_OF_CONDUCT.md** - Contributor Covenant 2.1 or equivalent
- **SECURITY.md** - Vulnerability disclosure (security@hack23.com)
- **LICENSE** - Apache-2.0 with copyright notice
- **README.md** - Security badges, features, usage, contributing

### 🛡️ Security Scanning (CI/CD)

**MUST configure:**
- **CodeQL** - SAST on every PR
- **Secret scanning** - GitHub Advanced Security
- **Dependabot** - Dependency and security updates
- **FOSSA** - License compliance
- **SonarCloud** - Quality gate (A rating, 0 vulnerabilities)

**MUST NOT:**
- Bypass security scan failures without CEO approval
- Disable security features
- Commit secrets (immediate rotation required)

For complete examples and detailed requirements, see [Hack23 Open Source Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Open_Source_Policy.md).

## 🔗 Related ISMS Policies

- **[Open Source Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Open_Source_Policy.md)** - Primary governance policy
- **[Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md)** - Architecture documentation
- **[STYLE_GUIDE.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/STYLE_GUIDE.md)** - Documentation standards and icons

## 🎯 Compliance Mapping

### ISO 27001:2022
- A.5.13 (Labeling), A.8.9 (Configuration), A.8.25 (Secure SDLC)

### NIST CSF 2.0
- ID.AM-2 (Software inventory), PR.DS-6 (Integrity checking), PR.IP-2 (SDLC)

### CIS Controls v8.1
- Control 2 (Software inventory), Control 16 (Application security)

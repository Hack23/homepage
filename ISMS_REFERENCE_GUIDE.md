<div align="center">

<img src="https://hack23.com/icon-192.png" alt="Hack23 AB Logo" width="192" height="192">

<h1 align="center">🔐 Hack23 AB — ISMS Reference Guide</h1>

**📘 Quick Reference: Homepage Blog → ISMS Policy Mapping**

*Transparency through precise documentation*

![Document owner: James Pether Sörling](https://img.shields.io/badge/Owner-James_Pether_Sörling-blue?style=flat-square) ![Version 1.0](https://img.shields.io/badge/Version-1.0-green?style=flat-square) ![Effective date: 2025-11-10](https://img.shields.io/badge/Effective-2025--11--10-orange?style=flat-square) ![Review cycle: Quarterly](https://img.shields.io/badge/Review_Cycle-Quarterly-purple?style=flat-square)

📄 Document | 🔐 Security Policy | 🌐 Public | ⚡ Living Document

</div>

---

## 🎯 **Purpose Statement**

> "This reference guide maps Hack23's public-facing blog content to our Information Security Management System (ISMS) policies in the [ISMS-PUBLIC repository](https://github.com/Hack23/ISMS-PUBLIC). It ensures accurate, verifiable references from marketing content to operational security documentation—demonstrating that our cybersecurity consulting expertise is backed by auditable implementation, not marketing claims."
>
> — **James Pether Sörling, CEO / Cybersecurity Expert, Hack23 AB**

---

## 📋 **Blog Post to ISMS Policy Mapping**

This guide documents the precise mapping between blog posts on [hack23.com](https://hack23.com) and the corresponding ISMS policies in our public [ISMS-PUBLIC repository](https://github.com/Hack23/ISMS-PUBLIC).

### 📧 **Email Security**

**Blog Page:** [discordian-email-security.html](https://hack23.com/discordian-email-security.html)

| Topic | Primary Policy | Section/Anchor | Status | Notes |
|-------|---------------|----------------|--------|-------|
| Email Authentication (SPF/DKIM/DMARC) | [Network_Security_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Network_Security_Policy.md#-email-security-architecture) | § Email Security Architecture | ✅ Verified | Comprehensive email security controls including SPF, DKIM, DMARC, MTA-STS, TLS-RPT |
| General Security Framework | [Information_Security_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md) | Full document | ✅ Verified | Overarching security policy |
| ISMS Repository Root | [ISMS-PUBLIC](https://github.com/Hack23/ISMS-PUBLIC) | Repository home | ✅ Verified | Public ISMS documentation |

**Coverage Summary:** Email security is comprehensively documented in the Network Security Policy's dedicated email section, covering all aspects of email authentication, transport security, and monitoring.

---

### ☁️ **Cloud Security**

**Blog Page:** [discordian-cloud-security.html](https://hack23.com/discordian-cloud-security.html)

| Topic | Primary Policy | Section/Anchor | Status | Notes |
|-------|---------------|----------------|--------|-------|
| AWS Cloud Architecture | [Network_Security_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Network_Security_Policy.md) | Full document | ✅ Verified | VPC architecture, security groups, CloudFront, WAF |
| Cloud Access Control | [Access_Control_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Access_Control_Policy.md) | Full document | ✅ Verified | IAM, MFA, least privilege |
| AWS Supplier Details | [SUPPLIER.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/SUPPLIER.md) | § AWS Section | ✅ Verified | AWS supplier risk assessment and controls |
| General Security Framework | [Information_Security_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md) | Full document | ✅ Verified | Overarching security policy |

**Coverage Summary:** Cloud security is distributed across Network Security Policy (technical controls), Access Control Policy (identity and permissions), and SUPPLIER.md (third-party risk management for AWS).

---

### 🏢 **Physical Security**

**Blog Page:** [discordian-physical-security.html](https://hack23.com/discordian-physical-security.html)

| Topic | Primary Policy | Section/Anchor | Status | Notes |
|-------|---------------|----------------|--------|-------|
| Physical Security Controls | [Physical_Security_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Physical_Security_Policy.md) | Full document | ✅ Verified | Standalone policy covering office access, device protection, home office security |
| Device Encryption | [Cryptography_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Cryptography_Policy.md) | § Full Disk Encryption | ✅ Verified | AES-256 FDE requirements |
| General Security Framework | [Information_Security_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md) | Full document | ✅ Verified | Overarching security policy |

**Coverage Summary:** Physical security has a dedicated standalone policy, with device encryption requirements cross-referenced in the Cryptography Policy.

---

### 📜 **Acceptable Use**

**Blog Page:** [discordian-acceptable-use.html](https://hack23.com/discordian-acceptable-use.html)

| Topic | Primary Policy | Section/Anchor | Status | Notes |
|-------|---------------|----------------|--------|-------|
| Acceptable Use Policy | [Acceptable_Use_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Acceptable_Use_Policy.md) | Full document | ✅ Verified | Standalone policy covering resource usage, prohibited activities, enforcement |
| General Security Framework | [Information_Security_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md) | Full document | ✅ Verified | Overarching security policy |

**Coverage Summary:** Acceptable Use has a comprehensive standalone policy document.

---

### 📊 **Monitoring and Logging**

**Blog Page:** [discordian-monitoring-logging.html](https://hack23.com/discordian-monitoring-logging.html)

| Topic | Primary Policy | Section/Anchor | Status | Notes |
|-------|---------------|----------------|--------|-------|
| Development Logging | [Secure_Development_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md) | § Security Monitoring | ✅ Verified | Application-level security logging, audit trails |
| Network Monitoring | [Network_Security_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Network_Security_Policy.md) | § Monitoring sections | ✅ Verified | CloudWatch, GuardDuty, Security Hub |
| Security Metrics | [Security_Metrics.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Security_Metrics.md) | Full document | ✅ Verified | Monitoring dashboards, KPIs, metrics framework |
| Incident Response | [Incident_Response_Plan.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Incident_Response_Plan.md) | § Detection & Monitoring | ✅ Verified | Incident detection and response procedures |
| General Security Framework | [Information_Security_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md) | Full document | ✅ Verified | Overarching security policy |

**Coverage Summary:** Monitoring and logging coverage is distributed across multiple policies: Secure Development Policy (application logging), Network Security Policy (infrastructure monitoring), Security Metrics (measurement framework), and Incident Response Plan (detection procedures).

---

### 🔐 **Remote Access**

**Blog Page:** [discordian-remote-access.html](https://hack23.com/discordian-remote-access.html)

| Topic | Primary Policy | Section/Anchor | Status | Notes |
|-------|---------------|----------------|--------|-------|
| Remote Access Controls | [Access_Control_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Access_Control_Policy.md) | Full document | ✅ Verified | Remote access integrated into general access control (MFA, session management, least privilege) |
| Mobile Device Management | [Mobile_Device_Management_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Mobile_Device_Management_Policy.md) | Full document | ✅ Verified | BYOD policy, mobile device security, remote work endpoints |
| Data Classification for Remote Access | [CLASSIFICATION.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md) | § CIA Classification | ✅ Verified | Data classification framework guiding remote access controls |
| General Security Framework | [Information_Security_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md) | Full document | ✅ Verified | Overarching security policy |

**Coverage Summary:** Remote access is treated as a subset of general access control rather than having a standalone policy. Coverage spans Access Control Policy (authentication, authorization), Mobile Device Management Policy (endpoint security), and CLASSIFICATION.md (data handling requirements).

---

### 🎓 **Security Training**

**Blog Page:** [discordian-security-training.html](https://hack23.com/discordian-security-training.html)

| Topic | Primary Policy | Section/Anchor | Status | Notes |
|-------|---------------|----------------|--------|-------|
| Security Awareness Training | [Information_Security_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md) | § Training & Awareness | ✅ Verified | Training requirements integrated into main security policy |
| Classification Training | [CLASSIFICATION.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md) | Full document | ✅ Verified | Data classification framework training requirements |
| Incident Response Training | [Incident_Response_Plan.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Incident_Response_Plan.md) | § Training & Exercises | ✅ Verified | Incident response drills and training |

**Coverage Summary:** Security training is documented within the Information Security Policy rather than as a standalone document, with specialized training requirements in Classification and Incident Response documents.

---

### 🔒 **Data Protection**

**Blog Page:** [discordian-data-protection.html](https://hack23.com/discordian-data-protection.html)

| Topic | Primary Policy | Section/Anchor | Status | Notes |
|-------|---------------|----------------|--------|-------|
| Privacy Policy | [Privacy_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Privacy_Policy.md) | Full document | ✅ Verified | GDPR compliance, data subject rights, retention policies |
| Data Classification | [Data_Classification_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Data_Classification_Policy.md) | Full document | ✅ Verified | Classification framework for data protection requirements |
| Privacy Levels | [CLASSIFICATION.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#privacy-levels) | § Privacy Levels | ✅ Verified | Privacy classification tiers |
| Encryption Controls | [Cryptography_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Cryptography_Policy.md) | Full document | ✅ Verified | Encryption requirements for data protection |
| Access Controls | [Access_Control_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Access_Control_Policy.md) | Full document | ✅ Verified | Data access control requirements |
| Backup & Recovery | [Backup_Recovery_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Backup_Recovery_Policy.md) | Full document | ✅ Verified | Data backup and retention |
| Third-Party Data Handling | [Third_Party_Management.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Third_Party_Management.md) | § Data Processing | ✅ Verified | Supplier data protection requirements |
| Incident Response | [Incident_Response_Plan.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Incident_Response_Plan.md) | § Data Breach Response | ✅ Verified | Data breach notification procedures |
| General Security Framework | [Information_Security_Policy.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md) | Full document | ✅ Verified | Overarching security policy |

**Coverage Summary:** Data protection has comprehensive coverage split between Privacy Policy (legal/regulatory requirements) and Data Classification Policy (technical controls), with supporting controls across multiple policies.

---

## 🏗️ **ISMS Policy Architecture**

### Policy Organization Philosophy

Hack23's ISMS follows a **modular, topic-focused architecture** rather than creating redundant standalone policies for every blog topic. This approach:

✅ **Reduces Redundancy:** Avoids duplicating common controls across multiple documents  
✅ **Maintains Single Source of Truth:** Each control defined once, referenced everywhere  
✅ **Improves Maintainability:** Changes propagate automatically through cross-references  
✅ **Demonstrates Real Implementation:** Structure reflects actual operational integration  

### Primary Policy Categories

#### 📜 **Policies** (Requirements & Standards)
- 🔐 Information_Security_Policy.md (master policy)
- 🔐 Acceptable_Use_Policy.md
- 🔐 Access_Control_Policy.md
- 🔐 Network_Security_Policy.md
- 🔐 Physical_Security_Policy.md
- 🔐 Privacy_Policy.md
- 🔐 Cryptography_Policy.md
- 🔐 Data_Classification_Policy.md
- 🔐 Mobile_Device_Management_Policy.md
- 🔐 Secure_Development_Policy.md
- 🔐 AI_Policy.md
- 🔐 OWASP_LLM_Security_Policy.md
- 🔐 Open_Source_Policy.md

#### 📋 **Plans** (Procedures & Responses)
- 📋 Incident_Response_Plan.md
- 📋 Business_Continuity_Plan.md
- 📋 Disaster_Recovery_Plan.md
- 📋 Backup_Recovery_Policy.md

#### 📊 **Registers** (Asset & Risk Management)
- 📊 Asset_Register.md
- 📊 Risk_Register.md
- 📊 External_Stakeholder_Registry.md

#### 🏷️ **Frameworks** (Standards & Methodologies)
- 🏷️ CLASSIFICATION.md
- 🏷️ Security_Metrics.md
- 🏷️ Risk_Assessment_Methodology.md
- 🏷️ Threat_Modeling.md

#### 📄 **Supporting Documents**
- 📄 SUPPLIER.md (third-party risk assessment)
- 📄 Third_Party_Management.md
- 📄 Change_Management.md
- 📄 Vulnerability_Management.md
- 📄 CRA_Conformity_Assessment_Process.md
- 📄 Compliance_Checklist.md
- 📄 ISMS_Transparency_Plan.md
- 📄 STYLE_GUIDE.md

---

## 🔍 **Verification & Testing**

All ISMS policy links are verified through:

### Automated Verification
- ✅ GitHub Actions link checker (weekly)
- ✅ Pre-deployment link validation
- ✅ Broken link detection in CI/CD

### Manual Verification
- ✅ Quarterly ISMS review (per review cycle)
- ✅ Blog content audit during ISMS updates
- ✅ Cross-reference validation during policy changes

### Testing Commands

```bash
# Verify all ISMS-PUBLIC links in blog files
grep -r "github.com/Hack23/ISMS-PUBLIC" *.html | wc -l

# Check for anchor existence by searching for the heading in the raw Markdown file
curl -s "https://raw.githubusercontent.com/Hack23/ISMS-PUBLIC/main/Network_Security_Policy.md" | grep -i "^##.*Email Security Architecture"

# Validate policy file existence
curl -I "https://raw.githubusercontent.com/Hack23/ISMS-PUBLIC/main/Acceptable_Use_Policy.md"
```

---

## 📚 **Related Documents**

| Document | Purpose | Link |
|----------|---------|------|
| 🔐 ISMS-PUBLIC Repository | Complete ISMS documentation | [GitHub](https://github.com/Hack23/ISMS-PUBLIC) |
| 📘 ISMS Style Guide | Documentation standards | [STYLE_GUIDE.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/STYLE_GUIDE.md) |
| 🏷️ Classification Framework | CIA classification levels | [CLASSIFICATION.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md) |
| 📋 Compliance Checklist | ISO 27001, NIST CSF, CIS Controls | [Compliance_Checklist.md](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Compliance_Checklist.md) |
| 🌐 Homepage Repository | Website source code | [GitHub](https://github.com/Hack23/homepage) |

---

## 🔄 **Maintenance Procedures**

### When Adding New Blog Posts

1. **Identify Topic Coverage:** Determine which ISMS policies cover the blog topic
2. **Check for Existing Sections:** Review policies for relevant section anchors
3. **Update This Guide:** Add new blog post mapping to this reference guide
4. **Verify Links:** Test all links before publication
5. **Cross-Reference:** Ensure bidirectional references (blog ↔ ISMS)

### When Updating ISMS Policies

1. **Check Blog References:** Search homepage repository for references to updated policy
2. **Update Section Anchors:** If section headings change, update blog anchor links
3. **Update This Guide:** Reflect any policy reorganization
4. **Communication:** Notify stakeholders of significant policy changes
5. **Version Control:** Update policy version badges and dates

### When Reorganizing ISMS Structure

1. **Impact Assessment:** Identify all homepage references affected
2. **Redirect Strategy:** Plan for deprecated policy redirects/mergers
3. **Batch Update:** Update all homepage references simultaneously
4. **This Guide Update:** Complete revision of mapping table
5. **Verification:** Full link validation across entire homepage

---

## 📊 **Current Status Summary**

**Last Verified:** 2025-11-10  
**Total Blog Posts Mapped:** 8 primary discordian-* blog posts  
**Total ISMS Policies Referenced:** 30+ policies, plans, and frameworks  
**Broken Links:** 0 ✅  
**Verification Status:** All links verified and working

### Link Health Dashboard

| Blog Post | ISMS Links | Status | Last Verified |
|-----------|-----------|--------|---------------|
| discordian-email-security.html | 3 references | ✅ Verified | 2025-11-10 |
| discordian-cloud-security.html | 3 policies | ✅ Verified | 2025-11-10 |
| discordian-physical-security.html | 3 policies | ✅ Verified | 2025-11-10 |
| discordian-acceptable-use.html | 2 policies | ✅ Verified | 2025-11-10 |
| discordian-monitoring-logging.html | 5 policies | ✅ Verified | 2025-11-10 |
| discordian-remote-access.html | 3 policies | ✅ Verified | 2025-11-10 |
| discordian-security-training.html | 3 policies | ✅ Verified | 2025-11-10 |
| discordian-data-protection.html | 9 policies | ✅ Verified | 2025-11-10 |

---

<div align="center">

## 📋 **Document Control**

**✅ Approved by:** James Pether Sörling, CEO  
**📤 Distribution:** Public  
**🏷️ Classification:** [![Confidentiality: Public](https://img.shields.io/badge/C-Public-lightgrey?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md#confidentiality-levels)

**📅 Effective Date:** 2025-11-10  
**⏰ Next Review:** 2026-02-10 (Quarterly)

**🎯 Framework Compliance:**  
[![ISO 27001](https://img.shields.io/badge/ISO_27001-2022_Aligned-blue?style=flat-square&logo=iso&logoColor=white)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Compliance_Checklist.md) [![NIST CSF 2.0](https://img.shields.io/badge/NIST_CSF-2.0_Aligned-green?style=flat-square&logo=nist&logoColor=white)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Compliance_Checklist.md) [![CIS Controls](https://img.shields.io/badge/CIS_Controls-v8.1_Aligned-orange?style=flat-square&logo=cisecurity&logoColor=white)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Compliance_Checklist.md)

**🔗 Related Documents:** [ISMS Transparency Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/ISMS_Transparency_Plan.md), [Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md), [Style Guide](https://github.com/Hack23/ISMS-PUBLIC/blob/main/STYLE_GUIDE.md)

---

*Living documentation maintained through continuous improvement. Report discrepancies via [GitHub Issues](https://github.com/Hack23/homepage/issues).*

</div>

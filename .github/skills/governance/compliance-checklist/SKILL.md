---
name: compliance-checklist
description: Comprehensive compliance checklist for ISO 27001, NIST CSF, CIS Controls, GDPR, and NIS2 across all Hack23 projects
license: Apache-2.0
---

# Compliance Checklist Skill

## Purpose

Provide a comprehensive compliance verification checklist for all Hack23 projects, ensuring alignment with ISO 27001:2022, NIST CSF 2.0, CIS Controls v8.1, GDPR, and NIS2 requirements.

## Rules

### Repository Compliance Requirements

Every Hack23 repository **MUST** have:

**Security Documentation:**
- [ ] `SECURITY_ARCHITECTURE.md` - Current security design
- [ ] `FUTURE_SECURITY_ARCHITECTURE.md` - Planned security improvements
- [ ] `SECURITY.md` - Security policy and reporting

**Architecture Documentation (C4 Model):**
- [ ] `ARCHITECTURE.md` - Context, Container, Component views
- [ ] `DATA_MODEL.md` - Data structures and relationships
- [ ] `FLOWCHART.md` - Business process and data flows
- [ ] `STATEDIAGRAM.md` - System state transitions
- [ ] `MINDMAP.md` - Conceptual relationships
- [ ] `SWOT.md` - Strategic analysis
- [ ] Future state variants of all above documents

**Development Security:**
- [ ] GitHub Advanced Security enabled (CodeQL, Dependabot, Secret Scanning)
- [ ] Branch protection rules configured
- [ ] CI/CD pipeline with security scanning
- [ ] Pre-commit hooks for secret detection
- [ ] Dependency pinning with hash verification

**Access Control:**
- [ ] Repository access follows least privilege
- [ ] MFA required for all contributors
- [ ] Review required before merge

### Framework-Specific Checks

**ISO 27001:2022:**
- [ ] Risk assessment documented
- [ ] Security controls implemented per Statement of Applicability
- [ ] Change management process followed
- [ ] Incident response procedures defined
- [ ] Business continuity plan maintained

**NIST CSF 2.0:**
- [ ] All six functions addressed (GV, ID, PR, DE, RS, RC)
- [ ] Implementation tier documented
- [ ] Profile aligned with business objectives

**CIS Controls v8.1:**
- [ ] Implementation Group 1 controls met (essential hygiene)
- [ ] Asset and software inventory maintained
- [ ] Vulnerability management SLAs defined
- [ ] Audit logging enabled

**GDPR:**
- [ ] Data processing activities documented
- [ ] Privacy by design principles applied
- [ ] Data subject rights procedures defined
- [ ] Data protection impact assessment (where required)
- [ ] Lawful basis for processing identified

**NIS2:**
- [ ] Cybersecurity risk management measures implemented
- [ ] Incident reporting procedures defined
- [ ] Supply chain security assessed
- [ ] Business continuity measures in place

## Hack23 ISMS Policy References

- [Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)
- [Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md)
- [Risk Assessment Methodology](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Risk_Assessment_Methodology.md)
- [Data Classification Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Data_Classification_Policy.md)
- [Privacy Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Privacy_Policy.md)
- [Business Continuity Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Business_Continuity_Plan.md)

**All Hack23 ISMS Policies**: https://github.com/Hack23/ISMS-PUBLIC

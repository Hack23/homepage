---
name: nist-csf
description: Map security controls to NIST Cybersecurity Framework 2.0 functions - Govern, Identify, Protect, Detect, Respond, Recover
license: Apache-2.0
---

# NIST Cybersecurity Framework 2.0 Skill

## Purpose

Map security implementations across all Hack23 projects to NIST CSF 2.0 framework functions and categories, ensuring comprehensive cybersecurity coverage aligned with the organization's risk profile.

## Rules

### CSF Core Functions

**MUST** address all six CSF 2.0 functions:

#### GOVERN (GV) - Organizational Context
- **MUST** maintain organizational cybersecurity strategy
- **MUST** define risk management strategy and appetite
- **MUST** establish cybersecurity supply chain risk management
- **MUST** maintain roles, responsibilities, and authorities

#### IDENTIFY (ID) - Asset & Risk Management
- **MUST** maintain inventory of all assets (repositories, infrastructure, data)
- **MUST** conduct risk assessments annually and after significant changes
- **MUST** identify and document all data flows and processing activities
- **MUST** assess improvement opportunities based on lessons learned

#### PROTECT (PR) - Safeguards
- **MUST** implement identity management and access control
- **MUST** enforce data security (encryption at rest and in transit)
- **MUST** maintain platform and infrastructure security
- **MUST** implement technology infrastructure resilience

#### DETECT (DE) - Monitoring
- **MUST** implement continuous security monitoring
- **MUST** analyze adverse events for potential incidents
- **MUST** enable GitHub Advanced Security features on all repositories

#### RESPOND (RS) - Incident Response
- **MUST** execute incident management procedures
- **MUST** perform incident analysis and triage
- **MUST** report incidents per regulatory requirements
- **MUST** contain and mitigate incidents promptly

#### RECOVER (RC) - Recovery
- **MUST** execute incident recovery plans
- **MUST** communicate recovery status to stakeholders
- **MUST** incorporate lessons learned into improved procedures

### Implementation Tiers

| Tier | Description | Hack23 Target |
|------|-------------|---------------|
| Tier 1 | Partial - Ad hoc responses | Not acceptable |
| Tier 2 | Risk Informed - Awareness exists | Minimum baseline |
| Tier 3 | Repeatable - Formal policies | **Target for all projects** |
| Tier 4 | Adaptive - Continuous improvement | Aspiration |

## Hack23 ISMS Policy References

- [Information Security Strategy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Strategy.md) - GV
- [Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md) - GV
- [Risk Assessment Methodology](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Risk_Assessment_Methodology.md) - ID.RA
- [Access Control Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Access_Control_Policy.md) - PR.AC
- [Cryptography Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Cryptography_Policy.md) - PR.DS
- [Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md) - PR.IP
- [Vulnerability Management](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Vulnerability_Management.md) - DE.CM
- [Incident Response Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Incident_Response_Plan.md) - RS
- [Business Continuity Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Business_Continuity_Plan.md) - RC
- [Backup Recovery Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Backup_Recovery_Policy.md) - RC.RP

## References

- **NIST CSF 2.0**: https://www.nist.gov/cyberframework
- **NIST CSF Quick Start Guide**: https://doi.org/10.6028/NIST.CSWP.29

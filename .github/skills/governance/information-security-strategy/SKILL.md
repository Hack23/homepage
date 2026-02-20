---
name: information-security-strategy
description: Organization-wide information security strategy aligned with business objectives and ISMS framework
license: Apache-2.0
---

# Information Security Strategy Skill

## Purpose

Define and maintain Hack23's information security strategy that aligns security objectives with business goals, ensuring all projects contribute to the organization's overall security posture.

## Rules

### Strategic Alignment

**MUST:**
- Align security controls with business risk appetite
- Consider security implications in all architectural decisions
- Balance security investment with business value
- Maintain security as a core differentiator (transparency, open-source ISMS)

**MUST NOT:**
- Implement security theater (controls that look good but don't protect)
- Sacrifice usability without corresponding risk reduction
- Ignore business context when applying security requirements

### Security Program Components

**MUST** maintain across all Hack23 projects:

1. **Governance** - Policies, roles, responsibilities
2. **Risk Management** - Assessment, treatment, monitoring
3. **Compliance** - ISO 27001, NIST CSF, CIS, GDPR, NIS2
4. **Operations** - Monitoring, incident response, continuity
5. **Awareness** - Documentation, training, culture

### Security Architecture Requirements

Every Hack23 repository **MUST** maintain:
- `SECURITY_ARCHITECTURE.md` - Current implemented security design
- `FUTURE_SECURITY_ARCHITECTURE.md` - Planned security improvements

### Defense-in-Depth Strategy

**MUST** implement layered security:
- **Perimeter**: Network security, WAF, DDoS protection
- **Identity**: Authentication, authorization, MFA
- **Application**: Input validation, output encoding, secure development
- **Data**: Encryption, classification, access control
- **Monitoring**: Logging, alerting, incident detection

### Transparency as Strategy

Hack23's unique differentiator:
- Public ISMS documentation demonstrates security maturity
- Open-source security tools build community trust
- Transparent security architecture shows commitment to excellence

## Hack23 ISMS Policy References

- [Information Security Strategy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Strategy.md)
- [Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)
- [Risk Assessment Methodology](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Risk_Assessment_Methodology.md)
- [Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md)

## Compliance Mapping

- **ISO 27001:2022**: Clause 5 (Leadership), Clause 6 (Planning)
- **NIST CSF 2.0**: GV (Govern)
- **NIS2**: Article 21 (Cybersecurity risk management measures)

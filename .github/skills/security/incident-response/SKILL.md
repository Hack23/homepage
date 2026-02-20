---
name: incident-response
description: Security incident detection, analysis, containment, eradication, recovery, and lessons learned per NIST SP 800-61r2 and ISO 27035
license: Apache-2.0
---

# Incident Response Skill

## Purpose

Establish comprehensive procedures for detecting, analyzing, containing, eradicating, and recovering from security incidents across all Hack23 projects, aligned with NIST SP 800-61r2 and ISO 27035.

## Rules

### Incident Classification

**MUST** classify incidents by severity:

| Severity | Description | Response Time | Escalation |
|----------|-------------|---------------|------------|
| **Critical** | Active exploitation, data breach, system compromise | 1 hour | CEO immediate |
| **High** | Vulnerability with exploit available, unauthorized access attempt | 4 hours | CEO within 24h |
| **Medium** | Suspicious activity, policy violation, failed attacks | 24 hours | Weekly review |
| **Low** | Minor policy deviations, informational alerts | 72 hours | Monthly review |

### Response Phases

**Phase 1: Detection & Analysis**
- **MUST** monitor security alerts from GitHub Advanced Security (CodeQL, Dependabot, Secret Scanning)
- **MUST** classify incident severity within 30 minutes of detection
- **MUST** preserve evidence before taking containment actions
- **MUST NOT** modify or delete log data during investigation

**Phase 2: Containment**
- **MUST** isolate affected systems/accounts immediately for Critical incidents
- **MUST** revoke compromised credentials within 1 hour
- **MUST** document all containment actions with timestamps
- **MUST NOT** allow affected systems to remain accessible during active exploitation

**Phase 3: Eradication & Recovery**
- **MUST** identify root cause before recovery
- **MUST** verify all malicious artifacts are removed
- **MUST** rotate all potentially compromised secrets
- **MUST** validate system integrity before restoring service

**Phase 4: Post-Incident**
- **MUST** conduct lessons-learned review within 5 business days
- **MUST** update incident response procedures based on findings
- **MUST** document incident in security log with full timeline

### Secret Compromise Response

When a secret is detected in source code:
1. Immediately rotate the compromised credential
2. Review git history for exposure duration
3. Check access logs for unauthorized use
4. Update `.gitignore` and pre-commit hooks
5. Document in incident log

## Hack23 ISMS Policy References

- [Incident Response Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Incident_Response_Plan.md)
- [Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)
- [Business Continuity Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Business_Continuity_Plan.md)

## Compliance Mapping

- **ISO 27001:2022**: A.5.24-A.5.28 (Incident Management)
- **NIST CSF 2.0**: RS (Respond), RC (Recover)
- **CIS Controls v8.1**: Control 17 (Incident Response Management)

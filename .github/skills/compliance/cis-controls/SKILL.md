---
name: cis-controls
description: CIS Controls v8.1 critical security controls for effective cyber defense across all Hack23 projects
license: Apache-2.0
---

# CIS Controls v8.1 Skill

## Purpose

Implement prioritized CIS Controls for cyber defense across all Hack23 projects, focusing on high-impact security controls organized by Implementation Groups.

## Rules

### Implementation Group 1 (Essential - All Projects)

**Control 1: Inventory of Enterprise Assets**
- **MUST** maintain asset inventory for all repositories and infrastructure
- **MUST** tag all cloud resources with Application, Environment, and Owner

**Control 2: Inventory of Software Assets**
- **MUST** track all dependencies (package.json, pom.xml, requirements.txt)
- **MUST** enable Dependabot for automated dependency tracking
- **MUST** generate Software Bill of Materials (SBOM) for releases

**Control 3: Data Protection**
- **MUST** classify data per Data Classification Policy
- **MUST** encrypt sensitive data at rest (AES-256) and in transit (TLS 1.3)
- **MUST** implement data retention and disposal procedures

**Control 4: Secure Configuration**
- **MUST** use secure defaults for all configurations
- **MUST** disable unnecessary features and services
- **MUST** never expose stack traces or debug information in production

**Control 5: Account Management**
- **MUST** enforce MFA for all privileged accounts
- **MUST** disable inactive accounts after 90 days
- **MUST** review access permissions quarterly

**Control 6: Access Control Management**
- **MUST** enforce principle of least privilege
- **MUST** use role-based access control (RBAC)
- **MUST** log all privileged actions

### Implementation Group 2 (Enhanced Security)

**Control 7: Continuous Vulnerability Management**
- **MUST** enable automated vulnerability scanning
- **MUST** remediate per SLA (Critical: 7d, High: 30d, Medium: 90d, Low: 180d)

**Control 8: Audit Log Management**
- **MUST** enable audit logging for all security-relevant events
- **MUST** protect log integrity (immutable storage)
- **MUST** retain logs per retention policy

**Control 11: Data Recovery**
- **MUST** maintain tested backup and recovery procedures
- **MUST** test recovery annually

**Control 16: Application Software Security**
- **MUST** integrate security scanning in CI/CD (CodeQL, OWASP)
- **MUST** perform code review for security-sensitive changes
- **MUST** use parameterized queries and encode output

### Implementation Group 3 (Advanced)

**Control 17: Incident Response Management**
- **MUST** maintain incident response plan
- **MUST** conduct tabletop exercises annually

**Control 18: Penetration Testing**
- **SHOULD** conduct security testing for public-facing applications

## Hack23 ISMS Policy References

- [Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)
- [Asset Register](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Asset_Register.md) - Control 1
- [Data Classification Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Data_Classification_Policy.md) - Control 3
- [Access Control Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Access_Control_Policy.md) - Controls 5-6
- [Vulnerability Management](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Vulnerability_Management.md) - Control 7
- [Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md) - Control 16
- [Incident Response Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Incident_Response_Plan.md) - Control 17
- [Backup Recovery Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Backup_Recovery_Policy.md) - Control 11

## References

- **CIS Controls v8.1**: https://www.cisecurity.org/controls/v8
- **CIS Benchmarks**: https://www.cisecurity.org/cis-benchmarks

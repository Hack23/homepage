---
name: threat-modeling
description: Systematic threat analysis using STRIDE and MITRE ATT&CK frameworks following Hack23 ISMS Threat Modeling Policy
license: Apache-2.0
---

# Threat Modeling Skill

## Purpose

This skill ensures systematic identification, analysis, and mitigation of security threats using structured methodologies as defined in the [Hack23 ISMS Threat Modeling Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Threat_Modeling.md). It applies to all systems, applications, and data flows within the organization.

## Rules

### Threat Modeling Process

**MUST:**
- Perform threat modeling during design phase of all new systems and features
- Use STRIDE framework (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege)
- Map threats to MITRE ATT&CK framework techniques
- Document threat model in version control alongside architecture docs
- Review and update threat models when architecture changes
- Assign risk ratings (Critical, High, Medium, Low) to identified threats
- Define mitigation strategies for all High and Critical threats
- Track threat model findings as security requirements

**MUST NOT:**
- Skip threat modeling for "simple" or "low-risk" features
- Perform threat modeling after implementation
- Ignore threats rated Medium or Low
- Treat threat modeling as one-time activity
- Document threats without corresponding mitigations

### STRIDE Framework Application

**Spoofing Identity (S):**
- MUST implement strong authentication (MFA for privileged access)
- MUST protect authentication credentials in transit and at rest
- MUST validate identity at every trust boundary
- MUST log authentication events

**Tampering with Data (T):**
- MUST protect data integrity using cryptographic hashing or digital signatures
- MUST implement input validation to prevent injection attacks
- MUST use secure transport protocols (TLS 1.2+)
- MUST implement audit logging for data modifications

**Repudiation (R):**
- MUST implement comprehensive audit logging
- MUST protect log integrity (append-only, tamper-evident)
- MUST log user actions with sufficient detail for accountability
- MUST implement time synchronization (NTP)

**Information Disclosure (I):**
- MUST classify all data according to Data Classification Policy
- MUST encrypt sensitive data at rest and in transit
- MUST implement proper access controls
- MUST sanitize error messages and logs

**Denial of Service (D):**
- MUST implement rate limiting and throttling
- MUST design for scalability and resource limits
- MUST implement DDoS protection for public-facing services
- MUST monitor resource utilization

**Elevation of Privilege (E):**
- MUST implement principle of least privilege
- MUST separate administrative and user functions
- MUST validate authorization at each access point
- MUST implement secure session management

### MITRE ATT&CK Mapping

**MUST:**
- Map identified threats to relevant ATT&CK techniques
- Reference ATT&CK tactic and technique IDs in threat documentation
- Use ATT&CK for threat intelligence and red team exercises
- Update mappings when ATT&CK framework is updated
- Consider both ATT&CK for Enterprise and ATT&CK for Cloud

**Example Mappings:**
- Credential Dumping → T1003
- Phishing → T1566
- SQL Injection → T1190
- Data Encrypted for Impact → T1486

### Data Flow Diagrams (DFD)

**MUST:**
- Create DFDs showing all data flows between system components
- Identify trust boundaries in DFDs
- Mark sensitive data flows
- Document external entities, processes, data stores, and data flows
- Use DFDs as basis for threat identification

**Components:**
- External Entity (user, external system)
- Process (application, service, function)
- Data Store (database, file system, cache)
- Data Flow (network traffic, API call, file access)
- Trust Boundary (authentication point, network boundary)

### Attack Trees

**MUST:**
- Build attack trees for High and Critical assets
- Identify multiple attack paths to achieve attacker goals
- Estimate attack difficulty and likelihood
- Prioritize mitigations based on attack tree analysis
- Update attack trees when new threats emerge

### Threat Risk Rating

**Risk Formula:** `Risk = Likelihood × Impact`

**Likelihood Ratings:**
- **High (3):** Easily exploitable, well-known attack, no skill required
- **Medium (2):** Moderate skill required, some barriers to exploitation
- **Low (1):** Expert skill required, significant barriers

**Impact Ratings:**
- **Critical (4):** Complete system compromise, data breach, financial loss >$100k
- **High (3):** Significant data loss, system unavailability, financial loss $10k-$100k
- **Medium (2):** Limited data exposure, degraded service, financial loss $1k-$10k
- **Low (1):** Minimal impact, no data loss, financial loss <$1k

**Risk Score Matrix:**
- 9-12: **Critical** (immediate action required)
- 6-8: **High** (action required within 30 days)
- 3-5: **Medium** (action required within 90 days)
- 1-2: **Low** (accept or monitor)

### Threat Mitigation

**MUST:**
- Define specific mitigations for each identified threat
- Assign mitigation responsibility
- Track mitigation implementation status
- Test that mitigations are effective
- Accept residual risk formally for threats that cannot be fully mitigated

**Mitigation Strategies:**
1. **Eliminate:** Remove the vulnerable feature or functionality
2. **Reduce:** Implement controls to reduce likelihood or impact
3. **Transfer:** Use insurance or third-party services
4. **Accept:** Formally accept residual risk with executive approval

## Examples

### Example 1: STRIDE Analysis for Authentication

```markdown
## Component: User Login API

### Data Flow Diagram
```
[User] --username/password--> [Login API] --SQL query--> [Database]
[Login API] --session token--> [User]
```

### Trust Boundaries
- Internet → Web Server
- Web Server → Database

### STRIDE Analysis

**S - Spoofing:**
- Threat: Attacker guesses weak passwords
- Risk: High Likelihood (3) × High Impact (3) = 9 (Critical)
- Mitigation: 
  - Implement strong password policy (12+ chars, complexity)
  - Implement account lockout after 5 failed attempts
  - Implement rate limiting (max 10 attempts/minute/IP)
  - Log all authentication attempts
- ATT&CK: T1110 (Brute Force)

**T - Tampering:**
- Threat: MitM attack captures credentials
- Risk: Medium Likelihood (2) × High Impact (3) = 6 (High)
- Mitigation:
  - Enforce TLS 1.2+ for all connections
  - Implement HSTS headers
  - Use secure session cookies (HTTPOnly, Secure, SameSite)
- ATT&CK: T1557 (Man-in-the-Middle)

**R - Repudiation:**
- Threat: User denies performing actions
- Risk: Low Likelihood (1) × Medium Impact (2) = 2 (Low)
- Mitigation:
  - Log all authentication events with timestamp, IP, user agent
  - Protect log integrity (append-only S3 bucket)
  - Implement log retention for 1 year
- ATT&CK: T1070 (Indicator Removal on Host)

**I - Information Disclosure:**
- Threat: SQL injection exposes user data
- Risk: Medium Likelihood (2) × Critical Impact (4) = 8 (High)
- Mitigation:
  - Use parameterized queries exclusively
  - Implement input validation (allowlist)
  - Run database with least privilege account
  - Implement Web Application Firewall (WAF)
- ATT&CK: T1190 (Exploit Public-Facing Application)

**D - Denial of Service:**
- Threat: Attacker floods login endpoint
- Risk: High Likelihood (3) × Medium Impact (2) = 6 (High)
- Mitigation:
  - Implement rate limiting (per IP and per account)
  - Use CAPTCHA after 3 failed attempts
  - Implement CDN with DDoS protection
  - Set up auto-scaling
- ATT&CK: T1498 (Network Denial of Service)

**E - Elevation of Privilege:**
- Threat: SQL injection bypasses authentication
- Risk: Medium Likelihood (2) × Critical Impact (4) = 8 (High)
- Mitigation:
  - Use ORM or parameterized queries
  - Implement principle of least privilege for database access
  - Separate admin and user authentication paths
  - Implement security testing in CI/CD
- ATT&CK: T1068 (Exploitation for Privilege Escalation)
```

### Example 2: Attack Tree for User Account Compromise

```
Goal: Compromise User Account
|
+-- [OR] Steal Credentials
|   |
|   +-- [AND] Phishing Attack
|   |   +-- Send phishing email (Easy)
|   |   +-- User clicks malicious link (Medium)
|   |   +-- User enters credentials (Medium)
|   |   → Mitigation: Security awareness training, email filtering, MFA
|   |   → ATT&CK: T1566 (Phishing)
|   |
|   +-- [AND] Password Guessing
|   |   +-- Obtain username (Easy)
|   |   +-- Guess weak password (Medium)
|   |   → Mitigation: Strong password policy, account lockout, rate limiting
|   |   → ATT&CK: T1110 (Brute Force)
|   |
|   +-- [AND] Database Breach
|       +-- SQL injection (Hard)
|       +-- Extract password hashes (Medium)
|       +-- Crack hashes (Hard)
|       → Mitigation: Parameterized queries, strong hashing (bcrypt), WAF
|       → ATT&CK: T1190 (Exploit Public-Facing Application)
|
+-- [OR] Session Hijacking
    |
    +-- [AND] XSS Attack
    |   +-- Find XSS vulnerability (Hard)
    |   +-- Inject JavaScript to steal session cookie (Medium)
    |   → Mitigation: Input validation, output encoding, HTTPOnly cookies, CSP
    |   → ATT&CK: T1185 (Browser Session Hijacking)
    |
    +-- [AND] Session Fixation
        +-- Provide victim with known session ID (Easy)
        +-- Victim authenticates with fixed session (Medium)
        → Mitigation: Regenerate session ID on login, use secure random IDs
        → ATT&CK: T1185 (Browser Session Hijacking)
```

### Example 3: Threat Model Document Template

```markdown
# Threat Model: [System Name]

## Document Control
- **Version:** 1.0
- **Date:** 2026-02-10
- **Author:** Security Team
- **Status:** Approved
- **Classification:** Internal

## 1. System Overview

### Purpose
[Brief description of system purpose and business value]

### Architecture
[High-level architecture diagram]

### Data Classification
- **Public:** Product catalog
- **Internal:** User activity logs
- **Confidential:** User PII, payment information
- **Restricted:** Encryption keys

## 2. Assumptions and Dependencies

### Assumptions
- Users access system via HTTPS only
- Database is hosted in secure AWS VPC
- All users complete security training annually

### Dependencies
- AWS (infrastructure)
- Stripe (payment processing)
- SendGrid (email delivery)

## 3. Data Flow Diagrams

### Level 0: Context Diagram
```
[User] --HTTPS--> [Web Application] --TLS--> [Payment Gateway]
[Web Application] --TLS--> [Database]
```

### Level 1: Detailed Flow
[Include detailed DFD with trust boundaries]

## 4. STRIDE Analysis

[For each component, perform STRIDE analysis as shown in Example 1]

## 5. Threat Summary

| ID | Component | Threat | STRIDE | Risk | ATT&CK | Status |
|----|-----------|--------|--------|------|--------|--------|
| T-001 | Login API | Password guessing | S | Critical (9) | T1110 | Mitigated |
| T-002 | Login API | SQL injection | I, E | High (8) | T1190 | Mitigated |
| T-003 | Web App | XSS | I, T | High (6) | T1185 | In Progress |

## 6. Mitigation Plan

| Threat ID | Mitigation | Owner | Due Date | Status |
|-----------|------------|-------|----------|--------|
| T-001 | Implement account lockout | Dev Team | 2026-02-15 | Complete |
| T-002 | Use parameterized queries | Dev Team | 2026-02-20 | Complete |
| T-003 | Implement CSP headers | DevOps | 2026-02-25 | In Progress |

## 7. Residual Risks

[List any accepted risks with executive approval]

## 8. References
- [Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md)
- [Risk Assessment Methodology](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Risk_Assessment_Methodology.md)
```

## Related ISMS Policies

This skill implements requirements from:

- **[Threat Modeling Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Threat_Modeling.md)** - Primary policy for threat analysis
- **[Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md)** - Security-by-design requirements
- **[Risk Assessment Methodology](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Risk_Assessment_Methodology.md)** - Risk rating and treatment
- **[Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)** - Overall security framework

## Related Documentation

- [SECURITY_ARCHITECTURE.md](../../../../SECURITY_ARCHITECTURE.md) - Security architecture patterns
- [THREAT_MODEL.md](../../../../THREAT_MODEL.md) - System threat models
- [Risk Register](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Risk_Register.md) - Identified risks and treatments

## Compliance Mapping

### ISO 27001:2022
- **A.5.7** Threat intelligence
- **A.8.9** Configuration management
- **A.8.25** Secure development life cycle
- **A.8.28** Secure coding

### NIST Cybersecurity Framework 2.0
- **ID.RA-1**: Asset vulnerabilities are identified and documented
- **ID.RA-3**: Threats, both internal and external, are identified and documented
- **PR.DS-5**: Protections against data leaks are implemented

### CIS Controls v8.1
- **Control 18**: Penetration Testing
  - 18.3 Perform Periodic Red Team Exercises
  - 18.4 Conduct Periodic Purple Team Exercises

## Enforcement

Threat modeling compliance is verified through:
- **Architecture reviews:** All new systems must have approved threat model before development
- **Security gate:** Threat model must be updated before production deployment
- **Quarterly audits:** Random sampling of systems to verify threat models exist and are current
- **Metrics:** Track percentage of systems with current threat models (target: 100%)

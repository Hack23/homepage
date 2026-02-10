---
name: "Acceptable Use"
description: "Behavioral expectations, professional standards, and responsible technology use"
license: "Apache-2.0"
version: "1.0"
author: "Hack23 AB"
tags: ["acceptable-use", "professional-standards", "system-usage"]
category: "security"
frameworks: ["ISO 27001:2022", "NIST CSF 2.0"]
related_policies: ["Acceptable_Use_Policy.md"]
---

# ✅ Acceptable Use Skill

## 🎯 Purpose

Enforce behavioral expectations and professional standards for information technology use, based on [Acceptable Use Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Acceptable_Use_Policy.md).

**Key Principle:** *"Clear expectations create secure behaviors."*

## 📚 Scope

- 💻 System Access & Authentication
- 📊 Data Handling & Privacy (GDPR)
- 💾 Software & Application Use
- 🌐 Internet & Network Use
- 📱 Mobile Device & Remote Work
- 📢 Communication & Social Media

## ⚙️ Security Rules

### MUST Requirements

```yaml
acceptable_practices:
  authentication:
    - strong_unique_passwords: per_access_control_policy
    - mfa_enabled: all_business_critical_systems
    - password_managers: approved_tools_only
    - no_credential_sharing: never_share_passwords
  
  data_handling:
    - classify_data: per_classification_framework
    - encrypt_sensitive: cryptography_policy_standards
    - gdpr_compliance: privacy_policy_requirements
    - secure_disposal: shred_or_wipe_sensitive_data
  
  software_use:
    - licensed_software: valid_commercial_or_oss_licenses
    - security_updates: vulnerability_management_sla
    - approved_apps: documented_in_asset_register
  
  network_use:
    - https_required: secure_connections_for_sensitive_data
    - vpn_for_remote: network_security_policy_requirements
    - no_public_wifi: for_unencrypted_business_access
  
  professional_conduct:
    - business_purpose_primary: limited_personal_use_acceptable
    - reputation_protection: conduct_reflects_company
    - confidentiality: no_unauthorized_disclosure
```

### MUST NOT Prohibitions

```yaml
prohibited_activities:
  illegal:
    - hacking_unauthorized_access
    - software_piracy
    - illegal_content
    - fraud_theft
  
  malicious:
    - introducing_malware
    - circumventing_security
    - data_theft
    - sabotage
  
  policy_violations:
    - unencrypted_sensitive_data
    - unapproved_software
    - credential_sharing
    - excessive_personal_use
  
  reputation_damage:
    - disclosing_confidential_info
    - harassment_discrimination
    - inappropriate_content
```

## 💡 Examples

### Example 1: Secure Work Practices (Compliant)

```yaml
daily_routine:
  start_of_day:
    - use_strong_password: password_manager_autofill
    - enable_mfa: google_authenticator_totp
    - verify_screen_lock: automatic_5_minute_timeout
  
  during_work:
    - classify_documents: apply_classification_labels
    - encrypt_communications: signal_for_sensitive_discussions
    - vpn_for_aws: wireguard_for_console_access
  
  end_of_day:
    - log_out_all_systems: close_all_sessions
    - secure_documents: lock_in_cabinet_or_encrypt
    - shred_waste: cross_cut_shredder_for_sensitive
```

### Example 2: Public Space Work (Non-Compliant → Corrected)

**❌ Non-Compliant:**
```yaml
coffee_shop_work:
  - no_vpn: direct_aws_console_access
  - no_screen_privacy: client_data_visible
  - public_wifi: unencrypted_network
```

**✅ Corrected:**
```yaml
remote_work_controls:
  location_assessment:
    - data_classification: only_LOW_MEDIUM_in_public
    - HIGH_CRITICAL: work_from_home_office_only
  
  required_controls:
    - screen_privacy_filter: prevents_shoulder_surfing
    - vpn_required: wireguard_for_business_access
    - screen_lock: immediate_when_leaving_seat
```

## 🔗 Integration

**Policies:** [Acceptable Use](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Acceptable_Use_Policy.md), [Information Security](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)

**Skills:** physical-security, mobile-device-management, data-classification

**Frameworks:** ISO 27001 A.5.10, NIST CSF PR, CIS Control 16.8

## 📋 Document Control

- **Version:** 1.0 | **Updated:** 2026-02-10
- **License:** Apache-2.0
- **Classification:** [![Public](https://img.shields.io/badge/C-Public-lightgrey)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md)

---
name: "Privacy Policy"
description: "GDPR-compliant privacy framework, privacy by design, and data subject rights"
license: "Apache-2.0"
version: "1.0"
author: "Hack23 AB"
tags: ["privacy", "gdpr", "data-protection"]
category: "security"
frameworks: ["GDPR", "ISO 27001:2022", "NIST CSF 2.0"]
related_policies: ["Privacy_Policy.md"]
---

# 🔒 Privacy Policy Skill

## 🎯 Purpose

Enforce GDPR-compliant privacy controls and privacy-by-design principles, based on [Privacy Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Privacy_Policy.md).

**Key Principle:** *"Privacy through transparency and user control."*

## 📚 Scope

- 🔐 Privacy by Design Principles
- 👤 Data Subject Rights (GDPR Articles 15-22)
- 📋 Consent Management
- 🔍 Privacy Impact Assessments
- 🛡️ Data Protection Measures
- 📊 Breach Notification (72-hour requirement)

## ⚙️ Security Rules

### MUST Requirements

```yaml
privacy_by_design:
  data_minimization:
    - collect_only_necessary: purpose_specific_data
    - retention_limits: delete_when_no_longer_needed
    - anonymization: pseudonymize_where_possible
  
  user_controls:
    - transparent_collection: clear_privacy_notices
    - consent_granular: per_processing_purpose
    - opt_out_easy: simple_withdrawal_mechanism
  
  technical_measures:
    - encryption: data_at_rest_and_in_transit
    - access_controls: role_based_least_privilege
    - audit_logging: track_personal_data_access

gdpr_compliance:
  lawful_basis:
    - identify_basis: [consent, contract, legal_obligation, legitimate_interest]
    - document_decision: record_in_data_register
  
  data_subject_rights:
    - right_to_access: provide_copy_within_30_days
    - right_to_rectification: correct_inaccurate_data
    - right_to_erasure: delete_upon_request_if_applicable
    - right_to_portability: machine_readable_format
    - right_to_object: stop_processing_upon_objection
  
  breach_notification:
    - assess_risk: within_24_hours_of_discovery
    - notify_authority: within_72_hours_if_high_risk
    - notify_subjects: without_undue_delay_if_high_risk
```

### MUST NOT Prohibitions

```yaml
prohibited_practices:
  - excessive_collection: data_not_needed_for_purpose
  - unclear_consent: vague_or_bundled_consent
  - indefinite_retention: keeping_data_longer_than_necessary
  - unencrypted_personal_data: storing_without_protection
  - third_party_sharing: without_legal_basis_or_consent
  - ignoring_dsar: data_subject_access_request_delay
```

## 💡 Examples

### Example 1: GDPR-Compliant User Registration

```yaml
user_registration:
  consent_collection:
    purpose: "Process account creation and service delivery"
    granular_options:
      - required: account_management_and_authentication
      - optional: marketing_communications
      - optional: analytics_and_product_improvement
    
    consent_record:
      timestamp: iso_8601_utc
      ip_address: logged_for_audit
      consent_text: versioned_and_stored
      user_confirmation: explicit_checkbox_tick
  
  data_minimization:
    required_fields:
      - email: authentication_and_communication
      - password: hashed_with_bcrypt
    optional_fields:
      - display_name: user_preference
    not_collected:
      - address: not_needed_for_service
      - phone: not_required_for_account
  
  security_measures:
    - encryption: aes_256_at_rest
    - access_control: rbac_with_audit_logging
    - backup: encrypted_daily_backups
  
  retention:
    active_account: retained_while_account_exists
    deleted_account: personal_data_erased_within_30_days
    legal_hold: billing_records_7_years_per_law
```

### Example 2: Data Subject Access Request (DSAR)

```yaml
dsar_process:
  request_received:
    - verify_identity: two_factor_authentication
    - log_request: incident_tracking_system
    - acknowledge: within_1_business_day
  
  data_compilation:
    systems_checked:
      - production_database: user_profile_and_activity
      - backup_systems: historical_data
      - log_files: access_and_audit_logs
      - email_archives: communications
  
  response_preparation:
    format: machine_readable_json_or_csv
    included_data:
      - personal_info: name_email_preferences
      - activity_data: login_history_actions
      - derived_data: analytics_and_inferences
    excluded_data:
      - third_party_data: data_about_others
      - trade_secrets: proprietary_algorithms
  
  delivery:
    method: secure_encrypted_email_or_portal
    timeline: within_30_days_of_request
    documentation: record_completion_in_privacy_log
```

### Example 3: Data Breach Response (72-Hour Notification)

```yaml
breach_response:
  immediate_0_24_hours:
    - contain_breach: isolate_affected_systems
    - assess_scope: identify_personal_data_exposed
    - document: incident_log_with_timeline
  
  notification_24_72_hours:
    authority_notification:
      recipient: swedish_data_protection_authority
      method: online_breach_notification_form
      content:
        - nature_of_breach: unauthorized_access_to_database
        - categories_affected: email_addresses_and_names
        - approximate_number: 150_data_subjects
        - likely_consequences: phishing_risk
        - measures_taken: forced_password_reset_monitoring
        - contact_details: dpo_contact_information
    
    subject_notification:
      required_if: high_risk_to_rights_and_freedoms
      method: direct_email_to_affected_users
      content:
        - describe_breach: what_happened_in_plain_language
        - potential_impact: explain_risks_to_individuals
        - measures_taken: what_we_did_to_fix
        - recommended_actions: change_passwords_monitor_accounts
  
  post_incident:
    - root_cause_analysis: within_7_days
    - remediation: implement_preventive_controls
    - lessons_learned: update_privacy_procedures
    - documentation: complete_breach_register_entry
```

## 🔗 Integration

**Policies:** [Privacy Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Privacy_Policy.md), [Data Classification](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Data_Classification_Policy.md)

**Skills:** data-classification, cryptography, access-control

**Frameworks:** GDPR Articles 5, 6, 15-22, 33, 34 | ISO 27001 A.18 | NIST CSF PR.IP-11

## 📋 Document Control

- **Version:** 1.0 | **Updated:** 2026-02-10
- **License:** Apache-2.0
- **Classification:** [![Public](https://img.shields.io/badge/C-Public-lightgrey)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md)

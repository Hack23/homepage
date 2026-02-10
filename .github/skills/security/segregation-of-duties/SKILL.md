---
name: "Segregation of Duties"
description: "Role separation, compensating controls for single-person operations, dual control"
license: "Apache-2.0"
version: "1.0"
author: "Hack23 AB"
tags: ["segregation-of-duties", "role-separation", "compensating-controls"]
category: "security"
frameworks: ["ISO 27001:2022", "SOC 2", "NIST CSF 2.0"]
related_policies: ["Information_Security_Policy.md"]
---

# 🔀 Segregation of Duties Skill

## 🎯 Purpose

Enforce role separation and implement compensating controls for single-person operations.

**Key Principle:** *"One person shouldn't have unchecked power over critical processes."*

## 📚 Scope

- 🔐 Role Separation Requirements
- 🛡️ Compensating Controls (single-person company context)
- 🔄 Dual Control Processes
- 📊 Access Reviews
- ⚖️ Conflict of Interest Prevention

## ⚙️ Security Rules

### MUST Requirements

```yaml
role_separation:
  development_vs_production:
    - separate_accounts: dev_and_prod_aws_accounts
    - approval_required: pr_review_before_merge
    - automated_testing: ci_cd_pipeline_validation
  
  financial_vs_technical:
    - separate_tools: different_systems_for_finance_and_tech
    - audit_trail: all_transactions_logged
    - third_party_validation: accountant_reviews_financials
  
compensating_controls:
  single_person_company:
    - automation: ci_cd_prevents_manual_errors
    - third_party_review: external_auditor_or_consultant
    - documentation: all_changes_documented_and_logged
    - transparency: public_isms_for_client_review
  
dual_control_processes:
  production_deployment:
    - automated_pipeline: github_actions_with_tests
    - manual_approval: ceo_approval_via_pr_merge
    - rollback_capability: immediate_rollback_if_issues
  
  financial_transactions:
    - bank_requires_bkid: separate_authentication_factor
    - accountant_review: quarterly_financial_review
    - audit_trail: all_transactions_logged_in_accounting_software
```

### MUST NOT Prohibitions

```yaml
prohibited:
  - bypass_controls: skip_ci_cd_and_deploy_directly
  - self_approve_financials: no_external_validation
  - delete_audit_logs: remove_evidence_of_actions
  - shared_credentials: use_same_password_everywhere
```

## 💡 Example: Production Deployment Controls

```yaml
deployment_process:
  development:
    developer: ceo_creates_feature_branch
    testing: automated_unit_e2e_security_tests
    code_review: self_review_with_ai_assistance
  
  pre_production:
    pull_request: github_pr_to_main_branch
    automated_checks:
      - sonarcloud: code_quality_security_scan
      - dependabot: dependency_vulnerability_check
      - codecov: test_coverage_minimum_80_percent
    approval: ceo_approves_pr_after_all_checks_pass
  
  production:
    automated_deployment: github_actions_on_merge
    monitoring: cloudwatch_alarms_for_errors
    rollback: automated_rollback_on_failure
  
  post_deployment:
    verification: smoke_tests_in_production
    documentation: changelog_updated
    audit_log: deployment_recorded_in_cloudtrail
```

## 🔗 Integration

**Policies:** [Information Security](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md), [Change Management](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Change_Management.md)

**Skills:** access-control, secure-development

**Frameworks:** ISO 27001 A.8.2, SOC 2 CC6.3, NIST CSF PR.AC-04

## 📋 Document Control

- **Version:** 1.0 | **Updated:** 2026-02-10
- **License:** Apache-2.0
- **Classification:** [![Public](https://img.shields.io/badge/C-Public-lightgrey)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md)

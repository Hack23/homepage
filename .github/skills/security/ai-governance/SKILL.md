---
name: "AI Governance"
description: "Comprehensive AI risk management, EU AI Act compliance, and LLM usage governance"
license: "Apache-2.0"
version: "1.0"
author: "Hack23 AB"
tags: ["ai-governance", "eu-ai-act", "llm-security"]
category: "security"
frameworks: ["EU AI Act", "ISO 27001:2022", "NIST AI RMF"]
related_policies: ["AI_Policy.md"]
---

# 🤖 AI Governance Skill

## 🎯 Purpose

Enforce comprehensive AI risk management and EU AI Act compliance, based on [AI Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/AI_Policy.md).

**Key Principle:** *"AI systems require systematic risk management and human oversight."*

## 📚 Scope

- 🤖 AI System Classification (EU AI Act risk levels)
- 🛡️ LLM Usage Governance (GitHub Copilot, ChatGPT)
- 👁️ Human Oversight Requirements
- ⚖️ Bias and Fairness Controls
- 📊 AI Risk Assessment
- 🔍 Transparency and Explainability

## ⚙️ Security Rules

### MUST Requirements

```yaml
ai_system_classification:
  unacceptable_risk:
    prohibited_systems:
      - social_scoring: government_or_private_social_credit
      - real_time_biometric: public_space_surveillance_without_warrant
      - subliminal_manipulation: ai_that_manipulates_behavior
      - exploit_vulnerabilities: ai_targeting_vulnerable_groups
    action: never_develop_deploy_or_use
  
  high_risk_systems:
    examples:
      - recruitment_ai: candidate_screening_or_selection
      - credit_scoring: loan_approval_algorithms
      - law_enforcement: predictive_policing_tools
    requirements:
      - risk_assessment: comprehensive_before_deployment
      - data_quality: high_quality_representative_datasets
      - documentation: technical_docs_and_user_manuals
      - human_oversight: meaningful_human_review_required
      - transparency: users_informed_of_ai_involvement
      - conformity_assessment: third_party_audit_required
  
  limited_risk_systems:
    examples:
      - chatbots: customer_service_bots
      - deepfakes: synthetic_media_generation
    requirements:
      - transparency_obligations: users_informed_interacting_with_ai
      - disclosure: ai_generated_content_labeled
  
  minimal_risk_systems:
    examples:
      - spam_filters: email_filtering
      - ai_video_games: entertainment_applications
      - github_copilot: code_completion_assistance
    requirements:
      - voluntary_codes: follow_best_practices
      - basic_transparency: disclose_ai_use_in_documentation

llm_usage_governance:
  github_copilot:
    approved_use:
      - code_completion: autocomplete_and_suggestions
      - documentation: generating_code_comments
      - test_generation: creating_unit_test_scaffolding
    
    security_controls:
      - code_review: all_ai_generated_code_manually_reviewed
      - secret_scanning: automated_pre_commit_hooks
      - license_compliance: verify_suggested_code_licenses
      - no_sensitive_data: never_input_customer_or_confidential_data
    
    prohibited_use:
      - production_secrets: entering_api_keys_or_passwords
      - customer_data: inputting_personal_or_business_data
      - unreviewed_deployment: deploying_ai_code_without_review
  
  chatgpt_claude:
    approved_use:
      - research: general_information_gathering
      - brainstorming: idea_generation_and_planning
      - documentation: writing_assistance_for_public_docs
    
    prohibited_use:
      - confidential_data: client_information_or_trade_secrets
      - source_code: proprietary_code_or_algorithms
      - personal_data: customer_or_employee_information

human_oversight:
  ai_decisions:
    code_generation:
      - review_required: all_copilot_suggestions_reviewed
      - testing: ai_code_must_pass_automated_tests
      - security_scan: sast_sca_checks_mandatory
    
    business_decisions:
      - ai_as_advisor: ai_provides_recommendations_only
      - human_final_decision: ceo_makes_final_call
      - documentation: record_ai_input_and_human_decision
```

### MUST NOT Prohibitions

```yaml
prohibited_ai_practices:
  - unclassified_systems: deploying_ai_without_risk_assessment
  - no_human_oversight: fully_automated_critical_decisions
  - biased_training_data: using_unrepresentative_datasets
  - black_box_systems: unexplainable_ai_for_high_risk_decisions
  - sensitive_data_training: training_ai_on_personal_data_without_consent
  - bypassing_controls: using_personal_ai_for_business_without_approval
```

## 💡 Examples

### Example 1: GitHub Copilot Secure Usage

```yaml
copilot_workflow:
  development:
    enable_copilot: vscode_github_copilot_extension
    use_suggestions:
      - code_completion: accept_for_boilerplate_code
      - function_generation: review_logic_before_accepting
      - test_scaffolding: verify_test_coverage_and_assertions
  
  security_checks:
    pre_commit:
      - secret_scanning: gitleaks_pre_commit_hook
      - code_review: manual_review_of_ai_suggestions
      - license_check: verify_no_copyleft_violations
    
    ci_cd_pipeline:
      - sast: sonarcloud_static_analysis
      - sca: dependabot_vulnerability_scanning
      - test_coverage: minimum_80_percent_coverage
  
  prohibited_inputs:
    never_type:
      - api_keys: aws_access_keys_database_passwords
      - customer_data: email_addresses_names_personal_info
      - proprietary_algorithms: trade_secret_business_logic
      - production_configs: database_connection_strings
  
  documentation:
    - attribution: note_ai_assisted_code_in_comments
    - review_notes: document_manual_changes_to_ai_suggestions
    - lessons_learned: track_copilot_false_positives_for_training
```

### Example 2: AI Risk Assessment Process

```yaml
ai_risk_assessment:
  system_identification:
    name: recruitment_candidate_screening_tool
    classification: HIGH_RISK_per_eu_ai_act
    trigger: involves_employment_decisions
  
  risk_analysis:
    potential_harms:
      - discrimination: algorithm_may_have_gender_or_age_bias
      - privacy: processes_personal_data_from_resumes
      - transparency: candidates_unaware_of_ai_involvement
    
    likelihood: MEDIUM
    impact: HIGH
    overall_risk: HIGH
  
  risk_mitigation:
    technical_measures:
      - bias_testing: fairness_metrics_on_diverse_test_set
      - explainability: shap_or_lime_for_decision_explanations
      - data_quality: representative_training_dataset
    
    organizational_measures:
      - human_review: recruiter_reviews_all_ai_recommendations
      - transparency: candidates_informed_of_ai_use
      - appeal_process: candidates_can_request_human_review
      - audit: annual_third_party_fairness_audit
  
  compliance_obligations:
    eu_ai_act:
      - risk_management_system: implemented_and_documented
      - data_governance: high_quality_training_data_verified
      - technical_documentation: available_for_authorities
      - conformity_assessment: third_party_audit_planned
    
    gdpr:
      - lawful_basis: legitimate_interest_assessment
      - data_minimization: only_relevant_resume_data_processed
      - automated_decision: human_review_prevents_art_22_violation
  
  approval:
    decision: APPROVED_WITH_CONDITIONS
    approver: CEO
    date: 2026_02_10
    review_date: 2026_08_10_semi_annual
    conditions:
      - quarterly_bias_testing
      - monthly_human_override_rate_monitoring
      - annual_external_audit
```

### Example 3: Prohibited AI Use (Corrected)

**❌ Non-Compliant:**
```yaml
incorrect_chatgpt_use:
  prompt: "Review this customer database schema and suggest optimizations"
  attached: production_database_dump_with_customer_emails
  risk: exposing_personal_data_to_third_party_ai
```

**✅ Corrected:**
```yaml
compliant_chatgpt_use:
  data_anonymization:
    - remove_personal_data: replace_emails_with_placeholders
    - sanitize_schema: generic_field_names_only
    - sample_data: synthetic_test_data_not_production
  
  prompt: "Review this anonymized schema and suggest optimizations"
  attached: sanitized_schema_with_no_real_data
  
  verification:
    - no_personal_data: verified_before_submission
    - no_secrets: no_connection_strings_or_credentials
    - documented: ai_consultation_logged_in_project_notes
```

## 🔗 Integration

**Policies:** [AI Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/AI_Policy.md), [Information Security](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)

**Skills:** owasp-llm-security, data-classification, privacy-policy

**Frameworks:** EU AI Act, NIST AI RMF, ISO 42001 (draft)

## 📋 Document Control

- **Version:** 1.0 | **Updated:** 2026-02-10
- **License:** Apache-2.0
- **Classification:** [![Public](https://img.shields.io/badge/C-Public-lightgrey)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md)

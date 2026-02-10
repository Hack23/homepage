---
name: "OWASP LLM Security"
description: "LLM-specific security controls, prompt injection prevention, OWASP LLM Top 10"
license: "Apache-2.0"
version: "1.0"
author: "Hack23 AB"
tags: ["owasp-llm", "prompt-injection", "llm-security"]
category: "security"
frameworks: ["OWASP LLM Top 10", "ISO 27001:2022"]
related_policies: ["AI_Policy.md"]
---

# 🧠 OWASP LLM Security Skill

## 🎯 Purpose

Enforce LLM-specific security controls aligned with OWASP LLM Top 10 2025.

**Key Principle:** *"LLMs introduce unique security risks requiring specialized controls."*

## 📚 Scope

- 🔓 Prompt Injection Prevention
- 💾 Insecure Output Handling
- 🏋️ Model Denial of Service
- �� Supply Chain Vulnerabilities
- 🔌 Insecure Plugin Design
- 📊 Excessive Agency
- 🛡️ Data Leakage Prevention

## ⚙️ Security Rules

### MUST Requirements

```yaml
owasp_llm_top_10_controls:
  llm01_prompt_injection:
    input_validation:
      - sanitize_user_input: remove_injection_attempts
      - prompt_templates: use_parameterized_prompts
      - context_isolation: separate_user_system_contexts
    
    detection:
      - monitor_outputs: alert_on_suspicious_responses
      - log_inputs: track_all_prompts_for_analysis
      - anomaly_detection: flag_unusual_input_patterns
  
  llm02_insecure_output_handling:
    output_validation:
      - sanitize_before_render: html_encode_llm_outputs
      - validate_format: check_expected_output_structure
      - xss_prevention: never_trust_llm_generated_html
    
    secure_integration:
      - escaped_rendering: use_safe_templating_engines
      - csp_headers: content_security_policy_strict
  
  llm03_training_data_poisoning:
    data_quality:
      - source_validation: verify_training_data_sources
      - adversarial_testing: test_for_backdoor_triggers
      - data_provenance: track_dataset_origins
    
    monitoring:
      - model_behavior: detect_unexpected_outputs
      - regular_retraining: update_with_clean_datasets
  
  llm04_model_denial_of_service:
    rate_limiting:
      - per_user_limits: 100_requests_per_hour
      - cost_caps: maximum_tokens_per_request
      - timeout_enforcement: 30_second_maximum_response_time
    
    resource_management:
      - queue_management: priority_queues_for_critical_users
      - circuit_breakers: auto_disable_on_abuse_detection
  
  llm05_supply_chain_vulnerabilities:
    third_party_models:
      - vendor_assessment: security_evaluation_before_use
      - model_provenance: verify_official_sources_only
      - sbom: software_bill_of_materials_for_ai_components
    
    monitoring:
      - dependency_scanning: check_for_vulnerable_libraries
      - model_updates: track_security_patches_from_vendors
  
  llm06_sensitive_info_disclosure:
    data_protection:
      - no_pii_training: never_train_on_personal_data
      - output_filtering: redact_potential_secrets_in_responses
      - context_limits: limit_context_window_to_reduce_leakage
    
    testing:
      - red_team: attempt_to_extract_training_data
      - regression_tests: verify_no_memorization_of_secrets
  
  llm07_insecure_plugin_design:
    plugin_security:
      - least_privilege: plugins_minimal_permissions_required
      - input_validation: validate_all_plugin_inputs
      - authentication: require_auth_for_plugin_execution
    
    review_process:
      - security_review: all_plugins_security_audited
      - sandboxing: isolate_plugin_execution_environment
  
  llm08_excessive_agency:
    authorization:
      - human_approval: require_approval_for_critical_actions
      - scope_limits: restrict_llm_to_read_only_operations
      - audit_trail: log_all_llm_initiated_actions
    
    safeguards:
      - action_validation: confirm_intended_action_before_execution
      - rollback_capability: undo_mechanism_for_llm_actions
  
  llm09_overreliance:
    human_oversight:
      - fact_checking: verify_llm_outputs_before_trust
      - disclaimer: inform_users_llm_may_hallucinate
      - critical_decisions: never_fully_automate_without_review
  
  llm10_model_theft:
    access_controls:
      - api_authentication: require_strong_auth_for_model_access
      - rate_limiting: prevent_model_extraction_via_queries
      - watermarking: embed_watermarks_in_model_outputs
```

### MUST NOT Prohibitions

```yaml
prohibited_llm_practices:
  - unvalidated_prompts: accepting_raw_user_input_to_llm
  - trusting_outputs: using_llm_responses_without_validation
  - no_rate_limits: allowing_unlimited_api_calls
  - exposing_models: public_access_to_model_weights
  - training_on_secrets: including_api_keys_in_training_data
  - unmonitored_usage: no_logging_or_alerting_for_abuse
```

## 💡 Examples

### Example 1: Prompt Injection Prevention

```python
# Secure LLM Integration with Input Validation
import re
from typing import Optional

def sanitize_user_input(user_input: str) -> str:
    """Remove potential prompt injection attempts"""
    # Remove system-like instructions
    injection_patterns = [
        r"ignore previous instructions",
        r"disregard above",
        r"you are now",
        r"system:",
        r"admin:",
    ]
    
    cleaned = user_input
    for pattern in injection_patterns:
        cleaned = re.sub(pattern, "", cleaned, flags=re.IGNORECASE)
    
    # Limit length to prevent token exhaustion
    max_length = 500
    cleaned = cleaned[:max_length]
    
    return cleaned.strip()

def safe_llm_query(user_question: str) -> Optional[str]:
    """Safely query LLM with validated input"""
    # Validate and sanitize input
    sanitized_input = sanitize_user_input(user_question)
    
    if not sanitized_input:
        return "Invalid input detected"
    
    # Use parameterized prompt template
    system_prompt = "You are a helpful assistant. Answer factually and concisely."
    user_prompt = f"User question: {sanitized_input}"
    
    # Query LLM with separated contexts
    response = query_llm(
        system=system_prompt,
        user=user_prompt,
        max_tokens=150,
        temperature=0.7
    )
    
    # Validate output before returning
    if contains_suspicious_content(response):
        log_security_event("Suspicious LLM output detected", response)
        return "Response blocked for security reasons"
    
    return html_escape(response)  # XSS prevention
```

### Example 2: Rate Limiting and DoS Prevention

```python
# LLM API Rate Limiting
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import time

app = Flask(__name__)

# Rate limiter configuration
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["100 per hour", "10 per minute"],
    storage_uri="redis://localhost:6379"
)

# Cost-based limiting
MAX_TOKENS_PER_REQUEST = 1000
MAX_COST_PER_USER_PER_DAY = 100  # USD

@app.route('/api/llm/query', methods=['POST'])
@limiter.limit("10 per minute")
def llm_query():
    """LLM API endpoint with comprehensive DoS protection"""
    user_id = request.headers.get('X-User-ID')
    user_input = request.json.get('prompt', '')
    
    # Token limit enforcement
    estimated_tokens = len(user_input.split()) * 1.3  # Rough estimate
    if estimated_tokens > MAX_TOKENS_PER_REQUEST:
        return jsonify({
            "error": "Request exceeds maximum token limit"
        }), 400
    
    # Daily cost limit check
    user_cost_today = get_user_cost_today(user_id)
    if user_cost_today >= MAX_COST_PER_USER_PER_DAY:
        return jsonify({
            "error": "Daily cost limit exceeded"
        }), 429
    
    # Timeout enforcement
    start_time = time.time()
    timeout_seconds = 30
    
    try:
        response = query_llm_with_timeout(
            user_input,
            timeout=timeout_seconds
        )
        
        # Track usage cost
        cost = calculate_usage_cost(user_input, response)
        record_user_cost(user_id, cost)
        
        return jsonify({
            "response": response,
            "cost": cost,
            "remaining_daily_quota": MAX_COST_PER_USER_PER_DAY - user_cost_today
        })
    
    except TimeoutError:
        return jsonify({
            "error": "Request timed out"
        }), 504
```

### Example 3: Sensitive Data Leakage Prevention

```python
# Output Filtering to Prevent Data Leakage
import re
from typing import List, Tuple

# Patterns for sensitive data detection
SENSITIVE_PATTERNS = {
    'api_key': r'[A-Za-z0-9]{32,}',
    'email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    'ssn': r'\b\d{3}-\d{2}-\d{4}\b',
    'credit_card': r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b',
    'aws_key': r'AKIA[0-9A-Z]{16}',
}

def detect_sensitive_data(text: str) -> List[Tuple[str, str]]:
    """Detect potential sensitive data in LLM output"""
    findings = []
    
    for data_type, pattern in SENSITIVE_PATTERNS.items():
        matches = re.findall(pattern, text)
        for match in matches:
            findings.append((data_type, match))
    
    return findings

def redact_sensitive_data(text: str) -> str:
    """Redact sensitive data from LLM output"""
    redacted = text
    
    for data_type, pattern in SENSITIVE_PATTERNS.items():
        redacted = re.sub(pattern, f"[REDACTED_{data_type.upper()}]", redacted)
    
    return redacted

def safe_llm_output_handler(llm_response: str) -> dict:
    """Validate and sanitize LLM output before display"""
    # Detect sensitive data
    sensitive_findings = detect_sensitive_data(llm_response)
    
    if sensitive_findings:
        # Log security incident
        log_security_event(
            "Sensitive data detected in LLM output",
            findings=sensitive_findings
        )
        
        # Redact sensitive data
        safe_response = redact_sensitive_data(llm_response)
        
        return {
            "response": safe_response,
            "warning": "Some content was redacted for security",
            "redacted_count": len(sensitive_findings)
        }
    
    # HTML escape to prevent XSS
    return {
        "response": html_escape(llm_response),
        "warning": None
    }
```

## 🔗 Integration

**Policies:** [AI Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/AI_Policy.md)

**Skills:** ai-governance, secure-development, data-classification

**Frameworks:** OWASP LLM Top 10 2025, ISO 27001 A.14

## 📋 Document Control

- **Version:** 1.0 | **Updated:** 2026-02-10
- **License:** Apache-2.0
- **Classification:** [![Public](https://img.shields.io/badge/C-Public-lightgrey)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md)

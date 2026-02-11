---
name: agentic-workflow-security
description: Security best practices, defense-in-depth architecture, threat detection, and safe operations for GitHub Agentic Workflows
license: Apache-2.0
---

# 🔒 Agentic Workflow Security Skill

## Purpose

This skill provides comprehensive security guidance for GitHub Agentic Workflows, implementing defense-in-depth architecture to protect against prompt injection, rogue MCP servers, malicious agents, and unauthorized actions. Security operates across multiple layers: compilation-time validation, runtime isolation, permission separation, network controls, and output sanitization.

## When to Use

Apply this skill when:
- Designing secure agentic workflows that handle sensitive operations
- Implementing defense-in-depth security controls
- Configuring safe inputs and safe outputs
- Setting up threat detection and monitoring
- Establishing security review processes for AI-generated content
- Responding to security incidents in agentic workflows

## Rules

### Defense-in-Depth Architecture

**MUST:**
- Implement security controls at every layer:
  - **Compilation**: Validate workflow structure, tools, permissions
  - **Runtime**: Isolate agent execution, sandbox operations
  - **Permission**: Enforce least privilege, separate concerns
  - **Network**: Control external access, allowlist domains
  - **Output**: Sanitize and validate before applying changes
- Use multiple overlapping security controls
- Design for graceful degradation if one control fails
- Assume breach mentality (one layer may be compromised)
- Log all security-relevant events

**MUST NOT:**
- Rely on single security control
- Skip security layers for convenience
- Assume AI agents are inherently trustworthy
- Bypass security controls for speed

### Principle of Least Privilege

**MUST:**
- Start with `permissions: read-all` as default
- Grant write permissions only through safe-outputs
- Use fine-grained Personal Access Tokens with minimal scopes
- Time-limit elevated permissions
- Audit permission usage regularly
- Document justification for elevated permissions

**MUST NOT:**
- Use `permissions: write-all` without explicit security review
- Grant repository-wide write access to workflows
- Use classic PATs instead of fine-grained tokens
- Allow unrestricted network access
- Bypass permission checks

### Safe Outputs (Write Operations Without Write Permissions)

**MUST:**
- Configure all write operations in `safe-outputs:` section
- Set reasonable limits with `max:` parameter
- Use separate permission-controlled jobs to execute safe outputs
- Validate AI-generated content before applying
- Include human review gates for critical operations
- Log all safe output executions

**MUST NOT:**
- Grant direct write permissions when safe-outputs can be used
- Set excessive `max:` limits without justification
- Skip validation of AI-generated content
- Auto-merge AI-generated pull requests without review
- Bypass safe output mechanisms

### Safe Inputs (Custom Tools)

**MUST:**
- Define custom tools inline using `safe-inputs:` section
- Use typed input parameters with validation
- Scope tool access appropriately
- Provide clear descriptions for each tool
- Use environment variables for secrets (never hard-code)
- Test tools thoroughly before production use

**MUST NOT:**
- Execute arbitrary code from external sources
- Trust user input without validation
- Expose secrets in tool definitions
- Grant excessive capabilities to custom tools
- Skip input sanitization

### Threat Detection

**MUST:**
- Enable automatic threat detection for safe-outputs workflows
- Configure `threat-detection:` settings appropriately
- Review threat detection alerts promptly
- Block workflow execution on critical threats
- Monitor for prompt injection attempts
- Scan for exposed credentials in outputs
- Detect malicious code patterns

**MUST NOT:**
- Disable threat detection without security review
- Ignore threat detection warnings
- Auto-approve flagged outputs
- Skip investigation of security alerts

### Network Security

**MUST:**
- Use `network:` configuration to control external access
- Start with `network: {}` (no external access) for sensitive workflows
- Use `network: defaults` for common development infrastructure
- Explicitly allowlist required domains
- Document why external access is needed
- Use HTTPS for all external communications
- Validate SSL/TLS certificates

**MUST NOT:**
- Allow unrestricted internet access without justification
- Use HTTP for sensitive communications
- Trust external APIs without validation
- Bypass certificate validation
- Access untrusted domains

### Secret Management

**MUST:**
- Store all secrets in GitHub Secrets (repository or organization level)
- Use descriptive secret names (e.g., `ANTHROPIC_API_KEY`)
- Rotate secrets regularly
- Use fine-grained PATs with minimal scopes
- Document required secrets in workflow documentation
- Audit secret access patterns
- Revoke compromised secrets immediately

**MUST NOT:**
- Hard-code secrets in workflow files
- Commit secrets to version control
- Share secrets between unrelated workflows
- Use overly permissive tokens
- Log secret values
- Expose secrets in error messages

### Prompt Injection Protection

**MUST:**
- Validate and sanitize all user inputs
- Use structured data formats (JSON, YAML) for inputs
- Implement input length limits
- Escape special characters in user content
- Separate instructions from user data
- Use safe-inputs for user-provided data
- Monitor for injection attempts

**MUST NOT:**
- Trust user input in issue titles, bodies, or comments
- Include raw user input in system prompts
- Execute commands containing user input without validation
- Allow users to modify workflow instructions
- Skip input validation for "trusted" users

### Audit and Monitoring

**MUST:**
- Log all workflow executions with timestamps
- Record AI model interactions and decisions
- Track safe output usage and approvals
- Monitor for unusual patterns or behaviors
- Generate security audit trails
- Review logs regularly
- Alert on suspicious activities

**MUST NOT:**
- Disable logging for performance
- Delete logs before retention period
- Log sensitive data (passwords, tokens)
- Ignore monitoring alerts
- Skip periodic security reviews

### Human-in-the-Loop Controls

**MUST:**
- Require human approval for critical operations:
  - Production deployments
  - Data modifications
  - Security-sensitive changes
  - User-facing content
- Implement approval workflows for safe-outputs
- Provide clear context for approval decisions
- Time-limit approval windows
- Escalate approval failures

**MUST NOT:**
- Auto-approve all AI-generated changes
- Skip review for "low-risk" operations without assessment
- Combine approval and execution in same role
- Allow expired approvals

## Examples

### Example 1: Minimal Security Configuration

```markdown
---
on: issues
permissions: read-all  # Read-only default
tools:
  github:
network: {}  # No external network access
safe-outputs:
  create-comment:
    max: 1  # Single comment per execution
---

# Secure Issue Triage

Analyze issue and post triage comment.
```

### Example 2: Safe Outputs with Threat Detection

```markdown
---
on: pull_request
permissions: read-all
tools:
  github:
safe-outputs:
  create-comment:
    max: 3
  threat-detection:
    enabled: true
    scan-for:
      - prompt-injection
      - secret-leak
      - malicious-code
    action: block  # Block on threats
---

# Secure Code Review

Review pull request for security issues.
Threat detection automatically scans outputs before posting.
```

### Example 3: Safe Inputs with Validation

```markdown
---
on: issues
permissions: read-all
tools:
  github:
safe-inputs:
  calculate_risk_score:
    type: function
    description: Calculate security risk score
    code: |
      function calculate_risk_score(title, labels) {
        // Input validation
        if (!title || typeof title !== 'string') return 0;
        if (!Array.isArray(labels)) return 0;
        
        let score = 0;
        // Sanitize inputs
        const safetitle = String(title).toLowerCase();
        
        if (labels.includes('security')) score += 10;
        if (labels.includes('vulnerability')) score += 10;
        if (safetitle.includes('rce')) score += 8;
        if (safetitle.includes('sql injection')) score += 8;
        
        return Math.min(score, 10);
      }
safe-outputs:
  create-comment:
    max: 1
---

# Security Risk Assessment

Use calculate_risk_score to assess security issues.
Post risk score and recommended response timeline.
```

### Example 4: Network-Restricted Workflow

```markdown
---
on: workflow_dispatch
permissions: read-all
tools:
  github:
network:
  defaults:
    - github.com
    - api.github.com
    - raw.githubusercontent.com
  # Explicitly no other domains allowed
safe-outputs:
  create-issue:
    max: 1
---

# Security Audit (Network Restricted)

Perform security audit using only GitHub APIs.
No external network access to prevent data exfiltration.
```

### Example 5: SARIF Security Report

```markdown
---
on: pull_request
permissions: read-all
tools:
  github:
safe-outputs:
  create-code-scanning-alert:
    max: 1
---

# Security Code Scanning

Analyze code changes for security vulnerabilities:
1. Check for hard-coded secrets
2. Identify injection vulnerabilities
3. Detect unsafe deserialization
4. Find insecure cryptography usage

Generate SARIF report and upload to GitHub Code Scanning.
```

### Example 6: Asset Upload Security

```markdown
---
on: workflow_dispatch
permissions: read-all
tools:
  github:
  playwright:
safe-outputs:
  upload-asset:
    branch: "assets/security-reports"
    max-size: 5120  # 5MB limit
    allowed-exts: [.png, .pdf, .json]
---

# Security Screenshot Generation

Generate security dashboard screenshots.
Upload only allowed file types to isolated branch.
```

### Example 7: Multi-Layer Security

```markdown
---
on: issues
permissions: read-all
tools:
  github:
network:
  defaults:  # Layer 1: Network restriction
safe-inputs:  # Layer 2: Validated custom tools
  sanitize_input:
    type: function
    code: |
      function sanitize_input(text) {
        return String(text)
          .replace(/[<>]/g, '')
          .substring(0, 1000);
      }
safe-outputs:  # Layer 3: Safe write operations
  create-comment:
    max: 1
  threat-detection:  # Layer 4: Output validation
    enabled: true
    action: block
---

# Defense-in-Depth Security Analysis

Multi-layer security for issue analysis.
```

### Example 8: Fine-Grained Token Configuration

```markdown
---
on: pull_request
permissions: read-all
tools:
  github:
safe-outputs:
  update-project:
    # Use fine-grained PAT with minimal scopes:
    # - Read access to metadata
    # - Write access to projects
    github-token: ${{ secrets.GH_AW_PROJECT_TOKEN }}
    max: 1
---

# Secure Project Board Update

Update project board with PR status.
Uses minimal-scope token for Projects API only.
```

## Security Checklist

Before deploying an agentic workflow:

### Design Phase
- [ ] Threat model completed
- [ ] Security requirements documented
- [ ] Least privilege design implemented
- [ ] Defense-in-depth layers identified

### Implementation Phase
- [ ] Read-only permissions by default
- [ ] Safe-outputs configured for write operations
- [ ] Network access restricted appropriately
- [ ] Safe-inputs validated and tested
- [ ] Secrets stored securely (not in code)
- [ ] Threat detection enabled

### Testing Phase
- [ ] Prompt injection tests passed
- [ ] Permission boundaries validated
- [ ] Safe-output limits tested
- [ ] Network isolation verified
- [ ] Secret exposure tests passed
- [ ] Threat detection alerts reviewed

### Deployment Phase
- [ ] Security review completed
- [ ] Secrets configured correctly
- [ ] Monitoring and alerting enabled
- [ ] Incident response plan documented
- [ ] Rollback procedure tested

### Operations Phase
- [ ] Logs reviewed regularly
- [ ] Threat detection alerts monitored
- [ ] Permission usage audited
- [ ] Security metrics tracked
- [ ] Incident response procedures tested

## Incident Response

### Detection
1. Monitor threat detection alerts
2. Review unusual workflow patterns
3. Check for unexpected safe-output executions
4. Investigate failed permission checks

### Containment
1. Pause affected workflows immediately
2. Revoke compromised tokens
3. Block suspicious network access
4. Isolate affected repositories

### Eradication
1. Identify root cause
2. Remove malicious content
3. Update workflow security controls
4. Patch vulnerabilities

### Recovery
1. Verify security controls are effective
2. Re-enable workflows with enhanced monitoring
3. Validate normal operations
4. Document lessons learned

### Post-Incident
1. Conduct security review
2. Update security procedures
3. Train team on new threats
4. Improve detection capabilities

## Security Anti-Patterns

### ❌ Excessive Permissions
```markdown
---
permissions: write-all  # WRONG: Too broad
---
```

**✅ Correct Approach:**
```markdown
---
permissions: read-all
safe-outputs:
  create-comment:
    max: 1
---
```

### ❌ Hard-Coded Secrets
```markdown
---
engine: claude
env:
  ANTHROPIC_API_KEY: sk-ant-abc123  # WRONG: Secret in code
---
```

**✅ Correct Approach:**
```markdown
---
engine: claude
# Secret configured in GitHub Secrets
---
```

### ❌ Unrestricted Network
```markdown
---
tools:
  web-fetch:  # WRONG: No network restrictions
---
```

**✅ Correct Approach:**
```markdown
---
tools:
  web-fetch:
network:
  defaults:
    - trusted-domain.com
---
```

### ❌ No Threat Detection
```markdown
---
safe-outputs:
  create-pull-request:
    max: 1
  # WRONG: No threat detection
---
```

**✅ Correct Approach:**
```markdown
---
safe-outputs:
  create-pull-request:
    max: 1
  threat-detection:
    enabled: true
    action: block
---
```

### ❌ Trusting User Input
```markdown
# WRONG: Using raw issue title in command
Execute: analyze-tool --input="${issue.title}"
```

**✅ Correct Approach:**
```markdown
# Sanitize user input before use
safe-inputs:
  sanitize:
    code: |
      function sanitize(input) {
        return input.replace(/[^a-zA-Z0-9 ]/g, '');
      }
```

## Related ISMS Policies

This skill implements requirements from:

- **[Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md)** - Secure automation and AI practices
- **[Access Control Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Access_Control_Policy.md)** - Least privilege and permission management
- **[Cryptographic Controls Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Cryptographic_Controls_Policy.md)** - Secure secret management
- **[Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)** - Overall security framework
- **[Incident Response Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Incident_Response_Policy.md)** - Security incident handling

## Related Skills

- **[GitHub Agentic Workflows](../github-agentic-workflows/SKILL.md)** - Core workflow fundamentals
- **[Secure Development](../../security/secure-development/SKILL.md)** - General secure coding practices
- **[Access Control](../../security/access-control/SKILL.md)** - Permission and authentication patterns
- **[Cryptography](../../security/cryptography/SKILL.md)** - Secure secret management

## Related Documentation

- [GitHub Agentic Workflows Security Guide](https://githubnext.github.io/gh-aw/guides/security/)
- [GitHub Actions Security Best Practices](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)
- [OWASP AI Security and Privacy Guide](https://owasp.org/www-project-ai-security-and-privacy-guide/)

## Compliance Mapping

### ISO 27001:2022
- **A.5.23** Information security for use of cloud services
- **A.8.24** Use of cryptography
- **A.8.25** Secure development life cycle
- **A.8.28** Secure coding
- **A.16.1** Management of information security incidents

### NIST Cybersecurity Framework 2.0
- **GV.RM-02**: Risk appetite and tolerance are established
- **PR.AA-01**: Identities are established, managed, and assured
- **PR.DS-02**: Data-in-transit is protected
- **DE.CM-01**: Network traffic is monitored

### CIS Controls v8.1
- **Control 3**: Data Protection
  - 3.3 Configure Data Access Control Lists
- **Control 4**: Secure Configuration
  - 4.1 Establish and Maintain a Secure Configuration Process
- **Control 6**: Access Control Management
  - 6.1 Establish an Access Granting Process
  - 6.8 Define and Maintain Role-Based Access Control

## Enforcement

Security violations in agentic workflows:
- **Critical**: Exposed secrets, unrestricted permissions, disabled security controls - Immediate incident response
- **High**: Missing threat detection, unsafe tool configuration - Block deployment
- **Medium**: Excessive permissions, missing network restrictions - Require remediation
- **Low**: Incomplete logging, missing documentation - Create improvement tickets

## Version History

- **2026-02-11**: Initial skill creation based on latest GitHub Agentic Workflows security features

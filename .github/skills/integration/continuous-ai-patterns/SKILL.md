---
name: continuous-ai-patterns
description: Continuous AI automation patterns for documentation sync, code quality, issue triage, and automated review using GitHub Agentic Workflows
license: Apache-2.0
---

# 🔄 Continuous AI Patterns Skill

## Purpose

This skill provides comprehensive guidance on implementing Continuous AI - systematic, automated application of AI to software collaboration. Continuous AI extends beyond traditional CI/CD by handling judgment-heavy, context-dependent tasks that previously required human intervention, such as documentation maintenance, code quality improvements, issue triage, and intelligent review.

## When to Use

Apply this skill when:
- Implementing automated documentation maintenance
- Setting up intelligent issue and PR triage
- Creating automated code quality improvements
- Building AI-assisted code review systems
- Maintaining repository health automatically
- Automating repetitive cognitive tasks
- Implementing feedback loops for continuous improvement

## Rules

### Continuous AI Principles

**MUST:**
- Start with low-risk, high-value automation
- Implement human review loops for critical changes
- Monitor AI performance and accuracy
- Iterate based on feedback
- Measure outcomes and ROI
- Document automation decisions
- Maintain human oversight

**MUST NOT:**
- Automate without monitoring
- Skip human review for production changes
- Ignore AI errors or low-quality outputs
- Implement without success metrics
- Auto-merge without validation

### Documentation Sync Pattern

**MUST:**
- Check documentation against codebase regularly (daily/weekly)
- Identify stale or incorrect documentation
- Generate specific, accurate updates
- Create pull requests for human review
- Link documentation changes to code changes
- Maintain documentation changelog

**MUST NOT:**
- Auto-merge documentation changes without review
- Generate generic or vague documentation
- Update documentation without verifying accuracy
- Skip linking to relevant code

### Issue Triage Pattern

**MUST:**
- Analyze new issues immediately
- Check for duplicates across repository
- Assess issue clarity and completeness
- Suggest appropriate labels and priorities
- Request clarification when needed
- Track triage accuracy metrics

**MUST NOT:**
- Auto-close issues without review
- Assign issues without team confirmation
- Ignore incomplete issue descriptions
- Skip duplicate detection

### Code Quality Pattern

**MUST:**
- Scan for code quality issues systematically
- Prioritize issues by severity and impact
- Generate specific, actionable suggestions
- Create issues or comments with clear remediation steps
- Track quality metrics over time
- Focus on incremental improvements

**MUST NOT:**
- Overwhelm team with too many suggestions
- Make style changes without team consensus
- Auto-apply code changes without review
- Ignore project-specific patterns

### Automated Review Pattern

**MUST:**
- Review all pull requests for common issues
- Check security vulnerabilities
- Verify test coverage
- Validate documentation updates
- Provide constructive, educational feedback
- Escalate critical issues immediately

**MUST NOT:**
- Replace human code review entirely
- Block PRs without clear justification
- Provide vague or generic feedback
- Ignore context or special cases

### Dependency Management Pattern

**MUST:**
- Monitor dependencies for updates and vulnerabilities
- Assess update impact and breaking changes
- Generate upgrade pull requests with testing notes
- Track dependency health metrics
- Prioritize security updates

**MUST NOT:**
- Auto-merge dependency updates
- Ignore breaking changes
- Update without testing
- Skip release notes review

### Repository Health Pattern

**MUST:**
- Generate periodic health reports
- Track key metrics (issue velocity, PR age, test coverage)
- Identify trends and patterns
- Provide actionable recommendations
- Alert on anomalies or degradation

**MUST NOT:**
- Generate reports without analysis
- Ignore metric trends
- Overwhelm with data
- Skip actionable recommendations

### Feedback Loop Pattern

**MUST:**
- Collect feedback on AI-generated content
- Measure accuracy and usefulness
- Iterate workflow instructions based on feedback
- Track improvement over time
- Document learnings

**MUST NOT:**
- Ignore negative feedback
- Assume AI is always correct
- Skip iterative improvement
- Fail to measure success

## Examples

### Example 1: Daily Documentation Sync

```markdown
---
on: daily at 9am
permissions: read-all
tools:
  github:
  edit:
safe-outputs:
  create-pull-request:
    max: 1
---

# Daily Documentation Sync

Maintain documentation currency automatically:

## Phase 1: Analysis
1. Compare README.md with actual project structure
2. Check API documentation against current endpoints
3. Verify example code still works
4. Check for undocumented new features (commits in last 7 days)
5. Identify outdated screenshots or diagrams

## Phase 2: Updates
If discrepancies found:
1. Update affected documentation files
2. Regenerate examples if needed
3. Update version numbers if changed

## Phase 3: Pull Request
Create PR titled "docs: Daily sync - [DATE]" with:
- Clear list of changes made
- Links to relevant code changes
- Screenshots if UI documentation updated
- Label: `documentation`, `automated`

## Quality Criteria
- All code examples must be syntactically correct
- Links must be valid
- Changes must be specific, not generic
```

### Example 2: Intelligent Issue Triage

```markdown
---
on: issues
permissions: read-all
tools:
  github:
  web-search:
safe-outputs:
  create-comment:
    max: 1
---

# Intelligent Issue Triage

Provide comprehensive triage for new issues:

## Step 1: Duplicate Detection
Search existing issues (open and closed) for duplicates.
If duplicate found, post comment with link and recommend closure.

## Step 2: Clarity Assessment
Evaluate if issue is clear and actionable:
- Is the problem clearly described?
- Are reproduction steps provided (for bugs)?
- Are success criteria defined (for features)?

If unclear, politely request clarification.

## Step 3: Categorization
Suggest labels based on content:
- Bug vs. Feature vs. Documentation
- Affected components
- Severity indicators
- Effort estimation

## Step 4: Similar Issues Search
Search web for similar issues in related projects.
Provide links to potential solutions or discussions.

## Step 5: Recommendation
Provide structured triage comment:
```
## Triage Analysis

**Type**: [Bug/Feature/Docs/Question]
**Priority**: [High/Medium/Low] - [Justification]
**Suggested Labels**: label1, label2, label3

### Analysis
[Clear explanation of issue understanding]

### Duplicates
[List any duplicates found, or "None found"]

### Similar Issues
[Links to related issues/discussions]

### Recommendations
[Specific next steps]
```

Include disclaimer: This is an automated triage. Human review recommended.
```

### Example 3: Weekly Code Quality Report

```markdown
---
on: weekly on friday
permissions: read-all
tools:
  github:
  bash:
safe-outputs:
  create-issue:
    max: 1
---

# Weekly Code Quality Report

Generate comprehensive code quality analysis:

## Analysis Areas

### 1. Code Coverage
- Run test suite with coverage reporting
- Compare to previous week
- Identify files/modules with low coverage

### 2. Static Analysis
- Run linters and static analyzers
- Count warnings by category
- Identify new issues vs. existing issues

### 3. Code Complexity
- Analyze cyclomatic complexity
- Identify overly complex functions
- Compare to thresholds

### 4. Technical Debt
- Count TODO/FIXME comments
- Estimate technical debt by age
- Prioritize debt items

### 5. Dependency Health
- Check for outdated dependencies
- Identify security vulnerabilities
- List unmaintained dependencies

## Report Generation

Create issue titled "Weekly Code Quality Report - [DATE]":

```markdown
# Code Quality Report - Week [NUMBER]

## Summary
- Overall Health Score: [X/100]
- Trend: [Improving/Stable/Declining]

## Coverage: [X%] ([+/-Y%] from last week)
Files below 80% coverage:
- file1.js: 65%
- file2.py: 72%

## Static Analysis: [X] issues ([+/-Y] from last week)
- Critical: [X]
- High: [X]
- Medium: [X]

Top issues:
1. [Issue type]: [Count] occurrences
2. [Issue type]: [Count] occurrences

## Complexity
Functions exceeding complexity threshold (>15):
- function1: 23
- function2: 18

## Technical Debt: [X] items
Priority items:
1. [TODO description] - Age: [X] days
2. [TODO description] - Age: [X] days

## Dependencies
- Outdated: [X] packages
- Security issues: [X] vulnerabilities
- Unmaintained: [X] packages

## Recommendations
1. [Specific action]
2. [Specific action]
3. [Specific action]

## Action Items
Create issues for:
- [ ] Critical security vulnerabilities
- [ ] Files with <60% coverage
- [ ] Functions with complexity >20
```

Labels: `quality`, `automated`, `weekly-report`
```

### Example 4: PR Security Review

```markdown
---
on: pull_request
permissions: read-all
tools:
  github:
safe-outputs:
  create-comment:
    max: 5
  create-code-scanning-alert:
    max: 1
---

# Automated Security Review

Perform comprehensive security analysis of PR:

## Security Checks

### 1. Hard-Coded Secrets
Scan for:
- API keys, tokens, passwords
- Private keys or certificates
- Database connection strings
- AWS/Cloud credentials

### 2. Injection Vulnerabilities
Check for:
- SQL injection risks (string concatenation in queries)
- Command injection (unsanitized input in exec/system calls)
- XSS vulnerabilities (unescaped output)
- Path traversal (user input in file paths)

### 3. Authentication & Authorization
Verify:
- Authentication checks on new endpoints
- Authorization enforcement
- Session management security
- Password handling (if applicable)

### 4. Cryptography
Check for:
- Weak algorithms (MD5, SHA-1, DES)
- Hard-coded encryption keys
- Insecure random number generation
- Missing TLS/SSL

### 5. Dependencies
Scan for:
- New dependencies with known vulnerabilities
- Outdated dependency versions
- Suspicious or unmaintained packages

## Reporting

For each finding:
1. Post inline comment on specific line
2. Explain security risk clearly
3. Provide remediation guidance
4. Include OWASP/CWE references when relevant

Generate SARIF report for Code Scanning.

## Comment Format
```
🔒 **Security Issue: [Category]**

**Risk**: [High/Medium/Low]
**CWE**: [CWE-XXX]

**Issue**: [Clear description]

**Recommendation**: [Specific fix]

**References**:
- [Link to documentation]
- [Link to best practices]
```

Add label `security-review-completed` when done.
```

### Example 5: Stale Issue Cleanup

```markdown
---
on: daily
permissions: read-all
tools:
  github:
safe-outputs:
  create-comment:
    max: 10
  minimize-comment:
    max: 5
---

# Stale Issue Management

Manage stale issues and keep repository tidy:

## Phase 1: Identify Stale Issues
Find issues that:
- No activity in 60 days
- Labeled as `needs-info` or `waiting-response`
- Not labeled as `long-term` or `backlog`

## Phase 2: Assess Relevance
For each stale issue:
1. Review issue content and comments
2. Check if issue is still relevant
3. Verify if issue blocks other work
4. Check for related recent commits

## Phase 3: Action
Based on assessment:

**Still Relevant**:
- Post comment asking for status update
- Suggest closing if no response in 14 days
- Remove `needs-info` if enough information now available

**No Longer Relevant**:
- Post comment explaining why issue may be outdated
- Suggest verification and potential closure
- Link to related closed issues if applicable

**Duplicate or Resolved**:
- Post comment with link to duplicate/resolution
- Recommend closure

## Phase 4: Cleanup
- Minimize spam comments on stale issues
- Update labels appropriately
- Generate summary of actions taken

Post summary comment on tracking issue.
```

### Example 6: Automated Test Failure Analysis

```markdown
---
on: 
  workflow_run:
    workflows: ["CI"]
    types: [completed]
permissions: read-all
tools:
  github:
  bash:
safe-outputs:
  create-comment:
    max: 1
---

# Test Failure Analysis

When CI workflow fails, provide intelligent analysis:

## Condition Check
Only proceed if:
- Workflow conclusion is "failure"
- Triggered by pull request
- Test failures present (not build/lint failures)

## Analysis

### 1. Identify Failed Tests
Parse test output to extract:
- Failed test names
- Error messages
- Stack traces

### 2. Classify Failures
Categorize as:
- Flaky test (intermittent failure)
- Environmental issue
- Regression (new code broke test)
- Test needs update (expected behavior changed)

### 3. Search for Patterns
- Check if test failed recently in other PRs
- Search for related issues
- Check if files changed are related to test

### 4. Root Cause Hypothesis
Generate hypothesis about failure cause based on:
- Error message analysis
- Recent code changes
- Historical failure patterns

## Report

Post comment on PR:
```markdown
## 🔴 Test Failure Analysis

### Failed Tests
- `test_authentication`: Authentication token validation failed
- `test_user_permissions`: Permission check returned unexpected result

### Analysis

**test_authentication**
- **Classification**: Regression
- **Hypothesis**: Recent changes to auth module (auth.py:45-67) may have altered token validation logic
- **Evidence**: Test passed on main branch, started failing after commit abc123
- **Recommendation**: Review authentication token generation changes

**test_user_permissions**
- **Classification**: Flaky Test
- **Hypothesis**: Test has intermittent failures (3 failures in last 10 runs)
- **Evidence**: No related code changes in this PR
- **Recommendation**: Consider adding test stability improvements

### Related Issues
- Similar failure: #123
- Tracking issue for flaky tests: #456

### Suggested Actions
1. Review auth.py changes carefully
2. Add unit test for new token validation logic
3. Consider quarantining flaky test until stabilized
```

Labels: `test-failure`, `needs-investigation`
```

### Example 7: Dependency Update Workflow

```markdown
---
on: weekly on monday
permissions: read-all
tools:
  github:
  bash:
safe-outputs:
  create-pull-request:
    max: 1
---

# Automated Dependency Updates

Intelligently update dependencies:

## Phase 1: Scan for Updates
1. Run dependency checker (npm outdated, pip list --outdated, etc.)
2. Identify available updates
3. Categorize:
   - Security updates (high priority)
   - Major version updates (breaking changes)
   - Minor/patch updates (safe)

## Phase 2: Risk Assessment
For each update:
- Check changelog for breaking changes
- Review security advisory if security update
- Estimate impact (low/medium/high)
- Check compatibility with current code

## Phase 3: Update Strategy
**Security Updates**:
- Apply immediately
- Include security advisory details in PR

**Patch Updates**:
- Batch together if multiple available
- Low risk, apply confidently

**Minor Updates**:
- Batch similar packages
- Include feature highlights in PR

**Major Updates**:
- Create separate issue for planning
- Document breaking changes
- Don't auto-apply

## Phase 4: Create PR
For safe updates (security + patch + minor):

1. Update dependency files
2. Run tests locally if possible
3. Create PR with detailed description:

```markdown
# Dependency Updates - [DATE]

## Summary
- Security updates: [X]
- Minor updates: [X]
- Patch updates: [X]

## Security Updates
- **package1** v1.2.3 → v1.2.4
  - CVE-2024-XXXX: [Description]
  - Severity: High
  - [Security Advisory Link]

## Minor Updates
- **package2** v2.3.0 → v2.4.0
  - New features: [List]
  - [Changelog link]

## Patch Updates
- **package3** v3.4.5 → v3.4.6
  - Bug fixes only

## Testing Notes
- All tests passed locally
- No breaking changes identified
- Review suggested for: [package] due to [reason]

## Action Required
- [ ] Review security advisory for package1
- [ ] Verify package2 new features don't conflict
- [ ] Run full test suite
```

Labels: `dependencies`, `automated`, `security` (if applicable)

## Phase 5: Major Version Issue
For major updates, create tracking issue with upgrade plan.
```

### Example 8: Repository Health Dashboard

```markdown
---
on: weekly on sunday
permissions: read-all
tools:
  github:
  bash:
  playwright:
safe-outputs:
  create-issue:
    max: 1
  upload-asset:
    branch: "assets/health-dashboard"
    max-size: 2048
    allowed-exts: [.png]
---

# Weekly Repository Health Dashboard

Generate comprehensive repository health dashboard:

## Metrics Collection

### Activity Metrics
- Commits this week vs. last week
- PRs opened/closed/merged
- Issues opened/closed
- Active contributors this week

### Quality Metrics
- Test coverage percentage
- Build success rate
- Average PR review time
- Code review comment rate

### Health Indicators
- PR age (open PRs > 7 days)
- Issue age (open issues > 30 days)
- Stale branches count
- Dependency freshness score

### Community Metrics
- New contributors this month
- Comment/response rate
- First-time contributor experience

## Visualization
Generate dashboard image using Playwright:
- Metrics summary cards
- Trend charts (week-over-week)
- Health score gauge
- Top contributors

Upload dashboard.png to assets branch.

## Report Generation
Create issue titled "📊 Repository Health - Week [NUMBER]":

```markdown
# Repository Health Dashboard
![Dashboard](link-to-dashboard.png)

## 🎯 Health Score: [X/100] ([+/-Y] from last week)

## 📈 Activity (Week over Week)
- Commits: [X] ([+/-Y%])
- PRs Merged: [X] ([+/-Y%])
- Issues Closed: [X] ([+/-Y%])

## ✅ Quality
- Test Coverage: [X%] ([+/-Y%])
- Build Success Rate: [X%]
- Avg PR Review Time: [X] hours

## ⚠️ Attention Needed
- [X] PRs open > 7 days
- [X] issues open > 30 days
- [X] stale branches

## 👥 Contributors
- Active this week: [X]
- New contributors: [X]
- Top contributors: @user1, @user2, @user3

## 📋 Recommendations
1. [Specific action based on metrics]
2. [Specific action based on metrics]
3. [Specific action based on metrics]

## 🔗 Quick Links
- [Open PRs](link)
- [Old Issues](link)
- [Stale Branches](link)
```

Labels: `health-report`, `weekly`, `automated`
Assign to: @repository-maintainers
```

## Continuous AI Best Practices

### Start Small
- Begin with read-only analysis workflows
- Graduate to suggestion workflows
- Finally implement automated change workflows
- Always maintain human oversight

### Measure Success
- Define clear success metrics
- Track accuracy and usefulness
- Monitor costs and resource usage
- Gather user feedback
- Iterate based on data

### Maintain Quality
- Review AI outputs regularly
- Refine instructions based on outcomes
- Update workflows as repository evolves
- Document what works and what doesn't

### Scale Gradually
- Prove value with pilot workflows
- Expand successful patterns
- Retire ineffective workflows
- Balance automation with human judgment

## Related ISMS Policies

This skill aligns with:

- **[Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md)** - Automated security practices
- **[Change Management Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Change_Management_Policy.md)** - Automated change workflows
- **[Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)** - Overall security framework

## Related Skills

- **[GitHub Agentic Workflows](../github-agentic-workflows/SKILL.md)** - Core workflow fundamentals
- **[Agentic Workflow Security](../agentic-workflow-security/SKILL.md)** - Security for automation
- **[Agentic Workflow Orchestration](../agentic-workflow-orchestration/SKILL.md)** - Complex workflow coordination
- **[Testing Strategy](../../development/testing-strategy/SKILL.md)** - Automated testing patterns
- **[Code Review Practices](../../development/code-review-practices/SKILL.md)** - Review automation

## Related Documentation

- [Continuous AI Blog Post](https://github.blog/ai-and-ml/generative-ai/continuous-ai-in-practice-what-developers-can-automate-today-with-agentic-ci/)
- [GitHub Agentic Workflows Patterns](https://github.github.com/gh-aw/patterns/)
- [GitHub Actions Best Practices](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions)

## Compliance Mapping

### ISO 27001:2022
- **A.8.25** Secure development life cycle
- **A.8.32** Change management
- **A.5.37** Documented operating procedures

### NIST Cybersecurity Framework 2.0
- **PR.IP-02**: System development lifecycle
- **PR.DS-06**: Integrity checking mechanisms
- **DE.CM-08**: Vulnerability scans performed

### CIS Controls v8.1
- **Control 16**: Application Software Security
  - 16.2 Address Software Vulnerabilities
  - 16.11 Leverage Vetted Modules

## Enforcement

Continuous AI pattern violations:
- **Critical**: Auto-merging without review, security bypass - Immediate incident response
- **High**: Missing human oversight, no success metrics - Block deployment
- **Medium**: Poor AI quality, missing monitoring - Require remediation
- **Low**: Optimization opportunities, documentation gaps - Optional improvements

## Version History

- **2026-02-11**: Initial skill creation based on latest Continuous AI patterns and best practices

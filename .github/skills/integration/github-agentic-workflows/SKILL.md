---
name: github-agentic-workflows
description: Fundamentals of GitHub Agentic Workflows - structure, compilation, triggers, and natural language automation
license: Apache-2.0
---

# 🤖 GitHub Agentic Workflows Skill

## Purpose

This skill provides comprehensive guidance on GitHub Agentic Workflows, a revolutionary approach to repository automation that uses AI to understand context, make decisions, and take autonomous actions through natural language instructions. Unlike traditional workflows with fixed if/then logic, agentic workflows interpret context and adapt behavior based on specific situations.

GitHub Agentic Workflows enables **Continuous AI** - systematic, automated application of AI to software collaboration tasks like triaging issues, maintaining documentation, improving code quality, and automating reviews.

## When to Use

Apply this skill when:
- Creating AI-powered repository automation workflows
- Converting deterministic GitHub Actions to intelligent, context-aware workflows
- Implementing continuous AI patterns for issue triage, documentation sync, or code review
- Building workflows that require judgment, synthesis, or content generation
- Automating tasks that traditionally require human decision-making

## Rules

### Workflow Structure

**MUST:**
- Create workflow files as Markdown (`.md`) in `.github/workflows/` directory
- Include YAML frontmatter between `---` markers at the top of the file
- Write natural language instructions below the frontmatter
- Compile Markdown workflows to `.lock.yml` files using `gh aw compile`
- Commit both `.md` (source) and `.lock.yml` (compiled) files to version control
- Use declarative, clear, imperative task descriptions in natural language
- Separate configuration (frontmatter) from instructions (markdown body)

**MUST NOT:**
- Write complex YAML conditionals or programming logic in workflow files
- Rely solely on `.lock.yml` files (they are generated artifacts)
- Mix configuration and instructions in the same section
- Use traditional GitHub Actions YAML syntax for agentic workflows
- Skip compilation step before deployment

### Frontmatter Configuration

**MUST:**
- Define `on:` trigger(s) for when the workflow runs
- Set `permissions:` (default to `read-all` for security)
- Configure `tools:` that the AI agent can use
- Specify `engine:` if not using default GitHub Copilot
- Include `safe-outputs:` for any write operations

**MUST NOT:**
- Grant unnecessary write permissions
- Use `permissions: write-all` without explicit justification
- Omit critical configuration fields
- Hard-code secrets in frontmatter

### Natural Language Instructions

**MUST:**
- Write clear, specific, actionable task descriptions
- Use imperative mood ("Analyze this issue", not "You should analyze")
- Include context about what the workflow should accomplish
- Define success criteria and constraints
- Specify expected outputs (comments, PRs, issues)
- Break complex tasks into clear phases
- Provide examples of expected behavior

**MUST NOT:**
- Write vague instructions ("Do something helpful")
- Assume the AI knows implicit context
- Include implementation details (let AI determine approach)
- Write instruction text that looks like code or YAML

### Engines (AI Models)

**MUST:**
- Use GitHub Copilot as default engine (no explicit configuration needed)
- Configure appropriate secrets for alternative engines:
  - Claude: `ANTHROPIC_API_KEY` secret
  - Codex: `OPENAI_API_KEY` secret
- Test workflows with chosen engine before production deployment

**MUST NOT:**
- Mix multiple engines in same workflow
- Assume all engines have identical capabilities
- Skip engine-specific setup documentation

### Triggers

**MUST:**
- Choose appropriate trigger(s) for workflow purpose:
  - `issues:` for issue-related automation
  - `pull_request:` for PR-related automation
  - `schedule:` for periodic tasks
  - `workflow_dispatch:` for manual execution
  - `slash_command:` for comment-triggered actions
- Use human-friendly schedule syntax: `daily`, `weekly on monday`
- Consider rate limits and costs for scheduled workflows
- Test manual triggers before enabling automated triggers

**MUST NOT:**
- Use overly frequent schedules that waste resources
- Trigger on every event type without considering necessity
- Use fixed cron times (prefer scattered schedule syntax)

### Tools and MCP Integration

**MUST:**
- Explicitly configure tools in frontmatter under `tools:` section
- Use `github:` tool for GitHub API operations (issues, PRs, comments)
- Configure network permissions when external API access is needed
- Use `safe-inputs:` for custom lightweight tools
- Use `edit:` tool for file modifications
- Use `bash:` tool for shell commands when needed
- Use `web-search:` or `web-fetch:` for external information
- Document tool purpose and constraints

**MUST NOT:**
- Grant unrestricted tool access without review
- Use tools without understanding their security implications
- Bypass tool allowlists
- Ignore network access controls

### Compilation Process

**MUST:**
- Install gh-aw CLI extension: `gh extension install github/gh-aw`
- Compile workflows: `gh aw compile` (generates `.lock.yml` files)
- Use `gh aw compile --watch` for iterative development
- Review generated `.lock.yml` for security hardening
- Validate compilation errors before pushing changes
- Keep `.md` and `.lock.yml` files synchronized

**MUST NOT:**
- Manually edit `.lock.yml` files (regenerate with compile)
- Push `.md` changes without recompiling
- Ignore compilation warnings or errors
- Skip validation of generated Actions workflow

### Repository Setup

**MUST:**
- Run `gh aw init` to initialize repository for agentic workflows
- Configure required secrets (engine API keys, tokens)
- Set up fine-grained Personal Access Tokens with minimal permissions
- Document secrets configuration in repository README
- Test workflow execution with `gh aw run <workflow-name>`

**MUST NOT:**
- Skip initialization steps
- Use classic PATs instead of fine-grained tokens
- Grant excessive permissions to workflow tokens
- Commit secrets to version control

## Examples

### Example 1: Simple Issue Triage Workflow

```markdown
---
on: issues
permissions: read-all
tools:
  github:
safe-outputs:
  create-comment:
    max: 1
---

# Issue Triage

Analyze new issues and provide helpful triage information:

1. Assess if the issue description is clear and actionable
2. Check if it's a duplicate of existing issues
3. Suggest appropriate labels based on content
4. If the issue is unclear, politely ask for clarification

Provide your analysis as a comment on the issue.
```

### Example 2: Documentation Sync Workflow

```markdown
---
on: daily
permissions: read-all
tools:
  github:
  edit:
safe-outputs:
  create-pull-request:
    max: 1
---

# Daily Documentation Sync

Check if repository documentation is up to date:

1. Review README.md and compare with actual codebase structure
2. Check if API documentation matches current endpoints
3. Verify example code still works with current version
4. Update changelog if recent commits aren't documented

If updates are needed, create a pull request with:
- Clear description of documentation changes
- Reference to relevant code changes
- Explanation of why updates were necessary
```

### Example 3: Code Review Assistant

```markdown
---
on: pull_request
permissions: read-all
tools:
  github:
safe-outputs:
  create-comment:
    max: 5
---

# Code Review Assistant

Provide constructive code review feedback:

1. Check for common security issues (SQL injection, XSS, secrets in code)
2. Identify code style inconsistencies
3. Suggest performance improvements if obvious
4. Check test coverage for new code
5. Verify documentation is updated for API changes

Post review comments on specific lines where issues are found.
Be constructive and educational in your feedback.
```

### Example 4: Weekly Repository Status Report

```markdown
---
on: weekly on monday
permissions: read-all
tools:
  github:
safe-outputs:
  create-issue:
    max: 1
---

# Weekly Repository Health Report

Generate a comprehensive repository status report:

## Analysis Areas

1. **Pull Requests**: Count open PRs, age of oldest PR, stale PRs
2. **Issues**: Count open issues, recently closed issues, issue velocity
3. **Activity**: Commits this week, contributors this month
4. **Dependencies**: Any security alerts or outdated dependencies

Create an issue with the report titled "Weekly Status Report - [DATE]".
Include actionable recommendations for repository maintainers.
```

### Example 5: Slash Command Workflow

```markdown
---
on:
  slash_command:
    command: /analyze
permissions: read-all
tools:
  github:
  web-search:
safe-outputs:
  create-comment:
    max: 1
---

# Issue Analysis Command

When triggered with `/analyze` command on an issue:

1. Search for similar issues in other repositories
2. Find relevant Stack Overflow discussions
3. Check if this is a known issue in dependencies
4. Provide links to relevant documentation

Respond with findings as a comment on the issue.
```

### Example 6: Custom Tool with Safe Inputs

```markdown
---
on: issues
permissions: read-all
tools:
  github:
safe-inputs:
  calculate_priority:
    type: function
    description: Calculate issue priority based on labels and content
    code: |
      function calculate_priority(labels, body) {
        let score = 0;
        if (labels.includes('critical')) score += 10;
        if (labels.includes('security')) score += 8;
        if (labels.includes('bug')) score += 5;
        if (body.toLowerCase().includes('production')) score += 3;
        return score;
      }
safe-outputs:
  create-comment:
    max: 1
---

# Priority Calculator

Use the calculate_priority tool to assess issue priority.
Post a comment with the priority score and recommended action timeline.
```

### Example 7: Network-Restricted Workflow

```markdown
---
on: pull_request
permissions: read-all
tools:
  github:
network:
  defaults:
    - github.com
    - api.github.com
safe-outputs:
  create-comment:
    max: 1
---

# Security-Focused PR Review

Review pull request for security issues.
Only access GitHub APIs - no external network calls allowed.

Focus on:
- Hard-coded secrets or credentials
- Unsafe input handling
- Missing authentication checks
```

### Example 8: Multi-Engine Configuration

```markdown
---
on: workflow_dispatch
engine: claude  # Use Anthropic Claude instead of Copilot
permissions: read-all
tools:
  github:
safe-outputs:
  create-issue:
    max: 1
---

# Advanced Analysis with Claude

Perform deep technical analysis of repository architecture.
Create an issue with findings and recommendations.

Note: Requires ANTHROPIC_API_KEY secret to be configured.
```

## Workflow Best Practices

### Start Simple, Iterate
- Begin with read-only workflows
- Test with `workflow_dispatch` before enabling automatic triggers
- Add safe-outputs incrementally
- Use `gh aw compile --watch` for rapid iteration

### Clear Instructions Win
- Write as if explaining task to a human colleague
- Include examples of desired output
- Define constraints and guardrails explicitly
- Specify what NOT to do when relevant

### Security First
- Use minimal permissions (read-all by default)
- Leverage safe-outputs instead of direct write permissions
- Review AI-generated content before merging
- Monitor workflow costs and usage

### Test Before Deploy
- Use `gh aw run` for manual testing
- Review logs with `gh aw logs`
- Test with real repository data
- Validate safe-outputs are appropriate

### Monitor and Improve
- Track workflow success rates
- Gather feedback from generated outputs
- Refine instructions based on actual behavior
- Update workflows as repository evolves

## Compilation and Deployment Flow

```
1. Author Workflow
   └─ Create .github/workflows/my-workflow.md

2. Compile
   └─ Run: gh aw compile
   └─ Generates: .github/workflows/my-workflow.lock.yml

3. Commit Both Files
   └─ git add .github/workflows/my-workflow.md
   └─ git add .github/workflows/my-workflow.lock.yml
   └─ git commit -m "Add my-workflow"

4. Push to GitHub
   └─ git push

5. Configure Secrets
   └─ Add required API keys/tokens in repository settings

6. Test
   └─ Run: gh aw run my-workflow
   └─ Or: Trigger from GitHub Actions tab

7. Monitor
   └─ Check: gh aw logs
   └─ Review: GitHub Actions logs
```

## Troubleshooting

### Compilation Fails
- Check YAML frontmatter syntax
- Verify all required fields are present
- Review error messages carefully
- Ensure gh-aw CLI is up to date: `gh extension upgrade gh-aw`

### Workflow Doesn't Trigger
- Verify trigger configuration in frontmatter
- Check that `.lock.yml` file exists and is committed
- Review GitHub Actions logs for errors
- Ensure workflow file name matches Actions expectations

### AI Output Quality Issues
- Refine instructions for clarity and specificity
- Add examples of desired outputs
- Include constraints and guardrails
- Consider switching engine if persistent issues

### Permission Errors
- Review permissions in frontmatter
- Check if safe-outputs are properly configured
- Verify secrets are correctly set up
- Ensure token has required scopes

## Related ISMS Policies

This skill aligns with:

- **[Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md)** - Secure automation practices
- **[Access Control Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Access_Control_Policy.md)** - Least privilege for workflows
- **[Cryptographic Controls Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Cryptographic_Controls_Policy.md)** - Secure secret management
- **[Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)** - Overall security framework

## Related Skills

- **[Agentic Workflow Security](../agentic-workflow-security/SKILL.md)** - Security best practices and threat detection
- **[Agentic Workflow Orchestration](../agentic-workflow-orchestration/SKILL.md)** - Multi-agent patterns and coordination
- **[Agentic Workflow Development](../agentic-workflow-development/SKILL.md)** - CLI usage, testing, debugging
- **[Continuous AI Patterns](../continuous-ai-patterns/SKILL.md)** - Automation patterns and best practices
- **[MCP Server Integration](../mcp-server-integration/SKILL.md)** - Model Context Protocol servers
- **[Copilot Agent Patterns](../copilot-agent-patterns/SKILL.md)** - Custom agent design patterns

## Related Documentation

- [GitHub Agentic Workflows Official Documentation](https://github.github.com/gh-aw/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)

## Compliance Mapping

### ISO 27001:2022
- **A.8.25** Secure development life cycle
- **A.8.32** Change management
- **A.5.23** Information security for use of cloud services

### NIST Cybersecurity Framework 2.0
- **GV.OV-03**: Cybersecurity supply chain risk management
- **PR.DS-02**: Data-in-transit is protected
- **DE.CM-07**: Monitoring for unauthorized changes

### CIS Controls v8.1
- **Control 16**: Application Software Security
  - 16.1 Establish and Maintain a Secure Application Development Process
  - 16.11 Leverage Vetted Modules or Services for Application Security Components

## Enforcement

Violations of GitHub Agentic Workflows rules:
- **Critical**: Hard-coded secrets, unrestricted permissions - Block deployment
- **High**: Missing compilation, unsafe tool configuration - Require remediation before merge
- **Medium**: Unclear instructions, missing documentation - Create improvement tickets
- **Low**: Style inconsistencies, optimization opportunities - Optional improvements

## Version History

- **2026-02-11**: Initial skill creation based on latest GitHub Agentic Workflows features and documentation

---
name: github-agentic-workflows
description: GitHub Agentic Workflows (gh-aw) - markdown-based AI automation with 5-layer security, safe outputs, and Continuous AI patterns
license: Apache-2.0
---

# 🤖 GitHub Agentic Workflows Skill

## Purpose

This skill provides comprehensive guidance on GitHub Agentic Workflows (gh-aw), a Go-based GitHub CLI extension that enables writing agentic workflows in natural language using Markdown files and running them as GitHub Actions workflows. Developed by GitHub Next and Microsoft Research, gh-aw delivers repository automation with strong guardrails, safe outputs, and sandboxed execution.

gh-aw augments existing deterministic CI/CD with **Continuous AI** capabilities — systematic, automated application of AI to software collaboration tasks like triaging issues, maintaining documentation, improving code quality, and automating reviews.

## When to Use

Apply this skill when:
- Writing AI-powered repository automation as Markdown workflows
- Implementing Continuous AI patterns (issue triage, documentation sync, code review, quality improvement)
- Leveraging safe-outputs for write operations without granting direct write permissions
- Using multiple AI engines (Copilot, Claude, Codex) for event-triggered and scheduled jobs
- Building orchestrator-worker patterns for complex multi-agent coordination
- Automating tasks that traditionally require human judgment

## 5-Layer Security Architecture

gh-aw enforces defense-in-depth with five security layers:

1. **Read-only tokens** — Agent receives only read-scoped GitHub token
2. **Zero secrets in agent** — Write tokens/API keys exist only in separate isolated jobs
3. **Containerized with network firewall** — Agent Workflow Firewall (AWF) routes all outbound traffic through Squid proxy with domain allowlist
4. **Safe outputs with guardrails** — Agent produces structured artifacts; a separate gated job applies only permitted actions
5. **Agentic threat detection** — AI-powered scan of proposed changes before any write; blocks prompt injection, leaked credentials, malicious code

## Rules

### Workflow Structure

**MUST:**
- Create workflow files as Markdown (`.md`) in `.github/workflows/`
- Include YAML frontmatter between `---` markers at the top
- Write natural language instructions below the frontmatter
- Compile to `.lock.yml` files using `gh aw compile`
- Commit both `.md` (source) and `.lock.yml` (compiled) files
- Use clear, imperative task descriptions in natural language
- Separate configuration (frontmatter) from instructions (body)

**MUST NOT:**
- Manually edit `.lock.yml` files (regenerate via compile)
- Push `.md` changes without recompiling
- Write complex YAML conditionals in workflow files
- Skip compilation step before deployment

### Frontmatter Configuration

**MUST:**
- Define `on:` trigger(s) with appropriate event types and activity filters
- Set `permissions:` with specific resource scopes (e.g., `issues: read`, `contents: read`)
- Configure `tools:` with specific toolsets (e.g., `github:` with `toolsets: [issues, labels]`)
- Include `safe-outputs:` for all write operations, using a hard limit where the output type supports it (e.g., `max`, `max-size`) or an allowlist where it does not (e.g., `allowed`)
- Set `timeout-minutes:` to prevent runaway workflows

**MUST NOT:**
- Use `permissions: write-all` without explicit security review
- Omit `safe-outputs:` for workflows that create/modify resources
- Hard-code secrets in frontmatter
- Grant unrestricted tool access

### Natural Language Instructions

**MUST:**
- Write as if explaining a task to a colleague
- Use imperative mood ("Analyze this issue", "Create a summary")
- Include context, success criteria, and constraints
- Define expected outputs (comments, PRs, issues)
- Break complex tasks into clear numbered phases
- Specify what NOT to do when relevant
- Include examples of desired output format

**MUST NOT:**
- Write vague instructions ("Do something helpful")
- Assume the AI knows implicit repository context
- Mix code/YAML in instruction text

### Engines (AI Models)

**MUST:**
- Use GitHub Copilot as default (no explicit `engine:` needed)
- For Claude: set `engine: claude` and configure `ANTHROPIC_API_KEY` secret
- For Codex: set `engine: codex` and configure `OPENAI_API_KEY` secret
- Test with chosen engine before production deployment

**MUST NOT:**
- Mix multiple engines in same workflow
- Assume identical capabilities across engines

### Triggers

**MUST:**
- Choose appropriate trigger(s):
  - `issues:` with `types: [opened, reopened]` for issue automation
  - `pull_request:` for PR-related automation
  - `schedule:` with human-friendly syntax (`daily`, `weekly on monday`) or cron
  - `workflow_dispatch:` for manual execution
  - `slash_command:` with `command:` for comment-triggered actions (e.g., `/plan`, `/analyze`)
- Consider rate limits and costs for scheduled workflows
- Test with `workflow_dispatch` before enabling automatic triggers

**MUST NOT:**
- Use overly frequent schedules that waste resources
- Trigger on every event type without necessity

### Tools and MCP Integration

**MUST:**
- Configure tools in frontmatter with specific toolsets:
  ```yaml
  tools:
    github:
      toolsets: [issues, labels, pull-requests]
  ```
- Use `safe-inputs:` for custom lightweight inline functions
- Use `edit:` tool for file modifications, `bash:` for shell commands
- Use `web-search:` or `web-fetch:` for external information with network restrictions
- Set `network:` allowlists when external access is needed
- Use `min-integrity:` for public repos to control event visibility

**MUST NOT:**
- Grant unrestricted tool access without review
- Bypass tool allowlists or network access controls

### Compilation and Setup

**MUST:**
- Install: `gh extension install github/gh-aw`
- Initialize: `gh aw init` for new repositories
- Compile: `gh aw compile` (generates `.lock.yml`)
- Watch mode: `gh aw compile --watch` for development
- Test: `gh aw run <workflow-name>` for manual testing
- Logs: `gh aw logs <workflow-name>` for debugging
- Add community workflows: `gh aw add-wizard <url>`
- Use fine-grained PATs with minimal scopes

**MUST NOT:**
- Use classic PATs instead of fine-grained tokens
- Skip `gh aw init` for new repositories
- Commit secrets to version control

## Examples

### Example 1: Issue Triage (Real-World Pattern from Agent Factory)

```markdown
---
timeout-minutes: 5
on:
  issues:
    types: [opened, reopened]
permissions:
  issues: read
tools:
  github:
    toolsets: [issues, labels]
safe-outputs:
  add-labels:
    allowed: [bug, feature, enhancement, documentation, question, "help wanted", "good first issue"]
  create-comment:
    max: 1
---

# Issue Triage Agent

Analyze the triggering issue (${{ github.event.issue.number }}) title and body,
then add one of the allowed labels: `bug`, `feature`, `enhancement`,
`documentation`, `question`, `help wanted`, or `good first issue`.

Skip the issue if it:
- Already has any of these labels
- Has been assigned to any user (especially non-bot users)

Do research on the issue in the context of the codebase and, after adding
the label, mention the issue author in a comment explaining why the label
was added and give a brief summary of how the issue may be addressed.
```

### Example 2: Daily Status Report

```markdown
---
on:
  schedule: daily
permissions:
  contents: read
  issues: read
  pull-requests: read
safe-outputs:
  create-issue:
    max: 1
    title-prefix: "[team-status] "
    labels: [report, daily-status]
    close-older-issues: true
---

## Daily Issues Report

Create an upbeat daily status report for the team as a GitHub issue.

## What to include

- Recent repository activity (issues, PRs, discussions, releases, code changes)
- Progress tracking, goal reminders and highlights
- Project status and recommendations
- Actionable next steps for maintainers
```

### Example 3: Plan Command (Slash Command)

```markdown
---
on:
  slash_command:
    command: /plan
permissions:
  issues: read
tools:
  github:
    toolsets: [issues]
safe-outputs:
  create-issue:
    max: 10
  create-comment:
    max: 1
---

# Plan Command

Break down the current issue into actionable sub-tasks.
Create child issues for each sub-task and link them.
Post a comment summarizing the plan with links to all created sub-issues.
```

### Example 4: Network-Restricted Security Review

```markdown
---
on: pull_request
timeout-minutes: 10
permissions:
  contents: read
  pull-requests: read
  security-events: read
tools:
  github:
    toolsets: [pull-requests, code-scanning]
network: defaults
safe-outputs:
  create-comment:
    max: 3
  threat-detection:
    enabled: true
    action: block
---

# Security-Focused PR Review

Review pull request for security issues. No external network access allowed.

Focus on:
- Hard-coded secrets or credentials
- Unsafe input handling
- Missing authentication checks
- Injection vulnerabilities
```

### Example 5: Safe Inputs with Custom Tool

```markdown
---
on: issues
permissions:
  issues: read
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
        return Math.min(score, 10);
      }
safe-outputs:
  create-comment:
    max: 1
---

# Priority Calculator

Use the calculate_priority tool to assess issue priority.
Post a comment with the priority score and recommended action timeline.
```

### Example 6: Multi-Engine Configuration

```markdown
---
on: workflow_dispatch
engine: claude
permissions:
  contents: read
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

## Best Practices

### Start Simple, Iterate
- Begin with read-only workflows using `workflow_dispatch`
- Add safe-outputs incrementally; start with `create-comment`
- Use `gh aw compile --watch` for rapid iteration
- Graduate to scheduled triggers after manual testing

### Clear Instructions Win
- Write as if explaining to a human colleague
- Include examples of desired output format
- Define constraints and guardrails explicitly
- Specify what NOT to do when relevant

### Security First
- Use specific permissions (e.g., `issues: read`) not `read-all`
- Use safe-outputs constraints: `title-prefix`, `labels`, `allowed`, `max`
- Use `network: {}` for zero external access, `network: defaults` for GitHub-only
- Enable `threat-detection` for all safe-outputs workflows
- Use `min-integrity:` in public repos for event visibility control

### Agent Factory Patterns (Proven at Scale)
The GitHub Next team operates 100+ workflows. Key learnings:
- **Customized agents beat generic ones** — tailor to your repo's context
- **Incremental improvement beats heroic efforts** — small daily PRs
- **Observability is essential** — track success rates and merge rates
- **Meta-analysis reveals hidden patterns** — use AI to analyze AI behavior
- **Task decomposition enables coordination** — `/plan` command + sub-issues

### Monitor and Improve
- Track workflow success/merge rates
- Review AI output quality regularly
- Refine instructions based on actual behavior
- Use `gh aw logs` and GitHub Actions logs

## Compilation Flow

```
1. Author:   .github/workflows/my-workflow.md
2. Compile:  gh aw compile → generates .lock.yml
3. Commit:   git add *.md *.lock.yml && git commit
4. Push:     git push
5. Secrets:  Configure API keys in repository settings
6. Test:     gh aw run my-workflow
7. Monitor:  gh aw logs my-workflow
```

## Safe Outputs Reference

| Output Type | Key Constraints | Example |
|------------|----------------|---------|
| `create-issue` | `title-prefix`, `labels`, `max`, `close-older-issues` | Status reports |
| `create-comment` | `max` | Triage analysis |
| `add-labels` | `allowed` list | Issue classification |
| `create-pull-request` | `max`, `title-prefix` | Code improvements |
| `create-code-scanning-alert` | `max` | Security scanning |
| `upload-asset` | `branch`, `max-size`, `allowed-exts` | Screenshots |

## Troubleshooting

| Symptom | Solution |
|---------|----------|
| Compilation fails | Check YAML frontmatter syntax; run `gh aw compile --verbose` |
| Workflow doesn't trigger | Verify `.lock.yml` is committed; check trigger config |
| AI output quality issues | Make instructions more specific; add examples; try different engine |
| Permission errors | Review `permissions:` and `safe-outputs:` config; check token scopes |
| Network timeout | Add domain to `network:` allowlist; check AWF firewall logs |

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

- [GitHub Agentic Workflows Official Site](https://github.github.com/gh-aw/)
- [Abridged LLM Documentation](https://github.github.com/gh-aw/llms-small.txt)
- [Full LLM Documentation](https://github.github.com/gh-aw/llms-full.txt)
- [Agent Factory Blog Series](https://github.github.com/gh-aw/_llms-txt/agentic-workflows.txt)
- [GitHub Blog: Automate Repository Tasks](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

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

| Severity | Violation | Action |
|----------|-----------|--------|
| Critical | Hard-coded secrets, `write-all` permissions | Block deployment |
| High | Missing compilation, unsafe tool config | Require remediation |
| Medium | Unclear instructions, missing docs | Create improvement ticket |
| Low | Style inconsistencies | Optional improvement |

## Version History

- **2026-04-02**: Major update with latest gh-aw v0.45+ features, 5-layer security architecture, real-world Agent Factory patterns, safe-outputs reference table
- **2026-02-11**: Initial skill creation

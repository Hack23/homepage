---
name: agentic-workflow-development
description: CLI usage, compilation, testing, debugging, and maintenance practices for GitHub Agentic Workflows
license: Apache-2.0
---

# 🛠️ Agentic Workflow Development Skill

## Purpose

This skill provides comprehensive guidance on the development lifecycle for GitHub Agentic Workflows, including CLI usage, compilation, testing, debugging, version control, and maintenance practices. It focuses on developer productivity, rapid iteration, and reliable deployment of agentic automation.

## When to Use

Apply this skill when:
- Setting up development environment for agentic workflows
- Creating, testing, and debugging workflows
- Implementing CI/CD for workflow deployment
- Troubleshooting workflow execution issues
- Maintaining and upgrading existing workflows
- Collaborating on workflow development with teams

## Rules

### CLI Setup and Usage

**MUST:**
- Install GitHub CLI: `gh --version` to verify
- Install gh-aw extension: `gh extension install github/gh-aw`
- Keep gh-aw updated: `gh extension upgrade gh-aw`
- Initialize repositories: `gh aw init` for new projects
- Use CLI for all workflow operations (not manual file editing of `.lock.yml`)

**MUST NOT:**
- Manually edit `.lock.yml` files
- Use outdated gh-aw versions
- Skip repository initialization
- Bypass CLI for workflow management

### Development Workflow

**MUST:**
- Create workflow `.md` files in `.github/workflows/`
- Use descriptive workflow names (kebab-case)
- Compile after every edit: `gh aw compile`
- Test workflows before committing: `gh aw run <workflow-name>`
- Review compilation output for warnings
- Commit both `.md` and `.lock.yml` files together
- Write meaningful commit messages

**MUST NOT:**
- Edit workflows without compiling
- Commit `.md` without `.lock.yml`
- Skip testing before merge
- Use generic commit messages

### Rapid Iteration with Watch Mode

**MUST:**
- Use `gh aw compile --watch` for active development
- Keep watch mode running in dedicated terminal
- Review compilation errors immediately
- Test changes incrementally
- Save frequently to trigger recompilation

**MUST NOT:**
- Ignore watch mode error messages
- Make multiple changes without testing
- Disable automatic compilation during development

### Testing Strategies

**MUST:**
- Test with `workflow_dispatch` trigger first
- Use `gh aw run <workflow-name>` for manual testing
- Test with real repository data
- Verify safe-outputs work as expected
- Test error conditions and edge cases
- Review GitHub Actions logs after each test run
- Test permission boundaries

**MUST NOT:**
- Test only happy path scenarios
- Skip permission testing
- Test in production without staging
- Ignore test failures

### Debugging Techniques

**MUST:**
- Use `gh aw logs` to review execution logs
- Check GitHub Actions workflow run details
- Review compilation output for syntax errors
- Add debug logging to workflow instructions
- Test workflows in isolation
- Use `gh aw status` to check workflow health
- Reproduce issues locally when possible

**MUST NOT:**
- Debug only by editing production workflows
- Ignore error messages
- Skip log review
- Make blind fixes without understanding root cause

### Version Control Practices

**MUST:**
- Use feature branches for workflow changes
- Write descriptive pull request descriptions
- Include workflow testing results in PRs
- Review workflow changes carefully (both `.md` and `.lock.yml`)
- Tag workflow versions for major changes
- Maintain changelog for workflow evolution
- Document breaking changes

**MUST NOT:**
- Commit directly to main branch
- Merge without review
- Skip documentation updates
- Delete workflow history

### Code Review for Workflows

**MUST:**
- Review natural language instructions for clarity
- Verify security settings (permissions, tools, network)
- Check safe-outputs configuration
- Validate trigger appropriateness
- Confirm secret usage is correct
- Test workflow before approving PR
- Verify compilation produces expected `.lock.yml`

**MUST NOT:**
- Approve without testing
- Skip security review
- Ignore compilation warnings
- Rubber-stamp workflow changes

### Workflow Organization

**MUST:**
- Group related workflows in subdirectories (if supported)
- Use consistent naming conventions
- Document workflow purpose in file header
- Create README for complex workflow systems
- Link related workflows explicitly
- Maintain workflow dependency documentation

**MUST NOT:**
- Create monolithic workflows (split into orchestrator-worker)
- Use unclear or cryptic names
- Leave workflows undocumented
- Create hidden dependencies

### Performance Optimization

**MUST:**
- Profile workflow execution time
- Optimize AI prompts for clarity and brevity
- Batch operations when possible
- Cache results to avoid redundant work
- Use appropriate trigger frequencies
- Monitor resource usage and costs

**MUST NOT:**
- Over-trigger workflows
- Create unnecessarily complex instructions
- Ignore performance warnings
- Skip cost monitoring

### Maintenance and Upgrades

**MUST:**
- Regularly update gh-aw CLI: `gh extension upgrade gh-aw`
- Upgrade workflow dependencies: `gh aw upgrade`
- Review and apply workflow template updates
- Monitor for deprecated features
- Test upgrades in non-production first
- Document upgrade procedures
- Maintain backward compatibility when possible

**MUST NOT:**
- Let workflows become outdated
- Skip testing after upgrades
- Apply breaking changes without notice
- Ignore deprecation warnings

## Examples

### Example 1: Complete Development Workflow

```bash
# 1. Initialize new repository for agentic workflows
cd my-repo
gh aw init

# 2. Create new workflow file
cat > .github/workflows/issue-triage.md << 'EOF'
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

Analyze new issues and provide triage information.
EOF

# 3. Start watch mode for development
gh aw compile --watch &

# 4. Edit workflow, save, watch auto-compiles
# (Make changes to issue-triage.md)

# 5. Test workflow manually
gh aw run issue-triage

# 6. Check logs
gh aw logs issue-triage

# 7. Commit both files
git add .github/workflows/issue-triage.md
git add .github/workflows/issue-triage.lock.yml
git commit -m "Add issue triage workflow"

# 8. Push and create PR
git push origin feature/issue-triage
gh pr create --title "Add issue triage workflow" \
  --body "Implements automated issue triage with AI"
```

### Example 2: Debugging Workflow Issues

```bash
# Check workflow status
gh aw status

# Review recent logs for specific workflow
gh aw logs my-workflow --tail 100

# Check compilation for errors
gh aw compile --verbose

# Test workflow with debug output
gh aw run my-workflow --debug

# Check GitHub Actions workflow runs
gh run list --workflow=my-workflow.lock.yml

# View specific run logs
gh run view <run-id> --log

# Check for common issues
gh aw doctor
```

### Example 3: Testing Workflow Changes

```bash
# Create test branch
git checkout -b test/workflow-improvements

# Make changes to workflow
vim .github/workflows/pr-reviewer.md

# Compile and check for errors
gh aw compile
if [ $? -ne 0 ]; then
  echo "Compilation failed"
  exit 1
fi

# Test workflow (requires PR or issue depending on trigger)
gh aw run pr-reviewer

# Wait and check results
sleep 30
gh aw logs pr-reviewer --tail 50

# If successful, commit
git add .github/workflows/pr-reviewer.md
git add .github/workflows/pr-reviewer.lock.yml
git commit -m "Improve PR reviewer workflow logic"
git push origin test/workflow-improvements
```

### Example 4: Workflow CI/CD Pipeline

```yaml
# .github/workflows/workflow-ci.yml
name: Workflow CI

on:
  pull_request:
    paths:
      - '.github/workflows/*.md'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup GitHub CLI
        run: gh --version
      
      - name: Install gh-aw
        run: gh extension install github/gh-aw
      
      - name: Compile workflows
        run: gh aw compile --check
      
      - name: Validate workflow structure
        run: |
          for workflow in .github/workflows/*.md; do
            echo "Validating $workflow"
            gh aw validate "$workflow"
          done
      
      - name: Check for security issues
        run: gh aw security-check
      
      - name: Verify lock files are up to date
        run: |
          gh aw compile
          if [ -n "$(git status --porcelain .github/workflows/*.lock.yml)" ]; then
            echo "Lock files out of date. Run: gh aw compile"
            exit 1
          fi
```

### Example 5: Workflow with Debug Logging

```markdown
---
on: workflow_dispatch
permissions: read-all
tools:
  github:
safe-outputs:
  create-comment:
    max: 1
---

# Debug Example Workflow

**DEBUG MODE ENABLED**

Log all steps for debugging:

1. List repository details
   - Log: Repository name, owner, default branch
   
2. Check issue count
   - Log: Total open issues, closed issues
   
3. Analyze most recent issue
   - Log: Issue number, title, author
   - Log: Label count, comment count
   
4. Generate report
   - Include all logged data
   - Post as comment on issue #1

Use verbose output for all operations.
```

### Example 6: Workflow Upgrade Process

```bash
# Check current gh-aw version
gh extension list

# Upgrade gh-aw extension
gh extension upgrade gh-aw

# Check for workflow upgrades
gh aw check-updates

# Upgrade workflows to latest patterns
gh aw upgrade --dry-run  # See what would change
gh aw upgrade            # Apply upgrades

# Recompile all workflows
gh aw compile

# Test critical workflows
gh aw run critical-workflow-1
gh aw run critical-workflow-2

# If tests pass, commit
git add .github/workflows/
git commit -m "Upgrade workflows to gh-aw v2.0"
```

### Example 7: Local Development Setup Script

```bash
#!/bin/bash
# setup-aw-dev.sh - Set up local environment for agentic workflows

set -e

echo "Setting up Agentic Workflows development environment..."

# Install/update GitHub CLI
if ! command -v gh &> /dev/null; then
  echo "Installing GitHub CLI..."
  # Installation varies by OS
  brew install gh  # macOS
fi

# Install gh-aw extension
echo "Installing gh-aw extension..."
gh extension install github/gh-aw || gh extension upgrade gh-aw

# Initialize repository
echo "Initializing repository..."
gh aw init

# Set up git hooks for workflow compilation
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
# Pre-commit hook: Compile workflows
if git diff --cached --name-only | grep -q ".github/workflows/.*\.md"; then
  echo "Compiling workflows..."
  gh aw compile || exit 1
  
  # Stage updated lock files
  git add .github/workflows/*.lock.yml
fi
EOF

chmod +x .git/hooks/pre-commit

echo "Setup complete! Development environment ready."
echo "- gh-aw version: $(gh aw version)"
echo "- Pre-commit hook installed"
```

### Example 8: Workflow Testing Framework

```bash
#!/bin/bash
# test-workflows.sh - Test all workflows

set -e

echo "Testing all agentic workflows..."

WORKFLOWS=$(ls .github/workflows/*.md | xargs -n1 basename -s .md)

for workflow in $WORKFLOWS; do
  echo "Testing: $workflow"
  
  # Compile
  gh aw compile "$workflow" || {
    echo "❌ Compilation failed: $workflow"
    exit 1
  }
  
  # Validate structure
  gh aw validate "$workflow" || {
    echo "❌ Validation failed: $workflow"
    exit 1
  }
  
  # Security check
  gh aw security-check "$workflow" || {
    echo "❌ Security check failed: $workflow"
    exit 1
  }
  
  echo "✅ $workflow passed all checks"
done

echo "All workflows tested successfully!"
```

## CLI Command Reference

### Essential Commands

```bash
# Initialize repository
gh aw init

# Compile workflows
gh aw compile                    # Compile all
gh aw compile <workflow>         # Compile specific
gh aw compile --watch            # Watch mode
gh aw compile --check            # Check only (CI)

# Run workflows
gh aw run <workflow>             # Run manually
gh aw run <workflow> --debug     # Run with debug

# View logs
gh aw logs                       # All recent logs
gh aw logs <workflow>            # Specific workflow
gh aw logs <workflow> --tail 100 # Last 100 lines

# Status and health
gh aw status                     # All workflows
gh aw status <workflow>          # Specific workflow
gh aw doctor                     # Diagnose issues

# Workflow management
gh aw add <url>                  # Add workflow from URL
gh aw add-wizard <url>           # Add with guided setup
gh aw upgrade                    # Upgrade workflows
gh aw check-updates              # Check for updates

# Validation and security
gh aw validate <workflow>        # Validate structure
gh aw security-check             # Security audit

# Version control
gh aw version                    # Show version
gh extension upgrade gh-aw       # Upgrade CLI
```

## Best Practices Checklist

### Development
- [ ] Repository initialized with `gh aw init`
- [ ] Watch mode used for active development
- [ ] Workflows tested before committing
- [ ] Both `.md` and `.lock.yml` committed together
- [ ] Meaningful commit messages written

### Testing
- [ ] Manual testing with `gh aw run`
- [ ] Logs reviewed with `gh aw logs`
- [ ] Edge cases tested
- [ ] Permission boundaries validated
- [ ] Error handling verified

### Security
- [ ] Security check passed: `gh aw security-check`
- [ ] Minimal permissions configured
- [ ] Safe-outputs used for write operations
- [ ] Secrets properly configured
- [ ] Network access restricted

### Collaboration
- [ ] Feature branch workflow used
- [ ] Pull requests reviewed by team
- [ ] Documentation updated
- [ ] Breaking changes documented
- [ ] Changelog maintained

### Maintenance
- [ ] gh-aw CLI kept up to date
- [ ] Workflows upgraded regularly
- [ ] Performance monitored
- [ ] Costs tracked
- [ ] Deprecated features replaced

## Troubleshooting Guide

### Compilation Errors
**Symptom**: `gh aw compile` fails
**Solutions**:
- Check YAML frontmatter syntax
- Verify all required fields present
- Review error message carefully
- Check for unclosed quotes or brackets
- Validate indentation

### Workflow Won't Trigger
**Symptom**: Workflow doesn't run on expected events
**Solutions**:
- Verify `.lock.yml` is committed
- Check trigger configuration in frontmatter
- Review GitHub Actions logs
- Ensure workflow name is correct
- Check repository workflow permissions

### Permission Denied Errors
**Symptom**: Workflow fails with permission errors
**Solutions**:
- Review `permissions:` in frontmatter
- Check if safe-outputs needed
- Verify secrets configured correctly
- Ensure token has required scopes
- Check repository Actions permissions

### Slow or Hanging Workflows
**Symptom**: Workflows take too long or never complete
**Solutions**:
- Add explicit timeouts
- Simplify workflow instructions
- Check for infinite loops
- Review tool usage (disable unused tools)
- Monitor GitHub Actions queue

### Unexpected AI Behavior
**Symptom**: AI doesn't follow instructions
**Solutions**:
- Make instructions more specific
- Add examples to workflow
- Break complex tasks into steps
- Use imperative language
- Consider different engine

## Related ISMS Policies

This skill aligns with:

- **[Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md)** - Secure development lifecycle
- **[Change Management Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Change_Management_Policy.md)** - Workflow change management
- **[Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)** - Overall security framework

## Related Skills

- **[GitHub Agentic Workflows](../github-agentic-workflows/SKILL.md)** - Core workflow fundamentals
- **[Agentic Workflow Security](../agentic-workflow-security/SKILL.md)** - Security best practices
- **[Agentic Workflow Orchestration](../agentic-workflow-orchestration/SKILL.md)** - Multi-workflow coordination
- **[GitHub Actions CI/CD](../../deployment/github-actions-cicd/SKILL.md)** - CI/CD integration
- **[Testing Strategy](../../development/testing-strategy/SKILL.md)** - Testing approaches

## Related Documentation

- [GitHub Agentic Workflows CLI Documentation](https://github.github.com/gh-aw/setup/cli/)
- [GitHub CLI Documentation](https://cli.github.com/manual/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## Compliance Mapping

### ISO 27001:2022
- **A.8.25** Secure development life cycle
- **A.8.32** Change management
- **A.5.37** Documented operating procedures

### NIST Cybersecurity Framework 2.0
- **PR.IP-02**: System development lifecycle
- **PR.MA-01**: Maintenance is performed
- **DE.CM-08**: Vulnerability scans are performed

### CIS Controls v8.1
- **Control 16**: Application Software Security
  - 16.1 Secure Application Development Process
  - 16.3 Maintain Separate Development Environments

## Enforcement

Development practice violations:
- **Critical**: Committing without compilation, exposed secrets - Block deployment
- **High**: Missing tests, no code review - Require remediation
- **Medium**: Incomplete documentation, style issues - Create improvement tickets
- **Low**: Minor optimization opportunities - Optional improvements

## Version History

- **2026-02-11**: Initial skill creation based on latest gh-aw CLI and development practices

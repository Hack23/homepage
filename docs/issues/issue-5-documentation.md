# 📚 Document Copilot environment permissions and best practices

## 🎯 Objective

Create comprehensive documentation explaining the copilot-setup-steps.yml configuration, permissions model, and best practices for customizing the GitHub Copilot coding agent environment for this static HTML/CSS repository.

## 📋 Background

The `.github/workflows/copilot-setup-steps.yml` file is a specialized workflow that customizes GitHub Copilot's development environment. While the file itself is simple, understanding **why** it's configured a certain way, what permissions are needed, and how to extend it is valuable for:

- **Team onboarding**: New developers understanding Copilot's environment
- **Maintenance**: Knowing what can/cannot be changed safely
- **Future enhancements**: Adding new tools without breaking permissions
- **Knowledge sharing**: Documenting decisions and rationale

Currently, there's no documentation explaining:
- Why `contents: read` permission is sufficient
- What other permissions are available and when they're needed
- How to add new tools to the environment
- What customizations make sense for a static HTML/CSS site
- How this integrates with the main deployment workflow

## ✅ Acceptance Criteria

- [ ] Create `docs/COPILOT_ENVIRONMENT.md` documentation file
- [ ] Explain permissions model (what Copilot gets vs what setup steps get)
- [ ] Document current setup steps and their purpose
- [ ] Provide examples of safe enhancements
- [ ] List customization options from GitHub documentation
- [ ] Explain integration with existing CI/CD (main.yml, pullrequest.yml)
- [ ] Include troubleshooting guide
- [ ] Add link to GitHub's official documentation

## 🛠️ Implementation Guidance

### Files to Create
- `docs/COPILOT_ENVIRONMENT.md` - Main documentation file

### Files to Modify
- `README.md` - Add link to Copilot environment docs (optional)

### Documentation Structure

```markdown
# GitHub Copilot Environment Customization

## Overview
[Explain what copilot-setup-steps.yml does]

## Permissions Model
[Explain the two-token system]

## Current Configuration
[Document existing setup]

## Available Customizations
[List GitHub-supported options]

## Tools Installed
[Document what's available to Copilot]

## Adding New Tools
[Step-by-step guide]

## Troubleshooting
[Common issues and solutions]

## Best Practices
[Recommendations for this repository]

## References
[Links to official docs]
```

### Key Documentation Points

#### 1. Permissions Model (Critical to Understand)
```yaml
permissions:
  contents: read  # What copilot-setup-steps job gets
```

- **Setup steps token**: Minimal permissions (`contents: read`)
- **Copilot's token**: Separate token with permissions to commit, push, manage PRs
- **Why separate**: Security - setup steps don't need write access

#### 2. What Can Be Customized
According to GitHub documentation:
- `steps` - Any commands to run before Copilot starts
- `permissions` - Minimal permissions for setup steps only
- `runs-on` - Runner size (can upgrade to larger runners)
- `services` - Docker services (databases, etc.)
- `snapshot` - Whether to snapshot the environment
- `timeout-minutes` - Maximum 59 minutes

#### 3. What CANNOT Be Changed
- Job name must be `copilot-setup-steps`
- Must be in `.github/workflows/copilot-setup-steps.yml`
- Must be on default branch (master) to activate
- `fetch-depth` for checkout is overridden by Copilot

#### 4. Static Site Specific Best Practices
For this repository (static HTML/CSS):
- ✅ Install validators (HTML, CSS)
- ✅ Install link checkers
- ✅ Install accessibility testers
- ❌ Don't install build tools (no build needed)
- ❌ Don't install databases (static site)
- ❌ Don't install runtime environments (no server-side code)

## 🔗 Related Resources

- [GitHub Official Documentation](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment)
- [GitHub Actions Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- Current workflow: `.github/workflows/copilot-setup-steps.yml`
- Related issues: #1 (HTML validation), #2 (CSS linting), #3 (link checker), #4 (accessibility)

## 📊 Metadata

**Documentation Scope:**
- Copilot environment customization
- Permissions model explanation
- Tool installation guide
- Best practices for static sites
- Troubleshooting guide

**Target Audience:**
- Developers using GitHub Copilot on this repository
- DevOps team maintaining CI/CD
- New team members learning the codebase

**Priority:** Medium  
**Effort:** Small (1-2 hours)  
**Impact:** Improves team knowledge, reduces confusion

**Suggested Labels:** `documentation`, `priority:medium`, `size:small`, `copilot-enhancement`, `knowledge-sharing`

## 💡 Why This Matters

### Knowledge Preservation
- Documents **why** configuration choices were made
- Explains permissions model clearly
- Provides guidance for future enhancements

### Onboarding
- New developers understand Copilot's environment
- Reduces questions and trial-and-error
- Establishes best practices

### Maintenance
- Clear reference for what can/cannot be changed
- Troubleshooting guide saves debugging time
- Integration points with main CI/CD documented

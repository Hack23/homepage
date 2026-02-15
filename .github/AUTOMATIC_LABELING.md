# Automatic Labeling System

## Overview

This repository uses an automatic labeling system to apply labels to pull requests based on the files changed, PR title, and PR body content. This helps organize and categorize PRs efficiently.

## Components

### 1. Labeler Configuration (`.github/labeler.yml`)

Defines rules for automatically applying labels based on:
- **File paths**: Labels are applied when specific files or patterns are changed
- **PR title**: Labels are applied based on conventional commit prefixes (e.g., `feat:`, `fix:`, `docs:`)
- **PR body**: Labels are applied based on checkboxes in PR descriptions
- **Change size**: Automatic size labels based on number of files changed

### 2. Setup Labels Workflow (`.github/workflows/setup-labels.yml`)

A **manual workflow** that creates and updates all repository labels with:
- Consistent colors
- Clear descriptions
- Option to recreate all labels from scratch

**To run this workflow:**
1. Go to **Actions** → **Setup Repository Labels**
2. Click **Run workflow**
3. Choose whether to recreate all labels (optional)
4. Wait for completion

### 3. Labeler Workflow (`.github/workflows/labeler.yml`)

An **automatic workflow** that runs on every pull request to apply labels based on the configuration in `labeler.yml`.

**Triggers:**
- When a PR is opened
- When a PR is synchronized (new commits)
- When a PR is reopened
- When a PR is edited

## Label Categories

### 🚀 Features and Enhancements
- `feature` - New feature or request
- `enhancement` - Enhancement to existing functionality

### 🐛 Bug Fixes
- `bug` - Something isn't working

### 🎨 UI/UX
- `ui` - User interface improvements
- `design` - Design and styling updates

### 🌐 Internationalization
- `i18n` - Internationalization and localization (automatically applied when translation files are changed)

### 🏗️ Infrastructure & DevOps
- `infrastructure` - CI/CD and infrastructure
- `deployment` - Deployment-related changes
- `performance` - Performance improvements
- `config` - Configuration changes

### 🔄 Code Quality
- `refactor` - Code refactoring
- `quality-checks` - Quality checks and validation

### 🔒 Security & Compliance
- `security` - Security improvements
- `compliance` - Compliance and ISMS-related
- `accessibility` - Accessibility improvements

### 📝 Documentation
- `documentation` - Documentation updates

### 📦 Dependencies
- `dependencies` - Dependency updates

### 🤖 GitHub Copilot & AI
- `copilot` - GitHub Copilot configuration
- `agents` - GitHub Copilot agents
- `skills` - GitHub Copilot skills

### 📄 Content Types
- `content-pages` - Main website pages
- `content-blog` - Blog content
- `content-projects` - Project showcase pages
- `content-isms` - ISMS policy pages
- `content-services` - Services and industries

### 🖼️ Assets
- `assets` - Images, icons, and media files

### 🎯 SEO & Analytics
- `seo` - SEO and sitemap changes

### 🔍 Specific Areas
- `area-homepage` - Homepage changes
- `area-cia` - Citizen Intelligence Agency
- `area-blacktrigram` - Black Trigram game
- `area-compliance` - Compliance Manager

### 📊 Size Labels
- `size-xs` - Extra small change (1-10 files)
- `size-s` - Small change (11-30 files)
- `size-m` - Medium change (31-100 files)
- `size-l` - Large change (101-500 files)
- `size-xl` - Extra large change (500+ files)

### Priority Labels
- `priority-high` - High priority
- `priority-medium` - Medium priority
- `priority-low` - Low priority

### Workflow Labels
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `wontfix` - This will not be worked on
- `duplicate` - This issue or pull request already exists
- `invalid` - This doesn't seem right
- `question` - Further information is requested

## Usage

### For PR Authors

#### Automatic Labeling
Labels are automatically applied based on the files you change. For example:
- Changing `*.html` files → `content-pages` label
- Changing files with `_sv.html`, `_de.html`, etc. → `i18n` label
- Changing `.github/workflows/*` → `infrastructure` label
- Changing `SECURITY.md` → `security` label

#### Manual Labeling via PR Title
Use conventional commit prefixes in your PR title:
- `feat:` or `feature:` → `feature` label
- `fix:` or `bug:` → `bug` label
- `docs:` or `doc:` → `documentation` label
- `perf:` or `optimize:` → `performance` label
- `refactor:` → `refactor` label
- `security:` → `security` label

#### Manual Labeling via PR Body
Add checkboxes to your PR description:
- `- [x] 🚀 New Feature/Enhancement` → `feature` label
- `- [x] 🐛 Bug Fix` → `bug` label
- `- [x] 🎨 UI/UX Improvements` → `ui` label
- `- [x] 🏗️ Infrastructure & DevOps` → `infrastructure` label
- `- [x] 🔒 Security & Compliance` → `security` label
- `- [x] 📝 Documentation` → `documentation` label
- `- [x] 📦 Dependencies Update` → `dependencies` label

### For Repository Maintainers

#### Initial Setup
1. Run the **Setup Repository Labels** workflow to create all labels
2. The **Labeler** workflow will automatically start working on new PRs

#### Updating Label Configuration
1. Edit `.github/labeler.yml` to add or modify labeling rules
2. Commit and push changes
3. New rules will apply to subsequent PRs

#### Updating Label Definitions
1. Edit `.github/workflows/setup-labels.yml` to modify label colors or descriptions
2. Commit and push changes
3. Run the **Setup Repository Labels** workflow to apply updates

## Examples

### Example 1: Translating a page to Swedish
**Files changed:**
- `services_sv.html`

**Labels automatically applied:**
- `i18n` (internationalization)
- `content-services` (services content)
- `size-xs` (1 file changed)

### Example 2: Adding a new blog post in all languages
**Files changed:**
- `blog-new-post.html`
- `blog-new-post_sv.html`
- `blog-new-post_de.html`
- `blog-new-post_es.html`
- ... (13+ language variants)

**Labels automatically applied:**
- `content-blog` (blog content)
- `i18n` (internationalization)
- `size-s` or `size-m` (depending on file count)

### Example 3: Updating CI/CD pipeline
**Files changed:**
- `.github/workflows/main.yml`

**PR title:**
- `ci: Optimize deployment to S3`

**Labels automatically applied:**
- `infrastructure` (workflow file changed)
- `deployment` (main.yml changed)
- `size-xs` (1 file changed)

### Example 4: Security fix
**Files changed:**
- `SECURITY.md`
- `SECURITY_ARCHITECTURE.md`
- `.github/workflows/scorecards.yml`

**PR title:**
- `security: Update security documentation and workflow`

**Labels automatically applied:**
- `security` (security files changed + title prefix)
- `documentation` (markdown files changed)
- `infrastructure` (workflow changed)
- `size-xs` (3 files changed)

## Troubleshooting

### Labels not being applied?
1. Check that the **Setup Repository Labels** workflow has been run at least once
2. Verify that the `.github/labeler.yml` file exists in the default branch
3. Check the **Labeler** workflow logs in the Actions tab
4. Ensure the PR is not from a fork (labeler only works on same-repo PRs for security)

### Need to add a new label?
1. Add the label definition to `.github/workflows/setup-labels.yml`
2. Add the labeling rule to `.github/labeler.yml`
3. Run the **Setup Repository Labels** workflow
4. New PRs will use the updated configuration

### Labels applied incorrectly?
1. Review the rules in `.github/labeler.yml`
2. Adjust file patterns or conditions as needed
3. Manually remove incorrect labels from the PR
4. Update the configuration for future PRs

## Best Practices

1. **Use conventional commit prefixes** in PR titles for consistent labeling
2. **Include checkboxes** in PR descriptions to trigger specific labels
3. **Run Setup Labels workflow** after adding new label types
4. **Review automatically applied labels** and adjust manually if needed
5. **Keep labeler.yml updated** as the repository structure evolves
6. **Document new label categories** when adding significant new labels

## Security Considerations

The labeler workflow uses `pull_request_target` trigger which:
- Runs in the context of the base repository (not the fork)
- Has write access to apply labels
- Is hardened with step-security/harden-runner for audit logging
- Only has permissions for contents:read, pull-requests:write, issues:write

This ensures safe operation even when processing PRs from untrusted forks.

## Maintenance

### Regular Tasks
- **Quarterly**: Review label usage and consolidate unused labels
- **When needed**: Update `.github/labeler.yml` for new file patterns
- **When needed**: Update `.github/workflows/setup-labels.yml` for new label types

### Monitoring
- Check the **Actions** tab for workflow failures
- Review PRs to ensure labels are applied correctly
- Gather feedback from contributors about labeling accuracy

## References

- [GitHub Actions Labeler](https://github.com/actions/labeler)
- [Hack23/blacktrigram labeling examples](https://github.com/Hack23/blacktrigram/.github/)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

**Last Updated**: 2026-02-15  
**Maintained By**: Hack23 DevOps Team

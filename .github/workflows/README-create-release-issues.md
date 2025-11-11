# GitHub Actions Workflow: Create Top 5 Release Issues

## Overview

This workflow automatically creates the top 5 priority issues for the next release of the Hack23 homepage. It includes duplicate detection to prevent creating issues that already exist.

## Issues Created

1. **🔒 Security Headers** - Fix CSP, SRI, and security headers (High Priority)
2. **⚡ Lighthouse Performance** - Optimize page load times and meet budget thresholds
3. **🔗 Broken Links** - Fix external documentation references and 404 errors
4. **🎯 SEO Enhancement** - Improve meta tags, structured data, and social sharing
5. **✅ ISMS Validation** - Automate ISMS reference checking in CI/CD

## How to Use

### Method 1: GitHub Web Interface

1. Go to the **Actions** tab in the repository
2. Select "Create Top 5 Release Issues" from the workflow list
3. Click **Run workflow** button
4. Confirm by entering "yes" in the input field
5. Click **Run workflow** to start

### Method 2: GitHub CLI

```bash
# Trigger the workflow manually
gh workflow run create-release-issues.yml
```

### Method 3: Automatic on Merge

This workflow can be configured to run automatically when this PR is merged by adding:

```yaml
on:
  push:
    branches:
      - master
    paths:
      - 'RELEASE_ISSUES.md'
```

## Features

### ✅ Duplicate Detection

Before creating each issue, the workflow checks if a similar issue already exists using title search. If found, it skips creation and reports the existing issue number.

### 📊 Summary Report

After execution, the workflow generates a summary report showing:
- Which issues were created
- Priority assessment
- Total estimated effort
- Links to created issues

### 🏷️ Automatic Labeling

Issues are automatically labeled:
- **Issue #1:** `security`, `enhancement`
- **Issue #2:** `performance`, `enhancement`
- **Issue #3:** `bug`, `documentation`
- **Issue #4:** `enhancement`, `seo`
- **Issue #5:** `automation`, `documentation`

## Workflow Structure

```yaml
name: Create Top 5 Release Issues
on:
  workflow_dispatch:  # Manual trigger only
    inputs:
      confirm:
        description: 'Confirm issue creation (yes/no)'
        required: true
        default: 'yes'

permissions:
  issues: write    # Required to create issues
  contents: read   # Required to checkout code

jobs:
  create-issues:
    runs-on: ubuntu-latest
    steps:
      - Check for duplicate issues
      - Create Issue 1 (Security Headers)
      - Create Issue 2 (Lighthouse Performance)
      - Create Issue 3 (Broken Links)
      - Create Issue 4 (SEO Enhancement)
      - Create Issue 5 (ISMS Validation)
      - Generate summary report
```

## Troubleshooting

### Issue Already Exists

**Symptom:** Workflow skips creating an issue with message "⚠️ Issue already exists"

**Solution:** This is expected behavior. The duplicate detection is working correctly. You can:
- Close the existing issue if it's outdated
- Use the existing issue if it's still valid
- Modify the workflow search query if needed

### Permission Denied

**Symptom:** Workflow fails with "403 Forbidden" or "Resource not accessible"

**Solution:** Ensure the workflow has proper permissions:
```yaml
permissions:
  issues: write
  contents: read
```

### Rate Limiting

**Symptom:** Workflow fails with "429 Too Many Requests"

**Solution:** The workflow includes `sleep 2` between issue creations to avoid rate limits. If still occurring:
- Wait 60 minutes before re-running
- Reduce the number of issues created at once

## Customization

### Modify Issue Content

Edit the workflow file `.github/workflows/create-release-issues.yml` and update the `--body` content for each issue.

### Change Labels

Modify the `--label` flag in each issue creation step:
```bash
--label "security,enhancement,priority:high"
```

### Add Assignees

Add assignee to issues:
```bash
gh issue create \
  --title "..." \
  --body "..." \
  --label "..." \
  --assignee "username"
```

### Modify Duplicate Detection

Update the search query in the duplicate check:
```bash
gh issue list --search "exact title here" --json number
```

## Best Practices

### When to Run

✅ **Run when:**
- Planning a new release
- After major milestone completion
- Quarterly for maintenance releases
- After security audit completion

❌ **Don't run when:**
- Previous issues are still open and active
- During active sprint (may disrupt planning)
- Without stakeholder review

### After Running

1. **Review created issues** - Ensure they align with current priorities
2. **Assign to team members** - Distribute work appropriately
3. **Set milestones** - Link issues to release milestone
4. **Update project board** - Add to GitHub Projects if used
5. **Communicate** - Notify team of new release tasks

## Issue Template

Each issue follows this structure:

```markdown
## 🎯 Objective
[Clear, one-sentence goal]

## 📋 Background
[Context and why this is needed]

## ✅ Acceptance Criteria
- [ ] Specific criterion 1
- [ ] Specific criterion 2
- [ ] Tests added/updated
- [ ] Documentation updated

## 🛠️ Implementation Guidance
### Files to Modify
- `file1.ext` - What changes
- `file2.ext` - What changes

### Step-by-Step
1. [Detailed step]
2. [Detailed step]

### Testing
[How to verify]

## 📊 Metadata
**Priority:** [High/Medium/Low]
**Effort:** [Small/Medium/Large]
**Impact:** [Description]
```

## Related Documentation

- [RELEASE_ISSUES.md](../../RELEASE_ISSUES.md) - Detailed issue descriptions
- [README.md](../../README.md) - Project overview
- [CLASSIFICATION.md](../../CLASSIFICATION.md) - Security classification
- [SECURITY.md](../../SECURITY.md) - Security policy

## Support

For questions or issues with this workflow:

1. **Check workflow logs** in the Actions tab
2. **Review this README** for troubleshooting steps
3. **Create an issue** with the `workflow` label
4. **Contact maintainers** via GitHub discussions

---

**Workflow Version:** 1.0  
**Last Updated:** 2025-11-11  
**Maintainer:** Hack23 Team

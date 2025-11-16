# How to Create the 5 Priority Issues

This repository has **5 fully-specified priority issues** ready to be created in GitHub.

## Quick Start (Easiest Method)

**Just run the convenience script:**

```bash
./CREATE_ISSUES_NOW.sh
```

This will automatically check for GitHub CLI authentication and use the Python script to create all 5 issues.

## What Issues Will Be Created?

1. **Add Subresource Integrity (SRI) to External Font Resources** `[security, enhancement]`
   - High priority security fix
   - Addresses ZAP scan findings

2. **Implement Content Security Policy (CSP) Meta Tags** `[security, enhancement]`
   - Critical priority security enhancement
   - Protects against XSS and clickjacking

3. **Enhance Accessibility with ARIA Labels and Keyboard Navigation** `[accessibility, enhancement, WCAG]`
   - High priority accessibility improvement
   - WCAG 2.1 AA compliance

4. **Complete Korean Translations for Key Pages** `[internationalization, documentation]`
   - Medium priority i18n enhancement
   - Complete parity with Swedish translations

5. **Optimize Lighthouse Performance Budget for Mobile** `[performance, optimization]`
   - Medium priority performance improvement
   - Establish realistic performance monitoring

## Prerequisites

You must have ONE of the following:

### Option A: GitHub CLI (Recommended)
```bash
# Install gh CLI (if not installed)
# macOS:
brew install gh

# Ubuntu/Debian:
sudo apt install gh

# Windows:
winget install --id GitHub.cli

# Authenticate
gh auth login
```

### Option B: GitHub Personal Access Token
```bash
# Set token in environment
export GH_TOKEN="ghp_your_token_here"
```

The token needs `repo` scope to create issues.

## Available Methods

### Method 1: Automated Script (Recommended)
```bash
./CREATE_ISSUES_NOW.sh
```
OR
```bash
python3 create_github_issues.py
```

### Method 2: Manual Creation via GitHub UI

1. Go to https://github.com/Hack23/homepage/issues/new
2. Open `ISSUES_TO_CREATE.md`
3. Copy each issue's content and paste into GitHub's issue form
4. Add the labels shown for each issue
5. Click "Submit new issue"
6. Repeat for all 5 issues

### Method 3: GitHub CLI Manual Commands

Run these commands one at a time:

```bash
# Issue 1
gh issue create --repo Hack23/homepage \
  --title "Add Subresource Integrity (SRI) to External Font Resources" \
  --label "security,enhancement" \
  --body-file <(sed -n '/^## Issue 1/,/^## Issue 2/p' TOP_5_ISSUES.md | head -n -2)

# Issue 2
gh issue create --repo Hack23/homepage \
  --title "Implement Content Security Policy (CSP) Meta Tags" \
  --label "security,enhancement" \
  --body-file <(sed -n '/^## Issue 2/,/^## Issue 3/p' TOP_5_ISSUES.md | head -n -2)

# Issue 3
gh issue create --repo Hack23/homepage \
  --title "Enhance Accessibility with ARIA Labels and Keyboard Navigation" \
  --label "accessibility,enhancement,WCAG" \
  --body-file <(sed -n '/^## Issue 3/,/^## Issue 4/p' TOP_5_ISSUES.md | head -n -2)

# Issue 4
gh issue create --repo Hack23/homepage \
  --title "Complete Korean Translations for Key Pages" \
  --label "internationalization,documentation" \
  --body-file <(sed -n '/^## Issue 4/,/^## Issue 5/p' TOP_5_ISSUES.md | head -n -2)

# Issue 5
gh issue create --repo Hack23/homepage \
  --title "Optimize Lighthouse Performance Budget for Mobile" \
  --label "performance,optimization" \
  --body-file <(sed -n '/^## Issue 5/,/^## Summary/p' TOP_5_ISSUES.md | head -n -2)
```

## Files Reference

- **TOP_5_ISSUES.md** - Original comprehensive issue specifications (447 lines)
- **ISSUES_TO_CREATE.md** - Copy-paste ready format with enhanced formatting (970 lines)
- **create_github_issues.py** - Automated Python script (executable)
- **CREATE_ISSUES_NOW.sh** - Convenience bash wrapper script (executable)
- **README_ISSUES.md** - Original guide for multiple creation methods
- **ISSUE_CREATION_SUMMARY.md** - Detailed status and strategic impact analysis
- **FINAL_REPORT.md** - Concise summary report

## Verification

After creating the issues, verify:
- [ ] All 5 issues are created in https://github.com/Hack23/homepage/issues
- [ ] Each issue has the correct labels
- [ ] Issue descriptions are properly formatted
- [ ] All acceptance criteria are included

## Estimated Total Effort

- **Total:** 15-24 hours across all 5 issues
- **Recommended order:** Issue 2 → 1 → 3 → 5 → 4 (by priority)

## Questions?

If you encounter issues:
1. Check GitHub CLI authentication: `gh auth status`
2. Verify you have `repo` scope permissions
3. Review error messages carefully
4. Fallback to manual creation via GitHub UI

---

**Note:** These issues are based on:
- ZAP security scan report (issue #355)
- Repository analysis (74+ HTML files, accessibility audit)
- Best practices (WCAG 2.1 AA, Core Web Vitals, SRI, CSP)
- Existing open issues (#432, #424, #355)

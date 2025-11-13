# GitHub Issues Creation Guide

This document provides multiple methods to create the 5 documented issues for the Hack23 homepage repository.

## Quick Summary

**5 Issues Fully Specified and Ready:**
1. Add Subresource Integrity (SRI) to External Font Resources
2. Implement Content Security Policy (CSP) Meta Tags  
3. Enhance Accessibility with ARIA Labels and Keyboard Navigation
4. Complete Korean Translations for Key Pages
5. Optimize Lighthouse Performance Budget for Mobile

## Method 1: Automated Script (Recommended)

The `create_github_issues.py` script will create all 5 issues automatically.

**Prerequisites:**
- GitHub CLI (`gh`) installed
- Authenticated with GitHub

**Steps:**
```bash
# Authenticate gh CLI
gh auth login
# OR set token
export GH_TOKEN="your_github_token"

# Run the script
./create_github_issues.py
```

## Method 2: Manual Creation from Specifications

Open `TOP_5_ISSUES.md` and use the detailed specifications to manually create each issue via GitHub web UI at:
https://github.com/Hack23/homepage/issues/new

Each issue section includes:
- Title
- Complete description with markdown
- Acceptance criteria
- Implementation guidance
- Related resources
- Suggested labels

## Method 3: Using gh CLI Manually

```bash
gh auth login  # Authenticate first

# Issue 1
gh issue create --repo Hack23/homepage \
  --title "Add Subresource Integrity (SRI) to External Font Resources" \
  --body-file <(sed -n '/^## Issue 1/,/^## Issue 2/p' TOP_5_ISSUES.md | head -n -1) \
  --label "security,enhancement"

# Repeat for issues 2-5...
```

## Issue Priorities

Based on impact and ZAP scan findings:

1. **Critical**: Issue #2 (CSP Meta Tags)
2. **High**: Issue #1 (SRI), Issue #3 (Accessibility)
3. **Medium**: Issue #4 (Korean Translations), Issue #5 (Performance Budget)

## Related Files

- `TOP_5_ISSUES.md` - Complete issue specifications
- `create_github_issues.py` - Automated creation script
- `ISSUE_CREATION_STATUS.md` - Status and technical details

## Current Status

All 5 issues are:
- ✅ Fully researched and analyzed
- ✅ Documented with complete specifications
- ✅ Ready for creation via multiple methods
- ⏳ Awaiting creation in GitHub issue tracker

The specifications are based on:
- ZAP security scan report (issue #355)
- Repository analysis (74+ HTML files, accessibility audit)
- Best practices (WCAG 2.1 AA, Core Web Vitals, SRI, CSP)
- Existing open issues (#432, #424, #355)

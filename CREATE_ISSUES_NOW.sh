#!/bin/bash
# Simple script to create the 5 priority issues
# Usage: ./CREATE_ISSUES_NOW.sh

set -e

echo "============================================="
echo "Creating 5 Priority Issues for Hack23/homepage"
echo "============================================="
echo ""

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ ERROR: GitHub CLI (gh) is not installed"
    echo ""
    echo "Install gh CLI:"
    echo "  • macOS: brew install gh"
    echo "  • Linux: https://github.com/cli/cli/blob/trunk/docs/install_linux.md"
    echo "  • Windows: winget install --id GitHub.cli"
    echo ""
    exit 1
fi

# Check authentication
if ! gh auth status &> /dev/null; then
    echo "❌ ERROR: Not authenticated with GitHub CLI"
    echo ""
    echo "Please authenticate by running:"
    echo "  gh auth login"
    echo ""
    echo "Or set a token:"
    echo "  export GH_TOKEN=<your_personal_access_token>"
    echo ""
    exit 1
fi

echo "✅ GitHub CLI is installed and authenticated"
echo ""

# Use the Python script if Python is available
if command -v python3 &> /dev/null; then
    echo "Using Python script to create issues..."
    python3 create_github_issues.py
    exit $?
fi

# Fallback: Manual instructions
echo "⚠️  Python 3 not found. Here are manual commands:"
echo ""
echo "Run these commands one by one:"
echo ""

echo "# Issue 1: Add SRI to External Font Resources"
echo "gh issue create --repo Hack23/homepage \\"
echo "  --title 'Add Subresource Integrity (SRI) to External Font Resources' \\"
echo "  --label 'security,enhancement' \\"
echo "  --body-file <(sed -n '/^## Issue 1/,/^## Issue 2/p' TOP_5_ISSUES.md | head -n -2)"
echo ""

echo "# Issue 2: Implement CSP Meta Tags"
echo "gh issue create --repo Hack23/homepage \\"
echo "  --title 'Implement Content Security Policy (CSP) Meta Tags' \\"
echo "  --label 'security,enhancement' \\"
echo "  --body-file <(sed -n '/^## Issue 2/,/^## Issue 3/p' TOP_5_ISSUES.md | head -n -2)"
echo ""

echo "# Issue 3: Enhance Accessibility"
echo "gh issue create --repo Hack23/homepage \\"
echo "  --title 'Enhance Accessibility with ARIA Labels and Keyboard Navigation' \\"
echo "  --label 'accessibility,enhancement,WCAG' \\"
echo "  --body-file <(sed -n '/^## Issue 3/,/^## Issue 4/p' TOP_5_ISSUES.md | head -n -2)"
echo ""

echo "# Issue 4: Complete Korean Translations"
echo "gh issue create --repo Hack23/homepage \\"
echo "  --title 'Complete Korean Translations for Key Pages' \\"
echo "  --label 'internationalization,documentation' \\"
echo "  --body-file <(sed -n '/^## Issue 4/,/^## Issue 5/p' TOP_5_ISSUES.md | head -n -2)"
echo ""

echo "# Issue 5: Optimize Lighthouse Performance Budget"
echo "gh issue create --repo Hack23/homepage \\"
echo "  --title 'Optimize Lighthouse Performance Budget for Mobile' \\"
echo "  --label 'performance,optimization' \\"
echo "  --body-file <(sed -n '/^## Issue 5/,/^## Summary/p' TOP_5_ISSUES.md | head -n -2)"
echo ""

exit 0

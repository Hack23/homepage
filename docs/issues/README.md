# Issue Templates - Quick Start Guide

This directory contains pre-written GitHub issue templates that can be quickly created using the GitHub CLI or web interface.

## Quick Creation with GitHub CLI

If you have `gh` CLI installed and authenticated:

```bash
# Navigate to repository
cd /home/runner/work/homepage/homepage

# Create all issues at once
for file in docs/issues/issue-*.md; do
  title=$(head -n 1 "$file" | sed 's/^# //')
  gh issue create --title "$title" --body-file "$file" --label "enhancement"
done

# Or create individually
gh issue create --title "$(head -n 1 docs/issues/issue-1-html-validation.md | sed 's/^# //')" \
  --body-file docs/issues/issue-1-html-validation.md \
  --label "enhancement,priority:high"
```

## Manual Creation via Web Interface

1. Go to https://github.com/Hack23/homepage/issues/new
2. Open the desired issue template file
3. Copy the title (first line after removing `#`)
4. Copy the body content (everything after title)
5. Paste into GitHub's issue creation form
6. Add suggested labels
7. Click "Submit new issue"

## Authentication Setup

If you encounter authentication errors:

1. **Install GitHub CLI**:
   ```bash
   # macOS
   brew install gh
   
   # Linux
   sudo apt install gh  # Debian/Ubuntu
   ```

2. **Authenticate**:
   ```bash
   gh auth login
   ```

3. **Verify**:
   ```bash
   gh auth status
   ```

For detailed authentication setup, see: [GITHUB_MCP_AUTHENTICATION.md](../GITHUB_MCP_AUTHENTICATION.md)

## Issue Templates

- **issue-1-html-validation.md** - Add HTML validation tools
- **issue-2-css-linting.md** - Add CSS linting and validation
- **issue-3-link-checker.md** - Add link checker for content validation
- **issue-4-accessibility-testing.md** - Add accessibility testing tools
- **issue-5-documentation.md** - Document Copilot environment

## Customization

Each template includes:
- Clear objectives and background
- Specific acceptance criteria
- Implementation guidance with code examples
- Accurate repository metrics
- Priority and effort estimates

Feel free to modify templates before creating issues to match your specific needs.

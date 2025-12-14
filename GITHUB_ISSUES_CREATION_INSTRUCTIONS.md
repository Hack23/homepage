# GitHub Issues Creation Instructions

## Status

The 10 translation issues have been fully specified and prepared, but could not be automatically created due to authentication limitations in the Copilot agent environment.

## Available Resources

1. **`TRANSLATION_ISSUES_TO_CREATE.md`** - Complete specifications for all 10 issues with full acceptance criteria
2. **`create_translation_issues_api.py`** - Python script to create issues via gh CLI
3. **`TRANSLATION_COMPLETION_SUMMARY.md`** - Executive summary and analysis

## Manual Creation Options

### Option 1: GitHub Web Interface (Recommended)

1. Open the [Hack23/homepage Issues page](https://github.com/Hack23/homepage/issues)
2. Click "New Issue"
3. Copy content from `TRANSLATION_ISSUES_TO_CREATE.md` for each issue:
   - Issue 1: Lines 12-100 (Asset Management & Backup Recovery)
   - Issue 2: Lines 102-150 (Business Continuity & Disaster Recovery)
   - Issue 3: Lines 152-200 (Cloud Security & Monitoring)
   - Issue 4: Lines 202-250 (Secure Development & Vulnerability Management)
   - Issue 5: Lines 252-300 (Security Strategy & Metrics)
   - Issue 6: Lines 302-350 (Stakeholder Management & Supplier Reality)
   - Issue 7: Lines 352-400 (LLM Security & CRA Conformity)
   - Issue 8: Lines 402-450 (Core Navigation - projects.html)
   - Issue 9: Lines 452-500 (AI Policy & Security Training)
   - Issue 10: Lines 502-end (Physical & Email Security)
4. Add labels as specified in each issue
5. Optionally assign to `copilot-swe-agent[bot]`

### Option 2: Using gh CLI with Token

```bash
# Set the GitHub token
export GH_TOKEN="<your_github_token>"

# Run the Python script
python3 create_translation_issues_api.py
```

### Option 3: Using gh CLI Directly

```bash
# Authenticate gh CLI first
gh auth login

# Then run the creation script
/tmp/create_github_issues.sh
```

### Option 4: GitHub Actions Workflow

Create a workflow file that runs with proper authentication:

```yaml
name: Create Translation Issues

on:
  workflow_dispatch:

jobs:
  create-issues:
    runs-on: ubuntu-latest
    permissions:
      issues: write
    steps:
      - uses: actions/checkout@v4
      
      - name: Create Issues
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          python3 create_translation_issues_api.py
```

## Issue Summary

| # | Title | Files | Priority | Labels |
|---|-------|-------|----------|--------|
| 1 | Asset Management & Backup Recovery | 26 | HIGH | translation, content, priority:high, size:medium, isms-documentation |
| 2 | Business Continuity & Disaster Recovery | 26 | HIGH | translation, content, priority:high, size:medium, isms-documentation |
| 3 | Cloud Security & Monitoring | 26 | HIGH | translation, content, priority:high, size:medium, isms-documentation |
| 4 | Secure Development & Vulnerability Mgmt | 26 | HIGH | translation, content, priority:high, size:medium, isms-documentation |
| 5 | Security Strategy & Metrics | 26 | HIGH | translation, content, priority:high, size:medium, isms-documentation |
| 6 | Stakeholder & Supplier Management | 26 | HIGH | translation, content, priority:high, size:medium, isms-documentation |
| 7 | LLM Security & CRA Conformity | 26 | HIGH | translation, content, priority:high, size:medium, isms-documentation, emerging-tech |
| 8 | Core Navigation (projects.html) | 13 | **CRITICAL** | translation, content, priority:critical, size:small, core-navigation |
| 9 | AI Policy & Security Training (Partial) | ~20 | MEDIUM | translation, content, priority:medium, size:medium, isms-documentation |
| 10 | Physical & Email Security (Partial) | ~20 | MEDIUM | translation, content, priority:medium, size:medium, isms-documentation |

**Total Impact:** 260+ translation files across 13 languages

## Authentication Issue Details

The Copilot agent environment has:
- ✅ Workflow permissions: `issues: write`
- ✅ Secret configured: `COPILOT_MCP_GITHUB_PERSONAL_ACCESS_TOKEN`
- ❌ Token not accessible in bash environment variables
- ❌ `gh` CLI cannot access token without explicit `GH_TOKEN` env var

This is a known limitation where the GitHub Actions token needs to be explicitly passed to tools like `gh` CLI.

## Next Steps

1. Choose one of the manual creation options above
2. Create all 10 issues
3. Assign to `copilot-swe-agent[bot]` for automated implementation
4. Tag with `@ui-enhancement-specialist` agent
5. Monitor implementation progress
6. Update Translation-Status.md files as issues are completed

## Expected Outcome

Once created and implemented:
- 260+ new translation files
- All 13 languages reach 85-95% completion
- Complete ISMS policy coverage
- Core navigation available in all languages
- Improved international SEO

---

**Created:** 2025-12-14  
**Status:** Ready for manual creation  
**Documentation:** Complete and comprehensive

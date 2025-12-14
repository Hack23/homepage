# Instructions: Create 10 Translation GitHub Issues

## Quick Summary

**10 GitHub issues are ready to be created** for completing homepage translations across all 13 supported languages.

All issue content has been prepared and is ready for creation.

## Files Created

### Issue Templates
- `/tmp/issue_1.md` - Core Navigation Page (CRITICAL)
- `/tmp/issue_2.md` - Security Operations ISMS Policies (HIGH)
- `/tmp/issue_3.md` - Cloud & Infrastructure Security ISMS Policies (HIGH)
- `/tmp/issue_4.md` - Development Security ISMS Policies (HIGH)
- `/tmp/issue_5.md` - Business Continuity ISMS Policies (HIGH)
- `/tmp/issue_6.md` - Governance & Compliance ISMS Policies (HIGH)
- `/tmp/issue_7.md` - Access & Email Security ISMS Policies (MEDIUM)
- `/tmp/issue_8.md` - Third-Party & AI Security ISMS Policies (MEDIUM)
- `/tmp/issue_9.md` - Corporate Culture ISMS Policies (MEDIUM)
- `/tmp/issue_10.md` - Data Protection ISMS Policies (MEDIUM)

### Documentation
- `TRANSLATION_ISSUES_SUMMARY.md` - Complete reference guide

### Automation Script
- `/tmp/create_github_issues.sh` - Bash script for automated creation

## Option 1: Manual Creation via GitHub Web Interface

### Steps for Each Issue

1. Open https://github.com/Hack23/homepage/issues/new
2. **Copy Title** from list below
3. **Copy Body** from corresponding `/tmp/issue_N.md` file
4. **Add Labels** as specified below
5. Click "Submit new issue"
6. **Assign to:** @hack23-ui-enhancement-specialist (or copilot-swe-agent[bot])

### Issue Details

#### Issue 1 (CRITICAL)
- **Title:** `Translate Core Navigation Page: projects.html (13 languages)`
- **Labels:** `translation`, `priority:critical`, `size:medium`, `domain:content`, `agent:ui-enhancement`
- **Body:** Content of `/tmp/issue_1.md`

#### Issue 2 (HIGH)
- **Title:** `Translate Security Operations ISMS Policies (13 languages, 3 files)`
- **Labels:** `translation`, `priority:high`, `size:large`, `domain:content`, `compliance:iso27001`, `agent:ui-enhancement`
- **Body:** Content of `/tmp/issue_2.md`

#### Issue 3 (HIGH)
- **Title:** `Translate Cloud & Infrastructure Security ISMS Policies (13 languages, 3 files)`
- **Labels:** `translation`, `priority:high`, `size:large`, `domain:content`, `compliance:iso27001`, `agent:ui-enhancement`
- **Body:** Content of `/tmp/issue_3.md`

#### Issue 4 (HIGH)
- **Title:** `Translate Development Security ISMS Policies (13 languages, 3 files)`
- **Labels:** `translation`, `priority:high`, `size:large`, `domain:content`, `compliance:iso27001`, `agent:ui-enhancement`
- **Body:** Content of `/tmp/issue_4.md`

#### Issue 5 (HIGH)
- **Title:** `Translate Business Continuity ISMS Policies (13 languages, 3 files)`
- **Labels:** `translation`, `priority:high`, `size:large`, `domain:content`, `compliance:iso27001`, `agent:ui-enhancement`
- **Body:** Content of `/tmp/issue_5.md`

#### Issue 6 (HIGH)
- **Title:** `Translate Governance & Compliance ISMS Policies (13 languages, 4 files)`
- **Labels:** `translation`, `priority:high`, `size:large`, `domain:content`, `compliance:iso27001`, `agent:ui-enhancement`
- **Body:** Content of `/tmp/issue_6.md`

#### Issue 7 (MEDIUM)
- **Title:** `Translate Access & Email Security ISMS Policies (13 languages, 3 files)`
- **Labels:** `translation`, `priority:medium`, `size:large`, `domain:content`, `compliance:iso27001`, `agent:ui-enhancement`
- **Body:** Content of `/tmp/issue_7.md`

#### Issue 8 (MEDIUM)
- **Title:** `Translate Third-Party & AI Security ISMS Policies (13 languages, 3 files)`
- **Labels:** `translation`, `priority:medium`, `size:large`, `domain:content`, `compliance:iso27001`, `agent:ui-enhancement`
- **Body:** Content of `/tmp/issue_8.md`

#### Issue 9 (MEDIUM)
- **Title:** `Translate Corporate Culture ISMS Policies (13 languages, 3 files)`
- **Labels:** `translation`, `priority:medium`, `size:large`, `domain:content`, `compliance:iso27001`, `agent:ui-enhancement`
- **Body:** Content of `/tmp/issue_9.md`

#### Issue 10 (MEDIUM)
- **Title:** `Translate Data Protection ISMS Policies (13 languages, 4 files)`
- **Labels:** `translation`, `priority:medium`, `size:large`, `domain:content`, `compliance:iso27001`, `agent:ui-enhancement`
- **Body:** Content of `/tmp/issue_10.md`

## Option 2: Automated Creation with GitHub CLI

If you have `gh` CLI installed and authenticated:

```bash
# Set GitHub token (if not already set)
export GH_TOKEN="your_github_token_here"

# Run the automation script
/tmp/create_github_issues.sh
```

This will create all 10 issues automatically.

## Option 3: Using GitHub REST API

### Prerequisites
- GitHub Personal Access Token with `repo` scope
- `curl` or similar HTTP client

### Example for Issue 1

```bash
# Set your token
export GITHUB_TOKEN="your_token_here"

# Read issue body
ISSUE_BODY=$(cat /tmp/issue_1.md)

# Create issue via API
curl -X POST \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/Hack23/homepage/issues \
  -d '{
    "title": "Translate Core Navigation Page: projects.html (13 languages)",
    "body": "'"$(cat /tmp/issue_1.md | sed 's/"/\\"/g')"'",
    "labels": ["translation", "priority:critical", "size:medium", "domain:content", "agent:ui-enhancement"]
  }'
```

Repeat for all 10 issues by changing the title, body file, and labels accordingly.

## After Creation

### Verify Issues
1. Check https://github.com/Hack23/homepage/issues
2. Confirm all 10 issues are created
3. Verify labels are correctly applied
4. Ensure issue bodies are properly formatted

### Assign to Agent
For each issue, assign to: `copilot-swe-agent[bot]` or `@hack23-ui-enhancement-specialist`

### Track Progress
Monitor issue completion via:
- GitHub Issues dashboard
- Project boards (if configured)
- Translation status files (`[Language]-Translation-Status.md`)

## Expected Outcomes

Once all 10 issues are resolved:

✅ **390 total translations** created
- 30 base HTML files
- × 13 languages each
- = 390 translated files

✅ **All 13 languages at 100% coverage**
- Arabic (ar)
- Danish (da)
- German (de)
- Spanish (es)
- Finnish (fi)
- French (fr)
- Hebrew (he)
- Japanese (ja)
- Korean (ko)
- Dutch (nl)
- Norwegian (no)
- Swedish (sv)
- Chinese (zh)

✅ **Complete SEO infrastructure**
- Proper `lang` attributes
- Complete hreflang tags
- Localized Schema.org structured data
- Translated meta tags and Open Graph

✅ **Updated documentation**
- All `[Language]-Translation-Status.md` files updated
- `TRANSLATION_DOCUMENTATION_README.md` reflects 100% completion

## Support & Questions

For questions about:
- **Issue content:** Review `TRANSLATION_ISSUES_SUMMARY.md`
- **Translation guidelines:** Check `[Language]-Translation-Guide.md` files
- **Agent capabilities:** See `.github/agents/ui-enhancement-specialist.md`
- **Overall project:** Reference `TRANSLATION_DOCUMENTATION_README.md`

---

**Created:** December 14, 2025  
**Purpose:** Facilitate creation of 10 GitHub issues for translation completion  
**Status:** Ready for issue creation

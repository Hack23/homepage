# Translation Issues - README

## Quick Start Guide

This directory contains complete documentation for 10 GitHub issues that need to be created to complete translation work across 13 languages in the Hack23/homepage repository.

## 📋 What You Need to Do

**Create 10 GitHub issues manually** using the templates in [TRANSLATION_ISSUES_TO_CREATE.md](TRANSLATION_ISSUES_TO_CREATE.md).

### Why Manual Creation?

Automated issue creation failed due to GitHub MCP server authentication. The server is running with proper capabilities, but the required secret (`COPILOT_MCP_GITHUB_PERSONAL_ACCESS_TOKEN`) is not accessible in the agent environment.

## 📚 Documentation Files

| File | Purpose | Size |
|------|---------|------|
| **[TRANSLATION_ISSUES_TO_CREATE.md](TRANSLATION_ISSUES_TO_CREATE.md)** | Complete templates for all 10 issues | 20KB |
| **[TRANSLATION_ISSUES_SUMMARY.md](TRANSLATION_ISSUES_SUMMARY.md)** | Executive summary & instructions | 9KB |
| **[GITHUB_ISSUE_CREATION_STATUS.md](GITHUB_ISSUE_CREATION_STATUS.md)** | Detailed status & troubleshooting | 7.5KB |
| **[TRANSLATION_DOCUMENTATION_README.md](TRANSLATION_DOCUMENTATION_README.md)** | Main translation docs | Existing |

## 🎯 The 10 Issues

### High Priority (276 files)
1. **Swedish (sv) Discordian ISMS Policies** - 20 files
2. **Nordic (DA/FI/NO) Discordian ISMS Policies** - 75 files
3. **RTL (AR/HE) Discordian ISMS Policies** - 75 files
4. **Asian (JA/ZH/KO) Discordian ISMS Policies** - 126 files

### Medium Priority (173 files)
5. **European (DE/NL/FR/ES) Discordian ISMS Policies** - 152 files
6. **Nordic (DA/FI/NO) ISO 27001 Pages** - 9 files
7. **European (DE/NL/FR/ES) ISO 27001 Pages** - 10 files
9. **Core Pages (why-hack23, cia-triad-faq)** - 2 files

### Low Priority (21 files)
8. **European (DE/NL/FR/ES) Blog Posts** - 12 files
10. **Swedish Election 2026 Page** - 9 files

**Total: 470 missing translation files**

## 🚀 How to Create Issues

### Option 1: GitHub Web Interface (Recommended - 15 minutes)

1. Go to https://github.com/Hack23/homepage/issues/new
2. Open [TRANSLATION_ISSUES_TO_CREATE.md](TRANSLATION_ISSUES_TO_CREATE.md)
3. For each issue:
   - Copy the title
   - Copy the body content
   - Add the labels (translation, priority, language tags)
   - Click "Submit new issue"

### Option 2: GitHub CLI (5 minutes with auth)

```bash
# Authenticate once
gh auth login

# Create issues (repeat for each)
gh issue create \
  --repo Hack23/homepage \
  --title "Complete Swedish (sv) Discordian ISMS Policy Translations (20 files)" \
  --label "translation,high-priority,swedish" \
  --body "$(cat issue1_body.txt)"
```

### Option 3: GitHub REST API (with PAT)

```bash
TOKEN="your_github_pat"

curl -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/Hack23/homepage/issues \
  -d '{"title":"Issue Title","body":"Issue Body","labels":["label1","label2"]}'
```

## 📊 Translation Status

| Language | Existing Files | Missing Files | Coverage |
|----------|----------------|---------------|----------|
| Swedish | 73 | 20 | 78.5% |
| Danish | 65 | 28 | 69.9% |
| Finnish | 65 | 28 | 69.9% |
| Norwegian | 65 | 28 | 69.9% |
| Arabic | 53 | 40 | 57.0% |
| Hebrew | 52 | 41 | 55.9% |
| Japanese | 50 | 43 | 53.8% |
| Chinese | 50 | 43 | 53.8% |
| Korean | 50 | 43 | 53.8% |
| German | 49 | 44 | 52.7% |
| Dutch | 49 | 44 | 52.7% |
| French | 48 | 45 | 51.6% |
| Spanish | 48 | 45 | 51.6% |

**Total: 736 files exist, 470 missing across all 13 languages**

## 🔧 Common Requirements

All translated files must include:
- ✅ Proper language attributes (`lang="xx"`)
- ✅ Complete hreflang tags for all 13 languages
- ✅ Localized og:locale metadata
- ✅ Schema.org structured data with correct `inLanguage`
- ✅ Localized navigation and breadcrumbs
- ✅ Professional translation in target language
- ✅ ISO 27001 terminology where applicable
- ✅ Preserve Discordian voice and humor
- ✅ **All headers, SEO meta, and structured data in target language**

## 🔐 Fix Authentication (For Future Automation)

To enable automated issue creation in future:

1. **Configure Repository Secret**:
   ```
   Settings → Secrets and variables → Actions → 
   Environments → copilot → Add secret:
   
   Name: COPILOT_MCP_GITHUB_PERSONAL_ACCESS_TOKEN
   Value: GitHub Personal Access Token with 'repo' scope
   ```

2. **Verify MCP Server Configuration**:
   - Check `.github/copilot-mcp.json`
   - Ensure secret is passed to MCP server at startup
   - Test with a simple issue creation

3. **Alternative**: Use GitHub Actions workflow with `${{ github.token }}`

## 📝 Translation Guides

Each language has detailed guides:
- Arabic-Translation-Guide.md
- Chinese-Translation-Guide.md
- Danish-Translation-Guide.md
- Dutch-Translation-Guide.md
- Finnish-Translation-Guide.md
- French-Translation-Guide.md
- German-Translation-Guide.md
- Hebrew-Translation-Guide.md
- Japanese-Translation-Guide.md
- Korean-Translation-Guide.md
- Norwegian-Translation-Guide.md
- Spanish-Translation-Guide.md
- Swedish-Translation-Guide.md

## 🎯 Next Steps

1. **IMMEDIATE**: Manually create the 10 issues
2. **SHORT-TERM**: Fix MCP authentication for future automation
3. **ONGOING**: Assign issues to `.github/agents/ui-enhancement-specialist.md`
4. **MONITOR**: Track progress in Translation-Status.md files

## 📞 Questions?

- Review [TRANSLATION_ISSUES_SUMMARY.md](TRANSLATION_ISSUES_SUMMARY.md) for detailed analysis
- Check [GITHUB_ISSUE_CREATION_STATUS.md](GITHUB_ISSUE_CREATION_STATUS.md) for technical details
- See individual Translation-Status.md files for per-language tracking

---

**Created**: 2025-12-14  
**Branch**: copilot/create-translation-issues  
**Commits**: 4  
**Files Changed**: 16 (3 new, 13 updated)  
**Issues Ready**: 10 (manual creation required)

# Creating Translation Issues with GitHub API

This directory contains a Python script to automatically create all 10 translation issues using the GitHub REST API.

## Quick Start

### Prerequisites
- Python 3.6 or higher
- GitHub Personal Access Token with `repo` scope

### Setup

1. **Create a Personal Access Token:**
   - Go to https://github.com/settings/tokens
   - Click "Generate new token (classic)"
   - Give it a name like "Create Translation Issues"
   - Select scopes:
     - ✅ `repo` (Full control of private repositories) - includes `public_repo` for public repos
   - Click "Generate token"
   - Copy the token (you won't see it again!)

2. **Set the environment variable:**
   ```bash
   export GITHUB_TOKEN=ghp_your_token_here
   ```

3. **Run the script:**
   ```bash
   python3 create_translation_issues.py
   ```

## What the Script Does

The script will create **10 GitHub issues** in the `Hack23/homepage` repository:

1. 🇫🇷 **French Translation** - 20 Critical ISMS Files
2. 🇪🇸 **Spanish Translation** - 20 Critical ISMS Files
3. 🇳🇱 **Dutch Translation** - 18 Critical ISMS Files
4. 🇩🇪 **German Translation** - 18 Critical ISMS Files
5. 🇯🇵 **Japanese Translation** - 20 Critical ISMS Files
6. 🇨🇳 **Chinese Translation** - 20 Critical ISMS Files
7. 🇰🇷 **Korean Translation** - 20 Critical ISMS Files
8. 🇩🇰🇫🇮🇳🇴 **Nordic Languages** - 15 Files Each (45 total)
9. 🇸🇪 **Swedish Translation** - 12 Final ISMS Files
10. 🇮🇱 **Hebrew Translation** - 15 Critical ISMS Files (RTL)

Each issue includes:
- Complete objective and background
- Detailed acceptance criteria with file lists
- Technical requirements (HTML5, hreflang, OpenGraph, Schema.org)
- Translation quality standards
- Agent assignment (@ui-enhancement-specialist)
- Success metrics

## Script Output

The script will:
- Print progress as each issue is created
- Show the issue number and URL for each created issue
- Save results to `issue_creation_results.json`
- Return exit code 0 on success, 1 if any issues failed

### Example Output

```
================================================================================
CREATING 10 GITHUB ISSUES FOR TRANSLATION COMPLETION
================================================================================

📁 Repository: Hack23/homepage
🎯 Creating 10 issues...

[1/10] Creating: 🇫🇷 French Translation: Complete 20 Critical Discordian ISMS...
        ✅ Created issue #123
        🔗 https://github.com/Hack23/homepage/issues/123

[2/10] Creating: 🇪🇸 Spanish Translation: Complete 20 Critical Discordian...
        ✅ Created issue #124
        🔗 https://github.com/Hack23/homepage/issues/124

...

================================================================================
SUMMARY
================================================================================

✅ Successfully created: 10/10 issues

Created issues:
  #123: https://github.com/Hack23/homepage/issues/123
  #124: https://github.com/Hack23/homepage/issues/124
  ...

📊 Results saved to: issue_creation_results.json
```

## Troubleshooting

### "GITHUB_TOKEN environment variable not set"
- Make sure you've exported the token: `export GITHUB_TOKEN=your_token`
- Check it's set: `echo $GITHUB_TOKEN`

### "HTTP 401: Unauthorized"
- Your token may be invalid or expired
- Generate a new token and try again

### "HTTP 403: Forbidden"
- Your token doesn't have the required `repo` scope
- Create a new token with the correct permissions

### "HTTP 422: Validation Failed"
- This usually means a label doesn't exist in the repository
- Check that all labels exist: `translation`, `priority:high`, `priority:medium`, `category:isms`, `size:small`, `size:medium`, `size:large`, language labels

## Alternative: Using GitHub CLI

If you have the GitHub CLI (`gh`) installed and authenticated, you can also use it:

```bash
# Authenticate
gh auth login

# The script will automatically detect and use gh CLI authentication
python3 create_translation_issues.py
```

## Files

- **`create_translation_issues.py`** - Main script to create issues via GitHub REST API
- **`CREATE_ISSUES_README.md`** - This file, documentation
- **`TRANSLATION_ISSUES_CREATED.md`** - Complete specifications for all 10 issues (reference)

## Total Impact

Creating these 10 issues will result in:
- **188 translation files** to be created
- **All 13 languages** covered (AR, HE, JA, ZH, KO, DA, FI, NO, NL, DE, FR, ES, SV)
- **Average completion increase:** ~18% per language
- Focus on **Discordian ISMS policies** (core security documentation)

## Next Steps

After creating the issues:
1. Review each issue in the GitHub UI
2. Assign issues to the @ui-enhancement-specialist agent
3. The agent will create the translation files according to specifications
4. Track progress through the Translation Status files (`*-Translation-Status.md`)

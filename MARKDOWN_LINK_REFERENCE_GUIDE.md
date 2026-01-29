# Markdown Link Reference Guide for Hack23AB Directory

## Overview
This guide documents the correct relative path patterns for markdown files in the `Hack23AB/` directory structure to ensure all internal links work correctly.

## Directory Structure

```
homepage/
├── CLASSIFICATION.md
├── Business_Strategy.md (potential)
├── Marketing_Strategy.md (potential)
├── Marketing_Plan.md (potential)
├── AnnualReport2025/
│   └── Annual_Report_2025.md (potential)
└── Hack23AB/
    └── Marketing/
        ├── Linkedin/
        │   └── LinkedIn_Analytics_Report_2025.md
        └── SearchEngines/
            └── Google/
                └── Google_Search_Console_Report_2025.md
```

## Correct Relative Path Patterns

### From: `Hack23AB/Marketing/Linkedin/LinkedIn_Analytics_Report_2025.md`

**Depth:** 3 levels deep from root

To root-level files:
- ✅ `../../../CLASSIFICATION.md#confidentiality-levels`
- ✅ `../../../Business_Strategy.md`
- ✅ `../../../Marketing_Strategy.md`
- ✅ `../../../Marketing_Plan.md`
- ✅ `../../../AnnualReport2025/Annual_Report_2025.md`

❌ INCORRECT: `../../CLASSIFICATION.md` (only 2 levels)

### From: `Hack23AB/Marketing/SearchEngines/Google/Google_Search_Console_Report_2025.md`

**Depth:** 4 levels deep from root

To root-level files:
- ✅ `../../../../CLASSIFICATION.md#confidentiality-levels`
- ✅ `../../../../Business_Strategy.md`
- ✅ `../../../../Marketing_Strategy.md`
- ✅ `../../../../Marketing_Plan.md`
- ✅ `../../../../AnnualReport2025/Annual_Report_2025.md`

To sibling Marketing directories:
- ✅ `../../Linkedin/LinkedIn_Analytics_Report_2025.md` (up 2 to Marketing, then down)

❌ INCORRECT: `../../CLASSIFICATION.md` (only 2 levels, needs 4)
❌ INCORRECT: `../Linkedin/...` (only 1 level up, needs 2)

## How to Calculate Relative Paths

1. **Count directory depth** from root to your file
   - Example: `Hack23AB/Marketing/Linkedin/file.md` = 3 levels

2. **Use `../` for each level** to reach root
   - 3 levels = `../../../`
   - 4 levels = `../../../../`

3. **Then add the target path** from root
   - `../../../CLASSIFICATION.md`
   - `../../../../AnnualReport2025/Annual_Report_2025.md`

## Quick Reference Table

| Source File Location | Depth | To Root | Example Path |
|---------------------|-------|---------|--------------|
| `Hack23AB/Marketing/Linkedin/*.md` | 3 | `../../../` | `../../../CLASSIFICATION.md` |
| `Hack23AB/Marketing/SearchEngines/Google/*.md` | 4 | `../../../../` | `../../../../CLASSIFICATION.md` |

## Verification

To verify your relative paths are correct:

1. **Manual check:** Count the directory separators in the path
2. **Link checker:** Use a markdown link checker tool
3. **Test locally:** Open the markdown file in an editor that renders links

## Common Mistakes

❌ **Using fixed `../../` everywhere** - Different file depths need different `../` counts
❌ **Forgetting to count the file itself** - Count all levels, including the file's directory
❌ **Not testing anchor links** - Anchors like `#confidentiality-levels` must exist in target

## Tools for Link Validation

- `markdown-link-check`: CLI tool for checking markdown links
- `markdownlint`: Linter that can detect some link issues
- `linkinator`: Used by this repo for HTML link checking (can be adapted for markdown)

## Reference: Existing Anchor

The anchor `#confidentiality-levels` exists in `CLASSIFICATION.md` at line 53:
```markdown
### 🛡️ Confidentiality Levels {#confidentiality-levels}
```

This is a valid anchor and can be linked to using:
- From 3 levels deep: `../../../CLASSIFICATION.md#confidentiality-levels`
- From 4 levels deep: `../../../../CLASSIFICATION.md#confidentiality-levels`

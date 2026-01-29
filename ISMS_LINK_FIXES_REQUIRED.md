# Broken Link Fixes Required in ISMS Repository

## Overview
Two markdown files in the `Hack23/ISMS` repository have broken relative links that need to be corrected.

## Files to Fix

### 1. LinkedIn_Analytics_Report_2025.md
**Location:** `Hack23AB/Marketing/Linkedin/LinkedIn_Analytics_Report_2025.md`  
**Depth from root:** 3 levels  
**Required prefix:** `../../../`

#### Broken Links (all at bottom of file):

**Line ~630 (Classification badge):**
```markdown
<!-- BROKEN -->
**🏷️ Classification:** [![Confidentiality: Internal](https://img.shields.io/badge/C-Internal-yellow?style=flat-square)](../../CLASSIFICATION.md#confidentiality-levels)

<!-- FIXED -->
**🏷️ Classification:** [![Confidentiality: Internal](https://img.shields.io/badge/C-Internal-yellow?style=flat-square)](../../../CLASSIFICATION.md#confidentiality-levels)
```

**Line ~631 (Related Documents):**
```markdown
<!-- BROKEN -->
**🔗 Related Documents:** [Marketing_Strategy.md](../../Marketing_Strategy.md) | [Marketing_Plan.md](../../Marketing_Plan.md) | [Annual_Report_2025.md](../../AnnualReport2025/Annual_Report_2025.md) | [Business_Strategy.md](../../Business_Strategy.md) | [Marketing_Analytics_Dashboard_2025.md](../Marketing_Analytics_Dashboard_2025.md)

<!-- FIXED -->
**🔗 Related Documents:** [Marketing_Strategy.md](../../../Marketing_Strategy.md) | [Marketing_Plan.md](../../../Marketing_Plan.md) | [Annual_Report_2025.md](../../../AnnualReport2025/Annual_Report_2025.md) | [Business_Strategy.md](../../../Business_Strategy.md) | [Marketing_Analytics_Dashboard_2025.md](../Marketing_Analytics_Dashboard_2025.md)
```

---

### 2. Google_Search_Console_Report_2025.md
**Location:** `Hack23AB/Marketing/SearchEngines/Google/Google_Search_Console_Report_2025.md`  
**Depth from root:** 4 levels  
**Required prefix:** `../../../../`

#### Broken Links (throughout document):

**Line ~105 (Business Strategy reference):**
```markdown
<!-- BROKEN -->
Per [Business_Strategy.md](../../Business_Strategy.md):

<!-- FIXED -->
Per [Business_Strategy.md](../../../../Business_Strategy.md):
```

**Line ~115 (Marketing Strategy reference):**
```markdown
<!-- BROKEN -->
Per [Marketing_Strategy.md](../../Marketing_Strategy.md) geographic targets:

<!-- FIXED -->
Per [Marketing_Strategy.md](../../../../Marketing_Strategy.md) geographic targets:
```

**Line ~197 (Annual Report reference):**
```markdown
<!-- BROKEN -->
For [Annual_Report_2025.md](../../AnnualReport2025/Annual_Report_2025.md) "Value Creation" section:

<!-- FIXED -->
For [Annual_Report_2025.md](../../../../AnnualReport2025/Annual_Report_2025.md) "Value Creation" section:
```

**Line ~445 (Classification badge):**
```markdown
<!-- BROKEN -->
**🏷️ Classification:** [![Confidentiality: Internal](https://img.shields.io/badge/C-Internal-yellow?style=flat-square)](../../CLASSIFICATION.md#confidentiality-levels)

<!-- FIXED -->
**🏷️ Classification:** [![Confidentiality: Internal](https://img.shields.io/badge/C-Internal-yellow?style=flat-square)](../../../../CLASSIFICATION.md#confidentiality-levels)
```

**Line ~447 (Related Documents):**
```markdown
<!-- BROKEN -->
**🔗 Related Documents:** [Marketing_Strategy.md](../../Marketing_Strategy.md) | [Marketing_Plan.md](../../Marketing_Plan.md) | [Annual_Report_2025.md](../../AnnualReport2025/Annual_Report_2025.md) | [LinkedIn_Analytics_Report_2025.md](../Linkedin/LinkedIn_Analytics_Report_2025.md)

<!-- FIXED -->
**🔗 Related Documents:** [Marketing_Strategy.md](../../../../Marketing_Strategy.md) | [Marketing_Plan.md](../../../../Marketing_Plan.md) | [Annual_Report_2025.md](../../../../AnnualReport2025/Annual_Report_2025.md) | [LinkedIn_Analytics_Report_2025.md](../../Linkedin/LinkedIn_Analytics_Report_2025.md)
```

---

## Summary of Changes

### LinkedIn_Analytics_Report_2025.md
- Change `../../CLASSIFICATION.md` → `../../../CLASSIFICATION.md` (1 occurrence)
- Change `../../Marketing_Strategy.md` → `../../../Marketing_Strategy.md` (1 occurrence)
- Change `../../Marketing_Plan.md` → `../../../Marketing_Plan.md` (1 occurrence)
- Change `../../AnnualReport2025/Annual_Report_2025.md` → `../../../AnnualReport2025/Annual_Report_2025.md` (1 occurrence)
- Change `../../Business_Strategy.md` → `../../../Business_Strategy.md` (1 occurrence)

**Total:** 5 link fixes

### Google_Search_Console_Report_2025.md
- Change `../../Business_Strategy.md` → `../../../../Business_Strategy.md` (1 occurrence)
- Change `../../Marketing_Strategy.md` → `../../../../Marketing_Strategy.md` (2 occurrences)
- Change `../../CLASSIFICATION.md#confidentiality-levels` → `../../../../CLASSIFICATION.md#confidentiality-levels` (1 occurrence)
- Change `../../Marketing_Plan.md` → `../../../../Marketing_Plan.md` (1 occurrence)
- Change `../../AnnualReport2025/Annual_Report_2025.md` → `../../../../AnnualReport2025/Annual_Report_2025.md` (2 occurrences)
- Change `../Linkedin/LinkedIn_Analytics_Report_2025.md` → `../../Linkedin/LinkedIn_Analytics_Report_2025.md` (1 occurrence)

**Total:** 8 link fixes (9 occurrences)

---

## Root Cause
Files at different directory depths require different numbers of `../` to reach root:
- **3 levels deep** (LinkedIn report): needs `../../../`
- **4 levels deep** (Google report): needs `../../../../`

The broken links all incorrectly used `../../` (2 levels) regardless of actual depth.

---

## How to Apply

### Option 1: Manual Edit
1. Open each file in the ISMS repository
2. Find and replace the broken links with fixed versions
3. Commit changes

### Option 2: Find & Replace (Linux/Mac)
```bash
# Navigate to ISMS repo
cd path/to/ISMS

# LinkedIn report (3 levels deep)
sed -i 's|](../../CLASSIFICATION.md|](../../../CLASSIFICATION.md|g' Hack23AB/Marketing/Linkedin/LinkedIn_Analytics_Report_2025.md
sed -i 's|](../../Marketing_Strategy.md|](../../../Marketing_Strategy.md|g' Hack23AB/Marketing/Linkedin/LinkedIn_Analytics_Report_2025.md
sed -i 's|](../../Marketing_Plan.md|](../../../Marketing_Plan.md|g' Hack23AB/Marketing/Linkedin/LinkedIn_Analytics_Report_2025.md
sed -i 's|](../../Business_Strategy.md|](../../../Business_Strategy.md|g' Hack23AB/Marketing/Linkedin/LinkedIn_Analytics_Report_2025.md
sed -i 's|](../../AnnualReport2025/|](../../../AnnualReport2025/|g' Hack23AB/Marketing/Linkedin/LinkedIn_Analytics_Report_2025.md

# Google report (4 levels deep)
sed -i 's|](../../Business_Strategy.md|](../../../../Business_Strategy.md|g' Hack23AB/Marketing/SearchEngines/Google/Google_Search_Console_Report_2025.md
sed -i 's|](../../Marketing_Strategy.md|](../../../../Marketing_Strategy.md|g' Hack23AB/Marketing/SearchEngines/Google/Google_Search_Console_Report_2025.md
sed -i 's|](../../Marketing_Plan.md|](../../../../Marketing_Plan.md|g' Hack23AB/Marketing/SearchEngines/Google/Google_Search_Console_Report_2025.md
sed -i 's|](../../CLASSIFICATION.md|](../../../../CLASSIFICATION.md|g' Hack23AB/Marketing/SearchEngines/Google/Google_Search_Console_Report_2025.md
sed -i 's|](../../AnnualReport2025/|](../../../../AnnualReport2025/|g' Hack23AB/Marketing/SearchEngines/Google/Google_Search_Console_Report_2025.md
sed -i 's|](../Linkedin/LinkedIn_Analytics|](../../Linkedin/LinkedIn_Analytics|g' Hack23AB/Marketing/SearchEngines/Google/Google_Search_Console_Report_2025.md
```

### Option 3: Automated via GitHub API
Use GitHub API or web interface to update the files directly in the ISMS repository.

---

## Verification

After applying fixes, verify links work by:
1. Opening the files in a markdown viewer
2. Clicking each link to ensure it resolves
3. Running a markdown link checker

Expected result: All 13 links (5 in LinkedIn + 8 in Google) should resolve correctly to their target files.

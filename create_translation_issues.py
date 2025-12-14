#!/usr/bin/env python3
"""
Create 10 GitHub issues for translation completion using GitHub REST API.

This script reads the issue specifications from TRANSLATION_ISSUES_CREATED.md
and creates them programmatically using the GitHub API.

Usage:
    export GITHUB_TOKEN=<your_personal_access_token>
    python3 create_translation_issues.py

The script will create all 10 issues in the Hack23/homepage repository.
"""

import os
import sys
import json
import urllib.request
import urllib.error

# GitHub API configuration
GITHUB_API_URL = "https://api.github.com"
REPO_OWNER = "Hack23"
REPO_NAME = "homepage"

# Issue data - complete specifications for all 10 translation issues
ISSUES = [
    {
        "title": "🇫🇷 French Translation: Complete 20 Critical Discordian ISMS Policy Files (Priority 1)",
        "body": """## 🎯 Objective
Create 20 high-priority Discordian ISMS policy translation files for French (fr), focusing on core security policies and compliance frameworks.

## 📋 Background
French translation is 51.1% complete (48/94 files). This batch focuses on the most critical ISMS policies that form the foundation of Hack23's security documentation.

**Target Audience:** French-speaking enterprise clients in France, Belgium, Switzerland, and Quebec seeking ISO 27001 and cybersecurity expertise.

## 📊 Current State
- **Language:** French (fr)
- **Completion:** 51.1% (48/94 files complete)
- **Missing:** 20 critical Discordian ISMS files
- **Priority:** HIGH

## ✅ Acceptance Criteria

### Files to Create (20 files)
- [ ] `discordian-info-sec-policy_fr.html` - Information Security Policy
- [ ] `discordian-access-control_fr.html` - Access Control Policy
- [ ] `discordian-incident-response_fr.html` - Incident Response Plan
- [ ] `discordian-acceptable-use_fr.html` - Acceptable Use Policy
- [ ] `discordian-cybersecurity_fr.html` - Cybersecurity Manifesto
- [ ] `discordian-risk-assessment_fr.html` - Risk Assessment
- [ ] `discordian-risk-register_fr.html` - Risk Register
- [ ] `discordian-compliance_fr.html` - Compliance Overview
- [ ] `discordian-compliance-frameworks_fr.html` - Compliance Frameworks
- [ ] `discordian-isms-review_fr.html` - ISMS Strategic Review
- [ ] `discordian-isms-transparency_fr.html` - ISMS Transparency Plan
- [ ] `discordian-secure-dev_fr.html` - Secure Development
- [ ] `discordian-vuln-mgmt_fr.html` - Vulnerability Management
- [ ] `discordian-crypto_fr.html` - Cryptography Policy
- [ ] `discordian-network-security_fr.html` - Network Security
- [ ] `discordian-cloud-security_fr.html` - Cloud Security
- [ ] `discordian-change-mgmt_fr.html` - Change Management
- [ ] `discordian-backup-recovery_fr.html` - Backup & Recovery
- [ ] `discordian-business-continuity_fr.html` - Business Continuity
- [ ] `discordian-disaster-recovery_fr.html` - Disaster Recovery

### Technical Requirements
- HTML5 with `lang="fr"` attribute
- Complete hreflang tags for all 13 languages
- Meta tags in French (title, description, keywords)
- OpenGraph with `og:locale="fr_FR"` and regional alternates (fr_BE, fr_CH, fr_CA)
- Schema.org with `inLanguage: "fr"`
- Translated headers and SEO content

### Translation Quality
- Professional business French for enterprise cybersecurity
- Technical terminology: ISMS → Système de Management de la Sécurité de l'Information (SMSI)
- AI translation acceptable per requirements
- Discordian narrative style preserved

## 🤖 Recommended Agent
**Agent:** @ui-enhancement-specialist

**Rationale:** Expert in HTML structure, accessibility, internationalization, and translation workflows.

## 📈 Success Metrics
- 20 French ISMS files created with valid HTML5
- Complete hreflang coverage (13 languages)
- Translation status updated to 72.3% (68/94 files)

---
**Priority:** HIGH | **Effort:** M (4-6h) | **Impact:** +21.2%""",
        "labels": ["translation", "priority:high", "language:french", "category:isms", "size:medium"]
    },
    {
        "title": "🇪🇸 Spanish Translation: Complete 20 Critical Discordian ISMS Policy Files (Priority 1)",
        "body": """## 🎯 Objective
Create 20 high-priority Discordian ISMS policy translation files for Spanish (es), focusing on core security policies and compliance frameworks.

## 📋 Background
Spanish translation is 51.1% complete (48/94 files). This batch focuses on critical ISMS policies for Spanish-speaking markets (Spain, Latin America).

**Target Audience:** Spanish-speaking enterprise clients in Spain, Mexico, Argentina, Colombia, and Latin America.

## 📊 Current State
- **Language:** Spanish (es)
- **Completion:** 51.1% (48/94 files complete)
- **Missing:** 20 critical Discordian ISMS files
- **Priority:** HIGH

## ✅ Acceptance Criteria

### Files to Create (20 files)
Same file structure as French issue, targeting Spanish translation.

### Technical Requirements
- HTML5 with `lang="es"` attribute
- Complete hreflang tags for all 13 languages
- OpenGraph with `og:locale="es_ES"` and alternates (es_MX, es_AR, es_CO)
- Schema.org with `inLanguage: "es"`

### Translation Quality
- Professional Spanish (European Spanish base, Latin American variants considered)
- Technical terminology: ISMS → Sistema de Gestión de Seguridad de la Información (SGSI)
- AI translation acceptable

## 🤖 Recommended Agent
**Agent:** @ui-enhancement-specialist

## 📈 Success Metrics
- 20 Spanish ISMS files created
- Translation status updated to 72.3% (68/94 files)

---
**Priority:** HIGH | **Effort:** M (4-6h) | **Impact:** +21.2%""",
        "labels": ["translation", "priority:high", "language:spanish", "category:isms", "size:medium"]
    },
    {
        "title": "🇳🇱 Dutch Translation: Complete 18 Critical Discordian ISMS Policy Files (Priority 1)",
        "body": """## 🎯 Objective
Create 18 high-priority Discordian ISMS policy translation files for Dutch (nl).

## 📋 Background
Dutch translation is 52.1% complete (49/94 files). Targeting Netherlands and Flanders (Belgium).

## 📊 Current State
- **Language:** Dutch (nl)
- **Completion:** 52.1% (49/94 files)
- **Missing:** 18 critical ISMS files
- **Priority:** HIGH

## ✅ Acceptance Criteria

### Files to Create (18 files)
Core ISMS policies for Dutch-speaking markets.

### Technical Requirements
- HTML5 with `lang="nl"` attribute
- OpenGraph with `og:locale="nl_NL"` and `nl_BE` alternate
- Complete hreflang tags

### Translation Quality
- Professional Dutch for Netherlands and Belgium
- Technical terminology: ISMS → Informatiebeveiligingsmanagementsysteem

## 🤖 Recommended Agent
**Agent:** @ui-enhancement-specialist

## 📈 Success Metrics
- 18 Dutch ISMS files created
- Translation status updated to 71.3% (67/94 files)

---
**Priority:** HIGH | **Effort:** M (4-6h) | **Impact:** +19.1%""",
        "labels": ["translation", "priority:high", "language:dutch", "category:isms", "size:medium"]
    },
    {
        "title": "🇩🇪 German Translation: Complete 18 Critical Discordian ISMS Policy Files (Priority 1)",
        "body": """## 🎯 Objective
Create 18 high-priority Discordian ISMS policy translation files for German (de).

## 📋 Background
German translation is 52.1% complete (49/94 files). Targeting DACH region (Germany, Austria, Switzerland).

## 📊 Current State
- **Language:** German (de)
- **Completion:** 52.1% (49/94 files)
- **Missing:** 18 critical ISMS files
- **Priority:** HIGH

## ✅ Acceptance Criteria

### Files to Create (18 files)
Core ISMS policies for DACH region.

### Technical Requirements
- HTML5 with `lang="de"` attribute
- OpenGraph with `og:locale="de_DE"` and alternates (de_AT, de_CH)
- Complete hreflang tags

### Translation Quality
- Professional German for DACH region
- Technical terminology: ISMS → Informationssicherheitsmanagementsystem

## 🤖 Recommended Agent
**Agent:** @ui-enhancement-specialist

## 📈 Success Metrics
- 18 German ISMS files created
- Translation status updated to 71.3% (67/94 files)

---
**Priority:** HIGH | **Effort:** M (4-6h) | **Impact:** +19.1%""",
        "labels": ["translation", "priority:high", "language:german", "category:isms", "size:medium"]
    },
    {
        "title": "🇯🇵 Japanese Translation: Complete 20 Critical Discordian ISMS Policy Files (Priority 1)",
        "body": """## 🎯 Objective
Create 20 high-priority Discordian ISMS policy translation files for Japanese (ja).

## 📋 Background
Japanese translation is 53.2% complete (50/94 files). Targeting Japanese market where ISO 27001 (JIS Q 27001) is highly valued.

## 📊 Current State
- **Language:** Japanese (ja)
- **Completion:** 53.2% (50/94 files)
- **Missing:** 20 critical ISMS files
- **Priority:** HIGH

## ✅ Acceptance Criteria

### Files to Create (20 files)
Core ISMS policies for Japanese market.

### Technical Requirements
- HTML5 with `lang="ja"` attribute
- Hreflang including ja + ja-JP variants
- OpenGraph with `og:locale="ja_JP"`
- Schema.org with `inLanguage: "ja"`

### Translation Quality
- Professional Japanese for business context
- Technical terminology: ISMS → 情報セキュリティマネジメントシステム
- ISO 27001 → JIS Q 27001 (日本産業規格)

## 🤖 Recommended Agent
**Agent:** @ui-enhancement-specialist

## 📈 Success Metrics
- 20 Japanese ISMS files created
- Translation status updated to 74.5% (70/94 files)

---
**Priority:** HIGH | **Effort:** M (4-6h) | **Impact:** +21.2%""",
        "labels": ["translation", "priority:high", "language:japanese", "category:isms", "size:medium"]
    },
    {
        "title": "🇨🇳 Chinese Translation: Complete 20 Critical Discordian ISMS Policy Files (Priority 1)",
        "body": """## 🎯 Objective
Create 20 high-priority Discordian ISMS policy translation files for Chinese (zh).

## 📋 Background
Chinese translation is 53.2% complete (50/94 files). Targeting mainland China, Hong Kong, Singapore, Taiwan.

## 📊 Current State
- **Language:** Chinese (zh)
- **Completion:** 53.2% (50/94 files)
- **Missing:** 20 critical ISMS files
- **Priority:** HIGH

## ✅ Acceptance Criteria

### Files to Create (20 files)
Core ISMS policies for Chinese-speaking markets.

### Technical Requirements
- HTML5 with `lang="zh"` attribute
- Hreflang including zh + zh-CN + zh-Hans + zh-SG variants
- OpenGraph with `og:locale="zh_CN"` and alternates
- Schema.org with `inLanguage: "zh"`

### Translation Quality
- Professional Simplified Chinese for business
- Technical terminology: ISMS → 信息安全管理体系
- ISO 27001 → GB/T 22080 (国家标准)

## 🤖 Recommended Agent
**Agent:** @ui-enhancement-specialist

## 📈 Success Metrics
- 20 Chinese ISMS files created
- Translation status updated to 74.5% (70/94 files)

---
**Priority:** HIGH | **Effort:** M (4-6h) | **Impact:** +21.2%""",
        "labels": ["translation", "priority:high", "language:chinese", "category:isms", "size:medium"]
    },
    {
        "title": "🇰🇷 Korean Translation: Complete 20 Critical Discordian ISMS Policy Files (Priority 1)",
        "body": """## 🎯 Objective
Create 20 high-priority Discordian ISMS policy translation files for Korean (ko).

## 📋 Background
Korean translation is 53.2% complete (50/94 files). Targeting Korean market where K-ISMS certification is highly valued.

## 📊 Current State
- **Language:** Korean (ko)
- **Completion:** 53.2% (50/94 files)
- **Missing:** 20 critical ISMS files
- **Priority:** HIGH

## ✅ Acceptance Criteria

### Files to Create (20 files)
Core ISMS policies for Korean market.

### Technical Requirements
- HTML5 with `lang="ko"` attribute
- Hreflang including ko + ko-KR variants
- OpenGraph with `og:locale="ko_KR"`
- Schema.org with `inLanguage: "ko"`

### Translation Quality
- Professional Korean for business context
- Technical terminology: ISMS → 정보보호관리체계
- ISO 27001 → K-ISMS (한국정보보호관리체계)

## 🤖 Recommended Agent
**Agent:** @ui-enhancement-specialist

## 📈 Success Metrics
- 20 Korean ISMS files created
- Translation status updated to 74.5% (70/94 files)

---
**Priority:** HIGH | **Effort:** M (4-6h) | **Impact:** +21.2%""",
        "labels": ["translation", "priority:high", "language:korean", "category:isms", "size:medium"]
    },
    {
        "title": "🇩🇰🇫🇮🇳🇴 Nordic Languages: Complete 15 Critical Discordian ISMS Files Each (DA/FI/NO)",
        "body": """## 🎯 Objective
Create 15 high-priority Discordian ISMS policy translation files each for Danish (da), Finnish (fi), and Norwegian (no), totaling 45 files.

## 📋 Background
Nordic languages are substantially complete but missing critical ISMS policies:
- **Danish:** 69.1% complete (65/94 files), 29 missing
- **Finnish:** 69.1% complete (65/94 files), 29 missing
- **Norwegian:** 69.1% complete (65/94 files), 29 missing

## 📊 Current State
- **Languages:** Danish (da), Finnish (fi), Norwegian (no)
- **Priority:** MEDIUM
- **Total files:** 45 (15 per language)

## ✅ Acceptance Criteria

### Files to Create (45 files total: 15 per language)
For each language (da, fi, no):
- AI Policy, Asset Management, Email Security, LLM Security, Mobile Device Management
- Monitoring & Logging, Open Source Policy, Physical Security, Secure Development, Vulnerability Management
- Security Metrics, Security Strategy, Security Training, Stakeholder Management, Supplier Reality

### Technical Requirements
- HTML5 with appropriate `lang` attribute (da/fi/no)
- Complete hreflang tags
- OpenGraph with proper locales (da_DK, fi_FI, nb_NO)

### Translation Quality
- Professional Nordic business language
- Market-specific terminology for each country

## 🤖 Recommended Agent
**Agent:** @ui-enhancement-specialist

## 📈 Success Metrics
- 45 Nordic ISMS files created (15 × 3 languages)
- Translation status updated to 85.1% for each language

---
**Priority:** MEDIUM | **Effort:** L (8-10h) | **Impact:** +15.9% per language""",
        "labels": ["translation", "priority:medium", "language:nordic", "category:isms", "size:large"]
    },
    {
        "title": "🇸🇪 Swedish Translation: Complete Final 12 Discordian ISMS Policy Files (High Priority)",
        "body": """## 🎯 Objective
Create the final 12 Discordian ISMS policy translation files for Swedish (sv).

## 📋 Background
Swedish translation is 77.7% complete (73/94 files), the most complete of all languages. This batch completes the home market translation.

## 📊 Current State
- **Language:** Swedish (sv)
- **Completion:** 77.7% (73/94 files)
- **Missing:** 12 final ISMS files
- **Priority:** HIGH

## ✅ Acceptance Criteria

### Files to Create (12 files)
- Asset Management, LLM Security, Monitoring & Logging
- Security Metrics, Security Strategy, Stakeholder Management
- Supplier Reality, Threat Modeling, CRA Conformity, Disaster Recovery

### Technical Requirements
- HTML5 with `lang="sv"` attribute
- Complete hreflang tags
- OpenGraph with `og:locale="sv_SE"`
- Schema.org with `inLanguage: "sv"`

### Translation Quality
- Professional Swedish for Swedish enterprise market
- Technical terminology: ISMS → Ledningssystem för informationssäkerhet (LIS)

## 🤖 Recommended Agent
**Agent:** @ui-enhancement-specialist

## 📈 Success Metrics
- 12 Swedish ISMS files created
- Translation status updated to 90.4% (85/94 files)

---
**Priority:** HIGH | **Effort:** S (2-3h) | **Impact:** +12.8%""",
        "labels": ["translation", "priority:high", "language:swedish", "category:isms", "size:small"]
    },
    {
        "title": "🇮🇱 Hebrew Translation: Complete 15 Critical Discordian ISMS Policy Files (RTL Priority)",
        "body": """## 🎯 Objective
Create 15 high-priority Discordian ISMS policy translation files for Hebrew (he) with proper RTL support.

## 📋 Background
Hebrew translation is 55.3% complete (52/94 files). This batch focuses on critical ISMS policies with proper RTL layout for the Israeli market.

## 📊 Current State
- **Language:** Hebrew (he)
- **Completion:** 55.3% (52/94 files)
- **Missing:** 15 critical ISMS files
- **Priority:** HIGH

## ✅ Acceptance Criteria

### Files to Create (15 files)
- AI Policy, Asset Management, Compliance, Compliance Frameworks
- Email Security, LLM Security, Mobile Device Management, Monitoring & Logging
- Open Source, Physical Security, Secure Development, Vulnerability Management
- Security Metrics, Security Strategy, Security Training

### Technical Requirements
- HTML5 with `lang="he"` and `dir="rtl"` attributes
- Noto Sans Hebrew font for proper RTL rendering
- Complete hreflang tags
- OpenGraph with `og:locale="he_IL"`
- RTL-compatible CSS layout

### Translation Quality
- Professional Hebrew for Israeli enterprise market
- Technical terminology: ISMS → מערכת ניהול אבטחת מידע
- AI translation acceptable

## 🤖 Recommended Agent
**Agent:** @ui-enhancement-specialist

## 📈 Success Metrics
- 15 Hebrew ISMS files created with proper RTL support
- Translation status updated to 71.3% (67/94 files)

---
**Priority:** HIGH | **Effort:** M (4-6h) | **Impact:** +15.9%""",
        "labels": ["translation", "priority:high", "language:hebrew", "category:isms", "rtl", "size:medium"]
    }
]


def create_github_issue(token, issue_data):
    """Create a single GitHub issue using the REST API."""
    url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }
    
    data = json.dumps(issue_data).encode('utf-8')
    
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            return {
                "success": True,
                "number": result["number"],
                "url": result["html_url"],
                "title": result["title"]
            }
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        return {
            "success": False,
            "error": f"HTTP {e.code}: {e.reason}",
            "details": error_body
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def main():
    """Main function to create all 10 issues."""
    print("=" * 80)
    print("CREATING 10 GITHUB ISSUES FOR TRANSLATION COMPLETION")
    print("=" * 80)
    print()
    
    # Check for GitHub token
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        print("❌ Error: GITHUB_TOKEN or GH_TOKEN environment variable not set")
        print()
        print("To use this script:")
        print("  1. Create a Personal Access Token at https://github.com/settings/tokens")
        print("  2. Grant 'repo' scope (for private repos) or 'public_repo' (for public repos)")
        print("  3. Export the token: export GITHUB_TOKEN=<your_token>")
        print("  4. Run this script: python3 create_translation_issues.py")
        print()
        sys.exit(1)
    
    print(f"📁 Repository: {REPO_OWNER}/{REPO_NAME}")
    print(f"🎯 Creating {len(ISSUES)} issues...")
    print()
    
    results = []
    
    for i, issue_spec in enumerate(ISSUES, 1):
        print(f"[{i}/10] Creating: {issue_spec['title'][:70]}...")
        
        # Prepare issue data for GitHub API
        issue_data = {
            "title": issue_spec["title"],
            "body": issue_spec["body"],
            "labels": issue_spec["labels"]
        }
        
        result = create_github_issue(token, issue_data)
        
        if result["success"]:
            print(f"        ✅ Created issue #{result['number']}")
            print(f"        🔗 {result['url']}")
            results.append(result)
        else:
            print(f"        ❌ Failed: {result.get('error', 'Unknown error')}")
            if result.get('details'):
                print(f"        Details: {result['details'][:200]}")
            results.append(result)
        
        print()
    
    # Summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print()
    
    successful = [r for r in results if r.get("success")]
    failed = [r for r in results if not r.get("success")]
    
    print(f"✅ Successfully created: {len(successful)}/{len(ISSUES)} issues")
    print()
    
    if successful:
        print("Created issues:")
        for r in successful:
            print(f"  #{r['number']}: {r['url']}")
        print()
    
    if failed:
        print(f"❌ Failed to create: {len(failed)}/{len(ISSUES)} issues")
        for r in failed:
            print(f"  - {r.get('error', 'Unknown error')}")
        print()
    
    # Save results to file
    results_file = "issue_creation_results.json"
    with open(results_file, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"📊 Results saved to: {results_file}")
    print()
    
    return 0 if len(failed) == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

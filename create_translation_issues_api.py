#!/usr/bin/env python3
"""
Create 10 translation GitHub issues using GitHub REST API.
This script uses environment variables or GitHub Actions context for authentication.
"""

import os
import sys
import json
import subprocess

def get_github_token():
    """Try to get GitHub token from various sources."""
    # Try environment variables
    token = os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN')
    if token:
        return token
    
    # Try to get from gh CLI auth status
    try:
        result = subprocess.run(
            ['gh', 'auth', 'token'],
            capture_output=True,
            text=True,
            check=False
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except Exception:
        pass
    
    return None

def create_issue_with_gh(title, body, labels):
    """Create issue using gh CLI."""
    try:
        cmd = [
            'gh', 'issue', 'create',
            '--repo', 'Hack23/homepage',
            '--title', title,
            '--body', body,
            '--label', ','.join(labels)
        ]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False
        )
        
        if result.returncode == 0:
            issue_url = result.stdout.strip()
            issue_number = issue_url.split('/')[-1] if issue_url else 'unknown'
            return True, issue_number, issue_url
        else:
            return False, None, result.stderr
            
    except Exception as e:
        return False, None, str(e)

# Define the 10 issues
issues = [
    {
        "title": "Translate Discordian Asset Management & Backup Recovery Policies to All 13 Languages",
        "body": """## 🎯 Objective
Create translation files for Discordian Asset Management and Backup Recovery ISMS policy pages across all 13 supported languages.

## 📊 Current State
- **Source Files:** `discordian-asset-mgmt.html`, `discordian-backup-recovery.html`
- **Missing:** 26 translation files (2 pages × 13 languages)
- **Languages:** ar, zh, da, nl, fi, fr, de, he, ja, ko, no, es, sv

## ✅ Acceptance Criteria
- [ ] Create 26 translation files with proper naming
- [ ] Proper lang attribute for each language
- [ ] RTL support for Arabic/Hebrew (`dir="rtl"`)
- [ ] Complete hreflang tags (14 total)
- [ ] All content translated (AI translation acceptable)
- [ ] Update Translation-Status.md for each language

## 🛠️ Implementation
**Key Terms:**
- Asset Management: 資産管理 (JA), 资产管理 (ZH), 자산 관리 (KO), Vermögensverwaltung (DE), Gestion des actifs (FR)
- Backup Recovery: バックアップ回復 (JA), 备份恢复 (ZH), 백업 복구 (KO)

## 🤖 Recommended Agent
@ui-enhancement-specialist

## 📏 Estimated Effort
8-12 hours""",
        "labels": ["translation", "content", "priority:high", "size:medium", "isms-documentation"]
    },
    {
        "title": "Translate Discordian Business Continuity & Disaster Recovery Policies to All 13 Languages",
        "body": """## 🎯 Objective
Create translation files for Discordian Business Continuity and Disaster Recovery ISMS policy pages across all 13 languages.

## 📊 Current State
- **Source Files:** `discordian-business-continuity.html`, `discordian-disaster-recovery.html`
- **Missing:** 26 translation files

## ✅ Acceptance Criteria
- [ ] 26 files created with proper infrastructure
- [ ] All content translated
- [ ] Status files updated

## 🛠️ Implementation
**Key Terms:**
- Business Continuity: 事業継続 (JA), 业务连续性 (ZH), 비즈니스 연속성 (KO)
- Disaster Recovery: 災害復旧 (JA), 灾难恢复 (ZH), 재해 복구 (KO)

## 🤖 Recommended Agent
@ui-enhancement-specialist

## 📏 Estimated Effort
8-12 hours""",
        "labels": ["translation", "content", "priority:high", "size:medium", "isms-documentation"]
    },
    {
        "title": "Translate Discordian Cloud Security & Monitoring Policies to All 13 Languages",
        "body": """## 🎯 Objective
Create translation files for Discordian Cloud Security and Monitoring/Logging ISMS policy pages across all 13 languages.

## 📊 Current State
- **Source Files:** `discordian-cloud-security.html`, `discordian-monitoring-logging.html`
- **Missing:** 26 translation files

## ✅ Acceptance Criteria
- [ ] 26 files created
- [ ] Infrastructure complete
- [ ] Content translated

## 🛠️ Implementation
**Key Terms:**
- Cloud Security: クラウドセキュリティ (JA), 云安全 (ZH), 클라우드 보안 (KO)
- Monitoring: 監視 (JA), 监控 (ZH), 모니터링 (KO)

## 🤖 Recommended Agent
@ui-enhancement-specialist

## 📏 Estimated Effort
8-12 hours""",
        "labels": ["translation", "content", "priority:high", "size:medium", "isms-documentation"]
    },
    {
        "title": "Translate Discordian Secure Development & Vulnerability Management to All 13 Languages",
        "body": """## 🎯 Objective
Create translation files for Discordian Secure Development and Vulnerability Management policy pages across all 13 languages.

## 📊 Current State
- **Source Files:** `discordian-secure-dev.html`, `discordian-vuln-mgmt.html`
- **Missing:** 26 translation files

## ✅ Acceptance Criteria
- [ ] 26 files created
- [ ] All content translated
- [ ] Status updated

## 🛠️ Implementation
**Key Terms:**
- Secure Development: セキュア開発 (JA), 安全开发 (ZH), 보안 개발 (KO)
- Vulnerability Management: 脆弱性管理 (JA), 漏洞管理 (ZH), 취약점 관리 (KO)

## 🤖 Recommended Agent
@ui-enhancement-specialist

## 📏 Estimated Effort
8-12 hours""",
        "labels": ["translation", "content", "priority:high", "size:medium", "isms-documentation"]
    },
    {
        "title": "Translate Discordian Security Strategy & Metrics to All 13 Languages",
        "body": """## 🎯 Objective
Create translation files for Discordian Security Strategy and Security Metrics policy pages across all 13 languages.

## 📊 Current State
- **Source Files:** `discordian-security-strategy.html`, `discordian-security-metrics.html`
- **Missing:** 26 translation files

## ✅ Acceptance Criteria
- [ ] 26 files created
- [ ] Infrastructure complete
- [ ] Content translated

## 🛠️ Implementation
**Key Terms:**
- Security Strategy: セキュリティ戦略 (JA), 安全策略 (ZH), 보안 전략 (KO)
- Security Metrics: セキュリティ指標 (JA), 安全指标 (ZH), 보안 메트릭 (KO)

## 🤖 Recommended Agent
@ui-enhancement-specialist

## 📏 Estimated Effort
8-12 hours""",
        "labels": ["translation", "content", "priority:high", "size:medium", "isms-documentation"]
    },
    {
        "title": "Translate Discordian Stakeholder Management & Supplier Reality to All 13 Languages",
        "body": """## 🎯 Objective
Create translation files for Discordian Stakeholder Management and Supplier Reality policy pages across all 13 languages.

## 📊 Current State
- **Source Files:** `discordian-stakeholders.html`, `discordian-supplier-reality.html`
- **Missing:** 26 translation files

## ✅ Acceptance Criteria
- [ ] 26 files created
- [ ] Complete metadata
- [ ] Translated content

## 🛠️ Implementation
**Key Terms:**
- Stakeholder Management: ステークホルダー管理 (JA), 利益相关者管理 (ZH), 이해관계자 관리 (KO)

## 🤖 Recommended Agent
@ui-enhancement-specialist

## 📏 Estimated Effort
8-12 hours""",
        "labels": ["translation", "content", "priority:high", "size:medium", "isms-documentation"]
    },
    {
        "title": "Translate Discordian LLM Security & CRA Conformity to All 13 Languages",
        "body": """## 🎯 Objective
Create translation files for Discordian LLM Security and EU Cyber Resilience Act (CRA) Conformity pages across all 13 languages.

## 📊 Current State
- **Source Files:** `discordian-llm-security.html`, `discordian-cra-conformity.html`
- **Missing:** 26 translation files

## ✅ Acceptance Criteria
- [ ] 26 files created
- [ ] Technical infrastructure
- [ ] Content translated

## 🛠️ Implementation
**Key Terms:**
- LLM Security: LLMセキュリティ (JA), LLM安全 (ZH), LLM 보안 (KO)
- CRA: サイバーレジリエンス法 (JA), 网络韧性法 (ZH)

## 🤖 Recommended Agent
@ui-enhancement-specialist

## 📏 Estimated Effort
8-12 hours""",
        "labels": ["translation", "content", "priority:high", "size:medium", "isms-documentation", "emerging-tech"]
    },
    {
        "title": "Translate Core Navigation Page (projects.html) to All 13 Languages",
        "body": """## 🎯 Objective
Create translation files for the core navigation projects.html page across all 13 languages.

## 📋 Background
The projects.html page is a core navigation element. It's missing in ALL languages - CRITICAL priority.

## 📊 Current State
- **Source File:** `projects.html`
- **Missing:** 13 translation files
- **Priority:** CRITICAL

## ✅ Acceptance Criteria
- [ ] Create 13 files: `projects_[lang].html`
- [ ] Proper lang/dir attributes
- [ ] Complete hreflang (14 tags)
- [ ] All project names translated

## 🛠️ Implementation
**Key Terms:**
- Projects: プロジェクト (JA), 项目 (ZH), 프로젝트 (KO)
- Citizen Intelligence Agency: 市民インテリジェンス (JA), 公民情报局 (ZH)

## 🤖 Recommended Agent
@ui-enhancement-specialist

## 📏 Estimated Effort
6-8 hours""",
        "labels": ["translation", "content", "priority:critical", "size:small", "core-navigation"]
    },
    {
        "title": "Complete Discordian AI Policy & Security Training Translations (Remaining Languages)",
        "body": """## 🎯 Objective
Complete remaining translations for Discordian AI Policy and Security Training pages.

## 📊 Current State
- **Source Files:** `discordian-ai-policy.html`, `discordian-security-training.html`
- **Missing:** ~20 files (some languages already exist)

## ✅ Acceptance Criteria
- [ ] Identify missing language files
- [ ] Create remaining translations
- [ ] Update status files

## 🛠️ Implementation
**Key Terms:**
- AI Policy: AIポリシー (JA), AI政策 (ZH), AI 정책 (KO)
- Security Training: セキュリティ訓練 (JA), 安全培训 (ZH)

## 🤖 Recommended Agent
@ui-enhancement-specialist

## 📏 Estimated Effort
6-8 hours""",
        "labels": ["translation", "content", "priority:medium", "size:medium", "isms-documentation"]
    },
    {
        "title": "Complete Discordian Physical Security & Email Security Translations (Remaining Languages)",
        "body": """## 🎯 Objective
Complete remaining translations for Discordian Physical Security and Email Security pages.

## 📊 Current State
- **Source Files:** `discordian-physical-security.html`, `discordian-email-security.html`
- **Missing:** ~20 files (some languages already exist)

## ✅ Acceptance Criteria
- [ ] Identify missing translations
- [ ] Create remaining language files
- [ ] Update Translation-Status.md

## 🛠️ Implementation
**Key Terms:**
- Physical Security: 物理セキュリティ (JA), 物理安全 (ZH), 물리적 보안 (KO)
- Email Security: メールセキュリティ (JA), 电子邮件安全 (ZH)

## 🤖 Recommended Agent
@ui-enhancement-specialist

## 📏 Estimated Effort
6-8 hours""",
        "labels": ["translation", "content", "priority:medium", "size:medium", "isms-documentation"]
    }
]

def main():
    print("=" * 60)
    print("Creating 10 Translation GitHub Issues")
    print("Repository: Hack23/homepage")
    print("=" * 60)
    print()
    
    # Check for token
    token = get_github_token()
    if not token:
        print("❌ No GitHub token found")
        print("   Set GITHUB_TOKEN or GH_TOKEN environment variable")
        print("   Or ensure gh CLI is authenticated")
        return 1
    
    print(f"✓ GitHub token found (length: {len(token)})")
    print()
    
    created = []
    failed = []
    
    for i, issue in enumerate(issues, 1):
        print(f"Creating Issue {i}/10: {issue['title'][:60]}...")
        
        success, issue_num, result = create_issue_with_gh(
            issue['title'],
            issue['body'],
            issue['labels']
        )
        
        if success:
            created.append((i, issue_num, result))
            print(f"  ✅ Created: {result}")
        else:
            failed.append((i, result))
            print(f"  ❌ Failed: {result[:100]}")
        
        print()
    
    print("=" * 60)
    print(f"Summary: {len(created)} created, {len(failed)} failed")
    print("=" * 60)
    
    if created:
        print("\n✅ Successfully created:")
        for i, num, url in created:
            print(f"  Issue {i}: #{num} - {url}")
    
    if failed:
        print("\n❌ Failed:")
        for i, error in failed:
            print(f"  Issue {i}: {error[:100]}")
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main())

#!/bin/bash
# Create 10 translation GitHub issues using curl and GitHub REST API
# This script works with GitHub Actions authentication

set -e

REPO_OWNER="Hack23"
REPO_NAME="homepage"
API_URL="https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/issues"

# Try to get token from environment or GitHub Actions context
if [ -n "$GITHUB_TOKEN" ]; then
    TOKEN="$GITHUB_TOKEN"
elif [ -n "$GH_TOKEN" ]; then
    TOKEN="$GH_TOKEN"
else
    echo "❌ No GitHub token found in GITHUB_TOKEN or GH_TOKEN"
    echo "This script requires authentication to create issues"
    exit 1
fi

echo "============================================================"
echo "Creating 10 Translation GitHub Issues via REST API"
echo "Repository: ${REPO_OWNER}/${REPO_NAME}"
echo "============================================================"
echo ""

create_issue() {
    local title="$1"
    local body="$2"
    local labels="$3"
    
    # Escape body for JSON
    local json_body=$(cat <<EOF
{
  "title": $(echo "$title" | jq -R -s .),
  "body": $(echo "$body" | jq -R -s .),
  "labels": $(echo "$labels" | jq -R -c 'split(",")')
}
EOF
)
    
    response=$(curl -s -w "\n%{http_code}" \
        -X POST \
        -H "Accept: application/vnd.github+json" \
        -H "Authorization: Bearer ${TOKEN}" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        "${API_URL}" \
        -d "$json_body")
    
    http_code=$(echo "$response" | tail -n1)
    response_body=$(echo "$response" | sed '$d')
    
    if [ "$http_code" = "201" ]; then
        issue_number=$(echo "$response_body" | jq -r '.number')
        issue_url=$(echo "$response_body" | jq -r '.html_url')
        echo "✅ Created: Issue #${issue_number} - ${issue_url}"
        return 0
    else
        echo "❌ Failed (HTTP $http_code)"
        echo "$response_body" | jq -r '.message // empty' | head -3
        return 1
    fi
}

# Issue 1
echo "Creating Issue 1/10..."
create_issue \
  "Translate Discordian Asset Management & Backup Recovery Policies to All 13 Languages" \
  "## 🎯 Objective
Create translation files for Discordian Asset Management and Backup Recovery ISMS policy pages across all 13 supported languages.

## 📊 Current State
- **Source Files:** \`discordian-asset-mgmt.html\`, \`discordian-backup-recovery.html\`
- **Missing:** 26 translation files (2 pages × 13 languages)
- **Languages:** ar, zh, da, nl, fi, fr, de, he, ja, ko, no, es, sv

## ✅ Acceptance Criteria
- [ ] Create 26 translation files with proper naming
- [ ] Proper lang attribute for each language
- [ ] RTL support for Arabic/Hebrew (\`dir=\"rtl\"\`)
- [ ] Complete hreflang tags (14 total)
- [ ] All content translated (AI translation acceptable)
- [ ] Update Translation-Status.md for each language

## 🛠️ Implementation
**Files:** \`discordian-asset-mgmt_[lang].html\`, \`discordian-backup-recovery_[lang].html\` (26 total)

**Key Terms:**
- Asset Management: 資産管理 (JA), 资产管理 (ZH), 자산 관리 (KO), Vermögensverwaltung (DE), Gestion des actifs (FR)

## 🤖 Recommended Agent
@ui-enhancement-specialist

## 📏 Estimated Effort
8-12 hours" \
  "translation,content,priority:high,size:medium,isms-documentation"

echo ""

# Issue 2
echo "Creating Issue 2/10..."
create_issue \
  "Translate Discordian Business Continuity & Disaster Recovery Policies to All 13 Languages" \
  "## 🎯 Objective
Create translation files for Discordian Business Continuity and Disaster Recovery ISMS policy pages across all 13 languages.

## 📊 Current State
- **Source Files:** \`discordian-business-continuity.html\`, \`discordian-disaster-recovery.html\`
- **Missing:** 26 translation files

## ✅ Acceptance Criteria
- [ ] 26 files created
- [ ] Complete infrastructure
- [ ] Content translated

## 🛠️ Implementation
**Key Terms:**
- Business Continuity: 事業継続 (JA), 业务连续性 (ZH), 비즈니스 연속성 (KO)

## 🤖 Recommended Agent
@ui-enhancement-specialist

## 📏 Estimated Effort
8-12 hours" \
  "translation,content,priority:high,size:medium,isms-documentation"

echo ""

# Issue 3
echo "Creating Issue 3/10..."
create_issue \
  "Translate Discordian Cloud Security & Monitoring Policies to All 13 Languages" \
  "## 🎯 Objective
Create translation files for Discordian Cloud Security and Monitoring/Logging ISMS policy pages across all 13 languages.

## 📊 Current State
- **Source Files:** \`discordian-cloud-security.html\`, \`discordian-monitoring-logging.html\`
- **Missing:** 26 translation files

## ✅ Acceptance Criteria
- [ ] 26 files created
- [ ] Infrastructure complete

## 🛠️ Implementation
**Key Terms:**
- Cloud Security: クラウドセキュリティ (JA), 云安全 (ZH), 클라우드 보안 (KO)

## 🤖 Recommended Agent
@ui-enhancement-specialist

## 📏 Estimated Effort
8-12 hours" \
  "translation,content,priority:high,size:medium,isms-documentation"

echo ""

# Issue 4
echo "Creating Issue 4/10..."
create_issue \
  "Translate Discordian Secure Development & Vulnerability Management to All 13 Languages" \
  "## 🎯 Objective
Create translation files for Discordian Secure Development and Vulnerability Management policy pages across all 13 languages.

## 📊 Current State
- **Source Files:** \`discordian-secure-dev.html\`, \`discordian-vuln-mgmt.html\`
- **Missing:** 26 translation files

## ✅ Acceptance Criteria
- [ ] 26 files created
- [ ] All content translated

## 🛠️ Implementation
**Key Terms:**
- Secure Development: セキュア開発 (JA), 安全开发 (ZH), 보안 개발 (KO)

## 🤖 Recommended Agent
@ui-enhancement-specialist

## 📏 Estimated Effort
8-12 hours" \
  "translation,content,priority:high,size:medium,isms-documentation"

echo ""

# Issue 5
echo "Creating Issue 5/10..."
create_issue \
  "Translate Discordian Security Strategy & Metrics to All 13 Languages" \
  "## 🎯 Objective
Create translation files for Discordian Security Strategy and Security Metrics policy pages across all 13 languages.

## 📊 Current State
- **Source Files:** \`discordian-security-strategy.html\`, \`discordian-security-metrics.html\`
- **Missing:** 26 translation files

## ✅ Acceptance Criteria
- [ ] 26 files created

## 🛠️ Implementation
**Key Terms:**
- Security Strategy: セキュリティ戦略 (JA), 安全策略 (ZH), 보안 전략 (KO)

## 🤖 Recommended Agent
@ui-enhancement-specialist

## 📏 Estimated Effort
8-12 hours" \
  "translation,content,priority:high,size:medium,isms-documentation"

echo ""

# Issue 6
echo "Creating Issue 6/10..."
create_issue \
  "Translate Discordian Stakeholder Management & Supplier Reality to All 13 Languages" \
  "## 🎯 Objective
Create translation files for Discordian Stakeholder Management and Supplier Reality policy pages across all 13 languages.

## 📊 Current State
- **Source Files:** \`discordian-stakeholders.html\`, \`discordian-supplier-reality.html\`
- **Missing:** 26 translation files

## ✅ Acceptance Criteria
- [ ] 26 files created

## 🛠️ Implementation
**Key Terms:**
- Stakeholder Management: ステークホルダー管理 (JA), 利益相关者管理 (ZH)

## 🤖 Recommended Agent
@ui-enhancement-specialist

## 📏 Estimated Effort
8-12 hours" \
  "translation,content,priority:high,size:medium,isms-documentation"

echo ""

# Issue 7
echo "Creating Issue 7/10..."
create_issue \
  "Translate Discordian LLM Security & CRA Conformity to All 13 Languages" \
  "## 🎯 Objective
Create translation files for Discordian LLM Security and EU Cyber Resilience Act (CRA) Conformity pages across all 13 languages.

## 📊 Current State
- **Source Files:** \`discordian-llm-security.html\`, \`discordian-cra-conformity.html\`
- **Missing:** 26 translation files

## ✅ Acceptance Criteria
- [ ] 26 files created

## 🛠️ Implementation
**Key Terms:**
- LLM Security: LLMセキュリティ (JA), LLM安全 (ZH)

## 🤖 Recommended Agent
@ui-enhancement-specialist

## 📏 Estimated Effort
8-12 hours" \
  "translation,content,priority:high,size:medium,isms-documentation,emerging-tech"

echo ""

# Issue 8
echo "Creating Issue 8/10..."
create_issue \
  "Translate Core Navigation Page (projects.html) to All 13 Languages" \
  "## 🎯 Objective
Create translation files for the core navigation projects.html page across all 13 languages.

## 📋 Background
The projects.html page is a core navigation element - CRITICAL priority.

## 📊 Current State
- **Source File:** \`projects.html\`
- **Missing:** 13 translation files
- **Priority:** CRITICAL

## ✅ Acceptance Criteria
- [ ] Create 13 files: \`projects_[lang].html\`
- [ ] Proper lang/dir attributes
- [ ] Complete hreflang (14 tags)

## 🛠️ Implementation
**Key Terms:**
- Projects: プロジェクト (JA), 项目 (ZH), 프로젝트 (KO)

## 🤖 Recommended Agent
@ui-enhancement-specialist

## 📏 Estimated Effort
6-8 hours" \
  "translation,content,priority:critical,size:small,core-navigation"

echo ""

# Issue 9
echo "Creating Issue 9/10..."
create_issue \
  "Complete Discordian AI Policy & Security Training Translations (Remaining Languages)" \
  "## 🎯 Objective
Complete remaining translations for Discordian AI Policy and Security Training pages.

## 📊 Current State
- **Source Files:** \`discordian-ai-policy.html\`, \`discordian-security-training.html\`
- **Missing:** ~20 files (some languages already exist)

## ✅ Acceptance Criteria
- [ ] Identify missing language files
- [ ] Create remaining translations

## 🛠️ Implementation
**Key Terms:**
- AI Policy: AIポリシー (JA), AI政策 (ZH)

## 🤖 Recommended Agent
@ui-enhancement-specialist

## 📏 Estimated Effort
6-8 hours" \
  "translation,content,priority:medium,size:medium,isms-documentation"

echo ""

# Issue 10
echo "Creating Issue 10/10..."
create_issue \
  "Complete Discordian Physical Security & Email Security Translations (Remaining Languages)" \
  "## 🎯 Objective
Complete remaining translations for Discordian Physical Security and Email Security pages.

## 📊 Current State
- **Source Files:** \`discordian-physical-security.html\`, \`discordian-email-security.html\`
- **Missing:** ~20 files (some languages already exist)

## ✅ Acceptance Criteria
- [ ] Identify missing translations
- [ ] Create remaining language files

## 🛠️ Implementation
**Key Terms:**
- Physical Security: 物理セキュリティ (JA), 物理安全 (ZH)

## 🤖 Recommended Agent
@ui-enhancement-specialist

## 📏 Estimated Effort
6-8 hours" \
  "translation,content,priority:medium,size:medium,isms-documentation"

echo ""
echo "============================================================"
echo "Issue Creation Complete!"
echo "============================================================"

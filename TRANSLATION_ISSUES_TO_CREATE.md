# Translation Issues to Create

## Summary

This document contains 10 detailed GitHub issues for completing translation files across all 13 supported languages.

**Total Impact:** 260+ translation files to be created
**Languages:** Arabic (ar), Chinese (zh), Danish (da), Dutch (nl), Finnish (fi), French (fr), German (de), Hebrew (he), Japanese (ja), Korean (ko), Norwegian (no), Spanish (es), Swedish (sv)

---

## Issue 1: Translate Discordian Asset Management & Backup Recovery Policies to All 13 Languages

**Labels:** `translation`, `content`, `priority:high`, `size:medium`, `isms-documentation`  
**Assignee:** copilot-swe-agent[bot]

### 🎯 Objective
Create translation files for Discordian Asset Management and Backup Recovery ISMS policy pages across all 13 supported languages.

### 📋 Background
These Discordian ISMS policy pages are currently only available in English. To complete our multilingual cybersecurity documentation, we need translations for all 13 languages. The English source files exist with complete HTML infrastructure, SEO metadata, and Schema.org structured data.

### 📊 Current State
- **Source Files:** `discordian-asset-mgmt.html`, `discordian-backup-recovery.html`
- **Missing:** 26 translation files (2 pages × 13 languages)
- **Languages:** Arabic (ar), Chinese (zh), Danish (da), Dutch (nl), Finnish (fi), French (fr), German (de), Hebrew (he), Japanese (ja), Korean (ko), Norwegian (no), Spanish (es), Swedish (sv)
- **Status:** English files exist with complete technical infrastructure

### ✅ Acceptance Criteria
- [ ] Create 26 translation files with proper naming: `discordian-asset-mgmt_[lang].html`, `discordian-backup-recovery_[lang].html`
- [ ] Each file must have proper `lang="[code]"` attribute
- [ ] RTL support for Arabic (`dir="rtl"`) and Hebrew (`dir="rtl"`)
- [ ] Complete hreflang tags for all 14 languages (13 translations + English + x-default)
- [ ] og:locale properly set for each language (e.g., `ar_AR`, `zh_CN`, `sv_SE`)
- [ ] Schema.org `inLanguage` property set correctly
- [ ] Headers, titles, meta descriptions fully translated
- [ ] Navigation breadcrumbs translated
- [ ] All content professionally translated (AI translation acceptable per ui-enhancement-specialist agent)
- [ ] Maintain Discordian voice and FNORD references in translations
- [ ] Update Translation-Status.md for each language after completion

### 🛠️ Implementation Guidance

**Files to Create:** 26 files across 13 languages

**Asset Management translations:**
- `discordian-asset-mgmt_ar.html` (Arabic, RTL)
- `discordian-asset-mgmt_zh.html` (Chinese Simplified)
- `discordian-asset-mgmt_da.html` (Danish)
- `discordian-asset-mgmt_nl.html` (Dutch)
- `discordian-asset-mgmt_fi.html` (Finnish)
- `discordian-asset-mgmt_fr.html` (French)
- `discordian-asset-mgmt_de.html` (German)
- `discordian-asset-mgmt_he.html` (Hebrew, RTL)
- `discordian-asset-mgmt_ja.html` (Japanese)
- `discordian-asset-mgmt_ko.html` (Korean)
- `discordian-asset-mgmt_no.html` (Norwegian)
- `discordian-asset-mgmt_es.html` (Spanish)
- `discordian-asset-mgmt_sv.html` (Swedish)

**Backup Recovery translations:** Same pattern for `discordian-backup-recovery_[lang].html`

**Translation Approach:**
1. Copy English source file structure
2. Update `<html lang="en">` to target language code
3. Add `dir="rtl"` for Arabic and Hebrew
4. Translate all visible text content maintaining Discordian style
5. Update meta tags (title, description, keywords)
6. Translate breadcrumb navigation
7. Update og:locale to match target language
8. Add complete hreflang tags (14 total: 13 languages + English + x-default)
9. Update Schema.org `inLanguage` property
10. Validate HTML structure

**Key Translation Terms:**
- Asset Management: Gestion des actifs (FR), Vermögensverwaltung (DE), 資産管理 (JA), 资产管理 (ZH), 자산 관리 (KO)
- Backup Recovery: Récupération de sauvegarde (FR), Backup-Wiederherstellung (DE), バックアップ回復 (JA), 备份恢复 (ZH), 백업 복구 (KO)
- Shadow IT: IT fantôme (FR), Schatten-IT (DE), シャドーIT (JA), 影子IT (ZH), 섀도우 IT (KO)
- ISMS: Système de gestion de la sécurité de l'information (FR), Informationssicherheits-Managementsystem (DE), 情報セキュリティマネジメントシステム (JA), 信息安全管理系统 (ZH), 정보보안 관리 체계 (KO)

### 📚 Reference Documentation
- English source: `discordian-asset-mgmt.html`, `discordian-backup-recovery.html`
- Translation guides: `[Language]-Translation-Guide.md` (13 files)
- Status files: `[Language]-Translation-Status.md` (13 files)
- Main translation doc: `TRANSLATION_DOCUMENTATION_README.md`
- Agent instructions: `.github/agents/ui-enhancement-specialist.md`

### 🤖 Recommended Agent
**Agent:** @ui-enhancement-specialist  
**Rationale:** Expert in HTML/CSS translations, accessibility (WCAG 2.1 AA), and multilingual website implementation. Authorized to use AI translation for content while maintaining technical infrastructure quality.

For implementation, the UI Enhancement Specialist will:
1. Review English source files for structure and content
2. Create 26 translation files following naming conventions
3. Apply language-specific attributes (lang, dir for RTL)
4. Translate all content using AI translation tools
5. Configure complete hreflang tags
6. Update Schema.org and Open Graph metadata
7. Validate HTML structure and accessibility
8. Update Translation-Status.md files for all 13 languages
9. Test responsive design and RTL layout for Arabic/Hebrew

### 📏 Estimated Effort
**8-12 hours** (26 files, template-based with AI translation assistance)

---

## Issue 2: Translate Discordian Business Continuity & Disaster Recovery Policies to All 13 Languages

**Labels:** `translation`, `content`, `priority:high`, `size:medium`, `isms-documentation`  
**Assignee:** copilot-swe-agent[bot]

### 🎯 Objective
Create translation files for Discordian Business Continuity and Disaster Recovery ISMS policy pages across all 13 supported languages.

### 📋 Background
Business continuity and disaster recovery policies are critical ISMS documentation currently only available in English.

### 📊 Current State
- **Source Files:** `discordian-business-continuity.html`, `discordian-disaster-recovery.html`
- **Missing:** 26 translation files (2 pages × 13 languages)
- **Languages:** ar, zh, da, nl, fi, fr, de, he, ja, ko, no, es, sv

### ✅ Acceptance Criteria
- [ ] Create 26 translation files
- [ ] Proper lang/dir attributes  
- [ ] Complete hreflang tags (14 total)
- [ ] og:locale and Schema.org metadata
- [ ] All content translated
- [ ] Update Translation-Status.md files

### 🛠️ Implementation Guidance
**Files:** `discordian-business-continuity_[lang].html`, `discordian-disaster-recovery_[lang].html` (26 total)

**Key Terms:**
- Business Continuity: 事業継続 (JA), 业务连续性 (ZH), 비즈니스 연속성 (KO), Geschäftskontinuität (DE), Continuité des activités (FR)
- Disaster Recovery: 災害復旧 (JA), 灾难恢复 (ZH), 재해 복구 (KO), Disaster Recovery (DE/FR use English)

### 🤖 Recommended Agent
@ui-enhancement-specialist - Multilingual HTML/CSS expert

### 📏 Estimated Effort
8-12 hours

---

## Issue 3: Translate Discordian Cloud Security & Monitoring Policies to All 13 Languages

**Labels:** `translation`, `content`, `priority:high`, `size:medium`, `isms-documentation`  
**Assignee:** copilot-swe-agent[bot]

### 🎯 Objective
Create translation files for Discordian Cloud Security and Monitoring/Logging ISMS policy pages across all 13 languages.

### 📋 Background
Cloud security and monitoring policies need multilingual support for international audience.

### 📊 Current State
- **Source Files:** `discordian-cloud-security.html`, `discordian-monitoring-logging.html`
- **Missing:** 26 translation files
- **Languages:** ar, zh, da, nl, fi, fr, de, he, ja, ko, no, es, sv

### ✅ Acceptance Criteria
- [ ] 26 translation files created
- [ ] Lang/dir/hreflang configured
- [ ] Metadata translated
- [ ] Update status files

### 🛠️ Implementation Guidance
**Key Terms:**
- Cloud Security: クラウドセキュリティ (JA), 云安全 (ZH), 클라우드 보안 (KO), Cloud-Sicherheit (DE), Sécurité cloud (FR)
- Monitoring: 監視 (JA), 监控 (ZH), 모니터링 (KO), Überwachung (DE), Surveillance (FR)

### 🤖 Recommended Agent
@ui-enhancement-specialist

### 📏 Estimated Effort
8-12 hours

---

## Issue 4: Translate Discordian Secure Development & Vulnerability Management to All 13 Languages

**Labels:** `translation`, `content`, `priority:high`, `size:medium`, `isms-documentation`  
**Assignee:** copilot-swe-agent[bot]

### 🎯 Objective
Create translation files for Discordian Secure Development and Vulnerability Management policy pages across all 13 languages.

### 📋 Background
Secure SDLC and vulnerability management are core security policies requiring multilingual documentation.

### 📊 Current State
- **Source Files:** `discordian-secure-dev.html`, `discordian-vuln-mgmt.html`
- **Missing:** 26 translation files
- **Languages:** ar, zh, da, nl, fi, fr, de, he, ja, ko, no, es, sv

### ✅ Acceptance Criteria
- [ ] 26 translation files
- [ ] Complete infrastructure
- [ ] All content translated
- [ ] Status files updated

### 🛠️ Implementation Guidance
**Key Terms:**
- Secure Development: セキュア開発 (JA), 安全开发 (ZH), 보안 개발 (KO), Sichere Entwicklung (DE), Développement sécurisé (FR)
- Vulnerability Management: 脆弱性管理 (JA), 漏洞管理 (ZH), 취약점 관리 (KO), Schwachstellenmanagement (DE), Gestion des vulnérabilités (FR)

### 🤖 Recommended Agent
@ui-enhancement-specialist

### 📏 Estimated Effort
8-12 hours

---

## Issue 5: Translate Discordian Security Strategy & Metrics to All 13 Languages

**Labels:** `translation`, `content`, `priority:high`, `size:medium`, `isms-documentation`  
**Assignee:** copilot-swe-agent[bot]

### 🎯 Objective
Create translation files for Discordian Security Strategy and Security Metrics policy pages across all 13 languages.

### 📋 Background
Security governance and metrics tracking require multilingual support.

### 📊 Current State
- **Source Files:** `discordian-security-strategy.html`, `discordian-security-metrics.html`
- **Missing:** 26 translation files
- **Languages:** ar, zh, da, nl, fi, fr, de, he, ja, ko, no, es, sv

### ✅ Acceptance Criteria
- [ ] 26 translation files created
- [ ] Infrastructure complete
- [ ] Content translated
- [ ] Status updated

### 🛠️ Implementation Guidance
**Key Terms:**
- Security Strategy: セキュリティ戦略 (JA), 安全策略 (ZH), 보안 전략 (KO), Sicherheitsstrategie (DE), Stratégie de sécurité (FR)
- Security Metrics: セキュリティ指標 (JA), 安全指标 (ZH), 보안 메트릭 (KO), Sicherheitsmetriken (DE), Métriques de sécurité (FR)

### 🤖 Recommended Agent
@ui-enhancement-specialist

### 📏 Estimated Effort
8-12 hours

---

## Issue 6: Translate Discordian Stakeholder Management & Supplier Reality to All 13 Languages

**Labels:** `translation`, `content`, `priority:high`, `size:medium`, `isms-documentation`  
**Assignee:** copilot-swe-agent[bot]

### 🎯 Objective
Create translation files for Discordian Stakeholder Management and Supplier Reality policy pages across all 13 languages.

### 📋 Background
Third-party and stakeholder engagement policies need multilingual support.

### 📊 Current State
- **Source Files:** `discordian-stakeholders.html`, `discordian-supplier-reality.html`
- **Missing:** 26 translation files
- **Languages:** ar, zh, da, nl, fi, fr, de, he, ja, ko, no, es, sv

### ✅ Acceptance Criteria
- [ ] 26 files created
- [ ] Complete metadata
- [ ] Translated content
- [ ] Updated status

### 🛠️ Implementation Guidance
**Key Terms:**
- Stakeholder Management: ステークホルダー管理 (JA), 利益相关者管理 (ZH), 이해관계자 관리 (KO), Stakeholder-Management (DE), Gestion des parties prenantes (FR)
- Third Party: サードパーティ (JA), 第三方 (ZH), 제3자 (KO), Drittanbieter (DE), Tiers (FR)

### 🤖 Recommended Agent
@ui-enhancement-specialist

### 📏 Estimated Effort
8-12 hours

---

## Issue 7: Translate Discordian LLM Security & CRA Conformity to All 13 Languages

**Labels:** `translation`, `content`, `priority:high`, `size:medium`, `isms-documentation`, `emerging-tech`  
**Assignee:** copilot-swe-agent[bot]

### 🎯 Objective
Create translation files for Discordian LLM Security and EU Cyber Resilience Act (CRA) Conformity pages across all 13 languages.

### 📋 Background
Emerging technology (AI/LLM) security and regulatory compliance (EU CRA) documentation.

### 📊 Current State
- **Source Files:** `discordian-llm-security.html`, `discordian-cra-conformity.html`
- **Missing:** 26 translation files
- **Languages:** ar, zh, da, nl, fi, fr, de, he, ja, ko, no, es, sv

### ✅ Acceptance Criteria
- [ ] 26 files created
- [ ] Technical infrastructure
- [ ] Content translated
- [ ] Status updated

### 🛠️ Implementation Guidance
**Key Terms:**
- LLM Security: LLMセキュリティ (JA), LLM安全 (ZH), LLM 보안 (KO), LLM-Sicherheit (DE), Sécurité LLM (FR)
- CRA: サイバーレジリエンス法 (JA), 网络韧性法 (ZH), 사이버 복원력법 (KO), Cyber Resilience Act (DE/FR use English)

### 🤖 Recommended Agent
@ui-enhancement-specialist

### 📏 Estimated Effort
8-12 hours

---

## Issue 8: Translate Core Navigation Page (projects.html) to All 13 Languages

**Labels:** `translation`, `content`, `priority:critical`, `size:small`, `core-navigation`  
**Assignee:** copilot-swe-agent[bot]

### 🎯 Objective
Create translation files for the core navigation projects.html page across all 13 languages.

### 📋 Background
The projects.html page is a core navigation element linking to CIA, Black Trigram, and Compliance Manager. It's missing in ALL languages, making it CRITICAL priority.

### 📊 Current State
- **Source File:** `projects.html`
- **Missing:** 13 translation files
- **Languages:** ar, zh, da, nl, fi, fr, de, he, ja, ko, no, es, sv
- **Priority:** CRITICAL (core navigation)

### ✅ Acceptance Criteria
- [ ] Create 13 translation files: `projects_[lang].html`
- [ ] Proper lang/dir attributes
- [ ] Complete hreflang (14 tags)
- [ ] og:locale per language
- [ ] All project names/descriptions translated
- [ ] Navigation links functional
- [ ] Update Translation-Status.md

### 🛠️ Implementation Guidance
**Files:** `projects_ar.html`, `projects_zh.html`, `projects_da.html`, `projects_nl.html`, `projects_fi.html`, `projects_fr.html`, `projects_de.html`, `projects_he.html`, `projects_ja.html`, `projects_ko.html`, `projects_no.html`, `projects_es.html`, `projects_sv.html`

**Key Terms:**
- Projects: プロジェクト (JA), 项目 (ZH), 프로젝트 (KO), Projekte (DE), Projets (FR), Proyectos (ES), Projecten (NL), Projekter (DA/NO), Projekt (FI/SV)
- Citizen Intelligence Agency: 市民インテリジェンス機関 (JA), 公民情报局 (ZH), 시민 인텔리전스 기관 (KO)
- Black Trigram: ブラックトライグラム (JA), 黑三角 (ZH), 블랙 트라이그램 (KO)
- Compliance Manager: コンプライアンスマネージャー (JA), 合规管理器 (ZH), 컴플라이언스 매니저 (KO)

### 🤖 Recommended Agent
@ui-enhancement-specialist

### 📏 Estimated Effort
6-8 hours

---

## Issue 9: Complete Discordian AI Policy & Security Training Translations (Remaining Languages)

**Labels:** `translation`, `content`, `priority:medium`, `size:medium`, `isms-documentation`  
**Assignee:** copilot-swe-agent[bot]

### 🎯 Objective
Complete remaining translations for Discordian AI Policy and Security Training pages (some languages already exist).

### 📋 Background
These pages have partial translation coverage. Need to complete remaining languages.

### 📊 Current State
- **Source Files:** `discordian-ai-policy.html`, `discordian-security-training.html`
- **Missing:** ~20 files (some languages already have translations)
- **Partially Complete:** Check Translation-Status.md files

### ✅ Acceptance Criteria
- [ ] Identify missing language files
- [ ] Create remaining translations
- [ ] Ensure consistency across all versions
- [ ] Update status files

### 🛠️ Implementation Guidance
**Check existing files first:**
```bash
ls -1 discordian-ai-policy_*.html
ls -1 discordian-security-training_*.html
```

**Create only missing languages**

**Key Terms:**
- AI Policy: AIポリシー (JA), AI政策 (ZH), AI 정책 (KO), KI-Richtlinie (DE), Politique IA (FR)
- Security Training: セキュリティ訓練 (JA), 安全培训 (ZH), 보안 교육 (KO), Sicherheitsschulung (DE), Formation à la sécurité (FR)

### 🤖 Recommended Agent
@ui-enhancement-specialist

### 📏 Estimated Effort
6-8 hours

---

## Issue 10: Complete Discordian Physical Security & Email Security Translations (Remaining Languages)

**Labels:** `translation`, `content`, `priority:medium`, `size:medium`, `isms-documentation`  
**Assignee:** copilot-swe-agent[bot]

### 🎯 Objective
Complete remaining translations for Discordian Physical Security and Email Security pages (some languages already exist).

### 📋 Background
These pages have partial translation coverage. Need to complete remaining languages for full multilingual support.

### 📊 Current State
- **Source Files:** `discordian-physical-security.html`, `discordian-email-security.html`
- **Missing:** ~20 files (some languages already exist)
- **Partially Complete:** Verify existing files

### ✅ Acceptance Criteria
- [ ] Identify missing translations
- [ ] Create remaining language files
- [ ] Consistent quality across versions
- [ ] Update Translation-Status.md

### 🛠️ Implementation Guidance
**Check existing:**
```bash
ls -1 discordian-physical-security_*.html
ls -1 discordian-email-security_*.html
```

**Create missing languages only**

**Key Terms:**
- Physical Security: 物理セキュリティ (JA), 物理安全 (ZH), 물리적 보안 (KO), Physische Sicherheit (DE), Sécurité physique (FR)
- Email Security: メールセキュリティ (JA), 电子邮件安全 (ZH), 이메일 보안 (KO), E-Mail-Sicherheit (DE), Sécurité des e-mails (FR)

### 🤖 Recommended Agent
@ui-enhancement-specialist

### 📏 Estimated Effort
6-8 hours

---

## Summary of All 10 Issues

| Issue # | Title | Files | Priority | Effort |
|---------|-------|-------|----------|--------|
| 1 | Asset Management & Backup Recovery | 26 | HIGH | 8-12h |
| 2 | Business Continuity & Disaster Recovery | 26 | HIGH | 8-12h |
| 3 | Cloud Security & Monitoring | 26 | HIGH | 8-12h |
| 4 | Secure Development & Vulnerability Mgmt | 26 | HIGH | 8-12h |
| 5 | Security Strategy & Metrics | 26 | HIGH | 8-12h |
| 6 | Stakeholder & Supplier Management | 26 | HIGH | 8-12h |
| 7 | LLM Security & CRA Conformity | 26 | HIGH | 8-12h |
| 8 | Core Navigation (projects.html) | 13 | CRITICAL | 6-8h |
| 9 | AI Policy & Security Training (partial) | ~20 | MEDIUM | 6-8h |
| 10 | Physical & Email Security (partial) | ~20 | MEDIUM | 6-8h |

**Total Files to Create:** ~260 translation files  
**Total Estimated Effort:** 70-100 hours across all issues  
**Total Impact:** Complete translation coverage for 13 languages  

## Next Steps

1. Create these 10 issues in the Hack23/homepage repository
2. Assign to copilot-swe-agent[bot] for automated implementation
3. Use @ui-enhancement-specialist agent for all translations
4. Monitor progress through Translation-Status.md files
5. Validate completed translations for quality and consistency

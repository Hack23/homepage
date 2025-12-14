# Japanese Translation Guide

## Overview

This guide provides comprehensive instructions for creating and maintaining Japanese language translations for the Hack23 AB website.

**Language Code:** `ja`  
**Locale:** `ja_JP`  
**Currency:** JPY (¥)  
**Files:** 51 HTML files

## 🎯 Translation Principles

### 1. Professional Tone
- Use formal business register appropriate for cybersecurity consulting
- Technical precision in terminology
- Cultural adaptation for target market

### 2. Technical Consistency
- Keep English terms where widely accepted (CI/CD, DevSecOps, GitHub)
- Use established Japanese cybersecurity terminology
- Maintain consistency across all translated pages

## 📚 Core Terminology

### Navigation Elements

| English | Japanese |
|---------|-------------|
| Home | ホーム |
| Blog | ブログ |
| Services | サービス |
| Products | 製品 |

### Cybersecurity Terms

**ISMS:** 情報セキュリティマネジメントシステム  
**CIA Triad:** CIA三要素  
**Confidentiality:** 機密性  
**Integrity:** 完全性  
**Availability:** 可用性  
**ISO 27001 Local Standard:** JIS Q 27001  
**Compliance:** コンプライアンス  
**Risk Assessment:** リスクアセスメント  


### DevSecOps & Technical Terms

| English | Japanese (JA) |
|---------|---------------|
| DevSecOps | DevSecOps |
| CI/CD | CI/CD |
| Repository | リポジトリ |
| Pipeline | パイプライン |
| Deployment | デプロイ |
| Container | コンテナ |
| Quality Gate | 品質ゲート |
| SAST | SAST (静的解析) |
| DAST | DAST (動的解析) |
| Code Quality | コード品質 |
| Technical Debt | 技術的負債 |
| Security Scanning | セキュリティスキャン |
| Vulnerability Detection | 脆弱性検出 |

### Threat Modeling

| English | Japanese (JA) |
|---------|---------------|
| STRIDE | STRIDE |
| Threat Modeling | 脅威モデリング |
| Attack Surface | 攻撃対象領域 |
| Vulnerability | 脆弱性 |
| Exploit | エクスプロイト |

### Call-to-Action

| English | Japanese |
|---------|-------------|
| Learn More | 詳細を見る |
| Get Started | 始める |
| Contact Us | お問い合わせ |
| Read More | もっと読む |
| Download | ダウンロード |

## 🛠️ HTML Structure

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta property="og:locale" content="ja_JP">
</head>
```

## 🌍 Market Context

**Target Market:** Japanese-speaking regions  
**Regulatory Bodies:** METI, NISC, JIPDEC  
**Currency:** JPY (¥)

## ✅ Translation Workflow

1. **Preparation:** Copy English source, rename with `_ja.html`
2. **Header:** Translate title, meta tags, update og:locale
3. **Schema.org:** Update structured data with Japanese content
4. **Content:** Translate all content maintaining professional tone
5. **Navigation:** Update breadcrumbs, menus, footer
6. **Quality:** Validate HTML, verify hreflang, test links

## 📊 Quality Standards

- Professional Japanese translation
- Technical terminology accuracy
- Proper HTML structure
- Complete hreflang tags
- Schema.org validation
- Native speaker review

## 🔍 Validation

- [ ] HTML validates (W3C)
- [ ] Hreflang tags correct
- [ ] Schema.org valid
- [ ] Grammar reviewed
- [ ] Technical terms verified
- [ ] Links functional
- [ ] Mobile responsive

## 📚 References

**Translation Guide:** `Japanese-Translation-Guide.md`  
**Translation Status:** `Japanese-Translation-Status.md`  
**Example Files:** `index_ja.html`, `services_ja.html`

---

**Created:** December 2025  
**Status:** Active  
**Maintainer:** Hack23 AB Translation Team

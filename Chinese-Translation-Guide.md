# Chinese Translation Guide

## Overview

This guide provides comprehensive instructions for creating and maintaining Chinese language translations for the Hack23 AB website.

**Language Code:** `zh`  
**Locale:** `zh_CN`  
**Currency:** CNY (¥)  
**Files:** 51 HTML files

## 🎯 Translation Principles

### 1. Professional Tone
- Use formal business register appropriate for cybersecurity consulting
- Technical precision in terminology
- Cultural adaptation for target market

### 2. Technical Consistency
- Keep English terms where widely accepted (CI/CD, DevSecOps, GitHub)
- Use established Chinese cybersecurity terminology
- Maintain consistency across all translated pages

## 📚 Core Terminology

### Navigation Elements

| English | Chinese |
|---------|-------------|
| Home | 首页 |
| Blog | 博客 |
| Services | 服务 |
| Products | 产品 |

### Cybersecurity Terms

**ISMS:** 信息安全管理体系  
**CIA Triad:** CIA三元组  
**ISO 27001 Local Standard:** GB/T 22080  


### DevSecOps & Technical Terms

| English | Chinese (ZH) |
|---------|--------------|
| DevSecOps | DevSecOps |
| CI/CD | CI/CD |
| Repository | 代码库 |
| Pipeline | 流水线 |
| Deployment | 部署 |
| Container | 容器 |
| Quality Gate | 质量门 |
| SAST | SAST (静态分析) |
| DAST | DAST (动态分析) |
| Code Quality | 代码质量 |
| Technical Debt | 技术债务 |
| Security Scanning | 安全扫描 |
| Vulnerability Detection | 漏洞检测 |

### Threat Modeling

| English | Chinese (ZH) |
|---------|--------------|
| STRIDE | STRIDE |
| Threat Modeling | 威胁建模 |
| Attack Surface | 攻击面 |
| Vulnerability | 漏洞 |
| Exploit | 利用 |

### Call-to-Action

| English | Chinese |
|---------|-------------|
| Learn More | 了解更多 |
| Get Started | 开始使用 |
| Contact Us | 联系我们 |
| Read More | 阅读更多 |
| Download | 下载 |

## 🛠️ HTML Structure

```html
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta property="og:locale" content="zh_CN">
</head>
```

## 🌍 Market Context

**Target Market:** Chinese-speaking regions  
**Regulatory Bodies:** CNCA, CQC, CAC  
**Currency:** CNY (¥)

## ✅ Translation Workflow

1. **Preparation:** Copy English source, rename with `_zh.html`
2. **Header:** Translate title, meta tags, update og:locale
3. **Schema.org:** Update structured data with Chinese content
4. **Content:** Translate all content maintaining professional tone
5. **Navigation:** Update breadcrumbs, menus, footer
6. **Quality:** Validate HTML, verify hreflang, test links

## 📊 Quality Standards

- Professional Chinese translation
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

**Translation Guide:** `Chinese-Translation-Guide.md`  
**Translation Status:** `Chinese-Translation-Status.md`  
**Example Files:** `index_zh.html`, `services_zh.html`

---

**Created:** December 2025  
**Status:** Active  
**Maintainer:** Hack23 AB Translation Team

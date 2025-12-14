# Korean Translation Guide

## Overview

This guide provides comprehensive instructions for creating and maintaining Korean language translations for the Hack23 AB website.

**Language Code:** `ko`  
**Locale:** `ko_KR`  
**Currency:** KRW (₩)  
**Files:** 51 HTML files

## 🎯 Translation Principles

### 1. Professional Tone
- Use formal business register appropriate for cybersecurity consulting
- Technical precision in terminology
- Cultural adaptation for target market

### 2. Technical Consistency
- Keep English terms where widely accepted (CI/CD, DevSecOps, GitHub)
- Use established Korean cybersecurity terminology
- Maintain consistency across all translated pages

## 📚 Core Terminology

### Navigation Elements

| English | Korean |
|---------|-------------|
| Home | 홈 |
| Blog | 블로그 |
| Services | 서비스 |
| Products | 제품 |

### Cybersecurity Terms

**ISMS:** 정보보안 관리체계  
**CIA Triad:** CIA 3요소  
**Confidentiality:** 기밀성  
**Integrity:** 무결성  
**Availability:** 가용성  
**ISO 27001 Local Standard:** K-ISMS  
**Compliance:** 컴플라이언스  
**Risk Assessment:** 위험 평가  


### DevSecOps & Technical Terms

| English | Korean (KO) |
|---------|-------------|
| DevSecOps | DevSecOps |
| CI/CD | CI/CD |
| Repository | 리포지토리 |
| Pipeline | 파이프라인 |
| Deployment | 배포 |
| Container | 컨테이너 |
| Quality Gate | 품질 게이트 |
| SAST | SAST (정적 분석) |
| DAST | DAST (동적 분석) |
| Code Quality | 코드 품질 |
| Technical Debt | 기술 부채 |
| Security Scanning | 보안 스캔 |
| Vulnerability Detection | 취약점 탐지 |

### Threat Modeling

| English | Korean (KO) |
|---------|-------------|
| STRIDE | STRIDE |
| Threat Modeling | 위협 모델링 |
| Attack Surface | 공격 표면 |
| Vulnerability | 취약점 |
| Exploit | 익스플로잇 |

### Black Trigram - Korean Martial Arts Terms

**Note:** Black Trigram game includes Korean martial arts. Preserve Hangul + romanization + translation:

| Hangul | Romanization | English |
|--------|--------------|---------|
| 무사 | Musa | Traditional Warrior |
| 암살자 | Amsalja | Shadow Assassin |
| 택견 | Taekkyeon | Taekkyeon (UNESCO Heritage) |
| 급소 | Kyusho | Vital Points |

### Call-to-Action

| English | Korean |
|---------|-------------|
| Learn More | 자세히 보기 |
| Get Started | 시작하기 |
| Contact Us | 문의하기 |
| Read More | 더 읽기 |
| Download | 다운로드 |

## 🛠️ HTML Structure

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta property="og:locale" content="ko_KR">
</head>
```

## 🌍 Market Context

**Target Market:** Korean-speaking regions  
**Regulatory Bodies:** KISA, KTI, MSIT  
**Currency:** KRW (₩)

## ✅ Translation Workflow

1. **Preparation:** Copy English source, rename with `_ko.html`
2. **Header:** Translate title, meta tags, update og:locale
3. **Schema.org:** Update structured data with Korean content
4. **Content:** Translate all content maintaining professional tone
5. **Navigation:** Update breadcrumbs, menus, footer
6. **Quality:** Validate HTML, verify hreflang, test links

## 📊 Quality Standards

- Professional Korean translation
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

**Translation Guide:** `Korean-Translation-Guide.md`  
**Translation Status:** `Korean-Translation-Status.md`  
**Example Files:** `index_ko.html`, `services_ko.html`

---

**Created:** December 2025  
**Status:** Active  
**Maintainer:** Hack23 AB Translation Team

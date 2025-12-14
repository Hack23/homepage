# Arabic Translation Guide

## Overview

This guide provides comprehensive instructions for creating and maintaining Arabic language translations for the Hack23 AB website.

**Language Code:** `ar`  
**Direction:** RTL (Right-to-Left)  
**Locale:** `ar_AR` (with regional alternates: ar_SA, ar_EG, ar_AE)  
**Font Family:** 'Noto Sans Arabic', 'Tahoma', 'Arial'

## 🎯 Translation Principles

### 1. RTL (Right-to-Left) Implementation
- All Arabic content must use `dir="rtl"` attribute
- HTML opening tag: `<html lang="ar" dir="rtl">`
- Code blocks and technical snippets remain LTR (Left-to-Right)
- CSS ensures proper directional layout

### 2. Professional Tone
- Use Modern Standard Arabic (MSA) for business content
- Formal register appropriate for cybersecurity consulting
- Technical precision in terminology
- Cultural adaptation for MENA markets

### 3. Technical Consistency
- Keep English terms where widely accepted (CI/CD, DevSecOps, GitHub)
- Use established Arabic cybersecurity terminology
- Maintain consistency across all translated pages

## 📚 Core Terminology Reference

### Cybersecurity Fundamentals

| English | Arabic | Transliteration |
|---------|--------|-----------------|
| Cybersecurity | الأمن السيبراني | Al-Amn Al-Saybāranī |
| Information Security | أمن المعلومات | Amn Al-Ma'lūmāt |
| CIA Triad | ثالوث أمن المعلومات | Thālūth Amn Al-Ma'lūmāt |
| Confidentiality | السرية | Al-Sirriyya |
| Integrity | السلامة | Al-Salāma |
| Availability | التوافر | Al-Tawāfur |
| ISMS | نظام إدارة أمن المعلومات | Niẓām Idārat Amn Al-Ma'lūmāt |
| ISO 27001 | آيزو 27001 | ISO 27001 |
| Compliance | الامتثال | Al-Imtithāl |
| Risk Assessment | تقييم المخاطر | Taqyīm Al-Makhāṭir |

### Technical & Development Terms

| English | Arabic | Notes |
|---------|--------|-------|
| Architecture | هندسة | Handasa |
| Security | الأمن | Al-Amn |
| DevSecOps | DevSecOps | Keep in English |
| CI/CD | CI/CD | Keep in English |
| Repository | مستودع الكود | Mustawda' Al-Kūd |
| Deployment | النشر | Al-Nashr |
| Pipeline | خط الأنابيب | Khaṭ Al-Anābīb |
| OSINT | المعلومات الاستخبارية مفتوحة المصدر | Al-Ma'lūmāt Al-Istikbārāt Maftūḥat Al-Maṣdar |

### Industry-Specific Terms

#### Gaming & Betting
| English | Arabic |
|---------|--------|
| Gaming Operator | مشغل الألعاب |
| Online Casino | كازينو على الإنترنت |
| Betting | المراهنات |
| Gambling License | رخصة المقامرة |

#### Cannabis Security
| English | Arabic |
|---------|--------|
| Cannabis | القنب |
| Dispensary | مستوصف |
| Cultivation | الزراعة |
| Medical Cannabis | القنب الطبي |

#### Investment & Fintech
| English | Arabic |
|---------|--------|
| Investment Firm | شركة استثمارية |
| Financial Services | الخدمات المالية |
| Regulatory Compliance | الامتثال التنظيمي |
| Asset Management | إدارة الأصول |

## 🛠️ HTML Structure Template

### Required Meta Tags
```html
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta property="og:locale" content="ar_AR">
    <meta property="og:locale:alternate" content="ar_SA">
    <meta property="og:locale:alternate" content="ar_EG">
    <meta property="og:locale:alternate" content="ar_AE">
</head>
```

### Hreflang Tags Pattern
Include all supported languages:
```html
<link rel="alternate" hreflang="en" href="https://hack23.com/[page].html">
<link rel="alternate" hreflang="ar" href="https://hack23.com/[page]_ar.html">
<link rel="alternate" hreflang="ar-SA" href="https://hack23.com/[page]_ar.html">
<link rel="alternate" hreflang="ar-EG" href="https://hack23.com/[page]_ar.html">
<link rel="alternate" hreflang="sv" href="https://hack23.com/[page]_sv.html">
<link rel="alternate" hreflang="x-default" href="https://hack23.com/[page].html">
```

### Schema.org Requirements
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "inLanguage": "ar",
  "headline": "[Arabic headline]",
  "description": "[Arabic description]",
  "breadcrumb": {
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "الرئيسية",
        "item": "https://hack23.com/index_ar.html"
      }
    ]
  }
}
```

### Navigation Elements
```html
<!-- Breadcrumb Navigation -->
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="/index_ar.html">الرئيسية</a></li>
    <li class="breadcrumb-item"><a href="/blog_ar.html">مدونة</a></li>
    <li class="breadcrumb-item" aria-current="page">[Page Title]</li>
  </ol>
</nav>

<!-- Header Links -->
<a href="index_ar.html">الرئيسية</a>
<a href="services_ar.html">الخدمات</a>
<a href="blog_ar.html">مدونة</a>
```

## 🎨 CSS Considerations

### RTL-Specific Styling
The website's CSS includes RTL support:
```css
[lang="ar"] {
  direction: rtl;
  text-align: right;
}

/* Code blocks remain LTR */
[lang="ar"] pre,
[lang="ar"] code {
  direction: ltr;
  text-align: left;
}
```

## 🌍 Regional Adaptations

### MENA Market Context
When translating for Arabic markets, consider:
- **Saudi Arabia:** Reference relevant regulators (CITC, SAMA)
- **UAE:** Reference Dubai/Abu Dhabi regulatory frameworks
- **Egypt:** Include Egypt-specific compliance requirements
- **General MENA:** Use neutral Arabic suitable for all regions

### Currency and Pricing
- Default: USD ($)
- Regional: SAR (ر.س), AED (د.إ), EGP (ج.م)
- Format: ١٢٬٣٤٥ د.إ (use Arabic-Indic numerals where appropriate)

## ✅ Translation Workflow

### Step 1: Preparation
1. Copy English source file
2. Rename with `_ar.html` suffix
3. Update `<html lang="ar" dir="rtl">`
4. Add all hreflang tags

### Step 2: Header Translation
1. Translate `<title>` tag
2. Translate meta description and keywords
3. Update og:title, og:description, og:locale
4. Update canonical and alternate links

### Step 3: Schema.org Translation
1. Update headline to Arabic
2. Translate description
3. Set inLanguage to "ar"
4. Update breadcrumb item names

### Step 4: Content Translation
1. Translate main heading `<h1>`
2. Translate all section headings
3. Translate paragraph content
4. **Preserve technical terms in code examples (keep LTR)**
5. Keep URLs unchanged
6. Translate link text but keep href targets
7. Maintain professional tone

### Step 5: Navigation Translation
1. Update breadcrumb navigation (الرئيسية, مدونة, etc.)
2. Translate header menu items
3. Update footer column headings
4. Translate footer navigation links

### Step 6: Quality Checks
1. Validate HTML structure
2. Verify RTL layout displays correctly
3. Check code blocks remain LTR
4. Verify all hreflang tags present
5. Ensure technical terminology consistent
6. Test links functionality
7. Review with native Arabic speaker

## 📊 Quality Standards

### Professional Arabic Translation
- Use Modern Standard Arabic (MSA)
- Formal register for business content
- Technically accurate cybersecurity terminology
- Culturally appropriate for MENA markets

### Technical Accuracy
- Verify Arabic technical terms with industry standards
- Maintain consistency with ISO 27001 Arabic translations
- Keep English terms where industry-standard (CI/CD, GitHub, AWS)

### Accessibility
- Proper ARIA labels in Arabic
- Alt text for images in Arabic
- Semantic HTML structure maintained
- Screen reader compatibility

## 🔍 Testing & Validation

### Browser Testing
- Test RTL layout in Chrome, Firefox, Safari
- Verify mobile responsive design works with RTL
- Check that code blocks remain LTR
- Validate font rendering

### Validation Tools
- W3C HTML Validator
- hreflang tag validation
- Schema.org structured data validator
- Lighthouse accessibility audit

## 📝 Common Translation Patterns

### Navigation Terms
| English | Arabic |
|---------|--------|
| Home | الرئيسية |
| Blog | مدونة |
| Services | الخدمات |
| Products | المنتجات |
| About | حول |
| Contact | اتصل بنا |
| Documentation | الوثائق |
| Features | الميزات |

### Call-to-Action
| English | Arabic |
|---------|--------|
| Learn More | اعرف المزيد |
| Get Started | ابدأ الآن |
| Contact Us | اتصل بنا |
| Read More | اقرأ المزيد |
| Download | تحميل |

## 🎯 Content Types

### Files by Category
- **Homepage:** `index_ar.html`
- **Services:** `services_ar.html`
- **Products:** `cia-project_ar.html`, `compliance-manager_ar.html`, `black-trigram_ar.html`
- **Blog Posts:** `blog-*_ar.html`
- **ISMS Policies:** `discordian-*_ar.html`
- **ISO 27001:** `iso-27001-*_ar.html`
- **Industries:** `industries-*_ar.html`

## 📚 Reference Materials

### Existing Files to Reference
- **Arabic homepage:** `index_ar.html`
- **Arabic services:** `services_ar.html`
- **Arabic ISMS policies:** `discordian-info-sec-policy_ar.html`
- **Arabic blog infrastructure:** `blog-cia-architecture_ar.html`

### External Resources
- **ISO 27001 Arabic terminology:** International standards organizations
- **MENA regulatory terms:** Local regulatory body websites
- **Technical glossaries:** Arabic IT and cybersecurity dictionaries

## 🚀 Deployment

### Pre-Deployment Checklist
- [ ] HTML validates with W3C validator
- [ ] All hreflang tags present and correct
- [ ] RTL layout displays correctly
- [ ] Code blocks remain LTR
- [ ] Schema.org structured data valid
- [ ] Arabic grammar reviewed
- [ ] Technical terms verified
- [ ] Links tested
- [ ] Mobile responsive

---

**Created:** December 2025  
**Status:** Active  
**Maintainer:** Hack23 AB Translation Team

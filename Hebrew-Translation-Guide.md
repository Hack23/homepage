# Hebrew Translation Guide

## Overview

This guide provides comprehensive instructions for creating and maintaining Hebrew language translations for the Hack23 AB website.

**Language Code:** `he`  
**Direction:** RTL (Right-to-Left)  
**Locale:** `he_IL` (Israel)  
**Font Family:** 'Noto Sans Hebrew', 'Arial Hebrew', 'David'

## 🎯 Translation Principles

### 1. RTL (Right-to-Left) Implementation
- All Hebrew content must use `dir="rtl"` attribute
- HTML opening tag: `<html lang="he" dir="rtl">`
- Code blocks and technical snippets remain LTR (Left-to-Right)
- CSS ensures proper directional layout

### 2. Professional Tone
- Use Modern Hebrew for business content
- Formal register appropriate for cybersecurity consulting
- Technical precision in terminology
- Cultural adaptation for Israeli market

### 3. Technical Consistency
- Keep English terms where widely accepted (CI/CD, DevSecOps, GitHub)
- Use established Hebrew cybersecurity terminology
- Maintain consistency across all translated pages

## 📚 Core Terminology Reference

### Cybersecurity Fundamentals

| English | Hebrew | Transliteration |
|---------|--------|-----------------|
| Cybersecurity | אבטחת סייבר | Avtachat Cyber |
| Information Security | אבטחת מידע | Avtachat Meida |
| CIA Triad | משולש CIA | Meshulash CIA |
| Confidentiality | סודיות | Sodiyut |
| Integrity | שלמות | Shlemut |
| Availability | זמינות | Zminut |
| ISMS | מערכת ניהול אבטחת מידע | Ma'arechet Nihul Avtachat Meida |
| ISO 27001 | ISO 27001 | ISO 27001 |
| Compliance | ציות | Tsiyut |
| Risk Assessment | הערכת סיכונים | Ha'arachat Sikunim |

### Technical & Development Terms

| English | Hebrew | Notes |
|---------|--------|-------|
| Architecture | ארכיטקטורה | Architektura |
| Security | אבטחה | Avtacha |
| DevSecOps | DevSecOps | Keep in English |
| CI/CD | CI/CD | Keep in English |
| Repository | מאגר קוד | Ma'agar Kod |
| Deployment | פריסה | Prisa |
| Pipeline | צינור | Tzinor |
| OSINT | מודיעין ממקורות גלויים | Modi'in Mimkorot Gluyim |

### Industry-Specific Terms

#### Gaming & Betting
| English | Hebrew |
|---------|--------|
| Gaming Operator | מפעיל משחקים |
| Online Casino | קזינו מקוון |
| Betting | הימורים |
| Gambling License | רישיון הימורים |

#### Cannabis Security
| English | Hebrew |
|---------|--------|
| Cannabis | קנאביס |
| Dispensary | מרפאה |
| Cultivation | גידול |
| Medical Cannabis | קנאביס רפואי |

#### Investment & Fintech
| English | Hebrew |
|---------|--------|
| Investment Firm | חברת השקעות |
| Financial Services | שירותים פיננסיים |
| Regulatory Compliance | ציות רגולטורי |
| Asset Management | ניהול נכסים |

## 🛠️ HTML Structure Template

### Required Meta Tags
```html
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta property="og:locale" content="he_IL">
</head>
```

### Hreflang Tags Pattern
Include all supported languages:
```html
<link rel="alternate" hreflang="en" href="https://hack23.com/[page].html">
<link rel="alternate" hreflang="he" href="https://hack23.com/[page]_he.html">
<link rel="alternate" hreflang="he-IL" href="https://hack23.com/[page]_he.html">
<link rel="alternate" hreflang="sv" href="https://hack23.com/[page]_sv.html">
<link rel="alternate" hreflang="x-default" href="https://hack23.com/[page].html">
```

### Schema.org Requirements
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "inLanguage": "he",
  "headline": "[Hebrew headline]",
  "description": "[Hebrew description]",
  "breadcrumb": {
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "דף הבית",
        "item": "https://hack23.com/index_he.html"
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
    <li class="breadcrumb-item"><a href="/index_he.html">דף הבית</a></li>
    <li class="breadcrumb-item"><a href="/blog_he.html">בלוג</a></li>
    <li class="breadcrumb-item" aria-current="page">[Page Title]</li>
  </ol>
</nav>

<!-- Header Links -->
<a href="index_he.html">דף הבית</a>
<a href="services_he.html">שירותים</a>
<a href="blog_he.html">בלוג</a>
```

## 🎨 CSS Considerations

### RTL-Specific Styling
The website's CSS includes RTL support:
```css
[lang="he"] {
  direction: rtl;
  text-align: right;
}

/* Code blocks remain LTR */
[lang="he"] pre,
[lang="he"] code {
  direction: ltr;
  text-align: left;
}
```

## 🌍 Regional Adaptations

### Israeli Market Context
When translating for Hebrew/Israeli market, consider:
- **Regulatory Bodies:** Reference Israeli regulators (ISA, Ministry of Finance)
- **Standards:** K-ISMS equivalent or ISO 27001 adoption in Israel
- **Currency:** ILS (₪) - New Israeli Shekel
- **Cultural Context:** Israeli business culture and terminology

### Currency and Pricing
- Currency: ILS (₪)
- Format: ₪12,345 or 12,345 ₪

## ✅ Translation Workflow

### Step 1: Preparation
1. Copy English source file
2. Rename with `_he.html` suffix
3. Update `<html lang="he" dir="rtl">`
4. Add all hreflang tags

### Step 2: Header Translation
1. Translate `<title>` tag
2. Translate meta description and keywords
3. Update og:title, og:description, og:locale
4. Update canonical and alternate links

### Step 3: Schema.org Translation
1. Update headline to Hebrew
2. Translate description
3. Set inLanguage to "he"
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
1. Update breadcrumb navigation (דף הבית, בלוג, etc.)
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
7. Review with native Hebrew speaker

## 📊 Quality Standards

### Professional Hebrew Translation
- Use Modern Hebrew
- Formal register for business content
- Technically accurate cybersecurity terminology
- Culturally appropriate for Israeli market

### Technical Accuracy
- Verify Hebrew technical terms with industry standards
- Maintain consistency with ISO 27001 Hebrew translations
- Keep English terms where industry-standard (CI/CD, GitHub, AWS)

### Accessibility
- Proper ARIA labels in Hebrew
- Alt text for images in Hebrew
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
| English | Hebrew |
|---------|--------|
| Home | דף הבית |
| Blog | בלוג |
| Services | שירותים |
| Products | מוצרים |
| About | אודות |
| Contact | צור קשר |
| Documentation | תיעוד |
| Features | תכונות |

### Call-to-Action
| English | Hebrew |
|---------|--------|
| Learn More | למד עוד |
| Get Started | התחל עכשיו |
| Contact Us | צור קשר |
| Read More | קרא עוד |
| Download | הורד |

## 🎯 Content Types

### Files by Category
- **Homepage:** `index_he.html`
- **Services:** `services_he.html`
- **Products:** `cia-project_he.html`, `compliance-manager_he.html`, `black-trigram_he.html`
- **Blog Posts:** `blog-*_he.html`
- **ISMS Policies:** `discordian-*_he.html`
- **ISO 27001:** `iso-27001-*_he.html`
- **Industries:** `industries-*_he.html`

## 📚 Reference Materials

### Existing Files to Reference
- **Hebrew homepage:** `index_he.html`
- **Hebrew services:** `services_he.html`
- **Hebrew ISMS policies:** `discordian-info-sec-policy_he.html`
- **Hebrew blog infrastructure:** `blog-cia-architecture_he.html`

### External Resources
- **ISO 27001 Hebrew terminology:** Israeli standards organizations
- **Israeli regulatory terms:** Local regulatory body websites
- **Technical glossaries:** Hebrew IT and cybersecurity dictionaries

## 🚀 Deployment

### Pre-Deployment Checklist
- [ ] HTML validates with W3C validator
- [ ] All hreflang tags present and correct
- [ ] RTL layout displays correctly
- [ ] Code blocks remain LTR
- [ ] Schema.org structured data valid
- [ ] Hebrew grammar reviewed
- [ ] Technical terms verified
- [ ] Links tested
- [ ] Mobile responsive

---

**Created:** December 2025  
**Status:** Active  
**Maintainer:** Hack23 AB Translation Team

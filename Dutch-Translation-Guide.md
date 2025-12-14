# Dutch Translation Guide

## Overview

This guide provides comprehensive instructions for creating and maintaining Dutch language translations for the Hack23 AB website.

**Language Code:** `nl`  
**Locale:** `nl_NL`  
**Currency:** EUR (€)  
**Files:** 50 HTML files

## 🎯 Translation Principles

### 1. Professional Tone
- Use formal business register appropriate for cybersecurity consulting
- Technical precision in terminology
- Cultural adaptation for target market

### 2. Technical Consistency
- Keep English terms where widely accepted (CI/CD, DevSecOps, GitHub)
- Use established Dutch cybersecurity terminology
- Maintain consistency across all translated pages

## 📚 Core Terminology

### Navigation Elements

| English | Dutch |
|---------|-------------|
| Home | Home |
| Blog | Blog |
| Services | Diensten |
| Products | Producten |

### Cybersecurity Terms

**ISMS:** Informatiebeveiligingsmanagementsysteem  
**CIA Triad:** BIV-classificatie  
**ISO 27001**  
**GDPR:** AVG

### Call-to-Action

| English | Dutch |
|---------|-------------|
| Learn More | Meer informatie |
| Get Started | Aan de slag |
| Contact Us | Contact |

## 🛠️ HTML Structure

```html
<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta property="og:locale" content="nl_NL">
</head>
```

## 🌍 Market Context

**Target Market:** Dutch-speaking regions  
**Regulatory Bodies:** Autoriteit Persoonsgegevens (AP), NCSC  
**Currency:** EUR (€)

## ✅ Translation Workflow

1. **Preparation:** Copy English source, rename with `_nl.html`
2. **Header:** Translate title, meta tags, update og:locale
3. **Schema.org:** Update structured data with Dutch content
4. **Content:** Translate all content maintaining professional tone
5. **Navigation:** Update breadcrumbs, menus, footer
6. **Quality:** Validate HTML, verify hreflang, test links

## 📊 Quality Standards

- Professional Dutch translation
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

**Translation Guide:** `Dutch-Translation-Guide.md`  
**Translation Status:** `Dutch-Translation-Status.md`  
**Example Files:** `index_nl.html`, `services_nl.html`

---

**Created:** December 2025  
**Status:** Active  
**Maintainer:** Hack23 AB Translation Team

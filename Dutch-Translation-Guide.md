# 🇳🇱 Dutch Translation Guide 🌷

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

| English | Dutch (NL) |
|---------|-----------|
| ISMS | Informatiebeveiligingsmanagementsysteem |
| CIA Triad | BIV-classificatie |
| Confidentiality | Vertrouwelijkheid |
| Integrity | Integriteit |
| Availability | Beschikbaarheid |
| ISO 27001 | ISO 27001 |
| GDPR | AVG |
| NIS2 | NIS 2-richtlijn |
| Compliance | Naleving |
| Risk Assessment | Risicoanalyse |
| Security | Beveiliging |
| Cybersecurity | Cyberbeveiliging |
| Architecture | Architectuur |
| Framework | Raamwerk |

### DevSecOps & Technical Terms

| English | Dutch (NL) |
|---------|-----------|
| DevSecOps | DevSecOps |
| CI/CD | CI/CD |
| Workflow | Workflow |
| Repository | Repository |
| Deployment | Implementatie |
| Pipeline | Pipeline |

### Industry-Specific Terms

#### Gaming/Betting
| English | Dutch (NL) |
|---------|-----------|
| Gaming operator | Speloperator |
| Online casino | Online casino |
| Betting | Weddenschappen |
| Gambling license | Spelvergunning |
| Gaming authority | Kansspelautoriteit |

#### Cannabis Industry
| English | Dutch (NL) |
|---------|-----------|
| Cannabis | Cannabis |
| Dispensary | Verkooppunt/Dispensary |
| Cultivation | Teelt/Kweek |
| Medical cannabis | Medicinale cannabis |
| Seed-to-sale | Van zaad tot verkoop |

#### Investment/Finance
| English | Dutch (NL) |
|---------|-----------|
| Investment firm | Beleggingsonderneming |
| Financial services | Financiële diensten |
| Regulatory compliance | Naleving van regelgeving |
| Asset management | Vermogensbeheer |

### Dutch Regulatory Bodies

| Domain | Regulatory Body |
|--------|-----------------|
| Data Protection | Autoriteit Persoonsgegevens (AP) |
| Cybersecurity | NCSC (National Cyber Security Centre) |
| Gaming | Kansspelautoriteit (KSA) |
| Finance | Autoriteit Financiële Markten (AFM) |
| Health | Inspectie Gezondheidszorg en Jeugd (IGJ) |

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

## 📝 Blog Translation Guidelines

### High-Priority Blog Posts

#### Progress Status
- ✅ `blog-public-isms-benefits_nl.html` - Infrastructure complete, needs content translation
- ✅ `blog-automated-convergence_nl.html` - Infrastructure complete, needs content translation
- ✅ `blog-information-hoarding_nl.html` - Infrastructure complete, needs content translation

All 3 high-priority blog posts have complete technical infrastructure (HTML, hreflang, Schema.org) with translated metadata. Content translation pending professional services.

#### Blog-Specific Terminology

| English | Dutch |
|---------|---------|
| Transparency | Transparantie |
| Competitive Advantage | Concurrentievoordeel |
| Trust | Vertrouwen |
| Verification | Verificatie |
| Automation | Automatisering |
| Convergence | Convergentie |
| Information Hoarding | Informatiehamstering |
| Data Integrity | Data-integriteit |
| Knowledge Sharing | Kennisdeling |

#### Discordian Style Elements

When translating blog posts, preserve these unique stylistic elements:

1. **"23 FNORD 5"** - Keep as-is (signature element)
2. **Law of Fives** - Translate to "Wet van Vijf"
3. **Chapel Perilous** - Keep in English or "Kapel van Gevaar"
4. **Think for yourself** - "Denk voor jezelf"
5. **Question authority** - "Twijfel aan autoriteit"
6. **Hidden wisdom sections** - Maintain class="hidden-wisdom"
7. **FNORD** - Keep as-is (Discordian term)

#### Blog-Specific Guidelines

**blog-public-isms-benefits_nl.html**
- Focus: Transparency as competitive advantage
- Complexity: Medium
- Key Terms: Concurrentievoordeel, Transparantie, Vertrouwen, Verificatie
- Cultural Adaptation: Dutch directness and pragmatic business approach
- Estimated Effort: 6-7 hours

**blog-automated-convergence_nl.html**
- Focus: DevSecOps automation
- Complexity: High (technical)
- Key Terms: Automatisering, Convergentie, CI/CD, DevSecOps
- Cultural Adaptation: Dutch innovation and tech-forward culture
- Estimated Effort: 6-7 hours

**blog-information-hoarding_nl.html**
- Focus: Knowledge sharing vs. hoarding
- Complexity: Medium
- Key Terms: Kennisdeling, Data-integriteit, Organisatiecultuur
- Cultural Adaptation: Dutch openness and collaborative culture
- Estimated Effort: 5-6 hours

#### Translation Workflow for Blogs

**Phase 1: Setup** ✅ (Complete)
- Technical infrastructure created
- Metadata translated
- Hreflang tags in place
- Schema.org structured data configured

**Phase 2: Content Translation** (Pending)
1. Remove translation notice section
2. Translate blog content maintaining:
   - Professional C-suite business tone (direct but professional)
   - Technical accuracy in cybersecurity terms
   - Discordian philosophical voice
   - HTML structure
3. Adapt regulatory references for Dutch market (AP, NCSC, AVG)
4. Keep code examples in English
5. Translate code explanations to Dutch

**Phase 3: Quality Assurance**
- Technical terminology accurate
- Business tone appropriate for Dutch executives
- Discordian style preserved
- HTML structure intact
- Links functional
- Schema.org valid

#### Budget Estimates

| Blog Post | Word Count | Translation Time | QA Time | Total | Cost |
|-----------|------------|------------------|---------|-------|------|
| Public ISMS Benefits | 3,200 | 5-6 hours | 1 hour | 6-7 hours | €540-640 |
| Automated Convergence | 3,000 | 5-6 hours | 1 hour | 6-7 hours | €510-600 |
| Information Hoarding | 2,800 | 4-5 hours | 1 hour | 5-6 hours | €480-560 |

**Total Estimated Effort:** 17-20 hours for professional translation  
**Total Budget Estimate:** €1,530-1,800 (9,000 words × €0.17-0.20/word)

## 📚 References

**Translation Guide:** `Dutch-Translation-Guide.md`  
**Translation Status:** `Dutch-Translation-Status.md`  
**Professional Translation Guide:** `PROFESSIONAL_TRANSLATION_GUIDE.md`  
**Example Files:** `index_nl.html`, `services_nl.html`

---

**Created:** December 2025  
**Status:** Active  
**Maintainer:** Hack23 AB Translation Team

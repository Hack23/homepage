# French Translation Guide

## Overview

This guide provides comprehensive instructions for creating and maintaining French language translations for the Hack23 AB website.

**Language Code:** `fr`  
**Locale:** `fr_FR`  
**Currency:** EUR (€)  
**Files:** 49 HTML files

## 🎯 Translation Principles

### 1. Professional Tone
- Use formal business register appropriate for cybersecurity consulting
- Technical precision in terminology
- Cultural adaptation for target market

### 2. Technical Consistency
- Keep English terms where widely accepted (CI/CD, DevSecOps, GitHub)
- Use established French cybersecurity terminology
- Maintain consistency across all translated pages

## 📚 Core Terminology

### Navigation Elements

| English | French |
|---------|-------------|
| Home | Accueil |
| Blog | Blog |
| Services | Services |
| Products | Produits |

### Cybersecurity Terms

| English | French (FR) |
|---------|-----------|
| ISMS | Système de management de la sécurité de l'information |
| CIA Triad | Triade CIA |
| Confidentiality | Confidentialité |
| Integrity | Intégrité |
| Availability | Disponibilité |
| ISO 27001 | ISO 27001 |
| GDPR | RGPD |
| NIS2 | Directive NIS 2 |
| Compliance | Conformité |
| Risk Assessment | Évaluation des risques |
| Security | Sécurité |
| Cybersecurity | Cybersécurité |
| Architecture | Architecture |
| Framework | Cadre |

### DevSecOps & Technical Terms

| English | French (FR) |
|---------|-----------|
| DevSecOps | DevSecOps |
| CI/CD | CI/CD |
| Workflow | Flux de travail |
| Repository | Dépôt |
| Deployment | Déploiement |
| Pipeline | Pipeline |

### Industry-Specific Terms

#### Gaming/Betting
| English | French (FR) |
|---------|-----------|
| Gaming operator | Opérateur de jeu |
| Online casino | Casino en ligne |
| Betting | Paris |
| Gambling license | Licence de jeu |
| Gaming authority | Autorité des jeux |

#### Cannabis Industry
| English | French (FR) |
|---------|-----------|
| Cannabis | Cannabis |
| Dispensary | Dispensaire |
| Cultivation | Culture |
| Medical cannabis | Cannabis médical |
| Seed-to-sale | De la graine à la vente |

#### Investment/Finance
| English | French (FR) |
|---------|-----------|
| Investment firm | Société d'investissement |
| Financial services | Services financiers |
| Regulatory compliance | Conformité réglementaire |
| Asset management | Gestion d'actifs |

### French Regulatory Bodies

| Domain | Regulatory Body |
|--------|-----------------|
| Data Protection | CNIL (Commission Nationale de l'Informatique et des Libertés) |
| Cybersecurity | ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information) |
| Gaming | ANJ (Autorité Nationale des Jeux) |
| Finance | AMF (Autorité des Marchés Financiers) |
| Health | ANSM (Agence Nationale de Sécurité du Médicament) |

### Call-to-Action

| English | French |
|---------|-------------|
| Learn More | En savoir plus |
| Get Started | Commencer |
| Contact Us | Contact |

## 🛠️ HTML Structure

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta property="og:locale" content="fr_FR">
</head>
```

## 🌍 Market Context

**Target Market:** French-speaking regions  
**Regulatory Bodies:** CNIL, ANSSI  
**Currency:** EUR (€)

## ✅ Translation Workflow

1. **Preparation:** Copy English source, rename with `_fr.html`
2. **Header:** Translate title, meta tags, update og:locale
3. **Schema.org:** Update structured data with French content
4. **Content:** Translate all content maintaining professional tone
5. **Navigation:** Update breadcrumbs, menus, footer
6. **Quality:** Validate HTML, verify hreflang, test links

## 📊 Quality Standards

- Professional French translation
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
- ✅ `blog-public-isms-benefits_fr.html` - Infrastructure complete, needs content translation
- ✅ `blog-automated-convergence_fr.html` - Infrastructure complete, needs content translation
- ✅ `blog-information-hoarding_fr.html` - Infrastructure complete, needs content translation

All 3 high-priority blog posts have complete technical infrastructure (HTML, hreflang, Schema.org) with translated metadata. Content translation pending professional services.

#### Blog-Specific Terminology

| English | French |
|---------|---------|
| Transparency | Transparence |
| Competitive Advantage | Avantage Concurrentiel |
| Trust | Confiance |
| Verification | Vérification |
| Automation | Automatisation |
| Convergence | Convergence |
| Information Hoarding | Accumulation d'Informations |
| Data Integrity | Intégrité des Données |
| Knowledge Sharing | Partage des Connaissances |

#### Discordian Style Elements

When translating blog posts, preserve these unique stylistic elements:

1. **"23 FNORD 5"** - Keep as-is (signature element)
2. **Law of Fives** - Translate to "Loi des Cinq"
3. **Chapel Perilous** - Keep in English or "Chapelle Périlleuse"
4. **Think for yourself** - "Pensez par vous-même"
5. **Question authority** - "Remettez en question l'autorité"
6. **Hidden wisdom sections** - Maintain class="hidden-wisdom"
7. **FNORD** - Keep as-is (Discordian term)

#### Blog-Specific Guidelines

**blog-public-isms-benefits_fr.html**
- Focus: Transparency as competitive advantage
- Complexity: Medium
- Key Terms: Avantage concurrentiel, Transparence, Confiance, Vérification
- Cultural Adaptation: French business formality and intellectual approach
- Estimated Effort: 6-7 hours

**blog-automated-convergence_fr.html**
- Focus: DevSecOps automation
- Complexity: High (technical)
- Key Terms: Automatisation, Convergence, CI/CD, DevSecOps
- Cultural Adaptation: French technical precision and methodology
- Estimated Effort: 6-7 hours

**blog-information-hoarding_fr.html**
- Focus: Knowledge sharing vs. hoarding
- Complexity: Medium
- Key Terms: Partage des connaissances, Intégrité des données, Culture organisationnelle
- Cultural Adaptation: French organizational culture and hierarchy
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
   - Professional C-suite business tone (formal "vous" register)
   - Technical accuracy in cybersecurity terms
   - Discordian philosophical voice
   - HTML structure
3. Adapt regulatory references for French market (CNIL, ANSSI, RGPD)
4. Keep code examples in English
5. Translate code explanations to French

**Phase 3: Quality Assurance**
- Technical terminology accurate
- Business tone appropriate for French executives
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

**Translation Guide:** `French-Translation-Guide.md`  
**Translation Status:** `French-Translation-Status.md`  
**Professional Translation Guide:** `PROFESSIONAL_TRANSLATION_GUIDE.md`  
**Example Files:** `index_fr.html`, `services_fr.html`

---

**Created:** December 2025  
**Status:** Active  
**Maintainer:** Hack23 AB Translation Team

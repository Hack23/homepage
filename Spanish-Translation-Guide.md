# 🇪🇸 Spanish Translation Guide 🎭

## Overview

This guide provides comprehensive instructions for creating and maintaining Spanish language translations for the Hack23 AB website.

**Language Code:** `es`  
**Locale:** `es_ES`  
**Currency:** EUR (€)  
**Files:** 49 HTML files

## 🎯 Translation Principles

### 1. Professional Tone
- Use formal business register appropriate for cybersecurity consulting
- Technical precision in terminology
- Cultural adaptation for target market

### 2. Technical Consistency
- Keep English terms where widely accepted (CI/CD, DevSecOps, GitHub)
- Use established Spanish cybersecurity terminology
- Maintain consistency across all translated pages

## 📚 Core Terminology

### Navigation Elements

| English | Spanish |
|---------|-------------|
| Home | Inicio |
| Blog | Blog |
| Services | Servicios |
| Products | Productos |

### Cybersecurity Terms

| English | Spanish (ES) |
|---------|-----------|
| ISMS | Sistema de gestión de seguridad de la información |
| CIA Triad | Tríada CIA |
| Confidentiality | Confidencialidad |
| Integrity | Integridad |
| Availability | Disponibilidad |
| ISO 27001 | ISO 27001 |
| GDPR | RGPD |
| NIS2 | Directiva NIS 2 |
| Compliance | Cumplimiento |
| Risk Assessment | Evaluación de riesgos |
| Security | Seguridad |
| Cybersecurity | Ciberseguridad |
| Architecture | Arquitectura |
| Framework | Marco |

### DevSecOps & Technical Terms

| English | Spanish (ES) |
|---------|-----------|
| DevSecOps | DevSecOps |
| CI/CD | CI/CD |
| Workflow | Flujo de trabajo |
| Repository | Repositorio |
| Deployment | Despliegue |
| Pipeline | Pipeline/Tubería |

### Industry-Specific Terms

#### Gaming/Betting
| English | Spanish (ES) |
|---------|-----------|
| Gaming operator | Operador de juegos |
| Online casino | Casino en línea |
| Betting | Apuestas |
| Gambling license | Licencia de juego |
| Gaming authority | Autoridad del juego |

#### Cannabis Industry
| English | Spanish (ES) |
|---------|-----------|
| Cannabis | Cannabis |
| Dispensary | Dispensario |
| Cultivation | Cultivo |
| Medical cannabis | Cannabis medicinal |
| Seed-to-sale | De la semilla a la venta |

#### Investment/Finance
| English | Spanish (ES) |
|---------|-----------|
| Investment firm | Empresa de inversión |
| Financial services | Servicios financieros |
| Regulatory compliance | Cumplimiento normativo |
| Asset management | Gestión de activos |

### Spanish Regulatory Bodies

| Domain | Regulatory Body |
|--------|-----------------|
| Data Protection | AEPD (Agencia Española de Protección de Datos) |
| Cybersecurity | CCN-CERT (Centro Criptológico Nacional) |
| Gaming | DGOJ (Dirección General de Ordenación del Juego) |
| Finance | CNMV (Comisión Nacional del Mercado de Valores) |
| Health | AEMPS (Agencia Española de Medicamentos y Productos Sanitarios) |

### Call-to-Action

| English | Spanish |
|---------|-------------|
| Learn More | Saber más |
| Get Started | Empezar |
| Contact Us | Contacto |

## 🛠️ HTML Structure

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta property="og:locale" content="es_ES">
</head>
```

## 🌍 Market Context

**Target Market:** Spanish-speaking regions  
**Regulatory Bodies:** AEPD, CCN-CERT  
**Currency:** EUR (€)

## ✅ Translation Workflow

1. **Preparation:** Copy English source, rename with `_es.html`
2. **Header:** Translate title, meta tags, update og:locale
3. **Schema.org:** Update structured data with Spanish content
4. **Content:** Translate all content maintaining professional tone
5. **Navigation:** Update breadcrumbs, menus, footer
6. **Quality:** Validate HTML, verify hreflang, test links

## 📊 Quality Standards

- Professional Spanish translation
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
- ✅ `blog-public-isms-benefits_es.html` - Infrastructure complete, needs content translation
- ✅ `blog-automated-convergence_es.html` - Infrastructure complete, needs content translation
- ✅ `blog-information-hoarding_es.html` - Infrastructure complete, needs content translation

All 3 high-priority blog posts have complete technical infrastructure (HTML, hreflang, Schema.org) with translated metadata. Content translation pending professional services.

#### Blog-Specific Terminology

| English | Spanish |
|---------|---------|
| Transparency | Transparencia |
| Competitive Advantage | Ventaja Competitiva |
| Trust | Confianza |
| Verification | Verificación |
| Automation | Automatización |
| Convergence | Convergencia |
| Information Hoarding | Acaparamiento de Información |
| Data Integrity | Integridad de Datos |
| Knowledge Sharing | Intercambio de Conocimientos |

#### Discordian Style Elements

When translating blog posts, preserve these unique stylistic elements:

1. **"23 FNORD 5"** - Keep as-is (signature element)
2. **Law of Fives** - Translate to "Ley de los Cincos"
3. **Chapel Perilous** - Keep in English or "Capilla Peligrosa"
4. **Think for yourself** - "Piensa por ti mismo"
5. **Question authority** - "Cuestiona la autoridad"
6. **Hidden wisdom sections** - Maintain class="hidden-wisdom"
7. **FNORD** - Keep as-is (Discordian term)

#### Blog-Specific Guidelines

**blog-public-isms-benefits_es.html**
- Focus: Transparency as competitive advantage
- Complexity: Medium
- Key Terms: Ventaja competitiva, Transparencia, Confianza, Verificación
- Cultural Adaptation: Emphasize Spanish and Latin American business culture
- Estimated Effort: 6-7 hours

**blog-automated-convergence_es.html**
- Focus: DevSecOps automation
- Complexity: High (technical)
- Key Terms: Automatización, Convergencia, CI/CD, DevSecOps
- Cultural Adaptation: Reference European and Latin American tech ecosystems
- Estimated Effort: 6-7 hours

**blog-information-hoarding_es.html**
- Focus: Knowledge sharing vs. hoarding
- Complexity: Medium
- Key Terms: Intercambio de conocimientos, Integridad de datos, Cultura organizacional
- Cultural Adaptation: Consider Spanish communication culture and hierarchy
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
   - Professional C-suite business tone (formal "usted" register)
   - Technical accuracy in cybersecurity terms
   - Discordian philosophical voice
   - HTML structure
3. Adapt regulatory references for Spanish market (AEPD, INCIBE, RGPD)
4. Keep code examples in English
5. Translate code explanations to Spanish

**Phase 3: Quality Assurance**
- Technical terminology accurate
- Business tone appropriate for Spanish executives
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

**Translation Guide:** `Spanish-Translation-Guide.md`  
**Translation Status:** `Spanish-Translation-Status.md`  
**Professional Translation Guide:** `PROFESSIONAL_TRANSLATION_GUIDE.md`  
**Example Files:** `index_es.html`, `services_es.html`

---

**Created:** December 2025  
**Status:** Active  
**Maintainer:** Hack23 AB Translation Team

# Swedish Translation Guide

## Overview

This guide provides comprehensive instructions for creating and maintaining Swedish language translations for the Hack23 AB website.

**Language Code:** `sv`  
**Locale:** `sv_SE`  
**Currency:** SEK (kr)  
**Files:** 74 HTML files

## 🎯 Translation Principles

### 1. Professional Tone
- Use formal business Swedish appropriate for cybersecurity consulting
- Technical precision in terminology
- Natural Swedish flow while maintaining technical accuracy

### 2. Swedish Market Context
- Reference Riksdagen (Swedish Parliament)
- Adapt to Swedish regulatory framework
- Use Swedish examples and context where appropriate

### 3. Technical Consistency
- Keep English terms where widely accepted in Swedish IT (CI/CD, DevSecOps)
- Use established Swedish cybersecurity terminology
- Maintain consistency across all pages

## 📚 Core Terminology

### Navigation Elements

| English | Swedish |
|---------|---------|
| Home | Hem |
| Blog | Blogg |
| Services | Tjänster |
| Products | Produkter |
| Documentation | Dokumentation |
| Features | Funktioner |
| About | Om |
| Contact | Kontakt |

### Cybersecurity Terms

**ISMS:** Ledningssystem för informationssäkerhet / Informationssäkerhetsledningssystem  
**CIA Triad:** CIA-triaden  
**ISO 27001:** ISO 27001 / SS-EN ISO/IEC 27001 (Swedish standard)  
**Confidentiality:** Konfidentialitet  
**Integrity:** Integritet  
**Availability:** Tillgänglighet  
**Compliance:** Efterlevnad  
**Risk Assessment:** Riskbedömning

## 🔐 ISMS Policy Translation Guide

### Core ISMS Terminology

| English | Swedish | Notes |
|---------|---------|-------|
| Information Security Management System (ISMS) | Ledningssystem för informationssäkerhet | ISO 27001 |
| Access Control | Åtkomstkontroll | ISO 27001 A.9 |
| Business Continuity | Verksamhetskontinuitet | ISO 22301 |
| Disaster Recovery | Katastrofåterställning | Part of BC/DR |
| Information Asset Management | Informationstillgångshantering | ISO 27001 A.8 |
| Risk Management | Riskhantering | ISO 27005 |
| Risk Assessment | Riskbedömning | Part of risk management |
| Risk Register | Riskregister | Living document |
| Statement of Applicability (SoA) | Tillämplighetsbeskrivning | ISO 27001 requirement |

### Access Control Terminology

| English | Swedish | Context |
|---------|---------|---------|
| Zero Trust | Zero Trust / Nolltillit | Both acceptable |
| Multi-Factor Authentication (MFA) | Multifaktorautentisering (MFA) | Keep acronym |
| Least Privilege | Minsta behörighet | Security principle |
| Identity-Centric Security | Identitetscentrerad säkerhet | Modern approach |
| Privileged Access | Privilegierad åtkomst | Admin/root access |
| Dormant Accounts | Vilande konton | Inactive accounts |
| Access Matrix | Åtkomstmatris | Permission mapping |
| Role-Based Access Control (RBAC) | Rollbaserad åtkomstkontroll (RBAC) | Keep acronym |
| Session Timeout | Sessionstimeout | Technical term |
| Access Review | Åtkomstgranskning | Periodic review |

### Business Continuity & Disaster Recovery

| English | Swedish | Context |
|---------|---------|---------|
| Business Continuity Plan (BCP) | Verksamhetskontinuitetsplan (BCP) | Keep acronym |
| Recovery Time Objective (RTO) | Återställningstidsmål (RTO) | Technical metric |
| Recovery Point Objective (RPO) | Återställningspunktsmål (RPO) | Technical metric |
| Business Impact Analysis (BIA) | Affärspåverkansanalys (BIA) | Assessment method |
| Crisis Management | Krishantering | Response process |
| Operational Resilience | Operativ resiliens | System capability |
| Chaos Engineering | Kaosteknik | Testing methodology |
| Failover | Failover / Omkoppling | Both acceptable |
| Five-Phase BCP | Femfas-BCP | Process methodology |

### Asset Management Terminology

| English | Swedish | Context |
|---------|---------|---------|
| Configuration Management Database (CMDB) | Konfigurationshanteringsdatabas (CMDB) | Keep acronym |
| Shadow IT | Shadow IT / Icke-sanktionerad IT | Keep English term |
| Asset Inventory | Tillgångsinventering | Catalog of assets |
| Lifecycle Management | Livscykelhantering | Cradle to grave |
| Asset Classification | Tillgångsklassificering | Security tagging |
| Asset Owner | Tillgångsägare | Responsible person |
| Infrastructure Archaeology | Infrastruktur-arkeologi | Discovery process |
| Automated Discovery | Automatisk upptäckt | Tool-based finding |

### Risk Management Terminology

| English | Swedish | Context |
|---------|---------|---------|
| Annual Loss Expectancy (ALE) | Årlig förlustförväntan (ALE) | Quantitative metric |
| Single Loss Expectancy (SLE) | Enskild händelseförlust (SLE) | Impact calculation |
| Annual Rate of Occurrence (ARO) | Årlig förekomstfrekvens (ARO) | Probability metric |
| Threat Actor | Hotaktör | Adversary |
| Vulnerability | Sårbarhet | Weakness |
| Risk Appetite | Riskaptit | Organizational tolerance |
| Risk Tolerance | Risktolerans | Specific threshold |
| Risk Treatment | Riskbehandling | Response strategy |
| Monte Carlo Simulation | Monte Carlo-simulering | Statistical method |
| Confidence Interval | Konfidensintervall | Statistical measure |

### Swedish Regulatory Agencies

| Swedish Name | English | Role |
|--------------|---------|------|
| Myndigheten för samhällsskydd och beredskap (MSB) | Swedish Civil Contingencies Agency | Crisis management, BC/DR |
| Integritetsskyddsmyndigheten (IMY) | Swedish Authority for Privacy Protection | GDPR enforcement |
| Finansinspektionen (FI) | Swedish Financial Supervisory Authority | Financial sector regulation |

### Regulatory Framework

| Regulation | Swedish Context |
|------------|-----------------|
| **GDPR** | GDPR / Dataskyddsförordningen (full Swedish term) |
| **ISO 27001** | ISO 27001 / SS-EN ISO/IEC 27001 (Swedish standard designation) |
| **ISO 22301** | ISO 22301 (Business Continuity - international standard) |
| **ISO 27005** | ISO 27005 (Risk Management - international standard) |
| **NIS2 Directive** | NIS2-direktivet (Network and Information Security) |
| **Bokföringslagen** | Swedish Accounting Act (7-year retention requirement) |

### Swedish Political Terminology

| English | Swedish |
|---------|---------|
| Parliament | Riksdagen |
| Member of Parliament | Riksdagsledamot |
| Committee | Utskott |
| Ministry | Departement |
| Government Agency | Myndighet |
| Election Authority | Valmyndigheten |

### Call-to-Action

| English | Swedish |
|---------|---------|
| Learn More | Läs mer |
| Get Started | Kom igång |
| Contact Us | Kontakta oss |
| Read More | Läs mer |
| Download | Ladda ner |

## 🛠️ HTML Structure

```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta property="og:locale" content="sv_SE">
</head>
```

### Hreflang Tags Pattern

```html
<link rel="alternate" hreflang="en" href="https://hack23.com/[page].html">
<link rel="alternate" hreflang="sv" href="https://hack23.com/[page]_sv.html">
<link rel="alternate" hreflang="sv-SE" href="https://hack23.com/[page]_sv.html">
<link rel="alternate" hreflang="x-default" href="https://hack23.com/[page].html">
```

## 🌍 Market Context

**Target Market:** Sweden  
**Regulatory Bodies:** Integritetsskyddsmyndigheten (IMY), MSB, FRA  
**Standards:** ISO 27001, NIS2, GDPR  
**Currency:** SEK (kr)  
**Parliament:** Riksdagen (349 members, 8 parties)

## ✅ Translation Workflow

1. **Preparation**
   - Copy English source file
   - Rename with `_sv.html` suffix
   - Update `<html lang="sv">`
   - Add hreflang tags

2. **Header Translation**
   - Translate `<title>` tag
   - Translate meta description and keywords
   - Update og:title, og:description, og:locale

3. **Schema.org Translation**
   - Update headline to Swedish
   - Translate description
   - Set `inLanguage: "sv"`
   - Update breadcrumb names (Hem, Blogg, etc.)

4. **Content Translation**
   - Translate all headings and content
   - Maintain professional business tone
   - Keep technical terms appropriate to context
   - Preserve code examples in English

5. **Navigation Translation**
   - Update breadcrumbs (Hem, Blogg, etc.)
   - Translate header menu
   - Update footer links to Swedish versions

6. **Quality Checks**
   - Validate HTML structure
   - Verify all hreflang tags
   - Check Swedish grammar and spelling
   - Test link functionality

## 📊 Quality Standards

### Professional Swedish Translation
- Natural Swedish business language
- Formal register appropriate for cybersecurity
- Technical terminology accurate
- Grammar and spelling correct

### Technical Accuracy
- Verify Swedish technical terms
- Maintain consistency with ISO 27001 Swedish translations
- Keep English terms where industry-standard
- Reference riksdagen.se for government terminology

### Accessibility
- Proper ARIA labels in Swedish
- Alt text for images in Swedish
- Screen reader compatibility

## 🔍 Validation

Pre-deployment checklist:
- [ ] HTML validates (W3C)
- [ ] Hreflang tags correct
- [ ] Schema.org structured data valid
- [ ] Swedish grammar reviewed
- [ ] Technical terms verified
- [ ] Links functional
- [ ] Mobile responsive

## 📚 References

**Translation Status:** `Swedish-Translation-Status.md`  
**Blog Translation Guide:** `SWEDISH_BLOG_TRANSLATION_GUIDE.md`  
**Blog Translation Status:** `SWEDISH_BLOG_TRANSLATION_STATUS.md`  
**Example Files:** `index_sv.html`, `services_sv.html`, `discordian-access-control-policy_sv.html`

## 🎯 Swedish-Specific Content

### Discordian Style Preservation
When translating Discordian content:
- **"23 FNORD 5"** - Keep as-is
- **Law of Fives** - "Femtals Lag"
- **Chapel Perilous** - Keep in English or "Kapellet Perilous"
- **Sacred Geometry** - "Helig geometri"
- **Think for yourself** - "Tänk själv"
- **Question authority** - "Ifrågasätt auktoritet"

### Swedish Political Context
- Reference Riksdagen (349 seats, 4% threshold)
- Mention Swedish parties where relevant
- Use Valmyndigheten for election references
- Reference Swedish media (SVT, SR, DN, SvD) appropriately

---

**Created:** December 2025  
**Status:** Active  
**Maintainer:** Hack23 AB Translation Team

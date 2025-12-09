# Industry Pages Translation Specification

## Overview
Create Dutch, German, French, and Spanish translations of 3 industry-specific cybersecurity pages with market-specific regulatory adaptations.

## Files to Create (12 total)

### Betting & Gaming Industry (4 files)
- `industries-betting-gaming_nl.html` - Dutch/Netherlands
- `industries-betting-gaming_de.html` - German/Germany  
- `industries-betting-gaming_fr.html` - French/France
- `industries-betting-gaming_es.html` - Spanish/Spain

### Cannabis Security (4 files)
- `industries-cannabis-security_nl.html` - Dutch/Netherlands
- `industries-cannabis-security_de.html` - German/Germany
- `industries-cannabis-security_fr.html` - French/France
- `industries-cannabis-security_es.html` - Spanish/Spain

### Investment & FinTech (4 files)
- `industries-investment-fintech_nl.html` - Dutch/Netherlands
- `industries-investment-fintech_de.html` - German/Germany
- `industries-investment-fintech_fr.html` - French/France
- `industries-investment-fintech_es.html` - Spanish/Spain

## Regulatory Adaptations by Market

### Betting & Gaming

**Dutch (NL):**
- Regulatory Authority: Kansspelautoriteit (KSA)
- Key Requirements: ISO 27001 mandatory, CRUKS integration (national self-exclusion register)
- New 2026 Rules: Exit strategy plans, material change notification
- Licensing: €48,000 fee + €50,000 security deposit, 34.2% tax rate

**German (DE):**
- Regulatory Authority: Glücksspielstaatsvertrag (GlüStV) - Interstate Treaty on Gambling
- Focus: Federal state-level compliance, strict advertising restrictions
- ISO Certification Body: DEKRA, TÜV

**French (FR):**
- Regulatory Authority: Autorité Nationale des Jeux (ANJ)
- Focus: Player protection, responsible gambling, advertising controls
- ISO Certification Body: AFNOR Certification

**Spanish (ES):**
- Regulatory Authority: Dirección General de Ordenación del Juego (DGOJ)
- Focus: Strict player protection, self-exclusion register (RGIAJ)
- ISO Certification Body: AENOR

### Cannabis Security

**Dutch (NL):**
- Regulatory Authority: Bureau voor Medicinale Cannabis
- Focus: Medical cannabis program, pharmacy distribution
- Data Protection: AVG (GDPR) compliance critical

**German (DE):**
- Regulatory Authority: BfArM (Bundesinstitut für Arzneimittel und Medizinprodukte)
- Focus: Medical cannabis regulations, prescription requirements
- ISO Certification Body: DEKRA

**French (FR):**
- Regulatory Authority: ANSM (Agence Nationale de Sécurité du Médicament)
- Focus: Medical cannabis pilot program
- ISO Certification Body: AFNOR Certification

**Spanish (ES):**
- Regulatory Authority: AEMPS (Agencia Española de Medicamentos y Productos Sanitarios)
- Focus: Medical cannabis associations, regional regulations
- ISO Certification Body: AENOR

### Investment & FinTech

**Dutch (NL):**
- Regulatory Authorities: AFM (Autoriteit Financiële Markten), DNB (De Nederlandsche Bank)
- Focus: MiFID II, PSD2, DORA compliance
- Payment Systems: iDEAL integration

**German (DE):**
- Regulatory Authority: BaFin (Bundesanstalt für Finanzdienstleistungsaufsicht)
- Focus: Banking regulation, FinTech licensing, payment services
- ISO Certification Body: DEKRA

**French (FR):**
- Regulatory Authorities: AMF (Autorité des Marchés Financiers), ACPR (Autorité de Contrôle Prudentiel et de Résolution)
- Focus: Investment services authorization, payment services
- ISO Certification Body: AFNOR Certification

**Spanish (ES):**
- Regulatory Authority: CNMV (Comisión Nacional del Mercado de Valores)
- Focus: Securities regulation, investment firm licensing
- ISO Certification Body: AENOR

## Translation Guidelines

### Technical Requirements

1. **HTML Structure:**
   - Maintain exact HTML structure from English source
   - Update `lang` attribute: `lang="nl"`, `lang="de"`, `lang="fr"`, `lang="es"`
   - Update `og:locale`: `nl_NL`, `de_DE`, `fr_FR`, `es_ES`

2. **Hreflang Tags (all files):**
   ```html
   <link rel="alternate" hreflang="en" href="https://hack23.com/industries-[industry].html">
   <link rel="alternate" hreflang="nl" href="https://hack23.com/industries-[industry]_nl.html">
   <link rel="alternate" hreflang="de" href="https://hack23.com/industries-[industry]_de.html">
   <link rel="alternate" hreflang="de-DE" href="https://hack23.com/industries-[industry]_de.html">
   <link rel="alternate" hreflang="fr" href="https://hack23.com/industries-[industry]_fr.html">
   <link rel="alternate" hreflang="fr-FR" href="https://hack23.com/industries-[industry]_fr.html">
   <link rel="alternate" hreflang="es" href="https://hack23.com/industries-[industry]_es.html">
   <link rel="alternate" hreflang="es-ES" href="https://hack23.com/industries-[industry]_es.html">
   <link rel="alternate" hreflang="sv" href="https://hack23.com/industries-[industry]_sv.html">
   <link rel="alternate" hreflang="sv-SE" href="https://hack23.com/industries-[industry]_sv.html">
   <link rel="alternate" hreflang="x-default" href="https://hack23.com/industries-[industry].html">
   ```

3. **Schema.org Updates:**
   - Add `"inLanguage": "nl"/"de"/"fr"/"es"` to WebPage
   - Update country names in `areaServed` to include local market
   - Translate service descriptions while maintaining schema structure

4. **Breadcrumb Navigation:**
   - Update links to localized versions: `index_nl.html`, `services_nl.html`, etc.
   - Translate breadcrumb labels

### Content Translation Guidelines

1. **Professional Terminology:**
   - Use industry-standard cybersecurity terms
   - Maintain consistency with existing translated pages
   - Use proper regulatory body official names

2. **Regulatory References:**
   - Replace generic references with market-specific regulatory bodies
   - Include local certification bodies for ISO 27001
   - Add market-specific compliance requirements

3. **Financial Information:**
   - Keep pricing in Euros (€)
   - Add local tax/licensing fee information where applicable

4. **Contact Information:**
   - Maintain English contact info (company based in Sweden)
   - Note "Remote consultancy available" in local language

## Quality Checklist

- [ ] All HTML validates (no syntax errors)
- [ ] Hreflang tags complete and accurate
- [ ] Schema.org structured data includes inLanguage
- [ ] Regulatory body names are official/accurate
- [ ] Professional cybersecurity terminology used
- [ ] Breadcrumb navigation localized
- [ ] Footer links localized where versions exist
- [ ] Meta descriptions translated and compelling
- [ ] FAQ schema localized
- [ ] All internal links point to correct language versions

## ISO 27001 Certification Bodies by Market

- **Netherlands:** BSI, DNV, LRQA, NQA
- **Germany:** DEKRA, TÜV (SÜD, Rheinland, NORD), DQS
- **France:** AFNOR Certification, Bureau Veritas, DEKRA
- **Spain:** AENOR, Bureau Veritas, LGAI, SGS

## Key Terms Translation Reference

### Cybersecurity Terms

| English | Dutch | German | French | Spanish |
|---------|-------|--------|--------|---------|
| Information Security Management System | Informatiebeveiligingsmanagementsysteem | Informationssicherheits-Managementsystem | Système de Management de la Sécurité de l'Information | Sistema de Gestión de Seguridad de la Información |
| Data Protection | Gegevensbescherming | Datenschutz | Protection des données | Protección de datos |
| Cybersecurity | Cyberbeveiliging | Cybersicherheit | Cybersécurité | Ciberseguridad |
| Compliance | Compliance/Naleving | Compliance | Conformité | Cumplimiento |
| Risk Assessment | Risicobeoordeling | Risikobewertung | Évaluation des risques | Evaluación de riesgos |
| Penetration Testing | Penetratietesten | Penetrationstest | Test d'intrusion | Pruebas de penetración |

### Services

| English | Dutch | German | French | Spanish |
|---------|-------|--------|--------|---------|
| Services | Diensten | Dienstleistungen | Services | Servicios |
| Consulting | Consultancy | Beratung | Conseil | Consultoría |
| Implementation | Implementatie | Implementierung | Mise en œuvre | Implementación |
| Audit | Audit | Audit | Audit | Auditoría |
| Training | Training | Schulung | Formation | Formación |

## Implementation Status

- [ ] industries-betting-gaming_nl.html
- [ ] industries-betting-gaming_de.html
- [ ] industries-betting-gaming_fr.html
- [ ] industries-betting-gaming_es.html
- [ ] industries-cannabis-security_nl.html
- [ ] industries-cannabis-security_de.html
- [ ] industries-cannabis-security_fr.html
- [ ] industries-cannabis-security_es.html
- [ ] industries-investment-fintech_nl.html
- [ ] industries-investment-fintech_de.html
- [ ] industries-investment-fintech_fr.html
- [ ] industries-investment-fintech_es.html

---

**Document Version:** 1.0  
**Created:** 2025-01-09  
**Purpose:** Translation specification for Issue #XXX - Batch 3 Industry Pages

# 🇩🇪 German (de) Translation Guide

**Version 5.0 - Comprehensive Hack23 Edition**  
*Last Updated: January 2026*

---

## 📋 Quick Reference

| Attribute | Value |
|-----------|-------|
| **Language Code** | `de` |
| **Locale** | `de_DE` (Germany), `de_AT` (Austria), `de_CH` (Switzerland) |
| **Text Direction** | LTR (Left-to-Right) → |
| **Currency** | EUR (€), CHF (Fr.) |
| **Date Format** | `DD.MM.YYYY` or `1. Januar 2026` |

---

## 🔄 Visual Translation Workflow

```mermaid
graph LR
    A[Datei auswählen] --> B[Terminologie prüfen]
    B --> C[Inhalt übersetzen]
    C --> D[QA-Validierung]
    D --> E{Genehmigt?}
    E -->|Ja| F[Veröffentlichen]
    E -->|Nein| C
```

## 🔄 Quality Standards Pyramid

```mermaid
graph TD
    L1[Basis: Technische Genauigkeit]
    L2[Mitte: Grammatik und Fluss]
    L3[Spitze: Kulturelle Relevanz]
    L1 --> L2 --> L3
```

---

## 📚 Comprehensive Vocabulary Reference

### 🔥 Brand & Key Entities (Never Translate)

| English | German | Notes |
|---------|--------|-------|
| Hack23 | Hack23 | Company name – never translate |
| Hack23 AB | Hack23 AB | Swedish company designation |
| Citizen Intelligence Agency | Citizen Intelligence Agency | Project name – keep English |
| CIA Compliance Manager | CIA Compliance Manager | Product name – keep English |
| Black Trigram | Black Trigram | Game product – keep English |
| 흑괘 | 흑괘 | Korean name for Black Trigram |
| James Pether Sörling | James Pether Sörling | Founder name |
| CISSP | CISSP | Certification |
| CISM | CISM | Certification |
| GitHub | GitHub | Platform name |
| LinkedIn | LinkedIn | Platform name |

### 🏢 Hack23 Business & Services

| English | German | Notes |
|---------|--------|-------|
| Cybersecurity Consulting Sweden | Cybersicherheitsberatung in Schweden | Main tagline |
| Public ISMS | Öffentliches ISMS | Core differentiator |
| Security Architecture | Sicherheitsarchitektur | |
| Security Strategy | Sicherheitsstrategie | |
| Cloud Security | Cloud-Sicherheit | |
| DevSecOps | DevSecOps | Keep English |
| Secure Development | Sichere Entwicklung | |
| Code Quality | Codequalität | |
| Compliance & Regulatory | Compliance und Regulierung | |
| Open Source Security | Open-Source-Sicherheit | |
| Security Culture | Sicherheitskultur | |
| Security Training | Sicherheitsschulung | |
| Full-Stack Security | Full-Stack-Sicherheit | |
| Current Practitioner | Aktiver Praktiker | Value proposition |
| Transparent Security | Transparente Sicherheit | |
| Developer-Friendly Security | Entwicklerfreundliche Sicherheit | |
| OSPO | OSPO | Open Source Program Office |
| Gothenburg | Göteborg | City in Sweden |
| Sweden | Schweden | |

### 🎮 Black Trigram Game Vocabulary

| English | German | Notes |
|---------|--------|-------|
| Precision Combat Simulator | Präzisionskampfsimulator | |
| Vital Points | Vitalpunkte | |
| 70 Anatomical Vital Points | 70 anatomische Vitalpunkte | |
| Fighter Archetypes | Kämpferarchetypen | |
| Musa (Warrior) | Musa (Krieger) | |
| Amsalja (Assassin) | Amsalja (Assassine) | |
| Hacker | Hacker | |
| Jeongbo (Intelligence) | Jeongbo (Geheimdienst) | |
| Jojik (Organization) | Jojik (Organisation) | |
| Korean Martial Arts | Koreanische Kampfkünste | |
| Taekkyeon | Taekkyeon | Korean martial art |
| Hapkido | Hapkido | Korean martial art |
| Cultural Preservation | Kulturelle Bewahrung | |
| Educational Gaming | Lernspiele | |
| Unity Game | Unity-Spiel | |
| Steam | Steam | Platform name |
| itch.io | itch.io | Platform name |

### 🔍 Citizen Intelligence Agency Vocabulary

| English | German | Notes |
|---------|--------|-------|
| Political Transparency | Politische Transparenz | |
| OSINT Platform | OSINT-Plattform | |
| Parliamentary Monitoring | Parlamentsüberwachung | |
| Voting Records | Abstimmungsprotokolle | |
| Accountability Metrics | Rechenschaftsmetriken | |
| Open Data | Offene Daten | |
| Civic Technology | Bürgertechnologie | |
| Swedish Parliament | Schwedisches Parlament | |
| Data Visualization | Datenvisualisierung | |
| Political Analytics | Politische Analytik | |

### 🔐 CIA Compliance Manager Vocabulary

| English | German | Notes |
|---------|--------|-------|
| Security Assessment Platform | Sicherheitsbewertungsplattform | |
| Business Impact Analysis | Geschäftsauswirkungsanalyse | |
| Multi-Framework Compliance | Multi-Framework-Compliance | |
| STRIDE Analysis | STRIDE-Analyse | Threat model |
| Threat Modeling | Bedrohungsmodellierung | |
| Evidence Collection | Beweissammlung | |
| Automated Compliance Reporting | Automatisierte Compliance-Berichterstattung | |
| Risk Register | Risikoregister | |
| Controls Monitoring | Kontrollüberwachung | |
| CRA Assessment | CRA-Bewertung | Cyber Resilience Act |

### 🍎 Discordian Philosophy & ISMS Blog

| English | German | Notes |
|---------|--------|-------|
| Think for Yourself | Denk selbst | Core motto |
| Question Authority | Hinterfrage Autorität | |
| FNORD | FNORD | Never translate |
| Nothing is True | Nichts ist wahr | |
| Everything is Permitted | Alles ist erlaubt | |
| Security Theater | Sicherheitstheater | Fake security |
| Radical Transparency | Radikale Transparenz | |
| Chapel Perilous | Gefährliche Kapelle | Keep English or translate |
| Operation Mindfuck | Operation Mindfuck | Keep English |
| Illuminatus Trilogy | Illuminatus-Trilogie | |
| Eris | Eris | Goddess of Chaos |
| Discordia | Discordia | |
| Law of Fives | Gesetz der Fünf | |
| Sacred Geometry | Heilige Geometrie | |
| Five-Layer Architecture | Fünfschichtige Architektur | |
| Nation-State Surveillance | Staatliche Überwachung | |
| Crypto Backdoors | Krypto-Hintertüren | |
| Security Through Obscurity | Sicherheit durch Unklarheit | Anti-pattern |
| Information Hoarding | Informationshortung | |
| Knowledge Transparency | Wissenstransparenz | |
| Simon Moon | Simon Moon | Character reference |
| Hagbard Celine | Hagbard Celine | Character reference |
| George Dorn | George Dorn | Character reference |

### 🧭 Navigation & UI Elements

| English | German |
|---------|--------|
| Home | Startseite |
| About Us | Über uns |
| Services | Dienstleistungen |
| Products | Produkte |
| Projects | Projekte |
| Contact | Kontakt |
| Blog | Blog |
| Search | Suche |
| Menu | Menü |
| Close | Schließen |
| Back | Zurück |
| Next | Weiter |
| Previous | Zurück |
| Submit | Absenden |
| Cancel | Abbrechen |
| **Expand All** | **Alle erweitern** |
| **Collapse All** | **Alle einklappen** |
| Download | Herunterladen |
| Read More | Mehr erfahren |
| View Details | Details anzeigen |
| Privacy Policy | Datenschutzrichtlinie |
| Terms of Service | Nutzungsbedingungen |
| Copyright | Urheberrecht |
| Sitemap | Sitemap |
| FAQ | FAQ / Häufige Fragen |
| Why Hack23 | Warum Hack23 |
| Accessibility Statement | Barrierefreiheitserklärung |
| Language | Sprache |
| Share | Teilen |
| Print | Drucken |
| Save | Speichern |
| Edit | Bearbeiten |
| Delete | Löschen |
| Confirm | Bestätigen |
| Loading | Wird geladen |
| Error | Fehler |
| Success | Erfolg |
| Warning | Warnung |

### 🔐 CIA Triad & Core Security Principles

| English | German | Notes |
|---------|--------|-------|
| CIA Triad | CIA-Dreiklang | |
| CIA+ Framework | CIA+-Framework | Extended framework |
| **Confidentiality** | **Vertraulichkeit** | Data protection |
| **Integrity** | **Integrität** | Data accuracy |
| **Availability** | **Verfügbarkeit** | System uptime |
| Non-Repudiation | Nichtabstreitbarkeit | |
| Authentication | Authentifizierung | |
| Authorization | Autorisierung | |

### 🔒 Security & Cybersecurity Terminology

| English | German | Notes |
|---------|--------|-------|
| Cybersecurity | Cybersicherheit | |
| Information Security | Informationssicherheit | |
| ISMS | Informationssicherheits-Managementsystem | |
| Security Policy | Sicherheitsrichtlinie | |
| Risk Management | Risikomanagement | |
| Risk Assessment | Risikobewertung | |
| Threat | Bedrohung | |
| Vulnerability | Schwachstelle | |
| Exploit | Exploit | |
| Patch | Patch / Sicherheitsupdate | |
| Firewall | Firewall | |
| Encryption | Verschlüsselung | |
| Decryption | Entschlüsselung | |
| Access Control | Zugriffskontrolle | |
| Multi-Factor Authentication (MFA) | Multi-Faktor-Authentifizierung | |
| Single Sign-On (SSO) | Single Sign-On | |
| Phishing | Phishing | |
| Ransomware | Ransomware / Erpressungstrojaner | |
| Malware | Schadsoftware | |
| Zero Trust | Zero Trust | |
| Defense in Depth | Verteidigung in der Tiefe | |
| Least Privilege | Minimale Rechte | |
| Incident Response | Incident Response | |
| Data Breach | Datenschutzverletzung | |
| Penetration Test | Penetrationstest | |
| Audit | Audit | |
| Compliance | Compliance | |
| Governance | Governance | |
| Security Awareness | Sicherheitsbewusstsein | |
| Backup | Backup / Datensicherung | |
| Disaster Recovery | Notfallwiederherstellung | |
| Business Continuity | Geschäftskontinuität | |
| Supply Chain Security | Lieferkettensicherheit | |
| SLSA Level 3 | SLSA Stufe 3 | Supply chain security |
| Container Security | Container-Sicherheit | |
| Serverless Security | Serverless-Sicherheit | |
| API Security | API-Sicherheit | |
| Endpoint Security | Endpunktsicherheit | |

### 🏛️ Regulatory & Standards

| English | German | Notes |
|---------|--------|-------|
| ISO 27001 | ISO 27001 | Keep as-is |
| ISO 27001:2022 | ISO 27001:2022 | |
| GDPR | DSGVO (Datenschutz-Grundverordnung) | EU regulation |
| NIS2 | NIS2-Richtlinie | EU directive |
| NIST CSF | NIST CSF | |
| CIS Controls | CIS Controls | |
| SOC2 | SOC2 | |
| HIPAA | HIPAA | US healthcare |
| EU Cyber Resilience Act (CRA) | EU Cyber Resilience Act | |
| Annex A Controls | Anhang-A-Kontrollen | ISO 27001 |
| Statement of Applicability | Erklärung zur Anwendbarkeit | |
| BSI | BSI (Bundesamt für Sicherheit in der Informationstechnik) | German regulator |

### 💼 Business & Professional Terms

| English | German |
|---------|--------|
| Consulting | Beratung |
| Enterprise | Unternehmen |
| Strategy | Strategie |
| Certification | Zertifizierung |
| Assessment | Bewertung |
| Implementation | Implementierung |
| Audit | Audit |
| Review | Überprüfung |
| Gap Analysis | Gap-Analyse |
| Roadmap | Roadmap |
| Best Practices | Best Practices |
| Case Study | Fallstudie |
| ROI | ROI |
| KPI | KPI |
| SLA | SLA |
| Stakeholder | Interessengruppe |
| Deliverable | Liefergegenstand |
| Milestone | Meilenstein |

### 📝 Blog Post Categories

| English | German |
|---------|--------|
| Security Architecture | Sicherheitsarchitektur |
| ISMS Policies | ISMS-Richtlinien |
| Compliance Frameworks | Compliance-Frameworks |
| Threat Modeling | Bedrohungsmodellierung |
| Secure Development | Sichere Entwicklung |
| Cloud Security | Cloud-Sicherheit |
| Access Control | Zugriffskontrolle |
| Cryptography | Kryptographie |
| Incident Response | Incident Response |
| Vulnerability Management | Schwachstellenmanagement |
| Asset Management | Asset-Management |
| Network Security | Netzwerksicherheit |
| Email Security | E-Mail-Sicherheit |
| Physical Security | Physische Sicherheit |
| Mobile Device Security | Mobilgerätesicherheit |
| Remote Access Security | Fernzugriffssicherheit |
| Monitoring & Logging | Überwachung und Protokollierung |
| Security Metrics | Sicherheitsmetriken |
| Third Party Risk | Drittanbieterrisiko |
| Change Management | Änderungsmanagement |

### 🏭 Industry-Specific Terms

| English | German |
|---------|--------|
| Investment & FinTech | Investition und FinTech |
| Betting & Gaming | Wetten und Gaming |
| Cannabis Security | Cannabis-Sicherheit |
| Healthcare | Gesundheitswesen |
| Government | Öffentlicher Sektor |
| Critical Infrastructure | Kritische Infrastruktur |
| Financial Services | Finanzdienstleistungen |
| E-commerce | E-Commerce |

---

## ✅ Translation Checklist

- [ ] `<html lang="de">` attribute set
- [ ] `<title>` translated
- [ ] `<meta name="description">` translated
- [ ] `og:locale` set to `de_DE`
- [ ] All hreflang tags present (14 languages)
- [ ] Navigation menu translated
- [ ] Footer translated
- [ ] Brand names kept in English
- [ ] German compound words formed correctly
- [ ] Noun capitalization correct (all nouns capitalized)
- [ ] Umlauts used correctly (ä, ö, ü, ß)

---

## 📝 Notes

- Use **formal German** (Sie form)
- DSGVO is the German term for GDPR
- BSI is the German cybersecurity authority
- All nouns are capitalized in German
- Compound words are common and written together

---

*23 FNORD 5*

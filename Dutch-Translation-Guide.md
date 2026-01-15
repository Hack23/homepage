# 🇳🇱 Dutch (nl) Translation Guide

**Version 6.0 - Expanded Hack23 Edition**  
*Last Updated: January 2026*

---

## 📋 Quick Reference

| Attribute | Value |
|-----------|-------|
| **Language Code** | `nl` |
| **Locale** | `nl_NL` (Netherlands), `nl_BE` (Belgium) |
| **Text Direction** | LTR (Left-to-Right) → |
| **Currency** | EUR (€) |
| **Date Format** | `DD-MM-YYYY` or `1 januari 2026` |

---

## 🔄 Visual Translation Workflow

```mermaid
graph LR
    A[Selecteer bestand] --> B[Bekijk terminologie]
    B --> C[Vertaal inhoud]
    C --> D[QA-validatie]
    D --> E{Goedgekeurd?}
    E -->|Ja| F[Publiceer]
    E -->|Nee| C
```

## 🔄 Quality Standards Pyramid

```mermaid
graph TD
    L1[Basis: Technische nauwkeurigheid]
    L2[Midden: Grammatica en vloeiendheid]
    L3[Top: Culturele relevantie]
    L1 --> L2 --> L3
```

---

## 📚 Comprehensive Vocabulary Reference

### 🔥 Brand & Key Entities (Never Translate)

| English | Dutch | Notes |
|---------|-------|-------|
| Hack23 | Hack23 | Company name – never translate |
| Hack23 AB | Hack23 AB | Swedish company designation |
| Citizen Intelligence Agency | Citizen Intelligence Agency | Project name – keep English |
| CIA Compliance Manager | CIA Compliance Manager | Product name – keep English |
| Black Trigram | Black Trigram | Game product – keep English |
| 흑괘 | 흑괘 | Korean name for Black Trigram |
| 黑卦 | 黑卦 | Chinese name for Black Trigram |
| James Pether Sörling | James Pether Sörling | Founder name |
| CISSP | CISSP | Certification |
| CISM | CISM | Certification |
| GitHub | GitHub | Platform name |
| LinkedIn | LinkedIn | Platform name |
| OpenSSF | OpenSSF | Open Source Security Foundation |
| CII Best Practices | CII Best Practices | Badge name |
| Riksdag | Riksdag | Swedish Parliament |

### 👔 Job Titles & Professional Roles

| English | Dutch | Notes |
|---------|-------|-------|
| CEO / Chief Executive Officer | CEO / Algemeen Directeur | |
| Founder | Oprichter | |
| CEO/Founder | CEO/Oprichter | |
| Application Security Officer | Applicatiebeveiligingsfunctionaris | |
| Information Security Officer | Informatiebeveiligingsfunctionaris | |
| Senior Security Architect | Senior beveiligingsarchitect | |
| Cloud Architect | Cloud-architect | |
| Security Consultant | Beveiligingsconsultant | |
| CISO | CISO | Chief Information Security Officer |
| Compliance Officer | Compliance officer | |
| Risk Manager | Risicomanager | |
| IT Security Manager | IT-beveiligingsmanager | |
| Security Auditor | Beveiligingsauditor | |
| Taekwondo Instructor | Taekwondo-instructeur | |
| System Developer | Systeemontwikkelaar | |
| Software Engineer | Software-engineer | |
| J2EE Developer | J2EE-ontwikkelaar | |
| Unix Helpdesk | Unix-helpdesk | |
| Teaching Assistant | Onderwijsassistent | |
| NBC Defence Group Leader | NBC-defensiegroepsleider | Military role |

### 🏢 Hack23 Business & Services

| English | Dutch | Notes |
|---------|-------|-------|
| Cybersecurity Consulting Sweden | Cybersecurity consulting in Zweden | Main tagline |
| Public ISMS | Openbaar ISMS | Core differentiator |
| Open ISMS Transparency | Open ISMS-transparantie | |
| Security Architecture & Strategy | Beveiligingsarchitectuur en strategie | Service line |
| Cloud Security & DevSecOps | Cloudbeveiliging en DevSecOps | Service line |
| Secure Development & Code Quality | Veilige ontwikkeling en codekwaliteit | Service line |
| Compliance & Regulatory | Compliance en regelgeving | Service line |
| Open Source Security | Open source beveiliging | Service line |
| Security Culture & Training | Beveiligingscultuur en training | Service line |
| Full-Stack Security | Full-stack beveiliging | |
| Current Practitioner | Actieve beoefenaar | Value proposition |
| Transparent Security | Transparante beveiliging | |
| Developer-Friendly Security | Ontwikkelaarsvriendelijke beveiliging | |
| Security Excellence Through Transparency | Beveiligingsexcellentie door transparantie | |
| OSPO | OSPO | Open Source Program Office |
| Gothenburg | Göteborg | City in Sweden |
| Sweden | Zweden | |
| Nordic Region | Scandinavië | |
| Europe | Europa | |
| Singapore | Singapore | |
| ASEAN Region | ASEAN-regio | |

### 🎮 Black Trigram Game Vocabulary

| English | Dutch | Notes |
|---------|-------|-------|
| Precision Combat Simulator | Precisie-gevechtssimulator | |
| Vital Points | Vitale punten | |
| 70 Anatomical Vital Points | 70 anatomische vitale punten | |
| 70 Techniques | 70 technieken | |
| Fighter Archetypes | Vechtersarchetypen | |
| Musa (Warrior) | Musa (Krijger) | |
| Amsalja (Assassin) | Amsalja (Moordenaar) | |
| Hacker | Hacker | |
| Jeongbo (Intelligence) | Jeongbo (Inlichtingen) | |
| Jojik (Organization) | Jojik (Organisatie) | |
| Korean Martial Arts | Koreaanse vechtsporten | |
| Taekkyeon | Taekkyeon | Korean martial art |
| Hapkido | Hapkido | Korean martial art |
| Taekwondo | Taekwondo | Korean martial art |
| Song Moo Kwan | Song Moo Kwan | Taekwondo school |
| Kukkiwon | Kukkiwon | World Taekwondo HQ |
| Black Belt | Zwarte band | |
| 3rd Dan | 3e dan | Rank |
| Cultural Preservation | Cultureel behoud | |
| Educational Gaming | Educatieve gaming | |
| Unity Game | Unity-game | |
| Steam | Steam | Platform name |
| itch.io | itch.io | Platform name |
| Fighting | Vechten | Game genre |
| Simulation | Simulatie | Game genre |
| Educational | Educatief | Game genre |
| Cultural | Cultureel | Game genre |
| Single-player | Singleplayer | |
| Multiplayer | Multiplayer | |
| Teen | Tiener | Content rating |
| Cross-platform | Cross-platform | |
| Open Source Game | Open source-game | |

### 🔍 Citizen Intelligence Agency Vocabulary

| English | Dutch | Notes |
|---------|-------|-------|
| Political Transparency | Politieke transparantie | |
| Political Intelligence Platform | Politiek inlichtingenplatform | |
| OSINT Platform | OSINT-platform | |
| Parliamentary Monitoring | Parlementaire monitoring | |
| Swedish Parliament Monitoring (Riksdag) | Monitoring Zweeds parlement (Riksdag) | |
| Political Decision Tracking | Tracking van politieke besluiten | |
| Governance Metrics & Rankings | Bestuursmaatstaven en rankings | |
| Democratic Accountability Analysis | Analyse democratische verantwoording | |
| Voting Records | Stemrecords | |
| Voting Pattern Analysis | Analyse van stempatronen | |
| Party Performance Metrics | Partijprestatiemetrieken | |
| Minister Activity Tracking | Tracking van ministeractiviteit | |
| Committee Work Analysis | Analyse van commissiewerk | |
| Political Trend Visualization | Visualisatie van politieke trends | |
| Open Data Integration | Integratie van open data | |
| World Bank | Wereldbank | |
| Swedish Government | Zweedse regering | |
| Accountability Metrics | Verantwoordingsmetrieken | |
| Open Data | Open data | |
| Civic Technology | Burgertechnologie | |
| Data Visualization | Datavisualisatie | |
| Political Analytics | Politieke analyse | |
| Citizens | Burgers | Audience |
| Journalists | Journalisten | Audience |
| Researchers | Onderzoekers | Audience |
| Policy Analysts | Beleidsanalisten | Audience |
| Political Scientists | Politicologen | Audience |
| Democracy Advocates | Democratievoorvechters | Audience |
| Parliamentary Process Analysis | Analyse van parlementair proces | |
| OSINT Methodology | OSINT-methodologie | |
| Swedish Governance System | Zweeds bestuurssysteem | |
| Data-Driven Political Analysis | Datagedreven politieke analyse | |
| Open Government Data Usage | Gebruik van open overheidsgegevens | |

### 🔐 CIA Compliance Manager Vocabulary

| English | Dutch | Notes |
|---------|-------|-------|
| Security Assessment Platform | Beveiligingsbeoordelingsplatform | |
| Enterprise Security Management | Enterprise beveiligingsbeheer | |
| CIA Triad Assessment | CIA-triade-beoordeling | |
| Business Impact Analysis | Bedrijfsimpactanalyse | |
| Multi-Framework Compliance | Multi-framework compliance | |
| STRIDE Analysis | STRIDE-analyse | Threat model |
| Threat Modeling | Dreigingsmodellering | |
| Evidence Collection | Bewijsverzameling | |
| Automated Compliance Reporting | Geautomatiseerde compliancerapportage | |
| Risk Register | Risicoregister | |
| Controls Monitoring | Controlemonitoring | |
| CRA Assessment | CRA-beoordeling | Cyber Resilience Act |
| Security Level Selection | Selectie beveiligingsniveau | |
| Cost Estimation | Kostenraming | |
| Implementation Guidance | Implementatierichtlijnen | |
| Gap Analysis | Gap-analyse | |
| Security Visualization | Beveiligingsvisualisatie | |
| Widget-Based Dashboard | Widget-gebaseerd dashboard | |
| Availability Impact Analysis | Beschikbaarheidsimpactanalyse | |
| Integrity Impact Analysis | Integriteitsimpactanalyse | |
| Confidentiality Impact Analysis | Vertrouwelijkheidsimpactanalyse | |
| Open Source Security Tool | Open source-beveiligingstool | |

### 🎓 Education & Learning Terms

| English | Dutch | Notes |
|---------|-------|-------|
| Educational Use | Educatief gebruik | |
| Self-Directed Learning | Zelfsturend leren | |
| Skill Development | Vaardigheidsontwikkeling | |
| Professional Development | Professionele ontwikkeling | |
| Teaches | Onderwijst | Schema.org property |
| Accessibility Features | Toegankelijkheidsfuncties | |
| Keyboard Navigation | Toetsenbordnavigatie | |
| High Contrast Mode | Hoog-contrastmodus | |
| Closed Captions | Ondertiteling | |
| Screen Reader Compatible | Schermlezercompatibel | |

### 🍎 Discordian Philosophy & ISMS Blog

| English | Dutch | Notes |
|---------|-------|-------|
| Think for Yourself | Denk zelf | Core motto |
| Question Authority | Bevraag autoriteit | |
| FNORD | FNORD | Never translate |
| Nothing is True | Niets is waar | |
| Everything is Permitted | Alles is toegestaan | |
| Security Theater | Beveiligingstheater | Fake security |
| Radical Transparency | Radicale transparantie | |
| Chapel Perilous | Chapel Perilous | Keep English |
| Operation Mindfuck | Operation Mindfuck | Keep English |
| Illuminatus Trilogy | Illuminatus-trilogie | |
| Eris | Eris | Goddess of Chaos |
| Discordia | Discordia | |
| Law of Fives | Wet van Vijf | |
| Sacred Geometry | Heilige geometrie | |
| Five-Layer Architecture | Vijflaags architectuur | |
| Nation-State Surveillance | Staatssurveillance | |
| Crypto Backdoors | Crypto-achterdeuren | |
| Security Through Obscurity | Beveiliging door onduidelijkheid | Anti-pattern |
| Information Hoarding | Informatie oppotten | |
| Knowledge Transparency | Kennistransparantie | |
| Simon Moon | Simon Moon | Character reference |
| Hagbard Celine | Hagbard Celine | Character reference |
| George Dorn | George Dorn | Character reference |

### 🧭 Navigation & UI Elements

| English | Dutch |
|---------|-------|
| Home | Home |
| About Us | Over ons |
| Services | Diensten |
| Products | Producten |
| Projects | Projecten |
| Contact | Contact |
| Blog | Blog |
| Search | Zoeken |
| Menu | Menu |
| Close | Sluiten |
| Back | Terug |
| Next | Volgende |
| Previous | Vorige |
| Submit | Verzenden |
| Cancel | Annuleren |
| **Expand All** | **Alles uitvouwen** |
| **Collapse All** | **Alles invouwen** |
| Download | Download |
| Read More | Lees meer |
| View Details | Bekijk details |
| Privacy Policy | Privacybeleid |
| Terms of Service | Servicevoorwaarden |
| Copyright | Auteursrecht |
| Sitemap | Sitemap |
| FAQ | FAQ |
| Why Hack23 | Waarom Hack23 |
| Accessibility Statement | Toegankelijkheidsverklaring |
| Language | Taal |
| Share | Delen |
| Print | Afdrukken |
| Save | Opslaan |
| Edit | Bewerken |
| Delete | Verwijderen |
| Confirm | Bevestigen |
| Loading | Laden |
| Error | Fout |
| Success | Succes |
| Warning | Waarschuwing |

### 🔐 CIA Triad & Core Security Principles

| English | Dutch | Notes |
|---------|-------|-------|
| CIA Triad | CIA-driehoek | |
| CIA+ Framework | CIA+ Framework | Extended framework |
| **Confidentiality** | **Vertrouwelijkheid** | Data protection |
| **Integrity** | **Integriteit** | Data accuracy |
| **Availability** | **Beschikbaarheid** | System uptime |
| Non-Repudiation | Onweerlegbaarheid | |
| Authentication | Authenticatie | |
| Authorization | Autorisatie | |

### 🔒 Security & Cybersecurity Terminology

| English | Dutch | Notes |
|---------|-------|-------|
| Cybersecurity | Cybersecurity | |
| Information Security | Informatiebeveiliging | |
| ISMS | ISMS / Informatiebeveiligingsmanagementsysteem | |
| Security Policy | Beveiligingsbeleid | |
| Risk Management | Risicobeheer | |
| Risk Assessment | Risicobeoordeling | |
| Threat | Dreiging | |
| Vulnerability | Kwetsbaarheid | |
| Exploit | Exploit | |
| Patch | Patch / Beveiligingsupdate | |
| Firewall | Firewall | |
| Encryption | Encryptie / Versleuteling | |
| Decryption | Decryptie / Ontsleuteling | |
| Access Control | Toegangscontrole | |
| Multi-Factor Authentication (MFA) | Multi-factor authenticatie | |
| Single Sign-On (SSO) | Single Sign-On | |
| Phishing | Phishing | |
| Ransomware | Ransomware | |
| Malware | Malware | |
| Zero Trust | Zero Trust | |
| Defense in Depth | Diepteverdediging | |
| Least Privilege | Minimale rechten | |
| Incident Response | Incidentrespons | |
| Data Breach | Datalek | |
| Penetration Test | Penetratietest | |
| Audit | Audit | |
| Compliance | Compliance | |
| Governance | Governance | |
| Security Awareness | Beveiligingsbewustzijn | |
| Backup | Backup | |
| Disaster Recovery | Rampenherstel | |
| Business Continuity | Bedrijfscontinuïteit | |
| Supply Chain Security | Toeleveringsketenbeveiliging | |
| SLSA Level 3 | SLSA Niveau 3 | Supply chain security |
| Container Security | Containerbeveiliging | |
| Serverless Security | Serverless beveiliging | |
| API Security | API-beveiliging | |
| Endpoint Security | Eindpuntbeveiliging | |

### 🏛️ Regulatory & Standards

| English | Dutch | Notes |
|---------|-------|-------|
| ISO 27001 | ISO 27001 | Keep as-is |
| ISO 27001:2022 | ISO 27001:2022 | |
| GDPR | AVG / GDPR | EU regulation |
| NIS2 | NIS2-richtlijn | EU directive |
| NIST CSF | NIST CSF | |
| CIS Controls | CIS Controls | |
| SOC2 | SOC2 | |
| HIPAA | HIPAA | US healthcare |
| EU Cyber Resilience Act (CRA) | EU Cyber Resilience Act | |
| Annex A Controls | Bijlage A-controles | ISO 27001 |
| Statement of Applicability | Verklaring van toepasselijkheid | |

### 💼 Business & Professional Terms

| English | Dutch |
|---------|-------|
| Consulting | Consultancy |
| Enterprise | Onderneming |
| Strategy | Strategie |
| Certification | Certificering |
| Assessment | Beoordeling |
| Implementation | Implementatie |
| Audit | Audit |
| Review | Review |
| Gap Analysis | Gap-analyse |
| Roadmap | Roadmap |
| Best Practices | Best practices |
| Case Study | Casestudy |
| ROI | ROI |
| KPI | KPI |
| SLA | SLA |
| Stakeholder | Belanghebbende |
| Deliverable | Deliverable |
| Milestone | Mijlpaal |

### 📝 Blog Post Categories

| English | Dutch |
|---------|-------|
| Security Architecture | Beveiligingsarchitectuur |
| ISMS Policies | ISMS-beleid |
| Compliance Frameworks | Compliance-frameworks |
| Threat Modeling | Dreigingsmodellering |
| Secure Development | Veilige ontwikkeling |
| Cloud Security | Cloudbeveiliging |
| Access Control | Toegangscontrole |
| Cryptography | Cryptografie |
| Incident Response | Incidentrespons |
| Vulnerability Management | Kwetsbaarheidsbeheer |
| Asset Management | Assetbeheer |
| Network Security | Netwerkbeveiliging |
| Email Security | E-mailbeveiliging |
| Physical Security | Fysieke beveiliging |
| Mobile Device Security | Mobiele apparaatbeveiliging |
| Remote Access Security | Remote access beveiliging |
| Monitoring & Logging | Monitoring en logging |
| Security Metrics | Beveiligingsmetrieken |
| Third Party Risk | Derdenrisico |
| Change Management | Wijzigingsbeheer |

### 🏭 Industry-Specific Terms

| English | Dutch |
|---------|-------|
| Investment & FinTech | Investering en FinTech |
| Betting & Gaming | Gokken en gaming |
| Cannabis Security | Cannabisbeveiliging |
| Healthcare | Gezondheidszorg |
| Government | Overheid |
| Critical Infrastructure | Kritieke infrastructuur |
| Financial Services | Financiële diensten |
| E-commerce | E-commerce |

---

## ✅ Translation Checklist

- [ ] `<html lang="nl">` attribute set
- [ ] `<title>` translated
- [ ] `<meta name="description">` translated
- [ ] `og:locale` set to `nl_NL`
- [ ] All hreflang tags present (14 languages)
- [ ] Navigation menu translated
- [ ] Footer translated
- [ ] Brand names kept in English
- [ ] Technical terms verified
- [ ] Dutch compound words formed correctly

---

## 📝 Notes

- Use **formal business Dutch**
- Many English IT terms are used directly in Dutch
- Dutch uses many compound words (write as one word)
- AVG is the Dutch name for GDPR

---

*23 FNORD 5*

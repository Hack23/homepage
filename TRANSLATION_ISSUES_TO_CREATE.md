# Translation Issues to Create

This document contains 10 GitHub issues that need to be created for completing missing translation files in the Hack23/homepage repository.

## Analysis Summary

- **Total English base files**: 93
- **Translation coverage**: 51.6% (FR/ES) to 78.5% (SV)
- **Total missing translations**: ~470 files across all languages
- **Focus**: Discordian ISMS policies, ISO 27001 pages, blog posts, core pages

---

## Issue 1: Complete Swedish (sv) Discordian ISMS Policy Translations (20 files)

**Title**: Complete Swedish (sv) Discordian ISMS Policy Translations (20 files)

**Labels**: `translation`, `high-priority`, `swedish`

**Assignee**: `.github/agents/ui-enhancement-specialist.md`

**Body**:
```markdown
## Translation Task: Swedish (sv) Discordian ISMS Policies

### Summary
Complete translation of 20 remaining Discordian ISMS policy files into Swedish. Swedish is the base language for Hack23 AB and requires high-quality translations.

### Status
- **Language**: Swedish (sv)
- **Category**: Discordian ISMS Policies  
- **Files to Translate**: 20
- **Priority**: HIGH
- **Assignee**: .github/agents/ui-enhancement-specialist.md

### Missing Files
```
discordian-ai-policy.html
discordian-asset-mgmt.html
discordian-backup-recovery.html
discordian-business-continuity.html
discordian-classification.html
discordian-cloud-security.html
discordian-cra-conformity.html
discordian-crypto.html
discordian-data-classification.html
discordian-data-protection.html
discordian-disaster-recovery.html
discordian-email-security.html
discordian-llm-security.html
discordian-mobile-device.html
discordian-monitoring-logging.html
discordian-network-security.html
discordian-physical-security.html
discordian-secure-dev.html
discordian-security-metrics.html
discordian-security-strategy.html
```

### Requirements
Each translated file must include:
- ✅ Proper Swedish language attributes (`lang="sv"`)
- ✅ Complete hreflang tags for all 13 languages
- ✅ Swedish og:locale metadata (`sv_SE`)
- ✅ Schema.org structured data with `inLanguage`: "sv"
- ✅ Localized navigation and breadcrumbs
- ✅ Professional Swedish translation of all content
- ✅ ISO 27001 terminology in Swedish
- ✅ Preserve Discordian voice and humor

### Translation Guide
See: [Swedish-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/Swedish-Translation-Guide.md)

### Status Tracking
Update: [Swedish-Translation-Status.md](https://github.com/Hack23/homepage/blob/master/Swedish-Translation-Status.md)

### Notes
- Swedish is HOME market - quality is critical
- AI translations are acceptable for speed
- Focus on technical accuracy and professional tone
- All headers, SEO meta, and structured data must be in Swedish
```

---

## Issue 2: Complete Nordic Languages (DA/FI/NO) Discordian ISMS Policy Translations (25 files each)

**Title**: Complete Nordic Languages (DA/FI/NO) Discordian ISMS Policy Translations (25 files each)

**Labels**: `translation`, `high-priority`, `nordic`

**Assignee**: `.github/agents/ui-enhancement-specialist.md`

**Body**:
```markdown
## Translation Task: Nordic Languages Discordian ISMS Policies

### Summary
Complete translation of 25 Discordian ISMS policy files into Danish, Finnish, and Norwegian (75 total files).

### Status
- **Languages**: Danish (da), Finnish (fi), Norwegian (no)
- **Category**: Discordian ISMS Policies
- **Files per Language**: ~25 (75 total)
- **Priority**: HIGH
- **Assignee**: .github/agents/ui-enhancement-specialist.md

### Missing Files (shared across DA/FI/NO)
25 Discordian policy files including: ai-policy, asset-mgmt, backup-recovery, business-continuity, classification, cloud-security, cra-conformity, crypto, data-classification, data-protection, disaster-recovery, email-security, llm-security, mobile-device, monitoring-logging, network-security, open-source, physical-security, risk-assessment, secure-dev, security-metrics, security-strategy, security-training, stakeholders, supplier-reality, third-party, threat-modeling, vuln-mgmt

### Requirements
- Proper language attributes (da/fi/no)
- 17 hreflang tags per file
- Localized og:locale (da_DK, fi_FI, nb_NO)
- Schema.org structured data
- ISO 27001 Nordic terminology
- Regulatory bodies: Datatilsynet (DA/NO), TRAFICOM (FI)

### Translation Guides
- [Danish-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/Danish-Translation-Guide.md)
- [Finnish-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/Finnish-Translation-Guide.md)
- [Norwegian-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/Norwegian-Translation-Guide.md)

### Notes
- Nordic regulatory bodies: Datatilsynet (DA/NO), TRAFICOM (FI)
- Similar linguistic patterns allow batch processing
- AI translations acceptable for efficiency
- All headers, SEO, and structured data in target language
```

---

## Issue 3: Complete RTL Languages (AR/HE) Discordian ISMS Policy Translations (37-38 files each)

**Title**: Complete RTL Languages (AR/HE) Discordian ISMS Policy Translations (37-38 files each)

**Labels**: `translation`, `high-priority`, `rtl`, `arabic`, `hebrew`

**Assignee**: `.github/agents/ui-enhancement-specialist.md`

**Body**:
```markdown
## Translation Task: RTL Languages Discordian ISMS Policies

### Summary
Complete translation of 37-38 Discordian ISMS policy files into Arabic and Hebrew (75 total files). RTL languages require special handling.

### Status
- **Languages**: Arabic (ar), Hebrew (he)
- **Category**: Discordian ISMS Policies
- **Files**: ~37 AR, ~38 HE (75 total)
- **Priority**: HIGH
- **Assignee**: .github/agents/ui-enhancement-specialist.md

### Missing Files
37-38 Discordian policy files including: ai-policy, asset-mgmt, backup-recovery, business-continuity, classification, cloud-security, cra-conformity, crypto, data-classification, data-protection, disaster-recovery, email-security, llm-security, mobile-device, monitoring-logging, network-security, open-source, physical-security, risk-assessment, secure-dev, security-metrics, security-strategy, security-training, stakeholders, supplier-reality, third-party, threat-modeling, vuln-mgmt

### RTL-Specific Requirements
- RTL attributes: `lang="ar/he" dir="rtl"`
- Fonts: Noto Sans Arabic/Hebrew
- 10 hreflang tags per file
- og:locale: ar_AR (with regional alternates), he_IL
- RTL-compatible layout (text alignment, padding)
- Professional translation in target language
- ISO 27001 terminology in Arabic/Hebrew
- Preserve Discordian voice

### Translation Guides
- [Arabic-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/Arabic-Translation-Guide.md)
- [Hebrew-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/Hebrew-Translation-Guide.md)

### Notes
- RTL requires special CSS considerations
- Arabic: MENA market focus
- Hebrew: Israeli market focus
- AI translations acceptable but verify RTL rendering
- All headers, SEO, and structured data in target language
```

---

## Issue 4: Complete Asian Languages (JA/ZH/KO) Discordian ISMS Policy Translations (42 files each)

**Title**: Complete Asian Languages (JA/ZH/KO) Discordian ISMS Policy Translations (42 files each)

**Labels**: `translation`, `high-priority`, `asian`, `japanese`, `chinese`, `korean`

**Assignee**: `.github/agents/ui-enhancement-specialist.md`

**Body**:
```markdown
## Translation Task: Asian Languages Discordian ISMS Policies

### Summary
Complete translation of 42 Discordian ISMS policy files into Japanese, Chinese, and Korean (126 total files).

### Status
- **Languages**: Japanese (ja), Chinese (zh), Korean (ko)
- **Category**: Discordian ISMS Policies
- **Files per Language**: 42 (126 total)
- **Priority**: HIGH
- **Assignee**: .github/agents/ui-enhancement-specialist.md

### Missing Files
42 Discordian policy files including: acceptable-use, access-control, ai-policy, asset-mgmt, backup-recovery, business-continuity, change-mgmt, classification, cloud-security, cra-conformity, crypto, data-classification, data-protection, disaster-recovery, email-security, incident-response, llm-security, mobile-device, monitoring-logging, network-security, open-source, physical-security, privacy, remote-access, risk-assessment, risk-register, secure-dev, security-metrics, security-strategy, security-training, stakeholders, supplier-reality, third-party, threat-modeling, vuln-mgmt

### Requirements
- Language attributes: ja/zh/ko
- 24 hreflang tags per file
- og:locale: ja_JP, zh_CN, ko_KR
- Local ISO standards: JIS Q 27001 (JP), GB/T 22080 (CN), K-ISMS (KR)
- Schema.org structured data
- Preserve Discordian voice

### Translation Guides
- [Japanese-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/Japanese-Translation-Guide.md)
- [Chinese-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/Chinese-Translation-Guide.md)
- [Korean-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/Korean-Translation-Guide.md)

### Notes
- Asian markets have local ISO 27001 equivalents
- Technical terminology must use local standards
- AI translations acceptable for efficiency
- All headers, SEO, and structured data in target language
```

---

## Issue 5: Complete European Languages (DE/NL/FR/ES) Discordian ISMS Policy Translations (38 files each)

**Title**: Complete European Languages (DE/NL/FR/ES) Discordian ISMS Policy Translations (38 files each)

**Labels**: `translation`, `medium-priority`, `european`

**Assignee**: `.github/agents/ui-enhancement-specialist.md`

**Body**:
```markdown
## Translation Task: European Languages Discordian ISMS Policies

### Summary
Complete translation of 38 Discordian ISMS policy files into German, Dutch, French, and Spanish (152 total files).

### Status
- **Languages**: German (de), Dutch (nl), French (fr), Spanish (es)
- **Category**: Discordian ISMS Policies
- **Files per Language**: ~38 (152 total)
- **Priority**: MEDIUM
- **Assignee**: .github/agents/ui-enhancement-specialist.md

### Missing Files
38 Discordian policy files including: acceptable-use, access-control, ai-policy, asset-mgmt, backup-recovery, business-continuity, change-mgmt, classification, cloud-security, cra-conformity, crypto, data-classification, data-protection, disaster-recovery, email-security, incident-response, llm-security, mobile-device, monitoring-logging, network-security, open-source, physical-security, privacy, remote-access, risk-assessment, risk-register, secure-dev, security-metrics, security-strategy, security-training, stakeholders, supplier-reality, third-party, threat-modeling, vuln-mgmt

### Requirements
- Language attributes: de/nl/fr/es
- Complete hreflang tags
- og:locale: de_DE, nl_NL, fr_FR, es_ES
- Schema.org structured data
- ISO 27001 terminology in local language
- Preserve Discordian voice

### Translation Guides
- [German-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/German-Translation-Guide.md)
- [Dutch-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/Dutch-Translation-Guide.md)
- [French-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/French-Translation-Guide.md)
- [Spanish-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/Spanish-Translation-Guide.md)

### Notes
- Major European markets
- AI translations acceptable for efficiency
- Professional business tone required
- All headers, SEO, and structured data in target language
```

---

## Issue 6: Complete Nordic Languages (DA/FI/NO) ISO 27001 Page Translations (3 files each)

**Title**: Complete Nordic Languages (DA/FI/NO) ISO 27001 Page Translations (3 files each)

**Labels**: `translation`, `medium-priority`, `nordic`, `iso-27001`

**Assignee**: `.github/agents/ui-enhancement-specialist.md`

**Body**:
```markdown
## Translation Task: Nordic Languages ISO 27001 Pages

### Summary
Complete translation of 3 ISO 27001 pages into Danish, Finnish, and Norwegian (9 total files).

### Status
- **Languages**: Danish (da), Finnish (fi), Norwegian (no)
- **Category**: ISO 27001 Pages
- **Files per Language**: 3 (9 total)
- **Priority**: MEDIUM
- **Assignee**: .github/agents/ui-enhancement-specialist.md

### Missing Files
- iso-27001-certification-costs-sweden.html
- iso-27001-implementation-mistakes.html
- iso-27001-implementation-sweden.html

### Requirements
- Language attributes: da/fi/no
- Complete hreflang tags
- Market-specific costs (DKK, EUR, NOK)
- Nordic regulatory context
- Certification bodies: Inspecta (FI), Nemko (NO), DQS/TÜV (DK)

### Translation Guides
- [Danish-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/Danish-Translation-Guide.md)
- [Finnish-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/Finnish-Translation-Guide.md)
- [Norwegian-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/Norwegian-Translation-Guide.md)

### Notes
- Focus on Nordic market specifics
- Cost ranges need currency conversion
- All headers, SEO, and structured data in target language
```

---

## Issue 7: Complete European Languages (DE/NL/FR/ES) ISO 27001 Page Translations (2-3 files each)

**Title**: Complete European Languages (DE/NL/FR/ES) ISO 27001 Page Translations (2-3 files each)

**Labels**: `translation`, `medium-priority`, `european`, `iso-27001`

**Assignee**: `.github/agents/ui-enhancement-specialist.md`

**Body**:
```markdown
## Translation Task: European Languages ISO 27001 Pages

### Summary
Complete translation of 2-3 ISO 27001 pages into German, Dutch, French, and Spanish (10 total files).

### Status
- **Languages**: German (de), Dutch (nl), French (fr), Spanish (es)
- **Category**: ISO 27001 Pages
- **Files**: 2-3 per language (10 total)
- **Priority**: MEDIUM
- **Assignee**: .github/agents/ui-enhancement-specialist.md

### Missing Files
- iso-27001-certification-costs-sweden.html (all)
- iso-27001-implementation-sweden.html (DE, NL)
- iso-27001-implementation-mistakes.html (FR, ES)

### Requirements
- Language attributes: de/nl/fr/es
- Complete hreflang tags
- Market-specific costs (EUR)
- Local regulatory context
- Local certification bodies

### Translation Guides
- [German-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/German-Translation-Guide.md)
- [Dutch-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/Dutch-Translation-Guide.md)
- [French-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/French-Translation-Guide.md)
- [Spanish-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/Spanish-Translation-Guide.md)

### Notes
- Market-specific adaptations required
- Certification bodies vary by country
- All headers, SEO, and structured data in target language
```

---

## Issue 8: Complete European Languages (DE/NL/FR/ES) Blog Post Translations (3 files each)

**Title**: Complete European Languages (DE/NL/FR/ES) Blog Post Translations (3 files each)

**Labels**: `translation`, `low-priority`, `european`, `blog`

**Assignee**: `.github/agents/ui-enhancement-specialist.md`

**Body**:
```markdown
## Translation Task: European Languages Blog Posts

### Summary
Complete translation of 3 blog posts into German, Dutch, French, and Spanish (12 total files).

### Status
- **Languages**: German (de), Dutch (nl), French (fr), Spanish (es)
- **Category**: Blog Posts
- **Files per Language**: 3 (12 total)
- **Priority**: LOW
- **Assignee**: .github/agents/ui-enhancement-specialist.md

### Missing Files
- blog-automated-convergence.html
- blog-information-hoarding.html
- blog-public-isms-benefits.html

### Requirements
- Language attributes: de/nl/fr/es
- Complete hreflang tags
- og:locale metadata
- Schema.org BlogPosting structured data
- Localized breadcrumb navigation
- Thought leadership tone

### Translation Guides
- [German-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/German-Translation-Guide.md)
- [Dutch-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/Dutch-Translation-Guide.md)
- [French-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/French-Translation-Guide.md)
- [Spanish-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/Spanish-Translation-Guide.md)

### Notes
- Thought leadership content
- Lower priority than core pages
- AI translations acceptable
- All headers, SEO, and structured data in target language
```

---

## Issue 9: Complete Core Page Translations (why-hack23, cia-triad-faq)

**Title**: Complete Core Page Translations (why-hack23, cia-triad-faq)

**Labels**: `translation`, `medium-priority`, `core-pages`

**Assignee**: `.github/agents/ui-enhancement-specialist.md`

**Body**:
```markdown
## Translation Task: Core Pages (why-hack23, cia-triad-faq)

### Summary
Complete translation of 2 core pages missing in multiple languages.

### Status
- **Languages**: Multiple (AR, HE missing both; others vary)
- **Category**: Core Pages
- **Files**: 2
- **Priority**: MEDIUM
- **Assignee**: .github/agents/ui-enhancement-specialist.md

### Missing Files
- why-hack23.html (missing in: AR, HE)
- cia-triad-faq.html (missing in: AR, HE)

### Requirements
- Proper language attributes
- Complete hreflang tags
- Localized og:locale metadata
- Schema.org FAQPage for cia-triad-faq
- Technical accuracy for CIA Triad concepts
- RTL considerations for AR/HE

### Translation Guides
- [Arabic-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/Arabic-Translation-Guide.md)
- [Hebrew-Translation-Guide.md](https://github.com/Hack23/homepage/blob/master/Hebrew-Translation-Guide.md)
- See other language guides as needed

### Notes
- **why-hack23**: Company value proposition
- **cia-triad-faq**: Core cybersecurity concepts (Confidentiality, Integrity, Availability)
- RTL considerations for AR/HE versions
- All headers, SEO, and structured data in target language
```

---

## Issue 10: Complete Swedish Election 2026 Page Translations (9 languages)

**Title**: Complete Swedish Election 2026 Page Translations (9 languages)

**Labels**: `translation`, `low-priority`, `special-topics`

**Assignee**: `.github/agents/ui-enhancement-specialist.md`

**Body**:
```markdown
## Translation Task: Swedish Election 2026 Page

### Summary
Complete translation of Swedish Election 2026 analysis page into 9 languages.

### Status
- **Languages**: AR, HE, JA, ZH, KO, NL, DE, FR, ES
- **Category**: Special Topics
- **Files**: 1 file × 9 languages = 9 files
- **Priority**: LOW
- **Assignee**: .github/agents/ui-enhancement-specialist.md

### Missing File
- swedish-election-2026.html

### Requirements
- Proper language attributes
- Complete hreflang tags
- Localized og:locale metadata
- Schema.org Article structured data
- Cultural adaptation (Swedish political context)
- Professional translation

### Translation Guides
See respective language translation guides for AR, HE, JA, ZH, KO, NL, DE, FR, ES

### Notes
- Specialized political content
- Cultural/political context requires careful translation
- Low priority due to specialized nature
- Already exists in: DA, FI, NO, SV (Nordic languages)
- All headers, SEO, and structured data in target language
```

---

## Summary

**Total Issues**: 10
**Total Missing Files**: ~470 across all languages
**Priority Breakdown**:
- HIGH: 4 issues (Issues 1-4) - 276 files
- MEDIUM: 4 issues (Issues 5-7, 9) - 181 files
- LOW: 2 issues (Issues 8, 10) - 21 files

**Common Requirements for All Issues**:
- All headers, SEO meta tags, and structured data must be in the target language
- AI translations are acceptable for efficiency
- Each file needs proper lang attributes, complete hreflang tags, og:locale metadata, and Schema.org structured data
- Preserve Discordian voice and humor where applicable
- Professional business tone for cybersecurity consulting

**References**:
- [TRANSLATION_DOCUMENTATION_README.md](https://github.com/Hack23/homepage/blob/master/TRANSLATION_DOCUMENTATION_README.md)
- Individual language Translation Guides (13 files)
- Individual language Translation Status files (13 files)

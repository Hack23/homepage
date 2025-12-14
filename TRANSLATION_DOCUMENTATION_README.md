# Translation Documentation

## Overview

This directory contains comprehensive translation guides and status files for all 13 languages supported by the Hack23 AB website.

## Structure

Each language has **two dedicated files**:
1. **`[Language]-Translation-Guide.md`** - Translation instructions, terminology, and best practices
2. **`[Language]-Translation-Status.md`** - Current translation progress and completion status

## Supported Languages (13)

### RTL Languages
| Language | Code | Files | Guide | Status |
|----------|------|-------|-------|--------|
| Arabic | ar | 59 | [Arabic-Translation-Guide.md](Arabic-Translation-Guide.md) | [Arabic-Translation-Status.md](Arabic-Translation-Status.md) |
| Hebrew | he | 64 | [Hebrew-Translation-Guide.md](Hebrew-Translation-Guide.md) | [Hebrew-Translation-Status.md](Hebrew-Translation-Status.md) |

### Asian Languages
| Language | Code | Files | Guide | Status |
|----------|------|-------|-------|--------|
| Japanese | ja | 51 | [Japanese-Translation-Guide.md](Japanese-Translation-Guide.md) | [Japanese-Translation-Status.md](Japanese-Translation-Status.md) |
| Chinese | zh | 51 | [Chinese-Translation-Guide.md](Chinese-Translation-Guide.md) | [Chinese-Translation-Status.md](Chinese-Translation-Status.md) |
| Korean | ko | 51 | [Korean-Translation-Guide.md](Korean-Translation-Guide.md) | [Korean-Translation-Status.md](Korean-Translation-Status.md) |

### Nordic Languages
| Language | Code | Files | Guide | Status |
|----------|------|-------|-------|--------|
| Danish | da | 66 | [Danish-Translation-Guide.md](Danish-Translation-Guide.md) | [Danish-Translation-Status.md](Danish-Translation-Status.md) |
| Finnish | fi | 66 | [Finnish-Translation-Guide.md](Finnish-Translation-Guide.md) | [Finnish-Translation-Status.md](Finnish-Translation-Status.md) |
| Norwegian | no | 66 | [Norwegian-Translation-Guide.md](Norwegian-Translation-Guide.md) | [Norwegian-Translation-Status.md](Norwegian-Translation-Status.md) |

### European Languages
| Language | Code | Files | Guide | Status |
|----------|------|-------|-------|--------|
| Dutch | nl | 50 | [Dutch-Translation-Guide.md](Dutch-Translation-Guide.md) | [Dutch-Translation-Status.md](Dutch-Translation-Status.md) |
| German | de | 50 | [German-Translation-Guide.md](German-Translation-Guide.md) | [German-Translation-Status.md](German-Translation-Status.md) |
| French | fr | 49 | [French-Translation-Guide.md](French-Translation-Guide.md) | [French-Translation-Status.md](French-Translation-Status.md) |
| Spanish | es | 49 | [Spanish-Translation-Guide.md](Spanish-Translation-Guide.md) | [Spanish-Translation-Status.md](Spanish-Translation-Status.md) |

### Base Language
| Language | Code | Files | Guide | Status |
|----------|------|-------|-------|--------|
| Swedish | sv | 74 | [Swedish-Translation-Guide.md](Swedish-Translation-Guide.md) | [Swedish-Translation-Status.md](Swedish-Translation-Status.md) |

**Total:** 746 HTML files across 13 languages

## Swedish Blog-Specific Documentation

Swedish has additional specialized documentation for blog translations:
- **[SWEDISH_BLOG_TRANSLATION_GUIDE.md](SWEDISH_BLOG_TRANSLATION_GUIDE.md)** - CIA blog series translation guide
- **[SWEDISH_BLOG_TRANSLATION_STATUS.md](SWEDISH_BLOG_TRANSLATION_STATUS.md)** - CIA blog translation status
- **[SWEDISH_BLOG_CREATION_STATUS.md](SWEDISH_BLOG_CREATION_STATUS.md)** - Blog creation progress

**Note:** These files use uppercase naming (`SWEDISH_BLOG_*`) as they are specialized, topic-specific documentation (CIA blog series), not general language guides. They are preserved from earlier work and referenced by the general Swedish translation files.

## Quick Start

### For Translators

1. **Find your language:** Locate `[YourLanguage]-Translation-Guide.md`
2. **Read the guide:** Understand terminology, structure, and requirements
3. **Check status:** Review `[YourLanguage]-Translation-Status.md` for current progress
4. **Follow workflow:** Use the step-by-step translation workflow in the guide
5. **Validate:** Complete the validation checklist before submission

### For Project Managers

1. **Check overall status:** Review individual language status files
2. **Identify priorities:** Look for "Priority: HIGH" markers in status files
3. **Track progress:** Monitor completion percentages in status files
4. **Estimate effort:** Each status file includes effort estimates

### For Developers

1. **HTML structure:** Each guide includes proper HTML templates
2. **Hreflang tags:** Comprehensive hreflang patterns documented
3. **Schema.org:** Structured data requirements specified
4. **Validation:** Technical validation checklists provided

## Translation Quality Standards

All translations must meet:
- ✅ **Professional business tone** appropriate for cybersecurity consulting
- ✅ **Technical accuracy** in cybersecurity terminology
- ✅ **Proper HTML structure** with valid markup
- ✅ **Complete hreflang tags** for SEO
- ✅ **Schema.org validation** for structured data
- ✅ **Native speaker review** for language quality
- ✅ **Mobile responsiveness** maintained
- ✅ **Accessibility standards** (WCAG 2.1 AA)

## File Naming Convention

### HTML Files
- English: `[page].html`
- Translations: `[page]_[code].html`
- Example: `index.html` → `index_sv.html`, `index_ja.html`

### Documentation Files
- Guide: `[Language]-Translation-Guide.md`
- Status: `[Language]-Translation-Status.md`
- Example: `Swedish-Translation-Guide.md`, `Swedish-Translation-Status.md`

## Infrastructure Status

| Status | Languages | Details |
|--------|-----------|---------|
| ✅ 100% Complete | All 13 | HTML structure, hreflang, Schema.org |
| ⚠️ Translation Required | Most | Professional content translation needed |
| ✅ Substantially Complete | Swedish | ~85-90% content translated |

## Translation Workflow

1. **Infrastructure** (✅ Complete for all languages)
   - HTML files created with proper lang attributes
   - Hreflang tags configured
   - Schema.org structured data in place
   - Navigation structure ready

2. **Content Translation** (⚠️ In Progress)
   - Professional translation of content
   - Technical terminology verification
   - Native speaker review
   - Quality assurance

3. **Validation** (Per File)
   - HTML validation (W3C)
   - Hreflang verification
   - Schema.org validation
   - Grammar and spelling check
   - Link functionality test
   - Mobile responsive test

## Technology Stack

- **HTML5:** Semantic markup
- **CSS3:** Single `styles.css` with RTL support
- **Deployment:** AWS S3 + CloudFront
- **CI/CD:** GitHub Actions with Lighthouse audits
- **Security:** ZAP security scanning

## Contact

For questions about translation documentation:
- **Repository:** https://github.com/Hack23/homepage
- **Issues:** Create GitHub issue with `translation` label
- **Documentation:** This file and individual language guides

---

**Last Updated:** December 2025  
**Maintainer:** Hack23 AB Translation Team  
**Total Files:** 29 documentation files (26 guides/status + 3 Swedish blog-specific)

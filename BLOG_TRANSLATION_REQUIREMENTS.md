# Blog Translation Requirements for Professional Translators

## Overview

This document outlines the requirements for translating Hack23 AB blog posts across 13 languages. These translations require professional cybersecurity expertise and native-level language proficiency.

**Status:** Infrastructure complete, content translation required  
**Priority:** Medium  
**Estimated Effort:** 20-30 hours  
**Languages:** 13 (Arabic, Chinese, Danish, Dutch, Finnish, French, German, Hebrew, Japanese, Korean, Norwegian, Spanish, Swedish)

## High-Priority Blog Posts (3)

### 1. blog-public-isms-benefits
**Word Count:** ~3,200 words  
**Type:** Thought Leadership  
**Audience:** C-suite executives, CISOs, security decision makers  
**Key Topics:**
- Why Hack23's ISMS is public on GitHub
- Transparency as competitive advantage
- Trust through verification
- Business value proposition
- Addressing objections to security transparency

**Translation Complexity:** Medium
- Professional business register required
- Technical security terminology
- Some Discordian philosophical references
- Business case arguments need cultural adaptation

**Files:** 13 translations
- blog-public-isms-benefits_{ar,da,de,es,fi,fr,he,ja,ko,nl,no,sv,zh}.html

### 2. blog-automated-convergence
**Word Count:** ~2,800 words  
**Type:** Technical DevSecOps  
**Audience:** Technical leaders, security architects, DevOps engineers  
**Key Topics:**
- AI agents creating self-healing secure software
- ISMS-aligned automation
- Pentagon of continuous improvement
- GitHub Copilot agents
- Automated issue creation and policy cross-reference

**Translation Complexity:** HIGH
- Strong Discordian voice (Hagbard Celine as author)
- Technical depth with code examples
- Philosophical concepts (Nothing is true, everything is permitted)
- Requires understanding of Illuminatus! trilogy references
- Code blocks must remain in English

**Files:** 13 translations
- blog-automated-convergence_{ar,da,de,es,fi,fr,he,ja,ko,nl,no,sv,zh}.html

### 3. blog-information-hoarding
**Word Count:** ~1,200 words  
**Type:** Security Philosophy  
**Audience:** All levels - management to technical  
**Key Topics:**
- CIA Triad integrity principles
- Breaking information silos
- Knowledge transparency as competitive advantage
- Organizational security culture
- Phantom meetings and email hoarding

**Translation Complexity:** Medium
- Professional but accessible tone
- Some technical terminology (CIA Triad, Clark-Wilson model)
- Organizational psychology concepts
- Examples of information hoarding behaviors

**Files:** 13 translations
- blog-information-hoarding_{ar,da,de,es,fi,fr,he,ja,ko,nl,no,sv,zh}.html

## Translation Guidelines

### Content to Translate

In each HTML file, translate:
1. **`<title>` tag** - Page title
2. **Meta description** - `<meta name="description">`
3. **Meta keywords** - `<meta name="keywords">`
4. **Open Graph title/description** - `og:title`, `og:description`
5. **Schema.org headline/description** - In JSON-LD script
6. **`<h1>` main heading**
7. **All `<h2>`, `<h3>` section headings**
8. **All paragraph content** within `<article>`
9. **List items** (`<ul>`, `<ol>`)
10. **Breadcrumb text** - Navigation labels
11. **Footer links** - Link text only

### Content to KEEP in English

1. **Code blocks** - All `<code>` and `<pre>` content
2. **Technical URLs** - GitHub links, repo URLs
3. **HTML structure** - All tags, classes, IDs
4. **Hreflang tags** - All 28 alternate language links
5. **Schema.org structure** - JSON-LD structure (translate values only)
6. **Product names** - "Citizen Intelligence Agency", "Black Trigram", "CIA Compliance Manager"

### Technical Terminology

**Use established translations from Translation Guides:**
- `[Language]-Translation-Guide.md` files in repository root
- ISO 27001 terminology (see guide tables)
- GDPR/DSGVO/RGPD (local regulation names)
- CIA Triad → Use localized term from guide

**Common Technical Terms (preserve in English when appropriate):**
- DevSecOps
- CI/CD
- GitHub
- Repository
- ISMS (may translate to full form)
- ISO 27001

### Tone and Style

#### Thought Leadership (blog-public-isms-benefits)
- **Register:** Professional business, C-suite appropriate
- **Tone:** Confident, authoritative, slightly provocative
- **Style:** Clear arguments with evidence, addressing objections
- **Goal:** Convince executives that transparency is competitive advantage

#### Technical (blog-automated-convergence)
- **Register:** Technical expert to technical audience
- **Tone:** Enthusiastic, visionary, philosophical
- **Style:** Discordian anarchist product owner voice
- **Discordian Elements:** 
  - "Nothing is true, everything is permitted"
  - FNORD references
  - Pentagon of continuous improvement
  - References to Illuminatus! trilogy concepts
- **Goal:** Inspire technical leaders with vision of automated security convergence

#### Philosophy (blog-information-hoarding)
- **Register:** Professional but accessible
- **Tone:** Problem-solving, practical, organizational focus
- **Style:** Clear examples with actionable insights
- **Goal:** Help organizations recognize and fix information hoarding

### Cultural Adaptation

#### Swedish Election Content
- The CIA blogs reference Swedish election monitoring (Riksdag 2026)
- **For non-Swedish markets:** Adapt to local political monitoring context:
  - EU: EU Parliament monitoring
  - US: Congressional/Presidential monitoring
  - Asia: Local parliament/government monitoring
- Maintain OSINT value proposition

#### Industry Examples
- Gaming/betting regulations vary by country
- Cannabis legal status differs significantly
- Financial regulations are market-specific
- Adapt regulatory references to target market

#### Discordian Philosophy
- Illuminatus! trilogy references may need explanation
- "Nothing is true, everything is permitted" → adapt culturally
- FNORD → consider if concept translates or needs explanation
- Maintain spirit of questioning authority and rigid thinking

### Quality Standards

Each translation must meet:

✅ **Language Quality**
- Native-level grammar and syntax
- Natural idioms appropriate to target culture
- No machine translation artifacts

✅ **Technical Accuracy**
- Cybersecurity terms correctly translated
- ISO 27001/NIST/CIS terminology matches local standards
- Technical explanations maintain accuracy

✅ **Business Tone**
- Appropriate register for professional consulting
- Confident without being arrogant
- Persuasive without being sales-y

✅ **HTML/SEO Integrity**
- No broken tags or structure
- All hreflang links preserved
- Schema.org JSON-LD valid
- Meta tags complete and accurate

✅ **Cultural Appropriateness**
- Examples resonate with target market
- Regulatory references accurate for region
- No cultural insensitivity or confusion

## File Structure

Each blog file follows this structure:

```html
<!DOCTYPE html>
<html lang="XX">  <!-- Two-letter language code -->
<head>
  <!-- Meta tags - TRANSLATE title, description, keywords -->
  <!-- Hreflang tags - DO NOT MODIFY -->
  <!-- Schema.org - TRANSLATE text values only -->
</head>
<body>
  <nav aria-label="Breadcrumb">
    <!-- TRANSLATE breadcrumb text -->
  </nav>
  <header>
    <!-- TRANSLATE h1 and navigation links text -->
  </header>
  <main>
    <article>
      <!-- TRANSLATE all content here -->
      <!-- KEEP code blocks in English -->
    </article>
  </main>
  <footer>
    <!-- TRANSLATE link text only -->
  </footer>
</body>
</html>
```

## RTL Languages (Arabic, Hebrew)

Files already have:
- `dir="rtl"` on `<html>` tag
- Appropriate fonts (Noto Sans Arabic/Hebrew)
- RTL-compatible CSS

**Translation considerations:**
- Text direction handled by HTML/CSS
- Translate content naturally in Arabic/Hebrew
- Numbers and English terms may remain LTR within RTL text

## Validation Checklist

After translation, verify:

- [ ] All visible text translated (except code blocks)
- [ ] HTML structure intact (no broken tags)
- [ ] 28 hreflang tags present and unchanged
- [ ] Schema.org JSON-LD valid
- [ ] Breadcrumb navigation functional
- [ ] Links point to correct language versions
- [ ] Meta tags complete (title, description, keywords)
- [ ] No English text remaining in content areas
- [ ] Technical terminology matches Translation Guide
- [ ] Business tone appropriate for target market
- [ ] File saves as UTF-8 encoding
- [ ] RTL attributes preserved for ar/he

## Delivery Format

**Files:** 39 HTML files (3 blogs × 13 languages)

**Naming Convention:**
- `blog-public-isms-benefits_{XX}.html`
- `blog-automated-convergence_{XX}.html`
- `blog-information-hoarding_{XX}.html`

Where XX = ar, da, de, es, fi, fr, he, ja, ko, nl, no, sv, zh

**Encoding:** UTF-8 with BOM for maximum compatibility

## Translation Status

| Blog | AR | DA | DE | ES | FI | FR | HE | JA | KO | NL | NO | SV | ZH |
|------|----|----|----|----|----|----|----|----|----|----|----|----|----| 
| public-isms-benefits | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| automated-convergence | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| information-hoarding | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Legend:** ✅ Complete | ⚠️ Partial | ❌ English content

## Reference Materials

**In Repository:**
- `TRANSLATION_DOCUMENTATION_README.md` - Overview
- `[Language]-Translation-Guide.md` - Terminology and conventions (13 files)
- `[Language]-Translation-Status.md` - Current status (13 files)
- English source files: `blog-*.html` (no language suffix)

**External Resources:**
- ISO 27001 standard (reference for terminology)
- Illuminatus! trilogy (for Discordian references)
- Hack23 ISMS-PUBLIC repository (context for ISMS blog)

## Contact

For questions about translation requirements:
- **Repository:** https://github.com/Hack23/homepage
- **Issues:** Create GitHub issue with `translation` label
- **Guidelines:** See individual Translation-Guide.md files

---

**Document Version:** 1.0  
**Last Updated:** December 2025  
**Maintainer:** Hack23 AB Translation Team

# Swedish Blog Translation Guide - CIA Series

## Overview
This guide documents the process for creating Swedish translations of the 9 CIA blog posts as specified in Issue #688.

## Progress Status

### Completed (1/9)
- ✅ `blog-cia-architecture_sv.html` - Complete Swedish translation with:
  - Proper hreflang tags (sv, sv-SE, x-default)
  - Swedish political terminology (Riksdagen, riksdagsledamöter, utskott, departement, myndigheter)
  - Preserved Discordian narrative style ("23 FNORD 5", Chapel Perilous references)
  - Updated schema.org structured data with Swedish language
  - Footer navigation updated to Swedish versions where available
  - Breadcrumb navigation in Swedish

### Remaining (8/9)
- [ ] `blog-cia-security_sv.html` - CIA Security (Defense Through Transparency)
- [ ] `blog-cia-workflows_sv.html` - CIA Workflows (CI/CD & State Machines)
- [ ] `blog-cia-mindmaps_sv.html` - CIA Mindmaps (Conceptual Sacred Geometry)
- [ ] `blog-cia-osint-intelligence_sv.html` - CIA OSINT Intelligence
- [ ] `blog-cia-future-security_sv.html` - CIA Future Security (Post-quantum & AI)
- [ ] `blog-cia-financial-strategy_sv.html` - CIA Financial Strategy ($24.70/Day Democracy)
- [ ] `blog-cia-business-case-global-news_sv.html` - CIA Business Case Global News
- [ ] `blog-cia-alternative-media-discordian-2026_sv.html` - CIA Alternative Media Discordian 2026

## Translation Standards Established

### Swedish Political Terminology
| English | Swedish | Usage Notes |
|---------|---------|-------------|
| Parliament | Riksdagen | Sweden's parliament |
| Member of Parliament | Riksdagsledamot | Use plural: riksdagsledamöter |
| Committee | Utskott | Parliamentary committee |
| Ministry | Departement | Government department |
| Government Agency | Myndighet / Myndighet sstyrelse | Context dependent |
| Parliamentary Monitoring | Parlamentarisk övervakning | |
| Political Transparency | Politisk öppenhet | |
| OSINT | Öppen källkodsintelligens / OSINT | Both acceptable |
| Election Analysis | Valanalys | |
| World Bank | Världsbanken | |
| Election Authority | Valmyndigheten | |
| Government Bodies | Myndighetsstyrelser | |

### Discordian Style Elements to Preserve
1. **"23 FNORD 5"** - Keep as-is (signature element)
2. **Law of Fives** - Translate to "Femtals Lag"
3. **Chapel Perilous** - Keep in English or translate to "Kapellet Perilous"
4. **Sacred Geometry** - "Helig geometri"
5. **Illumination paragraphs** - Start with "Upplysning:" in Swedish
6. **Hidden wisdom sections** - Use class="hidden-wisdom"
7. **Think for yourself** - "Tänk själv"
8. **Question authority** - "Ifrågasätt auktoritet"

### Technical Translation Terms
| English | Swedish |
|---------|---------|
| Architecture | Arkitektur |
| Security | Säkerhet |
| Five layers | Fem lager |
| Container | Container (keep English) |
| Service layer | Servicelager |
| Data access | Dataåtkomst |
| Workflows | Arbetsflöden |
| CI/CD | CI/CD (keep English acronym) |
| Threat modeling | Hotmodellering |
| Defense in depth | Försvar i djup |
| Zero trust | Noll förtroende |

## HTML Structure Template

### Required Meta Tags
```html
<html lang="sv">
<meta property="og:locale" content="sv_SE">
```

### Hreflang Tags Pattern
```html
<link rel="alternate" hreflang="en" href="https://hack23.com/blog-cia-[name].html">
<link rel="alternate" hreflang="sv" href="https://hack23.com/blog-cia-[name]_sv.html">
<link rel="alternate" hreflang="sv-SE" href="https://hack23.com/blog-cia-[name]_sv.html">
<link rel="alternate" hreflang="x-default" href="https://hack23.com/blog-cia-[name].html">
```

### Schema.org Requirements
- Set `"inLanguage": "sv"`
- Update breadcrumb names to Swedish: "Hem", "Blogg"
- Update article body excerpt to Swedish (first 150 chars)
- Keep English author names (Simon Moon, Hagbard Celine, George Dorn)

### Navigation Updates
```html
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="/">Hem</a></li>
    <li class="breadcrumb-item"><a href="/blog.html">Blogg</a></li>
    <li class="breadcrumb-item" aria-current="page">[Page Title in Swedish]</li>
  </ol>
</nav>
```

### Header Links
```html
<a href="index_sv.html">Hem</a>
<a href="blog_sv.html">Blogg</a>
<a href="cia-docs_sv.html">CIA-dokumentation</a>
```

### Footer Link Patterns
- Services: `services_sv.html` if it exists
- Products: Use `_sv` suffix where available (cia-features_sv.html, cia-docs_sv.html)
- Resources: blog_sv.html, cia-triad-faq_sv.html
- Company: why-hack23_sv.html
- Keep English links where Swedish versions don't exist

## Translation Workflow

### Step 1: Preparation
1. Copy English source file
2. Rename with `_sv.html` suffix
3. Update `<html lang="sv">`
4. Add all hreflang tags

### Step 2: Header Translation
1. Translate `<title>` tag
2. Translate meta description
3. Translate meta keywords (keep English technical terms where appropriate)
4. Update og:title, og:description, og:locale
5. Update canonical and alternate links

### Step 3: Schema.org Translation
1. Update headline to Swedish
2. Translate description
3. Set inLanguage to "sv"
4. Update breadcrumb item names
5. Translate articleBody excerpt

### Step 4: Content Translation
1. Translate main heading `<h1>`
2. Translate all section headings `<h2>`, `<h3>`
3. Translate paragraph content
4. Preserve technical terms in code examples
5. Keep URLs and external links unchanged
6. Translate link text but keep href targets
7. Maintain Discordian style elements

### Step 5: Navigation Translation
1. Update breadcrumb navigation
2. Translate header menu items
3. Update footer column headings
4. Translate footer navigation links
5. Update language switcher (keep current setup)

### Step 6: Quality Checks
1. Validate HTML structure
2. Verify all hreflang tags present
3. Check Swedish grammar and spelling
4. Ensure Discordian style preserved
5. Verify links work (especially Swedish versions)
6. Test responsive design hasn't broken

## Estimated Effort Per Post
- Translation time: 60-90 minutes per post
- Quality check: 15-20 minutes per post
- Total per post: ~75-110 minutes
- **Total for remaining 8 posts: 10-15 hours**

## Swedish Context Additions

### For Political Posts
- Reference Riksdagen (349 members)
- Mention Swedish political parties where relevant
- Reference Valmyndigheten (Election Authority)
- Use Swedish government structure context
- Mention Swedish media (SVT, SR, DN, SvD) where appropriate

### For Election 2026 Content
- September 2026 election date
- Eight parties in Riksdagen
- Proportional representation system
- 4% threshold
- 349 seats total

## Files to Reference
- **English Source Template**: `blog-cia-architecture.html`
- **Swedish Translation Example**: `blog-cia-architecture_sv.html`
- **Existing Swedish Content**: `blog-cia-swedish-media-election-2026_sv.html`
- **Swedish Homepage**: `index_sv.html`
- **Swedish Services**: `services_sv.html`

## Validation Checklist

### Per File
- [ ] HTML is well-formed
- [ ] All hreflang tags present and correct
- [ ] Schema.org structured data valid
- [ ] Swedish grammar checked
- [ ] Technical terms accurate
- [ ] Discordian elements preserved
- [ ] Footer links updated
- [ ] Breadcrumbs in Swedish
- [ ] No broken links

### After All Files Complete
- [ ] Update blog_sv.html to include all 9 posts
- [ ] Update sitemap_sv.html with new posts
- [ ] Verify cross-links between Swedish blog posts
- [ ] Test all navigation paths
- [ ] Run full HTML validation on all new files

## Notes
- Swedish translations should be professional but maintain the playful Discordian tone
- Technical accuracy is paramount - verify Swedish technical terms
- When in doubt about Swedish terminology, check riksdagen.se official terminology
- Preserve ALL "23 FNORD 5" signatures
- Keep English names for the three Discordian characters (Hagbard, Simon, George)

## Completion Criteria
All 9 Swedish CIA blog posts must:
1. Be complete, accurate Swedish translations
2. Preserve Discordian narrative style
3. Include proper hreflang and schema.org markup
4. Have working navigation (breadcrumbs, header, footer)
5. Be listed in blog_sv.html
6. Be included in sitemap_sv.html
7. Pass HTML validation
8. Be committed to the repository

---

**Created**: 2025-12-03
**Status**: 1/9 Complete (blog-cia-architecture_sv.html)
**Estimated Completion**: 10-15 additional hours for remaining 8 posts

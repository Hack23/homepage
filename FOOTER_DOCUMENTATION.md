# Footer Structure Documentation

This document describes the standardized footer structure used across all HTML pages on the Hack23 AB website.

## Standard Footer Format

The base footer format used across the site (as defined in `index.html`):

```html
<footer>
  <p>&copy; 2008-2025 | Hack23 AB (Org.nr 5595347807) |
    <a href="https://www.linkedin.com/in/jamessorling/">James Pether Sörling</a> |
    <a href="https://www.linkedin.com/company/hack23/">Company LinkedIn</a> |
    <a href="https://github.com/Hack23/ISMS-PUBLIC" title="Public ISMS Repository">ISMS</a> |
    <a href="https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md" title="Information Security Policy">Security Policy</a> |
    <a href="blog.html" title="Security Blog">Blog</a> |
    <a href="discordian-cybersecurity.html" title="Discordian Cybersecurity Blog">🍎 Discordian Blog</a> |
    <a href="https://hack23.com/index_sv.html" lang="sv">Swedish version</a>
  </p>
</footer>
```

## Footer Variations by Page Type

### 1. Main Site Pages
**Pages:** `index.html`, `blog.html`, `cia-triad-faq.html`, all blog posts
**Footer:** Standard footer (as above)

### 2. Localized Main Pages
**Pages:** `index_sv.html`, `index_ko.html`, `cia-triad-faq_sv.html`
**Footer:** Standard footer
**Note:** Language-specific link text may vary for Swedish/Korean versions

### 3. Product Pages - Black Trigram

**English Pages:** `black-trigram-docs.html`, `black-trigram-features.html`
**Korean Pages:** `black-trigram-docs_ko.html`, `black-trigram-features_ko.html`

**Footer Structure:**
```html
<footer>
  <p>&copy; 2008-2025 | Hack23 AB (Org.nr 5595347807) |
    [Standard links: James, LinkedIn, ISMS, Security Policy, Blog, Discordian Blog]
  </p>
  <p>
    <a href="black-trigram-docs.html" title="English documentation" lang="en">English Documentation</a> |
    <a href="black-trigram-docs_ko.html" title="Korean documentation" lang="ko">한국어 문서</a>
  </p>
</footer>
```

### 4. Product Pages - Citizen Intelligence Agency

**English Pages:** `cia-docs.html`, `cia-features.html`
**Swedish Pages:** `cia-docs_sv.html`, `cia-features_sv.html`

**Footer Structure:**
```html
<footer>
  <p>&copy; 2008-2025 | Hack23 AB (Org.nr 5595347807) |
    [Standard links]
  </p>
  <p>
    <a href="cia-docs.html" title="English documentation">English Documentation</a> |
    <a href="cia-docs_sv.html" title="Documentation in Swedish">Swedish Documentation</a>
  </p>
</footer>
```

### 5. Product Pages - CIA Compliance Manager

**English Pages:** `cia-compliance-manager-docs.html`, `cia-compliance-manager-features.html`
**Swedish Pages:** `cia-compliance-manager-docs_sv.html`, `cia-compliance-manager-features_sv.html`

**Footer Structure:**
```html
<footer>
  <p>&copy; 2008-2025 | Hack23 AB (Org.nr 5595347807) |
    [Standard links]
  </p>
  <p>
    <a href="cia-compliance-manager-docs.html" title="English documentation">English Documentation</a> |
    <a href="cia-compliance-manager-docs_sv.html" title="Swedish documentation">Swedish Documentation</a>
  </p>
</footer>
```

### 6. Discordian Blog Pages

**Pages:** All files matching `discordian-*.html` (32 files total)

**Footer Structure:**
```html
<footer>
  <p>&copy; 2008-2025 | Hack23 AB (Org.nr 5595347807) |
    [Standard links including Swedish version]
  </p>
  <p class="discordian-authors" style="margin-top: 0.5rem; font-style: italic; font-size: 0.9rem;">
    <strong>✍️ Authors:</strong>
    <a href="https://github.com/Hack23/homepage/blob/master/.github/agents/hagbard-celine.md" title="Hagbard Celine - Visionary anarchist Product Owner">Hagbard Celine</a> &
    <a href="https://github.com/Hack23/homepage/blob/master/.github/agents/simon-moon.md" title="Simon Moon - Philosopher-engineer System Architect">Simon Moon</a>
  </p>
</footer>
```

**Author Attribution:**
- **Hagbard Celine:** Visionary anarchist Product Owner (linked to `.github/agents/hagbard-celine.md`)
- **Simon Moon:** Philosopher-engineer System Architect (linked to `.github/agents/simon-moon.md`)

## Standard Footer Links

All footers include these core links:

1. **Copyright:** `© 2008-2025`
2. **Company:** Hack23 AB (Org.nr 5595347807)
3. **Personal LinkedIn:** James Pether Sörling
4. **Company LinkedIn:** Hack23 company page
5. **ISMS:** Public ISMS Repository on GitHub
6. **Security Policy:** Information Security Policy document
7. **Blog:** Main security blog
8. **Discordian Blog:** Discordian Cybersecurity blog (with 🍎 apple icon)

## Product-Specific Additions

Product pages add a second paragraph with language navigation:
- **Black Trigram:** English ↔ Korean (한국어)
- **CIA:** English ↔ Swedish (Svenska)
- **CIA Compliance Manager:** English ↔ Swedish (Svenska)

## Implementation Notes

### Updating Footers

When creating new HTML pages:

1. **Determine page type** (main site, product, discordian, localized)
2. **Copy appropriate footer template** from this documentation
3. **For Discordian pages:** Always include author attribution
4. **For product pages:** Include language navigation
5. **Maintain consistent formatting:** 2-space indentation for `<p>` tags

### Minification

All footers have been tested with HTML minification and work correctly:
- Author attribution is preserved
- Language links remain functional
- No zero-byte files created during minification
- File size reduction: 12-18% on average

### Validation

Run `html-validate *.html` to check for structural issues. Common warnings that can be ignored:
- Trailing whitespace (cosmetic)
- Inline styles (used intentionally for author attribution)
- Raw `&` characters (acceptable in href URLs)

## Maintenance

When updating the standard footer:

1. Update `index.html` footer first (the canonical reference)
2. Run the footer update script (`/tmp/update_footers.py` or equivalent)
3. Test minification on a sample of pages
4. Verify no zero-byte files created
5. Commit changes with descriptive message

## Related Files

- **Footer Update Script:** `/tmp/update_footers.py` (Python script for batch updates)
- **Standard Reference:** `index.html` (canonical footer format)
- **Agent Documentation:** `.github/agents/hagbard-celine.md`, `.github/agents/simon-moon.md`
- **Build Workflow:** `.github/workflows/main.yml` (includes minification step)

---

**Last Updated:** 2025-11-07  
**Maintained by:** Hack23 AB Development Team

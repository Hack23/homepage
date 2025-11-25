# Footer Structure Documentation

This document describes the enhanced footer structure implemented across the Hack23 AB website as of November 2025.

## Enhanced Footer Structure (November 2025)

The website now uses a comprehensive, SEO-optimized footer with improved navigation and accessibility.

### Main Site Pages Footer

**Pages:** `index.html`, `index_sv.html`, `index_ko.html`

**Structure:** 5-column grid layout with comprehensive navigation

```html
<footer role="contentinfo" aria-label="Site footer">
  <div class="footer-container">
    
    <!-- Company Info Column -->
    <div class="footer-column">
      <h2>Hack23 AB</h2>
      <p>Cybersecurity Consulting<br>
      Gothenburg, Sweden | Remote</p>
      <p>Org.nr: 5595347807</p>
      <p><a href="https://www.linkedin.com/company/hack23/" rel="noopener noreferrer" target="_blank">LinkedIn Company Page</a></p>
      <p><a href="https://www.linkedin.com/in/jamessorling/" rel="noopener noreferrer" target="_blank">CEO: James Pether Sörling</a></p>
    </div>
    
    <!-- Services Column -->
    <div class="footer-column">
      <h3>Services</h3>
      <ul>
        <li><a href="services.html">Security Consulting</a></li>
        <li><a href="services.html">Security Architecture</a></li>
        <li><a href="services.html">Cloud Security</a></li>
        <li><a href="services.html">DevSecOps Integration</a></li>
        <li><a href="services.html">Compliance & ISMS</a></li>
      </ul>
    </div>
    
    <!-- Products Column -->
    <div class="footer-column">
      <h3>Products</h3>
      <ul>
        <li><a href="black-trigram-features.html">Black Trigram</a></li>
        <li><a href="cia-features.html">Citizen Intelligence Agency</a></li>
        <li><a href="cia-compliance-manager-features.html">CIA Compliance Manager</a></li>
      </ul>
    </div>
    
    <!-- Resources Column -->
    <div class="footer-column">
      <h3>Resources</h3>
      <ul>
        <li><a href="blog.html">Security Blog</a></li>
        <li><a href="discordian-cybersecurity.html">🍎 Discordian Blog</a></li>
        <li><a href="cia-triad-faq.html">CIA Triad FAQ</a></li>
        <li><a href="https://github.com/Hack23/ISMS-PUBLIC" rel="noopener noreferrer" target="_blank">Public ISMS</a></li>
        <li><a href="sitemap.html">Sitemap</a></li>
      </ul>
    </div>
    
    <!-- Company Column -->
    <div class="footer-column">
      <h3>Company</h3>
      <ul>
        <li><a href="why-hack23.html">About Hack23</a></li>
        <li><a href="https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md" rel="noopener noreferrer" target="_blank">Security Policy</a></li>
        <li><a href="SECURITY.md">Report Security Issue</a></li>
        <li><a href="https://github.com/Hack23" rel="noopener noreferrer" target="_blank">GitHub Organization</a></li>
      </ul>
    </div>
    
  </div>
  
  <!-- Footer Bottom Bar -->
  <div class="footer-bottom">
    <p>&copy; 2008-2025 Hack23 AB. All rights reserved. | Licensed under <a href="LICENSE">Apache 2.0</a></p>
    <p>
      <a href="index.html" lang="en">English</a> | 
      <a href="index_sv.html" lang="sv">Svenska</a> | 
      <a href="index_ko.html" lang="ko">한국어</a>
    </p>
  </div>
</footer>
```

## Footer Features

### Accessibility
- **Semantic HTML**: Uses `<footer>` landmark with proper ARIA labels
- **Keyboard Navigation**: All links are keyboard accessible with visible focus indicators
- **WCAG 2.1 AA Compliant**: Color contrast ratios meet accessibility standards
- **Screen Reader Friendly**: Proper heading hierarchy and descriptive link text

### SEO Optimization
- **Comprehensive Internal Linking**: Links to all major site sections
- **Descriptive Anchor Text**: No generic "click here" links
- **Sitemap Links**: Direct access to HTML sitemap
- **Language Links**: Clear language switching in footer bottom

### Responsive Design
- **Desktop (1024px+)**: 5-column grid layout
- **Mobile (<768px)**: Single column stacked layout
- **Touch-Friendly**: Adequate spacing for mobile interaction

### CSS Classes

The footer uses the following CSS classes (defined in `styles.css`):

- `.footer-container`: Grid container for footer columns
- `.footer-column`: Individual footer column
- `.footer-bottom`: Bottom bar for copyright and language links

### Responsive Behavior

```css
/* Base: Flexible grid */
.footer-container {
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}

/* Desktop: Fixed 5-column grid */
@media (min-width: 1024px) {
  .footer-container {
    grid-template-columns: repeat(5, 1fr);
  }
}

/* Mobile: Single column */
@media (max-width: 767px) {
  .footer-container {
    grid-template-columns: 1fr;
  }
}
```

## Localized Footer Versions

### Swedish (index_sv.html)
- All column headings and link text translated to Swedish
- Links point to Swedish versions where available (e.g., `services_sv.html`)
- Maintains same structure as English version

### Korean (index_ko.html)
- All column headings and link text translated to Korean
- Links point to Korean versions where available (e.g., `services_ko.html`)
- Maintains same structure as English version

## Footer Navigation Columns

### Column 1: Company Information
- Company name and description
- Location (Gothenburg, Sweden | Remote)
- Organization number
- LinkedIn links (company and CEO)

### Column 2: Services
Links to main services page and specific service sections:
- Security Consulting
- Security Architecture
- Cloud Security
- DevSecOps Integration
- Compliance & ISMS

### Column 3: Products
Links to three main product offerings:
- Black Trigram (martial arts game)
- Citizen Intelligence Agency (political transparency)
- CIA Compliance Manager (security assessment)

### Column 4: Resources
Links to informational content:
- Security Blog
- Discordian Blog
- CIA Triad FAQ
- Public ISMS (GitHub)
- Sitemap

### Column 5: Company Links
Links to company information and policies:
- About Hack23
- Security Policy (GitHub)
- Report Security Issue
- GitHub Organization

## Footer Variations by Page Type

**Note:** Other pages (product pages, blog pages, etc.) still use the legacy simple footer format. Migration to the enhanced footer is planned for future updates.

### Legacy Footer Format (Still in Use)

Product pages and blog posts currently use a simpler footer format:

```html
<footer>
  <p>&copy; 2008-2025 | Hack23 AB (Org.nr 5595347807) |
    <a href="https://www.linkedin.com/in/jamessorling/">James Pether Sörling</a> |
    <a href="https://www.linkedin.com/company/hack23/">Company LinkedIn</a> |
    <a href="https://github.com/Hack23/ISMS-PUBLIC">ISMS</a> |
    <a href="https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md">Security Policy</a> |
    <a href="blog.html">Blog</a> |
    <a href="discordian-cybersecurity.html">🍎 Discordian Blog</a> |
    <a href="sitemap.html">Site Map</a> |
    <a href="index_sv.html" lang="sv">Swedish version</a>
  </p>
</footer>
```

### Product Pages - Black Trigram

**English Pages:** `black-trigram-docs.html`, `black-trigram-features.html`
**Korean Pages:** `black-trigram-docs_ko.html`, `black-trigram-features_ko.html`

**Footer Structure:**
```html
<footer>
  <p>&copy; 2008-2025 | Hack23 AB (Org.nr 5595347807) |
    [Standard links]
  </p>
  <p>
    <a href="black-trigram-docs.html" lang="en">English Documentation</a> |
    <a href="black-trigram-docs_ko.html" lang="ko">한국어 문서</a>
  </p>
</footer>
```

### Product Pages - Citizen Intelligence Agency

**English Pages:** `cia-docs.html`, `cia-features.html`
**Swedish Pages:** `cia-docs_sv.html`, `cia-features_sv.html`

**Footer Structure:**
```html
<footer>
  <p>&copy; 2008-2025 | Hack23 AB (Org.nr 5595347807) |
    [Standard links]
  </p>
  <p>
    <a href="cia-docs.html">English Documentation</a> |
    <a href="cia-docs_sv.html">Swedish Documentation</a>
  </p>
</footer>
```

### Product Pages - CIA Compliance Manager

**English Pages:** `cia-compliance-manager-docs.html`, `cia-compliance-manager-features.html`
**Swedish Pages:** `cia-compliance-manager-docs_sv.html`, `cia-compliance-manager-features_sv.html`

**Footer Structure:**
```html
<footer>
  <p>&copy; 2008-2025 | Hack23 AB (Org.nr 5595347807) |
    [Standard links]
  </p>
  <p>
    <a href="cia-compliance-manager-docs.html">English Documentation</a> |
    <a href="cia-compliance-manager-docs_sv.html">Swedish Documentation</a>
  </p>
</footer>
```

### Discordian Blog Pages

**Pages:** All files matching `discordian-*.html` (32 files total)

**Footer Structure:**
```html
<footer>
  <p>&copy; 2008-2025 | Hack23 AB (Org.nr 5595347807) |
    [Standard links including Swedish version]
  </p>
  <p class="discordian-authors" style="margin-top: 0.5rem; font-style: italic; font-size: 0.9rem;">
    <strong>✍️ Authors:</strong>
    <a href="https://github.com/Hack23/homepage/blob/master/.github/agents/hagbard-celine.md">Hagbard Celine</a> &
    <a href="https://github.com/Hack23/homepage/blob/master/.github/agents/simon-moon.md">Simon Moon</a>
  </p>
</footer>
```

**Author Attribution:**
- **Hagbard Celine:** Visionary anarchist Product Owner
- **Simon Moon:** Philosopher-engineer System Architect

## Implementation Notes

### CSS Styling

All footer styles are defined in `styles.css` starting at line ~1727. Key features:

- Grid-based layout with `auto-fit` for responsive columns
- CSS custom properties for consistent spacing and colors
- Hover effects and focus indicators for accessibility
- Dark mode support via `@media (prefers-color-scheme: dark)`

### Migration Strategy

To migrate other pages to the enhanced footer:

1. **Copy the enhanced footer HTML** from `index.html`
2. **Adjust links** as needed for page-specific content
3. **Update language links** to point to correct localized versions
4. **Test responsive behavior** on mobile and desktop
5. **Verify accessibility** with keyboard navigation

### Best Practices

When updating footers:

1. **Maintain semantic HTML** with proper landmarks
2. **Use descriptive link text** (not "click here")
3. **Include `rel="noopener noreferrer"` for external links**
4. **Add `target="_blank"` for external links that should open in new tabs**
5. **Use proper `lang` attributes** for language links
6. **Test keyboard navigation** and focus indicators
7. **Verify color contrast** meets WCAG 2.1 AA standards

## Standard Footer Links

All footers should include these core links:

1. **Copyright:** `© 2008-2025 Hack23 AB`
2. **Company:** Organization number 5595347807
3. **Personal LinkedIn:** James Pether Sörling
4. **Company LinkedIn:** Hack23 company page
5. **ISMS:** Public ISMS Repository on GitHub
6. **Security Policy:** Information Security Policy document
7. **Blog:** Main security blog
8. **Discordian Blog:** Discordian Cybersecurity blog (with 🍎 apple icon)
9. **Sitemap:** Link to HTML sitemap

## Maintenance

When updating the enhanced footer:

1. **Update `index.html` first** (the canonical reference)
2. **Update localized versions** (`index_sv.html`, `index_ko.html`)
3. **Test minification** to ensure no issues
4. **Verify no zero-byte files** created during build
5. **Commit with descriptive message**

## Related Files

- **CSS Styles:** `styles.css` (lines ~1727-1850)
- **English Version:** `index.html`
- **Swedish Version:** `index_sv.html`
- **Korean Version:** `index_ko.html`
- **Build Workflow:** `.github/workflows/main.yml`

---

**Last Updated:** 2025-11-25  
**Version:** 2.0 (Enhanced Footer)  
**Maintained by:** Hack23 AB Development Team

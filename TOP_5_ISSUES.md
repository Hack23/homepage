# Top 5 Priority Issues for Hack23 Homepage

This document outlines the top 5 most important issues identified for the Hack23 homepage repository. These issues are prioritized based on impact, alignment with repository goals, and the ZAP security scan findings.

---

## Issue 1: Add Subresource Integrity (SRI) to External Font Resources

**Priority:** High  
**Effort:** Small (1-2 hours)  
**Labels:** security, enhancement

### Objective
Add Subresource Integrity (SRI) attributes to all external Google Fonts links to protect against supply chain attacks and CDN compromises.

### Background
The ZAP security scan (issue #355) identified 11 instances of missing SRI attributes on external font resources. This is a security vulnerability that could allow attackers to inject malicious code if the CDN is compromised.

**Current State:**
- 0 HTML files use `integrity=` attribute
- All pages load Google Fonts without SRI protection
- Affects all 74+ HTML files in the repository

### Acceptance Criteria
- [ ] Generate SRI hashes for all Google Fonts CSS files
- [ ] Add `integrity` and `crossorigin` attributes to all font link tags
- [ ] Verify fonts still load correctly in all browsers
- [ ] Update all 74+ HTML files (English, Swedish, Korean)
- [ ] Test with different network conditions
- [ ] Document SRI update process in README or contributing guide

### Implementation Guidance

**Files to Update:**
- All `*.html` files in root directory
- All `*_sv.html` files (Swedish translations)
- All `*_ko.html` files (Korean translations)

**Current Pattern:**
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Orbitron:wght@400;500;600;700&family=Share+Tech+Mono&display=swap" rel="stylesheet">
```

**Updated Pattern:**
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Orbitron:wght@400;500;600;700&family=Share+Tech+Mono&display=swap" 
      rel="stylesheet"
      integrity="sha384-[HASH]"
      crossorigin="anonymous">
```

**Steps:**
1. Generate SRI hash: `curl -s URL | openssl dgst -sha384 -binary | openssl base64 -A`
2. Add integrity attribute to all font links
3. Test on multiple pages to ensure fonts load
4. Run ZAP scan again to verify fix

### Related Resources
- [ZAP Scan Report - Issue #355](https://github.com/Hack23/homepage/issues/355)
- [MDN: Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity)
- [SRI Hash Generator](https://www.srihash.org/)

---

## Issue 2: Implement Content Security Policy (CSP) Meta Tags

**Priority:** Critical  
**Effort:** Medium (4-6 hours)  
**Labels:** security, enhancement

### Objective
Add comprehensive Content Security Policy (CSP) meta tags to all HTML pages to mitigate XSS attacks, clickjacking, and Spectre vulnerabilities.

### Background
The ZAP security scan (issue #355) identified multiple CSP-related issues:
- **CSP: Failure to Define Directive with No Fallback** (3 instances)
- **CSP: script-src unsafe-inline** (3 instances)
- **CSP: style-src unsafe-inline** (3 instances)
- **Insufficient Site Isolation Against Spectre Vulnerability** (13 instances)

**Current State:**
- No CSP meta tags found in any HTML file
- Site vulnerable to XSS and clickjacking attacks
- No protection against Spectre-class vulnerabilities

### Acceptance Criteria
- [ ] Define comprehensive CSP policy for static site
- [ ] Add CSP meta tag to all HTML pages
- [ ] Remove or minimize `unsafe-inline` usage
- [ ] Add Cross-Origin-Embedder-Policy headers
- [ ] Add Cross-Origin-Opener-Policy headers
- [ ] Test all pages for functionality after CSP implementation
- [ ] Document CSP policy decisions and exceptions
- [ ] Verify ZAP scan issues are resolved

### Implementation Guidance

**Recommended CSP Policy:**
```html
<meta http-equiv="Content-Security-Policy" content="
  default-src 'self';
  script-src 'self' 'sha256-[HASH]' https://www.googletagmanager.com;
  style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
  font-src 'self' https://fonts.gstatic.com;
  img-src 'self' data: https:;
  connect-src 'self' https://api.githubcopilot.com;
  frame-ancestors 'none';
  base-uri 'self';
  form-action 'self';
">
<meta http-equiv="Cross-Origin-Embedder-Policy" content="require-corp">
<meta http-equiv="Cross-Origin-Opener-Policy" content="same-origin">
```

**Steps:**
1. Audit all inline scripts and styles
2. Move inline scripts to separate files or use nonces/hashes
3. Add CSP meta tags to `<head>` section of all pages
4. Test each page thoroughly
5. Adjust policy based on legitimate needs
6. Consider adding to CloudFront/S3 response headers

**Files to Update:**
- All 74+ HTML files

### Related Resources
- [ZAP Scan Report - Issue #355](https://github.com/Hack23/homepage/issues/355)
- [MDN: Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)
- [CSP Evaluator](https://csp-evaluator.withgoogle.com/)

---

## Issue 3: Enhance Accessibility with ARIA Labels and Keyboard Navigation

**Priority:** High  
**Effort:** Medium (4-8 hours)  
**Labels:** accessibility, enhancement, WCAG

### Objective
Improve website accessibility to achieve WCAG 2.1 AA compliance by adding comprehensive ARIA labels, roles, and keyboard navigation support.

### Background
**Current Accessibility State:**
- Only 14 aria attributes found across all HTML files
- Only 4 files have ARIA roles defined
- No comprehensive keyboard navigation patterns
- Navigation menus lack proper ARIA structure
- Interactive elements may not be keyboard accessible

**Impact:**
- Screen reader users have difficulty navigating
- Keyboard-only users cannot access all features
- May exclude users with disabilities
- Fails WCAG 2.1 AA compliance requirements

### Acceptance Criteria
- [ ] Add ARIA labels to all navigation elements
- [ ] Implement proper heading hierarchy (h1-h6)
- [ ] Add `role` attributes to semantic sections
- [ ] Ensure all interactive elements are keyboard accessible
- [ ] Add `aria-label` to icon-only buttons
- [ ] Implement focus indicators for keyboard navigation
- [ ] Add skip-to-content links
- [ ] Test with screen readers (NVDA/JAWS)
- [ ] Validate color contrast ratios (4.5:1 minimum)
- [ ] Update all language variants (English, Swedish, Korean)

### Implementation Guidance

**Priority Areas:**

1. **Navigation Menus:**
```html
<nav role="navigation" aria-label="Main navigation">
  <ul role="menubar">
    <li role="menuitem"><a href="/">Home</a></li>
    <!-- ... -->
  </ul>
</nav>
```

2. **Main Content Sections:**
```html
<main role="main" aria-label="Main content">
  <section aria-labelledby="services-heading">
    <h2 id="services-heading">Security Services</h2>
    <!-- ... -->
  </section>
</main>
```

3. **Interactive Elements:**
```html
<button aria-label="Open menu" aria-expanded="false">
  <span aria-hidden="true">☰</span>
</button>
```

4. **Skip Links:**
```html
<a href="#main-content" class="skip-link">Skip to main content</a>
```

**Files to Update:**
- All HTML files (prioritize main pages first)
- `styles.css` (focus indicators, skip link styles)

### Testing Checklist
- [ ] Test with keyboard only (Tab, Enter, Space, Arrow keys)
- [ ] Test with screen reader (NVDA on Windows / VoiceOver on Mac)
- [ ] Run axe DevTools or WAVE accessibility checker
- [ ] Verify color contrast with contrast checker
- [ ] Test focus indicators are visible

### Related Resources
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [WebAIM Keyboard Accessibility](https://webaim.org/techniques/keyboard/)

---

## Issue 4: Complete Korean Translations for Key Pages

**Priority:** Medium  
**Effort:** Medium (4-6 hours per page)  
**Labels:** internationalization, documentation

### Objective
Complete Korean translations for key pages to match Swedish translation coverage and honor the founder's Taekwondo background.

### Background
**Current Translation Status:**
- Swedish translations: 6 pages (`*_sv.html`)
- Korean translations: 3 pages (`*_ko.html`)
- Gap: 3 pages need Korean translation

**Missing Korean Translations:**
1. `cia-docs.html` → needs `cia-docs_ko.html`
2. `cia-compliance-manager-docs.html` → needs `cia-compliance-manager-docs_ko.html`
3. One additional page from the Swedish set

**Cultural Significance:**
James Pether Sörling's Taekwondo background (black belt, Swedish champion) connects to Korean martial arts tradition. Korean translation demonstrates cultural respect and expands reach to Korean cybersecurity professionals.

### Acceptance Criteria
- [ ] Identify 3 missing pages that have Swedish but not Korean translations
- [ ] Create Korean translations for all identified pages
- [ ] Ensure technical terminology is accurate in Korean
- [ ] Add `lang="ko"` attribute to HTML tag
- [ ] Update hreflang links in all related pages
- [ ] Add Korean pages to sitemap.xml
- [ ] Verify Korean fonts load correctly
- [ ] Test responsive design with Korean text
- [ ] Have translations reviewed by Korean speaker if possible

### Implementation Guidance

**Translation Process:**
1. Identify pages: `ls -1 *_sv.html | while read f; do base="${f%_sv.html}"; [ ! -f "${base}_ko.html" ] && echo "$base"; done`
2. Use existing Korean pages as templates for structure
3. Translate content (consider professional translation service)
4. Update navigation and hreflang tags
5. Add to sitemap.xml

**Pages to Translate (Priority Order):**
1. `cia-docs_ko.html` (most important project documentation)
2. `cia-compliance-manager-docs_ko.html` (compliance tool documentation)
3. Additional page based on Swedish coverage

**Files to Update:**
- New `*_ko.html` files (3 pages)
- Update hreflang in corresponding English and Swedish pages
- `sitemap.xml`
- Navigation menus in existing Korean pages

### Quality Checks
- [ ] Korean technical terms accurate and consistent
- [ ] Proper Korean punctuation and spacing
- [ ] Korean fonts display correctly (Inter, Orbitron)
- [ ] Layout works with Korean text (longer/shorter than English)
- [ ] All links work correctly
- [ ] Meta tags and descriptions translated

### Related Resources
- [Korean Language Technical Writing Guide](https://www.korean.go.kr/)
- [Microsoft Korean Style Guide](https://docs.microsoft.com/en-us/globalization/localization/ministyleguides)
- Existing Korean pages as templates: `index_ko.html`, `black-trigram-features_ko.html`, `black-trigram-docs_ko.html`

---

## Issue 5: Optimize Lighthouse Performance Budget for Mobile

**Priority:** Medium  
**Effort:** Small (1-2 hours)  
**Labels:** performance, optimization

### Objective
Update `budget.json` to include realistic mobile-specific performance budgets and align with modern web performance best practices.

### Background
**Current Budget Configuration:**
```json
{
  "total": 10000000,  // 10MB - unrealistic for mobile
  "script": 1000,     // 1KB - too restrictive
  "interactive": 7500,
  "first-contentful-paint": 5000
}
```

**Issues:**
- Total budget of 10MB is unrealistic and defeats purpose of budgets
- No mobile-specific budgets defined
- Missing key performance metrics (LCP, CLS, INP)
- Script budget of 1KB is too restrictive for Google Fonts
- No separate budgets for different page types

### Acceptance Criteria
- [ ] Research and set realistic performance budgets based on industry standards
- [ ] Add mobile-specific budgets (separate from desktop)
- [ ] Include Core Web Vitals metrics (LCP, FID/INP, CLS)
- [ ] Set appropriate budgets for different resource types
- [ ] Document budget rationale and targets
- [ ] Configure Lighthouse CI to enforce budgets
- [ ] Test against actual site performance
- [ ] Adjust budgets based on current baseline

### Implementation Guidance

**Recommended Budget Configuration:**
```json
[
  {
    "path": "/*",
    "timings": [
      {
        "metric": "interactive",
        "budget": 5000
      },
      {
        "metric": "first-contentful-paint",
        "budget": 2000
      },
      {
        "metric": "largest-contentful-paint",
        "budget": 2500
      },
      {
        "metric": "cumulative-layout-shift",
        "budget": 0.1
      }
    ],
    "resourceSizes": [
      {
        "resourceType": "script",
        "budget": 100000
      },
      {
        "resourceType": "stylesheet",
        "budget": 50000
      },
      {
        "resourceType": "image",
        "budget": 200000
      },
      {
        "resourceType": "font",
        "budget": 100000
      },
      {
        "resourceType": "document",
        "budget": 50000
      },
      {
        "resourceType": "total",
        "budget": 500000
      }
    ],
    "resourceCounts": [
      {
        "resourceType": "third-party",
        "budget": 10
      },
      {
        "resourceType": "script",
        "budget": 10
      }
    ]
  },
  {
    "path": "/blog*.html",
    "timings": [
      {
        "metric": "interactive",
        "budget": 6000
      }
    ],
    "resourceSizes": [
      {
        "resourceType": "total",
        "budget": 600000
      }
    ]
  }
]
```

**Performance Targets:**
- **Total Size:** 500KB (mobile), 750KB (desktop)
- **Time to Interactive:** < 5s (mobile), < 3s (desktop)
- **First Contentful Paint:** < 2s
- **Largest Contentful Paint:** < 2.5s
- **Cumulative Layout Shift:** < 0.1

**Files to Update:**
- `budget.json`
- `.github/workflows/main.yml` (if Lighthouse config needs updates)

### Testing Steps
1. Run Lighthouse audit on current site: `npm install -g lighthouse && lighthouse https://hack23.com --view`
2. Document current performance baseline
3. Set budgets 20% better than current baseline
4. Test budget enforcement in CI pipeline
5. Adjust as needed based on real-world results

### Related Resources
- [Lighthouse Performance Budgets](https://web.dev/performance-budgets-101/)
- [Core Web Vitals](https://web.dev/vitals/)
- [Budget.json Schema](https://github.com/GoogleChrome/lighthouse/blob/master/docs/performance-budgets.md)
- Current budget: `/home/runner/work/homepage/homepage/budget.json`

---

## Summary

These 5 issues address critical areas for improvement:

1. **Security** (Issues #1, #2): Address ZAP scan findings and harden against attacks
2. **Accessibility** (Issue #3): Ensure WCAG 2.1 AA compliance and inclusive design
3. **Internationalization** (Issue #4): Complete Korean translation coverage
4. **Performance** (Issue #5): Establish realistic performance monitoring

**Total Estimated Effort:** 15-24 hours  
**Recommended Priority Order:** 2 → 1 → 3 → 5 → 4

All issues align with the repository's commitment to security, transparency, and professional excellence in cybersecurity consulting.

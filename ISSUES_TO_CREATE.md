# GitHub Issues to Create for Hack23/homepage

This file contains the full specifications for 5 priority issues that need to be created in the GitHub repository.

---

## Issue 1: Add Subresource Integrity (SRI) to External Font Resources

**Title:** Add Subresource Integrity (SRI) to External Font Resources

**Labels:** `security`, `enhancement`

**Priority:** High

**Body:**

## 🎯 Objective
Add Subresource Integrity (SRI) attributes to all external Google Fonts links to protect against supply chain attacks and CDN compromises.

## 📊 Background
The ZAP security scan (issue #355) identified 11 instances of missing SRI attributes on external font resources. This is a security vulnerability that could allow attackers to inject malicious code if the CDN is compromised.

**Current State:**
- 0 HTML files use `integrity=` attribute  
- All pages load Google Fonts without SRI protection
- Affects all 74+ HTML files in the repository

**Discovery Method:** Automated ZAP security scan

## 🔍 Analysis
**Impact Assessment:**
- **Severity:** Medium-High (supply chain vulnerability)
- **Affected Pages:** All 74+ HTML files
- **Risk:** Malicious code injection if Google Fonts CDN compromised
- **ISMS Alignment:** Violates secure development practices (ISO 27001 A.14.2.5)

## ✅ Acceptance Criteria
- [ ] Generate SRI hashes for all Google Fonts CSS files
- [ ] Add `integrity` and `crossorigin` attributes to all font link tags
- [ ] Verify fonts still load correctly in all browsers
- [ ] Update all 74+ HTML files (English, Swedish, Korean)
- [ ] Test with different network conditions
- [ ] Document SRI update process in README or contributing guide

## 🛠️ Implementation Guidance

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

**Automation Suggestion:**
```bash
# Script to update all HTML files
for file in *.html *_sv.html *_ko.html; do
  sed -i 's|<link href="https://fonts.googleapis.com/css2[^>]*rel="stylesheet">|<link href="..." rel="stylesheet" integrity="sha384-..." crossorigin="anonymous">|g' "$file"
done
```

## 🏷️ ISMS Alignment
**Relevant Policies:**
- Secure Development Lifecycle (ISO 27001 A.14.2)
- Supply Chain Security (NIST CSF PR.DS-6)
- Third-Party Risk Management

**Compliance Impact:**
- Reduces supply chain attack surface
- Demonstrates proactive security measures
- Aligns with transparency principle of public ISMS

## 🔗 Related Resources
- [ZAP Scan Report - Issue #355](https://github.com/Hack23/homepage/issues/355)
- [MDN: Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity)
- [SRI Hash Generator](https://www.srihash.org/)
- [Complete Details in TOP_5_ISSUES.md](https://github.com/Hack23/homepage/blob/copilot/create-top-five-issues/TOP_5_ISSUES.md#issue-1)

## 👥 Recommended Assignment
**Primary:** @ui-enhancement-specialist  
**Collaborate with:** @george-dorn (for testing and validation)

**Rationale:** UI specialist has expertise in HTML/CSS modifications and can efficiently update all template files while ensuring consistency across language variants.

---

## Issue 2: Implement Content Security Policy (CSP) Meta Tags

**Title:** Implement Content Security Policy (CSP) Meta Tags

**Labels:** `security`, `enhancement`

**Priority:** Critical

**Body:**

## 🎯 Objective
Add comprehensive Content Security Policy (CSP) meta tags to all HTML pages to mitigate XSS attacks, clickjacking, and Spectre vulnerabilities.

## 📊 Background
The ZAP security scan (issue #355) identified multiple CSP-related issues:
- **CSP: Failure to Define Directive with No Fallback** (3 instances)
- **CSP: script-src unsafe-inline** (3 instances)
- **CSP: style-src unsafe-inline** (3 instances)
- **Insufficient Site Isolation Against Spectre Vulnerability** (13 instances)

**Current State:**
- No CSP meta tags found in any HTML file
- Site vulnerable to XSS and clickjacking attacks
- No protection against Spectre-class vulnerabilities

**Discovery Method:** ZAP security scan (Issue #355)

## 🔍 Analysis
**Security Impact:**
- **Severity:** Critical (multiple attack vectors unmitigated)
- **Vulnerabilities:** XSS, clickjacking, Spectre-class attacks
- **Affected Pages:** All 74+ HTML files
- **ISMS Impact:** Major compliance gap in security controls

**Technical Analysis:**
- Static site allows for strict CSP implementation
- No inline scripts currently (advantage for CSP)
- External resources limited to Google Fonts and potential analytics
- Can implement defense-in-depth with multiple policies

## ✅ Acceptance Criteria
- [ ] Define comprehensive CSP policy for static site
- [ ] Add CSP meta tag to all HTML pages
- [ ] Remove or minimize `unsafe-inline` usage
- [ ] Add Cross-Origin-Embedder-Policy headers
- [ ] Add Cross-Origin-Opener-Policy headers
- [ ] Test all pages for functionality after CSP implementation
- [ ] Document CSP policy decisions and exceptions
- [ ] Verify ZAP scan issues are resolved

## 🛠️ Implementation Guidance

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

**Implementation Steps:**
1. **Audit Phase:**
   - Identify all inline scripts and styles
   - Document all external resource dependencies
   - List all legitimate use cases

2. **Policy Design:**
   - Start with strict policy
   - Add exceptions only as needed
   - Use hashes instead of 'unsafe-inline' where possible

3. **Implementation:**
   - Add meta tags to `<head>` section of all pages
   - Test each page thoroughly
   - Adjust policy based on legitimate needs

4. **Enhancement (Optional):**
   - Consider adding to CloudFront/S3 response headers for redundancy
   - Implement CSP reporting endpoint

**Files to Update:**
- All 74+ HTML files
- Consider `.github/workflows/main.yml` for deployment headers

**Testing Strategy:**
```bash
# Check CSP implementation
grep -r "Content-Security-Policy" *.html | wc -l

# Test for violations in browser console
# Open developer tools → Console → Check for CSP warnings
```

## 🏷️ ISMS Alignment
**Relevant Policies:**
- Web Application Security (ISO 27001 A.14.2.5)
- Security by Design (NIST CSF PR.IP-2)
- Defense in Depth (CIS Control 18)

**Compliance Frameworks:**
- **ISO 27001:** A.14.2 (Security in development and support processes)
- **NIST CSF:** PR.DS (Data Security), PR.IP (Information Protection)
- **CIS Controls:** Control 18 (Application Software Security)

**Classification:** Public website (confidentiality: low, integrity: high, availability: high)

## 🔗 Related Resources
- [ZAP Scan Report - Issue #355](https://github.com/Hack23/homepage/issues/355)
- [MDN: Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)
- [CSP Evaluator](https://csp-evaluator.withgoogle.com/)
- [Complete Details in TOP_5_ISSUES.md](https://github.com/Hack23/homepage/blob/copilot/create-top-five-issues/TOP_5_ISSUES.md#issue-2)

## 👥 Recommended Assignment
**Primary:** @george-dorn (Developer)  
**Collaborate with:** @simon-moon (for architecture review), @ui-enhancement-specialist (for HTML updates)

**Rationale:** This requires careful security engineering and testing to avoid breaking functionality. George's development expertise combined with Simon's architectural oversight ensures robust implementation.

---

## Issue 3: Enhance Accessibility with ARIA Labels and Keyboard Navigation

**Title:** Enhance Accessibility with ARIA Labels and Keyboard Navigation

**Labels:** `accessibility`, `enhancement`, `WCAG`

**Priority:** High

**Body:**

## 🎯 Objective
Improve website accessibility to achieve WCAG 2.1 AA compliance by adding comprehensive ARIA labels, roles, and keyboard navigation support.

## 📊 Background
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
- Does not align with Hack23's commitment to inclusive security

**Discovery Method:** Code analysis and WCAG 2.1 audit

## 🔍 Analysis
**Accessibility Gaps Identified:**

1. **Navigation Structure:**
   - Missing `role="navigation"` attributes
   - No `aria-label` for navigation regions
   - Menu items lack proper ARIA attributes

2. **Content Hierarchy:**
   - Potential heading hierarchy issues
   - Missing `role="main"` for main content
   - Sections lack `aria-labelledby` references

3. **Interactive Elements:**
   - Icon buttons may lack accessible names
   - No skip-to-content links
   - Focus indicators may be insufficient

4. **Language Support:**
   - All three language variants need updates
   - ARIA labels must be translated appropriately

**WCAG 2.1 AA Requirements:**
- 1.3.1 Info and Relationships (Level A)
- 2.1.1 Keyboard (Level A)
- 2.4.1 Bypass Blocks (Level A)
- 2.4.6 Headings and Labels (Level AA)
- 4.1.2 Name, Role, Value (Level A)

## ✅ Acceptance Criteria
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

## 🛠️ Implementation Guidance

**Priority Areas:**

### 1. Navigation Menus
```html
<nav role="navigation" aria-label="Main navigation">
  <ul role="menubar">
    <li role="menuitem"><a href="/">Home</a></li>
    <li role="menuitem"><a href="/services.html">Services</a></li>
    <!-- ... -->
  </ul>
</nav>
```

### 2. Main Content Sections
```html
<main role="main" aria-label="Main content" id="main-content">
  <section aria-labelledby="services-heading">
    <h2 id="services-heading">Security Services</h2>
    <!-- ... -->
  </section>
</main>
```

### 3. Interactive Elements
```html
<button aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu">
  <span aria-hidden="true">☰</span>
</button>
```

### 4. Skip Links
```html
<a href="#main-content" class="skip-link">Skip to main content</a>

<!-- CSS for skip links -->
<style>
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: #000;
  color: #fff;
  padding: 8px;
  z-index: 100;
}

.skip-link:focus {
  top: 0;
}
</style>
```

### 5. Focus Indicators
```css
/* Add to styles.css */
:focus {
  outline: 2px solid #00d4ff;
  outline-offset: 2px;
}

:focus:not(:focus-visible) {
  outline: none;
}

:focus-visible {
  outline: 2px solid #00d4ff;
  outline-offset: 2px;
}
```

**Files to Update:**
- All HTML files (prioritize main pages first: `index.html`, `index_sv.html`, `index_ko.html`)
- `styles.css` (focus indicators, skip link styles)
- Project pages: `cia-docs.html`, `black-trigram-docs.html`, etc.

**Implementation Phases:**
1. **Phase 1 (Critical):** Main pages and navigation
2. **Phase 2 (Important):** Project pages and documentation
3. **Phase 3 (Complete):** Blog posts and detailed content pages

## Testing Checklist
- [ ] Test with keyboard only (Tab, Enter, Space, Arrow keys)
- [ ] Test with screen reader (NVDA on Windows / VoiceOver on Mac)
- [ ] Run axe DevTools or WAVE accessibility checker
- [ ] Verify color contrast with contrast checker
- [ ] Test focus indicators are visible
- [ ] Validate HTML with Nu HTML Checker
- [ ] Test on mobile devices with screen reader

**Testing Tools:**
- [axe DevTools](https://www.deque.com/axe/devtools/)
- [WAVE Browser Extension](https://wave.webaim.org/extension/)
- [Color Contrast Analyzer](https://www.tpgi.com/color-contrast-checker/)
- [Nu HTML Checker](https://validator.w3.org/nu/)

## 🏷️ ISMS Alignment
**Relevant Policies:**
- Inclusive Security Design
- User Experience Standards
- Web Accessibility Policy (WCAG 2.1 AA)

**Compliance Frameworks:**
- **WCAG 2.1 Level AA:** Web accessibility standard
- **Section 508:** US federal accessibility requirement
- **EN 301 549:** European accessibility standard
- **ISO 27001 A.7.1.1:** Screening (inclusive of accessibility needs)

**Business Value:**
- Expands potential client base
- Demonstrates inclusive values
- Reduces legal/compliance risk
- Improves SEO and usability for all users

## 🔗 Related Resources
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [WebAIM Keyboard Accessibility](https://webaim.org/techniques/keyboard/)
- [Complete Details in TOP_5_ISSUES.md](https://github.com/Hack23/homepage/blob/copilot/create-top-five-issues/TOP_5_ISSUES.md#issue-3)

## 👥 Recommended Assignment
**Primary:** @ui-enhancement-specialist  
**Collaborate with:** @george-dorn (for testing), @marketing-specialist (for accessible messaging)

**Rationale:** UI Enhancement Specialist has deep WCAG 2.1 AA expertise and can efficiently implement accessibility improvements across all pages while maintaining design consistency.

---

## Issue 4: Complete Korean Translations for Key Pages

**Title:** Complete Korean Translations for Key Pages

**Labels:** `internationalization`, `documentation`

**Priority:** Medium

**Body:**

## 🎯 Objective
Complete Korean translations for key pages to match Swedish translation coverage and honor the founder's Taekwondo background.

## �� Background
**Current Translation Status:**
- Swedish translations: 6 pages (`*_sv.html`)
- Korean translations: 3 pages (`*_ko.html`)
- Gap: 3 pages need Korean translation

**Missing Korean Translations:**
1. `cia-docs.html` → needs `cia-docs_ko.html`
2. `cia-compliance-manager-docs.html` → needs `cia-compliance-manager-docs_ko.html`
3. Additional pages from Swedish set (to be identified)

**Cultural Significance:**
James Pether Sörling's Taekwondo background (black belt, Swedish champion) connects to Korean martial arts tradition. Korean translation demonstrates:
- Cultural respect and awareness
- Commitment to international reach
- Recognition of Korean cybersecurity market
- Personal connection to Korean culture through martial arts

**Market Opportunity:**
- Korea has advanced cybersecurity industry
- Strong demand for security consulting
- Cultural alignment through Taekwondo connection
- Potential partnerships with Korean firms

**Discovery Method:** Repository analysis comparing Swedish and Korean translation coverage

## 🔍 Analysis
**Translation Gap Analysis:**

Existing Korean pages:
1. ✅ `index_ko.html` (homepage)
2. ✅ `black-trigram-features_ko.html`
3. ✅ `black-trigram-docs_ko.html`

Existing Swedish pages (need Korean equivalents):
1. ❌ `cia-docs_sv.html` → missing `cia-docs_ko.html`
2. ❌ `cia-compliance-manager-docs_sv.html` → missing `cia-compliance-manager-docs_ko.html`
3. ❌ `cia-compliance-manager-features_sv.html` → missing `cia-compliance-manager-features_ko.html`
4. ✅ `index_sv.html` → has `index_ko.html`
5. ❌ `cia-features_sv.html` → missing `cia-features_ko.html`

**Priority Ranking:**
1. **High:** `cia-docs_ko.html` (core project documentation)
2. **High:** `cia-compliance-manager-docs_ko.html` (enterprise product)
3. **Medium:** `cia-features_ko.html` (feature overview)
4. **Medium:** `cia-compliance-manager-features_ko.html` (product features)

## ✅ Acceptance Criteria
- [ ] Identify all pages with Swedish but not Korean translations
- [ ] Create Korean translations for at least 3 priority pages
- [ ] Ensure technical terminology is accurate in Korean
- [ ] Add `lang="ko"` attribute to HTML tag
- [ ] Update hreflang links in all related pages
- [ ] Add Korean pages to sitemap.xml
- [ ] Verify Korean fonts load correctly (Inter, Orbitron)
- [ ] Test responsive design with Korean text
- [ ] Have translations reviewed by native Korean speaker if possible
- [ ] Ensure consistent terminology across all Korean pages

## 🛠️ Implementation Guidance

**Translation Process:**

### Step 1: Identify Pages
```bash
# List Swedish pages without Korean equivalents
cd /home/runner/work/homepage/homepage
for file in *_sv.html; do
  base="${file%_sv.html}"
  ko_file="${base}_ko.html"
  if [ ! -f "$ko_file" ]; then
    echo "Missing: $ko_file (has $file)"
  fi
done
```

### Step 2: Translation Approach
**Options:**
1. **Professional Translation Service** (Recommended)
   - Use service like Gengo, Smartling, or Translated
   - Specify domain: Technical/cybersecurity
   - Provide glossary of key terms

2. **Machine Translation + Human Review**
   - Use DeepL or Google Translate for initial draft
   - Have native Korean speaker review and refine
   - Ensure technical accuracy

3. **Hybrid Approach**
   - Machine translate non-technical content
   - Professional translation for technical terms
   - Native speaker final review

### Step 3: Template Structure
Use existing Korean pages as templates:
```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Korean Title] - Hack23</title>
  <meta name="description" content="[Korean description]">
  
  <!-- hreflang tags -->
  <link rel="alternate" hreflang="en" href="https://hack23.com/[page].html">
  <link rel="alternate" hreflang="sv" href="https://hack23.com/[page]_sv.html">
  <link rel="alternate" hreflang="ko" href="https://hack23.com/[page]_ko.html">
  <link rel="alternate" hreflang="x-default" href="https://hack23.com/[page].html">
  
  <!-- Rest of head -->
</head>
<body>
  <!-- Korean content -->
</body>
</html>
```

### Step 4: Technical Terminology Glossary
Key terms to maintain consistency:

| English | Korean | Notes |
|---------|--------|-------|
| Cybersecurity | 사이버 보안 | Standard term |
| Open Source Intelligence | 오픈 소스 인텔리전스 (OSINT) | Keep acronym |
| Compliance | 규정 준수 | Formal term |
| Risk Assessment | 위험 평가 | Standard translation |
| Transparency | 투명성 | Core value |
| Information Security Management System | 정보 보안 관리 시스템 (ISMS) | Keep acronym |

### Step 5: Update Related Files
**Files to modify:**
- New `*_ko.html` files (3-4 pages)
- Update hreflang in corresponding English pages
- Update hreflang in corresponding Swedish pages
- Update `sitemap.xml` with new Korean URLs
- Update navigation menus in existing Korean pages

**Sitemap update example:**
```xml
<url>
  <loc>https://hack23.com/cia-docs_ko.html</loc>
  <lastmod>2025-11-16</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
  <xhtml:link rel="alternate" hreflang="en" href="https://hack23.com/cia-docs.html"/>
  <xhtml:link rel="alternate" hreflang="sv" href="https://hack23.com/cia-docs_sv.html"/>
  <xhtml:link rel="alternate" hreflang="ko" href="https://hack23.com/cia-docs_ko.html"/>
</url>
```

## Quality Checks
- [ ] Korean technical terms accurate and consistent
- [ ] Proper Korean punctuation and spacing (e.g., no spaces before punctuation)
- [ ] Korean fonts display correctly (Inter supports Hangul)
- [ ] Layout works with Korean text (may be longer/shorter than English)
- [ ] All links work correctly (internal and external)
- [ ] Meta tags and descriptions translated
- [ ] Navigation translated consistently
- [ ] Hreflang tags configured properly
- [ ] Language switcher works on all pages
- [ ] Mobile responsive with Korean text

**Validation Tools:**
- [Korean Language Checker](https://korean.go.kr/front/onlineQna/onlineQnaList.do)
- [HTML Validator](https://validator.w3.org/)
- Browser testing with Korean locale

## 🏷️ ISMS Alignment
**Relevant Policies:**
- Communication Strategy
- International Business Development
- Cultural Sensitivity and Inclusion

**Business Value:**
- Expands international market reach
- Demonstrates cultural respect
- Honors founder's Korean martial arts background
- Positions for Korean market entry
- Differentiates from competitors

**Strategic Alignment:**
- Supports Hack23's transparency mission globally
- Enables Korean security professionals to access ISMS
- Facilitates potential Korean partnerships
- Demonstrates commitment to inclusive security

## 🔗 Related Resources
- [Korean Language Technical Writing Guide](https://www.korean.go.kr/)
- [Microsoft Korean Style Guide](https://docs.microsoft.com/en-us/globalization/localization/ministyleguides)
- Existing Korean pages as templates: `index_ko.html`, `black-trigram-features_ko.html`, `black-trigram-docs_ko.html`
- [Complete Details in TOP_5_ISSUES.md](https://github.com/Hack23/homepage/blob/copilot/create-top-five-issues/TOP_5_ISSUES.md#issue-4)
- [James Pether Sörling's Taekwondo Background](https://hack23.com/index.html#about)

## 👥 Recommended Assignment
**Primary:** @marketing-specialist  
**Collaborate with:** @ui-enhancement-specialist (for HTML implementation), @business-development-specialist (for market context)

**Rationale:** Marketing specialist can coordinate professional translation services and ensure messaging consistency, while UI specialist handles technical implementation and responsive design validation.

---

## Issue 5: Optimize Lighthouse Performance Budget for Mobile

**Title:** Optimize Lighthouse Performance Budget for Mobile

**Labels:** `performance`, `optimization`

**Priority:** Medium

**Body:**

## 🎯 Objective
Update `budget.json` to include realistic mobile-specific performance budgets and align with modern web performance best practices.

## 📊 Background
**Current Budget Configuration:**
```json
{
  "total": 10000000,  // 10MB - unrealistic for mobile
  "script": 1000,     // 1KB - too restrictive
  "interactive": 7500,
  "first-contentful-paint": 5000
}
```

**Issues Identified:**
- Total budget of 10MB is unrealistic and defeats purpose of performance budgets
- No mobile-specific budgets defined
- Missing key performance metrics (LCP, CLS, INP)
- Script budget of 1KB is too restrictive for Google Fonts and other legitimate scripts
- No separate budgets for different page types
- Current format may not be compatible with latest Lighthouse CI

**Discovery Method:** Code review and performance audit preparation

## 🔍 Analysis
**Current Performance Baseline Needed:**
To set realistic budgets, we need to:
1. Run Lighthouse audit on current site
2. Document baseline metrics
3. Set improvement targets (typically 10-20% better than baseline)
4. Configure budgets for enforcement

**Industry Benchmarks:**
- **Total Page Weight:** 
  - Mobile: 300-500KB (target), 1-2MB (acceptable)
  - Desktop: 500-750KB (target), 2-3MB (acceptable)
- **Time to Interactive:** 
  - Mobile: <5s (target), <10s (acceptable)
  - Desktop: <3s (target), <5s (acceptable)
- **Core Web Vitals:**
  - LCP: <2.5s (good), 2.5-4s (needs improvement)
  - FID/INP: <100ms (good), 100-300ms (needs improvement)
  - CLS: <0.1 (good), 0.1-0.25 (needs improvement)

**Current Site Characteristics:**
- Static HTML/CSS (advantage)
- External Google Fonts (optimization opportunity)
- Minimal JavaScript (advantage)
- Image-light content (advantage)
- Should achieve excellent performance scores

## ✅ Acceptance Criteria
- [ ] Research and set realistic performance budgets based on industry standards
- [ ] Add mobile-specific budgets (separate from desktop if needed)
- [ ] Include Core Web Vitals metrics (LCP, FID/INP, CLS)
- [ ] Set appropriate budgets for different resource types
- [ ] Document budget rationale and targets
- [ ] Configure Lighthouse CI to enforce budgets in GitHub Actions
- [ ] Test against actual site performance
- [ ] Adjust budgets based on current baseline
- [ ] Ensure budget format is compatible with latest Lighthouse CI

## 🛠️ Implementation Guidance

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
      },
      {
        "metric": "total-blocking-time",
        "budget": 300
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
      },
      {
        "metric": "largest-contentful-paint",
        "budget": 3000
      }
    ],
    "resourceSizes": [
      {
        "resourceType": "total",
        "budget": 600000
      }
    ]
  },
  {
    "path": "/index*.html",
    "timings": [
      {
        "metric": "interactive",
        "budget": 4000
      },
      {
        "metric": "first-contentful-paint",
        "budget": 1500
      },
      {
        "metric": "largest-contentful-paint",
        "budget": 2000
      }
    ],
    "resourceSizes": [
      {
        "resourceType": "total",
        "budget": 400000
      }
    ]
  }
]
```

**Performance Targets:**

| Metric | Mobile Target | Desktop Target | Notes |
|--------|--------------|----------------|-------|
| Total Size | 500KB | 750KB | Includes all resources |
| Time to Interactive | < 5s | < 3s | Full interactivity |
| First Contentful Paint | < 2s | < 1.5s | First visual content |
| Largest Contentful Paint | < 2.5s | < 2s | Main content visible |
| Cumulative Layout Shift | < 0.1 | < 0.1 | Visual stability |
| Total Blocking Time | < 300ms | < 200ms | Main thread blocking |

**Implementation Steps:**

### Step 1: Baseline Performance Audit
```bash
# Install Lighthouse CLI
npm install -g lighthouse

# Run audit on current site
lighthouse https://hack23.com --output html --output-path ./lighthouse-report.html --view

# Run on multiple pages
for page in index.html cia-docs.html black-trigram-docs.html; do
  lighthouse https://hack23.com/$page --output json --output-path ./lighthouse-$page.json
done
```

### Step 2: Analyze Results
- Document current metrics
- Identify performance bottlenecks
- Set realistic improvement targets (typically 10-20% better)

### Step 3: Update budget.json
- Replace current configuration with new format
- Set budgets based on baseline + improvement target
- Include multiple path patterns for different page types

### Step 4: Configure GitHub Actions
Update `.github/workflows/main.yml` to enforce budgets:
```yaml
- name: Lighthouse CI
  uses: treosh/lighthouse-ci-action@v9
  with:
    urls: |
      https://hack23.com
      https://hack23.com/cia-docs.html
    budgetPath: ./budget.json
    uploadArtifacts: true
    temporaryPublicStorage: true
```

### Step 5: Test and Adjust
- Run workflow with new budgets
- Review failures and adjust thresholds if needed
- Document any exceptions or justifications

**Files to Update:**
- `budget.json` (primary change)
- `.github/workflows/main.yml` (if Lighthouse config needs updates)
- `README.md` (document performance targets)

## Testing Steps
1. ✅ Run Lighthouse audit on current site
2. ✅ Document current performance baseline
3. ✅ Update `budget.json` with realistic targets
4. ✅ Test locally: `npx lighthouse-ci --budget-path budget.json`
5. ✅ Commit and push to trigger GitHub Actions
6. ✅ Review Lighthouse CI results
7. ✅ Adjust budgets if needed based on real-world results
8. ✅ Document final budget rationale

**Validation Commands:**
```bash
# Validate budget.json format
cat budget.json | jq .

# Test budget against live site
npx lighthouse-ci assert --budgetPath=budget.json https://hack23.com
```

## 🏷️ ISMS Alignment
**Relevant Policies:**
- Service Level Standards
- User Experience Policy
- Performance Monitoring

**Compliance Frameworks:**
- **ISO 27001 A.12.1.3:** Capacity management
- **NIST CSF:** Availability and performance monitoring
- **CIS Control 12:** Network Infrastructure Management

**Business Value:**
- Improved user experience (faster load times)
- Better SEO rankings (Core Web Vitals are ranking factors)
- Reduced bounce rates
- Lower bandwidth costs
- Mobile-first optimization
- Competitive advantage

**Monitoring & Continuous Improvement:**
- Automated budget enforcement in CI/CD
- Regular performance audits
- Trend analysis over time
- Proactive performance optimization

## 🔗 Related Resources
- [Lighthouse Performance Budgets](https://web.dev/performance-budgets-101/)
- [Core Web Vitals](https://web.dev/vitals/)
- [Budget.json Schema](https://github.com/GoogleChrome/lighthouse/blob/master/docs/performance-budgets.md)
- [Lighthouse CI Documentation](https://github.com/GoogleChrome/lighthouse-ci/blob/main/docs/configuration.md)
- Current budget: `budget.json` in repository root
- [Complete Details in TOP_5_ISSUES.md](https://github.com/Hack23/homepage/blob/copilot/create-top-five-issues/TOP_5_ISSUES.md#issue-5)

## 👥 Recommended Assignment
**Primary:** @george-dorn (Developer)  
**Collaborate with:** @ui-enhancement-specialist (for optimization opportunities)

**Rationale:** George can run performance audits, analyze results, and configure proper budget thresholds with CI/CD integration expertise.

---

## Summary

**Total Issues:** 5
**Priority Distribution:**
- 🔴 Critical: 1 (CSP implementation)
- 🟠 High: 2 (SRI, Accessibility)
- 🟡 Medium: 2 (Korean translations, Performance budgets)

**Estimated Total Effort:** 15-24 hours
**Recommended Implementation Order:** Issue #2 → #1 → #3 → #5 → #4

**Strategic Impact:**
- ✅ Addresses critical ZAP security findings
- ✅ Achieves WCAG 2.1 AA compliance
- ✅ Expands international reach
- ✅ Establishes performance monitoring
- ✅ Demonstrates security leadership

All issues align with Hack23's commitment to transparency, security excellence, and inclusive design.

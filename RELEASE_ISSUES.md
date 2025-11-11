# Top 5 Priority Issues for Next Release

**Generated:** 2025-11-11  
**Repository:** Hack23/homepage  
**Purpose:** Prepare for next production release with high-impact, small-scope improvements

---

## 📊 Executive Summary

This document outlines the **top 5 priority issues** identified through comprehensive repository analysis for the next release of the Hack23 homepage. All issues are:

✅ **Small to Medium effort** (2-8 hours each)  
✅ **Independently mergeable** (no blocking dependencies)  
✅ **High impact** on security, performance, or user experience  
✅ **Well-documented** with clear acceptance criteria and implementation guidance

**Total Estimated Effort:** 18-28 hours across all issues  
**Priority Distribution:** 1 High, 4 Medium

---

## 🔒 Issue #1: Fix Critical Security Headers (CSP, SRI, Permissions-Policy)

### Priority: **HIGH**
### Effort: **MEDIUM** (4-8 hours)
### Impact: **HIGH** - Resolves recurring ZAP security findings

### Objective
Implement proper Content Security Policy directives, Subresource Integrity attributes, and modern security headers to resolve ZAP Full Scan findings (Issue #355).

### Background
ZAP security scans have consistently identified these vulnerabilities:
- **CSP: script-src unsafe-inline** and **style-src unsafe-inline** - Increases XSS attack surface
- **Sub Resource Integrity Attribute Missing** - External resources not integrity-checked
- **CSP: Failure to Define Directive with No Fallback** - Incomplete CSP coverage
- **Insufficient Site Isolation Against Spectre** - Missing COOP/COEP headers

### Key Acceptance Criteria
- [ ] Remove `unsafe-inline` from CSP directives
- [ ] Add Subresource Integrity (SRI) for all external resources
- [ ] Implement Cross-Origin headers (COOP, COEP)
- [ ] Add Permissions-Policy header
- [ ] Verify with ZAP scan (alerts resolved)

### Implementation Approach
**Primary:** CloudFront Response Headers Policy via CloudFormation  
**Secondary:** Add SRI attributes to HTML `<link>` and `<script>` tags  
**Validation:** Automated ZAP scanning in CI/CD

### Files to Modify
- CloudFormation stack configuration
- All 74 HTML files (add SRI attributes)
- `.github/workflows/pullrequest.yml` (validation)

### Related Issues
- #355 (ZAP Full Scan Report)

---

## ⚡ Issue #2: Optimize Lighthouse Performance Budget Compliance

### Priority: **MEDIUM**
### Effort: **MEDIUM** (4-6 hours)
### Impact: **MEDIUM** - Better UX, SEO, reduced bounce rates

### Objective
Improve website performance to consistently meet Lighthouse budget thresholds defined in `budget.json`.

### Current Performance Targets
From `budget.json`:
- **Interactive:** 7500ms target
- **First Contentful Paint:** 5000ms target
- **Script resources:** 1000KB budget
- **Total resources:** 10MB budget

### Key Acceptance Criteria
- [ ] Achieve Lighthouse Performance score ≥90
- [ ] Meet all timing budgets (interactive, FCP)
- [ ] Reduce JavaScript bundle to <1MB
- [ ] Optimize images (WebP, lazy loading)
- [ ] Implement resource hints (preconnect, dns-prefetch)
- [ ] Enable compression via CloudFront
- [ ] Pass Lighthouse CI checks

### Implementation Approach
1. **Image Optimization:** Ensure all images use WebP with lazy loading
2. **Resource Hints:** Add `preconnect` for Google Fonts
3. **CloudFront Compression:** Enable Brotli/Gzip
4. **Defer Non-Critical CSS:** Use media query trick for fonts
5. **Minification:** Already automated via GitHub Actions

### Files to Modify
- All 74 HTML files (add resource hints, lazy loading)
- CloudFormation stack (enable compression)
- `budget.json` (potentially adjust thresholds)

### Testing
- Local: `lighthouse https://hack23.com --view`
- CI/CD: Automated Lighthouse CI action

---

## 🔗 Issue #3: Fix Broken External Links and Documentation References

### Priority: **MEDIUM**
### Effort: **SMALL** (2-4 hours)
### Impact: **MEDIUM** - Professional appearance, better UX

### Objective
Fix or remove broken external links identified in DeadLinkChecker audit (Issue #344).

### Identified Issues
- **35 broken links** including:
  - Allabolag company registration URL (404)
  - GitHub documentation links (Black Trigram, CIA Compliance Manager)
  - Localhost development URLs in production
  - Screenshot path encoding issues

### Key Acceptance Criteria
- [ ] Fix or remove all 404 external links
- [ ] Update Allabolag company registration URL
- [ ] Remove localhost development URLs
- [ ] Verify all GitHub repository documentation links
- [ ] Pass lychee link checker in CI
- [ ] Document intentionally removed links

### High Priority Fixes

**1. Allabolag URL:**
```html
<!-- Current (broken) -->
<a href="https://www.allabolag.se/foretag/hack23-ab/-/-/2KJBPZZI0000">

<!-- Fixed -->
<a href="https://www.allabolag.se/foretag/hack23-ab/göteborg/konsulter/2KJBPZZI5YF3I">
```

**2. GitHub Documentation:**
- Verify existence of SECURITY_ARCHITECTURE.md, MINDMAP.md, etc.
- Remove or update links to non-existent docs

**3. Localhost URLs:**
- Remove all `https://localhost:28443` references

### Files to Modify
- `index.html`, `index_sv.html` (Allabolag link)
- `black-trigram-docs.html` (GitHub doc links)
- `cia-docs.html`, `cia-compliance-manager-docs.html`
- `.github/workflows/pullrequest.yml` (enable external link checking)

### Related Issues
- #344 (Create missing docs / broken links)

---

## 🎯 Issue #4: Enhance SEO and Metadata Across All Pages

### Priority: **MEDIUM**
### Effort: **MEDIUM** (6-8 hours)
### Impact: **MEDIUM** - Increased organic traffic, better social sharing

### Objective
Improve search engine visibility and social media sharing by enhancing meta tags, structured data, and SEO elements.

### Current State
- Limited Open Graph and Twitter Card metadata
- Inconsistent page titles and descriptions
- Missing Schema.org structured data
- No `hreflang` tags for multi-language pages
- Sitemap needs optimization

### Key Acceptance Criteria
- [ ] Add complete Open Graph meta tags to all pages
- [ ] Add Twitter Card meta tags to all pages
- [ ] Implement Schema.org structured data (Organization, WebSite)
- [ ] Add `hreflang` tags for multi-language pages
- [ ] Optimize `<title>` tags (50-60 characters)
- [ ] Write meta descriptions (150-160 characters)
- [ ] Update sitemap.xml with proper priority/changefreq
- [ ] Add canonical URLs
- [ ] Achieve Lighthouse SEO score ≥95

### Implementation Examples

**Open Graph:**
```html
<meta property="og:type" content="website">
<meta property="og:url" content="https://hack23.com/">
<meta property="og:title" content="Hack23 - Cybersecurity Consulting & Gaming Innovation">
<meta property="og:description" content="Swedish hub for security consulting and precision gaming">
<meta property="og:image" content="https://hack23.com/jamespethersorling.webp">
```

**Schema.org:**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Hack23 AB",
  "url": "https://hack23.com",
  "description": "Cybersecurity consulting and gaming innovation"
}
</script>
```

**Hreflang:**
```html
<link rel="alternate" hreflang="en" href="https://hack23.com/index.html">
<link rel="alternate" hreflang="sv" href="https://hack23.com/index_sv.html">
<link rel="alternate" hreflang="ko" href="https://hack23.com/index_ko.html">
```

### Files to Modify
- All 74 HTML files (add meta tags)
- `sitemap.xml` (optimize priorities)

### Testing
- Twitter Card Validator
- Open Graph Validator
- Schema.org Validator
- Lighthouse SEO audit

---

## ✅ Issue #5: Automate ISMS Reference Validation in CI/CD

### Priority: **MEDIUM**
### Effort: **SMALL** (2-4 hours)
### Impact: **MEDIUM** - Prevents documentation drift, maintains quality

### Objective
Create automated validation to ensure all Discordian blog posts correctly link to existing ISMS policies in Hack23/ISMS-PUBLIC repository.

### Background
Issue #424 identified that many blog pages link to ISMS policies that:
- Don't exist (404 errors)
- Have been renamed or reorganized
- Are covered in different policy documents

Manual verification is error-prone and doesn't scale.

### Key Acceptance Criteria
- [ ] Create validation script for ISMS policy links
- [ ] Integrate into `.github/workflows/pullrequest.yml`
- [ ] Verify all `github.com/Hack23/ISMS-PUBLIC` links return 200 OK
- [ ] Check referenced policy files exist
- [ ] Validate section anchors if specified
- [ ] Generate report of broken/missing references
- [ ] Fail CI if critical ISMS links broken
- [ ] Update ISMS_REFERENCE_GUIDE.md

### Implementation Approach

**1. Validation Script:**
```bash
#!/bin/bash
# scripts/validate-isms-links.sh

isms_links=$(grep -roh 'https://github.com/Hack23/ISMS-PUBLIC[^"]*' *.html | sort -u)

failed=0
for link in $isms_links; do
  status=$(curl -s -o /dev/null -w "%{http_code}" "$link")
  if [ "$status" != "200" ]; then
    echo "❌ FAILED: $link"
    ((failed++))
  fi
done

exit $failed
```

**2. GitHub Actions Integration:**
```yaml
- name: Validate ISMS References
  run: |
    chmod +x scripts/validate-isms-links.sh
    ./scripts/validate-isms-links.sh
```

**3. Advanced: Local Validation**
- Clone ISMS-PUBLIC repo in CI
- Check file existence locally (faster, no rate limits)

### Files to Create/Modify
- `scripts/validate-isms-links.sh` (new)
- `scripts/generate-isms-mapping.sh` (new)
- `.github/workflows/pullrequest.yml` (update)
- `ISMS_REFERENCE_GUIDE.md` (update)

### Related Issues
- #424 (ISMS Reference Verification)

---

## 📈 Priority Assessment Matrix

| Issue | Priority | Effort | Impact | Urgency | Total Score |
|-------|----------|--------|--------|---------|-------------|
| #1 Security Headers | High | Medium (6) | High (10) | High (8) | **24** |
| #2 Lighthouse Performance | Medium | Medium (6) | Medium (6) | Medium (6) | **18** |
| #3 Broken Links | Medium | Small (8) | Medium (6) | Medium (6) | **20** |
| #4 SEO Enhancement | Medium | Medium (6) | Medium (6) | Low (4) | **16** |
| #5 ISMS Validation | Medium | Small (8) | Medium (6) | Medium (6) | **20** |

**Scoring:** Priority Score = (Impact × 2) + Urgency + Effort Bonus (S=8, M=6, L=4)

---

## 🎯 Release Readiness Checklist

### Before Starting
- [ ] Review all 5 issues with stakeholders
- [ ] Assign issues to developers
- [ ] Set release target date
- [ ] Ensure test environment available

### During Development
- [ ] Each issue implemented independently
- [ ] PR created for each issue
- [ ] CI/CD checks passing (HTML validation, link checking, etc.)
- [ ] Code review completed
- [ ] ZAP scan run on staging

### Before Release
- [ ] All 5 issues merged to master
- [ ] Final ZAP scan shows improvements
- [ ] Lighthouse performance meets targets
- [ ] All link checkers pass
- [ ] SEO validators show improvements
- [ ] ISMS validation automated and passing

### Post-Release
- [ ] Monitor CloudFront cache invalidation
- [ ] Verify security headers in production
- [ ] Check Google Search Console for SEO improvements
- [ ] Update release notes with improvements

---

## 🚀 Getting Started

### For Developers

**Quick Start:**
```bash
# Clone repository
git clone https://github.com/Hack23/homepage.git
cd homepage

# View issues
gh issue list --label "priority:high"

# Pick an issue and create branch
gh issue develop <issue-number> --checkout

# Make changes, test locally
# ... make changes ...

# Create PR
gh pr create --fill
```

### For Project Managers

**To create all issues at once:**
```bash
# Manually trigger workflow
gh workflow run create-release-issues.yml
```

The workflow will:
1. Check for duplicate issues
2. Create all 5 issues with full descriptions
3. Apply appropriate labels
4. Generate summary report

---

## 📚 Additional Resources

### Documentation
- [README.md](README.md) - Project overview
- [SECURITY.md](SECURITY.md) - Security policy
- [CLASSIFICATION.md](CLASSIFICATION.md) - Security classification framework
- [ISMS_REFERENCE_GUIDE.md](ISMS_REFERENCE_GUIDE.md) - Blog-to-ISMS mapping

### External References
- [ZAP Security Scan (Issue #355)](https://github.com/Hack23/homepage/issues/355)
- [Broken Links Audit (Issue #344)](https://github.com/Hack23/homepage/issues/344)
- [ISMS Verification (Issue #424)](https://github.com/Hack23/homepage/issues/424)
- [ISMS-PUBLIC Repository](https://github.com/Hack23/ISMS-PUBLIC)

### CI/CD Workflows
- `.github/workflows/main.yml` - Deployment to S3/CloudFront
- `.github/workflows/pullrequest.yml` - PR validation
- `.github/workflows/scorecards.yml` - Security scorecard
- `.github/workflows/create-release-issues.yml` - Issue creation (NEW)

---

## 💡 Design Principles

These issues follow Hack23's development principles:

1. **Security First:** Issue #1 prioritizes security over features
2. **Transparency:** ISMS validation ensures public documentation accuracy
3. **User Experience:** Performance and SEO improvements benefit users
4. **Automation:** CI/CD integration reduces manual work
5. **Small Increments:** All issues independently mergeable
6. **Quality Gates:** Each issue includes validation criteria

---

## 🤝 Contributing

When working on these issues:

1. **Read the full issue description** - Acceptance criteria are comprehensive
2. **Follow implementation guidance** - Proven approaches provided
3. **Test thoroughly** - Local and CI/CD validation required
4. **Update documentation** - Keep README and guides current
5. **Minimal changes** - Surgical fixes, don't refactor unrelated code
6. **Accessibility matters** - Maintain WCAG 2.1 AA compliance

---

## 📞 Support

Questions about these issues?

- **GitHub Issues:** Comment on the specific issue
- **Company LinkedIn:** https://www.linkedin.com/company/hack23/
- **Personal LinkedIn:** https://www.linkedin.com/in/jamessorling/

---

**Document Version:** 1.0  
**Last Updated:** 2025-11-11  
**Status:** Ready for implementation  
**Next Review:** After release completion

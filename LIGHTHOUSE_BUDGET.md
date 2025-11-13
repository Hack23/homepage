# Lighthouse Performance Budget Documentation

## Overview

This document explains the performance budgets defined in `budget.json` for the Hack23 AB website. These budgets are enforced automatically via Lighthouse CI in the GitHub Actions deployment pipeline.

## Performance Philosophy

As a static HTML/CSS website focused on cybersecurity, performance is critical:
- **Fast load times** build trust and credibility
- **Mobile-first** approach ensures accessibility on all devices
- **Realistic budgets** prevent performance regression while remaining achievable
- **Core Web Vitals** compliance ensures good user experience metrics

## Current Site Baseline

- **HTML Document**: ~84KB (index.html)
- **CSS Stylesheet**: ~40KB (styles.css)
- **Images**: ~40KB total (WebP optimized)
- **Google Fonts**: ~50-100KB (Inter, Orbitron, Share Tech Mono)
- **JavaScript**: Minimal to none on static pages
- **Estimated Total**: 250-350KB per page

## Budget Configuration

### Default Budget (`/*` - All Pages)

Applies to all pages unless overridden by specific path budgets.

#### Performance Timing Budgets

| Metric | Budget | Rationale |
|--------|---------|-----------|
| **Time to Interactive (TTI)** | 5000ms | Mobile 3G target - site should be fully interactive within 5 seconds |
| **First Contentful Paint (FCP)** | 2000ms | Users see content within 2 seconds for fast perceived load |
| **Largest Contentful Paint (LCP)** | 2500ms | Core Web Vital "Good" threshold - main content visible quickly |
| **Speed Index** | 3500ms | Visual progress metric - content should appear progressively |
| **Cumulative Layout Shift (CLS)** | 0.1 | Core Web Vital "Good" threshold - stable layout, no jumps |
| **Max Potential FID** | 130ms | First Input Delay proxy - site responds to user interaction quickly |

#### Resource Size Budgets (in bytes)

| Resource Type | Budget | Rationale |
|---------------|---------|-----------|
| **Document (HTML)** | 100KB | Current: ~84KB. Allows room for growth while staying lean |
| **Stylesheet (CSS)** | 60KB | Current: ~40KB. Room for features without bloat |
| **Image** | 200KB | Total images per page using WebP optimization |
| **Font** | 100KB | Google Fonts with 3 font families (Inter, Orbitron, Share Tech Mono) |
| **Script (JS)** | 50KB | Minimal JavaScript - static site doesn't need much |
| **Third-party** | 150KB | Primarily Google Fonts CDN resources |
| **Total** | 500KB | **Mobile target** - fast load on 3G/4G networks |

#### Resource Count Budgets

| Resource Type | Budget | Rationale |
|---------------|---------|-----------|
| **Script** | 5 files | Minimal JavaScript footprint |
| **Stylesheet** | 3 files | Main CSS + Google Fonts CSS |
| **Image** | 15 files | Sufficient for typical page layout |
| **Font** | 6 files | Multiple weights/styles from Google Fonts |
| **Third-party** | 10 requests | Google Fonts API + font files |
| **Total** | 40 requests | Keep HTTP request count reasonable |

### Homepage Budget (`/index*.html`)

**Strictest performance requirements** - first impression matters!

| Metric | Budget | Why Stricter? |
|--------|---------|---------------|
| **TTI** | 4000ms | Homepage should load fastest (1s faster than default) |
| **FCP** | 1500ms | Immediate engagement on landing page |
| **LCP** | 2000ms | Excellent first impression (0.5s faster) |
| **Total Size** | 400KB | Leaner than default - homepage optimized for speed |

### Blog Pages Budget (`/blog*.html`)

**Slightly relaxed** - content-heavy pages need flexibility.

| Metric | Budget | Why More Relaxed? |
|--------|---------|-------------------|
| **TTI** | 6000ms | Blog content can take slightly longer to be interactive |
| **LCP** | 3000ms | Larger content areas acceptable for blog posts |
| **Document** | 150KB | Blog HTML can be larger with more content |
| **Image** | 300KB | Blog posts may include more visual content |
| **Total Size** | 600KB | Content-rich pages need more room |

## Core Web Vitals Alignment

Our budgets align with [Google's Core Web Vitals](https://web.dev/vitals/) thresholds:

| Core Web Vital | Good | Needs Improvement | Poor | Our Budget |
|----------------|------|-------------------|------|------------|
| **LCP** | ≤ 2.5s | 2.5-4.0s | > 4.0s | **2.5s** (default), **2.0s** (homepage) |
| **FID/INP** | ≤ 100ms | 100-300ms | > 300ms | **130ms** (max-potential-fid proxy) |
| **CLS** | ≤ 0.1 | 0.1-0.25 | > 0.25 | **0.1** |

## Testing and Validation

### Automated Testing

The budget is enforced automatically in the deployment pipeline:

```yaml
# .github/workflows/main.yml
- name: Audit URLs using Lighthouse
  uses: treosh/lighthouse-ci-action@v9
  with:
    urls: https://hack23.com/
    budgetPath: ./budget.json
    uploadArtifacts: true
    temporaryPublicStorage: true
```

### Manual Testing

To test locally:

```bash
# Install Lighthouse CLI
npm install -g lighthouse

# Run audit against production site
lighthouse https://hack23.com --budget-path=budget.json --view

# Test specific pages
lighthouse https://hack23.com/blog-cia-security.html --budget-path=budget.json
```

## Budget Evolution Strategy

### When to Adjust Budgets

- **Tighten budgets** when consistently beating targets by 20%+
- **Relax budgets** only if business-critical features require it
- **Review quarterly** to ensure alignment with site evolution

### Current vs. Target Performance

| Metric | Current Estimate | Budget | Headroom |
|--------|------------------|--------|----------|
| Total Size | 250-350KB | 500KB | 30-50% |
| HTML | 84KB | 100KB | 16% |
| CSS | 40KB | 60KB | 33% |
| Images | 40KB | 200KB | 80% |

**Status**: Budgets are achievable with current site. Significant headroom allows for future content growth without performance regression.

## Performance Best Practices

To maintain compliance with these budgets:

1. **Optimize Images**: Use WebP format, lazy loading, responsive images
2. **Minimize CSS**: Remove unused styles, use CSS minification
3. **Limit Fonts**: Use `font-display: swap` and limit font weights
4. **Reduce HTML**: Minimize HTML, remove comments and whitespace
5. **Cache Aggressively**: Leverage CloudFront CDN and cache headers (already configured)
6. **Monitor Regularly**: Review Lighthouse reports on every deployment

## Related Resources

- [Web.dev Performance Budgets Guide](https://web.dev/performance-budgets-101/)
- [Google Core Web Vitals](https://web.dev/vitals/)
- [Lighthouse Budget.json Schema](https://github.com/GoogleChrome/lighthouse/blob/master/docs/performance-budgets.md)
- [Lighthouse CI Documentation](https://github.com/GoogleChrome/lighthouse-ci)

## Maintenance

- **Owner**: Development Team
- **Review Frequency**: Quarterly or when adding major features
- **Last Updated**: 2025-11-13
- **Budget Version**: 2.0 (Mobile-optimized)

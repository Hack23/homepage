---
name: seo-optimization
description: SEO best practices including meta tags, structured data (Schema.org), semantic HTML, performance optimization, and multilingual SEO with hreflang
license: Apache-2.0
---

# SEO Optimization Skill

## Purpose

Ensures websites are optimized for search engines following modern SEO best practices, with focus on technical SEO, structured data, and international/multilingual support.

## Rules

### Meta Tags (MUST HAVE)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Title: 50-60 characters -->
  <title>Cybersecurity Consulting Services | Hack23 AB</title>
  
  <!-- Meta Description: 150-160 characters -->
  <meta name="description" content="Expert cybersecurity consulting with transparent security practices. ISO 27001, GDPR, and NIS2 compliance support for Swedish organizations.">
  
  <!-- Canonical URL -->
  <link rel="canonical" href="https://www.hack23.com/services.html">
  
  <!-- Open Graph (Social Media) -->
  <meta property="og:title" content="Cybersecurity Consulting Services">
  <meta property="og:description" content="Expert security consulting with transparency">
  <meta property="og:image" content="https://www.hack23.com/images/og-image.jpg">
  <meta property="og:url" content="https://www.hack23.com/services.html">
  <meta property="og:type" content="website">
  
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Cybersecurity Consulting Services">
  <meta name="twitter:description" content="Expert security consulting">
  <meta name="twitter:image" content="https://www.hack23.com/images/twitter-card.jpg">
</head>
```

### Structured Data (Schema.org)

**MUST USE for:**
- Organization
- WebSite
- BreadcrumbList
- Article (blog posts)
- FAQPage
- Service

**Example - Organization:**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Hack23 AB",
  "url": "https://www.hack23.com",
  "logo": "https://www.hack23.com/images/logo.png",
  "description": "Cybersecurity consulting with transparent security practices",
  "address": {
    "@type": "PostalAddress",
    "addressCountry": "SE"
  },
  "sameAs": [
    "https://github.com/Hack23",
    "https://www.linkedin.com/company/hack23"
  ]
}
</script>
```

### Multilingual SEO (hreflang)

**MUST IMPLEMENT for translated pages:**
```html
<link rel="alternate" hreflang="en" href="https://www.hack23.com/services.html">
<link rel="alternate" hreflang="sv" href="https://www.hack23.com/services_sv.html">
<link rel="alternate" hreflang="de" href="https://www.hack23.com/services_de.html">
<link rel="alternate" hreflang="x-default" href="https://www.hack23.com/services.html">
```

### Semantic HTML for SEO

**MUST:**
- Use `<h1>` once per page
- Maintain proper heading hierarchy (h1→h2→h3)
- Use semantic elements (`<article>`, `<nav>`, `<header>`, `<footer>`)
- Include `alt` text on all images
- Use descriptive anchor text

### Performance Optimization

**MUST:**
- Achieve Lighthouse Performance score ≥ 90
- First Contentful Paint < 1.5s
- Largest Contentful Paint < 2.5s
- Time to Interactive < 3.5s
- Use WebP images with fallbacks
- Minify HTML/CSS/JavaScript
- Enable gzip/Brotli compression
- Implement lazy loading for images

### Sitemap & Robots.txt

**sitemap.xml:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://www.hack23.com/services.html</loc>
    <lastmod>2025-01-24</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
    <xhtml:link rel="alternate" hreflang="sv" href="https://www.hack23.com/services_sv.html"/>
    <xhtml:link rel="alternate" hreflang="de" href="https://www.hack23.com/services_de.html"/>
  </url>
</urlset>
```

**robots.txt:**
```
User-agent: *
Allow: /
Sitemap: https://www.hack23.com/sitemap.xml
```

### Security Headers (SEO Impact)

**MUST INCLUDE:**
```
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Referrer-Policy: strict-origin-when-cross-origin
```

## SEO Checklist

- [ ] Unique `<title>` per page (50-60 chars)
- [ ] Unique meta description per page (150-160 chars)
- [ ] Canonical URL specified
- [ ] Structured data (Schema.org) implemented
- [ ] hreflang tags for translations
- [ ] Sitemap.xml generated and submitted
- [ ] robots.txt configured
- [ ] Mobile-friendly (responsive design)
- [ ] HTTPS enforced
- [ ] Page load time < 3 seconds
- [ ] Images optimized (WebP)
- [ ] Alt text on all images
- [ ] Internal linking structure
- [ ] Breadcrumb navigation
- [ ] 404 page exists
- [ ] No broken links

## Related Documentation

- [html-css-best-practices SKILL.md](../html-css-best-practices/SKILL.md)
- [accessibility-wcag SKILL.md](../accessibility-wcag/SKILL.md)

## Tools

- **Google Search Console**: Monitor search performance
- **Schema.org Validator**: https://validator.schema.org/
- **Rich Results Test**: https://search.google.com/test/rich-results
- **Lighthouse**: Performance and SEO audits

---
name: html-css-best-practices
description: Semantic HTML5, CSS custom properties, responsive design, and performance optimization for web development
license: Apache-2.0
---

# HTML/CSS Best Practices Skill

## Purpose

This skill defines HTML and CSS best practices for building accessible, performant, and maintainable web interfaces, specifically for the Hack23 Homepage and related projects.

## Rules

### Semantic HTML5

**MUST USE:**
- `<header>` for site/page header
- `<nav>` for navigation menus
- `<main>` for main content (one per page)
- `<article>` for self-contained content
- `<section>` for thematic grouping
- `<aside>` for tangential content
- `<footer>` for site/page footer
- `<h1>-<h6>` in hierarchical order (don't skip levels)
- `<button>` for interactive actions
- `<a>` for navigation
- `<figure>` and `<figcaption>` for images with captions
- `<time datetime="">` for dates/times

**MUST NOT:**
- Use `<div>` when semantic element exists
- Use `<span>` for block-level content
- Skip heading levels (e.g., h1 → h3)
- Use `<br>` for spacing (use CSS)
- Use tables for layout (use CSS Grid/Flexbox)

### HTML Structure

**MUST:**
- Include `<!DOCTYPE html>`
- Set `lang` attribute on `<html>` element
- Include charset: `<meta charset="UTF-8">`
- Include viewport meta: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- Use descriptive `<title>` (unique per page)
- Include meta description
- Close all tags properly
- Use lowercase for element names and attributes
- Quote all attribute values
- Validate HTML with W3C validator

**Example:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Hack23 - Cybersecurity consulting with transparency">
  <title>Hack23 - Cybersecurity Consulting</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <nav>...</nav>
  </header>
  <main>
    <article>...</article>
  </main>
  <footer>...</footer>
</body>
</html>
```

### CSS Organization

**MUST:**
- Use single external stylesheet (`styles.css`)
- Organize CSS logically:
  1. CSS Custom Properties (variables)
  2. Reset/normalization
  3. Base styles (html, body, headings)
  4. Layout (header, nav, main, footer)
  5. Components
  6. Utilities
  7. Media queries
- Use meaningful class names (BEM methodology recommended)
- Avoid `!important` (use specificity correctly)
- Group related properties
- Use shorthand properties where appropriate
- Comment complex sections

**Example:**
```css
/* CSS Custom Properties */
:root {
  --primary-color: #2c3e50;
  --secondary-color: #3498db;
  --text-color: #333;
  --bg-color: #fff;
  --max-width: 1200px;
  --spacing-unit: 8px;
}

/* Base Styles */
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: var(--text-color);
  background-color: var(--bg-color);
  line-height: 1.6;
  margin: 0;
  padding: 0;
}

/* Layout */
.container {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 calc(var(--spacing-unit) * 2);
}

/* Components */
.button {
  display: inline-block;
  padding: calc(var(--spacing-unit) * 1.5) calc(var(--spacing-unit) * 3);
  background-color: var(--primary-color);
  color: white;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.button:hover,
.button:focus {
  background-color: var(--secondary-color);
}
```

### CSS Custom Properties (Variables)

**MUST USE for:**
- Colors (primary, secondary, backgrounds, text)
- Spacing (margins, padding multiples)
- Typography (font sizes, line heights)
- Breakpoints
- Transitions/animations
- Z-index values

**Benefits:**
- Easy theme switching
- Consistent values across site
- Easier maintenance
- Runtime updates possible

### Responsive Design

**MUST:**
- Design mobile-first (base styles for mobile, media queries for larger screens)
- Use relative units (`rem`, `em`, `%`, `vw`, `vh`) over fixed `px`
- Test at multiple breakpoints (320px, 768px, 1024px, 1440px+)
- Use CSS Grid or Flexbox for layouts
- Ensure touch targets are at least 44×44px
- Avoid horizontal scrolling
- Use `max-width` for readability (60-80 characters per line)

**Recommended Breakpoints:**
```css
/* Mobile-first base styles */

/* Tablet */
@media (min-width: 768px) {
  /* Tablet styles */
}

/* Desktop */
@media (min-width: 1024px) {
  /* Desktop styles */
}

/* Large Desktop */
@media (min-width: 1440px) {
  /* Large desktop styles */
}
```

### Performance Optimization

**MUST:**
- Minimize CSS file size (remove unused styles)
- Use CSS minification in production
- Avoid deep selector nesting (max 3 levels)
- Use efficient selectors (avoid universal `*`)
- Load CSS in `<head>` (blocking is necessary)
- Consider critical CSS for above-the-fold content
- Use `will-change` sparingly for animations
- Optimize images (WebP format, lazy loading)

**Image Optimization:**
```html
<!-- Use WebP with fallback -->
<picture>
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="Description" loading="lazy">
</picture>

<!-- For icons, prefer inline SVG -->
<svg width="24" height="24" aria-hidden="true">
  <use xlink:href="#icon-name"></use>
</svg>
```

### Browser Compatibility

**MUST:**
- Test in modern browsers (Chrome, Firefox, Safari, Edge)
- Use autoprefixer for vendor prefixes
- Provide fallbacks for newer CSS features
- Use progressive enhancement

**Example with fallback:**
```css
.grid {
  display: flex; /* Fallback */
  flex-wrap: wrap;
}

@supports (display: grid) {
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
  }
}
```

## Examples

### Example 1: Semantic HTML Page Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Cybersecurity consulting services with transparent security practices">
  <title>Services - Hack23 Cybersecurity Consulting</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header class="site-header">
    <div class="container">
      <a href="index.html" class="logo">
        <img src="logo.svg" alt="Hack23 Logo" width="150" height="50">
      </a>
      <nav aria-label="Main navigation">
        <ul class="nav-menu">
          <li><a href="index.html">Home</a></li>
          <li><a href="services.html" aria-current="page">Services</a></li>
          <li><a href="projects.html">Projects</a></li>
          <li><a href="blog.html">Blog</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main class="main-content">
    <div class="container">
      <article>
        <header>
          <h1>Cybersecurity Consulting Services</h1>
          <p class="lead">Transparent, effective security for modern organizations</p>
        </header>

        <section>
          <h2>Security Assessments</h2>
          <p>Comprehensive evaluation of your security posture...</p>
        </section>

        <section>
          <h2>Compliance Support</h2>
          <p>ISO 27001, GDPR, NIS2 compliance assistance...</p>
        </section>
      </article>

      <aside class="sidebar">
        <h2>Related Services</h2>
        <nav aria-label="Related services">
          <ul>
            <li><a href="penetration-testing.html">Penetration Testing</a></li>
            <li><a href="security-training.html">Security Training</a></li>
          </ul>
        </nav>
      </aside>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; <time datetime="2025">2025</time> Hack23 AB. All rights reserved.</p>
      <nav aria-label="Footer navigation">
        <ul>
          <li><a href="privacy.html">Privacy Policy</a></li>
          <li><a href="accessibility.html">Accessibility</a></li>
        </ul>
      </nav>
    </div>
  </footer>
</body>
</html>
```

### Example 2: CSS with Custom Properties

```css
/* ===========================
   CSS Custom Properties
   =========================== */
:root {
  /* Colors */
  --color-primary: #2c3e50;
  --color-secondary: #3498db;
  --color-accent: #e74c3c;
  --color-text: #333;
  --color-text-light: #666;
  --color-bg: #ffffff;
  --color-bg-alt: #f8f9fa;
  --color-border: #dee2e6;

  /* Typography */
  --font-base: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  --font-mono: 'Courier New', Courier, monospace;
  --font-size-base: 16px;
  --font-size-sm: 0.875rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.5rem;
  --line-height-base: 1.6;
  --line-height-heading: 1.2;

  /* Spacing */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  --spacing-xxl: 48px;

  /* Layout */
  --max-width: 1200px;
  --max-width-narrow: 800px;
  --header-height: 80px;

  /* Transitions */
  --transition-fast: 0.15s ease;
  --transition-base: 0.3s ease;
  --transition-slow: 0.5s ease;

  /* Z-index */
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-modal: 1000;
}

/* ===========================
   Reset & Base Styles
   =========================== */
* {
  box-sizing: border-box;
}

html {
  font-size: var(--font-size-base);
}

body {
  font-family: var(--font-base);
  color: var(--color-text);
  background-color: var(--color-bg);
  line-height: var(--line-height-base);
  margin: 0;
  padding: 0;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

h1, h2, h3, h4, h5, h6 {
  line-height: var(--line-height-heading);
  margin-top: 0;
  margin-bottom: var(--spacing-md);
  color: var(--color-primary);
}

h1 { font-size: 2.5rem; }
h2 { font-size: 2rem; }
h3 { font-size: 1.75rem; }
h4 { font-size: 1.5rem; }
h5 { font-size: 1.25rem; }
h6 { font-size: 1rem; }

a {
  color: var(--color-secondary);
  text-decoration: none;
  transition: color var(--transition-fast);
}

a:hover,
a:focus {
  color: var(--color-accent);
  text-decoration: underline;
}

/* ===========================
   Layout
   =========================== */
.container {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 var(--spacing-md);
}

.site-header {
  background-color: var(--color-primary);
  color: white;
  height: var(--header-height);
  display: flex;
  align-items: center;
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
}

.main-content {
  min-height: calc(100vh - var(--header-height) - 200px);
  padding: var(--spacing-xxl) 0;
}

.site-footer {
  background-color: var(--color-bg-alt);
  padding: var(--spacing-xl) 0;
  border-top: 1px solid var(--color-border);
}

/* ===========================
   Components
   =========================== */
.button {
  display: inline-block;
  padding: var(--spacing-sm) var(--spacing-lg);
  background-color: var(--color-primary);
  color: white;
  border: none;
  border-radius: 4px;
  font-size: var(--font-size-base);
  cursor: pointer;
  transition: background-color var(--transition-base);
}

.button:hover,
.button:focus {
  background-color: var(--color-secondary);
  text-decoration: none;
}

.card {
  background-color: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: 8px;
  padding: var(--spacing-lg);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: box-shadow var(--transition-base);
}

.card:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

/* ===========================
   Utilities
   =========================== */
.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

.text-center {
  text-align: center;
}

/* ===========================
   Responsive
   =========================== */
@media (min-width: 768px) {
  .container {
    padding: 0 var(--spacing-lg);
  }

  h1 { font-size: 3rem; }
  h2 { font-size: 2.5rem; }
}

@media (min-width: 1024px) {
  .container {
    padding: 0 var(--spacing-xl);
  }
}
```

### Example 3: Responsive Navigation

```html
<nav class="main-nav" aria-label="Main navigation">
  <button class="nav-toggle" aria-expanded="false" aria-controls="nav-menu">
    <span class="visually-hidden">Toggle navigation</span>
    <span class="hamburger"></span>
  </button>
  <ul id="nav-menu" class="nav-menu">
    <li><a href="index.html">Home</a></li>
    <li><a href="services.html">Services</a></li>
    <li><a href="projects.html">Projects</a></li>
    <li><a href="blog.html">Blog</a></li>
  </ul>
</nav>
```

```css
.main-nav {
  position: relative;
}

.nav-toggle {
  display: block;
  background: none;
  border: none;
  cursor: pointer;
  padding: var(--spacing-sm);
}

.nav-menu {
  display: none;
  list-style: none;
  margin: 0;
  padding: 0;
}

/* Show menu when expanded */
.nav-toggle[aria-expanded="true"] + .nav-menu {
  display: block;
}

/* Desktop: horizontal menu, hide toggle */
@media (min-width: 768px) {
  .nav-toggle {
    display: none;
  }

  .nav-menu {
    display: flex;
    gap: var(--spacing-md);
  }
}
```

## Related ISMS Policies

- **[Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md)** - Security in frontend code

## Related Documentation

- [accessibility-wcag SKILL.md](../accessibility-wcag/SKILL.md) - Accessibility requirements
- [seo-optimization SKILL.md](../seo-optimization/SKILL.md) - SEO best practices

## Performance Budget

- **CSS file size**: < 50KB (gzipped)
- **First Contentful Paint**: < 1.5s
- **Largest Contentful Paint**: < 2.5s
- **Cumulative Layout Shift**: < 0.1

## Validation & Testing

- **HTML Validator**: https://validator.w3.org/
- **CSS Validator**: https://jigsaw.w3.org/css-validator/
- **Lighthouse**: Run audits in Chrome DevTools
- **BrowserStack**: Cross-browser testing

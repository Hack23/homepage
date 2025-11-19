# Breadcrumb Implementation Guide

## Overview
This guide provides instructions for implementing the breadcrumb visual UI component across all 79 pages of the Hack23 AB website.

## CSS Component
The breadcrumb CSS component has been added to `styles.css` with full WCAG 2.1 AA compliance. It includes:
- Responsive design (mobile, tablet, desktop)
- Light mode, dark mode, and Black Trigram theme support
- Keyboard navigation with visible focus indicators
- Screen reader accessibility with ARIA attributes
- Color contrast ratios meeting 4.5:1 minimum

## HTML Structure

### Basic Two-Level Breadcrumb
```html
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item">
      <a href="/">Home</a>
    </li>
    <li class="breadcrumb-item" aria-current="page">
      Current Page Name
    </li>
  </ol>
</nav>
```

### Three-Level Breadcrumb
```html
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item">
      <a href="/">Home</a>
    </li>
    <li class="breadcrumb-item">
      <a href="/section.html">Section Name</a>
    </li>
    <li class="breadcrumb-item" aria-current="page">
      Current Page Name
    </li>
  </ol>
</nav>
```

### Four-Level Breadcrumb
```html
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item">
      <a href="/">Home</a>
    </li>
    <li class="breadcrumb-item">
      <a href="/section.html">Section Name</a>
    </li>
    <li class="breadcrumb-item">
      <a href="/subsection.html">Subsection Name</a>
    </li>
    <li class="breadcrumb-item" aria-current="page">
      Current Page Name
    </li>
  </ol>
</nav>
```

## Placement Guidelines

### Standard Placement
Place the breadcrumb navigation **immediately after the opening `<body>` tag** or **before the `<header>` element** for optimal accessibility:

```html
<body>
  <!-- Breadcrumb goes here -->
  <nav aria-label="Breadcrumb">
    <ol class="breadcrumb">
      <!-- breadcrumb items -->
    </ol>
  </nav>
  
  <header>
    <h1>Page Title</h1>
    <!-- header content -->
  </header>
  
  <!-- main content -->
</body>
```

### Alternative Placement
For pages where breadcrumbs should appear within the header context, place them **after the logo but before the main heading**:

```html
<body>
  <header>
    <div class="logo-container">
      <img src="logo.png" alt="Logo" class="logo" />
    </div>
    
    <!-- Breadcrumb goes here -->
    <nav aria-label="Breadcrumb">
      <ol class="breadcrumb">
        <!-- breadcrumb items -->
      </ol>
    </nav>
    
    <h1>Page Title</h1>
    <!-- rest of header content -->
  </header>
</body>
```

## Page-Specific Implementations

### Homepage (index.html, index_sv.html, index_ko.html)
**No breadcrumb needed** - the homepage is the root of the navigation hierarchy.

### Project Feature Pages
Examples: `cia-features.html`, `black-trigram-features.html`, `cia-compliance-manager-features.html`

```html
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item">
      <a href="/">Home</a>
    </li>
    <li class="breadcrumb-item" aria-current="page">
      Project Name Features
    </li>
  </ol>
</nav>
```

### Project Documentation Pages
Examples: `cia-docs.html`, `black-trigram-docs.html`, `cia-compliance-manager-docs.html`

```html
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item">
      <a href="/">Home</a>
    </li>
    <li class="breadcrumb-item">
      <a href="/project-features.html">Project Name</a>
    </li>
    <li class="breadcrumb-item" aria-current="page">
      Documentation
    </li>
  </ol>
</nav>
```

### Blog Pages
Main blog listing (`blog.html`):
```html
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item">
      <a href="/">Home</a>
    </li>
    <li class="breadcrumb-item" aria-current="page">
      Blog
    </li>
  </ol>
</nav>
```

Individual blog posts (e.g., `blog-cia-architecture.html`):
```html
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item">
      <a href="/">Home</a>
    </li>
    <li class="breadcrumb-item">
      <a href="/blog.html">Blog</a>
    </li>
    <li class="breadcrumb-item" aria-current="page">
      Article Title
    </li>
  </ol>
</nav>
```

### ISMS/Discordian Policy Pages
Examples: `discordian-acceptable-use.html`, `discordian-cloud-security.html`

```html
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item">
      <a href="/">Home</a>
    </li>
    <li class="breadcrumb-item">
      <a href="/">ISMS Policies</a>
    </li>
    <li class="breadcrumb-item" aria-current="page">
      Policy Name
    </li>
  </ol>
</nav>
```

### FAQ Pages
Examples: `cia-triad-faq.html`, `cia-triad-faq_sv.html`

```html
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <ol class="breadcrumb">
    <li class="breadcrumb-item">
      <a href="/">Home</a>
    </li>
    <li class="breadcrumb-item" aria-current="page">
      FAQ
    </li>
  </ol>
</nav>
```

## Localized Pages
For Swedish (`_sv`) and Korean (`_ko`) pages, update the breadcrumb text accordingly:

### Swedish Example
```html
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item">
      <a href="/index_sv.html">Hem</a>
    </li>
    <li class="breadcrumb-item" aria-current="page">
      Funktioner
    </li>
  </ol>
</nav>
```

### Korean Example
```html
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item">
      <a href="/index_ko.html">홈</a>
    </li>
    <li class="breadcrumb-item" aria-current="page">
      기능
    </li>
  </ol>
</nav>
```

## Accessibility Requirements

### Required Attributes
1. **`<nav>` element**: Must have `aria-label="Breadcrumb"`
2. **Current page**: Must have `aria-current="page"` on the `<li>` element
3. **Semantic structure**: Use `<ol>` (ordered list) for proper hierarchy

### Keyboard Navigation
- All breadcrumb links must be keyboard accessible via Tab key
- Focus indicators are automatically styled with visible outlines
- Enter key activates the focused link

### Screen Reader Support
- The `aria-label="Breadcrumb"` announces the navigation type
- The `aria-current="page"` indicates the current page to screen readers
- The ordered list structure provides hierarchical context

## Testing Checklist

Before deploying breadcrumbs on a page, verify:

- [ ] Breadcrumb appears in correct location (before or within header)
- [ ] All links are functional and point to correct URLs
- [ ] Current page is marked with `aria-current="page"` (not a link)
- [ ] Keyboard navigation works (Tab, Shift+Tab, Enter)
- [ ] Focus indicators are clearly visible
- [ ] Breadcrumb is responsive on mobile (320px+), tablet (768px+), and desktop (1280px+)
- [ ] Text is readable in both light and dark modes
- [ ] Color contrast meets WCAG 2.1 AA standards (test with browser DevTools)
- [ ] Screen reader announces breadcrumb correctly (test with NVDA, JAWS, or VoiceOver)

## Schema.org Integration

The breadcrumb UI component complements the existing BreadcrumbList schema.org markup. Ensure both are present:

```html
<!-- Visual breadcrumb UI (new) -->
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item">
      <a href="/">Home</a>
    </li>
    <li class="breadcrumb-item" aria-current="page">
      Current Page
    </li>
  </ol>
</nav>

<!-- Schema.org BreadcrumbList (existing - keep in <head>) -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://hack23.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Current Page",
      "item": "https://hack23.com/current-page.html"
    }
  ]
}
</script>
```

## Support and Questions

For questions or issues with breadcrumb implementation:
1. Review this guide thoroughly
2. Check the example file: `breadcrumb-example.html`
3. Inspect the CSS in `styles.css` (search for "BREADCRUMB NAVIGATION COMPONENT")
4. Test with browser DevTools accessibility panel

## Visual Examples

See the example file `breadcrumb-example.html` for live demonstrations of:
- Two-level, three-level, and four-level breadcrumbs
- Keyboard navigation and focus states
- Responsive design across viewport sizes
- Light mode, dark mode, and Black Trigram theme support

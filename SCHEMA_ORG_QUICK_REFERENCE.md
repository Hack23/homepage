# Schema.org Quick Reference Guide

## Quick Validation Checklist

When adding or updating structured data, verify:

- [ ] Valid JSON syntax (no trailing commas, proper quotes)
- [ ] All required properties present for schema type
- [ ] @id values are unique and properly formatted URLs
- [ ] References (@id links) point to valid entities
- [ ] datePublished and dateModified use ISO 8601 format (YYYY-MM-DD)
- [ ] Content matches visible page content exactly
- [ ] Images URLs are valid and accessible
- [ ] All URLs use https:// protocol

## Common Schema Templates

### BreadcrumbList Template
```json
{
  "@type": "BreadcrumbList",
  "@id": "https://hack23.com/PAGE-NAME.html#breadcrumb",
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
      "name": "PAGE TITLE",
      "item": "https://hack23.com/PAGE-NAME.html"
    }
  ]
}
```

### WebPage Template
```json
{
  "@type": "WebPage",
  "@id": "https://hack23.com/PAGE-NAME.html#webpage",
  "url": "https://hack23.com/PAGE-NAME.html",
  "name": "PAGE TITLE | Hack23",
  "description": "PAGE DESCRIPTION",
  "isPartOf": {
    "@type": "WebSite",
    "@id": "https://hack23.com/#website"
  },
  "about": { "@id": "RELATED-ENTITY-ID" },
  "primaryImageOfPage": {
    "@type": "ImageObject",
    "url": "IMAGE-URL"
  },
  "breadcrumb": { "@id": "https://hack23.com/PAGE-NAME.html#breadcrumb" },
  "inLanguage": "en",
  "datePublished": "YYYY-MM-DD",
  "dateModified": "YYYY-MM-DD"
}
```

### BlogPosting + Article Template
```json
{
  "@type": ["BlogPosting", "Article"],
  "headline": "BLOG POST TITLE",
  "url": "https://hack23.com/blog-post.html",
  "datePublished": "YYYY-MM-DD",
  "dateModified": "YYYY-MM-DD",
  "author": { "@id": "https://hack23.com/#james-pether-sorling" },
  "publisher": { "@id": "https://hack23.com/#org" },
  "image": "https://hack23.com/blog.png",
  "articleSection": "SECTION-NAME",
  "keywords": ["keyword1", "keyword2", "keyword3"]
}
```

### Service Template
```json
{
  "@type": "Service",
  "@id": "https://hack23.com/#service-id",
  "serviceType": "SERVICE NAME",
  "provider": { "@id": "https://hack23.com/#org" },
  "areaServed": [
    {
      "@type": "Country",
      "name": "COUNTRY NAME"
    }
  ],
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "SERVICE CATALOG NAME",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "SPECIFIC SERVICE NAME",
          "description": "SERVICE DESCRIPTION"
        }
      }
    ]
  }
}
```

## Common Update Scenarios

### Adding a New Blog Post
1. Open `blog.html`
2. Find the `"blogPost"` array in the Blog schema
3. Add new entry at the top of the array:
```json
{
  "@type": ["BlogPosting", "Article"],
  "headline": "YOUR BLOG TITLE",
  "url": "https://hack23.com/your-blog-post.html",
  "datePublished": "2025-MM-DD",
  "dateModified": "2025-MM-DD",
  "author": { "@id": "https://hack23.com/#james-pether-sorling" },
  "publisher": { "@id": "https://hack23.com/#org" },
  "image": "https://hack23.com/blog.png",
  "articleSection": "YOUR-SECTION",
  "keywords": ["keyword1", "keyword2"]
}
```
4. Update `"numberOfItems"` count
5. Update WebPage `"dateModified"` to today's date
6. Validate JSON syntax

### Adding a New Product Page
1. Create page with `@graph` structure
2. Include three schemas: Product/Application + BreadcrumbList + WebPage
3. Link WebPage to product using `"about": { "@id": "product-id" }`
4. Add breadcrumb with proper position numbers
5. Include all required product properties (name, description, url, etc.)
6. Validate all @id references

### Updating Service Offerings
1. Open `index.html`
2. Find the Service schema (search for `"@type": "Service"`)
3. Update `"hasOfferCatalog"` → `"itemListElement"` array
4. Add/modify Offer entries with new services
5. Update Organization `"dateModified"` if significant changes
6. Validate JSON syntax

### Updating Product Features
1. Find the product schema (SoftwareApplication, VideoGame, WebApplication)
2. Update `"featureList"` array with new features
3. Update `"dateModified"` to current date
4. Update `"softwareVersion"` if version changed
5. Add new screenshots to `"screenshot"` array if available
6. Validate JSON syntax

## Entity ID Reference

Standard entity IDs used across the site:

- **Organization:** `"@id": "https://hack23.com/#org"`
- **Website:** `"@id": "https://hack23.com/#website"`
- **James Pether Sörling:** `"@id": "https://hack23.com/#james-pether-sorling"`
- **Black Trigram:** `"@id": "https://blacktrigram.com/#blacktrigram"`
- **CIA Compliance Manager:** `"@id": "https://hack23.com/#cia-compliance-manager"`
- **Citizen Intelligence Agency:** `"@id": "https://hack23.com/#citizen-intelligence-agency"`
- **Cybersecurity Consulting Service:** `"@id": "https://hack23.com/#cybersecurity-consulting"`

## Validation Commands

### Python JSON Validation
```bash
python3 << 'EOF'
import json
import re

with open('YOUR_FILE.html', 'r') as f:
    content = f.read()
    match = re.search(r'<script type="application/ld\+json">(.*?)</script>', 
                     content, re.DOTALL)
    if match:
        try:
            data = json.loads(match.group(1))
            print("✓ Valid JSON-LD")
        except json.JSONDecodeError as e:
            print(f"✗ Invalid JSON: {e}")
EOF
```

### Online Validators
1. **Schema.org Validator:** https://validator.schema.org/
   - Paste full HTML or just JSON-LD
   - Shows schema type and property completeness
   - Identifies missing required properties

2. **Google Rich Results Test:** https://search.google.com/test/rich-results
   - Enter page URL or HTML
   - Shows which rich results are eligible
   - Identifies errors preventing rich results

3. **JSON Formatter:** https://jsonformatter.org/
   - Validates JSON syntax only
   - Formats for readability
   - Quick syntax check before Schema.org validation

## Common Errors and Fixes

### Trailing Comma Error
**Error:** `"Unexpected token }" or "Unexpected token ]"`
**Fix:** Remove trailing commas from last item in arrays/objects
```json
// Wrong
"keywords": ["security", "ISMS",]

// Correct
"keywords": ["security", "ISMS"]
```

### Missing Required Property
**Error:** `"Missing required property: publisher"`
**Fix:** Add the required property with proper reference
```json
"publisher": { "@id": "https://hack23.com/#org" }
```

### Invalid @id Reference
**Error:** `"Referenced entity not found"`
**Fix:** Ensure referenced @id exists in the same or related page
```json
// Ensure this entity exists somewhere
{ "@id": "https://hack23.com/#org", "@type": "Organization", ... }

// Then reference it
"publisher": { "@id": "https://hack23.com/#org" }
```

### Date Format Error
**Error:** `"Invalid date format"`
**Fix:** Use ISO 8601 format (YYYY-MM-DD)
```json
// Wrong
"datePublished": "11/17/2025"

// Correct
"datePublished": "2025-11-17"
```

## Testing Workflow

1. **Before Commit:**
   - Run Python JSON validation
   - Check for trailing commas
   - Verify all @id references exist
   - Confirm dates are ISO 8601 format

2. **After Deploy:**
   - Test with Google Rich Results Test
   - Validate with Schema.org validator
   - Check Search Console for errors
   - Monitor rich result appearance (can take days/weeks)

3. **Monthly:**
   - Review Search Console → Enhancements
   - Check for new structured data errors
   - Update dateModified on changed pages
   - Verify rich results are still working

## Support Resources

- **Schema.org Documentation:** https://schema.org/
- **Google Structured Data Guide:** https://developers.google.com/search/docs/appearance/structured-data
- **Schema.org Slack Community:** https://schemadotorg.slack.com/
- **Google Search Central Help:** https://support.google.com/webmasters/

---

**Last Updated:** November 17, 2025  
**Maintained By:** Hack23 AB  
**Questions:** https://www.linkedin.com/company/hack23/

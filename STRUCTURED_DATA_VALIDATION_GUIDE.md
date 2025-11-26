# Structured Data Validation Quick Guide

**Purpose:** Quick reference for validating structured data (Schema.org JSON-LD) on the Hack23 AB website.

## Quick Validation Commands

### 1. Check for Duplicate FAQPage (or any schema type)

```bash
# Check all homepage files for FAQPage count
for file in index*.html; do 
  count=$(grep -c '"@type": "FAQPage"' "$file")
  echo "$file: $count FAQPage(s) - $([ $count -eq 1 ] && echo '✅ OK' || echo '❌ CHECK')"
done
```

**Expected:** Each file should have exactly **1 FAQPage**

### 2. Run Comprehensive Validation Script

```bash
cd /home/runner/work/homepage/homepage
python3 validate_structured_data.py
```

**What it checks:**
- Duplicate schema types
- JSON-LD syntax errors
- Required properties
- Breadcrumb structure
- Canonical tags
- Hreflang tags

### 3. Validate JSON-LD Syntax

```bash
python3 << 'EOF'
import json, re
from pathlib import Path

for file in Path('.').glob('index*.html'):
    content = file.read_text()
    pattern = r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>'
    for i, match in enumerate(re.findall(pattern, content, re.DOTALL), 1):
        try:
            json.loads(match)
            print(f"✅ {file.name} block {i}: Valid")
        except json.JSONDecodeError as e:
            print(f"❌ {file.name} block {i}: {e}")
EOF
```

## Online Validation Tools

### Google Rich Results Test
**URL:** https://search.google.com/test/rich-results  
**What to test:** 
- https://hack23.com/ (English)
- https://hack23.com/index_sv.html (Swedish)
- Any other page with structured data

**What to check:**
- ✅ Schema detected (FAQPage, Organization, BreadcrumbList, etc.)
- ❌ No errors
- ⚠️ Warnings are OK (usually recommendations)

### Schema.org Validator
**URL:** https://validator.schema.org/  
**How to use:**
1. View page source
2. Copy JSON-LD block (everything between `<script type="application/ld+json">` tags)
3. Paste into validator
4. Check for errors

### Google Search Console
**URL:** https://search.google.com/search-console  
**Navigation:** Enhancements → [Schema Type] (e.g., FAQPage, Article, BreadcrumbList)  
**What to monitor:**
- Valid pages count
- Error count (should be 0)
- Warning count (low is OK)
- Impressions and clicks

## Common Schema Types on Hack23 Website

| Schema Type | Pages | Required Properties | Notes |
|------------|-------|-------------------|--------|
| **Organization** | All homepages | name, url | Main business entity |
| **FAQPage** | All homepages | mainEntity | Should be only 1 per page |
| **BreadcrumbList** | Most pages | itemListElement | Navigation hierarchy |
| **BlogPosting** | Blog posts | headline, datePublished, author | Article content |
| **WebPage** | All pages | name, url | Page metadata |
| **Service** | Homepages | name, provider | Consulting services |
| **SoftwareApplication** | Product pages | name, applicationCategory | Software products |
| **VideoGame** | Black Trigram pages | name, gamePlatform | Game product |

## Pre-Deployment Checklist

Before pushing changes that affect structured data:

- [ ] **Run validation script:** `python3 validate_structured_data.py`
- [ ] **Check for duplicates:** Ensure no duplicate schema types per page
- [ ] **Validate JSON syntax:** All JSON-LD blocks parse correctly
- [ ] **Test with Google Rich Results:** At least 1 affected page
- [ ] **Update all language versions:** Changes applied consistently
- [ ] **Check canonical tags:** Self-referencing for localized pages
- [ ] **Verify hreflang tags:** Bidirectional links present
- [ ] **Review modified dateModified:** Update if content changed significantly

## Schema Update Workflow

### When updating FAQ content:

```bash
# 1. Find the FAQPage schema
grep -n "FAQPage" index.html

# 2. Edit within existing schema block
# DO NOT create a new <script> tag

# 3. Validate after editing
python3 validate_structured_data.py

# 4. Test with Google
# Visit: https://search.google.com/test/rich-results

# 5. Apply to all language versions
for file in index_sv.html index_ko.html index_nl.html; do
  echo "Don't forget to update: $file"
done
```

### When adding new structured data:

```bash
# 1. Choose correct schema type from schema.org
# Visit: https://schema.org/

# 2. Add to existing @graph if present, or create new block
# Example for adding to @graph:
# "@graph": [
#   { existing schemas },
#   { "@type": "NewType", ... }
# ]

# 3. Validate required properties
# Check schema.org documentation

# 4. Test and validate
python3 validate_structured_data.py
```

## Troubleshooting

### Issue: "Duplicate field 'FAQPage'" in Search Console

**Cause:** Multiple FAQPage schema blocks on same page  
**Solution:** 
```bash
# Find duplicates
grep -n "FAQPage" index.html

# Keep only one (the most comprehensive)
# Remove duplicate <script type="application/ld+json"> block

# Validate
python3 validate_structured_data.py
```

### Issue: "Missing required property"

**Cause:** Schema missing required field (e.g., `name`, `url`, `datePublished`)  
**Solution:**
```bash
# Check what's required for your schema type
# Visit: https://developers.google.com/search/docs/appearance/structured-data

# Add missing properties to JSON-LD
# Validate with: python3 validate_structured_data.py
```

### Issue: JSON parsing error

**Cause:** Invalid JSON syntax (missing comma, bracket, quote)  
**Solution:**
```bash
# Extract JSON-LD and test
python3 << 'EOF'
import json
content = open('index.html').read()
# Extract relevant block
# json.loads(block) will show exact error
EOF

# Common issues:
# - Missing comma between properties
# - Unescaped quotes in text
# - Missing closing brackets
```

### Issue: Canonical or hreflang errors

**Cause:** Missing or incorrect tags  
**Solution:**
```bash
# Check canonical tags
grep -n "canonical" index.html

# Check hreflang tags
grep -n "hreflang" index.html

# Ensure:
# - English: canonical to https://hack23.com/
# - Localized: canonical to self (e.g., index_sv.html)
# - All: hreflang tags for all 11 languages + x-default
```

## Regular Monitoring Schedule

### Weekly
- [ ] Check Google Search Console for new structured data errors
- [ ] Review any declined pages or warnings

### Monthly
- [ ] Run full validation: `python3 validate_structured_data.py`
- [ ] Check rich result impressions and CTR in Search Console
- [ ] Review Google's structured data documentation for updates

### Quarterly
- [ ] Full audit of all structured data across site
- [ ] Update schemas based on Google's latest guidelines
- [ ] Test sample pages with Google Rich Results Test
- [ ] Review and update this documentation if needed

## Quick Reference: Schema.org Properties

### Organization
```json
{
  "@type": "Organization",
  "name": "Required",
  "url": "Required",
  "logo": "Recommended",
  "description": "Recommended",
  "address": "Recommended for local business"
}
```

### FAQPage
```json
{
  "@type": "FAQPage",
  "mainEntity": [ /* Required: array of Questions */
    {
      "@type": "Question",
      "name": "Required: question text",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Required: answer text"
      }
    }
  ]
}
```

### BlogPosting
```json
{
  "@type": "BlogPosting",
  "headline": "Required",
  "datePublished": "Required",
  "author": "Required",
  "image": "Recommended",
  "publisher": "Recommended"
}
```

### BreadcrumbList
```json
{
  "@type": "BreadcrumbList",
  "itemListElement": [ /* Required */
    {
      "@type": "ListItem",
      "position": 1, /* Required */
      "name": "Home", /* Required */
      "item": "https://example.com/" /* Recommended */
    }
  ]
}
```

## Resources

- **Google Search Central:** https://developers.google.com/search/docs/appearance/structured-data
- **Schema.org:** https://schema.org/
- **Google Rich Results Test:** https://search.google.com/test/rich-results
- **Schema.org Validator:** https://validator.schema.org/
- **JSON-LD Playground:** https://json-ld.org/playground/

## Contact

For questions or issues with structured data:
- **Email:** james@hack23.com
- **See also:** SEO_FAQPAGE_FIX_REPORT.md for detailed fix documentation

---

**Last Updated:** November 26, 2025  
**Maintained by:** Hack23 AB Development Team

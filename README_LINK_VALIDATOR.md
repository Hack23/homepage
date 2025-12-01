# Internal Link Validator

Validates all internal links across HTML pages, excluding metadata links in `<head>` sections (hreflang, canonical, etc.).

## Usage

```bash
python3 validate_internal_links.py
```

## What It Checks

- Links in `<a href="">` tags within the `<body>` section
- Relative links (page.html)
- Root-relative links (/page.html)
- Absolute hack23.com links

## What It Excludes

- Metadata in `<head>` section (hreflang, canonical, etc.)
- External links
- Protocol links (mailto:, tel:, etc.)
- Code examples in `<pre>` and `<code>` tags
- HTML comments

## Exit Codes

- 0 = All links valid
- 1 = Broken links found

## Output

- Console report with statistics
- `link_validation_report.json` for detailed analysis

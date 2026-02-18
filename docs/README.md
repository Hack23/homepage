# Release Documentation Directory

This directory contains automatically generated documentation and reports for each release.

## Generated Content

The release workflow automatically generates the following documentation and reports:

- **lighthouse-*.html** - Individual Lighthouse reports for each audited page (performance, accessibility, best practices, and SEO)
- **lighthouse-summary.html** - Aggregated Lighthouse summary report across all audited pages
- **html-validation.txt** - HTML validation results for all pages
- **accessibility-report.html** - WCAG 2.1 AA compliance verification
- **security-report.html** - OWASP ZAP security scan results
- **SBOM files** - Software Bill of Materials in SPDX format, published as GitHub Release assets
- **Attestation files** - Build provenance and SBOM attestations, published as GitHub Release assets

## Documentation as Code

Generated documentation and reports are:
- ✅ Automatically generated during release
- ✅ HTML and validation reports are committed to the repository
- ✅ Committed reports are versioned alongside code
- ✅ SBOM and attestation files are available as assets in each GitHub Release

View releases at: https://github.com/Hack23/homepage/releases

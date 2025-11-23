# Cache Optimization Recommendations

## Overview
This document provides recommendations for improving cache lifetimes for external resources to enhance Lighthouse performance scores.

## External Resources Cache Issues

The following external resources currently have short cache lifetimes and should be optimized:

### 1. GitHub Utility Resources
- **Resource**: GitHub raw content (e.g., CIA logo from `raw.githubusercontent.com`)
- **Current Cache TTL**: ~5 minutes
- **Recommendation**: Consider hosting static assets locally or using a CDN with longer cache durations
- **Action**: Copy external images to the repository and update references

### 2. Shields.io Badges
- **Resources**: 
  - OpenSSF Scorecard badge (`img.shields.io`) - 2 minute TTL
  - GitHub badge (`img.shields.io`) - 1 day TTL
- **Current Issue**: Dynamic badges have short cache times by design
- **Recommendation**: For static badges, consider:
  - Using static badge images downloaded and hosted locally
  - Implementing Service Worker caching strategy
  - Accepting the trade-off between freshness and caching for dynamic badges

## Implementation Notes

### AWS CloudFront Configuration
The site is deployed via AWS S3 + CloudFront. To improve caching:

1. **S3 Bucket Configuration**:
   - Set appropriate `Cache-Control` headers for static assets
   - Example: `Cache-Control: public, max-age=31536000, immutable` for versioned assets

2. **CloudFront Distribution**:
   - Configure cache behaviors for different file types
   - Use query string forwarding judiciously
   - Consider using Lambda@Edge for custom cache control logic

### Recommended Cache-Control Headers

```
# Static Images (versioned)
Cache-Control: public, max-age=31536000, immutable

# HTML Pages
Cache-Control: public, max-age=3600, must-revalidate

# CSS/JS (versioned via hash/version)
Cache-Control: public, max-age=31536000, immutable

# CSS/JS (not versioned)
Cache-Control: public, max-age=86400, must-revalidate

# Fonts
Cache-Control: public, max-age=31536000, immutable
```

## Trade-offs to Consider

1. **Dynamic Badges**: Some badges (OpenSSF Scorecard) update frequently and intentionally have short cache times to show current status
2. **Security Updates**: Longer cache times may delay security badge updates
3. **Development Workflow**: Aggressive caching requires cache-busting strategies during updates

## Next Steps

1. Audit external dependencies and determine which can be hosted locally
2. Implement CloudFront cache policies via GitHub Actions workflow
3. Consider using Service Worker for advanced caching strategies
4. Monitor Lighthouse scores after implementing changes

## References

- [Lighthouse: Uses Long Cache Lifetimes](https://web.dev/uses-long-cache-ttl/)
- [AWS CloudFront Cache Control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html)
- [HTTP Caching Best Practices](https://web.dev/http-cache/)

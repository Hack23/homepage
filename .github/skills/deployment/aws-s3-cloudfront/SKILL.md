---
name: aws-s3-cloudfront
description: AWS S3 bucket configuration, CloudFront distribution setup, security headers (CSP, HSTS), cache policies, and SSL/TLS configuration
license: Apache-2.0
---

# AWS S3/CloudFront Deployment Skill

## Purpose

Defines secure configuration and deployment practices for static websites using AWS S3 for storage and CloudFront CDN for global distribution.

## Rules

### S3 Bucket Configuration

**MUST:**
- Block all public access (use CloudFront Origin Access Identity)
- Enable versioning
- Enable server-side encryption (AES-256)
- Enable access logging
- Set lifecycle policies for old versions
- Use least-privilege IAM policies

**Example Bucket Policy:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCloudFrontOAI",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity EXAMPLE"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}
```

### CloudFront Distribution

**MUST:**
- Use HTTPS only (redirect HTTP → HTTPS)
- Use TLS 1.2 as minimum
- Enable HTTP/2 and HTTP/3
- Configure custom SSL certificate (ACM)
- Set appropriate cache TTLs
- Enable gzip/Brotli compression
- Use Origin Access Identity (OAI) for S3
- Configure custom error pages

**Security Headers (Lambda@Edge or CloudFront Functions):**
```javascript
function handler(event) {
  var response = event.response;
  var headers = response.headers;
  
  // Security Headers
  headers['strict-transport-security'] = {
    value: 'max-age=31536000; includeSubDomains; preload'
  };
  headers['content-security-policy'] = {
    value: "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self' data:; connect-src 'self'"
  };
  headers['x-content-type-options'] = { value: 'nosniff' };
  headers['x-frame-options'] = { value: 'SAMEORIGIN' };
  headers['x-xss-protection'] = { value: '1; mode=block' };
  headers['referrer-policy'] = { value: 'strict-origin-when-cross-origin' };
  headers['permissions-policy'] = { value: 'geolocation=(), microphone=(), camera=()' };
  
  return response;
}
```

### Cache Configuration

**Recommended TTLs:**
- HTML files: 0-3600s (1 hour max)
- CSS/JS: 31536000s (1 year, use cache busting)
- Images: 31536000s (1 year)
- Fonts: 31536000s (1 year)

**CloudFront Cache Policy:**
```json
{
  "CachePolicyConfig": {
    "Name": "StaticWebsite-CachePolicy",
    "MinTTL": 0,
    "MaxTTL": 31536000,
    "DefaultTTL": 86400,
    "ParametersInCacheKeyAndForwardedToOrigin": {
      "EnableAcceptEncodingGzip": true,
      "EnableAcceptEncodingBrotli": true,
      "QueryStringsConfig": {
        "QueryStringBehavior": "none"
      },
      "HeadersConfig": {
        "HeaderBehavior": "none"
      },
      "CookiesConfig": {
        "CookieBehavior": "none"
      }
    }
  }
}
```

## Related Documentation

- [github-actions-cicd SKILL.md](../github-actions-cicd/SKILL.md)
- [security-architecture SKILL.md](../../architecture/security-architecture/SKILL.md)

# Content Security Policy (CSP) Implementation Documentation

## 📋 Overview

This document describes the Content Security Policy (CSP) and related security headers implemented across all 74 HTML pages of the Hack23 AB website to mitigate XSS attacks, clickjacking, and other web vulnerabilities.

**Implementation Date:** November 13, 2025  
**Related Issue:** [#356 - Implement Content Security Policy (CSP) Meta Tags](https://github.com/Hack23/homepage/issues/356)  
**ZAP Scan Issue:** [#355 - ZAP Security Scan Report](https://github.com/Hack23/homepage/issues/355)

## 🛡️ Security Headers Implemented

All 74 HTML files now include the following security headers in the `<head>` section:

```html
<!-- Security Headers -->
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https:; connect-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'; object-src 'none'; upgrade-insecure-requests;">
<meta http-equiv="Cross-Origin-Opener-Policy" content="same-origin">
<meta http-equiv="X-Content-Type-Options" content="nosniff">
<meta http-equiv="X-Frame-Options" content="DENY">
<meta http-equiv="Referrer-Policy" content="strict-origin-when-cross-origin">
```

## 📖 Policy Breakdown

### Content-Security-Policy Directives

| Directive | Value | Rationale |
|-----------|-------|-----------|
| `default-src` | `'self'` | Only allow resources from the same origin by default |
| `script-src` | `'self'` | Only allow JavaScript from the same origin. JSON-LD structured data scripts (`type="application/ld+json"`) don't execute and are not subject to this directive |
| `style-src` | `'self' 'unsafe-inline' https://fonts.googleapis.com` | Allow same-origin styles, inline styles (used in 19 HTML files), and Google Fonts CSS |
| `font-src` | `'self' https://fonts.gstatic.com` | Allow fonts from same origin and Google Fonts CDN |
| `img-src` | `'self' data: https:` | Allow same-origin images, data URIs, and any HTTPS images (needed for external badges from shields.io, GitHub, etc.) |
| `connect-src` | `'self'` | Only allow AJAX/fetch requests to same origin |
| `frame-ancestors` | `'none'` | Prevent page from being embedded in iframes (anti-clickjacking) |
| `base-uri` | `'self'` | Restrict base tag URLs to same origin |
| `form-action` | `'self'` | Only allow form submissions to same origin |
| `object-src` | `'none'` | Disallow plugins (Flash, Java, etc.) |
| `upgrade-insecure-requests` | (flag) | Automatically upgrade HTTP requests to HTTPS |

### Additional Security Headers

| Header | Value | Purpose |
|--------|-------|---------|
| `Cross-Origin-Opener-Policy` | `same-origin` | Mitigates Spectre-class attacks by isolating browsing context |
| `X-Content-Type-Options` | `nosniff` | Prevents MIME type sniffing |
| `X-Frame-Options` | `DENY` | Prevents clickjacking attacks (legacy support, also covered by CSP) |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | Controls referrer information in cross-origin requests |

## 🎯 Security Issues Addressed

This implementation addresses the following ZAP security scan findings:

### ✅ Resolved Issues

1. **CSP: Failure to Define Directive with No Fallback**
   - All major directives are now explicitly defined with fallback to `default-src 'self'`

2. **CSP: script-src unsafe-inline**
   - No `'unsafe-inline'` in `script-src` - only allowing same-origin scripts
   - JSON-LD structured data is exempt from CSP script restrictions

3. **CSP: style-src unsafe-inline**
   - While `'unsafe-inline'` is still present in `style-src`, this is necessary for:
     - Inline styles in 19 HTML files (e.g., `style="width:50%;"`)
     - Google Fonts preconnect hints
   - **Mitigation:** Future work can move inline styles to external stylesheet

4. **Insufficient Site Isolation Against Spectre Vulnerability**
   - Implemented `Cross-Origin-Opener-Policy: same-origin`
   - **Note:** `Cross-Origin-Embedder-Policy: require-corp` was NOT implemented as it would break external badge images from shields.io, GitHub assets, etc. This is an acceptable tradeoff for a static marketing site with no sensitive data processing.

5. **Missing Security Headers**
   - Added `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`

## 🔍 Design Decisions

### Why `'unsafe-inline'` in style-src?

The site currently uses inline styles in 19 HTML files, primarily for:
- Table layouts (`style="width:50%"`)
- Flexbox containers
- Text alignment and padding

**Alternatives Considered:**
1. **Remove all inline styles** - Would require extensive refactoring of 19 files
2. **Use nonce/hash for each inline style** - Not practical with 74+ pages and dynamic content
3. **Accept `'unsafe-inline'` with mitigation** - Current approach

**Mitigation Strategy:**
- Inline styles are minimal and developer-controlled
- No user-generated content is styled
- Future refactoring can move styles to external stylesheet

### Why `img-src` allows all HTTPS?

The site displays many external badge images:
- shields.io badges (build status, version, etc.)
- GitHub badges
- OpenSSF Scorecard
- SonarCloud metrics
- FOSSA license scans

**Alternatives Considered:**
1. **List each domain explicitly** - Would be fragile and require updates
2. **Self-host all badges** - Not practical for dynamic badges
3. **Allow all HTTPS images** - Current approach, acceptable for static site

### Why no Cross-Origin-Embedder-Policy?

`Cross-Origin-Embedder-Policy: require-corp` requires all cross-origin resources to opt-in via CORS headers or CORP headers. This would break:
- External badge images from shields.io, GitHub, etc.
- Google Fonts
- Any future external resources

**Risk Assessment:**
- This is a static marketing website with no sensitive data
- No SharedArrayBuffer or high-resolution timers are used
- Spectre vulnerability risk is minimal in this context

**Mitigation:**
- Implemented `Cross-Origin-Opener-Policy: same-origin` for process isolation
- No sensitive operations in JavaScript
- Future consideration if site adds dynamic features

## 📊 Implementation Statistics

- **Total HTML files updated:** 74
- **Files with inline styles:** 19
- **External script sources:** None (only JSON-LD structured data)
- **External style sources:** Google Fonts (fonts.googleapis.com)
- **External image sources:** Multiple HTTPS domains (shields.io, GitHub, etc.)

## ✅ Testing & Validation

### Manual Testing Checklist

- [x] Index pages load correctly (index.html, index_sv.html, index_ko.html)
- [x] Google Fonts load properly
- [x] External badge images display correctly
- [x] Inline styles render as expected
- [x] JSON-LD structured data is not blocked
- [x] Browser console shows no CSP violations

### Browser Compatibility

These meta tags are supported by all modern browsers:
- Chrome/Edge 76+
- Firefox 79+
- Safari 15.4+

### CSP Validation Tools

The policy can be validated using:
- [CSP Evaluator by Google](https://csp-evaluator.withgoogle.com/)
- [Mozilla Observatory](https://observatory.mozilla.org/)
- Browser Developer Tools (Console for CSP violations)

## 🔮 Future Improvements

### Short Term
1. **Move inline styles to external stylesheet** - Remove need for `'unsafe-inline'` in style-src
2. **Add CSP headers at CloudFront level** - Currently using meta tags; HTTP headers are preferred
3. **Monitor CSP violations** - Set up CSP reporting endpoint

### Long Term
1. **Consider Cross-Origin-Embedder-Policy** - If external dependencies can be updated with CORS/CORP headers
2. **Implement Subresource Integrity (SRI)** - For external resources like Google Fonts
3. **Stricter img-src** - List specific domains instead of allowing all HTTPS

## 📚 References

- [MDN: Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)
- [OWASP CSP Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
- [Google CSP Evaluator](https://csp-evaluator.withgoogle.com/)
- [Web.dev: Mitigating Spectre](https://web.dev/spectre/)

## 🤝 Contributing

When adding new features or content:

1. **Avoid inline scripts** - Use external files or JSON-LD for structured data
2. **Minimize inline styles** - Add styles to `styles.css` instead
3. **Test CSP compliance** - Check browser console for violations
4. **Update this document** - If CSP policy needs changes

## 📝 Change Log

### 2025-11-13 - Initial Implementation
- Added CSP meta tags to all 74 HTML files
- Added Cross-Origin-Opener-Policy header
- Added X-Content-Type-Options, X-Frame-Options, Referrer-Policy headers
- Created this documentation

---

**Maintained by:** Hack23 AB  
**Contact:** [LinkedIn Company Page](https://www.linkedin.com/company/hack23/)  
**Repository:** [GitHub - Hack23/homepage](https://github.com/Hack23/homepage)

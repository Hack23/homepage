---
name: input-validation
description: Comprehensive input validation and output encoding practices to prevent injection attacks across all Hack23 projects
license: Apache-2.0
---

# Input Validation Skill

## Purpose

Ensure all user-supplied and external data is properly validated before processing and all output is properly encoded, preventing injection attacks (XSS, SQLi, command injection, path traversal) across all Hack23 projects.

## Rules

### Input Validation

**MUST:**
- Validate ALL input at the point of entry (server-side validation is mandatory)
- Use allowlist validation (define what IS allowed, not what ISN'T)
- Validate data type, length, format, and range
- Reject invalid input with clear error messages (without exposing system details)
- Sanitize file names and paths to prevent path traversal
- Validate content type for file uploads
- Apply consistent validation across all API endpoints

**MUST NOT:**
- Rely solely on client-side validation
- Trust data from external sources without validation
- Use blocklist validation as the primary defense
- Echo raw user input back to the browser
- Expose stack traces or system information in error messages
- Accept arbitrary file paths from user input

### Output Encoding

**MUST:**
- Encode output before rendering in HTML context (HTML entity encoding)
- Use parameterized queries for all database operations
- Use framework-provided template engines with auto-escaping enabled
- Encode data appropriately for the output context (HTML, URL, JavaScript, CSS)
- Set `Content-Type` headers correctly on all responses

**MUST NOT:**
- Build SQL queries with string concatenation
- Use `innerHTML` with unsanitized user input
- Disable auto-escaping in template engines
- Pass user input directly to shell commands

### Content Security Policy

**MUST:**
- Set strict Content-Security-Policy headers
- Avoid `unsafe-inline` and `unsafe-eval` in CSP directives where possible
- Use nonce-based CSP for inline scripts when absolutely needed

### For Static HTML Sites (homepage)

**MUST:**
- Escape all dynamic content in meta tags
- Validate and sanitize URLs in href/src attributes
- Use `rel="noopener noreferrer"` for external links
- Ensure all forms use proper action URLs and method attributes

## Hack23 ISMS Policy References

- [Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md)
- [Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)

## Compliance Mapping

- **ISO 27001:2022**: A.8.26 (Application Security Requirements)
- **NIST CSF 2.0**: PR.DS (Data Security)
- **CIS Controls v8.1**: Control 16 (Application Software Security)
- **OWASP Top 10**: A03:2021 (Injection), A07:2021 (XSS)

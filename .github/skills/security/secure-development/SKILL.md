---
name: secure-development
description: Security-by-design principles for developing secure applications following Hack23 ISMS Secure Development Policy
license: Apache-2.0
---

# Secure Development Skill

## Purpose

This skill ensures all code development follows security-by-design principles as defined in the [Hack23 ISMS Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md). It applies to all software development activities including web applications, APIs, infrastructure code, and scripts.

## Rules

### Input Validation

**MUST:**
- Validate ALL user input at the point of entry (server-side validation is mandatory)
- Use allowlist validation (define what IS allowed, not what ISN'T)
- Validate data type, length, format, and range
- Encode output before rendering to prevent XSS
- Sanitize input before use in queries, commands, or file operations
- Reject invalid input with clear error messages (without exposing system details)

**MUST NOT:**
- Rely solely on client-side validation
- Trust data from external sources (APIs, databases, files) without validation
- Use blocklist validation as the primary defense
- Echo raw user input back to the browser
- Expose stack traces or system information in error messages

### Authentication and Authorization

**MUST:**
- Enforce authentication for all non-public resources
- Implement multi-factor authentication (MFA) for administrative access
- Use secure session management (HTTPOnly, Secure, SameSite cookies)
- Enforce strong password policies (minimum 12 characters, complexity requirements)
- Implement account lockout after failed login attempts (5 attempts)
- Log all authentication events (success and failure)
- Use the principle of least privilege for all access controls
- Verify authorization at each access point, not just at entry

**MUST NOT:**
- Store passwords in plaintext or reversible encryption
- Use weak hashing algorithms (MD5, SHA-1) for passwords
- Implement custom authentication schemes without security review
- Share authentication credentials between users or systems
- Grant broad access by default

### Cryptography

**MUST:**
- Use AES-256 for symmetric encryption
- Use RSA-2048 or higher for asymmetric encryption
- Use SHA-256 or higher for hashing
- Enforce TLS 1.2 or higher for all network communications
- Store cryptographic keys securely (use key management systems, not code)
- Use cryptographically secure random number generators (not Math.random())
- Rotate encryption keys according to policy

**MUST NOT:**
- Hard-code encryption keys, passwords, or secrets in source code
- Use deprecated algorithms (DES, 3DES, MD5, SHA-1, SSL, TLS 1.0/1.1)
- Implement custom cryptographic algorithms
- Store secrets in version control (use secret management tools)
- Use weak or predictable initialization vectors (IVs)

### Secure Error Handling

**MUST:**
- Implement centralized error handling
- Log all security-relevant errors with sufficient detail for investigation
- Return generic error messages to users
- Fail securely (deny access on error, don't fall back to insecure state)
- Clean up resources in finally blocks or using equivalent patterns
- Monitor and alert on unusual error patterns

**MUST NOT:**
- Expose stack traces to users
- Include sensitive data in error messages (passwords, keys, tokens, PII)
- Log sensitive data (passwords, credit card numbers, SSNs)
- Continue processing after critical security errors
- Suppress security exceptions without logging

### Secure Configuration

**MUST:**
- Use environment variables or secret management for sensitive configuration
- Implement secure defaults (disable debug mode, enable security headers)
- Document all security-relevant configuration options
- Review configuration changes for security implications
- Use principle of least privilege for service accounts and API keys
- Disable unnecessary features, services, and endpoints

**MUST NOT:**
- Commit configuration files with secrets to version control
- Use default credentials in production
- Enable debug/verbose logging in production
- Expose administrative interfaces to public networks
- Use overly permissive CORS policies

### Security Testing

**MUST:**
- Perform static application security testing (SAST) on every commit
- Perform dynamic application security testing (DAST) before production deployment
- Include security test cases in test suites
- Perform dependency vulnerability scanning
- Test authentication and authorization controls
- Test input validation for injection vulnerabilities
- Document security test results

**MUST NOT:**
- Deploy code without passing security scans
- Ignore or suppress security findings without proper justification and approval
- Test security controls in production environments
- Use production data in testing environments

### Dependency Management

**MUST:**
- Use dependency scanning tools (e.g., Dependabot, Snyk)
- Keep dependencies up to date with security patches
- Review dependencies for known vulnerabilities before use
- Use package lock files to ensure reproducible builds
- Document approved dependencies and their versions
- Remove unused dependencies

**MUST NOT:**
- Use dependencies with known critical vulnerabilities
- Use abandoned or unmaintained dependencies
- Download dependencies from untrusted sources
- Bypass dependency version constraints without security review

### Code Review

**MUST:**
- Require peer review for all code changes
- Include security review in code review process
- Use automated security scanning in PR pipelines
- Document security decisions in PR comments
- Verify security requirements are met before approval

**MUST NOT:**
- Merge code without required approvals
- Bypass security checks in CI/CD pipeline
- Approve your own security-critical changes

## Examples

### Example 1: Secure Input Validation (JavaScript)

```javascript
// GOOD: Allowlist validation with type checking
function validateUsername(username) {
  // Define what IS allowed
  const usernameRegex = /^[a-zA-Z0-9_-]{3,20}$/;
  
  // Validate type
  if (typeof username !== 'string') {
    throw new Error('Invalid input type');
  }
  
  // Validate format and length
  if (!usernameRegex.test(username)) {
    throw new Error('Username must be 3-20 characters and contain only letters, numbers, hyphens, and underscores');
  }
  
  return username;
}

// BAD: No validation
function validateUsernameBad(username) {
  return username; // Accepts anything!
}

// BAD: Blocklist validation
function validateUsernameBad2(username) {
  if (username.includes('<') || username.includes('>')) {
    throw new Error('Invalid characters');
  }
  return username; // Still vulnerable to many attacks
}
```

### Example 2: Secure Password Hashing (Node.js)

```javascript
const bcrypt = require('bcrypt');

// GOOD: Use strong hashing with salt
async function hashPassword(password) {
  // MUST use at least 12 rounds (2^12 iterations)
  const saltRounds = 12;
  const hashedPassword = await bcrypt.hash(password, saltRounds);
  return hashedPassword;
}

async function verifyPassword(password, hashedPassword) {
  return await bcrypt.compare(password, hashedPassword);
}

// BAD: Using weak hashing
const crypto = require('crypto');
function hashPasswordBad(password) {
  // NEVER use MD5 or SHA-1 for passwords!
  return crypto.createHash('md5').update(password).digest('hex');
}

// BAD: Storing plaintext
function storePasswordBad(password) {
  return password; // NEVER store passwords in plaintext!
}
```

### Example 3: Secure Session Management (Express.js)

```javascript
const session = require('express-session');
const RedisStore = require('connect-redis')(session);

// GOOD: Secure session configuration
app.use(session({
  store: new RedisStore({ client: redisClient }),
  secret: process.env.SESSION_SECRET, // From environment, not hardcoded
  name: 'sessionId', // Don't use default 'connect.sid'
  resave: false,
  saveUninitialized: false,
  cookie: {
    secure: true,      // MUST use HTTPS
    httpOnly: true,    // MUST prevent JavaScript access
    maxAge: 1800000,   // 30 minutes
    sameSite: 'strict' // CSRF protection
  }
}));

// BAD: Insecure session configuration
app.use(session({
  secret: 'mysecret123', // Hardcoded secret!
  cookie: {
    secure: false,    // Allows HTTP
    httpOnly: false   // Vulnerable to XSS
  }
}));
```

### Example 4: Preventing SQL Injection (Node.js)

```javascript
const mysql = require('mysql2/promise');

// GOOD: Parameterized queries
async function getUserByEmail(email) {
  const [rows] = await connection.execute(
    'SELECT * FROM users WHERE email = ?',
    [email]
  );
  return rows[0];
}

// BAD: String concatenation
async function getUserByEmailBad(email) {
  // NEVER concatenate user input into SQL!
  const query = `SELECT * FROM users WHERE email = '${email}'`;
  const [rows] = await connection.execute(query);
  return rows[0];
}
```

### Example 5: Secure Error Handling (Python)

```python
import logging

# GOOD: Generic error messages to users, detailed logging
def process_payment(user_id, amount):
    try:
        # Process payment logic
        charge_credit_card(user_id, amount)
        return {"success": True, "message": "Payment processed"}
    except CreditCardError as e:
        # Log detailed error securely
        logging.error(f"Payment failed for user {user_id}: {str(e)}", 
                     extra={"user_id": user_id, "amount": amount})
        # Return generic message to user
        return {"success": False, "message": "Payment processing failed. Please try again."}
    except Exception as e:
        # Log unexpected errors
        logging.exception(f"Unexpected error processing payment for user {user_id}")
        # Return generic message
        return {"success": False, "message": "An error occurred. Please contact support."}

# BAD: Exposing detailed errors
def process_payment_bad(user_id, amount):
    try:
        charge_credit_card(user_id, amount)
        return {"success": True}
    except Exception as e:
        # NEVER expose stack traces or system details to users!
        return {"success": False, "error": str(e), "trace": traceback.format_exc()}
```

### Example 6: Secure Configuration (Environment Variables)

```javascript
// GOOD: Use environment variables for secrets
require('dotenv').config();

const config = {
  database: {
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD, // Never hardcode!
    database: process.env.DB_NAME
  },
  api: {
    key: process.env.API_KEY,
    secret: process.env.API_SECRET
  },
  // Secure defaults
  security: {
    httpsOnly: true,
    hstsEnabled: true,
    debugMode: false
  }
};

// Validate required environment variables
const required = ['DB_HOST', 'DB_USER', 'DB_PASSWORD', 'API_KEY'];
required.forEach(key => {
  if (!process.env[key]) {
    throw new Error(`Missing required environment variable: ${key}`);
  }
});

// BAD: Hardcoded secrets
const configBad = {
  database: {
    host: 'localhost',
    user: 'admin',
    password: 'P@ssw0rd123', // NEVER hardcode passwords!
    database: 'production'
  },
  api: {
    key: 'sk_live_abcdef123456' // NEVER commit API keys!
  }
};
```

### Example 7: XSS Prevention (HTML Output Encoding)

```javascript
// GOOD: Encode output before rendering
function escapeHtml(unsafe) {
  return unsafe
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function displayUserComment(comment) {
  const safeComment = escapeHtml(comment);
  document.getElementById('comment').innerHTML = safeComment;
}

// Or use a trusted library
const DOMPurify = require('dompurify');
function displayUserContent(content) {
  const clean = DOMPurify.sanitize(content);
  document.getElementById('content').innerHTML = clean;
}

// BAD: Direct HTML insertion
function displayUserCommentBad(comment) {
  // NEVER insert unsanitized user input into HTML!
  document.getElementById('comment').innerHTML = comment;
}
```

## Related ISMS Policies

This skill implements requirements from:

- **[Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md)** - Primary policy for secure coding practices
- **[Access Control Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Access_Control_Policy.md)** - Authentication and authorization requirements
- **[Cryptographic Controls Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Cryptographic_Controls_Policy.md)** - Encryption and hashing requirements
- **[Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)** - Overall security framework
- **[Data Classification Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Data_Classification_Policy.md)** - Data handling requirements

## Related Documentation

- [SECURITY_ARCHITECTURE.md](../../../../SECURITY_ARCHITECTURE.md) - Security controls and architecture
- [THREAT_MODEL.md](../../../../THREAT_MODEL.md) - Threat analysis and mitigation
- [SECURITY.md](../../../../SECURITY.md) - Security vulnerability reporting

## Compliance Mapping

### ISO 27001:2022
- **A.8.24** Use of cryptography
- **A.8.25** Secure development life cycle
- **A.8.26** Application security requirements
- **A.8.28** Secure coding

### NIST Cybersecurity Framework
- **PR.DS-2**: Data-in-transit is protected
- **PR.DS-6**: Integrity checking mechanisms verify software integrity
- **PR.IP-2**: A System Development Life Cycle to manage systems is implemented

### CIS Controls
- **Control 16**: Application Software Security
  - 16.1 Establish and Maintain a Secure Application Development Process
  - 16.2 Establish and Maintain a Process to Accept and Address Software Vulnerabilities
  - 16.10 Apply Secure Design Principles in Application Architectures

## Enforcement

Violations of secure development rules:
- **Critical violations** (hardcoded secrets, use of banned algorithms): Block deployment, require immediate remediation
- **High severity violations** (missing input validation, weak authentication): Require remediation before merge
- **Medium severity violations**: Require remediation within sprint
- **Low severity violations**: Create technical debt tickets

All violations must be tracked and reported in security metrics.

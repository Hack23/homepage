---
name: cryptography
description: Approved cryptographic algorithms, TLS enforcement, key management, and certificate handling per Hack23 Cryptographic Controls Policy
license: Apache-2.0
---

# Cryptography Skill

## Purpose

This skill enforces cryptographic requirements as defined in the [Hack23 ISMS Cryptographic Controls Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Cryptographic_Controls_Policy.md). It ensures that all cryptographic operations use approved algorithms and follow best practices for key management.

## Rules

### Approved Algorithms

**Symmetric Encryption - MUST USE:**
- **AES-256** (Advanced Encryption Standard, 256-bit key)
- **AES-128** (minimum, prefer AES-256)
- **ChaCha20-Poly1305** (for authenticated encryption)

**Asymmetric Encryption - MUST USE:**
- **RSA-2048** or higher (minimum 2048-bit key, prefer 3072 or 4096)
- **ECDSA** with P-256, P-384, or P-521 curves
- **Ed25519** (EdDSA with Curve25519)

**Hashing - MUST USE:**
- **SHA-256** (minimum)
- **SHA-384**
- **SHA-512**
- **SHA-3** family
- **BLAKE2** (for high-performance applications)

**Password Hashing - MUST USE:**
- **bcrypt** (cost factor 12 minimum)
- **scrypt**
- **Argon2id** (preferred)
- **PBKDF2** with SHA-256, minimum 100,000 iterations

**Message Authentication - MUST USE:**
- **HMAC-SHA256** (minimum)
- **HMAC-SHA512**

**MUST NOT USE (Deprecated/Broken):**
- DES, 3DES
- MD5, SHA-1 (except for non-security purposes like checksums)
- RC4
- RSA < 2048 bits
- CBC mode without authenticated encryption
- ECB mode (ever)

### TLS/SSL Requirements

**MUST:**
- Use TLS 1.2 as minimum
- Prefer TLS 1.3
- Use strong cipher suites only
- Verify server certificates
- Use certificate pinning for high-security applications
- Enforce HSTS (HTTP Strict Transport Security)
- Use Perfect Forward Secrecy (PFS) cipher suites

**TLS 1.2 Approved Cipher Suites (in order of preference):**
```
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
TLS_DHE_RSA_WITH_AES_128_GCM_SHA256
```

**TLS 1.3 Approved Cipher Suites:**
```
TLS_AES_256_GCM_SHA384
TLS_AES_128_GCM_SHA256
TLS_CHACHA20_POLY1305_SHA256
```

**MUST NOT:**
- Use SSL 2.0, SSL 3.0, TLS 1.0, TLS 1.1
- Use export-grade ciphers
- Use NULL cipher suites
- Use anonymous cipher suites
- Accept self-signed certificates in production (except for explicitly trusted CAs)

### Key Management

**MUST:**
- Generate keys using cryptographically secure random number generators (CSPRNGs)
- Store keys securely (use key management systems, HSMs for highly sensitive keys)
- Never hardcode keys in source code
- Use environment variables or secret management systems
- Rotate keys according to schedule:
  - TLS certificates: Annually or before expiry
  - Symmetric keys: Annually for CONFIDENTIAL data, quarterly for RESTRICTED
  - API keys: Annually or on compromise
  - Passwords: 90 days for privileged accounts
- Destroy keys securely when no longer needed
- Log key lifecycle events (creation, rotation, destruction)
- Separate key generation from key usage
- Use different keys for different purposes
- Implement key escrow for business continuity (with strict controls)

**Key Length Requirements:**
- AES: 256 bits (128 minimum)
- RSA: 2048 bits minimum (prefer 3072 or 4096)
- ECDSA: P-256 minimum (prefer P-384 or P-521)
- HMAC: 256 bits minimum

**MUST NOT:**
- Store keys in plaintext
- Commit keys to version control
- Send keys via email or unencrypted channels
- Reuse keys across different applications or contexts
- Use weak key derivation functions
- Share private keys

### Random Number Generation

**MUST:**
- Use cryptographically secure PRNGs (CSPRNGs)
- For Node.js: `crypto.randomBytes()`, `crypto.randomInt()`
- For Python: `secrets` module, `os.urandom()`
- For Java: `SecureRandom`
- For browser: `window.crypto.getRandomValues()`

**MUST NOT:**
- Use `Math.random()` for security purposes
- Use predictable seeds
- Use non-cryptographic PRNGs for security tokens, keys, or IVs

### Initialization Vectors (IVs) and Nonces

**MUST:**
- Generate unique IV/nonce for each encryption operation
- Use cryptographically random IVs for CBC mode
- Use sequential nonces for CTR/GCM modes (ensure uniqueness)
- Store IV with ciphertext (IVs are not secret)
- Never reuse IV with same key

**MUST NOT:**
- Use predictable or sequential IVs with CBC mode
- Reuse nonces with same key in CTR/GCM modes
- Treat IVs as secrets (they should be random but can be public)

### Certificate Management

**MUST:**
- Use certificates from trusted Certificate Authorities (CAs)
- Validate certificate chains
- Check certificate revocation status (CRL/OCSP)
- Use Subject Alternative Names (SANs) for multiple domains
- Implement certificate expiry monitoring and alerting
- Renew certificates before expiry (30-day minimum buffer)
- Use automated certificate management (e.g., Let's Encrypt with auto-renewal)
- Store private keys securely (encrypted, access-controlled)
- Use separate certificates for different services/environments

**Certificate Validity:**
- Production: Maximum 1 year
- Development/Testing: Maximum 90 days
- Internal CA: Maximum 2 years

**MUST NOT:**
- Use self-signed certificates in production (except for internal CA)
- Share private keys between certificates
- Use wildcard certificates without proper access controls
- Ignore certificate warnings or errors

### Encryption at Rest

**MUST:**
- Encrypt CONFIDENTIAL and RESTRICTED data at rest
- Use full disk encryption for laptops and mobile devices
- Use database encryption (TDE) for sensitive databases
- Encrypt sensitive files before storage in cloud services
- Use envelope encryption (encrypt data key with master key)
- Store encryption keys separately from encrypted data

**MUST NOT:**
- Store unencrypted CONFIDENTIAL or RESTRICTED data
- Use same key for encryption and authentication
- Use deterministic encryption for high-sensitivity data

### Encryption in Transit

**MUST:**
- Use TLS 1.2+ for all network communications
- Encrypt email containing CONFIDENTIAL or RESTRICTED data (S/MIME or PGP)
- Use VPN for remote access to internal systems
- Use SSH (not Telnet) for remote administration
- Use HTTPS for all web applications
- Use secure protocols (SFTP, FTPS, not FTP)

**MUST NOT:**
- Transmit RESTRICTED data over unencrypted channels
- Use unencrypted protocols (HTTP, FTP, Telnet, SMTP without TLS)
- Disable certificate verification

## Examples

### Example 1: Symmetric Encryption (Node.js)

```javascript
const crypto = require('crypto');

// GOOD: AES-256-GCM encryption
function encrypt(plaintext, key) {
  // Generate random IV (12 bytes for GCM)
  const iv = crypto.randomBytes(12);
  
  // Create cipher
  const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
  
  // Encrypt
  let ciphertext = cipher.update(plaintext, 'utf8', 'hex');
  ciphertext += cipher.final('hex');
  
  // Get authentication tag
  const authTag = cipher.getAuthTag();
  
  // Return IV + authTag + ciphertext
  return {
    iv: iv.toString('hex'),
    authTag: authTag.toString('hex'),
    ciphertext: ciphertext
  };
}

function decrypt(encrypted, key) {
  // Create decipher
  const decipher = crypto.createDecipheriv(
    'aes-256-gcm',
    key,
    Buffer.from(encrypted.iv, 'hex')
  );
  
  // Set authentication tag
  decipher.setAuthTag(Buffer.from(encrypted.authTag, 'hex'));
  
  // Decrypt
  let plaintext = decipher.update(encrypted.ciphertext, 'hex', 'utf8');
  plaintext += decipher.final('utf8');
  
  return plaintext;
}

// Generate secure key (store securely, don't hardcode!)
const key = crypto.randomBytes(32); // 256 bits

// Usage
const encrypted = encrypt('Sensitive data', key);
console.log('Encrypted:', encrypted);

const decrypted = decrypt(encrypted, key);
console.log('Decrypted:', decrypted);

// BAD: Using deprecated algorithm
function encryptBad(plaintext, key) {
  // NEVER use DES!
  const cipher = crypto.createCipheriv('des-ede3-cbc', key, iv);
  return cipher.update(plaintext, 'utf8', 'hex') + cipher.final('hex');
}
```

### Example 2: Password Hashing (Node.js with bcrypt)

```javascript
const bcrypt = require('bcrypt');

// GOOD: bcrypt with appropriate cost factor
async function hashPassword(password) {
  // Cost factor 12 = 2^12 iterations (minimum)
  const saltRounds = 12;
  const hash = await bcrypt.hash(password, saltRounds);
  return hash;
}

async function verifyPassword(password, hash) {
  return await bcrypt.compare(password, hash);
}

// Usage
const password = 'MySecurePassword123!';
const hash = await hashPassword(password);
console.log('Hash:', hash);

const isValid = await verifyPassword(password, hash);
console.log('Valid:', isValid);

// BAD: Using weak hashing
function hashPasswordBad(password) {
  // NEVER use MD5 or SHA-1 for passwords!
  return crypto.createHash('md5').update(password).digest('hex');
}

// BAD: Insufficient iterations
async function hashPasswordWeak(password) {
  // Cost factor 4 is too weak!
  return await bcrypt.hash(password, 4);
}
```

### Example 3: Secure Random Generation

```javascript
const crypto = require('crypto');

// GOOD: Cryptographically secure random
function generateToken(length = 32) {
  return crypto.randomBytes(length).toString('hex');
}

function generateApiKey() {
  return crypto.randomBytes(32).toString('base64');
}

function generateSecurePin(digits = 6) {
  const max = Math.pow(10, digits);
  return crypto.randomInt(0, max).toString().padStart(digits, '0');
}

// Usage
const sessionToken = generateToken();
const apiKey = generateApiKey();
const pin = generateSecurePin(6);

// BAD: Using Math.random() for security
function generateTokenBad() {
  // NEVER use Math.random() for security!
  return Math.random().toString(36).substring(2);
}
```

### Example 4: TLS Configuration (Node.js HTTPS Server)

```javascript
const https = require('https');
const fs = require('fs');

// GOOD: Secure TLS configuration
const options = {
  key: fs.readFileSync('/path/to/private-key.pem'),
  cert: fs.readFileSync('/path/to/certificate.pem'),
  ca: fs.readFileSync('/path/to/ca-bundle.pem'),
  
  // TLS 1.2 minimum
  minVersion: 'TLSv1.2',
  
  // Prefer TLS 1.3
  maxVersion: 'TLSv1.3',
  
  // Strong cipher suites only
  ciphers: [
    'TLS_AES_256_GCM_SHA384',
    'TLS_AES_128_GCM_SHA256',
    'TLS_CHACHA20_POLY1305_SHA256',
    'ECDHE-RSA-AES256-GCM-SHA384',
    'ECDHE-RSA-AES128-GCM-SHA256',
    'ECDHE-ECDSA-AES256-GCM-SHA384',
    'ECDHE-ECDSA-AES128-GCM-SHA256'
  ].join(':'),
  
  // Prefer server cipher order
  honorCipherOrder: true,
  
  // Enable Perfect Forward Secrecy
  ecdhCurve: 'prime256v1:secp384r1:secp521r1',
  
  // Require client certificate (if needed)
  requestCert: false,
  rejectUnauthorized: true
};

const server = https.createServer(options, (req, res) => {
  // Set security headers
  res.setHeader('Strict-Transport-Security', 'max-age=31536000; includeSubDomains; preload');
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'DENY');
  
  res.writeHead(200);
  res.end('Secure connection');
});

server.listen(443);

// BAD: Weak TLS configuration
const optionsBad = {
  key: fs.readFileSync('/path/to/private-key.pem'),
  cert: fs.readFileSync('/path/to/certificate.pem'),
  
  // NEVER allow TLS 1.0/1.1
  minVersion: 'TLSv1.0', // TOO WEAK!
  
  // Allowing weak ciphers
  ciphers: 'ALL', // INSECURE!
  
  // Not rejecting unauthorized
  rejectUnauthorized: false // DANGEROUS!
};
```

### Example 5: Key Derivation (PBKDF2)

```javascript
const crypto = require('crypto');

// Derive encryption key from password
function deriveKey(password, salt, keyLength = 32) {
  // Use PBKDF2 with SHA-256, 100,000 iterations minimum
  return crypto.pbkdf2Sync(
    password,
    salt,
    100000, // iterations (minimum)
    keyLength,
    'sha256'
  );
}

// Usage
const password = 'UserPassword123!';
const salt = crypto.randomBytes(16); // Store salt with encrypted data
const key = deriveKey(password, salt, 32); // 256-bit key

console.log('Derived key:', key.toString('hex'));

// BAD: Weak key derivation
function deriveKeyWeak(password) {
  // NEVER use simple hashing for key derivation!
  return crypto.createHash('sha256').update(password).digest();
}
```

### Example 6: Secure File Encryption

```javascript
const crypto = require('crypto');
const fs = require('fs').promises;

async function encryptFile(inputPath, outputPath, key) {
  // Read file
  const plaintext = await fs.readFile(inputPath);
  
  // Generate IV
  const iv = crypto.randomBytes(12);
  
  // Encrypt
  const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
  const ciphertext = Buffer.concat([
    cipher.update(plaintext),
    cipher.final()
  ]);
  
  // Get auth tag
  const authTag = cipher.getAuthTag();
  
  // Write IV + authTag + ciphertext
  const encrypted = Buffer.concat([iv, authTag, ciphertext]);
  await fs.writeFile(outputPath, encrypted);
}

async function decryptFile(inputPath, outputPath, key) {
  // Read encrypted file
  const encrypted = await fs.readFile(inputPath);
  
  // Extract IV, auth tag, and ciphertext
  const iv = encrypted.slice(0, 12);
  const authTag = encrypted.slice(12, 28);
  const ciphertext = encrypted.slice(28);
  
  // Decrypt
  const decipher = crypto.createDecipheriv('aes-256-gcm', key, iv);
  decipher.setAuthTag(authTag);
  
  const plaintext = Buffer.concat([
    decipher.update(ciphertext),
    decipher.final()
  ]);
  
  // Write decrypted file
  await fs.writeFile(outputPath, plaintext);
}

// Usage
const key = crypto.randomBytes(32);
await encryptFile('sensitive.pdf', 'sensitive.pdf.enc', key);
await decryptFile('sensitive.pdf.enc', 'sensitive-decrypted.pdf', key);
```

### Example 7: Certificate Validation

```javascript
const https = require('https');
const tls = require('tls');

// GOOD: Verify certificate
function makeSecureRequest(url) {
  return new Promise((resolve, reject) => {
    https.get(url, {
      // Verify certificate chain
      rejectUnauthorized: true,
      
      // Check hostname
      checkServerIdentity: (hostname, cert) => {
        const err = tls.checkServerIdentity(hostname, cert);
        if (err) {
          return err;
        }
        
        // Additional checks
        const now = new Date();
        const notBefore = new Date(cert.valid_from);
        const notAfter = new Date(cert.valid_to);
        
        if (now < notBefore || now > notAfter) {
          return new Error('Certificate not valid for current date');
        }
        
        return undefined;
      }
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve(data));
    }).on('error', reject);
  });
}

// BAD: Skipping certificate verification
function makeInsecureRequest(url) {
  return new Promise((resolve, reject) => {
    https.get(url, {
      // NEVER disable certificate verification!
      rejectUnauthorized: false // DANGEROUS!
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve(data));
    }).on('error', reject);
  });
}
```

## Related ISMS Policies

- **[Cryptographic Controls Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Cryptographic_Controls_Policy.md)** - Primary policy for cryptography
- **[Data Protection Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Data_Protection_Policy.md)** - Encryption requirements
- **[Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md)** - Cryptographic implementation in code

## Related Documentation

- [SECURITY_ARCHITECTURE.md](../../../../SECURITY_ARCHITECTURE.md) - Cryptographic controls in architecture
- [secure-development SKILL.md](../secure-development/SKILL.md) - Secure coding practices
- [data-classification SKILL.md](../data-classification/SKILL.md) - Encryption requirements by classification

## Compliance Mapping

### ISO 27001:2022
- **A.8.24** Use of cryptography

### NIST Cybersecurity Framework
- **PR.DS-1**: Data-at-rest is protected
- **PR.DS-2**: Data-in-transit is protected

### CIS Controls
- **Control 3**: Data Protection
  - 3.10 Encrypt Sensitive Data in Transit
  - 3.11 Encrypt Sensitive Data at Rest

## Key Rotation Schedule

| Key Type | Rotation Frequency | Trigger for Immediate Rotation |
|----------|-------------------|-------------------------------|
| TLS Certificates | Annually | Compromise, algorithm weakness |
| Symmetric Keys (RESTRICTED) | Quarterly | Compromise, employee departure |
| Symmetric Keys (CONFIDENTIAL) | Annually | Compromise |
| API Keys | Annually | Compromise, employee departure |
| SSH Keys | 2 years | Compromise |
| Root CA Keys | 10 years | Compromise |
| Database Encryption Keys | 2 years | Compromise |

## Enforcement

Violations of cryptographic requirements:
- **Critical** (use of banned algorithms, hardcoded keys): Block deployment
- **High** (weak configurations, missing encryption): Require immediate remediation
- **Medium** (suboptimal configurations): Remediate within sprint

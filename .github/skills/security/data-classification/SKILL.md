---
name: data-classification
description: Data classification levels (Public, Internal, Confidential, Restricted) and handling requirements per Hack23 Data Classification Policy
license: Apache-2.0
---

# Data Classification Skill

## Purpose

This skill implements data classification requirements as defined in the [Hack23 ISMS Data Classification Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Data_Classification_Policy.md). It ensures that all data is properly classified and handled according to its sensitivity level.

## Rules

### Classification Levels

Hack23 uses four classification levels:

1. **PUBLIC** - Information intended for public disclosure
2. **INTERNAL** - Information for internal use only
3. **CONFIDENTIAL** - Sensitive information requiring protection
4. **RESTRICTED** - Highly sensitive information requiring maximum protection

### PUBLIC Data

**Definition:** Information that can be freely disclosed to the public without harm to Hack23, customers, or partners.

**Examples:**
- Published website content
- Marketing materials
- Press releases
- Open-source code in public repositories
- Public ISMS policies
- Public API documentation
- Blog posts
- Product brochures

**MUST:**
- Mark as "PUBLIC" in metadata/headers
- Allow unrestricted access
- Can be stored on public cloud services
- Can be transmitted unencrypted (though HTTPS is still recommended)
- Apply standard backup procedures
- Review before publication to ensure no unintended disclosure

**MUST NOT:**
- Include any Internal, Confidential, or Restricted information
- Include information that could aid attackers (detailed security configurations, vulnerability details)

### INTERNAL Data

**Definition:** Information for use within Hack23 that should not be publicly disclosed but is not highly sensitive.

**Examples:**
- Internal documentation
- Meeting notes
- Project plans
- Employee directories
- Internal policies
- Development roadmaps
- Non-confidential customer communications
- Internal training materials

**MUST:**
- Mark as "INTERNAL" in metadata/headers
- Require authentication to access
- Store on approved internal systems or cloud services with access controls
- Transmit over encrypted channels (TLS 1.2+)
- Include in regular backup procedures
- Remove access when employees leave
- Apply retention policies

**MUST NOT:**
- Share with external parties without approval
- Store on personal devices without encryption
- Transmit over unencrypted channels
- Post on public websites or forums

### CONFIDENTIAL Data

**Definition:** Sensitive information that could cause significant harm if disclosed.

**Examples:**
- Customer personal data (PII)
- Financial records
- Contracts and agreements
- Strategic plans
- Security assessment reports
- Non-public vulnerability information
- Source code for proprietary systems
- Audit reports
- Legal documents
- HR records (non-sensitive)

**MUST:**
- Mark as "CONFIDENTIAL" in metadata/headers
- Require strong authentication (MFA recommended)
- Implement role-based access control
- Encrypt at rest (AES-256)
- Encrypt in transit (TLS 1.2+)
- Log all access
- Store only on approved systems with encryption
- Apply strict retention and disposal policies
- Require NDA before sharing with external parties
- Conduct access reviews quarterly
- Remove access immediately when no longer needed

**MUST NOT:**
- Share via unsecured channels (email without encryption, chat without E2E encryption)
- Store on personal devices without full disk encryption and MDM
- Include in logs or error messages
- Share on public cloud services without encryption
- Copy to removable media without encryption and approval

### RESTRICTED Data

**Definition:** Highly sensitive information that could cause severe harm if disclosed.

**Examples:**
- Passwords, encryption keys, API secrets
- Authentication credentials
- Personal health information (PHI)
- Financial account credentials
- Credit card data (PAN, CVV)
- National ID numbers (SSN, passport numbers)
- Biometric data
- Cryptographic private keys
- Security vulnerability details (before patching)

**MUST:**
- Mark as "RESTRICTED" in metadata/headers
- Require MFA for all access
- Implement strict role-based access control with separation of duties
- Encrypt at rest with AES-256
- Encrypt in transit with TLS 1.2+
- Log and monitor all access with alerts
- Store in dedicated secure systems (key management systems for secrets)
- Apply immediate retention (delete when no longer needed)
- Require explicit approval for each access
- Conduct access reviews monthly
- Use secret management systems (never hardcode)
- Implement automated rotation where possible
- Revoke access immediately when no longer needed

**MUST NOT:**
- Store in plaintext
- Include in source code, configuration files, or version control
- Include in logs, error messages, or debug output
- Transmit via email, chat, or unsecured channels
- Store on personal devices
- Copy to removable media
- Share screenshots or copies
- Display on screen in public areas
- Print unless absolutely necessary (and securely destroy after use)

### Data Handling Matrix

| Requirement | PUBLIC | INTERNAL | CONFIDENTIAL | RESTRICTED |
|------------|--------|----------|--------------|------------|
| Authentication | Not required | Required | Required | MFA required |
| Access Control | Open | RBAC | Strict RBAC | Strict RBAC + approval |
| Encryption at Rest | Optional | Recommended | Required (AES-256) | Required (AES-256) |
| Encryption in Transit | Recommended | Required (TLS 1.2+) | Required (TLS 1.2+) | Required (TLS 1.2+) |
| Access Logging | Optional | Recommended | Required | Required + monitoring |
| Access Review | N/A | Annually | Quarterly | Monthly |
| Backup | Standard | Standard | Encrypted backup | Encrypted backup |
| Retention | As needed | Per policy | Strict policy | Immediate deletion |
| External Sharing | Allowed | With approval | NDA required | Prohibited |

### Classification Guidelines

**MUST:**
- Classify all data at creation
- Apply the highest classification if multiple types are present
- Document classification decisions
- Review classification periodically (annually minimum)
- Train employees on classification
- Mark documents/files with classification labels
- Handle data according to its classification throughout its lifecycle

**MUST NOT:**
- Downgrade classification without approval
- Mix classifications in single document/database
- Ignore classification in automated systems

### Storage Requirements

**PUBLIC:**
- Any approved storage

**INTERNAL:**
- Approved internal file shares
- Cloud storage with authentication
- Internal databases

**CONFIDENTIAL:**
- Encrypted cloud storage (approved providers)
- Encrypted databases
- Encrypted file systems
- Encrypted backups

**RESTRICTED:**
- Dedicated secure storage systems
- Key management systems (for secrets)
- HSM (for cryptographic keys)
- Encrypted backups in secure locations

### Transmission Requirements

**PUBLIC:**
- Any method (HTTPS recommended)

**INTERNAL:**
- TLS 1.2+ for network transmission
- Authenticated email
- VPN for remote access

**CONFIDENTIAL:**
- TLS 1.2+ mandatory
- Encrypted email (S/MIME or PGP)
- Secure file transfer (SFTP, HTTPS)
- VPN for remote access

**RESTRICTED:**
- TLS 1.2+ mandatory
- End-to-end encrypted channels
- Out-of-band key exchange
- Never via standard email

### Disposal Requirements

**PUBLIC:**
- Standard deletion

**INTERNAL:**
- Secure deletion (overwrite)
- Shred physical documents

**CONFIDENTIAL:**
- Secure deletion with verification
- Multiple overwrites
- Cross-cut shred physical documents
- Degauss magnetic media

**RESTRICTED:**
- Cryptographic erasure
- Physical destruction of media
- Certificate of destruction
- Immediate deletion from all locations

## Examples

### Example 1: Data Classification Headers (HTML)

```html
<!-- PUBLIC data -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta name="classification" content="PUBLIC">
  <title>Hack23 - Cybersecurity Consulting</title>
</head>

<!-- INTERNAL data -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta name="classification" content="INTERNAL">
  <meta name="robots" content="noindex, nofollow">
  <title>Internal Project Documentation</title>
</head>
```

### Example 2: Database Field Classification

```javascript
// Define classification metadata
const userSchema = new mongoose.Schema({
  // PUBLIC
  username: {
    type: String,
    classification: 'PUBLIC',
    required: true
  },
  
  // INTERNAL
  email: {
    type: String,
    classification: 'INTERNAL',
    required: true
  },
  
  // CONFIDENTIAL
  firstName: {
    type: String,
    classification: 'CONFIDENTIAL',
    required: true
  },
  lastName: {
    type: String,
    classification: 'CONFIDENTIAL',
    required: true
  },
  dateOfBirth: {
    type: Date,
    classification: 'CONFIDENTIAL'
  },
  
  // RESTRICTED
  passwordHash: {
    type: String,
    classification: 'RESTRICTED',
    required: true,
    select: false // Never return in queries by default
  },
  ssn: {
    type: String,
    classification: 'RESTRICTED',
    select: false,
    // Encrypt at application level before storage
    get: (value) => decrypt(value),
    set: (value) => encrypt(value)
  }
});
```

### Example 3: Logging with Classification

```javascript
const winston = require('winston');

// Create logger with classification filter
const logger = winston.createLogger({
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  transports: [
    new winston.transports.File({ filename: 'application.log' })
  ]
});

// Safe logging helper
function logSafely(level, message, metadata = {}) {
  // Filter out sensitive data
  const safeMetadata = {};
  
  for (const [key, value] of Object.entries(metadata)) {
    const classification = value?.classification || 'INTERNAL';
    
    // NEVER log RESTRICTED data
    if (classification === 'RESTRICTED') {
      safeMetadata[key] = '[RESTRICTED - REDACTED]';
    }
    // Mask CONFIDENTIAL data
    else if (classification === 'CONFIDENTIAL') {
      safeMetadata[key] = maskConfidential(value);
    }
    // INTERNAL and PUBLIC can be logged
    else {
      safeMetadata[key] = value;
    }
  }
  
  logger.log(level, message, safeMetadata);
}

function maskConfidential(value) {
  if (typeof value === 'string' && value.length > 4) {
    return value.substring(0, 2) + '***' + value.substring(value.length - 2);
  }
  return '***';
}

// Usage
logSafely('info', 'User login', {
  username: { value: 'john_doe', classification: 'PUBLIC' },
  email: { value: 'john@example.com', classification: 'INTERNAL' },
  ipAddress: { value: '192.168.1.1', classification: 'INTERNAL' },
  password: { value: 'secretpassword', classification: 'RESTRICTED' } // Will be redacted
});

// Output: { username: 'john_doe', email: 'john@example.com', ipAddress: '192.168.1.1', password: '[RESTRICTED - REDACTED]' }
```

### Example 4: API Response Classification

```javascript
// Filter API responses based on user permissions and classification
function filterResponseByClassification(data, userRole) {
  // Define role clearance levels
  const clearanceLevels = {
    'public': ['PUBLIC'],
    'user': ['PUBLIC', 'INTERNAL'],
    'admin': ['PUBLIC', 'INTERNAL', 'CONFIDENTIAL']
    // RESTRICTED data is never included in API responses
  };
  
  const allowedClassifications = clearanceLevels[userRole] || ['PUBLIC'];
  
  const filtered = {};
  for (const [key, value] of Object.entries(data)) {
    const classification = value?.classification || 'INTERNAL';
    
    if (classification === 'RESTRICTED') {
      // Never include RESTRICTED data in API responses
      continue;
    }
    
    if (allowedClassifications.includes(classification)) {
      filtered[key] = value.data || value;
    }
  }
  
  return filtered;
}

// Usage
app.get('/api/user/:id', requireAuth, async (req, res) => {
  const user = await db.users.findById(req.params.id);
  
  const userData = {
    username: { data: user.username, classification: 'PUBLIC' },
    email: { data: user.email, classification: 'INTERNAL' },
    firstName: { data: user.firstName, classification: 'CONFIDENTIAL' },
    lastName: { data: user.lastName, classification: 'CONFIDENTIAL' },
    ssn: { data: user.ssn, classification: 'RESTRICTED' } // Will never be included
  };
  
  const filtered = filterResponseByClassification(userData, req.user.role);
  res.json(filtered);
});
```

### Example 5: File Classification Metadata

```javascript
const fs = require('fs');
const xattr = require('fs-xattr');

// Set classification on file using extended attributes
async function setFileClassification(filePath, classification) {
  const validClassifications = ['PUBLIC', 'INTERNAL', 'CONFIDENTIAL', 'RESTRICTED'];
  
  if (!validClassifications.includes(classification)) {
    throw new Error(`Invalid classification: ${classification}`);
  }
  
  // Set extended attribute
  await xattr.set(filePath, 'user.classification', classification);
  
  // Set appropriate file permissions
  const permissions = {
    'PUBLIC': 0o644,      // rw-r--r--
    'INTERNAL': 0o640,    // rw-r-----
    'CONFIDENTIAL': 0o600, // rw-------
    'RESTRICTED': 0o600   // rw-------
  };
  
  await fs.promises.chmod(filePath, permissions[classification]);
}

// Get file classification
async function getFileClassification(filePath) {
  try {
    return await xattr.get(filePath, 'user.classification');
  } catch (err) {
    return 'INTERNAL'; // Default classification
  }
}

// Verify file handling based on classification
async function verifyFileHandling(filePath) {
  const classification = await getFileClassification(filePath);
  
  switch (classification) {
    case 'RESTRICTED':
    case 'CONFIDENTIAL':
      // Verify encryption
      const encrypted = await isFileEncrypted(filePath);
      if (!encrypted) {
        throw new Error(`${classification} file must be encrypted: ${filePath}`);
      }
      break;
      
    case 'INTERNAL':
      // Verify access controls
      const stats = await fs.promises.stat(filePath);
      if (stats.mode & 0o004) { // World readable
        throw new Error(`INTERNAL file must not be world-readable: ${filePath}`);
      }
      break;
  }
}
```

### Example 6: Secure Deletion by Classification

```javascript
const crypto = require('crypto');
const fs = require('fs').promises;

async function secureDelete(filePath, classification) {
  const stats = await fs.stat(filePath);
  const fileSize = stats.size;
  
  switch (classification) {
    case 'PUBLIC':
    case 'INTERNAL':
      // Simple deletion
      await fs.unlink(filePath);
      break;
      
    case 'CONFIDENTIAL':
      // Overwrite with random data 3 times
      for (let i = 0; i < 3; i++) {
        const randomData = crypto.randomBytes(fileSize);
        await fs.writeFile(filePath, randomData);
      }
      // Then delete
      await fs.unlink(filePath);
      break;
      
    case 'RESTRICTED':
      // Overwrite with random data 7 times (DoD 5220.22-M standard)
      for (let i = 0; i < 7; i++) {
        const randomData = crypto.randomBytes(fileSize);
        await fs.writeFile(filePath, randomData);
        // Sync to ensure write to disk
        const fd = await fs.open(filePath, 'r+');
        await fd.sync();
        await fd.close();
      }
      // Final overwrite with zeros
      await fs.writeFile(filePath, Buffer.alloc(fileSize, 0));
      // Then delete
      await fs.unlink(filePath);
      break;
  }
  
  // Log secure deletion
  logger.info('Secure deletion completed', {
    file: filePath,
    classification: classification,
    timestamp: new Date().toISOString()
  });
}
```

## Related ISMS Policies

- **[Data Classification Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Data_Classification_Policy.md)** - Primary policy for data classification
- **[Privacy Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Privacy_Policy.md)** - Data protection and privacy requirements
- **[Cryptographic Controls Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Cryptographic_Controls_Policy.md)** - Encryption requirements
- **[Access Control Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Access_Control_Policy.md)** - Access control by classification

## Related Documentation

- [CLASSIFICATION.md](../../../../CLASSIFICATION.md) - Data classification guidance
- [secure-development SKILL.md](../secure-development/SKILL.md) - Secure coding for classified data
- [cryptography SKILL.md](../cryptography/SKILL.md) - Encryption for classified data

## Compliance Mapping

### ISO 27001:2022
- **A.5.12** Classification of information
- **A.5.13** Labelling of information
- **A.5.14** Information transfer
- **A.8.10** Information deletion

### GDPR
- **Article 32** - Security of processing (based on sensitivity)
- **Article 17** - Right to erasure

### NIST Cybersecurity Framework
- **PR.DS-5**: Protections against data leaks are implemented
- **PR.IP-2**: A System Development Life Cycle manages systems based on data sensitivity

## Enforcement

All data MUST be classified. Violations:
- **Unclassified data**: Default to INTERNAL until properly classified
- **Misclassification**: Review and correct immediately
- **Improper handling**: Incident response, remediation required
- **Unauthorized disclosure**: Security incident, potential breach notification

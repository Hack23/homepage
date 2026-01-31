---
name: access-control
description: Least privilege principle, RBAC, authentication, authorization, and session management following Hack23 Access Control Policy
license: Apache-2.0
---

# Access Control Skill

## Purpose

This skill enforces access control requirements as defined in the [Hack23 ISMS Access Control Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Access_Control_Policy.md). It ensures that all systems implement proper authentication, authorization, and session management based on the principle of least privilege.

## Rules

### Principle of Least Privilege

**MUST:**
- Grant minimum permissions necessary to perform job functions
- Default to deny access (allowlist approach)
- Separate duties for critical functions (no single person has complete control)
- Regularly review and revoke unnecessary permissions
- Document permission requirements for each role
- Implement time-limited access for temporary needs

**MUST NOT:**
- Grant administrative privileges by default
- Share user accounts between multiple people
- Use shared service accounts without audit trails
- Grant permanent access when temporary access is sufficient
- Allow users to escalate their own privileges

### Role-Based Access Control (RBAC)

**MUST:**
- Define roles based on job functions
- Assign permissions to roles, not individual users
- Document role definitions and their permissions
- Implement role hierarchy where appropriate
- Enforce separation of duties through role conflicts
- Review role assignments quarterly

**Roles for Hack23 Projects:**
- **Public**: Unauthenticated users (read-only access to public content)
- **User**: Authenticated regular users (basic functionality)
- **Contributor**: Code contributors (read/write to repositories)
- **Maintainer**: Project maintainers (merge, release, moderate)
- **Administrator**: System administrators (full control, user management)
- **Security Officer**: Security team (audit logs, security settings)

**MUST NOT:**
- Create user-specific permissions (use roles instead)
- Assign multiple conflicting roles to same user
- Allow role self-assignment without approval
- Create overly broad roles that violate least privilege

### Authentication Requirements

**MUST:**
- Require authentication for all non-public resources
- Implement multi-factor authentication (MFA) for:
  - Administrative accounts
  - Access to Confidential or Restricted data
  - Remote access to internal systems
  - Privileged operations (deployments, configuration changes)
- Enforce strong password requirements:
  - Minimum 12 characters
  - At least one uppercase, lowercase, number, symbol
  - No common passwords (check against known breached passwords)
  - No reuse of last 5 passwords
- Implement account lockout after 5 failed attempts
- Require password change every 90 days for privileged accounts
- Terminate sessions after 30 minutes of inactivity
- Support passwordless authentication (FIDO2/WebAuthn) where possible

**MUST NOT:**
- Use basic authentication over unencrypted connections
- Store passwords in plaintext or reversible encryption
- Allow anonymous access to sensitive resources
- Use weak hashing algorithms (MD5, SHA-1) for passwords
- Implement custom authentication without security review
- Bypass authentication for "trusted" networks

### Authorization Requirements

**MUST:**
- Verify authorization at every access point
- Check permissions server-side (never rely on client-side checks)
- Validate user permissions for each resource accessed
- Implement attribute-based access control (ABAC) for complex policies
- Deny access by default (fail closed)
- Log all authorization failures
- Enforce authorization consistently across all interfaces (web, API, CLI)

**MUST NOT:**
- Assume authentication implies authorization
- Use client-side authorization checks as primary control
- Grant access based solely on URL/endpoint knowledge
- Skip authorization checks for internal APIs
- Use security through obscurity (hidden URLs don't require authentication)

### Session Management

**MUST:**
- Generate cryptographically random session IDs (minimum 128 bits entropy)
- Set HTTPOnly flag on session cookies (prevent JavaScript access)
- Set Secure flag on session cookies (HTTPS only)
- Set SameSite=Strict or Lax on session cookies (CSRF protection)
- Implement session timeout (30 minutes inactivity, 8 hours absolute)
- Regenerate session ID after authentication
- Invalidate sessions on logout
- Store session data securely (encrypted, integrity-protected)
- Implement concurrent session limits
- Provide users visibility into active sessions

**MUST NOT:**
- Include session IDs in URLs
- Use predictable session IDs
- Transmit session cookies over unencrypted connections
- Store sensitive data in client-side storage (localStorage, sessionStorage)
- Allow session fixation attacks
- Share sessions across different security contexts

### API Authentication

**MUST:**
- Require authentication for all non-public API endpoints
- Use OAuth 2.0 or OpenID Connect for third-party integrations
- Implement API key rotation (at least annually)
- Rate limit API requests to prevent abuse
- Validate API tokens on every request
- Use short-lived access tokens (< 1 hour) with refresh tokens
- Scope API tokens to minimum necessary permissions

**MUST NOT:**
- Include API keys in URLs or logs
- Use long-lived API keys without rotation
- Share API keys across multiple applications
- Transmit API keys over unencrypted connections
- Store API keys in client-side code

### Access Reviews

**MUST:**
- Review user access rights quarterly
- Remove access for terminated employees immediately
- Review privileged access monthly
- Document access review results
- Revoke unused accounts after 90 days of inactivity
- Audit access control changes

**MUST NOT:**
- Skip access reviews for "trusted" users
- Allow indefinite access without review
- Ignore orphaned accounts
- Delay access revocation for terminated users

## Examples

### Example 1: RBAC Implementation (Node.js/Express)

```javascript
// Define roles and permissions
const ROLES = {
  PUBLIC: 'public',
  USER: 'user',
  CONTRIBUTOR: 'contributor',
  MAINTAINER: 'maintainer',
  ADMIN: 'administrator'
};

const PERMISSIONS = {
  READ_PUBLIC: 'read:public',
  READ_PRIVATE: 'read:private',
  WRITE_CODE: 'write:code',
  MERGE_PR: 'merge:pr',
  MANAGE_USERS: 'manage:users',
  MANAGE_SECURITY: 'manage:security'
};

// Role to permissions mapping
const rolePermissions = {
  [ROLES.PUBLIC]: [PERMISSIONS.READ_PUBLIC],
  [ROLES.USER]: [PERMISSIONS.READ_PUBLIC, PERMISSIONS.READ_PRIVATE],
  [ROLES.CONTRIBUTOR]: [PERMISSIONS.READ_PUBLIC, PERMISSIONS.READ_PRIVATE, PERMISSIONS.WRITE_CODE],
  [ROLES.MAINTAINER]: [PERMISSIONS.READ_PUBLIC, PERMISSIONS.READ_PRIVATE, PERMISSIONS.WRITE_CODE, PERMISSIONS.MERGE_PR],
  [ROLES.ADMIN]: Object.values(PERMISSIONS) // All permissions
};

// Middleware to check permission
function requirePermission(permission) {
  return (req, res, next) => {
    // Must be authenticated
    if (!req.user) {
      return res.status(401).json({ error: 'Authentication required' });
    }
    
    // Get user's permissions from their role
    const userPermissions = rolePermissions[req.user.role] || [];
    
    // Check if user has required permission
    if (!userPermissions.includes(permission)) {
      return res.status(403).json({ error: 'Insufficient permissions' });
    }
    
    next();
  };
}

// Usage in routes
app.get('/api/public/data', requirePermission(PERMISSIONS.READ_PUBLIC), (req, res) => {
  // Public data endpoint
});

app.post('/api/code/commit', requirePermission(PERMISSIONS.WRITE_CODE), (req, res) => {
  // Commit code endpoint
});

app.post('/api/pr/merge', requirePermission(PERMISSIONS.MERGE_PR), (req, res) => {
  // Merge PR endpoint
});
```

### Example 2: Secure Session Management (Express)

```javascript
const session = require('express-session');
const RedisStore = require('connect-redis')(session);
const redis = require('redis');

const redisClient = redis.createClient({
  host: process.env.REDIS_HOST,
  port: process.env.REDIS_PORT,
  password: process.env.REDIS_PASSWORD
});

// GOOD: Secure session configuration
app.use(session({
  store: new RedisStore({ 
    client: redisClient,
    prefix: 'sess:' 
  }),
  secret: process.env.SESSION_SECRET, // Strong random secret from env
  name: 'sid', // Don't use default name
  resave: false,
  saveUninitialized: false,
  rolling: true, // Reset expiry on activity
  cookie: {
    secure: true,        // HTTPS only
    httpOnly: true,      // No JavaScript access
    maxAge: 1800000,     // 30 minutes
    sameSite: 'strict',  // CSRF protection
    domain: 'hack23.com' // Explicit domain
  }
}));

// Session timeout middleware
app.use((req, res, next) => {
  if (req.session) {
    const now = Date.now();
    const lastActivity = req.session.lastActivity || now;
    const inactivityTimeout = 30 * 60 * 1000; // 30 minutes
    
    if (now - lastActivity > inactivityTimeout) {
      req.session.destroy();
      return res.status(401).json({ error: 'Session expired due to inactivity' });
    }
    
    req.session.lastActivity = now;
  }
  next();
});

// Regenerate session ID after authentication
app.post('/login', async (req, res) => {
  const { username, password } = req.body;
  
  const user = await authenticateUser(username, password);
  if (!user) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }
  
  // Regenerate session to prevent fixation
  req.session.regenerate((err) => {
    if (err) {
      return res.status(500).json({ error: 'Session error' });
    }
    
    req.session.userId = user.id;
    req.session.role = user.role;
    req.session.lastActivity = Date.now();
    
    res.json({ success: true, user: { id: user.id, role: user.role } });
  });
});

// Logout
app.post('/logout', (req, res) => {
  req.session.destroy((err) => {
    if (err) {
      return res.status(500).json({ error: 'Logout failed' });
    }
    res.clearCookie('sid');
    res.json({ success: true });
  });
});
```

### Example 3: MFA Implementation (TOTP)

```javascript
const speakeasy = require('speakeasy');
const QRCode = require('qrcode');

// Enable MFA for user
app.post('/api/user/mfa/enable', requireAuth, async (req, res) => {
  const user = req.user;
  
  // Generate secret
  const secret = speakeasy.generateSecret({
    name: `Hack23 (${user.email})`,
    issuer: 'Hack23'
  });
  
  // Generate QR code
  const qrCodeUrl = await QRCode.toDataURL(secret.otpauth_url);
  
  // Store secret (encrypted) in database
  await db.users.update(user.id, {
    mfa_secret: encrypt(secret.base32),
    mfa_enabled: false // Not enabled until verified
  });
  
  res.json({
    secret: secret.base32,
    qrCode: qrCodeUrl
  });
});

// Verify and activate MFA
app.post('/api/user/mfa/verify', requireAuth, async (req, res) => {
  const { token } = req.body;
  const user = req.user;
  
  const userData = await db.users.findById(user.id);
  const secret = decrypt(userData.mfa_secret);
  
  // Verify token
  const verified = speakeasy.totp.verify({
    secret: secret,
    encoding: 'base32',
    token: token,
    window: 1 // Allow 1 step before/after for clock skew
  });
  
  if (!verified) {
    return res.status(400).json({ error: 'Invalid verification code' });
  }
  
  // Enable MFA
  await db.users.update(user.id, {
    mfa_enabled: true
  });
  
  res.json({ success: true });
});

// Login with MFA
app.post('/api/login', async (req, res) => {
  const { username, password, mfa_token } = req.body;
  
  // Verify username/password
  const user = await authenticateUser(username, password);
  if (!user) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }
  
  // Check if MFA is enabled
  if (user.mfa_enabled) {
    if (!mfa_token) {
      return res.status(401).json({ 
        error: 'MFA token required',
        mfa_required: true 
      });
    }
    
    // Verify MFA token
    const secret = decrypt(user.mfa_secret);
    const verified = speakeasy.totp.verify({
      secret: secret,
      encoding: 'base32',
      token: mfa_token,
      window: 1
    });
    
    if (!verified) {
      return res.status(401).json({ error: 'Invalid MFA token' });
    }
  }
  
  // Create session
  req.session.regenerate((err) => {
    if (err) {
      return res.status(500).json({ error: 'Session error' });
    }
    
    req.session.userId = user.id;
    req.session.role = user.role;
    
    res.json({ success: true, user: { id: user.id, role: user.role } });
  });
});
```

### Example 4: API Key Management

```javascript
const crypto = require('crypto');

// Generate API key
function generateApiKey() {
  // Generate 32 bytes (256 bits) of random data
  const key = crypto.randomBytes(32).toString('base64');
  return key;
}

// Hash API key for storage
function hashApiKey(apiKey) {
  return crypto.createHash('sha256').update(apiKey).digest('hex');
}

// Create API key with scopes
app.post('/api/keys', requireAuth, async (req, res) => {
  const { name, scopes, expiresInDays } = req.body;
  
  // Generate key
  const apiKey = generateApiKey();
  const hashedKey = hashApiKey(apiKey);
  
  // Calculate expiry
  const expiresAt = new Date();
  expiresAt.setDate(expiresAt.getDate() + (expiresInDays || 365));
  
  // Store hashed key
  await db.apiKeys.create({
    user_id: req.user.id,
    name: name,
    key_hash: hashedKey,
    scopes: scopes,
    expires_at: expiresAt,
    created_at: new Date()
  });
  
  // Return plaintext key ONCE (user must save it)
  res.json({
    apiKey: apiKey,
    name: name,
    scopes: scopes,
    expiresAt: expiresAt,
    warning: 'Save this key now. It will not be shown again.'
  });
});

// Validate API key middleware
async function validateApiKey(req, res, next) {
  const authHeader = req.headers.authorization;
  
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'API key required' });
  }
  
  const apiKey = authHeader.substring(7);
  const hashedKey = hashApiKey(apiKey);
  
  // Lookup key
  const keyRecord = await db.apiKeys.findByHash(hashedKey);
  
  if (!keyRecord) {
    return res.status(401).json({ error: 'Invalid API key' });
  }
  
  // Check expiry
  if (new Date() > keyRecord.expires_at) {
    return res.status(401).json({ error: 'API key expired' });
  }
  
  // Check if key is active
  if (!keyRecord.active) {
    return res.status(401).json({ error: 'API key revoked' });
  }
  
  // Update last used
  await db.apiKeys.updateLastUsed(keyRecord.id);
  
  // Attach user and scopes to request
  req.apiKey = keyRecord;
  req.user = await db.users.findById(keyRecord.user_id);
  
  next();
}

// Usage
app.get('/api/data', validateApiKey, requireScope('read:data'), (req, res) => {
  // API endpoint
});
```

## Related ISMS Policies

- **[Access Control Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Access_Control_Policy.md)** - Primary policy for access control
- **[Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)** - Overall security framework
- **[Acceptable Use Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Acceptable_Use_Policy.md)** - User responsibilities

## Related Documentation

- [SECURITY_ARCHITECTURE.md](../../../../SECURITY_ARCHITECTURE.md) - Security controls implementation
- [secure-development SKILL.md](../secure-development/SKILL.md) - Related secure coding practices

## Compliance Mapping

### ISO 27001:2022
- **A.5.15** Access control
- **A.5.16** Identity management
- **A.5.17** Authentication information
- **A.5.18** Access rights

### NIST Cybersecurity Framework
- **PR.AC-1**: Identities and credentials are issued, managed, verified, revoked
- **PR.AC-4**: Access permissions and authorizations are managed
- **PR.AC-6**: Identities are proofed and bound to credentials
- **PR.AC-7**: Users, devices, and assets are authenticated

### CIS Controls
- **Control 5**: Account Management
- **Control 6**: Access Control Management

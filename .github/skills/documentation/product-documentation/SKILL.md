---
name: product-documentation
description: Product documentation standards covering user guides, feature documentation, release notes, and end-user communication
license: Apache-2.0
---

# Product Documentation Skill

## Purpose

Ensures product documentation is clear, comprehensive, and user-focused, helping users understand features, solve problems, and get maximum value from products.

## Rules

### Documentation Types

**User Guides (MUST HAVE):**
- Getting Started guide
- Feature documentation
- Troubleshooting guide
- FAQ
- Glossary

**Release Documentation:**
- Release notes (new features, bug fixes, breaking changes)
- Migration guides
- Upgrade instructions
- Deprecation notices

**Reference Documentation:**
- Feature specifications
- Configuration options
- Keyboard shortcuts / CLI commands
- System requirements

### Writing Standards

**MUST:**
- Use clear, concise language
- Write for the target audience (technical level)
- Use active voice ("Click Save" not "Save should be clicked")
- Include visuals (screenshots, diagrams, videos)
- Provide examples
- Keep up-to-date with product

**Structure:**
```markdown
# Feature Name

## Overview
[What it does and why it's useful]

## Prerequisites
[What users need before starting]

## How to Use
### Step 1: [Action]
[Detailed instructions with screenshots]

### Step 2: [Action]
[More instructions]

## Examples
[Real-world use cases]

## Troubleshooting
[Common problems and solutions]

## Related
[Links to related documentation]
```

## Examples

### Feature Documentation Template
```markdown
# Email Notifications

## Overview
Receive automatic email alerts when important events occur in your account.

## Setting Up Notifications

1. Go to **Settings** → **Notifications**
2. Toggle the events you want to be notified about
3. Verify your email address
4. Click **Save Preferences**

## Available Notification Types

- **Security Alerts**: Login attempts, password changes
- **System Updates**: Maintenance windows, feature releases
- **Account Activity**: Billing changes, user additions

## Troubleshooting

**Problem**: Not receiving notifications  
**Solution**: Check spam folder, verify email address

## Related
- [Email Configuration](./email-config.md)
- [Security Settings](./security.md)
```

## Related Policies

- [Documentation Portfolio SKILL](../../architecture/documentation-portfolio/SKILL.md)
- [Brand Voice & Tone SKILL](../../business/brand-voice-tone/SKILL.md)

## Related Documentation

- [hagbard-celine Agent](../../../agents/hagbard-celine.md)

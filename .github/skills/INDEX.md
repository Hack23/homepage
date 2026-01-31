# Hack23 Skills Library - Index

This index catalogs all available skills in the Hack23 ecosystem for GitHub Copilot to reference when generating code, documentation, or configurations.

## Purpose

Skills are reusable knowledge units that encode Hack23's security policies, architecture patterns, quality standards, and compliance requirements. Each skill provides explicit, actionable rules that GitHub Copilot can apply during development.

## Skills Catalog

### Security Skills

Based on [Hack23 ISMS-PUBLIC](https://github.com/Hack23/ISMS-PUBLIC) policies:

- **[Secure Development](security/secure-development/SKILL.md)** - Security-by-design principles, input validation, secure authentication, cryptographic best practices
- **[Access Control](security/access-control/SKILL.md)** - Least privilege, RBAC, authentication, authorization, session management
- **[Data Classification](security/data-classification/SKILL.md)** - Classification levels (Public, Internal, Confidential, Restricted), handling requirements
- **[Cryptography](security/cryptography/SKILL.md)** - Approved algorithms, TLS enforcement, key management, certificate handling

### Architecture Skills

Based on C4 model and Hack23 documentation standards:

- **[C4 Modeling](architecture/c4-modeling/SKILL.md)** - Context, Container, Component, Code diagrams with Mermaid syntax
- **[Security Architecture](architecture/security-architecture/SKILL.md)** - Security controls documentation, threat model integration, defense-in-depth
- **[Documentation Portfolio](architecture/documentation-portfolio/SKILL.md)** - Required architecture documents and documentation standards

### Quality Skills

Based on web standards and accessibility requirements:

- **[HTML/CSS Best Practices](quality/html-css-best-practices/SKILL.md)** - Semantic HTML5, CSS custom properties, responsive design, performance
- **[Accessibility WCAG](quality/accessibility-wcag/SKILL.md)** - WCAG 2.1 AA compliance, semantic markup, keyboard navigation, ARIA
- **[SEO Optimization](quality/seo-optimization/SKILL.md)** - Meta tags, structured data (Schema.org), semantic HTML, multilingual SEO

### Deployment Skills

Based on AWS and CI/CD best practices:

- **[AWS S3/CloudFront](deployment/aws-s3-cloudfront/SKILL.md)** - S3 configuration, CloudFront setup, security headers, SSL/TLS
- **[GitHub Actions CI/CD](deployment/github-actions-cicd/SKILL.md)** - Workflow structure, security scanning, Lighthouse audits, deployment automation

### Compliance Skills

Based on ISO 27001, GDPR, and regulatory requirements:

- **[ISO 27001](compliance/iso-27001/SKILL.md)** - ISO 27001:2022 requirements, control implementation, documentation, audit preparation
- **[GDPR Compliance](compliance/gdpr/SKILL.md)** - Privacy by design, data protection, consent management, breach response

## How to Use Skills

### For GitHub Copilot

Skills are automatically loaded when working in the Hack23 repositories. Copilot will reference these skills to:
- Generate secure code following ISMS policies
- Create compliant architecture documentation
- Implement accessible and performant web interfaces
- Configure secure deployment pipelines
- Ensure regulatory compliance

### For Developers

1. **Reference skills** before starting new work to understand requirements
2. **Cite specific skills** in PR descriptions to show compliance
3. **Update skills** when policies or standards change
4. **Propose new skills** for emerging technologies or practices

## Skill Structure

Each skill follows this structure:

```yaml
---
name: skill-name
description: When and why to use this skill
license: Apache-2.0
---

# Skill Name

## Purpose
Why this skill exists and when to apply it

## Rules
Explicit, concrete rules (MUST/MUST NOT)

## Examples
Code, configuration, or documentation examples

## Related Policies
Links to ISMS policies

## Related Documentation
Links to project documentation
```

## Maintenance

Skills are maintained by:
- **Security Skills**: Security team, updated when ISMS policies change
- **Architecture Skills**: Architecture team, updated when patterns evolve
- **Quality Skills**: Quality team, updated when standards change
- **Deployment Skills**: DevOps team, updated when infrastructure changes
- **Compliance Skills**: Compliance team, updated when regulations change

## Version History

- **2025-01-24**: Initial skills library creation
  - 11 skills covering security, architecture, quality, deployment, and compliance
  - Based on ISMS-PUBLIC policies and Hack23 standards

## License

All skills are licensed under Apache-2.0, consistent with Hack23's open-source commitment.

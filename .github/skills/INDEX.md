# Hack23 Skills Library - Index

This index catalogs all available skills in the Hack23 ecosystem for GitHub Copilot to reference when generating code, documentation, or configurations.

## Purpose

Skills are reusable knowledge units that encode Hack23's security policies, architecture patterns, quality standards, and compliance requirements. Each skill provides explicit, actionable rules that GitHub Copilot can apply during development.

## Skills Catalog

### Security Skills (4 skills)

Based on [Hack23 ISMS-PUBLIC](https://github.com/Hack23/ISMS-PUBLIC) policies:

- **[Secure Development](security/secure-development/SKILL.md)** - Security-by-design principles, input validation, secure authentication, cryptographic best practices
- **[Access Control](security/access-control/SKILL.md)** - Least privilege, RBAC, authentication, authorization, session management
- **[Data Classification](security/data-classification/SKILL.md)** - Classification levels (Public, Internal, Confidential, Restricted), handling requirements
- **[Cryptography](security/cryptography/SKILL.md)** - Approved algorithms, TLS enforcement, key management, certificate handling

### Architecture Skills (3 skills)

Based on C4 model and Hack23 documentation standards:

- **[C4 Modeling](architecture/c4-modeling/SKILL.md)** - Context, Container, Component, Code diagrams with Mermaid syntax
- **[Security Architecture](architecture/security-architecture/SKILL.md)** - Security controls documentation, threat model integration, defense-in-depth
- **[Documentation Portfolio](architecture/documentation-portfolio/SKILL.md)** - Required architecture documents and documentation standards

### Quality Skills (3 skills)

Based on web standards and accessibility requirements:

- **[HTML/CSS Best Practices](quality/html-css-best-practices/SKILL.md)** - Semantic HTML5, CSS custom properties, responsive design, performance
- **[Accessibility WCAG](quality/accessibility-wcag/SKILL.md)** - WCAG 2.1 AA compliance, semantic markup, keyboard navigation, ARIA
- **[SEO Optimization](quality/seo-optimization/SKILL.md)** - Meta tags, structured data (Schema.org), semantic HTML, multilingual SEO

### Deployment Skills (2 skills)

Based on AWS and CI/CD best practices:

- **[AWS S3/CloudFront](deployment/aws-s3-cloudfront/SKILL.md)** - S3 configuration, CloudFront setup, security headers, SSL/TLS
- **[GitHub Actions CI/CD](deployment/github-actions-cicd/SKILL.md)** - Workflow structure, security scanning, Lighthouse audits, deployment automation

### Compliance Skills (2 skills)

Based on ISO 27001, GDPR, and regulatory requirements:

- **[ISO 27001](compliance/iso-27001/SKILL.md)** - ISO 27001:2022 requirements, control implementation, documentation, audit preparation
- **[GDPR Compliance](compliance/gdpr/SKILL.md)** - Privacy by design, data protection, consent management, breach response

### Operations Skills (4 skills) 🆕

Based on [Hack23 ISMS-PUBLIC](https://github.com/Hack23/ISMS-PUBLIC) operational policies:

- **[🔄 Change Management](operations/change-management/SKILL.md)** - Risk-controlled change processes, CAB governance, rollback procedures, testing requirements
- **[💾 Backup & Recovery](operations/backup-recovery/SKILL.md)** - Business impact-driven data protection, RTO/RPO alignment, recovery validation
- **[🏢 Business Continuity](operations/business-continuity/SKILL.md)** - Business resilience framework, work area recovery, MTD-based prioritization
- **[🔥 Disaster Recovery](operations/disaster-recovery/SKILL.md)** - AWS-native technical resilience, chaos engineering, FIS experiments, multi-region failover

### Governance Skills (5 skills) 🆕

Based on [Hack23 ISMS-PUBLIC](https://github.com/Hack23/ISMS-PUBLIC) governance frameworks:

- **[📊 Risk Assessment](governance/risk-assessment/SKILL.md)** - Quantified risk analysis, 5x5 risk matrices, likelihood/impact evaluation
- **[📋 Risk Register](governance/risk-register/SKILL.md)** - Enterprise risk tracking, treatment planning, quarterly risk reviews
- **[💼 Asset Management](governance/asset-management/SKILL.md)** - IT asset inventory, classification, lifecycle management, dependency tracking
- **[🤝 Supplier Management](governance/supplier-management/SKILL.md)** - Vendor security assessment, due diligence, SLA monitoring, supply chain risk
- **[👥 Stakeholder Registry](governance/stakeholder-registry/SKILL.md)** - External stakeholder engagement, regulatory relationships, breach notification coordination

### Business Skills (3 skills) 🆕

Strategic business development and marketing expertise:

- **[Business Strategy](business/business-strategy/SKILL.md)** - Strategic business growth, market positioning, client acquisition, partnership development, revenue optimization
- **[Content Marketing](business/content-marketing/SKILL.md)** - B2B content marketing, demand generation, SEO content creation, thought leadership
- **[Brand Voice & Tone](business/brand-voice-tone/SKILL.md)** - Hack23 brand voice, tone, messaging guidelines, content style standards

### Intelligence Skills (2 skills) 🆕

OSINT and ethical information operations:

- **[OSINT Methods](intelligence/osint-methods/SKILL.md)** - Open Source Intelligence collection, analysis, verification, GDPR compliance
- **[Ethical Information Operations](intelligence/ethical-information-ops/SKILL.md)** - Ethical information operations, strategic communication, counter-disinformation, transparency advocacy

### Development Skills (2 skills) 🆕

Testing and code review best practices:

- **[Testing Strategy](development/testing-strategy/SKILL.md)** - Comprehensive testing: unit, integration, E2E, security, accessibility, performance
- **[Code Review Practices](development/code-review-practices/SKILL.md)** - Code review standards, quality gates, security checks, constructive feedback

### Documentation Skills (2 skills) 🆕

Product and API documentation standards:

- **[Product Documentation](documentation/product-documentation/SKILL.md)** - User guides, feature documentation, release notes, end-user communication
- **[API Documentation](documentation/api-documentation/SKILL.md)** - OpenAPI/Swagger, endpoints, authentication, examples, error handling

### Integration Skills (2 skills) 🆕

MCP servers and agent patterns:

- **[MCP Server Integration](integration/mcp-server-integration/SKILL.md)** - Model Context Protocol server configuration, usage patterns, security
- **[Copilot Agent Patterns](integration/copilot-agent-patterns/SKILL.md)** - Custom agent design patterns, collaboration workflows, orchestration

## Skills by Agent

### task-agent (Orchestration)
- All skills (comprehensive analysis and delegation)
- Particularly: business-strategy, copilot-agent-patterns, mcp-server-integration

### ui-enhancement-specialist
- html-css-best-practices
- accessibility-wcag
- seo-optimization
- c4-modeling
- secure-development

### marketing-specialist
- seo-optimization
- content-marketing
- brand-voice-tone
- html-css-best-practices
- gdpr

### business-development-specialist
- business-strategy
- content-marketing
- brand-voice-tone
- iso-27001
- security-architecture

### political-analyst
- osint-methods
- ethical-information-ops
- gdpr
- data-classification

### george-dorn (Developer)
- testing-strategy
- code-review-practices
- secure-development
- access-control
- github-actions-cicd

### simon-moon (Architect)
- c4-modeling
- security-architecture
- documentation-portfolio
- api-documentation
- cryptography

### hagbard-celine (Product Owner)
- product-documentation
- business-strategy
- content-marketing
- documentation-portfolio

## How to Use Skills

### For GitHub Copilot

Skills are automatically loaded when working in the Hack23 repositories. Copilot will reference these skills to:
- Generate secure code following ISMS policies
- Create compliant architecture documentation
- Implement accessible and performant web interfaces
- Configure secure deployment pipelines
- Ensure regulatory compliance
- Execute business and marketing strategies
- Conduct ethical intelligence operations
- Design and orchestrate custom agents

### For Developers

1. **Reference skills** before starting new work to understand requirements
2. **Cite specific skills** in PR descriptions to show compliance
3. **Update skills** when policies or standards change
4. **Propose new skills** for emerging technologies or practices

### For Custom Agents

Agents should document which skills they leverage in their profile:

```markdown
## 🎯 Skills Integration

This agent leverages these skills:
- **Secure Development** - Security-by-design principles
- **Testing Strategy** - Comprehensive testing approach
- **Code Review Practices** - Quality gates and feedback
```

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

## Skills Statistics

**Total Skills**: 23 skills (expanded from 14)
- Security: 4 skills
- Architecture: 3 skills
- Quality: 3 skills
- Deployment: 2 skills
- Compliance: 2 skills
- Business: 3 skills (new)
- Intelligence: 2 skills (new)
- Development: 2 skills (new)
- Documentation: 2 skills (new)
- Integration: 2 skills (new)

## Maintenance

Skills are maintained by:
- **Security Skills**: Security team, updated when ISMS policies change
- **Architecture Skills**: Architecture team, updated when patterns evolve
- **Quality Skills**: Quality team, updated when standards change
- **Deployment Skills**: DevOps team, updated when infrastructure changes
- **Compliance Skills**: Compliance team, updated when regulations change
- **Business Skills**: Business development and marketing teams
- **Intelligence Skills**: OSINT and strategic communication teams
- **Development Skills**: Engineering and QA teams
- **Documentation Skills**: Technical writers and product teams
- **Integration Skills**: DevOps and agent development teams

## Version History

- **2026-02-06**: Major skills expansion
  - Added 9 new skills across 5 new categories
  - Total skills: 23 (from 14)
  - New categories: Business (3), Intelligence (2), Development (2), Documentation (2), Integration (2)
  - Enhanced agent-to-skill mappings
  
- **2025-01-24**: Initial skills library creation
  - 14 skills covering security, architecture, quality, deployment, and compliance
  - Based on ISMS-PUBLIC policies and Hack23 standards

## License

All skills are licensed under Apache-2.0, consistent with Hack23's open-source commitment.

# GitHub Copilot Agent Skills

This directory contains **23 specialized agent skills** organized across **9 categories** that teach GitHub Copilot repeatable, best-practice workflows for Hack23 AB projects. Skills are automatically loaded by Copilot when relevant to your task.

**Latest Update (2026-02-06)**: Expanded from 14 to 23 skills with 5 new categories (Business, Intelligence, Development, Documentation, Integration)

## 📚 What Are Agent Skills?

Agent Skills are collections of instructions, rules, and examples that guide Copilot's behavior for specific tasks. They enable:

- **Consistency**: Ensure all code changes follow Hack23 standards
- **Security**: Enforce security-by-design principles from ISMS policies
- **Quality**: Maintain high code quality and documentation standards
- **Automation**: Repeatable workflows that save time and reduce errors
- **Business Strategy**: Guide market positioning and revenue optimization
- **Intelligence Operations**: Enable ethical OSINT and strategic communication
- **Comprehensive Testing**: Cover unit, integration, E2E, security, accessibility
- **Agent Orchestration**: Support custom agent collaboration and patterns

## 🎯 Skill Organization

Skills are organized by domain and follow the directory structure:

```
.github/skills/
├── README.md (this file)
├── INDEX.md (skill catalog)
├── security/ (4 skills)
│   ├── secure-development/
│   ├── access-control/
│   ├── cryptography/
│   └── data-classification/
├── architecture/ (3 skills)
│   ├── c4-modeling/
│   ├── security-architecture/
│   └── documentation-portfolio/
├── quality/ (3 skills)
│   ├── html-css-best-practices/
│   ├── accessibility-wcag/
│   └── seo-optimization/
├── deployment/ (2 skills)
│   ├── aws-s3-cloudfront/
│   └── github-actions-cicd/
├── compliance/ (2 skills)
│   ├── iso-27001/
│   └── gdpr/
├── business/ (3 skills) 🆕
│   ├── business-strategy/
│   ├── content-marketing/
│   └── brand-voice-tone/
├── intelligence/ (2 skills) 🆕
│   ├── osint-methods/
│   └── ethical-information-ops/
├── development/ (2 skills) 🆕
│   ├── testing-strategy/
│   └── code-review-practices/
├── documentation/ (2 skills) 🆕
│   ├── product-documentation/
│   └── api-documentation/
└── integration/ (2 skills) 🆕
    ├── mcp-server-integration/
    └── copilot-agent-patterns/
```

## 📖 How Skills Work

### Automatic Loading

GitHub Copilot automatically:
1. Scans `.github/skills/` when you open the repository
2. Loads relevant skills based on your task context
3. Applies skill instructions to guide code generation
4. Ensures compliance with defined rules and patterns

### Skill Structure

Each skill is a subdirectory containing:

```
skill-name/
├── SKILL.md          # Main skill definition with YAML frontmatter
├── examples/         # Code examples and templates (optional)
├── templates/        # File templates (optional)
└── docs/            # Additional documentation (optional)
```

### SKILL.md Format

```markdown
---
name: skill-name
description: When and why Copilot should use this skill
license: Apache-2.0
---

# Skill Name

## Purpose
Clear explanation of what this skill teaches Copilot to do.

## Rules
- Explicit, concrete rules
- What MUST be done
- What MUST NOT be done

## Examples
Concrete code examples showing correct patterns.

## Related Policies
Links to relevant ISMS policies and documentation.
```

## 🔐 Security-First Skills

All skills in this repository enforce **security-by-design** principles aligned with:

- **[Hack23 Public ISMS](https://github.com/Hack23/ISMS-PUBLIC)** - Complete security framework
- **[Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md)** - Development standards
- **ISO 27001:2022** - International security management standard
- **NIST CSF 2.0** - Cybersecurity framework
- **CIS Controls v8.1** - Security best practices
- **GDPR & NIS2** - Privacy and network security regulations

## 📋 Available Skills

See [INDEX.md](INDEX.md) for the complete catalog of available skills organized by category.

## 🎓 Using Skills

### For Developers

Skills work automatically - just work on your code and Copilot will apply relevant skills based on context. No special commands needed.

### For Custom Agents

Agents can reference specific skills in their instructions:

```markdown
## Skill Integration

When working on this task, leverage these skills:
- `.github/skills/security/secure-development/` - Follow secure coding practices
- `.github/skills/architecture/c4-modeling/` - Use C4 model documentation patterns
- `.github/skills/quality/accessibility-wcag/` - Ensure WCAG 2.1 AA compliance
```

### Testing Skills

Test skills by working on relevant tasks:

1. Make a code change related to the skill domain
2. Ask Copilot to review or suggest improvements
3. Verify that Copilot applies the skill's rules and patterns

## 🔄 Skill Lifecycle

### Creating New Skills

1. Identify a repeatable workflow or pattern
2. Create skill directory: `.github/skills/category/skill-name/`
3. Write SKILL.md with YAML frontmatter
4. Add examples and templates as needed
5. Reference relevant ISMS policies
6. Test with Copilot
7. Update INDEX.md

### Updating Skills

1. Modify SKILL.md content
2. Update examples if needed
3. Test changes with Copilot
4. Update skill version in frontmatter if using versioning

### Best Practices

- **Be Explicit**: Use concrete rules, not vague suggestions
- **Provide Examples**: Show correct patterns with code
- **Set Boundaries**: Clearly state what NOT to do
- **Reference Standards**: Link to ISMS policies and external standards
- **Keep Focused**: One skill = one concern
- **Stay Current**: Update skills as standards evolve

## 🌟 Skill Categories

### 🔐 Security Skills (4 skills)
Enforce security controls from Hack23 ISMS policies.

### 🏛️ Architecture Skills (3 skills)
Guide proper system design and documentation patterns.

### ✅ Quality Skills (3 skills)
Ensure code quality, accessibility, and performance.

### ☁️ Deployment Skills (2 skills)
Standardize deployment and infrastructure patterns.

### 📋 Compliance Skills (2 skills)
Maintain regulatory compliance (ISO 27001, GDPR, etc.).

### 💼 Business Skills (3 skills) 🆕
Strategic business development, marketing, and brand management.

### 🔍 Intelligence Skills (2 skills) 🆕
OSINT methods and ethical information operations.

### 💻 Development Skills (2 skills) 🆕
Testing strategies and code review best practices.

### 📖 Documentation Skills (2 skills) 🆕
Product and API documentation standards.

### 🔗 Integration Skills (2 skills) 🆕
MCP server integration and Copilot agent patterns.

## 📚 Learning Resources

- **[GitHub Copilot Agent Skills Documentation](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)**
- **[Anthropic Skills Repository](https://github.com/anthropics/skills)**
- **[GitHub Awesome Copilot](https://github.com/github/awesome-copilot)**
- **[Hack23 ISMS-PUBLIC](https://github.com/Hack23/ISMS-PUBLIC)**

## 🤝 Contributing

When adding new skills:

1. Follow the skill structure and naming conventions
2. Ensure alignment with ISMS policies
3. Include concrete examples
4. Test with GitHub Copilot
5. Update this README and INDEX.md
6. Submit pull request with clear description

## 📞 Questions?

- Review the skill's SKILL.md file for detailed guidance
- Check [INDEX.md](INDEX.md) for skill descriptions
- Reference [Hack23 ISMS-PUBLIC](https://github.com/Hack23/ISMS-PUBLIC) for policy details
- Consult with the Security Architect or relevant agent

---

**Remember**: Skills are your team's playbook. Keep them concrete, testable, and aligned with Hack23's security-first principles.

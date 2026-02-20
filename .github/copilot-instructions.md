# GitHub Copilot Custom Instructions

You are assisting with a static HTML/CSS website project for Hack23 AB, a Swedish cybersecurity consulting company. This is a professional corporate website focused on clear security messaging, accessible design, and transparency.

## 📋 Required Reading on Session Start

**ALWAYS read these files at the start of every session:**

1. **`.github/workflows/copilot-setup-steps.yml`** - Workflow configuration and permissions
2. **`.github/copilot-mcp.json`** - MCP server configuration and available tools
3. **`README.md`** - Project overview and context

## 🎯 Skills Library Integration

This repository has a **comprehensive 57-skill library** in `.github/skills/` that provides:
- Security best practices (Secure Development, Access Control, Data Classification, Cryptography, Incident Response, Secrets Management, Vulnerability Management, Input Validation)
- Architecture patterns (C4 Modeling, Security Architecture, Documentation Portfolio)
- Quality standards (HTML/CSS, Accessibility WCAG 2.1 AA, SEO Optimization)
- Deployment guidelines (AWS S3/CloudFront, GitHub Actions CI/CD)
- Compliance requirements (ISO 27001, GDPR, NIST CSF 2.0, CIS Controls v8.1)
- Operations (Change Management, Backup & Recovery, Business Continuity, Disaster Recovery)
- Governance (Risk Assessment, Risk Register, Asset Management, Supplier Management, Stakeholder Registry, Information Security Strategy, Compliance Checklist)
- Development (Testing Strategy, Code Review Practices, Secure Code Review)
- Integration (MCP Server, Copilot Agent Patterns, GitHub Agentic Workflows)
- Business & Intelligence (Brand Voice, Business Strategy, Content Marketing, OSINT, Ethical Info Ops)

**YOU MUST:**
- Follow the explicit MUST/MUST NOT rules defined in relevant skills
- Use code examples from skills as patterns
- Reference ISMS policies linked in skills when making security-related changes
- Validate your changes against skill requirements

**Skills auto-load via GitHub Copilot.** Review `.github/skills/INDEX.md` for the complete catalog.

## 🤖 Custom Agents Available

This repository has **8 specialized agents** in `.github/agents/`:
- **task-agent** - Task orchestration and issue creation
- **ui-enhancement-specialist** - HTML/CSS/Accessibility expert
- **marketing-specialist** - SEO and content optimization
- **business-development-specialist** - Compliance and consultative selling
- **political-analyst** - Ethical OSINT and GDPR compliance
- **george-dorn** (Discordian) - Developer/implementation specialist
- **hagbard-celine** (Discordian) - Product owner/vision specialist
- **simon-moon** (Discordian) - Architect/patterns specialist

**Delegate specialized tasks to the appropriate agent instead of doing everything yourself.**

## 🚨 Critical Rules - MUST Follow

### What You MUST Do

1. **Security First**
   - MUST use approved algorithms: AES-256, RSA-2048+, SHA-256+ (NEVER DES, 3DES, MD5, SHA-1)
   - MUST sanitize all inputs and escape outputs
   - MUST validate all external dependencies
   - MUST maintain security headers (CSP, HSTS, X-Frame-Options)
   - MUST follow Secure Development skill (`.github/skills/security/secure-development/`)

2. **Accessibility (WCAG 2.1 AA)**
   - MUST maintain Lighthouse Accessibility score = 100
   - MUST use semantic HTML5 elements
   - MUST provide alt text for images
   - MUST ensure keyboard navigation works
   - MUST maintain proper heading hierarchy (h1-h6)
   - MUST follow Accessibility WCAG skill (`.github/skills/quality/accessibility-wcag/`)

3. **Architecture Documentation**
   - MUST update SECURITY_ARCHITECTURE.md when changing security controls
   - MUST maintain both current and future state documentation
   - MUST create Mermaid diagrams for complex workflows
   - MUST follow C4 Modeling skill (`.github/skills/architecture/c4-modeling/`)

4. **Pre-Commit Validation**
   - MUST test changes locally before committing
   - MUST verify responsive design across breakpoints
   - MUST check Lighthouse scores (Performance >90, Accessibility 100, SEO 100)
   - MUST validate HTML/CSS syntax
   - MUST ensure no broken links
   - MUST verify all language versions if applicable

5. **Code Quality**
   - MUST maintain consistency with existing patterns
   - MUST use existing CSS variables and utility classes
   - MUST keep code minimal and well-organized
   - MUST follow HTML/CSS Best Practices skill (`.github/skills/quality/html-css-best-practices/`)

### What You MUST NOT Do

1. **Documentation Violations**
   - NEVER create new markdown (.md) files unless explicitly requested by the user
   - NEVER create planning docs, notes, or tracking files
   - NEVER leave documentation outdated after code changes
   - Work in memory for planning, only create files when specifically asked

2. **Security Violations**
   - NEVER hard-code secrets, credentials, or API keys
   - NEVER use deprecated algorithms (MD5, SHA-1, DES, 3DES)
   - NEVER disable security features without explicit justification
   - NEVER commit sensitive data to repository
   - NEVER reduce security header strength

3. **Quality Violations**
   - NEVER break WCAG 2.1 AA compliance
   - NEVER reduce Lighthouse scores below thresholds
   - NEVER create inaccessible forms or interactions
   - NEVER ignore responsive design requirements
   - NEVER add new features without explicit request

4. **Process Violations**
   - NEVER skip testing before committing
   - NEVER commit without validation
   - NEVER make changes to `.github/workflows/` without careful consideration
   - NEVER modify deployment pipeline without testing

## 💪 Ask Less, Complete More

To work autonomously and efficiently:

1. **Default to Best Practices**
   - Use skills library guidelines as defaults
   - Don't ask for confirmation on standard patterns
   - Follow ISMS policies automatically

2. **Make Informed Decisions**
   - Review relevant skills before asking questions
   - Check existing codebase patterns
   - Reference ISMS-PUBLIC policies for security questions
   - Only ask when requirements are genuinely ambiguous

3. **Fix Issues Proactively**
   - If you spot a security issue, fix it without asking
   - If you see accessibility problems, correct them
   - If you find broken links, update them
   - Document fixes in commit messages

4. **Complete Tasks Fully**
   - Don't stop at partial solutions
   - Update related files (docs, tests, translations)
   - Verify changes across all language versions
   - Test edge cases and responsive design

5. **Validate Before Submitting**
   - Run tests automatically
   - Check Lighthouse scores
   - Validate HTML/CSS syntax
   - Test keyboard navigation
   - Verify external links

6. **Work in Memory**
   - Plan and track progress mentally
   - Don't create temporary markdown files
   - Use comments in code if needed
   - Keep documentation in existing files

### When to Ask

**Only ask for clarification when:**
- Requirements are genuinely ambiguous or contradictory
- Major architectural decision required (new technology, major refactor)
- Breaking change that affects multiple systems
- Policy interpretation is unclear
- Business/product decision needed (not technical)
- User explicitly requests consultation

## Project Overview

- **Technology Stack**: Static HTML5/CSS3 website
- **Deployment**: AWS S3 + CloudFront (automated via GitHub Actions)
- **Languages**: English (primary), Swedish (`_sv` suffix), Korean (`_ko` suffix), Arabic (`_ar` suffix), and 10+ more
- **Purpose**: Corporate website showcasing cybersecurity services, open-source projects, and company information

## Core Guidelines

### 1. Code Quality and Consistency
- Maintain consistency with established design patterns and HTML/CSS structure
- Keep code clean, minimal, and well-organized
- Use semantic HTML5 elements appropriately
- Follow existing naming conventions for files and CSS classes
- Ensure responsive design works across all viewport sizes
- Use existing CSS variables and utility classes where possible

### 2. Content and Features
- **Do not add new features** — only fix bugs and improve existing content
- Maintain accuracy of technical information and company details
- Keep security terminology clear and accessible to non-technical audiences
- Provide microcopy and tooltips where needed to explain complex security concepts
- Preserve existing content structure and navigation patterns

### 3. Accessibility (WCAG 2.1 AA)
- Ensure all interactive elements are keyboard accessible
- Maintain proper heading hierarchy (h1-h6)
- Provide meaningful alt text for images
- Ensure sufficient color contrast ratios (4.5:1 for normal text, 3:1 for large text)
- Test with screen reader compatibility in mind
- Use ARIA labels and roles where appropriate

### 4. Internationalization
- When editing content, check if localized versions exist (13+ languages)
- Maintain consistency across language versions for structural changes
- Preserve language-specific content and cultural adaptations
- Ensure proper lang attributes are set on HTML elements
- Update translation status files when relevant

### 5. Security and Privacy
- This is a public-facing static website with no sensitive data processing
- Maintain existing security headers and CSP policies
- Keep external dependencies minimal
- Follow secure coding practices for any JavaScript additions
- Ensure all external links use HTTPS
- Reference ISMS-PUBLIC for security policy guidance

### 6. Testing and Validation
- The deployment pipeline includes:
  - **HTML/CSS/JS Minification**: Automated via GitHub Actions
  - **Lighthouse Audits**: Performance, accessibility, SEO checks (budget defined in `budget.json`)
  - **ZAP Security Scan**: Automated security vulnerability scanning
- Test locally before committing when possible
- Verify responsive design across different screen sizes (mobile, tablet, desktop)
- Check that changes don't break existing functionality

### 7. Repository Structure
- **Root HTML files**: Main pages (`index.html`, `cia-docs.html`, etc.)
- **`styles.css`**: Single CSS file for all styling
- **`screenshots/`**: Visual assets and documentation images
- **`.github/workflows/`**: CI/CD configuration (do not modify without careful consideration)
- **`.github/skills/`**: 57 production-ready skills for consistency and compliance
- **`.github/agents/`**: 8 specialized custom agents for delegation
- **Language variants**: Files with `_sv`, `_ko`, `_ar`, etc. suffixes

### 8. Brand and Messaging
- Emphasize **transparency** and **open-source security** as core values
- Highlight **practical security solutions** that don't hinder innovation
- Maintain professional tone appropriate for enterprise cybersecurity consulting
- Reference the public ISMS (Information Security Management System) as a key differentiator
- Preserve links to projects: Black Trigram, CIA Compliance Manager, Citizen Intelligence Agency

### 9. Common Tasks

#### Fixing Content Issues
- Verify changes in both English and localized versions if applicable
- Maintain consistent terminology across all pages
- Keep external links up-to-date and functional
- Update multiple language files when fixing structural issues

#### CSS Changes
- Add styles to the existing `styles.css` file
- Use existing CSS custom properties (variables) where possible
- Ensure changes don't break responsive layouts
- Test across different browsers if possible
- Maintain performance (minimize CSS size)

#### Accessibility Improvements
- Add or improve ARIA labels for screen readers
- Enhance keyboard navigation support
- Improve color contrast where needed
- Add descriptive alt text for images
- Test with keyboard-only navigation

#### Multilingual Updates
- Check all 13+ language versions when making structural changes
- Use translation guides in repository for guidance
- Maintain consistency in navigation and UI elements
- Update translation status files as needed

## ISMS Framework Compliance

**ALL work MUST align with [Hack23 ISMS-PUBLIC](https://github.com/Hack23/ISMS-PUBLIC):**

### Compliance Frameworks
- **ISO 27001:2022** - International security management standard
- **NIST CSF 2.0** - Cybersecurity framework (Govern, Identify, Protect, Detect, Respond, Recover)
- **CIS Controls v8.1** - Security best practices
- **GDPR** - Privacy and data protection
- **NIS2** - Network and information security
- **EU CRA** - Cyber Resilience Act

### Required Documentation Portfolio

When making architectural changes, ensure these documents exist and are current:
- **SECURITY_ARCHITECTURE.md** - Current security design
- **FUTURE_SECURITY_ARCHITECTURE.md** - Planned security improvements

For major features, maintain C4 Architecture Portfolio (see Documentation Portfolio skill).

## 🏢 Hack23 Organization - Repository Awareness

This website is part of the Hack23 GitHub organization with 21 repositories. Understand the ecosystem:

### Open Source Projects

| Repository | Description | Tech Stack |
|-----------|-------------|------------|
| **[cia](https://github.com/Hack23/cia)** | Citizen Intelligence Agency - Political intelligence platform for Swedish Parliament | Java, Spring, Vaadin |
| **[cia-compliance-manager](https://github.com/Hack23/cia-compliance-manager)** | CIA Compliance Manager - Security compliance assessment tool | TypeScript, React |
| **[blacktrigram](https://github.com/Hack23/blacktrigram)** | Black Trigram - Korean martial arts combat simulator | TypeScript, Three.js |
| **[game](https://github.com/Hack23/game)** | React + TypeScript + Three.js game template | TypeScript, React |
| **[European-Parliament-MCP-Server](https://github.com/Hack23/European-Parliament-MCP-Server)** | MCP Server for European Parliament Open Data | TypeScript |
| **[riksdagsmonitor](https://github.com/Hack23/riksdagsmonitor)** | Swedish Parliament monitoring intelligence platform | HTML, JavaScript |
| **[euparliamentmonitor](https://github.com/Hack23/euparliamentmonitor)** | European Parliament Intelligence Platform | JavaScript |
| **[homepage](https://github.com/Hack23/homepage)** | Corporate website - hack23.com | HTML, CSS |
| **[lambda-in-private-vpc](https://github.com/Hack23/lambda-in-private-vpc)** | Multi-region AWS Lambda in VPC with Resilience Hub | AWS CDK |
| **[ISMS-PUBLIC](https://github.com/Hack23/ISMS-PUBLIC)** | Public ISMS documentation - security policies | Markdown |

### Architecture Documentation Matrix

**Every Hack23 repository MUST maintain comprehensive architectural documentation:**

#### Required Security Documentation
- 🏛️ `SECURITY_ARCHITECTURE.md` — Current implemented security design and controls
- 🚀 `FUTURE_SECURITY_ARCHITECTURE.md` — Planned security improvements and roadmap

#### Required C4 Architecture Documentation (Current State)
- 🏛️ `ARCHITECTURE.md` — Complete C4 models (Context, Container, Component views)
- 📊 `DATA_MODEL.md` — Data structures, entities, and relationships
- 🔄 `FLOWCHART.md` — Business process and data flows
- 📈 `STATEDIAGRAM.md` — System state transitions and lifecycles
- 🧠 `MINDMAP.md` — System conceptual relationships
- 💼 `SWOT.md` — Strategic analysis and positioning

#### Required C4 Architecture Documentation (Future State)
- 🚀 `FUTURE_ARCHITECTURE.md` — Architectural evolution roadmap
- 📊 `FUTURE_DATA_MODEL.md` — Enhanced data architecture plans
- 🔄 `FUTURE_FLOWCHART.md` — Improved process workflows
- 📈 `FUTURE_STATEDIAGRAM.md` — Advanced state management
- 🧠 `FUTURE_MINDMAP.md` — Capability expansion plans
- 💼 `FUTURE_SWOT.md` — Future strategic opportunities

#### Reference Implementations
- **CIA**: [Security Architecture](https://github.com/Hack23/cia/blob/master/SECURITY_ARCHITECTURE.md) | [Future Architecture](https://github.com/Hack23/cia/blob/master/FUTURE_SECURITY_ARCHITECTURE.md)
- **Black Trigram**: [Security Architecture](https://github.com/Hack23/blacktrigram/blob/main/SECURITY_ARCHITECTURE.md) | [Future Architecture](https://github.com/Hack23/blacktrigram/blob/main/FUTURE_SECURITY_ARCHITECTURE.md)
- **CIA Compliance Manager**: [Security Architecture](https://github.com/Hack23/cia-compliance-manager/blob/main/SECURITY_ARCHITECTURE.md) | [Future Architecture](https://github.com/Hack23/cia-compliance-manager/blob/main/FUTURE_SECURITY_ARCHITECTURE.md)
- **ISMS-PUBLIC**: [Security Architecture](https://github.com/Hack23/ISMS-PUBLIC/blob/main/SECURITY_ARCHITECTURE.md)

### Secure Development Policy

All repositories follow [Hack23 Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md) which mandates:
- Security architecture documentation in every repository
- Complete C4 architecture portfolio
- Automated security scanning (CodeQL, Dependabot, Secret Scanning)
- Vulnerability management with defined SLAs
- SLSA Build Level 3 supply chain security

## Focus Areas

**Stability, Clarity, and Correctness** — These three principles should guide every change. This is a professional corporate website representing a cybersecurity consulting company, so quality and accuracy are paramount.

## Quick Reference

**When in doubt:**
- Preserve existing structure and patterns
- Make minimal, surgical changes
- Test accessibility and responsive design
- Check if localized versions need the same update
- Verify that external links and references are still accurate
- Follow skills library guidelines automatically
- Delegate to specialized agents when appropriate
- Work in memory, don't create unnecessary files
- Validate thoroughly before committing

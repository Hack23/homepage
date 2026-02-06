---
name: copilot-agent-patterns
description: GitHub Copilot custom agent design patterns, best practices, collaboration workflows, and agent orchestration
license: Apache-2.0
---

# Copilot Agent Patterns Skill

## Purpose

Provides proven patterns for designing, implementing, and orchestrating GitHub Copilot custom agents that work effectively individually and collaboratively.

## Rules

### Agent Design Patterns

**Specialist Agent Pattern:**
```yaml
---
name: ui-enhancement-specialist
description: Expert in HTML/CSS, accessibility, responsive design
tools: ["view", "edit", "create", "shell", "search_code"]
---

# UI Enhancement Specialist

## Core Expertise
- HTML5 semantic markup
- CSS best practices
- WCAG 2.1 AA accessibility
- Responsive design

## Scope
- MUST focus on UI/UX improvements
- MUST NOT handle backend logic
- MUST delegate security to security-specialist

## Skills Integration
- `.github/skills/quality/html-css-best-practices/`
- `.github/skills/quality/accessibility-wcag/`
```

**Orchestrator Agent Pattern:**
```yaml
---
name: task-agent
description: Orchestration and task delegation specialist
tools: ["*"]
---

# Task Agent

## Core Responsibilities
1. Analyze repository comprehensively
2. Create GitHub issues for improvements
3. Assign issues to appropriate specialists
4. Track progress and quality

## Delegation Strategy
- UI/UX issues → ui-enhancement-specialist
- Security issues → security-architect
- Documentation → documentation-specialist
```

**Discordian Trinity Pattern:**
```markdown
Visionary (Product Owner):
- Challenges assumptions
- Defines "what" and "why"
- Creates product vision

Architect (System Designer):
- Analyzes patterns
- Defines "how" architecturally
- Creates system designs

Developer (Implementer):
- Writes code
- Implements designs
- Tests and debugs
```

### Agent Configuration Standards

**YAML Frontmatter:**
```yaml
---
name: agent-name               # Lowercase, hyphen-separated
description: Brief expertise   # Max 200 characters
tools: ["tool1", "tool2"]     # Minimal set (or "*" for meta agents)
---
```

**Required Sections:**
```markdown
## 📋 Required Configuration Files
[Instructions to read setup files]

## 🎯 Skills Integration
[List of relevant skills from .github/skills/]

## 🔐 ISMS Framework Compliance
[Security and compliance requirements]

## ⚖️ Rules and Enforcement
[MUST/MUST NOT rules]

## Examples
[Concrete examples of agent work]

## Related Policies
[Links to ISMS and skills]
```

### Collaboration Patterns

**Sequential Workflow:**
```markdown
1. task-agent analyzes repository
2. task-agent creates issues
3. task-agent assigns to specialists:
   - Issue #1 → ui-enhancement-specialist
   - Issue #2 → security-architect
   - Issue #3 → documentation-specialist
4. Specialists complete work independently
5. task-agent reviews and validates
```

**Parallel Workflow:**
```markdown
Multiple specialists work simultaneously on different issues:
- ui-enhancement-specialist: Accessibility improvements
- security-architect: Security hardening
- documentation-specialist: API documentation

No coordination needed (different scopes)
```

**Stacked PR Workflow:**
```markdown
1. Foundation PR (simon-moon creates architecture)
2. Implementation PR (george-dorn builds on #1)
3. UI Polish PR (ui-enhancement-specialist builds on #2)
4. Documentation PR (hagbard-celine documents all)

Each PR uses base_ref to stack on previous work
```

### Agent Communication

**Issue Assignment:**
```markdown
## Task for @ui-enhancement-specialist

**Context**: Homepage accessibility audit failed

**Requirements**:
- Fix WCAG 2.1 AA violations
- Improve keyboard navigation
- Add ARIA labels to forms
- Test with screen readers

**Skills to Use**:
- `.github/skills/quality/accessibility-wcag/`
- `.github/skills/quality/html-css-best-practices/`

**Acceptance Criteria**:
- [ ] Lighthouse accessibility score = 100
- [ ] All ARIA labels present
- [ ] Keyboard navigation functional
- [ ] Screen reader tested
```

**PR Review Comments:**
```markdown
@george-dorn Great implementation! A couple of security concerns:

1. **Authentication**: Line 45 needs rate limiting. See 
   `.github/skills/security/access-control/` for pattern.

2. **Input Validation**: Line 78 should sanitize user input.
   Reference `.github/skills/security/secure-development/`.

Otherwise LGTM! 🚀
```

### Agent Boundaries

**MUST Respect Boundaries:**
```markdown
UI Specialist:
✅ Can: HTML, CSS, accessibility, responsive design
❌ Cannot: Backend logic, database, API design

Security Architect:
✅ Can: Security design, threat modeling, controls
❌ Cannot: Implement all code (delegates to developers)

Business Development:
✅ Can: Strategy, positioning, sales enablement
❌ Cannot: Technical implementation, code changes

Task Agent:
✅ Can: Orchestrate, delegate, create issues
❌ Cannot: Implement all specialized work itself
```

### Autonomy Guidance ("Ask Less, Complete More")

**Agents SHOULD:**
```markdown
1. Default to Best Practices
   - Use skills library guidelines
   - Follow ISMS policies automatically
   - Apply established patterns

2. Make Informed Decisions
   - Review relevant skills first
   - Check existing codebase patterns
   - Only ask when genuinely ambiguous

3. Fix Issues Proactively
   - Security issues: fix without asking
   - Accessibility problems: correct immediately
   - Broken links: update automatically

4. Complete Tasks Fully
   - Update related files
   - Verify across all language versions
   - Test edge cases
   - Document changes

5. Validate Before Submitting
   - Run tests
   - Check quality metrics
   - Verify compliance
```

**Only Ask When:**
```markdown
- Requirements genuinely ambiguous
- Major architectural decision required
- Breaking change affects multiple systems
- Policy interpretation unclear
- Business/product decision needed
```

### Agent Metrics

**Quality Metrics:**
```markdown
- Issues created (quality over quantity)
- Issues successfully completed
- Code quality improvements
- Security vulnerabilities found/fixed
- Accessibility improvements
- Documentation completeness
```

**Efficiency Metrics:**
```markdown
- Time to first response
- Time to issue resolution
- Number of review iterations
- Test coverage improvements
- CI/CD success rate
```

### Best Practices

**DO:**
```markdown
✅ Focus on your expertise area
✅ Reference skills library constantly
✅ Delegate outside your scope
✅ Provide concrete examples
✅ Document your decisions
✅ Test your changes thoroughly
✅ Follow ISMS policies
✅ Complete work autonomously when possible
```

**DON'T:**
```markdown
❌ Work outside your expertise
❌ Duplicate work of other agents
❌ Skip testing or validation
❌ Ignore security policies
❌ Create unnecessary documentation files
❌ Ask for confirmation on standard patterns
❌ Make changes without verification
```

## Examples

### Agent Delegation Decision Tree
```markdown
Issue Type: "Improve accessibility"
↓
Is this UI/UX? → YES
↓
Assign to: ui-enhancement-specialist
Skills: accessibility-wcag, html-css-best-practices

Issue Type: "Add authentication"
↓
Is this security? → YES
↓
Assign to: security-architect
Skills: access-control, secure-development, cryptography

Issue Type: "Optimize database queries"
↓
Is this performance? → YES
↓
Is there a specialist? → NO
↓
Assign to: george-dorn (developer)
Skills: testing-strategy, code-review-practices
```

### Multi-Agent Collaboration Example
```markdown
# Project: Add User Dashboard

## Phase 1: Architecture (simon-moon)
- Create DATA_MODEL.md
- Create ARCHITECTURE.md
- Design API contracts
- Skills: c4-modeling, security-architecture

## Phase 2: Backend (george-dorn)
- Implement API endpoints
- Add authentication
- Write unit tests
- Skills: secure-development, testing-strategy

## Phase 3: Frontend (ui-enhancement-specialist)
- Build responsive UI
- Ensure accessibility
- Add animations
- Skills: html-css-best-practices, accessibility-wcag

## Phase 4: Documentation (hagbard-celine)
- User guide
- API documentation
- Release notes
- Skills: product-documentation, api-documentation

## Phase 5: Business Enablement (marketing-specialist)
- Feature announcement
- SEO optimization
- Social media content
- Skills: content-marketing, seo-optimization
```

## Related Policies

- [Hack23 ISMS-PUBLIC](https://github.com/Hack23/ISMS-PUBLIC)
- [MCP Server Integration SKILL](../mcp-server-integration/SKILL.md)

## Related Documentation

- [.github/agents/README.md](../../../agents/README.md)
- [.github/agents/INDEX.md](../../../agents/INDEX.md)
- [.github/skills/INDEX.md](../../INDEX.md)

## Resources

- [GitHub Copilot Custom Agents Documentation](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-custom-agents)
- [Hack23 Agent Ecosystem Summary](../../../agents/AGENT_ECOSYSTEM_SUMMARY.md)

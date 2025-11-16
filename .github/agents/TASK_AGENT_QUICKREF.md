# Task Agent Quick Reference

> **TL;DR**: Product quality orchestrator that analyzes the Hack23 homepage comprehensively and creates actionable GitHub issues with intelligent agent assignments.

## When to Use Task Agent

Use the Task Agent when you need:
- ✅ Comprehensive product analysis across all dimensions
- ✅ GitHub issue creation with proper structure and context
- ✅ Intelligent assignment to specialist agents
- ✅ ISMS compliance validation
- ✅ AWS infrastructure review
- ✅ Multi-dimensional quality assessment
- ✅ Don't know which specialist agent to use

## Quick Commands

### Comprehensive Analysis
```
@task-agent analyze the homepage comprehensively and create prioritized issues
```

### Focused Analysis
```
@task-agent analyze homepage for accessibility issues and create GitHub issues
@task-agent review ISMS compliance and generate improvement tasks
@task-agent audit AWS infrastructure and create optimization issues
@task-agent check security and performance, create issues with priorities
```

### Domain-Specific Analysis
```
@task-agent analyze UI/UX quality and assign to appropriate specialists
@task-agent review content accuracy and SEO, create issues for marketing team
@task-agent check responsive design across all pages and create UI issues
```

## What Task Agent Does

### Phase 1: Deep Analysis (Always First)
1. **Repository Deep-Dive**
   - Clone and analyze code structure
   - Review recent commits and PRs
   - Identify technical debt

2. **ISMS Alignment Check**
   - Review public ISMS documentation
   - Validate security policy compliance
   - Check accessibility standards (WCAG 2.1 AA)

3. **Visual Testing (Playwright)**
   - Navigate live website
   - Capture screenshots
   - Test responsive design
   - Verify all language versions (EN/SV/KO)

4. **Quality Assessment**
   - Review Lighthouse scores
   - Analyze ZAP security scans
   - Check HTML/CSS/JS quality

5. **AWS Infrastructure Review**
   - Use aws-knowledge MCP
   - Validate S3/CloudFront configuration
   - Check best practices compliance

### Phase 2: Issue Creation
Creates structured GitHub issues with:
- 🎯 Clear objective
- 📊 Detailed background and analysis
- 🔍 Visual evidence (screenshots)
- ✅ Testable acceptance criteria
- 🛠️ Implementation guidance
- 🏷️ ISMS alignment notes
- 🔗 Related resources
- 👥 Agent recommendation

### Phase 3: Smart Assignment
Matches issues to specialists:
- 🚢 **Hagbard** - Product vision, strategy
- 🔢 **Simon** - Architecture, design patterns
- 💻 **George** - Implementation, debugging
- 🎨 **UI Specialist** - HTML/CSS, accessibility
- 💼 **Business Dev** - Market positioning
- 📢 **Marketing** - Content, SEO
- 🏛️ **Political Analyst** - OSINT features

## Issue Categories

The Task Agent identifies issues across:

| Category | Icon | Priority Range | Typical Assignee |
|----------|------|----------------|------------------|
| Security | 🔐 | Critical-High | George + Simon |
| Accessibility | ♿ | High-Medium | UI Specialist |
| Performance | ⚡ | High-Medium | George |
| UI/UX | 🎨 | Medium-Low | UI Specialist |
| Content | 📝 | Medium-Low | Marketing |
| ISMS Alignment | 📋 | High | Multiple |
| Infrastructure | ☁️ | High-Medium | Simon + George |
| Quality | ✅ | Medium-Low | George |

## Priority Framework

**Pentagon of Importance** (inspired by Discordian thinking):

1. 🔴 **Critical** - Security vulnerabilities, broken functionality, major accessibility issues
2. 🟠 **High** - ISMS non-compliance, poor UX, performance issues
3. 🟡 **Medium** - Content improvements, minor UI issues, optimization
4. 🟢 **Low** - Nice-to-have features, documentation enhancements
5. 🔵 **Future** - Vision items, major features, strategic initiatives

## MCP Servers Used

Task Agent leverages these extensively:

| MCP | Usage |
|-----|-------|
| **github** | Create/search issues, analyze repos, review PRs/commits |
| **playwright** | Visual testing, screenshots, responsive design checks |
| **aws-knowledge** | Infrastructure best practices, S3/CloudFront validation |
| **brave-search** | Industry research, competitive analysis, tool discovery |
| **fetch** | Analyze external documentation and resources |

## Example Outputs

### Typical Analysis Output
```
Task Agent analyzed:
✅ 74 HTML files across 3 languages
✅ Live website with Playwright (5 viewports)
✅ ISMS compliance against ISO 27001
✅ Lighthouse scores (Performance: 92, Accessibility: 87, SEO: 95)
✅ ZAP security scan (11 issues found)
✅ AWS S3/CloudFront configuration

Created 15 GitHub issues:
🔴 Critical (2): CSP missing, SRI not implemented
🟠 High (5): Accessibility violations, slow page load
🟡 Medium (4): Content updates, minor UI fixes
🟢 Low (3): Documentation improvements
🔵 Future (1): New feature consideration

Assigned to:
- George Dorn (5 issues) - Implementation
- UI Specialist (4 issues) - Accessibility
- Marketing (3 issues) - Content
- Simon Moon (2 issues) - Architecture
- Hagbard (1 issue) - Strategy
```

### Sample Issue Structure
```markdown
## 🎯 Objective
Add Subresource Integrity (SRI) to External Font Resources

## 📊 Background
Found via ZAP security scan - 11 instances of missing SRI on Google Fonts
Impact: Supply chain attack vulnerability

## 🔍 Analysis
- Current: All 74 HTML files load fonts without SRI
- Risk: CDN compromise could inject malicious code
- Standard: SRI recommended for external resources
[Screenshot attached]

## ✅ Acceptance Criteria
- [ ] Generate SRI hashes for all Google Fonts
- [ ] Add integrity and crossorigin attributes
- [ ] Test across all browsers
- [ ] Update all 74+ HTML files

## 🛠️ Implementation Guidance
curl -s [URL] | openssl dgst -sha384 -binary | openssl base64 -A
Add to all <link> tags for fonts

## 🏷️ ISMS Alignment
- Policy: Supply Chain Security
- Control: ISO 27001 A.15.1 (Supplier Security)
- Classification: Public site, but needs integrity

## 👥 Recommended Assignment
Primary: @george-dorn (implementation)
Review: @simon-moon (pattern consistency)
```

## Best Practices

### DO ✅
- Let Task Agent perform comprehensive analysis first
- Trust its agent assignment recommendations
- Use it for quality audits and ISMS compliance
- Provide specific focus areas when needed
- Review created issues before specialists start work

### DON'T ❌
- Skip the analysis phase
- Override agent assignments without reason
- Use for simple, single-file changes (use specialists directly)
- Expect implementation (Task Agent orchestrates, doesn't implement)
- Ignore ISMS alignment recommendations

## Complementary Agents

After Task Agent creates issues, these agents execute:

| Agent | Use When Issue Involves |
|-------|------------------------|
| 🚢 Hagbard | Product vision, strategic direction, major features |
| 🔢 Simon | System architecture, design patterns, Mermaid diagrams |
| 💻 George | Code implementation, debugging, technical fixes |
| 🎨 UI Specialist | HTML/CSS, accessibility, responsive design |
| 💼 Business Dev | Market strategy, client acquisition, partnerships |
| 📢 Marketing | Content creation, SEO, brand messaging |
| 🏛️ Political Analyst | OSINT features, political analysis capabilities |

## Real-World Scenarios

### Scenario 1: Monthly Quality Review
```
@task-agent perform monthly quality audit of homepage and create prioritized improvement issues
```
**Result**: 20-30 issues across all categories, properly prioritized and assigned

### Scenario 2: Pre-Release Check
```
@task-agent analyze homepage for security and accessibility before release
```
**Result**: Focused issues on critical areas, must-fix before deployment

### Scenario 3: ISMS Compliance Audit
```
@task-agent validate ISMS compliance across homepage and create remediation tasks
```
**Result**: Issues linked to specific policies, assigned to appropriate owners

### Scenario 4: Performance Optimization
```
@task-agent analyze performance metrics and create optimization issues
```
**Result**: Focused performance issues with metrics and targets

## Tips & Tricks

1. **Be Specific**: "analyze accessibility" is better than "analyze everything"
2. **Set Context**: Mention if there's a specific concern or deadline
3. **Review First**: Check created issues before specialists start
4. **Iterate**: Run periodic audits to track improvement over time
5. **Trust the Process**: Task Agent's 5-phase workflow is comprehensive

## Common Questions

**Q: Should I use Task Agent or a specialist directly?**  
A: Use Task Agent when you need analysis and don't know what issues exist. Use specialists when you have a specific, known issue.

**Q: Can Task Agent implement fixes?**  
A: No, Task Agent analyzes and creates issues. Specialists (like George, UI Specialist) implement.

**Q: How often should I run Task Agent?**  
A: Monthly for general quality, before releases for critical checks, after major changes.

**Q: What if I disagree with agent assignments?**  
A: Task Agent provides recommendations. You can reassign, but consider its rationale first.

**Q: Can Task Agent work on other repos besides homepage?**  
A: Yes, but it's optimized for Hack23 homepage. May need guidance for other repos.

## Quick Stats

- **Tools**: Full access (`tools: ["*"]`)
- **MCP Servers**: 5 primary (github, playwright, aws-knowledge, brave-search, fetch)
- **Issue Template**: 8 sections (Objective, Background, Analysis, Criteria, Guidance, ISMS, Resources, Assignment)
- **Categories**: 8 issue types
- **Priorities**: 5 levels (Pentagon of Importance)
- **Specialists**: Can assign to 7 different agent types

---

**Remember**: Task Agent is your product quality guardian. Let it analyze deeply, create precisely, and assign intelligently. 🍎

**Quick Help**: `@task-agent --help` or see full documentation in `task-agent.md`

# ♿ Add accessibility testing tools to Copilot environment

## 🎯 Objective

Install accessibility testing tools in `.github/workflows/copilot-setup-steps.yml` to help GitHub Copilot ensure WCAG 2.1 AA compliance when making changes to the website.

## 📋 Background

As a **cybersecurity consulting company**, Hack23's website must demonstrate commitment to security AND accessibility best practices. The repository's custom instructions explicitly mention:

> **3. Accessibility (WCAG 2.1 AA)**
> - Ensure all interactive elements are keyboard accessible
> - Maintain proper heading hierarchy (h1-h6)
> - Provide meaningful alt text for images
> - Ensure sufficient color contrast ratios
> - Test with screen reader compatibility in mind
> - Use ARIA labels and roles where appropriate

Currently, accessibility checks are manual. Adding automated tools will:
- Catch accessibility issues during development
- Ensure consistent WCAG compliance across all 74 pages
- Prevent accessibility regressions when making changes
- Demonstrate professional standards to enterprise clients

## ✅ Acceptance Criteria

- [ ] Install axe-core CLI or pa11y for accessibility testing
- [ ] Add accessibility testing tool to copilot-setup-steps.yml
- [ ] Create configuration file with WCAG 2.1 AA rules
- [ ] Verify Copilot can run accessibility checks during its work
- [ ] Keep permissions minimal (`contents: read` only)
- [ ] Test workflow via workflow_dispatch
- [ ] Document tool choice and configuration in PR description

## 🛠️ Implementation Guidance

### Files to Modify
- `.github/workflows/copilot-setup-steps.yml` - Add accessibility tool installation
- `.axerc.json` or `.pa11yrc` (NEW) - Configuration file

### Approach

**Option 1: Using axe-core CLI (Recommended - Industry Standard)**
```yaml
- name: Install axe-core CLI
  run: |
    npm install -g @axe-core/cli
    axe --version
```

**Option 2: Using pa11y (Alternative - More configurable)**
```yaml
- name: Install pa11y
  run: |
    npm install -g pa11y
    pa11y --version
```

**Recommended**: Use axe-core CLI - it's the industry standard used by most development teams and integrates well with browser DevTools.

### Configuration File: .axerc.json
```json
{
  "rules": {
    "color-contrast": { "enabled": true },
    "html-has-lang": { "enabled": true },
    "image-alt": { "enabled": true },
    "label": { "enabled": true },
    "valid-lang": { "enabled": true },
    "landmark-one-main": { "enabled": true },
    "page-has-heading-one": { "enabled": true },
    "heading-order": { "enabled": true }
  },
  "tags": ["wcag2a", "wcag2aa"],
  "locale": "en"
}
```

**Alternative Configuration: .pa11yrc**
```json
{
  "standard": "WCAG2AA",
  "level": "error",
  "timeout": 10000,
  "wait": 1000,
  "chromeLaunchConfig": {
    "args": ["--no-sandbox", "--disable-setuid-sandbox"]
  },
  "ignore": []
}
```

### Example Usage by Copilot

**With axe-core:**
```bash
# Test single file
axe index.html

# Test with specific file protocol
axe file:///home/runner/work/homepage/homepage/index.html

# Test multiple files with custom config
axe --config .axerc.json index.html cia-docs.html blog.html

# Output as JSON for parsing
axe index.html --save results.json
```

**With pa11y:**
```bash
# Test single page
pa11y index.html

# Test with reporter
pa11y --reporter cli index.html

# Test multiple pages
pa11y index.html cia-docs.html blog.html
```

### Key Accessibility Areas for Hack23 Website

Based on repository custom instructions:

1. **Color Contrast** - Ensure text is readable
2. **Keyboard Navigation** - All interactive elements accessible via keyboard
3. **Heading Hierarchy** - Proper h1-h6 structure
4. **Alt Text** - All images have meaningful descriptions
5. **ARIA Labels** - Screen reader compatibility
6. **Language Attributes** - Proper lang tags for multilingual content (English, Swedish, Korean)

### Testing Steps
1. Add accessibility tool installation to copilot-setup-steps.yml
2. Create configuration file (.axerc.json or .pa11yrc)
3. Commit to feature branch
4. Run workflow via workflow_dispatch
5. Test tool on a sample page: `axe file://$(pwd)/index.html`
6. Review accessibility violations and verify tool works

## 🔗 Related Resources

- [axe-core CLI Documentation](https://github.com/dequelabs/axe-core-npm/tree/develop/packages/cli)
- [pa11y Documentation](https://pa11y.org/)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Deque University - axe Rules](https://dequeuniversity.com/rules/axe/)
- Repository custom instructions: Accessibility section

## 📊 Metadata

**Repository Stats:**
- 74 HTML files requiring WCAG compliance
- Multi-language support (English, Swedish, Korean)
- Corporate website for enterprise cybersecurity consulting

**Accessibility Priority Areas:**
- Color contrast (professional color scheme)
- Semantic HTML structure
- Keyboard navigation
- Screen reader compatibility
- Multi-language support (lang attributes)

**Priority:** High  
**Effort:** Small (2 hours)  
**Impact:** Ensures professional accessibility standards, demonstrates security expertise

**Suggested Labels:** `enhancement`, `priority:high`, `size:small`, `accessibility`, `WCAG`, `copilot-enhancement`

## 💡 Business Value

**Why This Matters for Hack23:**

1. **Credibility**: A security consulting company must demonstrate comprehensive best practices
2. **Compliance**: Enterprise clients often have accessibility requirements (WCAG 2.1 AA)
3. **Inclusivity**: Shows commitment to universal access
4. **Legal**: Many jurisdictions require accessibility compliance
5. **SEO**: Accessible sites rank better in search engines

**Direct Quote from Custom Instructions:**
> "Maintain accessibility (WCAG 2.1 AA)" and "Preserve links to projects: Black Trigram, CIA Compliance Manager, Citizen Intelligence Agency"

Automated accessibility testing ensures Copilot maintains these standards when making changes.

## 🎯 Success Metrics

After implementation, Copilot should be able to:
- ✅ Test any page for WCAG 2.1 AA compliance
- ✅ Identify color contrast issues
- ✅ Verify heading hierarchy
- ✅ Check alt text completeness
- ✅ Validate ARIA labels
- ✅ Test keyboard navigation paths

## 🔄 Integration with Existing Workflow

This complements existing quality checks:
- **Lighthouse audits** (already in main.yml) - Performance + basic accessibility
- **ZAP security scan** (already in main.yml) - Security testing
- **This enhancement** - Comprehensive WCAG 2.1 AA testing during development

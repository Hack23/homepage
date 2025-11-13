# 🎨 Add CSS linting and validation to Copilot setup

## 🎯 Objective

Install CSS linting and validation tools in `.github/workflows/copilot-setup-steps.yml` to help GitHub Copilot maintain code quality in the 1,931-line `styles.css` file.

## 📋 Background

The homepage has a single comprehensive CSS file (1,931 lines) that styles all 74 HTML pages. CSS validation is critical for:
- Preventing CSS syntax errors
- Ensuring cross-browser compatibility
- Maintaining consistent styling patterns
- Catching deprecated properties early
- Validating CSS custom properties (variables)

## ✅ Acceptance Criteria

- [ ] Install stylelint with standard configuration in copilot-setup-steps.yml
- [ ] Add CSS validator (W3C CSS validator or alternative)
- [ ] Create minimal `.stylelintrc.json` configuration file
- [ ] Verify Copilot can run linting during its work
- [ ] Keep permissions minimal (`contents: read` only)
- [ ] Test workflow via workflow_dispatch
- [ ] Document linting rules in PR description

## 🛠️ Implementation Guidance

### Files to Modify
- `.github/workflows/copilot-setup-steps.yml` - Add CSS linting installation
- `.stylelintrc.json` (NEW) - Stylelint configuration

### Approach

**Step 1: Install stylelint in copilot-setup-steps.yml**
```yaml
- name: Install CSS Linting Tools
  run: |
    npm install -g stylelint stylelint-config-standard
    stylelint --version
```

**Step 2: Create .stylelintrc.json**
```json
{
  "extends": "stylelint-config-standard",
  "rules": {
    "indentation": 2,
    "color-hex-case": "lower",
    "selector-max-id": 1,
    "declaration-block-no-duplicate-properties": true,
    "no-descending-specificity": null
  },
  "ignoreFiles": [
    "screenshots/**/*"
  ]
}
```

**Alternative: CSS Validator (W3C)**
```yaml
- name: Install CSS Validator
  run: |
    npm install -g css-validator
```

### Current CSS File Analysis
From `styles.css` (1,931 lines):
- Uses CSS custom properties (variables)
- Responsive design with media queries
- Flexbox and Grid layouts
- Modern CSS features

### Example Usage by Copilot
```bash
# Lint all CSS files
stylelint "**/*.css"

# Lint specific file
stylelint styles.css

# Lint with auto-fix
stylelint styles.css --fix

# Validate CSS syntax
css-validator styles.css
```

### Testing Steps
1. Add stylelint installation to copilot-setup-steps.yml
2. Create .stylelintrc.json with standard config
3. Commit to feature branch
4. Run workflow via workflow_dispatch
5. Verify stylelint is installed and can lint styles.css

## 🔗 Related Resources

- [Stylelint Documentation](https://stylelint.io/)
- [stylelint-config-standard Rules](https://github.com/stylelint/stylelint-config-standard)
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- Current CSS file: `styles.css` (1,931 lines)

## 📊 Metadata

**Repository Stats:**
- 1 CSS file: `styles.css` (1,931 lines)
- Used by all 74 HTML pages
- Contains: variables, flexbox, grid, media queries

**Priority:** High  
**Effort:** Small (1-2 hours)  
**Impact:** Prevents CSS errors and maintains code quality

**Suggested Labels:** `enhancement`, `priority:high`, `size:small`, `domain:frontend`, `copilot-enhancement`

## 💡 Additional Considerations

### Why stylelint?
- Industry standard CSS linter
- Extensible with plugins
- Auto-fix capability
- Good error messages
- Well-maintained

### Configuration Philosophy
- Start with standard config (not too strict)
- Can be tightened over time
- Disable problematic rules initially
- Focus on syntax errors first

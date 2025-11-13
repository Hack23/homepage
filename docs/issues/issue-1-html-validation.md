# 🔧 Add HTML validation tools to copilot-setup-steps.yml

## 🎯 Objective

Enhance `.github/workflows/copilot-setup-steps.yml` with HTML validation tools to help GitHub Copilot coding agent validate HTML correctness when making changes to the 74 HTML files in this static website.

## 📋 Background

The homepage repository contains 74 HTML files (averaging 349 lines each) and currently has a minimal `copilot-setup-steps.yml` with only a checkout step. Adding HTML validation tools will enable Copilot to:
- Validate HTML syntax before committing changes
- Catch accessibility issues early
- Ensure HTML5 compliance across all pages
- Prevent broken markup that could affect SEO and user experience

## ✅ Acceptance Criteria

- [ ] Install `html5validator` or `vnu` (W3C Nu Html Checker) in copilot-setup-steps.yml
- [ ] Add setup step to install HTML validation tool
- [ ] Verify the tool can be invoked by Copilot during its work
- [ ] Keep permissions minimal (`contents: read` is sufficient)
- [ ] Test workflow runs successfully via workflow_dispatch
- [ ] Document which validator was chosen and why in PR description

## 🛠️ Implementation Guidance

### Files to Modify
- `.github/workflows/copilot-setup-steps.yml` - Add HTML validator installation step

### Approach

**Option 1: Using html5validator (Python-based) - RECOMMENDED**
```yaml
- name: Install HTML5 Validator
  run: |
    pip install html5validator
    html5validator --version
```

**Why recommended**: 
- Fast installation (pip-based)
- No Java dependency
- Can validate HTML and CSS together
- Works well with Ubuntu runners

**Option 2: Using vnu (Official W3C validator)**
```yaml
- name: Install vnu Validator
  run: |
    wget https://github.com/validator/validator/releases/latest/download/vnu.jar_latest.zip
    unzip -q vnu.jar_latest.zip
    echo "VNU_JAR=$(pwd)/vnu-runtime-image/bin/vnu" >> $GITHUB_ENV
```

### Current copilot-setup-steps.yml structure:
```yaml
permissions:
  contents: read  # ✅ Sufficient - no additional permissions needed

steps:
  - name: Checkout
    uses: actions/checkout@v5
  
  # ADD HERE: HTML validator installation
```

### Example Usage by Copilot
Once installed, Copilot can run:
```bash
# Validate all HTML files
html5validator --root . --also-check-css

# Validate specific file
html5validator index.html

# Validate with specific options
html5validator --root . --ignore screenshots/ --log INFO
```

### Testing Steps
1. Add the installation step to copilot-setup-steps.yml
2. Commit to a feature branch
3. Go to Actions tab → Copilot Setup Steps → Run workflow (workflow_dispatch)
4. Verify the workflow completes successfully
5. Check logs to confirm html5validator is installed

## 🔗 Related Resources

- [GitHub Copilot Environment Customization](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment)
- [html5validator Documentation](https://github.com/svenkreiss/html5validator)
- [W3C Nu Html Checker](https://validator.github.io/validator/)
- Current workflow: `.github/workflows/copilot-setup-steps.yml`

## 📊 Metadata

**Repository Stats:**
- 74 HTML files (average 349 lines each)
- 1,931 lines in styles.css
- Static site deployed to AWS S3/CloudFront

**Priority:** High  
**Effort:** Small (1-2 hours)  
**Impact:** Enables Copilot to validate HTML changes automatically

**Suggested Labels:** `enhancement`, `priority:high`, `size:small`, `domain:infrastructure`, `copilot-enhancement`

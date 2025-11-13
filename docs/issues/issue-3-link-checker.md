# 🔗 Add link checker for homepage content validation

## 🎯 Objective

Install a link checker tool in `.github/workflows/copilot-setup-steps.yml` to help GitHub Copilot validate that all external and internal links remain functional when making content changes.

## 📋 Background

The homepage contains extensive links across 74 HTML files:
- **External links**: ISMS-PUBLIC repository, GitHub project pages, blog posts
- **Internal links**: Navigation between pages, anchor links, image references
- **ISMS references**: Critical links to policy documents (issue #424 addresses this)
- **Social media**: LinkedIn, GitHub profiles, project links

Link rot is a real problem, especially for:
- References to ISMS policies in the public repository
- Links to specific sections in markdown files (anchor links)
- External blog post references
- Project documentation URLs

## ✅ Acceptance Criteria

- [ ] Install link checker tool (lychee or linkchecker) in copilot-setup-steps.yml
- [ ] Configure to check both internal and external links
- [ ] Add configuration to skip known problematic domains (rate-limited sites)
- [ ] Verify Copilot can run link checks during its work
- [ ] Keep permissions minimal (`contents: read` only)
- [ ] Test workflow via workflow_dispatch
- [ ] Document configuration choices in PR description

## 🛠️ Implementation Guidance

### Files to Modify
- `.github/workflows/copilot-setup-steps.yml` - Add link checker installation
- `.lycheeignore` or `lychee.toml` (NEW) - Configuration file

### Approach

**Option 1: Using lychee (Recommended - Fast, Rust-based)**
```yaml
- name: Install lychee Link Checker
  run: |
    wget -qO- https://github.com/lycheeverse/lychee/releases/latest/download/lychee-x86_64-unknown-linux-gnu.tar.gz | tar -xz
    sudo mv lychee /usr/local/bin/
    lychee --version
```

**Option 2: Using linkchecker (Python-based)**
```yaml
- name: Install linkchecker
  run: |
    pip install linkchecker
    linkchecker --version
```

**Recommended**: Use lychee for speed and modern features (parallel checking, markdown support, retry logic)

### Configuration File: lychee.toml
```toml
# Maximum number of concurrent requests
max_concurrency = 10

# Accept HTTP status codes as valid
accept = [200, 201, 204, 301, 302, 307, 308, 429]

# Exclude specific URLs or patterns
exclude = [
  # Rate-limited sites
  'https://www.linkedin.com/.*',
  # Local testing
  'http://localhost.*',
  # Placeholder URLs
  'https://example.com.*'
]

# Include email links
include_mail = false

# Timeout per request (seconds)
timeout = 20

# Number of retries per request
max_retries = 3
```

### Sample Link Statistics (from analysis)
- `black-trigram-docs.html`: 141 HTTP references
- `black-trigram-docs_ko.html`: 151 HTTP references
- `blog-cia-architecture.html`: 40 HTTP references
- Average per file: ~50-60 links

### Example Usage by Copilot
```bash
# Check all HTML files
lychee "*.html"

# Check specific file
lychee index.html

# Check with custom config
lychee --config lychee.toml .

# Check only internal links
lychee --offline "*.html"

# Generate report
lychee "*.html" --format markdown --output link-report.md
```

### Testing Steps
1. Add lychee installation to copilot-setup-steps.yml
2. Create lychee.toml configuration file
3. Commit to feature branch
4. Run workflow via workflow_dispatch
5. Verify lychee can check a sample HTML file
6. Review output for any broken links

## 🔗 Related Resources

- [lychee Documentation](https://github.com/lycheeverse/lychee)
- [linkchecker Documentation](https://linkchecker.github.io/linkchecker/)
- Related Issue: #424 (ISMS Reference Verification)
- [W3C Link Checker](https://validator.w3.org/checklink)

## 📊 Metadata

**Repository Stats:**
- 74 HTML files with extensive linking
- ~50-60 HTTP references per file average
- Critical ISMS policy links to GitHub
- Multiple language versions (_sv, _ko suffixes)

**Link Categories:**
- Internal navigation links
- ISMS policy references (GitHub)
- Project links (CIA, Black Trigram, Compliance Manager)
- Blog post cross-references
- Social media profiles

**Priority:** Medium  
**Effort:** Small (1 hour)  
**Impact:** Prevents broken links, improves user experience

**Suggested Labels:** `enhancement`, `priority:medium`, `size:small`, `quality`, `copilot-enhancement`

## 💡 Why This Matters

**For a consulting company website**, broken links to:
- ISMS policies = Loss of credibility
- Project demos = Missed business opportunities
- Blog posts = Poor SEO ranking
- Documentation = Support burden

**Copilot benefit**: Can validate links before committing content changes, catching issues during development rather than after deployment.

## 🔄 Related Work

This issue complements #424 (ISMS Reference Verification) by providing automated tooling to verify the corrected links remain functional over time.

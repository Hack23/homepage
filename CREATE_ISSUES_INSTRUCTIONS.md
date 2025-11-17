# How to Create the 5 GitHub Issues

The file `ISSUES_TO_CREATE.md` contains detailed specifications for 5 issues to be assigned to the UI Enhancement Specialist agent.

## Quick Creation Methods

### Option 1: GitHub Web Interface (Recommended)

1. Go to https://github.com/Hack23/homepage/issues/new
2. Copy the title and body for each issue from `ISSUES_TO_CREATE.md`
3. Add the specified labels
4. Click "Submit new issue"
5. Repeat for all 5 issues

### Option 2: GitHub CLI (Automated)

If you have GitHub CLI authenticated, run these commands:

```bash
# Issue 1: Homepage Card Layouts
gh issue create \
  --repo Hack23/homepage \
  --title "🎨 Fix Unbalanced Card Layouts on Homepage (index.html)" \
  --label "type:improvement,domain:ui-ux,domain:frontend,priority:high,size:medium" \
  --body "$(awk '/^## Issue 1:/,/^---$/' ISSUES_TO_CREATE.md | sed '1d;$d')"

# Issue 2: Blog Page Card Layouts
gh issue create \
  --repo Hack23/homepage \
  --title "🎨 Fix Unbalanced Card Layouts on Blog Page (blog.html)" \
  --label "type:improvement,domain:ui-ux,domain:frontend,domain:content,priority:high,size:medium" \
  --body "$(awk '/^## Issue 2:/,/^---$/' ISSUES_TO_CREATE.md | sed '1d;$d')"

# Issue 3: Sitemap Enhancement
gh issue create \
  --repo Hack23/homepage \
  --title "🗺️ Enhance Sitemap.xml Structure and Update Metadata" \
  --label "type:improvement,domain:seo,domain:infrastructure,priority:medium,size:small" \
  --body "$(awk '/^## Issue 3:/,/^---$/' ISSUES_TO_CREATE.md | sed '1d;$d')"

# Issue 4: SEO Structured Data
gh issue create \
  --repo Hack23/homepage \
  --title "🔍 Improve SEO with Enhanced Structured Data (Schema.org)" \
  --label "type:improvement,domain:seo,domain:frontend,priority:medium,size:medium" \
  --body "$(awk '/^## Issue 4:/,/^---$/' ISSUES_TO_CREATE.md | sed '1d;$d')"

# Issue 5: Responsive Grid Consistency
gh issue create \
  --repo Hack23/homepage \
  --title "📱 Improve Responsive Card Grid and Spacing Consistency" \
  --label "type:improvement,domain:ui-ux,domain:frontend,domain:accessibility,priority:high,size:medium" \
  --body "$(awk '/^## Issue 5:/,/^---$/' ISSUES_TO_CREATE.md | sed '1d;$d')"
```

### Option 3: API Script

See the example Node.js script in the repository for programmatic creation using the GitHub REST API.

## Issue Summary

| # | Title | Priority | Effort | Labels |
|---|-------|----------|--------|--------|
| 1 | Fix Unbalanced Card Layouts on Homepage | High | M (4-6h) | type:improvement, domain:ui-ux, domain:frontend, priority:high, size:medium |
| 2 | Fix Unbalanced Card Layouts on Blog Page | High | M (4-6h) | type:improvement, domain:ui-ux, domain:frontend, domain:content, priority:high, size:medium |
| 3 | Enhance Sitemap.xml Structure | Medium | S (2-3h) | type:improvement, domain:seo, domain:infrastructure, priority:medium, size:small |
| 4 | Improve SEO with Enhanced Structured Data | Medium | M (4-6h) | type:improvement, domain:seo, domain:frontend, priority:medium, size:medium |
| 5 | Improve Responsive Card Grid Consistency | High | M (4-6h) | type:improvement, domain:ui-ux, domain:frontend, domain:accessibility, priority:high, size:medium |

All issues are documented with measured baseline metrics, clear acceptance criteria, implementation guidance, and WCAG 2.1 AA compliance requirements.

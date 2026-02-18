# Quick Start: Release Workflow

**Ready to create your first release?** Follow these simple steps.

## Option 1: Tag-Based Release (Recommended)

```bash
# 1. Make sure you're on master and up to date
git checkout master
git pull origin master

# 2. Create and push a tag
git tag v1.0.0
git push origin v1.0.0

# 3. That's it! The workflow will:
#    - Generate documentation
#    - Create release with attestations
#    - Deploy to GitHub Pages
```

## Option 2: Manual Release via GitHub UI

1. Go to **Actions** tab
2. Click **Build, Attest and Release** workflow
3. Click **Run workflow** button
4. Enter version (e.g., `v1.0.0`)
5. Select if pre-release
6. Click **Run workflow**

## What Happens Next?

The workflow will automatically:

1. **📊 Generate Reports** (5-10 minutes)
   - HTML validation
   - Lighthouse audits
   - Accessibility compliance
   - Security summaries

2. **📦 Build Package** (2-3 minutes)
   - Minify HTML/CSS/JS
   - Create ZIP archive
   - Generate SBOM
   - Create attestations

3. **🚀 Deploy** (2-3 minutes)
   - Create GitHub Release
   - Attach all artifacts
   - Deploy to GitHub Pages
   - Update documentation

**Total time**: ~10-15 minutes

## Where to Find Your Release

- **GitHub Release**: https://github.com/Hack23/homepage/releases
- **GitHub Pages**: https://hack23.github.io/homepage/
- **Documentation**: In the `docs/` directory
- **S3/CloudFront**: Deployed automatically by main.yml on master

## Verify Your Release

```bash
# Verify build attestation
gh attestation verify homepage-v1.0.0.zip --owner Hack23

# View SBOM
gh release download v1.0.0 -R Hack23/homepage -p "*.spdx.json"
cat homepage-v1.0.0.spdx.json | jq .packages[].name
```

## Versioning Guide

Use [Semantic Versioning](https://semver.org/):

- `v1.0.0` - First production release
- `v1.1.0` - New feature (new page, service, blog post)
- `v1.1.1` - Bug fix (typo, broken link)
- `v2.0.0` - Major change (redesign, restructure)

## Pre-Release Testing

Test before going live:

```bash
# Create a release candidate
git tag v1.0.0-rc.1
git push origin v1.0.0-rc.1

# Test it thoroughly, then create final release
git tag v1.0.0
git push origin v1.0.0
```

## Need Help?

- **Full Documentation**: `docs/WORKFLOW_DOCUMENTATION.md`
- **Implementation Details**: `RELEASE_WORKFLOW_IMPLEMENTATION.md`
- **View Documentation**: Open `docs/index.html` in your browser
- **Issues**: Open an issue on GitHub

---

**That's it!** You're ready to create releases with full supply chain security. 🎉

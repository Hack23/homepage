# Release Workflow Documentation

This document describes the automated release workflow for the Hack23 homepage.

## Overview

The release workflow implements a comprehensive CI/CD pipeline with:
- 🔐 **Supply Chain Security**: SLSA Build Level 3 attestations
- 📦 **SBOM**: Software Bill of Materials generation
- 📚 **Documentation as Code**: Automated report generation
- 🌐 **Dual Deployment**: GitHub Pages + S3/CloudFront
- ✅ **Quality Assurance**: Automated validation and audits

## Workflow Structure

### 1. Prepare Job
**Purpose**: Generate documentation and prepare release artifacts

**Actions**:
- Extract version from git tag or workflow input
- Generate HTML validation reports
- Run Lighthouse audits (performance, accessibility, SEO)
- Create accessibility compliance reports (WCAG 2.1 AA)
- Generate security report summaries
- Commit all documentation to `docs/` directory

**Documentation Generated**:
- `docs/html-validation.txt` - HTML validation results
- `docs/lighthouse-*.html` - Lighthouse audit reports
- `docs/accessibility-report.html` - WCAG 2.1 AA compliance
- `docs/security-report.html` - Security scan summary
- `docs/RELEASE_SUMMARY.md` - Release metadata
- `docs/version.txt` - Version and timestamp

### 2. Build Job
**Purpose**: Create release package with supply chain security attestations

**Actions**:
- Minify HTML, CSS, and JavaScript
- Create ZIP archive of website
- Generate SBOM in SPDX format
- Create build provenance attestation
- Create SBOM attestation
- Upload all artifacts

**Artifacts Created**:
- `homepage-vX.Y.Z.zip` - Complete website package
- `homepage-vX.Y.Z.spdx.json` - Software Bill of Materials
- `homepage-vX.Y.Z.zip.intoto.jsonl` - Build provenance attestation
- `homepage-vX.Y.Z.spdx.json.intoto.jsonl` - SBOM attestation

### 3. Release Job
**Purpose**: Publish release and deploy to production

**Actions**:
- Download all artifacts
- Generate release notes with release-drafter
- Create GitHub Release with all artifacts
- Deploy to GitHub Pages (backup)
- Create deployment summary

**Deployment Targets**:
- **GitHub Pages**: `https://hack23.github.io/homepage/` (automated backup)
- **S3/CloudFront**: `https://hack23.com` (via main.yml workflow on master)

## Triggering a Release

### Method 1: Create and Push a Tag
```bash
# Create a tag
git tag v1.0.0

# Push the tag to trigger release
git push origin v1.0.0
```

### Method 2: Manual Workflow Dispatch
1. Go to Actions tab in GitHub
2. Select "Build, Attest and Release" workflow
3. Click "Run workflow"
4. Enter version (e.g., `v1.0.0`)
5. Select if pre-release
6. Click "Run workflow"

## Versioning Strategy

Follow Semantic Versioning (SemVer):
- **Major (vX.0.0)**: Breaking changes, major redesigns
- **Minor (v1.X.0)**: New features, new pages, significant enhancements
- **Patch (v1.0.X)**: Bug fixes, typo corrections, minor updates

Examples:
- `v1.0.0` - Initial release
- `v1.1.0` - Add new blog post or service page
- `v1.1.1` - Fix typo or broken link
- `v2.0.0` - Complete redesign

## Supply Chain Security

### Verifying Release Artifacts

```bash
# Install GitHub CLI if not already installed
# https://cli.github.com/

# Verify the build provenance attestation
gh attestation verify homepage-v1.0.0.zip --owner Hack23

# View the SBOM
gh release download v1.0.0 -R Hack23/homepage -p "*.spdx.json"
cat homepage-v1.0.0.spdx.json | jq
```

### SLSA Build Level 3

The release workflow achieves SLSA Build Level 3 by:
- ✅ **Build as Code**: Workflow defined in version control
- ✅ **Provenance**: Cryptographic attestation of build process
- ✅ **Isolation**: Jobs run in isolated environments
- ✅ **Parameterless**: Build is reproducible from source
- ✅ **Ephemeral**: Build environment is ephemeral
- ✅ **Non-falsifiable**: Uses GitHub's OIDC for signing

## Documentation as Code

All documentation is automatically generated and committed to the repository:

```
docs/
├── index.html                    # Documentation viewer
├── README.md                     # This file
├── VERSION.txt                   # Current version
├── version.txt                   # Release metadata
├── html-validation.txt           # HTML validation results
├── lighthouse-*.html             # Lighthouse reports
├── lighthouse-*.json             # Lighthouse data
├── accessibility-report.html     # WCAG 2.1 AA compliance
├── security-report.html          # Security summary
└── RELEASE_SUMMARY.md            # Release overview
```

## Workflow Permissions

The workflow follows the principle of least privilege:

```yaml
# Top-level: read-only by default
permissions: read-all

# Prepare job: write to commit docs
permissions:
  contents: write

# Build job: attestation generation
permissions:
  contents: read
  id-token: write
  attestations: write

# Release job: create releases
permissions:
  contents: write
  id-token: write
```

## Security Features

1. **Step Security Harden Runner**: Audits egress traffic
2. **Pinned Action Versions**: SHA-pinned for supply chain security
3. **Minimal Permissions**: Principle of least privilege
4. **SBOM Generation**: Complete dependency inventory
5. **Attestations**: Cryptographic proof of build process
6. **Code Scanning**: Automated vulnerability detection

## Integration with Existing Workflows

The release workflow complements the existing `main.yml` workflow:

- **main.yml**: Continuous deployment on every push to master
  - Deploys to S3/CloudFront
  - Runs Lighthouse audits
  - Performs security scans (OWASP ZAP)

- **release.yml**: Versioned releases with attestations
  - Creates tagged releases
  - Generates SBOM and attestations
  - Commits documentation
  - Deploys to GitHub Pages

## Troubleshooting

### Release Workflow Fails

1. Check workflow run logs in Actions tab
2. Verify tag format matches `v*` pattern
3. Ensure GITHUB_TOKEN has necessary permissions
4. Check artifact upload/download steps

### Documentation Not Generated

1. Verify npm packages are installed correctly
2. Check HTML validation step logs
3. Ensure docs/ directory is not in .gitignore

### Attestation Generation Fails

1. Verify `id-token: write` permission is set
2. Check GitHub's OIDC configuration
3. Ensure artifact exists before attestation

## Best Practices

1. **Always test in a feature branch first**
2. **Use pre-release tags for testing** (e.g., `v1.0.0-beta.1`)
3. **Review generated documentation before final release**
4. **Verify attestations after release**
5. **Update CHANGELOG.md for major releases**

## Example Release Process

```bash
# 1. Prepare for release
git checkout master
git pull origin master

# 2. Test the release workflow with a pre-release tag
git tag v1.0.0-rc.1
git push origin v1.0.0-rc.1

# 3. Verify the release in GitHub
# - Check Actions tab for workflow success
# - Review generated documentation in docs/
# - Verify attestations

# 4. Create final release
git tag v1.0.0
git push origin v1.0.0

# 5. Verify deployment
# - Check https://hack23.github.io/homepage/
# - Check https://hack23.com (after main.yml runs)
```

## References

- [SLSA Framework](https://slsa.dev/)
- [SPDX SBOM](https://spdx.dev/)
- [GitHub Attestations](https://docs.github.com/en/actions/security-guides/using-artifact-attestations)
- [Semantic Versioning](https://semver.org/)
- [Release Drafter](https://github.com/release-drafter/release-drafter)

## Support

For issues or questions:
- Open an issue in the repository
- Review workflow logs in Actions tab
- Consult the main README.md

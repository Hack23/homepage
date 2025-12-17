# GitHub Actions Workflow Caching Guide

## Overview

This document describes the comprehensive caching strategy implemented across all GitHub Actions workflows in this repository to improve performance, resilience, and reduce costs.

## Cache Strategy

All workflows use `actions/cache@9255dc7a253b0ccc959486e2bca901246202afeb # v5.0.1` for caching.

### Cached Resources

#### 1. APT Packages (`/var/cache/apt/archives`)
- **Purpose**: Cache system packages installed via `apt-get`
- **Key Pattern**: `${{ runner.os }}-apt-${{ hashFiles('**/.github/workflows/<workflow-name>.yml') }}`
- **Restore Keys**: `${{ runner.os }}-apt-`
- **Used in**: All workflows (main.yml, quality-checks.yml, pullrequest.yml, scorecards.yml, dependency-review.yml)

#### 2. NPM Packages (`~/.npm`)
- **Purpose**: Cache Node.js packages installed globally or locally
- **Key Pattern**: `${{ runner.os }}-npm-<tool>-${{ hashFiles('**/package-lock.json') }}`
- **Restore Keys**: 
  - `${{ runner.os }}-npm-<tool>-`
  - `${{ runner.os }}-npm-`
- **Used in**: 
  - main.yml (minify tools)
  - quality-checks.yml (htmlhint, linkinator)
  - pullrequest.yml (validator, minify)

#### 3. Docker Layers (`/tmp/.buildx-cache`)
- **Purpose**: Cache Docker image layers for faster builds
- **Key Pattern**: `${{ runner.os }}-docker-${{ github.sha }}`
- **Restore Keys**: `${{ runner.os }}-docker-`
- **Used in**: main.yml (ZAP scanner image)

## Cache Key Design Principles

### 1. OS-Specific Keys
All cache keys include `${{ runner.os }}` to prevent cross-platform cache collisions:
```yaml
key: ${{ runner.os }}-apt-...
```

### 2. Content-Based Hashing
Keys use `hashFiles()` to detect changes:
- Workflow files for apt caches: `${{ hashFiles('**/.github/workflows/main.yml') }}`
- Package lock files for npm caches: `${{ hashFiles('**/package-lock.json') }}`

### 3. Hierarchical Restore Keys
Multiple restore-keys provide fallback options:
```yaml
restore-keys: |
  ${{ runner.os }}-npm-minify-
  ${{ runner.os }}-npm-
```
This allows:
- First: Match exact tool and lock file hash
- Second: Match any tool with same lock file
- Third: Match any npm cache

### 4. Scoped Naming
Tool-specific identifiers prevent cache conflicts:
- `npm-htmlhint` for HTMLHint
- `npm-linkinator` for Linkinator
- `npm-minify` for minification tools
- `npm-validator` for HTML validator

## Implementation Examples

### APT Package Cache
```yaml
- name: Cache apt packages
  uses: actions/cache@9255dc7a253b0ccc959486e2bca901246202afeb # v5.0.1
  with:
    path: /var/cache/apt/archives
    key: ${{ runner.os }}-apt-${{ hashFiles('**/.github/workflows/main.yml') }}
    restore-keys: |
      ${{ runner.os }}-apt-
```

### NPM Package Cache
```yaml
- name: Cache npm dependencies
  uses: actions/cache@9255dc7a253b0ccc959486e2bca901246202afeb # v5.0.1
  with:
    path: ~/.npm
    key: ${{ runner.os }}-npm-minify-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-npm-minify-
      ${{ runner.os }}-npm-
```

### Docker Layer Cache
```yaml
- name: Cache Docker layers
  uses: actions/cache@9255dc7a253b0ccc959486e2bca901246202afeb # v5.0.1
  with:
    path: /tmp/.buildx-cache
    key: ${{ runner.os }}-docker-${{ github.sha }}
    restore-keys: |
      ${{ runner.os }}-docker-
```

## Performance Benefits

### Expected Improvements
1. **Speed**: 20-40% faster workflow execution
   - Skip npm downloads: ~5-15s per workflow
   - Skip apt downloads: ~10-30s per workflow
   - Skip Docker pulls: ~30-60s for ZAP scanner

2. **Resilience**: Reduced external dependency failures
   - Works when npm registry is slow/unavailable
   - Works when apt repositories are slow/unavailable
   - Reduces network-related failures

3. **Cost**: Lower GitHub Actions usage
   - Cache hits: ~1-2s vs. full downloads
   - Estimated 10-20% reduction in workflow time
   - Lower network bandwidth consumption

## Workflow-Specific Details

### main.yml (Verify and Deploy)
**Caches**: APT, NPM, Docker
- APT: System dependencies
- NPM: Minification tools
- Docker: ZAP security scanner image

### quality-checks.yml
**Caches**: NPM (2 jobs), APT
- Job 1 (html-validation): NPM cache for HTMLHint
- Job 2 (link-checker): NPM cache for Linkinator + APT cache for jq

### pullrequest.yml (Verify Pull Request)
**Caches**: APT, NPM
- APT: HTML validator dependencies
- NPM: Validator and minify tools

### scorecards.yml (Supply-Chain Security)
**Caches**: APT
- APT: Scorecard analysis dependencies

### dependency-review.yml
**Caches**: APT
- APT: Dependency review dependencies

## Monitoring and Optimization

### Cache Hit Rates
Monitor cache performance in workflow logs:
- Look for "Cache restored from key" messages
- Compare workflow times before/after caching
- Track cache size growth over time

### Cache Size Limits
GitHub Actions cache has limits:
- Per repository: 10 GB total
- Per cache entry: 10 GB max
- Unused caches expire after 7 days

### Troubleshooting

#### Cache Miss
If caches aren't hitting:
1. Check cache key matches restore-keys pattern
2. Verify cached paths exist and are populated
3. Ensure workflow hasn't changed (invalidates apt cache)

#### Performance Not Improved
If no speed improvement:
1. Check cache is actually being used (workflow logs)
2. Verify network isn't the bottleneck elsewhere
3. Consider if packages are already cached by action maintainers

#### Cache Size Too Large
If hitting size limits:
1. Exclude unnecessary paths
2. Use more specific cache keys
3. Consider shorter cache retention

## Best Practices

1. **Always version cache action**: Use SHA pinning for security
   ```yaml
   uses: actions/cache@9255dc7a253b0ccc959486e2bca901246202afeb # v5.0.1
   ```

2. **Place cache steps early**: Before package installation steps
   ```yaml
   - name: Checkout
   - name: Cache npm    # ← Cache before install
   - name: Install npm
   ```

3. **Use hierarchical keys**: Enable partial cache matches
   ```yaml
   restore-keys: |
     ${{ runner.os }}-npm-tool-
     ${{ runner.os }}-npm-
   ```

4. **Scope cache keys**: Prevent conflicts between tools
   ```yaml
   key: ${{ runner.os }}-npm-htmlhint-...  # Not just npm-
   ```

5. **Monitor cache usage**: Check GitHub Actions cache dashboard regularly

## Future Enhancements

### Potential Improvements
1. **Python pip cache**: If pip packages are added
   ```yaml
   path: ~/.cache/pip
   ```

2. **Cargo cache**: If Rust tools are added
   ```yaml
   path: ~/.cargo
   ```

3. **Go module cache**: If Go tools are added
   ```yaml
   path: ~/go/pkg/mod
   ```

4. **Action-specific caches**: Some actions support built-in caching
   - setup-node has `cache: 'npm'`
   - setup-python has `cache: 'pip'`

### Monitoring Metrics
Track these metrics over time:
- Average workflow duration (before/after caching)
- Cache hit rate percentage
- Cache size usage vs. limits
- Network failure rate reduction

## References

- [GitHub Actions Cache Documentation](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows)
- [actions/cache GitHub Repository](https://github.com/actions/cache)
- [Cache Usage Limits](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows#usage-limits-and-eviction-policy)

## Changelog

### 2025-12-16: Initial Implementation
- Added APT caching to all workflows
- Added NPM caching to main.yml, quality-checks.yml, pullrequest.yml
- Added Docker layer caching to main.yml
- Established cache key patterns and best practices
- Created comprehensive documentation

---

**Document Control:**
- **Approved by**: DevOps Team
- **Distribution**: Internal Development Team
- **Classification**: Public (Technical Documentation)
- **Effective Date**: 2025-12-16
- **Next Review**: 2026-03-16 (Quarterly)

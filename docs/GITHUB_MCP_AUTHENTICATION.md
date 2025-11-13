# GitHub MCP Server Authentication Setup Guide

**Document Version**: 1.0  
**Last Updated**: November 13, 2025  
**Repository**: Hack23/homepage

---

## Overview

The GitHub MCP (Model Context Protocol) server provides tools for programmatic interaction with GitHub repositories, including creating issues, pull requests, and managing repository content. However, these tools require proper authentication to function.

This guide explains how to set up authentication for GitHub MCP server tools in different contexts.

---

## Table of Contents

1. [Understanding the Authentication Requirement](#understanding-the-authentication-requirement)
2. [Authentication Methods](#authentication-methods)
3. [Local Development Setup](#local-development-setup)
4. [GitHub Actions Setup](#github-actions-setup)
5. [Copilot Agent Environment Limitations](#copilot-agent-environment-limitations)
6. [Troubleshooting](#troubleshooting)
7. [Security Best Practices](#security-best-practices)

---

## Understanding the Authentication Requirement

### Why Authentication is Required

GitHub MCP server tools need authentication to:
- **Create/modify issues**: Requires write access to repository
- **Create/update pull requests**: Requires write access to repository
- **Manage labels and milestones**: Requires write access to repository metadata
- **Access private repositories**: Requires read access permissions

### Error Messages

When authentication is missing or invalid, you'll see errors like:

```
Tool call failed: MCP error -32603: Failed to create issue: Requires authentication
GitHubAuthenticationError: Requires authentication
```

---

## Authentication Methods

### Method 1: GitHub Personal Access Token (PAT)

**Best for**: Local development, scripts, CI/CD pipelines

#### Creating a Personal Access Token

1. **Navigate to GitHub Settings**
   - Go to https://github.com/settings/tokens
   - Or: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)

2. **Generate New Token**
   - Click "Generate new token" → "Generate new token (classic)"
   - Give it a descriptive name: e.g., "GitHub MCP Server - Homepage"
   - Set expiration: Choose appropriate duration (30-90 days recommended)

3. **Select Permissions (Scopes)**

   For **issue creation** (minimum permissions):
   ```
   ✅ repo
      ✅ repo:status
      ✅ repo_deployment
      ✅ public_repo (for public repos only)
      ✅ repo:invite
      ✅ security_events
   ```

   For **full repository management**:
   ```
   ✅ repo (full access)
   ✅ workflow (if managing GitHub Actions)
   ✅ write:packages (if managing packages)
   ✅ read:org (if working with organization repos)
   ```

4. **Generate and Copy Token**
   - Click "Generate token"
   - **IMPORTANT**: Copy the token immediately - you won't be able to see it again!
   - Format: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

#### Storing the Token Securely

**DO NOT** commit tokens to git or save in plain text files tracked by version control!

**Option A: Environment Variable**
```bash
# Add to ~/.bashrc, ~/.zshrc, or ~/.profile
export GITHUB_TOKEN="ghp_your_token_here"

# Or set for current session only
export GITHUB_TOKEN="ghp_your_token_here"
```

**Option B: GitHub CLI**
```bash
# Authenticate via GitHub CLI (recommended)
gh auth login

# This stores the token securely in the system keychain
```

**Option C: .env File (for local development)**
```bash
# Create .env file (ensure it's in .gitignore!)
echo "GITHUB_TOKEN=ghp_your_token_here" > .env

# Load in your application
source .env
```

---

### Method 2: GitHub App

**Best for**: Production applications, organization-wide tools

#### Creating a GitHub App

1. **Register GitHub App**
   - Go to https://github.com/settings/apps
   - Click "New GitHub App"

2. **Configure Permissions**
   - **Repository permissions**:
     - Issues: Read & Write
     - Pull requests: Read & Write
     - Contents: Read (or Read & Write)
     - Metadata: Read

3. **Install App**
   - After creation, install the app to your repository/organization
   - Note the Installation ID

4. **Generate Private Key**
   - In app settings, generate a private key
   - Download and store securely

5. **Authentication Flow**
   ```javascript
   // Example: Generate installation access token
   const jwt = generateJWT(appId, privateKey);
   const installationToken = await getInstallationToken(jwt, installationId);
   ```

---

### Method 3: GitHub Actions (GITHUB_TOKEN)

**Best for**: Automated workflows within GitHub Actions

#### Default GITHUB_TOKEN

GitHub Actions automatically provides a `GITHUB_TOKEN`:

```yaml
jobs:
  create-issues:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Use GitHub Token
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # Token is automatically available
          echo "Token is set"
```

#### GITHUB_TOKEN Permissions

Default permissions are **read-only**. To enable issue creation:

```yaml
permissions:
  issues: write      # Required for creating/editing issues
  contents: read     # Required for reading repository
  pull-requests: write  # Required for creating/editing PRs
```

**Full example**:
```yaml
name: Create Issues via MCP
on:
  workflow_dispatch:

permissions:
  issues: write
  contents: read
  
jobs:
  create-issues:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
      
      - name: Install MCP Server
        run: npm install -g @modelcontextprotocol/server-github
      
      - name: Create Issues
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # Use MCP server tools here
          # Token is automatically authenticated
```

---

## Local Development Setup

### Step-by-Step Configuration

#### 1. Install GitHub CLI (Recommended)

**macOS**:
```bash
brew install gh
```

**Linux**:
```bash
# Debian/Ubuntu
sudo apt install gh

# Fedora
sudo dnf install gh

# Arch
sudo pacman -S github-cli
```

**Windows**:
```powershell
winget install --id GitHub.cli
# or
choco install gh
```

#### 2. Authenticate GitHub CLI

```bash
# Interactive authentication (recommended)
gh auth login

# Follow prompts:
# - Choose GitHub.com
# - Choose HTTPS or SSH
# - Authenticate with browser or token
# - Grant permissions
```

#### 3. Verify Authentication

```bash
# Check authentication status
gh auth status

# Test API access
gh api user
```

#### 4. Configure MCP Server

Create configuration file for MCP server:

**~/.config/mcp/github.json**:
```json
{
  "github": {
    "token": "${GITHUB_TOKEN}",
    "owner": "Hack23",
    "repo": "homepage"
  }
}
```

#### 5. Set Environment Variable

```bash
# Get token from GitHub CLI
export GITHUB_TOKEN=$(gh auth token)

# Verify it's set
echo $GITHUB_TOKEN | head -c 20
```

---

## GitHub Actions Setup

### Example Workflow for Issue Creation

Create `.github/workflows/create-issues-mcp.yml`:

```yaml
name: Create Issues via GitHub MCP Server

on:
  workflow_dispatch:
    inputs:
      issue_title:
        description: 'Issue title'
        required: true
      issue_body:
        description: 'Issue body'
        required: true

permissions:
  issues: write
  contents: read

jobs:
  create-issue:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
      
      - name: Install MCP CLI (if available)
        run: |
          # Install MCP tools
          npm install -g @modelcontextprotocol/cli
      
      - name: Create Issue
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # Use GitHub CLI as fallback
          gh issue create \
            --title "${{ github.event.inputs.issue_title }}" \
            --body "${{ github.event.inputs.issue_body }}" \
            --repo ${{ github.repository }}
```

### Using Custom PAT in Actions

If default `GITHUB_TOKEN` lacks permissions:

1. **Create PAT** (as described above)
2. **Add as Repository Secret**:
   - Go to repository Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Name: `GH_PAT` (or any name)
   - Value: Your PAT

3. **Use in Workflow**:
```yaml
- name: Create Issue with PAT
  env:
    GITHUB_TOKEN: ${{ secrets.GH_PAT }}
  run: |
    # Your commands here
```

---

## Copilot Agent Environment Limitations

### Why Copilot Agent Cannot Create Issues Directly

The GitHub Copilot coding agent runs in an **ephemeral, sandboxed environment** with the following limitations:

1. **No Persistent Authentication**
   - Copilot agent doesn't have access to persistent GitHub credentials
   - Cannot access GitHub CLI authentication
   - Cannot access environment variables set outside its session

2. **Minimal Permissions**
   - Agent receives minimal permissions for its work
   - Issue creation requires elevated permissions not granted to agent

3. **Security Isolation**
   - By design: agents cannot perform actions that require authentication
   - Prevents potential misuse or credential leakage

### Current Error Explanation

When Copilot agent tries to use GitHub MCP server:

```
Tool call failed: MCP error -32603: Failed to create issue: Requires authentication
GitHubAuthenticationError: Requires authentication
```

This is **expected behavior** because:
- Agent environment lacks `GITHUB_TOKEN` variable
- Agent cannot authenticate via GitHub CLI
- MCP server tools require explicit authentication

### Workarounds for Copilot Agent

#### Option 1: Create Issue Templates (Recommended)

Instead of creating issues directly, Copilot can:

1. **Generate issue content** with complete details
2. **Save to repository** as markdown files
3. **User creates issues** manually or via script

**Example**:
```bash
# Copilot creates: docs/issues/issue-001.md
# User runs:
gh issue create --title "$(head -1 docs/issues/issue-001.md)" \
  --body-file docs/issues/issue-001.md
```

#### Option 2: Workflow Trigger

Copilot can create a trigger file that runs a GitHub Action:

1. Copilot creates: `.github/create-issues.json`
2. Workflow triggers on push
3. Workflow creates issues with proper authentication

**Example workflow**:
```yaml
name: Auto-create Issues
on:
  push:
    paths:
      - '.github/create-issues.json'

permissions:
  issues: write

jobs:
  create-issues:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Create Issues from JSON
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # Parse JSON and create issues
          cat .github/create-issues.json | jq -r '.[] | 
            gh issue create --title .title --body .body'
```

#### Option 3: Manual Creation with CLI

Copilot provides complete issue content, user runs:

```bash
# Copy issue content from Copilot's output
gh issue create \
  --title "🔧 Add HTML validation tools" \
  --body "$(cat /tmp/issue-content.md)" \
  --label "enhancement" \
  --assignee "@me"
```

---

## Troubleshooting

### Common Issues and Solutions

#### 1. "Requires authentication" Error

**Problem**: MCP server cannot authenticate

**Solutions**:
```bash
# Check if token is set
echo $GITHUB_TOKEN

# If empty, set it:
export GITHUB_TOKEN=$(gh auth token)

# Or create new PAT and set:
export GITHUB_TOKEN="ghp_your_token_here"
```

#### 2. "Bad credentials" Error

**Problem**: Token is invalid or expired

**Solutions**:
```bash
# Check token validity
gh auth status

# Refresh authentication
gh auth refresh -h github.com -s repo,write:org

# Or generate new PAT
```

#### 3. "Resource not accessible by integration"

**Problem**: Token lacks required permissions

**Solutions**:
- For PAT: Regenerate with `repo` scope
- For GITHUB_TOKEN: Add `permissions:` block to workflow
- For GitHub App: Update app permissions

#### 4. Token Not Found in Copilot Environment

**Problem**: Copilot agent cannot access credentials

**Solution**: This is **expected behavior**. Use workarounds:
- Create issue templates in repository
- Use workflow triggers
- Provide complete content for manual creation

---

## Security Best Practices

### ✅ DO

1. **Use minimal permissions**: Only grant scopes you need
2. **Set expiration dates**: Tokens should expire (30-90 days)
3. **Use environment variables**: Never hardcode tokens
4. **Add to .gitignore**: Ensure `.env` files are excluded
5. **Rotate regularly**: Generate new tokens periodically
6. **Use GitHub CLI**: Leverages system keychain for secure storage
7. **Monitor usage**: Check token usage in GitHub settings
8. **Revoke unused tokens**: Clean up old/unused tokens

### ❌ DON'T

1. **Never commit tokens**: Don't add tokens to git
2. **Don't share tokens**: Each user should have their own
3. **Don't use broad permissions**: Avoid `admin:*` unless necessary
4. **Don't log tokens**: Avoid printing tokens in logs
5. **Don't reuse tokens**: Use different tokens for different purposes
6. **Don't skip expiration**: Always set reasonable expiration

### .gitignore Entries

Ensure your `.gitignore` includes:

```gitignore
# Environment variables
.env
.env.local
.env.*.local

# GitHub tokens
.github-token
github-token.txt

# MCP configuration with secrets
.config/mcp/github.json
mcp-config.json
```

---

## Quick Reference

### Creating PAT for Issue Management

**Minimum scopes needed**:
```
✅ public_repo (for public repositories)
✅ repo (for private repositories)
```

**Commands**:
```bash
# Set token
export GITHUB_TOKEN="ghp_xxxxxxxxxxxx"

# Verify
gh auth status

# Use in scripts
gh issue create --title "Test" --body "Test issue"
```

### GitHub Actions Quick Setup

```yaml
permissions:
  issues: write
  contents: read

env:
  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Copilot Agent Workaround

```bash
# 1. Copilot creates: docs/issues/*.md
# 2. You run:
for file in docs/issues/*.md; do
  gh issue create --body-file "$file"
done
```

---

## Additional Resources

- [GitHub PAT Documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [GitHub Actions Permissions](https://docs.github.com/en/actions/security-guides/automatic-token-authentication)
- [GitHub CLI Manual](https://cli.github.com/manual/)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [GitHub API Authentication](https://docs.github.com/en/rest/overview/authenticating-to-the-rest-api)

---

## Summary

- **GitHub MCP server tools require authentication** to create/modify issues
- **Personal Access Tokens (PAT)** are the most common authentication method
- **GitHub Actions** can use `GITHUB_TOKEN` with proper permissions
- **Copilot agents** cannot authenticate directly - use workarounds
- **Security is paramount** - never commit tokens, use minimal permissions

For the **Hack23/homepage** repository specifically, the recommended approach is:
1. Copilot creates issue templates in `docs/issues/` directory
2. Maintainer reviews templates
3. Maintainer creates issues using `gh` CLI with proper authentication

This maintains security while enabling efficient issue creation.

---

**Document Maintained By**: Hack23 DevOps Team  
**Questions?** Create an issue or see CONTRIBUTING.md

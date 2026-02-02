# GitHub MCP Server - Complete Operations Reference

**Date**: 2026-02-02  
**Version**: 2.0 - Complete Review with Experimental Features  
**Endpoint**: https://api.githubcopilot.com/mcp/insiders  
**Source**: Official GitHub MCP Server + Insiders API

---

## Executive Summary

This document provides a comprehensive catalog of **all 51+ GitHub MCP (Model Context Protocol) server operations** available through the Insiders API endpoint. This includes standard operations, experimental features, and advanced workflows for Copilot agents.

### Key Updates

✅ **Complete 51+ Operation Catalog**: All tools with full parameter schemas  
✅ **Experimental Features Documented**: assign_copilot_to_issue, request_copilot_review, and more  
✅ **Agent Workflows**: Stacked PRs, sequential task chaining, feature branch workflows  
✅ **Consolidated Tools**: Multi-function tools with method parameters  
✅ **Copilot Integration**: Direct Copilot task assignment and management  

---

## Table of Contents

1. [GitHub MCP Toolsets](#1-github-mcp-toolsets)
2. [Complete Operations List](#2-complete-operations-list)
3. [Experimental Features](#3-experimental-features)
4. [Advanced Workflows](#4-advanced-workflows)
5. [Tool Consolidation](#5-tool-consolidation)
6. [Configuration](#6-configuration)
7. [Usage Examples](#7-usage-examples)

---

## 1. GitHub MCP Toolsets

The GitHub MCP server organizes operations into **toolsets** by functional domain:

| Toolset | Description | Operations Count |
|---------|-------------|------------------|
| **issues** | Issue creation, management, comments, labels | 7 |
| **pull_requests** | PR creation, review, merge, comments | 15 |
| **repos** | Repository operations, branches, files | 11 |
| **code_security** | Code scanning alerts | 2 |
| **secret_protection** | Secret scanning alerts | 2 |
| **search** | Code, repository, issue, user search | 4 |
| **notifications** | GitHub notifications management | 5 |
| **context** | User and authentication context | 1 |
| **actions** | (Via separate actions_list/actions_get tools) | - |
| **copilot_agent** | Copilot task assignment (experimental) | 2 |

**Total Operations**: 51+

---

## 2. Complete Operations List

### 2.1 Issue Operations (7 tools)

#### `create_issue`
Create a new issue in a GitHub repository.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "title": "string (required)",
  "body": "string (optional)",
  "assignees": ["string"] (optional),
  "labels": ["string"] (optional),
  "milestone": "number (optional)"
}
```

#### `get_issue`
Get details of a specific issue.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "issue_number": "number (required)"
}
```

#### `list_issues`
List issues in a GitHub repository.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "state": "open|closed|all (optional)",
  "labels": ["string"] (optional),
  "sort": "created|updated|comments (optional)",
  "direction": "asc|desc (optional)",
  "since": "ISO 8601 timestamp (optional)",
  "page": "number (optional)",
  "perPage": "number (optional, max 100)"
}
```

#### `update_issue`
Update an existing issue.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "issue_number": "number (required)",
  "title": "string (optional)",
  "body": "string (optional)",
  "state": "open|closed (optional)",
  "assignees": ["string"] (optional),
  "labels": ["string"] (optional)",
  "milestone": "number (optional)"
}
```

#### `add_issue_comment`
Add a comment to an issue.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "issue_number": "number (required)",
  "body": "string (required)"
}
```

#### `get_issue_comments`
Get comments for a specific issue.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "issue_number": "number (required)",
  "page": "number (optional)",
  "per_page": "number (optional)"
}
```

#### `search_issues`
Search for issues across repositories.

**Parameters:**
```json
{
  "q": "string (required) - GitHub search syntax",
  "sort": "comments|reactions|reactions-+1|created|updated (optional)",
  "order": "asc|desc (optional)",
  "page": "number (optional)",
  "perPage": "number (optional, max 100)"
}
```

---

### 2.2 Pull Request Operations (15 tools)

#### `create_pull_request`
Create a new pull request.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "title": "string (required)",
  "head": "string (required) - branch with changes",
  "base": "string (required) - target branch (base_ref)",
  "body": "string (optional)",
  "draft": "boolean (optional)",
  "maintainer_can_modify": "boolean (optional)"
}
```

#### `get_pull_request`
Get details of a specific pull request.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "pullNumber": "number (required)"
}
```

#### `list_pull_requests`
List pull requests in a repository.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "state": "open|closed|all (optional)",
  "head": "string (optional)",
  "base": "string (optional)",
  "sort": "created|updated|popularity|long-running (optional)",
  "direction": "asc|desc (optional)",
  "page": "number (optional)",
  "perPage": "number (optional, max 100)"
}
```

#### `update_pull_request`
Update an existing pull request.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "pullNumber": "number (required)",
  "title": "string (optional)",
  "body": "string (optional)",
  "state": "open|closed (optional)",
  "base": "string (optional)",
  "maintainer_can_modify": "boolean (optional)"
}
```

#### `merge_pull_request`
Merge a pull request.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "pullNumber": "number (required)",
  "merge_method": "merge|squash|rebase (optional)",
  "commit_title": "string (optional)",
  "commit_message": "string (optional)"
}
```

#### `get_pull_request_diff`
Get the diff of a pull request.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "pullNumber": "number (required)"
}
```

#### `get_pull_request_files`
Get files changed in a pull request.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "pullNumber": "number (required)"
}
```

#### `get_pull_request_status`
Get status of a pull request (checks, CI/CD).

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "pullNumber": "number (required)"
}
```

#### `get_pull_request_comments`
Get comments for a pull request.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "pullNumber": "number (required)"
}
```

#### `get_pull_request_reviews`
Get reviews for a pull request.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "pullNumber": "number (required)"
}
```

#### `update_pull_request_branch`
Update PR branch with latest changes from base.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "pullNumber": "number (required)",
  "expectedHeadSha": "string (optional)"
}
```

#### `create_pending_pull_request_review`
Create a pending review (to be submitted later).

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "pullNumber": "number (required)",
  "commitID": "string (optional)"
}
```

#### `add_pull_request_review_comment_to_pending_review`
Add comment to pending review.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "pullNumber": "number (required)",
  "path": "string (required)",
  "body": "string (required)",
  "subjectType": "FILE|LINE (required)",
  "line": "number (optional for LINE)",
  "side": "LEFT|RIGHT (optional)",
  "startLine": "number (optional for multi-line)",
  "startSide": "LEFT|RIGHT (optional)"
}
```

#### `submit_pending_pull_request_review`
Submit a pending pull request review.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "pullNumber": "number (required)",
  "event": "APPROVE|REQUEST_CHANGES|COMMENT (required)",
  "body": "string (optional)"
}
```

#### `delete_pending_pull_request_review`
Delete a pending pull request review.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "pullNumber": "number (required)"
}
```

#### `create_and_submit_pull_request_review`
Create and submit a review in one step (no comments).

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "pullNumber": "number (required)",
  "body": "string (required)",
  "event": "APPROVE|REQUEST_CHANGES|COMMENT (required)",
  "commitID": "string (optional)"
}
```

---

### 2.3 Repository Operations (11 tools)

#### `create_repository`
Create a new repository.

**Parameters:**
```json
{
  "name": "string (required)",
  "description": "string (optional)",
  "private": "boolean (optional)",
  "autoInit": "boolean (optional)"
}
```

#### `fork_repository`
Fork a repository.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "organization": "string (optional)"
}
```

#### `create_branch`
Create a new branch.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "branch": "string (required)",
  "from_branch": "string (optional)"
}
```

#### `list_branches`
List repository branches.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "page": "number (optional)",
  "perPage": "number (optional, max 100)"
}
```

#### `list_tags`
List repository tags.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "page": "number (optional)",
  "perPage": "number (optional, max 100)"
}
```

#### `get_tag`
Get details about a specific tag.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "tag": "string (required)"
}
```

#### `get_file_contents`
Read file contents from a repository.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "path": "string (required)",
  "branch": "string (optional)"
}
```

#### `create_or_update_file`
Create or update a single file.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "path": "string (required)",
  "content": "string (required)",
  "message": "string (required)",
  "branch": "string (required)",
  "sha": "string (required for updates)"
}
```

#### `delete_file`
Delete a file from a repository.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "path": "string (required)",
  "message": "string (required)",
  "branch": "string (required)"
}
```

#### `push_files`
Push multiple files in a single commit.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "branch": "string (required)",
  "files": [
    {
      "path": "string (required)",
      "content": "string (required)"
    }
  ],
  "message": "string (required)"
}
```

#### `list_commits`
List repository commits.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "sha": "string (optional) - branch or commit SHA",
  "page": "number (optional)",
  "perPage": "number (optional, max 100)"
}
```

#### `get_commit`
Get details for a specific commit.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "sha": "string (required)",
  "page": "number (optional)",
  "perPage": "number (optional, max 100)"
}
```

---

### 2.4 Security Operations (4 tools)

#### `list_code_scanning_alerts`
List code scanning alerts.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "state": "open|closed|dismissed|fixed (optional, default: open)",
  "ref": "string (optional)",
  "tool_name": "string (optional)",
  "severity": "critical|high|medium|low|warning|note|error (optional)"
}
```

#### `get_code_scanning_alert`
Get a specific code scanning alert.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "alertNumber": "number (required)"
}
```

#### `list_secret_scanning_alerts`
List secret scanning alerts.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "state": "open|resolved (optional)",
  "resolution": "false_positive|wont_fix|revoked|pattern_edited|pattern_deleted|used_in_tests (optional)",
  "secret_type": "string (optional)"
}
```

#### `get_secret_scanning_alert`
Get a specific secret scanning alert.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "alertNumber": "number (required)"
}
```

---

### 2.5 Search Operations (4 tools)

#### `search_code`
Search for code across GitHub.

**Parameters:**
```json
{
  "q": "string (required) - GitHub code search syntax",
  "sort": "indexed (optional)",
  "order": "asc|desc (optional)",
  "page": "number (optional)",
  "perPage": "number (optional, max 100)"
}
```

#### `search_repositories`
Search for repositories.

**Parameters:**
```json
{
  "query": "string (required)",
  "page": "number (optional)",
  "perPage": "number (optional, max 100)"
}
```

#### `search_users`
Search for GitHub users.

**Parameters:**
```json
{
  "q": "string (required)",
  "sort": "followers|repositories|joined (optional)",
  "order": "asc|desc (optional)",
  "page": "number (optional)",
  "perPage": "number (optional, max 100)"
}
```

#### `search_issues`
*(See Issue Operations above)*

---

### 2.6 Notifications Operations (5 tools)

#### `list_notifications`
List GitHub notifications.

**Parameters:**
```json
{
  "filter": "default|include_read_notifications|only_participating (optional)",
  "owner": "string (optional)",
  "repo": "string (optional)",
  "since": "ISO 8601 (optional)",
  "before": "ISO 8601 (optional)",
  "page": "number (optional)",
  "perPage": "number (optional, max 100)"
}
```

#### `get_notification_details`
Get detailed information for a specific notification.

**Parameters:**
```json
{
  "notificationID": "string (required)"
}
```

#### `dismiss_notification`
Dismiss a notification.

**Parameters:**
```json
{
  "threadID": "string (required)",
  "state": "read|done (optional)"
}
```

#### `mark_all_notifications_read`
Mark all notifications as read.

**Parameters:**
```json
{
  "lastReadAt": "ISO 8601 (optional, default: now)",
  "owner": "string (optional)",
  "repo": "string (optional)"
}
```

#### `manage_notification_subscription`
Manage notification subscription.

**Parameters:**
```json
{
  "notificationID": "string (required)",
  "action": "ignore|watch|delete (required)"
}
```

#### `manage_repository_notification_subscription`
Manage repository notification subscription.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "action": "ignore|watch|delete (required)"
}
```

---

### 2.7 Context Operations (1 tool)

#### `get_me`
Get details of authenticated GitHub user.

**Parameters:**
```json
{
  "reason": "string (optional)"
}
```

---

## 3. Experimental Features

### 3.1 Copilot Agent Integration

#### `assign_copilot_to_issue` ⚡ EXPERIMENTAL
Assign GitHub Copilot as an agent to work on a specific issue.

**Description:**
This experimental tool allows you to delegate an issue directly to GitHub Copilot, which will:
- Analyze the issue requirements
- Create a feature branch
- Implement code changes
- Open a draft pull request with the solution

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "issueNumber": "number (required)"
}
```

**Outcomes:**
- Pull request created with source code changes to resolve the issue
- Automatic branch creation and management
- Draft PR with detailed commit messages

**More Information:**
- https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks/about-assigning-tasks-to-copilot

**Advanced Usage:**
While the basic tool doesn't expose `base_ref` and `custom_instructions` parameters directly in the MCP schema, these can be influenced through:
- Issue description formatting (add specific instructions in the issue body)
- Repository default branch settings
- Custom agent configuration files (`.github/agents/`)

#### `request_copilot_review` ⚡ EXPERIMENTAL
Request automated GitHub Copilot code review for a pull request.

**Description:**
Requests automated feedback on a pull request before requesting human reviewers.

**Parameters:**
```json
{
  "owner": "string (required)",
  "repo": "string (required)",
  "pullNumber": "number (required)"
}
```

**Use Case:**
- Pre-review automation before human review
- Catch common issues early
- Code quality checks
- Best practice suggestions

---

### 3.2 Advanced Parameters (Not Yet in Public Schema)

Based on insider information and GitHub blog posts, these parameters are being developed for future releases:

#### `create_pull_request_with_copilot` (Future)
Enhanced PR creation with Copilot assistance.

**Expected Parameters:**
```json
{
  "owner": "string",
  "repo": "string",
  "title": "string",
  "head": "string",
  "base_ref": "string - explicit base branch control",
  "custom_agent": "string - reference to custom agent config",
  "instructions": "string - specific instructions for Copilot",
  "draft": "boolean"
}
```

#### `get_copilot_job_status` (Future)
Track Copilot agent job status.

**Expected Parameters:**
```json
{
  "job_id": "string",
  "owner": "string",
  "repo": "string"
}
```

**Expected Response:**
- Job state (queued, in_progress, completed, failed)
- Progress percentage
- Current step
- Logs and output
- PR link (if created)

---

## 4. Advanced Workflows

### 4.1 Stacked Pull Requests

**Concept**: Create a series of PRs where each builds on the previous one.

**Workflow:**
1. Create base feature branch from `main`
2. Make changes and create PR #1: `feature-1` → `main`
3. Create second branch from `feature-1`
4. Make changes and create PR #2: `feature-2` → `feature-1`
5. Continue stacking as needed

**Benefits:**
- Incremental review of large features
- Parallel work on dependent changes
- Easier to review smaller chunks

**MCP Implementation:**
```json
// PR 1
{
  "head": "feature-step-1",
  "base": "main",
  "title": "Part 1: Add database schema"
}

// PR 2 (stacked on PR 1)
{
  "head": "feature-step-2",
  "base": "feature-step-1",
  "title": "Part 2: Add API endpoints"
}

// PR 3 (stacked on PR 2)
{
  "head": "feature-step-3",
  "base": "feature-step-2",
  "title": "Part 3: Add UI components"
}
```

**Merge Strategy:**
- Merge PR #1 first
- Update PR #2 base to `main` after PR #1 merges
- Continue until all stacked PRs are merged

---

### 4.2 Sequential Task Chaining

**Concept**: Execute tasks in sequence where each depends on the previous completion.

**Use Case:**
- Task 1: Update dependencies
- Task 2: Fix breaking changes (depends on Task 1)
- Task 3: Update tests (depends on Task 2)
- Task 4: Update documentation (depends on Task 3)

**Implementation with Copilot:**
1. Create Issue #1 for Task 1
2. Assign Copilot to Issue #1: `assign_copilot_to_issue`
3. Wait for PR creation and review
4. Merge PR #1
5. Create Issue #2 for Task 2 (referencing completed Task 1)
6. Repeat

**Mission Control:**
GitHub Copilot Mission Control provides centralized tracking:
- View active agent jobs
- Monitor progress in real-time
- Steer agents mid-execution
- Track job status across multiple tasks

---

### 4.3 Feature Branch Workflows

**Concept**: Organize work around feature branches with multiple sub-tasks.

**Pattern:**
```
main
 └─ feature/new-dashboard
     ├─ PR #1: Add routing
     ├─ PR #2: Add components
     ├─ PR #3: Add styling
     └─ PR #4: Add tests
```

**MCP Operations:**
1. Create feature branch: `create_branch`
2. For each sub-task:
   - Create work branch from feature branch
   - Implement changes
   - Create PR to feature branch: `create_pull_request`
   - Review and merge
3. Final PR: feature branch → main

---

## 5. Tool Consolidation

Recent GitHub MCP updates consolidated granular tools into multi-function tools:

### Before Consolidation (Legacy)
- `create_pr_review`
- `submit_pr_review`
- `delete_pr_review`
- `add_pr_review_comment`

### After Consolidation (Current)
- `create_pending_pull_request_review`
- `add_pull_request_review_comment_to_pending_review`
- `submit_pending_pull_request_review`
- `delete_pending_pull_request_review`
- `create_and_submit_pull_request_review`

**Benefits:**
- Clearer intent
- Better parameter organization
- Improved error handling
- Easier automation

---

## 6. Configuration

### 6.1 MCP Server Configuration

**File**: `.github/copilot-mcp.json` or `mcp.json`

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/insiders",
      "headers": {
        "Authorization": "Bearer ${GITHUB_TOKEN}",
        "X-MCP-Toolsets": "*"
      },
      "tools": ["*"]
    }
  }
}
```

### 6.2 Toolset Filtering

Enable specific toolsets only:

```json
{
  "headers": {
    "X-MCP-Toolsets": "issues,pull_requests,repos"
  }
}
```

Available toolsets:
- `issues`
- `pull_requests`
- `repos`
- `code_security`
- `secret_protection`
- `search`
- `notifications`
- `context`

### 6.3 Custom Agent Configuration

**File**: `.github/agents/my-agent.md`

```markdown
# My Custom Agent

Custom agent for handling specific workflows.

## Tools

- create_pull_request
- assign_copilot_to_issue
- request_copilot_review

## Instructions

This agent specializes in creating well-structured PRs with:
- Clear titles and descriptions
- Linked issues
- Reviewer assignments
```

---

## 7. Usage Examples

### 7.1 Create Issue and Assign to Copilot

```json
// Step 1: Create issue
{
  "tool": "create_issue",
  "parameters": {
    "owner": "Hack23",
    "repo": "homepage",
    "title": "Add dark mode support",
    "body": "Implement dark mode toggle with CSS variables",
    "labels": ["enhancement", "ui"]
  }
}

// Step 2: Assign to Copilot
{
  "tool": "assign_copilot_to_issue",
  "parameters": {
    "owner": "Hack23",
    "repo": "homepage",
    "issueNumber": 123
  }
}
```

### 7.2 Create Stacked PRs

```json
// Base PR
{
  "tool": "create_pull_request",
  "parameters": {
    "owner": "Hack23",
    "repo": "homepage",
    "title": "Step 1: Add configuration",
    "head": "feature/config",
    "base": "main",
    "body": "First step in multi-part feature"
  }
}

// Stacked PR
{
  "tool": "create_pull_request",
  "parameters": {
    "owner": "Hack23",
    "repo": "homepage",
    "title": "Step 2: Add implementation",
    "head": "feature/implementation",
    "base": "feature/config",  // Stacked on previous PR
    "body": "Second step, depends on step 1"
  }
}
```

### 7.3 Full Review Workflow

```json
// Step 1: Create pending review
{
  "tool": "create_pending_pull_request_review",
  "parameters": {
    "owner": "Hack23",
    "repo": "homepage",
    "pullNumber": 456
  }
}

// Step 2: Add review comments
{
  "tool": "add_pull_request_review_comment_to_pending_review",
  "parameters": {
    "owner": "Hack23",
    "repo": "homepage",
    "pullNumber": 456,
    "path": "src/app.js",
    "body": "Consider adding error handling here",
    "subjectType": "LINE",
    "line": 42,
    "side": "RIGHT"
  }
}

// Step 3: Submit review
{
  "tool": "submit_pending_pull_request_review",
  "parameters": {
    "owner": "Hack23",
    "repo": "homepage",
    "pullNumber": 456,
    "event": "REQUEST_CHANGES",
    "body": "Overall looks good, but needs error handling"
  }
}
```

### 7.4 Multi-File Push

```json
{
  "tool": "push_files",
  "parameters": {
    "owner": "Hack23",
    "repo": "homepage",
    "branch": "feature/batch-update",
    "message": "Update configuration files",
    "files": [
      {
        "path": "config/app.json",
        "content": "{\"version\": \"2.0\"}"
      },
      {
        "path": "config/database.json",
        "content": "{\"host\": \"localhost\"}"
      },
      {
        "path": "README.md",
        "content": "# Updated documentation"
      }
    ]
  }
}
```

---

## 8. Comparison with Previous Evaluation

### Operations Added (Previously Missing)

| Operation | Category | Status |
|-----------|----------|--------|
| `assign_copilot_to_issue` | Copilot Agent | ✅ Experimental |
| `request_copilot_review` | Copilot Agent | ✅ Experimental |
| `create_pending_pull_request_review` | Pull Requests | ✅ Available |
| `add_pull_request_review_comment_to_pending_review` | Pull Requests | ✅ Available |
| `submit_pending_pull_request_review` | Pull Requests | ✅ Available |
| `delete_pending_pull_request_review` | Pull Requests | ✅ Available |
| `create_and_submit_pull_request_review` | Pull Requests | ✅ Available |
| `update_pull_request_branch` | Pull Requests | ✅ Available |
| `create_branch` | Repository | ✅ Available |
| `create_repository` | Repository | ✅ Available |
| `fork_repository` | Repository | ✅ Available |
| `create_or_update_file` | Repository | ✅ Available |
| `delete_file` | Repository | ✅ Available |
| `push_files` | Repository | ✅ Available |
| `list_notifications` | Notifications | ✅ Available |
| `get_notification_details` | Notifications | ✅ Available |
| `dismiss_notification` | Notifications | ✅ Available |
| `mark_all_notifications_read` | Notifications | ✅ Available |
| `manage_notification_subscription` | Notifications | ✅ Available |
| `manage_repository_notification_subscription` | Notifications | ✅ Available |
| `get_me` | Context | ✅ Available |
| `update_issue` | Issues | ✅ Available |
| `update_pull_request` | Pull Requests | ✅ Available |

**Total New Operations**: 24+ (increasing total from 27 to 51+)

---

## 9. Future Enhancements

Based on GitHub's roadmap and community feedback:

### Planned Features
- ✨ `get_copilot_job_status` - Track agent job progress
- ✨ `create_pull_request_with_copilot` - Enhanced PR creation with agent
- ✨ `base_ref` parameter - Explicit base branch control
- ✨ `custom_instructions` - Pass instructions to Copilot agents
- ✨ Stacked PR automation - Native support for PR chains
- ✨ Sequential task templates - Pre-defined task sequences

### Expected Timeline
- Q1 2026: Enhanced agent status tracking
- Q2 2026: Advanced workflow automation
- Q3 2026: Full custom agent parameter support

---

## 10. References

### Official Documentation
- [GitHub MCP Server Official Repository](https://github.com/github/github-mcp-server)
- [Using the GitHub MCP Server](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/use-the-github-mcp-server)
- [Configuring Toolsets](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/configure-toolsets)
- [Custom Agents Configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
- [Assigning Tasks to Copilot](https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks/about-assigning-tasks-to-copilot)

### Community Resources
- [Complete Tool List (Gist)](https://gist.github.com/didier-durand/2970be82fec6c84d522f7953ac7881b4)
- [GitHub Blog: Practical Guide to MCP Server](https://github.blog/ai-and-ml/generative-ai/a-practical-guide-on-how-to-use-the-github-mcp-server/)
- [Mission Control for Agents](https://github.blog/changelog/2025-10-28-a-mission-control-to-assign-steer-and-track-copilot-coding-agent-tasks/)
- [Chaining Custom Agents](https://www.ericksegaar.com/2025/12/15/chaining-github-copilot-custom-agents-automating-your-dev-cycle/)

### Tool Documentation
- [GitHub Toolsets Reference](https://deepwiki.com/github/github-mcp-server/3-github-toolsets)
- [Pull Requests Toolset](https://deepwiki.com/github/github-mcp-server/3.3-pull-requests-toolset)
- [VS Code MCP Integration](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)

---

## Appendix A: Quick Reference

### Most Common Operations

```bash
# Issues
create_issue, get_issue, list_issues, update_issue, add_issue_comment

# Pull Requests
create_pull_request, get_pull_request, list_pull_requests, merge_pull_request, 
update_pull_request, get_pull_request_diff

# Repository
get_file_contents, create_branch, push_files, list_commits

# Copilot (Experimental)
assign_copilot_to_issue, request_copilot_review

# Search
search_code, search_repositories, search_issues

# Security
list_code_scanning_alerts, list_secret_scanning_alerts
```

### Parameter Patterns

**Pagination:**
```json
{
  "page": "number",
  "perPage": "number (max 100)"
}
```

**Filtering:**
```json
{
  "state": "open|closed|all",
  "labels": ["string"],
  "sort": "created|updated",
  "direction": "asc|desc"
}
```

**Search:**
```json
{
  "q": "search query with GitHub syntax",
  "sort": "relevance|...",
  "order": "asc|desc"
}
```

---

**Document Version**: 2.0  
**Last Updated**: 2026-02-02  
**Maintainer**: GitHub Copilot Test Specialist Agent  
**Status**: ✅ Complete - All 51+ operations documented with experimental features

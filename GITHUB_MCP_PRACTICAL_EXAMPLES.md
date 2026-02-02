# GitHub MCP Server - Practical Examples & Usage Guide

This document provides **hands-on examples** and **practical usage patterns** for GitHub MCP server operations, with a focus on experimental Copilot features and automation workflows.

## Table of Contents

1. [Quick Start Examples](#quick-start-examples)
2. [Experimental Copilot Features - Hands On](#experimental-copilot-features---hands-on)
3. [Real-World Automation Scenarios](#real-world-automation-scenarios)
4. [Troubleshooting Guide](#troubleshooting-guide)
5. [Best Practices](#best-practices)

---

## Quick Start Examples

### Example 1: Search Organization Repositories

```javascript
// Find all TypeScript repositories with high activity
const repos = await search_repositories({
  query: "org:Hack23 language:TypeScript stars:>5",
  sort: "updated",
  order: "desc",
  perPage: 10
});

console.log(`Found ${repos.total_count} repositories`);
repos.items.forEach(repo => {
  console.log(`- ${repo.full_name} (${repo.stargazers_count} stars)`);
});
```

**Expected Output:**
```
Found 4 repositories
- Hack23/cia-compliance-manager (15 stars)
- Hack23/blacktrigram (4 stars)
- Hack23/game (10 stars)
```

---

### Example 2: Cross-Repository File Access

```javascript
// Read security policy from ISMS-PUBLIC
const securityPolicy = await get_file_contents({
  owner: "Hack23",
  repo: "ISMS-PUBLIC",
  path: "Information_Security_Policy.md"
});

console.log(`Policy size: ${securityPolicy.size} bytes`);
console.log(`Last updated: ${securityPolicy.commit.author.date}`);

// Apply to another repository (via PR)
const job = await create_pull_request_with_copilot({
  owner: "Hack23",
  repo: "homepage",
  problem_statement: `
    Update SECURITY.md to reference the organization security policy from ISMS-PUBLIC.
    Add a link to the full policy: https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md
  `,
  title: "Security: Link to organization security policy",
  base_ref: "main"
});

console.log(`Created job: ${job.job_id}`);
```

---

### Example 3: Find and Fix Security Issues

```javascript
// List open security alerts
const codeAlerts = await list_code_scanning_alerts({
  owner: "Hack23",
  repo: "homepage",
  state: "open",
  severity: "high"
});

const secretAlerts = await list_secret_scanning_alerts({
  owner: "Hack23",
  repo: "homepage",
  state: "open"
});

const dependabotAlerts = await list_dependabot_alerts({
  owner: "Hack23",
  repo: "homepage",
  state: "open",
  severity: "high"
});

console.log(`Security Status:
- Code scanning: ${codeAlerts.length} high severity
- Secret scanning: ${secretAlerts.length} open
- Dependabot: ${dependabotAlerts.length} high severity
`);

// Auto-fix Dependabot alerts
for (const alert of dependabotAlerts) {
  const issue = await issue_write({
    method: "create",
    owner: "Hack23",
    repo: "homepage",
    title: `Security: Upgrade ${alert.security_advisory.package.name}`,
    body: `
Dependabot Alert #${alert.number}

**Vulnerability:** ${alert.security_advisory.summary}
**Severity:** ${alert.security_advisory.severity}
**Affected:** ${alert.security_advisory.package.name}@${alert.dependency.manifest_path}

**Recommendation:** Upgrade to ${alert.security_advisory.first_patched_version}

**References:**
- CVE: ${alert.security_advisory.cve_id}
- GHSA: ${alert.security_advisory.ghsa_id}
    `,
    labels: ["security", "dependencies"]
  });

  // Assign Copilot to fix
  await assign_copilot_to_issue({
    owner: "Hack23",
    repo: "homepage",
    issue_number: issue.number,
    custom_instructions: "Update package version in package.json and run npm audit. Ensure no breaking changes."
  });
}
```

---

### Example 4: Bulk Issue Management

```javascript
// Find all stale issues
const staleIssues = await search_issues({
  query: "is:open is:issue repo:Hack23/homepage updated:<2025-01-01",
  sort: "updated",
  order: "asc"
});

console.log(`Found ${staleIssues.total_count} stale issues`);

// Add comment to each
for (const issue of staleIssues.items) {
  await add_issue_comment({
    owner: "Hack23",
    repo: "homepage",
    issue_number: issue.number,
    body: `
This issue has been inactive for over a year. 

@${issue.user.login} Is this still relevant? If not, please close it.

If no response within 14 days, this issue will be automatically closed.
    `
  });
}
```

---

## Experimental Copilot Features - Hands On

### Feature 1: assign_copilot_to_issue

**Use Case:** Automatically fix a reported bug

```javascript
// Scenario: User reports accessibility issue
const issue = await issue_write({
  method: "create",
  owner: "Hack23",
  repo: "homepage",
  title: "Accessibility: Missing alt text on blog images",
  body: `
## Description
Blog post images in the Korean version (blog_ko.html) are missing alt text, failing WCAG 2.1 AA compliance.

## Steps to Reproduce
1. Open blog_ko.html
2. Run Lighthouse accessibility audit
3. See "Images must have alternate text" warning

## Expected Behavior
All images should have descriptive alt text in Korean.

## Affected Files
- blog_ko.html (lines 150-200)
  `,
  labels: ["bug", "accessibility", "priority:high"]
});

console.log(`Created issue #${issue.number}`);

// Assign to Copilot
const assignment = await assign_copilot_to_issue({
  owner: "Hack23",
  repo: "homepage",
  issue_number: issue.number,
  base_ref: "main",
  custom_instructions: `
Follow these guidelines:
1. Use the HTML/CSS Best Practices skill
2. Ensure WCAG 2.1 AA compliance
3. Alt text should be descriptive and in Korean
4. Test with Lighthouse (Accessibility score must be 100)
5. Follow existing image alt text patterns in the codebase
  `
});

console.log(`Copilot assigned to issue #${issue.number}`);
// Copilot will:
// 1. Create branch: copilot/fix-issue-{number}
// 2. Add alt text to all images
// 3. Test with Lighthouse
// 4. Create PR with fix
// 5. Link PR to issue
```

**Monitoring Progress:**

```javascript
// Check if PR was created
setTimeout(async () => {
  const prs = await search_pull_requests({
    query: `is:open repo:Hack23/homepage fixes #${issue.number}`
  });
  
  if (prs.total_count > 0) {
    console.log(`PR created: ${prs.items[0].html_url}`);
    console.log(`Title: ${prs.items[0].title}`);
  } else {
    console.log("Copilot still working...");
  }
}, 60000); // Check after 1 minute
```

---

### Feature 2: create_pull_request_with_copilot

**Use Case:** Implement a new feature with detailed requirements

```javascript
// Scenario: Add dark mode support
const job = await create_pull_request_with_copilot({
  owner: "Hack23",
  repo: "homepage",
  title: "Feature: Add dark mode support",
  problem_statement: `
# Dark Mode Implementation

## Requirements
1. Add dark mode toggle to navigation bar
2. Store user preference in localStorage
3. Implement CSS custom properties for theming
4. Support system preference detection (prefers-color-scheme)
5. Smooth transition between modes

## Design Specifications
- Toggle icon: Sun (☀️) for light mode, Moon (🌙) for dark mode
- Colors:
  - Background: #1a1a1a (dark), #ffffff (light)
  - Text: #e0e0e0 (dark), #333333 (light)
  - Primary: #4a9eff (dark), #0066cc (light)
  - Secondary: #6c757d (same for both)
  
## Technical Requirements
- Use CSS variables in :root
- JavaScript for toggle functionality
- Maintain accessibility (WCAG 2.1 AA contrast ratios)
- Update all 13+ language versions
- Test with Lighthouse

## Files to Modify
- styles.css: Add CSS variables and dark mode styles
- All HTML files: Add toggle button and script
- Follow existing patterns in the codebase

## Testing
- Lighthouse accessibility score must remain 100
- Test in Chrome, Firefox, Safari
- Test with keyboard navigation
- Test localStorage persistence
  `,
  base_ref: "main"
});

console.log(`Job created: ${job.job_id}`);
console.log(`Status: ${job.status}`);
```

**Tracking Job Progress:**

```javascript
// Poll for completion
async function waitForCompletion(jobId, owner, repo) {
  let status;
  let attempts = 0;
  const maxAttempts = 60; // 10 minutes max (10s interval)
  
  do {
    status = await get_copilot_job_status({
      owner,
      repo,
      id: jobId
    });
    
    console.log(`Attempt ${attempts + 1}: ${status.status}`);
    
    if (status.status === "completed") {
      console.log(`✅ Job completed!`);
      console.log(`PR URL: ${status.pr_url}`);
      return status;
    }
    
    if (status.status === "failed") {
      console.log(`❌ Job failed: ${status.error}`);
      return status;
    }
    
    await new Promise(resolve => setTimeout(resolve, 10000)); // Wait 10s
    attempts++;
  } while (attempts < maxAttempts);
  
  console.log(`⏱️ Timeout: Job still ${status.status} after ${maxAttempts} attempts`);
  return status;
}

// Use the function
const result = await waitForCompletion(job.job_id, "Hack23", "homepage");

if (result.status === "completed") {
  // Automatically request Copilot review
  const prNumber = result.pr_url.split('/').pop();
  
  await request_copilot_review({
    owner: "Hack23",
    repo: "homepage",
    pullNumber: parseInt(prNumber)
  });
  
  console.log(`Copilot review requested for PR #${prNumber}`);
}
```

---

### Feature 3: get_copilot_job_status

**Use Case:** Monitor multiple jobs and coordinate sequential tasks

```javascript
// Launch multiple parallel jobs
const jobs = [
  {
    name: "Swedish Translation",
    job: await create_pull_request_with_copilot({
      owner: "Hack23",
      repo: "homepage",
      title: "i18n: Add Swedish translation for Q1 blog posts",
      problem_statement: "Translate blog posts published in Q1 2026 to Swedish following Swedish-Translation-Guide.md",
      base_ref: "main"
    })
  },
  {
    name: "Korean Translation",
    job: await create_pull_request_with_copilot({
      owner: "Hack23",
      repo: "homepage",
      title: "i18n: Add Korean translation for Q1 blog posts",
      problem_statement: "Translate blog posts published in Q1 2026 to Korean following Korean-Translation-Guide.md",
      base_ref: "main"
    })
  },
  {
    name: "Accessibility Audit",
    job: await create_pull_request_with_copilot({
      owner: "Hack23",
      repo: "homepage",
      title: "Accessibility: Fix WCAG 2.1 AA issues",
      problem_statement: "Run Lighthouse audit, fix all accessibility issues to achieve score of 100",
      base_ref: "main"
    })
  }
];

console.log(`Launched ${jobs.length} parallel jobs`);

// Monitor all jobs
async function monitorJobs(jobs) {
  const results = [];
  
  for (const {name, job} of jobs) {
    console.log(`\n=== ${name} ===`);
    const status = await waitForCompletion(job.job_id, "Hack23", "homepage");
    results.push({name, status});
  }
  
  return results;
}

const results = await monitorJobs(jobs);

// Summary
console.log("\n=== Summary ===");
results.forEach(({name, status}) => {
  const icon = status.status === "completed" ? "✅" : "❌";
  console.log(`${icon} ${name}: ${status.status}`);
  if (status.pr_url) {
    console.log(`   PR: ${status.pr_url}`);
  }
});
```

---

## Real-World Automation Scenarios

### Scenario 1: Weekly Security Audit

```javascript
// automation/security-audit.js

async function weeklySecurityAudit() {
  const repos = ["homepage", "blacktrigram", "cia-compliance-manager"];
  const report = {
    date: new Date().toISOString(),
    findings: []
  };
  
  for (const repo of repos) {
    console.log(`\n🔍 Auditing ${repo}...`);
    
    // Check code scanning
    const codeAlerts = await list_code_scanning_alerts({
      owner: "Hack23",
      repo,
      state: "open"
    });
    
    // Check secrets
    const secretAlerts = await list_secret_scanning_alerts({
      owner: "Hack23",
      repo,
      state: "open"
    });
    
    // Check dependencies
    const depAlerts = await list_dependabot_alerts({
      owner: "Hack23",
      repo,
      state: "open"
    });
    
    const finding = {
      repo,
      code_alerts: codeAlerts.length,
      secret_alerts: secretAlerts.length,
      dependency_alerts: depAlerts.length,
      total: codeAlerts.length + secretAlerts.length + depAlerts.length
    };
    
    report.findings.push(finding);
    
    // Create issue if findings exist
    if (finding.total > 0) {
      await issue_write({
        method: "create",
        owner: "Hack23",
        repo,
        title: `Security Audit: ${finding.total} findings (Week ${getWeekNumber()})`,
        body: `
## Weekly Security Audit Report

**Date:** ${new Date().toLocaleDateString()}

### Findings
- 🔍 Code Scanning: ${finding.code_alerts} alerts
- 🔐 Secret Scanning: ${finding.secret_alerts} alerts
- 📦 Dependency Scanning: ${finding.dependency_alerts} alerts

### Action Required
Please review and address these security findings. High and critical severity issues should be prioritized.

### References
- [ISMS Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)
- [Vulnerability Management](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Vulnerability_Management_Policy.md)
        `,
        labels: ["security", "audit"]
      });
    }
  }
  
  // Summary
  console.log("\n=== Security Audit Summary ===");
  console.log(`Total repositories: ${repos.length}`);
  console.log(`Total findings: ${report.findings.reduce((sum, f) => sum + f.total, 0)}`);
  
  return report;
}

// Run weekly
weeklySecurityAudit();
```

---

### Scenario 2: Automated Translation Pipeline

```javascript
// automation/translation-pipeline.js

async function translateContent(sourceFile, languages) {
  const jobs = [];
  
  for (const lang of languages) {
    const job = await create_pull_request_with_copilot({
      owner: "Hack23",
      repo: "homepage",
      title: `i18n: Translate ${sourceFile} to ${lang.name}`,
      problem_statement: `
Translate ${sourceFile} to ${lang.name}.

## Guidelines
- Follow ${lang.guide} for translation standards
- Maintain HTML structure exactly
- Preserve all links and references
- Use culturally appropriate examples
- Test rendering after translation

## Quality Checklist
- [ ] All text translated
- [ ] Links updated (if locale-specific)
- [ ] Images have alt text in target language
- [ ] No broken HTML
- [ ] Lighthouse score maintained
      `,
      base_ref: "main"
    });
    
    jobs.push({lang: lang.name, jobId: job.job_id});
  }
  
  // Monitor all translations
  for (const {lang, jobId} of jobs) {
    console.log(`Waiting for ${lang} translation...`);
    const status = await waitForCompletion(jobId, "Hack23", "homepage");
    
    if (status.status === "completed") {
      console.log(`✅ ${lang}: ${status.pr_url}`);
      
      // Auto-merge if tests pass (optional)
      // await mergePR(status.pr_number);
    } else {
      console.log(`❌ ${lang}: Failed`);
    }
  }
}

// Example usage
const languages = [
  { name: "Swedish", code: "sv", guide: "Swedish-Translation-Guide.md" },
  { name: "Korean", code: "ko", guide: "Korean-Translation-Guide.md" },
  { name: "German", code: "de", guide: "German-Translation-Guide.md" },
  { name: "French", code: "fr", guide: "French-Translation-Guide.md" }
];

translateContent("blog-post-new.html", languages);
```

---

### Scenario 3: Stacked Feature Development

```javascript
// automation/stacked-feature.js

async function implementFeature(feature) {
  const phases = feature.phases;
  const results = [];
  
  for (let i = 0; i < phases.length; i++) {
    const phase = phases[i];
    console.log(`\n📦 Phase ${i + 1}/${phases.length}: ${phase.title}`);
    
    // Create PR for this phase
    const job = await create_pull_request_with_copilot({
      owner: feature.owner,
      repo: feature.repo,
      title: `${feature.name}: ${phase.title}`,
      problem_statement: phase.description,
      base_ref: feature.base_ref
    });
    
    // Wait for completion
    const status = await waitForCompletion(job.job_id, feature.owner, feature.repo);
    
    if (status.status !== "completed") {
      console.log(`❌ Phase ${i + 1} failed. Aborting.`);
      return { success: false, failedPhase: i + 1, results };
    }
    
    results.push({
      phase: i + 1,
      title: phase.title,
      pr_url: status.pr_url,
      pr_number: status.pr_url.split('/').pop()
    });
    
    // Request review
    await request_copilot_review({
      owner: feature.owner,
      repo: feature.repo,
      pullNumber: parseInt(results[i].pr_number)
    });
    
    console.log(`✅ Phase ${i + 1} complete: ${status.pr_url}`);
    
    // Wait for manual merge before next phase
    console.log("⏸️  Waiting for PR merge...");
    await waitForPRMerge(feature.owner, feature.repo, parseInt(results[i].pr_number));
    console.log("✅ PR merged. Continuing to next phase.");
  }
  
  return { success: true, results };
}

// Example: Implement payment system
const paymentFeature = {
  name: "Payment System",
  owner: "Hack23",
  repo: "cia-compliance-manager",
  base_ref: "main",
  phases: [
    {
      title: "Database Schema",
      description: `
Add database tables for payment system:
- payments: id, user_id, amount, currency, status, created_at
- payment_methods: id, user_id, type, details, is_default
- transactions: id, payment_id, type, amount, timestamp

Include migrations and indexes.
      `
    },
    {
      title: "Backend API",
      description: `
Implement REST API for payments:
- POST /api/payments - Create payment
- GET /api/payments/:id - Get payment details
- GET /api/payments - List user payments
- POST /api/payment-methods - Add payment method
- GET /api/payment-methods - List payment methods

Use database schema from previous phase.
Include input validation and error handling.
      `
    },
    {
      title: "Frontend UI",
      description: `
Create payment UI components:
- PaymentForm component (card input, validation)
- PaymentMethodList component (saved cards)
- PaymentHistory component (transaction list)

Use API endpoints from previous phase.
Follow existing UI patterns and design system.
Include loading states and error handling.
      `
    },
    {
      title: "Tests",
      description: `
Add comprehensive tests:
- Unit tests for payment API endpoints (Jest)
- Integration tests for payment flow (Supertest)
- E2E tests for payment UI (Cypress)

Target: 80% line coverage, 70% branch coverage.
Test error scenarios and edge cases.
      `
    }
  ]
};

// Run the feature implementation
implementFeature(paymentFeature);
```

---

## Troubleshooting Guide

### Issue 1: Job Stuck in "in_progress"

**Symptoms:**
```javascript
get_copilot_job_status({owner, repo, id: job_id})
// Returns: { status: "in_progress" } for > 10 minutes
```

**Possible Causes:**
1. Complex task requiring more time
2. Build/test failures
3. Merge conflicts
4. API rate limits

**Solutions:**
```javascript
// Increase polling interval
await new Promise(resolve => setTimeout(resolve, 30000)); // 30s instead of 10s

// Check workflow runs for errors
const runs = await github-actions_list({
  method: "list_workflow_runs",
  owner: "Hack23",
  repo: "homepage",
  workflow_runs_filter: {
    status: "in_progress"
  }
});

// Check for failed jobs
const failedJobs = await github-actions_list({
  method: "list_workflow_jobs",
  owner: "Hack23",
  repo: "homepage",
  resource_id: runs[0].id,
  workflow_jobs_filter: {
    filter: "latest"
  }
});

// Get logs for failed jobs
for (const job of failedJobs.jobs) {
  if (job.conclusion === "failure") {
    const logs = await get_job_logs({
      owner: "Hack23",
      repo: "homepage",
      job_id: job.id,
      return_content: true,
      tail_lines: 100
    });
    console.log(`Failed job ${job.name}:\n${logs}`);
  }
}
```

---

### Issue 2: PAT Access Denied

**Symptoms:**
```
Error: Resource not accessible with current permissions
```

**Verification:**
```javascript
// Test basic access
try {
  const repos = await search_repositories({
    query: "org:Hack23"
  });
  console.log(`✅ Organization access: ${repos.total_count} repos`);
} catch (error) {
  console.log(`❌ Organization access: ${error.message}`);
}

// Test cross-repo access
try {
  const file = await get_file_contents({
    owner: "Hack23",
    repo: "ISMS-PUBLIC",
    path: "README.md"
  });
  console.log(`✅ Cross-repo access: File size ${file.size} bytes`);
} catch (error) {
  console.log(`❌ Cross-repo access: ${error.message}`);
}

// Test write permissions
try {
  const issue = await issue_write({
    method: "create",
    owner: "Hack23",
    repo: "homepage",
    title: "Test Issue - Please Delete",
    body: "Testing PAT permissions"
  });
  console.log(`✅ Write access: Created issue #${issue.number}`);
  
  // Clean up
  await issue_write({
    method: "update",
    owner: "Hack23",
    repo: "homepage",
    issue_number: issue.number,
    state: "closed"
  });
} catch (error) {
  console.log(`❌ Write access: ${error.message}`);
}
```

---

### Issue 3: Rate Limiting

**Symptoms:**
```
Error: API rate limit exceeded
```

**Solution:**
```javascript
// Implement exponential backoff
async function retryWithBackoff(fn, maxRetries = 5) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (error) {
      if (error.message.includes("rate limit")) {
        const delay = Math.pow(2, i) * 1000; // 1s, 2s, 4s, 8s, 16s
        console.log(`Rate limited. Retrying in ${delay}ms...`);
        await new Promise(resolve => setTimeout(resolve, delay));
      } else {
        throw error;
      }
    }
  }
  throw new Error("Max retries exceeded");
}

// Usage
const repos = await retryWithBackoff(() =>
  search_repositories({
    query: "org:Hack23"
  })
);
```

---

## Best Practices

### 1. Always Provide Detailed Instructions

**❌ Bad:**
```javascript
create_pull_request_with_copilot({
  owner: "Hack23",
  repo: "homepage",
  problem_statement: "Add dark mode",
  title: "Dark mode"
});
```

**✅ Good:**
```javascript
create_pull_request_with_copilot({
  owner: "Hack23",
  repo: "homepage",
  problem_statement: `
Add dark mode support to the website.

Requirements:
1. Use CSS custom properties for theming
2. Add toggle button in navigation
3. Persist preference in localStorage
4. Support prefers-color-scheme media query
5. Maintain WCAG 2.1 AA contrast ratios

Design:
- Background: #1a1a1a (dark), #ffffff (light)
- Text: #e0e0e0 (dark), #333333 (light)
- Smooth transition between modes

Files to modify:
- styles.css: Add variables and dark mode styles
- All HTML files: Add toggle button

Testing:
- Lighthouse accessibility score must be 100
- Test in Chrome, Firefox, Safari
  `,
  title: "Feature: Add dark mode support with user toggle"
});
```

---

### 2. Use Custom Instructions for assign_copilot_to_issue

**❌ Bad:**
```javascript
assign_copilot_to_issue({
  owner: "Hack23",
  repo: "homepage",
  issue_number: 123
});
```

**✅ Good:**
```javascript
assign_copilot_to_issue({
  owner: "Hack23",
  repo: "homepage",
  issue_number: 123,
  custom_instructions: `
Follow these repository standards:
- Use HTML/CSS Best Practices skill
- Ensure WCAG 2.1 AA accessibility compliance
- Test with Lighthouse (score 100)
- Update all 13 language versions if needed
- Follow existing code patterns
- Add comments for complex logic
  `
});
```

---

### 3. Monitor Job Progress

**❌ Bad:**
```javascript
const job = await create_pull_request_with_copilot({...});
// Assume it completed...
```

**✅ Good:**
```javascript
const job = await create_pull_request_with_copilot({...});

// Poll for completion
const status = await waitForCompletion(job.job_id, owner, repo);

if (status.status === "completed") {
  console.log(`Success: ${status.pr_url}`);
  // Continue with next step
} else {
  console.log(`Failed: ${status.error}`);
  // Handle failure
}
```

---

### 4. Handle Errors Gracefully

**❌ Bad:**
```javascript
const job = await create_pull_request_with_copilot({...});
await waitForCompletion(job.job_id, owner, repo);
```

**✅ Good:**
```javascript
try {
  const job = await create_pull_request_with_copilot({...});
  const status = await waitForCompletion(job.job_id, owner, repo);
  
  if (status.status === "completed") {
    console.log(`✅ Success: ${status.pr_url}`);
  } else if (status.status === "failed") {
    console.log(`❌ Failed: ${status.error}`);
    // Notify team, create issue, etc.
    await notifyFailure(status);
  }
} catch (error) {
  console.error(`Error: ${error.message}`);
  // Fallback or retry logic
}
```

---

### 5. Use base_ref for Feature Branches

**❌ Bad:**
```javascript
// All PRs to main, potential conflicts
create_pull_request_with_copilot({
  owner, repo, title, problem_statement,
  base_ref: "main"
});
```

**✅ Good:**
```javascript
// Create feature branch first
await create_branch({
  owner: "Hack23",
  repo: "homepage",
  branch: "feature/dark-mode",
  from_branch: "main"
});

// PR 1: Foundation
await create_pull_request_with_copilot({
  owner, repo,
  title: "Dark mode: CSS variables",
  problem_statement: "...",
  base_ref: "feature/dark-mode" // Target feature branch
});

// PR 2: Build on foundation
await create_pull_request_with_copilot({
  owner, repo,
  title: "Dark mode: Toggle UI",
  problem_statement: "...",
  base_ref: "feature/dark-mode" // Builds on previous work
});

// Final PR: Feature branch to main
await create_pull_request({
  owner, repo,
  title: "Feature: Complete dark mode implementation",
  head: "feature/dark-mode",
  base: "main"
});
```

---

### 6. Leverage Cross-Repository Access

**❌ Bad:**
```javascript
// Manually copy policies between repos
```

**✅ Good:**
```javascript
// Read from central ISMS repo
const policy = await get_file_contents({
  owner: "Hack23",
  repo: "ISMS-PUBLIC",
  path: "Security_Policy.md"
});

// Apply to all repos
const repos = ["homepage", "blacktrigram", "cia-compliance-manager"];

for (const repo of repos) {
  await create_pull_request_with_copilot({
    owner: "Hack23",
    repo,
    title: "Security: Update policy to org standard",
    problem_statement: `
Update security policy to match organization standard from ISMS-PUBLIC.
Reference: https://github.com/Hack23/ISMS-PUBLIC/blob/main/Security_Policy.md

Maintain any repo-specific sections.
    `,
    base_ref: "main"
  });
}
```

---

## Summary

This guide provides **practical examples** for using GitHub MCP server operations, with a focus on:

✅ **Experimental Copilot features** for AI-assisted development  
✅ **Real-world automation scenarios** for common tasks  
✅ **Troubleshooting** common issues  
✅ **Best practices** for reliable automation  

For complete API reference, see [GITHUB_MCP_SERVER_OPERATIONS.md](./GITHUB_MCP_SERVER_OPERATIONS.md).

---

**Last Updated:** 2026-02-02  
**Maintained By:** Hack23 AB DevOps Team

---
name: mcp-server-integration
description: Model Context Protocol (MCP) server integration, configuration, and usage patterns for GitHub Copilot custom agents
license: Apache-2.0
---

# MCP Server Integration Skill

## Purpose

Guides proper configuration and usage of Model Context Protocol (MCP) servers for GitHub Copilot custom agents, ensuring secure, efficient, and standards-compliant integrations.

## Rules

### MCP Server Configuration

**Standard MCP Servers for Hack23:**
```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/insiders",
      "headers": {
        "Authorization": "Bearer ${{ secrets.COPILOT_MCP_GITHUB_PERSONAL_ACCESS_TOKEN }}",
        "X-MCP-Toolsets": "all"
      },
      "tools": ["*"]
    },
    "filesystem": {
      "type": "local",
      "command": "mcp-server-filesystem",
      "args": ["/home/runner/work/homepage/homepage"],
      "tools": ["*"]
    },
    "memory": {
      "type": "local",
      "command": "mcp-server-memory",
      "args": [],
      "tools": ["*"]
    },
    "sequential-thinking": {
      "type": "local",
      "command": "mcp-server-sequential-thinking",
      "args": [],
      "tools": ["*"]
    },
    "playwright": {
      "type": "local",
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest", "--headless"],
      "env": {
        "DISPLAY": ":99"
      },
      "tools": ["*"]
    }
  }
}
```

### MCP Server Security

**MUST:**
- Use GitHub secrets for all credentials (`${{ secrets.NAME }}`)
- Never hardcode tokens or API keys
- Use least-privilege access (specific tools, not "*" unless necessary)
- Validate all MCP server inputs
- Use HTTPS for remote MCP servers

**GitHub MCP Authentication:**
```json
{
  "github": {
    "type": "http",
    "url": "https://api.githubcopilot.com/mcp/insiders",
    "headers": {
      "Authorization": "Bearer ${{ secrets.COPILOT_MCP_GITHUB_PERSONAL_ACCESS_TOKEN }}"
    }
  }
}
```

### Available MCP Servers

**Core Services:**
```markdown
1. GitHub MCP
   - Repository operations
   - Issue/PR management
   - GitHub Actions
   - Copilot coding agent tools

2. Filesystem MCP
   - Read/write files
   - Directory navigation
   - File search

3. Git MCP
   - Commit history
   - Branch operations
   - Diff viewing

4. Memory MCP
   - Context preservation
   - Cross-session memory
   - Knowledge retention
```

**Intelligence Services:**
```markdown
5. Sequential Thinking MCP
   - Complex problem breakdown
   - Reasoning chains
   - Decision documentation

6. Brave Search MCP (optional)
   - Web search
   - Research capabilities
   - Requires API key
```

**Automation Services:**
```markdown
7. Playwright MCP
   - Browser automation
   - UI testing
   - Screenshot capture
   - Web scraping
```

### Agent Tool Configuration

**Minimal Tool Set (Recommended):**
```yaml
---
name: ui-enhancement-specialist
description: UI/UX specialist
tools: ["view", "edit", "create", "shell", "search_code"]
---
```

**Full Tool Access (For Meta Agents):**
```yaml
---
name: agent-curator
description: Meta agent for agent management
tools: ["*"]
---
```

### MCP Server Usage Patterns

**GitHub MCP - Issue Management:**
```javascript
// Create issue with Copilot assignment
github-create_issue({
  owner: "Hack23",
  repo: "homepage",
  title: "Implement feature X",
  body: "Detailed requirements...",
  assignees: ["copilot-swe-agent[bot]"]
})

// Advanced: Assign with base_ref and custom instructions
assign_copilot_to_issue({
  owner: "Hack23",
  repo: "homepage",
  issue_number: 123,
  base_ref: "feature/branch",
  custom_instructions: "Follow accessibility guidelines"
})
```

**Filesystem MCP - File Operations:**
```javascript
// Read file
filesystem-read_text_file({ path: "/path/to/file.md" })

// Write file
filesystem-write_file({
  path: "/path/to/file.md",
  content: "# New Content"
})

// List directory
filesystem-list_directory({ path: "/path/to/dir" })
```

**Memory MCP - Context Retention:**
```javascript
// Store knowledge
memory-store({
  key: "project-architecture",
  value: "This project uses microservices with AWS Lambda..."
})

// Retrieve knowledge
memory-retrieve({ key: "project-architecture" })
```

**Playwright MCP - Browser Automation:**
```javascript
// Navigate and screenshot
playwright-browser_navigate({ url: "https://hack23.com" })
playwright-browser_take_screenshot({ filename: "homepage.png" })

// Test accessibility
playwright-browser_snapshot()
```

### Environment Configuration

**Workflow Setup (.github/workflows/copilot-setup-steps.yml):**
```yaml
env:
  GITHUB_TOKEN: ${{ secrets.COPILOT_MCP_GITHUB_PERSONAL_ACCESS_TOKEN }}
  GITHUB_PERSONAL_ACCESS_TOKEN: ${{ secrets.COPILOT_MCP_GITHUB_PERSONAL_ACCESS_TOKEN }}
  DISPLAY: ":99"

steps:
  - name: Install MCP Servers
    run: |
      npm install -g @modelcontextprotocol/server-filesystem
      npm install -g @modelcontextprotocol/server-memory
      npm install -g @modelcontextprotocol/server-sequential-thinking
      npm install -g @playwright/mcp
```

### Troubleshooting

**Common Issues:**
```markdown
1. MCP Server Not Found
   - Verify installation: `which mcp-server-filesystem`
   - Check PATH environment variable
   - Reinstall: `npm install -g @modelcontextprotocol/server-filesystem`

2. Authentication Errors
   - Verify secret exists: COPILOT_MCP_GITHUB_PERSONAL_ACCESS_TOKEN
   - Check token permissions
   - Ensure proper secret reference syntax

3. Permission Denied
   - Check filesystem permissions
   - Verify workspace paths
   - Review allowed directories

4. Playwright Display Error
   - Verify Xvfb running
   - Check DISPLAY environment variable
   - Install display dependencies
```

## Related Policies

- [Secure Development SKILL](../../security/secure-development/SKILL.md)
- [GitHub Actions CI/CD SKILL](../../deployment/github-actions-cicd/SKILL.md)

## Related Documentation

- [task-agent Agent](../../../agents/task-agent.md)
- [.github/copilot-mcp.json](../../../../copilot-mcp.json)
- [.github/workflows/copilot-setup-steps.yml](../../../../workflows/copilot-setup-steps.yml)

## Resources

- [MCP Specification](https://github.com/modelcontextprotocol/specification)
- [GitHub Copilot MCP Documentation](https://docs.github.com/en/copilot)
- [@modelcontextprotocol packages](https://www.npmjs.com/search?q=%40modelcontextprotocol)

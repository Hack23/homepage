# GitHub Copilot Custom Agent Profiles

This directory contains specialized custom agent profiles that enable domain-specific assistance from GitHub Copilot. Each profile provides deep expertise in a specific area relevant to Hack23 AB's operations.

## Agent Profile Format

Each agent profile is a Markdown file with YAML frontmatter that specifies:
- **name**: Unique identifier for the agent (kebab-case)
- **description**: Brief explanation of the agent's capabilities and expertise
- **tools**: List of tools the agent can use (optional - if omitted, agent has access to all tools)

The YAML frontmatter is followed by the agent's instructions in Markdown format, which define behavior, expertise, and guidelines.

## Available Agent Profiles

### 1. UI Enhancement Specialist (`ui-enhancement-specialist.md`)
**Focus**: HTML/CSS, Web Accessibility, Responsive Design

Expert in creating accessible, responsive, and visually appealing web interfaces using modern web standards. Specializes in:
- HTML5 semantic markup and accessibility (WCAG 2.1 AA)
- CSS3 modern features (Flexbox, Grid, custom properties)
- Responsive design and mobile-first approaches
- Performance optimization and Lighthouse compliance
- Cross-browser compatibility and progressive enhancement

**Available Tools**: view, edit, create, bash

**Use Cases**:
- Improving website accessibility and keyboard navigation
- Fixing responsive design issues across devices
- Enhancing UI/UX of existing pages
- Optimizing CSS architecture and performance
- Ensuring WCAG 2.1 AA compliance

---

### 2. Business Development Specialist (`business-development-specialist.md`)
**Focus**: Strategic Growth, Market Positioning, Client Acquisition

Expert in B2B business development for cybersecurity consulting services. Specializes in:
- Strategic business development and market analysis
- Cybersecurity consulting market knowledge
- Sales enablement and client acquisition
- Partnership development and channel strategies
- Market positioning and competitive differentiation

**Available Tools**: view, edit, search, bash, web

**Use Cases**:
- Developing go-to-market strategies
- Identifying target market segments and ideal customers
- Creating sales enablement materials
- Building partnership opportunities
- Optimizing website for lead generation and conversions

---

### 3. Political Analyst (`political-analyst.md`)
**Focus**: OSINT, Political Analysis, Information Operations

Expert in open source intelligence, political analysis, and ethical information operations. Specializes in:
- OSINT methodologies and collection frameworks
- Political analysis and risk assessment
- Strategic communication and influence operations
- Information warfare awareness and defense
- Data analysis and visualization for intelligence

**Available Tools**: view, edit, search, bash, web

**Use Cases**:
- Enhancing the Citizen Intelligence Agency project
- Developing political monitoring and analysis features
- Creating transparency and accountability metrics
- Building OSINT collection and analysis frameworks
- Designing ethical intelligence reporting systems

---

### 4. Marketing Specialist (`marketing-specialist.md`)
**Focus**: B2B Marketing, Content Strategy, Digital Marketing

Expert in B2B technology marketing for cybersecurity professional services. Specializes in:
- B2B technology marketing and demand generation
- Digital marketing, SEO, and content strategy
- Brand positioning and messaging development
- Content marketing and thought leadership
- Marketing analytics and performance optimization

**Available Tools**: view, edit, search, bash

**Use Cases**:
- Developing content marketing strategies
- Optimizing website for SEO and conversions
- Creating marketing collateral and messaging
- Building social media and thought leadership programs
- Designing demand generation campaigns

---

## How to Use These Profiles

These custom agent profiles are designed to be used with GitHub Copilot's coding agent to provide specialized, context-aware assistance. When you need help with a specific domain, you can select the appropriate agent from the dropdown in the Copilot prompt box.

### Invoking an Agent

1. Click in the Copilot prompt box
2. Select the agent from the dropdown menu that appears
3. Describe your task or question
4. The agent will respond with specialized expertise and use its configured tools

### Profile Structure

Each profile follows the GitHub Copilot custom agents format:

```markdown
---
name: agent-name
description: Brief description of capabilities
tools: ["tool1", "tool2", "tool3"]  # Optional
---

Agent instructions and behavior guidelines in Markdown...
```

**Components:**
1. **YAML Frontmatter**: Contains metadata (name, description, tools)
2. **Name**: Unique identifier in kebab-case
3. **Description**: Brief explanation of agent's capabilities
4. **Tools**: Optional list of allowed tools. If omitted, agent has access to all tools
5. **Instructions**: Markdown content defining behavior, expertise, and guidelines

---

## Creating New Agent Profiles

To create a new custom agent profile:

1. Create a new `.md` file in `.github/agents/` directory
2. Use kebab-case for the filename (e.g., `my-agent.md`)
3. Add YAML frontmatter with required properties:
   ```yaml
   ---
   name: my-agent
   description: Brief description of what the agent does
   tools: ["read", "edit", "search"]  # Optional
   ---
   ```
4. Write the agent's instructions in Markdown below the frontmatter
5. Commit the file to the repository
6. Refresh the Copilot agents dropdown to see your new agent

### Tool Configuration

**Tools property** defines which tools the agent can use:
- **Omit the property**: Agent has access to all available tools
- **Specify tools**: Limit agent to only the listed tools

Common tools include:
- `view`, `edit`, `create` - File operations
- `bash` - Command execution
- `search` - Code and repository search
- `web` - Web search capabilities (if enabled)
- `custom-agent` - Invoke other custom agents
- `todo` - Task management (if enabled)

Example limiting tools:
```yaml
tools: ["view", "edit", "bash"]
```

### Profile Alignment

### Profile Alignment

All agent profiles are aligned with Hack23's core values:
- **Transparency**: Open practices and honest communication
- **Practicality**: Real-world solutions that work
- **Expertise**: Deep technical knowledge and experience
- **Ethics**: Responsible and ethical practices
- **Quality**: High standards and attention to detail

### Profile Content Structure

Each profile typically includes:
1. **Core Expertise**: Deep domain knowledge and technical skills
2. **Project Context**: Understanding of Hack23 AB, its projects, and business model
3. **Responsibilities**: Specific tasks and areas of focus
4. **Frameworks & Methodologies**: Proven approaches and best practices
5. **Constraints & Guidelines**: What to do and what to avoid
6. **Success Metrics**: How to measure effectiveness
7. **Collaboration**: How to work with other specialists

---

## Project Context

### About Hack23 AB

Hack23 AB is a Swedish cybersecurity consulting company (Org.nr 5595347807) founded in 2025 by James Pether Sörling. The company focuses on:

- **Cybersecurity Consulting**: Practical security solutions for enterprise clients
- **Gaming Innovation**: Precision combat simulators with educational value
- **Transparency**: Public ISMS and open source contributions
- **Open Source Security**: Active development of security tools and platforms

### Technology Stack

- **Website**: Static HTML5/CSS3 website
- **Deployment**: AWS S3 + CloudFront via GitHub Actions
- **Languages**: English (primary), Swedish (`_sv`), Korean (`_ko`)
- **CI/CD**: Automated minification, Lighthouse audits, ZAP security scans

### Key Projects

1. **Black Trigram**: Realistic 2D precision combat simulator
2. **CIA Compliance Manager**: Security assessment platform
3. **Citizen Intelligence Agency**: OSINT platform for Swedish political transparency
4. **Lambda in Private VPC**: Multi-region resilient cloud architecture
5. **Sonar-CloudFormation Plugin**: IaC security scanning for SonarQube

---

## Agent Validation and Quality Standards

### YAML Frontmatter Validation

All custom agent profiles must have valid YAML frontmatter with these properties:

#### Required Properties
```yaml
name: agent-name           # Lowercase, hyphen-separated, unique identifier
description: Brief description (max 200 chars)
tools: ["tool1", "tool2"]  # Array of valid tool aliases
```

#### Tool Aliases (Official GitHub Copilot Names)

Use only these standardized tool aliases:

| Tool Alias | Purpose |
|------------|---------|
| `view` | Read file contents |
| `edit` | Modify file contents |
| `create` | Create new files |
| `bash` | Execute shell commands |
| `search` | Search code and repositories |
| `web` | Web search (if enabled) |
| `custom-agent` | Invoke other custom agents |
| `todo` | Task management (if enabled) |

**Important:** Do NOT use these incorrect aliases:
- ❌ `search_code` - Use `search` instead
- ❌ `search_repositories` - Use `search` instead  
- ❌ `web_search` - Use `web` instead
- ❌ `read` - Use `view` instead
- ❌ `shell` - Use `bash` instead

### Agent Naming Standards

**✅ Good Names:**
- `marketing-specialist` - Descriptive role with hyphen separation
- `ui-enhancement-specialist` - Clear purpose and function
- `business-development-specialist` - Domain expertise clear
- `political-analyst` - Area and role defined

**❌ Bad Names:**
- `agent1` - Generic, not descriptive
- `MyAgent` - Use lowercase with hyphens
- `marketing_specialist` - Use hyphens, not underscores
- `really-long-agent-name-that-is-too-verbose` - Keep concise

### Description Guidelines

- **Maximum 200 characters** (GitHub UI requirement)
- Clear and concise explanation of expertise
- Describes key capabilities and focus areas
- Professional tone appropriate for enterprise use
- Avoids jargon where possible

### Validation Checklist

Before committing a new or updated agent profile:

- [ ] Valid YAML syntax (no parsing errors)
- [ ] `name` follows kebab-case convention (lowercase, hyphens)
- [ ] `description` is under 200 characters
- [ ] `tools` array uses only valid aliases from the table above
- [ ] No extra or invalid properties in frontmatter
- [ ] Proper indentation (2 spaces for YAML)
- [ ] Agent prompt content is clear and well-structured
- [ ] Examples provided where helpful
- [ ] Tested with GitHub Copilot (if possible)

### Common Validation Errors

#### Error: Invalid Tool Alias
```yaml
# ❌ Wrong
tools: ["view", "edit", "search_code", "bash"]

# ✅ Correct
tools: ["view", "edit", "search", "bash"]
```

#### Error: Description Too Long
```yaml
# ❌ Wrong (over 200 chars)
description: This is a really long description that goes on and on explaining every single detail about what this agent can do and all the various capabilities it has which makes it way too long for the GitHub UI to handle properly

# ✅ Correct (under 200 chars)
description: Expert in B2B marketing, digital strategy, SEO, and demand generation for cybersecurity professional services
```

#### Error: Invalid Name Format
```yaml
# ❌ Wrong
name: Marketing_Specialist

# ✅ Correct
name: marketing-specialist
```

---

## Maintenance

These profiles should be updated when:
- New projects or services are launched
- Business strategy or positioning changes
- New technologies or methodologies are adopted
- Feedback indicates gaps or inaccuracies in agent guidance
- Regulatory or industry standards evolve
- GitHub Copilot tool aliases or standards change

Last updated: 2025-01-04

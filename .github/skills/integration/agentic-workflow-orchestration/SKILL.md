---
name: agentic-workflow-orchestration
description: Multi-agent coordination patterns, orchestrator-worker designs, and complex workflow orchestration for GitHub Agentic Workflows
license: Apache-2.0
---

# 🎭 Agentic Workflow Orchestration Skill

## Purpose

This skill provides comprehensive guidance on orchestrating multiple agentic workflows to solve complex problems through coordination, delegation, and parallel execution. Orchestration patterns enable systematic breakdown of large tasks into manageable units, efficient resource utilization, and robust error handling across distributed agent systems.

## When to Use

Apply this skill when:
- Breaking down complex automation into multiple coordinated workflows
- Implementing orchestrator-worker patterns for scalable task execution
- Coordinating multiple AI agents with different specializations
- Building hierarchical or graph-based workflow systems
- Managing parallel execution and result aggregation
- Implementing continuous AI at scale

## Rules

### Orchestration Fundamentals

**MUST:**
- Design orchestrators to coordinate, not execute
- Create focused workers with single responsibilities
- Use workflow dispatch for orchestrator-worker communication
- Implement clear contracts between orchestrator and workers
- Handle worker failures gracefully in orchestrators
- Aggregate and validate worker results
- Log orchestration decisions and outcomes

**MUST NOT:**
- Mix orchestration logic with execution logic
- Create overly complex orchestration hierarchies
- Ignore worker failures
- Create circular dependencies between workflows
- Skip result validation from workers

### Orchestrator Design

**MUST:**
- Keep orchestrators stateless when possible
- Use GitHub APIs to track worker status
- Implement retry logic for failed workers
- Provide clear success/failure criteria
- Generate summary reports of orchestrated work
- Scale workers horizontally, not vertically
- Document orchestration logic clearly

**MUST NOT:**
- Hard-code worker names or configurations
- Assume workers will always succeed
- Create long-running orchestrators (use scheduled checks instead)
- Tightly couple orchestrators to specific worker implementations

### Worker Design

**MUST:**
- Focus each worker on single, well-defined task
- Make workers independently testable
- Report clear success/failure status
- Provide detailed output for orchestrator consumption
- Handle edge cases locally
- Implement appropriate timeouts
- Use consistent output formats

**MUST NOT:**
- Create workers with multiple responsibilities
- Depend on other workers directly (use orchestrator)
- Assume orchestrator context
- Create workers that never finish
- Skip error reporting

### Communication Patterns

**MUST:**
- Use `workflow_dispatch` with inputs for orchestrator→worker communication
- Use issues, comments, or pull requests for worker→orchestrator communication
- Implement structured data formats (JSON, YAML) for inter-workflow communication
- Version communication protocols
- Validate all inter-workflow messages
- Document communication contracts

**MUST NOT:**
- Use file system for inter-workflow communication
- Trust unchecked data from other workflows
- Create hidden communication channels
- Skip message validation

### Parallel Execution

**MUST:**
- Dispatch independent workers in parallel
- Set appropriate concurrency limits
- Implement timeout handling for parallel workers
- Collect and validate results from all workers
- Handle partial success scenarios
- Track execution metrics (timing, success rates)

**MUST NOT:**
- Wait for workers sequentially when parallel execution is possible
- Create unbounded parallelism
- Ignore partial failures
- Assume workers complete in specific order

### Error Handling and Resilience

**MUST:**
- Implement circuit breakers for failing workers
- Use exponential backoff for retries
- Set maximum retry limits
- Log all failures with context
- Escalate persistent failures to humans
- Implement graceful degradation
- Maintain audit trail of orchestration decisions

**MUST NOT:**
- Retry indefinitely
- Hide failures from orchestrators
- Cascade failures without containment
- Skip logging of error conditions

## Orchestration Patterns

### Pattern 1: Simple Orchestrator-Worker

**Structure:**
- 1 orchestrator workflow
- N homogeneous worker workflows
- Workers execute identical tasks on different inputs

**Use Cases:**
- Batch processing (analyze all open issues)
- Parallel validation (test multiple configurations)
- Distributed scanning (security audit across repos)

### Pattern 2: Hierarchical Orchestration

**Structure:**
- Top-level orchestrator
- Mid-level specialized orchestrators
- Leaf-level execution workers

**Use Cases:**
- Complex multi-phase operations
- Different orchestration strategies per phase
- Nested task decomposition

### Pattern 3: Pipeline Orchestration

**Structure:**
- Orchestrator manages sequential stages
- Each stage has specialized workers
- Output of one stage feeds next stage

**Use Cases:**
- CI/CD pipelines
- Data processing pipelines
- Multi-step validation workflows

### Pattern 4: Router/Dispatcher

**Structure:**
- Router analyzes input and selects appropriate worker
- Heterogeneous workers with different capabilities
- Dynamic worker selection based on context

**Use Cases:**
- Issue triage (route to specialized handlers)
- Content moderation (route by content type)
- Multi-language support (route by language)

### Pattern 5: Map-Reduce

**Structure:**
- Map phase: Orchestrator spawns workers for each input
- Reduce phase: Orchestrator aggregates worker results
- Final report generation

**Use Cases:**
- Repository analysis across multiple repos
- Parallel testing with result aggregation
- Distributed data collection and synthesis

### Pattern 6: Reflection (Self-Improving)

**Structure:**
- Generator workflow produces output
- Critic workflow reviews and provides feedback
- Coordinator orchestrates iterations until quality threshold met

**Use Cases:**
- Documentation generation with quality review
- Code generation with security review
- Content creation with style validation

## Examples

### Example 1: Simple Orchestrator-Worker Pattern

**Orchestrator (`daily-orchestrator.md`):**
```markdown
---
on: daily
permissions: read-all
tools:
  github:
safe-outputs:
  create-issue:
    max: 1
---

# Daily Repository Orchestrator

Coordinate daily analysis across all open issues:

1. List all open issues in repository
2. For each issue, dispatch `issue-analyzer` worker workflow with issue number
3. Wait for all workers to complete (check workflow run statuses)
4. Collect results from worker comments
5. Generate summary report issue titled "Daily Analysis Report - [DATE]"

Include:
- Total issues analyzed
- Critical issues found
- Recommendations summary
- Links to worker analysis comments
```

**Worker (`issue-analyzer.md`):**
```markdown
---
on:
  workflow_dispatch:
    inputs:
      issue_number:
        required: true
        type: number
permissions: read-all
tools:
  github:
safe-outputs:
  create-comment:
    max: 1
---

# Issue Analyzer Worker

Analyze issue #${{ inputs.issue_number }}:

1. Read issue title, body, labels, and comments
2. Check for duplicates
3. Assess clarity and completeness
4. Identify missing information
5. Suggest appropriate labels

Post analysis as comment on the issue.
Use structured format:
- Status: [Clear/Unclear/Duplicate]
- Suggested Labels: [label1, label2]
- Action: [what should happen next]
```

### Example 2: Hierarchical Orchestration

**Top-Level Orchestrator (`repo-health-orchestrator.md`):**
```markdown
---
on: weekly on monday
permissions: read-all
tools:
  github:
safe-outputs:
  create-issue:
    max: 1
---

# Repository Health Orchestrator

Coordinate comprehensive repository health check:

Phase 1: Dispatch specialized orchestrators
1. Dispatch `issue-health-orchestrator`
2. Dispatch `pr-health-orchestrator`
3. Dispatch `code-health-orchestrator`

Phase 2: Wait and collect
1. Wait for all phase 1 orchestrators to complete
2. Collect results from each orchestrator issue

Phase 3: Synthesize
1. Combine results into master health report
2. Generate action items by priority
3. Create issue with complete repository health status
```

**Mid-Level Orchestrator (`issue-health-orchestrator.md`):**
```markdown
---
on:
  workflow_dispatch:
permissions: read-all
tools:
  github:
safe-outputs:
  create-issue:
    max: 1
---

# Issue Health Orchestrator

Coordinate issue-specific analysis:

1. Dispatch workers for:
   - Stale issue detection
   - Issue categorization
   - Response time analysis
   - Label consistency check

2. Collect worker results
3. Generate issue health report
4. Create issue with findings
```

### Example 3: Pipeline Orchestration

**Pipeline Orchestrator (`deployment-pipeline.md`):**
```markdown
---
on: workflow_dispatch
permissions: read-all
tools:
  github:
safe-outputs:
  create-comment:
    max: 5
---

# Deployment Pipeline Orchestrator

Coordinate deployment pipeline stages:

Stage 1: Validation
1. Dispatch `security-validator` worker
2. Dispatch `test-validator` worker
3. Wait for both, check results
4. If any failures, stop and report

Stage 2: Staging Deployment
1. Dispatch `staging-deployer` worker
2. Wait for completion
3. Dispatch `staging-validator` worker
4. If validation fails, rollback and stop

Stage 3: Production Deployment
1. Require manual approval (create approval issue)
2. After approval, dispatch `production-deployer` worker
3. Dispatch `production-validator` worker
4. Generate deployment report

Post progress comments at each stage.
```

### Example 4: Router/Dispatcher Pattern

**Router (`issue-router.md`):**
```markdown
---
on: issues
permissions: read-all
tools:
  github:
---

# Issue Router

Route new issues to specialized handlers:

1. Analyze issue labels and content
2. Determine issue type:
   - Bug → dispatch `bug-triage-worker`
   - Feature Request → dispatch `feature-triage-worker`
   - Security → dispatch `security-triage-worker`
   - Documentation → dispatch `docs-triage-worker`
   - General → dispatch `general-triage-worker`

3. Dispatch appropriate worker with issue number
4. Post comment indicating routing decision
```

### Example 5: Map-Reduce Pattern

**Map-Reduce Orchestrator (`security-audit-orchestrator.md`):**
```markdown
---
on: workflow_dispatch
permissions: read-all
tools:
  github:
safe-outputs:
  create-issue:
    max: 1
  create-code-scanning-alert:
    max: 1
---

# Security Audit Orchestrator (Map-Reduce)

Coordinate security audit across entire codebase:

MAP PHASE:
1. List all repositories in organization
2. For each repository, dispatch `security-scanner` worker
3. Track dispatched workers

REDUCE PHASE:
1. Wait for all scanners to complete
2. Collect SARIF reports from each worker
3. Aggregate findings:
   - Total vulnerabilities by severity
   - Top vulnerability types
   - Repositories with most issues
4. Generate consolidated SARIF report
5. Create master security issue with summary
```

### Example 6: Reflection Pattern

**Reflection Orchestrator (`doc-generator-orchestrator.md`):**
```markdown
---
on: workflow_dispatch
permissions: read-all
tools:
  github:
safe-outputs:
  create-pull-request:
    max: 1
---

# Documentation Generator with Reflection

Use reflection pattern for high-quality docs:

Iteration Loop (max 3 iterations):
1. Dispatch `doc-generator` worker to create documentation
2. Dispatch `doc-critic` worker to review generated docs
3. Collect critique feedback
4. If quality score >= 8/10, proceed to next step
5. If quality score < 8/10, regenerate with critique feedback

Final Step:
1. Create pull request with approved documentation
2. Include quality metrics in PR description
3. Link to critic reviews
```

### Example 7: Circuit Breaker Pattern

**Orchestrator with Circuit Breaker (`resilient-orchestrator.md`):**
```markdown
---
on: schedule
permissions: read-all
tools:
  github:
safe-outputs:
  create-issue:
    max: 1
---

# Resilient Orchestrator with Circuit Breaker

Coordinate workers with failure protection:

For each task in task_list:
  1. Check circuit breaker state for worker type
  2. If OPEN (too many recent failures), skip and log
  3. If CLOSED, dispatch worker
  4. Track worker success/failure
  5. Update circuit breaker state:
     - 3 consecutive failures → OPEN circuit
     - 1 success after OPEN → HALF-OPEN
     - 3 successes in HALF-OPEN → CLOSED

Generate report with:
- Tasks completed successfully
- Tasks skipped (circuit open)
- Circuit breaker states
- Recommended actions
```

### Example 8: Dynamic Worker Pool

**Dynamic Pool Orchestrator (`scalable-orchestrator.md`):**
```markdown
---
on: workflow_dispatch
permissions: read-all
tools:
  github:
safe-outputs:
  create-issue:
    max: 1
---

# Dynamic Worker Pool Orchestrator

Scale workers based on workload:

1. Assess workload size (e.g., count of items to process)
2. Calculate optimal worker count (workload / items_per_worker)
3. Respect concurrency limits (max 10 concurrent workers)
4. Batch items for each worker
5. Dispatch workers with batch assignments
6. Monitor worker progress
7. If workers fail, redistribute work to new workers
8. Aggregate results when all batches complete
9. Generate completion report with metrics:
   - Items processed
   - Workers used
   - Success rate
   - Processing time
```

## Best Practices

### Orchestrator Design
- Keep orchestration logic simple and linear
- Use timeouts to prevent infinite waiting
- Implement health checks for long-running coordination
- Log all orchestration decisions
- Generate human-readable summary reports

### Worker Design
- Make workers idempotent (safe to retry)
- Include worker ID in outputs for traceability
- Report progress for long-running workers
- Use consistent success/failure signals
- Minimize external dependencies

### Communication
- Use structured data (JSON/YAML) for all inter-workflow data
- Version communication protocols
- Validate all inputs from other workflows
- Document communication contracts clearly

### Testing
- Test workers independently before orchestration
- Test orchestrator with mock worker responses
- Test failure scenarios (timeouts, errors)
- Test partial success scenarios
- Load test with realistic workloads

### Monitoring
- Track orchestration execution time
- Monitor worker success rates
- Alert on orchestration failures
- Measure end-to-end latency
- Dashboard key metrics

## Troubleshooting

### Workers Not Completing
- Check worker timeout settings
- Review worker logs for errors
- Verify worker dispatch succeeded
- Check GitHub Actions queue status
- Implement worker health checks

### Orchestration Hangs
- Verify timeout logic in orchestrator
- Check for circular dependencies
- Review worker status polling logic
- Ensure failure cases are handled

### Inconsistent Results
- Verify worker idempotency
- Check for race conditions
- Review result aggregation logic
- Validate worker communication format

### Performance Issues
- Optimize worker batch sizes
- Increase parallelism if possible
- Review orchestrator polling frequency
- Consider worker caching strategies

## Related ISMS Policies

This skill aligns with:

- **[Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md)** - Secure orchestration practices
- **[Change Management Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Change_Management_Policy.md)** - Coordinated deployment patterns
- **[Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)** - Overall security framework

## Related Skills

- **[GitHub Agentic Workflows](../github-agentic-workflows/SKILL.md)** - Core workflow fundamentals
- **[Agentic Workflow Security](../agentic-workflow-security/SKILL.md)** - Security for orchestrated workflows
- **[Agentic Workflow Development](../agentic-workflow-development/SKILL.md)** - Development and testing
- **[Copilot Agent Patterns](../copilot-agent-patterns/SKILL.md)** - Custom agent patterns

## Related Documentation

- [GitHub Agentic Workflows Orchestration Guide](https://github.github.com/gh-aw/patterns/orchestration/)
- [GitHub Actions Reusable Workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows)

## Compliance Mapping

### ISO 27001:2022
- **A.8.25** Secure development life cycle
- **A.8.32** Change management
- **A.5.37** Documented operating procedures

### NIST Cybersecurity Framework 2.0
- **PR.IP-02**: A System Development Life Cycle is implemented
- **PR.MA-01**: Maintenance is performed
- **DE.AE-03**: Event data is collected and correlated

### CIS Controls v8.1
- **Control 16**: Application Software Security
  - 16.1 Establish Secure Development Process
  - 16.14 Establish Remediation Processes

## Enforcement

Orchestration pattern violations:
- **Critical**: Circular dependencies, infinite loops - Block deployment
- **High**: Missing error handling, no timeouts - Require remediation
- **Medium**: Suboptimal patterns, missing monitoring - Create improvement tickets
- **Low**: Documentation gaps, optimization opportunities - Optional improvements

## Version History

- **2026-02-11**: Initial skill creation based on latest orchestration patterns and best practices

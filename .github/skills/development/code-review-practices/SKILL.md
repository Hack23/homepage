---
name: code-review-practices
description: Code review best practices, quality gates, security checks, and constructive feedback guidelines for collaborative development
license: Apache-2.0
---

# Code Review Practices Skill

## Purpose

Establishes effective code review practices that improve code quality, share knowledge, catch bugs early, and maintain security standards while fostering collaborative development culture.

## Rules

### Code Review Principles (MUST Follow)

**Core Principles:**
```markdown
1. Respectful Communication
   - Focus on code, not the person
   - Ask questions, don't make demands
   - Provide constructive suggestions
   - Acknowledge good work

2. Timeliness
   - Review within 24 hours
   - Small PRs reviewed faster
   - Block releases for critical issues only
   - Don't let PRs go stale

3. Thoroughness
   - Understand the context
   - Test the changes locally
   - Check for side effects
   - Verify all review points

4. Continuous Learning
   - Explain reasoning behind feedback
   - Share knowledge and best practices
   - Learn from others' approaches
   - Iterate on review process
```

### What to Review

**MUST CHECK:**
```markdown
1. Functionality
   ✓ Code solves the stated problem
   ✓ Edge cases handled
   ✓ Error handling present
   ✓ No obvious bugs
   ✓ Follows requirements

2. Design & Architecture
   ✓ Appropriate abstraction level
   ✓ Follows project patterns
   ✓ No unnecessary complexity
   ✓ Proper separation of concerns
   ✓ Scalable approach

3. Code Quality
   ✓ Readable and maintainable
   ✓ Follows style guide
   ✓ DRY (Don't Repeat Yourself)
   ✓ Appropriate naming
   ✓ No magic numbers
   ✓ Commented where needed

4. Testing
   ✓ Unit tests included
   ✓ Integration tests if needed
   ✓ Test coverage adequate
   ✓ Tests are meaningful
   ✓ Edge cases tested

5. Security
   ✓ No hardcoded secrets
   ✓ Input validation present
   ✓ SQL injection prevention
   ✓ XSS protection
   ✓ Authentication/authorization checks
   ✓ Secure dependencies

6. Performance
   ✓ No obvious inefficiencies
   ✓ Database queries optimized
   ✓ Caching where appropriate
   ✓ No memory leaks
   ✓ Async operations used properly

7. Documentation
   ✓ README updated if needed
   ✓ API documentation updated
   ✓ Complex logic explained
   ✓ Breaking changes noted
```

### Review Process

**Pull Request Author:**
```markdown
Before Requesting Review:
1. Self-review your changes
2. Run tests locally
3. Run linter/formatter
4. Write clear PR description
5. Link related issues
6. Tag appropriate reviewers
7. Mark as draft if work-in-progress

PR Description Template:
## Changes
- [Bullet list of changes made]

## Why
[Explanation of motivation]

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed

## Screenshots (if UI changes)
[Before/after screenshots]

## Checklist
- [ ] Code follows style guide
- [ ] Tests passing
- [ ] Documentation updated
- [ ] No secrets committed
```

**Reviewer:**
```markdown
Review Steps:
1. Read PR description and linked issues
2. Understand the context and goals
3. Review code changes in logical order
4. Check out branch and test locally
5. Run automated checks (tests, linter)
6. Leave inline comments for specific issues
7. Provide summary comment
8. Approve, Request Changes, or Comment

Comment Types:
- **MUST FIX**: Blocking issue (security, bug, breaking)
- **SHOULD FIX**: Important but not blocking
- **NIT**: Nitpick, style preference
- **QUESTION**: Clarification needed
- **SUGGESTION**: Alternative approach
- **PRAISE**: Good work, clever solution
```

### Feedback Guidelines

**Effective Comments:**
```markdown
❌ BAD: "This is wrong."
✅ GOOD: "This could cause a race condition when multiple users 
         access the cache simultaneously. Consider using a lock
         or atomic operation."

❌ BAD: "Why did you do it this way?"
✅ GOOD: "Have you considered using Array.map() here? It might be
         more readable and is functionally equivalent."

❌ BAD: "This is terrible naming."
✅ GOOD: "Could we rename 'tmp' to 'temporaryUserData' for clarity?
         It would help future maintainers understand the purpose."
```

**Praise Effectively:**
```markdown
✅ "Great use of dependency injection here! Makes this very testable."
✅ "I like how you extracted this into a separate function. Much cleaner."
✅ "Excellent test coverage of edge cases!"
✅ "This optimization is impressive. Nice catch!"
```

### Code Review Anti-Patterns

**AVOID:**
```markdown
1. Rubber Stamping
   - Approving without thorough review
   - "LGTM" without understanding changes
   - Skipping testing locally

2. Nitpicking Without Value
   - Focusing only on style (use automated tools)
   - Personal preferences without reasoning
   - Arguing about subjective choices

3. Review Hostility
   - Hostile or condescending tone
   - Dismissing author's approach without discussion
   - Making it personal

4. Perfectionism
   - Holding up PR for minor issues
   - Requesting unnecessary refactors
   - Scope creep in review

5. Review Overload
   - PRs too large to review effectively
   - Too many reviewers required
   - Review fatigue
```

### Pull Request Size Guidelines

**MUST:**
```markdown
Target Sizes:
- Small: < 200 lines changed (ideal)
- Medium: 200-500 lines (acceptable)
- Large: 500-1000 lines (split if possible)
- XL: > 1000 lines (must split)

For Large Changes:
1. Break into smaller, logical PRs
2. Use feature flags for incremental merges
3. Create base branch for related PRs
4. Document overall design in RFC/issue

Exceptions (acceptable large PRs):
- Generated code
- Configuration updates
- Dependency bumps
- Data migrations
```

### Security-Focused Review

**MUST CHECK:**
```markdown
Authentication & Authorization:
✓ Authentication required for protected endpoints
✓ Authorization checks before resource access
✓ No role/permission bypass vulnerabilities
✓ Session management secure

Input Validation:
✓ All user input validated
✓ SQL injection prevention (parameterized queries)
✓ XSS prevention (output encoding)
✓ Path traversal prevention
✓ File upload validation

Sensitive Data:
✓ No secrets in code
✓ No API keys committed
✓ Sensitive data encrypted at rest
✓ PII handled per GDPR
✓ Secure logging (no passwords/tokens in logs)

Dependencies:
✓ npm audit / pip-audit passed
✓ No known vulnerable dependencies
✓ Dependencies from trusted sources
✓ Lock files updated

Example Security Comment:
"⚠️ SECURITY: This endpoint allows unauthenticated access to user
data. We need to add authentication middleware and verify the user
has permission to access this resource. See access-control SKILL.md
for implementation pattern."
```

### Automated Review Checks

**CI/CD Integration:**
```yaml
# .github/workflows/pr-checks.yml
name: PR Checks

on: [pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Lint
        run: npm run lint
      
      - name: Unit Tests
        run: npm run test:unit -- --coverage
      
      - name: Security Scan
        run: npm audit --audit-level=moderate
      
      - name: Code Coverage
        uses: codecov/codecov-action@v4
        with:
          fail_ci_if_error: true
          min_coverage: 80
      
      - name: CodeQL Analysis
        uses: github/codeql-action/analyze@v3
      
      - name: Lighthouse CI
        run: npm run lighthouse:ci
```

**Branch Protection Rules:**
```markdown
MUST ENFORCE:
- ✓ Require pull request reviews (at least 1)
- ✓ Require status checks to pass
- ✓ Require branches to be up to date
- ✓ Require conversation resolution
- ✓ No force push
- ✓ No deletion
- ✓ Include administrators
```

### Review Approval Process

**Approval Criteria:**
```markdown
✅ APPROVE when:
- All MUST FIX issues resolved
- Tests passing
- Security checks pass
- No outstanding questions
- Code meets quality standards

💬 COMMENT when:
- Need clarification
- Have suggestions but not blocking
- Want to share knowledge
- Acknowledge good work

🔄 REQUEST CHANGES when:
- Critical bugs found
- Security vulnerabilities
- Breaking changes without discussion
- Tests missing or failing
- Major design concerns
```

### Review Metrics & Improvement

**TRACK:**
```markdown
Review Efficiency:
- Time to first review
- Time to merge after approval
- Number of review rounds
- PR size distribution

Review Quality:
- Bugs caught in review
- Bugs found in production
- Test coverage trends
- Security issues prevented

Team Health:
- Review participation distribution
- Review comment sentiment
- Knowledge sharing occurrences
- Team satisfaction with process
```

## Examples

### Exemplary Review Comments

**Functionality Issue:**
```markdown
🐛 **Bug**: This will fail when `user.profile` is null. We should add
a null check or use optional chaining:

const email = user.profile?.email || 'no-email@example.com';

This handles the null case gracefully and prevents runtime errors.
```

**Performance Suggestion:**
```markdown
⚡ **Performance**: This loops through users twice (filter then map).
We could combine into a single pass:

const activeUserEmails = users
  .filter(u => u.active)
  .map(u => u.email);

Could become:

const activeUserEmails = users.reduce((emails, u) => {
  if (u.active) emails.push(u.email);
  return emails;
}, []);

Though honestly, for small arrays the original is more readable. What's
the expected size of the users array?
```

**Security Issue:**
```markdown
🔒 **SECURITY**: This SQL query is vulnerable to injection:

const query = `SELECT * FROM users WHERE email = '${email}'`;

We must use parameterized queries:

const query = 'SELECT * FROM users WHERE email = $1';
const result = await db.query(query, [email]);

See our secure-development SKILL.md for more examples.
```

**Praise:**
```markdown
✨ Really nice abstraction here! Extracting this logic into a reusable
utility function makes it testable and DRY. The naming is also very
clear. Great work! 🎉
```

### PR Description Template
```markdown
## Summary
[Brief description of what this PR accomplishes]

## Related Issues
Closes #123
Related to #456

## Changes Made
- Added user authentication middleware
- Implemented JWT token validation
- Added unit tests for auth flow
- Updated API documentation

## Type of Change
- [ ] Bug fix
- [x] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing Performed
- [x] Unit tests (95% coverage)
- [x] Integration tests
- [x] Manual testing on staging
- [ ] E2E tests (not applicable)

## Screenshots (if applicable)
[Before/After screenshots for UI changes]

## Checklist
- [x] Code follows style guide
- [x] Self-reviewed code
- [x] Commented complex code
- [x] Updated documentation
- [x] No new warnings
- [x] Added tests
- [x] All tests passing
- [x] No secrets committed
- [x] CHANGELOG updated (if applicable)

## Deployment Notes
[Any special deployment steps or configuration changes needed]

## Rollback Plan
[How to rollback if issues arise in production]
```

## Related Policies

- [Secure Development SKILL](../../security/secure-development/SKILL.md)
- [Testing Strategy SKILL](../testing-strategy/SKILL.md)
- [Access Control SKILL](../../security/access-control/SKILL.md)

## Related Documentation

- [george-dorn Agent](../../../agents/george-dorn.md)
- [simon-moon Agent](../../../agents/simon-moon.md)

## Tools

**Code Review:**
- GitHub Pull Requests
- GitLab Merge Requests
- Gerrit
- Phabricator

**Automated Checks:**
- GitHub Actions
- CodeQL
- SonarQube
- Codecov

**Code Quality:**
- ESLint, Prettier
- pylint, black
- RuboCop
- Checkstyle

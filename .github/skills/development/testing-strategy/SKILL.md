---
name: testing-strategy
description: Comprehensive testing strategy covering unit, integration, E2E, security, accessibility, and performance testing for web applications
license: Apache-2.0
---

# Testing Strategy Skill

## Purpose

Defines comprehensive testing approaches for web applications, ensuring code quality, security, accessibility, and performance through automated and manual testing practices.

## Rules

### Testing Pyramid (MUST Follow)

```markdown
         /\
        /E2E\       ← Few, slow, expensive (UI tests)
       /------\
      /Integration\ ← More, moderate speed (API, DB tests)
     /------------\
    /   Unit Tests  \ ← Many, fast, cheap (function/method tests)
   /------------------\
```

**Distribution:**
- 70% Unit Tests (fast, isolated, many)
- 20% Integration Tests (moderate speed, component interaction)
- 10% E2E Tests (slow, full user journeys)

### Unit Testing Standards

**MUST:**
```markdown
Coverage Requirements:
- Minimum 80% code coverage
- 100% coverage for critical paths
- Test all public APIs
- Test error handling
- Test edge cases

Test Structure (AAA Pattern):
// Arrange - Set up test data
const user = { name: 'Alice', role: 'admin' };

// Act - Execute the code under test
const result = validateUser(user);

// Assert - Verify the outcome
expect(result.valid).toBe(true);
```

**JavaScript/TypeScript (Jest):**
```javascript
describe('UserValidator', () => {
  describe('validateEmail', () => {
    it('should accept valid email addresses', () => {
      expect(validateEmail('user@example.com')).toBe(true);
    });

    it('should reject invalid email addresses', () => {
      expect(validateEmail('invalid-email')).toBe(false);
    });

    it('should handle null input gracefully', () => {
      expect(validateEmail(null)).toBe(false);
    });
  });
});
```

**Python (pytest):**
```python
class TestUserValidator:
    def test_validate_email_accepts_valid_addresses(self):
        assert validate_email('user@example.com') is True
    
    def test_validate_email_rejects_invalid_addresses(self):
        assert validate_email('invalid-email') is False
    
    def test_validate_email_handles_none(self):
        assert validate_email(None) is False
```

### Integration Testing

**MUST TEST:**
```markdown
Component Integration:
- Database queries and transactions
- API endpoint functionality
- External service integration
- Cache behavior
- Message queue processing

API Testing Example (Supertest):
describe('POST /api/users', () => {
  it('should create new user with valid data', async () => {
    const response = await request(app)
      .post('/api/users')
      .send({ email: 'test@example.com', name: 'Test' })
      .expect(201);
    
    expect(response.body).toHaveProperty('id');
    expect(response.body.email).toBe('test@example.com');
  });
});
```

### End-to-End (E2E) Testing

**Critical User Journeys:**
```markdown
Web Applications:
- User registration and login
- Core feature workflows
- Checkout and payment flows
- Form submissions
- File uploads/downloads

Playwright Example:
test('user can complete checkout', async ({ page }) => {
  await page.goto('/shop');
  await page.click('[data-testid="add-to-cart"]');
  await page.click('[data-testid="checkout"]');
  await page.fill('[name="email"]', 'test@example.com');
  await page.fill('[name="card"]', '4242424242424242');
  await page.click('button[type="submit"]');
  
  await expect(page.locator('.success-message')).toBeVisible();
});
```

### Security Testing

**MUST INCLUDE:**
```markdown
1. Static Analysis Security Testing (SAST)
   - CodeQL scanning
   - SonarQube security rules
   - Bandit (Python), ESLint security plugins

2. Dependency Scanning
   - npm audit / pip-audit
   - Dependabot alerts
   - OWASP Dependency-Check

3. Dynamic Analysis Security Testing (DAST)
   - OWASP ZAP scans
   - Burp Suite Professional
   - Penetration testing

4. Common Vulnerabilities
   - SQL Injection tests
   - XSS (Cross-Site Scripting) tests
   - CSRF protection verification
   - Authentication/authorization tests
   - Input validation tests
```

**Security Test Example:**
```javascript
describe('Authentication Security', () => {
  it('should prevent SQL injection in login', async () => {
    const maliciousInput = "admin' OR '1'='1";
    const response = await request(app)
      .post('/api/login')
      .send({ username: maliciousInput, password: 'test' })
      .expect(401);
  });

  it('should protect against XSS in user input', () => {
    const xssPayload = '<script>alert("XSS")</script>';
    const sanitized = sanitizeInput(xssPayload);
    expect(sanitized).not.toContain('<script>');
  });
});
```

### Accessibility Testing

**MUST TEST:**
```markdown
WCAG 2.1 AA Compliance:
- Keyboard navigation (Tab, Enter, Esc, Arrow keys)
- Screen reader compatibility
- Color contrast ratios (4.5:1 normal, 3:1 large text)
- Form labels and ARIA attributes
- Focus management
- Semantic HTML

Automated Tools:
- axe-core (Playwright axe, Jest axe)
- Lighthouse accessibility audits
- Pa11y

Manual Testing:
- Keyboard-only navigation
- Screen reader testing (NVDA, JAWS, VoiceOver)
- Zoom to 200% without horizontal scroll
- Tab order verification
```

**Accessibility Test Example:**
```javascript
import { injectAxe, checkA11y } from 'axe-playwright';

test('page should be accessible', async ({ page }) => {
  await page.goto('/');
  await injectAxe(page);
  await checkA11y(page, null, {
    detailedReport: true,
    detailedReportOptions: { html: true }
  });
});
```

### Performance Testing

**MUST MEASURE:**
```markdown
Core Web Vitals:
- LCP (Largest Contentful Paint) < 2.5s
- FID (First Input Delay) < 100ms
- CLS (Cumulative Layout Shift) < 0.1

Load Testing:
- Response time under normal load
- Response time under peak load
- Throughput (requests/second)
- Error rate under load
- Resource utilization (CPU, memory)

Tools:
- Lighthouse performance audits
- k6 load testing
- Apache JMeter
- WebPageTest
```

**Performance Test Example (k6):**
```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '2m', target: 100 }, // Ramp up
    { duration: '5m', target: 100 }, // Stay at peak
    { duration: '2m', target: 0 },   // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% under 500ms
  },
};

export default function () {
  const response = http.get('https://api.example.com/data');
  check(response, {
    'status is 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500,
  });
  sleep(1);
}
```

### Test Data Management

**MUST:**
```markdown
Test Data Strategies:
1. Fixtures - Static test data files
2. Factories - Programmatic test data generation
3. Mocks - Simulated external dependencies
4. Stubs - Predefined responses
5. Test Doubles - Replacements for real objects

Example (Jest factory):
const userFactory = (overrides = {}) => ({
  id: faker.datatype.uuid(),
  email: faker.internet.email(),
  name: faker.name.fullName(),
  role: 'user',
  createdAt: new Date(),
  ...overrides
});

const adminUser = userFactory({ role: 'admin' });
```

### Continuous Integration Testing

**CI Pipeline:**
```yaml
# GitHub Actions example
name: Test Suite

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run linter
        run: npm run lint
      
      - name: Run unit tests
        run: npm run test:unit -- --coverage
      
      - name: Run integration tests
        run: npm run test:integration
      
      - name: Run E2E tests
        run: npm run test:e2e
      
      - name: Security scan
        run: npm audit
      
      - name: Lighthouse CI
        run: npm run lighthouse:ci
      
      - name: Upload coverage
        uses: codecov/codecov-action@v4
```

### Test Documentation

**MUST DOCUMENT:**
```markdown
Test Plan:
- Scope and objectives
- Test types and strategies
- Entry/exit criteria
- Test environments
- Responsibilities
- Schedule and milestones

Test Cases:
- Test ID and name
- Prerequisites
- Test steps
- Expected results
- Actual results
- Pass/Fail status

Example:
## TC-001: User Login with Valid Credentials

**Preconditions**: User account exists in test database

**Steps**:
1. Navigate to /login
2. Enter valid email: test@example.com
3. Enter valid password: TestPass123!
4. Click "Login" button

**Expected**: User redirected to dashboard, see welcome message

**Priority**: High
**Type**: Integration
```

## Examples

### Test Suite Structure
```
tests/
├── unit/
│   ├── utils/
│   │   ├── validation.test.js
│   │   └── formatting.test.js
│   └── services/
│       └── user-service.test.js
├── integration/
│   ├── api/
│   │   ├── users.test.js
│   │   └── auth.test.js
│   └── database/
│       └── queries.test.js
├── e2e/
│   ├── user-flows/
│   │   ├── registration.spec.js
│   │   └── checkout.spec.js
│   └── accessibility/
│       └── wcag.spec.js
├── security/
│   └── vulnerabilities.test.js
└── performance/
    └── load-test.js
```

## Related Policies

- [Secure Development SKILL](../../security/secure-development/SKILL.md)
- [Accessibility WCAG SKILL](../../quality/accessibility-wcag/SKILL.md)
- [Code Review Practices SKILL](../code-review-practices/SKILL.md)

## Related Documentation

- [george-dorn Agent](../../../agents/george-dorn.md)

## Tools

**Unit/Integration:**
- Jest (JavaScript/TypeScript)
- pytest (Python)
- JUnit (Java)
- RSpec (Ruby)

**E2E:**
- Playwright
- Cypress
- Selenium WebDriver

**Security:**
- OWASP ZAP
- CodeQL
- Snyk

**Accessibility:**
- axe-core
- Pa11y
- Lighthouse

**Performance:**
- k6
- Apache JMeter
- Lighthouse CI

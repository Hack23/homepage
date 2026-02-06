---
name: api-documentation
description: API documentation standards using OpenAPI/Swagger, including endpoints, authentication, examples, and error handling
license: Apache-2.0
---

# API Documentation Skill

## Purpose

Provides comprehensive API documentation that enables developers to quickly understand and integrate with APIs through clear examples, authentication guidance, and error handling.

## Rules

### OpenAPI/Swagger Specification

**MUST USE OpenAPI 3.0+:**
```yaml
openapi: 3.0.0
info:
  title: Hack23 API
  version: 1.0.0
  description: Cybersecurity services API
  contact:
    email: api@hack23.com
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0.html

servers:
  - url: https://api.hack23.com/v1
    description: Production
  - url: https://staging-api.hack23.com/v1
    description: Staging

paths:
  /users:
    get:
      summary: List users
      operationId: listUsers
      tags: [Users]
      security:
        - bearerAuth: []
      parameters:
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'
        '401':
          $ref: '#/components/responses/Unauthorized'

components:
  schemas:
    User:
      type: object
      required: [id, email]
      properties:
        id:
          type: string
          format: uuid
        email:
          type: string
          format: email
  
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
```

### API Reference Structure

**MUST INCLUDE:**
```markdown
1. Overview & Getting Started
   - What the API does
   - Base URL
   - Authentication
   - Rate limits
   - Quick start example

2. Authentication
   - How to obtain credentials
   - How to authenticate requests
   - Token refresh process
   - Security best practices

3. Endpoints
   - HTTP method and path
   - Description
   - Request parameters
   - Request body schema
   - Response schema
   - Error responses
   - Code examples

4. Error Handling
   - Error code list
   - Error response format
   - Common errors
   - Troubleshooting

5. SDKs & Libraries
   - Official SDK links
   - Community libraries
   - Code samples

6. Changelog
   - Version history
   - Breaking changes
   - Migration guides
```

### Code Examples

**MUST PROVIDE examples in:**
- cURL
- JavaScript/Node.js
- Python
- (Other popular languages as needed)

**Example:**
```markdown
## Create User

`POST /users`

Creates a new user account.

### Request Body
```json
{
  "email": "user@example.com",
  "name": "John Doe"
}
```

### Example Request (cURL)
```bash
curl -X POST https://api.hack23.com/v1/users \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","name":"John Doe"}'
```

### Example Request (JavaScript)
```javascript
const response = await fetch('https://api.hack23.com/v1/users', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    email: 'user@example.com',
    name: 'John Doe'
  })
});
const user = await response.json();
```

### Response (201 Created)
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "email": "user@example.com",
  "name": "John Doe",
  "createdAt": "2026-02-06T10:00:00Z"
}
```
```

### Error Documentation

**Standard Error Format:**
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid email format",
    "details": [
      {
        "field": "email",
        "message": "Must be a valid email address"
      }
    ],
    "requestId": "req_123456",
    "timestamp": "2026-02-06T10:00:00Z"
  }
}
```

## Related Policies

- [Secure Development SKILL](../../security/secure-development/SKILL.md)
- [Documentation Portfolio SKILL](../../architecture/documentation-portfolio/SKILL.md)

## Related Documentation

- [simon-moon Agent](../../../agents/simon-moon.md)

## Tools

- Swagger UI
- ReDoc
- Postman
- Insomnia

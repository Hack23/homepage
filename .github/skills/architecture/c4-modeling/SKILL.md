---
name: c4-modeling
description: C4 model (Context, Container, Component, Code) diagram patterns with Mermaid syntax for architecture documentation
license: Apache-2.0
---

# C4 Model Skill

## Purpose

This skill provides guidance on creating C4 (Context, Container, Component, Code) model diagrams using Mermaid syntax for architecture documentation. C4 models provide a hierarchical way to visualize software architecture at different levels of abstraction, following Simon Brown's C4 model methodology.

## Rules

### C4 Model Levels

The C4 model consists of four levels of abstraction:

1. **Level 1: System Context** - Shows how the system fits into its environment
2. **Level 2: Container** - Shows the high-level technology choices and communication between containers
3. **Level 3: Component** - Shows how containers are decomposed into components
4. **Level 4: Code** - Shows implementation details (optional, often better shown in IDEs)

### When to Use Each Level

**System Context Diagram - MUST USE:**
- When documenting a new system
- To show system boundaries
- To identify users and external dependencies
- In architecture decision records
- In system documentation home page

**Container Diagram - MUST USE:**
- For all systems with multiple deployable units
- To show technology stack
- To document inter-container communication
- For security architecture (trust boundaries)
- In deployment documentation

**Component Diagram - SHOULD USE:**
- For complex containers with many components
- When explaining internal structure
- For onboarding new developers
- For technical debt analysis

**Code Diagram - RARELY USE:**
- Only for explaining specific complex patterns
- Better suited for IDE visualization
- Consider UML class diagrams instead

### Documentation Requirements

**MUST:**
- Create both CURRENT and FUTURE state diagrams (ARCHITECTURE.md and FUTURE_ARCHITECTURE.md)
- Include title, description, and key for each diagram
- Use consistent notation across diagrams
- Document relationships between elements
- Include technologies used
- Version diagrams when architecture changes
- Keep diagrams up-to-date with code changes

**MUST NOT:**
- Create overly detailed diagrams (focus on key elements)
- Mix different abstraction levels in same diagram
- Omit technology choices from Container diagrams
- Use ambiguous relationship labels

### Mermaid Syntax for C4 Diagrams

Mermaid supports C4 diagrams through the `C4Context`, `C4Container`, and `C4Component` directives.

## Examples

### Example 1: System Context Diagram

```mermaid
C4Context
    title System Context Diagram for Hack23 CIA Platform

    Person(user, "Political Analyst", "A user analyzing political data")
    Person(admin, "Administrator", "Manages the system")
    
    System(cia, "Citizen Intelligence Agency", "Provides political data analysis and visualization")
    
    System_Ext(riksdagen, "Riksdagen API", "Swedish Parliament open data")
    System_Ext(worldbank, "World Bank API", "Global economic indicators")
    System_Ext(github, "GitHub API", "Politician activity tracking")
    System_Ext(auth, "OAuth Provider", "Authentication service")
    
    Rel(user, cia, "Uses", "HTTPS")
    Rel(admin, cia, "Administers", "HTTPS")
    Rel(cia, riksdagen, "Fetches data from", "HTTPS/REST")
    Rel(cia, worldbank, "Fetches data from", "HTTPS/REST")
    Rel(cia, github, "Tracks activity via", "HTTPS/REST")
    Rel(cia, auth, "Authenticates via", "OAuth 2.0")
    
    UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="1")
```

### Example 2: Container Diagram

```mermaid
C4Container
    title Container Diagram for Hack23 CIA Platform

    Person(user, "Political Analyst", "Analyzes political data")
    
    System_Boundary(cia, "Citizen Intelligence Agency") {
        Container(web, "Web Application", "React, JavaScript", "Provides political analysis UI")
        Container(api, "API Application", "Spring Boot, Java", "Provides data via REST API")
        Container(worker, "Background Worker", "Java", "Processes data updates")
        ContainerDb(db, "Database", "PostgreSQL", "Stores political data, analytics")
        ContainerDb(cache, "Cache", "Redis", "Caches frequently accessed data")
        Container(search, "Search Engine", "Elasticsearch", "Full-text search")
    }
    
    System_Ext(riksdagen, "Riksdagen API", "Parliament data")
    System_Ext(cdn, "CloudFront CDN", "Static content delivery")
    System_Ext(auth, "Auth0", "Authentication")
    
    Rel(user, web, "Uses", "HTTPS")
    Rel(user, cdn, "Loads static assets", "HTTPS")
    Rel(web, api, "Makes API calls", "HTTPS/REST")
    Rel(web, auth, "Authenticates", "OAuth 2.0")
    Rel(api, db, "Reads/Writes", "JDBC/SSL")
    Rel(api, cache, "Reads/Writes", "Redis Protocol")
    Rel(api, search, "Queries", "HTTPS/REST")
    Rel(worker, riksdagen, "Fetches data", "HTTPS/REST")
    Rel(worker, db, "Writes", "JDBC/SSL")
    
    UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="1")
```

### Example 3: Component Diagram

```mermaid
C4Component
    title Component Diagram for CIA API Application

    Container(web, "Web Application", "React", "UI for political analysis")
    Container(worker, "Background Worker", "Java", "Data processing")
    ContainerDb(db, "Database", "PostgreSQL", "Data storage")
    
    Container_Boundary(api, "API Application") {
        Component(auth, "Authentication Controller", "Spring Security", "Handles authentication/authorization")
        Component(politician, "Politician Controller", "Spring MVC", "Manages politician data")
        Component(vote, "Vote Controller", "Spring MVC", "Manages voting records")
        Component(analytics, "Analytics Controller", "Spring MVC", "Provides analytics data")
        
        Component(politicianService, "Politician Service", "Spring Bean", "Business logic for politicians")
        Component(voteService, "Vote Service", "Spring Bean", "Business logic for votes")
        Component(analyticsService, "Analytics Service", "Spring Bean", "Calculates analytics")
        
        Component(dataAccess, "Data Access Layer", "Spring Data JPA", "Database access")
        Component(cacheLayer, "Cache Layer", "Spring Cache", "Caching abstraction")
    }
    
    Rel(web, auth, "Authenticates", "HTTPS/REST")
    Rel(web, politician, "Gets politician data", "HTTPS/REST")
    Rel(web, vote, "Gets voting records", "HTTPS/REST")
    Rel(web, analytics, "Gets analytics", "HTTPS/REST")
    
    Rel(politician, politicianService, "Uses")
    Rel(vote, voteService, "Uses")
    Rel(analytics, analyticsService, "Uses")
    
    Rel(politicianService, dataAccess, "Uses")
    Rel(voteService, dataAccess, "Uses")
    Rel(analyticsService, dataAccess, "Uses")
    
    Rel(politicianService, cacheLayer, "Uses")
    Rel(voteService, cacheLayer, "Uses")
    
    Rel(dataAccess, db, "Reads/Writes", "JDBC")
    Rel(worker, dataAccess, "Writes data")
    
    UpdateLayoutConfig($c4ShapeInRow="4", $c4BoundaryInRow="1")
```

### Example 4: Simple Homepage Container Diagram

```mermaid
C4Container
    title Container Diagram for Hack23 Homepage

    Person(visitor, "Visitor", "Someone browsing the website")
    
    System_Boundary(homepage, "Hack23 Homepage") {
        Container(web, "Static Website", "HTML/CSS/JavaScript", "Corporate website")
    }
    
    System_Ext(s3, "AWS S3", "Static file storage")
    System_Ext(cloudfront, "AWS CloudFront", "CDN for global delivery")
    System_Ext(github, "GitHub Actions", "CI/CD pipeline")
    
    Rel(visitor, cloudfront, "Visits", "HTTPS")
    Rel(cloudfront, s3, "Fetches content", "HTTPS")
    Rel(github, s3, "Deploys to", "AWS SDK")
    
    UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="1")
```

### Example 5: Security Architecture with Trust Boundaries

```mermaid
C4Container
    title Security Architecture for CIA Platform

    Person(publicUser, "Public User", "Unauthenticated visitor")
    Person(authUser, "Authenticated User", "Registered analyst")
    Person(admin, "Administrator", "System administrator")
    
    System_Boundary(dmz, "DMZ - Public Access") {
        Container(cdn, "CloudFront CDN", "AWS", "Static content delivery")
        Container(waf, "Web Application Firewall", "AWS WAF", "Threat protection")
        Container(web, "Web Application", "React/S3", "Public UI")
    }
    
    System_Boundary(app, "Application Tier - Authenticated") {
        Container(api, "API Gateway", "AWS API Gateway", "API management, rate limiting")
        Container(lambda, "API Functions", "AWS Lambda", "Business logic")
        Container(auth, "Authentication", "AWS Cognito", "User authentication")
    }
    
    System_Boundary(data, "Data Tier - Restricted") {
        ContainerDb(db, "Database", "RDS PostgreSQL", "Encrypted data storage")
        ContainerDb(cache, "Cache", "ElastiCache Redis", "Session and data cache")
    }
    
    Rel(publicUser, cdn, "HTTPS", "Public access")
    Rel(cdn, waf, "Filtered traffic", "HTTPS")
    Rel(waf, web, "Protected traffic", "HTTPS")
    
    Rel(authUser, api, "HTTPS + JWT", "Authenticated access")
    Rel(api, auth, "Validates token", "AWS IAM")
    Rel(api, lambda, "Invokes", "AWS IAM")
    
    Rel(admin, api, "HTTPS + JWT + MFA", "Admin access")
    
    Rel(lambda, db, "JDBC over SSL", "VPC private subnet")
    Rel(lambda, cache, "Redis over TLS", "VPC private subnet")
    
    UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="1")
```

### Example 6: Future State Architecture

```mermaid
C4Container
    title Future Container Diagram for Hack23 CIA Platform (2026)

    Person(user, "Analyst", "Political data analyst")
    
    System_Boundary(cia, "CIA Platform - Microservices Architecture") {
        Container(web, "Web Application", "Next.js/React", "Modern responsive UI")
        Container(mobile, "Mobile App", "React Native", "iOS/Android app")
        
        Container(gateway, "API Gateway", "Kong", "API management, auth")
        
        Container(politicianSvc, "Politician Service", "Go", "Politician data microservice")
        Container(voteSvc, "Vote Service", "Go", "Voting records microservice")
        Container(analyticsSvc, "Analytics Service", "Python", "ML-powered analytics")
        Container(notificationSvc, "Notification Service", "Node.js", "Real-time notifications")
        
        ContainerDb(politicianDb, "Politician DB", "PostgreSQL", "Politician data")
        ContainerDb(voteDb, "Vote DB", "PostgreSQL", "Voting records")
        ContainerDb(analyticsDb, "Analytics DB", "TimescaleDB", "Time-series analytics")
        
        Container(eventBus, "Event Bus", "Apache Kafka", "Event streaming")
        Container(cache, "Cache", "Redis Cluster", "Distributed cache")
        Container(search, "Search", "Elasticsearch", "Full-text search")
    }
    
    System_Ext(riksdagen, "Riksdagen API", "Parliament data")
    System_Ext(ml, "ML Platform", "TensorFlow Serving", "ML predictions")
    
    Rel(user, web, "Uses", "HTTPS")
    Rel(user, mobile, "Uses", "HTTPS")
    
    Rel(web, gateway, "API calls", "HTTPS/REST")
    Rel(mobile, gateway, "API calls", "HTTPS/REST")
    
    Rel(gateway, politicianSvc, "Routes", "gRPC")
    Rel(gateway, voteSvc, "Routes", "gRPC")
    Rel(gateway, analyticsSvc, "Routes", "gRPC")
    Rel(gateway, notificationSvc, "Routes", "WebSocket")
    
    Rel(politicianSvc, politicianDb, "Reads/Writes", "SQL")
    Rel(voteSvc, voteDb, "Reads/Writes", "SQL")
    Rel(analyticsSvc, analyticsDb, "Reads/Writes", "SQL")
    
    Rel(politicianSvc, eventBus, "Publishes events", "Kafka")
    Rel(voteSvc, eventBus, "Publishes events", "Kafka")
    Rel(analyticsSvc, eventBus, "Subscribes to events", "Kafka")
    Rel(notificationSvc, eventBus, "Subscribes to events", "Kafka")
    
    Rel(politicianSvc, cache, "Uses", "Redis")
    Rel(voteSvc, cache, "Uses", "Redis")
    Rel(analyticsSvc, ml, "Inference", "HTTPS/REST")
    
    UpdateLayoutConfig($c4ShapeInRow="4", $c4BoundaryInRow="1")
```

## Best Practices

### Naming Conventions

**MUST:**
- Use clear, descriptive names for elements
- Use consistent terminology across diagrams
- Specify technology/framework in Container diagrams
- Include protocols in relationship labels

### Visual Clarity

**SHOULD:**
- Limit elements per diagram (max 15-20)
- Group related elements
- Use consistent colors for element types
- Arrange elements logically (left-to-right flow for data)

### Documentation Structure

**MUST:**
- Include diagram title
- Add description explaining purpose
- Provide key/legend if using custom notation
- Document assumptions and constraints
- Link to related diagrams

**Recommended File Structure:**
```
docs/
  architecture/
    ARCHITECTURE.md              # Current state C4 diagrams
    FUTURE_ARCHITECTURE.md       # Future state C4 diagrams
    decisions/                   # Architecture Decision Records
      ADR-001-microservices.md
      ADR-002-database-choice.md
```

## Related ISMS Policies

- **[Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md)** - Architecture documentation requirements
- **[Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)** - Security architecture

## Related Documentation

- [SECURITY_ARCHITECTURE.md](../../../../SECURITY_ARCHITECTURE.md) - Security-focused C4 diagrams
- [security-architecture SKILL.md](../security-architecture/SKILL.md) - Security architecture patterns
- [documentation-portfolio SKILL.md](../documentation-portfolio/SKILL.md) - Complete documentation set

## Tool Support

### Mermaid Live Editor
- URL: https://mermaid.live/
- Use for creating and testing diagrams

### VS Code Extensions
- Mermaid Preview
- Markdown Preview Mermaid Support

### Rendering in GitHub
- GitHub natively renders Mermaid diagrams in Markdown

## C4 Model References

- **Official C4 Model**: https://c4model.com/
- **Mermaid C4 Syntax**: https://mermaid.js.org/syntax/c4.html
- **Simon Brown's Architecture Resources**: https://www.architectis.je/

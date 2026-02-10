---
license: Apache-2.0
skill_category: operations
skill_name: change-management
difficulty: intermediate
tags: [change-management, operations, risk-control, rollback, testing, approval, cab]
related_policies:
  - Change_Management.md
  - Risk_Assessment_Methodology.md
  - Business_Continuity_Plan.md
  - Disaster_Recovery_Plan.md
compliance_frameworks:
  - ISO 27001:2022 (A.8.32 Change Management)
  - NIST CSF 2.0 (PR.IP-3, PR.IP-4)
  - CIS Controls v8.1 (3.14 Change Management)
---

# 🔄 Change Management Operations

**Risk-Controlled Change Processes for Production Systems**

## Purpose

This skill defines **risk-controlled change management procedures** ensuring all production changes are documented, tested, approved, and reversible. Change management balances the need for agility with operational stability through systematic approval workflows, comprehensive testing requirements, and documented rollback procedures.

Based on the [Change Management Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Change_Management.md) from Hack23 AB's ISMS framework, this skill demonstrates how **automated change control directly enables both innovation velocity and risk mitigation**—serving as competitive advantage for cybersecurity consulting methodologies.

## Rules (Change Management MUST/MUST NOT)

### 🎯 MUST: Mandatory Change Control Requirements

#### Change Documentation
- **MUST document all production changes** through formal change requests with:
  - 🎯 Change description and business justification
  - 🔍 Risk assessment per [Risk Assessment Methodology](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Risk_Assessment_Methodology.md)
  - 📋 Implementation plan with rollback procedures
  - 🧪 Test evidence and validation results
  - 👥 Stakeholder notifications and approvals
  
#### Change Classification
- **MUST classify changes** by risk level:
  - 🔴 **High Risk**: Database schema, authentication, payment systems (CAB approval required)
  - 🟠 **Medium Risk**: API changes, infrastructure updates (peer review + automated tests)
  - 🟢 **Low Risk**: Documentation, UI styling (automated deployment gates)
  - ⚡ **Emergency**: Security patches, critical bugs (post-implementation CAB review)

#### Testing Requirements
- **MUST validate changes** before production deployment:
  - ✅ Unit tests (80%+ coverage for code changes)
  - ✅ Integration tests (API contract validation)
  - ✅ Security scans (SAST/DAST/SCA passing)
  - ✅ Performance testing (no degradation vs. baseline)
  - ✅ Rollback procedure validation

#### Change Approval Workflows
- **MUST obtain appropriate approvals**:
  - 🔴 **High Risk Changes**: Change Advisory Board (CAB) approval required
  - 🟠 **Medium Risk Changes**: Peer review + automated gates
  - 🟢 **Low Risk Changes**: Automated validation gates
  - ⚡ **Emergency Changes**: Implement first, CAB review within 24 hours

#### Rollback Capabilities
- **MUST maintain rollback procedures** for all changes:
  - 📦 Immutable deployment artifacts in version control
  - 🔄 Database migration rollback scripts
  - 🎯 Infrastructure as Code (IaC) version pinning
  - 🔙 Blue-green or canary deployment strategies
  - ⏱️ Maximum 15-minute rollback time for critical systems

### ⚠️ MUST NOT: Prohibited Change Practices

#### Unauthorized Changes
- **MUST NOT deploy to production without approval**:
  - ❌ No direct production access (all changes via CI/CD)
  - ❌ No bypassing automated validation gates
  - ❌ No production "hotfixes" without emergency change process
  - ❌ No undocumented configuration changes

#### Risky Change Windows
- **MUST NOT schedule high-risk changes** during:
  - ❌ Business-critical time windows (defined in [Business Continuity Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Business_Continuity_Plan.md))
  - ❌ Weekends without on-call coverage
  - ❌ Public holidays or vacation periods
  - ❌ Concurrent with other high-risk changes

#### Incomplete Testing
- **MUST NOT deploy changes without**:
  - ❌ Passing automated test suites
  - ❌ Security scan validation
  - ❌ Verified rollback procedures
  - ❌ Stakeholder communication

## Examples

### Example 1: Standard Change Request (Medium Risk)

**Scenario**: API endpoint modification adding new query parameter

**Change Request Template**:
```markdown
## Change Request CR-2026-0123

**Change Type**: 🟠 Medium Risk - API Modification
**Requested By**: Development Team
**Business Justification**: Enable filtering by date range for reporting feature
**Target Date**: 2026-02-15

### Change Description
Add optional `start_date` and `end_date` query parameters to `/api/v1/reports` endpoint

### Risk Assessment
- **Likelihood**: Low (backward compatible, optional parameters)
- **Impact**: Medium (API contract change)
- **Risk Rating**: 🟡 Low-Medium (acceptable with testing)

### Implementation Plan
1. Update OpenAPI specification
2. Implement parameter validation (ISO 8601 dates)
3. Update database query with date filtering
4. Deploy to staging environment
5. Run integration test suite
6. Update API documentation
7. Deploy to production via blue-green strategy

### Testing Evidence
- ✅ Unit tests: 85% coverage (target: 80%)
- ✅ Integration tests: All 47 tests passing
- ✅ SAST: SonarCloud quality gate passed
- ✅ Performance: 95th percentile response time unchanged
- ✅ Rollback: Verified blue-green instant rollback

### Rollback Procedure
```bash
# Instant traffic shift back to previous version
aws elbv2 modify-listener --listener-arn $LISTENER_ARN \
  --default-actions Type=forward,TargetGroupArn=$PREVIOUS_TG
```

### Approvals Required
- ✅ Peer Review: Senior Developer (completed)
- ✅ Automated Gates: CI/CD validation passed
- ⏳ CAB Approval: Not required (medium risk with comprehensive testing)

### Stakeholder Notifications
- 📧 API consumers: 5-day advance notice
- 📋 Documentation: Updated before deployment
- 🔔 Status page: Change window announcement
```

**CI/CD Integration** (GitHub Actions):
```yaml
name: Change Management Validation

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  change-validation:
    runs-on: ubuntu-latest
    steps:
      - name: Validate Change Classification
        run: |
          # Extract change type from PR labels
          if [[ "${{ contains(github.event.pull_request.labels.*.name, 'high-risk') }}" == "true" ]]; then
            echo "🔴 High Risk Change - CAB Approval Required"
            # Check for CAB approval comment
            if ! gh pr view ${{ github.event.pull_request.number }} \
                 --json comments \
                 --jq '.comments[].body' | grep -q "CAB-APPROVED"; then
              echo "❌ Missing CAB approval"
              exit 1
            fi
          fi

      - name: Verify Testing Requirements
        run: |
          # Check test coverage
          coverage=$(cat coverage-summary.json | jq '.total.lines.pct')
          if (( $(echo "$coverage < 80" | bc -l) )); then
            echo "❌ Test coverage below 80%: $coverage%"
            exit 1
          fi
          echo "✅ Test coverage: $coverage%"

      - name: Verify Rollback Procedure
        run: |
          # Check for rollback documentation
          if [ ! -f "ROLLBACK.md" ]; then
            echo "❌ Missing ROLLBACK.md"
            exit 1
          fi
          echo "✅ Rollback procedure documented"

      - name: Security Scan Validation
        run: |
          # Verify SonarCloud quality gate
          curl -s "$SONARCLOUD_URL/api/qualitygates/project_status?projectKey=$PROJECT_KEY" \
            | jq -e '.projectStatus.status == "OK"' || exit 1
```

### Example 2: Emergency Change Procedure (Critical Security Patch)

**Scenario**: Critical CVE in Log4j library requires immediate patching

**Emergency Change Process**:
```markdown
## Emergency Change EC-2026-0089

**Change Type**: ⚡ EMERGENCY - Critical Security Vulnerability
**Severity**: 🔴 CRITICAL - CVSS 10.0 (RCE via JNDI injection)
**CVE**: CVE-2021-44228 (Log4Shell)
**Discovered**: 2026-02-10 09:00 UTC
**Implemented**: 2026-02-10 14:30 UTC

### Emergency Authorization
**Authorized By**: CEO (via Slack at 09:15 UTC)
**Reason**: Critical remote code execution vulnerability actively exploited

### Rapid Implementation
1. **Immediate Actions** (completed within 4 hours):
   - Updated Log4j 2.14.1 → 2.17.1 (patched version)
   - Verified no vulnerable JNDI lookups in codebase
   - Deployed WAF rules blocking exploit attempts
   - Scanned infrastructure for indicators of compromise

2. **Deployment Strategy**:
   - Zero-downtime rolling update across all environments
   - Real-time monitoring for anomalies during rollout
   - Backup snapshots taken before deployment

3. **Validation**:
   - ✅ Dependency scan: No vulnerable Log4j versions detected
   - ✅ Exploit test: JNDI injection attempts blocked
   - ✅ Functional testing: All critical paths validated
   - ✅ Performance: No degradation observed

### Post-Implementation CAB Review (within 24 hours)
**Review Date**: 2026-02-11 10:00 UTC
**Findings**:
- ✅ Emergency justified: Active exploitation in the wild
- ✅ Proper authorization obtained
- ✅ Rollback procedure available (revert to previous container image)
- ✅ Communication timely: All stakeholders notified within 1 hour
- ⚠️ Improvement: Enhance dependency scanning frequency

**Lessons Learned**:
1. Implement daily dependency vulnerability scans (added to CI/CD)
2. Maintain pre-approved emergency change templates
3. Document third-party library update procedures
```

**Automated Emergency Deployment** (AWS Lambda + Systems Manager):
```python
# emergency_patch.py - Automated emergency patching workflow
import boto3
import json
from datetime import datetime

def lambda_handler(event, context):
    """
    Emergency change automation for critical security patches
    Triggered via AWS EventBridge on CVE alerts
    """
    ssm = boto3.client('ssm')
    sns = boto3.client('sns')
    
    cve_id = event['detail']['cve_id']
    severity = event['detail']['severity']
    
    if severity not in ['CRITICAL', 'HIGH']:
        return {'status': 'SKIPPED', 'reason': 'Below emergency threshold'}
    
    # Execute emergency patch via Systems Manager
    response = ssm.start_automation_execution(
        DocumentName='Emergency-Patch-Application',
        Parameters={
            'CVE': [cve_id],
            'ApprovalOverride': ['CEO-AUTHORIZED'],  # Emergency bypass
            'RollbackEnabled': ['true'],
            'NotificationTopic': [os.environ['EMERGENCY_SNS_TOPIC']]
        }
    )
    
    # Notify CAB for post-implementation review
    sns.publish(
        TopicArn=os.environ['CAB_SNS_TOPIC'],
        Subject=f'🚨 Emergency Change Implemented: {cve_id}',
        Message=json.dumps({
            'change_id': f'EC-{datetime.utcnow().strftime("%Y-%m-%d-%H%M")}',
            'cve': cve_id,
            'severity': severity,
            'automation_execution': response['AutomationExecutionId'],
            'cab_review_required': 'within 24 hours',
            'rollback_available': True
        }, indent=2)
    )
    
    return {
        'statusCode': 200,
        'emergency_change_id': response['AutomationExecutionId'],
        'cab_review_scheduled': True
    }
```

### Example 3: Change Advisory Board (CAB) Review

**Scenario**: Database schema change for new feature requires CAB approval

**CAB Meeting Structure**:
```markdown
## CAB Meeting Minutes - 2026-02-15

**Attendees**:
- 👨‍💼 CEO (Chair)
- 🔧 Senior Developer
- 🔐 Security Architect (virtual)
- 📊 Business Analyst

**Changes Reviewed**: 3 high-risk, 12 medium-risk

---

### High-Risk Change CR-2026-0145: Database Schema Modification

**Change Description**: Add `user_preferences` JSONB column to `users` table (500K+ rows)

**Risk Assessment**:
- **Likelihood**: Medium (schema change on large table)
- **Impact**: High (core user authentication table)
- **Risk Rating**: 🔴 High (requires CAB approval)

**CAB Discussion**:
- ✅ **Testing**: Validated on staging with realistic data volume
- ✅ **Performance**: Index strategy prevents table locks
- ✅ **Rollback**: Column nullable, can be dropped if needed
- ⚠️ **Concern**: Potential brief degradation during index creation
- ✅ **Mitigation**: Schedule during low-traffic window (03:00 UTC Sunday)

**CAB Decision**: ✅ **APPROVED** with conditions
- **Condition 1**: Real-time monitoring during deployment
- **Condition 2**: Rollback plan validated in dry run
- **Condition 3**: Stakeholder notification 48 hours in advance
- **Approved Window**: 2026-02-18 03:00-04:00 UTC

**Implementation Plan** (approved):
```sql
-- Step 1: Add nullable column (non-blocking)
ALTER TABLE users ADD COLUMN user_preferences JSONB DEFAULT '{}';

-- Step 2: Populate existing rows (batched, off-peak)
UPDATE users SET user_preferences = '{}'::jsonb 
WHERE user_preferences IS NULL;

-- Step 3: Create GIN index (concurrent, minimal locking)
CREATE INDEX CONCURRENTLY idx_users_preferences 
ON users USING GIN (user_preferences);

-- Step 4: Add application constraints (after verification)
ALTER TABLE users ALTER COLUMN user_preferences SET NOT NULL;
```

**Rollback Procedure** (validated in dry run):
```sql
-- Immediate rollback if issues detected
ALTER TABLE users DROP COLUMN user_preferences;
-- Rollback time: <30 seconds
```

**Post-Deployment Validation**:
- [ ] Query performance within 5% of baseline
- [ ] No connection pool exhaustion
- [ ] Application error rate <0.1%
- [ ] Rollback tested in staging after production deployment
```

**CAB Tracking Dashboard** (AWS CloudWatch + Grafana):
```python
# cab_metrics.py - CAB performance tracking
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class CABMetrics:
    """Track Change Advisory Board effectiveness"""
    
    def calculate_metrics(self, start_date: datetime, end_date: datetime):
        """Generate CAB performance KPIs"""
        return {
            'change_volume': {
                'high_risk': self.count_changes('high-risk', start_date, end_date),
                'medium_risk': self.count_changes('medium-risk', start_date, end_date),
                'emergency': self.count_changes('emergency', start_date, end_date),
            },
            'approval_metrics': {
                'approval_rate': self.calculate_approval_rate(),  # Target: >85%
                'avg_approval_time': self.calculate_avg_approval_time(),  # Target: <48h
                'rejected_changes': self.count_rejections(),
            },
            'success_metrics': {
                'failed_changes': self.count_failed_deployments(),  # Target: <5%
                'rollback_rate': self.calculate_rollback_rate(),  # Target: <10%
                'emergency_changes': self.count_emergency_bypasses(),  # Target: <2%
            },
            'compliance_metrics': {
                'documented_changes': self.calculate_documentation_rate(),  # Target: 100%
                'tested_changes': self.calculate_testing_compliance(),  # Target: 100%
                'cab_attendance': self.calculate_attendance_rate(),  # Target: >80%
            }
        }
```

### Example 4: Infrastructure as Code (IaC) Change Management

**Scenario**: Terraform infrastructure changes with automated validation

**Terraform Change Workflow**:
```hcl
# terraform/environments/production/main.tf
terraform {
  required_version = ">= 1.5"
  
  backend "s3" {
    bucket         = "hack23-terraform-state"
    key            = "production/terraform.tfstate"
    region         = "eu-west-1"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"
  }
}

# Change management metadata
locals {
  change_metadata = {
    change_id          = "CR-2026-0198"
    requested_by       = "infrastructure-team"
    approved_by        = "CAB"
    deployment_window  = "2026-02-20T03:00:00Z"
    rollback_plan      = "terraform apply -target=module.rollback"
  }
  
  tags = merge(
    var.common_tags,
    local.change_metadata,
    {
      Environment = "production"
      ManagedBy   = "terraform"
    }
  )
}

# Example infrastructure change: Add new Lambda function
module "api_processor" {
  source = "../../modules/lambda"
  
  function_name = "api-data-processor"
  runtime       = "python3.11"
  handler       = "app.lambda_handler"
  
  # Change-controlled configuration
  memory_size = 512  # Changed from 256 (CAB approved)
  timeout     = 30   # Changed from 10 (risk assessment: Low)
  
  # Immutable versioning for rollback
  source_code_hash = filebase64sha256("${path.module}/lambda_package.zip")
  publish          = true  # Enable versioned deployments
  
  tags = local.tags
}

# Automated rollback alias
resource "aws_lambda_alias" "api_processor_live" {
  name             = "live"
  function_name    = module.api_processor.function_name
  function_version = module.api_processor.version
  
  # Lifecycle prevents accidental deletion during rollback
  lifecycle {
    create_before_destroy = true
  }
}
```

**GitHub Actions Terraform Change Validation**:
```yaml
name: Terraform Change Management

on:
  pull_request:
    paths:
      - 'terraform/**'

jobs:
  terraform-change-validation:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: 1.5.0

      - name: Terraform Plan
        id: plan
        run: |
          cd terraform/environments/production
          terraform init
          terraform plan -out=tfplan
          terraform show -json tfplan > plan.json

      - name: Change Risk Assessment
        run: |
          # Analyze Terraform plan for high-risk changes
          python3 << 'EOF'
          import json
          
          with open('terraform/environments/production/plan.json') as f:
              plan = json.load(f)
          
          high_risk_resources = [
              'aws_db_instance',  # Database changes
              'aws_iam_role',     # Permission changes
              'aws_security_group',  # Network security
          ]
          
          risk_level = 'LOW'
          for change in plan['resource_changes']:
              if any(res in change['type'] for res in high_risk_resources):
                  if change['change']['actions'] in [['delete'], ['replace']]:
                      risk_level = 'HIGH'
                      print(f"🔴 HIGH RISK: {change['type']} {change['change']['actions']}")
          
          print(f"::set-output name=risk_level::{risk_level}")
          EOF

      - name: Require CAB Approval for High-Risk
        if: steps.plan.outputs.risk_level == 'HIGH'
        run: |
          echo "🔴 High-risk infrastructure change detected"
          echo "CAB approval required before merge"
          # Check for CAB approval label
          if ! gh pr view ${{ github.event.pull_request.number }} \
               --json labels \
               --jq '.labels[].name' | grep -q "cab-approved"; then
            echo "❌ Missing CAB approval"
            exit 1
          fi

      - name: Generate Rollback Plan
        run: |
          cd terraform/environments/production
          # Create rollback plan targeting previous state
          terraform plan -destroy -target=module.api_processor -out=rollback.tfplan
          echo "📦 Rollback plan generated and stored"
```

## Related ISMS Policies

### Core Change Management Framework
- [📝 Change Management Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Change_Management.md) — Complete change control procedures and CAB governance
- [🔐 Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md) — Security governance and risk management framework

### Risk and Business Continuity
- [📊 Risk Assessment Methodology](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Risk_Assessment_Methodology.md) — Systematic risk evaluation for change classification
- [🔄 Business Continuity Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Business_Continuity_Plan.md) — Change windows and critical time periods
- [🆘 Disaster Recovery Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Disaster_Recovery_Plan.md) — Rollback procedures and recovery integration

### Technical Implementation
- [🛡️ Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md) — Testing requirements and CI/CD security gates
- [💻 Asset Register](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Asset_Register.md) — Systems inventory and change impact assessment
- [🚨 Incident Response Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Incident_Response_Plan.md) — Emergency change procedures

## Compliance Mapping

### ISO 27001:2022
- **A.8.32 Change Management** - Control of changes to information processing facilities and systems
- **A.5.37 Documented Operating Procedures** - Change documentation and approval workflows
- **A.8.31 Separation of Development, Test and Production Environments** - Change testing requirements

### NIST Cybersecurity Framework 2.0
- **PR.IP-3** - Configuration change control processes
- **PR.IP-4** - Backups of information maintained
- **DE.CM-7** - Monitoring for unauthorized changes

### CIS Controls v8.1
- **Control 3.14** - Log all changes to network infrastructure
- **Control 4.1** - Establish and maintain secure configuration process
- **Control 16.14** - Establish and maintain change management process

## Key Takeaways

✅ **Document Every Change**: Formal change requests with risk assessment, testing evidence, and rollback procedures  
✅ **Risk-Based Approval**: CAB for high-risk changes, automated gates for low-risk changes  
✅ **Comprehensive Testing**: Unit/integration/security/performance validation before production  
✅ **Always Reversible**: Immutable artifacts, IaC versioning, and validated rollback procedures  
✅ **Emergency Procedures**: Expedited process for critical security issues with post-implementation review  
✅ **Continuous Monitoring**: Real-time change tracking, success metrics, and compliance validation

**Remember**: Change management is **not a bureaucratic obstacle** but an **enabler of safe innovation**—allowing rapid deployment while maintaining operational stability through systematic risk control.

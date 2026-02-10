---
license: Apache-2.0
skill_category: governance
skill_name: risk-register
difficulty: intermediate
tags: [risk-register, risk-tracking, risk-treatment, risk-monitoring, quarterly-review]
related_policies:
  - Risk_Register.md
  - Risk_Assessment_Methodology.md
  - Information_Security_Policy.md
  - Asset_Register.md
compliance_frameworks:
  - ISO 27001:2022 (Clause 6.1.3 Risk Treatment, A.5.7 Threat Intelligence)
  - NIST CSF 2.0 (ID.RM-1, ID.RM-2, ID.RM-3)
  - CIS Controls v8.1 (18.2 Remediation Process)
---

# 📋 Risk Register Management

**Enterprise Risk Tracking, Treatment Plans, and Continuous Monitoring**

## Purpose

This skill defines **comprehensive risk register management** for tracking identified risks, documenting treatment plans, monitoring control effectiveness, and reporting risk posture to stakeholders. The risk register serves as the central repository connecting risk assessments to actionable treatment strategies with clear ownership and accountability.

Based on the [Risk Register](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Risk_Register.md) from Hack23 AB's ISMS framework, this skill demonstrates how **structured risk tracking directly enables executive visibility and compliance reporting**—serving as competitive advantage for cybersecurity consulting methodologies.

## Rules (Risk Register MUST/MUST NOT)

### 🎯 MUST: Mandatory Risk Register Requirements

#### Risk Register Structure
- **MUST maintain central risk register** containing:
  - 🆔 Unique risk identifier (e.g., `RR-2026-001`)
  - 📝 Risk description and business context
  - 🎯 Affected assets and systems
  - 📊 Inherent risk score (before controls)
  - 🛡️ Existing controls and effectiveness
  - 📉 Residual risk score (after controls)
  - ⚠️ Risk treatment strategy (Accept/Mitigate/Transfer/Avoid)
  - 👥 Risk owner and accountability
  - 📅 Review dates and status
  - 💰 Financial impact estimates

#### Risk Lifecycle Management
- **MUST track risks through complete lifecycle**:
  - 🆕 **Identified**: Risk discovered and documented
  - 📊 **Assessed**: Likelihood and impact evaluated
  - ✅ **Approved**: Treatment plan approved by risk owner
  - 🔄 **In Treatment**: Controls being implemented
  - ✔️ **Mitigated**: Controls implemented and verified
  - 🔒 **Closed**: Risk accepted or resolved
  - 👁️ **Monitoring**: Ongoing surveillance

#### Treatment Plan Documentation
- **MUST document treatment plans** with:
  - 🎯 Specific controls to be implemented
  - 💰 Budget allocation and resources required
  - 📅 Implementation timeline and milestones
  - 📊 Success criteria and KPIs
  - 🔄 Residual risk target after treatment
  - 👥 Responsible parties and dependencies

#### Quarterly Risk Review
- **MUST conduct quarterly reviews** of:
  - 🔴 All high risks (score ≥15): Detailed status review
  - 🟡 Medium risks (score 8-14): Status verification
  - 🟢 Low risks (score ≤7): Annual validation only
  - 📊 Risk trend analysis (increasing/decreasing)
  - 🎯 Treatment plan progress and blockers
  - 📈 New risks identified since last review

#### Executive Reporting
- **MUST provide risk reports** to leadership:
  - 📊 Quarterly board reporting with risk dashboard
  - 🚨 Immediate escalation for new high risks
  - 📈 Trend analysis and risk appetite compliance
  - 💰 Treatment budget status and ROI
  - ✅ Regulatory compliance status

### ⚠️ MUST NOT: Prohibited Risk Register Practices

#### Incomplete Risk Documentation
- **MUST NOT maintain risk register without**:
  - ❌ No risks without assigned owners
  - ❌ No risks without treatment plans
  - ❌ No risks without review dates
  - ❌ No risks without financial impact estimates

#### Stale Risk Data
- **MUST NOT allow outdated information**:
  - ❌ No high risks unreviewed >30 days
  - ❌ No medium risks unreviewed >90 days
  - ❌ No "In Treatment" status >6 months without progress
  - ❌ No closed risks without verification evidence

#### Shadow Risk Registers
- **MUST NOT maintain separate registers**:
  - ❌ No department-specific risk registers
  - ❌ No project risk logs outside central register
  - ❌ No spreadsheet-based tracking (use centralized system)
  - ❌ No duplicate risk entries

## Examples

### Example 1: Comprehensive Risk Register Entry

**Scenario**: Document ransomware risk with full lifecycle tracking

**Risk Register Entry Template**:
```markdown
## Risk Register Entry: RR-2026-0015

### Risk Identification
**Risk ID**: RR-2026-0015
**Risk Title**: Ransomware Attack on Production Systems
**Date Identified**: 2026-02-10
**Identified By**: Security Architect
**Risk Category**: Cyber Threat
**Status**: 🔄 In Treatment

### Risk Description
Cybercriminal groups may deploy ransomware via phishing emails or exploited vulnerabilities, 
encrypting production databases and file servers, causing business disruption and potential 
data loss. Recent intelligence indicates increased targeting of companies in our sector.

### Asset Impact
**Affected Assets**:
- Production PostgreSQL database (500K customer records)
- File servers (10TB business documents)
- Email system (365 users)
- Business operations (€50K/day revenue)

**Asset Classification**: 🔴 Critical

### Risk Assessment

#### Inherent Risk (Before Controls)
- **Likelihood**: 4 - Likely (60% probability based on industry data)
  - *Justification*: Common attack vector, high attacker motivation, proven delivery methods
- **Impact**: 5 - Severe (€500K+ estimated impact)
  - *Financial*: €50K/day downtime + €200K recovery + €300K GDPR fine
  - *Reputational*: Customer trust loss, negative media coverage
- **Inherent Risk Score**: 20 🔴 HIGH

#### Existing Controls
**Preventive Controls**:
✅ Email filtering (Proofpoint) - blocks 95% phishing attempts
✅ Endpoint antivirus (CrowdStrike) - 80% deployment
✅ Network firewalls (Palo Alto) - perimeter protection
⚠️ Limited network segmentation
⚠️ No privileged access management (PAM)

**Detective Controls**:
✅ SIEM logging (Splunk) - 30-day retention
✅ Daily backup monitoring
⚠️ Limited user behavior analytics

**Corrective Controls**:
✅ Daily backups - RPO 24h, RTO 4h
✅ Incident response plan documented
⚠️ No tested recovery procedures

**Control Effectiveness**: 60%

#### Residual Risk (After Current Controls)
- **Likelihood**: 3 - Possible (40% probability with controls)
- **Impact**: 4 - Major (€100K-€500K with backup recovery)
- **Residual Risk Score**: 12 🟡 MEDIUM

### Risk Treatment Plan

**Treatment Strategy**: ⚠️ MITIGATE - Reduce to acceptable level

**Treatment Actions**:
1. **Network Segmentation** (Priority 1)
   - Budget: €30K
   - Timeline: 60 days
   - Owner: Infrastructure Lead
   - Expected Risk Reduction: Likelihood 3 → 2

2. **Privileged Access Management** (Priority 2)
   - Budget: €20K
   - Timeline: 90 days
   - Owner: Security Architect
   - Expected Risk Reduction: Likelihood 2 → 2, Impact 4 → 3

3. **Quarterly Tabletop Exercises** (Priority 3)
   - Budget: €5K/year
   - Timeline: Ongoing
   - Owner: Security Team
   - Expected Risk Reduction: Impact 4 → 3

**Total Treatment Budget**: €55K
**Target Residual Risk**: 6 🟢 LOW (Likelihood 2 × Impact 3)

**Treatment Timeline**:
```
Month 1-2: Network segmentation design and procurement
Month 3: Network segmentation implementation
Month 4-6: PAM solution selection and deployment
Month 7+: Ongoing exercises and monitoring
```

### Risk Monitoring

**Review Frequency**: Monthly (high risk)
**Key Risk Indicators (KRIs)**:
- Phishing email detection rate (target: >95%)
- Endpoint antivirus coverage (target: 100%)
- Backup success rate (target: 100%)
- Mean time to detect (MTTD) anomalies (target: <15min)

**Last Review**: 2026-02-15
**Next Review**: 2026-03-15
**Risk Trend**: ↘️ Decreasing (treatment in progress)

### Risk Ownership

**Risk Owner**: CTO (accountability for treatment)
**Treatment Lead**: Security Architect (implementation responsibility)
**Business Impact Owner**: CEO (business continuity)
**Compliance Owner**: DPO (GDPR implications)

### Audit Trail
| Date | Action | User | Notes |
|------|--------|------|-------|
| 2026-02-10 | Risk Identified | Security Architect | SecurityHub finding escalation |
| 2026-02-12 | Initial Assessment | Risk Committee | Scored as HIGH risk |
| 2026-02-15 | Treatment Approved | CTO | €55K budget allocated |
| 2026-03-01 | Segmentation Started | Infrastructure Lead | Vendor contracts signed |

### Related Documentation
- [Risk Assessment: RA-2026-0034](link)
- [Incident Response Playbook: Ransomware](link)
- [Business Continuity Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Business_Continuity_Plan.md)
- [Backup and Recovery Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Backup_and_Recovery_Policy.md)
```

**DynamoDB Risk Register Schema**:
```python
# risk_register_schema.py - DynamoDB table design
import boto3
from datetime import datetime, timedelta

def create_risk_register_table():
    """Create DynamoDB table for risk register"""
    dynamodb = boto3.client('dynamodb')
    
    table = dynamodb.create_table(
        TableName='RiskRegister',
        KeySchema=[
            {'AttributeName': 'risk_id', 'KeyType': 'HASH'},  # Partition key
            {'AttributeName': 'status_date', 'KeyType': 'RANGE'}  # Sort key for history
        ],
        AttributeDefinitions=[
            {'AttributeName': 'risk_id', 'AttributeType': 'S'},
            {'AttributeName': 'status_date', 'AttributeType': 'S'},
            {'AttributeName': 'risk_owner', 'AttributeType': 'S'},
            {'AttributeName': 'residual_score', 'AttributeType': 'N'},
            {'AttributeName': 'status', 'AttributeType': 'S'}
        ],
        GlobalSecondaryIndexes=[
            {
                'IndexName': 'OwnerIndex',
                'KeySchema': [
                    {'AttributeName': 'risk_owner', 'KeyType': 'HASH'}
                ],
                'Projection': {'ProjectionType': 'ALL'},
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            },
            {
                'IndexName': 'ScoreIndex',
                'KeySchema': [
                    {'AttributeName': 'residual_score', 'KeyType': 'HASH'}
                ],
                'Projection': {'ProjectionType': 'ALL'},
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            },
            {
                'IndexName': 'StatusIndex',
                'KeySchema': [
                    {'AttributeName': 'status', 'KeyType': 'HASH'}
                ],
                'Projection': {'ProjectionType': 'ALL'},
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        },
        StreamSpecification={
            'StreamEnabled': True,
            'StreamViewType': 'NEW_AND_OLD_IMAGES'
        },
        Tags=[
            {'Key': 'Environment', 'Value': 'production'},
            {'Key': 'Purpose', 'Value': 'risk-management'},
            {'Key': 'Compliance', 'Value': 'ISO27001'}
        ]
    )
    
    return table

# Example risk entry
risk_entry_example = {
    'risk_id': 'RR-2026-0015',
    'status_date': datetime.utcnow().isoformat(),
    'risk_title': 'Ransomware Attack on Production Systems',
    'risk_description': 'Cybercriminal ransomware deployment via phishing',
    'risk_category': 'cyber-threat',
    'date_identified': '2026-02-10',
    'identified_by': 'security-architect',
    
    # Risk assessment
    'inherent_likelihood': 4,
    'inherent_impact': 5,
    'inherent_score': 20,
    'residual_likelihood': 3,
    'residual_impact': 4,
    'residual_score': 12,
    'target_residual_score': 6,
    
    # Treatment
    'treatment_strategy': 'mitigate',
    'treatment_budget': 55000,
    'treatment_timeline': '90 days',
    'treatment_actions': [
        {'action': 'Network Segmentation', 'budget': 30000, 'owner': 'infrastructure-lead'},
        {'action': 'PAM Implementation', 'budget': 20000, 'owner': 'security-architect'},
        {'action': 'Tabletop Exercises', 'budget': 5000, 'owner': 'security-team'}
    ],
    
    # Ownership
    'risk_owner': 'CTO',
    'treatment_lead': 'security-architect',
    'business_impact_owner': 'CEO',
    
    # Status tracking
    'status': 'in-treatment',
    'review_frequency': 'monthly',
    'last_review_date': '2026-02-15',
    'next_review_date': '2026-03-15',
    'risk_trend': 'decreasing',
    
    # Affected assets
    'affected_assets': [
        'prod-database',
        'file-servers',
        'email-system'
    ],
    
    # KRIs
    'key_risk_indicators': [
        {'kri': 'phishing_detection_rate', 'target': 0.95, 'current': 0.95},
        {'kri': 'av_coverage', 'target': 1.0, 'current': 0.8},
        {'kri': 'backup_success_rate', 'target': 1.0, 'current': 0.98}
    ]
}
```

### Example 2: Automated Risk Register Updates (Lambda + DynamoDB Streams)

**Scenario**: Automated risk lifecycle management and notifications

**Lambda Function for Risk Updates**:
```python
# lambda_risk_register_automation.py
import boto3
import json
from datetime import datetime, timedelta
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')
risk_table = dynamodb.Table('RiskRegister')

def lambda_handler(event, context):
    """
    Process DynamoDB Stream events for risk register changes
    Automate notifications and lifecycle transitions
    """
    
    for record in event['Records']:
        if record['eventName'] in ['INSERT', 'MODIFY']:
            new_risk = record['dynamodb']['NewImage']
            old_risk = record['dynamodb'].get('OldImage', {})
            
            risk_id = new_risk['risk_id']['S']
            
            # Check for status transitions
            check_status_transition(risk_id, old_risk, new_risk)
            
            # Check for overdue reviews
            check_review_schedule(risk_id, new_risk)
            
            # Check for risk score changes
            check_risk_score_change(risk_id, old_risk, new_risk)
            
            # Update risk trending
            update_risk_trend(risk_id, new_risk)
    
    return {'statusCode': 200, 'message': 'Risk register automation complete'}

def check_status_transition(risk_id: str, old_risk: dict, new_risk: dict):
    """Validate and notify on status changes"""
    
    old_status = old_risk.get('status', {}).get('S', 'unknown')
    new_status = new_risk.get('status', {}).get('S', 'unknown')
    
    if old_status != new_status:
        # Notify risk owner of status change
        risk_owner = new_risk.get('risk_owner', {}).get('S', 'unknown')
        
        sns.publish(
            TopicArn=f'arn:aws:sns:eu-west-1:123456789012:RiskOwner-{risk_owner}',
            Subject=f'Risk Status Change: {risk_id}',
            Message=json.dumps({
                'risk_id': risk_id,
                'old_status': old_status,
                'new_status': new_status,
                'transition_date': datetime.utcnow().isoformat(),
                'action_required': get_action_required(new_status)
            }, indent=2)
        )
        
        # Automatic transitions
        if new_status == 'mitigated':
            # Schedule post-mitigation review in 30 days
            schedule_review(risk_id, days_from_now=30)

def check_review_schedule(risk_id: str, risk: dict):
    """Alert on overdue risk reviews"""
    
    next_review = risk.get('next_review_date', {}).get('S')
    residual_score = int(risk.get('residual_score', {}).get('N', 0))
    
    if next_review:
        next_review_date = datetime.fromisoformat(next_review)
        
        if datetime.utcnow() > next_review_date:
            # Review overdue - escalate
            risk_owner = risk.get('risk_owner', {}).get('S', 'unknown')
            
            severity = '🔴 CRITICAL' if residual_score >= 15 else '⚠️ WARNING'
            
            sns.publish(
                TopicArn='arn:aws:sns:eu-west-1:123456789012:RiskManagementTeam',
                Subject=f'{severity} Overdue Risk Review: {risk_id}',
                Message=f"""
Risk {risk_id} review is overdue.

Residual Score: {residual_score}
Risk Owner: {risk_owner}
Scheduled Review: {next_review}
Days Overdue: {(datetime.utcnow() - next_review_date).days}

Action Required: Complete risk review immediately.
                """
            )

def check_risk_score_change(risk_id: str, old_risk: dict, new_risk: dict):
    """Alert on significant risk score changes"""
    
    old_score = int(old_risk.get('residual_score', {}).get('N', 0)) if old_risk else 0
    new_score = int(new_risk.get('residual_score', {}).get('N', 0))
    
    # Alert if risk increased by 5+ points or crossed thresholds
    if new_score - old_score >= 5:
        sns.publish(
            TopicArn='arn:aws:sns:eu-west-1:123456789012:ExecutiveTeam',
            Subject=f'🚨 Risk Score Increase: {risk_id}',
            Message=json.dumps({
                'risk_id': risk_id,
                'old_score': old_score,
                'new_score': new_score,
                'increase': new_score - old_score,
                'new_rating': calculate_risk_rating(new_score),
                'action': 'Executive review required'
            }, indent=2)
        )

def update_risk_trend(risk_id: str, risk: dict):
    """Calculate risk trend based on historical data"""
    
    # Query last 3 months of risk scores
    response = risk_table.query(
        KeyConditionExpression='risk_id = :rid',
        ExpressionAttributeValues={
            ':rid': risk_id
        },
        ScanIndexForward=False,  # Descending order
        Limit=90  # ~3 months daily
    )
    
    scores = [int(item['residual_score']) for item in response['Items']]
    
    if len(scores) >= 2:
        trend = 'increasing' if scores[0] > scores[-1] else \
                'decreasing' if scores[0] < scores[-1] else \
                'stable'
        
        # Update trend in risk register
        risk_table.update_item(
            Key={'risk_id': risk_id, 'status_date': risk['status_date']['S']},
            UpdateExpression='SET risk_trend = :trend',
            ExpressionAttributeValues={':trend': trend}
        )

def get_action_required(status: str) -> str:
    """Get action required for each status"""
    actions = {
        'identified': 'Perform risk assessment',
        'assessed': 'Approve treatment plan',
        'approved': 'Begin treatment implementation',
        'in-treatment': 'Monitor treatment progress',
        'mitigated': 'Verify control effectiveness',
        'closed': 'None - continue monitoring',
        'monitoring': 'Review KRIs quarterly'
    }
    return actions.get(status, 'Review risk status')

def calculate_risk_rating(score: int) -> str:
    """Calculate risk rating from score"""
    if score <= 6:
        return '🟢 LOW'
    elif score <= 12:
        return '🟡 MEDIUM'
    else:
        return '🔴 HIGH'

def schedule_review(risk_id: str, days_from_now: int):
    """Schedule next review date"""
    next_review = (datetime.utcnow() + timedelta(days=days_from_now)).isoformat()
    
    # Update risk with next review date
    risk_table.update_item(
        Key={'risk_id': risk_id},
        UpdateExpression='SET next_review_date = :date',
        ExpressionAttributeValues={':date': next_review}
    )
```

### Example 3: Quarterly Risk Register Review Report

**Scenario**: Generate executive risk dashboard for board meeting

**Quarterly Review Report Generator**:
```python
# quarterly_risk_report.py - Executive risk reporting
import boto3
from datetime import datetime, timedelta
from collections import Counter
import json

class QuarterlyRiskReport:
    """Generate comprehensive quarterly risk report"""
    
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.risk_table = self.dynamodb.Table('RiskRegister')
        self.s3 = boto3.client('s3')
    
    def generate_report(self, quarter: str, year: int) -> dict:
        """Generate Q1-Q4 risk report"""
        
        # Get all current risks
        response = self.risk_table.scan()
        risks = response['Items']
        
        # While more items exist (pagination)
        while 'LastEvaluatedKey' in response:
            response = self.risk_table.scan(
                ExclusiveStartKey=response['LastEvaluatedKey']
            )
            risks.extend(response['Items'])
        
        # Calculate metrics
        report = {
            'reporting_period': f'{quarter} {year}',
            'report_date': datetime.utcnow().isoformat(),
            'total_risks': len(risks),
            'risk_distribution': self._calculate_distribution(risks),
            'risk_trends': self._analyze_trends(risks),
            'treatment_status': self._treatment_summary(risks),
            'top_risks': self._identify_top_risks(risks, limit=10),
            'overdue_reviews': self._find_overdue_reviews(risks),
            'risk_appetite_compliance': self._check_risk_appetite(risks),
            'key_risk_indicators': self._aggregate_kris(risks),
            'recommendations': self._generate_recommendations(risks)
        }
        
        # Export to S3 and send to executives
        self._publish_report(report)
        
        return report
    
    def _calculate_distribution(self, risks: list) -> dict:
        """Calculate risk score distribution"""
        high = sum(1 for r in risks if r['residual_score'] >= 15)
        medium = sum(1 for r in risks if 8 <= r['residual_score'] < 15)
        low = sum(1 for r in risks if r['residual_score'] < 8)
        
        return {
            'high_risk_count': high,
            'high_risk_percentage': f"{high / len(risks) * 100:.1f}%",
            'medium_risk_count': medium,
            'medium_risk_percentage': f"{medium / len(risks) * 100:.1f}%",
            'low_risk_count': low,
            'low_risk_percentage': f"{low / len(risks) * 100:.1f}%"
        }
    
    def _analyze_trends(self, risks: list) -> dict:
        """Analyze risk trends over quarter"""
        trends = Counter(r.get('risk_trend', 'stable') for r in risks)
        
        return {
            'increasing': trends['increasing'],
            'decreasing': trends['decreasing'],
            'stable': trends['stable'],
            'overall_trend': 'improving' if trends['decreasing'] > trends['increasing'] 
                           else 'deteriorating' if trends['increasing'] > trends['decreasing']
                           else 'stable'
        }
    
    def _treatment_summary(self, risks: list) -> dict:
        """Summarize treatment status"""
        statuses = Counter(r.get('status', 'unknown') for r in risks)
        
        # Calculate treatment budget
        total_budget = sum(r.get('treatment_budget', 0) for r in risks)
        spent_budget = sum(
            r.get('treatment_budget', 0) 
            for r in risks 
            if r.get('status') in ['in-treatment', 'mitigated']
        )
        
        return {
            'identified': statuses['identified'],
            'assessed': statuses['assessed'],
            'in_treatment': statuses['in-treatment'],
            'mitigated': statuses['mitigated'],
            'closed': statuses['closed'],
            'total_treatment_budget': f"€{total_budget:,.0f}",
            'spent_budget': f"€{spent_budget:,.0f}",
            'budget_utilization': f"{spent_budget / total_budget * 100:.1f}%" if total_budget > 0 else "0%"
        }
    
    def _identify_top_risks(self, risks: list, limit: int = 10) -> list:
        """Identify top risks by residual score"""
        sorted_risks = sorted(
            risks, 
            key=lambda r: r['residual_score'], 
            reverse=True
        )[:limit]
        
        return [
            {
                'risk_id': r['risk_id'],
                'title': r['risk_title'],
                'residual_score': r['residual_score'],
                'risk_owner': r['risk_owner'],
                'status': r['status'],
                'treatment_strategy': r.get('treatment_strategy', 'undefined')
            }
            for r in sorted_risks
        ]
    
    def _find_overdue_reviews(self, risks: list) -> list:
        """Find risks with overdue reviews"""
        now = datetime.utcnow()
        
        overdue = [
            {
                'risk_id': r['risk_id'],
                'title': r['risk_title'],
                'residual_score': r['residual_score'],
                'risk_owner': r['risk_owner'],
                'next_review_date': r['next_review_date'],
                'days_overdue': (now - datetime.fromisoformat(r['next_review_date'])).days
            }
            for r in risks
            if 'next_review_date' in r and 
               datetime.fromisoformat(r['next_review_date']) < now
        ]
        
        return sorted(overdue, key=lambda r: r['days_overdue'], reverse=True)
    
    def _check_risk_appetite(self, risks: list) -> dict:
        """Check compliance with risk appetite statement"""
        # Risk appetite: No more than 3 HIGH risks, avg score < 10
        high_risks = [r for r in risks if r['residual_score'] >= 15]
        avg_score = sum(r['residual_score'] for r in risks) / len(risks)
        
        return {
            'high_risk_limit': 3,
            'current_high_risks': len(high_risks),
            'high_risk_compliant': len(high_risks) <= 3,
            'average_score_target': 10,
            'current_average_score': round(avg_score, 2),
            'average_score_compliant': avg_score < 10,
            'overall_compliance': len(high_risks) <= 3 and avg_score < 10
        }
    
    def _aggregate_kris(self, risks: list) -> dict:
        """Aggregate Key Risk Indicators across all risks"""
        # Example KRI aggregation
        return {
            'risks_with_kris': sum(1 for r in risks if 'key_risk_indicators' in r),
            'kri_compliance_rate': "85%",  # Calculate from KRI targets
            'critical_kri_breaches': 2  # KRIs exceeding thresholds
        }
    
    def _generate_recommendations(self, risks: list) -> list:
        """Generate executive recommendations"""
        recommendations = []
        
        # High risk count recommendation
        high_risks = [r for r in risks if r['residual_score'] >= 15]
        if len(high_risks) > 3:
            recommendations.append({
                'priority': 'HIGH',
                'recommendation': f'Accelerate treatment of {len(high_risks)} HIGH risks to meet risk appetite',
                'action': 'Allocate additional budget for risk mitigation'
            })
        
        # Overdue reviews recommendation
        overdue = self._find_overdue_reviews(risks)
        if len(overdue) > 0:
            recommendations.append({
                'priority': 'MEDIUM',
                'recommendation': f'{len(overdue)} risk reviews are overdue',
                'action': 'Schedule quarterly risk committee meeting'
            })
        
        # Treatment budget recommendation
        treatment_summary = self._treatment_summary(risks)
        if float(treatment_summary['budget_utilization'].rstrip('%')) < 50:
            recommendations.append({
                'priority': 'MEDIUM',
                'recommendation': 'Treatment budget underutilized',
                'action': 'Review treatment plan execution and remove blockers'
            })
        
        return recommendations
    
    def _publish_report(self, report: dict):
        """Publish report to S3 and notify executives"""
        # Upload to S3
        s3_key = f"risk-reports/{report['reporting_period'].replace(' ', '-')}.json"
        self.s3.put_object(
            Bucket='hack23-compliance-reports',
            Key=s3_key,
            Body=json.dumps(report, indent=2),
            ContentType='application/json',
            ServerSideEncryption='AES256'
        )
        
        # Send executive summary via SNS
        sns = boto3.client('sns')
        sns.publish(
            TopicArn='arn:aws:sns:eu-west-1:123456789012:ExecutiveTeam',
            Subject=f'📊 Quarterly Risk Report: {report["reporting_period"]}',
            Message=self._format_executive_summary(report)
        )
    
    def _format_executive_summary(self, report: dict) -> str:
        """Format concise executive summary"""
        return f"""
QUARTERLY RISK REPORT - {report['reporting_period']}

RISK OVERVIEW:
- Total Risks: {report['total_risks']}
- High Risks: {report['risk_distribution']['high_risk_count']} ({report['risk_distribution']['high_risk_percentage']})
- Risk Trend: {report['risk_trends']['overall_trend'].upper()}

RISK APPETITE COMPLIANCE:
- {'✅ COMPLIANT' if report['risk_appetite_compliance']['overall_compliance'] else '❌ NON-COMPLIANT'}
- High Risk Limit: {report['risk_appetite_compliance']['high_risk_limit']} (Current: {report['risk_appetite_compliance']['current_high_risks']})
- Average Score Target: <{report['risk_appetite_compliance']['average_score_target']} (Current: {report['risk_appetite_compliance']['current_average_score']})

ACTION REQUIRED:
{chr(10).join(f"- {r['recommendation']}" for r in report['recommendations'][:3])}

Full report available: s3://hack23-compliance-reports/risk-reports/
        """

# Generate quarterly report
if __name__ == "__main__":
    reporter = QuarterlyRiskReport()
    report = reporter.generate_report(quarter='Q1', year=2026)
    print(json.dumps(report, indent=2))
```

### Example 4: Risk Register API (AWS API Gateway + Lambda)

**Scenario**: RESTful API for risk register CRUD operations

**API Gateway OpenAPI Specification**:
```yaml
# risk-register-api.yaml
openapi: 3.0.0
info:
  title: Risk Register API
  version: 1.0.0
  description: RESTful API for enterprise risk register management

servers:
  - url: https://api.hack23.com/v1/risk-register

paths:
  /risks:
    get:
      summary: List all risks
      parameters:
        - name: status
          in: query
          schema:
            type: string
            enum: [identified, assessed, in-treatment, mitigated, closed]
        - name: min_score
          in: query
          schema:
            type: integer
            minimum: 1
            maximum: 25
      responses:
        '200':
          description: List of risks
          content:
            application/json:
              schema:
                type: object
                properties:
                  risks:
                    type: array
                    items:
                      $ref: '#/components/schemas/Risk'
    
    post:
      summary: Create new risk
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RiskCreate'
      responses:
        '201':
          description: Risk created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Risk'
  
  /risks/{riskId}:
    get:
      summary: Get risk by ID
      parameters:
        - name: riskId
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Risk details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Risk'
    
    put:
      summary: Update risk
      parameters:
        - name: riskId
          in: path
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RiskUpdate'
      responses:
        '200':
          description: Risk updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Risk'

components:
  schemas:
    Risk:
      type: object
      properties:
        risk_id:
          type: string
          example: "RR-2026-0015"
        risk_title:
          type: string
        risk_description:
          type: string
        inherent_score:
          type: integer
          minimum: 1
          maximum: 25
        residual_score:
          type: integer
          minimum: 1
          maximum: 25
        risk_owner:
          type: string
        status:
          type: string
          enum: [identified, assessed, in-treatment, mitigated, closed]
        treatment_plan:
          $ref: '#/components/schemas/TreatmentPlan'
    
    TreatmentPlan:
      type: object
      properties:
        strategy:
          type: string
          enum: [accept, mitigate, transfer, avoid]
        budget:
          type: number
        timeline:
          type: string
        actions:
          type: array
          items:
            type: object
```

## Related ISMS Policies

### Core Risk Management Framework
- [📋 Risk Register](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Risk_Register.md) — Complete register structure and management procedures
- [📊 Risk Assessment Methodology](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Risk_Assessment_Methodology.md) — Risk scoring and evaluation framework
- [🔐 Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md) — Risk governance and accountability

### Asset and Context
- [💼 Asset Register](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Asset_Register.md) — Asset identification for risk assessment
- [🌐 External Stakeholder Registry](https://github.com/Hack23/ISMS-PUBLIC/blob/main/External_Stakeholder_Registry.md) — Regulatory risk context

### Operational Integration
- [🔄 Change Management](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Change_Management.md) — Risk-based change approval
- [🚨 Incident Response Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Incident_Response_Plan.md) — Event-driven risk updates
- [🆘 Business Continuity Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Business_Continuity_Plan.md) — Business impact validation

## Compliance Mapping

### ISO 27001:2022
- **Clause 6.1.3 Treatment of Information Security Risks** - Risk treatment planning and implementation
- **Clause 8.2 Information Security Risk Assessment** - Ongoing risk assessment requirements
- **Clause 8.3 Information Security Risk Treatment** - Risk treatment monitoring
- **Clause 9.3 Management Review** - Risk register review by leadership

### NIST Cybersecurity Framework 2.0
- **ID.RM-1** - Risk management processes established and managed
- **ID.RM-2** - Organizational risk tolerance determined and expressed
- **ID.RM-3** - Organization's determination of risk tolerance is informed by its role in critical infrastructure
- **GV.RM-1** - Risk management objectives are established and agreed to by organizational stakeholders

### CIS Controls v8.1
- **Control 18.2** - Establish and maintain a remediation process
- **Control 18.4** - Remediate penetration test findings
- **Control 18.5** - Perform periodic enterprise risk assessments

## Key Takeaways

✅ **Central Repository**: Single source of truth for all organizational risks  
✅ **Complete Lifecycle**: Track from identification through closure with clear statuses  
✅ **Treatment Planning**: Document specific controls, budgets, and timelines  
✅ **Quarterly Reviews**: Regular validation of high/medium risks, annual for low risks  
✅ **Executive Visibility**: Board-level reporting with risk appetite compliance  
✅ **Automated Monitoring**: DynamoDB Streams + Lambda for real-time alerting

**Remember**: The risk register is **not a static document** but a **living management tool**—enabling continuous risk-based decision-making through systematic tracking, treatment monitoring, and executive visibility into organizational security posture.

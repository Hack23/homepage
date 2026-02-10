---
license: Apache-2.0
skill_category: governance
skill_name: risk-assessment
difficulty: intermediate
tags: [risk-assessment, risk-analysis, risk-matrix, quantified-risk, likelihood, impact, iso-27001]
related_policies:
  - Risk_Assessment_Methodology.md
  - Information_Security_Policy.md
  - Risk_Register.md
  - Asset_Register.md
compliance_frameworks:
  - ISO 27001:2022 (A.5.7 Threat Intelligence, A.8.8 Risk Assessment)
  - NIST CSF 2.0 (ID.RA-1 through ID.RA-6)
  - CIS Controls v8.1 (18.1 Risk Assessment Programs)
---

# 📊 Risk Assessment & Analysis

**Quantified Risk Evaluation for Information Security Management**

## Purpose

This skill defines **systematic risk assessment methodologies** for identifying, analyzing, and evaluating information security risks using quantified matrices and frameworks. Risk assessment enables data-driven decision-making about security investments by translating subjective threats into measurable risk ratings through standardized likelihood and impact scales.

Based on the [Risk Assessment Methodology](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Risk_Assessment_Methodology.md) from Hack23 AB's ISMS framework, this skill demonstrates how **automated risk analysis tooling directly enables proactive security posture management**—serving as competitive advantage for cybersecurity consulting methodologies.

## Rules (Risk Assessment MUST/MUST NOT)

### 🎯 MUST: Mandatory Risk Assessment Requirements

#### Risk Identification
- **MUST identify risks systematically** through structured analysis:
  - 🎯 Asset-based risk identification per [Asset Register](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Asset_Register.md)
  - 🔍 Threat intelligence integration from external sources
  - 📋 Vulnerability scanning and penetration testing results
  - 👥 Stakeholder interviews and workshops
  - 📊 Historical incident analysis

#### Risk Analysis Framework
- **MUST use 5x5 risk matrix** for consistent evaluation:
  - **Likelihood Scale** (1-5):
    - 1 - Rare: <5% annual probability
    - 2 - Unlikely: 5-25% annual probability
    - 3 - Possible: 25-50% annual probability
    - 4 - Likely: 50-75% annual probability
    - 5 - Almost Certain: >75% annual probability
  - **Impact Scale** (1-5):
    - 1 - Negligible: <€10K financial impact
    - 2 - Minor: €10K-€50K financial impact
    - 3 - Moderate: €50K-€100K financial impact
    - 4 - Major: €100K-€500K financial impact
    - 5 - Severe: >€500K financial impact

#### Quantified Risk Rating
- **MUST calculate risk scores** using matrix multiplication:
  - 🟢 **Low Risk** (1-6): Accept with monitoring
  - 🟡 **Medium Risk** (8-12): Mitigate with controls
  - 🔴 **High Risk** (15-25): Urgent treatment required
  - Formula: `Risk Score = Likelihood × Impact`

#### Risk Documentation
- **MUST document all assessments** with:
  - 📝 Risk description and business context
  - 🎯 Asset identification and classification
  - 🔍 Threat and vulnerability analysis
  - 📊 Likelihood and impact justification
  - 🛡️ Existing controls evaluation
  - 📋 Residual risk calculation
  - 👥 Risk owner assignment

#### Assessment Frequency
- **MUST perform risk assessments**:
  - 🔄 **Annual**: Comprehensive organizational risk assessment
  - 📅 **Quarterly**: High-risk area reviews
  - 🆕 **Ad-hoc**: New projects, systems, or material changes
  - 🚨 **Event-driven**: Post-incident or emerging threat response

### ⚠️ MUST NOT: Prohibited Risk Assessment Practices

#### Subjective Risk Evaluation
- **MUST NOT assess risks without quantified criteria**:
  - ❌ No "gut feeling" or unsubstantiated ratings
  - ❌ No inconsistent likelihood/impact definitions
  - ❌ No assessment without asset context
  - ❌ No risk evaluation without existing control consideration

#### Incomplete Risk Analysis
- **MUST NOT skip critical assessment steps**:
  - ❌ No risk identification without threat intelligence
  - ❌ No impact assessment without business context
  - ❌ No residual risk calculation ignoring controls
  - ❌ No risk treatment without cost-benefit analysis

#### Outdated Risk Data
- **MUST NOT rely on stale assessments**:
  - ❌ No annual assessment older than 12 months
  - ❌ No high-risk areas without quarterly review
  - ❌ No unchanged assessments after major incidents
  - ❌ No risk register without regular validation

## Examples

### Example 1: Systematic Risk Assessment (Cloud Infrastructure)

**Scenario**: Assess risks for AWS-hosted web application

**Risk Assessment Template**:
```markdown
## Risk Assessment: RA-2026-0034

**Asset**: Production Web Application (AWS ECS/RDS)
**Asset Classification**: 🔴 Critical - Customer Data Processing
**Assessment Date**: 2026-02-15
**Assessor**: Security Architect
**Risk Owner**: CTO

---

### Risk 1: Unauthorized Database Access

**Description**: External attacker gains unauthorized access to RDS database containing customer PII through SQL injection or credential compromise

**Threat Actor**: External cybercriminals, nation-state actors
**Vulnerability**: Insufficient input validation, weak database credentials
**Asset at Risk**: Customer database (500K+ records, €2M+ impact)

#### Inherent Risk (Before Controls)
- **Likelihood**: 4 - Likely (common attack vector, high attacker motivation)
- **Impact**: 5 - Severe (GDPR breach, >€500K fines + reputational damage)
- **Inherent Risk Score**: 20 🔴 HIGH

#### Existing Controls
✅ **Preventive Controls**:
- Database encryption at rest (AES-256)
- Network isolation (private subnets, security groups)
- IAM database authentication
- Web Application Firewall (AWS WAF)

✅ **Detective Controls**:
- Database activity monitoring (GuardDuty)
- CloudWatch anomaly detection
- Quarterly penetration testing

✅ **Corrective Controls**:
- Incident response playbook
- Database backup/restore procedures

#### Control Effectiveness Assessment
- **Preventive**: 80% effective (strong network isolation)
- **Detective**: 70% effective (GuardDuty alerts validated)
- **Corrective**: 90% effective (tested recovery procedures)

#### Residual Risk (After Controls)
- **Likelihood**: 2 - Unlikely (reduced by preventive controls)
- **Impact**: 4 - Major (reduced by detective/corrective controls)
- **Residual Risk Score**: 8 🟡 MEDIUM

#### Risk Treatment Decision
✅ **ACCEPT with additional monitoring**
- Justification: Residual risk within acceptable threshold
- Additional Control: Implement database query audit logging
- Review Frequency: Quarterly
```

**Automated Risk Calculation** (Python script):
```python
#!/usr/bin/env python3
"""
risk_calculator.py - Quantified risk assessment automation
Implements 5x5 risk matrix per ISMS-PUBLIC methodology
"""

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional
import json

class LikelihoodLevel(Enum):
    """Likelihood scale (1-5) with probability thresholds"""
    RARE = (1, "Rare", "< 5% annual probability")
    UNLIKELY = (2, "Unlikely", "5-25% annual probability")
    POSSIBLE = (3, "Possible", "25-50% annual probability")
    LIKELY = (4, "Likely", "50-75% annual probability")
    ALMOST_CERTAIN = (5, "Almost Certain", "> 75% annual probability")
    
    def __init__(self, score: int, label: str, description: str):
        self.score = score
        self.label = label
        self.description = description

class ImpactLevel(Enum):
    """Impact scale (1-5) with financial thresholds (EUR)"""
    NEGLIGIBLE = (1, "Negligible", "< €10,000", "Minor inconvenience")
    MINOR = (2, "Minor", "€10,000 - €50,000", "Limited business disruption")
    MODERATE = (3, "Moderate", "€50,000 - €100,000", "Significant operational impact")
    MAJOR = (4, "Major", "€100,000 - €500,000", "Severe business consequences")
    SEVERE = (5, "Severe", "> €500,000", "Catastrophic organizational impact")
    
    def __init__(self, score: int, label: str, financial: str, business: str):
        self.score = score
        self.label = label
        self.financial_impact = financial
        self.business_impact = business

@dataclass
class RiskAssessment:
    """Structured risk assessment with quantified scoring"""
    risk_id: str
    description: str
    asset_name: str
    asset_classification: str
    threat_actor: str
    vulnerability: str
    
    # Inherent risk (before controls)
    inherent_likelihood: LikelihoodLevel
    inherent_impact: ImpactLevel
    
    # Existing controls
    preventive_controls: List[str]
    detective_controls: List[str]
    corrective_controls: List[str]
    control_effectiveness: float  # 0.0-1.0
    
    # Residual risk (after controls)
    residual_likelihood: LikelihoodLevel
    residual_impact: ImpactLevel
    
    risk_owner: str
    assessment_date: str
    
    def calculate_inherent_risk(self) -> tuple[int, str]:
        """Calculate inherent risk score and rating"""
        score = self.inherent_likelihood.score * self.inherent_impact.score
        rating = self._risk_rating(score)
        return score, rating
    
    def calculate_residual_risk(self) -> tuple[int, str]:
        """Calculate residual risk score and rating"""
        score = self.residual_likelihood.score * self.residual_impact.score
        rating = self._risk_rating(score)
        return score, rating
    
    @staticmethod
    def _risk_rating(score: int) -> str:
        """Map risk score to rating per 5x5 matrix"""
        if score <= 6:
            return "🟢 LOW"
        elif score <= 12:
            return "🟡 MEDIUM"
        else:
            return "🔴 HIGH"
    
    def risk_treatment_recommendation(self) -> str:
        """Recommend treatment based on residual risk"""
        _, rating = self.calculate_residual_risk()
        
        if "LOW" in rating:
            return "✅ ACCEPT - Monitor quarterly, no additional controls required"
        elif "MEDIUM" in rating:
            return "⚠️ MITIGATE - Implement additional controls, review within 90 days"
        else:  # HIGH
            return "🚨 URGENT - Immediate treatment required, executive escalation"
    
    def to_json(self) -> str:
        """Export risk assessment to JSON"""
        inherent_score, inherent_rating = self.calculate_inherent_risk()
        residual_score, residual_rating = self.calculate_residual_risk()
        
        return json.dumps({
            'risk_id': self.risk_id,
            'description': self.description,
            'asset': {
                'name': self.asset_name,
                'classification': self.asset_classification
            },
            'inherent_risk': {
                'likelihood': self.inherent_likelihood.label,
                'impact': self.inherent_impact.label,
                'score': inherent_score,
                'rating': inherent_rating
            },
            'controls': {
                'preventive': self.preventive_controls,
                'detective': self.detective_controls,
                'corrective': self.corrective_controls,
                'effectiveness': f"{self.control_effectiveness * 100:.0f}%"
            },
            'residual_risk': {
                'likelihood': self.residual_likelihood.label,
                'impact': self.residual_impact.label,
                'score': residual_score,
                'rating': residual_rating
            },
            'treatment_recommendation': self.risk_treatment_recommendation(),
            'risk_owner': self.risk_owner,
            'assessment_date': self.assessment_date
        }, indent=2)

# Example usage
if __name__ == "__main__":
    # Assess unauthorized database access risk
    risk = RiskAssessment(
        risk_id="RA-2026-0034-R1",
        description="Unauthorized access to customer database via SQL injection",
        asset_name="Production RDS PostgreSQL Database",
        asset_classification="🔴 Critical - Customer PII",
        threat_actor="External cybercriminals, nation-state actors",
        vulnerability="Insufficient input validation, credential exposure",
        
        # Inherent risk assessment
        inherent_likelihood=LikelihoodLevel.LIKELY,
        inherent_impact=ImpactLevel.SEVERE,
        
        # Existing controls
        preventive_controls=[
            "Database encryption at rest (AES-256)",
            "Network isolation (private subnets)",
            "IAM database authentication",
            "AWS WAF with OWASP Core Rule Set"
        ],
        detective_controls=[
            "GuardDuty database activity monitoring",
            "CloudWatch anomaly detection",
            "Quarterly penetration testing"
        ],
        corrective_controls=[
            "Incident response playbook",
            "Automated backup/restore (RPO 15min)"
        ],
        control_effectiveness=0.75,  # 75% effective
        
        # Residual risk after controls
        residual_likelihood=LikelihoodLevel.UNLIKELY,
        residual_impact=ImpactLevel.MAJOR,
        
        risk_owner="CTO",
        assessment_date="2026-02-15"
    )
    
    print("=" * 70)
    print("RISK ASSESSMENT REPORT")
    print("=" * 70)
    print(risk.to_json())
    
    print("\n" + "=" * 70)
    print("RISK ANALYSIS SUMMARY")
    print("=" * 70)
    
    inherent_score, inherent_rating = risk.calculate_inherent_risk()
    residual_score, residual_rating = risk.calculate_residual_risk()
    
    print(f"Inherent Risk: {inherent_score} {inherent_rating}")
    print(f"Residual Risk: {residual_score} {residual_rating}")
    print(f"Risk Reduction: {inherent_score - residual_score} points")
    print(f"Treatment: {risk.risk_treatment_recommendation()}")
```

### Example 2: Automated Risk Scanning (AWS Lambda + SecurityHub)

**Scenario**: Continuous risk identification through automated vulnerability scanning

**Lambda Function for Automated Risk Assessment**:
```python
# lambda_risk_scanner.py - Automated risk identification via AWS SecurityHub
import boto3
import json
from datetime import datetime
from typing import Dict, List

def lambda_handler(event, context):
    """
    Automated risk assessment triggered by SecurityHub findings
    Maps vulnerabilities to risk register entries
    """
    securityhub = boto3.client('securityhub')
    dynamodb = boto3.resource('dynamodb')
    risk_table = dynamodb.Table('RiskRegister')
    
    # Retrieve SecurityHub findings (HIGH/CRITICAL only)
    findings = securityhub.get_findings(
        Filters={
            'SeverityLabel': [
                {'Value': 'CRITICAL', 'Comparison': 'EQUALS'},
                {'Value': 'HIGH', 'Comparison': 'EQUALS'}
            ],
            'WorkflowStatus': [
                {'Value': 'NEW', 'Comparison': 'EQUALS'},
                {'Value': 'NOTIFIED', 'Comparison': 'EQUALS'}
            ]
        },
        MaxResults=100
    )
    
    risks_identified = []
    
    for finding in findings['Findings']:
        # Extract vulnerability details
        finding_id = finding['Id']
        severity = finding['Severity']['Label']
        title = finding['Title']
        description = finding['Description']
        resource = finding['Resources'][0]['Id']
        
        # Map SecurityHub severity to risk matrix
        likelihood, impact = map_severity_to_risk_matrix(
            severity=severity,
            compliance_status=finding.get('Compliance', {}).get('Status'),
            remediation_available=finding.get('Remediation', {}).get('Recommendation')
        )
        
        risk_score = likelihood * impact
        risk_rating = calculate_risk_rating(risk_score)
        
        # Create risk register entry
        risk_entry = {
            'risk_id': f"AUTO-{finding_id[:8]}",
            'risk_type': 'vulnerability',
            'description': title,
            'detail': description,
            'asset': resource,
            'threat_source': 'automated_scan',
            'vulnerability': finding.get('Types', ['Unknown'])[0],
            'inherent_likelihood': likelihood,
            'inherent_impact': impact,
            'inherent_risk_score': risk_score,
            'risk_rating': risk_rating,
            'detection_date': datetime.utcnow().isoformat(),
            'risk_owner': 'security-team',
            'status': 'identified',
            'source_finding_id': finding_id
        }
        
        # Store in risk register
        risk_table.put_item(Item=risk_entry)
        risks_identified.append(risk_entry)
        
        # Escalate HIGH risks immediately
        if risk_rating == 'HIGH':
            escalate_risk_to_security_team(risk_entry)
    
    return {
        'statusCode': 200,
        'risks_identified': len(risks_identified),
        'high_risks': sum(1 for r in risks_identified if r['risk_rating'] == 'HIGH'),
        'risks': risks_identified
    }

def map_severity_to_risk_matrix(severity: str, compliance_status: str, 
                                  remediation_available: dict) -> tuple[int, int]:
    """
    Map SecurityHub finding to 5x5 risk matrix
    Returns (likelihood, impact) scores
    """
    # Likelihood based on compliance status and exploitability
    if compliance_status == 'FAILED':
        likelihood = 4  # Likely - control failure detected
    elif remediation_available and 'Url' in remediation_available:
        likelihood = 3  # Possible - known vulnerability with public exploit
    else:
        likelihood = 2  # Unlikely - theoretical vulnerability
    
    # Impact based on SecurityHub severity
    impact_mapping = {
        'CRITICAL': 5,  # Severe
        'HIGH': 4,      # Major
        'MEDIUM': 3,    # Moderate
        'LOW': 2,       # Minor
        'INFORMATIONAL': 1  # Negligible
    }
    impact = impact_mapping.get(severity, 3)
    
    return likelihood, impact

def calculate_risk_rating(score: int) -> str:
    """Map risk score to rating (LOW/MEDIUM/HIGH)"""
    if score <= 6:
        return 'LOW'
    elif score <= 12:
        return 'MEDIUM'
    else:
        return 'HIGH'

def escalate_risk_to_security_team(risk: Dict):
    """Send SNS alert for high-risk findings"""
    sns = boto3.client('sns')
    sns.publish(
        TopicArn='arn:aws:sns:eu-west-1:123456789012:SecurityTeamAlerts',
        Subject=f'🚨 HIGH RISK Identified: {risk["risk_id"]}',
        Message=json.dumps(risk, indent=2)
    )
```

**EventBridge Rule for Automated Triggering**:
```json
{
  "source": ["aws.securityhub"],
  "detail-type": ["Security Hub Findings - Imported"],
  "detail": {
    "findings": {
      "Severity": {
        "Label": ["CRITICAL", "HIGH"]
      },
      "Workflow": {
        "Status": ["NEW", "NOTIFIED"]
      }
    }
  }
}
```

### Example 3: Risk Assessment Workshop (Tabletop Exercise)

**Scenario**: Quarterly risk assessment workshop with stakeholders

**Workshop Facilitation Guide**:
```markdown
## Risk Assessment Workshop - Q1 2026

**Date**: 2026-03-15
**Duration**: 3 hours
**Participants**:
- 👨‍💼 CEO (Business Risk Owner)
- 🔧 CTO (Technical Risk Owner)
- 🔐 Security Architect (Facilitator)
- 📊 Compliance Manager
- 💼 Business Analyst

---

### Workshop Structure

#### Phase 1: Risk Identification (60 minutes)
**Objective**: Brainstorm potential security risks across all business functions

**Method**: Structured brainstorming using STRIDE threat model
- **S**poofing: Identity theft, credential compromise
- **T**ampering: Data modification, configuration changes
- **R**epudiation: Audit log deletion, non-accountability
- **I**nformation Disclosure: Data leaks, unauthorized access
- **D**enial of Service: Availability attacks, resource exhaustion
- **E**levation of Privilege: Unauthorized access escalation

**Output**: List of 20+ identified risks

#### Phase 2: Risk Analysis (90 minutes)
**Objective**: Evaluate each risk using 5x5 matrix

**Example Risk Analysis**:
```
Risk: Ransomware Attack Encrypting Customer Database

Asset at Risk:
- Production database (500K customer records)
- Business operations (€50K/day revenue)

Threat Actor:
- Cybercriminal gangs (financially motivated)
- Delivery method: Phishing, RDP exploitation

Vulnerability:
- Insufficient endpoint protection
- Limited network segmentation
- Weak user security awareness

Inherent Risk Assessment:
├─ Likelihood: 4 (Likely) - Common attack, high motivation
├─ Impact: 5 (Severe) - Business disruption + GDPR breach
└─ Inherent Score: 20 🔴 HIGH

Existing Controls:
✅ Endpoint antivirus (80% coverage)
✅ Email filtering (blocks 95% phishing)
✅ Daily backups (RPO 24h, RTO 4h)
✅ Network firewalls
⚠️ No network segmentation
⚠️ No privileged access management

Control Effectiveness: 60%

Residual Risk Assessment:
├─ Likelihood: 3 (Possible) - Reduced by email filtering
├─ Impact: 4 (Major) - Reduced by backup recovery
└─ Residual Score: 12 🟡 MEDIUM

Risk Treatment:
➡️ MITIGATE - Implement network segmentation
➡️ ENHANCE - Add privileged access management
➡️ TRANSFER - Cyber insurance (€1M coverage)
Budget: €50K, Timeline: 90 days
```

#### Phase 3: Risk Treatment (30 minutes)
**Objective**: Determine treatment strategy for each risk

**Treatment Options**:
1. ✅ **ACCEPT** - Low risks within appetite
2. ⚠️ **MITIGATE** - Implement additional controls
3. 🔄 **TRANSFER** - Insurance, outsourcing
4. ❌ **AVOID** - Discontinue risky activities

**Risk Treatment Matrix**:
| Risk ID | Description | Residual Score | Treatment | Owner | Deadline |
|---------|-------------|----------------|-----------|-------|----------|
| R-01 | Ransomware | 12 🟡 | Mitigate | CTO | 2026-06-15 |
| R-02 | SQL Injection | 8 🟡 | Mitigate | Dev Lead | 2026-04-30 |
| R-03 | Insider Threat | 15 🔴 | Mitigate | CEO | 2026-05-01 |
| R-04 | DDoS Attack | 6 🟢 | Accept | CTO | - |
```

**Workshop Deliverables**:
```python
# workshop_report_generator.py
from dataclasses import dataclass
from typing import List
import datetime

@dataclass
class WorkshopRisk:
    risk_id: str
    description: str
    inherent_score: int
    residual_score: int
    treatment: str
    owner: str
    deadline: str

def generate_workshop_report(risks: List[WorkshopRisk]) -> str:
    """Generate executive summary from workshop"""
    
    high_risks = [r for r in risks if r.residual_score >= 15]
    medium_risks = [r for r in risks if 8 <= r.residual_score < 15]
    low_risks = [r for r in risks if r.residual_score < 8]
    
    report = f"""
# Risk Assessment Workshop Report
**Date**: {datetime.date.today().isoformat()}
**Participants**: CEO, CTO, Security Architect, Compliance Manager

## Executive Summary
- **Total Risks Identified**: {len(risks)}
- **High Risks (15-25)**: {len(high_risks)} 🔴
- **Medium Risks (8-14)**: {len(medium_risks)} 🟡
- **Low Risks (1-7)**: {len(low_risks)} 🟢

## Risk Treatment Summary
- **Mitigate**: {sum(1 for r in risks if r.treatment == 'mitigate')} risks
- **Accept**: {sum(1 for r in risks if r.treatment == 'accept')} risks
- **Transfer**: {sum(1 for r in risks if r.treatment == 'transfer')} risks

## Priority Actions (Next 90 Days)
"""
    
    for risk in sorted(risks, key=lambda r: r.residual_score, reverse=True)[:5]:
        report += f"\n### {risk.risk_id}: {risk.description}"
        report += f"\n- **Residual Risk**: {risk.residual_score}"
        report += f"\n- **Treatment**: {risk.treatment.upper()}"
        report += f"\n- **Owner**: {risk.owner}"
        report += f"\n- **Deadline**: {risk.deadline}\n"
    
    return report

# Example usage
risks = [
    WorkshopRisk("R-01", "Ransomware attack", 20, 12, "mitigate", "CTO", "2026-06-15"),
    WorkshopRisk("R-02", "SQL injection", 16, 8, "mitigate", "Dev Lead", "2026-04-30"),
    WorkshopRisk("R-03", "Insider threat", 20, 15, "mitigate", "CEO", "2026-05-01"),
    WorkshopRisk("R-04", "DDoS attack", 12, 6, "accept", "CTO", "N/A"),
]

print(generate_workshop_report(risks))
```

### Example 4: Continuous Risk Monitoring (CloudWatch + Grafana)

**Scenario**: Real-time risk posture dashboard

**CloudWatch Custom Metrics**:
```python
# risk_metrics_publisher.py - Publish risk KPIs to CloudWatch
import boto3
from datetime import datetime

class RiskMetricsPublisher:
    """Publish risk assessment metrics to CloudWatch"""
    
    def __init__(self):
        self.cloudwatch = boto3.client('cloudwatch')
        self.namespace = 'Hack23/RiskManagement'
    
    def publish_risk_metrics(self, risk_register: list):
        """Calculate and publish risk posture metrics"""
        
        # Calculate risk distribution
        high_risks = sum(1 for r in risk_register if r['residual_score'] >= 15)
        medium_risks = sum(1 for r in risk_register if 8 <= r['residual_score'] < 15)
        low_risks = sum(1 for r in risk_register if r['residual_score'] < 8)
        
        # Calculate average risk score
        avg_risk_score = sum(r['residual_score'] for r in risk_register) / len(risk_register)
        
        # Calculate treatment status
        open_risks = sum(1 for r in risk_register if r['status'] == 'open')
        mitigated_risks = sum(1 for r in risk_register if r['status'] == 'mitigated')
        accepted_risks = sum(1 for r in risk_register if r['status'] == 'accepted')
        
        # Publish metrics
        self.cloudwatch.put_metric_data(
            Namespace=self.namespace,
            MetricData=[
                {
                    'MetricName': 'HighRiskCount',
                    'Value': high_risks,
                    'Unit': 'Count',
                    'Timestamp': datetime.utcnow()
                },
                {
                    'MetricName': 'MediumRiskCount',
                    'Value': medium_risks,
                    'Unit': 'Count',
                    'Timestamp': datetime.utcnow()
                },
                {
                    'MetricName': 'LowRiskCount',
                    'Value': low_risks,
                    'Unit': 'Count',
                    'Timestamp': datetime.utcnow()
                },
                {
                    'MetricName': 'AverageRiskScore',
                    'Value': avg_risk_score,
                    'Unit': 'None',
                    'Timestamp': datetime.utcnow()
                },
                {
                    'MetricName': 'OpenRisks',
                    'Value': open_risks,
                    'Unit': 'Count',
                    'Timestamp': datetime.utcnow()
                },
                {
                    'MetricName': 'MitigatedRisks',
                    'Value': mitigated_risks,
                    'Unit': 'Count',
                    'Timestamp': datetime.utcnow()
                }
            ]
        )
        
        print(f"✅ Published risk metrics to CloudWatch:")
        print(f"   - High Risks: {high_risks}")
        print(f"   - Medium Risks: {medium_risks}")
        print(f"   - Low Risks: {low_risks}")
        print(f"   - Average Risk Score: {avg_risk_score:.2f}")
```

**Grafana Dashboard JSON** (risk-posture-dashboard.json):
```json
{
  "dashboard": {
    "title": "Risk Management Posture",
    "panels": [
      {
        "title": "Risk Distribution",
        "type": "piechart",
        "targets": [
          {
            "expr": "cloudwatch_Hack23_RiskManagement_HighRiskCount",
            "legendFormat": "🔴 High Risk"
          },
          {
            "expr": "cloudwatch_Hack23_RiskManagement_MediumRiskCount",
            "legendFormat": "🟡 Medium Risk"
          },
          {
            "expr": "cloudwatch_Hack23_RiskManagement_LowRiskCount",
            "legendFormat": "🟢 Low Risk"
          }
        ]
      },
      {
        "title": "Average Risk Score Trend",
        "type": "graph",
        "targets": [
          {
            "expr": "cloudwatch_Hack23_RiskManagement_AverageRiskScore",
            "legendFormat": "Average Risk Score"
          }
        ],
        "alert": {
          "name": "Risk Score Threshold",
          "conditions": [
            {
              "evaluator": {
                "type": "gt",
                "params": [10]
              },
              "operator": {
                "type": "and"
              },
              "query": {
                "params": ["A", "5m", "now"]
              },
              "reducer": {
                "type": "avg"
              }
            }
          ],
          "message": "🚨 Average risk score exceeded threshold (10)"
        }
      },
      {
        "title": "Risk Treatment Progress",
        "type": "stat",
        "targets": [
          {
            "expr": "cloudwatch_Hack23_RiskManagement_MitigatedRisks / cloudwatch_Hack23_RiskManagement_OpenRisks * 100",
            "legendFormat": "Treatment Rate %"
          }
        ]
      }
    ]
  }
}
```

## Related ISMS Policies

### Core Risk Management Framework
- [📊 Risk Assessment Methodology](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Risk_Assessment_Methodology.md) — Complete 5x5 matrix framework and assessment procedures
- [📋 Risk Register](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Risk_Register.md) — Enterprise risk tracking and treatment plans
- [🔐 Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md) — Risk management governance and accountability

### Asset and Context
- [💼 Asset Register](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Asset_Register.md) — Asset classification and inventory for risk assessment
- [🌐 External Stakeholder Registry](https://github.com/Hack23/ISMS-PUBLIC/blob/main/External_Stakeholder_Registry.md) — Regulatory and stakeholder context

### Operational Integration
- [🔄 Change Management](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Change_Management.md) — Risk-based change classification
- [🚨 Incident Response Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Incident_Response_Plan.md) — Event-driven risk assessment
- [🆘 Business Continuity Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Business_Continuity_Plan.md) — Business impact analysis

## Compliance Mapping

### ISO 27001:2022
- **A.5.7 Threat Intelligence** - Systematic threat identification and analysis
- **A.8.8 Management of Technical Vulnerabilities** - Vulnerability-based risk assessment
- **Clause 6.1.2 Information Security Risk Assessment** - Risk assessment methodology requirements

### NIST Cybersecurity Framework 2.0
- **ID.RA-1** - Asset vulnerabilities are identified and documented
- **ID.RA-2** - Cyber threat intelligence is received from information sharing forums
- **ID.RA-3** - Threats, vulnerabilities, likelihoods, and impacts are used to determine risk
- **ID.RA-4** - Potential business impacts and likelihoods are identified
- **ID.RA-5** - Threats, vulnerabilities, likelihoods, and impacts are used to determine risk
- **ID.RA-6** - Risk responses are identified and prioritized

### CIS Controls v8.1
- **Control 18.1** - Establish and maintain a risk assessment program
- **Control 18.2** - Establish and maintain a remediation process
- **Control 18.3** - Remediate detected vulnerabilities

## Key Takeaways

✅ **Quantified Assessment**: Use 5x5 matrix with standardized likelihood/impact scales  
✅ **Systematic Identification**: Leverage threat intelligence, vulnerability scans, and stakeholder input  
✅ **Control Evaluation**: Calculate residual risk after existing controls assessment  
✅ **Automated Monitoring**: Integrate SecurityHub findings into risk register automatically  
✅ **Regular Review**: Annual comprehensive, quarterly high-risk, ad-hoc for changes  
✅ **Risk-Based Decisions**: Data-driven treatment strategies with cost-benefit analysis

**Remember**: Risk assessment is **not a one-time compliance exercise** but a **continuous management process**—enabling proactive security posture improvement through systematic threat evaluation and control effectiveness measurement.

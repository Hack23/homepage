---
license: Apache-2.0
skill_category: governance
skill_name: supplier-management
difficulty: advanced
tags: [supplier-management, third-party-risk, vendor-security, due-diligence, sla, supply-chain]
related_policies:
  - SUPPLIER.md
  - Third_Party_Management_Policy.md
  - Risk_Assessment_Methodology.md
  - Data_Protection_Policy.md
compliance_frameworks:
  - ISO 27001:2022 (A.5.19 Supplier Relationships, A.5.20 Supplier Agreements)
  - NIST CSF 2.0 (ID.SC-1 through ID.SC-5, GV.SC-1 through GV.SC-10)
  - CIS Controls v8.1 (15.1 Third-Party Service Provider Inventory)
---

# 🤝 Supplier & Third-Party Risk Management

**Comprehensive Vendor Security Posture Assessment and SLA Management**

## Purpose

This skill defines **systematic supplier and third-party risk management** for evaluating vendor security posture, conducting due diligence assessments, managing contractual obligations, and monitoring ongoing compliance. Supplier management extends the organization's security perimeter to include external parties who process data or provide critical services.

Based on the [Supplier Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/SUPPLIER.md) from Hack23 AB's ISMS framework, this skill demonstrates how **automated vendor risk assessment directly enables supply chain security and regulatory compliance**—serving as competitive advantage for cybersecurity consulting methodologies.

## Rules (Supplier Management MUST/MUST NOT)

### 🎯 MUST: Mandatory Supplier Management Requirements

#### Supplier Classification
- **MUST classify all suppliers** by risk tier:
  - 🔴 **Critical**: Process sensitive data, business-essential services, regulatory scope
  - 🟠 **High**: Access to internal systems, moderate data exposure
  - 🟡 **Medium**: Limited system access, low-sensitivity data
  - 🟢 **Low**: No data access, commodity services

#### Due Diligence Assessment
- **MUST conduct pre-contract assessments**:
  - 📋 **Security Questionnaire**: ISO 27001, SOC 2, security controls validation
  - 🔍 **Financial Stability**: Credit rating, business continuity capability
  - 📊 **Compliance Verification**: GDPR, ISO certifications, industry regulations
  - 🎯 **References**: Customer testimonials, security incident history
  - 🛡️ **Insurance Coverage**: Cyber liability, errors & omissions
  - 📝 **Data Processing Addendum (DPA)**: GDPR Article 28 compliance

#### Contractual Requirements
- **MUST include in supplier contracts**:
  - 🔐 **Security Obligations**: Encryption, access controls, incident notification
  - 📊 **SLA Commitments**: Availability, performance, support response times
  - 🔍 **Audit Rights**: Right to audit security controls (ISO 27001 A.5.19)
  - 📋 **Data Protection**: Data residency, sub-processor notification, deletion
  - 🚨 **Breach Notification**: 24-hour notification requirement
  - 📅 **Contract Renewal**: Annual security reassessment
  - ⚖️ **Liability**: Financial caps, indemnification clauses

#### Ongoing Monitoring
- **MUST monitor supplier compliance**:
  - 📊 **Quarterly**: SLA performance review, security questionnaire updates
  - 📅 **Annual**: Comprehensive security assessment, contract renewal
  - 🚨 **Ad-hoc**: Post-incident reviews, major supplier changes
  - 📈 **Metrics**: Availability %, response times, incident count
  - 🔄 **Certifications**: Verify ISO 27001, SOC 2 validity

#### Supplier Offboarding
- **MUST execute secure offboarding**:
  - 🔑 **Access Revocation**: Immediate credential/token deletion
  - 📁 **Data Return**: Secure transfer or certified destruction
  - 📋 **Asset Recovery**: Hardware, software licenses, documentation
  - 🔍 **Final Audit**: Verify data deletion compliance
  - 📝 **Documentation**: Offboarding checklist and sign-off

### ⚠️ MUST NOT: Prohibited Supplier Management Practices

#### Unauthorized Suppliers
- **MUST NOT engage suppliers without**:
  - ❌ No vendor onboarding without security assessment
  - ❌ No data sharing before DPA execution
  - ❌ No production access before security review
  - ❌ No payment processing without PCI-DSS validation

#### Inadequate Oversight
- **MUST NOT maintain supplier relationships without**:
  - ❌ No annual security reassessments
  - ❌ No SLA monitoring or performance tracking
  - ❌ No breach notification procedures
  - ❌ No documented exit strategy

#### Shadow IT Suppliers
- **MUST NOT allow**:
  - ❌ No department-level SaaS without IT approval
  - ❌ No unapproved cloud services
  - ❌ No personal accounts for business data
  - ❌ No bypassing procurement process

## Examples

### Example 1: Comprehensive Supplier Risk Assessment

**Scenario**: Evaluate new cloud hosting provider for production workloads

**Supplier Assessment Template**:
```markdown
## Supplier Assessment: SA-2026-0023

### Supplier Information
**Supplier Name**: CloudTech Solutions AB
**Service Type**: Cloud Infrastructure (IaaS)
**Proposed Use**: Production application hosting
**Data Classification**: 🔴 Critical - Customer PII, payment data
**Contract Value**: €120,000/year
**Assessment Date**: 2026-02-15
**Assessor**: Security Architect

---

### Risk Classification

**Initial Risk Tier**: 🔴 **CRITICAL**
**Justification**:
- Processes customer PII (GDPR scope)
- Hosts production payment systems (PCI-DSS scope)
- Business-critical service (99.9% availability requirement)
- Access to encryption keys and credentials

**Required Assessment Depth**: Comprehensive due diligence

---

### Security Posture Assessment

#### Certifications & Compliance ✅
- ✅ ISO 27001:2022 (valid until 2027-03-15)
- ✅ SOC 2 Type II (latest report: 2025-12-01)
- ✅ PCI-DSS Level 1 Service Provider
- ✅ GDPR compliant (EU data residency)
- ✅ NIS2 Directive compliance (Swedish regulation)

**Verification Method**: Certificate copies obtained, SSAE 18 SOC 2 report reviewed

#### Security Controls Evaluation

**Preventive Controls** (Score: 85/100):
- ✅ **Access Control**: MFA enforced, RBAC, privileged access management
- ✅ **Encryption**: AES-256 at rest, TLS 1.3 in transit
- ✅ **Network Security**: Microsegmentation, IDS/IPS, DDoS protection
- ✅ **Physical Security**: ISO 27001-certified datacenters (Tier III+)
- ⚠️ **Patching**: 30-day SLA (prefer 14 days for critical)

**Detective Controls** (Score: 90/100):
- ✅ **Logging**: Centralized SIEM, 1-year retention
- ✅ **Monitoring**: 24/7 SOC, real-time alerting
- ✅ **Penetration Testing**: Quarterly external, annual internal
- ✅ **Vulnerability Scanning**: Weekly automated scans

**Corrective Controls** (Score: 95/100):
- ✅ **Incident Response**: 24/7 team, <1h initial response
- ✅ **Backup/DR**: Daily backups, 4h RTO, 15min RPO
- ✅ **Business Continuity**: Multi-region failover
- ✅ **Insurance**: €10M cyber liability coverage

**Overall Security Score**: 90/100 ✅ **PASS** (threshold: 85)

#### Financial Stability ✅
- **Credit Rating**: AA- (S&P equivalent)
- **Years in Business**: 12 years
- **Annual Revenue**: €50M
- **Customer Base**: 2,000+ clients (including Fortune 500)
- **Financial Risk**: 🟢 LOW

#### References & Due Diligence ✅
**Customer References** (3 contacted):
1. TechCorp AB - "Excellent uptime, responsive support" (5/5)
2. FinanceApp Ltd - "Strong security posture, smooth SOC 2 audits" (4.5/5)
3. RetailChain SE - "Minor service interruptions, good recovery" (4/5)

**Security Incident History**:
- No major breaches in past 5 years
- 2 minor incidents (DDoS, patched within SLA)
- Transparent incident disclosure practices

---

### Data Protection Assessment

#### GDPR Article 28 Compliance ✅
- ✅ **Data Processing Addendum (DPA)**: Signed, GDPR-compliant
- ✅ **Sub-processors**: Documented, notification upon changes
- ✅ **Data Residency**: EU-only (Stockholm, Amsterdam)
- ✅ **Data Subject Rights**: Procedures for access, erasure, portability
- ✅ **Data Breach Notification**: 24-hour notification commitment

#### Data Security Controls
- **Data-at-Rest Encryption**: AES-256 with customer-managed keys (AWS KMS)
- **Data-in-Transit Encryption**: TLS 1.3, perfect forward secrecy
- **Data Segregation**: Logical separation per tenant
- **Data Backup**: Encrypted, geographically distributed, 35-day retention
- **Data Disposal**: NIST SP 800-88 Rev. 1 certified destruction

---

### Service Level Agreements (SLAs)

#### Availability SLA
- **Uptime Commitment**: 99.95% monthly (max 21.6 min downtime)
- **Measurement**: Calculated per customer account
- **Exclusions**: Scheduled maintenance (4h/month, off-peak)
- **Credits**: 10% monthly fee per 0.5% below SLA

#### Performance SLA
- **API Response Time**: p95 <200ms, p99 <500ms
- **Database Latency**: p95 <50ms, p99 <100ms
- **Network Throughput**: 10 Gbps per instance

#### Support SLA
- **Critical Issues**: 15min initial response, 4h resolution target
- **High Issues**: 1h initial response, 24h resolution target
- **Medium Issues**: 4h initial response, 72h resolution target
- **Support Hours**: 24/7/365 via phone, email, portal

#### Security SLA
- **Vulnerability Patching**: Critical <14 days, High <30 days
- **Incident Response**: Initial response <1h
- **Penetration Testing**: Quarterly + customer-requested (2/year)

---

### Risk Mitigation & Contract Terms

#### Key Contract Clauses

**Audit Rights** (ISO 27001 A.5.19):
```
Customer shall have the right to audit Supplier's security controls
annually, with 30 days' advance notice. Audits may be conducted by
Customer or designated third-party auditor. Supplier shall provide
access to facilities, systems, and documentation.
```

**Breach Notification** (GDPR Article 33):
```
Supplier shall notify Customer of any data breach within 24 hours of
discovery. Notification shall include breach scope, affected data,
remediation actions, and root cause analysis.
```

**Data Deletion** (GDPR Article 17):
```
Upon contract termination, Supplier shall securely delete or return
all Customer data within 30 days. Deletion shall be certified per
NIST SP 800-88 Rev. 1 with attestation letter.
```

**Liability Cap**:
```
Supplier liability for data breaches: €5M (uncapped for gross negligence)
General liability cap: €1M per incident (€3M aggregate annual)
```

#### Risk Mitigation Actions
1. ✅ **Escrow Agreement**: Source code held by third-party (business continuity)
2. ✅ **Multi-Region Deployment**: Avoid single-region lock-in
3. ✅ **Data Encryption**: Customer-managed keys (KMS) for data sovereignty
4. ✅ **Exit Strategy**: Documented migration plan, annual testing

---

### Assessment Decision

**Recommendation**: ✅ **APPROVE** with conditions

**Conditions**:
1. Upgrade patching SLA from 30 days to 14 days for critical vulnerabilities
2. Add quarterly security questionnaire updates
3. Require notification 90 days before sub-processor changes
4. Include annual penetration test report sharing

**Contract Approval Authority**: CTO + DPO (critical supplier)

**Monitoring Plan**:
- Monthly: SLA performance dashboard review
- Quarterly: Security questionnaire update, incident log review
- Annual: Comprehensive security reassessment, SOC 2 report review

**Next Review Date**: 2027-02-15
```

**Automated Supplier Assessment (Python):**
```python
# supplier_assessment_automation.py
from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import requests

@dataclass
class SupplierCertification:
    """Supplier security certification"""
    name: str  # e.g., "ISO 27001", "SOC 2 Type II"
    issuer: str
    valid_until: datetime
    verification_url: Optional[str] = None

@dataclass
class SupplierSLA:
    """Service Level Agreement metrics"""
    metric_name: str
    commitment: str
    measurement_method: str
    penalty: str

@dataclass
class SupplierAssessment:
    """Comprehensive supplier risk assessment"""
    supplier_id: str
    supplier_name: str
    service_type: str
    data_classification: str  # critical, high, medium, low
    contract_value_annual: float
    
    # Security posture
    certifications: List[SupplierCertification]
    security_score: int  # 0-100
    preventive_controls_score: int
    detective_controls_score: int
    corrective_controls_score: int
    
    # Financial stability
    credit_rating: str
    years_in_business: int
    annual_revenue: float
    
    # SLAs
    slas: List[SupplierSLA]
    
    # Compliance
    gdpr_compliant: bool
    dpa_signed: bool
    data_residency: str
    
    # Risk assessment
    risk_tier: str  # critical, high, medium, low
    assessment_date: datetime
    next_review_date: datetime
    
    def calculate_risk_score(self) -> int:
        """Calculate overall supplier risk score (0-100, lower is better)"""
        
        # Security score component (40% weight)
        security_component = (100 - self.security_score) * 0.4
        
        # Financial stability component (20% weight)
        financial_risk = self._assess_financial_risk()
        financial_component = financial_risk * 0.2
        
        # Compliance component (30% weight)
        compliance_score = self._assess_compliance()
        compliance_component = (100 - compliance_score) * 0.3
        
        # Data classification component (10% weight)
        classification_risk = {
            'critical': 100,
            'high': 75,
            'medium': 50,
            'low': 25
        }[self.data_classification.lower()]
        classification_component = classification_risk * 0.1
        
        total_risk = (security_component + financial_component + 
                     compliance_component + classification_component)
        
        return int(total_risk)
    
    def _assess_financial_risk(self) -> int:
        """Assess financial stability risk (0-100)"""
        risk = 50  # Baseline
        
        # Credit rating impact
        if self.credit_rating in ['AAA', 'AA+', 'AA', 'AA-']:
            risk -= 30
        elif self.credit_rating in ['A+', 'A', 'A-']:
            risk -= 15
        
        # Business maturity impact
        if self.years_in_business > 10:
            risk -= 10
        elif self.years_in_business > 5:
            risk -= 5
        
        # Revenue stability impact
        if self.annual_revenue > 100_000_000:  # €100M+
            risk -= 10
        elif self.annual_revenue > 10_000_000:  # €10M+
            risk -= 5
        
        return max(0, min(100, risk))
    
    def _assess_compliance(self) -> int:
        """Assess regulatory compliance (0-100)"""
        score = 0
        
        # GDPR compliance
        if self.gdpr_compliant and self.dpa_signed:
            score += 30
        
        # EU data residency
        if 'EU' in self.data_residency or 'Sweden' in self.data_residency:
            score += 20
        
        # Security certifications
        cert_names = [c.name for c in self.certifications]
        if 'ISO 27001' in ' '.join(cert_names):
            score += 25
        if 'SOC 2' in ' '.join(cert_names):
            score += 15
        if 'PCI-DSS' in ' '.join(cert_names):
            score += 10
        
        return min(100, score)
    
    def get_risk_tier_recommendation(self) -> str:
        """Recommend risk tier based on assessment"""
        risk_score = self.calculate_risk_score()
        
        if risk_score >= 75:
            return '🔴 CRITICAL'
        elif risk_score >= 50:
            return '🟠 HIGH'
        elif risk_score >= 25:
            return '🟡 MEDIUM'
        else:
            return '🟢 LOW'
    
    def approval_required_from(self) -> List[str]:
        """Determine required approvals based on risk tier"""
        risk_tier = self.get_risk_tier_recommendation()
        
        if '🔴 CRITICAL' in risk_tier:
            return ['CTO', 'DPO', 'CEO']
        elif '🟠 HIGH' in risk_tier:
            return ['CTO', 'DPO']
        elif '🟡 MEDIUM' in risk_tier:
            return ['Security Architect']
        else:
            return ['Procurement Manager']
    
    def generate_monitoring_plan(self) -> Dict:
        """Generate monitoring schedule based on risk"""
        risk_tier = self.get_risk_tier_recommendation()
        
        if '🔴 CRITICAL' in risk_tier:
            return {
                'monthly': ['SLA review', 'incident log', 'uptime metrics'],
                'quarterly': ['Security questionnaire', 'certification validation'],
                'annual': ['Comprehensive reassessment', 'SOC 2 report review', 'penetration test'],
                'ad_hoc': ['Post-incident review', 'major change notification']
            }
        elif '🟠 HIGH' in risk_tier:
            return {
                'quarterly': ['SLA review', 'security questionnaire'],
                'annual': ['Comprehensive reassessment', 'certification validation'],
                'ad_hoc': ['Post-incident review']
            }
        else:
            return {
                'annual': ['Security questionnaire', 'certification validation'],
                'ad_hoc': ['Post-incident review']
            }

# Example usage
assessment = SupplierAssessment(
    supplier_id='SUP-2026-0023',
    supplier_name='CloudTech Solutions AB',
    service_type='Cloud Infrastructure (IaaS)',
    data_classification='critical',
    contract_value_annual=120000,
    certifications=[
        SupplierCertification('ISO 27001:2022', 'BSI', datetime(2027, 3, 15)),
        SupplierCertification('SOC 2 Type II', 'EY', datetime(2026, 12, 1)),
        SupplierCertification('PCI-DSS Level 1', 'QSA', datetime(2026, 8, 30))
    ],
    security_score=90,
    preventive_controls_score=85,
    detective_controls_score=90,
    corrective_controls_score=95,
    credit_rating='AA-',
    years_in_business=12,
    annual_revenue=50_000_000,
    slas=[
        SupplierSLA('Uptime', '99.95%', 'Monthly calculation', '10% credit per 0.5% below SLA'),
        SupplierSLA('Support Response', '<15min critical', 'Ticket timestamp', 'Credit for missed SLA')
    ],
    gdpr_compliant=True,
    dpa_signed=True,
    data_residency='EU (Sweden, Netherlands)',
    risk_tier='critical',
    assessment_date=datetime(2026, 2, 15),
    next_review_date=datetime(2027, 2, 15)
)

print("=" * 70)
print("SUPPLIER RISK ASSESSMENT SUMMARY")
print("=" * 70)
print(f"Supplier: {assessment.supplier_name}")
print(f"Overall Risk Score: {assessment.calculate_risk_score()}/100")
print(f"Recommended Tier: {assessment.get_risk_tier_recommendation()}")
print(f"Approval Required From: {', '.join(assessment.approval_required_from())}")
print(f"\nMonitoring Plan:")
for frequency, activities in assessment.generate_monitoring_plan().items():
    print(f"  {frequency.upper()}: {', '.join(activities)}")
```

### Example 2: Supplier Performance Monitoring (AWS Lambda + CloudWatch)

**Scenario**: Automated SLA monitoring and alerting

**Lambda Function for SLA Monitoring**:
```python
# lambda_supplier_sla_monitor.py
import boto3
import json
from datetime import datetime, timedelta
from typing import Dict, List

def lambda_handler(event, context):
    """
    Monitor supplier SLA compliance and generate alerts
    Triggered daily by EventBridge
    """
    
    dynamodb = boto3.resource('dynamodb')
    cloudwatch = boto3.client('cloudwatch')
    sns = boto3.client('sns')
    
    supplier_table = dynamodb.Table('SupplierRegister')
    sla_metrics_table = dynamodb.Table('SupplierSLAMetrics')
    
    # Get all active critical suppliers
    suppliers = supplier_table.scan(
        FilterExpression='risk_tier = :tier AND contract_status = :status',
        ExpressionAttributeValues={
            ':tier': 'critical',
            ':status': 'active'
        }
    )['Items']
    
    sla_violations = []
    
    for supplier in suppliers:
        supplier_id = supplier['supplier_id']
        supplier_name = supplier['supplier_name']
        
        # Check availability SLA
        uptime_violation = check_uptime_sla(
            supplier_id=supplier_id,
            target_uptime=supplier.get('sla_uptime_target', 99.95)
        )
        
        # Check response time SLA
        response_time_violation = check_response_time_sla(
            supplier_id=supplier_id,
            target_p95=supplier.get('sla_response_p95_ms', 200)
        )
        
        # Check support SLA
        support_violation = check_support_sla(
            supplier_id=supplier_id,
            target_response_min=supplier.get('sla_support_response_min', 15)
        )
        
        # Collect violations
        violations = []
        if uptime_violation:
            violations.append(uptime_violation)
        if response_time_violation:
            violations.append(response_time_violation)
        if support_violation:
            violations.append(support_violation)
        
        if violations:
            sla_violations.append({
                'supplier_id': supplier_id,
                'supplier_name': supplier_name,
                'violations': violations
            })
            
            # Send alert
            send_sla_violation_alert(supplier, violations)
            
            # Publish CloudWatch metrics
            publish_sla_metrics(cloudwatch, supplier_id, violations)
    
    return {
        'statusCode': 200,
        'suppliers_monitored': len(suppliers),
        'violations_detected': len(sla_violations),
        'violations': sla_violations
    }

def check_uptime_sla(supplier_id: str, target_uptime: float) -> Dict:
    """Check availability SLA compliance"""
    cloudwatch = boto3.client('cloudwatch')
    
    # Query CloudWatch for uptime metrics (last 30 days)
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=30)
    
    response = cloudwatch.get_metric_statistics(
        Namespace='Hack23/Suppliers',
        MetricName='Availability',
        Dimensions=[
            {'Name': 'SupplierID', 'Value': supplier_id}
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=2592000,  # 30 days
        Statistics=['Average']
    )
    
    if response['Datapoints']:
        actual_uptime = response['Datapoints'][0]['Average']
        
        if actual_uptime < target_uptime:
            downtime_minutes = (30 * 24 * 60) * ((100 - actual_uptime) / 100)
            allowed_downtime = (30 * 24 * 60) * ((100 - target_uptime) / 100)
            
            return {
                'sla_type': 'availability',
                'target': f"{target_uptime}%",
                'actual': f"{actual_uptime:.2f}%",
                'downtime_minutes': round(downtime_minutes, 1),
                'allowed_downtime_minutes': round(allowed_downtime, 1),
                'severity': 'HIGH' if actual_uptime < (target_uptime - 1) else 'MEDIUM'
            }
    
    return None

def check_response_time_sla(supplier_id: str, target_p95: int) -> Dict:
    """Check API response time SLA"""
    cloudwatch = boto3.client('cloudwatch')
    
    # Query p95 response time (last 24 hours)
    response = cloudwatch.get_metric_statistics(
        Namespace='Hack23/Suppliers',
        MetricName='ResponseTime',
        Dimensions=[
            {'Name': 'SupplierID', 'Value': supplier_id}
        ],
        StartTime=datetime.utcnow() - timedelta(hours=24),
        EndTime=datetime.utcnow(),
        Period=86400,  # 24 hours
        Statistics=['ExtendedStatistics'],
        ExtendedStatistics=['p95']
    )
    
    if response['Datapoints']:
        actual_p95 = response['Datapoints'][0]['ExtendedStatistics']['p95']
        
        if actual_p95 > target_p95:
            return {
                'sla_type': 'performance',
                'metric': 'API Response Time (p95)',
                'target': f"{target_p95}ms",
                'actual': f"{actual_p95:.0f}ms",
                'deviation': f"+{actual_p95 - target_p95:.0f}ms",
                'severity': 'HIGH' if actual_p95 > (target_p95 * 1.5) else 'MEDIUM'
            }
    
    return None

def check_support_sla(supplier_id: str, target_response_min: int) -> Dict:
    """Check support ticket response time SLA"""
    dynamodb = boto3.resource('dynamodb')
    tickets_table = dynamodb.Table('SupportTickets')
    
    # Query tickets from last 30 days
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=30)
    
    response = tickets_table.query(
        IndexName='SupplierDateIndex',
        KeyConditionExpression='supplier_id = :sid AND created_date > :start',
        ExpressionAttributeValues={
            ':sid': supplier_id,
            ':start': start_time.isoformat()
        }
    )
    
    tickets = response['Items']
    
    if tickets:
        # Calculate average response time
        total_response_time = 0
        sla_breaches = 0
        
        for ticket in tickets:
            if ticket.get('first_response_time'):
                response_minutes = ticket['first_response_time']
                total_response_time += response_minutes
                
                if response_minutes > target_response_min:
                    sla_breaches += 1
        
        avg_response = total_response_time / len(tickets)
        breach_rate = (sla_breaches / len(tickets)) * 100
        
        if breach_rate > 10:  # >10% breach rate unacceptable
            return {
                'sla_type': 'support',
                'metric': 'Critical Ticket Response Time',
                'target': f"<{target_response_min} min",
                'actual': f"{avg_response:.1f} min avg",
                'breach_rate': f"{breach_rate:.1f}%",
                'total_breaches': sla_breaches,
                'total_tickets': len(tickets),
                'severity': 'HIGH' if breach_rate > 25 else 'MEDIUM'
            }
    
    return None

def send_sla_violation_alert(supplier: Dict, violations: List[Dict]):
    """Send SNS alert for SLA violations"""
    sns = boto3.client('sns')
    
    severity = max([v['severity'] for v in violations])
    
    message = f"""
SLA VIOLATION DETECTED

Supplier: {supplier['supplier_name']} ({supplier['supplier_id']})
Risk Tier: {supplier['risk_tier'].upper()}
Contract Value: €{supplier['contract_value_annual']:,.0f}/year

VIOLATIONS ({len(violations)}):
"""
    
    for v in violations:
        message += f"\n{v['sla_type'].upper()}:"
        message += f"\n  Target: {v['target']}"
        message += f"\n  Actual: {v['actual']}"
        message += f"\n  Severity: {v['severity']}\n"
    
    message += f"""
ACTION REQUIRED:
1. Contact supplier regarding SLA breach
2. Document violation in supplier register
3. Calculate SLA credits owed
4. Schedule contract review if pattern continues

Contract Manager: {supplier.get('contract_manager', 'Unknown')}
Next Review: {supplier.get('next_review_date', 'Not scheduled')}
    """
    
    sns.publish(
        TopicArn='arn:aws:sns:eu-west-1:123456789012:SupplierManagement',
        Subject=f'{"🔴" if severity == "HIGH" else "⚠️"} SLA Violation: {supplier["supplier_name"]}',
        Message=message
    )

def publish_sla_metrics(cloudwatch, supplier_id: str, violations: List[Dict]):
    """Publish SLA violation metrics to CloudWatch"""
    
    cloudwatch.put_metric_data(
        Namespace='Hack23/SupplierCompliance',
        MetricData=[
            {
                'MetricName': 'SLAViolations',
                'Value': len(violations),
                'Unit': 'Count',
                'Timestamp': datetime.utcnow(),
                'Dimensions': [
                    {'Name': 'SupplierID', 'Value': supplier_id}
                ]
            },
            {
                'MetricName': 'HighSeverityViolations',
                'Value': sum(1 for v in violations if v['severity'] == 'HIGH'),
                'Unit': 'Count',
                'Timestamp': datetime.utcnow(),
                'Dimensions': [
                    {'Name': 'SupplierID', 'Value': supplier_id}
                ]
            }
        ]
    )
```

### Example 3: Supplier Offboarding Workflow (Step Functions)

**Scenario**: Automated secure supplier termination

**Step Functions State Machine**:
```json
{
  "Comment": "Supplier Offboarding with Secure Data Disposal",
  "StartAt": "ValidateOffboardingRequest",
  "States": {
    "ValidateOffboardingRequest": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:ValidateSupplierOffboarding",
      "Next": "NotifyStakeholders"
    },
    "NotifyStakeholders": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:NotifySupplierOffboarding",
      "Next": "RevokeAccessCredentials"
    },
    "RevokeAccessCredentials": {
      "Type": "Parallel",
      "Branches": [
        {
          "StartAt": "RevokeAPIKeys",
          "States": {
            "RevokeAPIKeys": {
              "Type": "Task",
              "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:RevokeAPIKeys",
              "End": true
            }
          }
        },
        {
          "StartAt": "RevokeIAMAccess",
          "States": {
            "RevokeIAMAccess": {
              "Type": "Task",
              "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:RevokeIAMAccess",
              "End": true
            }
          }
        },
        {
          "StartAt": "RevokeVPNAccess",
          "States": {
            "RevokeVPNAccess": {
              "Type": "Task",
              "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:RevokeVPNAccess",
              "End": true
            }
          }
        }
      ],
      "Next": "RequestDataReturn"
    },
    "RequestDataReturn": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:RequestDataReturn",
      "Next": "WaitForDataReturn"
    },
    "WaitForDataReturn": {
      "Type": "Wait",
      "Seconds": 604800,
      "Next": "VerifyDataReturn"
    },
    "VerifyDataReturn": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:VerifyDataReturn",
      "Next": "DataReturnComplete"
    },
    "DataReturnComplete": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.data_return.status",
          "StringEquals": "complete",
          "Next": "RequestDataDeletion"
        }
      ],
      "Default": "EscalateDataReturn"
    },
    "EscalateDataReturn": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:EscalateDataReturnIssue",
      "End": true
    },
    "RequestDataDeletion": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:RequestSupplierDataDeletion",
      "Next": "WaitForDeletionCertificate"
    },
    "WaitForDeletionCertificate": {
      "Type": "Wait",
      "Seconds": 2592000,
      "Next": "VerifyDeletionCertificate"
    },
    "VerifyDeletionCertificate": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:VerifyDeletionCertificate",
      "Next": "UpdateSupplierRegister"
    },
    "UpdateSupplierRegister": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:UpdateSupplierRegister",
      "Next": "GenerateOffboardingReport"
    },
    "GenerateOffboardingReport": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:GenerateOffboardingReport",
      "End": true
    }
  }
}
```

**Lambda Function for Data Deletion Verification**:
```python
# lambda_verify_data_deletion.py
import boto3
import json
from datetime import datetime

def lambda_handler(event, context):
    """
    Verify supplier data deletion certificate
    Ensure GDPR Article 17 compliance
    """
    
    supplier_id = event['supplier_id']
    certificate_s3_key = event.get('certificate_s3_key')
    
    s3 = boto3.client('s3')
    dynamodb = boto3.resource('dynamodb')
    supplier_table = dynamodb.Table('SupplierRegister')
    
    if not certificate_s3_key:
        return {
            'statusCode': 400,
            'error': 'No deletion certificate provided',
            'action': 'Request certificate from supplier'
        }
    
    # Download certificate from S3
    try:
        certificate_obj = s3.get_object(
            Bucket='hack23-supplier-documents',
            Key=certificate_s3_key
        )
        certificate_content = certificate_obj['Body'].read().decode('utf-8')
    except Exception as e:
        return {
            'statusCode': 500,
            'error': f'Failed to retrieve certificate: {str(e)}'
        }
    
    # Validate certificate contents
    validation_result = validate_deletion_certificate(
        certificate_content,
        supplier_id
    )
    
    if validation_result['valid']:
        # Update supplier register
        supplier_table.update_item(
            Key={'supplier_id': supplier_id},
            UpdateExpression='SET contract_status = :status, data_deletion_certified = :cert, offboarding_date = :date',
            ExpressionAttributeValues={
                ':status': 'offboarded',
                ':cert': True,
                ':date': datetime.utcnow().isoformat()
            }
        )
        
        # Notify compliance team
        sns = boto3.client('sns')
        sns.publish(
            TopicArn='arn:aws:sns:eu-west-1:123456789012:ComplianceTeam',
            Subject=f'✅ Supplier Offboarding Complete: {supplier_id}',
            Message=json.dumps({
                'supplier_id': supplier_id,
                'offboarding_date': datetime.utcnow().isoformat(),
                'data_deletion_certified': True,
                'certificate_location': certificate_s3_key,
                'validation_method': 'NIST SP 800-88 Rev. 1'
            }, indent=2)
        )
        
        return {
            'statusCode': 200,
            'data_deletion_certified': True,
            'offboarding_complete': True
        }
    else:
        # Escalate invalid certificate
        return {
            'statusCode': 400,
            'data_deletion_certified': False,
            'validation_errors': validation_result['errors'],
            'action': 'Request corrected certificate'
        }

def validate_deletion_certificate(certificate: str, supplier_id: str) -> dict:
    """Validate data deletion certificate contents"""
    
    required_elements = [
        'NIST SP 800-88',  # Deletion standard
        supplier_id,  # Supplier identification
        'certify',  # Certification statement
        'deleted',  # Deletion confirmation
        datetime.utcnow().strftime('%Y')  # Current year
    ]
    
    errors = []
    
    for element in required_elements:
        if element not in certificate:
            errors.append(f"Missing required element: {element}")
    
    # Check for authorized signatory
    if not any(title in certificate for title in ['CEO', 'CTO', 'DPO', 'CISO']):
        errors.append("Certificate not signed by authorized executive")
    
    return {
        'valid': len(errors) == 0,
        'errors': errors
    }
```

### Example 4: Supplier Risk Dashboard (Grafana)

**Scenario**: Executive visibility into supplier risk posture

**Grafana Dashboard JSON** (supplier-risk-dashboard.json):
```json
{
  "dashboard": {
    "title": "Supplier Risk Management Dashboard",
    "panels": [
      {
        "title": "Supplier Risk Distribution",
        "type": "piechart",
        "targets": [
          {
            "expr": "count by (risk_tier) (supplier_register)",
            "legendFormat": "{{risk_tier}}"
          }
        ]
      },
      {
        "title": "SLA Compliance Rate (%)",
        "type": "graph",
        "targets": [
          {
            "expr": "100 * (1 - rate(supplier_sla_violations_total[30d]) / rate(supplier_sla_checks_total[30d]))",
            "legendFormat": "{{supplier_name}}"
          }
        ],
        "alert": {
          "name": "SLA Compliance Below 95%",
          "conditions": [
            {
              "evaluator": {
                "type": "lt",
                "params": [95]
              }
            }
          ]
        }
      },
      {
        "title": "Critical Suppliers Pending Review",
        "type": "stat",
        "targets": [
          {
            "expr": "count(supplier_register{risk_tier=\"critical\", next_review_date < time()})"
          }
        ]
      },
      {
        "title": "Supplier Spend by Risk Tier",
        "type": "bargauge",
        "targets": [
          {
            "expr": "sum by (risk_tier) (supplier_contract_value_annual)",
            "legendFormat": "{{risk_tier}}"
          }
        ]
      },
      {
        "title": "Overdue Security Assessments",
        "type": "table",
        "targets": [
          {
            "expr": "supplier_register{next_assessment_date < time()}",
            "format": "table"
          }
        ],
        "transformations": [
          {
            "id": "organize",
            "options": {
              "excludeByName": {},
              "indexByName": {},
              "renameByName": {
                "supplier_name": "Supplier",
                "risk_tier": "Risk",
                "next_assessment_date": "Due Date",
                "contract_manager": "Owner"
              }
            }
          }
        ]
      }
    ]
  }
}
```

## Related ISMS Policies

### Core Supplier Management Framework
- [🤝 Supplier Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/SUPPLIER.md) — Complete supplier lifecycle and risk management
- [📋 Third-Party Management Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Third_Party_Management_Policy.md) — Vendor selection and oversight procedures
- [🔐 Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md) — Security governance framework

### Risk and Compliance
- [📊 Risk Assessment Methodology](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Risk_Assessment_Methodology.md) — Supplier risk evaluation framework
- [🛡️ Data Protection Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Data_Protection_Policy.md) — GDPR Article 28 processor requirements
- [📝 Data Processing Agreement Template](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Data_Processing_Agreement_Template.md) — Standard DPA clauses

### Operational Integration
- [🔄 Change Management](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Change_Management.md) — Supplier-initiated changes
- [🚨 Incident Response Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Incident_Response_Plan.md) — Supplier breach notification
- [🆘 Business Continuity Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Business_Continuity_Plan.md) — Supplier dependency management

## Compliance Mapping

### ISO 27001:2022
- **A.5.19 Information Security in Supplier Relationships** - Systematic supplier management
- **A.5.20 Addressing Information Security in Supplier Agreements** - Contractual security requirements
- **A.5.21 Managing Information Security in ICT Supply Chain** - Supply chain risk management
- **A.5.22 Monitoring, Review and Change Management of Supplier Services** - Ongoing oversight

### NIST Cybersecurity Framework 2.0
- **ID.SC-1** - Cyber supply chain risk management processes identified
- **ID.SC-2** - Suppliers and third-party partners identified and prioritized
- **ID.SC-3** - Contracts with suppliers include cybersecurity requirements
- **ID.SC-4** - Suppliers assessed using cybersecurity requirements
- **ID.SC-5** - Response and recovery planning includes suppliers
- **GV.SC-1** through **GV.SC-10** - Supply chain governance requirements

### CIS Controls v8.1
- **Control 15.1** - Establish and maintain third-party service provider inventory
- **Control 15.2** - Establish and maintain service provider management policy
- **Control 15.3** - Classify service providers
- **Control 15.4** - Ensure service provider contracts include security requirements
- **Control 15.5** - Assess service providers
- **Control 15.6** - Monitor service providers
- **Control 15.7** - Securely decommission service providers

## Key Takeaways

✅ **Risk-Based Classification**: Four-tier system (Critical/High/Medium/Low) drives assessment depth  
✅ **Comprehensive Due Diligence**: Security questionnaires, certifications, financials, references  
✅ **Strong Contracts**: Audit rights, breach notification, data protection, SLAs with penalties  
✅ **Continuous Monitoring**: Quarterly reviews for critical, annual for others, real-time SLA tracking  
✅ **Secure Offboarding**: Access revocation, data return, certified deletion (NIST SP 800-88)  
✅ **Executive Visibility**: Grafana dashboards, automated alerting, compliance reporting

**Remember**: Supplier management is **not a procurement formality** but an **extension of security perimeter governance**—enabling risk-based oversight of third parties who access data, operate critical systems, or process information on the organization's behalf through systematic assessment, monitoring, and contractual enforcement.

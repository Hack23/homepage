---
license: Apache-2.0
skill_category: governance
skill_name: stakeholder-registry
difficulty: intermediate
tags: [stakeholder-registry, regulatory-relationships, stakeholder-engagement, external-stakeholders, compliance-reporting]
related_policies:
  - External_Stakeholder_Registry.md
  - Information_Security_Policy.md
  - Privacy_Policy.md
  - Incident_Response_Plan.md
compliance_frameworks:
  - ISO 27001:2022 (A.5.1 Policies, A.5.2 Information Security Roles, Clause 4.2 Stakeholder Needs)
  - NIST CSF 2.0 (GV.OC-1, GV.PO-1 through GV.PO-2)
  - CIS Controls v8.1 (1.1 Asset Management extended to stakeholders)
---

# 👥 External Stakeholder Registry Management

**Comprehensive Regulatory Relationship Tracking and Stakeholder Engagement**

## Purpose

This skill defines **systematic external stakeholder management** for identifying, classifying, and maintaining relationships with regulatory bodies, customers, partners, and other external parties who have interest or influence in information security practices. Stakeholder management ensures transparent communication, regulatory compliance, and coordinated incident response with external entities.

Based on the [External Stakeholder Registry](https://github.com/Hack23/ISMS-PUBLIC/blob/main/External_Stakeholder_Registry.md) from Hack23 AB's ISMS framework, this skill demonstrates how **structured stakeholder engagement directly enables regulatory compliance and transparent security governance**—serving as competitive advantage for cybersecurity consulting methodologies.

## Rules (Stakeholder Registry MUST/MUST NOT)

### 🎯 MUST: Mandatory Stakeholder Registry Requirements

#### Stakeholder Identification
- **MUST maintain comprehensive registry** of:
  - 🏛️ **Regulatory Bodies**: Data protection authorities (DPA), sector regulators, auditors
  - 💼 **Customers**: Enterprise clients, key accounts, contractual security contacts
  - 🤝 **Business Partners**: Technology partners, resellers, joint venture parties
  - 📰 **Media**: Technology journalists, industry analysts, PR contacts
  - 🎓 **Industry Bodies**: Standards organizations (ISO, NIST), certification bodies
  - ⚖️ **Legal**: External legal counsel, compliance advisors
  - 🚨 **Emergency Contacts**: CERT-SE, law enforcement, cyber insurance

#### Stakeholder Classification
- **MUST categorize stakeholders** by:
  - 📊 **Influence Level**: High/Medium/Low impact on security posture
  - 🎯 **Interest Level**: High/Medium/Low interest in security practices
  - 🔴 **Criticality**: Must-notify (regulatory), should-notify (contractual), may-notify (courtesy)
  - 📋 **Engagement Type**: Regular reporting, incident notification, ad-hoc consultation

#### Contact Information Management
- **MUST document for each stakeholder**:
  - 🆔 Organization name and type
  - 👤 Primary contact and role
  - 📞 Phone, email, emergency contact details
  - 🌐 Website and official communication channels
  - 📋 Notification preferences and SLAs
  - 📅 Last engagement date and next scheduled contact
  - 🎯 Engagement requirements and frequency

#### Regulatory Notification Requirements
- **MUST define notification triggers**:
  - 🚨 **Data Breaches**: GDPR 72-hour notification to DPA
  - 🔒 **Security Incidents**: Customer notification per contract
  - 📊 **Audit Findings**: ISO certification body reporting
  - 📋 **Compliance Changes**: Regulatory filing requirements
  - 🔄 **Certification Renewals**: Annual submission to certifying bodies

#### Engagement Tracking
- **MUST log all stakeholder interactions**:
  - 📅 Date and time of engagement
  - 📝 Purpose and topics discussed
  - 👥 Participants from both organizations
  - 📊 Outcomes and action items
  - 📄 Documentation generated (reports, letters, agreements)
  - 🔄 Follow-up actions and deadlines

### ⚠️ MUST NOT: Prohibited Stakeholder Registry Practices

#### Incomplete Stakeholder Records
- **MUST NOT maintain registry without**:
  - ❌ No stakeholders without contact information
  - ❌ No regulatory bodies without notification SLAs
  - ❌ No customers without security contact details
  - ❌ No emergency contacts without 24/7 availability

#### Outdated Contact Information
- **MUST NOT allow**:
  - ❌ No contact details unverified >6 months
  - ❌ No emergency contacts without annual testing
  - ❌ No regulatory contacts without validation
  - ❌ No stakeholders without engagement history

#### Missing Notification Procedures
- **MUST NOT operate without**:
  - ❌ No GDPR breach notification procedures
  - ❌ No customer incident notification templates
  - ❌ No regulatory reporting workflows
  - ❌ No escalation paths for critical stakeholders

## Examples

### Example 1: Comprehensive Stakeholder Registry Entry

**Scenario**: Document Swedish Data Protection Authority (IMY) as regulatory stakeholder

**Stakeholder Registry Entry Template**:
```markdown
## Stakeholder Record: STK-REG-0001

### Basic Information
**Stakeholder ID**: STK-REG-0001
**Organization Name**: Integritetsskyddsmyndigheten (IMY)
**Organization Type**: 🏛️ Regulatory Body - Data Protection Authority
**Country**: Sweden
**Regulatory Scope**: GDPR enforcement, national data protection law

### Classification
**Influence Level**: 🔴 **HIGH** - Legal enforcement authority
**Interest Level**: 🔴 **HIGH** - Data protection compliance oversight
**Criticality**: 🚨 **MUST-NOTIFY** - Regulatory obligation
**Engagement Type**: Incident notification, annual reporting, ad-hoc inquiries

### Contact Information

#### Primary Contact
**Name**: Data Breach Notification Office
**Role**: Breach Investigation Team
**Email**: dataskyddsincident@imy.se
**Phone**: +46 (0)8 657 61 00
**Hours**: Mon-Fri 09:00-16:00 CET
**Emergency**: dataskyddsincident@imy.se (monitored 24/7)
**Website**: https://www.imy.se

#### Alternative Contacts
**General Inquiries**: imy@imy.se
**Postal Address**: 
```
Integritetsskyddsmyndigheten
Box 8114
104 20 Stockholm
Sweden
```

### Notification Requirements

#### GDPR Data Breach (Article 33)
**Notification Deadline**: 72 hours from breach awareness
**Notification Method**: Online portal (https://www.imy.se/anmal-incident)
**Required Information**:
- Nature of breach (categories of data, number of individuals)
- Name and contact details of DPO
- Likely consequences of breach
- Measures taken/proposed to mitigate

**Template**: See `templates/imy-breach-notification-sv.md`

#### Annual Compliance Reporting
**Frequency**: Optional (only if requested)
**Method**: Written correspondence
**Content**: Security measures, DPIAs, processing activities

### Engagement History
| Date | Type | Purpose | Outcome | Documents |
|------|------|---------|---------|-----------|
| 2025-03-15 | Breach Notification | Customer database incident | Investigation closed - adequate response | INC-2025-0034-IMY.pdf |
| 2025-06-20 | Inquiry | GDPR Art. 35 DPIA guidance | Guidance received | IMY-DPIA-Guidance.pdf |
| 2025-12-10 | Courtesy | New DPO appointment | Acknowledgment received | DPO-Change-Notice.pdf |

### Next Scheduled Engagement
**Date**: As required (incident-driven)
**Purpose**: Breach notification or compliance inquiry
**Owner**: Data Protection Officer (DPO)

### Related Documentation
- [GDPR Breach Notification Procedure](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Incident_Response_Plan.md)
- [Privacy Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Privacy_Policy.md)
- [External Stakeholder Registry Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/External_Stakeholder_Registry.md)
- Breach Notification Template: `templates/imy-breach-notification-sv.md`
- DPO Contact: dpo@hack23.com

### Internal Notes
- IMY has 3-month average response time for non-urgent inquiries
- Prefer Swedish language for formal notifications (English acceptable)
- Use online portal for breach notifications (faster than email)
- Keep CEO and DPO in CC for all IMY communications
```

**Stakeholder Registry DynamoDB Schema**:
```python
# stakeholder_registry_schema.py
import boto3
from datetime import datetime
from typing import List, Dict, Optional

def create_stakeholder_registry_table():
    """Create DynamoDB table for external stakeholder registry"""
    dynamodb = boto3.client('dynamodb')
    
    table = dynamodb.create_table(
        TableName='StakeholderRegistry',
        KeySchema=[
            {'AttributeName': 'stakeholder_id', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'stakeholder_id', 'AttributeType': 'S'},
            {'AttributeName': 'stakeholder_type', 'AttributeType': 'S'},
            {'AttributeName': 'criticality', 'AttributeType': 'S'},
            {'AttributeName': 'last_engagement_date', 'AttributeType': 'S'}
        ],
        GlobalSecondaryIndexes=[
            {
                'IndexName': 'TypeIndex',
                'KeySchema': [
                    {'AttributeName': 'stakeholder_type', 'KeyType': 'HASH'}
                ],
                'Projection': {'ProjectionType': 'ALL'},
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            },
            {
                'IndexName': 'CriticalityIndex',
                'KeySchema': [
                    {'AttributeName': 'criticality', 'KeyType': 'HASH'}
                ],
                'Projection': {'ProjectionType': 'ALL'},
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            },
            {
                'IndexName': 'EngagementIndex',
                'KeySchema': [
                    {'AttributeName': 'last_engagement_date', 'KeyType': 'HASH'}
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
            {'Key': 'Purpose', 'Value': 'stakeholder-management'},
            {'Key': 'Compliance', 'Value': 'ISO27001'}
        ]
    )
    
    return table

# Example stakeholder entry
stakeholder_entry_example = {
    'stakeholder_id': 'STK-REG-0001',
    'organization_name': 'Integritetsskyddsmyndigheten (IMY)',
    'organization_type': 'regulatory-body',
    'stakeholder_type': 'data-protection-authority',
    'country': 'Sweden',
    'regulatory_scope': 'GDPR enforcement, national data protection law',
    
    # Classification
    'influence_level': 'high',
    'interest_level': 'high',
    'criticality': 'must-notify',
    'engagement_type': ['incident-notification', 'annual-reporting', 'ad-hoc-inquiry'],
    
    # Contact information
    'primary_contact': {
        'name': 'Data Breach Notification Office',
        'role': 'Breach Investigation Team',
        'email': 'dataskyddsincident@imy.se',
        'phone': '+46 (0)8 657 61 00',
        'hours': 'Mon-Fri 09:00-16:00 CET',
        'emergency': 'dataskyddsincident@imy.se'
    },
    'alternative_contacts': [
        {
            'purpose': 'General Inquiries',
            'email': 'imy@imy.se'
        }
    ],
    'website': 'https://www.imy.se',
    'postal_address': 'Box 8114, 104 20 Stockholm, Sweden',
    
    # Notification requirements
    'notification_requirements': [
        {
            'trigger': 'gdpr-data-breach',
            'deadline_hours': 72,
            'method': 'online-portal',
            'url': 'https://www.imy.se/anmal-incident',
            'template': 'templates/imy-breach-notification-sv.md'
        }
    ],
    
    # Engagement tracking
    'last_engagement_date': '2025-12-10',
    'engagement_history': [
        {
            'date': '2025-03-15',
            'type': 'breach-notification',
            'purpose': 'Customer database incident',
            'outcome': 'Investigation closed',
            'documents': ['INC-2025-0034-IMY.pdf']
        },
        {
            'date': '2025-06-20',
            'type': 'inquiry',
            'purpose': 'GDPR Art. 35 DPIA guidance',
            'outcome': 'Guidance received',
            'documents': ['IMY-DPIA-Guidance.pdf']
        }
    ],
    
    # Metadata
    'created_date': '2024-01-15T10:00:00Z',
    'last_updated': '2025-12-10T14:30:00Z',
    'owner': 'dpo',
    'next_scheduled_engagement': 'as-required',
    'internal_notes': [
        'IMY has 3-month average response time for non-urgent inquiries',
        'Prefer Swedish language for formal notifications',
        'Use online portal for breach notifications'
    ]
}
```

### Example 2: Automated GDPR Breach Notification (Lambda + SNS)

**Scenario**: Automated 72-hour breach notification workflow to IMY

**Lambda Function for Breach Notification**:
```python
# lambda_gdpr_breach_notification.py
import boto3
import json
from datetime import datetime, timedelta
from typing import Dict, List

def lambda_handler(event, context):
    """
    Automated GDPR breach notification workflow
    Triggered when data breach incident is classified as GDPR-reportable
    """
    
    incident_id = event['incident_id']
    breach_details = event['breach_details']
    
    dynamodb = boto3.resource('dynamodb')
    stakeholder_table = dynamodb.Table('StakeholderRegistry')
    incident_table = dynamodb.Table('IncidentRegister')
    
    # Get IMY stakeholder details
    imy = stakeholder_table.get_item(
        Key={'stakeholder_id': 'STK-REG-0001'}
    )['Item']
    
    # Calculate breach timeline
    breach_awareness_time = datetime.fromisoformat(breach_details['awareness_time'])
    notification_deadline = breach_awareness_time + timedelta(hours=72)
    hours_remaining = (notification_deadline - datetime.utcnow()).total_seconds() / 3600
    
    # Generate breach notification
    notification = generate_imy_breach_notification(
        incident_id=incident_id,
        breach_details=breach_details,
        deadline=notification_deadline
    )
    
    # Store notification in S3
    s3 = boto3.client('s3')
    notification_key = f"breach-notifications/{incident_id}/IMY-notification.pdf"
    s3.put_object(
        Bucket='hack23-compliance-documents',
        Key=notification_key,
        Body=notification['pdf_content'],
        ContentType='application/pdf',
        ServerSideEncryption='AES256',
        Metadata={
            'incident_id': incident_id,
            'stakeholder': 'IMY',
            'notification_type': 'gdpr-breach',
            'deadline': notification_deadline.isoformat()
        }
    )
    
    # Send notification to IMY (via online portal automation)
    imy_response = submit_to_imy_portal(
        notification=notification,
        incident_id=incident_id
    )
    
    # Update incident register
    incident_table.update_item(
        Key={'incident_id': incident_id},
        UpdateExpression='SET imy_notification_sent = :sent, imy_notification_time = :time, imy_reference = :ref',
        ExpressionAttributeValues={
            ':sent': True,
            ':time': datetime.utcnow().isoformat(),
            ':ref': imy_response['reference_number']
        }
    )
    
    # Update stakeholder engagement history
    stakeholder_table.update_item(
        Key={'stakeholder_id': 'STK-REG-0001'},
        UpdateExpression='SET last_engagement_date = :date, engagement_history = list_append(engagement_history, :entry)',
        ExpressionAttributeValues={
            ':date': datetime.utcnow().isoformat(),
            ':entry': [{
                'date': datetime.utcnow().isoformat(),
                'type': 'breach-notification',
                'purpose': f'GDPR breach notification (INC-{incident_id})',
                'outcome': f'Submitted (ref: {imy_response["reference_number"]})',
                'documents': [notification_key]
            }]
        }
    )
    
    # Notify internal stakeholders
    notify_internal_stakeholders(
        incident_id=incident_id,
        imy_reference=imy_response['reference_number'],
        hours_until_deadline=hours_remaining
    )
    
    return {
        'statusCode': 200,
        'notification_sent': True,
        'imy_reference': imy_response['reference_number'],
        'deadline': notification_deadline.isoformat(),
        'hours_remaining': round(hours_remaining, 1)
    }

def generate_imy_breach_notification(incident_id: str, breach_details: Dict, 
                                     deadline: datetime) -> Dict:
    """Generate GDPR Article 33 breach notification for IMY"""
    
    # Load Swedish template
    with open('templates/imy-breach-notification-sv.md', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Populate template
    notification_text = template.format(
        incident_id=incident_id,
        breach_date=breach_details['occurrence_time'],
        awareness_date=breach_details['awareness_time'],
        affected_individuals=breach_details['affected_count'],
        data_categories=', '.join(breach_details['data_categories']),
        breach_description=breach_details['description'],
        breach_cause=breach_details['root_cause'],
        consequences=breach_details['impact_assessment'],
        mitigation_actions='\n'.join(f"- {action}" for action in breach_details['actions_taken']),
        dpo_name='James Pether Sörling',
        dpo_email='dpo@hack23.com',
        dpo_phone='+46 70 123 45 67',
        company_name='Hack23 AB',
        org_number='559116-2894'
    )
    
    # Convert to PDF
    pdf_content = convert_markdown_to_pdf(notification_text)
    
    return {
        'text_content': notification_text,
        'pdf_content': pdf_content,
        'language': 'sv',
        'format': 'pdf'
    }

def submit_to_imy_portal(notification: Dict, incident_id: str) -> Dict:
    """
    Submit breach notification to IMY online portal
    (Placeholder - actual implementation would use IMY API/portal automation)
    """
    
    # In production, this would integrate with IMY's online portal
    # For now, simulate successful submission
    
    reference_number = f"IMY-{datetime.utcnow().strftime('%Y%m%d')}-{incident_id[-6:]}"
    
    return {
        'success': True,
        'reference_number': reference_number,
        'submission_time': datetime.utcnow().isoformat(),
        'acknowledgment': f'Breach notification submitted to IMY (ref: {reference_number})'
    }

def notify_internal_stakeholders(incident_id: str, imy_reference: str, 
                                  hours_until_deadline: float):
    """Notify internal stakeholders about IMY notification"""
    
    sns = boto3.client('sns')
    
    sns.publish(
        TopicArn='arn:aws:sns:eu-west-1:123456789012:ExecutiveTeam',
        Subject=f'✅ IMY Breach Notification Sent: {incident_id}',
        Message=f"""
GDPR BREACH NOTIFICATION SUBMITTED TO IMY

Incident: {incident_id}
IMY Reference: {imy_reference}
Submission Time: {datetime.utcnow().isoformat()}
Hours Until Deadline: {hours_until_deadline:.1f}h

Status: ✅ Submitted within 72-hour deadline

Next Steps:
1. Monitor IMY response (expected within 3 months)
2. Prepare for potential follow-up questions
3. Continue internal investigation and remediation
4. Update affected individuals per GDPR Art. 34 if required

Documentation: s3://hack23-compliance-documents/breach-notifications/{incident_id}/

Responsible: Data Protection Officer (DPO)
        """
    )
    
    # Also notify DPO via SMS for critical breach
    sns.publish(
        PhoneNumber='+46701234567',
        Message=f'IMY breach notification submitted for {incident_id}. Ref: {imy_reference}. Check email for details.'
    )

def convert_markdown_to_pdf(markdown_text: str) -> bytes:
    """Convert markdown to PDF (placeholder)"""
    # In production, use library like WeasyPrint or pandoc
    return markdown_text.encode('utf-8')
```

**EventBridge Rule for Automated Triggering**:
```json
{
  "source": ["custom.incident-management"],
  "detail-type": ["Incident Classification Change"],
  "detail": {
    "classification": ["gdpr-breach"],
    "severity": ["high", "critical"],
    "imy_notification_required": [true]
  }
}
```

### Example 3: Customer Stakeholder Engagement Tracking

**Scenario**: Track security communications with enterprise customers

**Customer Engagement Dashboard** (Python):
```python
# customer_engagement_tracker.py
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import boto3

@dataclass
class CustomerStakeholder:
    """Enterprise customer stakeholder record"""
    stakeholder_id: str
    company_name: str
    contract_value_annual: float
    security_contact_name: str
    security_contact_email: str
    security_contact_phone: str
    
    # Engagement requirements (from contract)
    quarterly_security_review: bool
    annual_penetration_test_report: bool
    incident_notification_sla_hours: int
    soc2_report_sharing: bool
    
    # Engagement tracking
    last_security_review_date: Optional[datetime]
    last_pentest_report_date: Optional[datetime]
    last_soc2_report_date: Optional[datetime]
    
    def is_review_overdue(self) -> bool:
        """Check if quarterly security review is overdue"""
        if not self.quarterly_security_review:
            return False
        
        if not self.last_security_review_date:
            return True  # Never conducted
        
        next_due = self.last_security_review_date + timedelta(days=90)
        return datetime.utcnow() > next_due
    
    def days_until_next_review(self) -> int:
        """Calculate days until next quarterly review"""
        if not self.last_security_review_date:
            return -999  # Overdue
        
        next_due = self.last_security_review_date + timedelta(days=90)
        days = (next_due - datetime.utcnow()).days
        return days
    
    def is_pentest_report_overdue(self) -> bool:
        """Check if annual pentest report sharing is overdue"""
        if not self.annual_penetration_test_report:
            return False
        
        if not self.last_pentest_report_date:
            return True
        
        next_due = self.last_pentest_report_date + timedelta(days=365)
        return datetime.utcnow() > next_due
    
    def generate_engagement_reminder(self) -> Dict:
        """Generate engagement reminders for upcoming deadlines"""
        reminders = []
        
        if self.is_review_overdue():
            reminders.append({
                'type': 'quarterly_security_review',
                'status': '🔴 OVERDUE',
                'days_overdue': abs(self.days_until_next_review()),
                'action': 'Schedule review call immediately'
            })
        elif self.days_until_next_review() <= 14:
            reminders.append({
                'type': 'quarterly_security_review',
                'status': '⚠️ DUE SOON',
                'days_remaining': self.days_until_next_review(),
                'action': 'Schedule review call within 2 weeks'
            })
        
        if self.is_pentest_report_overdue():
            reminders.append({
                'type': 'annual_pentest_report',
                'status': '🔴 OVERDUE',
                'action': 'Share latest pentest report'
            })
        
        return {
            'stakeholder_id': self.stakeholder_id,
            'company_name': self.company_name,
            'reminders': reminders,
            'has_overdue_items': any(r['status'] == '🔴 OVERDUE' for r in reminders)
        }

class CustomerEngagementTracker:
    """Track and automate customer stakeholder engagements"""
    
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.stakeholder_table = self.dynamodb.Table('StakeholderRegistry')
        self.sns = boto3.client('sns')
    
    def get_all_customer_stakeholders(self) -> List[CustomerStakeholder]:
        """Retrieve all enterprise customer stakeholders"""
        response = self.stakeholder_table.scan(
            FilterExpression='stakeholder_type = :type',
            ExpressionAttributeValues={':type': 'enterprise-customer'}
        )
        
        customers = []
        for item in response['Items']:
            customer = CustomerStakeholder(
                stakeholder_id=item['stakeholder_id'],
                company_name=item['company_name'],
                contract_value_annual=item['contract_value_annual'],
                security_contact_name=item['security_contact']['name'],
                security_contact_email=item['security_contact']['email'],
                security_contact_phone=item['security_contact']['phone'],
                quarterly_security_review=item.get('quarterly_security_review', False),
                annual_penetration_test_report=item.get('annual_penetration_test_report', False),
                incident_notification_sla_hours=item.get('incident_notification_sla_hours', 24),
                soc2_report_sharing=item.get('soc2_report_sharing', False),
                last_security_review_date=datetime.fromisoformat(item['last_security_review_date']) if item.get('last_security_review_date') else None,
                last_pentest_report_date=datetime.fromisoformat(item['last_pentest_report_date']) if item.get('last_pentest_report_date') else None,
                last_soc2_report_date=datetime.fromisoformat(item['last_soc2_report_date']) if item.get('last_soc2_report_date') else None
            )
            customers.append(customer)
        
        return customers
    
    def generate_weekly_engagement_report(self) -> Dict:
        """Generate weekly customer engagement status report"""
        customers = self.get_all_customer_stakeholders()
        
        overdue_reviews = []
        upcoming_reviews = []
        overdue_pentests = []
        
        for customer in customers:
            reminder = customer.generate_engagement_reminder()
            
            if reminder['reminders']:
                for r in reminder['reminders']:
                    if r['type'] == 'quarterly_security_review':
                        if r['status'] == '🔴 OVERDUE':
                            overdue_reviews.append({
                                'company': customer.company_name,
                                'days_overdue': r['days_overdue'],
                                'contact': customer.security_contact_email
                            })
                        else:
                            upcoming_reviews.append({
                                'company': customer.company_name,
                                'days_remaining': r['days_remaining'],
                                'contact': customer.security_contact_email
                            })
                    
                    elif r['type'] == 'annual_pentest_report':
                        overdue_pentests.append({
                            'company': customer.company_name,
                            'contact': customer.security_contact_email
                        })
        
        report = {
            'report_date': datetime.utcnow().isoformat(),
            'total_customers': len(customers),
            'overdue_reviews': {
                'count': len(overdue_reviews),
                'customers': overdue_reviews
            },
            'upcoming_reviews': {
                'count': len(upcoming_reviews),
                'customers': upcoming_reviews
            },
            'overdue_pentest_reports': {
                'count': len(overdue_pentests),
                'customers': overdue_pentests
            }
        }
        
        # Send to customer success team
        self.send_engagement_report(report)
        
        return report
    
    def send_engagement_report(self, report: Dict):
        """Email weekly engagement report to customer success team"""
        
        message = f"""
WEEKLY CUSTOMER ENGAGEMENT REPORT
{report['report_date']}

OVERVIEW:
- Total Enterprise Customers: {report['total_customers']}
- Overdue Security Reviews: {report['overdue_reviews']['count']} 🔴
- Upcoming Security Reviews (2 weeks): {report['upcoming_reviews']['count']} ⚠️
- Overdue Pentest Reports: {report['overdue_pentest_reports']['count']} 🔴

IMMEDIATE ACTION REQUIRED:
"""
        
        if report['overdue_reviews']['customers']:
            message += "\n🔴 OVERDUE SECURITY REVIEWS:\n"
            for customer in report['overdue_reviews']['customers']:
                message += f"  - {customer['company']}: {customer['days_overdue']} days overdue ({customer['contact']})\n"
        
        if report['overdue_pentest_reports']['customers']:
            message += "\n🔴 OVERDUE PENTEST REPORTS:\n"
            for customer in report['overdue_pentest_reports']['customers']:
                message += f"  - {customer['company']} ({customer['contact']})\n"
        
        if report['upcoming_reviews']['customers']:
            message += "\n⚠️ UPCOMING SECURITY REVIEWS (NEXT 14 DAYS):\n"
            for customer in report['upcoming_reviews']['customers']:
                message += f"  - {customer['company']}: {customer['days_remaining']} days ({customer['contact']})\n"
        
        self.sns.publish(
            TopicArn='arn:aws:sns:eu-west-1:123456789012:CustomerSuccessTeam',
            Subject=f'📊 Weekly Customer Engagement Report - {datetime.utcnow().strftime("%Y-%m-%d")}',
            Message=message
        )

# Run weekly report generation
if __name__ == "__main__":
    tracker = CustomerEngagementTracker()
    report = tracker.generate_weekly_engagement_report()
    print(f"Generated report with {report['overdue_reviews']['count']} overdue reviews")
```

### Example 4: Multi-Stakeholder Incident Notification Workflow

**Scenario**: Coordinate incident notifications to multiple stakeholder groups

**Step Functions State Machine**:
```json
{
  "Comment": "Multi-Stakeholder Incident Notification Workflow",
  "StartAt": "ClassifyIncident",
  "States": {
    "ClassifyIncident": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:ClassifyIncidentSeverity",
      "Next": "DetermineNotificationRecipients"
    },
    "DetermineNotificationRecipients": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:DetermineStakeholders",
      "Next": "ParallelNotifications"
    },
    "ParallelNotifications": {
      "Type": "Parallel",
      "Branches": [
        {
          "StartAt": "NotifyRegulatoryBodies",
          "States": {
            "NotifyRegulatoryBodies": {
              "Type": "Task",
              "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:NotifyRegulatoryBodies",
              "End": true
            }
          }
        },
        {
          "StartAt": "NotifyCustomers",
          "States": {
            "NotifyCustomers": {
              "Type": "Task",
              "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:NotifyAffectedCustomers",
              "End": true
            }
          }
        },
        {
          "StartAt": "NotifyPartners",
          "States": {
            "NotifyPartners": {
              "Type": "Task",
              "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:NotifyBusinessPartners",
              "End": true
            }
          }
        },
        {
          "StartAt": "NotifyInsurance",
          "States": {
            "NotifyInsurance": {
              "Type": "Task",
              "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:NotifyCyberInsurance",
              "End": true
            }
          }
        }
      ],
      "Next": "LogNotificationOutcomes"
    },
    "LogNotificationOutcomes": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:LogStakeholderEngagements",
      "End": true
    }
  }
}
```

**Lambda Function for Stakeholder Determination**:
```python
# lambda_determine_stakeholders.py
import boto3
from typing import Dict, List

def lambda_handler(event, context):
    """
    Determine which stakeholders to notify based on incident classification
    """
    
    incident = event['incident']
    severity = incident['severity']
    classification = incident['classification']
    affected_data_types = incident.get('affected_data_types', [])
    affected_customer_count = incident.get('affected_customer_count', 0)
    
    dynamodb = boto3.resource('dynamodb')
    stakeholder_table = dynamodb.Table('StakeholderRegistry')
    
    stakeholders_to_notify = {
        'regulatory': [],
        'customers': [],
        'partners': [],
        'insurance': [],
        'media': []
    }
    
    # Determine regulatory notifications
    if 'pii' in affected_data_types or 'gdpr-breach' in classification:
        # Notify data protection authority (IMY)
        imy = stakeholder_table.get_item(Key={'stakeholder_id': 'STK-REG-0001'})['Item']
        stakeholders_to_notify['regulatory'].append({
            'stakeholder_id': imy['stakeholder_id'],
            'name': imy['organization_name'],
            'notification_method': 'online-portal',
            'deadline_hours': 72,
            'required': True
        })
    
    # Determine customer notifications
    if affected_customer_count > 0:
        # Query affected customers from stakeholder registry
        customers = stakeholder_table.query(
            IndexName='TypeIndex',
            KeyConditionExpression='stakeholder_type = :type',
            ExpressionAttributeValues={':type': 'enterprise-customer'}
        )['Items']
        
        for customer in customers:
            # Check if customer is affected (match against incident scope)
            if is_customer_affected(customer, incident):
                sla_hours = customer.get('incident_notification_sla_hours', 24)
                stakeholders_to_notify['customers'].append({
                    'stakeholder_id': customer['stakeholder_id'],
                    'name': customer['company_name'],
                    'contact_email': customer['security_contact']['email'],
                    'notification_method': 'email',
                    'deadline_hours': sla_hours,
                    'required': True
                })
    
    # Determine partner notifications
    if severity in ['high', 'critical']:
        partners = stakeholder_table.query(
            IndexName='TypeIndex',
            KeyConditionExpression='stakeholder_type = :type',
            ExpressionAttributeValues={':type': 'business-partner'}
        )['Items']
        
        for partner in partners:
            if 'must-notify' in partner.get('criticality', ''):
                stakeholders_to_notify['partners'].append({
                    'stakeholder_id': partner['stakeholder_id'],
                    'name': partner['organization_name'],
                    'contact_email': partner['primary_contact']['email'],
                    'notification_method': 'email',
                    'required': True
                })
    
    # Determine insurance notification
    if severity == 'critical':
        insurance = stakeholder_table.get_item(Key={'stakeholder_id': 'STK-INS-0001'})
        if insurance.get('Item'):
            stakeholders_to_notify['insurance'].append({
                'stakeholder_id': insurance['Item']['stakeholder_id'],
                'name': insurance['Item']['organization_name'],
                'contact_email': insurance['Item']['primary_contact']['email'],
                'notification_method': 'email-and-phone',
                'deadline_hours': 24,
                'required': True
            })
    
    return {
        'stakeholders_to_notify': stakeholders_to_notify,
        'total_recipients': sum(len(v) for v in stakeholders_to_notify.values())
    }

def is_customer_affected(customer: Dict, incident: Dict) -> bool:
    """Determine if specific customer is affected by incident"""
    
    # Check if customer uses affected service
    affected_services = incident.get('affected_services', [])
    customer_services = customer.get('services_used', [])
    
    return any(service in customer_services for service in affected_services)
```

## Related ISMS Policies

### Core Stakeholder Management Framework
- [👥 External Stakeholder Registry](https://github.com/Hack23/ISMS-PUBLIC/blob/main/External_Stakeholder_Registry.md) — Complete stakeholder identification and engagement procedures
- [🔐 Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md) — Stakeholder communication governance
- [🛡️ Privacy Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Privacy_Policy.md) — Data protection stakeholder transparency

### Incident and Communication
- [🚨 Incident Response Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Incident_Response_Plan.md) — Stakeholder notification procedures
- [📋 Business Continuity Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Business_Continuity_Plan.md) — Stakeholder communication during crisis
- [📝 Communication Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Communication_Policy.md) — External communication protocols

### Regulatory Compliance
- [📊 GDPR Compliance Procedures](https://github.com/Hack23/ISMS-PUBLIC/blob/main/GDPR_Compliance_Procedures.md) — Data protection authority engagement
- [🔍 Data Breach Notification Procedure](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Data_Breach_Notification_Procedure.md) — Regulatory breach notification
- [✅ Compliance Monitoring](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Compliance_Monitoring_Policy.md) — Regulatory reporting schedule

## Compliance Mapping

### ISO 27001:2022
- **A.5.1 Policies for Information Security** - Stakeholder-informed policy development
- **A.5.2 Information Security Roles and Responsibilities** - External stakeholder roles
- **Clause 4.2 Understanding the Needs and Expectations of Interested Parties** - Stakeholder needs identification
- **Clause 5.3 Organizational Roles, Responsibilities and Authorities** - External accountability

### NIST Cybersecurity Framework 2.0
- **GV.OC-1** - Organizational cybersecurity policy established and communicated to stakeholders
- **GV.PO-1** - Organizational mission, objectives, and activities understood by internal and external stakeholders
- **GV.PO-2** - Internal and external stakeholders identified and relationships characterized
- **PR.AT-1** - Users informed about security requirements and organizational policies
- **RS.CO-1** through **RS.CO-5** - Stakeholder communications during incidents

### CIS Controls v8.1
- **Control 1.1** - Asset management extended to stakeholder relationships
- **Control 17.1** - Incident response communications with stakeholders
- **Control 17.9** - Incident information shared with external stakeholders

## Key Takeaways

✅ **Comprehensive Registry**: All regulatory, customer, partner, media, and industry stakeholders documented  
✅ **Risk-Based Classification**: Influence/interest matrix with must-notify/should-notify/may-notify tiers  
✅ **Regulatory Compliance**: GDPR 72-hour notification automation with IMY integration  
✅ **Customer Engagement**: Quarterly reviews, annual pentests, automated reminder system  
✅ **Incident Coordination**: Multi-stakeholder parallel notification workflows  
✅ **Engagement Tracking**: Complete audit trail of all stakeholder communications

**Remember**: Stakeholder registry management is **not administrative overhead** but **strategic relationship governance**—enabling transparent security communication, regulatory compliance, coordinated incident response, and trust-building through systematic engagement with all parties who have interest or influence in information security practices.

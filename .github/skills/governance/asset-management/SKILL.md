---
license: Apache-2.0
skill_category: governance
skill_name: asset-management
difficulty: intermediate
tags: [asset-management, asset-register, asset-lifecycle, classification, inventory, cmdb]
related_policies:
  - Asset_Register.md
  - Information_Security_Policy.md
  - Data_Classification_Policy.md
  - Acceptable_Use_Policy.md
compliance_frameworks:
  - ISO 27001:2022 (A.5.9 Inventory of Assets, A.5.12 Classification of Information)
  - NIST CSF 2.0 (ID.AM-1 through ID.AM-6)
  - CIS Controls v8.1 (1.1 Hardware Asset Inventory, 2.1 Software Asset Inventory)
---

# 💼 IT Asset Management & Lifecycle

**Comprehensive Asset Inventory, Classification, and Lifecycle Management**

## Purpose

This skill defines **systematic IT asset management** for maintaining accurate inventories, classifying assets by criticality, tracking lifecycle stages, and ensuring security controls align with asset value. Asset management provides the foundation for risk assessment, change management, and incident response by establishing a definitive record of all IT resources.

Based on the [Asset Register](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Asset_Register.md) from Hack23 AB's ISMS framework, this skill demonstrates how **automated asset discovery and tracking directly enables security control optimization and compliance reporting**—serving as competitive advantage for cybersecurity consulting methodologies.

## Rules (Asset Management MUST/MUST NOT)

### 🎯 MUST: Mandatory Asset Management Requirements

#### Asset Identification
- **MUST maintain comprehensive asset inventory** including:
  - 💻 **Hardware Assets**: Servers, workstations, network devices, mobile devices
  - 💾 **Software Assets**: Applications, operating systems, databases, SaaS subscriptions
  - ☁️ **Cloud Resources**: IaaS/PaaS instances, storage, network resources
  - 📊 **Data Assets**: Databases, file repositories, backups, data lakes
  - 👥 **Information Assets**: Documents, intellectual property, customer data
  - 🌐 **External Services**: Third-party APIs, managed services, vendors

#### Asset Classification
- **MUST classify all assets** using standardized scheme:
  - 🔴 **Critical**: Business-essential, <15min RTO, regulatory compliance
  - 🟠 **High**: Important operations, <4h RTO, significant business impact
  - 🟡 **Medium**: Standard operations, <24h RTO, moderate impact
  - 🟢 **Low**: Non-essential, >24h RTO, minimal business impact

#### Asset Metadata
- **MUST document for each asset**:
  - 🆔 Unique asset identifier (e.g., `AST-HW-001`)
  - 📝 Asset name and description
  - 🏷️ Classification level and data sensitivity
  - 👥 Asset owner and custodian
  - 📍 Physical/logical location
  - 💰 Financial value and depreciation
  - 📅 Acquisition date and lifecycle stage
  - 🔧 Configuration baseline
  - 🛡️ Applied security controls
  - 📋 Dependencies and relationships

#### Lifecycle Management
- **MUST track assets through lifecycle stages**:
  - 🆕 **Requisition**: Approval and procurement
  - 📦 **Acquisition**: Receipt and initial configuration
  - ⚙️ **Deployment**: Production rollout with security hardening
  - 🔄 **Operations**: Active use with monitoring and maintenance
  - 🔧 **Maintenance**: Updates, patches, and support
  - 📤 **Retirement**: Secure decommissioning and data disposal
  - 🗑️ **Disposal**: Physical destruction or secure transfer

#### Discovery and Updates
- **MUST maintain current inventory** through:
  - 🔍 Automated discovery scanning (daily for cloud, weekly for on-prem)
  - 📊 CMDB integration with configuration management
  - 🔄 Change management process updates
  - 🧾 Procurement system integration
  - 👁️ Quarterly manual verification and reconciliation

### ⚠️ MUST NOT: Prohibited Asset Management Practices

#### Untracked Assets
- **MUST NOT allow assets outside inventory**:
  - ❌ No shadow IT or unapproved systems
  - ❌ No unregistered cloud resources
  - ❌ No personal devices without MDM enrollment
  - ❌ No production data on unclassified assets

#### Missing Classification
- **MUST NOT operate assets without**:
  - ❌ No assets without classification level
  - ❌ No assets without designated owner
  - ❌ No assets without security controls baseline
  - ❌ No production assets without backup/recovery

#### Stale Asset Data
- **MUST NOT maintain outdated inventory**:
  - ❌ No asset records unverified >90 days
  - ❌ No decommissioned assets in "Active" status
  - ❌ No EOL software without upgrade plan
  - ❌ No unpatched critical assets >30 days

## Examples

### Example 1: Comprehensive Asset Register Entry

**Scenario**: Document production database server with full metadata

**Asset Register Entry Template**:
```markdown
## Asset Record: AST-SRV-0042

### Basic Information
**Asset ID**: AST-SRV-0042
**Asset Type**: Hardware - Server
**Asset Name**: Production PostgreSQL Database (Primary)
**Description**: Primary database server for web application backend
**Serial Number**: DELL-SN-7894561234
**Asset Tag**: HACK23-DB-PROD-01

### Classification
**Asset Classification**: 🔴 CRITICAL
- **Business Criticality**: Revenue-generating system, 500K+ customer records
- **Data Sensitivity**: Contains PII, payment data (GDPR/PCI-DSS scope)
- **Availability Requirement**: 99.9% uptime (15min RTO, 15min RPO)
- **Compliance Scope**: ISO 27001, GDPR, PCI-DSS

### Ownership & Accountability
**Asset Owner**: CTO (strategic decisions, budget approval)
**Technical Custodian**: Database Administrator (day-to-day management)
**Business Owner**: VP Engineering (business requirements)
**Information Owner**: Data Protection Officer (data governance)

### Location & Environment
**Physical Location**: AWS eu-west-1a (Stockholm region)
**Logical Location**: Production VPC (172.31.10.0/24)
**Instance Type**: RDS db.r6g.2xlarge (8 vCPU, 64GB RAM)
**Availability Zone**: Multi-AZ deployment (eu-west-1a primary, eu-west-1b standby)

### Financial Information
**Purchase Date**: 2025-06-15
**Purchase Cost**: €48,000/year (reserved instance)
**Current Value**: €48,000 (annual subscription)
**Depreciation**: N/A (OpEx, not CapEx)
**Maintenance Cost**: €12,000/year (AWS support + backup storage)

### Lifecycle Status
**Current Stage**: 🔄 Operations (Active Production)
**Deployment Date**: 2025-07-01
**Last Major Update**: 2026-01-15 (PostgreSQL 15.3 → 15.6)
**Expected Retirement**: 2028-06-30 (3-year lifecycle)
**Next Review Date**: 2026-04-01 (quarterly)

### Technical Configuration
**Operating System**: AWS RDS Managed PostgreSQL 15.6
**Database Engine**: PostgreSQL 15.6
**Storage**: 2TB gp3 SSD (3000 IOPS, 125 MB/s throughput)
**Backup Strategy**: 
- Automated daily snapshots (35-day retention)
- Continuous transaction log backup (PITR to any second)
- Cross-region replication to eu-central-1

**Network Configuration**:
- Security Group: sg-0a1b2c3d4e5f6g7h8
- Subnet: subnet-prod-db-private-1a
- Encryption in transit: TLS 1.3
- Encryption at rest: AES-256 KMS (key ID: alias/rds-encryption)

### Security Controls Applied
**Preventive Controls**:
✅ Network isolation (private subnet, no internet access)
✅ IAM database authentication (no password auth)
✅ Encryption at rest (KMS-managed keys)
✅ Encryption in transit (TLS 1.3 enforced)
✅ Security group restrictions (application tier only)

**Detective Controls**:
✅ AWS CloudTrail logging
✅ Database activity monitoring (GuardDuty)
✅ CloudWatch performance monitoring
✅ Automated backup verification
✅ Quarterly penetration testing

**Corrective Controls**:
✅ Automated failover to standby (Multi-AZ)
✅ Point-in-time recovery capability
✅ Incident response playbook
✅ Disaster recovery procedures

### Dependencies
**Upstream Dependencies** (assets this depends on):
- VPC: vpc-prod-01 (AST-NET-001)
- KMS Key: alias/rds-encryption (AST-KEY-005)
- Security Group: sg-prod-db (AST-SG-010)
- IAM Role: rds-monitoring-role (AST-IAM-025)

**Downstream Dependencies** (assets that depend on this):
- Application Servers: AST-SRV-0050 through AST-SRV-0055
- Backup System: AST-SRV-0100
- Monitoring System: AST-SRV-0200
- Reporting Service: AST-SRV-0300

### Compliance & Audit
**Compliance Frameworks**:
- ISO 27001:2022 (A.5.9 Asset Inventory, A.8.1 Endpoint Security)
- GDPR Article 32 (Security of Processing)
- PCI-DSS v4.0 (Requirement 2: Secure Configurations)

**Last Audit Date**: 2026-01-20
**Audit Findings**: 0 critical, 0 high, 1 medium (automated patching SLA)
**Next Audit Date**: 2026-07-20

### Change History
| Date | Change Type | Description | Change ID | Approver |
|------|-------------|-------------|-----------|----------|
| 2025-07-01 | Deployment | Initial production deployment | CR-2025-0234 | CTO |
| 2025-09-15 | Maintenance | Storage upgrade 1TB → 2TB | CR-2025-0456 | DBA |
| 2026-01-15 | Security | PostgreSQL 15.3 → 15.6 | CR-2026-0012 | DBA |

### Monitoring & Metrics
**Key Performance Indicators**:
- CPU Utilization: Target <70%, Current 45%
- Memory Utilization: Target <80%, Current 62%
- IOPS: Target <2500, Current 1200
- Connection Count: Target <500, Current 280
- Replication Lag: Target <5s, Current 0.8s

**Alerting Thresholds**:
- CPU >80% for 5min → Warning
- CPU >90% for 5min → Critical
- Storage >85% → Warning
- Backup failure → Critical
- Replication lag >30s → Warning

### Related Documentation
- [Asset Register Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Asset_Register.md)
- [Data Classification Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Data_Classification_Policy.md)
- [Backup and Recovery Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Backup_and_Recovery_Policy.md)
- Technical Documentation: docs/infrastructure/database-architecture.md
- Disaster Recovery Plan: docs/disaster-recovery/database-dr.md
```

**Asset Register DynamoDB Schema**:
```python
# asset_register_schema.py
import boto3
from datetime import datetime
from typing import List, Dict

def create_asset_register_table():
    """Create DynamoDB table for asset register"""
    dynamodb = boto3.client('dynamodb')
    
    table = dynamodb.create_table(
        TableName='AssetRegister',
        KeySchema=[
            {'AttributeName': 'asset_id', 'KeyType': 'HASH'},  # Partition key
            {'AttributeName': 'version', 'KeyType': 'RANGE'}  # Sort key for versioning
        ],
        AttributeDefinitions=[
            {'AttributeName': 'asset_id', 'AttributeType': 'S'},
            {'AttributeName': 'version', 'AttributeType': 'N'},
            {'AttributeName': 'asset_owner', 'AttributeType': 'S'},
            {'AttributeName': 'classification', 'AttributeType': 'S'},
            {'AttributeName': 'lifecycle_stage', 'AttributeType': 'S'},
            {'AttributeName': 'asset_type', 'AttributeType': 'S'}
        ],
        GlobalSecondaryIndexes=[
            {
                'IndexName': 'OwnerIndex',
                'KeySchema': [
                    {'AttributeName': 'asset_owner', 'KeyType': 'HASH'}
                ],
                'Projection': {'ProjectionType': 'ALL'},
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            },
            {
                'IndexName': 'ClassificationIndex',
                'KeySchema': [
                    {'AttributeName': 'classification', 'KeyType': 'HASH'}
                ],
                'Projection': {'ProjectionType': 'ALL'},
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            },
            {
                'IndexName': 'LifecycleIndex',
                'KeySchema': [
                    {'AttributeName': 'lifecycle_stage', 'KeyType': 'HASH'}
                ],
                'Projection': {'ProjectionType': 'ALL'},
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            },
            {
                'IndexName': 'TypeIndex',
                'KeySchema': [
                    {'AttributeName': 'asset_type', 'KeyType': 'HASH'}
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
            {'Key': 'Purpose', 'Value': 'asset-management'},
            {'Key': 'Compliance', 'Value': 'ISO27001'}
        ]
    )
    
    return table

# Example asset entry
asset_entry_example = {
    'asset_id': 'AST-SRV-0042',
    'version': 3,  # Incremented on each update
    'asset_type': 'hardware-server',
    'asset_name': 'Production PostgreSQL Database (Primary)',
    'description': 'Primary database server for web application backend',
    
    # Classification
    'classification': 'critical',
    'data_sensitivity': 'pii-payment',
    'availability_requirement': '99.9%',
    'rto_minutes': 15,
    'rpo_minutes': 15,
    
    # Ownership
    'asset_owner': 'CTO',
    'technical_custodian': 'database-admin',
    'business_owner': 'vp-engineering',
    'information_owner': 'dpo',
    
    # Location
    'physical_location': 'aws-eu-west-1a',
    'logical_location': 'prod-vpc-172.31.10.0/24',
    'cloud_resource_id': 'db-ABCDEFGH123456',
    
    # Financial
    'purchase_date': '2025-06-15',
    'purchase_cost': 48000,
    'current_value': 48000,
    'maintenance_cost_annual': 12000,
    
    # Lifecycle
    'lifecycle_stage': 'operations',
    'deployment_date': '2025-07-01',
    'expected_retirement': '2028-06-30',
    'last_major_update': '2026-01-15',
    'next_review_date': '2026-04-01',
    
    # Technical
    'configuration': {
        'os': 'AWS RDS PostgreSQL 15.6',
        'storage_gb': 2048,
        'instance_type': 'db.r6g.2xlarge',
        'multi_az': True
    },
    
    # Security
    'security_controls': [
        'network-isolation',
        'iam-authentication',
        'encryption-at-rest',
        'encryption-in-transit',
        'automated-backups',
        'activity-monitoring'
    ],
    
    # Dependencies
    'upstream_dependencies': [
        'AST-NET-001',  # VPC
        'AST-KEY-005',  # KMS Key
        'AST-SG-010'    # Security Group
    ],
    'downstream_dependencies': [
        'AST-SRV-0050',  # App Server 1
        'AST-SRV-0051',  # App Server 2
        'AST-SRV-0100'   # Backup System
    ],
    
    # Compliance
    'compliance_frameworks': [
        'ISO27001',
        'GDPR',
        'PCI-DSS'
    ],
    'last_audit_date': '2026-01-20',
    'next_audit_date': '2026-07-20',
    
    # Metadata
    'created_date': '2025-07-01T10:00:00Z',
    'last_updated': '2026-01-15T14:30:00Z',
    'updated_by': 'database-admin'
}
```

### Example 2: Automated Asset Discovery (AWS Config + Lambda)

**Scenario**: Continuous asset discovery and inventory synchronization

**Lambda Function for Asset Discovery**:
```python
# lambda_asset_discovery.py - Automated AWS asset discovery
import boto3
import json
from datetime import datetime
from typing import Dict, List

def lambda_handler(event, context):
    """
    Discover AWS resources and sync to asset register
    Triggered by AWS Config rule compliance changes
    """
    
    config_client = boto3.client('config')
    dynamodb = boto3.resource('dynamodb')
    asset_table = dynamodb.Table('AssetRegister')
    
    # Resource types to discover
    resource_types = [
        'AWS::EC2::Instance',
        'AWS::RDS::DBInstance',
        'AWS::Lambda::Function',
        'AWS::S3::Bucket',
        'AWS::DynamoDB::Table',
        'AWS::ECS::Service',
        'AWS::ElasticLoadBalancingV2::LoadBalancer'
    ]
    
    discovered_assets = []
    
    for resource_type in resource_types:
        # Query AWS Config for resources
        resources = config_client.list_discovered_resources(
            resourceType=resource_type
        )
        
        for resource in resources['resourceIdentifiers']:
            resource_id = resource['resourceId']
            
            # Get detailed configuration
            config_item = config_client.get_resource_config_history(
                resourceType=resource_type,
                resourceId=resource_id,
                limit=1
            )
            
            if config_item['configurationItems']:
                asset = transform_config_to_asset(
                    config_item['configurationItems'][0]
                )
                
                # Sync to asset register
                sync_asset_to_register(asset_table, asset)
                discovered_assets.append(asset)
    
    return {
        'statusCode': 200,
        'assets_discovered': len(discovered_assets),
        'assets': discovered_assets
    }

def transform_config_to_asset(config_item: Dict) -> Dict:
    """Transform AWS Config item to asset register format"""
    
    resource_type = config_item['resourceType']
    resource_id = config_item['resourceId']
    configuration = config_item['configuration']
    tags = {t['key']: t['value'] for t in config_item.get('tags', [])}
    
    # Generate asset ID
    asset_id = generate_asset_id(resource_type, resource_id)
    
    # Determine classification from tags
    classification = tags.get('Classification', 'medium').lower()
    
    # Extract common attributes
    asset = {
        'asset_id': asset_id,
        'version': 1,
        'asset_type': map_resource_type_to_asset_type(resource_type),
        'asset_name': tags.get('Name', resource_id),
        'cloud_resource_id': resource_id,
        'cloud_resource_type': resource_type,
        'classification': classification,
        'asset_owner': tags.get('Owner', 'unassigned'),
        'environment': tags.get('Environment', 'unknown'),
        'lifecycle_stage': 'operations',
        'discovery_date': datetime.utcnow().isoformat(),
        'last_updated': datetime.utcnow().isoformat(),
        'configuration': json.dumps(configuration),
        'tags': tags,
        'compliance_frameworks': extract_compliance_from_tags(tags)
    }
    
    # Resource-specific enrichment
    if resource_type == 'AWS::RDS::DBInstance':
        asset.update({
            'rto_minutes': 15 if classification == 'critical' else 240,
            'rpo_minutes': 15 if classification == 'critical' else 240,
            'backup_enabled': configuration.get('BackupRetentionPeriod', 0) > 0,
            'multi_az': configuration.get('MultiAZ', False),
            'encryption_enabled': configuration.get('StorageEncrypted', False)
        })
    
    return asset

def sync_asset_to_register(table, asset: Dict):
    """Upsert asset to register with version control"""
    
    # Check if asset exists
    try:
        response = table.get_item(
            Key={
                'asset_id': asset['asset_id'],
                'version': asset['version']
            }
        )
        
        if 'Item' in response:
            # Asset exists, increment version
            asset['version'] = response['Item']['version'] + 1
    except:
        pass  # Asset doesn't exist, use version 1
    
    # Write to DynamoDB
    table.put_item(Item=asset)
    
    # Check for configuration drift
    check_configuration_drift(table, asset)

def check_configuration_drift(table, asset: Dict):
    """Detect configuration changes requiring approval"""
    
    # Query previous version
    response = table.query(
        KeyConditionExpression='asset_id = :aid',
        ExpressionAttributeValues={':aid': asset['asset_id']},
        ScanIndexForward=False,
        Limit=2
    )
    
    if len(response['Items']) >= 2:
        current = response['Items'][0]
        previous = response['Items'][1]
        
        # Detect critical configuration changes
        critical_changes = []
        
        if current.get('classification') != previous.get('classification'):
            critical_changes.append('classification_change')
        
        if current.get('encryption_enabled') != previous.get('encryption_enabled'):
            critical_changes.append('encryption_change')
        
        if current.get('backup_enabled') != previous.get('backup_enabled'):
            critical_changes.append('backup_change')
        
        if critical_changes:
            alert_configuration_drift(asset, critical_changes)

def alert_configuration_drift(asset: Dict, changes: List[str]):
    """Send SNS alert for unapproved configuration changes"""
    sns = boto3.client('sns')
    
    sns.publish(
        TopicArn='arn:aws:sns:eu-west-1:123456789012:ConfigurationDrift',
        Subject=f'⚠️ Configuration Drift Detected: {asset["asset_id"]}',
        Message=json.dumps({
            'asset_id': asset['asset_id'],
            'asset_name': asset['asset_name'],
            'changes_detected': changes,
            'classification': asset['classification'],
            'owner': asset['asset_owner'],
            'action_required': 'Verify change authorization via Change Management'
        }, indent=2)
    )

def generate_asset_id(resource_type: str, resource_id: str) -> str:
    """Generate standardized asset ID"""
    type_prefix = {
        'AWS::EC2::Instance': 'AST-SRV',
        'AWS::RDS::DBInstance': 'AST-DB',
        'AWS::Lambda::Function': 'AST-FN',
        'AWS::S3::Bucket': 'AST-S3',
        'AWS::DynamoDB::Table': 'AST-DDB'
    }
    
    prefix = type_prefix.get(resource_type, 'AST-UNK')
    # Use hash of resource_id for consistent numbering
    id_hash = hash(resource_id) % 10000
    return f"{prefix}-{id_hash:04d}"

def map_resource_type_to_asset_type(resource_type: str) -> str:
    """Map AWS resource type to asset type"""
    mapping = {
        'AWS::EC2::Instance': 'compute-instance',
        'AWS::RDS::DBInstance': 'database-managed',
        'AWS::Lambda::Function': 'serverless-function',
        'AWS::S3::Bucket': 'object-storage',
        'AWS::DynamoDB::Table': 'database-nosql'
    }
    return mapping.get(resource_type, 'unknown')

def extract_compliance_from_tags(tags: Dict) -> List[str]:
    """Extract compliance frameworks from resource tags"""
    frameworks = []
    
    if 'ISO27001' in tags.get('Compliance', ''):
        frameworks.append('ISO27001')
    if 'GDPR' in tags.get('Compliance', ''):
        frameworks.append('GDPR')
    if 'PCI-DSS' in tags.get('Compliance', ''):
        frameworks.append('PCI-DSS')
    
    return frameworks
```

**EventBridge Rule for Continuous Discovery**:
```json
{
  "source": ["aws.config"],
  "detail-type": ["Config Configuration Item Change"],
  "detail": {
    "messageType": ["ConfigurationItemChangeNotification"],
    "configurationItem": {
      "resourceType": [
        "AWS::EC2::Instance",
        "AWS::RDS::DBInstance",
        "AWS::Lambda::Function",
        "AWS::S3::Bucket",
        "AWS::DynamoDB::Table"
      ]
    }
  }
}
```

### Example 3: Asset Lifecycle Automation (Retirement Workflow)

**Scenario**: Automated asset decommissioning with secure data disposal

**Step Functions State Machine for Asset Retirement**:
```json
{
  "Comment": "Asset Retirement Workflow with Secure Disposal",
  "StartAt": "ValidateRetirementRequest",
  "States": {
    "ValidateRetirementRequest": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:ValidateRetirement",
      "Next": "CheckDependencies"
    },
    "CheckDependencies": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:CheckAssetDependencies",
      "Next": "HasDependencies"
    },
    "HasDependencies": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.dependencies.count",
          "NumericGreaterThan": 0,
          "Next": "RejectRetirement"
        }
      ],
      "Default": "CreateFinalBackup"
    },
    "RejectRetirement": {
      "Type": "Fail",
      "Cause": "Asset has active dependencies",
      "Error": "DependenciesExist"
    },
    "CreateFinalBackup": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:CreateFinalBackup",
      "Next": "WaitForBackupCompletion"
    },
    "WaitForBackupCompletion": {
      "Type": "Wait",
      "Seconds": 300,
      "Next": "VerifyBackup"
    },
    "VerifyBackup": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:VerifyBackup",
      "Next": "BackupSuccessful"
    },
    "BackupSuccessful": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.backup.status",
          "StringEquals": "success",
          "Next": "SecureDataWipe"
        }
      ],
      "Default": "BackupFailed"
    },
    "BackupFailed": {
      "Type": "Fail",
      "Cause": "Final backup verification failed",
      "Error": "BackupFailed"
    },
    "SecureDataWipe": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:SecureDataWipe",
      "Next": "TerminateResource"
    },
    "TerminateResource": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:TerminateResource",
      "Next": "UpdateAssetRegister"
    },
    "UpdateAssetRegister": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:UpdateAssetRegister",
      "Next": "NotifyStakeholders"
    },
    "NotifyStakeholders": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:eu-west-1:123456789012:function:NotifyRetirementComplete",
      "End": true
    }
  }
}
```

**Lambda Function for Secure Data Wipe**:
```python
# lambda_secure_data_wipe.py
import boto3
import json

def lambda_handler(event, context):
    """
    Perform secure data disposal before asset retirement
    NIST SP 800-88 Rev. 1 compliant
    """
    
    asset_id = event['asset_id']
    resource_type = event['resource_type']
    resource_id = event['resource_id']
    
    if resource_type == 'AWS::RDS::DBInstance':
        # RDS database secure disposal
        return secure_wipe_rds(resource_id)
    
    elif resource_type == 'AWS::EC2::Instance':
        # EC2 instance secure disposal
        return secure_wipe_ec2(resource_id)
    
    elif resource_type == 'AWS::S3::Bucket':
        # S3 bucket secure disposal
        return secure_wipe_s3(resource_id)
    
    return {
        'statusCode': 400,
        'error': f'Unsupported resource type: {resource_type}'
    }

def secure_wipe_rds(db_instance_id: str) -> dict:
    """Secure RDS database disposal"""
    rds = boto3.client('rds')
    
    # Create final snapshot (encrypted)
    snapshot_id = f"{db_instance_id}-final-{int(time.time())}"
    rds.create_db_snapshot(
        DBSnapshotIdentifier=snapshot_id,
        DBInstanceIdentifier=db_instance_id,
        Tags=[
            {'Key': 'Purpose', 'Value': 'final-backup'},
            {'Key': 'Retention', 'Value': '7-years'}
        ]
    )
    
    # Delete database (skip final snapshot as we manually created it)
    rds.delete_db_instance(
        DBInstanceIdentifier=db_instance_id,
        SkipFinalSnapshot=True,
        DeleteAutomatedBackups=False  # Retain for compliance period
    )
    
    return {
        'statusCode': 200,
        'method': 'rds-deletion',
        'final_snapshot': snapshot_id,
        'compliance': 'NIST-SP-800-88-Rev1'
    }

def secure_wipe_ec2(instance_id: str) -> dict:
    """Secure EC2 instance disposal"""
    ec2 = boto3.client('ec2')
    
    # Get EBS volumes
    instance = ec2.describe_instances(InstanceIds=[instance_id])
    volumes = []
    for reservation in instance['Reservations']:
        for inst in reservation['Instances']:
            for volume in inst.get('BlockDeviceMappings', []):
                volumes.append(volume['Ebs']['VolumeId'])
    
    # Terminate instance
    ec2.terminate_instances(InstanceIds=[instance_id])
    
    # Wait for termination, then delete volumes
    ec2.get_waiter('instance_terminated').wait(InstanceIds=[instance_id])
    
    for volume_id in volumes:
        # Encrypted EBS volumes are cryptographically erased when deleted
        ec2.delete_volume(VolumeId=volume_id)
    
    return {
        'statusCode': 200,
        'method': 'cryptographic-erasure',
        'volumes_deleted': volumes,
        'compliance': 'NIST-SP-800-88-Rev1'
    }

def secure_wipe_s3(bucket_name: str) -> dict:
    """Secure S3 bucket disposal"""
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    
    # Delete all objects and versions
    bucket.object_versions.delete()
    
    # Delete bucket
    bucket.delete()
    
    return {
        'statusCode': 200,
        'method': 'cryptographic-erasure',
        'bucket_deleted': bucket_name,
        'compliance': 'NIST-SP-800-88-Rev1'
    }
```

### Example 4: Asset Dependency Mapping (Neo4j Graph Database)

**Scenario**: Visualize asset relationships and impact analysis

**Cypher Queries for Dependency Graph**:
```cypher
// Create asset nodes and relationships in Neo4j

// Create database asset node
CREATE (db:Asset {
  asset_id: 'AST-SRV-0042',
  asset_type: 'database',
  asset_name: 'Production PostgreSQL',
  classification: 'critical',
  owner: 'CTO'
})

// Create application server nodes
CREATE (app1:Asset {
  asset_id: 'AST-SRV-0050',
  asset_type: 'application-server',
  asset_name: 'App Server 1',
  classification: 'high'
})

CREATE (app2:Asset {
  asset_id: 'AST-SRV-0051',
  asset_type: 'application-server',
  asset_name: 'App Server 2',
  classification: 'high'
})

// Create infrastructure dependencies
CREATE (vpc:Asset {
  asset_id: 'AST-NET-001',
  asset_type: 'network',
  asset_name: 'Production VPC',
  classification: 'critical'
})

CREATE (kms:Asset {
  asset_id: 'AST-KEY-005',
  asset_type: 'encryption-key',
  asset_name: 'RDS Encryption Key',
  classification: 'critical'
})

// Create relationships
CREATE (db)-[:DEPENDS_ON {dependency_type: 'network'}]->(vpc)
CREATE (db)-[:DEPENDS_ON {dependency_type: 'encryption'}]->(kms)
CREATE (app1)-[:DEPENDS_ON {dependency_type: 'data'}]->(db)
CREATE (app2)-[:DEPENDS_ON {dependency_type: 'data'}]->(db)

// Query: Find all assets dependent on database
MATCH (asset:Asset)-[:DEPENDS_ON*]->(db:Asset {asset_id: 'AST-SRV-0042'})
RETURN asset.asset_id, asset.asset_name, asset.classification

// Query: Calculate blast radius (assets affected if database fails)
MATCH path=(asset:Asset)-[:DEPENDS_ON*]->(db:Asset {asset_id: 'AST-SRV-0042'})
RETURN COUNT(DISTINCT asset) as affected_asset_count,
       COLLECT(DISTINCT asset.asset_id) as affected_assets

// Query: Find circular dependencies (problematic)
MATCH (a:Asset)-[:DEPENDS_ON*]->(b:Asset)
WHERE a = b
RETURN a.asset_id, a.asset_name

// Query: Critical path analysis (longest dependency chain)
MATCH path=(start:Asset)-[:DEPENDS_ON*]->(end:Asset)
WHERE NOT (end)-[:DEPENDS_ON]->()
RETURN path, LENGTH(path) as depth
ORDER BY depth DESC
LIMIT 1
```

**Python Integration with Neo4j**:
```python
# asset_dependency_analyzer.py
from neo4j import GraphDatabase

class AssetDependencyAnalyzer:
    """Analyze asset dependencies using Neo4j graph database"""
    
    def __init__(self, uri: str, user: str, password: str):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        self.driver.close()
    
    def calculate_blast_radius(self, asset_id: str) -> dict:
        """Calculate impact if asset fails"""
        
        with self.driver.session() as session:
            result = session.run("""
                MATCH path=(asset:Asset)-[:DEPENDS_ON*]->(target:Asset {asset_id: $asset_id})
                RETURN COUNT(DISTINCT asset) as affected_count,
                       COLLECT(DISTINCT asset.asset_id) as affected_assets,
                       MAX(LENGTH(path)) as max_depth
            """, asset_id=asset_id)
            
            record = result.single()
            
            return {
                'target_asset': asset_id,
                'affected_asset_count': record['affected_count'],
                'affected_assets': record['affected_assets'],
                'dependency_depth': record['max_depth'],
                'impact_rating': self._calculate_impact_rating(record['affected_count'])
            }
    
    def _calculate_impact_rating(self, affected_count: int) -> str:
        """Rate impact based on affected asset count"""
        if affected_count == 0:
            return '🟢 ISOLATED'
        elif affected_count <= 5:
            return '🟡 MODERATE'
        elif affected_count <= 10:
            return '🟠 SIGNIFICANT'
        else:
            return '🔴 CRITICAL'
    
    def find_circular_dependencies(self) -> list:
        """Identify problematic circular dependencies"""
        
        with self.driver.session() as session:
            result = session.run("""
                MATCH (a:Asset)-[:DEPENDS_ON*]->(b:Asset)
                WHERE a = b
                RETURN a.asset_id as asset_id, a.asset_name as asset_name
            """)
            
            return [dict(record) for record in result]
    
    def validate_retirement_feasibility(self, asset_id: str) -> dict:
        """Check if asset can be safely retired"""
        
        blast_radius = self.calculate_blast_radius(asset_id)
        
        return {
            'asset_id': asset_id,
            'can_retire': blast_radius['affected_asset_count'] == 0,
            'blocking_dependencies': blast_radius['affected_assets'],
            'required_actions': self._generate_retirement_actions(blast_radius)
        }
    
    def _generate_retirement_actions(self, blast_radius: dict) -> list:
        """Generate actions required before retirement"""
        actions = []
        
        if blast_radius['affected_asset_count'] > 0:
            actions.append({
                'action': 'Migrate dependent services',
                'affected_assets': blast_radius['affected_assets'],
                'priority': 'HIGH'
            })
        
        return actions

# Example usage
analyzer = AssetDependencyAnalyzer(
    uri="bolt://localhost:7687",
    user="neo4j",
    password="password"
)

# Calculate blast radius for database
blast_radius = analyzer.calculate_blast_radius('AST-SRV-0042')
print(f"Blast Radius: {blast_radius}")

# Check retirement feasibility
retirement_check = analyzer.validate_retirement_feasibility('AST-SRV-0042')
print(f"Can Retire: {retirement_check['can_retire']}")

analyzer.close()
```

## Related ISMS Policies

### Core Asset Management Framework
- [💼 Asset Register](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Asset_Register.md) — Complete asset inventory and classification procedures
- [🔐 Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md) — Asset governance and accountability
- [📊 Data Classification Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Data_Classification_Policy.md) — Information asset classification scheme

### Operational Integration
- [🔄 Change Management](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Change_Management.md) — Asset configuration control
- [📋 Risk Register](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Risk_Register.md) — Asset-based risk assessment
- [📝 Acceptable Use Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Acceptable_Use_Policy.md) — Asset usage guidelines

### Lifecycle Management
- [🔧 System Development Lifecycle Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/System_Development_Lifecycle_Policy.md) — Asset deployment procedures
- [♻️ Backup and Recovery Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Backup_and_Recovery_Policy.md) — Asset backup requirements
- [🗑️ Data Retention and Disposal Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Data_Retention_and_Disposal_Policy.md) — Asset retirement and disposal

## Compliance Mapping

### ISO 27001:2022
- **A.5.9 Inventory of Assets** - Comprehensive asset identification and ownership
- **A.5.12 Classification of Information** - Systematic asset classification scheme
- **A.8.1 User Endpoint Devices** - Endpoint asset management
- **A.8.19 Installation of Software on Operational Systems** - Software asset control

### NIST Cybersecurity Framework 2.0
- **ID.AM-1** - Physical devices and systems inventoried
- **ID.AM-2** - Software platforms and applications inventoried
- **ID.AM-3** - Organizational communication and data flows mapped
- **ID.AM-4** - External information systems catalogued
- **ID.AM-5** - Resources prioritized based on classification and criticality
- **ID.AM-6** - Cybersecurity roles and responsibilities established

### CIS Controls v8.1
- **Control 1.1** - Establish and maintain detailed enterprise asset inventory
- **Control 2.1** - Establish and maintain software inventory
- **Control 4.1** - Establish and maintain secure configuration process
- **Control 5.1** - Establish and maintain asset management program

## Key Takeaways

✅ **Comprehensive Inventory**: Track all hardware, software, cloud, data, and service assets  
✅ **Systematic Classification**: Four-tier scheme (Critical/High/Medium/Low) with clear criteria  
✅ **Complete Metadata**: Owner, custodian, location, financials, dependencies documented  
✅ **Lifecycle Tracking**: Requisition through retirement with secure disposal  
✅ **Automated Discovery**: AWS Config + Lambda for continuous synchronization  
✅ **Dependency Mapping**: Graph database for impact analysis and blast radius calculation

**Remember**: Asset management is **not just inventory tracking** but the **foundation for security risk management**—enabling accurate risk assessments, effective incident response, and optimized security control implementation through comprehensive asset visibility and lifecycle governance.

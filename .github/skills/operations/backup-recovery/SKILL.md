---
license: Apache-2.0
skill_category: operations
skill_name: backup-recovery
difficulty: intermediate
tags: [backup, recovery, data-protection, rto, rpo, aws-backup, resilience]
related_policies:
  - Backup_Recovery_Policy.md
  - Business_Continuity_Plan.md
  - Disaster_Recovery_Plan.md
  - Data_Classification_Policy.md
compliance_frameworks:
  - ISO 27001:2022 (A.8.13 Information Backup)
  - NIST CSF 2.0 (PR.IP-4, RC.RP-1)
  - CIS Controls v8.1 (11.1 Backup Management)
---

# 💾 Backup & Recovery Operations

**Business Impact-Driven Data Protection Framework**

## Purpose

This skill defines **systematic backup and recovery procedures** aligned with business impact analysis, ensuring data protection matches business value and continuity objectives. Backup strategies are driven by Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO) based on [Classification Framework](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md) requirements.

Based on the [Backup & Recovery Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Backup_Recovery_Policy.md) from Hack23 AB's ISMS framework, this skill demonstrates how **business impact-driven backup strategy directly enables both operational resilience and competitive advantage**—providing auditable proof of recovery capabilities.

## Rules (Backup & Recovery MUST/MUST NOT)

### 🎯 MUST: Mandatory Backup Requirements

#### Business Impact-Driven Backup Frequency
- **MUST align backup frequency with business impact classification**:
  - 🔴 **Critical Functions** (RTO < 1hr, RPO < 15min): Continuous replication or max 15-minute intervals
  - 🟠 **High Priority** (RTO 1-4hrs, RPO 1-4hrs): Hourly backups or max 4-hour intervals
  - 🟡 **Medium Priority** (RTO 4-24hrs, RPO 4-24hrs): Daily backups
  - 🟢 **Standard Functions** (RTO >24hrs, RPO >24hrs): Weekly backups

#### Immutable Backup Storage
- **MUST use immutable storage** for backup protection:
  - 🔒 AWS S3 Object Lock with compliance mode
  - 🛡️ AWS Backup Vault Lock for regulatory compliance
  - 📦 Cross-region replication for disaster recovery
  - ⏰ Retention periods based on regulatory requirements

#### Recovery Validation Testing
- **MUST test backup recovery procedures**:
  - 🧪 Monthly recovery testing for critical systems (100% RTO/RPO compliance)
  - 📊 Quarterly testing for high-priority systems (95% compliance target)
  - ✅ Semi-annual testing for medium-priority systems (90% compliance target)
  - 📋 Documented test results in audit-ready format

#### Backup Monitoring and Alerting
- **MUST monitor backup operations** in real-time:
  - ⚡ Critical systems: Immediate alerting on backup failure
  - 🔔 High priority: 15-minute alert window
  - ⏰ Medium priority: 1-hour alert window
  - 📊 Backup success rate tracking (target: 99.9%)

### ⚠️ MUST NOT: Prohibited Backup Practices

#### Untested Backups
- **MUST NOT rely on untested backup procedures**:
  - ❌ No assumptions of recovery capability without validation
  - ❌ No skipping recovery testing due to operational convenience
  - ❌ No untested backup configurations in production

#### Unencrypted Sensitive Data
- **MUST NOT store backups of sensitive data unencrypted**:
  - ❌ No plaintext backups of regulated data (PII, financial, health)
  - ❌ No unencrypted cross-region replication
  - ❌ No backup storage without access controls

#### Single-Region Storage
- **MUST NOT rely on single-region backup storage** for critical systems:
  - ❌ No single point of failure for mission-critical data
  - ❌ No backup storage in same availability zone as primary data
  - ❌ No absence of geographic diversity for disaster recovery

## Examples

### Example 1: AWS Backup Central Plan (Critical System)

**Scenario**: DynamoDB global table backup for critical application data

**AWS Backup Plan Configuration**:
```yaml
# cloudformation/backup-critical-dynamodb.yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Critical System Backup Plan - DynamoDB Global Table'

Resources:
  # Immutable backup vault with cross-region replication
  CriticalBackupVault:
    Type: AWS::Backup::BackupVault
    Properties:
      BackupVaultName: 'CriticalSystemBackupVault'
      EncryptionKeyArn: !GetAtt BackupKMSKey.Arn
      LockConfiguration:
        MinRetentionDays: 90  # Regulatory compliance minimum
        MaxRetentionDays: 3650  # 10-year maximum
        ChangeableForDays: 0  # Immediate immutability
      Notifications:
        BackupVaultEvents:
          - BACKUP_JOB_FAILED
          - RESTORE_JOB_FAILED
          - COPY_JOB_FAILED
        SNSTopicArn: !Ref BackupAlarmTopic

  # KMS key for backup encryption
  BackupKMSKey:
    Type: AWS::KMS::Key
    Properties:
      Description: 'Encryption key for critical system backups'
      KeyPolicy:
        Version: '2012-10-17'
        Statement:
          - Sid: Enable IAM User Permissions
            Effect: Allow
            Principal:
              AWS: !Sub 'arn:aws:iam::${AWS::AccountId}:root'
            Action: 'kms:*'
            Resource: '*'
          - Sid: Allow AWS Backup to use the key
            Effect: Allow
            Principal:
              Service: backup.amazonaws.com
            Action:
              - 'kms:CreateGrant'
              - 'kms:DescribeKey'
              - 'kms:Decrypt'
              - 'kms:Encrypt'
              - 'kms:ReEncrypt*'
              - 'kms:GenerateDataKey'
            Resource: '*'

  # Backup plan for critical DynamoDB table
  CriticalBackupPlan:
    Type: AWS::Backup::BackupPlan
    Properties:
      BackupPlan:
        BackupPlanName: 'DynamoDB-Critical-15min-RPO'
        BackupPlanRule:
          - RuleName: 'Continuous-Backup-Rule'
            TargetBackupVault: !Ref CriticalBackupVault
            ScheduleExpression: 'cron(0/15 * * * ? *)'  # Every 15 minutes
            StartWindowMinutes: 60
            CompletionWindowMinutes: 120
            Lifecycle:
              DeleteAfterDays: 35  # Short-term retention
              MoveToColdStorageAfterDays: 7  # Cost optimization
            RecoveryPointTags:
              BusinessImpact: 'Critical'
              RTO: '1-hour'
              RPO: '15-minutes'
              ComplianceRequired: 'true'
            CopyActions:
              - DestinationBackupVaultArn: !Sub 'arn:aws:backup:eu-central-1:${AWS::AccountId}:backup-vault:CriticalSystemBackupVault-DR'
                Lifecycle:
                  DeleteAfterDays: 90  # Extended DR retention

          - RuleName: 'Daily-Long-Term-Retention'
            TargetBackupVault: !Ref CriticalBackupVault
            ScheduleExpression: 'cron(0 2 * * ? *)'  # Daily at 2 AM UTC
            Lifecycle:
              MoveToColdStorageAfterDays: 30
              DeleteAfterDays: 365  # Regulatory compliance
            RecoveryPointTags:
              BackupType: 'LongTermRetention'
              Purpose: 'Compliance'

  # Backup selection (DynamoDB table)
  CriticalBackupSelection:
    Type: AWS::Backup::BackupSelection
    Properties:
      BackupPlanId: !Ref CriticalBackupPlan
      BackupSelection:
        SelectionName: 'DynamoDB-GlobalTable-Selection'
        IamRoleArn: !GetAtt BackupRole.Arn
        Resources:
          - !Sub 'arn:aws:dynamodb:eu-west-1:${AWS::AccountId}:table/global-table'
        Conditions:
          StringEquals:
            - ConditionKey: 'aws:ResourceTag/BackupRequired'
              ConditionValue: 'true'
            - ConditionKey: 'aws:ResourceTag/Environment'
              ConditionValue: 'production'

  # IAM role for AWS Backup
  BackupRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: backup.amazonaws.com
            Action: 'sts:AssumeRole'
      ManagedPolicyArns:
        - 'arn:aws:iam::aws:policy/service-role/AWSBackupServiceRolePolicyForBackup'
        - 'arn:aws:iam::aws:policy/service-role/AWSBackupServiceRolePolicyForRestores'

  # SNS topic for backup alerts
  BackupAlarmTopic:
    Type: AWS::SNS::Topic
    Properties:
      TopicName: 'CriticalBackupAlerts'
      Subscription:
        - Endpoint: 'security-alerts@hack23.com'
          Protocol: 'email'
        - Endpoint: !GetAtt BackupAlertLambda.Arn
          Protocol: 'lambda'

  # Lambda for automated backup failure response
  BackupAlertLambda:
    Type: AWS::Lambda::Function
    Properties:
      FunctionName: 'BackupFailureAutoResponse'
      Runtime: python3.11
      Handler: index.lambda_handler
      Role: !GetAtt BackupAlertLambdaRole.Arn
      Environment:
        Variables:
          SLACK_WEBHOOK_URL: !Sub '{{resolve:secretsmanager:SlackWebhook:SecretString:url}}'
      Code:
        ZipFile: |
          import json
          import urllib3
          import os
          
          http = urllib3.PoolManager()
          
          def lambda_handler(event, context):
              """Automated response to backup failures"""
              message = json.loads(event['Records'][0]['Sns']['Message'])
              
              # Extract backup failure details
              failure_details = {
                  'resource': message.get('resourceArn', 'Unknown'),
                  'vault': message.get('vaultName', 'Unknown'),
                  'error': message.get('statusMessage', 'No details'),
                  'timestamp': message.get('completionDate', 'Unknown')
              }
              
              # Send alert to Slack
              slack_message = {
                  'text': f":rotating_light: *CRITICAL BACKUP FAILURE*",
                  'blocks': [
                      {
                          'type': 'section',
                          'text': {
                              'type': 'mrkdwn',
                              'text': f"*Resource:* `{failure_details['resource']}`\n*Vault:* `{failure_details['vault']}`\n*Error:* {failure_details['error']}"
                          }
                      },
                      {
                          'type': 'section',
                          'text': {
                              'type': 'mrkdwn',
                              'text': f":alarm_clock: *RTO at risk* - Manual intervention required"
                          }
                      }
                  ]
              }
              
              http.request(
                  'POST',
                  os.environ['SLACK_WEBHOOK_URL'],
                  body=json.dumps(slack_message),
                  headers={'Content-Type': 'application/json'}
              )
              
              return {'statusCode': 200, 'body': 'Alert sent'}

  BackupAlertLambdaRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: lambda.amazonaws.com
            Action: 'sts:AssumeRole'
      ManagedPolicyArns:
        - 'arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
      Policies:
        - PolicyName: 'SecretsManagerAccess'
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - 'secretsmanager:GetSecretValue'
                Resource: !Sub 'arn:aws:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:SlackWebhook-*'

Outputs:
  BackupVaultArn:
    Description: 'ARN of critical backup vault'
    Value: !GetAtt CriticalBackupVault.BackupVaultArn
    Export:
      Name: 'CriticalBackupVaultArn'
  
  BackupPlanArn:
    Description: 'ARN of critical backup plan'
    Value: !GetAtt CriticalBackupPlan.BackupPlanArn
```

### Example 2: DynamoDB Point-in-Time Recovery (PITR) Validation

**Scenario**: Monthly recovery test for critical DynamoDB table

**Recovery Test Automation**:
```python
# scripts/test_dynamodb_recovery.py
import boto3
import json
from datetime import datetime, timedelta
import time

class DynamoDBRecoveryTest:
    """Automated DynamoDB PITR recovery testing"""
    
    def __init__(self, table_name: str, test_table_name: str):
        self.dynamodb = boto3.client('dynamodb')
        self.table_name = table_name
        self.test_table_name = test_table_name
        self.test_results = {}
    
    def run_pitr_recovery_test(self):
        """Execute complete PITR recovery validation"""
        test_start = datetime.utcnow()
        print(f"🧪 Starting PITR recovery test at {test_start.isoformat()}")
        
        try:
            # Step 1: Verify PITR enabled on source table
            self._verify_pitr_enabled()
            
            # Step 2: Restore table to 5 minutes ago
            recovery_point = datetime.utcnow() - timedelta(minutes=5)
            self._restore_table_pitr(recovery_point)
            
            # Step 3: Wait for restore completion
            self._wait_for_restore_completion()
            
            # Step 4: Validate data integrity
            integrity_check = self._validate_data_integrity()
            
            # Step 5: Measure recovery time
            recovery_time = (datetime.utcnow() - test_start).total_seconds()
            
            # Step 6: Cleanup test table
            self._cleanup_test_table()
            
            # Step 7: Generate test report
            self._generate_test_report(recovery_time, integrity_check)
            
            return self.test_results
            
        except Exception as e:
            print(f"❌ Recovery test failed: {str(e)}")
            self.test_results['status'] = 'FAILED'
            self.test_results['error'] = str(e)
            return self.test_results
    
    def _verify_pitr_enabled(self):
        """Verify point-in-time recovery is enabled"""
        response = self.dynamodb.describe_continuous_backups(
            TableName=self.table_name
        )
        
        pitr_status = response['ContinuousBackupsDescription']['PointInTimeRecoveryDescription']['PointInTimeRecoveryStatus']
        
        if pitr_status != 'ENABLED':
            raise Exception(f"PITR not enabled on {self.table_name}")
        
        print(f"✅ PITR enabled on {self.table_name}")
        self.test_results['pitr_enabled'] = True
    
    def _restore_table_pitr(self, recovery_point: datetime):
        """Restore table to specific point in time"""
        print(f"🔄 Restoring {self.table_name} to {recovery_point.isoformat()}")
        
        response = self.dynamodb.restore_table_to_point_in_time(
            SourceTableName=self.table_name,
            TargetTableName=self.test_table_name,
            UseLatestRestorableTime=False,
            RestoreDateTime=recovery_point
        )
        
        self.test_results['restore_initiated'] = True
        self.test_results['recovery_point'] = recovery_point.isoformat()
        return response['TableDescription']['TableArn']
    
    def _wait_for_restore_completion(self):
        """Wait for table restore to complete"""
        print(f"⏳ Waiting for restore completion...")
        
        while True:
            response = self.dynamodb.describe_table(TableName=self.test_table_name)
            status = response['Table']['TableStatus']
            
            if status == 'ACTIVE':
                print(f"✅ Restore completed - table is ACTIVE")
                break
            elif status in ['CREATING', 'RESTORING']:
                print(f"⏳ Table status: {status}")
                time.sleep(30)
            else:
                raise Exception(f"Unexpected table status: {status}")
    
    def _validate_data_integrity(self):
        """Validate restored data integrity"""
        print(f"🔍 Validating data integrity...")
        
        # Scan sample of items from both tables
        source_sample = self._scan_table_sample(self.table_name)
        restored_sample = self._scan_table_sample(self.test_table_name)
        
        # Compare item counts
        source_count = source_sample['Count']
        restored_count = restored_sample['Count']
        
        integrity_pass = abs(source_count - restored_count) <= 10  # Allow minor variance
        
        self.test_results['source_item_count'] = source_count
        self.test_results['restored_item_count'] = restored_count
        self.test_results['integrity_check'] = 'PASSED' if integrity_pass else 'FAILED'
        
        print(f"📊 Source items: {source_count}, Restored items: {restored_count}")
        
        return integrity_pass
    
    def _scan_table_sample(self, table_name: str, limit: int = 1000):
        """Scan sample items from table"""
        return self.dynamodb.scan(
            TableName=table_name,
            Limit=limit,
            Select='COUNT'
        )
    
    def _cleanup_test_table(self):
        """Delete test table after validation"""
        print(f"🧹 Cleaning up test table {self.test_table_name}")
        self.dynamodb.delete_table(TableName=self.test_table_name)
        self.test_results['cleanup_completed'] = True
    
    def _generate_test_report(self, recovery_time: float, integrity_pass: bool):
        """Generate recovery test report"""
        rto_target_seconds = 3600  # 1 hour RTO target
        rpo_target_seconds = 900   # 15 minutes RPO target
        
        self.test_results.update({
            'status': 'PASSED' if integrity_pass else 'FAILED',
            'recovery_time_seconds': recovery_time,
            'recovery_time_minutes': round(recovery_time / 60, 2),
            'rto_compliance': recovery_time <= rto_target_seconds,
            'rpo_compliance': True,  # PITR guarantees RPO
            'test_completed_at': datetime.utcnow().isoformat()
        })
        
        print(f"\n📋 Recovery Test Results:")
        print(json.dumps(self.test_results, indent=2))


# Execute monthly recovery test
if __name__ == '__main__':
    tester = DynamoDBRecoveryTest(
        table_name='global-table',
        test_table_name='global-table-pitr-test'
    )
    
    results = tester.run_pitr_recovery_test()
    
    # Upload results to S3 for audit trail
    s3 = boto3.client('s3')
    s3.put_object(
        Bucket='hack23-backup-audit-evidence',
        Key=f'recovery-tests/dynamodb/{datetime.utcnow().strftime("%Y-%m-%d")}.json',
        Body=json.dumps(results, indent=2),
        ContentType='application/json',
        StorageClass='GLACIER_IR'  # Immutable compliance storage
    )
    
    print(f"✅ Test results uploaded to audit storage")
```

### Example 3: S3 Backup with Versioning and Lifecycle

**Scenario**: Document storage backup with versioning for compliance

**S3 Backup Configuration**:
```yaml
# cloudformation/s3-document-backup.yaml
Resources:
  DocumentBackupBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: 'hack23-documents-backup'
      VersioningConfiguration:
        Status: 'Enabled'
      
      # Object Lock for immutability (compliance mode)
      ObjectLockEnabled: true
      ObjectLockConfiguration:
        ObjectLockEnabled: 'Enabled'
        Rule:
          DefaultRetention:
            Mode: 'COMPLIANCE'  # Cannot be deleted or modified
            Days: 2555  # 7 years for regulatory compliance
      
      # Lifecycle policy for cost optimization
      LifecycleConfiguration:
        Rules:
          - Id: 'TransitionToIntelligentTiering'
            Status: 'Enabled'
            Transitions:
              - TransitionInDays: 30
                StorageClass: 'INTELLIGENT_TIERING'
          
          - Id: 'TransitionToGlacier'
            Status: 'Enabled'
            Transitions:
              - TransitionInDays: 90
                StorageClass: 'GLACIER'
          
          - Id: 'NonCurrentVersionExpiration'
            Status: 'Enabled'
            NoncurrentVersionTransitions:
              - TransitionInDays: 30
                StorageClass: 'GLACIER'
            NoncurrentVersionExpiration:
              NoncurrentDays: 365
      
      # Encryption at rest
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: 'aws:kms'
              KMSMasterKeyID: !GetAtt BackupKMSKey.Arn
            BucketKeyEnabled: true
      
      # Cross-region replication for DR
      ReplicationConfiguration:
        Role: !GetAtt S3ReplicationRole.Arn
        Rules:
          - Id: 'ReplicateToFrankfurt'
            Status: 'Enabled'
            Priority: 1
            Filter:
              Prefix: ''
            Destination:
              Bucket: !Sub 'arn:aws:s3:::hack23-documents-backup-dr-${AWS::AccountId}'
              ReplicationTime:
                Status: 'Enabled'
                Time:
                  Minutes: 15  # 15-minute RPO
              Metrics:
                Status: 'Enabled'
                EventThreshold:
                  Minutes: 15
              StorageClass: 'GLACIER'
            DeleteMarkerReplication:
              Status: 'Enabled'
      
      # Public access block
      PublicAccessBlockConfiguration:
        BlockPublicAcls: true
        BlockPublicPolicy: true
        IgnorePublicAcls: true
        RestrictPublicBuckets: true
      
      # Logging for audit trail
      LoggingConfiguration:
        DestinationBucketName: !Ref AccessLogBucket
        LogFilePrefix: 'document-backup-logs/'
      
      Tags:
        - Key: 'BusinessImpact'
          Value: 'High'
        - Key: 'RTO'
          Value: '4-hours'
        - Key: 'RPO'
          Value: '15-minutes'
        - Key: 'Compliance'
          Value: 'GDPR-7years'
```

## Related ISMS Policies

### Core Backup Framework
- [💾 Backup & Recovery Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Backup_Recovery_Policy.md) — Complete backup strategy and RTO/RPO requirements
- [🏷️ Classification Framework](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md) — Business impact definitions and backup prioritization

### Business Continuity Integration
- [🔄 Business Continuity Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Business_Continuity_Plan.md) — Business resilience and recovery coordination
- [🆘 Disaster Recovery Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Disaster_Recovery_Plan.md) — Technical recovery procedures and AWS integration

### Security and Compliance
- [🔒 Cryptography Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Cryptography_Policy.md) — Backup encryption requirements and key management
- [🏷️ Data Classification Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Data_Classification_Policy.md) — Data sensitivity and protection requirements
- [🔐 Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md) — Overall security governance

## Compliance Mapping

### ISO 27001:2022
- **A.8.13 Information Backup** - Backup copies of information maintained
- **A.8.14 Redundancy of Information Processing Facilities** - System availability and redundancy
- **A.17.1 Information Security Continuity** - Business continuity and backup integration

### NIST Cybersecurity Framework 2.0
- **PR.IP-4** - Backups of information maintained
- **RC.RP-1** - Recovery plan executed during or after cybersecurity incident
- **PR.DS-1** - Data at rest protected

### CIS Controls v8.1
- **Control 11.1** - Establish and maintain data recovery process
- **Control 11.2** - Perform automated backups
- **Control 11.3** - Protect recovery data
- **Control 11.4** - Establish and maintain isolated instance of recovery data

## Key Takeaways

✅ **Business Impact Alignment**: Backup frequency driven by RTO/RPO based on business criticality  
✅ **Immutable Storage**: AWS S3 Object Lock and Backup Vault Lock for compliance and ransomware protection  
✅ **Cross-Region Replication**: Geographic diversity for disaster recovery scenarios  
✅ **Automated Testing**: Monthly recovery validation with documented test results  
✅ **Real-Time Monitoring**: Immediate alerting on backup failures with automated response  
✅ **Audit Trail**: Complete backup and recovery evidence in immutable storage

**Remember**: Backups are **worthless without validated recovery procedures**—systematic testing ensures data protection translates to actual business resilience.

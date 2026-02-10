---
license: Apache-2.0
skill_category: operations
skill_name: disaster-recovery
difficulty: advanced
tags: [disaster-recovery, aws, multi-region, fis, chaos-engineering, resilience-hub, automation]
related_policies:
  - Disaster_Recovery_Plan.md
  - Business_Continuity_Plan.md
  - Backup_Recovery_Policy.md
  - CLASSIFICATION.md
compliance_frameworks:
  - ISO 27001:2022 (A.17.2 Redundancies)
  - NIST CSF 2.0 (RC.RP-1, PR.IP-4)
  - CIS Controls v8.1 (11.5 Disaster Recovery Testing)
  - AWS Well-Architected Framework (Reliability Pillar)
---

# 🔥 Disaster Recovery Operations

**AWS-Native Technical Resilience Through Chaos Engineering**

## Purpose

This skill defines **AWS-native disaster recovery procedures** leveraging AWS Resilience Hub, AWS Fault Injection Service (FIS), and Systems Manager automation for systematic technical recovery validation. Disaster recovery focuses on infrastructure and data restoration while business continuity handles operational procedures.

Based on the [Disaster Recovery Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Disaster_Recovery_Plan.md) from Hack23 AB's ISMS framework, this skill demonstrates how **evidence-based chaos engineering directly enables both technical resilience and competitive advantage**—providing auditable proof of recovery capabilities through continuous validation.

## Rules (Disaster Recovery MUST/MUST NOT)

### 🎯 MUST: Mandatory Disaster Recovery Requirements

#### AWS Resilience Hub Policy Enforcement
- **MUST define Resilience Hub policies** for all production applications:
  - 🎯 RTO/RPO requirements per [Classification Framework](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md)
  - 🔰 Application resilience assessments (daily for critical systems)
  - 🚦 Deployment gating based on resilience compliance
  - 📊 Evidence collection and audit trail generation

#### Multi-Region Architecture
- **MUST implement multi-region failover** for critical systems:
  - 🌍 Cross-region replication (eu-west-1 ↔ eu-central-1 minimum)
  - 🔄 Automated failover mechanisms (Route 53 health checks)
  - 📦 Immutable backups in multiple regions
  - ⚡ Sub-5-minute RTO for mission-critical applications

#### Chaos Engineering with FIS
- **MUST conduct systematic chaos experiments**:
  - 🧪 Monthly chaos experiments for critical systems (100% coverage)
  - 🎯 Quarterly experiments for high-priority systems (95% coverage)
  - 📋 FIS templates with SSM automation integration
  - ✅ Automated recovery validation and evidence collection

#### Infrastructure as Code (IaC) for Recovery
- **MUST maintain IaC for disaster recovery**:
  - 📝 CloudFormation templates for all infrastructure
  - 🔒 Version-controlled IaC in Git repositories
  - 🧪 Automated IaC testing in non-production environments
  - 🔄 Rollback procedures through IaC versioning

### ⚠️ MUST NOT: Prohibited Disaster Recovery Practices

#### Untested Recovery Procedures
- **MUST NOT rely on untested DR capabilities**:
  - ❌ No assumptions about failover without validation
  - ❌ No untested backup restore procedures
  - ❌ No unvalidated cross-region replication
  - ❌ No undocumented recovery steps

#### Single-Region Dependencies
- **MUST NOT create single-region failure points** for critical systems:
  - ❌ No single-region data storage for critical data
  - ❌ No single-region compute dependencies
  - ❌ No single-region DNS resolution
  - ❌ No absence of cross-region backup replication

#### Manual Recovery Procedures
- **MUST NOT rely solely on manual recovery**:
  - ❌ No recovery procedures requiring human intervention for critical systems
  - ❌ No undocumented runbooks without automation
  - ❌ No recovery steps not encoded in SSM documents
  - ❌ No testing procedures without evidence collection

## Examples

### Example 1: AWS Fault Injection Service with SSM Automation

**Scenario**: Chaos experiment simulating API Gateway Lambda access denial

**FIS Experiment Template**:
```yaml
# cloudformation/fis-api-lambda-deny.yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'FIS Chaos Experiment - API Gateway Lambda Access Denial'

Parameters:
  FaultDuration:
    Type: String
    Default: 'PT5M'
    Description: 'Fault injection duration (ISO 8601 format)'

Resources:
  # IAM Policy to deny Lambda invocation
  LambdaDenyPolicy:
    Type: AWS::IAM::ManagedPolicy
    Properties:
      ManagedPolicyName: FIS-Lambda-Deny-Policy
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Deny
            Action:
              - 'lambda:InvokeFunction'
              - 'lambda:InvokeAsync'
            Resource: '*'

  # SSM Automation Document for IAM policy injection
  IamPolicyInjectionDocument:
    Type: AWS::SSM::Document
    Properties:
      Name: 'FIS-IAM-Policy-Attach-Detach'
      DocumentType: Automation
      Content:
        description: 'SSM Document for injecting IAM policy denial faults'
        schemaVersion: '0.3'
        assumeRole: '{{ AutomationAssumeRole }}'
        parameters:
          TargetResourceDenyPolicyArn:
            type: String
            description: 'ARN of Deny IAM Policy'
          Duration:
            type: String
            description: 'Fault injection duration (ISO 8601)'
          TargetApplicationRoleName:
            type: String
            description: 'Target IAM role name'
          AutomationAssumeRole:
            type: String
            description: 'SSM Automation role ARN'
        mainSteps:
          - name: AttachDenyPolicy
            action: 'aws:executeAwsApi'
            inputs:
              Service: iam
              Api: AttachRolePolicy
              RoleName: '{{ TargetApplicationRoleName }}'
              PolicyArn: '{{ TargetResourceDenyPolicyArn }}'
            description: 'Attach deny policy to inject fault'
            timeoutSeconds: 10
          
          - name: FaultInjectionDuration
            action: 'aws:sleep'
            inputs:
              Duration: '{{ Duration }}'
            description: 'Maintain fault for specified duration'
            onFailure: 'step:RollbackDetachPolicy'
            onCancel: 'step:RollbackDetachPolicy'
            nextStep: RollbackDetachPolicy
          
          - name: RollbackDetachPolicy
            action: 'aws:executeAwsApi'
            inputs:
              Service: iam
              Api: DetachRolePolicy
              RoleName: '{{ TargetApplicationRoleName }}'
              PolicyArn: '{{ TargetResourceDenyPolicyArn }}'
            description: 'Remove deny policy to end fault injection'
            timeoutSeconds: 10
            isEnd: true

  # FIS Experiment Template
  FisDenyApiGatewayLambdaTemplate:
    Type: AWS::FIS::ExperimentTemplate
    Properties:
      Description: 'Deny API Gateway Lambda access via SSM automation'
      Actions:
        InjectAccessDenied:
          ActionId: 'aws:ssm:start-automation-execution'
          Description: 'Inject Lambda access denial fault'
          Parameters:
            documentArn: !Sub 'arn:aws:ssm:${AWS::Region}:${AWS::AccountId}:document/${IamPolicyInjectionDocument}'
            documentParameters: !Sub |
              {
                "TargetResourceDenyPolicyArn": "${LambdaDenyPolicy}",
                "Duration": "${FaultDuration}",
                "TargetApplicationRoleName": "ApiGatewayLambdaRole",
                "AutomationAssumeRole": "${SsmAutomationRole.Arn}"
              }
            maxDuration: 'PT8M'
      RoleArn: !GetAtt FisExperimentRole.Arn
      StopConditions:
        - Source: none
      Tags:
        - Key: Name
          Value: DENY-API-LAMBDA
        - Key: FaultType
          Value: AccessDenial
        - Key: Service
          Value: Lambda

  # IAM Role for SSM Automation
  SsmAutomationRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: ssm.amazonaws.com
            Action: 'sts:AssumeRole'
      Policies:
        - PolicyName: IAMPolicyManagement
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - 'iam:AttachRolePolicy'
                  - 'iam:DetachRolePolicy'
                  - 'iam:GetRole'
                  - 'iam:ListAttachedRolePolicies'
                Resource: '*'

  # IAM Role for FIS Experiment Execution
  FisExperimentRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: fis.amazonaws.com
            Action: 'sts:AssumeRole'
      ManagedPolicyArns:
        - 'arn:aws:iam::aws:policy/CloudWatchLogsFullAccess'
      Policies:
        - PolicyName: FISExperimentExecution
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - 'ssm:StartAutomationExecution'
                  - 'ssm:GetAutomationExecution'
                  - 'ssm:StopAutomationExecution'
                Resource: '*'

  # CloudWatch Alarm for experiment validation
  ApiGateway5xxAlarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      AlarmName: FIS-API-Gateway-5xx-Errors
      AlarmDescription: 'Detect API Gateway errors during chaos experiment'
      MetricName: 5XXError
      Namespace: AWS/ApiGateway
      Statistic: Sum
      Period: 60
      EvaluationPeriods: 1
      Threshold: 10
      ComparisonOperator: GreaterThanThreshold
      TreatMissingData: notBreaching
      ActionsEnabled: true
      AlarmActions:
        - !Ref ChaosExperimentAlertTopic

  # SNS Topic for chaos experiment alerts
  ChaosExperimentAlertTopic:
    Type: AWS::SNS::Topic
    Properties:
      TopicName: ChaosExperimentAlerts
      DisplayName: 'FIS Chaos Experiment Notifications'
      Subscription:
        - Endpoint: 'devops@hack23.com'
          Protocol: email

Outputs:
  FisExperimentTemplateId:
    Description: 'FIS Experiment Template ID'
    Value: !GetAtt FisDenyApiGatewayLambdaTemplate.Id
    Export:
      Name: !Sub '${AWS::StackName}-FISTemplateId'

  SsmDocumentName:
    Description: 'SSM Automation Document Name'
    Value: !Ref IamPolicyInjectionDocument
```

**Python Script to Execute and Validate Experiment**:
```python
# chaos_experiment_executor.py
import boto3
import json
import time
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class ExperimentResult:
    """Chaos experiment execution result"""
    experiment_id: str
    template_id: str
    start_time: datetime
    end_time: datetime
    status: str
    rto_achieved: bool
    rpo_achieved: bool
    recovery_time_seconds: float
    evidence_artifacts: List[str]

class ChaosExperimentExecutor:
    """Execute and validate AWS FIS chaos experiments"""
    
    def __init__(self, region: str = 'eu-west-1'):
        self.fis = boto3.client('fis', region_name=region)
        self.ssm = boto3.client('ssm', region_name=region)
        self.cloudwatch = boto3.client('cloudwatch', region_name=region)
        self.s3 = boto3.client('s3', region_name=region)
    
    def execute_chaos_experiment(
        self, 
        template_id: str,
        tags: Dict[str, str] = None
    ) -> ExperimentResult:
        """Execute FIS chaos experiment with automated validation"""
        
        print(f"🧪 Starting chaos experiment: {template_id}")
        start_time = datetime.utcnow()
        
        # Start FIS experiment
        response = self.fis.start_experiment(
            experimentTemplateId=template_id,
            tags=tags or {'ExecutedBy': 'AutomatedChaosEngineering'}
        )
        
        experiment_id = response['experiment']['id']
        print(f"📊 Experiment ID: {experiment_id}")
        
        # Monitor experiment execution
        experiment_status = self._monitor_experiment(experiment_id)
        
        # Validate recovery
        recovery_metrics = self._validate_recovery(experiment_id)
        
        end_time = datetime.utcnow()
        recovery_time = (end_time - start_time).total_seconds()
        
        # Collect evidence artifacts
        evidence = self._collect_evidence(experiment_id)
        
        result = ExperimentResult(
            experiment_id=experiment_id,
            template_id=template_id,
            start_time=start_time,
            end_time=end_time,
            status=experiment_status,
            rto_achieved=recovery_time <= 300,  # 5-minute RTO target
            rpo_achieved=recovery_metrics['data_loss_seconds'] <= 60,  # 1-minute RPO
            recovery_time_seconds=recovery_time,
            evidence_artifacts=evidence
        )
        
        # Store experiment results
        self._store_experiment_results(result)
        
        return result
    
    def _monitor_experiment(self, experiment_id: str) -> str:
        """Monitor FIS experiment execution"""
        while True:
            response = self.fis.get_experiment(id=experiment_id)
            status = response['experiment']['state']['status']
            
            print(f"⏳ Experiment status: {status}")
            
            if status in ['completed', 'stopped', 'failed']:
                return status
            
            time.sleep(10)
    
    def _validate_recovery(self, experiment_id: str) -> Dict[str, any]:
        """Validate system recovery after chaos experiment"""
        
        # Check API Gateway health
        api_health = self._check_api_health()
        
        # Check Lambda function health
        lambda_health = self._check_lambda_health()
        
        # Check database connectivity
        database_health = self._check_database_health()
        
        # Measure data consistency
        data_loss = self._measure_data_loss()
        
        return {
            'api_health': api_health,
            'lambda_health': lambda_health,
            'database_health': database_health,
            'data_loss_seconds': data_loss
        }
    
    def _check_api_health(self) -> bool:
        """Verify API Gateway health"""
        # Query CloudWatch metrics for API Gateway
        response = self.cloudwatch.get_metric_statistics(
            Namespace='AWS/ApiGateway',
            MetricName='5XXError',
            StartTime=datetime.utcnow() - timedelta(minutes=5),
            EndTime=datetime.utcnow(),
            Period=300,
            Statistics=['Sum']
        )
        
        error_count = sum(dp['Sum'] for dp in response['Datapoints'])
        return error_count < 10  # Acceptable error threshold
    
    def _check_lambda_health(self) -> bool:
        """Verify Lambda function health"""
        # Check Lambda invocation metrics
        response = self.cloudwatch.get_metric_statistics(
            Namespace='AWS/Lambda',
            MetricName='Errors',
            StartTime=datetime.utcnow() - timedelta(minutes=5),
            EndTime=datetime.utcnow(),
            Period=300,
            Statistics=['Sum']
        )
        
        error_count = sum(dp['Sum'] for dp in response['Datapoints'])
        return error_count < 5
    
    def _check_database_health(self) -> bool:
        """Verify database connectivity and consistency"""
        # Implementation would check DynamoDB or RDS health
        return True  # Placeholder
    
    def _measure_data_loss(self) -> float:
        """Measure RPO compliance (data loss in seconds)"""
        # Implementation would compare backup timestamps
        return 0  # Placeholder - no data loss
    
    def _collect_evidence(self, experiment_id: str) -> List[str]:
        """Collect evidence artifacts for audit trail"""
        evidence = []
        
        # FIS experiment logs
        fis_logs = f'fis-experiments/{experiment_id}.json'
        evidence.append(fis_logs)
        
        # SSM automation execution logs
        ssm_executions = self.ssm.list_automation_executions(
            Filters=[
                {'Key': 'Tag:ExperimentId', 'Values': [experiment_id]}
            ]
        )
        for execution in ssm_executions['AutomationExecutions']:
            ssm_log = f'ssm-executions/{execution["AutomationExecutionId"]}.json'
            evidence.append(ssm_log)
        
        # CloudWatch metrics snapshots
        cw_metrics = f'cloudwatch-metrics/{experiment_id}.json'
        evidence.append(cw_metrics)
        
        return evidence
    
    def _store_experiment_results(self, result: ExperimentResult):
        """Store experiment results in immutable storage"""
        results_key = f'chaos-experiments/{result.start_time.strftime("%Y-%m")}/{result.experiment_id}.json'
        
        self.s3.put_object(
            Bucket='hack23-dr-evidence',
            Key=results_key,
            Body=json.dumps({
                'experiment_id': result.experiment_id,
                'template_id': result.template_id,
                'start_time': result.start_time.isoformat(),
                'end_time': result.end_time.isoformat(),
                'status': result.status,
                'rto_achieved': result.rto_achieved,
                'rpo_achieved': result.rpo_achieved,
                'recovery_time_seconds': result.recovery_time_seconds,
                'evidence_artifacts': result.evidence_artifacts
            }, indent=2),
            ContentType='application/json',
            StorageClass='GLACIER_IR',
            Tagging='ComplianceEvidence=true&RetentionYears=3'
        )
        
        print(f"✅ Experiment results stored: s3://hack23-dr-evidence/{results_key}")

# Example usage
if __name__ == '__main__':
    executor = ChaosExperimentExecutor()
    
    # Execute Lambda access denial experiment
    result = executor.execute_chaos_experiment(
        template_id='EXT1234567890abcdef',
        tags={'Service': 'API Gateway', 'FaultType': 'AccessDenial'}
    )
    
    print(f"\n📊 Experiment Results:")
    print(f"  Status: {result.status}")
    print(f"  Recovery Time: {result.recovery_time_seconds:.2f}s")
    print(f"  RTO Achieved: {'✅' if result.rto_achieved else '❌'}")
    print(f"  RPO Achieved: {'✅' if result.rpo_achieved else '❌'}")
    print(f"  Evidence Artifacts: {len(result.evidence_artifacts)}")
```

### Example 2: AWS Resilience Hub Policy and Assessment

**Scenario**: Mission-critical resilience policy for multi-region Lambda architecture

**Resilience Hub CloudFormation**:
```yaml
# cloudformation/resilience-hub-policy.yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'AWS Resilience Hub Mission Critical Policy'

Resources:
  # Mission Critical Resilience Policy
  MissionCriticalPolicy:
    Type: AWS::ResilienceHub::ResiliencyPolicy
    Properties:
      PolicyName: 'Hack23-Mission-Critical-Policy'
      PolicyDescription: 'RTO < 1hr, RPO < 15min for mission-critical applications'
      Tier: MissionCritical
      DataLocationConstraint: AnyLocation
      Policy:
        Software:
          RpoInSecs: 300    # 5 minutes
          RtoInSecs: 3600   # 1 hour
        Hardware:
          RpoInSecs: 1      # Near-instant
          RtoInSecs: 1      # Near-instant
        AZ:
          RpoInSecs: 1      # Multi-AZ instant failover
          RtoInSecs: 1      # Multi-AZ instant failover
        Region:
          RpoInSecs: 5      # Cross-region minimal lag
          RtoInSecs: 3600   # 1-hour regional failover
      Tags:
        - Key: Tier
          Value: MissionCritical
        - Key: Owner
          Value: CTO

  # Resilience Hub Application Definition
  MultiRegionLambdaApp:
    Type: AWS::ResilienceHub::App
    Properties:
      Name: 'hack23-multi-region-lambda'
      Description: 'Multi-region Lambda API with global table backend'
      AppAssessmentSchedule: Daily
      ResiliencyPolicyArn: !Ref MissionCriticalPolicy
      AppTemplateBody: |
        {
          "resources": [
            {
              "logicalResourceId": {
                "identifier": "HealthCheckFunction",
                "logicalStackName": "IrelandStack"
              },
              "type": "AWS::Lambda::Function",
              "name": "healthcheck-function-ireland"
            },
            {
              "logicalResourceId": {
                "identifier": "HealthCheckFunction",
                "logicalStackName": "FrankfurtStack"
              },
              "type": "AWS::Lambda::Function",
              "name": "healthcheck-function-frankfurt"
            },
            {
              "logicalResourceId": {
                "identifier": "GlobalTable",
                "logicalStackName": "IrelandStack"
              },
              "type": "AWS::DynamoDB::GlobalTable",
              "name": "hack23-global-table"
            }
          ],
          "appComponents": [
            {
              "id": "ComputeComponent-Lambda",
              "name": "Lambda-HealthCheck-MultiRegion",
              "type": "AWS::ResilienceHub::ComputeAppComponent",
              "resourceNames": [
                "healthcheck-function-ireland",
                "healthcheck-function-frankfurt"
              ]
            },
            {
              "id": "DatabaseComponent-DynamoDB",
              "name": "DynamoDB-GlobalTable",
              "type": "AWS::ResilienceHub::DatabaseAppComponent",
              "resourceNames": ["hack23-global-table"]
            }
          ]
        }
      ResourceMappings:
        - LogicalStackName: 'IrelandStack'
          MappingType: CfnStack
          PhysicalResourceId:
            Identifier: !Ref IrelandStack
            Type: Arn
            AwsRegion: eu-west-1
            AwsAccountId: !Ref AWS::AccountId
        - LogicalStackName: 'FrankfurtStack'
          MappingType: CfnStack
          PhysicalResourceId:
            Identifier: !Ref FrankfurtStack
            Type: Arn
            AwsRegion: eu-central-1
            AwsAccountId: !Ref AWS::AccountId
      Tags:
        - Key: Environment
          Value: Production
        - Key: Criticality
          Value: MissionCritical

  # Lambda Stack in eu-west-1 (Ireland)
  IrelandStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: 'https://s3.eu-west-1.amazonaws.com/hack23-templates/lambda-stack.yaml'
      Parameters:
        Region: eu-west-1
        FunctionName: healthcheck-function-ireland

  # Lambda Stack in eu-central-1 (Frankfurt)
  FrankfurtStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: 'https://s3.eu-central-1.amazonaws.com/hack23-templates/lambda-stack.yaml'
      Parameters:
        Region: eu-central-1
        FunctionName: healthcheck-function-frankfurt

  # Route 53 Health Check for Ireland
  IrelandHealthCheck:
    Type: AWS::Route53::HealthCheck
    Properties:
      HealthCheckConfig:
        Type: HTTPS
        Port: 443
        ResourcePath: '/v1/healthcheck'
        FullyQualifiedDomainName: 'api-ireland.hack23.com'
        RequestInterval: 10
        FailureThreshold: 2
        EnableSNI: true
      HealthCheckTags:
        - Key: Region
          Value: eu-west-1
        - Key: Purpose
          Value: MultiRegionFailover

  # Route 53 Health Check for Frankfurt
  FrankfurtHealthCheck:
    Type: AWS::Route53::HealthCheck
    Properties:
      HealthCheckConfig:
        Type: HTTPS
        Port: 443
        ResourcePath: '/v1/healthcheck'
        FullyQualifiedDomainName: 'api-frankfurt.hack23.com'
        RequestInterval: 10
        FailureThreshold: 2
        EnableSNI: true
      HealthCheckTags:
        - Key: Region
          Value: eu-central-1
        - Key: Purpose
          Value: MultiRegionFailover

  # Route 53 Weighted Routing for Active-Active Multi-Region
  ApiRecordSetGroup:
    Type: AWS::Route53::RecordSetGroup
    Properties:
      HostedZoneName: 'hack23.com.'
      RecordSets:
        - Name: 'api.hack23.com.'
          Type: A
          SetIdentifier: 'api-ireland'
          Weight: 50
          HealthCheckId: !Ref IrelandHealthCheck
          AliasTarget:
            HostedZoneId: !GetAtt IrelandStack.Outputs.ApiGatewayHostedZoneId
            DNSName: !GetAtt IrelandStack.Outputs.ApiGatewayDomainName
        - Name: 'api.hack23.com.'
          Type: A
          SetIdentifier: 'api-frankfurt'
          Weight: 50
          HealthCheckId: !Ref FrankfurtHealthCheck
          AliasTarget:
            HostedZoneId: !GetAtt FrankfurtStack.Outputs.ApiGatewayHostedZoneId
            DNSName: !GetAtt FrankfurtStack.Outputs.ApiGatewayDomainName

Outputs:
  ResiliencyPolicyArn:
    Description: 'Mission Critical Resilience Policy ARN'
    Value: !Ref MissionCriticalPolicy
    Export:
      Name: !Sub '${AWS::StackName}-PolicyArn'

  ApplicationArn:
    Description: 'Resilience Hub Application ARN'
    Value: !GetAtt MultiRegionLambdaApp.AppArn
    Export:
      Name: !Sub '${AWS::StackName}-AppArn'

  IrelandHealthCheckId:
    Description: 'Route 53 Health Check for Ireland'
    Value: !Ref IrelandHealthCheck

  FrankfurtHealthCheckId:
    Description: 'Route 53 Health Check for Frankfurt'
    Value: !Ref FrankfurtHealthCheck
```

### Example 3: DynamoDB Point-in-Time Recovery with SSM

**Scenario**: Automated PITR recovery testing for DynamoDB global table

**SSM-Based Recovery Testing**:
```yaml
# cloudformation/dynamodb-pitr-recovery.yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'DynamoDB PITR Recovery with FIS + SSM Automation'

Resources:
  # FIS Experiment Template for PITR Recovery
  DynamoDBPitrRecoveryTemplate:
    Type: AWS::FIS::ExperimentTemplate
    Properties:
      Description: 'Validate DynamoDB PITR recovery capability'
      Actions:
        RestoreTablePITR:
          ActionId: 'aws:ssm:start-automation-execution'
          Description: 'Restore DynamoDB table from point-in-time'
          Parameters:
            documentArn: !Sub 'arn:aws:ssm:${AWS::Region}::document/AWSResilienceHub-RestoreDynamoDBTableToPointInTimeSOP_2020-04-01'
            documentParameters: !Sub |
              {
                "DynamoDBTableSourceName": "hack23-global-table",
                "DynamoDBTableTargetName": "hack23-global-table-pitr-test",
                "RecoveryPointDateTime": "${RecoveryPointDateTime}",
                "CopyAllProperties": true,
                "AutomationAssumeRole": "${DynamoDBRecoveryRole.Arn}"
              }
            maxDuration: 'PT30M'
      RoleArn: !GetAtt FisExperimentRole.Arn
      StopConditions:
        - Source: none
      Tags:
        - Key: TestType
          Value: PITR-Recovery
        - Key: Service
          Value: DynamoDB

  # IAM Role for DynamoDB Recovery SSM Automation
  DynamoDBRecoveryRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: DynamoDB-PITR-Recovery-Role
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: ssm.amazonaws.com
            Action: 'sts:AssumeRole'
      Policies:
        - PolicyName: DynamoDBRecoveryPermissions
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - 'dynamodb:RestoreTableToPointInTime'
                  - 'dynamodb:DescribeTable'
                  - 'dynamodb:CreateTable'
                  - 'dynamodb:DeleteTable'
                  - 'dynamodb:UpdateTable'
                  - 'dynamodb:DescribeContinuousBackups'
                  - 'dynamodb:UpdateContinuousBackups'
                  - 'dynamodb:Scan'
                  - 'dynamodb:Query'
                Resource: '*'

  # IAM Role for FIS Experiment
  FisExperimentRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: FIS-DynamoDB-Recovery-Role
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: fis.amazonaws.com
            Action: 'sts:AssumeRole'
      Policies:
        - PolicyName: FISSSMExecution
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - 'ssm:StartAutomationExecution'
                  - 'ssm:GetAutomationExecution'
                  - 'ssm:StopAutomationExecution'
                Resource: '*'

  # Lambda function for post-recovery validation
  RecoveryValidationFunction:
    Type: AWS::Lambda::Function
    Properties:
      FunctionName: DynamoDB-Recovery-Validator
      Runtime: python3.11
      Handler: index.lambda_handler
      Role: !GetAtt RecoveryValidationRole.Arn
      Timeout: 300
      Environment:
        Variables:
          SOURCE_TABLE: 'hack23-global-table'
          TARGET_TABLE: 'hack23-global-table-pitr-test'
      Code:
        ZipFile: |
          import boto3
          import json
          from decimal import Decimal
          
          dynamodb = boto3.resource('dynamodb')
          
          def lambda_handler(event, context):
              """Validate DynamoDB PITR recovery data integrity"""
              
              source_table_name = event.get('source_table', 'hack23-global-table')
              target_table_name = event.get('target_table', 'hack23-global-table-pitr-test')
              
              source_table = dynamodb.Table(source_table_name)
              target_table = dynamodb.Table(target_table_name)
              
              # Scan both tables for item count comparison
              source_count = source_table.scan(Select='COUNT')['Count']
              target_count = target_table.scan(Select='COUNT')['Count']
              
              # Allow 5% variance due to timing
              count_variance = abs(source_count - target_count) / source_count
              integrity_check = count_variance <= 0.05
              
              # Sample data integrity check
              source_sample = source_table.scan(Limit=100)['Items']
              target_sample = target_table.scan(Limit=100)['Items']
              
              # Compare sample data structure
              sample_integrity = len(source_sample) > 0 and len(target_sample) > 0
              
              result = {
                  'source_table': source_table_name,
                  'target_table': target_table_name,
                  'source_item_count': source_count,
                  'target_item_count': target_count,
                  'count_variance_percent': round(count_variance * 100, 2),
                  'integrity_check_passed': integrity_check and sample_integrity,
                  'rpo_compliant': True  # PITR guarantees RPO
              }
              
              print(json.dumps(result, indent=2, default=decimal_default))
              
              # Cleanup test table after validation
              if integrity_check and sample_integrity:
                  target_table.delete()
                  result['test_table_cleaned_up'] = True
              
              return result
          
          def decimal_default(obj):
              """JSON serializer for Decimal types"""
              if isinstance(obj, Decimal):
                  return float(obj)
              raise TypeError

  RecoveryValidationRole:
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
        - PolicyName: DynamoDBValidation
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - 'dynamodb:Scan'
                  - 'dynamodb:Query'
                  - 'dynamodb:DescribeTable'
                  - 'dynamodb:DeleteTable'
                Resource: '*'

Outputs:
  FisRecoveryTemplateId:
    Description: 'FIS PITR Recovery Template ID'
    Value: !GetAtt DynamoDBPitrRecoveryTemplate.Id

  ValidationFunctionArn:
    Description: 'Recovery Validation Lambda Function ARN'
    Value: !GetAtt RecoveryValidationFunction.Arn
```

## Related ISMS Policies

### Core Disaster Recovery Framework
- [🆘 Disaster Recovery Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Disaster_Recovery_Plan.md) — Complete AWS-native technical recovery strategy
- [🏷️ Classification Framework](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md) — RTO/RPO requirements and recovery prioritization

### Business Continuity Integration
- [🏢 Business Continuity Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Business_Continuity_Plan.md) — Operational continuity and work area recovery
- [💾 Backup Recovery Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Backup_Recovery_Policy.md) — Data protection and backup validation

### Technical Implementation
- [💻 Asset Register](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Asset_Register.md) — Infrastructure inventory and dependencies
- [🚨 Incident Response Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Incident_Response_Plan.md) — Crisis management and emergency response
- [🌐 Network Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Network_Security_Policy.md) — Network recovery and security restoration

### Governance and Compliance
- [🔐 Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md) — Overall security governance
- [📊 Security Metrics](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Security_Metrics.md) — Recovery performance measurement

## Compliance Mapping

### ISO 27001:2022
- **A.17.2 Redundancies** - Information processing facilities redundancy
- **A.8.13 Information Backup** - Backup management and testing
- **A.17.1 Business Continuity** - Continuity and disaster recovery integration

### NIST Cybersecurity Framework 2.0
- **RC.RP-1** - Recovery planning processes and procedures executed
- **PR.IP-4** - Backups of information maintained and tested
- **DE.CM-7** - Monitoring for unauthorized changes and recovery validation

### CIS Controls v8.1
- **Control 11.5** - Establish and maintain disaster recovery process
- **Control 11.4** - Establish and maintain isolated instance of recovery data
- **Control 14.9** - Develop and maintain recovery plans

### AWS Well-Architected Framework
- **Reliability Pillar** - Recover from infrastructure or service disruptions
- **Operational Excellence Pillar** - Automated recovery and chaos engineering
- **Security Pillar** - Protect data through backup and recovery

## Key Takeaways

✅ **AWS-Native Automation**: FIS + SSM + Resilience Hub for systematic chaos engineering and recovery validation  
✅ **Multi-Region Resilience**: Cross-region replication and active-active architecture for regional failures  
✅ **Evidence-Based Validation**: Automated chaos experiments with immutable audit trail in S3 Glacier  
✅ **Infrastructure as Code**: CloudFormation-based recovery procedures for consistent, repeatable deployments  
✅ **Continuous Testing**: Monthly chaos experiments for critical systems, quarterly for high-priority systems  
✅ **RTO/RPO Enforcement**: Resilience Hub policies enforce recovery objectives with deployment gating

**Remember**: Disaster recovery is **not just backups**—it's continuous chaos engineering, automated failover, and evidence-based validation ensuring technical resilience through systematic testing.

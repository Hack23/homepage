---
name: "Network Security"
description: "Cloud-native network protection, zero-trust architecture, and AWS VPC security"
license: "Apache-2.0"
version: "1.0"
author: "Hack23 AB"
tags: ["network-security", "zero-trust", "aws-vpc"]
category: "security"
frameworks: ["ISO 27001:2022", "NIST CSF 2.0", "CIS Controls v8.1"]
related_policies: ["Network_Security_Policy.md"]
---

# 🌐 Network Security Skill

## 🎯 Purpose

Enforce cloud-native network security with zero-trust architecture, based on [Network Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Network_Security_Policy.md).

**Key Principle:** *"The perimeter is dead. Long live zero-trust."*

## 📚 Scope

- ☁️ Cloud-Native Protection (AWS-native services)
- 🔐 Zero-Trust Architecture (never trust, always verify)
- 🛡️ Network Segmentation (VPC isolation, security groups)
- 🔑 VPN Requirements (secure remote access)
- 🔥 Firewall Rules (AWS WAF, security groups, NACLs)

## ⚙️ Security Rules

### MUST Requirements

```yaml
aws_vpc_architecture:
  network_design:
    multi_tier: [public_subnets, private_subnets, isolated_subnets]
    availability_zones: minimum_2_for_ha
    security_groups: default_deny_least_privilege
    nacls: additional_subnet_protection
  
zero_trust_controls:
  identity: iam_roles_with_mfa
  segmentation: micro_segmentation_per_workload
  encryption: tls_1_3_preferred_vpn_for_admin
  monitoring: cloudtrail_guardduty_flowlogs

aws_waf:
  managed_rules: [owasp_top_10, known_bad_inputs, ip_reputation]
  custom_rules: [rate_limiting, geo_blocking]
  logging: s3_with_90_day_retention
```

### MUST NOT Prohibitions

```yaml
prohibited:
  - public_databases: rds_in_public_subnets
  - unrestricted_sg: 0.0.0.0/0_for_admin_ports
  - default_vpc: production_in_default_vpc
  - disabled_monitoring: no_cloudtrail_or_flow_logs
```

## 💡 Example: Three-Tier VPC

```yaml
vpc_deployment:
  public_subnets: [alb, nat_gateway]
  private_subnets: [ec2_app_servers, lambda]
  isolated_subnets: [rds_database]
  
  security_groups:
    alb_sg:
      inbound: [443_from_0.0.0.0/0, 80_redirect]
      outbound: [8080_to_app_sg]
    app_sg:
      inbound: [8080_from_alb_sg, 22_from_bastion]
      outbound: [5432_to_db_sg, 443_external_apis]
    db_sg:
      inbound: [5432_from_app_sg_only]
      outbound: deny_all

  monitoring:
    vpc_flow_logs: enabled
    guardduty: active
    cloudwatch_alarms: configured
```

## 🔗 Integration

**Policies:** [Network Security](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Network_Security_Policy.md), [Information Security](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)

**Frameworks:** ISO 27001 A.8.20-23, NIST CSF PR.AC-05, CIS Control 12

## 📋 Document Control

- **Version:** 1.0 | **Updated:** 2026-02-10
- **License:** Apache-2.0
- **Classification:** [![Public](https://img.shields.io/badge/C-Public-lightgrey)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md)

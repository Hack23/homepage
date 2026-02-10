---
name: "Physical Security"
description: "Home office security controls, equipment protection, and environmental security for remote operations"
license: "Apache-2.0"
version: "1.0"
author: "Hack23 AB"
tags:
  - physical-security
  - home-office
  - equipment-protection
  - environmental-security
  - clean-desk-policy
category: "security"
frameworks:
  - "ISO 27001:2022"
  - "NIST CSF 2.0"
  - "CIS Controls v8.1"
related_policies:
  - "Physical_Security_Policy.md"
  - "Asset_Register.md"
  - "Information_Security_Policy.md"
---

# 🏠 Physical Security Skill

## 🎯 Purpose

This skill enforces physical security controls for home office environments, equipment protection, and environmental security. Based on Hack23 AB's [Physical Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Physical_Security_Policy.md), it demonstrates how enterprise-grade physical security is achievable for remote-first operations.

**Key Principle:** *Physical security isn't just locks and guards—it's layered protection for remote work environments where traditional perimeter security doesn't exist.*

## 📚 Scope

This skill covers:
- **🏠 Home Office Security:** Workspace protection, access control, secure storage
- **💻 Equipment Protection:** Laptops, monitors, mobile devices, storage media
- **👥 Visitor Management:** Guest access controls for home office environment
- **🌡️ Environmental Security:** Fire, water, temperature, humidity protection
- **🧹 Clean Desk/Screen Policy:** Information exposure prevention
- **🔒 Physical Access Controls:** Device locks, secure storage, theft prevention

## ⚙️ Security Rules

### MUST Requirements

Physical security controls you **MUST** implement:

1. **🏠 Workspace Security**
   ```yaml
   home_office_requirements:
     dedicated_workspace: required
     lockable_door: recommended
     window_security: blinds_or_curtains_required
     visitor_visibility: minimize_screen_visibility
     secure_storage: lockable_cabinet_or_drawer
     backup_media: fireproof_safe_or_offsite_storage
   ```

2. **💻 Equipment Protection**
   ```yaml
   device_security:
     laptops:
       - physical_lock_cable: when_in_public_spaces
       - full_disk_encryption: mandatory
       - screen_privacy_filter: recommended_for_sensitive_work
       - automatic_screen_lock: 5_minutes_idle_maximum
       - boot_password: BIOS/UEFI_password_required
     
     mobile_devices:
       - screen_lock: biometric_or_strong_PIN
       - device_encryption: mandatory
       - remote_wipe_capability: enrolled_in_MDM
       - physical_protection: use_protective_case
     
     storage_media:
       - encryption: all_removable_media_encrypted
       - labeling: classification_labels_applied
       - secure_storage: locked_cabinet_when_not_in_use
       - disposal: secure_wipe_or_physical_destruction
   ```

3. **🌡️ Environmental Controls**
   ```yaml
   environmental_protection:
     fire_safety:
       - smoke_detectors: installed_and_tested_monthly
       - fire_extinguisher: accessible_and_inspected
       - evacuation_plan: documented_and_practiced
       - electrical_safety: no_overloaded_circuits
     
     water_damage:
       - equipment_placement: elevated_off_floor
       - leak_detection: water_sensors_near_equipment
       - backup_protection: waterproof_bags_for_critical_items
     
     climate_control:
       - temperature_range: 15-25°C_optimal
       - humidity_control: 30-60%_relative_humidity
       - ventilation: adequate_airflow_for_equipment
   ```

4. **🧹 Clean Desk/Screen Policy**
   ```yaml
   information_protection:
     end_of_day:
       - lock_sensitive_documents: secure_cabinet_or_safe
       - secure_removable_media: encrypted_and_locked_away
       - log_out_of_systems: all_sessions_terminated
       - screen_lock: automatic_lock_enabled
       - shred_confidential_waste: cross_cut_shredder
     
     during_work:
       - minimize_paper: digital_first_approach
       - classify_documents: apply_classification_labels
       - visitor_awareness: hide_sensitive_information
       - screen_positioning: away_from_windows_and_visitors
   ```

5. **👥 Visitor Management**
   ```yaml
   home_office_visitors:
     before_visit:
       - schedule_visitors: avoid_overlap_with_sensitive_work
       - prepare_workspace: secure_all_confidential_materials
       - screen_positioning: ensure_no_visibility_of_work
     
     during_visit:
       - lock_screens: all_devices_locked
       - escort_required: visitor_never_left_alone_in_workspace
       - conversation_awareness: avoid_discussing_confidential_matters
     
     after_visit:
       - verify_security: check_all_devices_and_documents_secure
       - access_review: review_system_access_logs_if_visitor_near_devices
   ```

### MUST NOT Prohibitions

Physical security practices you **MUST NOT** do:

1. **❌ Equipment Exposure**
   ```yaml
   prohibited_practices:
     - leave_devices_unlocked: in_public_or_shared_spaces
     - work_in_public: with_sensitive_data_visible_to_others
     - store_devices_visibly: in_vehicles_or_unsecured_locations
     - share_workspace: with_unauthorized_individuals_during_sensitive_work
     - leave_doors_unlocked: when_workspace_contains_business_equipment
   ```

2. **❌ Information Exposure**
   ```yaml
   prohibited_behaviors:
     - print_unnecessary_documents: use_digital_workflows_instead
     - leave_documents_unattended: always_secure_or_destroy
     - discuss_confidential_matters: in_public_or_with_visitors_present
     - dispose_unsecurely: regular_trash_for_sensitive_documents
     - store_passwords_physically: written_passwords_in_visible_locations
   ```

3. **❌ Unsafe Practices**
   ```yaml
   dangerous_behaviors:
     - overload_circuits: multiple_high_power_devices_on_one_outlet
     - block_exits: equipment_blocking_emergency_egress
     - ignore_alarms: smoke_detector_or_security_system_alerts
     - disable_protection: removing_security_cables_or_locks
     - unsecured_backup_media: leaving_backup_drives_visible_or_unlocked
   ```

## 💡 Examples

### Example 1: Home Office Setup (Compliant)

**Scenario:** Setting up a secure home office workspace for cybersecurity consulting work.

```yaml
# Home Office Security Configuration
workspace_security:
  location:
    room: dedicated_home_office
    door: lockable_from_inside
    windows:
      - privacy_film_applied: true
      - blinds_installed: true
      - desk_positioned: perpendicular_to_window
  
  equipment:
    primary_workstation:
      device: Ubuntu_22.04_LTS_laptop
      security:
        - full_disk_encryption: LUKS_enabled
        - BIOS_password: configured
        - physical_lock_cable: attached_to_desk
        - screen_privacy_filter: installed
    
    monitors:
      count: 2
      positioning: facing_away_from_door_and_windows
      privacy: screen_not_visible_from_hallway
    
    mobile_devices:
      - iPhone_with_MDM: biometric_lock_enabled
      - iPad: encrypted_and_screen_locked
  
  storage:
    secure_cabinet:
      type: lockable_metal_filing_cabinet
      contents:
        - backup_drives: encrypted_USB_drives
        - client_contracts: physical_copies_locked
        - hardware_tokens: YubiKeys_secured
    
    fireproof_safe:
      contents:
        - critical_backups: offline_encrypted_backups
        - emergency_contacts: printed_emergency_procedures
  
  environmental:
    fire_protection:
      - smoke_detectors: 2_units_tested_monthly
      - fire_extinguisher: ABC_rated_inspected_annually
    
    climate_control:
      - temperature: thermostat_set_20°C
      - humidity: dehumidifier_maintains_45%_RH
    
    power_protection:
      - UPS: 1500VA_battery_backup_for_workstation
      - surge_protection: all_devices_on_surge_protectors

  clean_desk_policy:
    daily_routine:
      - end_of_day: all_documents_locked_in_cabinet
      - screen_lock: automatic_after_5_minutes
      - shredding: cross_cut_shredder_for_sensitive_waste
```

**Result:** ✅ Compliant - Comprehensive physical security controls for home office

**ISO 27001:2022 Mapping:**
- A.7.4: Physical security monitoring
- A.7.9: Security of assets off-premises
- A.7.13: Clear desk and clear screen

### Example 2: Visitor Access Control (Compliant)

**Scenario:** Client visiting home office for project kick-off meeting.

```yaml
# Visitor Management Procedure
visitor_access_control:
  pre_visit_preparation:
    schedule:
      date: 2026-02-15
      time: 10:00-12:00
      visitor: client_representative
    
    security_actions:
      - review_calendar: no_overlapping_sensitive_work
      - secure_materials:
          - lock_client_contracts: all_other_clients_secured
          - close_applications: client_systems_logged_out
          - position_screens: face_away_from_guest_seating
      - prepare_meeting_area:
          - clean_desk: no_documents_visible
          - lock_cabinets: filing_cabinet_secured
          - test_screen_lock: automatic_lock_verified
  
  during_visit:
    physical_controls:
      - workspace_access: visitor_not_allowed_in_office_area
      - meeting_location: living_room_separate_from_workspace
      - screen_status: all_devices_locked_before_meeting
      - door_closed: office_door_closed_and_locked
    
    behavioral_controls:
      - conversation_topics: project_scope_only_no_other_clients
      - document_handling: only_visitor_specific_materials_shown
      - device_access: visitor_devices_not_connected_to_network
      - escort_policy: visitor_escorted_if_bathroom_access_needed
  
  post_visit:
    verification_checklist:
      - physical_security:
          - devices_still_locked: verified
          - documents_secured: filing_cabinet_still_locked
          - no_items_left_behind: workspace_checked
      - access_review:
          - system_logs: no_unauthorized_access_detected
          - network_connections: no_unknown_devices_connected
      - follow_up:
          - meeting_notes: sensitive_details_encrypted
          - next_steps: documented_in_project_tracker
```

**Result:** ✅ Compliant - Proper visitor management with information protection

**ISO 27001:2022 Mapping:**
- A.7.1: Physical security perimeters
- A.7.2: Physical entry
- A.7.13: Clear desk and clear screen

### Example 3: Equipment Loss Prevention (Non-Compliant → Corrected)

**Scenario:** Laptop left unattended in coffee shop while working remotely.

**❌ Non-Compliant Practice:**
```yaml
# INCORRECT - Physical Security Violation
coffee_shop_work:
  laptop_security:
    - screen_lock: disabled_for_convenience
    - physical_security: left_on_table_while_ordering_coffee
    - confidential_work: client_contract_visible_on_screen
    - location: public_coffee_shop_with_high_traffic
```

**Problems:**
- ❌ Device left unattended in public space
- ❌ Screen lock disabled exposing confidential information
- ❌ No physical security (cable lock) used
- ❌ Sensitive work performed in public location

**✅ Corrected Approach:**
```yaml
# CORRECT - Secure Remote Work Practices
remote_work_policy:
  location_assessment:
    - evaluate_sensitivity: client_contract_work_is_HIGH_classification
    - decision: work_from_home_office_only_for_sensitive_tasks
  
  public_space_work:
    allowed_activities:
      - general_research: non_client_specific_industry_research
      - email_review: non_confidential_communications_only
      - code_review: public_open_source_projects_only
    
    required_controls:
      - screen_privacy_filter: prevents_shoulder_surfing
      - VPN_connection: always_enabled_for_business_access
      - screen_lock: automatic_after_2_minutes_in_public
      - physical_security: laptop_never_left_unattended
      - positioning: back_to_wall_screen_not_visible_to_others
    
    prohibited_activities:
      - client_contracts: no_confidential_documents_in_public
      - sensitive_data: no_HIGH_or_CRITICAL_data_access
      - production_systems: no_administrative_access_from_public_wifi
  
  device_protection:
    - physical_lock_cable: attached_when_in_public_spaces
    - screen_lock: automatic_and_immediate_when_leaving_seat
    - backup_awareness: work_saved_to_cloud_before_leaving_home
```

**Result:** ✅ Corrected - Appropriate controls for remote work based on data sensitivity

**Classification Impact:**
- 🔴 **Critical/High Data:** Work from home office only with full security controls
- 🟡 **Medium Data:** Public spaces with screen privacy filter and VPN
- 🟢 **Low/Public Data:** Public spaces with basic security awareness

## 🔗 Integration Points

### ISMS Policy Integration

This skill implements controls from:
- **[Physical Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Physical_Security_Policy.md)** - Home office security framework
- **[Asset Register](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Asset_Register.md)** - Equipment inventory and classification
- **[Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)** - Overall security framework
- **[Classification Framework](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md)** - Data sensitivity levels
- **[Incident Response Plan](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Incident_Response_Plan.md)** - Device loss/theft procedures

### Related Security Skills

- **cryptography** - Encryption requirements for devices and storage media
- **data-classification** - Information sensitivity and handling requirements
- **mobile-device-management** - Mobile device security controls
- **access-control** - Authentication and authorization for devices

### Compliance Frameworks

**ISO 27001:2022 Controls:**
- **A.7.1** - Physical security perimeters (home office boundary definition)
- **A.7.2** - Physical entry (visitor management and access control)
- **A.7.4** - Physical security monitoring (environmental and equipment monitoring)
- **A.7.9** - Security of assets off-premises (remote work equipment protection)
- **A.7.13** - Clear desk and clear screen (information exposure prevention)
- **A.7.14** - Secure disposal or re-use of equipment (secure destruction procedures)

**NIST CSF 2.0 Functions:**
- **PR.AC-01** - Physical access to assets is managed and protected
- **PR.DS-01** - Data-at-rest is protected (encrypted storage media)
- **PR.IP-06** - Data is destroyed according to policy (secure disposal)
- **PR.PT-02** - Removable media is protected (encrypted and secured)

**CIS Controls v8.1:**
- **1.1** - Establish and maintain detailed enterprise asset inventory (equipment tracking)
- **3.6** - Securely manage enterprise assets and data (physical security controls)
- **10.7** - Use behavior-based anti-malware software (environmental threat detection)
- **12.8** - Define and maintain role-based access control (visitor management)

## 🎯 Best Practices

### Home Office Security Checklist

```markdown
## Daily Security Routine

**Start of Day:**
- [ ] Verify workspace door is locked
- [ ] Check environmental controls (smoke detector, temperature)
- [ ] Boot devices with BIOS password
- [ ] Verify screen privacy filter is clean and positioned correctly
- [ ] Check UPS battery status

**During Work:**
- [ ] Lock screen when leaving workspace
- [ ] Position screens away from windows and hallways
- [ ] Secure documents immediately after use
- [ ] Shred sensitive waste in cross-cut shredder
- [ ] Escort visitors if they need access to home during work hours

**End of Day:**
- [ ] Log out of all systems
- [ ] Lock all devices with cable locks or in secure storage
- [ ] Secure all documents in lockable cabinet
- [ ] Secure backup media in fireproof safe
- [ ] Verify all windows and doors locked
- [ ] Set alarm system if available
```

### Equipment Protection Matrix

| Device Type | Physical Security | Encryption | Access Control | Backup |
|------------|------------------|------------|---------------|---------|
| **💻 Laptop** | Cable lock + locked office | LUKS full disk | BIOS password + screen lock | Daily to AWS S3 |
| **📱 Mobile** | Physical case + MDM | Device encryption | Biometric + PIN | iCloud/Google backup |
| **💾 USB Drive** | Locked cabinet | BitLocker/LUKS | Password protected | Not primary storage |
| **🖥️ Desktop** | Locked office + bolted desk | LUKS full disk | BIOS password + screen lock | Daily to AWS S3 |
| **⌚ Smart Watch** | Physical security + MDM | Device encryption | PIN/Biometric | Synced to phone |

### Environmental Monitoring

```yaml
# Recommended Environmental Sensors
home_office_monitoring:
  fire_detection:
    - smoke_detectors: 2_units_interconnected
    - heat_detectors: 1_unit_above_equipment
    - testing_schedule: monthly_button_test
  
  water_damage:
    - water_sensors: under_AC_units_and_near_windows
    - leak_detection: near_water_heater_if_adjacent
    - alert_method: SMS_notification_to_phone
  
  climate:
    - temperature_sensor: smart_thermostat_with_alerts
    - humidity_sensor: standalone_hygrometer
    - alert_thresholds:
        - temperature: below_15°C_or_above_30°C
        - humidity: below_25%_or_above_70%
  
  power:
    - UPS_monitoring: software_alerts_for_power_events
    - surge_protection: LED_indicators_on_surge_protectors
    - generator: optional_for_critical_infrastructure
```

## 📊 Risk Mitigation

### Physical Security Threats

| Threat | Impact | Likelihood | Risk Level | Mitigation |
|--------|--------|-----------|-----------|------------|
| **Device Theft** | 🔴 Critical | 🟡 Medium | 🔴 High | Cable locks, locked office, encryption |
| **Fire Damage** | 🔴 Critical | 🟢 Low | 🟡 Medium | Smoke detectors, fire extinguisher, offsite backups |
| **Water Damage** | 🟠 High | 🟡 Medium | 🟠 High | Elevated equipment, water sensors, waterproof bags |
| **Visitor Snooping** | 🟠 High | 🟡 Medium | 🟠 High | Clean desk policy, screen positioning, visitor escort |
| **Environmental** | 🟡 Medium | 🟡 Medium | 🟡 Medium | Climate control, humidity monitoring, UPS |
| **Power Loss** | 🟡 Medium | 🟠 High | 🟡 Medium | UPS backup, surge protection, saved work |
| **Shoulder Surfing** | 🟡 Medium | 🟠 High | 🟠 High | Screen privacy filters, positioning, awareness |

### Incident Response

**Device Loss/Theft:**
1. Immediately report to CEO (self-reporting for single-person company)
2. Remote wipe device if MDM capable (see [Mobile Device Management Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Mobile_Device_Management_Policy.md))
3. Change all passwords accessed from device
4. Report to police if theft suspected
5. Review access logs for unauthorized activity
6. Update [Asset Register](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Asset_Register.md)

**Fire/Water Damage:**
1. Ensure personal safety first
2. Contact emergency services if necessary
3. Document damage with photos
4. Recover equipment if safe to do so
5. Assess data recovery options
6. Restore from backups per [Backup Recovery Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Backup_Recovery_Policy.md)
7. File insurance claim if applicable

## 🔍 Validation & Testing

### Physical Security Audit

```bash
#!/bin/bash
# Physical Security Self-Assessment Script

echo "🏠 Hack23 AB - Physical Security Audit"
echo "========================================"
echo ""

# Workspace Security
echo "📋 Workspace Security Checklist:"
read -p "Is workspace in a lockable room? (yes/no): " lockable_room
read -p "Are windows covered with blinds/film? (yes/no): " window_privacy
read -p "Is secure storage (cabinet/safe) available? (yes/no): " secure_storage
read -p "Are screens positioned away from windows/doors? (yes/no): " screen_position

# Equipment Protection
echo ""
echo "💻 Equipment Protection Checklist:"
read -p "Are laptops using full disk encryption? (yes/no): " disk_encryption
read -p "Are cable locks used for equipment? (yes/no): " cable_locks
read -p "Are mobile devices enrolled in MDM? (yes/no): " mdm_enrolled
read -p "Is automatic screen lock enabled (<5 min)? (yes/no): " screen_lock

# Environmental Controls
echo ""
echo "🌡️ Environmental Controls Checklist:"
read -p "Are smoke detectors installed and tested? (yes/no): " smoke_detectors
read -p "Is fire extinguisher accessible and inspected? (yes/no): " fire_extinguisher
read -p "Is equipment elevated off floor? (yes/no): " elevated_equipment
read -p "Is UPS/surge protection installed? (yes/no): " power_protection

# Clean Desk Policy
echo ""
echo "🧹 Clean Desk Policy Checklist:"
read -p "Are documents locked at end of day? (yes/no): " documents_secured
read -p "Is cross-cut shredder available? (yes/no): " shredder_available
read -p "Are backup media secured in safe/cabinet? (yes/no): " backup_secured

# Calculate compliance score
score=0
total=13

[[ "$lockable_room" == "yes" ]] && ((score++))
[[ "$window_privacy" == "yes" ]] && ((score++))
[[ "$secure_storage" == "yes" ]] && ((score++))
[[ "$screen_position" == "yes" ]] && ((score++))
[[ "$disk_encryption" == "yes" ]] && ((score++))
[[ "$cable_locks" == "yes" ]] && ((score++))
[[ "$mdm_enrolled" == "yes" ]] && ((score++))
[[ "$screen_lock" == "yes" ]] && ((score++))
[[ "$smoke_detectors" == "yes" ]] && ((score++))
[[ "$fire_extinguisher" == "yes" ]] && ((score++))
[[ "$elevated_equipment" == "yes" ]] && ((score++))
[[ "$power_protection" == "yes" ]] && ((score++))
[[ "$documents_secured" == "yes" ]] && ((score++))
[[ "$backup_secured" == "yes" ]] && ((score++))

compliance_percentage=$((score * 100 / total))

echo ""
echo "========================================"
echo "📊 Compliance Score: $score/$total ($compliance_percentage%)"
echo ""

if [ $compliance_percentage -ge 90 ]; then
    echo "✅ EXCELLENT - Physical security controls are comprehensive"
elif [ $compliance_percentage -ge 70 ]; then
    echo "⚠️  GOOD - Minor improvements needed"
elif [ $compliance_percentage -ge 50 ]; then
    echo "⚠️  FAIR - Significant gaps exist, immediate action required"
else
    echo "❌ POOR - Critical physical security deficiencies"
fi

echo ""
echo "📝 Document findings in Security Metrics and Asset Register"
echo "🔄 Schedule remediation for any 'no' responses"
```

### Monthly Security Review

```markdown
## Physical Security Monthly Review Checklist

**Date:** [YYYY-MM-DD]  
**Reviewer:** CEO

### Equipment Inventory
- [ ] Verify all devices in Asset Register are accounted for
- [ ] Check encryption status on all laptops and storage media
- [ ] Test screen locks and BIOS passwords
- [ ] Inspect cable locks for damage or tampering
- [ ] Verify mobile device MDM enrollment status

### Environmental Systems
- [ ] Test smoke detectors (button test)
- [ ] Inspect fire extinguisher pressure gauge
- [ ] Check UPS battery status and runtime test
- [ ] Test water sensors if installed
- [ ] Review climate control (temperature/humidity logs)

### Workspace Security
- [ ] Verify lockable cabinet is functional
- [ ] Inspect fireproof safe for damage
- [ ] Check window coverings for damage or gaps
- [ ] Assess screen positioning for visitor visibility
- [ ] Review clean desk policy compliance

### Visitor Management
- [ ] Review visitor log (if any visits occurred)
- [ ] Assess visitor access procedures effectiveness
- [ ] Update visitor management procedures if needed

### Remediation Actions
- [ ] Document any deficiencies found
- [ ] Assign remediation tasks with deadlines
- [ ] Update Asset Register with any changes
- [ ] Schedule next monthly review
```

## 🎓 Training & Awareness

### Physical Security Principles

**Layered Protection Approach:**
1. **Perimeter Security:** Home office boundary (locked doors, windows secured)
2. **Equipment Security:** Device locks, encryption, screen privacy
3. **Information Security:** Clean desk policy, secure disposal, classification awareness
4. **Environmental Security:** Fire/water/climate protection
5. **Behavioral Security:** Visitor awareness, situational awareness, incident reporting

**Security Culture:**
- Physical security is everyone's responsibility (even in single-person company)
- "If you see something, say something" applies to physical threats too
- Security controls are not obstacles—they protect business continuity
- Transparency in security practices demonstrates professional maturity

### Resources

- **Physical Security Policy:** [View on GitHub](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Physical_Security_Policy.md)
- **Asset Register:** [View on GitHub](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Asset_Register.md)
- **ISO 27001:2022 A.7:** Physical and environmental security controls
- **NIST SP 800-171:** Protecting Controlled Unclassified Information in Nonfederal Systems

---

## 📋 Document Control

**Skill Metadata:**
- **Version:** 1.0
- **Last Updated:** 2026-02-10
- **Review Cycle:** Annual
- **Owner:** Hack23 AB Security Team
- **Classification:** [![Public](https://img.shields.io/badge/C-Public-lightgrey?style=flat-square)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md)

**Framework Compliance:**
- [![ISO 27001:2022](https://img.shields.io/badge/ISO_27001-2022_Aligned-blue?style=flat-square&logo=iso&logoColor=white)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md)
- [![NIST CSF 2.0](https://img.shields.io/badge/NIST_CSF-2.0_Aligned-green?style=flat-square&logo=nist&logoColor=white)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md)
- [![CIS Controls v8.1](https://img.shields.io/badge/CIS_Controls-v8.1_Aligned-orange?style=flat-square&logo=cisecurity&logoColor=white)](https://github.com/Hack23/ISMS-PUBLIC/blob/main/CLASSIFICATION.md)

**License:** Apache-2.0  
**Repository:** https://github.com/Hack23/homepage

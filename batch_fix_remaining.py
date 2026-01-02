#!/usr/bin/env python3
"""
Batch fix remaining 16 Chinese translation files with English titles/descriptions.
"""

import re

# Files and their fixes
fixes = {
    'blog-cia-security_zh.html': {
        'title_old': '<title>CIA Security | Defense Through Transparency | Hack23</title>',
        'title_new': '<title>CIA安全 | 透明防御 | Hack23</title>',
        'desc_pattern': r'<meta name="description" content="([^"]*[A-Za-z]{10,}[^"]*)"',
        'desc_new': '<meta name="description" content="五层防御架构保护政治透明度平台：多重级别安全保护民主监督OSINT系统。">',
    },
    'blog-cia-workflows_zh.html': {
        'title_old': '<title>CIA Workflows | Five-Stage CI/CD Democracy | Hack23</title>',
        'title_new': '<title>CIA工作流程 | 五阶段CI/CD民主 | Hack23</title>',
        'desc_pattern': r'<meta name="description" content="([^"]*[A-Za-z]{10,}[^"]*)"',
        'desc_new': '<meta name="description" content="DevSecOps神圣几何：五个CI/CD工作流程实现代码即民主、构建即透明、部署即责任。">',
    },
    'cia-compliance-manager-docs_zh.html': {
        'title_old': '<title>CIA Compliance Manager Architecture | Technical Documentation | Hack23</title>',
        'title_new': '<title>CIA合规管理器架构 | 技术文档 | Hack23</title>',
    },
    'cia-docs_zh.html': {
        'title_old': '<title>CIA Documentation | System Architecture Guide | Hack23</title>',
        'title_new': '<title>CIA文档 | 系统架构指南 | Hack23</title>',
    },
    'discordian-access-control_zh.html': {
        'desc_pattern': r'<meta name="description" content="访问控制与身份管理">',
        'desc_new': '<meta name="description" content="访问控制与身份管理策略：基于角色的访问控制、多因素认证、最小权限原则和定期审计。">',
    },
    'discordian-asset-mgmt_zh.html': {
        'desc_pattern': r'<meta name="description" content="资产管理与信息分类">',
        'desc_new': '<meta name="description" content="资产管理与信息分类策略：识别、分类和保护组织的信息资产，确保安全责任制和生命周期管理。">',
    },
    'discordian-business-continuity_zh.html': {
        'desc_pattern': r'<meta name="description" content="业务连续性规划">',
        'desc_new': '<meta name="description" content="业务连续性规划策略：确保关键业务功能在中断期间保持运营，包括恢复目标和持续测试。">',
    },
    'discordian-email-security_zh.html': {
        'title_old': '<title>Email Security Policy - Discordian ISMS | Hack23 AB</title>',
        'title_new': '<title>电子邮件安全策略 - Discordian ISMS | Hack23 AB</title>',
        'desc_pattern': r'<meta name="description" content="([^"]*[A-Za-z]{10,}[^"]*)"',
        'desc_new': '<meta name="description" content="电子邮件安全策略：加密、网络钓鱼防护、安全邮件网关和用户培训，保护企业通信安全。">',
    },
    'discordian-incident-response_zh.html': {
        'desc_pattern': r'<meta name="description" content="事件响应与管理">',
        'desc_new': '<meta name="description" content="事件响应与管理策略：检测、响应和从安全事件中恢复的综合流程，包括响应团队和升级程序。">',
    },
    'discordian-isms-transparency_zh.html': {
        'desc_pattern': r'<meta name="description" content="ISMS透明度与公共访问">',
        'desc_new': '<meta name="description" content="ISMS透明度与公共访问策略：通过公开我们的信息安全管理系统建立信任和问责制，展现对安全的承诺。">',
    },
    'discordian-network-security_zh.html': {
        'desc_pattern': r'<meta name="description" content="网络安全与边界保护">',
        'desc_new': '<meta name="description" content="网络安全与边界保护策略：防火墙、入侵检测系统、网络分段和零信任架构保护网络基础设施。">',
    },
    'discordian-risk-assessment_zh.html': {
        'desc_pattern': r'<meta name="description" content="风险评估与管理方法论">',
        'desc_new': '<meta name="description" content="风险评估与管理方法论：系统识别、分析和缓解信息安全风险的结构化方法，持续监控和审查。">',
    },
    'discordian-security-metrics_zh.html': {
        'desc_pattern': r'<meta name="description" content="安全指标与KPI">',
        'desc_new': '<meta name="description" content="安全指标与KPI策略：测量和报告安全计划有效性的关键绩效指标和度量标准，数据驱动决策。">',
    },
    'discordian-threat-modeling_zh.html': {
        'desc_pattern': r'<meta name="description" content="威胁建模方法论">',
        'desc_new': '<meta name="description" content="威胁建模方法论策略：系统识别和评估潜在安全威胁的结构化方法，包括STRIDE、攻击树和风险评级。">',
    },
}

def fix_file(filename, fixes_dict):
    """Apply fixes to a file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified = False
        
        # Fix title if specified
        if 'title_old' in fixes_dict and 'title_new' in fixes_dict:
            if fixes_dict['title_old'] in content:
                content = content.replace(fixes_dict['title_old'], fixes_dict['title_new'])
                modified = True
                print(f"  ✅ Updated title")
        
        # Fix description
        if 'desc_pattern' in fixes_dict and 'desc_new' in fixes_dict:
            content = re.sub(fixes_dict['desc_pattern'], fixes_dict['desc_new'], content)
            modified = True
            print(f"  ✅ Updated description")
        
        if modified:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

# Main execution
print("Fixing remaining 16 Chinese translation files...")
print()

success_count = 0
for filename, file_fixes in fixes.items():
    print(f"Processing {filename}:")
    if fix_file(filename, file_fixes):
        success_count += 1
    print()

print(f"✅ Successfully fixed {success_count}/{len(fixes)} files")

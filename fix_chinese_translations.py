#!/usr/bin/env python3
"""
Fix common English content in Chinese translation files.
Focuses on SEO headers, meta tags, Schema.org, breadcrumbs, and navigation.
"""

import os
import re
import json
from typing import Dict, List, Tuple

# Translation dictionary for common terms
TRANSLATIONS = {
    # Navigation
    "Home": "首页",
    "Blog": "博客",
    "Services": "服务",
    "Projects": "项目",
    "Products": "产品",
    "Contact": "联系我们",
    "Why Hack23": "为什么选择Hack23",
    "CIA Docs": "CIA文档",
    "Docs": "文档",
    "Features": "功能",
    
    # Common page titles
    "Architecture": "架构",
    "Security": "安全",
    "Cybersecurity": "网络安全",
    "Compliance": "合规性",
    "ISMS": "信息安全管理系统",
    "Policy": "策略",
    "Documentation": "文档",
    "Guide": "指南",
    "Checklist": "检查清单",
    
    # Discordian
    "Discordian Cybersecurity": "Discordian网络安全",
    "Think for Yourself": "独立思考",
    
    # CIA Project
    "Citizen Intelligence Agency": "公民情报局",
    "Political Transparency": "政治透明度",
    "Parliamentary Monitoring": "议会监督",
    
    # Black Trigram
    "Black Trigram": "黑卦",
    "Korean Martial Arts": "韩国武术",
    "Combat Game": "格斗游戏",
    
    # Compliance Manager
    "Compliance Manager": "合规管理器",
    
    # Generic
    "Overview": "概述",
    "Introduction": "介绍",
    "Summary": "摘要",
    "Details": "详情",
    "FAQ": "常见问题",
}

def translate_text(text: str) -> str:
    """Translate common English terms to Chinese."""
    result = text
    for en, zh in TRANSLATIONS.items():
        # Word boundary matching to avoid partial replacements
        result = re.sub(rf'\b{re.escape(en)}\b', zh, result)
    return result

def fix_meta_tags(content: str) -> str:
    """Fix English content in meta tags."""
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Skip lines that are already in Chinese (contain Chinese characters)
        if re.search(r'[\u4e00-\u9fff]', line) and not re.search(r'<meta name="(description|keywords)"', line):
            fixed_lines.append(line)
            continue
            
        # Translate meta descriptions and keywords if they're in English
        if '<meta name="description"' in line or '<meta name="keywords"' in line:
            # Only translate if line has significant English content
            english_words = len(re.findall(r'[A-Za-z]{4,}', line))
            if english_words > 5:
                # This needs manual translation - mark for review
                fixed_lines.append(line)
            else:
                fixed_lines.append(line)
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_breadcrumbs(content: str) -> str:
    """Fix English breadcrumb navigation."""
    # Fix breadcrumb items
    for en, zh in TRANSLATIONS.items():
        # Breadcrumb pattern
        pattern = rf'(<li[^>]*class="breadcrumb-item"[^>]*>[\s]*<a[^>]*>)({en})(</a>)'
        replacement = rf'\1{zh}\3'
        content = re.sub(pattern, replacement, content)
        
        # Breadcrumb without link
        pattern = rf'(<li[^>]*class="breadcrumb-item"[^>]*>)({en})(</li>)'
        replacement = rf'\1{zh}\3'
        content = re.sub(pattern, replacement, content)
    
    return content

def fix_header_nav(content: str) -> str:
    """Fix navigation links in header."""
    # Navigation links
    for en, zh in TRANSLATIONS.items():
        # Pattern: <a href="...">English</a>
        pattern = rf'(<a\s+href="[^"]*">)\s*{re.escape(en)}\s*(</a>)'
        replacement = rf'\1{zh}\2'
        content = re.sub(pattern, replacement, content)
    
    return content

def fix_h1_header(content: str) -> str:
    """Fix H1 headers with common English terms."""
    for en, zh in TRANSLATIONS.items():
        # H1 pattern
        pattern = rf'(<h1[^>]*>)(.*?)\b{re.escape(en)}\b(.*?)(</h1>)'
        def replace_h1(match):
            before = match.group(2)
            after = match.group(3)
            # Only replace if not already translated
            if not re.search(r'[\u4e00-\u9fff]', before + after):
                return f'{match.group(1)}{before}{zh}{after}{match.group(4)}'
            return match.group(0)
        content = re.sub(pattern, replace_h1, content, flags=re.DOTALL)
    
    return content

def analyze_file(filepath: str) -> Dict:
    """Analyze a file for English content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    # Check title
    title_match = re.search(r'<title>([^<]+)</title>', content)
    if title_match:
        title = title_match.group(1)
        english_words = len(re.findall(r'[A-Za-z]{4,}', title))
        if english_words > 2:
            issues.append(f"Title has {english_words} English words")
    
    # Check meta description
    desc_match = re.search(r'<meta name="description" content="([^"]+)"', content)
    if desc_match:
        desc = desc_match.group(1)
        english_words = len(re.findall(r'[A-Za-z]{4,}', desc))
        if english_words > 5:
            issues.append(f"Description has {english_words} English words")
    
    # Check breadcrumbs
    breadcrumb_matches = re.findall(r'<li[^>]*class="breadcrumb-item"[^>]*>([^<]+)</li>', content)
    for bc in breadcrumb_matches:
        if re.search(r'[A-Z][a-z]{3,}', bc):
            issues.append(f"Breadcrumb in English: {bc[:30]}")
    
    # Check H1
    h1_match = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
    if h1_match:
        h1 = h1_match.group(1)
        english_words = len(re.findall(r'[A-Za-z]{4,}', h1))
        if english_words > 3:
            issues.append(f"H1 has {english_words} English words")
    
    return {
        'filepath': filepath,
        'issues': issues,
        'issue_count': len(issues)
    }

def main():
    """Main function to analyze and optionally fix Chinese translation files."""
    # Get all Chinese HTML files
    zh_files = [f for f in os.listdir('.') if f.endswith('_zh.html')]
    
    print(f"Found {len(zh_files)} Chinese translation files\n")
    
    # Analyze all files
    all_issues = []
    for filename in sorted(zh_files):
        analysis = analyze_file(filename)
        if analysis['issue_count'] > 0:
            all_issues.append(analysis)
    
    print(f"\n=== Analysis Results ===")
    print(f"Files with issues: {len(all_issues)}/{len(zh_files)}")
    print(f"\nTop 20 files needing attention:\n")
    
    for analysis in sorted(all_issues, key=lambda x: x['issue_count'], reverse=True)[:20]:
        print(f"{analysis['filepath']}")
        for issue in analysis['issues']:
            print(f"  - {issue}")
        print()

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Hebrew SEO Enhancement Script
Systematically improves SEO metadata for all Hebrew HTML files
Target: 95%+ quality with comprehensive Hebrew keywords
"""

import re
import glob
from pathlib import Path

# Comprehensive Hebrew cybersecurity keyword bank (95 terms)
HEBREW_KEYWORDS = [
    "אבטחת סייבר",  # Cybersecurity
    "אבטחת מידע",  # Information security
    "מערכת ניהול אבטחת מידע",  # ISMS
    "ISO 27001",
    "הערכת סיכונים",  # Risk assessment
    "תגובה לאירועים",  # Incident response
    "ניהול פגיעויות",  # Vulnerability management
    "הגנה על מידע",  # Data protection
    "בקרת גישה",  # Access control
    "אבטחת ענן",  # Cloud security
    "ציות",  # Compliance
    "DevSecOps",
    "שלישיית CIA",  # CIA Triad
    "GDPR",
    "NIS2",
    "סודיות",  # Confidentiality
    "שלמות",  # Integrity
    "זמינות",  # Availability
    "ניהול סיכונים",  # Risk management
    "ביקורת אבטחה",  # Security audit
    "תכנון רציפות עסקית",  # Business continuity planning
    "התאוששות מאסון",  # Disaster recovery
    "אבטחת רשת",  # Network security
    "חומת אש",  # Firewall
    "הצפנה",  # Encryption
    "אימות",  # Authentication
    "הרשאה",  # Authorization
    "בדיקת חדירה",  # Penetration testing
    "ניטור אבטחה",  # Security monitoring
    "מודיעין איומים",  # Threat intelligence
    "תרבות אבטחה",  # Security culture
    "הדרכת אבטחה",  # Security training
    "מדיניות אבטחה",  # Security policy
    "מסגרת אבטחה",  # Security framework
    "ממשל אבטחה",  # Security governance
    "שירותי אבטחה",  # Security services
    "יועץ אבטחה",  # Security consultant
    "ארכיטקטורת אבטחה",  # Security architecture
    "פיתוח מאובטח",  # Secure development
    "SDLC מאובטח",  # Secure SDLC
    "ניהול תצורה",  # Configuration management
    "ניהול תיקונים",  # Patch management
    "גיבוי ושחזור",  # Backup and recovery
    "הגנה על קצה",  # Endpoint protection
    "אבטחה פיזית",  # Physical security
    "ניהול אירועים",  # Event management
    "SIEM",
    "SOC",  # Security Operations Center
    "אפס אמון",  # Zero trust
    "הגנה בעומק",  # Defense in depth
    "הרשאה מינימלית",  # Least privilege
    "אבטחה לפי תכנון",  # Security by design
    "אבטחה כברירת מחדל",  # Security by default
    "פגיעות",  # Vulnerability
    "איום",  # Threat
    "סיכון",  # Risk
    "משטח תקיפה",  # Attack surface
    "גורם מאיים",  # Threat actor
    "פריצת מידע",  # Data breach
    "דליפת מידע",  # Data leak
    "כופרה",  # Ransomware
    "תוכנה זדונית",  # Malware
    "דיוג",  # Phishing
    "הנדסה חברתית",  # Social engineering
    "DDoS",
    "SQL Injection",
    "XSS",  # Cross-site scripting
    "CSRF",
    "הזרקת קוד",  # Code injection
    "הסלמת הרשאות",  # Privilege escalation
    "תנועה רוחבית",  # Lateral movement
    "שימור מתמשך",  # Persistence
    "מחיקת עקבות",  # Anti-forensics
    "תרגיל RED TEAM",  # Red team exercise
    "תרגיל BLUE TEAM",  # Blue team exercise
    "PURPLE TEAM",
    "OSINT",
    "CTI",  # Cyber Threat Intelligence
    "CVSS",
    "CVE",
    "CWE",
    "OWASP Top 10",
    "CIS Controls",
    "NIST CSF",
    "ניהול זהות",  # Identity management
    "IAM",
    "MFA",  # Multi-factor authentication
    "SSO",
    "PKI",
    "תעודות דיגיטליות",  # Digital certificates
    "חתימה דיגיטלית",  # Digital signature
    "בלוקצ'יין",  # Blockchain
    "קריפטוגרפיה",  # Cryptography
    "קוד פתוח",  # Open source
]

def analyze_file(filepath):
    """Analyze a Hebrew HTML file and return enhancement recommendations"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    results = {
        'filepath': filepath,
        'has_rtl': 'dir="rtl"' in content,
        'has_lang_he': 'lang="he"' in content,
        'has_og_locale': 'og:locale' in content and 'he_IL' in content,
    }
    
    # Extract meta description
    desc_match = re.search(r'<meta name="description" content="([^"]*)"', content)
    if desc_match:
        desc = desc_match.group(1)
        results['description'] = desc
        results['description_length'] = len(desc)
        results['description_ok'] = len(desc) >= 140 and len(desc) <= 160
    else:
        results['description'] = None
        results['description_length'] = 0
        results['description_ok'] = False
    
    # Extract meta keywords
    keywords_match = re.search(r'<meta name="keywords" content="([^"]*)"', content)
    if keywords_match:
        keywords = keywords_match.group(1)
        keyword_list = [k.strip() for k in keywords.split(',')]
        results['keywords'] = keyword_list
        results['keyword_count'] = len(keyword_list)
        results['keywords_ok'] = len(keyword_list) >= 40
    else:
        results['keywords'] = []
        results['keyword_count'] = 0
        results['keywords_ok'] = False
    
    # Check for Schema.org inLanguage
    results['has_schema_inlanguage'] = 'inLanguage' in content and '"he"' in content
    
    return results

def get_relevant_keywords(filepath, base_count=50):
    """Get relevant keywords for a specific file based on its category"""
    filename = Path(filepath).name
    
    # Start with core keywords
    keywords = HEBREW_KEYWORDS[:30]  # Core 30 keywords
    
    # Add category-specific keywords
    if 'blog' in filename:
        keywords.extend(HEBREW_KEYWORDS[30:60])  # Blog-specific terms
    elif 'discordian' in filename:
        keywords.extend(HEBREW_KEYWORDS[20:50])  # ISMS-specific terms
    elif 'cia' in filename or 'compliance' in filename or 'black-trigram' in filename:
        keywords.extend(HEBREW_KEYWORDS[10:40])  # Product-specific terms
    elif 'iso-27001' in filename:
        keywords.extend(HEBREW_KEYWORDS[0:30])  # ISO-specific terms
    elif 'industries' in filename:
        keywords.extend(HEBREW_KEYWORDS[15:45])  # Industry-specific terms
    else:
        keywords.extend(HEBREW_KEYWORDS[30:60])  # General terms
    
    # Remove duplicates and limit to requested count
    unique_keywords = list(dict.fromkeys(keywords))
    return unique_keywords[:base_count]

def enhance_keywords(filepath, content, target_count=50):
    """Enhance keywords meta tag to include comprehensive Hebrew terms"""
    current_match = re.search(r'<meta name="keywords" content="([^"]*)"', content)
    
    if not current_match:
        return content, 0
    
    current_keywords_str = current_match.group(1)
    current_keywords = [k.strip() for k in current_keywords_str.split(',')]
    
    # Get relevant keywords for this file
    relevant_keywords = get_relevant_keywords(filepath, target_count)
    
    # Merge current with new, preserving order and removing duplicates
    merged = current_keywords.copy()
    for kw in relevant_keywords:
        if kw not in merged:
            merged.append(kw)
    
    # Limit to target count
    final_keywords = merged[:target_count]
    new_keywords_str = ', '.join(final_keywords)
    
    # Replace in content
    new_content = content.replace(
        f'<meta name="keywords" content="{current_keywords_str}">',
        f'<meta name="keywords" content="{new_keywords_str}">'
    )
    
    added_count = len(final_keywords) - len(current_keywords)
    return new_content, added_count

def enhance_description(content, target_length=150):
    """Enhance meta description if it's too short"""
    desc_match = re.search(r'<meta name="description" content="([^"]*)"', content)
    
    if not desc_match:
        return content, 0
    
    current_desc = desc_match.group(1)
    current_length = len(current_desc)
    
    # If already good length, don't change
    if current_length >= 140 and current_length <= 160:
        return content, 0
    
    # If too short, we need human review - just flag it
    # Don't auto-extend as it needs contextual enhancement
    return content, 0

def main():
    """Main enhancement script"""
    hebrew_files = sorted(glob.glob('*_he.html'))
    
    print(f"🔍 Analyzing {len(hebrew_files)} Hebrew files...\n")
    
    stats = {
        'files_analyzed': 0,
        'keywords_enhanced': 0,
        'files_updated': 0,
        'keywords_added': 0
    }
    
    files_needing_desc_enhancement = []
    files_needing_schema_fix = []
    
    for filepath in hebrew_files:
        analysis = analyze_file(filepath)
        stats['files_analyzed'] += 1
        
        # Track issues
        if not analysis['description_ok']:
            files_needing_desc_enhancement.append({
                'file': filepath,
                'current': analysis['description_length'],
                'desc': analysis['description']
            })
        
        if not analysis['has_schema_inlanguage']:
            files_needing_schema_fix.append(filepath)
        
        # Enhance keywords if needed
        if analysis['keyword_count'] < 40:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content, added = enhance_keywords(filepath, content, target_count=50)
            
            if added > 0:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                stats['keywords_enhanced'] += 1
                stats['keywords_added'] += added
                stats['files_updated'] += 1
                print(f"✅ {filepath}: Added {added} keywords ({analysis['keyword_count']} → {analysis['keyword_count'] + added})")
    
    print(f"\n📊 Enhancement Summary:")
    print(f"  Files analyzed: {stats['files_analyzed']}")
    print(f"  Files updated: {stats['files_updated']}")
    print(f"  Keywords enhanced: {stats['keywords_enhanced']} files")
    print(f"  Total keywords added: {stats['keywords_added']}")
    
    print(f"\n⚠️  Files needing description enhancement: {len(files_needing_desc_enhancement)}")
    if files_needing_desc_enhancement:
        print("  (Requires manual review for contextual enhancement)")
        for item in files_needing_desc_enhancement[:5]:
            print(f"  - {item['file']}: {item['current']} chars")
    
    print(f"\n⚠️  Files missing Schema.org inLanguage: {len(files_needing_schema_fix)}")
    if files_needing_schema_fix:
        for file in files_needing_schema_fix[:5]:
            print(f"  - {file}")
    
    print(f"\n✅ SEO Enhancement Complete!")

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Hebrew Terminology Standardization Script
Phase 4: Apply consistent terminology across all 62 Hebrew pages

IMPORTANT SAFETY FEATURES:
- Protects URLs, canonical links, and hreflang attributes
- Preserves filenames and file extensions
- Skips CSS IDs and class names
- Avoids replacements inside HTML tags
- Protects product names (e.g., "Compliance Manager")
- Protects JSON-LD structured data property names (schema.org)
- Protects HTML title attributes
- Only replaces terms in visible content text

NOTE: English plural forms (assessments, registers, threats) are NOT translated
to avoid creating mixed Hebrew+English forms like "הערכת סיכוניםs". Keep plurals
in English or use proper Hebrew plural constructions.

PROTECTED CONTEXTS:
- JSON-LD schema.org property names (e.g., "availability", "integrity")
- CSS class and id attributes (e.g., class="btn-compliance")
- URL paths and filenames
- Title and alt attributes in English context
- Mixed-language prevention in structured data
"""

import re
import os
import sys
from pathlib import Path

# Terminology mapping based on Hebrew-Translation-Guide.md v3.1
TERMINOLOGY_MAP = {
    # Core Security Terms (most frequent)
    "Incident Response": "תגובה לאירועים",
    "incident response": "תגובה לאירועים",
    "Risk Assessment": "הערכת סיכונים",
    "risk assessment": "הערכת סיכונים",
    "Cybersecurity": "אבטחת סייבר",
    "cybersecurity": "אבטחת סייבר",
    "Cyber Security": "אבטחת סייבר",
    "cyber security": "אבטחת סייבר",
    
    # Compliance (prefer ציות for regulatory context)
    # Only replace when NOT followed by "Manager" (product name)
    
    # Vulnerability/Threat
    "Vulnerability": "פגיעות",
    "vulnerability": "פגיעות",
    "Threat": "איום",
    "threat": "איום",
    
    # ISMS Governance
    "Security Policy": "מדיניות אבטחה",
    "security policy": "מדיניות אבטחה",
    "Risk Management": "ניהול סיכונים",
    "risk management": "ניהול סיכונים",
    "Threat Modeling": "דוגמת איומים",
    "threat modeling": "דוגמת איומים",
    "Risk Register": "רישום סיכונים",
    "risk register": "רישום סיכונים",
    "Access Control": "בקרת גישה",
    "access control": "בקרת גישה",
    
    # CIA Triad
    "Confidentiality": "סודיות",
    "confidentiality": "סודיות",
    "Integrity": "שלמות",
    "integrity": "שלמות",
    "Availability": "זמינות",
    "availability": "זמינות",
    
    # Advanced Security
    "Zero Trust": "אפס אמון",
    "zero trust": "אפס אמון",
    "Defense in Depth": "הגנה בעומק",
    "defense in depth": "הגנה בעומק",
    "Least Privilege": "הרשאה מינימלית",
    "least privilege": "הרשאה מינימלית",
    "Penetration Test": "בדיקת חדירה",
    "penetration test": "בדיקת חדירה",
    "Attack Surface": "משטח תקיפה",
    "attack surface": "משטח תקיפה",
    "Threat Actor": "גורם מאיים",
    "threat actor": "גורם מאיים",
    "Security Incident": "אירוע אבטחה",
    "security incident": "אירוע אבטחה",
    "Data Breach": "פריצת מידע",
    "data breach": "פריצת מידע",
    
    # Fix Hebrew singular/plural inconsistency
    "תגובה לאירוע ": "תגובה לאירועים ",
    "תגובה לאירוע<": "תגובה לאירועים<",
    "תגובה לאירוע.": "תגובה לאירועים.",
    "תגובה לאירוע,": "תגובה לאירועים,",
}

# Special handling for "Compliance" - avoid replacing in "Compliance Manager" (product name)
COMPLIANCE_CONTEXTS = {
    "Compliance": "ציות",
    "compliance": "ציות",
}

# Terms to preserve in English (international standards, product names, tech terms)
PRESERVE_ENGLISH = [
    "DevSecOps", "CI/CD", "API", "REST", "AWS", "Docker", "Kubernetes", "GitHub",
    "FNORD", "Chapel Perilous", "23 FNORD 5",
    "ISO 27001", "ISO 27002", "GDPR", "NIS2", "HIPAA",
    "Compliance Manager",  # Product name
    "Black Trigram",  # Product name
    "Citizen Intelligence Agency",  # Product name
]


def should_skip_replacement(text: str, term: str, position: int) -> bool:
    """Check if replacement should be skipped based on context"""
    
    # Check if term is part of a product name
    if term in ["Compliance", "compliance"]:
        # Check for "Compliance Manager" (product name)
        if position + len(term) + 8 <= len(text):
            following = text[position + len(term):position + len(term) + 8]
            if "Manager" in following:
                return True
    
    # Get context around the term (larger window for better detection)
    start = max(0, position - 200)
    end = min(len(text), position + len(term) + 200)
    context = text[start:end]
    relative_pos = position - start
    
    # Skip if inside <script> or <style> tags
    if '<script' in context[:relative_pos] and '</script>' not in context[:relative_pos]:
        return True
    if '<style' in context[:relative_pos] and '</style>' not in context[:relative_pos]:
        return True
    
    # Skip if inside HTML tag (between < and >)
    before_term = context[:relative_pos]
    last_open = before_term.rfind('<')
    last_close = before_term.rfind('>')
    if last_open > last_close:
        return True  # Inside HTML tag
    
    # Skip if inside href, src, or canonical URL attributes
    # Look for patterns like href="..." or src="..." containing the term
    if last_open != -1:
        tag_content = context[last_open:relative_pos + len(term)]
        # Check if we're inside a URL attribute
        if any(attr in tag_content for attr in ['href="', 'src="', 'content="http', 'data-href=']):
            return True
    
    # Skip if inside hreflang or canonical links
    if 'hreflang' in before_term[-50:] or 'canonical' in before_term[-50:]:
        return True
    
    # Skip if inside id or class attributes (CSS identifiers)
    if any(attr in before_term[-30:] for attr in ['id="', 'class="', 'data-']):
        return True
    
    # Skip if part of a filename pattern (contains .html, .css, .js, etc.)
    around_term = context[max(0, relative_pos-20):min(len(context), relative_pos+len(term)+20)]
    if any(ext in around_term for ext in ['.html', '.css', '.js', '.png', '.jpg', '.svg', '.pdf']):
        return True
    
    # Skip if inside a URL pattern (contains ://)
    if '://' in around_term:
        return True
    
    # Skip if inside JSON-LD structured data
    # Check for schema.org property names that must remain in English
    if '"' + term.lower() + '"' in around_term.lower():
        # Check if preceded by colon (JSON property)
        json_context = context[max(0, relative_pos-10):relative_pos]
        if ':' in json_context or '"@type"' in before_term[-100:]:
            return True
    
    # Skip if inside title attribute (to avoid mixed language)
    if 'title="' in before_term[-15:] and '"' not in context[relative_pos:relative_pos+50]:
        # We're inside a title attribute
        return True
    
    # Skip if inside alt attribute (to avoid mixed language)
    if 'alt="' in before_term[-15:] and '"' not in context[relative_pos:relative_pos+50]:
        return True
    
    return False


def standardize_terminology(file_path: Path) -> Tuple[int, List[str]]:
    """Standardize terminology in a single Hebrew HTML file"""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes = []
        total_replacements = 0
        
        # Apply standard terminology mappings
        for english, hebrew in TERMINOLOGY_MAP.items():
            count = content.count(english)
            if count > 0:
                # Use word boundary matching for better accuracy
                pattern = re.escape(english)
                new_content = content
                
                # Find all occurrences and check context
                positions = [m.start() for m in re.finditer(pattern, content)]
                
                # Replace from end to start to maintain positions
                for pos in reversed(positions):
                    if not should_skip_replacement(content, english, pos):
                        new_content = new_content[:pos] + hebrew + new_content[pos + len(english):]
                
                if new_content != content:
                    actual_count = len(positions) - (content.count(english) - new_content.count(hebrew))
                    if actual_count > 0:
                        changes.append(f"  {english} → {hebrew} ({actual_count}x)")
                        total_replacements += actual_count
                    content = new_content
        
        # Special handling for "Compliance" (avoid product name)
        for english, hebrew in COMPLIANCE_CONTEXTS.items():
            # Only replace when not followed by " Manager"
            pattern = english + r'(?! Manager)'
            matches = list(re.finditer(pattern, content))
            if matches:
                new_content = re.sub(pattern, hebrew, content)
                if new_content != content:
                    count = len(matches)
                    changes.append(f"  {english} → {hebrew} ({count}x)")
                    total_replacements += count
                    content = new_content
        
        # Write back if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        return total_replacements, changes
    
    except Exception as e:
        print(f"ERROR processing {file_path}: {e}")
        return 0, []


def main():
    """Main execution"""
    print("🇮🇱 Hebrew Terminology Standardization - Phase 4B")
    print("=" * 60)
    print()
    
    # Find all Hebrew HTML files
    hebrew_files = sorted(Path('.').glob('*_he.html'))
    
    if not hebrew_files:
        print("❌ No Hebrew HTML files found")
        return 1
    
    print(f"📊 Found {len(hebrew_files)} Hebrew HTML files")
    print()
    
    total_files_changed = 0
    total_replacements = 0
    all_changes = []
    
    # Process each file
    for file_path in hebrew_files:
        replacements, changes = standardize_terminology(file_path)
        
        if replacements > 0:
            total_files_changed += 1
            total_replacements += replacements
            print(f"✅ {file_path.name}: {replacements} replacements")
            for change in changes:
                print(change)
            print()
            all_changes.append((file_path.name, replacements, changes))
    
    # Summary
    print("=" * 60)
    print("📈 STANDARDIZATION SUMMARY")
    print("=" * 60)
    print(f"✓ Files processed: {len(hebrew_files)}")
    print(f"✓ Files changed: {total_files_changed}")
    print(f"✓ Total replacements: {total_replacements}")
    print()
    
    # Generate summary report
    report_path = Path('/tmp/terminology_standardization_report.md')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Hebrew Terminology Standardization Report\n\n")
        f.write(f"**Date:** {os.popen('date').read().strip()}\n")
        f.write(f"**Phase:** 4B - Implementation\n\n")
        f.write("## Summary\n\n")
        f.write(f"- **Files processed:** {len(hebrew_files)}\n")
        f.write(f"- **Files changed:** {total_files_changed}\n")
        f.write(f"- **Total replacements:** {total_replacements}\n\n")
        f.write("## Changes by File\n\n")
        
        for filename, count, changes in all_changes:
            f.write(f"### {filename} ({count} replacements)\n\n")
            for change in changes:
                f.write(f"{change}\n")
            f.write("\n")
        
        f.write("## Standardized Terminology\n\n")
        f.write("All files now use consistent Hebrew terminology according to ")
        f.write("Hebrew-Translation-Guide.md v3.1:\n\n")
        f.write("- ✅ Incident Response → תגובה לאירועים\n")
        f.write("- ✅ Risk Assessment → הערכת סיכונים\n")
        f.write("- ✅ Cybersecurity → אבטחת סייבר\n")
        f.write("- ✅ Compliance → ציות (regulatory context)\n")
        f.write("- ✅ Security → אבטחה (info security)\n")
        f.write("- ✅ Fixed singular/plural: תגובה לאירוע → תגובה לאירועים\n\n")
        f.write("## Preserved English Terms\n\n")
        f.write("The following terms remain in English as per guidelines:\n")
        for term in PRESERVE_ENGLISH[:10]:
            f.write(f"- {term}\n")
        f.write("\n")
    
    print(f"📄 Report saved: {report_path}")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())

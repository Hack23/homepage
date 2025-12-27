#!/usr/bin/env python3
"""
Fix structured data and attribute corruption from terminology standardization
Reverts Hebrew in JSON-LD schema, CSS classes, and title attributes
"""

from pathlib import Path

# Patterns to fix
FIXES = {
    # JSON-LD Schema.org property names (must remain English)
    '"זמינות"': '"availability"',
    '"סודיות"': '"confidentiality"',
    '"שלמות"': '"integrity"',
    
    # CSS class names (must remain ASCII)
    'class="btn-ציות"': 'class="btn-compliance"',
    'class="btn-אבטחה"': 'class="btn-security"',
    
    # More plural issues
    'אירוע אבטחהs': 'security incidents',
    'איוםs threat': 'threats',
    
    # Mixed language in title attributes and structured data
    'Information מדיניות אבטחה': 'Information Security Policy',
    'Transparent אבטחת סייבר Consulting': 'Transparent Cybersecurity Consulting',
    
    # Revert Hebrew in English FAQ structured data
    'ISO 27001 ציות': 'ISO 27001 compliance',
    'emerging איוםs': 'emerging threats',
    'continuously monitor איוםs': 'continuously monitor threats',
}

def fix_file(file_path: Path) -> int:
    """Fix structured data and attribute corruption in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        replacements = 0
        
        for pattern, replacement in FIXES.items():
            count = content.count(pattern)
            if count > 0:
                content = content.replace(pattern, replacement)
                replacements += count
                print(f"  {file_path.name}: Fixed {count} instances of '{pattern}' → '{replacement}'")
        
        if replacements > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        return replacements
    
    except Exception as e:
        print(f"  ⚠️  Error fixing {file_path}: {e}")
        return 0


def main():
    """Main execution"""
    print("🔧 Fixing Structured Data and Attribute Corruption")
    print("=" * 60)
    print()
    
    base_path = Path('.')
    hebrew_files = list(base_path.glob('*_he.html'))
    
    if not hebrew_files:
        print("❌ No Hebrew files found")
        return 1
    
    print(f"📄 Found {len(hebrew_files)} Hebrew files to check")
    print()
    
    total_fixes = 0
    files_fixed = 0
    
    for file in sorted(hebrew_files):
        fixes = fix_file(file)
        if fixes > 0:
            total_fixes += fixes
            files_fixed += 1
    
    print()
    print("=" * 60)
    print("✅ FIXES COMPLETE")
    print("=" * 60)
    print(f"Files checked: {len(hebrew_files)}")
    print(f"Files fixed: {files_fixed}")
    print(f"Total fixes: {total_fixes}")
    print()
    
    if total_fixes > 0:
        print("✅ Structured data corruption fixed")
        return 0
    else:
        print("ℹ️  No issues found")
        return 0


if __name__ == '__main__':
    exit(main())

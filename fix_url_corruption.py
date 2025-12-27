#!/usr/bin/env python3
"""
Fix URL and filename corruption from terminology standardization
Reverts Hebrew characters in URLs, canonical links, and hrefs back to English
"""

import re
from pathlib import Path

# Patterns to fix
FIXES = {
    # Fix compliance-manager URLs
    r'ציות-manager': 'compliance-manager',
    r'cia-ציות-manager': 'cia-compliance-manager',
    
    # Fix plural issues (Hebrew + English 's')
    r'הערכת סיכוניםs': 'risk assessments',
    r'רישום סיכוניםs': 'risk registers',
    r'איוםs': 'threats',
    r'פגיעותs': 'vulnerabilities',
}

def fix_file(file_path: Path) -> int:
    """Fix URL corruption in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
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
    print("🔧 Fixing URL and Filename Corruption")
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
        print("✅ URL corruption fixed")
        return 0
    else:
        print("ℹ️  No issues found")
        return 0


if __name__ == '__main__':
    exit(main())

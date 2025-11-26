#!/usr/bin/env python3
"""
Fix Duplicate FAQPage Schemas - REFERENCE ONLY

⚠️  NOTE: This script was used during the initial fix and is kept for reference only.
⚠️  It is NOT part of the production codebase and should NOT be run again.
⚠️  For ongoing validation, use: validate_structured_data.py

This script removes duplicate FAQPage schemas from homepage files.
It keeps the more comprehensive second FAQPage and removes the first one.

Historical Context:
- Used to fix duplicate FAQPage issues detected by Google Search Console
- Fixed all 11 homepage language versions (index.html, index_sv.html, etc.)
- Ran once on November 26, 2025
- All fixes have been validated and committed

CodeQL Alert (py/redos):
- Line 23 contains a regex pattern that could cause exponential backtracking
- This is acceptable for a one-time reference script
- If reusing this pattern, consider using a simpler approach or atomic groups
"""

import re
from pathlib import Path

def fix_duplicate_faqpage(file_path: Path) -> bool:
    """
    Fix duplicate FAQPage in a file.
    Returns True if changes were made.
    
    ⚠️  WARNING: This function is for reference only. Do not run without review.
    """
    print(f"\nProcessing {file_path.name}...")
    
    content = file_path.read_text(encoding='utf-8')
    original_content = content
    
    # Find all FAQPage occurrences
    faqpage_pattern = r'(\{\s*"@type":\s*"FAQPage"[^}]*"mainEntity":\s*\[[^\]]*(?:\{[^\}]*\}[^\]]*)*\]\s*\})'
    matches = list(re.finditer(faqpage_pattern, content, re.DOTALL))
    
    if len(matches) < 2:
        print(f"  ✓ Only {len(matches)} FAQPage found - no duplicates")
        return False
    
    print(f"  Found {len(matches)} FAQPage schemas")
    
    # Strategy: Remove the first FAQPage along with its script tag wrapper if it exists
    # We need to be more careful and look for the pattern of the first FAQ
    
    # Pattern 1: Standalone script tag with FAQPage (like in index.html)
    pattern1 = r'\n\s*<!-- FAQ Schema for SEO -->\s*\n\s*<script type="application/ld\+json">\s*\n\s*\{\s*\n\s*"@context":\s*"https://schema\.org",\s*\n\s*"@type":\s*"FAQPage",\s*\n\s*"mainEntity":\s*\[.*?\]\s*\n\s*\}\s*\n\s*</script>\s*\n'
    
    if re.search(pattern1, content, re.DOTALL):
        print("  Removing standalone FAQPage schema (pattern 1)...")
        content = re.sub(pattern1, '\n', content, count=1, flags=re.DOTALL)
        if content != original_content:
            file_path.write_text(content, encoding='utf-8')
            print(f"  ✓ Removed duplicate FAQPage from {file_path.name}")
            return True
    
    # Pattern 2: FAQPage inside @graph array
    # Look for the FAQPage object inside a @graph, followed by a closing brace and bracket
    pattern2 = r',\s*\n\s*\{\s*\n\s*"@type":\s*"FAQPage",\s*\n\s*"mainEntity":\s*\[.*?\]\s*\n\s*\}\s*\n\s*\]'
    
    if re.search(pattern2, content, re.DOTALL):
        print("  Removing FAQPage from @graph (pattern 2)...")
        # Replace with just the closing bracket (removes the FAQPage and its comma)
        content = re.sub(pattern2, '\n\t  ]\n', content, count=1, flags=re.DOTALL)
        if content != original_content:
            file_path.write_text(content, encoding='utf-8')
            print(f"  ✓ Removed duplicate FAQPage from {file_path.name}")
            return True
    
    print(f"  ⚠️  Could not match known patterns - manual review needed")
    return False


def main():
    """Main entry point."""
    
    # Files to fix
    files_to_fix = [
        'index_nl.html',
        'index_de.html', 
        'index_fr.html',
        'index_es.html',
        'index_he.html',
        'index_ar.html',
        'index_ja.html',
        'index_zh.html'
    ]
    
    current_dir = Path.cwd()
    fixed_count = 0
    
    print("="*80)
    print("DUPLICATE FAQPAGE REMOVAL SCRIPT")
    print("="*80)
    
    for filename in files_to_fix:
        file_path = current_dir / filename
        if file_path.exists():
            if fix_duplicate_faqpage(file_path):
                fixed_count += 1
        else:
            print(f"\n⚠️  {filename} not found")
    
    print("\n" + "="*80)
    print(f"✅ Fixed {fixed_count} files")
    print("="*80)

if __name__ == '__main__':
    main()

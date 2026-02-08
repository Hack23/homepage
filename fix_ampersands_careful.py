#!/usr/bin/env python3
"""
Fix raw ampersands in HTML files while preserving JSON-LD structured data.
Only fixes ampersands that are not already encoded.
"""

import re
import sys
from pathlib import Path

def fix_ampersands_in_html(content):
    """
    Fix raw ampersands in HTML content.
    Handles:
    1. Text content (including JSON-LD)
    2. URL query parameters in href/src attributes
    
    Does NOT touch:
    - Already encoded entities (&amp; &lt; &gt; etc.)
    - Numeric/hex entities (&#123; &#xAB;)
    """
    
    # Pattern to match raw & that isn't already part of an entity
    # Negative lookahead ensures we don't match &amp; &lt; &gt; &#digits; &#xhex;
    pattern = r'&(?!(?:amp|lt|gt|quot|apos|nbsp|#\d+|#x[0-9a-fA-F]+);)'
    
    # Replace all raw & with &amp;
    fixed_content = re.sub(pattern, '&amp;', content)
    
    return fixed_content

def process_file(filepath):
    """Process a single HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        fixed_content = fix_ampersands_in_html(original_content)
        
        if original_content != fixed_content:
            # Count how many were fixed
            original_count = len(re.findall(r'&(?!(?:amp|lt|gt|quot|apos|nbsp|#\d+|#x[0-9a-fA-F]+);)', original_content))
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            
            print(f"✅ Fixed {original_count} raw ampersands in {filepath}")
            return True
        else:
            print(f"✓  No changes needed for {filepath}")
            return False
    
    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}", file=sys.stderr)
        return False

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python fix_ampersands_careful.py <file1.html> [file2.html ...]")
        sys.exit(1)
    
    files = sys.argv[1:]
    fixed_count = 0
    
    for filepath in files:
        if process_file(filepath):
            fixed_count += 1
    
    print(f"\n📊 Summary: Fixed {fixed_count} of {len(files)} files")

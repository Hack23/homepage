#!/usr/bin/env python3
"""
HTML Locale Header Validator and Fixer
Validates and corrects lang attributes and og:locale in HTML files
"""

import os
import re
from pathlib import Path

# Language configurations
LANGUAGES = {
    'en': {'locale': 'en_US', 'name': 'English'},
    'sv': {'locale': 'sv_SE', 'name': 'Swedish'},
    'ko': {'locale': 'ko_KR', 'name': 'Korean'},
    'da': {'locale': 'da_DK', 'name': 'Danish'},
    'fi': {'locale': 'fi_FI', 'name': 'Finnish'},
    'no': {'locale': 'nb_NO', 'name': 'Norwegian'},
    'de': {'locale': 'de_DE', 'name': 'German'},
    'nl': {'locale': 'nl_NL', 'name': 'Dutch'},
    'fr': {'locale': 'fr_FR', 'name': 'French'},
    'es': {'locale': 'es_ES', 'name': 'Spanish'},
    'ar': {'locale': 'ar_SA', 'name': 'Arabic'},
    'he': {'locale': 'he_IL', 'name': 'Hebrew'},
    'ja': {'locale': 'ja_JP', 'name': 'Japanese'},
    'zh': {'locale': 'zh_CN', 'name': 'Chinese'},
}

def get_language_code(filename):
    """Extract language code from filename"""
    for lang in LANGUAGES.keys():
        if lang != 'en' and filename.endswith(f'_{lang}.html'):
            return lang
    return 'en'

def check_html_file(filepath):
    """Check if HTML file has correct lang and og:locale"""
    filename = os.path.basename(filepath)
    expected_lang = get_language_code(filename)
    expected_locale = LANGUAGES[expected_lang]['locale']
    
    issues = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check <html lang="">
        html_lang_match = re.search(r'<html\s+lang="([^"]+)"', content, re.IGNORECASE)
        if html_lang_match:
            actual_lang = html_lang_match.group(1)
            if actual_lang != expected_lang:
                issues.append(f'lang="{actual_lang}" (expected "{expected_lang}")')
        else:
            issues.append(f'Missing lang attribute')
        
        # Check og:locale
        og_locale_match = re.search(r'<meta\s+property="og:locale"\s+content="([^"]+)"', content, re.IGNORECASE)
        if og_locale_match:
            actual_locale = og_locale_match.group(1)
            if actual_locale != expected_locale:
                issues.append(f'og:locale="{actual_locale}" (expected "{expected_locale}")')
        else:
            # og:locale is optional, not an issue
            pass
        
        return issues
    
    except Exception as e:
        return [f'Error reading file: {e}']

def fix_html_file(filepath):
    """Fix lang and og:locale in HTML file"""
    filename = os.path.basename(filepath)
    expected_lang = get_language_code(filename)
    expected_locale = LANGUAGES[expected_lang]['locale']
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix <html lang="">
        content = re.sub(
            r'<html\s+lang="[^"]+"',
            f'<html lang="{expected_lang}"',
            content,
            flags=re.IGNORECASE
        )
        
        # Fix og:locale if it exists
        if re.search(r'<meta\s+property="og:locale"', content, re.IGNORECASE):
            content = re.sub(
                r'(<meta\s+property="og:locale"\s+content=")[^"]+"',
                rf'\1{expected_locale}"',
                content,
                flags=re.IGNORECASE
            )
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f'Error fixing {filepath}: {e}')
        return False

def main():
    print("Checking locale headers in all HTML files...")
    
    html_files = list(Path('.').glob('*.html'))
    total = len(html_files)
    issues_found = 0
    fixed = 0
    
    for filepath in sorted(html_files):
        issues = check_html_file(filepath)
        if issues:
            issues_found += 1
            print(f'⚠️  {filepath.name}: {", ".join(issues)}')
            if fix_html_file(filepath):
                fixed += 1
                print(f'   ✅ Fixed')
        else:
            print(f'✅ {filepath.name}')
    
    print(f'\n=== Summary ===')
    print(f'Total files: {total}')
    print(f'Issues found: {issues_found}')
    print(f'Fixed: {fixed}')
    print(f'OK: {total - issues_found}')

if __name__ == '__main__':
    main()

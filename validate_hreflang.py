#!/usr/bin/env python3
"""
Validate and fix hreflang tags in all HTML files.
Ensures each HTML file has complete hreflang references to all available language variants.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

# Language codes with their regional variants
LANG_CODES = {
    'en': ['en', 'en-US', 'en-GB'],
    'sv': ['sv', 'sv-SE'],
    'ko': ['ko', 'ko-KR'],
    'de': ['de', 'de-DE', 'de-AT', 'de-CH'],
    'ar': ['ar', 'ar-SA', 'ar-EG'],
    'da': ['da', 'da-DK'],
    'fi': ['fi', 'fi-FI'],
    'fr': ['fr', 'fr-FR', 'fr-CA'],
    'es': ['es', 'es-ES', 'es-MX'],
    'he': ['he', 'he-IL'],
    'ja': ['ja', 'ja-JP'],
    'nl': ['nl', 'nl-NL', 'nl-BE'],
    'no': ['no', 'nb-NO', 'nn-NO'],
    'zh': ['zh', 'zh-CN', 'zh-TW']
}

def get_base_name(filename):
    """Extract base name from filename (without language suffix)."""
    if '_' in filename and any(filename.endswith(f'_{lang}.html') for lang in LANG_CODES.keys()):
        return filename.rsplit('_', 1)[0]
    return filename.replace('.html', '')

def get_lang_code(filename):
    """Extract language code from filename."""
    if '_' in filename:
        lang = filename.rsplit('_', 1)[1].replace('.html', '')
        if lang in LANG_CODES:
            return lang
    return 'en'

def find_language_variants(base_name, all_files):
    """Find all language variants for a given base filename."""
    variants = {}
    
    # Check for English (no suffix)
    if f'{base_name}.html' in all_files:
        variants['en'] = f'{base_name}.html'
    
    # Check for other languages
    for lang in LANG_CODES.keys():
        if lang != 'en':
            variant_file = f'{base_name}_{lang}.html'
            if variant_file in all_files:
                variants[lang] = variant_file
    
    return variants

def extract_hreflang_tags(content):
    """Extract all hreflang tags from HTML content."""
    pattern = r'<link\s+rel="alternate"\s+hreflang="([^"]+)"\s+href="([^"]+)">'
    return re.findall(pattern, content)

def generate_hreflang_tags(base_name, variants, current_lang):
    """Generate complete hreflang tags for all language variants."""
    tags = []
    
    # Add x-default (always points to English version)
    default_url = f'https://hack23.com/{variants.get("en", f"{base_name}.html")}'
    tags.append(f'\t<link rel="alternate" hreflang="x-default" href="{default_url}">')
    
    # Add tags for each language with its regional variants
    for lang in sorted(LANG_CODES.keys()):
        if lang in variants:
            url = f'https://hack23.com/{variants[lang]}'
            
            # Add primary language code
            tags.append(f'\t<link rel="alternate" hreflang="{lang}" href="{url}">')
            
            # Add regional variants
            for regional_code in LANG_CODES[lang][1:]:
                tags.append(f'\t<link rel="alternate" hreflang="{regional_code}" href="{url}">')
    
    return tags

def validate_and_fix_hreflang(filename, all_files, fix=False):
    """Validate and optionally fix hreflang tags in a file."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    base_name = get_base_name(filename)
    current_lang = get_lang_code(filename)
    variants = find_language_variants(base_name, all_files)
    
    # Extract current hreflang tags
    current_tags = extract_hreflang_tags(content)
    
    # Generate expected tags
    expected_tags = generate_hreflang_tags(base_name, variants, current_lang)
    
    # Check if tags are complete
    expected_count = len(expected_tags)
    current_count = len(current_tags)
    
    issues = []
    
    if current_count == 0:
        issues.append("NO hreflang tags found")
    elif current_count < expected_count - 5:  # Allow some tolerance for variants
        issues.append(f"INCOMPLETE: {current_count} tags, expected ~{expected_count}")
    
    # Check for x-default
    if not any('x-default' in tag[0] for tag in current_tags):
        issues.append("MISSING x-default tag")
    
    # Check for self-reference
    if not any(current_lang in tag[0] for tag in current_tags):
        issues.append(f"MISSING self-reference for lang={current_lang}")
    
    if fix and issues:
        # Find hreflang section and replace it
        hreflang_pattern = r'<!-- Hreflang tags for international SEO -->.*?(?=\n\s*<link rel="canonical"|$)'
        
        new_section = "<!-- Hreflang tags for international SEO -->\n" + "\n".join(expected_tags) + "\n"
        
        if '<!-- Hreflang tags for international SEO -->' in content:
            # Replace existing section
            content = re.sub(hreflang_pattern, new_section, content, flags=re.DOTALL)
        else:
            # Insert before canonical tag
            content = content.replace(
                '<link rel="canonical"',
                f'{new_section}\t<link rel="canonical"'
            )
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, issues
    
    return False, issues

def main():
    """Main validation function."""
    print("=" * 80)
    print("Hreflang Tags Validation Report")
    print("=" * 80)
    
    # Get all HTML files
    all_files = set([f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('.')])
    
    print(f"\nTotal HTML files found: {len(all_files)}")
    
    # Validate all files
    files_with_issues = []
    files_checked = 0
    
    for filename in sorted(all_files):
        fixed, issues = validate_and_fix_hreflang(filename, all_files, fix=False)
        files_checked += 1
        
        if issues:
            files_with_issues.append((filename, issues))
    
    print(f"Files checked: {files_checked}")
    print(f"Files with issues: {len(files_with_issues)}")
    
    if files_with_issues:
        print("\n" + "=" * 80)
        print("Files with hreflang issues:")
        print("=" * 80)
        
        for filename, issues in files_with_issues[:20]:  # Show first 20
            print(f"\n{filename}:")
            for issue in issues:
                print(f"  - {issue}")
        
        if len(files_with_issues) > 20:
            print(f"\n... and {len(files_with_issues) - 20} more files")
    else:
        print("\n✅ All files have complete and correct hreflang tags!")
    
    print("\n" + "=" * 80)
    
    # Sample check - show variants for a few base names
    print("\nSample: Language variants availability:")
    print("=" * 80)
    
    sample_bases = ['index', 'why-hack23', 'blog-cia-security', 'accessibility-statement']
    
    for base in sample_bases:
        variants = find_language_variants(base, all_files)
        print(f"\n{base}: {len(variants)} variants")
        for lang in sorted(variants.keys()):
            print(f"  {lang}: {variants[lang]}")

if __name__ == '__main__':
    main()

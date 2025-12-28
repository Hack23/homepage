#!/usr/bin/env python3
"""
Sitemap Generator for Hack23 AB Homepage
Generates sitemap.xml with all HTML files and proper hreflang tags
"""

import os
from datetime import datetime
from pathlib import Path
import xml.etree.ElementTree as ET

# Language configurations
LANGUAGES = {
    'en': {'name': 'English', 'region': 'US'},
    'sv': {'name': 'Swedish', 'region': 'SE'},
    'ko': {'name': 'Korean', 'region': 'KR'},
    'da': {'name': 'Danish', 'region': 'DK'},
    'fi': {'name': 'Finnish', 'region': 'FI'},
    'no': {'name': 'Norwegian', 'region': 'NO'},
    'de': {'name': 'German', 'region': 'DE'},
    'nl': {'name': 'Dutch', 'region': 'NL'},
    'fr': {'name': 'French', 'region': 'FR'},
    'es': {'name': 'Spanish', 'region': 'ES'},
    'ar': {'name': 'Arabic', 'region': 'SA'},
    'he': {'name': 'Hebrew', 'region': 'IL'},
    'ja': {'name': 'Japanese', 'region': 'JP'},
    'zh': {'name': 'Chinese', 'region': 'CN'},
}

BASE_URL = 'https://hack23.com'

def get_all_html_files(base_dir='.'):
    """Get all HTML files in the repository root"""
    files = []
    for file in Path(base_dir).glob('*.html'):
        files.append(file.name)
    return sorted(files)

def get_base_name(filename):
    """Get base name without language suffix"""
    for lang in LANGUAGES.keys():
        if lang != 'en' and filename.endswith(f'_{lang}.html'):
            return filename.replace(f'_{lang}.html', '.html')
    return filename

def get_language_code(filename):
    """Extract language code from filename"""
    for lang in LANGUAGES.keys():
        if lang != 'en' and filename.endswith(f'_{lang}.html'):
            return lang
    return 'en'

def group_files_by_base():
    """Group files by their base name"""
    all_files = get_all_html_files()
    groups = {}
    
    for file in all_files:
        base = get_base_name(file)
        if base not in groups:
            groups[base] = []
        groups[base].append(file)
    
    return groups

def get_priority(filename):
    """Determine priority for sitemap based on file type"""
    if filename == 'index.html':
        return '1.0'
    elif filename in ['services.html', 'projects.html', 'why-hack23.html']:
        return '0.9'
    elif filename.startswith('blog-'):
        return '0.7'
    elif filename.startswith('discordian-') or filename.startswith('cia-'):
        return '0.8'
    else:
        return '0.6'

def get_changefreq(filename):
    """Determine change frequency based on file type"""
    if filename.startswith('blog-'):
        return 'monthly'
    elif filename == 'index.html':
        return 'weekly'
    else:
        return 'monthly'

def get_lastmod():
    """Get last modification date"""
    return datetime.now().strftime('%Y-%m-%d')

def generate_sitemap_xml():
    """Generate sitemap.xml with all HTML files and hreflang tags"""
    
    # Create XML structure
    urlset = ET.Element('urlset')
    urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    urlset.set('xmlns:xhtml', 'http://www.w3.org/1999/xhtml')
    
    # Group files by base name
    file_groups = group_files_by_base()
    
    # Sort by base name for consistency
    for base_name in sorted(file_groups.keys()):
        variants = file_groups[base_name]
        
        # Create URL entry for each variant
        for variant in sorted(variants):
            url_elem = ET.SubElement(urlset, 'url')
            
            # Add loc
            loc = ET.SubElement(url_elem, 'loc')
            loc.text = f'{BASE_URL}/{variant}'
            
            # Add lastmod
            lastmod = ET.SubElement(url_elem, 'lastmod')
            lastmod.text = get_lastmod()
            
            # Add changefreq
            changefreq = ET.SubElement(url_elem, 'changefreq')
            changefreq.text = get_changefreq(base_name)
            
            # Add priority
            priority = ET.SubElement(url_elem, 'priority')
            priority.text = get_priority(base_name)
            
            # Add hreflang tags for all variants
            for hreflang_variant in sorted(variants):
                lang_code = get_language_code(hreflang_variant)
                region = LANGUAGES[lang_code]['region']
                
                # Add primary language
                link = ET.SubElement(url_elem, '{http://www.w3.org/1999/xhtml}link')
                link.set('rel', 'alternate')
                link.set('hreflang', lang_code)
                link.set('href', f'{BASE_URL}/{hreflang_variant}')
                
                # Add language-region variant
                link_region = ET.SubElement(url_elem, '{http://www.w3.org/1999/xhtml}link')
                link_region.set('rel', 'alternate')
                link_region.set('hreflang', f'{lang_code}-{region}')
                link_region.set('href', f'{BASE_URL}/{hreflang_variant}')
            
            # Add x-default (English version)
            english_file = base_name if base_name in variants else variants[0]
            link_default = ET.SubElement(url_elem, '{http://www.w3.org/1999/xhtml}link')
            link_default.set('rel', 'alternate')
            link_default.set('hreflang', 'x-default')
            link_default.set('href', f'{BASE_URL}/{english_file}')
    
    # Create tree and write to file
    tree = ET.ElementTree(urlset)
    ET.indent(tree, space='  ')
    
    with open('sitemap.xml', 'wb') as f:
        f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        tree.write(f, encoding='utf-8', xml_declaration=False)
    
    return len(file_groups), sum(len(v) for v in file_groups.values())

def main():
    print("Generating sitemap.xml...")
    base_count, total_count = generate_sitemap_xml()
    print(f"✅ Generated sitemap.xml")
    print(f"   Base pages: {base_count}")
    print(f"   Total URLs: {total_count}")
    print(f"   Languages: {len(LANGUAGES)}")

if __name__ == '__main__':
    main()

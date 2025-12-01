#!/usr/bin/env python3
"""
Meta Description Audit Tool
Validates meta descriptions across all HTML files in the repository.
"""
import re
import glob
import json
from collections import defaultdict
from pathlib import Path

def extract_meta_description(html_file):
    """Extract meta description from HTML file."""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for meta description tag (case insensitive)
        match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', content, re.IGNORECASE)
        if not match:
            # Try alternative format
            match = re.search(r'<meta\s+content=["\']([^"\']+)["\']\s+name=["\']description["\']', content, re.IGNORECASE)
        
        return match.group(1) if match else None
    except Exception as e:
        print(f"Error reading {html_file}: {e}")
        return None

def extract_page_title(html_file):
    """Extract page title from HTML file."""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        match = re.search(r'<title>([^<]+)</title>', content, re.IGNORECASE)
        return match.group(1).strip() if match else "No title"
    except:
        return "Error reading title"

def categorize_file(filename):
    """Categorize file by type and language."""
    name = Path(filename).name
    
    # Detect language suffix
    lang = "en"
    for suffix in ["_sv", "_ko", "_da", "_fi", "_no", "_he", "_ar", "_de", "_es", "_fr", "_ja", "_nl", "_zh"]:
        if suffix in name:
            lang = suffix[1:]
            break
    
    # Detect file type
    if name.startswith("index"):
        category = "homepage"
    elif name.startswith("sitemap"):
        category = "sitemap"
    elif name.startswith("services"):
        category = "services"
    elif name.startswith("blog-"):
        category = "blog"
    elif name.startswith("discordian-"):
        category = "discordian"
    elif name.startswith("black-trigram"):
        category = "product-black-trigram"
    elif name.startswith("cia-"):
        category = "product-cia"
    elif name.startswith("why-hack23"):
        category = "why-hack23"
    elif name.startswith("industries-"):
        category = "industries"
    elif name.startswith("iso-"):
        category = "iso-guides"
    else:
        category = "other"
    
    return category, lang

def validate_descriptions():
    """Validate all meta descriptions."""
    results = {
        'missing': [],
        'too_short': [],
        'too_long': [],
        'duplicates': defaultdict(list),
        'good': [],
        'by_category': defaultdict(lambda: {'total': 0, 'missing': 0, 'issues': 0}),
        'by_language': defaultdict(lambda: {'total': 0, 'missing': 0, 'issues': 0})
    }
    
    html_files = sorted(glob.glob('*.html'))
    
    for html_file in html_files:
        desc = extract_meta_description(html_file)
        title = extract_page_title(html_file)
        category, lang = categorize_file(html_file)
        
        # Update category and language stats
        results['by_category'][category]['total'] += 1
        results['by_language'][lang]['total'] += 1
        
        if desc is None:
            results['missing'].append((html_file, title, category, lang))
            results['by_category'][category]['missing'] += 1
            results['by_language'][lang]['missing'] += 1
        elif len(desc) < 120:
            results['too_short'].append((html_file, len(desc), desc, category, lang))
            results['by_category'][category]['issues'] += 1
            results['by_language'][lang]['issues'] += 1
        elif len(desc) > 160:
            results['too_long'].append((html_file, len(desc), desc, category, lang))
            results['by_category'][category]['issues'] += 1
            results['by_language'][lang]['issues'] += 1
        else:
            results['good'].append((html_file, len(desc), desc, category, lang))
            results['duplicates'][desc].append((html_file, category, lang))
    
    # Filter actual duplicates
    results['duplicates'] = {k: v for k, v in results['duplicates'].items() if len(v) > 1}
    
    return results, html_files

def print_report(results, html_files):
    """Print comprehensive audit report."""
    print("=" * 80)
    print("META DESCRIPTION AUDIT REPORT")
    print("=" * 80)
    print(f"\nTotal HTML files analyzed: {len(html_files)}")
    print()
    
    # Summary statistics
    print("=" * 80)
    print("SUMMARY STATISTICS")
    print("=" * 80)
    print(f"✓ Good (140-160 chars):     {len(results['good'])}")
    print(f"⚠ Missing:                  {len(results['missing'])}")
    print(f"⚠ Too short (<120 chars):  {len(results['too_short'])}")
    print(f"⚠ Too long (>160 chars):   {len(results['too_long'])}")
    print(f"⚠ Duplicates:               {len(results['duplicates'])} unique descriptions used multiple times")
    print()
    
    # Percentage breakdown
    total = len(html_files)
    print(f"Success rate: {len(results['good']) / total * 100:.1f}%")
    print(f"Issues: {(len(results['missing']) + len(results['too_short']) + len(results['too_long'])) / total * 100:.1f}%")
    print()
    
    # By Category
    print("=" * 80)
    print("BY CATEGORY")
    print("=" * 80)
    for category, stats in sorted(results['by_category'].items()):
        print(f"\n{category.upper()}:")
        print(f"  Total: {stats['total']}")
        print(f"  Missing: {stats['missing']}")
        print(f"  Issues: {stats['issues']}")
        print(f"  Good: {stats['total'] - stats['missing'] - stats['issues']}")
    print()
    
    # By Language
    print("=" * 80)
    print("BY LANGUAGE")
    print("=" * 80)
    for lang, stats in sorted(results['by_language'].items()):
        print(f"\n{lang.upper()}:")
        print(f"  Total: {stats['total']}")
        print(f"  Missing: {stats['missing']}")
        print(f"  Issues: {stats['issues']}")
        print(f"  Good: {stats['total'] - stats['missing'] - stats['issues']}")
    print()
    
    # Missing meta descriptions
    if results['missing']:
        print("=" * 80)
        print("MISSING META DESCRIPTIONS")
        print("=" * 80)
        for file, title, category, lang in sorted(results['missing']):
            print(f"\n📄 {file}")
            print(f"   Title: {title}")
            print(f"   Category: {category} | Language: {lang}")
    
    # Too short descriptions
    if results['too_short']:
        print("\n" + "=" * 80)
        print("TOO SHORT (<120 chars)")
        print("=" * 80)
        for file, length, desc, category, lang in sorted(results['too_short'], key=lambda x: x[1]):
            print(f"\n📄 {file} ({length} chars)")
            print(f"   Category: {category} | Language: {lang}")
            print(f"   \"{desc}\"")
    
    # Too long descriptions
    if results['too_long']:
        print("\n" + "=" * 80)
        print("TOO LONG (>160 chars)")
        print("=" * 80)
        for file, length, desc, category, lang in sorted(results['too_long'], key=lambda x: x[1], reverse=True):
            print(f"\n📄 {file} ({length} chars)")
            print(f"   Category: {category} | Language: {lang}")
            print(f"   \"{desc[:80]}...\"")
    
    # Duplicate descriptions
    if results['duplicates']:
        print("\n" + "=" * 80)
        print("DUPLICATE DESCRIPTIONS")
        print("=" * 80)
        for desc, files in sorted(results['duplicates'].items(), key=lambda x: len(x[1]), reverse=True):
            print(f"\n🔄 Used by {len(files)} files:")
            for file, category, lang in sorted(files):
                print(f"   • {file} ({category}, {lang})")
            print(f"   Description: \"{desc[:100]}{'...' if len(desc) > 100 else ''}\"")
    
    # Good examples
    print("\n" + "=" * 80)
    print("GOOD EXAMPLES (140-160 chars)")
    print("=" * 80)
    print("\nShowing first 10 examples:")
    for file, length, desc, category, lang in results['good'][:10]:
        print(f"\n✓ {file} ({length} chars)")
        print(f"  \"{desc}\"")

def save_json_report(results, html_files):
    """Save detailed JSON report for programmatic access."""
    report = {
        'total_files': len(html_files),
        'summary': {
            'good': len(results['good']),
            'missing': len(results['missing']),
            'too_short': len(results['too_short']),
            'too_long': len(results['too_long']),
            'duplicates': len(results['duplicates'])
        },
        'by_category': dict(results['by_category']),
        'by_language': dict(results['by_language']),
        'details': {
            'missing': [{'file': f, 'title': t, 'category': c, 'language': l} 
                       for f, t, c, l in results['missing']],
            'too_short': [{'file': f, 'length': ln, 'description': d, 'category': c, 'language': l} 
                         for f, ln, d, c, l in results['too_short']],
            'too_long': [{'file': f, 'length': ln, 'description': d, 'category': c, 'language': l} 
                        for f, ln, d, c, l in results['too_long']],
            'duplicates': {desc: [{'file': f, 'category': c, 'language': l} for f, c, l in files]
                          for desc, files in results['duplicates'].items()}
        }
    }
    
    with open('meta_descriptions_audit.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print("\n" + "=" * 80)
    print("JSON report saved to: meta_descriptions_audit.json")
    print("=" * 80)

if __name__ == '__main__':
    print("\nStarting meta description audit...\n")
    results, html_files = validate_descriptions()
    print_report(results, html_files)
    save_json_report(results, html_files)
    print("\n✓ Audit complete!\n")

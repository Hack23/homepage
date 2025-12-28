#!/usr/bin/env python3
"""
Translation Status Analyzer
Analyzes all HTML files for a specific language and generates/updates the Translation-Status.md file
"""

import os
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Language configurations
LANGUAGES = {
    'sv': {'name': 'Swedish', 'flag': '🇸🇪', 'icon': '👑', 'market': 'Sweden'},
    'ko': {'name': 'Korean', 'flag': '🇰🇷', 'icon': '🏯', 'market': 'South Korea'},
    'da': {'name': 'Danish', 'flag': '🇩🇰', 'icon': '⚓', 'market': 'Denmark'},
    'fi': {'name': 'Finnish', 'flag': '🇫🇮', 'icon': '🦌', 'market': 'Finland'},
    'no': {'name': 'Norwegian', 'flag': '🇳🇴', 'icon': '⛷️', 'market': 'Norway'},
    'de': {'name': 'German', 'flag': '🇩🇪', 'icon': '🦅', 'market': 'Germany, Austria, Switzerland'},
    'nl': {'name': 'Dutch', 'flag': '🇳🇱', 'icon': '🌷', 'market': 'Netherlands, Belgium (Flemish)'},
    'fr': {'name': 'French', 'flag': '🇫🇷', 'icon': '🥐', 'market': 'France, French-speaking regions'},
    'es': {'name': 'Spanish', 'flag': '🇪🇸', 'icon': '🎭', 'market': 'Spain, Latin America'},
    'ar': {'name': 'Arabic', 'flag': '🇸🇦', 'icon': '🌙', 'market': 'MENA (Middle East & North Africa)', 'rtl': True},
    'he': {'name': 'Hebrew', 'flag': '🇮🇱', 'icon': '✡️', 'market': 'Israel', 'rtl': True},
    'ja': {'name': 'Japanese', 'flag': '🇯🇵', 'icon': '🗾', 'market': 'Japan'},
    'zh': {'name': 'Chinese', 'flag': '🇨🇳', 'icon': '🐉', 'market': 'China, Chinese-speaking regions'},
}

def get_all_base_html_files(base_dir='.'):
    """Get all base English HTML files (excluding translations)"""
    files = []
    for file in Path(base_dir).glob('*.html'):
        filename = file.name
        # Exclude translated files (those with language suffix)
        if not any(filename.endswith(f'_{lang}.html') for lang in LANGUAGES.keys()):
            files.append(filename)
    return sorted(files)

def get_translated_files(lang_code, base_dir='.'):
    """Get all translated HTML files for a specific language"""
    pattern = f'*_{lang_code}.html'
    files = [f.name for f in Path(base_dir).glob(pattern)]
    return sorted(files)

def categorize_files(files):
    """Categorize files by type"""
    categories = {
        'Blog Posts': [],
        'Core Pages': [],
        'ISMS Documentation': [],
        'ISMS Policy Files': [],
        'ISO 27001 Resources': [],
        'Industry Solutions': [],
        'Product Pages': [],
        'Other Pages': []
    }
    
    for file in files:
        if file.startswith('blog-'):
            categories['Blog Posts'].append(file)
        elif file.startswith('discordian-') and not file.startswith('discordian-ai-policy') and not file.startswith('discordian-info-sec-policy'):
            categories['ISMS Documentation'].append(file)
        elif file.startswith('discordian-ai-policy') or file.startswith('discordian-info-sec-policy'):
            categories['ISMS Policy Files'].append(file)
        elif file.startswith('iso-27001-'):
            categories['ISO 27001 Resources'].append(file)
        elif file.startswith('industries-'):
            categories['Industry Solutions'].append(file)
        elif any(file.startswith(prefix) for prefix in ['black-trigram', 'cia-', 'compliance-manager']):
            categories['Product Pages'].append(file)
        elif file in ['index.html', 'services.html', 'projects.html', 'blog.html', 
                      'why-hack23.html', 'sitemap.html', 'accessibility-statement.html']:
            categories['Core Pages'].append(file)
        else:
            categories['Other Pages'].append(file)
    
    return categories

def analyze_translation_quality(file_path):
    """
    Analyze the quality of a translation file
    Returns: 'fully_translated', 'mostly_translated', 'partially_translated', or 'needs_translation'
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract main content areas (paragraphs, headings, list items)
        # Exclude meta, script, style, and technical attributes
        body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL | re.IGNORECASE)
        if not body_match:
            return 'needs_translation'
        
        body_content = body_match.group(1)
        
        # Remove technical sections that legitimately have English
        body_content = re.sub(r'<script[^>]*>.*?</script>', '', body_content, flags=re.DOTALL | re.IGNORECASE)
        body_content = re.sub(r'<style[^>]*>.*?</style>', '', body_content, flags=re.DOTALL | re.IGNORECASE)
        body_content = re.sub(r'<code[^>]*>.*?</code>', '', body_content, flags=re.DOTALL | re.IGNORECASE)
        body_content = re.sub(r'<pre[^>]*>.*?</pre>', '', body_content, flags=re.DOTALL | re.IGNORECASE)
        
        # Extract visible text content from paragraphs and headings
        text_patterns = [
            r'<p[^>]*>(.*?)</p>',
            r'<h[1-6][^>]*>(.*?)</h[1-6]>',
            r'<li[^>]*>(.*?)</li>',
            r'<div[^>]*class="[^"]*card[^"]*"[^>]*>(.*?)</div>'
        ]
        
        visible_text = []
        for pattern in text_patterns:
            matches = re.findall(pattern, body_content, re.DOTALL | re.IGNORECASE)
            for match in matches:
                # Strip HTML tags from the matched content
                clean_text = re.sub(r'<[^>]+>', '', match)
                visible_text.append(clean_text.strip())
        
        combined_text = ' '.join(visible_text).lower()
        
        # Skip if no substantial text found
        if len(combined_text) < 100:
            return 'needs_translation'
        
        # Look for substantial English phrases (more specific)
        english_phrases = [
            r'\bour (services|products|solutions|approach|team)\b',
            r'\bwe (provide|offer|deliver|ensure|help)\b',
            r'\bcontact us\b',
            r'\blearn more about\b',
            r'\bget started with\b',
            r'\bread more about (our|the)\b',
            r'\bclick here to\b',
            r'\bwhy choose (us|our)\b',
            r'\b(comprehensive|innovative|cutting-edge) (solution|approach)\b',
            r'\bour commitment to\b',
            r'\b(security|privacy) (is|are) (our|a) (priority|commitment)\b'
        ]
        
        english_matches = 0
        for phrase in english_phrases:
            if re.search(phrase, combined_text):
                english_matches += 1
        
        # Also check for high concentration of common English words
        common_english_words = ['the', 'and', 'are', 'with', 'for', 'this', 'that', 'your', 'our']
        english_word_count = sum(1 for word in common_english_words if len(re.findall(r'\b' + word + r'\b', combined_text)) > 3)
        
        # Classification
        if english_matches == 0 and english_word_count < 2:
            return 'fully_translated'
        elif english_matches <= 2 or english_word_count < 4:
            return 'mostly_translated'
        elif english_matches <= 5 or english_word_count < 6:
            return 'partially_translated'
        else:
            return 'needs_translation'
            
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return 'unknown'

def calculate_quality_score(quality_distribution):
    """Calculate overall quality score"""
    total = sum(quality_distribution.values())
    if total == 0:
        return 0.0
    
    fully = quality_distribution.get('fully_translated', 0)
    mostly = quality_distribution.get('mostly_translated', 0)
    
    # Quality score: fully translated = 1.0, mostly = 0.8
    score = (fully + (mostly * 0.8)) / total * 100
    return round(score, 1)

def generate_status_report(lang_code, base_dir='.'):
    """Generate complete status report for a language"""
    
    if lang_code not in LANGUAGES:
        print(f"Error: Unknown language code '{lang_code}'")
        return None
    
    lang_info = LANGUAGES[lang_code]
    
    # Get all files
    base_files = get_all_base_html_files(base_dir)
    translated_files = get_translated_files(lang_code, base_dir)
    
    # Calculate coverage
    total_base = len(base_files)
    total_translated = len(translated_files)
    completion_pct = round((total_translated / total_base * 100), 2) if total_base > 0 else 0
    
    # Analyze translation quality
    quality_distribution = defaultdict(int)
    for trans_file in translated_files:
        file_path = os.path.join(base_dir, trans_file)
        quality = analyze_translation_quality(file_path)
        quality_distribution[quality] += 1
    
    quality_score = calculate_quality_score(quality_distribution)
    
    # Categorize files
    base_categories = categorize_files(base_files)
    trans_categories = categorize_files(translated_files)
    
    # Find missing files
    translated_base_names = {f.replace(f'_{lang_code}.html', '.html') for f in translated_files}
    missing_files = sorted([f for f in base_files if f not in translated_base_names])
    
    return {
        'lang_code': lang_code,
        'lang_info': lang_info,
        'total_base': total_base,
        'total_translated': total_translated,
        'completion_pct': completion_pct,
        'quality_distribution': dict(quality_distribution),
        'quality_score': quality_score,
        'base_categories': base_categories,
        'trans_categories': trans_categories,
        'missing_files': missing_files,
        'translated_files': translated_files
    }

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python analyze_translation_status.py <language_code>")
        print(f"Available languages: {', '.join(LANGUAGES.keys())}")
        sys.exit(1)
    
    lang_code = sys.argv[1]
    
    print(f"Analyzing {LANGUAGES.get(lang_code, {}).get('name', lang_code)} translation status...")
    
    report = generate_status_report(lang_code)
    
    if report:
        print(f"\n=== {report['lang_info']['name']} Translation Status ===")
        print(f"Files: {report['total_translated']}/{report['total_base']} ({report['completion_pct']}%)")
        print(f"Quality Score: {report['quality_score']}%")
        print(f"\nQuality Distribution:")
        for quality, count in report['quality_distribution'].items():
            print(f"  {quality}: {count}")
        print(f"\nMissing files: {len(report['missing_files'])}")
        
        return report
    
    return None

if __name__ == '__main__':
    main()

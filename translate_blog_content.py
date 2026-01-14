#!/usr/bin/env python3
"""
Translate blog HTML body content from English/Swedish to target languages.
Uses language-specific translation guides for terminology consistency.
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# Language configuration - based on BLOG_TRANSLATION_STATUS.md
LANGUAGE_CONFIGS = {
    # Languages with English body content
    'ar': {'name': 'Arabic', 'source': 'en', 'rtl': True},
    'es': {'name': 'Spanish', 'source': 'en', 'rtl': False},
    'he': {'name': 'Hebrew', 'source': 'en', 'rtl': True},
    'ja': {'name': 'Japanese', 'source': 'en', 'rtl': False},
    'ko': {'name': 'Korean', 'source': 'en', 'rtl': False},
    'zh': {'name': 'Chinese', 'source': 'en', 'rtl': False},
    
    # Languages with Swedish body content (Nordic mixing issue)
    'da': {'name': 'Danish', 'source': 'sv', 'rtl': False},
    'fi': {'name': 'Finnish', 'source': 'sv', 'rtl': False},
    'no': {'name': 'Norwegian', 'source': 'sv', 'rtl': False},
}

# Key terminology for each language (from translation guides)
TERMINOLOGY = {
    'ko': {
        'Cybersecurity': '사이버보안',
        'Information Security': '정보보안',
        'Compliance': '규정 준수',
        'Risk': '위험',
        'Architecture': '아키텍처',
        'System': '시스템',
        'Security': '보안',
        'Data': '데이터',
        'When democracies hide in darkness': '민주주의가 어둠 속에 숨을 때',
        'transparency becomes revolution': '투명성은 혁명이 됩니다',
        'The Pattern Reveals Itself': '패턴이 스스로를 드러낸다',
        'The Five Sacred Data Layers': '다섯 개의 신성한 데이터 계층',
        'Presentation Layer': '프레젠테이션 계층',
        'Service Layer': '서비스 계층',
        'Domain Layer': '도메인 계층',
        'Data Access Layer': '데이터 액세스 계층',
        'Integration & Analytics': '통합 및 분석',
    },
    # Add more language terminologies as needed
}

def extract_body_content(html_content: str) -> Tuple[str, str, str]:
    """
    Extract the body content section from HTML file.
    Returns: (before_body, body_content, after_body)
    """
    # Find the main content section (after <main> tag)
    main_start = html_content.find('<main>')
    if main_start == -1:
        raise ValueError("No <main> tag found")
    
    main_end = html_content.find('</main>')
    if main_end == -1:
        raise ValueError("No </main> closing tag found")
    
    before_body = html_content[:main_start + 6]  # Include <main> tag
    body_content = html_content[main_start + 6:main_end]
    after_body = html_content[main_end:]
    
    return before_body, body_content, after_body

def needs_translation(file_path: Path, lang_code: str, config: Dict) -> bool:
    """Check if file needs translation based on content."""
    try:
        content = file_path.read_text(encoding='utf-8')
        
        # Check for English markers
        if config['source'] == 'en':
            return 'When democracies hide in darkness' in content
        # Check for Swedish markers
        elif config['source'] == 'sv':
            return 'När demokratier' in content or 'Mönstret Avslöjar Sig' in content
        
        return False
    except Exception as e:
        print(f"Error checking {file_path}: {e}")
        return False

def list_files_needing_translation(blog_dir: Path) -> Dict[str, List[Path]]:
    """List all blog files that need translation, grouped by language."""
    files_by_lang = {}
    
    for lang_code, config in LANGUAGE_CONFIGS.items():
        pattern = f"blog-*_{lang_code}.html"
        matching_files = list(blog_dir.glob(pattern))
        
        files_needing_translation = [
            f for f in matching_files 
            if needs_translation(f, lang_code, config)
        ]
        
        if files_needing_translation:
            files_by_lang[lang_code] = files_needing_translation
    
    return files_by_lang

def generate_translation_notice(lang_code: str, lang_name: str, english_url: str) -> str:
    """Generate a translation notice to add at the top of the translated content."""
    notices = {
        'ko': f'''
    <div class="translation-notice" style="background-color: #fff3cd; border: 1px solid #ffc107; padding: 1rem; margin: 1rem 0; border-radius: 0.25rem;">
      <p><strong>📝 번역 주의사항:</strong> 이 페이지는 AI 번역 지원을 통해 한국어로 번역되었습니다. 원문(영어)은 <a href="{english_url}">여기</a>에서 확인하실 수 있습니다.</p>
    </div>''',
        'ar': f'''
    <div class="translation-notice" style="background-color: #fff3cd; border: 1px solid #ffc107; padding: 1rem; margin: 1rem 0; border-radius: 0.25rem;">
      <p><strong>📝 ملاحظة الترجمة:</strong> تمت ترجمة هذه الصفحة إلى العربية بمساعدة الذكاء الاصطناعي. يمكن العثور على النص الأصلي (بالإنجليزية) <a href="{english_url}">هنا</a>.</p>
    </div>''',
        'ja': f'''
    <div class="translation-notice" style="background-color: #fff3cd; border: 1px solid #ffc107; padding: 1rem; margin: 1rem 0; border-radius: 0.25rem;">
      <p><strong>📝 翻訳について:</strong> このページはAI翻訳支援により日本語に翻訳されています。原文(英語)は<a href="{english_url}">こちら</a>でご覧いただけます。</p>
    </div>''',
        'zh': f'''
    <div class="translation-notice" style="background-color: #fff3cd; border: 1px solid #ffc107; padding: 1rem; margin: 1rem 0; border-radius: 0.25rem;">
      <p><strong>📝 翻译说明:</strong> 本页面通过AI翻译辅助翻译成中文。原文(英文)请见<a href="{english_url}">此处</a>。</p>
    </div>''',
    }
    
    return notices.get(lang_code, f'''
    <div class="translation-notice" style="background-color: #fff3cd; border: 1px solid #ffc107; padding: 1rem; margin: 1rem 0; border-radius: 0.25rem;">
      <p><strong>📝 Translation Notice:</strong> This page has been translated to {lang_name} with AI translation assistance. Original (English) can be found <a href="{english_url}">here</a>.</p>
    </div>''')

def main():
    """Main execution function."""
    blog_dir = Path('/home/runner/work/homepage/homepage')
    
    print("🔍 Scanning for blog files needing translation...")
    files_by_lang = list_files_needing_translation(blog_dir)
    
    if not files_by_lang:
        print("✅ No files need translation!")
        return 0
    
    print("\n📊 Translation Status:\n")
    total_files = 0
    for lang_code, files in sorted(files_by_lang.items()):
        config = LANGUAGE_CONFIGS[lang_code]
        print(f"{config['name']} ({lang_code}): {len(files)} files need translation")
        total_files += len(files)
    
    print(f"\n📈 Total: {total_files} files need translation across {len(files_by_lang)} languages")
    
    # Detailed file list
    print("\n📁 Detailed file list:")
    for lang_code, files in sorted(files_by_lang.items()):
        config = LANGUAGE_CONFIGS[lang_code]
        print(f"\n{config['name']} ({lang_code}):")
        for file_path in sorted(files):
            print(f"  - {file_path.name}")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())

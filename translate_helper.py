#!/usr/bin/env python3
"""
Helper to extract English content from source file for manual translation.
"""

import sys

# Read the English source
with open('/home/runner/work/homepage/homepage/blog-cia-osint-intelligence.html', 'r', encoding='utf-8') as f:
    english_content = f.read()

# Read the Chinese file
with open('/home/runner/work/homepage/homepage/blog-cia-osint-intelligence_zh.html', 'r', encoding='utf-8') as f:
    chinese_content = f.read()

# Count English vs Chinese words
english_words = len([w for w in english_content.split() if w.strip()])
chinese_chars = len([c for c in chinese_content if '\u4e00' <= c <= '\u9fff'])

print(f"English source: {english_words} words")
print(f"Chinese file: {chinese_chars} Chinese characters")
print(f"\nTranslation needed!")

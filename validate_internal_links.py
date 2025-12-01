#!/usr/bin/env python3
"""
Comprehensive Internal Link Validator for Hack23 Homepage
Validates ALL internal links across 145+ HTML files in 14 languages
"""
import re
import sys
import glob
from pathlib import Path
from collections import defaultdict
from urllib.parse import urlparse, unquote
import json

class LinkValidator:
    def __init__(self, root_dir="."):
        self.root_dir = Path(root_dir)
        self.broken_links = defaultdict(list)
        self.all_pages = set()
        self.incoming_links = defaultdict(list)
        self.link_types = defaultdict(int)
        
    def normalize_link(self, link, source_file):
        """
        Normalize link to a consistent format for validation.
        Handles:
        - Relative links: page.html
        - Root-relative links: /page.html
        - Absolute links: https://hack23.com/page.html
        - Anchors: #section (skip)
        - External links (skip)
        - Protocol links: mailto:, tel:, javascript: (skip)
        """
        # Skip empty links
        if not link or link.startswith('#'):
            return None
        
        # Skip protocol links (mailto:, tel:, javascript:, etc.)
        if ':' in link and not link.startswith('http'):
            return None
            
        # Skip external links (not hack23.com)
        if link.startswith('http'):
            parsed = urlparse(link)
            if 'hack23.com' not in parsed.netloc:
                return None
            # Convert absolute hack23.com links to relative
            link = parsed.path.lstrip('/')
        
        # Remove leading slash for root-relative links
        if link.startswith('/'):
            link = link.lstrip('/')
        
        # URL decode
        link = unquote(link)
        
        # Remove query strings and fragments
        if '?' in link:
            link = link.split('?')[0]
        if '#' in link:
            link = link.split('#')[0]
            
        # Skip if empty after processing
        if not link:
            return None
            
        return link
    
    def extract_links_from_file(self, html_file):
        """Extract all href links from an HTML file, excluding code examples."""
        try:
            with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {html_file}: {e}")
            return []
        
        # Remove code examples to avoid false positives
        # Remove content within <pre>, <code>, and <!-- comments -->
        content_clean = re.sub(r'<pre[^>]*>.*?</pre>', '', content, flags=re.DOTALL | re.IGNORECASE)
        content_clean = re.sub(r'<code[^>]*>.*?</code>', '', content_clean, flags=re.DOTALL | re.IGNORECASE)
        content_clean = re.sub(r'<!--.*?-->', '', content_clean, flags=re.DOTALL)
        
        # Find all href attributes
        # Match href="..." and href='...'
        pattern = r'href=["\']([^"\']+)["\']'
        matches = re.findall(pattern, content_clean)
        
        return matches
    
    def validate_links(self):
        """Main validation logic - extract and validate all links."""
        # Get all HTML files
        html_files = list(self.root_dir.glob('*.html'))
        self.all_pages = {f.name for f in html_files}
        
        print(f"🔍 Found {len(html_files)} HTML files to validate")
        print(f"📂 Pages: {sorted(self.all_pages)[:10]}... (showing first 10)")
        print()
        
        # Process each file
        for html_file in html_files:
            source = html_file.name
            links = self.extract_links_from_file(html_file)
            
            for raw_link in links:
                # Normalize the link
                normalized = self.normalize_link(raw_link, source)
                
                if normalized is None:
                    continue
                
                # Track link type
                if raw_link.startswith('http'):
                    self.link_types['absolute'] += 1
                elif raw_link.startswith('/'):
                    self.link_types['root_relative'] += 1
                else:
                    self.link_types['relative'] += 1
                
                # Check if target exists
                target_path = self.root_dir / normalized
                
                if target_path.exists() and target_path.is_file():
                    # Valid link - track incoming link
                    self.incoming_links[normalized].append(source)
                else:
                    # Broken link
                    self.broken_links[source].append({
                        'raw': raw_link,
                        'normalized': normalized,
                        'reason': 'File not found'
                    })
    
    def find_orphaned_pages(self):
        """Find pages with no incoming links."""
        orphaned = []
        
        for page in self.all_pages:
            # Skip index pages and sitemap - they're entry points
            if page.startswith('index') or page.startswith('sitemap'):
                continue
            
            if page not in self.incoming_links:
                orphaned.append(page)
        
        return sorted(orphaned)
    
    def find_low_linked_pages(self, threshold=3):
        """Find pages with very few incoming links."""
        low_linked = []
        
        for page in self.all_pages:
            # Skip entry point pages
            if page.startswith('index') or page.startswith('sitemap'):
                continue
            
            count = len(self.incoming_links.get(page, []))
            if 0 < count < threshold:
                low_linked.append((page, count))
        
        return sorted(low_linked, key=lambda x: x[1])
    
    def generate_report(self):
        """Generate comprehensive validation report."""
        print("=" * 80)
        print("🔗 INTERNAL LINK VALIDATION REPORT")
        print("=" * 80)
        print()
        
        # Summary statistics
        print("📊 SUMMARY STATISTICS")
        print("-" * 80)
        print(f"Total HTML pages:        {len(self.all_pages)}")
        print(f"Total internal links:    {sum(self.link_types.values())}")
        print(f"  - Relative links:      {self.link_types['relative']}")
        print(f"  - Root-relative links: {self.link_types['root_relative']}")
        print(f"  - Absolute links:      {self.link_types['absolute']}")
        print(f"Broken links found:      {sum(len(v) for v in self.broken_links.values())}")
        print(f"Pages with broken links: {len(self.broken_links)}")
        print()
        
        # Broken links section
        if self.broken_links:
            print("🚨 BROKEN LINKS")
            print("-" * 80)
            for source, links in sorted(self.broken_links.items()):
                print(f"\n📄 {source} ({len(links)} broken link{'s' if len(links) > 1 else ''}):")
                for link in links:
                    print(f"  ❌ {link['raw']}")
                    print(f"     → Normalized: {link['normalized']}")
                    print(f"     → Reason: {link['reason']}")
        else:
            print("✅ NO BROKEN LINKS FOUND!")
        print()
        
        # Orphaned pages
        orphaned = self.find_orphaned_pages()
        if orphaned:
            print("🏝️  ORPHANED PAGES (No Incoming Links)")
            print("-" * 80)
            print(f"Found {len(orphaned)} orphaned page(s):")
            for page in orphaned:
                print(f"  📄 {page}")
        else:
            print("✅ NO ORPHANED PAGES FOUND!")
        print()
        
        # Low-linked pages
        low_linked = self.find_low_linked_pages(threshold=3)
        if low_linked:
            print("⚠️  PAGES WITH FEW INCOMING LINKS (< 3)")
            print("-" * 80)
            print(f"Found {len(low_linked)} page(s) with limited discoverability:")
            for page, count in low_linked:
                print(f"  📄 {page}: {count} incoming link(s)")
                print(f"     From: {', '.join(self.incoming_links[page][:3])}")
        print()
        
        # Top linked pages
        print("🌟 TOP 10 MOST LINKED PAGES")
        print("-" * 80)
        top_pages = sorted(
            [(page, len(sources)) for page, sources in self.incoming_links.items()],
            key=lambda x: x[1],
            reverse=True
        )[:10]
        for page, count in top_pages:
            print(f"  📄 {page}: {count} incoming link(s)")
        print()
        
        # Language coverage check
        print("🌍 LANGUAGE VARIANT COVERAGE")
        print("-" * 80)
        languages = ['ar', 'da', 'de', 'es', 'fi', 'fr', 'he', 'ja', 'ko', 'nl', 'no', 'sv', 'zh']
        base_pages = ['index', 'sitemap', 'services', 'why-hack23']
        
        for base in base_pages:
            print(f"\n{base}.html variants:")
            print(f"  ✅ {base}.html (English)")
            for lang in languages:
                variant = f"{base}_{lang}.html"
                if variant in self.all_pages:
                    print(f"  ✅ {variant}")
                else:
                    print(f"  ❌ {variant} - MISSING")
        print()
        
        # Export detailed JSON report
        self.export_json_report()
        
        # Return validation result - only fail on broken links
        has_broken_links = bool(self.broken_links)
        return not has_broken_links
    
    def export_json_report(self):
        """Export detailed report as JSON for further analysis."""
        report = {
            'summary': {
                'total_pages': len(self.all_pages),
                'total_links': sum(self.link_types.values()),
                'broken_links': sum(len(v) for v in self.broken_links.values()),
                'pages_with_broken_links': len(self.broken_links),
                'link_types': self.link_types
            },
            'broken_links': {
                source: [{'raw': l['raw'], 'normalized': l['normalized']} 
                        for l in links]
                for source, links in self.broken_links.items()
            },
            'orphaned_pages': self.find_orphaned_pages(),
            'low_linked_pages': {page: count for page, count in self.find_low_linked_pages()},
            'all_pages': sorted(self.all_pages),
            'incoming_links': {
                page: sources for page, sources in self.incoming_links.items()
            }
        }
        
        report_file = self.root_dir / 'link_validation_report.json'
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"📊 Detailed JSON report saved to: {report_file}")

def main():
    """Main entry point."""
    print("🚀 Starting Internal Link Validation")
    print("=" * 80)
    print()
    
    validator = LinkValidator(".")
    validator.validate_links()
    success = validator.generate_report()
    
    print("=" * 80)
    if success:
        print("✅ VALIDATION PASSED - All links are valid!")
        return 0
    else:
        print("❌ VALIDATION FAILED - Issues found above")
        return 1

if __name__ == '__main__':
    sys.exit(main())

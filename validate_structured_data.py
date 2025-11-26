#!/usr/bin/env python3
"""
Structured Data Validation Script for Hack23 AB Website

This script validates all structured data (Schema.org JSON-LD) across the website:
- Checks for duplicate schema types on the same page
- Validates JSON syntax
- Checks required properties for each schema type
- Validates breadcrumb implementations
- Checks canonical and hreflang tags

Usage: python3 validate_structured_data.py
"""

import json
import re
import sys
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple, Set

class StructuredDataValidator:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.stats = {
            'files_checked': 0,
            'schemas_found': 0,
            'duplicates_found': 0,
            'canonical_issues': 0,
            'hreflang_issues': 0
        }
        
        # Required properties for common schema types
        self.required_properties = {
            'FAQPage': ['mainEntity'],
            'BreadcrumbList': ['itemListElement'],
            'Organization': ['name', 'url'],
            'BlogPosting': ['headline', 'datePublished', 'author'],
            'WebPage': ['name', 'url'],
            'Service': ['name', 'provider'],
            'Person': ['name']
        }
    
    def find_html_files(self, directory: Path) -> List[Path]:
        """Find all HTML files in the directory."""
        return list(directory.glob('*.html'))
    
    def extract_json_ld(self, html_content: str) -> List[Dict]:
        """Extract all JSON-LD structured data from HTML."""
        pattern = r'<script\s+type=["\']\s*application/ld\+json\s*["\']>\s*(\{.*?\})\s*</script>'
        matches = re.findall(pattern, html_content, re.DOTALL | re.IGNORECASE)
        
        json_objects = []
        for match in matches:
            try:
                data = json.loads(match)
                json_objects.append(data)
            except json.JSONDecodeError as e:
                self.errors.append(f"Invalid JSON-LD: {str(e)}")
        
        return json_objects
    
    def get_schema_types(self, schema: Dict) -> List[str]:
        """Extract all @type values from a schema object."""
        types = []
        
        def extract_types(obj):
            if isinstance(obj, dict):
                if '@type' in obj:
                    type_val = obj['@type']
                    if isinstance(type_val, str):
                        types.append(type_val)
                    elif isinstance(type_val, list):
                        types.extend(type_val)
                
                # Check @graph array
                if '@graph' in obj and isinstance(obj['@graph'], list):
                    for item in obj['@graph']:
                        extract_types(item)
                
                # Recursively check other properties
                for value in obj.values():
                    if isinstance(value, (dict, list)):
                        extract_types(value)
            
            elif isinstance(obj, list):
                for item in obj:
                    extract_types(item)
        
        extract_types(schema)
        return types
    
    def check_duplicate_schemas(self, file_path: Path, schemas: List[Dict]) -> List[str]:
        """Check for duplicate schema types in the same file."""
        duplicates = []
        
        # Count occurrences of each schema type across all JSON-LD blocks
        type_counts = defaultdict(int)
        
        for schema in schemas:
            types = self.get_schema_types(schema)
            for schema_type in types:
                type_counts[schema_type] += 1
        
        # Report duplicates
        for schema_type, count in type_counts.items():
            if count > 1:
                duplicates.append(f"Duplicate '{schema_type}' schema found {count} times")
                self.stats['duplicates_found'] += 1
        
        return duplicates
    
    def validate_required_properties(self, schema: Dict, schema_type: str) -> List[str]:
        """Validate that required properties are present."""
        issues = []
        
        if schema_type in self.required_properties:
            required = self.required_properties[schema_type]
            
            for prop in required:
                if prop not in schema:
                    issues.append(f"{schema_type} missing required property: {prop}")
        
        return issues
    
    def check_canonical_tag(self, file_path: Path, html_content: str) -> List[str]:
        """Check canonical tag implementation."""
        issues = []
        
        canonical_pattern = r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']'
        matches = re.findall(canonical_pattern, html_content, re.IGNORECASE)
        
        if not matches:
            # Only warn for main content pages, not all pages need canonical
            if file_path.name.startswith('index') or file_path.name.startswith('blog-'):
                issues.append("No canonical tag found")
        elif len(matches) > 1:
            issues.append(f"Multiple canonical tags found: {len(matches)}")
            self.stats['canonical_issues'] += 1
        
        return issues
    
    def check_hreflang_tags(self, file_path: Path, html_content: str) -> List[str]:
        """Check hreflang implementation for multilingual pages."""
        issues = []
        
        hreflang_pattern = r'<link\s+rel=["\']alternate["\']\s+hreflang=["\'](.*?)["\']\s+href=["\'](.*?)["\']'
        matches = re.findall(hreflang_pattern, html_content, re.IGNORECASE)
        
        if file_path.name.startswith('index'):
            if not matches:
                issues.append("Homepage should have hreflang tags for multilingual support")
                self.stats['hreflang_issues'] += 1
            else:
                # Check for x-default
                langs = [lang for lang, url in matches]
                if 'x-default' not in langs:
                    issues.append("Missing x-default hreflang tag")
        
        return issues
    
    def validate_breadcrumb(self, schema: Dict) -> List[str]:
        """Validate BreadcrumbList structure."""
        issues = []
        
        if schema.get('@type') == 'BreadcrumbList':
            items = schema.get('itemListElement', [])
            
            if not items:
                issues.append("BreadcrumbList has no items")
            else:
                # Check positions are sequential
                positions = []
                for item in items:
                    if 'position' in item:
                        positions.append(item['position'])
                    if 'name' not in item:
                        issues.append("BreadcrumbList item missing 'name'")
                    if 'item' not in item and item != items[-1]:  # Last item can omit 'item'
                        issues.append("BreadcrumbList item missing 'item' URL")
                
                if positions != list(range(1, len(positions) + 1)):
                    issues.append(f"BreadcrumbList positions not sequential: {positions}")
        
        return issues
    
    def validate_file(self, file_path: Path) -> Dict:
        """Validate a single HTML file."""
        result = {
            'file': file_path.name,
            'schemas': [],
            'errors': [],
            'warnings': [],
            'duplicates': []
        }
        
        try:
            html_content = file_path.read_text(encoding='utf-8')
            self.stats['files_checked'] += 1
            
            # Extract and validate JSON-LD
            schemas = self.extract_json_ld(html_content)
            self.stats['schemas_found'] += len(schemas)
            
            # Check for duplicate schemas
            duplicates = self.check_duplicate_schemas(file_path, schemas)
            result['duplicates'] = duplicates
            
            # Validate each schema
            for schema in schemas:
                schema_types = self.get_schema_types(schema)
                
                for schema_type in schema_types:
                    # Check required properties
                    property_issues = self.validate_required_properties(schema, schema_type)
                    result['errors'].extend(property_issues)
                    
                    # Special validation for breadcrumbs
                    if schema_type == 'BreadcrumbList':
                        breadcrumb_issues = self.validate_breadcrumb(schema)
                        result['warnings'].extend(breadcrumb_issues)
            
            # Check canonical and hreflang tags
            canonical_issues = self.check_canonical_tag(file_path, html_content)
            result['warnings'].extend(canonical_issues)
            
            hreflang_issues = self.check_hreflang_tags(file_path, html_content)
            result['warnings'].extend(hreflang_issues)
            
            result['schemas'] = [self.get_schema_types(s) for s in schemas]
            
        except Exception as e:
            result['errors'].append(f"Error reading file: {str(e)}")
        
        return result
    
    def print_report(self, results: List[Dict]):
        """Print validation report."""
        print("\n" + "="*80)
        print("STRUCTURED DATA VALIDATION REPORT")
        print("="*80)
        
        # Summary
        print(f"\n📊 SUMMARY")
        print(f"   Files checked: {self.stats['files_checked']}")
        print(f"   Schemas found: {self.stats['schemas_found']}")
        print(f"   Duplicates found: {self.stats['duplicates_found']}")
        print(f"   Canonical issues: {self.stats['canonical_issues']}")
        print(f"   Hreflang issues: {self.stats['hreflang_issues']}")
        
        # Files with issues
        files_with_errors = [r for r in results if r['errors'] or r['duplicates']]
        files_with_warnings = [r for r in results if r['warnings']]
        
        if files_with_errors:
            print(f"\n❌ FILES WITH ERRORS ({len(files_with_errors)}):")
            for result in files_with_errors:
                print(f"\n   📄 {result['file']}")
                
                if result['duplicates']:
                    print(f"      🔁 DUPLICATES:")
                    for dup in result['duplicates']:
                        print(f"         - {dup}")
                
                if result['errors']:
                    print(f"      ❌ ERRORS:")
                    for error in result['errors']:
                        print(f"         - {error}")
        
        if files_with_warnings:
            print(f"\n⚠️  FILES WITH WARNINGS ({len(files_with_warnings)}):")
            for result in files_with_warnings:
                if result['warnings']:
                    print(f"\n   📄 {result['file']}")
                    for warning in result['warnings']:
                        print(f"      - {warning}")
        
        # Success summary
        clean_files = [r for r in results if not r['errors'] and not r['duplicates'] and not r['warnings']]
        if clean_files:
            print(f"\n✅ CLEAN FILES ({len(clean_files)}):")
            for result in clean_files[:10]:  # Show first 10
                schemas = [t for types in result['schemas'] for t in types]
                unique_schemas = set(schemas)
                print(f"   ✓ {result['file']} - {len(unique_schemas)} schema types")
            if len(clean_files) > 10:
                print(f"   ... and {len(clean_files) - 10} more")
        
        print("\n" + "="*80)
        
        # Exit code
        if files_with_errors:
            print("❌ VALIDATION FAILED - Please fix errors above")
            return 1
        elif files_with_warnings:
            print("⚠️  VALIDATION PASSED WITH WARNINGS")
            return 0
        else:
            print("✅ VALIDATION PASSED - All structured data is valid!")
            return 0

def main():
    """Main entry point."""
    validator = StructuredDataValidator()
    
    # Get current directory
    current_dir = Path.cwd()
    
    print(f"🔍 Scanning HTML files in: {current_dir}")
    
    # Find all HTML files
    html_files = validator.find_html_files(current_dir)
    
    if not html_files:
        print("❌ No HTML files found!")
        return 1
    
    print(f"📝 Found {len(html_files)} HTML files to validate\n")
    
    # Validate each file
    results = []
    for file_path in sorted(html_files):
        result = validator.validate_file(file_path)
        results.append(result)
    
    # Print report
    exit_code = validator.print_report(results)
    
    return exit_code

if __name__ == '__main__':
    sys.exit(main())

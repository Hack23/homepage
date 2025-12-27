#!/usr/bin/env python3
"""
Hebrew Translation Validation Sample Generator
Creates a stratified sample of Hebrew files for native speaker validation
"""

import random
from pathlib import Path
from typing import List, Dict

# File categories for stratified sampling
FILE_CATEGORIES = {
    "core_pages": [
        "index_he.html",
        "why-hack23_he.html",
        "services_he.html",
        "blog_he.html",
        "projects_he.html",
        "sitemap_he.html",
        "accessibility-statement_he.html"
    ],
    "product_pages": [
        "cia-project_he.html",
        "black-trigram_he.html",
        "compliance-manager_he.html",
        "cia-features_he.html",
        "black-trigram-features_he.html",
        "cia-compliance-manager-features_he.html",
        "cia-docs_he.html",
        "black-trigram-docs_he.html",
        "cia-compliance-manager-docs_he.html"
    ],
    "isms_policies": [
        "discordian-info-sec-policy_he.html",
        "discordian-incident-response_he.html",
        "discordian-risk-register_he.html",
        "discordian-remote-access_he.html",
        "discordian-acceptable-use_he.html"
    ],
    "blog_posts": [
        "blog-cia-security_he.html",
        "blog-compliance-security_he.html",
        "blog-investment-firm-security_he.html",
        "blog-betting-gaming-cybersecurity_he.html",
        "blog-cannabis-cybersecurity-guide_he.html",
        "blog-public-isms-benefits_he.html",
        "blog-information-hoarding_he.html",
        "blog-cia-architecture_he.html",
        "blog-compliance-architecture_he.html",
        "blog-trigram-architecture_he.html",
        # ... more blog files available
    ],
    "iso_resources": [
        "iso-27001-2022-vs-2013_he.html",
        "iso-27001-implementation-sweden_he.html",
        "iso-27001-certification-costs-sweden_he.html",
        "iso-27001-implementation-mistakes_he.html"
    ],
    "industry_solutions": [
        "industries-betting-gaming_he.html",
        "industries-cannabis-security_he.html",
        "industries-investment-fintech_he.html"
    ],
    "other_pages": [
        "security-assessment-checklist_he.html",
        "cia-triad-faq_he.html"
    ]
}

# Recommended sample sizes by category (20% total = ~13 files)
SAMPLE_SIZES = {
    "core_pages": 2,
    "product_pages": 3,
    "isms_policies": 2,
    "blog_posts": 3,
    "iso_resources": 2,
    "industry_solutions": 1,
    "other_pages": 0  # Optional
}


def verify_files_exist(base_path: Path) -> Dict[str, List[str]]:
    """Verify which files actually exist in the repository"""
    existing_files = {}
    
    for category, files in FILE_CATEGORIES.items():
        existing = []
        for file in files:
            if (base_path / file).exists():
                existing.append(file)
        existing_files[category] = existing
    
    return existing_files


def generate_stratified_sample(existing_files: Dict[str, List[str]], 
                               seed: int = 42) -> Dict[str, List[str]]:
    """Generate a stratified random sample for validation"""
    random.seed(seed)
    sample = {}
    
    for category, files in existing_files.items():
        sample_size = SAMPLE_SIZES.get(category, 0)
        if sample_size > 0 and files:
            # Take sample size or all files if fewer available
            n_to_sample = min(sample_size, len(files))
            sample[category] = random.sample(files, n_to_sample)
        else:
            sample[category] = []
    
    return sample


def generate_validation_report(sample: Dict[str, List[str]], 
                               output_path: Path) -> None:
    """Generate a validation report with the sample files"""
    
    total_files = sum(len(files) for files in sample.values())
    
    report = f"""# Hebrew Translation Validation Sample

**Generated:** {Path(__file__).name}
**Date:** 2025-12-26
**Total Sample Size:** {total_files} files (~20% of 62 total)
**Sampling Method:** Stratified random sampling by category

---

## 📋 Sample Files for Validation

"""
    
    for category, files in sample.items():
        if files:
            category_name = category.replace('_', ' ').title()
            report += f"\n### {category_name} ({len(files)} files)\n\n"
            for file in sorted(files):
                report += f"- [ ] `{file}`\n"
    
    report += """
---

## 📊 Validation Process

For each file listed above:

1. **Open the file** in a web browser (RTL Hebrew layout)
2. **Review content** using HEBREW_VALIDATION_CHECKLIST.md criteria
3. **Score each criterion** (1-5 scale)
4. **Note specific issues** with examples
5. **Provide recommendations** for improvements

**Expected Time:** 30-45 minutes per file = ~8-10 hours total

---

## ✅ Validation Criteria Summary

1. **Professional Business Tone (25%)** - Formal, appropriate for executives
2. **Technical Accuracy (30%)** - Correct cybersecurity terminology
3. **Natural Hebrew Fluency (25%)** - Reads like native content
4. **Cultural Appropriateness (10%)** - Suitable for Israeli market
5. **Consistency & Clarity (10%)** - Terminology consistency

**Target Score:** 4.0+ (out of 5.0) = Very Good to Excellent

---

## 📝 Recording Results

Create a spreadsheet or document with:
- File name
- Scores for each criterion (1-5)
- Specific issues found
- Recommendations
- Overall assessment

**Template columns:**
| File | Prof. Tone | Tech Accuracy | Fluency | Cultural | Consistency | Total | Issues | Recommendations |
|------|------------|---------------|---------|----------|-------------|-------|--------|-----------------|

---

## 🎯 Priority Focus Areas

Based on Phase 4 standardization, validate:
- **Incident Response** → תגובה לאירועים (plural form)
- **Cybersecurity** → אבטחת סייבר (not English)
- **Risk Assessment** → הערכת סיכונים
- **Compliance** → ציות (regulatory context)
- **CIA Triad** → סודיות, שלמות, זמינות

Verify no singular form (תגובה לאירוע) appears anywhere.

---

*This validation sample provides comprehensive coverage across all page types while maintaining manageable review workload.*
"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✅ Validation report generated: {output_path}")


def main():
    """Main execution"""
    print("🇮🇱 Hebrew Translation Validation Sample Generator")
    print("=" * 60)
    print()
    
    # Get current directory
    base_path = Path('.')
    
    # Verify files exist
    print("📁 Verifying Hebrew files...")
    existing_files = verify_files_exist(base_path)
    
    total_existing = sum(len(files) for files in existing_files.values())
    print(f"✓ Found {total_existing} Hebrew files")
    print()
    
    # Generate stratified sample
    print("🎲 Generating stratified sample...")
    sample = generate_stratified_sample(existing_files)
    
    sample_size = sum(len(files) for files in sample.values())
    print(f"✓ Selected {sample_size} files for validation (~{sample_size/total_existing*100:.1f}%)")
    print()
    
    # Print sample breakdown
    print("📊 Sample breakdown:")
    for category, files in sample.items():
        if files:
            category_name = category.replace('_', ' ').title()
            print(f"  {category_name}: {len(files)} files")
    print()
    
    # Generate report
    output_path = Path('HEBREW_VALIDATION_SAMPLE.md')
    print("📄 Generating validation report...")
    generate_validation_report(sample, output_path)
    print()
    
    # Summary
    print("=" * 60)
    print("✅ VALIDATION SAMPLE READY")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Review HEBREW_VALIDATION_SAMPLE.md for file list")
    print("2. Use HEBREW_VALIDATION_CHECKLIST.md for evaluation criteria")
    print("3. Recruit native Hebrew speaker with cybersecurity knowledge")
    print("4. Allocate 8-10 hours for thorough validation")
    print("5. Compile results and prioritize issues")
    print()


if __name__ == '__main__':
    main()

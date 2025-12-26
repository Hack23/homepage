#!/usr/bin/env python3
"""
Hebrew Terminology Quarterly Audit Tool
Automated maintenance script to verify terminology consistency and identify drift
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple
from datetime import datetime
import json

# Core standardized terminology (from Phase 4)
STANDARD_TERMS = {
    # Core Security Terms
    "תגובה לאירועים": {
        "english": "Incident Response",
        "category": "Core Security",
        "expected_min": 90,
        "notes": "Always plural, never תגובה לאירוע"
    },
    "אבטחת סייבר": {
        "english": "Cybersecurity",
        "category": "Core Security",
        "expected_min": 450,
        "notes": "Not English 'Cybersecurity'"
    },
    "הערכת סיכונים": {
        "english": "Risk Assessment",
        "category": "Core Security",
        "expected_min": 70,
        "notes": "Standard ISMS term"
    },
    "ציות": {
        "english": "Compliance",
        "category": "Core Security",
        "expected_min": 1300,
        "notes": "Regulatory compliance (not תאימות)"
    },
    
    # ISMS Governance
    "מדיניות אבטחה": {
        "english": "Security Policy",
        "category": "ISMS Governance",
        "expected_min": 50,
        "notes": "Formal security policies"
    },
    "ניהול סיכונים": {
        "english": "Risk Management",
        "category": "ISMS Governance",
        "expected_min": 30,
        "notes": "Systematic risk processes"
    },
    "בקרת גישה": {
        "english": "Access Control",
        "category": "ISMS Governance",
        "expected_min": 25,
        "notes": "Authentication and authorization"
    },
    
    # CIA Triad
    "סודיות": {
        "english": "Confidentiality",
        "category": "CIA Triad",
        "expected_min": 100,
        "notes": "CIA Triad component"
    },
    "שלמות": {
        "english": "Integrity",
        "category": "CIA Triad",
        "expected_min": 150,
        "notes": "CIA Triad component"
    },
    "זמינות": {
        "english": "Availability",
        "category": "CIA Triad",
        "expected_min": 120,
        "notes": "CIA Triad component"
    },
    
    # Advanced Security
    "אפס אמון": {
        "english": "Zero Trust",
        "category": "Advanced Security",
        "expected_min": 5,
        "notes": "Security architecture"
    },
    "בדיקת חדירה": {
        "english": "Penetration Test",
        "category": "Advanced Security",
        "expected_min": 10,
        "notes": "Security testing"
    },
    "פריצת מידע": {
        "english": "Data Breach",
        "category": "Advanced Security",
        "expected_min": 5,
        "notes": "Unauthorized data access"
    },
}

# Terms that should NOT appear (deprecated/incorrect)
DEPRECATED_TERMS = {
    "תגובה לאירוע ": "Singular form - should be תגובה לאירועים",
    "תגובה לאירוע<": "Singular form - should be תגובה לאירועים",
    "תגובה לאירוע.": "Singular form - should be תגובה לאירועים",
    "תגובה לאירוע,": "Singular form - should be תגובה לאירועים",
}


def count_term_occurrences(file_path: Path, term: str) -> int:
    """Count occurrences of a term in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content.count(term)
    except Exception as e:
        print(f"  ⚠️  Error reading {file_path}: {e}")
        return 0


def audit_terminology(base_path: Path) -> Dict:
    """Audit Hebrew terminology across all files"""
    
    hebrew_files = list(base_path.glob('*_he.html'))
    
    if not hebrew_files:
        print("❌ No Hebrew files found")
        return {}
    
    results = {
        "audit_date": datetime.now().isoformat(),
        "files_audited": len(hebrew_files),
        "standard_terms": {},
        "deprecated_found": {},
        "summary": {},
        "warnings": [],
        "recommendations": []
    }
    
    print(f"📊 Auditing {len(hebrew_files)} Hebrew files...")
    print()
    
    # Check standard terms
    print("✅ Checking standard terminology...")
    for term, info in STANDARD_TERMS.items():
        total_count = 0
        files_with_term = []
        
        for file in hebrew_files:
            count = count_term_occurrences(file, term)
            if count > 0:
                total_count += count
                files_with_term.append(file.name)
        
        results["standard_terms"][term] = {
            "english": info["english"],
            "category": info["category"],
            "count": total_count,
            "files": len(files_with_term),
            "expected_min": info["expected_min"],
            "status": "✅" if total_count >= info["expected_min"] else "⚠️"
        }
        
        if total_count < info["expected_min"]:
            warning = f"{info['english']} ({term}): {total_count} uses (expected ≥{info['expected_min']})"
            results["warnings"].append(warning)
            print(f"  ⚠️  {warning}")
        else:
            print(f"  ✅ {info['english']}: {total_count} uses")
    
    print()
    
    # Check deprecated terms
    print("🚫 Checking for deprecated terms...")
    deprecated_found = False
    for term, issue in DEPRECATED_TERMS.items():
        total_count = 0
        files_with_issue = []
        
        for file in hebrew_files:
            count = count_term_occurrences(file, term)
            if count > 0:
                total_count += count
                files_with_issue.append(file.name)
        
        if total_count > 0:
            deprecated_found = True
            results["deprecated_found"][term] = {
                "issue": issue,
                "count": total_count,
                "files": files_with_issue
            }
            print(f"  ❌ Found {total_count} instances of '{term}': {issue}")
            print(f"     Files: {', '.join(files_with_issue[:3])}{'...' if len(files_with_issue) > 3 else ''}")
    
    if not deprecated_found:
        print("  ✅ No deprecated terms found")
    
    print()
    
    # Generate summary
    total_terms_ok = sum(1 for t in results["standard_terms"].values() if t["status"] == "✅")
    total_terms = len(results["standard_terms"])
    
    results["summary"] = {
        "terms_meeting_target": total_terms_ok,
        "total_terms_checked": total_terms,
        "consistency_score": round((total_terms_ok / total_terms) * 100, 1) if total_terms > 0 else 0,
        "deprecated_found": len(results["deprecated_found"]),
        "overall_status": "✅ PASS" if total_terms_ok >= (total_terms * 0.9) and len(results["deprecated_found"]) == 0 else "⚠️ NEEDS ATTENTION"
    }
    
    # Generate recommendations
    if results["warnings"]:
        results["recommendations"].append("Review files for missing standard terminology")
        results["recommendations"].append("Run standardize_hebrew_terminology.py on new content")
    
    if results["deprecated_found"]:
        results["recommendations"].append("Fix deprecated terms using standardize_hebrew_terminology.py")
    
    if not results["warnings"] and not results["deprecated_found"]:
        results["recommendations"].append("Terminology maintained at Phase 4 quality level")
        results["recommendations"].append("No immediate action required")
    
    return results


def generate_audit_report(results: Dict, output_path: Path) -> None:
    """Generate a detailed audit report"""
    
    report = f"""# Hebrew Terminology Quarterly Audit Report

**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Files Audited:** {results['files_audited']}  
**Audit Script:** quarterly_terminology_audit.py

---

## 📊 Executive Summary

**Overall Status:** {results['summary']['overall_status']}

| Metric | Value |
|--------|-------|
| Terms Meeting Target | {results['summary']['terms_meeting_target']}/{results['summary']['total_terms_checked']} |
| Consistency Score | {results['summary']['consistency_score']}% |
| Deprecated Terms Found | {results['summary']['deprecated_found']} |

---

## ✅ Standard Terminology Status

"""
    
    # Group by category
    by_category = {}
    for term, info in results["standard_terms"].items():
        category = info["category"]
        if category not in by_category:
            by_category[category] = []
        by_category[category].append((term, info))
    
    for category, terms in sorted(by_category.items()):
        report += f"\n### {category}\n\n"
        report += "| Hebrew Term | English | Count | Expected | Status |\n"
        report += "|-------------|---------|-------|----------|--------|\n"
        
        for term, info in terms:
            report += f"| {term} | {info['english']} | {info['count']} | ≥{info['expected_min']} | {info['status']} |\n"
    
    # Warnings section
    if results["warnings"]:
        report += "\n---\n\n## ⚠️ Warnings\n\n"
        for warning in results["warnings"]:
            report += f"- {warning}\n"
    
    # Deprecated terms section
    if results["deprecated_found"]:
        report += "\n---\n\n## 🚫 Deprecated Terms Found\n\n"
        for term, info in results["deprecated_found"].items():
            report += f"\n**`{term}`** - {info['issue']}\n"
            report += f"- Count: {info['count']}\n"
            report += f"- Files affected: {', '.join(info['files'][:5])}{'...' if len(info['files']) > 5 else ''}\n"
    
    # Recommendations section
    report += "\n---\n\n## 💡 Recommendations\n\n"
    for rec in results["recommendations"]:
        report += f"- {rec}\n"
    
    report += """
---

## 🔄 Next Steps

1. **Review warnings** and investigate low-count terms
2. **Fix deprecated terms** if any found
3. **Update Hebrew-Translation-Guide.md** if new terms needed
4. **Schedule next audit** in 3 months

---

## 📚 Reference

- Hebrew-Translation-Guide.md v4.0 (terminology standards)
- standardize_hebrew_terminology.py (automated standardization)
- HEBREW_PHASE4_COMPLETION_REPORT.md (baseline metrics)

**Phase 4 Baseline (Dec 2025):**
- Quality Score: 80%+
- Terminology Consistency: 90%+
- Standard Terms: 675 replacements applied

---

*This quarterly audit helps maintain the professional Hebrew cybersecurity terminology established in Phase 4.*
"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"📄 Report saved: {output_path}")


def main():
    """Main execution"""
    print("🇮🇱 Hebrew Terminology Quarterly Audit Tool")
    print("=" * 60)
    print()
    
    base_path = Path('.')
    
    # Run audit
    results = audit_terminology(base_path)
    
    if not results:
        return 1
    
    # Print summary
    print("=" * 60)
    print("📈 AUDIT SUMMARY")
    print("=" * 60)
    print(f"Status: {results['summary']['overall_status']}")
    print(f"Consistency Score: {results['summary']['consistency_score']}%")
    print(f"Terms Meeting Target: {results['summary']['terms_meeting_target']}/{results['summary']['total_terms_checked']}")
    print(f"Deprecated Terms: {results['summary']['deprecated_found']}")
    print()
    
    # Generate report
    timestamp = datetime.now().strftime('%Y%m%d')
    output_path = Path(f'HEBREW_TERMINOLOGY_AUDIT_{timestamp}.md')
    
    print("📄 Generating audit report...")
    generate_audit_report(results, output_path)
    print()
    
    # Save JSON for programmatic access
    json_path = Path(f'HEBREW_TERMINOLOGY_AUDIT_{timestamp}.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"💾 JSON data saved: {json_path}")
    print()
    
    # Final recommendations
    print("=" * 60)
    print("💡 RECOMMENDATIONS")
    print("=" * 60)
    for rec in results["recommendations"]:
        print(f"- {rec}")
    print()
    
    # Exit code based on status
    if results['summary']['overall_status'] == "✅ PASS":
        print("✅ Audit PASSED - Terminology maintained at Phase 4 quality")
        return 0
    else:
        print("⚠️  Audit NEEDS ATTENTION - Review warnings and take action")
        return 1


if __name__ == '__main__':
    exit(main())

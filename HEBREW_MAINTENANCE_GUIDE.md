# Hebrew Translation Maintenance Guide

**Version:** 1.0  
**Date:** December 26, 2025  
**Status:** Post-Phase 4 Maintenance  
**Quality Baseline:** 80%+ (Phase 4 Complete)

---

## 🎯 Purpose

This guide provides instructions for maintaining the professional Hebrew cybersecurity terminology established in Phase 4 across all 62 translated pages.

**Maintenance Goals:**
- Maintain 80%+ quality score
- Preserve 90%+ terminology consistency
- Prevent terminology drift
- Ensure new content follows standards

---

## 📚 Available Tools & Resources

### 1. Standardization Tools

**`standardize_hebrew_terminology.py`**
- **Purpose:** Apply Phase 4 terminology standards to new or updated content
- **When to use:** After creating new Hebrew content or updating existing pages
- **Usage:**
  ```bash
  python3 standardize_hebrew_terminology.py
  ```
- **Output:** Detailed report of replacements made

**`quarterly_terminology_audit.py`**
- **Purpose:** Quarterly consistency checks and drift detection
- **When to use:** Every 3 months or after significant content updates
- **Usage:**
  ```bash
  python3 quarterly_terminology_audit.py
  ```
- **Output:** Audit report (MD + JSON) with pass/fail status

### 2. Validation Tools

**`generate_validation_sample.py`**
- **Purpose:** Generate stratified sample for native speaker validation
- **When to use:** Before major releases or annually
- **Usage:**
  ```bash
  python3 generate_validation_sample.py
  ```
- **Output:** HEBREW_VALIDATION_SAMPLE.md with 13 files (~20%)

**`HEBREW_VALIDATION_CHECKLIST.md`**
- **Purpose:** Structured validation guide for native speakers
- **When to use:** During native speaker validation sessions
- **Criteria:** 5 weighted validation dimensions

### 3. Documentation

**`Hebrew-Translation-Guide.md` v4.0**
- **Purpose:** Comprehensive terminology reference and standards
- **Sections:** 128+ English → Hebrew term mappings
- **Update frequency:** As needed when new terms emerge

**`HEBREW_PHASE4_COMPLETION_REPORT.md`**
- **Purpose:** Phase 4 methodology, baseline metrics, and results
- **Use as:** Reference for quality baseline and historical context

**`Hebrew-Translation-Status.md`**
- **Purpose:** Track translation coverage and quality metrics
- **Update frequency:** After significant changes or new files

---

## 🔄 Maintenance Workflows

### Workflow 1: Adding New Hebrew Content

**When:** Creating a new `*_he.html` file

**Steps:**
1. Create initial Hebrew translation following Hebrew-Translation-Guide.md v4.0
2. Run standardization:
   ```bash
   python3 standardize_hebrew_terminology.py
   ```
3. Review changes and verify accuracy
4. Update Hebrew-Translation-Status.md with new file
5. Commit changes with clear message

**Quality Checks:**
- [ ] Follows Phase 4 terminology standards
- [ ] No deprecated terms (e.g., singular תגובה לאירוע)
- [ ] Consistent with Hebrew-Translation-Guide.md v4.0
- [ ] RTL layout properly configured
- [ ] Professional business tone maintained

---

### Workflow 2: Updating Existing Hebrew Content

**When:** Modifying existing `*_he.html` files

**Steps:**
1. Make content updates
2. If terminology changed, run standardization:
   ```bash
   python3 standardize_hebrew_terminology.py
   ```
3. Review audit warnings if any
4. Verify consistency with guide
5. Commit with descriptive message

**Quality Checks:**
- [ ] Terminology remains consistent with standards
- [ ] No introduction of deprecated terms
- [ ] Professional tone maintained
- [ ] Updates align with Hebrew-Translation-Guide.md v4.0

---

### Workflow 3: Quarterly Terminology Audit

**When:** Every 3 months (March, June, September, December)

**Steps:**
1. Run quarterly audit:
   ```bash
   python3 quarterly_terminology_audit.py
   ```
2. Review generated report (`HEBREW_TERMINOLOGY_AUDIT_YYYYMMDD.md`)
3. Check audit status:
   - **✅ PASS:** No action needed, file report
   - **⚠️ NEEDS ATTENTION:** Address warnings and deprecated terms
4. If issues found:
   - Run `standardize_hebrew_terminology.py` to fix
   - Re-run audit to verify fixes
5. Update Hebrew-Translation-Status.md if needed
6. Archive audit report for records

**Expected Results:**
- Consistency Score: ≥90%
- Terms Meeting Target: ≥12/13 (92%+)
- Deprecated Terms: 0

---

### Workflow 4: Annual Native Speaker Validation

**When:** Annually or before major releases

**Steps:**
1. Generate validation sample:
   ```bash
   python3 generate_validation_sample.py
   ```
2. Review HEBREW_VALIDATION_SAMPLE.md (13 files)
3. Recruit qualified native speaker:
   - Native Hebrew proficiency
   - Cybersecurity domain knowledge
   - Israeli market experience
4. Provide validator with:
   - HEBREW_VALIDATION_SAMPLE.md (file list)
   - HEBREW_VALIDATION_CHECKLIST.md (criteria)
   - Hebrew-Translation-Guide.md v4.0 (reference)
5. Allocate 8-10 hours for thorough review
6. Compile validation results
7. Prioritize issues (Critical → Important → Minor)
8. Address critical and important issues
9. Update Hebrew-Translation-Guide.md if terminology changes
10. Document findings and actions taken

**Validation Criteria:**
- Professional Business Tone: 25%
- Technical Accuracy: 30%
- Natural Hebrew Fluency: 25%
- Cultural Appropriateness: 10%
- Consistency & Clarity: 10%

**Target Score:** 4.0+ out of 5.0

---

## 📊 Quality Metrics & Targets

### Terminology Consistency Targets

| Metric | Target | Current (Phase 4) | Status |
|--------|--------|-------------------|--------|
| Quality Score | ≥80% | 80%+ | ✅ |
| Consistency | ≥90% | 90%+ | ✅ |
| תגובה לאירועים | ≥90 | 94 | ✅ |
| אבטחת סייבר | ≥450 | 471 | ✅ |
| הערכת סיכונים | ≥70 | 74 | ✅ |
| ציות | ≥1300 | 1360 | ✅ |
| Deprecated Terms | 0 | 0 | ✅ |

### Quarterly Audit Targets

| Check | Target | Action if Failed |
|-------|--------|------------------|
| Consistency Score | ≥90% | Run standardization script |
| Terms Meeting Target | ≥12/13 | Investigate low-count terms |
| Deprecated Terms | 0 | Fix immediately |
| Overall Status | PASS | Address all warnings |

---

## 🚨 Common Issues & Solutions

### Issue 1: Terminology Drift

**Symptoms:**
- Quarterly audit shows declining consistency score
- New English terms appearing in Hebrew files
- Inconsistent term usage across pages

**Solution:**
```bash
# Re-standardize all Hebrew files
python3 standardize_hebrew_terminology.py

# Verify fix
python3 quarterly_terminology_audit.py
```

---

### Issue 2: Deprecated Terms Reappearing

**Symptoms:**
- Audit reports deprecated terms (e.g., singular תגובה לאירוע)
- Inconsistency warnings increase

**Solution:**
1. Run standardization script
2. Review recent commits for source of reintroduction
3. Educate content contributors on standards
4. Add to .gitignore if needed to prevent accidental commits

---

### Issue 3: New Terminology Needed

**Symptoms:**
- New cybersecurity concepts not in Hebrew-Translation-Guide.md
- Uncertainty about correct Hebrew translation
- Inconsistent usage of new terms

**Solution:**
1. Research Israeli cybersecurity industry usage
2. Consult Israeli National Cyber Directorate if available
3. Document new term in Hebrew-Translation-Guide.md v4.0
4. Add to standardize_hebrew_terminology.py mapping
5. Update quarterly_terminology_audit.py expected counts
6. Apply across all relevant files

---

### Issue 4: Quality Score Decline

**Symptoms:**
- Quality score drops below 80%
- User feedback indicates confusion
- SEO metrics decline

**Solution:**
1. Run full quarterly audit to identify specific issues
2. Review recent changes that may have introduced problems
3. Re-run standardization script
4. Consider native speaker validation session
5. Address all critical and important issues
6. Re-audit to verify improvement

---

## 📅 Maintenance Schedule

### Monthly Tasks
- [ ] None required (unless major updates)

### Quarterly Tasks (Every 3 Months)
- [ ] Run quarterly terminology audit
- [ ] Review audit report and address issues
- [ ] Update Hebrew-Translation-Status.md if needed
- [ ] Archive audit reports for historical tracking

### Annual Tasks (Yearly)
- [ ] Conduct native speaker validation (optional but recommended)
- [ ] Review Hebrew-Translation-Guide.md for updates
- [ ] Assess need for new terminology additions
- [ ] Update maintenance procedures if needed
- [ ] Review Phase 4 baseline and adjust targets if appropriate

### As-Needed Tasks
- [ ] Standardize new Hebrew content (after creation)
- [ ] Update guide when new terms emerge
- [ ] Address urgent terminology issues immediately
- [ ] Respond to user feedback on Hebrew content

---

## 👥 Roles & Responsibilities

### Content Contributors
- Follow Hebrew-Translation-Guide.md v4.0 for new content
- Run standardization script after updates
- Maintain professional business tone
- Preserve RTL layout and Hebrew fonts

### Quality Assurance
- Execute quarterly audits on schedule
- Review audit reports and prioritize issues
- Coordinate native speaker validation
- Track quality metrics over time

### Hebrew Subject Matter Expert (Optional)
- Validate new terminology additions
- Advise on Israeli market appropriateness
- Review contentious translation decisions
- Provide cultural context guidance

---

## 🎓 Training & Onboarding

### For New Contributors

**Before creating Hebrew content:**
1. Read Hebrew-Translation-Guide.md v4.0 (focus on terminology tables)
2. Review 2-3 existing Hebrew pages as examples
3. Understand RTL layout requirements
4. Familiarize with standardization script

**After creating content:**
1. Run `python3 standardize_hebrew_terminology.py`
2. Review changes made by script
3. Verify professional tone and accuracy
4. Test RTL layout in browser
5. Commit with clear description

**Resources:**
- Hebrew-Translation-Guide.md v4.0 (comprehensive terminology)
- HEBREW_PHASE4_COMPLETION_REPORT.md (methodology)
- This maintenance guide (ongoing procedures)

---

## 📈 Success Metrics

### Maintenance Success Indicators

**Green Status (Excellent):**
- ✅ Quarterly audits consistently PASS
- ✅ Consistency score ≥92%
- ✅ No deprecated terms
- ✅ Native speaker validation ≥4.0/5.0
- ✅ Quality score stable at 80%+

**Yellow Status (Needs Attention):**
- ⚠️ Quarterly audit warnings appearing
- ⚠️ Consistency score 85-90%
- ⚠️ 1-2 terms below target
- ⚠️ Minor terminology drift detected

**Red Status (Action Required):**
- ❌ Quarterly audit FAILS
- ❌ Consistency score <85%
- ❌ Deprecated terms reappearing
- ❌ Quality score dropping
- ❌ User complaints about Hebrew content

---

## 🔗 Related Documentation

**Primary References:**
- Hebrew-Translation-Guide.md v4.0 - Terminology standards
- HEBREW_PHASE4_COMPLETION_REPORT.md - Baseline and methodology
- Hebrew-Translation-Status.md - Current state tracking

**Validation Resources:**
- HEBREW_VALIDATION_CHECKLIST.md - Validation criteria
- HEBREW_VALIDATION_SAMPLE.md - Sample file list (regenerate as needed)

**Automation Scripts:**
- standardize_hebrew_terminology.py - Apply standards
- quarterly_terminology_audit.py - Consistency checks
- generate_validation_sample.py - Sample generation

---

## 📞 Escalation & Support

**For Terminology Questions:**
1. Check Hebrew-Translation-Guide.md v4.0 first
2. Search Phase 4 completion report for context
3. Consult Israeli cybersecurity industry standards
4. If still uncertain, mark for native speaker review

**For Technical Issues:**
1. Check script output for error messages
2. Verify Python environment (Python 3.7+)
3. Ensure all Hebrew files are UTF-8 encoded
4. Review recent git commits for conflicts

**For Quality Concerns:**
1. Run quarterly audit to quantify issues
2. Review audit report recommendations
3. Apply standardization script
4. Schedule native speaker validation if needed

---

## ✅ Maintenance Checklist

### Before Each Release
- [ ] Run quarterly terminology audit
- [ ] Review and address any warnings
- [ ] Verify no deprecated terms present
- [ ] Consistency score ≥90%
- [ ] Quality score maintained at 80%+

### After Major Updates
- [ ] Run standardization script on changed files
- [ ] Spot-check terminology consistency
- [ ] Update Hebrew-Translation-Status.md
- [ ] Commit with descriptive message

### Quarterly Review
- [ ] Execute full terminology audit
- [ ] Archive audit report
- [ ] Track metrics trends over time
- [ ] Address any declining metrics
- [ ] Update this guide if procedures change

---

## 📝 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-26 | Initial maintenance guide created post-Phase 4 |

---

*This maintenance guide ensures the professional Hebrew cybersecurity terminology established in Phase 4 is preserved and improved over time. Following these procedures maintains the 80%+ quality score and 90%+ consistency that makes Hack23's Hebrew content industry-leading.*

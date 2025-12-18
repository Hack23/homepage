# 🇰🇷 Korean Translation Standardization Plan

> **Surgical Fix Strategy for 68 Korean HTML Files**  
> *Version 1.0 - December 2025*

## 📋 Executive Summary

**Objective:** Standardize Korean cybersecurity terminology across 68 Korean HTML files (`*_ko.html`) with minimal, surgical changes.

**Current State:**
- ✅ 68 Korean files exist (60.4% of 96 base files)
- ⚠️ 62.1% quality (33 fully translated, 3 mostly translated, 22 partially translated)
- ❌ Multiple terminology inconsistencies identified
- ❌ 23 files missing Schema.org `"inLanguage": "ko"`

**Target State:**
- ✅ 100% terminology consistency across all 68 files
- ✅ Professional Korean cybersecurity terminology (K-ISMS context)
- ✅ All 68 files have `"inLanguage": "ko"` in Schema.org
- ✅ Enhanced market relevance with PIPA and K-ISMS references

## 📊 Inconsistency Analysis

### 1️⃣ Spacing Inconsistencies

#### Issue 1A: Cybersecurity (사이버보안 vs 사이버 보안)

**Current State:**
- ✅ **사이버보안** (no space): **112 occurrences** ← PREFERRED
- ❌ **사이버 보안** (with space): **59 occurrences** ← INCONSISTENT

**Fix Required:**
```bash
Find: "사이버 보안"
Replace: "사이버보안"
Estimated Changes: ~59 replacements across multiple files
```

**Rationale:** Technical compound term representing single concept; industry standard is no spacing.

---

#### Issue 1B: Information Security (정보보안 vs 정보 보안)

**Current State:**
- ✅ **정보보안** (no space): **93 occurrences** ← PREFERRED
- ❌ **정보 보안** (with space): **22 occurrences** ← INCONSISTENT

**Fix Required:**
```bash
Find: "정보 보안"
Replace: "정보보안"
Estimated Changes: ~22 replacements across multiple files
```

**Rationale:** Technical compound term representing single concept; matches K-ISMS official terminology (정보보호관리체계).

---

#### Issue 1C: Compliance (규정 준수 vs 규정준수)

**Current State:**
- ✅ **규정 준수** (with space): **144 occurrences** ← PREFERRED
- ❌ **규정준수** (no space): **11 occurrences** ← INCONSISTENT

**Fix Required:**
```bash
Find: "규정준수"
Replace: "규정 준수"
Estimated Changes: ~11 replacements across multiple files
```

**Rationale:** Action phrase (regulations + adherence); proper Korean requires spacing between noun and verb phrase.

**Note:** **컴플라이언스** (Konglish, 142 occurrences) is acceptable in formal business contexts but should be balanced with **규정 준수**.

---

### 2️⃣ Konglish vs. Proper Korean

#### Issue 2A: Risk (리스크 vs 위험)

**Current State:**
- ✅ **위험** (proper Korean): **150 occurrences** ← PREFERRED
- ❌ **리스크** (Konglish): **7 occurrences** ← AVOID

**Fix Required:**
```bash
Find: "리스크"
Replace: "위험"
Estimated Changes: ~7 replacements across multiple files
```

**Rationale:** Clear Korean equivalent exists; professional documents should use proper Korean term. Konglish adds no value.

---

### 3️⃣ Regulatory Context Additions

#### Issue 3A: K-ISMS Context Missing

**Current State:**
- ✅ **ISO 27001** mentioned: **400 occurrences**
- ❌ **K-ISMS** mentioned: **33 occurrences** (TOO FEW for Korean market)
- ❌ **정보보호관리체계** mentioned: **0 occurrences** (MISSING Korean term)

**Fix Required:**
Add K-ISMS context where ISO 27001 is mentioned prominently:

**Pattern 1: Parallel Mention**
```korean
Before: ISO 27001 인증
After:  ISO 27001 및 K-ISMS 인증
```

**Pattern 2: Explanatory Context**
```korean
Before: ISO 27001 구현
After:  ISO 27001 및 K-ISMS(한국 정보보호관리체계) 구현
```

**Target Files:**
- ISO 27001 implementation guides
- ISMS policy pages
- Services pages mentioning ISO 27001
- Blog posts about ISMS

**Estimated Changes:** ~30-40 strategic additions (not every mention, only prominent ones)

---

#### Issue 3B: PIPA Context Missing

**Current State:**
- ❌ **GDPR** mentioned: **152 occurrences**
- ❌ **PIPA** mentioned: **11 occurrences** (TOO FEW for Korean market)
- ❌ **개인정보보호법** mentioned: **11 occurrences** (TOO FEW)

**Fix Required:**
Add PIPA context where GDPR is mentioned for Korean market:

**Pattern 1: Parallel Mention**
```korean
Before: GDPR 준수
After:  GDPR 및 개인정보보호법(PIPA) 준수
```

**Pattern 2: Korean Primary**
```korean
Before: GDPR 규정
After:  개인정보보호법(PIPA) 및 GDPR 규정
```

**Target Files:**
- Privacy policy pages
- Data protection pages
- Compliance pages
- Industry solution pages (cannabis, investment)
- Blog posts about data protection

**Estimated Changes:** ~25-35 strategic additions

---

### 4️⃣ Schema.org Technical Issues

#### Issue 4: Missing `"inLanguage": "ko"`

**Current State:**
- ✅ 45 files have `"inLanguage": "ko"` in Schema.org structured data
- ❌ 23 files missing `"inLanguage": "ko"` in Schema.org

**Files Missing `inLanguage`:**

```
blog-cannabis-cybersecurity-guide_ko.html
blog-cia-alternative-media-discordian-2026_ko.html
blog-cia-architecture_ko.html
blog-cia-business-case-global-news_ko.html
blog-cia-financial-strategy_ko.html
blog-cia-future-security_ko.html
blog-cia-mindmaps_ko.html
blog-cia-osint-intelligence_ko.html
blog-cia-security_ko.html
blog-cia-workflows_ko.html
blog-compliance-architecture_ko.html
blog-compliance-future_ko.html
blog-compliance-security_ko.html
blog-george-dorn-cia-code_ko.html
blog-george-dorn-compliance-code_ko.html
blog-george-dorn-trigram-code_ko.html
blog-investment-firm-security_ko.html
blog-medical-cannabis-hipaa-gdpr_ko.html
blog-trigram-architecture_ko.html
blog-trigram-combat_ko.html
blog-trigram-future_ko.html
discordian-cybersecurity_ko.html
discordian-info-sec-policy_ko.html
```

**Fix Required:**

Add `"inLanguage": "ko"` to all Schema.org structured data blocks:

**Pattern 1: WebPage Schema**
```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "...",
  "description": "...",
  "inLanguage": "ko",  ← ADD THIS LINE
  "url": "..."
}
```

**Pattern 2: BlogPosting Schema**
```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "...",
  "description": "...",
  "inLanguage": "ko",  ← ADD THIS LINE
  "datePublished": "..."
}
```

**Estimated Changes:** 23 files × 1-3 Schema.org blocks per file = ~30-40 additions

---

## 🎯 Surgical Fix Strategy

### Phase 1: Terminology Standardization (Issues 1A-2A)

**Total Estimated Changes:** ~99 text replacements

| Issue | Find | Replace | Count | Priority |
|-------|------|---------|-------|----------|
| 1A | 사이버 보안 | 사이버보안 | ~59 | 🔴 HIGH |
| 1B | 정보 보안 | 정보보안 | ~22 | 🔴 HIGH |
| 1C | 규정준수 | 규정 준수 | ~11 | 🟡 MEDIUM |
| 2A | 리스크 | 위험 | ~7 | 🟡 MEDIUM |

**Approach:**
1. Use automated find-and-replace with careful review
2. Validate each file after changes
3. Check for context-specific exceptions (e.g., in code examples or quotes)
4. Manual review of borderline cases

**Risk Mitigation:**
- ✅ Changes are reversible (version control)
- ✅ Each change is a clear improvement
- ✅ No semantic meaning changes
- ✅ All changes align with professional standards

---

### Phase 2: Regulatory Context Enhancement (Issues 3A-3B)

**Total Estimated Changes:** ~55-75 strategic additions

#### Phase 2A: K-ISMS Context Addition

**Target Files (Priority Order):**

1. **ISO 27001 Resource Pages** (4 files):
   - `iso-27001-implementation-sweden_ko.html`
   - `iso-27001-certification-costs-sweden_ko.html`
   - `iso-27001-2022-vs-2013_ko.html`
   - `iso-27001-implementation-mistakes_ko.html`

2. **ISMS Policy Pages** (2 files):
   - `discordian-info-sec-policy_ko.html`
   - `discordian-isms-review_ko.html` (if translated)

3. **Services & Core Pages** (2 files):
   - `services_ko.html`
   - `why-hack23_ko.html`

4. **Blog Posts Mentioning ISO 27001** (~5-7 strategic posts):
   - CIA architecture series
   - Compliance series
   - Public ISMS benefits

**Insertion Points:**

```korean
Context: "ISO 27001 인증을 통한 정보보안관리체계 구축"

Add K-ISMS:
"ISO 27001 및 K-ISMS 인증을 통한 정보보안관리체계(한국 정보보호관리체계) 구축"
```

**Estimated Changes:** ~30-40 additions

---

#### Phase 2B: PIPA Context Addition

**Target Files (Priority Order):**

1. **Privacy & Data Protection Pages** (if translated):
   - `discordian-privacy_ko.html`
   - `discordian-data-protection_ko.html`
   - `discordian-data-classification_ko.html`

2. **Compliance Pages** (2 files):
   - `discordian-compliance_ko.html`
   - `discordian-compliance-frameworks_ko.html`

3. **Industry Solution Pages** (3 files):
   - `industries-cannabis-security_ko.html` (healthcare data)
   - `industries-investment-fintech_ko.html` (financial data)
   - `blog-medical-cannabis-hipaa-gdpr_ko.html`

4. **Blog Posts Mentioning GDPR** (~3-5 strategic posts):
   - Medical cannabis HIPAA/GDPR post
   - Privacy-focused blog posts

**Insertion Points:**

```korean
Context: "GDPR 준수를 통한 개인정보 보호"

Add PIPA:
"개인정보보호법(PIPA) 및 GDPR 준수를 통한 개인정보 보호"
```

**Estimated Changes:** ~25-35 additions

---

### Phase 3: Schema.org Technical Fix (Issue 4)

**Total Estimated Changes:** ~30-40 additions

**Approach:**
1. Identify all Schema.org JSON-LD blocks in each of 23 files
2. Add `"inLanguage": "ko"` after `@type` declaration
3. Validate JSON-LD syntax
4. Test with Google Rich Results Test

**Example Fix:**

```json
// BEFORE
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "CIA 아키텍처: 5개의 펜타클",
  "description": "...",
  "datePublished": "2025-11-15T00:00:00Z"
}

// AFTER
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "CIA 아키텍처: 5개의 펜타클",
  "description": "...",
  "inLanguage": "ko",  ← ADDED
  "datePublished": "2025-11-15T00:00:00Z"
}
```

**Files to Fix (23 total):**
- 21 blog posts
- 2 ISMS policy pages

---

## 📋 Implementation Checklist

### Pre-Implementation

- [x] Create comprehensive glossary (Korean-Cybersecurity-Glossary.md)
- [x] Document all inconsistencies with counts
- [x] Create detailed fix plan with examples
- [ ] Review plan with native Korean speaker (recommended)
- [ ] Set up testing environment
- [ ] Create backup branch for rollback

### Phase 1: Terminology Standardization

**Issue 1A: 사이버 보안 → 사이버보안**
- [ ] Create search pattern: `"사이버 보안"`
- [ ] Identify affected files (grep results)
- [ ] Perform replacements with validation
- [ ] Review 10% sample manually
- [ ] Run HTML validation on changed files
- [ ] Commit changes: "Fix: Standardize 사이버보안 spacing (Issue 1A)"

**Issue 1B: 정보 보안 → 정보보안**
- [ ] Create search pattern: `"정보 보안"`
- [ ] Identify affected files
- [ ] Perform replacements with validation
- [ ] Review 10% sample manually
- [ ] Run HTML validation
- [ ] Commit changes: "Fix: Standardize 정보보안 spacing (Issue 1B)"

**Issue 1C: 규정준수 → 규정 준수**
- [ ] Create search pattern: `"규정준수"`
- [ ] Identify affected files
- [ ] Perform replacements with validation
- [ ] Review 10% sample manually
- [ ] Run HTML validation
- [ ] Commit changes: "Fix: Standardize 규정 준수 spacing (Issue 1C)"

**Issue 2A: 리스크 → 위험**
- [ ] Create search pattern: `"리스크"`
- [ ] Identify affected files
- [ ] Perform replacements with validation
- [ ] Manual review of ALL occurrences (only 7 total)
- [ ] Run HTML validation
- [ ] Commit changes: "Fix: Replace Konglish 리스크 with proper Korean 위험 (Issue 2A)"

### Phase 2A: K-ISMS Context Addition

- [ ] Identify all ISO 27001 mentions across 68 files
- [ ] Prioritize high-impact pages (ISO guides, services, ISMS policies)
- [ ] Add K-ISMS context following patterns from glossary
- [ ] Manual review of each addition for natural flow
- [ ] Native speaker review (recommended)
- [ ] Run HTML validation
- [ ] Commit changes: "Enhance: Add K-ISMS context alongside ISO 27001 (Issue 3A)"

### Phase 2B: PIPA Context Addition

- [ ] Identify all GDPR mentions across 68 files
- [ ] Prioritize data protection and privacy pages
- [ ] Add PIPA context following patterns from glossary
- [ ] Manual review of each addition for natural flow
- [ ] Native speaker review (recommended)
- [ ] Run HTML validation
- [ ] Commit changes: "Enhance: Add PIPA context alongside GDPR (Issue 3B)"

### Phase 3: Schema.org Technical Fix

- [ ] Identify all 23 files missing `inLanguage: ko`
- [ ] Locate all Schema.org JSON-LD blocks in each file
- [ ] Add `"inLanguage": "ko"` in correct position
- [ ] Validate JSON-LD syntax for all blocks
- [ ] Test with Google Rich Results Test (sample)
- [ ] Run HTML validation
- [ ] Commit changes: "Fix: Add missing inLanguage: ko to Schema.org (Issue 4)"

### Post-Implementation

- [ ] Full HTML validation suite (all 68 files)
- [ ] Accessibility audit (WAVE/axe - sample files)
- [ ] Cross-browser testing (Chrome, Firefox, Safari - sample pages)
- [ ] Mobile responsiveness check (sample pages)
- [ ] Native Korean speaker final review
- [ ] Update Korean-Translation-Status.md
- [ ] Update Korean-Translation-Guide.md (version 5.0)
- [ ] Document lessons learned

---

## 🧪 Testing & Validation

### Automated Testing

**HTML Validation:**
```bash
# Validate all Korean files
for file in *_ko.html; do
  echo "Validating: $file"
  htmlhint "$file"
done
```

**Schema.org Validation:**
```bash
# Check for inLanguage in all files
grep -l '"inLanguage".*"ko"' *_ko.html | wc -l
# Should return: 68 (all files)
```

**Terminology Consistency Check:**
```bash
# Verify no spacing errors remain
echo "사이버 보안 (should be 0):"
grep -r "사이버 보안" *_ko.html | wc -l

echo "정보 보안 (should be 0):"
grep -r "정보 보안" *_ko.html | wc -l

echo "규정준수 (should be 0):"
grep -r "규정준수" *_ko.html | wc -l

echo "리스크 (should be 0):"
grep -r "리스크" *_ko.html | wc -l
```

### Manual Testing

**Sample Review (10% of files = 7 files):**
1. `index_ko.html` (homepage)
2. `services_ko.html` (services)
3. `blog-cia-architecture_ko.html` (blog post)
4. `iso-27001-implementation-sweden_ko.html` (ISO guide)
5. `discordian-info-sec-policy_ko.html` (ISMS policy)
6. `industries-cannabis-security_ko.html` (industry solution)
7. `cia-triad-faq_ko.html` (FAQ page)

**Review Checklist per File:**
- [ ] All terminology changes applied correctly
- [ ] K-ISMS context added where appropriate
- [ ] PIPA context added where appropriate
- [ ] Schema.org has `inLanguage: ko`
- [ ] HTML validates (W3C)
- [ ] Text flows naturally in Korean
- [ ] No broken links
- [ ] Mobile responsive
- [ ] Accessibility maintained

---

## 📊 Expected Outcomes

### Quantitative Improvements

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| **Spacing Consistency (사이버보안)** | 65.5% (112/171) | 100% (171/171) | +34.5% |
| **Spacing Consistency (정보보안)** | 80.9% (93/115) | 100% (115/115) | +19.1% |
| **Spacing Consistency (규정 준수)** | 92.9% (144/155) | 100% (155/155) | +7.1% |
| **Proper Korean (위험 not 리스크)** | 95.5% (150/157) | 100% (157/157) | +4.5% |
| **K-ISMS Mentions** | 33 | ~63-73 | +91-121% |
| **PIPA Mentions** | 11 | ~36-46 | +227-318% |
| **Schema.org Compliance** | 66.2% (45/68) | 100% (68/68) | +33.8% |

### Qualitative Improvements

1. **Professional Quality**: Consistent terminology matching industry standards and official K-ISMS documentation
2. **Market Relevance**: Enhanced focus on Korean regulatory context (K-ISMS, PIPA) alongside international standards
3. **SEO Enhancement**: Complete Schema.org compliance with proper language declarations
4. **User Experience**: More natural Korean language flow with proper spacing conventions
5. **Credibility**: Professional cybersecurity terminology demonstrates domain expertise

---

## 🚨 Risk Management

### Identified Risks

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Breaking HTML structure | HIGH | LOW | Surgical text-only changes; validate after each phase |
| Changing semantic meaning | MEDIUM | LOW | Manual review of each change; native speaker validation |
| Context-inappropriate changes | MEDIUM | LOW | Pattern-based approach; manual review of additions |
| Inconsistent style | LOW | MEDIUM | Follow glossary patterns strictly; comprehensive checklist |
| Rollback requirement | MEDIUM | LOW | Git version control; backup branch; phase-by-phase commits |

### Rollback Plan

If issues are discovered:

1. **Immediate Rollback**: `git revert [commit-hash]` for problematic commits
2. **Phase Rollback**: Revert entire phase if systemic issues found
3. **Full Rollback**: Restore from backup branch if major problems
4. **Re-evaluation**: Review glossary and fix plan before re-attempting

---

## 📅 Implementation Timeline

### Recommended Approach: Phased Implementation

**Phase 1: Terminology Standardization (Issues 1A-2A)**
- **Duration**: 2-3 hours
- **Effort**: Mostly automated with validation
- **Risk**: LOW
- **Priority**: 🔴 HIGH

**Phase 2A: K-ISMS Context Addition (Issue 3A)**
- **Duration**: 3-4 hours
- **Effort**: Manual additions with pattern following
- **Risk**: MEDIUM
- **Priority**: 🟡 MEDIUM

**Phase 2B: PIPA Context Addition (Issue 3B)**
- **Duration**: 2-3 hours
- **Effort**: Manual additions with pattern following
- **Risk**: MEDIUM
- **Priority**: 🟡 MEDIUM

**Phase 3: Schema.org Technical Fix (Issue 4)**
- **Duration**: 1-2 hours
- **Effort**: Straightforward JSON-LD additions
- **Risk**: LOW
- **Priority**: 🟢 LOW (but easy win)

**Total Estimated Time**: 8-12 hours for complete implementation

---

## 📚 References

### Key Documents

1. **Korean-Cybersecurity-Glossary.md** - Comprehensive terminology reference (200+ terms)
2. **Korean-Translation-Guide.md** - General translation guidelines (v4.0)
3. **Korean-Translation-Status.md** - Current translation status (62.1% quality)
4. **TRANSLATION_DOCUMENTATION_README.md** - Master translation documentation

### Korean Language Resources

- **National Institute of Korean Language** (국립국어원)
- **KISA Publications** (한국인터넷진흥원)
- **K-ISMS Certification Guide**
- **Personal Information Protection Act (PIPA)**

### Technical Validation

- **HTML Validator**: https://validator.w3.org/
- **Schema.org Validator**: https://validator.schema.org/
- **Google Rich Results Test**: https://search.google.com/test/rich-results

---

## ✅ Success Criteria

### Completion Criteria

- [ ] All 99 terminology replacements completed and validated
- [ ] 55-75 regulatory context enhancements added
- [ ] All 68 files have `inLanguage: ko` in Schema.org
- [ ] Zero HTML validation errors
- [ ] Zero Schema.org validation errors
- [ ] 100% terminology consistency achieved
- [ ] Native speaker approval obtained
- [ ] Documentation updated (Status and Guide)

### Quality Gates

- [ ] All automated tests pass
- [ ] Manual review of 10% sample shows quality
- [ ] Native Korean speaker confirms natural flow
- [ ] Accessibility maintained (WCAG 2.1 AA)
- [ ] Mobile responsiveness preserved
- [ ] No broken links introduced
- [ ] SEO metadata preserved

---

## 📧 Contacts & Support

**Questions or Issues:**
- GitHub Issues: https://github.com/Hack23/homepage/issues
- Label: `korean-translation`

**Native Speaker Review:**
- Contact: [To be determined]
- Role: Final quality validation

**Project Owner:**
- Hack23 AB Translation Team
- GitHub: @Hack23

---

**Document Control:**
- **Version**: 1.0
- **Status**: ✅ Ready for Implementation
- **Created**: 2025-12-18
- **Next Review**: After Phase 1 completion
- **Approved By**: Hack23 AB Translation Team

---

*This plan provides a comprehensive, surgical approach to fixing Korean translation inconsistencies while minimizing risk and ensuring professional quality.*

**🇰🇷 Professional Korean cybersecurity translations for the global market.**

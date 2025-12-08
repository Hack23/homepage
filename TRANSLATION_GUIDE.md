# Translation Guide for CIA Blog Posts

## Overview

This guide provides translation patterns and terminology for translating the CIA blog series into Arabic and Hebrew.

## Technical Terminology Reference

### Core Security Concepts

| English | Arabic | Hebrew |
|---------|--------|--------|
| CIA Triad | مثلث أمن المعلومات | משולש CIA |
| Confidentiality | السرية | סודיות |
| Integrity | السلامة | שלמות |
| Availability | التוافر | זמינות |
| Security | الأمن | אבטחה |
| Transparency | الشفافية | שקיפות |
| Architecture | هندسة | ארכיטקטורה |

### DevSecOps & CI/CD

| English | Arabic | Hebrew |
|---------|--------|--------|
| CI/CD | تكامل وتسليم البرمجيات المستمر | CI/CD |
| Continuous Deployment | النشر المستمر | פריסה רצופה |
| DevSecOps | DevSecOps | DevSecOps |
| GitHub Actions | إجراءات GitHub | GitHub Actions |
| State Machine | آلة الحالات | מכונת מצבים |
| Workflow | سير عمل | זרימת עבודה |
| Pipeline | خط أنابيب | צינור |

### Intelligence & Monitoring

| English | Arabic | Hebrew |
|---------|--------|--------|
| OSINT | المعلومات الاستخبارية مفتوحة المصدر | מודיעין ממקורות גלויים |
| Intelligence Agency | وكالة المخابرات | סוכנות מודיעין |
| Monitoring | المراقبة | ניטור |
| Parliament | البرلمان | פרלמנט |
| Citizen | المواطن | אזרח |
| Democracy | الديمقراطية | דמוקרטיה |

### Software Architecture

| English | Arabic | Hebrew |
|---------|--------|--------|
| Container | حاوية | מכולה |
| Service Layer | طبقة الخدمة | שכבת שירות |
| Data Model | نموذج البيانات | מודל נתונים |
| API | واجهة برمجة التطبيقات | API |
| Database | قاعدة البيانات | מסד נתונים |
| Entity | كيان | ישות |

## Example Translation: blog-cia-workflows

### English Title:
```
CIA Workflows: Five-Stage CI/CD & State Machine Democracy
```

### Arabic Translation:
```
سير عمل CIA: الديمقراطية ذات المراحل الخمس لتكامل وتسليم البرمجيات المستمر وآلات الحالات
```

### Hebrew Translation:
```
זרימות עבודה CIA: דמוקרטיה של CI/CD בחמישה שלבים ומכונות מצבים
```

### English Description:
```
DevSecOps sacred geometry: Five CI/CD workflows orchestrating democratic transparency through automated state machine transitions, GitHub Actions security scanning, and continuous deployment patterns.
```

### Arabic Translation:
```
الهندسة المقدسة لـ DevSecOps: خمسة سير عمل لتكامل وتسليم البرمجيات المستمر تنسق الشفافية الديمقراطية من خلال انتقالات آلات الحالات الآلية، ومسح الأمن عبر إجراءات GitHub، وأنماط النشر المستمر.
```

### Hebrew Translation:
```
הגיאומטריה הקדושה של DevSecOps: חמש זרימות עבודה של CI/CD המתזמרות שקיפות דמוקרטית דרך מעברי מכונת מצבים אוטומטיים, סריקת אבטחה של GitHub Actions, ודפוסי פריסה רצופה.
```

## Translation Rules

### 1. Preserve Technical Terms
Keep certain terms in English when widely used in technical contexts:
- GitHub, GitHub Actions
- CI/CD (can add Arabic/Hebrew explanation)
- DevSecOps (widely recognized)
- CodeQL
- SLSA
- SBOM
- Maven

### 2. Code Blocks Stay English
All code examples, command-line snippets, and technical examples remain in English with LTR direction (CSS handles this automatically).

```yaml
# This stays in English
name: Verify & Release
on:
  push:
    tags:
      - '*'
```

### 3. URLs and Links
All URLs remain in English:
```html
<a href="https://github.com/Hack23/cia">Citizen Intelligence Agency</a>
```

Translate the link text:
```html
<!-- Arabic -->
<a href="https://github.com/Hack23/cia">وكالة المخابرات المواطنة</a>

<!-- Hebrew -->
<a href="https://github.com/Hack23/cia">סוכנות המודיעין האזרחי</a>
```

### 4. Discordian Philosophy
Maintain the philosophical and metaphorical language:

**English:**
"When democracies hide in darkness, transparency becomes revolution."

**Arabic:**
"عندما تختبئ الديمقراطيات في الظلام، تصبح الشفافية ثورة."

**Hebrew:**
"כאשר דמוקרטיות מסתתרות בחושך, השקיפות הופכת למהפכה."

### 5. Breadcrumb Navigation

**English:**
```html
<li class="breadcrumb-item">
  <a href="/">Home</a>
</li>
<li class="breadcrumb-item">
  <a href="/blog.html">Blog</a>
</li>
```

**Arabic:**
```html
<li class="breadcrumb-item">
  <a href="/">الصفحة الرئيسية</a>
</li>
<li class="breadcrumb-item">
  <a href="/blog.html">المدونة</a>
</li>
```

**Hebrew:**
```html
<li class="breadcrumb-item">
  <a href="/">בית</a>
</li>
<li class="breadcrumb-item">
  <a href="/blog.html">בלוג</a>
</li>
```

### 6. Footer Elements

Footer remains largely in English with language selectors, but copyright text can be translated:

**Arabic:**
```html
<p>&copy; 2008-2025 Hack23 AB. جميع الحقوق محفوظة. | مرخص بموجب <a href="LICENSE">Apache 2.0</a></p>
```

**Hebrew:**
```html
<p>&copy; 2008-2025 Hack23 AB. כל הזכויות שמורות. | רישיון תחת <a href="LICENSE">Apache 2.0</a></p>
```

## Quality Checklist

For each translated file:

- [ ] Title translated accurately
- [ ] Meta description translated
- [ ] Keywords translated/adapted
- [ ] Breadcrumb navigation translated
- [ ] All headings (h1, h2, h3) translated
- [ ] Paragraph content translated
- [ ] Technical terms consistent with glossary
- [ ] Code blocks remain in English/LTR
- [ ] Links remain functional
- [ ] Link text translated
- [ ] Philosophical language preserved
- [ ] Schema.org articleBody snippet translated
- [ ] HTML validates
- [ ] RTL layout renders correctly

## Workflow

1. **Start with metadata** (title, description, keywords)
2. **Translate headings** to understand structure
3. **Translate body paragraphs** section by section
4. **Verify technical terms** against glossary
5. **Keep code blocks** in English
6. **Update schema.org** structured data
7. **Validate HTML** with htmlhint
8. **Visual review** in browser

## Tools Recommended

- **Translation Memory:** Trados, MemoQ, or Crowdin
- **Terminology Database:** Maintain consistent term usage
- **HTML Validator:** htmlhint, W3C Validator
- **Browser Testing:** Chrome, Firefox, Safari
- **RTL Testing:** Test in Arabic/Hebrew locale

## Contact

For questions about technical terminology or translation approach:
- GitHub Issue: [Issue Number]
- Repository: https://github.com/Hack23/homepage
- Documentation: ARABIC_HEBREW_TRANSLATION_STATUS.md

---

**Last Updated:** 2025-12-08

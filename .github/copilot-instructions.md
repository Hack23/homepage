# GitHub Copilot Custom Instructions

Static HTML/CSS website for **Hack23 AB** (Swedish cybersecurity consulting). ~105 English pages, 13 languages, deployed to AWS S3 + CloudFront via GitHub Actions.

## Required Reading

**Read at session start:** `.github/workflows/copilot-setup-steps.yml`, `.github/copilot-mcp.json`, `README.md`

## Skills & Agents

- **58 skills** in `.github/skills/` auto-load via Copilot — follow their MUST/MUST NOT rules. See `.github/skills/INDEX.md`.
- **8 agents** in `.github/agents/` — delegate specialized tasks to them.

## Key Rules

**MUST:**
- Follow skills library rules (security, accessibility, architecture, quality)
- Maintain Lighthouse scores: Performance >90, Accessibility 100, SEO 100
- Use semantic HTML5, WCAG 2.1 AA, existing CSS variables
- Test locally, validate HTML/CSS, check responsive design before committing
- Update localized versions (`_sv`, `_ko`, `_ar`, etc.) for structural changes
- Align with [ISMS-PUBLIC](https://github.com/Hack23/ISMS-PUBLIC) policies

**MUST NOT:**
- Create markdown files unless explicitly requested — work in memory
- Hard-code secrets or use deprecated algorithms (MD5, SHA-1, DES)
- Break accessibility, reduce Lighthouse scores, or add unrequested features
- Modify `.github/workflows/` without careful consideration

## Project Structure

- **Root HTML files**: `index.html`, `cia-docs.html`, etc. (language variants use `_sv`, `_ko`, `_ar` suffixes)
- **`styles.css`**: Single CSS file — use existing custom properties
- **`budget.json`**: Lighthouse performance budget
- **`.github/skills/`**: 58 production-ready skills
- **`.github/agents/`**: 8 specialized custom agents

## Autonomy

- Default to skills library best practices — don't ask for confirmation on standard patterns
- Fix security, accessibility, and broken-link issues proactively
- Complete tasks fully: update docs, translations, and related files
- Only ask when requirements are genuinely ambiguous or a major architectural decision is needed

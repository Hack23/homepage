# GitHub Copilot Custom Instructions

Static HTML/CSS website for **Hack23 AB** (Swedish cybersecurity consulting). ~105 English pages, 13 languages, deployed to AWS S3 + CloudFront via GitHub Actions.

## Required Reading

**Read at session start:** `.github/workflows/copilot-setup-steps.yml`, `.github/copilot-mcp.json`, `README.md`

## Skills & Agents

- **58 skills** in `.github/skills/` auto-load via Copilot — follow their MUST/MUST NOT rules. See `.github/skills/INDEX.md`.
- **8 agents** in `.github/agents/` — delegate specialized tasks to them. See `.github/agents/INDEX.md`.

## 🔐 ISMS Policy Anchors (authoritative source of rules)

Every change MUST be reconcilable with the public ISMS. When in doubt, consult:

| Policy | When it governs your change |
|--------|----------------------------|
| [Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md) | Overall framework, risk appetite, roles, accountability |
| [Secure Development Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Secure_Development_Policy.md) | **Any code, IaC, CI/CD, or supply-chain change** — input validation, authN/Z, cryptography, error handling, testing, deps, code review |
| [Open Source Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Open_Source_Policy.md) | Adding dependencies (license check: Apache-2.0/MIT/BSD/ISC/MPL-2.0 default; AGPL/SSPL/BSL forbidden without CEO approval), SBOM, SLSA L3, OpenSSF Scorecard ≥ 7.0, REUSE, FOSSA, README badges |
| [Access Control Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Access_Control_Policy.md) | Auth, secrets, RBAC, MFA, session management |
| [Cryptographic Controls Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Cryptographic_Controls_Policy.md) | TLS 1.2+, AES-256, RSA-2048+, SHA-256+ only; MD5/SHA-1/DES/3DES/SSL/TLS<1.2 banned |
| [Data Classification Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Data_Classification_Policy.md) | Any data handling (logging, analytics, forms, translations) — Public / Internal / Confidential / Restricted |
| [AI Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/AI_Policy.md) | Agent, LLM, MCP, Copilot workflow, or AI-generated content changes |
| [Change Management Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Change_Management_Policy.md) | Deploys, workflow edits, infrastructure changes |
| [Acceptable Use Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Acceptable_Use_Policy.md) | Public artefacts, community interactions, third-party services |

## 🔁 Secure SDLC (Plan → Design → Build → Test → Deploy → Operate)

Every PR description SHOULD identify which SDLC phase(s) it touches and which Secure Development Policy control it satisfies:

| Phase | Required gates (CI-enforced where possible) |
|-------|--------------------------------------------|
| **Plan** | Risk assessment, data classification, threat hypotheses |
| **Design** | Architecture + SECURITY_ARCHITECTURE.md updates, STRIDE/LINDDUN threat model, control mapping (ISO 27001 A.x / NIST CSF / CIS) |
| **Build** | Secure coding (input validation allowlist, output encoding, parameterised queries), zero hardcoded secrets, peer review |
| **Test** | HTML/CSS validation, Lighthouse (Perf ≥ 90, A11y 100, SEO 100), axe a11y, OWASP ZAP baseline clean, SAST/dependency scan |
| **Deploy** | SLSA L3 provenance, SBOM published, signed artefacts, CloudFront cache warmed, security headers intact |
| **Operate** | Log review, incident-response readiness, vulnerability SLA tracking (Crit 7d / High 30d / Med 90d / Low 180d) |

## Key Rules

**MUST:**
- Follow skills library rules (see `.github/skills/INDEX.md` — 58 skills across 12 categories)
- Maintain Lighthouse scores: Performance ≥ 90, Accessibility 100, SEO 100
- Use semantic HTML5, WCAG 2.1 AA, existing CSS custom properties in `styles.css`
- Validate HTML/CSS + test responsive behaviour (320px → 4K) before committing
- Update localized versions (`_sv`, `_ko`, `_ar`, `_zh`, `_de`, `_fi`, `_fr`, `_es`, `_hi`, `_ja`, `_pt`, `_ru`, `_it`) for structural changes
- Preserve CSP, SRI, HTTPS-only, no inline scripts/styles
- Verify dependency licenses + scan for vulnerabilities before adding anything (see Open Source Policy)
- Align every change with ISMS-PUBLIC policies above

**MUST NOT:**
- Create markdown files unless explicitly requested — work in memory
- Hard-code secrets, API keys, tokens, or connection strings
- Use deprecated algorithms (MD5, SHA-1, DES, 3DES, SSL, TLS < 1.2, ECB)
- Break accessibility, reduce Lighthouse scores, introduce CLS/LCP regressions
- Add external dependencies from unverified sources or with incompatible licenses (AGPL/SSPL/BSL/PolyForm without CEO approval)
- Modify `.github/workflows/` without careful consideration (affects SLSA provenance chain)
- Expose Internal/Confidential/Restricted data in public HTML

## Project Structure

- **Root HTML files**: `index.html`, `cia-docs.html`, `cia-compliance-manager-docs.html`, `black-trigram-docs.html`, etc. Language variants use suffixes (`_sv`, `_ko`, `_ar`, …)
- **`styles.css`**: Single CSS file — use existing custom properties, never duplicate variables
- **`budget.json`**: Lighthouse performance budget — respect or raise deliberately with justification
- **`.github/skills/`**: 58 production-ready skills (security, architecture, quality, deployment, compliance, operations, governance, business, intelligence, development, documentation, integration)
- **`.github/agents/`**: 8 specialized custom agents (task-agent, hagbard-celine, simon-moon, george-dorn, ui-enhancement-specialist, business-development-specialist, marketing-specialist, political-analyst)

## Autonomy

- **Default to skills + ISMS policies** — they encode best practice; no need to re-derive or ask
- **Fix proactively**: security, accessibility, broken links, dead translations, license issues
- **Complete changes fully**: docs, all 13 translations, architecture portfolio, related issues
- **Only ask** for: requirement ambiguity, strategic architectural pivots, non-standard license requests, cost-impacting infrastructure changes

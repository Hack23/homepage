# GitHub Copilot Custom Instructions

You are assisting with a static HTML/CSS website project for Hack23 AB, a Swedish cybersecurity consulting company founded in 2025. This is a professional corporate website focused on clear security messaging, accessible design, and radical transparency.

## Project Overview

- **Technology Stack**: Static HTML5/CSS3 website
- **Deployment**: AWS S3 + CloudFront (automated via GitHub Actions)
- **Languages**: 14 language variants - English (primary), Swedish (`_sv`), Korean (`_ko`), Arabic (`_ar`), Chinese (`_zh`), Danish (`_da`), Dutch (`_nl`), Finnish (`_fi`), French (`_fr`), German (`_de`), Hebrew (`_he`), Japanese (`_ja`), Norwegian (`_no`), Spanish (`_es`)
- **Purpose**: Corporate website showcasing cybersecurity services, open-source projects, and company information
- **ISMS**: Public ISMS v3.2 (effective 2026-01-25) at https://github.com/Hack23/ISMS-PUBLIC

## Core Guidelines

### 1. Code Quality and Consistency
- Maintain consistency with established design patterns and HTML/CSS structure
- Keep code clean, minimal, and well-organized
- Use semantic HTML5 elements appropriately
- Follow existing naming conventions for files and CSS classes
- Ensure responsive design works across all viewport sizes
- Use existing CSS variables and utility classes where possible

### 2. Content and Features
- **Do not add new features** — only fix bugs and improve existing content
- Maintain accuracy of technical information and company details
- Keep security terminology clear and accessible to non-technical audiences
- Provide microcopy and tooltips where needed to explain complex security concepts
- Preserve existing content structure and navigation patterns

### 3. Accessibility (WCAG 2.1 AA)
- Ensure all interactive elements are keyboard accessible
- Maintain proper heading hierarchy (h1-h6)
- Provide meaningful alt text for images
- Ensure sufficient color contrast ratios
- Test with screen reader compatibility in mind
- Use ARIA labels and roles where appropriate

### 4. Internationalization
- When editing content, check if localized versions exist (`index_sv.html`, `index_ko.html`, etc.)
- Maintain consistency across language versions for structural changes
- Preserve language-specific content and cultural adaptations
- Ensure proper lang attributes are set on HTML elements

### 5. Security and Privacy
- This is a public-facing static website with no sensitive data processing
- Maintain existing security headers and CSP policies
- Keep external dependencies minimal
- Follow secure coding practices for any JavaScript additions
- Ensure all external links use HTTPS

### 6. Testing and Validation
- The deployment pipeline includes:
  - **HTML/CSS/JS Minification**: Automated via GitHub Actions
  - **Lighthouse Audits**: Performance, accessibility, SEO checks (budget defined in `budget.json`)
  - **ZAP Security Scan**: Automated security vulnerability scanning
- Test locally before committing when possible
- Verify responsive design across different screen sizes
- Check that changes don't break existing functionality

### 7. Repository Structure
- **Root HTML files**: Main pages (`index.html`, `cia-docs.html`, `blog*.html`, `discordian-*.html`, etc.)
- **`styles.css`**: Single CSS file for all styling
- **`screenshots/`**: Visual assets and documentation images
- **`.github/workflows/`**: CI/CD configuration (do not modify without careful consideration)
- **`.github/agents/`**: 8 custom Copilot agent profiles with Discordian philosophy
- **Language variants**: 13 localized versions with suffixes `_sv`, `_ko`, `_ar`, `_da`, `_de`, `_es`, `_fi`, `_fr`, `_he`, `_ja`, `_nl`, `_no`, `_zh`

### 8. Brand and Messaging
- Emphasize **radical transparency** and **open-source security** as core values
- Highlight **practical security solutions** that enable innovation, not hinder it
- Maintain professional tone appropriate for enterprise cybersecurity consulting
- Reference the **Public ISMS v3.2 (2026-01-25)** as a key differentiator - https://github.com/Hack23/ISMS-PUBLIC
- Preserve links to projects: Black Trigram, CIA Compliance Manager, Citizen Intelligence Agency
- **Discordian philosophy**: "Think for yourself, question authority" - inspired by Principia Discordia

### 9. Common Tasks

#### Fixing Content Issues
- Verify changes in both English and localized versions if applicable
- Maintain consistent terminology across all pages
- Keep external links up-to-date and functional

#### CSS Changes
- Add styles to the existing `styles.css` file
- Use existing CSS custom properties (variables) where possible
- Ensure changes don't break responsive layouts
- Test across different browsers if possible

#### Accessibility Improvements
- Add or improve ARIA labels for screen readers
- Enhance keyboard navigation support
- Improve color contrast where needed
- Add descriptive alt text for images

## Focus Areas

**Stability, Clarity, and Correctness** — These three principles should guide every change. This is a professional corporate website representing a cybersecurity consulting company, so quality and accuracy are paramount.

## Need Help?

When in doubt:
- Preserve existing structure and patterns
- Make minimal, surgical changes
- Test accessibility and responsive design
- Check if localized versions need the same update
- Verify that external links and references are still accurate

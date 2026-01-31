---
name: accessibility-wcag
description: WCAG 2.1 AA compliance requirements including semantic markup, keyboard navigation, ARIA labels, and color contrast
license: Apache-2.0
---

# Accessibility WCAG Skill

## Purpose

This skill ensures all web content meets WCAG 2.1 Level AA standards for accessibility, making websites usable by people with disabilities including visual, auditory, motor, and cognitive impairments.

## Rules

### WCAG 2.1 AA Requirements

WCAG is organized around four principles (POUR):
1. **Perceivable** - Information must be presentable in ways users can perceive
2. **Operable** - Interface must be operable by all users
3. **Understandable** - Information and operation must be understandable
4. **Robust** - Content must be robust enough for assistive technologies

### Perceivable Requirements

#### Text Alternatives (1.1)

**MUST:**
- Provide `alt` text for all meaningful images
- Use empty `alt=""` for decorative images
- Provide captions for audio/video content
- Provide transcripts for audio-only content
- Use descriptive link text (not "click here")

**Examples:**
```html
<!-- GOOD: Meaningful alt text -->
<img src="security-audit.jpg" alt="Security professional reviewing network logs on dual monitors">

<!-- GOOD: Decorative image -->
<img src="divider.png" alt="" aria-hidden="true">

<!-- BAD: Missing alt -->
<img src="chart.png">

<!-- BAD: Useless alt text -->
<img src="photo.jpg" alt="Image">
```

#### Time-based Media (1.2)

**MUST:**
- Provide captions for videos (prerecorded and live)
- Provide audio descriptions for video content
- Provide transcripts for audio content

#### Adaptable Content (1.3)

**MUST:**
- Use semantic HTML (headings, lists, tables correctly)
- Ensure content is accessible without CSS
- Don't rely on sensory characteristics alone (color, shape, position)
- Use proper reading order in DOM

**Examples:**
```html
<!-- GOOD: Semantic markup -->
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
  </ul>
</nav>

<!-- BAD: Div soup -->
<div class="nav">
  <div class="item"><a href="/">Home</a></div>
  <div class="item"><a href="/about">About</a></div>
</div>
```

#### Distinguishable Content (1.4)

**MUST:**
- Maintain color contrast ratio of at least 4.5:1 for normal text
- Maintain color contrast ratio of at least 3:1 for large text (18pt+ or 14pt+ bold)
- Don't use color alone to convey information
- Allow text resize up to 200% without loss of functionality
- Avoid background audio that can't be paused/stopped
- Ensure text can be selected and copied

**Color Contrast Examples:**
```css
/* GOOD: High contrast (7:1) */
.text {
  color: #000000; /* Black */
  background-color: #FFFFFF; /* White */
}

/* GOOD: Sufficient contrast (4.6:1) */
.link {
  color: #0066CC; /* Blue */
  background-color: #FFFFFF; /* White */
}

/* BAD: Insufficient contrast (2.3:1) */
.subtle-text {
  color: #CCCCCC; /* Light gray */
  background-color: #FFFFFF; /* White */
}
```

### Operable Requirements

#### Keyboard Accessible (2.1)

**MUST:**
- Make all functionality available via keyboard
- Provide visible focus indicators
- Don't create keyboard traps
- Ensure logical tab order
- Provide keyboard shortcuts for complex interfaces

**Examples:**
```html
<!-- GOOD: Button is keyboard accessible -->
<button onclick="submitForm()">Submit</button>

<!-- BAD: Div onClick is not keyboard accessible -->
<div onclick="submitForm()">Submit</div>

<!-- BETTER: If you must use div, add role and tabindex -->
<div role="button" tabindex="0" onclick="submitForm()" onkeypress="handleKeyPress(event)">
  Submit
</div>
```

```css
/* GOOD: Visible focus indicator */
a:focus,
button:focus {
  outline: 2px solid #0066CC;
  outline-offset: 2px;
}

/* BAD: Removing focus outline without replacement */
*:focus {
  outline: none; /* Never do this without providing alternative! */
}
```

#### Enough Time (2.2)

**MUST:**
- Allow users to turn off, adjust, or extend time limits
- Provide pause, stop, hide for auto-updating content
- No time limits unless essential (auctions, real-time games)

#### Seizures and Physical Reactions (2.3)

**MUST NOT:**
- Use content that flashes more than 3 times per second
- Create large flashing areas

#### Navigable (2.4)

**MUST:**
- Provide skip links to bypass repeated content
- Use descriptive page titles
- Ensure logical focus order
- Provide clear link purposes
- Offer multiple ways to navigate (menu, search, sitemap)
- Provide visible focus indicators
- Use clear headings and labels

**Examples:**
```html
<!-- GOOD: Skip link -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<nav>...</nav>

<main id="main-content">...</main>

<!-- GOOD: Descriptive title -->
<title>Security Services - ISO 27001 Implementation | Hack23</title>

<!-- BAD: Generic title -->
<title>Services</title>
```

#### Input Modalities (2.5)

**MUST:**
- Ensure touch targets are at least 44×44 pixels
- Don't rely on device motion alone
- Allow cancellation of pointer events
- Make clickable label text match accessible name

### Understandable Requirements

#### Readable (3.1)

**MUST:**
- Specify language of page with `lang` attribute
- Specify language of passages that differ from page language
- Keep content at appropriate reading level (when possible)

**Examples:**
```html
<!-- GOOD: Language specified -->
<html lang="en">

<!-- GOOD: Foreign language phrase -->
<p>The phrase <span lang="fr">je ne sais quoi</span> is French.</p>
```

#### Predictable (3.2)

**MUST:**
- Don't change context on focus
- Don't change context on input (without warning)
- Use consistent navigation across pages
- Use consistent identification of components

#### Input Assistance (3.3)

**MUST:**
- Identify input errors clearly
- Provide labels or instructions for user input
- Provide error suggestions when possible
- Prevent errors in legal/financial transactions
- Allow review/confirmation before final submission

**Examples:**
```html
<!-- GOOD: Clear label and error -->
<label for="email">Email Address *</label>
<input type="email" id="email" aria-required="true" aria-describedby="email-error">
<span id="email-error" class="error" role="alert">
  Please enter a valid email address (e.g., name@example.com)
</span>

<!-- GOOD: Required field indicator -->
<label for="password">
  Password *
  <span class="required-note">(required)</span>
</label>
<input type="password" id="password" aria-required="true">
```

### Robust Requirements

#### Compatible (4.1)

**MUST:**
- Ensure HTML is valid (no duplicate IDs, proper nesting)
- Use ARIA correctly (roles, states, properties)
- Provide name, role, value for all UI components
- Ensure status messages can be programmatically determined

**ARIA Examples:**
```html
<!-- GOOD: ARIA for custom component -->
<div role="tablist" aria-label="Account settings">
  <button role="tab" aria-selected="true" aria-controls="panel-1" id="tab-1">
    Profile
  </button>
  <button role="tab" aria-selected="false" aria-controls="panel-2" id="tab-2">
    Security
  </button>
</div>
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">
  <!-- Profile content -->
</div>
<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden>
  <!-- Security content -->
</div>

<!-- GOOD: Status message -->
<div role="status" aria-live="polite" aria-atomic="true">
  Changes saved successfully
</div>
```

## ARIA Best Practices

**Use ARIA When:**
- Native HTML element doesn't exist for your component
- Need to enhance semantic meaning
- Need to communicate state or property not available in HTML

**ARIA Landmarks:**
```html
<header role="banner">
<nav role="navigation" aria-label="Main navigation">
<main role="main">
<aside role="complementary">
<footer role="contentinfo">
```

**ARIA States and Properties:**
- `aria-label` - Provides accessible name
- `aria-labelledby` - References element that labels this one
- `aria-describedby` - References element that describes this one
- `aria-hidden` - Hides element from screen readers
- `aria-live` - Announces dynamic content changes
- `aria-expanded` - Indicates if expandable element is open
- `aria-pressed` - Indicates toggle button state
- `aria-current` - Indicates current item in set

## Testing Checklist

**MUST TEST:**
1. **Keyboard Navigation**
   - Tab through all interactive elements
   - Use Enter/Space to activate buttons/links
   - Verify visible focus indicators
   - Check for keyboard traps

2. **Screen Reader**
   - Test with NVDA (Windows), VoiceOver (Mac), or JAWS
   - Verify all content is announced
   - Check heading structure
   - Test form labels and error messages

3. **Color Contrast**
   - Use WebAIM Contrast Checker
   - Test all text/background combinations
   - Check focus indicators

4. **Zoom/Resize**
   - Zoom to 200% and verify functionality
   - Test with browser text-only zoom
   - Verify responsive design works

5. **Automated Tools**
   - WAVE (browser extension)
   - axe DevTools
   - Lighthouse accessibility audit
   - Pa11y

## Common Accessibility Errors

### 1. Missing Alt Text
```html
<!-- BAD -->
<img src="logo.png">

<!-- GOOD -->
<img src="logo.png" alt="Hack23 Cybersecurity">
```

### 2. Poor Color Contrast
```css
/* BAD: 2.5:1 ratio */
color: #999999;
background: #FFFFFF;

/* GOOD: 7:1 ratio */
color: #333333;
background: #FFFFFF;
```

### 3. Missing Form Labels
```html
<!-- BAD -->
<input type="text" placeholder="Email">

<!-- GOOD -->
<label for="email">Email</label>
<input type="text" id="email">
```

### 4. Empty Links
```html
<!-- BAD -->
<a href="report.pdf">
  <img src="pdf-icon.png">
</a>

<!-- GOOD -->
<a href="report.pdf">
  <img src="pdf-icon.png" alt="Download Annual Report (PDF, 2MB)">
</a>
```

### 5. Non-descriptive Link Text
```html
<!-- BAD -->
<a href="/services">Click here</a> for our services.

<!-- GOOD -->
<a href="/services">View our cybersecurity services</a>
```

## Related ISMS Policies

- **[Information Security Policy](https://github.com/Hack23/ISMS-PUBLIC/blob/main/Information_Security_Policy.md)** - Accessibility as part of service delivery

## Related Documentation

- [accessibility-statement.html](../../../../accessibility-statement.html) - Published accessibility statement
- [html-css-best-practices SKILL.md](../html-css-best-practices/SKILL.md) - Semantic HTML foundation

## Resources

- **WCAG 2.1**: https://www.w3.org/WAI/WCAG21/quickref/
- **WebAIM**: https://webaim.org/
- **A11Y Project**: https://www.a11yproject.com/
- **MDN Accessibility**: https://developer.mozilla.org/en-US/docs/Web/Accessibility

## Accessibility Statement

Every website MUST include an accessibility statement at `/accessibility-statement.html` that includes:
- Commitment to accessibility
- WCAG 2.1 AA conformance claim
- Known issues and limitations
- Contact information for accessibility concerns
- Date of last review

---
name: osint-methods
description: Open Source Intelligence (OSINT) collection, analysis, and verification methods for political intelligence, security research, and transparency projects
license: Apache-2.0
---

# OSINT Methods Skill

## Purpose

Provides ethical Open Source Intelligence (OSINT) methodologies for political analysis, security research, and transparency projects, emphasizing verification, privacy protection, and responsible disclosure.

## Rules

### OSINT Principles (MUST Follow)

**Core Principles:**
```markdown
1. Legality & Ethics
   - MUST only use publicly available information
   - MUST NOT hack, breach, or social engineer
   - MUST respect privacy and data protection laws (GDPR)
   - MUST follow responsible disclosure for vulnerabilities
   - MUST NOT collect or retain personal data unnecessarily

2. Verification & Accuracy
   - MUST verify information from multiple sources
   - MUST distinguish fact from opinion
   - MUST track source credibility and bias
   - MUST document collection methodology
   - MUST correct errors promptly

3. Privacy & Security
   - MUST anonymize sensitive information
   - MUST use VPN/Tor when appropriate
   - MUST protect source confidentiality
   - MUST secure collected data
   - MUST dispose of data appropriately

4. Transparency & Attribution
   - MUST cite sources and methodology
   - MUST disclose limitations and biases
   - MUST distinguish between collection and analysis
   - MUST provide context for findings
```

### OSINT Collection Framework

**Intelligence Cycle:**
```markdown
1. Planning & Direction
   - Define intelligence requirements
   - Identify information gaps
   - Prioritize collection efforts
   - Establish ethical boundaries

2. Collection
   - Gather data from public sources
   - Document source metadata
   - Preserve digital evidence
   - Maintain chain of custody

3. Processing & Exploitation
   - Organize collected information
   - Extract relevant data points
   - Convert formats as needed
   - Tag and categorize findings

4. Analysis & Production
   - Verify information accuracy
   - Identify patterns and relationships
   - Contextualize findings
   - Generate intelligence products

5. Dissemination & Feedback
   - Share findings with stakeholders
   - Protect sensitive information
   - Solicit feedback and questions
   - Refine collection priorities
```

### OSINT Sources & Categories

**Public Records & Databases:**
```markdown
Government Sources:
- Corporate registries (Bolagsverket in Sweden)
- Public procurement databases
- Court filings and legal documents
- Parliamentary records and votes
- Freedom of Information (FOI) responses
- Property and land records
- Regulatory filings

International Sources:
- EU transparency register
- UN databases
- World Bank open data
- ICIJ databases (Offshore Leaks, Paradise Papers)
```

**Digital Footprints:**
```markdown
Social Media:
- LinkedIn (professional networks)
- Twitter/X (public statements, opinions)
- Facebook (groups, pages, events)
- Instagram (visual content, locations)
- YouTube (video content, comments)

Websites & Domains:
- WHOIS lookups
- Historical snapshots (Wayback Machine)
- SSL certificate transparency logs
- DNS records and subdomains
- Metadata analysis
```

**News & Media:**
```markdown
Traditional Media:
- News articles and archives
- Press releases
- Broadcast transcripts
- Investigative reports

Alternative Media:
- Blogs and independent journalists
- Podcasts and video channels
- Newsletters
- Community forums
```

**Technical Intelligence:**
```markdown
Network Intelligence:
- IP address geolocation
- Autonomous System (AS) information
- BGP routing data
- Shodan/Censys IoT/device searches

Document Intelligence:
- Leaked documents (WikiLeaks, SecureDrop)
- FOIA documents
- Academic research papers
- Technical reports and whitepapers
```

### OSINT Tools & Techniques

**Search & Discovery:**
```markdown
Google Dorking:
- site:gov.se "contract award"
- filetype:pdf "annual report" Sweden
- intitle:"index of" procurement
- inurl:admin site:example.com

Social Media Tools:
- Twitter Advanced Search
- LinkedIn Sales Navigator
- Facebook Graph Search
- Instagram location search
- Reddit search and archives

Specialized Search:
- Shodan (IoT devices, exposed services)
- Censys (internet-wide scans)
- FOCA (metadata extraction)
- Maltego (link analysis)
- Recon-ng (OSINT framework)
```

**Verification Techniques:**
```markdown
Image Verification:
- Reverse image search (Google, TinEye, Yandex)
- EXIF metadata analysis
- Geolocation from visual clues
- Photo forensics (FotoForensics)

Account Verification:
- Cross-platform username search
- Account creation date verification
- Follower/network analysis
- Content history review

Document Verification:
- Metadata analysis
- Format forensics
- Language and style analysis
- Cross-reference with known documents
```

### OSINT Analysis Methods

**Link Analysis:**
```markdown
Network Mapping:
- Identify relationships between entities
- Map organizational structures
- Trace financial flows
- Visualize influence networks

Tools:
- Maltego
- Gephi
- NodeXL
- i2 Analyst Notebook
```

**Timeline Analysis:**
```markdown
Chronological Mapping:
- Sequence events accurately
- Identify temporal patterns
- Correlate activities across sources
- Detect anomalies and gaps

Techniques:
- Event extraction from documents
- Date correlation across sources
- Activity pattern analysis
- Behavioral change detection
```

**Pattern Recognition:**
```markdown
Behavioral Patterns:
- Communication patterns
- Location patterns
- Financial patterns
- Social network patterns

Anomaly Detection:
- Unusual transactions
- Pattern breaks
- Timing anomalies
- Relationship changes
```

### GDPR Compliance in OSINT

**Data Protection Requirements:**
```markdown
Lawful Basis:
- MUST have legitimate interest or consent
- MUST conduct Data Protection Impact Assessment (DPIA)
- MUST document legal basis for processing

Data Minimization:
- MUST collect only necessary information
- MUST NOT retain data longer than needed
- MUST delete or anonymize when possible

Individual Rights:
- MUST provide transparency about collection
- MUST allow access, rectification, erasure requests
- MUST respect opt-out and do-not-track

Security Measures:
- MUST encrypt stored OSINT data
- MUST restrict access to authorized personnel
- MUST log and monitor data access
- MUST have breach notification procedures
```

### Responsible Disclosure

**Vulnerability Disclosure:**
```markdown
Process:
1. Identify security vulnerability in public system
2. Document finding with screenshots/evidence
3. Contact organization privately (security@domain)
4. Allow 90 days for remediation
5. Coordinate public disclosure if appropriate
6. Do NOT exploit or share exploit code

Example Message:
"I've identified a potential security issue in your system 
during research. I'd like to report it responsibly. Please 
confirm the best way to share details securely."
```

### OSINT Documentation Standards

**Research Documentation:**
```markdown
Collection Record:
- Source URL and access date
- Preservation method (screenshot, archive.org, PDF)
- Search queries or discovery method
- Relevance to intelligence requirement
- Initial assessment notes

Analysis Documentation:
- Analytical framework used
- Key findings and evidence
- Confidence level (High/Medium/Low)
- Alternative hypotheses considered
- Limitations and gaps
- Recommendations

Report Structure:
1. Executive Summary
2. Intelligence Requirements
3. Methodology
4. Findings (with evidence)
5. Analysis and Assessment
6. Confidence Levels
7. Recommendations
8. Appendices (sources, tools, raw data)
```

## Examples

### OSINT Research Request Template
```markdown
## Intelligence Requirement

**Topic**: [Specific question or information need]
**Purpose**: [How findings will be used]
**Priority**: High / Medium / Low
**Deadline**: [Date]

**Scope**:
- Geographic: [Countries, regions]
- Temporal: [Time period]
- Entities: [Organizations, individuals, topics]

**Constraints**:
- Legal: [GDPR, privacy laws]
- Ethical: [Sensitive topics, personal data]
- Technical: [Access limitations]

**Deliverable**: [Report format, briefing, database]
```

### Source Credibility Assessment
```markdown
## Source Evaluation

**Source**: [Name, URL, type]
**Date Accessed**: [YYYY-MM-DD]

**Credibility Factors**:
- Authority: [Subject matter expertise] ⭐⭐⭐⭐☆
- Accuracy: [Verification record] ⭐⭐⭐⭐⭐
- Objectivity: [Bias assessment] ⭐⭐⭐☆☆
- Currency: [Timeliness] ⭐⭐⭐⭐☆
- Coverage: [Depth and breadth] ⭐⭐⭐⭐☆

**Overall Rating**: 4/5 - Reliable with minor bias

**Notes**: [Specific observations about source reliability]
```

### OSINT Report Template
```markdown
# OSINT Report: [Topic]

**Classification**: Public / Internal / Confidential
**Date**: [YYYY-MM-DD]
**Analyst**: [Name]

## Executive Summary
[2-3 paragraph summary of key findings]

## Intelligence Requirements
[What questions this research aimed to answer]

## Methodology
- **Sources**: [Types of sources used]
- **Tools**: [OSINT tools employed]
- **Time Period**: [Research duration]
- **Limitations**: [Known gaps or constraints]

## Key Findings

### Finding 1: [Title]
**Confidence**: High / Medium / Low
**Evidence**: [Supporting information with sources]
**Analysis**: [What this means]

### Finding 2: [Title]
[Same structure]

## Assessment & Implications
[Analysis of what findings mean in context]

## Recommendations
[Actionable suggestions based on findings]

## Appendices
- Appendix A: Source List
- Appendix B: Methodology Details
- Appendix C: Raw Data
```

## Related Policies

- [Hack23 ISMS-PUBLIC](https://github.com/Hack23/ISMS-PUBLIC)
- [GDPR Compliance SKILL](../../compliance/gdpr/SKILL.md)
- [Data Classification SKILL](../../security/data-classification/SKILL.md)
- [Ethical Information Operations SKILL](../ethical-information-ops/SKILL.md)

## Related Documentation

- [political-analyst Agent](../../../agents/political-analyst.md)

## Tools & Resources

**OSINT Frameworks:**
- [OSINT Framework](https://osintframework.com/) - Tool directory
- [Bellingcat's Online Investigation Toolkit](https://docs.google.com/spreadsheets/d/18rtqh8EG2q1xBo2cLNyhIDuK9jrPGwYr9DI2UncoqJQ/)

**Training Resources:**
- Bellingcat's Online Investigation Workshops
- SANS SEC487: Open-Source Intelligence (OSINT) Gathering and Analysis
- Trace Labs OSINT Search Party Events

**Verification Tools:**
- InVID/WeVerify (video/image verification)
- Google Fact Check Explorer
- Full Fact (UK fact-checking)

**Privacy & Security:**
- Tor Browser
- ProtonVPN
- Tails OS (for sensitive research)

# Test Link Structure

## Purpose
This document tests whether the link paths work correctly.

## Test Links

From root to CLASSIFICATION.md:
- [Direct link](./CLASSIFICATION.md)
- [With anchor](./CLASSIFICATION.md#confidentiality-levels)

From a hypothetical Hack23AB/Marketing/Linkedin/ location to root CLASSIFICATION.md:
- Would need: `../../../CLASSIFICATION.md#confidentiality-levels`
  - One `..` to go from Linkedin to Marketing
  - Another `..` to go from Marketing to Hack23AB  
  - Another `..` to go from Hack23AB to root

Wait, let me recalculate:
- File at: `./Hack23AB/Marketing/Linkedin/LinkedIn_Analytics_Report_2025.md`
- Target: `./CLASSIFICATION.md`
- Path: `../../../CLASSIFICATION.md`
  - `..` from Linkedin → Marketing
  - `..` from Marketing → Hack23AB
  - `..` from Hack23AB → root

But the error shows: `../../CLASSIFICATION.md#confidentiality-levels`

This is WRONG - it's one `..` short! That's the issue!

## Correct Paths

For file at `./Hack23AB/Marketing/Linkedin/LinkedIn_Analytics_Report_2025.md`:
- To CLASSIFICATION.md: `../../../CLASSIFICATION.md#confidentiality-levels` (NOT `../../`)

For file at `./Hack23AB/Marketing/SearchEngines/Google/Google_Search_Console_Report_2025.md`:
- To CLASSIFICATION.md: `../../../../CLASSIFICATION.md#confidentiality-levels` (NOT `../../`)
- To Business_Strategy.md: `../../../../Business_Strategy.md` (NOT `../../`)
- To LinkedIn report: `../../Linkedin/LinkedIn_Analytics_Report_2025.md` (NOT `../Linkedin/`)

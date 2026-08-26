# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository publishes **legally operative privacy policies** for Prameya LLC apps as a static GitHub Pages site at https://prameyallc.github.io/privacy/. Each app has its own privacy policy because they handle data differently. Apps that process consumer health data also have separate Consumer Health Data Privacy Policies to comply with Washington's My Health My Data Act (RCW 19.373.020) and Nevada SB 370.

**Critical**: The published policies are live legal documents relied upon by shipping apps. Changes must be accurate, verified against app source code, and fetched from the live URL after deployment.

## Source-First Architecture

- **Source files**: Markdown files in `src/<app>/policy.md` and `src/<app>/health-data.md`
- **Generated files**: All `index.html` files in the repository root and app directories
- **Build process**: The Python generator (`src/build_privacy_site.py`) converts source markdown to standalone HTML

**Never edit generated HTML files directly** — they will be silently overwritten on the next build.

## Building the Site

```bash
python3 src/build_privacy_site.py src . https://prameyallc.github.io/privacy
```

This command:
- Reads markdown source from `src/`
- Outputs HTML to the repository root (`.`)
- Uses `https://prameyallc.github.io/privacy` as the canonical URL base
- Generates the hub index page listing all apps
- Creates `/support/` page from `src/support.md`
- Refuses to build if any accent color fails WCAG AA contrast (4.5:1)

## Repository Structure

```
src/
  <app>/
    policy.md         # Main privacy policy for the app
    health-data.md    # Consumer health data policy (only for health apps)
    _audit.md         # Source code audit notes (not published)
  build_privacy_site.py  # Static site generator
  README.md            # Build instructions and rules

<app>/
  index.html          # Generated main policy page
  health-data/
    index.html        # Generated consumer health data policy

index.html            # Generated hub page listing all apps
support/
  index.html          # Generated support/contact page
.nojekyll             # Prevents GitHub Pages from running Jekyll
```

## Apps Covered

Each app has distinct data-handling characteristics:

**Health apps** (have both `policy.md` and `health-data.md`):
- OmniSalub — chronic-condition companion
- OmniDent — dental photo analysis
- OmniDerm — skin journal
- OmniRx — medication education

**Other apps** (have only `policy.md`):
- OmniLex — legal document assistant
- OmniWealth — financial education
- OmniMathematics — discrete mathematics
- OmniBuild — construction reference
- OmniOps — personal discipline habits
- OmniAero — ACS ground school
- OmniPhysics — interactive physics lessons

## Generator Implementation Details

The generator (`src/build_privacy_site.py`):

1. **Parses effective dates** from `**Effective date:**` lines in markdown source, so footer dates cannot contradict policy text
2. **Validates WCAG AA contrast** for all accent colors against light (#ffffff) and dark (#131316) backgrounds
3. **Generates responsive HTML** with light/dark mode support via `prefers-color-scheme` and print stylesheets
4. **Creates distinct health data policy links** as callouts in the main policy (RCW requirement)
5. **Uses `.nojekyll`** to prevent GitHub Pages build steps that could silently fail
6. **Wraps tables** in scrollable containers for mobile compatibility
7. **Converts markdown** using Python-Markdown with extensions: tables, attr_list, sane_lists, toc, nl2br

## Audit Files

`src/<app>/_audit.md` files contain data-flow audits from the app's source code. These are NOT published to the site but inform policy content. They document:
- Network egress (what connects where, when, with what data)
- HealthKit scope and permissions
- Local storage and encryption
- Third-party dependencies
- Corrections to prior policy claims
- Open questions and verification items

Treat audit files as critical context when updating policies. They are the evidence trail.

## Critical Rules

1. **Edit `.md` files, never `.html` files** — HTML is generated and will be overwritten
2. **Verify policy changes at the live URL** after pushing — don't trust build output alone
3. **`.nojekyll` must remain** — GitHub Pages would otherwise process the site and could break it
4. **App Store Connect URLs must match** the generated paths exactly:
   - Main policy: `https://prameyallc.github.io/privacy/<app>/`
   - Health data policy: `https://prameyallc.github.io/privacy/<app>/health-data/`
5. **Consumer health data policies must be linked distinctly** (RCW 19.373.020 requirement) — not buried as a section
6. **Effective dates are per-policy** — read from markdown, not a global constant
7. **WCAG AA contrast is enforced** — builds fail if accent colors don't meet 4.5:1 ratio

## App Configuration

App metadata lives in the `APPS` list in `build_privacy_site.py` (line ~29):

```python
(slug, display_name, tagline, light_accent, dark_accent, has_health_data)
```

Changing an app's name, tagline, or accent colors requires editing this list and rebuilding.

## Legal Context

These are **legally operative documents**, not just informational pages:

- Policies are the privacy disclosures relied upon in App Store submissions
- Consumer health data policies satisfy Washington MHMDA and Nevada SB 370 requirements
- Inaccurate disclosures create both App Review and FTC Act §5 problems
- Policies must match what the app actually does (verified via source audits in `_audit.md` files)

When modifying policies:
- Cross-reference the corresponding `_audit.md` file
- Check that claims match the app's `PrivacyInfo.xcprivacy`, entitlements, and actual code behavior
- Flag any "TO VERIFY" notes in the markdown as blockers
- Update App Store Connect privacy labels if claims change

## Common Tasks

**Add a new app:**
1. Add entry to `APPS` list in `src/build_privacy_site.py`
2. Create `src/<app>/policy.md` (and `health-data.md` if it processes health data)
3. Run build command
4. Verify contrast warnings pass
5. Check live URL after push

**Update a policy:**
1. Edit `src/<app>/policy.md` (or `health-data.md`)
2. Update `**Effective date:**` line if this is a material change
3. Run build command
4. Review generated HTML locally
5. Push and verify at live URL
6. Update App Store Connect if necessary

**Change accent colors:**
1. Edit `APPS` list in `build_privacy_site.py`
2. Run build (will fail if new colors don't meet WCAG AA)
3. Verify colors render correctly in both light and dark modes

## Testing and Verification

- **Contrast validation**: Automatically enforced during build
- **Markdown rendering**: Check tables, lists, links in browser
- **Responsive layout**: Test on mobile viewport
- **Print stylesheet**: Use browser print preview
- **Dark mode**: Toggle system appearance
- **Live verification**: Always fetch the published URL after push — deployment can fail silently

## Dependencies

- Python 3 (standard library: `os`, `re`, `sys`, `html`, `shutil`, `datetime`)
- `markdown` package (installable via `pip install markdown`)

No other dependencies. No build step on GitHub's side (hence `.nojekyll`).

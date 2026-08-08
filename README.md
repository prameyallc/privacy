# Prameya App Privacy Policies

Public privacy policies for **Prameya LLC** apps, published as a static site via GitHub Pages.

**Live site:** https://prameyallc.github.io/privacy/

## Why one policy per app

These apps do genuinely different things with data — one takes intraoral photographs, one reads
HealthKit, one ingests privileged legal documents, one serves ads. A single shared policy cannot be
accurate for all of them, and an inaccurate privacy disclosure is both an App Review problem and an
FTC Act §5 problem. So each app gets its own policy, written from an audit of that app's actual
code (`PrivacyInfo.xcprivacy`, entitlements, `Info.plist` purpose strings, and the network,
HealthKit, CloudKit and camera call sites).

## URLs for App Store Connect

| App | Privacy Policy URL | Consumer Health Data Policy |
|-----|--------------------|------------------------------|
| OmniSalub  | https://prameyallc.github.io/privacy/omnisalub/  | https://prameyallc.github.io/privacy/omnisalub/health-data/ |
| OmniDent   | https://prameyallc.github.io/privacy/omnident/   | https://prameyallc.github.io/privacy/omnident/health-data/ |
| OmniDerm   | https://prameyallc.github.io/privacy/omniderm/   | https://prameyallc.github.io/privacy/omniderm/health-data/ |
| OmniRx     | https://prameyallc.github.io/privacy/omnirx/     | https://prameyallc.github.io/privacy/omnirx/health-data/ |
| OmniLex    | https://prameyallc.github.io/privacy/omnilex/    | — |
| OmniWealth | https://prameyallc.github.io/privacy/omniwealth/ | — |
| OmniMath   | https://prameyallc.github.io/privacy/omnimath/   | — |
| OmniBuild  | https://prameyallc.github.io/privacy/omnibuild/  | — |

### Consumer health data

Four apps process consumer health data. Washington's My Health My Data Act
(RCW 19.373.020) requires a **separate** consumer health data privacy policy, linked
distinctly — not a section inside the main policy. Those live at `/<app>/health-data/` and are
linked from the hub and from each app's main policy. Nevada SB 370 imposes analogous duties.

## How the site is built

Static HTML with `.nojekyll` — no build step on GitHub's side, so nothing can silently fail to
render. (The previous version of this repo served `PRIVACY.md` as raw `text/markdown`.)

Sources live in the generator, not here; pages are committed as built output. Each page is
responsive, supports light and dark, and has a print stylesheet.

## Contact

**Prameya LLC** · bobby@prameya.legal

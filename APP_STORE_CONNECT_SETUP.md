# App Store Connect: the fields this site supplies

**Rewritten:** 7 October 2026, from each app's code, StoreKit configuration, privacy manifests and
published policy.

This replaces the guide of 26 August 2026, which was a plan that never shipped. It listed Plus and
Premium, Foundation and Scholar, and other tiers, with product IDs no app uses. It said Family
Sharing was off for some apps when it is on in all of them. It also told readers to declare
"Purchase History" as data linked to the user, which no policy or privacy manifest says.

This page covers only the parts of each app's App Store Connect record that come from this site,
and the rules that keep them in step with the apps. Everything else about an app's record (the
listing, review notes, age rating, screenshots and products) is kept in that app's own repository.
Section 5 says where.

---

## 1. Fields per app

| App (App Store name) | Bundle ID | Privacy Policy URL | Consumer health data policy |
|---|---|---|---|
| OmniAvia | `legal.prameya.OmniAvia` | https://prameyallc.github.io/privacy/omniavia/ | — |
| OmniBuild | `legal.prameya.OmniBuild` | https://prameyallc.github.io/privacy/omnibuild/ | — |
| OmniCadence | `legal.prameya.OmniOps` | https://prameyallc.github.io/privacy/omniops/ | — |
| OmniDent | `legal.prameya.OmniDent` | https://prameyallc.github.io/privacy/omnident/ | https://prameyallc.github.io/privacy/omnident/health-data/ |
| OmniDerm | `legal.prameya.OmniDerm` | https://prameyallc.github.io/privacy/omniderm/ | https://prameyallc.github.io/privacy/omniderm/health-data/ |
| OmniLex | `legal.prameya.OmniLex` | https://prameyallc.github.io/privacy/omnilex/ | — |
| OmniMathematics | `legal.prameya.OmniMathematics` | https://prameyallc.github.io/privacy/omnimath/ | — |
| OmniPhysics | `legal.prameya.OmniPhysics` | https://prameyallc.github.io/privacy/omniphysics/ | — |
| OmniRx | `legal.prameya.OmniRx` | https://prameyallc.github.io/privacy/omnirx/ | https://prameyallc.github.io/privacy/omnirx/health-data/ |
| OmniSalub | `legal.prameya.omnisalub` (lower case) | https://prameyallc.github.io/privacy/omnisalub/ | https://prameyallc.github.io/privacy/omnisalub/health-data/ |
| OmniWealth | `legal.prameya.OmniWealth` | https://prameyallc.github.io/privacy/omniwealth/ | — |

- In every app the Apple TV app uses the host app's bundle ID and shares its App Store record. The
  Apple Watch app is `<host ID>.watch` (OmniSalub's is `legal.prameya.omnisalub.watchkit`).
- Enter the Privacy Policy URL exactly as shown, with the trailing slash. The apps link these same
  strings.
- `/privacy/omniaero/` is an old address that redirects to `/privacy/omniavia/`. There is no
  `/privacy/omnimathematics/` page; OmniMathematics is `/privacy/omnimath/`.
- The consumer health data policy has no field of its own in App Store Connect. Washington's My
  Health My Data Act wants it linked distinctly, so each health app links it in the app, from its
  main policy, and from the hub page at https://prameyallc.github.io/privacy/.
- Support page: https://prameyallc.github.io/privacy/support/.

## 2. The "Apple TV Privacy Policy" field

The Apple TV app shows the privacy policy's effective date and its short version. App Store Connect
holds the same text in its own **Apple TV Privacy Policy** field. Paste the text exactly as the app
renders it, from this source in the app's repository:

| App | Swift source of the Apple TV privacy text |
|---|---|
| OmniAvia | `AviaPrivacySummary.plainText`, `OmniAviaKit/Sources/DesignSystem/AviaComponents/AviaPrivacySummary.swift` |
| OmniBuild | `LivingRoomLegalCopy.privacySummary`, `OmniBuildKit/Sources/Knowledge/LivingRoomLegalCopy.swift` |
| OmniCadence | `OpsTVAbout.privacySummary`, `OmniCadenceKit/Sources/DesignSystem/Components/OpsTVAbout.swift` |
| OmniDent | `LivingRoomLegalCopy`, `OmniDentKit/Sources/Knowledge/LivingRoomLegalCopy.swift` |
| OmniDerm | `LivingRoomLegal.privacySummary`, `OmniDermKit/Sources/DermCore/Legal/LivingRoomLegal.swift` |
| OmniLex | `LivingRoomAbout.privacySummary`, `OmniLexKit/Sources/LexCore/Legal/LivingRoomAbout.swift` |
| OmniMathematics | `CompanionLegalCopy`, `OmniMathematicsKit/Sources/Continuity/CompanionLegalCopy.swift` |
| OmniPhysics | `TVLegalCopy.privacyParagraphs`, `OmniPhysicsKit/Sources/Continuity/TVLegalCopy.swift` |
| OmniRx | `RxTVAboutCopy.privacyShortVersion`, `OmniRxKit/Sources/RxCore/Content/RxTVAboutCopy.swift` |
| OmniSalub | `LivingRoomLegalCopy.privacySummary`, `CompanionKit/Sources/Continuity/LivingRoomLegalCopy.swift` |
| OmniWealth | `WealthPrivacySummary.appStoreFieldText`, `WealthKit/Sources/WealthCore/Compliance/WealthPrivacySummary.swift` |

Each source is pinned by a test in its repository. When a
policy's effective date or short version changes, change the Swift source and its test in the same
pass, and then paste the new text into App Store Connect. Every policy was re-dated on 7 October 2026
(privacy PR #59), so every field needs the 7 October text.

## 3. App Privacy (the privacy label)

Apple counts data as "collected" when it leaves the device and the developer or its partners can
access it for longer than it takes to serve the request. No app sends anything to Prameya, which runs
no server. The policy, the privacy manifests and the App Store Connect answers must agree; change
all three together.

| App | Answer | What the privacy manifests declare |
|---|---|---|
| OmniPhysics | **Purchases → Purchase History**: not linked to you, not used for tracking, purpose App Functionality. Nothing else. | The host app's manifest declares Purchase History (not linked, no tracking, App Functionality). The policy says the same in "StoreKit transaction data". The TV, Watch and widget manifests declare nothing. |
| Every other app | **Data Not Collected** | Every manifest's collected data types list is empty, with tracking off. |

- Do not add "Purchase History, linked to you" for any app. That was the old guide's advice and no
  policy supports it. OmniPhysics declares Purchase History only because its manifest does, and as
  not linked to you.
- No app tracks. Every manifest sets tracking to false, with no tracking domains.
- Any open question about a label answer is kept in that app's repository (section 5), not here.

## 4. In-app purchases (summary)

Every app sells one upgrade, **<App> Pro**, as three products. Any one of them unlocks the same Pro.

| Product ID | Type |
|---|---|
| `legal.prameya.<id>.pro.monthly` | Auto-renewable subscription, 1 month |
| `legal.prameya.<id>.pro.annual` | Auto-renewable subscription, 1 year, in the same subscription group |
| `legal.prameya.<id>.pro.lifetime` | Non-consumable |

`<id>` is `omniavia`, `omnibuild`, `omniops`, `omnident`, `omniderm`, `omnilex`, `omnimath`,
`omniphysics`, `omnirx`, `omnisalub` or `omniwealth`. Product IDs are lower case, unlike most bundle
IDs.

- **Family Sharing is on for all three products in every app.** Every policy says so, and each
  app's `.storekit` file sets it. Keep it on in App Store Connect.
- Prices and free trials are in each policy's "Available tiers" table. OmniMathematics' policy has
  no table; its prices are in its Terms of Use and on the in-app paywall. The app's `.storekit` file
  and its own docs (section 5) are the source of truth.
- Purchases go through StoreKit and Apple. No app sends anything about a purchase to Prameya.

## 5. Where each app keeps the rest of its App Store Connect record

| App | GitHub repository | Connect record |
|---|---|---|
| OmniAvia | `prameyallc/OmniAvia` | `STORE_LISTING.md`, `BUSINESS_STRATEGY.md`, `OmniAvia.storekit` |
| OmniBuild | `prameyallc/OmniBuild` | `docs/APP_STORE.md`, `STORE_LISTING.md`, `OmniBuild.storekit` |
| OmniCadence | `prameyallc/OmniCadence` | `STORE_LISTING.md`, `OmniCadence.storekit` |
| OmniDent | `prameyallc/OmniDent` | `Docs/APP_STORE.md`, `STORE_LISTING.md`, `APP_STORE_SETUP.md`, `OmniDent.storekit` |
| OmniDerm | `prameyallc/OmniDerm` | `docs/APP_STORE.md`, `STORE_LISTING.md`, `OmniDerm.storekit` |
| OmniLex | `prameyallc/OmniLex` | `docs/APP_STORE.md`, `docs/STORE_LISTING.md`, `OmniLex.storekit` |
| OmniMathematics | `prameyallc/OmniMathematics` | `docs/APP_STORE.md`, `docs/APP_STORE_LISTING.md`, `docs/APP_REVIEW_INFORMATION.md`, `OmniMathematics.storekit` |
| OmniPhysics | `prameyallc/OmniPhysics` | `STORE_LISTING.md`, `AppStore/Metadata.md`, `OmniPhysics.storekit` |
| OmniRx | `prameyallc/OmniRx` | `docs/APP_STORE.md`, `STORE_LISTING.md`, `OmniRx.storekit` |
| OmniSalub | `prameyallc/OmniSalub` | `AGENTS.md`, `STORE_LISTING.md`, `OmniSalub.storekit` |
| OmniWealth | `prameyallc/OmniWealth` | `docs/APP_STORE.md`, `docs/STORE_LISTING.md`, `OmniWealth.storekit` |

## 6. When a policy changes

1. Edit `src/<app>/policy.md` (or `health-data.md`), move its effective date and add a dated
   "what changed" entry. Regenerate the site (`python3 src/build_privacy_site.py src .
   https://prameyallc.github.io/privacy`), merge, and fetch the live page to confirm it.
2. In the app's repository, update the Apple TV privacy text and its test (section 2), plus any
   in-app copy that quotes the policy. Land it.
3. Paste the new Apple TV text into App Store Connect.
4. If what the app collects or shares changed, update the privacy manifests and the App Privacy
   answers (section 3) at the same time, and record them in the app's own docs.

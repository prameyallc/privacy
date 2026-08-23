# OmniMathematics Privacy Policy

**Effective date:** 23 August 2026
**Publisher:** Prameya LLC ("Prameya", "we", "us")
**App:** OmniMathematics for iPhone — bundle ID `legal.prameya.OmniMathematics`
**Contact:** admin@prameya.legal
**Scope:** This policy covers the OmniMathematics iOS app and nothing else. Prameya's other apps have their own policies, because they work differently. Index: <https://prameyallc.github.io/privacy/>
**Canonical public URL (slug stays `omnimath`):** <https://prameyallc.github.io/privacy/omnimath/>

---

## The short version

- **There are no accounts.** No sign-in, no email address, no name, no profile. There is nothing to fill in.
- **Your learning progress stays on your phone.** Completed chapters and pack progress are written to your device's local storage. We do not run a server that receives them. We have no database of users.
- **OmniMathematics makes no network requests at all.** Not to us, not to anyone. Every lesson, concept and worked example ships inside the app download.
- **OmniMathematics has no ads and no App Tracking Transparency prompt.** AdMob, Google's User Messaging Platform, and the advertising identifier request were removed on 12 August 2026 in commit `df7919f`. The last ad-injection code in the app's view layer was removed on 16 August 2026.
- **There is no advertising identifier (IDFA) collection, and no third party receives anything.** The app ships no third-party SDKs of any kind.
- **The app asks for no other permissions.** No camera, photos, microphone, location, contacts, health or files.
- **There is no AI model in OmniMathematics and it downloads none.** Nothing you read, tap or type is sent to us or to any model.
- **There is nothing to buy today.** No paywall, purchase screen or subscription prompt is reachable in this build.
- **OmniMathematics is built for a general audience** — computer-science students, self-learners and adults. It is not in the App Store Kids Category.
- **No health data of any kind** is involved. See "Health data" below.

---

## What OmniMathematics is

OmniMathematics teaches discrete mathematics for computer science through written lessons, a searchable Codex of concepts, and interactive demonstrations. All of the learning content ships inside the app.

It is free, and at present nothing pays for it. Until 12 August 2026 advertising did, and earlier versions of this policy said so. That business model was removed from the code, not merely disabled. There is no in-app purchase, paywall, or StoreKit product identifier in the app — there is no reachable purchase route, so the app takes no money from you by any means. If that changes, this policy will be updated before the purchase route ships.

---

## What stays on your device

OmniMathematics writes the following to your iPhone's local app storage (Apple's `UserDefaults`):

| What | Why |
|---|---|
| Which chapters you have completed | To show your Journey progress |
| Which knowledge packs you have worked through | Same |
| Chapter and pack progress | Same |
| The last chapter you visited, and the realm it belongs to | To take you back where you were |
| Which step of that lesson you had reached | Same |
| The last knowledge pack you opened | Same |
| Whether you have seen the intro screens | So onboarding shows once |

That is the complete list. It never leaves your phone through OmniMathematics. We cannot see it, and we have no way to request it.

*Correction, 16 August 2026:* earlier versions of this policy described "four things". That undercounted — the app also records the realm, the lesson step and the last knowledge pack. None of it is transmitted anywhere, so nothing about what the app discloses changed, but the list was wrong and is now complete.

Two ordinary caveats that are true of any iPhone app:

- If you use iCloud or iTunes device backup, this data is included in your backup, under Apple's terms and your control. OmniMathematics does not sync anything to iCloud itself — the app has no iCloud capability enabled at all.
- Deleting the app deletes this data. You can also clear it any time with **More → Progress → Reset All Progress**.

---

## What OmniMathematics does not do

One line each, because the honest answer is short.

- No user accounts, and no way to create one.
- No ads of any kind — no banners, no interstitials, no rewarded ads.
- No advertising identifier (IDFA), no `AdSupport`, no SKAdNetwork entries, no App Tracking Transparency prompt.
- No third-party SDKs. Every code module in the app is written by us.
- No network requests. There is no upload path, no download path, and no server for the app to talk to.
- Nothing you write, draw, tap, search or type in the Ask box is transmitted anywhere.
- No camera, photo library, microphone, contacts, calendar, or file access.
- No location permission is requested, and the app uses no location APIs. Nothing in the app estimates your location by any other means either.
- No health, fitness or medical data of any kind.
- No iCloud or CloudKit sync.
- No analytics or crash-reporting service — ours or anyone else's.
- No AI model, no on-device inference, and no model downloads.
- Nothing to buy: no paywall, purchase screen or subscription prompt is reachable.

---

## Advertising — removed

**OmniMathematics shows no ads, and no data leaves your device for advertising or for anything else.**

This section used to be the longest in the policy, because it was the one place data left your device. It described banner and interstitial ads served by Google AdMob, ad loading that began the moment you opened the app, Google's consent form for the EEA and UK, the advertising identifier being used for cross-app tracking, a coarse location Google's ad software estimated from your IP address, SKAdNetwork install measurement, and an in-app control for reporting a bad ad.

None of that is true of the shipping app, and every word of it is deleted here:

- **12 August 2026, commit `df7919f`** — the Google Mobile Ads SDK, the User Messaging Platform (consent) SDK, the whole `App/OmniMathematics/Ads` tree, the `NSUserTrackingUsageDescription` string, the SKAdNetwork identifier list and the ATT request were removed from the app. The **Settings → Ads → Ad privacy choices** row was removed with them; there is no consent form left for it to reopen. The in-app ad report control went at the same time, with the ad container that hosted it.
- **16 August 2026** — `MathAds.swift`, the last ad-injection seam in the view layer (banner and interstitial slots, `AdTileView`), was deleted. Nothing referenced it.
- The build now enforces this. `ci_scripts/ci_post_clone.sh` **fails the build** if `ThirdParty/GoogleAdsSPM` or `App/OmniMathematics/Ads` is ever restored, and a test suite asserts that no ad symbols are linked.

**Google receives nothing from this app.** Google is no longer a recipient of any data from OmniMathematics, because the app contacts no server at all. The links to Google's privacy policy and ad settings that used to appear here have been removed rather than left as decoration: pointing you at a third party's controls implies that third party has something of yours, and it does not.

**This part is on us, not on the reader.** The top of this policy was corrected on 12 August 2026 to say the ads were gone, while the body below it went on describing them in the present tense for four days. A policy that contradicts itself in one file is worse than one that is merely out of date, because a reader cannot tell which half to believe. The whole document has now been read against the shipping binary.

---

## No AI model, no model downloads

Some apps download machine-learning model files on first use. **OmniMathematics does not.** It contains no model, downloads nothing from any model host, and performs no inference. Every explanation and worked example in the app was written by a person and ships inside the download from the App Store.

The Codex has an **Ask** box. What it does is a deterministic keyword lookup over the lessons and concept entries already on your phone: it finds the closest passage and shows you that passage, copied word for word from the shipped curriculum. It generates no prose of its own, and it sends your question nowhere — there is no network code in the app for it to use. Your question is not stored either.

The source also contains an inert programming interface reserved for a possible future on-device model. It has no model behind it, links no model runtime, and adds no network access. If that ever changes, this policy will change first.

---

## If you email us

If you write to admin@prameya.legal — a question, a bug report, a rights request — we receive your email address and whatever you put in the message. We keep it only as long as we need it to deal with your message and to keep a record that we did, and you can ask us to delete it. That mailbox is the only place Prameya holds anything about a user of this app.

---

## Children and OmniMathematics

**Who OmniMathematics is for.** University and later-secondary computer-science students, self-taught programmers, and adults who want to understand discrete mathematics. It is a general-audience educational app. It is not in the App Store Kids Category, it is not designed or marketed for young children, and its content, artwork and language are aimed at older students and adults.

**What that means in practice, stated plainly.** Nothing is collected from anyone who uses OmniMathematics, at any age. There is no identifier to transmit, no advertising network to transmit it to, and no network request of any kind. A child using this app is in the same position as an adult using it: their progress is written to their own phone and stays there.

**What we do not do.** We do not knowingly collect personal information from children — we collect nothing from anyone, because there is nothing to collect and nowhere for it to go. We do not build profiles. We do not use any school, classroom or ClassKit data; the app has no such integration.

**On the signal that used to be sent to the ad network.** Google's ad software let a publisher flag an app as directed to children, flag it as not directed to children, or send no flag at all. OmniMathematics sent no flag. That decision no longer has anything to attach to: the ad SDK is gone, so no flag of any kind is transmitted or transmittable.

**What parents and guardians can do.** Use **Screen Time** to manage which apps a child can use, and write to us at admin@prameya.legal with any concern. The tracking-permission advice this section used to give is obsolete: OmniMathematics no longer appears under **iOS Settings → Privacy & Security → Tracking**, because it never asks to track.

---

## Health data

OmniMathematics processes **no consumer health data**. It has no health, wellness, symptom, fitness or biometric features, no HealthKit access, and nothing in it is derived from your body or your care. Washington's My Health My Data Act, Nevada's SB 370 and similar consumer-health-data laws are therefore not engaged, and OmniMathematics has no separate consumer health data privacy policy. Other Prameya apps do — see the index at <https://prameyallc.github.io/privacy/>.

---

## HIPAA, FERPA and school privacy laws

- **HIPAA does not apply to OmniMathematics.** HIPAA governs health plans, health-care clearinghouses, most health-care providers, and their business associates. OmniMathematics is a consumer education app with no health function and no relationship to any of those. We do not claim HIPAA compliance, because there is nothing here for HIPAA to reach.
- **FERPA does not apply.** FERPA binds schools and other educational agencies receiving federal funding, and those acting for them. OmniMathematics has no relationship with any school and holds no education records.
- **Student-privacy statutes** such as California's SOPIPA apply to services designed and marketed for K-12 school purposes. OmniMathematics is a consumer app and is not sold to schools. If that ever changes, this policy will be rewritten before it does.

---

## Your privacy rights

Because we hold nothing, most requests have a very short answer — but the routes are real and we will use them.

### Everyone

- **See what we hold about you.** Ask us. The answer is normally "your email to us, if you sent one, and nothing else".
- **Delete it.** Ask us to delete your correspondence. For your on-device learning data, use **More → Progress → Reset All Progress**, or delete the app — that is a genuine deletion, not a request to us.
- **Advertising controls.** There are none to give you, and none needed: no advertising happens in this app, and no advertising identifier is requested.
- Write to **admin@prameya.legal**. We aim to respond within 30 days.

### California (CCPA / CPRA)

California residents have the rights to know, delete, correct, and to opt out of the sale or sharing of personal information, and not to be discriminated against for exercising them.

**Do Not Sell or Share My Personal Information.** We do not sell personal information, and we do not share it for cross-context behavioural advertising. Until 12 August 2026 this section said the opposite, and it was accurate then: advertising identifiers and ad-interaction data were disclosed to Google for personalised advertising, which California calls "sharing". That disclosure stopped when the ad SDK was removed. There is now no recipient, no identifier and no transmission, so there is nothing to opt out of. The opt-out this section used to name — denying tracking under iOS Settings → Privacy & Security → Tracking — no longer applies either, because OmniMathematics never asks to track and so does not appear in that list.

**Categories.** We collect none of the CCPA categories. No identifiers, no internet or network activity, no geolocation of any precision, no name, contact details, financial information, biometric, health, employment or education records. The only personal information Prameya ever holds about a user of this app is an email you choose to send us, at the address above.

**Sensitive personal information.** OmniMathematics does not collect sensitive personal information as California defines it. There is nothing here for a "Limit the Use of My Sensitive Personal Information" control to limit.

**Minors.** We do not sell or share the personal information of consumers under 16 — or of anyone else, at any age.

**Global Privacy Control.** GPC is a browser signal and there is no established equivalent for native iOS apps. It makes no difference here: there is no sale or sharing for a GPC signal to stop.

**A candid note on scope.** Prameya is a very small company and may fall below the revenue and volume thresholds that make the CCPA legally binding. We describe and honour these choices regardless of whether we are required to.

### Other US states

Virginia, Colorado, Connecticut, Texas, Oregon, Montana and a growing number of other states give residents rights to access, correct, delete and port personal data, and specifically to opt out of targeted advertising and profiling. If any of those laws applies to us, the answer is the same one: no targeted advertising occurs in OmniMathematics, no profiling occurs, and no personal data is collected to access, correct, delete or port. Email us for anything else. Some of these states offer an appeal if we refuse a request — if we ever refuse yours, we will tell you how to appeal and how to contact your state Attorney General.

### EEA and United Kingdom (GDPR / UK GDPR)

OmniMathematics is available worldwide, so this section applies if you are in the EEA or the UK.

**Controller.** Prameya LLC, contact admin@prameya.legal, is the controller for the only processing it carries out — correspondence you send us. There is no joint controller and no processor: as of 12 August 2026 no third party receives personal data through this app. Google was previously an independent controller for advertising data collected through its own software in the app; it no longer receives anything.

**Legal bases.**

- *Answering your email:* legitimate interests, or the steps needed to respond to you.

That is the whole list. The advertising entries that used to sit above it — consent for personalised advertising, and legitimate interests in funding a free app through contextual ads — are gone because the processing they described is gone.

**Consent.** No consent form appears in OmniMathematics. Google's consent form (the User Messaging Platform) was removed on 12 August 2026 along with the advertising it gated. There is no advertising consent to give, withdraw or re-open.

**Profiling.** None. No automated decision-making of any kind takes place, and nothing in the app builds a profile of you.

**Special-category data (Article 9).** None is processed. There is no health, biometric, racial, religious, political, trade-union or sexual-life data anywhere in this app.

**Your rights.** Access, rectification, erasure, restriction, portability, objection to processing based on legitimate interests, and withdrawal of consent. In practice these reach only an email you have sent us, because that is all that exists.

**International transfers.** None. We do not transfer your data internationally, because we do not hold it and the app sends nothing anywhere.

**Complaints.** You may complain to your national data protection authority, or to the UK Information Commissioner's Office if you are in the UK.

**Children in Europe.** Where consent is the legal basis for processing a child's data, GDPR requires the child to be at least 16, or younger only with the consent of a parent or guardian, subject to each member state's lower age limit (never below 13). No consent-based processing of anyone's data occurs in OmniMathematics. See "Children and OmniMathematics" above.

---

## Security

There is not much to secure, and that is the design.

- Your learning data stays in your app's private storage on your device, protected by iOS and your passcode. Use a passcode and keep iOS up to date.
- The app makes no network requests, so there is no traffic to intercept. As of 16 August 2026, a search of the compiled sources for `URLSession`, `URLRequest` and `dataTask` returns nothing at all. The transport-security discussion that used to sit here covered the advertising SDK's traffic; there is no such traffic now.
- We operate no server holding user data, so there is no user database of ours that could be breached.

We make no claim to unbreakable security. No system is perfectly secure.

---

## Data retention

- **On your device:** kept until you clear it (More → Progress → Reset All Progress) or delete the app.
- **With us:** only emails you send us, kept as long as needed to handle your message and to record that we handled it. Ask and we will delete yours.
- **With anyone else:** nothing. No third party receives anything from this app, so no third party has anything to retain.

---

## App Store privacy labels — one clarification

Apple's App Store privacy labels use Apple's own definition of "collect", which turns on data leaving your device. That definition is useful for reading the labels and nothing more. It does not shrink our duties under state or national privacy law, and we have not used it to narrow anything in this policy.

---

## Changes to this policy

We will update this policy when the app changes — and, where we can, before the change ships. When we do, we will change the effective date at the top and describe what changed. If a change materially expands what is collected or who receives it, we will surface it in the app rather than relying on you to re-read this page.

**23 August 2026 — what changed.** The legal name on this page is **OmniMathematics** (bundle ID `legal.prameya.OmniMathematics`). The public URL slug stays `omnimath`. User-facing “Insight Stars” copy is chapter and pack progress; reset is **More → Progress → Reset All Progress**.

**21 August 2026 — what changed.** The unused StoreKit scaffold that this policy used to describe as a `Monetization` module with product identifiers was deleted from the app. There is still nothing to buy. The live URL for this page is <https://prameyallc.github.io/privacy/omnimath/>.

**16 August 2026 — what changed.** Advertising was removed from OmniMathematics in commit `df7919f` on 12 August 2026, and the last ad-injection code in the view layer was removed on 16 August 2026. On 12 August the summary at the top of this policy was corrected, but the body was not: for four days this file said "no ads" in its first section and then described banner ads, interstitials, ad load timing, Google's data-collection table, the advertising identifier, IP-derived coarse location, SKAdNetwork and an ad-reporting control in the present tense. Every one of those passages has now been deleted or rewritten, along with the advertising legal bases under GDPR, the California "sharing" disclosure and its tracking-based opt-out, the ad-related retention entry, the ad-traffic security claim, and the ad-dependent reasoning in the children's section. The on-device data table was also corrected: it had listed four stored items where the app stores eight. This update removes disclosures; it adds no collection.

Older versions are kept in the public repository behind <https://prameyallc.github.io/privacy/>.

---

## Contact

**Prameya LLC**
Email: **admin@prameya.legal**
Privacy policies for all Prameya apps: <https://prameyallc.github.io/privacy/>
This policy: <https://prameyallc.github.io/privacy/omnimath/>

If you are writing about a privacy right, say which right and which app, and we will get to it faster.

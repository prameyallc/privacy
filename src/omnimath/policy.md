# OmniMath Privacy Policy

**Effective date:** 8 August 2026
**Publisher:** Prameya LLC ("Prameya", "we", "us")
**App:** OmniMath for iPhone — bundle ID `legal.prameya.OmniMath`
**Contact:** admin@prameya.legal
**Scope:** This policy covers the OmniMath iOS app and nothing else. Prameya's other apps have their own policies, because they work differently. Index: <https://prameyallc.github.io/privacy/>

---

## The short version

- **There are no accounts.** No sign-in, no email address, no name, no profile. There is nothing to fill in.
- **Your learning progress stays on your phone.** Completed chapters and Insight Stars are written to your device's local storage. We do not run a server that receives them. We have no database of users.
- **OmniMath shows ads.** They come from Google AdMob. This is the only part of the app that sends anything off your device, and it starts when you open the app.
- **The ad software collects device and advertising information**, including your device's advertising identifier if you allow tracking. The exact list is below, taken from Google's own published declarations.
- **We do not sell your personal information for money.** But when you allow tracking, an advertising identifier is disclosed to Google for personalised advertising, and California law calls that "sharing". We say so plainly rather than hiding behind "we don't sell data".
- **The app asks for no other permissions.** No camera, photos, microphone, location, contacts, health or files.
- **There is no AI model in OmniMath and it downloads none.** Nothing you read or tap is sent to us or to any model.
- **OmniMath is built for a general audience** — computer-science students, self-learners and adults. It is not a children's app and is not in the App Store Kids Category.
- **No health data of any kind** is involved. See "Health data" below.

---

## What OmniMath is

OmniMath teaches discrete mathematics for computer science through written lessons, a searchable Codex of concepts, and interactive demonstrations. All of the learning content ships inside the app. It is free, and advertising is what pays for it.

---

## What stays on your device

OmniMath writes four things to your iPhone's local app storage (Apple's `UserDefaults`):

| What | Why |
|---|---|
| Which chapters you have completed | To show your Journey progress |
| Your Insight Star count | Same |
| The last chapter you visited | To take you back where you were |
| Whether you have seen the intro screens | So onboarding shows once |

That is the complete list. It never leaves your phone through OmniMath. We cannot see it, and we have no way to request it.

Two ordinary caveats that are true of any iPhone app:

- If you use iCloud or iTunes device backup, this data is included in your backup, under Apple's terms and your control. OmniMath does not sync anything to iCloud itself — the app has no iCloud capability enabled at all.
- Deleting the app deletes this data. You can also clear it any time with **Progress → Reset All Progress**.

---

## What OmniMath does not do

One line each, because the honest answer is short.

- No user accounts, and no way to create one.
- No in-app purchases or subscriptions.
- No uploads. Nothing you write, draw, tap or search is transmitted anywhere.
- No camera, photo library, microphone, contacts, calendar, or file access.
- No location permission is requested, and the app uses no location APIs. (Google's ad software still estimates a coarse location from your IP address — see below.)
- No health, fitness or medical data of any kind.
- No iCloud or CloudKit sync.
- No analytics or crash-reporting service of ours.
- No AI model, no on-device inference, and no model downloads.

---

## Advertising — the one place data leaves your device

OmniMath displays banner ads and occasional full-screen (interstitial) ads through **Google AdMob**. Interstitials are rate-limited: at most one after every second chapter you complete, and never within 90 seconds of the last one.

Ad loading begins **when you open the app**, before you tap anything. That is worth knowing, and we say it because it is true rather than because it is flattering.

We choose to show ads. We do not choose which ads you see. Google's systems decide that.

### What the ad software collects

Google publishes a machine-readable declaration inside the Mobile Ads SDK we ship. Taken directly from it, the Google Mobile Ads SDK collects:

| Category | Linked to you? | Used for |
|---|---|---|
| Device ID (your advertising identifier, when available) | Yes | Third-party advertising, analytics — **and this is the item Google marks as used for tracking** |
| Advertising data (ads shown, tapped, ad interactions) | Yes | Third-party advertising, analytics |
| Coarse location (estimated from your IP address, not from GPS) | Yes | Third-party advertising, analytics |
| Product interaction | Yes | Analytics, advertising |
| Performance data | No | Advertising, analytics |
| Crash data | No | Analytics |
| Other diagnostic data | No | Advertising, analytics |

Google's consent software (the "User Messaging Platform") additionally handles coarse location, performance data and product-interaction data for the limited purpose of making the consent form work.

This data goes to Google, not to us. **We never receive it.** We see only aggregate revenue and impression counts in the AdMob dashboard — no identifiers, no per-user records.

What Google does with it is governed by Google's own terms:

- Google Privacy Policy — <https://policies.google.com/privacy>
- How Google uses information from sites or apps that use our services — <https://policies.google.com/technologies/partner-sites>

### App Tracking Transparency

The first time you open OmniMath, iOS shows Apple's tracking permission dialog.

- **Allow** — Google may use your device's advertising identifier (IDFA) to personalise ads and measure them across apps.
- **Ask App Not to Track** — the identifier is withheld by iOS. The app works exactly the same and still shows ads, but they are not personalised using that identifier.

You can change your answer at any time in **iOS Settings → Privacy & Security → Tracking**.

### The Google consent form (EEA, UK and other regions)

Where the law requires it — the European Economic Area and the UK in particular — Google's consent form appears before ads load, asking for your choices about personalised advertising and related purposes. That form is where your advertising consent is given or refused.

You can change or withdraw those choices at any time: open **Settings** (the gear in the Codex tab) → **Ads** → **Ad privacy choices**, which reopens the same consent form. That row appears whenever the consent framework requires an entry point (normally the EEA and UK); elsewhere the form does not apply and the row is not shown.

### How to limit personalised ads

1. Turn off tracking for OmniMath: **iOS Settings → Privacy & Security → Tracking**.
2. If the Google consent form was shown to you, change your answers there (**Settings → Ads → Ad privacy choices** inside the app).
3. Review and change what Google uses about you at **<https://adssettings.google.com>**.

Ads will still appear. They will simply be less targeted. There is no paid ad-free version of OmniMath today.

### Install measurement (SKAdNetwork)

OmniMath includes Apple's SKAdNetwork identifiers so ad networks can tell that an install happened without learning who you are. This is Apple's privacy-preserving attribution system; it reports aggregate, delayed results and does not identify you individually.

### Reporting an ad

If an ad is inappropriate, misleading, or wrong for this app's audience, tap the report control on the ad container, or use **Settings → Ads**. It opens an email to **admin@prameya.legal** containing only what you type plus the app version and build number — no identifiers, no learning progress. We escalate reports to Google.

We ask Google to cap ad content at the **"G" (general audiences)** rating. That is a request Google honours for ads it serves; it is not a guarantee about every buyer in the auction, which is why the reporting route exists.

---

## No AI model, no model downloads

Some apps download machine-learning model files on first use. **OmniMath does not.** It contains no model, downloads nothing from any model host, and performs no inference. Every explanation and worked example in the app was written by a person and ships inside the download from the App Store.

The app's source contains an unused programming interface reserved for a possible future on-device model. It is inert, has no implementation, and adds no network access. If that ever changes, this policy will change first.

---

## If you email us

If you write to admin@prameya.legal — an ad report, a question, a rights request — we receive your email address and whatever you put in the message. We keep it only as long as we need it to deal with your message and to keep a record that we did, and you can ask us to delete it. That mailbox is the only place Prameya holds anything about a user of this app.

---

## Children and OmniMath

This matters more here than in our other apps, because this is the one app that shows ads.

**Who OmniMath is for.** University and later-secondary computer-science students, self-taught programmers, and adults who want to understand discrete mathematics. It is a general-audience educational app. It is not in the App Store Kids Category, it is not designed or marketed for young children, and its content, artwork and language are aimed at older students and adults.

**What that means in practice, stated honestly.** Ads load when the app opens, before anyone is asked anything. If a young child uses OmniMath on a device where tracking is allowed, an advertising identifier can be transmitted to Google in the same way it would be for any other user. We do not have a way to detect a child's age, and we do not ask for one.

**What parents and guardians can do.**

- Turn off tracking for OmniMath in **iOS Settings → Privacy & Security → Tracking**, or turn off "Allow Apps to Request to Track" device-wide.
- Use **Screen Time** to manage which apps a child can use.
- Write to us at admin@prameya.legal with any concern about a child's use of the app.

**What we do not do.** We do not knowingly collect personal information from children ourselves — we collect nothing from anyone directly, because there is nothing to collect and nowhere for it to go. We do not build profiles. We do not use any school, classroom or ClassKit data; the app has no such integration.

**On the signal we send the ad network.** Google's software lets a publisher flag an app as directed to children, flag it as not directed to children, or send no flag at all. OmniMath sends **no flag**. Sending "not directed to children" would be a formal certification, and we do not make certifications we have not properly assessed — we have not made that certification, here or anywhere else. Leaving it unset is the accurate option, not an evasive one.

If you believe a child under 13 has used OmniMath in a way that concerns you, contact us and we will help with whatever is within our control — which, given that we hold no user data, is chiefly helping you switch off tracking and pointing you to Google's controls.

---

## Health data

OmniMath processes **no consumer health data**. It has no health, wellness, symptom, fitness or biometric features, no HealthKit access, and nothing in it is derived from your body or your care. Washington's My Health My Data Act, Nevada's SB 370 and similar consumer-health-data laws are therefore not engaged, and OmniMath has no separate consumer health data privacy policy. Other Prameya apps do — see the index at <https://prameyallc.github.io/privacy/>.

---

## HIPAA, FERPA and school privacy laws

- **HIPAA does not apply to OmniMath.** HIPAA governs health plans, health-care clearinghouses, most health-care providers, and their business associates. OmniMath is a consumer education app with no health function and no relationship to any of those. We do not claim HIPAA compliance, because there is nothing here for HIPAA to reach.
- **FERPA does not apply.** FERPA binds schools and other educational agencies receiving federal funding, and those acting for them. OmniMath has no relationship with any school and holds no education records.
- **Student-privacy statutes** such as California's SOPIPA apply to services designed and marketed for K-12 school purposes. OmniMath is a consumer app and is not sold to schools. If that ever changes, this policy will be rewritten before it does.

---

## Your privacy rights

Because we hold almost nothing, most requests have a very short answer — but the routes are real and we will use them.

### Everyone

- **See what we hold about you.** Ask us. The answer is normally "your email to us, if you sent one, and nothing else".
- **Delete it.** Ask us to delete your correspondence. For your on-device learning data, use **Progress → Reset All Progress**, or delete the app — that is a genuine deletion, not a request to us.
- **Control advertising.** Use the three steps in "How to limit personalised ads" above.
- Write to **admin@prameya.legal**. That is a small publisher mailbox rather than a staffed support desk; we aim to answer within 30 days, and if we need longer we will say so.

### California (CCPA / CPRA)

California residents have the rights to know, delete, correct, and to opt out of the sale or sharing of personal information, and not to be discriminated against for exercising them.

**Do Not Sell or Share My Personal Information.** We do not sell personal information for money. We do disclose advertising identifiers and ad-interaction data to Google for personalised advertising when you have allowed tracking. Under California law that is **"sharing" for cross-context behavioural advertising**, and some other state laws would call it a "sale". We are telling you that directly. **Your opt-out is to deny tracking** — iOS Settings → Privacy & Security → Tracking. Once denied, the identifier is not available to be shared. The same disclosure appears in the app itself, under Settings → Ads.

**Categories.** The categories involved are *identifiers* (advertising identifier), *internet or network activity* (ad interactions, app interaction data), and *coarse geolocation inferred from IP address*. The source is your device. The business purpose is advertising and the measurement of advertising. The category of third party receiving it is the advertising network (Google). We do not collect the other CCPA categories at all — no name, contact details, financial information, biometric, health, precise geolocation, employment or education records.

**Sensitive personal information.** OmniMath does not collect sensitive personal information as California defines it. There is nothing here for a "Limit the Use of My Sensitive Personal Information" control to limit.

**Minors.** We do not knowingly sell or share the personal information of consumers under 16.

**Global Privacy Control.** GPC is a browser signal and there is no established equivalent for native iOS apps. Apple's tracking permission is the effective control here, and denying it stops the sharing described above.

**A candid note on scope.** Prameya is a very small company and may fall below the revenue and volume thresholds that make the CCPA legally binding. We describe and honour these choices regardless of whether we are required to.

### Other US states

Virginia, Colorado, Connecticut, Texas, Oregon, Montana and a growing number of other states give residents rights to access, correct, delete and port personal data, and specifically to **opt out of targeted advertising** and profiling. If any of those laws applies to us, the same mechanisms answer it: deny tracking on your device to stop targeted advertising, and email us for anything else. Some of these states offer an appeal if we refuse a request — if we ever refuse yours, we will tell you how to appeal and how to contact your state Attorney General.

### EEA and United Kingdom (GDPR / UK GDPR)

OmniMath is available worldwide, so this section applies if you are in the EEA or the UK.

**Controller.** Prameya LLC, contact admin@prameya.legal, is the controller for the very limited processing it carries out — that is, correspondence you send us. Google acts as an independent controller for the advertising data it collects through its own software; its policies and its rights processes govern that data.

**Legal bases.**

- *Personalised advertising:* your **consent**, collected through the Google consent form. You may withdraw it at any time, through **Settings → Ads → Ad privacy choices** in the app wherever that form applies to you.
- *Non-personalised (contextual) ad delivery, fraud prevention and basic ad measurement:* **legitimate interests** in funding a free app, balanced against the limited data involved.
- *Answering your email:* legitimate interests, or the steps needed to respond to you.

**Profiling.** Personalised advertising involves profiling for advertising purposes. It has no legal or similarly significant effect on you, and you can switch it off at any time.

**Special-category data (Article 9).** None is processed. There is no health, biometric, racial, religious, political, trade-union or sexual-life data anywhere in this app.

**Your rights.** Access, rectification, erasure, restriction, portability, objection to processing based on legitimate interests, and withdrawal of consent. Because we hold no user records, requests about advertising data need to go to Google, and we will point you there and help where we can.

**International transfers.** We do not transfer your data internationally, because we do not hold it. Google's transfers are covered by Google's own safeguards.

**Complaints.** You may complain to your national data protection authority, or to the UK Information Commissioner's Office if you are in the UK.

**Children in Europe.** Where consent is the legal basis for processing a child's data, GDPR requires the child to be at least 16, or younger only with the consent of a parent or guardian, subject to each member state's lower age limit (never below 13). OmniMath is aimed at older students and adults; see "Children and OmniMath" above for the controls available to parents.

---

## Security

There is not much to secure, and that is the design.

- Your learning data stays in your app's private storage on your device, protected by iOS and your passcode. Use a passcode and keep iOS up to date.
- All network traffic from the advertising software is encrypted in transit using standard iOS transport security.
- We operate no server holding user data, so there is no user database of ours that could be breached.

We make no claim to unbreakable security. No system is perfectly secure.

---

## Data retention

- **On your device:** kept until you clear it (Progress → Reset All Progress) or delete the app.
- **With us:** only emails you send us, kept as long as needed to handle your message and to record that we handled it. Ask and we will delete yours.
- **With Google:** governed by Google's retention practices, described in Google's privacy policy.

---

## App Store privacy labels — one clarification

Apple's App Store privacy labels use Apple's own definition of "collect", which turns on data leaving your device. That definition is useful for reading the labels and nothing more. It does not shrink our duties under state or national privacy law, and we have not used it to narrow anything in this policy. If you ever find the labels on our App Store page saying less than this policy does, this policy is the fuller account — tell us and we will correct the listing.

**The app's own privacy manifest.** The shipping build includes an Apple privacy manifest (`PrivacyInfo.xcprivacy`). It declares the one "required reason" API OmniMath uses — Apple's `UserDefaults`, for the four on-device items listed near the top of this policy — and declares no data collected by the app itself, because the app itself collects none. It does **not** declare app tracking, for a reason worth stating plainly: Apple requires a list of tracking domains alongside such a declaration, and Google publishes none for the Mobile Ads SDK. Do not read our manifest as a promise that no advertising identifier ever leaves your device — it can, exactly as described in the Advertising section above. The advertising collection is declared in Google's own manifests inside its SDKs, which Apple combines with ours.

---

## Changes to this policy

We will update this policy when the app changes — and, where we can, before the change ships. When we do, we will change the effective date at the top and describe what changed. If a change materially expands what is collected or who receives it, we will surface it in the app rather than relying on you to re-read this page.

**This revision (8 August 2026)** corrected statements in the previous version so that they match the code that actually ships. Specifically: the paragraph about withdrawing advertising consent now describes the **Settings → Ads → Ad privacy choices** row that exists in the build, instead of describing it as forthcoming; the paragraph about the app's privacy manifest now describes what that manifest actually declares, replacing an earlier statement that it would declare tracking as enabled with Google's advertising domains — it does not; and two internal review notes that should never have been published were removed. Nothing about what the app collects or who receives it changed in this revision; the description of it got more accurate.

The current version of this policy, and the policies for Prameya's other apps, are always at <https://prameyallc.github.io/privacy/>.

---

## Contact

**Prameya LLC**
Email: **admin@prameya.legal**
Privacy policies for all Prameya apps: <https://prameyallc.github.io/privacy/>
This policy: <https://prameyallc.github.io/privacy/omnimath/>

This page is also reachable from inside the app: **Settings** (the gear in the Codex tab toolbar) → **Privacy** → **Privacy Policy**.

If you are writing about a privacy right, say which right and which app, and we will get to it faster.
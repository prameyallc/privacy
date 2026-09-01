# OmniMathematics Privacy Policy

**Effective date:** 30 August 2026
**Publisher:** Prameya LLC ("Prameya", "we", "us")
**App:** OmniMathematics for iPhone — bundle ID `legal.prameya.OmniMathematics`
**Contact:** admin@prameya.legal
**Scope:** This policy covers the OmniMathematics iOS app and nothing else. Prameya's other apps have their own policies, because they work differently. Index: <https://prameyallc.github.io/privacy/>
**Canonical public URL (slug stays `omnimath`):** <https://prameyallc.github.io/privacy/omnimath/>

---

## The short version

- **There are no accounts.** No sign-in, no email address, no name, no profile. There is nothing to fill in.
- **Your learning progress is yours.** Completed chapters and pack progress are written on the device and, if you are signed in to iCloud, roam through your CloudKit private database so your other Apple devices can continue. We do not run a server that receives them. We have no database of users.
- **OmniMathematics does not talk to our servers.** Every lesson, concept and worked example ships inside the app download. Paths off the device are Apple's (StoreKit, iCloud) and, if on-device Ask fetches model weights, Hugging Face.
- **OmniMathematics has no ads and no App Tracking Transparency prompt.** AdMob, Google's User Messaging Platform, and the advertising identifier request were removed on 12 August 2026 in commit `df7919f`. The last ad-injection code in the app's view layer was removed on 16 August 2026.
- **There is no advertising identifier (IDFA) collection.** The app ships no advertising SDK. Recipients that are not Prameya: Apple (App Store checkout if you buy Pro; iCloud if you are signed in) and, if on-device Ask downloads weights, Hugging Face (repository id and the device IP — not your question and not your marks).
- **The app asks for no other permissions.** No camera, photos, microphone, location, contacts, health or files.
- **Ask is retrieval first.** Matching excerpts come from the sourced packs and Codex on the device. If an on-device model is installed it may rephrase that excerpt, labelled as generated and able to be wrong. Your question is not sent to us.
- **Purchases go through Apple.** If you buy OmniMathematics Pro, StoreKit talks to Apple to complete the purchase and to check that it is still valid. We receive a transaction identifier and entitlement status from Apple. We do not collect payment details. Chapters, Codex and your marks stay free either way.
- **OmniMathematics is built for a general audience** — computer-science students, self-learners and adults. It is not in the App Store Kids Category.
- **No health data of any kind** is involved. See "Health data" below.

---

## What OmniMathematics is

OmniMathematics teaches discrete mathematics for computer science through written lessons, a searchable Codex of concepts, and interactive demonstrations. All of the learning content ships inside the app.

Until 12 August 2026 advertising paid for it, and earlier versions of this policy said so. That business model was removed from the code, not merely disabled. As of 26 August 2026 the app offers OmniMathematics Pro (monthly, annual, or lifetime) through Apple's in-app purchase. Apple processes the payment. We do not collect payment card numbers or billing addresses. Knowledge — the chapters, the Codex, the sourced packs — stays free.

---

## What stays on your device

OmniMathematics writes the following on the device (SwiftData; older installs migrated once from Apple's `UserDefaults`):

| What | Why |
|---|---|
| Which chapters you have completed | To show your Journey progress |
| Which knowledge packs you have worked through | Same |
| Chapter and pack progress | Same |
| The last chapter you visited, and the realm it belongs to | To take you back where you were |
| Which step of that lesson you had reached | Same |
| The last knowledge pack you opened | Same |
| Whether you have seen the intro screens | So onboarding shows once |

That is the complete list of *what* is stored. We cannot see it, and we have no way to request it.

If you are signed in to iCloud, those marks roam through **your** CloudKit private database, and a tiny iCloud key-value store remembers the last lesson so Apple Watch and Apple TV can continue it. Prameya cannot open another person's private database. Removing a mark in **More → Progress** updates the iCloud copy. Deleting the app on one device does not by itself empty iCloud.

*Correction, 16 August 2026:* earlier versions of this policy described "four things". That undercounted — the app also records the realm, the lesson step and the last knowledge pack. The list of *what* is stored was wrong and is now complete.

*Correction, 30 August 2026:* earlier versions said this data "never leaves your phone" and that "the app has no iCloud capability enabled at all". Both sentences stopped being true when study-mark CloudKit and Continue key-value sync shipped. The list of fields did not grow; the *place they can live* did.

Two ordinary caveats that are true of any iPhone app:

- If you use iCloud or iTunes device backup, this data is included in your backup, under Apple's terms and your control.
- You can clear the on-device copy any time with **More → Progress → Reset All Progress**. That also updates the iCloud copy. Deleting the app on one device is not enough on its own if iCloud still holds the record.

---

## What OmniMathematics does not do

One line each, because the honest answer is short.

- No user accounts, and no way to create one.
- No ads of any kind — no banners, no interstitials, no rewarded ads.
- No advertising identifier (IDFA), no `AdSupport`, no SKAdNetwork entries, no App Tracking Transparency prompt.
- No advertising SDKs. The on-device Ask runtime is mlx-swift / mlx-swift-lm; optional weight download uses Hugging Face's libraries. There is still no analytics SDK and no ad SDK.
- No network requests to us. There is no upload path and no server of ours for the app to talk to. StoreKit may talk to Apple if you buy or restore Pro. iCloud may sync your marks when you are signed in. Ask may fetch model weights from Hugging Face.
- Nothing you write, draw, tap, search or type in the Ask box is transmitted to us. The question stays on the device; a generated rephrase, if any, is produced on the device.
- No camera, photo library, microphone, contacts, calendar, or file access.
- No location permission is requested, and the app uses no location APIs. Nothing in the app estimates your location by any other means either.
- No health, fitness or medical data of any kind.
- No analytics or crash-reporting service — ours or anyone else's.
- Purchases, if you make one, go through Apple StoreKit. We do not collect payment details.

---

## Advertising — removed

**OmniMathematics shows no ads, and no data leaves your device for advertising or for anything else.**

This section used to be the longest in the policy, because it was the one place data left your device. It described banner and interstitial ads served by Google AdMob, ad loading that began the moment you opened the app, Google's consent form for the EEA and UK, the advertising identifier being used for cross-app tracking, a coarse location Google's ad software estimated from your IP address, SKAdNetwork install measurement, and an in-app control for reporting a bad ad.

None of that is true of the shipping app, and every word of it is deleted here:

- **12 August 2026, commit `df7919f`** — the Google Mobile Ads SDK, the User Messaging Platform (consent) SDK, the whole `App/OmniMathematics/Ads` tree, the `NSUserTrackingUsageDescription` string, the SKAdNetwork identifier list and the ATT request were removed from the app. The **Settings → Ads → Ad privacy choices** row was removed with them; there is no consent form left for it to reopen. The in-app ad report control went at the same time, with the ad container that hosted it.
- **16 August 2026** — `MathAds.swift`, the last ad-injection seam in the view layer (banner and interstitial slots, `AdTileView`), was deleted. Nothing referenced it.
- The build now enforces this. `ci_scripts/ci_post_clone.sh` **fails the build** if `ThirdParty/GoogleAdsSPM` or `App/OmniMathematics/Ads` is ever restored, and a test suite asserts that no ad symbols are linked.

**Google receives nothing from this app.** Google is no longer a recipient of any data from OmniMathematics. The links to Google's privacy policy and ad settings that used to appear here have been removed rather than left as decoration: pointing you at a third party's controls implies that third party has something of yours, and it does not. Recipients that are not Prameya are named in the short version: Apple (StoreKit and, if you are signed in, iCloud) and Hugging Face (optional model-weight download).

**This part is on us, not on the reader.** The top of this policy was corrected on 12 August 2026 to say the ads were gone, while the body below it went on describing them in the present tense for four days. A policy that contradicts itself in one file is worse than one that is merely out of date, because a reader cannot tell which half to believe. The whole document has now been read against the shipping binary.

---

## Ask the Codex, and the optional on-device model

Every sourced explanation and worked example in the app was written by a person and ships inside the download from the App Store.

The Codex has an **Ask** box. The default answer is a deterministic lookup over the lessons and concept entries already on your phone: it finds the closest passage and shows you that passage, copied word for word from the shipped curriculum, labelled **From the Codex**.

If on-device generation is available, Ask may then rephrase that same excerpt on the device. Generated text is labelled **On-device model** and carries a persistent notice that it can be wrong. Retrieval remains the fallback when weights are missing, when generation is refused, or on Apple Watch (which never links the model runtime).

Weights, when fetched, come from Hugging Face (`mlx-community/Qwen3-0.6B-4bit`) using the mlx-swift runtime. That request carries the repository identifier and the device's IP address. It does not carry your question, your marks, or the curriculum. Nothing you type is sent to us or to a hosted model API.

Your question is not stored as its own record. Chapter and pack marks are a separate store, described above.

---

## If you email us

If you write to admin@prameya.legal — a question, a bug report, a rights request — we receive your email address and whatever you put in the message. We keep it only as long as we need it to deal with your message and to keep a record that we did, and you can ask us to delete it. That mailbox is the only place Prameya holds anything about a user of this app.

---

## Children and OmniMathematics

**Who OmniMathematics is for.** University and later-secondary computer-science students, self-taught programmers, and adults who want to understand discrete mathematics. It is a general-audience educational app. It is not in the App Store Kids Category, it is not designed or marketed for young children, and its content, artwork and language are aimed at older students and adults.

**What that means in practice, stated plainly.** Nothing is collected from anyone who uses OmniMathematics, at any age, by us. There is no identifier we transmit, no advertising network, and no server of ours. If a parent buys Pro, Apple processes that purchase (Family Sharing is on). A child using this app is in the same position as an adult using it for learning data: progress is written on the device and, if that Apple ID is signed in to iCloud, roams through that account's private database.

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

**Do Not Sell or Share My Personal Information.** We do not sell personal information, and we do not share it for cross-context behavioural advertising. Until 12 August 2026 this section said the opposite, and it was accurate then: advertising identifiers and ad-interaction data were disclosed to Google for personalised advertising, which California calls "sharing". That disclosure stopped when the ad SDK was removed. There is now no advertising recipient and no advertising identifier, so there is nothing to opt out of for that kind of sharing. Apple (StoreKit, iCloud) and Hugging Face (optional model weights) are not cross-context behavioural advertising. The opt-out this section used to name — denying tracking under iOS Settings → Privacy & Security → Tracking — no longer applies either, because OmniMathematics never asks to track and so does not appear in that list.

**Categories.** We collect none of the CCPA categories. No identifiers, no internet or network activity, no geolocation of any precision, no name, contact details, financial information, biometric, health, employment or education records. The only personal information Prameya ever holds about a user of this app is an email you choose to send us, at the address above.

**Sensitive personal information.** OmniMathematics does not collect sensitive personal information as California defines it. There is nothing here for a "Limit the Use of My Sensitive Personal Information" control to limit.

**Minors.** We do not sell or share the personal information of consumers under 16 — or of anyone else, at any age.

**Global Privacy Control.** GPC is a browser signal and there is no established equivalent for native iOS apps. It makes no difference here: there is no sale or sharing for a GPC signal to stop.

**A candid note on scope.** Prameya is a very small company and may fall below the revenue and volume thresholds that make the CCPA legally binding. We describe and honour these choices regardless of whether we are required to.

### Other US states

Virginia, Colorado, Connecticut, Texas, Oregon, Montana and a growing number of other states give residents rights to access, correct, delete and port personal data, and specifically to opt out of targeted advertising and profiling. If any of those laws applies to us, the answer is the same one: no targeted advertising occurs in OmniMathematics, no profiling occurs, and no personal data is collected to access, correct, delete or port. Email us for anything else. Some of these states offer an appeal if we refuse a request — if we ever refuse yours, we will tell you how to appeal and how to contact your state Attorney General.

### EEA and United Kingdom (GDPR / UK GDPR)

OmniMathematics is available worldwide, so this section applies if you are in the EEA or the UK.

**Controller.** Prameya LLC, contact admin@prameya.legal, is the controller for the only processing it carries out — correspondence you send us. There is no joint controller, and no processor: nobody processes personal data on our instructions. Google was previously an independent controller for advertising data collected through its own software in the app; since 12 August 2026 it receives nothing. Since 26 August 2026 one other party is in the picture: **Apple**, which runs the App Store checkout if you buy OmniMathematics Pro. Apple decides for itself what it does with that transaction; we do not direct it, we receive no payment details from it, and we receive nothing at all from it unless you buy.

**Legal bases.**

- *Answering your email:* legitimate interests, or the steps needed to respond to you.

That is the whole list. The advertising entries that used to sit above it — consent for personalised advertising, and legitimate interests in funding a free app through contextual ads — are gone because the processing they described is gone.

**Consent.** No consent form appears in OmniMathematics. Google's consent form (the User Messaging Platform) was removed on 12 August 2026 along with the advertising it gated. There is no advertising consent to give, withdraw or re-open.

**Profiling.** None. No automated decision-making of any kind takes place, and nothing in the app builds a profile of you.

**Special-category data (Article 9).** None is processed. There is no health, biometric, racial, religious, political, trade-union or sexual-life data anywhere in this app.

**Your rights.** Access, rectification, erasure, restriction, portability, objection to processing based on legitimate interests, and withdrawal of consent. In practice these reach only an email you have sent us, because that is all that exists.

**International transfers.** None of yours, by us. We do not hold learning data to transfer. Purchases, if you make one, are processed by Apple.

**Complaints.** You may complain to your national data protection authority, or to the UK Information Commissioner's Office if you are in the UK.

**Children in Europe.** Where consent is the legal basis for processing a child's data, GDPR requires the child to be at least 16, or younger only with the consent of a parent or guardian, subject to each member state's lower age limit (never below 13). No consent-based processing of anyone's data occurs in OmniMathematics. See "Children and OmniMathematics" above.

---

## Security

There is not much to secure, and that is the design.

- Your learning data stays in your app's private storage on your device, protected by iOS and your passcode, and — if you are signed in — in your iCloud private database under Apple's terms. Use a passcode and keep iOS up to date.
- The app does not talk to our servers, so there is no traffic of yours to intercept on a path we run. StoreKit is Apple's API and may contact the App Store if you buy or restore Pro. iCloud is Apple's API for the private database and the Continue key-value store. Optional Ask weight download talks to Hugging Face. The transport-security discussion that used to sit here covered the advertising SDK's traffic; there is no such traffic now.
- We operate no server holding user data, so there is no user database of ours that could be breached.

We make no claim to unbreakable security. No system is perfectly secure.

---

## Data retention

- **On your device:** kept until you clear it (More → Progress → Reset All Progress) or delete the app.
- **In your iCloud, if you are signed in:** the same marks, plus the last-lesson Continue payload, until you remove them in the app (which updates the iCloud copy) or you delete the iCloud data. Deleting the app on one device does not by itself empty iCloud.
- **With us:** only emails you send us, kept as long as needed to handle your message and to record that we handled it. Ask and we will delete yours.
- **With Apple, if you buy Pro:** Apple keeps its own record of the transaction, under Apple's terms and Apple's retention rules rather than ours. What we hold is the entitlement state StoreKit reports, and that stays on your device with everything else.
- **With Hugging Face, if Ask fetches weights:** the repository identifier and the device IP, under Hugging Face's terms. We do not receive that request.
- **With anyone else:** nothing.

---

## App Store privacy labels — one clarification

Apple's App Store privacy labels use Apple's own definition of "collect", which turns on data leaving your device. That definition is useful for reading the labels and nothing more. It does not shrink our duties under state or national privacy law, and we have not used it to narrow anything in this policy.

---

## Changes to this policy

We will update this policy when the app changes — and, where we can, before the change ships. When we do, we will change the effective date at the top and describe what changed. If a change materially expands what is collected or who receives it, we will surface it in the app rather than relying on you to re-read this page.

**1 September 2026 — what changed (bundle identifier, again).** The identifier is now
`legal.prameya.OmniMathematics`, matching the repository, project, scheme and display name, and
matching how every other app in the portfolio is named. The 27 August entry below recorded the
opposite decision — keeping the shorter `legal.prameya.OmniMath` because Apple already held it —
and that reasoning was sound at the time. The owner has since chosen portfolio-wide consistency,
accepting that Apple ID 6789206341 cannot be renamed and a new App Store record will be created
instead. **Nothing about what is collected, stored or transmitted changed with it.** The public
URL slug stays `omnimath` and this page's canonical address is unchanged.

**30 August 2026 — what changed.** Two paths that had already shipped in the binary were named here: study marks roam through the user's CloudKit private database (and a tiny iCloud key-value store remembers the last lesson for Watch and TV), and Ask may fetch on-device model weights from Hugging Face. Earlier sentences that said the app had "no iCloud capability", "no AI model" and "no third-party SDKs" were false against that binary and are deleted from the body rather than left standing. Prameya still collects nothing and still runs no server of users. The published Pages copy is updated in the privacy repository separately.

**27 August 2026 — what changed (bundle identifier).** The app's bundle identifier was set to `legal.prameya.OmniMath`. It had been `legal.prameya.OmniMathematics` in this policy and in the project until that day. A bundle identifier cannot be edited once Apple holds it, and the App ID Apple holds for this listing (Apple ID 6789206341) is `legal.prameya.OmniMath` — so the two sides were reconciled by moving the one that could move, which was the binary. Registering the longer identifier as a second App ID would have orphaned this listing, its reviews, its ratings and this policy's own published URL. (Superseded on 1 September 2026 — see the entry above.) **Nothing about what is collected, stored or transmitted changed with it**: the identifier names the app to the operating system and to the App Store, and it is disclosed here only so that the app you install and the app this policy describes are the same app. The app name, the public URL slug `omnimath`, and this page's canonical address are all unchanged.

**27 August 2026 — what changed.** Three sentences left over from the no-commerce era were corrected, because they contradicted the StoreKit disclosures added the day before and a policy that contradicts itself in one file is worse than one that is merely out of date. The short version said "no third party receives anything" four bullets above the bullet describing Apple taking your money; the retention section said "no third party has anything to retain" when Apple retains the transaction record; the GDPR controller paragraph said "no third party receives personal data through this app". All three now name Apple's role in an App Store purchase. Nothing about what *we* collect changed — we still collect nothing — and no new recipient was added; the recipient added on 26 August was simply not carried through the whole document.

**26 August 2026 — what changed.** OmniMathematics Pro is offered through Apple StoreKit (monthly, annual, lifetime). Apple processes the purchase; we receive a transaction identifier and entitlement status; we do not collect payment details. StoreKit talking to Apple is the commerce path. Chapters stay free. The published Pages copy is updated in the privacy repository separately.

**23 August 2026 — what changed.** The legal name on this page is **OmniMathematics**. The public URL slug stays `omnimath`. ⚠️ This entry also quoted a bundle identifier, and that identifier changed on 27 August 2026 — see that entry. The quotation is removed rather than left standing beside a correction, because a change history that keeps asserting a retired identifier is a second place for a reader to be told the wrong one; the identifier is stated once, in the header at the top. User-facing “Insight Stars” copy is chapter and pack progress; reset is **More → Progress → Reset All Progress**.

**21 August 2026 — what changed.** The unused StoreKit scaffold that this policy used to describe as a `Monetization` module with product identifiers was deleted from the app. That deletion did not last: StoreKit Pro returned on 26 August 2026 (see that entry). The live URL for this page is <https://prameyallc.github.io/privacy/omnimath/>.

**16 August 2026 — what changed.** Advertising was removed from OmniMathematics in commit `df7919f` on 12 August 2026, and the last ad-injection code in the view layer was removed on 16 August 2026. On 12 August the summary at the top of this policy was corrected, but the body was not: for four days this file said "no ads" in its first section and then described banner ads, interstitials, ad load timing, Google's data-collection table, the advertising identifier, IP-derived coarse location, SKAdNetwork and an ad-reporting control in the present tense. Every one of those passages has now been deleted or rewritten, along with the advertising legal bases under GDPR, the California "sharing" disclosure and its tracking-based opt-out, the ad-related retention entry, the ad-traffic security claim, and the ad-dependent reasoning in the children's section. The on-device data table was also corrected: it had listed four stored items where the app stores eight. This update removes disclosures; it adds no collection.

Older versions are kept in the public repository behind <https://prameyallc.github.io/privacy/>.

---

## Contact

**Prameya LLC**
Email: **admin@prameya.legal**
Privacy policies for all Prameya apps: <https://prameyallc.github.io/privacy/>
This policy: <https://prameyallc.github.io/privacy/omnimath/>

If you are writing about a privacy right, say which right and which app, and we will get to it faster.

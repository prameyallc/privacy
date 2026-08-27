# OmniDent Privacy Policy

**Effective date:** 24 August 2026 *(supersedes the 21 August 2026 version; section 9 now matches the per-record delete controls and the photograph-carrying export)*
**Publisher:** Prameya LLC, a United States limited liability company ("Prameya", "we", "us")
**Contact:** admin@prameya.legal
**This policy lives at:** https://prameyallc.github.io/privacy/omnident/
**All Prameya app policies:** https://prameyallc.github.io/privacy/

> ### Consumer health data
> OmniDent processes consumer health data. Washington State law requires a separate policy for that. It is here, and it is a distinct document from this one:
> **[OmniDent Consumer Health Data Privacy Policy](https://prameyallc.github.io/privacy/omnident/health-data/)**
> If you live in Washington or Nevada, please read it. It applies to you in addition to this policy.

---

## The short version

- OmniDent lets you photograph your own teeth and gums, keep a dated record, log home-care habits, and get educational information.
- **Your photos stay on your iPhone or iPad.** They are saved inside the app's private storage. They are never sent to Prameya. Prameya operates no server that receives your photos, your analysis, or your notes.
- **The AI runs on your device.** Nothing you photograph or type is sent anywhere for analysis.
- **The app does connect to the internet in three narrow ways**, and we describe each one below: downloading AI model files from Hugging Face when you ask it to, syncing a small amount of non-health data through your own iCloud account, and Apple's push service telling the app that iCloud data changed.
- **No ads. No analytics. No trackers. No third-party SDK that phones home.** We do not sell your data. We have never sold your data.
- **Prameya has no user database.** We do not know who you are. There is no account on our systems to look you up in.
- Sign in with Apple is optional. If you use it, you can delete your account and everything on the device from inside the app. Because OmniDent has no server and never exchanges Apple's authorization code, no Apple token for OmniDent exists — deletion clears the association held on your device and removes the app's records from your own iCloud, and there is no token for the app to revoke.
- OmniDent is an educational wellness app with **no FDA authorization of any kind**, and **HIPAA does not apply to it**. What the photo analysis puts on your screen is a written note about the image, with no condition name and no confidence score. Do not use it to decide whether to seek or delay dental care.

---

## 1. What OmniDent does

OmniDent is a direct-to-consumer app for your own oral care. It lets you:

- take photographs of your mouth with the in-app camera, and keep them as a dated record;
- run an on-device AI model over a photo to get general educational information;
- log daily habits such as brushing, flossing, mouthwash and sugary drinks;
- run illustrative cost scenarios using figures you enter;
- read general information about oral health;
- optionally share brushing and dietary-sugar entries with Apple Health.

**OmniDent has no FDA authorization.** Analysis of dental images for clinical purposes is a regulated activity in the United States. What the photo analysis puts on your screen today is a written note about the image, with no condition name and no confidence score. We are not replacing that description with a blanket "the app does not diagnose" claim — a free-text on-device chat can still name a condition, and nothing in the app filters that output. Do not act on chat or photo-note text. Ask a dentist.

Two things in the shipping app are worth stating plainly, because they involve numbers and disease words even though they are not findings about you:

- The Studio screen contains an unfinished **Regenerative Projection** feature. It lists terms drawn from your own scan history and shows a percentage range — "X–Y% chance of meaningful recovery in ~N months". **Those percentages are fixed values written into the app** and they are not a prediction about your health. The numbers themselves are constants, but *which* constant you see is chosen by matching terms in your own scan history. Do not rely on them.
- Some feature descriptions in the app still use dental-condition wording — "caries, erosion, stain & gum risks", "gingival inflammation" — to describe what a feature is about. That is subject-matter wording, not a finding the app has made about your mouth.

---

## 2. Subscriptions and In-App Purchases

### Available tiers

There is one paid upgrade, **OmniDent Pro**, sold as three products. Buying any one of
them grants exactly the same Pro — there are no separate feature tiers.

| Product | Price (US) | Billing |
|---|---|---|
| OmniDent Pro Monthly | $4.99 | Auto-renews monthly. 7-day free trial. |
| OmniDent Pro Annual | $29.99 | Auto-renews yearly. 7-day free trial. |
| OmniDent Pro Lifetime | $79.99 | One-time purchase. Not a subscription. |

Family Sharing is enabled on all three. Subscriptions renew until you cancel in
Settings; Lifetime is a one-time non-consumable.

**The knowledge layer is free and stays free.** Without paying anything you get
your routine, the reference library and a visit-prep outline, with no account and no time limit. Pro adds full photo history, cadence reminders and the visit sheet.

**Pro does not add cloud sync, and there is no paid iCloud option.** OmniDent stores your
records on your device in every case, paid or not. If a subscription lapses you keep your
own data and can still export it in its raw form; only the Pro tools stop.


### Free vs paid tier data collection

**Both tiers process the same consumer health data** (listed in the [Consumer Health Data Privacy Policy](https://prameyallc.github.io/privacy/omnident/health-data/)).

- **Free:** Photos analysed on-device, your routine, the reference library and a visit-prep outline
- **With Pro:** Photos analysed on-device (same models), full photo history, habits logged locally, cadence reminders and the visit sheet

In both tiers:
- Photos stay on your device
- No health data syncs to iCloud
- No transmission of photos or analysis to Prameya
- Same AI models, same on-device processing

**Subscription unlocks features. It does not change what data is collected or where it goes.**

### Cancellation and refunds

Subscriptions are managed by Apple:
- **Cancel:** iOS Settings → your name → Subscriptions → OmniDent
- **Refund requests:** reportaproblem.apple.com

Prameya cannot cancel your subscription or issue refunds. Apple controls all billing.

### StoreKit transaction data

When you purchase a subscription, the app receives and stores locally on your device:
- Transaction ID (an opaque identifier from Apple)
- Product ID (which tier you purchased)
- Purchase and expiration dates

This data:
- Is stored only on your device
- Is NOT synced to iCloud
- Is used only to unlock tier-appropriate features
- Is deleted when you use "Delete All Data"

---

## 3. Photographs of your mouth

Photographs of a person's mouth are sensitive. Here is exactly what happens to them.

### Where they are stored

When you take a photo in OmniDent, the image is written as a JPEG file into the app's own private storage on your device — the `Documents/Scans` folder inside the OmniDent sandbox. A small thumbnail and some metadata (the date, a capture-quality number, the analysis output) are stored in the app's local database, also on your device.

That storage is protected by iOS Data Protection at the **Complete** level. In practical terms, the files are encrypted with a key tied to your device passcode and are unreadable while the device is locked. This is why OmniDent requires a passcode-protected device to be meaningful — if you have no passcode, iOS has nothing to protect the files with.

### Where they are not stored

- **They are never uploaded to Prameya.** We have no server that could receive them.
- **They are not synced to iCloud by OmniDent.** The app's iCloud sync deliberately excludes photos and analysis. The local photo database is configured with cloud sync switched off entirely.
- They are not sent to Hugging Face, to any AI provider, to any partner, or to any advertiser.

One thing this does **not** mean: OmniDent does not mark the `Documents/Scans` folder as excluded from your device backup. If you back your iPhone or iPad up to iCloud or to a computer, those files are part of that backup, in your own Apple Account or on your own computer, under Apple's terms rather than ours.

### One important exception: your own Photos library

OmniDent has a setting called **auto-save captures to Photos**. When it is on, every new photo you take in the app is also copied into your device's system Photos library, the same place your ordinary camera photos go.

**This setting is off by default.** You have to turn it on.

If you turn it on and you use iCloud Photos, that means new mouth photos will be backed up to your personal iCloud Photo Library, under your Apple Account, subject to Apple's terms — not ours. This is still your data in your account, and Prameya still never sees it. But it does leave OmniDent's protected container, and you should know that.

You can turn it on at **Settings → Photos** inside OmniDent. You can also revoke OmniDent's permission to add to your Photos library at any time in iOS Settings → Privacy & Security → Photos.

### Photos you pick from your library

Some screens let you attach a photo from your library to an on-device chat. That uses Apple's system photo picker. OmniDent receives only the single image you pick. It has no access to the rest of your library.

### Deleting photos

- A single photo: open the scan and delete it. The JPEG file and its database record are both removed.
- Everything: **Settings → Privacy & Security → Delete All Scans & Data**. This is immediate and permanent, and it includes your stored oral-health profile (age, brushing frequency, sugar intake, smoking, diabetes, dry mouth, goals).
- If you turned on auto-save to Photos, copies in your Photos library are yours to delete in the Photos app. OmniDent cannot reach into your Photos library to remove them, and does not try to.

---

## 4. The on-device AI, and the one thing it downloads

### Analysis happens on your device

OmniDent uses Apple's MLX framework to run vision and language models locally, on your device's own chip. When you analyse a photo or ask a question in the chat, the image and the text are processed in memory on your device. **They are not transmitted to Prameya, to a cloud AI provider, or to anyone else.** There is no remote inference path in the app, and no remote fallback.

### Model files come from Hugging Face

The models themselves are large files that are not shipped inside the app. To use an AI feature you first download a model, and **that download comes from Hugging Face** (`huggingface.co`), the public repository where these open models are published.

What that means precisely:

| Question | Answer |
|---|---|
| What is sent to Hugging Face? | A request for a model file — the repository name and the file being fetched. Standard web request information such as your IP address is visible to Hugging Face, as it is to any website you connect to. |
| Is any of your content sent? | **No.** No photograph, no analysis result, no habit log, no chat message, no identifier of you. |
| When does it happen? | Only when you tap Download in **Settings → AI Models → Manage Models**. Taking a photo or running an analysis will never silently start a download — if a model is not already on disk, the app declines to run rather than fetch it. |
| Which models? | Open 4-bit and 8-bit builds published by the `mlx-community` organisation, including `SmolVLM-Instruct-4bit`, `gemma-3-4b-it-qat-4bit`, `paligemma-3b-mix-448-8bit`, `Qwen2.5-0.5B-Instruct-4bit`, `Llama-3.2-1B-Instruct-4bit` and `gemma-4-e2b-it-4bit`. |
| Where do they go? | Onto your device. You can delete any downloaded model from the same screen. |

The app does **not** currently show a disclosure sheet naming the download host, the file size and the model licence before a download begins. This section is that disclosure.

Hugging Face is not our processor and receives nothing about you from us. Your connection to them is governed by their own privacy policy.

---

## 5. Sign in with Apple, and how to delete your account

Signing in is **optional**. OmniDent works fully without it.

If you choose **Sign in with Apple**, this is what we get and where it goes:

- an opaque Apple user identifier — a random-looking string that identifies you to this app only;
- your name and email address, **only if Apple passes them and only on the very first sign-in**. Apple lets you use its private email relay instead of your real address, and we recommend it.

All three are stored in your device's **Keychain**. They are used for one thing: to associate your device with your own private iCloud data so it can roam between your devices. **They are not sent to Prameya.** We have no account record for you, no profile database, and no way to look you up.

### Deleting your account

Apple requires that an app offering Sign in with Apple also lets you start account deletion from inside the app. Where an app has exchanged Apple's authorization code for tokens on its own server, Apple additionally requires those tokens to be revoked through Apple's Sign in with Apple REST API.

**OmniDent has no server and never exchanges the authorization code.** No access token and no refresh token for OmniDent is ever minted, so none exists anywhere to revoke, and **the app makes no revocation call**. The only thing that ever exists is the app-scoped identifier sitting in the Keychain on your own device, and deleting that is the whole of the deletion rather than part of it.

In OmniDent, **Settings → iCloud Sync → Delete Account & All Data** does all of the following:

1. clears the Apple user identifier, name and email from this device's Keychain, ending the association;
2. removes the records this app placed in your private iCloud database, by deleting the app's CloudKit zone — if you are not signed into iCloud, are offline, or the zone was never created, there is nothing there to remove and the step simply completes;
3. turns iCloud sync off;
4. deletes your local data, including the photo files in `Documents/Scans`, your scans and analyses, habit logs, trajectory scenarios, programme progress and your oral-health profile.

If you also want OmniDent removed from the list of apps you have used Sign in with Apple with, that control belongs to Apple, not to us: **iOS Settings → your name → Sign in with Apple → OmniDent**. You can use it at any time, before or after deleting in the app.

You can also sign out without deleting, which clears the Keychain entries on that device but leaves your data in place.

---

## 6. iCloud sync — what is excluded

OmniDent can sync a small amount of data between your own devices using **CloudKit**, Apple's iCloud service. Two things are true of this and both matter:

1. The data goes into **your private iCloud database**, inside your own Apple Account. It does not go to Prameya. We cannot read it. We have no CloudKit administrative access to your private database.
2. **No health data syncs.** Your photographs, your analysis results, your oral-health profile and your habit history do not sync. They stay on the device that created them.

### Why health data is excluded

**This is required by Apple Guideline 5.1.3(ii)**, which prohibits storing personal health information in iCloud. OmniDent complies:

1. The health database is created with `cloudKitDatabase: .none`
2. Photographs, analysis results, and oral-health profile are excluded from the sync schema
3. An automated test (`CloudKitBoundaryTests`) fails the build if any health record type is added to the sync container
4. If the exclusion list ever drifts, sync switches itself off entirely rather than transmit something it should not

What syncs:

| Syncs | Does not sync |
|---|---|
| App preferences (which AI model you prefer, whether AI features are enabled, auto-save-to-Photos setting) | Photographs |
| Interface state (whether you have seen the welcome screen, whether you acknowledged the wellness disclaimer) | Analysis results and any finding derived from a photograph |
| The list of models you have downloaded | Your health profile (age, brushing frequency, sugar intake, smoking, diabetes, dry mouth) |
| | Habit logs (brushing, flossing, mouthwash, sugary drinks) |
| | Cost trajectory scenarios and 30-day programme progress |

That list is not a description of good intentions: the set of records permitted to sync is pinned in the app by an allow-list, and if anything ever drifts from it, sync switches itself off entirely rather than send something it should not.

You can turn sync off entirely at **Settings → iCloud Sync**.

Because sync uses CloudKit, iOS uses Apple's push service to tell the app that something changed. That is a silent, content-free signal. **OmniDent sends no marketing or promotional push notifications, and Prameya sends you no push notifications at all.**

---

## 7. Apple Health

Apple Health integration is **off until you turn it on** and grant permission through iOS.

If you enable it:

- **OmniDent writes** the toothbrushing and dietary-sugar entries you log in the app into Apple Health, so they sit alongside your other health data.
- **OmniDent reads** four things, to show optional context alongside your habits: step count, sleep analysis, mindful minutes, and active energy burned.

Apple Health data lives in Apple's Health store on your device, under your control. **Prameya never receives it.** You can revoke either direction at any time in iOS Settings → Health → Data Access & Devices, or turn the whole integration off in OmniDent's settings.

OmniDent does not request access to Health Records (clinical records from a provider) and cannot read them.

---

## 8. Everything the app sends over the network — the complete list

| Destination | What goes there | When | Contains your content? |
|---|---|---|---|
| `huggingface.co` | A request for an AI model file | Only when you tap Download in Manage Models | No |
| Apple iCloud (CloudKit), your private database | App preferences and interface state; a request to delete the app's zone when you delete your account | While iCloud Sync is on, and at account deletion | No health data |
| Apple push notification service | A silent signal that iCloud data changed | While iCloud Sync is on | No |
| Apple (Sign in with Apple) | The sign-in exchange itself, handled by iOS | Only if you choose to sign in | No |

There is no token-revocation request in that list, because there is no OmniDent token to revoke — see section 4.

All connections use HTTPS. The app disallows unencrypted connections at the platform level.

**That is the whole list.** There is no analytics endpoint, no crash-reporting endpoint, no advertising network, no attribution SDK, no remote AI service, and no Prameya server of any kind. The app's privacy manifest declares no crash data, no tracking and no tracking domains, and no crash-reporting SDK is built into the app.

### What Prameya does receive

Almost nothing, and none of it from the app:

- **Aggregate App Store statistics from Apple** — downloads, territories, crash counts. Apple provides these in aggregate. They do not identify you. If you have Apple's "Share with App Developers" analytics setting enabled at the system level, Apple may include your device's crash reports in what it shares with us; you control that in iOS Settings → Privacy & Security → Analytics & Improvements.
- **Emails you send us.** If you write to admin@prameya.legal, we have your email and whatever you put in it. We keep support correspondence only as long as needed to handle it.

---

## 9. Things we do not do

One line each, because the honest answer is short.

- **We do not sell your personal information.** We never have.
- **We do not share your personal information for cross-context behavioural advertising.**
- **We do not show ads.** There is no ad SDK in the app.
- **We do not track you across apps or websites.** The app declares no tracking and no tracking domains, and does not ask for the App Tracking Transparency permission because it has nothing to track you with.
- **We do not use third-party analytics.**
- **We do not build a profile of you.** We have no database in which to put one.
- **We do not use your photographs or your data to train AI models.** Not ours, not anyone's.
- **We do not share your data with dentists, insurers, employers, or the "partner" offers shown in the app.** Those offers are informational only; tapping one records a note on your device and transmits nothing.
- **We do not use geofencing** around dental offices, hospitals, pharmacies or any other health care facility. The app requests no location permission and contains no location code.
- **We do not contribute your data to any shared or "collective" dataset.** The Studio screen shows a toggle offering "private collective priors" with an optional anonymised contribution. That feature is not built: switching it on only swaps in different fixed numbers already inside the app, and nothing is transmitted to us or to anyone else.

---

## 10. Retention, export and deletion

**Retention.** Because your content lives on your device, you decide how long it is kept. We impose no retention period because we hold nothing to retain. If you delete the app, iOS deletes its container and everything in it. Data synced to your private iCloud database is removed when you delete your account in the app, or when you delete the app's iCloud data from iOS Settings → your name → iCloud.

**Export.** **Settings → Privacy & Security → Export My Data** produces a **`.zip` file**, generated entirely on your device, and hands it to the standard iOS share sheet so you can put it wherever you want. Inside it:

- `export.json` — your photo records, the caption and view tag you wrote on each one, your logged care days, your saved what-if scenarios, your claimed partner promotions, your 30-day programme progress and your oral-health profile. The per-scan entries include the coded dental vocabulary terms derived from each photo's analysis, alongside the capability labels and the number of findings.
- `Photos/` — **every photograph you took in OmniDent, at full resolution**, under the file name the matching scan entry gives as `photoFileInExport`.
- `Thumbnails/` — the small preview of each one.

If a photograph's file is missing from your device — it was removed outside the app, for example — the scan entry is still exported, marked `photoFileMissingOnDisk`, with the thumbnail. It is not quietly dropped, and the file does not claim a picture it does not carry. If a photograph is on your device and cannot be read, no file is produced at all and the app tells you which one: a short export that looks complete is worse than no export.

The text of a note the on-device model attached to a photo is still not in the file.

**Deletion.**

| To delete | Where |
|---|---|
| One photo | Act → All your photos → tap the photo → Delete this photo (or press-and-hold the row) |
| One logged care day | Do → Your care log → tap the day → Delete this care day (or press-and-hold the row) |
| One saved what-if scenario | More → What-if → Saved Scenarios → tap it → Delete this scenario |
| One claimed partner promotion | Settings → Privacy & Security → Claimed offers → Delete this claim (the row is shown only if you have one) |
| Your 30-day programme progress | 30-Day Reset → Delete my 30-day progress |
| Your oral-health profile | Settings → Edit My Health Profile → Delete my health profile |
| Your scans, photo files, analyses, habit logs, trajectory scenarios, programme progress, claimed promotions and oral-health profile — **and** the settings store behind them: care-day history, profile names, Smile Points, widget snapshot, reminder schedule and cost-model sliders — **and** the on-device model cache | Settings → Privacy & Security → Delete All Scans & Data |
| Your Sign in with Apple association, your iCloud records for this app, and all local data | Settings → iCloud Sync → Delete Account & All Data |
| OmniDent from your Apple Account's Sign in with Apple list | iOS Settings → your name → Sign in with Apple → OmniDent |
| Data written to Apple Health | The Apple Health app |
| Photos copied to your Photos library | The Photos app |

If you want help with any of this, or you want us to confirm in writing that we hold nothing about you, write to admin@prameya.legal.

---

## 11. Security

- Photographs and app data are stored with iOS Data Protection at the Complete level — encrypted at rest and inaccessible while the device is locked.
- Your Apple sign-in identifier, name and email are stored in the iOS Keychain.
- All network connections use HTTPS. Unencrypted connections are blocked by app configuration.
- The app uses only Apple's platform cryptography and standard TLS. We make no claims about proprietary or "military-grade" encryption, because we do not use any.

The strongest security property here is structural rather than technical: **there is no Prameya server holding your data, so there is no Prameya breach that can expose it.** The corresponding limitation is equally real — the security of your data depends on the security of your device and your Apple Account. Use a passcode. Use two-factor authentication on your Apple Account.

---

## 12. Children

OmniDent is intended for adults. It is not directed to children, we do not knowingly collect personal information from a child under 13, and there is no sign-up flow, no advertising, no analytics and no social feature through which a child's information could be collected or shared.

The Children's Online Privacy Protection Act (COPPA) applies to operators of services directed to children under 13, or who have actual knowledge that they are collecting personal information from a child under 13. We believe neither applies to OmniDent. That said, oral hygiene is a subject parents share with children. If you believe a child under 13 has provided information through this app, write to admin@prameya.legal and we will help you remove it — although in almost every case the answer is that the information is on your own device and you can delete it yourself in seconds using the controls in section 10.

A parent supervising a child's brushing should be aware that the app can photograph a child's mouth and store it on the device, and that with auto-save on, those photos also go to the device's Photos library.

---

## 13. California residents

If you live in California, the California Consumer Privacy Act as amended by the California Privacy Rights Act (CCPA/CPRA) gives you specific rights.

**Categories of personal information.** Over the past 12 months, OmniDent has handled, on your device, the following categories as defined by the CCPA:

| Category | What it is here | Do we receive it? |
|---|---|---|
| Identifiers | Apple sign-in identifier, name, email — Keychain only | No |
| Sensitive personal information — health data | Mouth photographs, oral-health profile, habit logs, analysis output | No |
| Internet or network activity | The connection to Hugging Face when you download a model | No |

**We do not sell personal information, and we do not share it for cross-context behavioural advertising.** We have not done either in the preceding 12 months. We do not use or disclose sensitive personal information for any purpose other than the purposes permitted under the CCPA regulations without your direction — in practice, we do not receive it at all, so the "limit the use of my sensitive personal information" right has nothing to operate on. We provide the control anyway: turning off AI features, iCloud sync and Apple Health stops the app processing that data.

**Your rights** are to know, to access, to correct, to delete, to opt out of sale or sharing, to limit the use of sensitive personal information, and not to be discriminated against for exercising any of them.

**How to exercise them.** Because we hold no personal information about you on any server, the fastest route for access, correction and deletion is the in-app controls in section 9 — they are immediate and require no verification step. If you would rather make a formal request, or you want written confirmation of what we hold, email admin@prameya.legal with "California privacy request" in the subject. We will respond within 45 days, and may extend once by a further 45 days if we tell you why. We will verify a request by corresponding with you at the address you write from; we will not ask you for additional identity documents, because we have nothing to match them against. An authorised agent may act for you with your written permission.

We do not use personal information for automated decision-making that produces legal or similarly significant effects.

---

## 14. Washington and Nevada residents — consumer health data

Washington's My Health My Data Act (RCW ch. 19.373) and Nevada's SB 370 give you rights over consumer health data, and Washington requires a separate, distinctly linked policy for it.

**That policy is here: [OmniDent Consumer Health Data Privacy Policy](https://prameyallc.github.io/privacy/omnident/health-data/).** Both policies are also linked inside the app, as two distinct links, in Settings.

Two points worth stating in this document as well:

- **Washington's definition of "collect" is much broader than Apple's.** Apple's App Store privacy labels use "collect" to mean transmitting data off your device. Washington's statute defines it as to "buy, rent, access, retain, receive, acquire, infer, derive, or otherwise process" consumer health data in any manner. **We do not use the narrow App Store definition to claim state health-privacy law does not reach us.** Under Washington's definition, OmniDent collects consumer health data, and the separate policy is written on that basis.
- The Washington Act is enforced through the state Consumer Protection Act (RCW ch. 19.86), and a violation may be pursued by a private individual under RCW 19.86.090 as well as by the Attorney General.

---

## 15. Other US states

Several other states — including Colorado, Connecticut, Virginia, Utah, Texas, Oregon and Montana — give residents rights to access, correct, delete and port personal data, and to opt out of targeted advertising, sale, and profiling. Some require opt-in consent for sensitive data including health data.

We honour all of these. The mechanics are the same as everywhere else in this policy: the in-app controls are the fastest route, and admin@prameya.legal is the formal route. We do not conduct targeted advertising, sale of data, or profiling, so those opt-outs have nothing to switch off.

---

## 16. Outside the United States

If you use OmniDent in the European Economic Area, the United Kingdom or Switzerland, the GDPR or UK GDPR may apply. Prameya LLC is the controller for the limited processing described in this policy.

- **Legal bases.** Where processing occurs, we rely on your **consent** (Article 6(1)(a)) for optional features such as camera access, AI analysis, iCloud sync and Apple Health, and on **contract** (Article 6(1)(b)) for the core operation of the app you installed.
- **Health data (Article 9).** Photographs of your mouth and oral-health information are special category data. Our basis is your **explicit consent** under Article 9(2)(a), given through the iOS permission prompts and the in-app wellness acknowledgement. Withdraw it at any time by turning the feature off or deleting the data; withdrawal does not affect processing that already happened.
- **Your rights** — access, rectification, erasure, restriction, portability, objection, and to complain to your supervisory authority. Exercise them in-app or at admin@prameya.legal.
- **International transfers.** Your content is not transferred anywhere, because it is not transmitted anywhere. The only cross-border flows are your own connection to Hugging Face for a model file and your own iCloud data under Apple's arrangements.
- **Automated decision-making.** The on-device AI does not make decisions producing legal or similarly significant effects about you. Its output is educational information.
- **Representative.** Prameya LLC has not appointed an Article 27 or UK representative, and none is named in this policy today. If OmniDent is released in the EEA or the United Kingdom and a representative is required, we will appoint one and name them here before the app becomes available in those territories.

---

## 17. HIPAA does not apply

We say this clearly because it is genuinely useful to know, and because plenty of health apps are vague about it.

**The Health Insurance Portability and Accountability Act (HIPAA) does not apply to OmniDent.** HIPAA regulates covered entities — health plans, health care clearinghouses, and health care providers who bill electronically — and their business associates. Prameya is none of those. You are our user, not our patient. We have no treatment relationship with you and no contract with your dentist.

Two consequences follow, and the second is the important one:

1. Data you put into OmniDent is **not** protected health information under HIPAA.
2. **Do not read this as OmniDent having weaker protection.** The data does not leave your device, so the practical protection is stronger than most HIPAA-covered arrangements. But it is not HIPAA protection, and we will not imply that it is. Anyone who tells you their consumer app is "HIPAA compliant" when they have no covered-entity relationship is telling you something meaningless.

If OmniDent is ever offered through a dental practice or a dental service organisation, this analysis changes and this policy will change with it, before that happens.

---

## 18. No FDA authorization, and not medical advice

**OmniDent has no FDA authorization, clearance or approval of any kind.** It is not a substitute for examination by a licensed dentist, and it cannot see what a dentist sees. Analysis of dental images is a regulated activity in the United States. OmniDent is not an authorized device and does not claim to be.

We are not replacing that with a blanket "the app does not diagnose" claim. What can be checked:

- **Nothing the app shows you has been reviewed or authorized by any regulator.**
- **What the analysis produces is a written description of the photograph, with no condition name and no confidence score.**
- **The on-device chat is not filtered.** It can name a dental condition, describe it as yours, or suggest a treatment. Do not act on chat output. Ask a dentist.
- **Do not use anything on those screens to decide whether to seek or delay dental care.**

The percentage ranges shown by the Studio screen's Regenerative Projection feature are fixed values built into the app and are not a clinical estimate of anything (section 1).

If something in your mouth hurts, bleeds, changes, or worries you, see a dentist. Do not wait for an app.

---

## 19. Changes to this policy

We will update this policy when the app's behaviour changes — and we will update it **before** the change ships, not after.

- The effective date at the top always reflects the current version.
- **This 24 August 2026 revision** updates section 9 so the export is a `.zip` that carries the photographs themselves, and so the deletion table names the per-record controls. No category of data, source, recipient or purpose changed.
- **This 21 August 2026 revision** matches the shipping code on auto-save captures to Photos (**off** by default), withdraws the blanket "does not diagnose" wording in favour of describing the photo note and the unfiltered chat, and corrects the Studio Regenerative Projection percentages: the values are constants, but which constant you see is keyed on your own scan history.
- **The 8 August 2026 revision was a correction pass.** We re-read the shipping source code and rewrote every statement that did not match it. In particular: the previous version said that deleting your account revokes your Sign in with Apple token through Apple's REST API. It does not, and it never did — the app has no server and mints no token, so there is nothing to revoke; section 4 now describes what deletion actually does. We also corrected the name of the deletion control, described the Studio Regenerative Projection placeholder percentages, stated that scan files are not excluded from your device backup, recorded that no pre-download disclosure sheet exists, and confirmed the items that had been marked as pending internal verification and are now in the build.
- For any material change — a new destination the app connects to, a new category of data, a new third party, a change to what syncs, or the addition of any advertising or analytics — we will show an in-app notice and, where the law requires it, ask for your consent before the change takes effect. Under Washington's My Health My Data Act, collecting a new category of consumer health data, or using it for a new purpose, requires your affirmative consent first, and we will obtain it first.
- Previous versions are available on request from admin@prameya.legal.
- Continuing to use the app after a non-material change means the updated policy applies. That is not how we will handle a material one.

---

## 20. Contact

**Prameya LLC**
Privacy questions, data requests, complaints: **admin@prameya.legal**

Please put "Privacy" in the subject line. We answer every request, including the ones where the answer is "we do not have any of your data, and here is how to confirm that yourself."

All Prameya app privacy policies: https://prameyallc.github.io/privacy/
OmniDent consumer health data policy: https://prameyallc.github.io/privacy/omnident/health-data/
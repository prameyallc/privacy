# OmniDerm Privacy Policy

**Effective date:** 21 August 2026 *(supersedes the 8 August 2026 version: journal photographs, HealthKit removed, reminders off by default, no Settings model download)*
**Publisher:** Prameya LLC ("Prameya", "we", "us"), a United States limited liability company
**Contact:** admin@prameya.legal
**This policy covers:** the OmniDerm iOS app only.

**Related pages**

- **[Consumer Health Data Privacy Policy for OmniDerm](https://prameyallc.github.io/privacy/omniderm/health-data/)** — a separate, additional policy required by Washington's My Health My Data Act. If you live in Washington or Nevada, read that one too. It is a distinct document, not a section of this one.
- [Privacy policies for all Prameya apps](https://prameyallc.github.io/privacy/)
- This policy lives at [https://prameyallc.github.io/privacy/omniderm/](https://prameyallc.github.io/privacy/omniderm/)

---

## The short version

- **The photo self-check (any assessment of a skin photograph) is switched off.** It sits behind a regulatory clearance gate that is closed, so the shipping app produces no observations, flags, ratings or any other output about a photo of your skin.
- **You can still save a journal photograph.** That is a picture you picked, stored on this device, shown back to you. It is not analysed.
- **There is no account and no password.** We do not know who you are.
- **Prameya runs no server that receives your data.** We have no database of users. There is nothing on our side to hack, subpoena, or sell.
- **The shipping app does not download an on-device model.** Settings has no download control. A Hugging Face download would start only if the gated generate surface ran, and that surface is off.
- **No ads. No analytics. No tracking. We do not sell your data**, and we never will.
- **OmniDerm does not read Apple Health.** iCloud sync is off unless you turn it on. **Reminders start off** — they are local notifications from your own phone, and you turn them on in Settings.
- **OmniDerm does not diagnose anything.** It is not a substitute for a dermatologist. See "What OmniDerm will not do" below.

---

## Who we are

OmniDerm is published by Prameya LLC, a US limited liability company. You can reach a human at **admin@prameya.legal**. We do not have a phone line.

## What OmniDerm is

OmniDerm is a consumer app for skin-care habits and education. It helps you:

- keep a private journal of notes and optional photographs on this device;
- log daily habits (sunscreen in the morning, reapplying, barrier care, doing a self-check) and see your streak and consistency;
- learn about sun protection and the ABCDE self-check ideas.

## What OmniDerm will not do

OmniDerm is **not a medical device** and does **not** diagnose, screen for, or detect skin cancer or any other condition. It does not tell you whether a mole is dangerous. It does not tell you whether to see a doctor.

Features that would produce an assessment of a photograph of your skin are behind a **clearance gate that is switched off**. In the version of OmniDerm on the App Store, the app does not produce observations, flags, ratings, or any other output about a photo of your skin. The gate is enforced in three places — the button that would open the feature, the screen behind it, and the type that carries the result — and the shipping app does not even include the vision model such a feature would need. That gate stays off unless and until the feature has the regulatory clearance it would need.

In practice this means the **assessment** screen cannot be opened in the shipping app. You can still save a journal photograph. Where Learn would offer a self-check of an image, you see an explanation of why that assessment is switched off instead.

If you notice a new spot, a changing spot, or anything that worries you, see a licensed clinician. Do not use this app to decide not to.

---

## Your skin photos

Two different things used to be described as if they were one. They are not.

**Journal photographs (shipping).** You can attach a photo from your library to a journal entry. OmniDerm stores that JPEG on this device under Application Support (`OmniDerm/JournalPhotos`), excluded from device backup, never uploaded, never synced to iCloud by this app, and never assessed. Clear All Local Data deletes those files. The app does not ask for camera access — intake is Apple's photo picker only.

**Photo self-check / on-device generate (not shipping).** Features that would produce an observation about a photograph sit behind an FDA clearance gate that is off. The shipping catalogue does not include a vision model. That gated screen is not reachable.

**If the gate were ever opened**, this is how the assessment path is built:

| Question | Answer |
|---|---|
| Where would a photo come from? | Only from you, through Apple's standard photo picker, one image at a time. |
| Is the photo uploaded to Prameya? | No. We have no server that could receive it. |
| Is the photo sent to any AI company or cloud model? | No. Any processing happens on your phone. |
| Is a journal photo uploaded? | No. Journal JPEGs stay on this device. |

**One honest caveat.** Your own iPhone backup and your own iCloud Photos settings are Apple's, not ours. Journal JPEGs are excluded from this app's backup; originals in Apple Photos follow your Photos settings.

---

## Everything the app stores, and where

| What | Where it lives | Leaves your device? |
|---|---|---|
| Habit logs (date, and whether you did morning SPF, reapplied, barrier care, a self-check) | On your device, in the app's local database | No |
| Your goals list, reminder setting | On your device, in app preferences | No |
| Downloaded AI model files | **Not a shipping feature.** Settings has no download control | No |
| Small security flags and keys | Your device Keychain, set to this-device-only | No |
| Journal photographs you save | On your device, as JPEG files under Application Support (`OmniDerm/JournalPhotos`). Excluded from device backup. Deleted with Clear All Local Data. Never uploaded, never assessed. | No |
| Diagnostic log messages | Apple's on-device system log | No |
| Preferences and screen state, **if** you switch iCloud sync on | Your own private iCloud, in your Apple Account | Yes — to your iCloud, not to us |

We do not build a profile of you. We could not: we receive nothing.

---

## The one outside connection: AI model downloads

**The shipping app does not download a model.** Settings has no download control, and the generate surface is behind an FDA clearance gate that is off. Nothing in a shipping session starts a Hugging Face pull.

If that gated surface were ever opened, model weights would download over HTTPS from **Hugging Face** (huggingface.co). That request would carry the name of a file, not your photos, notes, or identity. The shipping catalogue has no vision model.

The app is configured to refuse non-HTTPS connections entirely.

**This is the only non-Apple server OmniDerm would talk to.** There is no analytics endpoint, no crash-reporting SDK, no ad network, no remote "ask the cloud" fallback. If that ever changes, we will change this policy first and tell you in the app.

---

## Apple Health (HealthKit)

**OmniDerm does not read Apple Health.** The HealthKit entitlement, purpose string, and Settings toggle were removed: a previous toggle authorised a seven-day steps/sleep read whose only consumers were two log lines, and no screen rendered a correlation. If a Health integration returns, it returns with the screen that renders it, and this policy gains its row back in the same change.

## iCloud sync

**Off by default.** If you turn on sync in Settings, OmniDerm can copy a small amount of data into **your own private iCloud database**, inside your own Apple Account.

**What syncs:** seven settings, and nothing else. Appearance mode, whether reminders are on, the reminder hour, which tab the app opens on, which AI model you selected, whether you have acknowledged the app's disclosure, and whether citations are expanded by default. That list is enforced in code, not just described here, and each field only accepts a fixed set of values, so free text cannot ride along.

**What never syncs:** journal photographs. Habit logs. Anything derived from your habit logs, including streaks, consistency scores, goals, and any observation about your skin. Those are on an explicit deny list, and no part of the app's local database is mirrored to iCloud.

**Who can read it:** you. Records go to the private database in your Apple Account. Prameya has no ability to read, list, or recover them — that is how Apple's private databases work, not a promise we are asking you to take on faith.

**To stop it:** switch the toggle off. To remove what is already there, sign out of iCloud for the app or delete the app's iCloud data in **iOS Settings → your name → iCloud → Manage Account Storage**.

## Notifications

**Reminders start off.** Permission is requested only from the Settings control. When reminders are on, they are **local notifications** scheduled by your own phone. There is no push server, and no notification is triggered by us. Turn them off in the app or in iOS Settings.

---

## Things we do not do

One line each, because that is all they need.

- **No accounts.** No sign-up, no email, no password, no Sign in with Apple.
- **No advertising.** No ad SDK, no ad network, no sponsored content.
- **No analytics.** No usage tracking, no event logging, no session recording, no third-party analytics SDK of any kind.
- **No tracking across apps or websites.** The app declares no tracking and no tracking domains, and does not use the advertising identifier. Its privacy manifest declares no collected data types at all.
- **No selling or sharing your data.** Not to advertisers, not to data brokers, not to anyone, for money or for anything else.
- **No location.** OmniDerm does not request or use your location, precise or approximate. It uses no geofences.
- **No camera, contacts, microphone, or health records.**
- **No background activity.** The app declares no background modes and schedules no background tasks; it does nothing when you are not using it.
- **No profiling and no automated decisions about you** in the legal sense — the app makes no decision that produces legal or similarly significant effects.

## What Apple may see

Apple runs the App Store and iOS, and a few things flow to Apple rather than to us:

- **Crash and performance reports.** If you have turned on "Share with App Developers" in iOS Settings → Privacy & Security → Analytics & Improvements, Apple may give us aggregated crash and performance data through App Store Connect. This contains technical information about the crash. It does not contain your photos, your habit logs, or your health data. You can turn it off in iOS Settings.
- **App Store transactions.** Any download or purchase happens through Apple. We never see your name, payment details, or Apple Account.

## If you email us

If you write to admin@prameya.legal, we will have your email address and whatever you put in the message. We use it to answer you and we do not add you to any list. Our practice is to delete support threads once they are resolved — that is a commitment about how we work, not something you can verify from the app, so we state it as our intent rather than as a technical guarantee. Please **do not** send us photos of your skin — we do not want them and we have no secure place to put them.

---

## Security

- Data the app stores stays in the app's own sandbox on your device, protected by iOS.
- Sensitive flags and keys are held in the device Keychain, marked as **this device only**, so they are not carried into iCloud Keychain or restored to another device.
- All network traffic is HTTPS. The app refuses to make unencrypted connections.
- OmniDerm declares `NSFileProtectionComplete` (`com.apple.developer.default-data-protection`), so journal photographs, notes, body sites and habit logs are unreadable while your device is locked. The app declares no background modes.
- Your device passcode or Face ID is the main protection for everything on your phone, including this app's data. Please use one.

No system is perfect, and we will not pretend otherwise. What we can say plainly is that we hold nothing of yours on a server, so a breach of Prameya cannot expose your skin photos or your health data.

**If something does go wrong.** If we ever learn of a security breach involving health-related information from this app, we will notify affected users and the regulators we are required to notify — including under the FTC's Health Breach Notification Rule and applicable state breach laws — as promptly as the law requires.

## Retention and deletion

We do not retain your data, because we never receive it. On your device:

- **Delete your habit logs, journal entries, photographs, goals and settings:** open **Settings → Export & Data Management → Clear All Local Data**. If a later file removal fails after the store is emptied, the app says so rather than claiming a complete delete.
- **Delete a single journal photograph:** delete that journal entry in the app, or use Clear All Local Data. Originals in Apple Photos are yours — delete them there if you want them gone.
- **Delete everything:** delete the app. That removes the app's database, preferences, journal JPEGs, cached models if any, and Keychain items.
- **Delete synced data:** if you used iCloud sync, remove the app's iCloud data in iOS Settings as described above.
- **Take your data with you first:** **Settings → Export Full Data (JSON)** produces a file with your habit logs, journal notes (not photographs), your consistency snapshot and your goals, and presents the iOS share sheet.

---

## Health privacy law: what applies and what does not

### HIPAA does not apply

**OmniDerm is not covered by HIPAA.** HIPAA applies to health plans, health care clearinghouses, most health care providers, and their business associates. Prameya is none of those, we have no relationship with your doctor or your insurer, and we are not acting on any provider's behalf. We are telling you this because "HIPAA compliant" is a phrase consumer apps throw around loosely. We are not making that claim.

This does not leave you without protection. Other laws apply — see below — and, more to the point, the app is built so there is nothing on our side to protect.

### Washington and Nevada: consumer health data

Washington's **My Health My Data Act (RCW ch. 19.373)** and Nevada's **SB 370 (2023)** both regulate "consumer health data" much more broadly than Apple's App Store definitions do. Washington's definition of "collect" reaches data that is merely accessed, processed, **inferred or derived** — including entirely on a device. So the fact that nothing is transmitted to us does **not** end the analysis, and we do not argue that it does.

Because OmniDerm processes consumer health data, Washington law requires a **separate** consumer health data privacy policy. We have one:

> **[Consumer Health Data Privacy Policy for OmniDerm](https://prameyallc.github.io/privacy/omniderm/health-data/)**

It sets out the categories of consumer health data involved, where they come from, what they are used for, who they are shared with (no one), and how to exercise your rights, including the right to withdraw consent and the right to delete.

### California (CCPA/CPRA)

California residents have rights to know, delete, correct, and opt out of the sale or sharing of personal information, and to limit the use of **sensitive personal information** — a category that includes health information.

Our answers, honestly:

- **We do not collect personal information about you.** No account, no identifiers, no server logs of your activity.
- **We do not sell or share personal information** as those terms are defined in the CCPA, and we have not in the preceding 12 months.
- **We do not use sensitive personal information for any purpose you could need to limit**, because we do not receive it.
- **We do not discriminate** against anyone for exercising a privacy right. There is nothing to withhold — the app is the same for everyone.
- **To exercise a right:** email admin@prameya.legal. We will respond within 45 days. In most cases our honest answer will be that we hold no personal information about you, and we will tell you exactly how to delete the data on your own device (see "Retention and deletion" above).
- **Authorized agents** may submit requests on your behalf with written proof of authorization.

### Other US states

Several other states (Colorado, Connecticut, Virginia, Texas, Oregon, Montana and others) give residents similar rights of access, correction, deletion, portability, and opt-out of targeted advertising, profiling and sale. We do not target advertising, do not profile, and do not sell. The same route applies: email admin@prameya.legal.

### Europe and the UK

We have not written this section around any assumption about which countries the App Store makes OmniDerm available in. Wherever it is available to you, this applies.

If OmniDerm is available where you are in the EEA, UK or Switzerland:

- Information about your skin and your health is **special category data** under Article 9 of the GDPR and the UK GDPR. It is processed **only on your own device**, at your initiative, under your explicit choice to use the feature. Prameya does not receive it and does not process it.
- Prameya is not in a position to access, export, or erase device-resident data — you control it directly, and the deletion steps above are complete and immediate.
- For the little we might ever hold — an email you choose to send us — the legal basis is our legitimate interest in answering you, and you may ask us to delete it.
- You have rights of access, rectification, erasure, restriction, portability and objection, and the right to complain to your national data protection authority.
- The shipping app does not download model files. If the gated generate surface were ever opened, that download would be a connection from your device to Hugging Face, which may be outside your country. No personal data of yours would be included in that request.

### Children

**OmniDerm is not directed to children.** It is written for adults managing their own skin-care habits, it has no ads, no accounts, no social features, no chat with other people, and no in-app purchases. We do not knowingly collect personal information from anyone, including anyone under 13, and there is no mechanism by which a child could send us information — we have no server.

Under the Children's Online Privacy Protection Act (COPPA), an operator's obligations attach to collecting personal information online from children under 13. We collect none, from anyone.

If you are a parent or guardian and believe a child has somehow sent us information, email admin@prameya.legal and we will delete it.

---

## Limitations you should know about

This is a privacy policy, but two facts about the app affect the choices you make with your own health data, so they belong here.

**AI models perform differently across skin tones.** Published, peer-reviewed research (Daneshjou et al., *Science Advances*, 2022) found that **every** dermatology AI model evaluated performed worse on darker skin tones and on less common conditions. This is one of the reasons the photo feature is switched off. The shipping app contains no image model and says nothing about anyone's skin, of any tone. If a photo feature is ever cleared and enabled, this caveat becomes directly relevant and we will say so here first.

**Smartphone skin apps have a poor track record.** A systematic review in the *BMJ* (Freeman et al., 2020) concluded that current algorithm-based smartphone apps cannot be relied on to detect all cases of melanoma. That is a large part of why the assessment feature in OmniDerm is switched off.

**Nothing in this app is screening.** Logging a self-check is a record of what you did. It is not a screening result and it does not mean anything was checked properly. See a clinician.

---

## Changes to this policy

If we change how OmniDerm handles your data, we will update this policy and change the effective date at the top. For any change that materially affects your privacy — a new network connection, a new category of data, a change to what syncs — we will:

- post the updated policy here before the change ships, and
- tell you inside the app, and
- ask for your consent again where the law requires it, including a fresh consent for any new collection or sharing of consumer health data under Washington's My Health My Data Act.

**What changed on 21 August 2026.** Journal photographs you save are stored on this device (they always were; the previous page said the app touched none). HealthKit is not used. Reminders start off. Settings does not offer a model download. File protection is `NSFileProtectionComplete`. The photo self-check remains gated off.

**What changed on 8 August 2026.** An earlier revision corrected internal review notes, gated the photo-assessment feature, and named the model-download host. Some of those sentences were already stale by 21 August and are superseded above.

We will keep previous versions available at [https://prameyallc.github.io/privacy/](https://prameyallc.github.io/privacy/) so you can see what changed.

## Contact

Questions, requests, complaints, or corrections:

**Prameya LLC** — **admin@prameya.legal**

If you are exercising a privacy right, please say which state or country you are in, so we can apply the right rules. We will not ask you to create an account to make a request.
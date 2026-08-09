# OmniDerm Privacy Policy

**Effective date:** 8 August 2026
**Publisher:** Prameya LLC ("Prameya", "we", "us"), a United States limited liability company
**Contact:** admin@prameya.legal
**This policy covers:** the OmniDerm iOS app only.

**Related pages**

- **[Consumer Health Data Privacy Policy for OmniDerm](https://prameyallc.github.io/privacy/omniderm/health-data/)** — a separate, additional policy required by Washington's My Health My Data Act. If you live in Washington or Nevada, read that one too. It is a distinct document, not a section of this one.
- [Privacy policies for all Prameya apps](https://prameyallc.github.io/privacy/)
- This policy lives at [https://prameyallc.github.io/privacy/omniderm/](https://prameyallc.github.io/privacy/omniderm/)

---

## The short version

- **The photo self-check is switched off in the version you can install.** It sits behind a regulatory clearance gate that is closed, so the shipping app produces no observations, flags, ratings or any other output about a photo of your skin — and the photo screen cannot be opened at all.
- **There is no account and no password.** We do not know who you are.
- **Prameya runs no server that receives your data.** We have no database of users. There is nothing on our side to hack, subpoena, or sell.
- **The app does connect to one outside service:** Hugging Face, to download the AI model files that run on your phone. That download carries a request for a file. It does not carry your photos, your notes, or anything else about you.
- **The AI runs on your phone**, not in the cloud.
- **No ads. No analytics. No tracking. We do not sell your data**, and we never will.
- **Apple Health is off unless you turn it on.** iCloud sync is off unless you turn it on. **Reminders start on** — they are local notifications from your own phone, and you can switch them off.
- **OmniDerm does not diagnose anything.** It is not a substitute for a dermatologist. See "What OmniDerm will not do" below.
- **Skin-analysis AI is known to work less well on darker skin.** We explain that honestly below because you deserve to know it.

---

## Who we are

OmniDerm is published by Prameya LLC, a US limited liability company. You can reach a human at **admin@prameya.legal**. We do not have a phone line.

## What OmniDerm is

OmniDerm is a consumer app for skin-care habits and education. It helps you:

- log daily habits (sunscreen in the morning, reapplying, barrier care, doing a self-check) and see your streak and consistency;
- learn about sun protection and the ABCDE self-check ideas;
- optionally see how activity and sleep from Apple Health line up with your habits.

## What OmniDerm will not do

OmniDerm is **not a medical device** and does **not** diagnose, screen for, or detect skin cancer or any other condition. It does not tell you whether a mole is dangerous. It does not tell you whether to see a doctor.

Features that would produce an assessment of a photograph of your skin are behind a **clearance gate that is switched off**. In the version of OmniDerm on the App Store, the app does not produce observations, flags, ratings, or any other output about a photo of your skin. The gate is enforced in three places — the button that would open the feature, the screen behind it, and the type that carries the result — and the shipping app does not even include the vision model such a feature would need. That gate stays off unless and until the feature has the regulatory clearance it would need.

In practice this means the photo screen cannot be opened in the shipping app. Where the Learn section would offer it, you see an explanation of why it is switched off instead.

If you notice a new spot, a changing spot, or anything that worries you, see a licensed clinician. Do not use this app to decide not to.

---

## Your skin photos

This is the most sensitive thing OmniDerm could touch, so it gets its own section.

**In the shipping app, it touches none.** Because the clearance gate is closed, there is no screen from which you can hand OmniDerm a photo. The app does not open your photo library, does not read an image, and does not analyse one.

**If the gate were ever opened**, this is how the feature is built, and this is what we would be bound by:

| Question | Answer |
|---|---|
| Where would a photo come from? | Only from you, through Apple's standard photo picker, one image at a time. The picker hands the app only the image you chose; the app cannot browse, index or read the rest of your library. |
| Is the photo uploaded to Prameya? | No. We have no server that could receive it. |
| Is the photo sent to any AI company or cloud model? | No. Any processing happens on your phone. |
| Is the photo saved into the app's own storage? | No. No code path writes an image to a file, a database, the Keychain, or iCloud. |
| Is the photo synced to iCloud by OmniDerm? | No. Photos are on the explicit list of things that are never synced. |
| Is the photo backed up as part of the app's data? | No, because the app does not store it. |
| How long would the app keep it? | Only while the screen is open. It is held in the phone's working memory and released when you leave the screen or close the app. |

**The app does not ask for camera access.** There is no camera permission request in OmniDerm and no photo-capture code in it.

**How to remove a photo from OmniDerm.** There is nothing to remove — the app never made a copy. If you want an original gone, delete it in Apple's Photos app; that is your photo library, which OmniDerm does not control.

**One honest caveat.** Your own iPhone backup and your own iCloud Photos settings are Apple's, not ours. If your photo library syncs to iCloud, your skin photos are in your iCloud like every other photo you take. That is a setting in iOS, and you control it.

---

## Everything the app stores, and where

| What | Where it lives | Leaves your device? |
|---|---|---|
| Habit logs (date, and whether you did morning SPF, reapplied, barrier care, a self-check) | On your device, in the app's local database | No |
| Your goals list, reminder setting | On your device, in app preferences | No |
| Which AI model you chose, and which models are downloaded | On your device, in app preferences | No |
| Downloaded AI model files | On your device, in app storage | No (they came *to* the device) |
| Small security flags and keys | Your device Keychain, set to this-device-only | No |
| Skin photos | Nothing is stored: the photo screen is gated off, so no image is read at all | No |
| Diagnostic log messages | Apple's on-device system log | No |
| Preferences and screen state, **if** you switch iCloud sync on | Your own private iCloud, in your Apple Account | Yes — to your iCloud, not to us |

We do not build a profile of you. We could not: we receive nothing.

---

## The one outside connection: AI model downloads

OmniDerm's AI runs on your phone. To do that, it first has to get the model files. When you choose to use the on-device AI, the app downloads model weights over HTTPS from **Hugging Face** (huggingface.co), a third-party model host.

**What that request contains:** the name of the model file the app wants. In the shipping app there is exactly one model in the catalogue — a text model of roughly **420 MB**. Like any internet request, it also reveals your device's IP address and standard network information to Hugging Face.

**What that request does not contain:** your photos, your habit logs, your Apple Health data, your notes, your goals, your identity, or anything else about you. It is a file download, not an upload.

**There is no vision model to download.** The larger image model that a photo feature would need is not in the shipping catalogue at all; it is compiled out until and unless the feature is cleared.

**What we do not do before that download, so you are not surprised by it.** Settings names the model and shows its approximate download size before anything happens, and the download only starts when you tap the download button. Beyond that there is no confirmation step: OmniDerm does **not** warn you about download size thresholds and does **not** check whether you are on cellular data or Wi-Fi. If you are on a metered connection, the download will use it. If that matters to you, start it on Wi-Fi.

After the files are on your phone, everything the model does happens locally. Nothing you feed the model is transmitted anywhere.

Hugging Face is an independent company with its own privacy practices. We do not send them anything about you, but the connection itself is theirs to log, as with any website you visit.

The app is configured to refuse non-HTTPS connections entirely.

**This is the only non-Apple server OmniDerm talks to.** There is no analytics endpoint, no crash-reporting SDK, no ad network, no remote "ask the cloud" fallback for hard cases. If that ever changes, we will change this policy first and tell you in the app.

---

## Apple Health (HealthKit)

**Off by default.** OmniDerm asks for Apple Health only if you turn the toggle on in Settings, and iOS then asks you separately.

If you allow it, OmniDerm **reads** three things from the last seven days:

- step count
- sleep analysis
- active energy burned

It uses them on your device to show how your activity and sleep line up with your logged habits. That is all.

- OmniDerm **never writes** anything into Apple Health. It asks for read access only, with nothing on the write list.
- OmniDerm **does not read your clinical health records** — not lab results, not medications, not visits, not anything from a health provider. The app does not hold the Clinical Health Records capability at all.
- OmniDerm does not hold the HealthKit **background delivery** capability either, so it cannot receive Health data while you are not using it.
- Apple Health data is **never** sent to Prameya, never uploaded, and never included in iCloud sync by this app.
- You can revoke access any time in **iOS Settings → Health → Data Access & Devices → OmniDerm**, or by switching the toggle off in the app.

## iCloud sync

**Off by default.** If you turn on sync in Settings, OmniDerm can copy a small amount of data into **your own private iCloud database**, inside your own Apple Account.

**What syncs:** seven settings, and nothing else. Appearance mode, whether reminders are on, the reminder hour, which tab the app opens on, which AI model you selected, whether you have acknowledged the app's disclosure, and whether citations are expanded by default. That list is enforced in code, not just described here, and each field only accepts a fixed set of values, so free text cannot ride along.

**What never syncs:** photos. Habit logs. Anything derived from your habit logs, including streaks, consistency scores, goals, and any observation about your skin. Anything from Apple Health. Those are on an explicit deny list, and no part of the app's local database is mirrored to iCloud.

**Who can read it:** you. Records go to the private database in your Apple Account. Prameya has no ability to read, list, or recover them — that is how Apple's private databases work, not a promise we are asking you to take on faith.

**To stop it:** switch the toggle off. To remove what is already there, sign out of iCloud for the app or delete the app's iCloud data in **iOS Settings → your name → iCloud → Manage Account Storage**.

## Notifications

**Reminders start on.** The reminder setting in the app is on when you first open it, and iOS still asks you separately before the app can show you anything. When reminders are on, they are **local notifications** scheduled by your own phone. There is no push server, and no notification is triggered by us. Turn them off in the app or in iOS Settings.

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
- **What we do not claim:** OmniDerm does not turn on iOS's strictest file-protection level, the one that would keep the app's own files unreadable the whole time your device is locked. Its stored files get the standard protection iOS gives app data and nothing beyond it. We would rather say that plainly than let you assume more.
- Your device passcode or Face ID is the main protection for everything on your phone, including this app's data. Please use one.

No system is perfect, and we will not pretend otherwise. What we can say plainly is that we hold nothing of yours on a server, so a breach of Prameya cannot expose your skin photos or your health data.

**If something does go wrong.** If we ever learn of a security breach involving health-related information from this app, we will notify affected users and the regulators we are required to notify — including under the FTC's Health Breach Notification Rule and applicable state breach laws — as promptly as the law requires.

## Retention and deletion

We do not retain your data, because we never receive it. On your device:

- **Delete your habit logs, goals and settings:** open **Settings → Export & Data Management → Clear All Local Data**. This deletes all habit logs, clears your goals and reminder preference, and cancels pending reminders.
- **Delete a photo:** there is nothing to delete inside OmniDerm — no image is ever stored, and in this version none is ever read. To remove an original, use Apple's Photos app.
- **Delete downloaded AI models:** remove them from the on-device AI section in Settings, or delete the app.
- **Delete everything:** delete the app. That removes the app's database, preferences, cached models and Keychain items.
- **Delete synced data:** if you used iCloud sync, remove the app's iCloud data in iOS Settings as described above.
- **Take your data with you first:** **Settings → Export Full Data (JSON)** produces a file with your habit logs, your streak snapshot and your goals, which you can save or share wherever you like.

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
- Model files are downloaded from Hugging Face, which may involve a connection to servers outside your country. No personal data of yours is included in that request.

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

**What changed on 8 August 2026.** This revision corrected the policy against the code that actually ships. Statements that the app's behaviour did not support were rewritten or removed rather than left standing: internal review notes that had been published by mistake were taken out, the photo section now says the feature is gated off rather than describing it as if it ran, the model download section names the one model that ships and states that there is no download-size or cellular-data prompt, and the security section no longer implies file protection the app does not enable. Where the code now does what the policy said, we say so plainly. Nothing here describes a capability the shipping app does not have.

We will keep previous versions available at [https://prameyallc.github.io/privacy/](https://prameyallc.github.io/privacy/) so you can see what changed.

## Contact

Questions, requests, complaints, or corrections:

**Prameya LLC** — **admin@prameya.legal**

If you are exercising a privacy right, please say which state or country you are in, so we can apply the right rules. We will not ask you to create an account to make a request.
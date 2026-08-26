# OmniSalub Privacy Policy

**Effective date:** 8 August 2026
**Last updated:** 21 August 2026
**Publisher:** Prameya LLC ("Prameya", "we", "us")
**Applies to:** OmniSalub for iPhone, iPad and Mac (bundle identifier `legal.prameya.omnisalub`)
**Contact:** admin@prameya.legal

**Washington and Nevada residents — and anyone who wants the health-specific detail:** we publish a separate [Consumer Health Data Privacy Policy](https://prameyallc.github.io/privacy/omnisalub/health-data/). **Prameya collects no consumer health data**; processing is on-device. Apple's App Privacy label is **Data Not Collected**. Please read the separate policy alongside this one.

Other Prameya app policies: [prameyallc.github.io/privacy](https://prameyallc.github.io/privacy/).

---

## The short version

OmniSalub helps you keep track of a chronic condition — blood pressure, heart failure, kidney disease — on your own device.

- **We have no server.** Prameya operates no backend that receives your data. There is no account, no login, no user database, and no profile of you anywhere at Prameya.
- **Your readings stay on your device**, and in your own Apple Health app if you allow that.
- **The app asks Apple Health only for the data types it actually uses.** It does not ask for reproductive or sexual health data, and it does not ask for your date of birth, biological sex or blood type. Section 2.1 lists exactly what it asks for and what it does not.
- **We do not sell, rent, share or trade your information.** We do not run ads and there is no advertising, analytics or crash-reporting SDK in the app.
- **The app does connect to the internet in two situations**, and only these two: if you choose to install the optional on-device assistant, the app downloads model files from Hugging Face; and if you turn on settings sync, your app *preferences* (not health data) go to your own iCloud account. Details in section 5.
- **The assistant runs on your device.** Your health data is not sent to us, to Hugging Face, or to any AI company.
- **HIPAA does not apply to this app.** We are not a doctor, hospital, insurer or their contractor. See section 14.

Where this policy says "we do not do X", it means the capability is absent from the software — or, where we say so explicitly, that it exists in the code but is hard-wired off and fails closed.

---

## 1. Who we are and what this covers

Prameya LLC is a US limited liability company. OmniSalub is a direct-to-consumer app. You buy or download it from Apple; you do not create an account with us, and we do not know who you are.

This policy covers the OmniSalub app on iPhone, iPad and Mac. It does not cover Apple's services (the App Store, Apple Health, iCloud, Siri), which are governed by Apple's privacy policy, or any app or service you choose to send an export to.

---

## 2. Subscriptions and In-App Purchases

### Available tiers

OmniSalub offers three tiers:

| Feature | Free | Plus ($9.99/mo or $99/yr) | Premium ($19.99/mo or $199/yr) |
|---------|------|---------------------------|--------------------------------|
| Tracking History | 30 days | Unlimited | Unlimited |
| HealthKit Sync | Manual only | Auto | Auto |
| Data Export | None | PDF/JSON | PDF/JSON/FHIR |
| CloudKit Sync | None | Preferences + logs | Preferences + logs |
| Analytics | Current values | 30-day trends | Advanced correlations |
| Device Integration | None | None | Yes (Omron, Withings) |

**Critical: HealthKit data collection is identical across all tiers.** The app reads the same health data types in all tiers. Subscription unlocks features, not data access.

### What Apple receives

All transactions go through Apple's App Store. When you subscribe:
- **Apple receives:** Your Apple Account ID, payment method, transaction details
- **Prameya receives:** A transaction ID from StoreKit, subscription status (active/expired), tier purchased
- **Prameya does NOT receive:** Your name, email, payment card details, or Apple Account credentials

### Data Linked to You

Apple's privacy labels mark Purchase History as "Data Linked to User" for subscribers.

**This does NOT mean your health data leaves your device.** Health readings, symptoms, and vital signs remain on-device only (and in Apple Health if you enable it). StoreKit tells us you're a paying subscriber so we can unlock features — it does not transmit your health readings or any health information.

### Free vs paid tier data collection

**Both tiers process the same consumer health data** (listed in the [Consumer Health Data Privacy Policy](https://prameyallc.github.io/privacy/omnisalub/health-data/)).

- **Free tier:** Health data processed on-device, 30-day history limit, HealthKit manual sync
- **Plus/Premium tier:** Health data processed on-device (same processing), unlimited history, HealthKit auto sync, device integrations

In both tiers:
- Health readings stay on your device
- No health data transmitted to Prameya
- Same HealthKit permissions and data types
- Same on-device processing

**Subscription unlocks features. It does not change what data is collected or where it goes.**

### Cancellation and refunds

Subscriptions are managed by Apple:
- **Cancel:** iOS Settings → your name → Subscriptions → OmniSalub
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

## 3. Apple Health (HealthKit)

This is the most important section, so it is the longest.

### 3.1 What the app asks to read

If you tap "Connect Apple Health", iOS shows you Apple's own permission sheet. **OmniSalub asks only for the health data types the conditions you have switched on actually use.**

This has been narrowed twice, and the second narrowing is the one you will notice.

**2026-08-08, first narrowing.** An earlier version of this policy said the app "asks for the full set of health data types that Apple lets an ordinary app read". That described an earlier build and it is no longer true: the set of types the app is *capable* of requesting was cut to the ones it actually consumes.

**2026-08-08, second narrowing.** The first change fixed what the app could ask for; it did not fix what it *did* ask for. Every user was still shown the whole capability regardless of which condition they had chosen. Now the request is built from your active conditions.

**What that means concretely.** If you chose blood pressure and nothing else, the permission sheet asks for **eight** types:

- systolic blood pressure
- diastolic blood pressure
- body weight
- exercise minutes
- chest tightness or pain
- shortness of breath
- dizziness
- fainting

Those last four are there because the app's emergency rule checks them alongside a very high reading. **It previously asked for twenty-nine types.** It does not ask for your sleep, your workouts, your Watch heart-rhythm notifications, your nutrition, or your cycling data, because nothing in a blood-pressure programme reads them. Switch on another condition and only that condition's types are added.

The table below is therefore a **ceiling, not a request**: it is everything the app could ever ask for, across all of its condition programmes combined. You will only ever see the part that belongs to what you switched on — unless you use **Settings → Import all Health history**, a deliberate one-off action that does ask for the whole table, because a partial import of "all my history" would be a false promise. You never have to use it.

| Group | What is requested |
|---|---|
| Vitals | Blood pressure, heart rate, resting and walking heart rate, heart-rate recovery, heart rate variability, AFib burden, oxygen saturation, respiratory rate, body temperature (including basal and wrist temperature), peripheral perfusion index |
| Body | Weight, BMI, body fat, lean mass, height, waist circumference |
| Glucose and related | Blood glucose, insulin delivery, blood alcohol content |
| Alcohol | **Number of alcoholic drinks** |
| Breathing tests | FEV1, forced vital capacity, peak flow, inhaler use |
| Activity and fitness | Steps, exercise minutes, move and stand time, energy burned, flights climbed, distances (walking and running, cycling, swimming, wheelchair, snow sports), push count, swimming strokes, VO₂ max, time in daylight, UV exposure, running and cycling metrics |
| Workouts | Workout records, from which the app reads duration, active energy and distance |
| Mobility | Walking speed and steadiness, step length, asymmetry, double-support percentage, stair speeds, six-minute walk distance, times fallen |
| Sleep | Sleep analysis records — time in bed, time asleep, and sleep stages |
| Heart events from a Watch | Exactly four record types: high heart rate, low heart rate, irregular rhythm notification, low cardio fitness |
| Hearing | Environmental and headphone audio-exposure levels |
| Nutrition | Energy, carbohydrates, protein, fats, cholesterol, fibre, sugar, water, caffeine, and minerals including **sodium and potassium** (both matter clinically in hypertension and kidney disease), plus calcium, iron, magnesium and zinc |
| Symptoms | The symptom records the app can represent: breathlessness, chest tightness or pain, dizziness, palpitations, **skipped heartbeat**, fainting, nausea, vomiting, fever, diarrhoea, abdominal cramps, bloating, constipation, heartburn, fatigue, headache, mood changes, appetite changes, sleep changes |

**Added on 2026-08-08:** *number of alcoholic drinks* and the *skipped heartbeat* symptom record. The alcohol-use programme previously had no Apple Health source at all, so every drink had to be entered twice; and Apple Health records a skipped heartbeat separately from palpitations, which made it the one cardiac symptom the app could not import. Both are requested only when a condition that uses them is active.

Background refreshes use the same scope as the first-run request — there is no separate, wider set read on every refresh. An earlier version of this policy described "the fixed set of records the app reads on every refresh (sleep, the four Watch heart-event types, the symptom records above, and workouts)". That fixed set is gone: sleep is requested only if something you switched on reads sleep, each Watch heart-event type only if something reads that event, workouts only if something reads workouts, and a symptom record only if one of your active conditions' rules checks it.

**What the app does not ask for.** These types were in an earlier build's request and have been removed from it:

- **All reproductive and sexual health records** — menstrual flow, intermenstrual bleeding, infrequent, irregular, persistent or prolonged cycle records, ovulation, pregnancy and progesterone test results, cervical mucus, contraceptive use, lactation, pregnancy, sexual activity. Fourteen record types in total, none of which the app can request.
- **All profile facts** — date of birth, biological sex, blood type, Fitzpatrick skin type, wheelchair use, activity move mode. The app contains no code that reads any of them.
- **Electrocardiograms and audiograms.**
- **Mindful sessions, Apple's stand-hour records, audio-exposure event notifications, toothbrushing and handwashing records.**
- **Medications, dose records and Clinical Health Records** — see section 2.3.

None of these can appear on the permission sheet, and the bans are asserted against the **widest** request the app can build — not a narrow one that would pass for the wrong reason. The tests that fail the build if any of them returns are `noReproductiveHealthTypeIsEverRequested`, `noCharacteristicTypeIsEverRequested`, `unconsumedCategoryFamiliesStayOutOfTheRequest` and `readRequestHonoursTheCallersMetrics`, joined on 2026-08-08 by `categoryTypesAreScopedToTheirConsumers`, `consumedCategoriesAreRequestedWhenSomethingConsumesThem` and `hypertensionScopeDoesNotReachIntoOtherConditions`, which assert the second narrowing above.

**You are not obliged to grant any of it.** Apple's sheet has an individual toggle for every category, and the app works with whatever subset you allow. If you only want blood pressure to come through, turn on only blood pressure.

We are listing the removed categories explicitly, rather than quietly dropping them, because the previous version of this policy told you the app asked for them. It no longer does, and you should be able to check that against the permission sheet.

### 3.2 What the app writes back to Health

The app writes back a much narrower set, and only readings **you typed into OmniSalub yourself**:

- Systolic and diastolic blood pressure, heart rate, body weight, height, blood glucose, oxygen saturation.
- The symptom types listed in the table above, and only where the symptom means exactly the same thing in Apple Health.

Readings that came *from* Health are never written back, so the app cannot create duplicates of your own data. Symptoms carrying an extra clinical qualifier — "breathlessness on waking", for example — stay only on your device, because writing them as a plain symptom would misrepresent what you recorded.

Writing to Health is how your readings reach your other Apple devices. Data inside Health is managed by Apple under Apple's terms and encryption. **We never see it.**

### 3.3 What the app does *not* read

- **Medications and dose records.** The shipping app does **not** read your medication list or your record of doses taken or skipped. Those are gated Apple capabilities; the capability flag in this build is hard-coded off and the code path returns without asking for anything. If that ever changes, this policy will be updated before that version ships.
- **Clinical Health Records** — lab results and other records imported from a participating hospital or clinic. The app does not request the entitlement and does not query them; that capability flag is hard-coded off as well.
- **Everything listed under "what the app does not ask for" in section 3.1.** It is not requested, so it cannot be read.

### 3.4 Withdrawing permission

Go to **Settings → Privacy & Security → Health → OmniSalub**, or use the Health app. Revoking permission stops future reads and writes. It does not delete anything already in Health — you control that in the Health app.

### 3.5 Apple's extra rules for health apps

Apple's App Store Review Guideline 5.1.3 imposes obligations beyond ordinary privacy law. We follow them:

- **5.1.3(i)** — health and fitness data must not be used or disclosed for advertising, marketing or other use-based data mining. We do none of those things at all, with any data.
- **5.1.3(ii)** — apps must not write false or inaccurate data into HealthKit, and **may not store personal health information in iCloud**. The app's health database is created with iCloud syncing explicitly disabled, and an automated test blocks any health record type from being added to the part of the app that does sync.
- We disclose the specific health data the app collects from the device — that is section 3.1 above.
- Guideline 5.1.1(i) also requires an app to request only the data it needs. Narrowing the read request, as described in section 3.1, is how we meet that.

---

## 4. What is stored on your device

| What | Where it lives | Leaves the device? |
|---|---|---|
| Readings you record or import | Encrypted local database, app's private storage | Only to Apple Health, if you allow it |
| Symptoms you report | Same database | Same |
| Alerts the app raised | Same database — which guideline rule fired, when, at which rule-set version | No |
| Activity log (section 11) | Same database | No |
| Your settings — theme, guideline set, app lock, whether onboarding is done | Separate preferences database | Only to your own iCloud, and only if you turn sync on (section 4) |
| Which conditions you track, and whether you asked to hide food and weight scoring | On-device preferences only | **Never** — both are treated as health information |
| The latest reading, pre-formatted for the widget | A small file in the app's shared container, so the Home Screen widget can show it | No |
| Optional assistant model files | App Support folder, ~400 MB | No |

The health database is stored in Application Support (not a user-visible folder). On iPhone and iPad it is set to iOS Data Protection "complete", which means the operating system encrypts it with a key tied to your device passcode and it cannot be read while the device is locked. The database and its two working files are marked as excluded from iCloud backup.

The widget's snapshot file — which holds your most recent reading in display form, for example "132/84" — is also **excluded from device backup**, and the exclusion is re-applied every time the app writes the file, so snapshots left behind by older versions of the app are covered too. On iPhone and iPad that file is encrypted at rest **until the first time you unlock the device after a restart**, rather than being locked again whenever the screen locks. That is a deliberate difference from the health database: the Home Screen widget has to be able to redraw your latest reading while the phone is locked, and it could not do that under the stronger setting. Treat the widget snapshot as the one value on your device with slightly weaker protection than the rest, and turn the widget off if you would rather it did not exist at all.

---

## 5. iCloud

**Your health data is never stored in iCloud by this app.** That is an architectural boundary, not a setting, and it is also required by Apple's Guideline 5.1.3(ii).

If — and only if — you turn on **Sync settings with iCloud** in Settings, exactly five things are stored in **your own** iCloud account so they match across your devices:

- your chosen theme
- which published guideline set you follow
- whether onboarding has been completed on a device
- whether app lock is enabled
- the time that record was last updated

This uses Apple's CloudKit **private** database, which is your iCloud account and not ours. We cannot read it. The setting is **off by default**, and the app does not even create the syncing database until you say yes.

Deliberately never synced: readings, symptoms, alerts, the activity log, which conditions you track, and your answer to the food-and-weight screening question. The list of fields allowed to sync is enforced by an automated test, not by a promise.

---

## 6. When the app connects to the internet

Earlier versions of this policy said the app "makes no network requests of its own". **That statement was wrong, and it is corrected here.** Here is the complete and accurate list.

### 6.1 Hugging Face — the optional assistant model

The app can offer written explanations using a small language model that runs on your device. That model is not bundled with the app. If you choose to install it in Settings, the app downloads the model files from **huggingface.co**, a public model host run by Hugging Face, Inc.

- **It never happens automatically.** Nothing downloads unless you tap the button.
- **What is sent:** a request for a named public model repository (`mlx-community/Qwen3-0.6B-4bit`) and, unavoidably, your device's IP address, as with any web request. Hugging Face's own privacy policy governs what they do with that request.
- **What is not sent:** your health data, your readings, your symptoms, your questions to the assistant, any account identifier, or any identifier of you. None of that is in the request, because the request is for model files.
- **Size:** roughly 400 MB. You can delete the files in Settings at any time.
- If you never install the model, the app never contacts Hugging Face.

For completeness, because it is verifiable from the public source: the app is built on the MLX machine-learning packages `mlx-swift-lm`, `swift-huggingface` and `swift-transformers`. These are how the model is downloaded and run. They are not analytics, advertising or tracking libraries, and none of them transmits your content.

### 6.2 iCloud settings sync

Off by default. Described in section 5. This goes to Apple, into your own account — not to us.

### 6.3 Apple's own services, which the app uses but does not control

- **Apple Health** moves your data between your own devices, under Apple's encryption.
- **Siri and Shortcuts.** The app offers spoken shortcuts such as logging a blood pressure reading. When you speak to Siri, Apple handles the speech, under Apple's privacy policy. The app receives the resulting values and stores them locally.
- **iCloud Backup**, if you use it, backs up your device under Apple's terms. The health database is excluded from it, as is the widget snapshot.
- **"Share With App Developers"**, if you have it on in iOS Settings, may give Apple's aggregated crash reports to us. That is Apple's mechanism and it contains no health data.

### 6.4 What does not exist

There is **no Prameya server**. No API, no backend, no endpoint that receives your data. We could not read your readings if we wanted to. There is no analytics SDK, no advertising SDK, no crash-reporting SDK, no attribution SDK, and no third-party code in the app that transmits user content.

The Mac version of the app carries macOS's outgoing-network entitlement, and it is there for the two connections named above and no others we have built: iCloud settings sync, and the optional Hugging Face model download. Neither carries health data or anything you have written.

The app also contains **no** code for location, camera, photo library, contacts, microphone recording, the advertising identifier, App Tracking Transparency, or in-app purchases.

An unfinished multi-device sync engine exists in the public source tree. **It is not built into any shipping app** — no app target links it. If it is ever completed, this policy will be updated before that build ships.

---

## 7. The on-device assistant

- The assistant runs **on your device**, using the model you chose to install. Generation happens locally on your phone or Mac.
- To answer usefully, the app assembles a summary of what you have logged — recent readings, symptoms, the conditions you track, the guideline set in use, and any open alert — and gives it to the local model as context. **That context never leaves your device.** It is not sent to us, to Apple, to Hugging Face, or to any AI provider.
- A refusal layer runs before and after the model, so it cannot give diagnoses, dosing instructions or emergency advice.
- The app's design allows for two further modes — Apple's Private Cloud Compute, and an outside AI provider. **Neither is enabled or reachable in this version**; both are hard-wired off. If either ever ships, it will be off by default, will require separate explicit consent, will name the provider, and this policy will be updated first.
- Every other feature — logging, trends, alerts, export — works without the assistant.

---

## 8. Widgets, the Lock Screen and Siri

- The **Home Screen widget** shows your latest reading. To do that, the app saves a small display snapshot — a formatted headline such as "132/84", a timestamp, and what to log next — into a container shared between the app and the widget. It stays on the device, is excluded from backup, and never goes to iCloud. See section 4 for how it is protected.
- The **Live Activity** shown during a measurement session carries the session's state: which measurement, how many readings so far, positioning guidance and a countdown. It does not carry your values, and it is drawn on your device. The app sends no push notifications, and holds no push capability.
- **Siri shortcuts** let you log a reading or start a measurement by voice. See section 6.3 for what that means.

---

## 9. Exports and sharing

The app can produce a summary of your readings as a **PDF**, a **CSV** file, or a **FHIR** bundle to give to a clinician.

- An export is created only when you ask for one.
- It is handed to the standard iOS or macOS share sheet. **You** choose what happens next — print it, email it, save it to Files, hand it over in person.
- The app does not upload it anywhere and we never receive a copy.
- Once you send an export to another person, app or service, this policy no longer governs it. The recipient's terms apply. An export contains real health data, so treat it the way you would treat a paper record.

---

## 10. Notifications

The app can send reminders and prompts. These are **local notifications** scheduled on your device by the app itself. There is no notification server, and no notification content is transmitted anywhere. Alerts about a concerning reading are shown in the app, not pushed to your Lock Screen as text.

---

## 11. Diagnostics and analytics

**This version records no usage analytics.** There is no counter, no event log of what you tapped, and nothing to send even if there were a place to send it.

On iPhone and iPad the app subscribes to Apple's **MetricKit**, which delivers performance and crash diagnostics for the app to the app itself. OmniSalub counts these reports and discards them. Nothing from MetricKit is stored, inspected or transmitted. The Mac app does not use MetricKit.

The app does contain the scaffolding for future on-device usage counting, built so that any event name must come from a fixed, closed list — a reading could not end up in one even by mistake — kept only on your device and deleted after 180 days. **Nothing switches it on today.** If a future version does, this section will be updated before that version ships.

The app's privacy manifest, which Apple ships inside the app and which anyone can inspect, declares that the app does **no tracking** and collects **no data types**. It declares two of Apple's "required reason" API uses: storing your settings in UserDefaults, and checking available disk space before a download or an import.

---

## 12. The activity log

The app keeps a local log of security-relevant events: when health data was read, written, exported or erased; when permissions were requested, granted or denied; when settings sync was turned on or off; when the app was unlocked.

This log:

- **contains no health values.** Each entry is one of a fixed list of event types plus a short identifier such as a measurement name or an export format — never a number you recorded, and never text you wrote.
- is stored only on your device.
- is tamper-evident: each entry is cryptographically chained to the one before it, so if entries are altered or removed, the app can tell you.
- is visible to you at any time under **Settings → Activity log**.

It exists so that "what happened to my data?" has an answer, which is impossible after the fact if nothing recorded it.

---

## 13. Security

- **iPhone and iPad.** The health database uses iOS Data Protection set to "complete": encrypted by the operating system with a key derived from your passcode, and unreadable while the device is locked. **Set a passcode.** Without one, iOS cannot protect the file.
- **Mac.** macOS does not offer the same per-file protection. On a Mac the database is protected by the app sandbox and by **FileVault, if you have FileVault turned on.** We recommend turning it on in System Settings → Privacy & Security.
- **App lock.** You can require Face ID, Touch ID or your device passcode to open the app. Your fingerprint or face data is handled entirely by Apple's Secure Enclave; the app never receives it and never stores it.
- **Keys.** Any encryption key the app uses is held in the device Keychain, marked so it is available only when the device is unlocked and never leaves that device.
- **Backups.** The health database and the widget snapshot are both excluded from iCloud backup. The widget snapshot's at-rest protection is weaker than the database's, for the reason given in section 4.

No security measure is absolute. Because your data lives on your device, its safety depends heavily on that device having a passcode and up-to-date software.

---

## 14. Keeping and deleting data

**We hold nothing, so there is nothing at Prameya to delete.** On your device:

- Readings, symptoms and alerts are kept until you delete them.
- **Settings → Delete all data on this device** erases them immediately. It also clears the widget snapshot.
- **Deleting the app** removes all of its local data, including the health database, the activity log, the widget snapshot and any downloaded model files.
- You can remove the assistant model files on their own in Settings.
- If you turned on settings sync, turning it off stops future syncing. You can remove what is already stored through **Settings → [your name] → iCloud → Manage Account Storage** on your device.

> Erasing data in OmniSalub does **not** delete anything the app previously wrote to Apple Health. That data is yours and lives in the Health app, where it may also be arriving from a cuff, a watch or a clinic. Delete it there if you want it gone.

---

## 15. Your privacy rights

Because we neither collect nor receive your personal data, we hold no record about you to disclose, correct, port or delete. There is nothing for us to sell or share. But you retain complete, direct control:

| Right | How you exercise it |
|---|---|
| Know / access | Everything is visible in the app, and exportable as PDF, CSV or FHIR |
| Portability | Use the FHIR or CSV export |
| Correction | Edit or delete any entry in the app |
| Deletion | Settings → Delete all data, or delete the app |
| Limit processing | Revoke Health permission; turn off settings sync; do not install the assistant |
| Withdraw consent | Any permission can be revoked at any time in iOS or macOS Settings |

If you believe we hold data about you and want to make a request anyway, write to **admin@prameya.legal**. We will respond within 45 days. In almost every case the honest answer will be that we hold nothing.

### California (CCPA/CPRA)

We do **not sell** or **share** (for cross-context behavioural advertising) personal information, as those terms are defined in the CCPA, and we have not done so in the preceding twelve months. We do not use or disclose sensitive personal information — which includes health information — for purposes beyond those permitted by the CCPA, because we do not receive it in the first place. There is no financial incentive programme and we do not discriminate against anyone for exercising a privacy right.

Note that health data is treated as **sensitive personal information** under the CPRA. The app processes it on your device, under your control, and none of it reaches us.

### Washington and Nevada consumer health data

Washington's My Health My Data Act (RCW ch. 19.373) and Nevada's consumer health data law (SB 370, NRS ch. 603A) both require a **separate, distinctly-labelled consumer health data privacy policy**. Ours is here:

**→ [OmniSalub Consumer Health Data Privacy Policy](https://prameyallc.github.io/privacy/omnisalub/health-data/)**

**Prameya collects no consumer health data.** Readings stay on your device (and in your own Apple Health account if you allow that). We receive nothing. Apple's App Privacy nutrition label for this app is **Data Not Collected**. The separate policy states that same position, plus how to exercise your rights, including deletion and appeal. Please read it. Washington's law also makes a violation an unfair practice under the Washington Consumer Protection Act (RCW ch. 19.86), which gives individuals their own right to sue under RCW 19.86.090.

### Other US states

Several other states (Colorado, Connecticut, Virginia, Texas, Oregon and others) give residents rights of access, correction, deletion, portability and opt-out, with extra protection for health data. The same answer applies everywhere: we hold no personal data about you, we run no targeted advertising, we do no profiling, and we do not sell data. Requests can be sent to admin@prameya.legal.

### If you are in the EU, EEA or UK (GDPR / UK GDPR)

For the processing that happens entirely on your device, Prameya LLC is the controller. Our lawful basis is your consent (Article 6(1)(a)) and, because health data is a special category, your **explicit** consent (Article 9(2)(a)) — given through the in-app acknowledgements and through iOS's own Health permission sheet. You may withdraw consent at any time as described in section 13, without affecting anything that already happened. You have rights of access, rectification, erasure, restriction, portability and objection; in practice you exercise all of them directly in the app, because we hold no copy. You may complain to your supervisory authority.

Where the app is available is set on the App Store, not here, and can change. This subsection applies to you if you obtained the app in the EEA or the UK.

### HIPAA — plainly

**HIPAA does not apply to OmniSalub.** HIPAA covers healthcare providers, health plans and clearinghouses, and the contractors that handle data for them. Prameya is none of those, and we are not a business associate of any of them. You are using a consumer app you chose yourself, not a service arranged by your doctor or insurer.

We say this because it matters: it means the protection your data has here comes from this app's design and from consumer-protection law, not from HIPAA. It also means we do not claim HIPAA compliance and you should be sceptical of any consumer app that does. If OmniSalub is ever distributed through a clinic, employer or insurer, that analysis changes and this policy will change with it.

---

## 15. Children

OmniSalub is intended for adults managing a chronic condition. It is not directed to children under 13, is age-rated for older teenagers and adults because it contains medical information, and we do not knowingly process children's data. Because the app collects nothing and transmits nothing to us, we hold no children's data and there is nothing for us to delete on request. **We serve no advertising of any kind**, so there is no advertising or behavioural profiling of anyone, children included.

A parent or guardian concerned about a child's use of the app can remove everything by using Settings → Delete all data, or by deleting the app. Questions: admin@prameya.legal.

---

## 16. What OmniSalub is not

Stated here because it affects how you should treat what the app shows you.

**OmniSalub is a general wellness tool. It does not diagnose, treat, cure or prevent any disease, and it is not a medical device.** It does not give medical advice and does not give medication instructions. When it flags something, it tells you what it observed and suggests you speak to a doctor.

**It is not a substitute for professional medical care and must never be relied on in an emergency.** If you think you are having a medical emergency, call your local emergency number.

---

## 17. Changes to this policy

If this policy changes, we will change the effective date at the top and publish the new version at [prameyallc.github.io/privacy/omnisalub](https://prameyallc.github.io/privacy/omnisalub/).

Where a change materially affects how your data is handled — in particular if any future version were to transmit health data off your device, add an account, add a server, or enable cloud or third-party AI processing — we will show you the change in the app and ask for your consent **before** it takes effect. We will not quietly widen what we do and rely on you re-reading this page.

This revision corrected statements in the previous version so that they match the code that actually ships. The main correction narrows the description of what the app asks to read from Apple Health: the earlier text described a much broader permission request than the app now makes, including reproductive-health and profile categories that have been removed from it (section 2.1). Section 3 also replaces a placeholder note about the widget snapshot with a statement of what the shipping app does.

Material changes are also described in the Consumer Health Data Privacy Policy, which has its own change process.

---

## 18. Contact

Questions, requests or complaints about privacy in OmniSalub:

**admin@prameya.legal**
Prameya LLC
Postal address available on request by email.

---

*This policy describes OmniSalub version 1.0 and later. It replaces the previous OmniSalub privacy policy dated 7 August 2026, which incorrectly stated that the app makes no network requests and that it reads your medication records — neither was true of the shipping app — and it corrects the earlier description of the Apple Health permission request, which described a broader request than the app now makes.*

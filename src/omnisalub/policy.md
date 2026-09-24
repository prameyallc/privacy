# OmniSalub Privacy Policy

**Effective date:** 23 September 2026
**Last updated:** 23 September 2026
**Publisher:** Prameya LLC ("Prameya", "we", "us")
**Applies to:** OmniSalub for iPhone, iPad, Mac, Apple Vision Pro and Apple TV (bundle identifier `legal.prameya.omnisalub`), and the OmniSalub Apple Watch app that comes with the iPhone app (`legal.prameya.omnisalub.watchkit`)
**Contact:** admin@prameya.legal

**Washington and Nevada residents — and anyone who wants the health-specific detail:** we publish a separate [Consumer Health Data Privacy Policy](https://prameyallc.github.io/privacy/omnisalub/health-data/). **Prameya collects no consumer health data**; processing is on-device. Apple's App Privacy label is **Data Not Collected**. Please read the separate policy alongside this one.

Other Prameya app policies: [prameyallc.github.io/privacy](https://prameyallc.github.io/privacy/).

---

## The short version

OmniSalub helps you keep track of a chronic condition — blood pressure, heart failure, kidney disease — on your own device.

- **We have no server.** Prameya operates no backend that receives your data. There is no account, no login, no user database, and no profile of you anywhere at Prameya.
- **Your readings stay on your device**, and in your own Apple Health app if you allow that. They are never stored in iCloud by this app.
- **Apple Health: you choose what to allow.** When you tap **Connect Apple Health**, Apple's permission sheet lists only the health data types the conditions you switched on use, and for each type you allow, the app imports the last 400 days of it (your symptom records in full). It never asks for reproductive or sexual health data, your date of birth, biological sex or blood type. Section 3.1 lists everything it can ask for and what it never asks for.
- **We do not sell, rent, share or trade your information.** We do not run ads and there is no advertising, analytics or crash-reporting SDK in the app.
- **Ask answers on your device.** Ask gives the question you type, together with a summary of what you have logged (recent readings, symptoms and the conditions you track), to a language model that runs on your device: Apple Intelligence where it is turned on and ready, or an optional model you download. Your question and your readings are not sent to us, to Apple, to Hugging Face, or to any AI company. Section 7.
- **The app's own connections off the device are few, and none carries health data:** downloading the optional Ask model from Hugging Face, if you choose to; syncing a few *preferences* (not health data) to your own iCloud account, if you turn that on; and the App Store, if you buy or restore OmniSalub Pro. Apple's own services — Apple Health, Handoff, the connection to your Apple Watch — also move some data between your own devices. Details in section 6.
- **Notifications only if you ask.** Visit reminders are off until you turn them on. Section 10.
- **HIPAA does not apply to this app.** We are not a doctor, hospital, insurer or their contractor. See section 15.

Where this policy says "we do not do X", it means the capability is absent from the software — or, where we say so explicitly, that it exists in the code but is hard-wired off and fails closed.

---

## 1. Who we are and what this covers

Prameya LLC is a US limited liability company. OmniSalub is a direct-to-consumer app. You buy or download it from Apple; you do not create an account with us, and we do not know who you are.

This policy covers the OmniSalub app on iPhone, iPad, Mac, Apple Vision Pro and Apple TV, its Home Screen widget, and the OmniSalub Apple Watch app. What each device can do differs, and the differences are stated where they matter: Apple Health exists only on iPhone and iPad, so the Mac and Vision Pro show only what was entered on that device; the Apple Watch app and the Apple TV app keep no readings at all (section 8).

This policy does not cover Apple's services (the App Store, Apple Health, iCloud, Handoff, Siri, Apple Intelligence), which are governed by Apple's privacy policy, or any app or service you choose to send an export to.

---

## 2. Subscriptions and In-App Purchases

### Available tiers

There is one paid upgrade, **OmniSalub Pro**, sold as three products. Buying any one of
them grants exactly the same Pro — there are no separate feature tiers.

| Product | Price (US) | Billing |
|---|---|---|
| OmniSalub Pro Monthly | $4.99 | Auto-renews monthly. 7-day free trial. |
| OmniSalub Pro Annual | $29.99 | Auto-renews yearly. 7-day free trial. |
| OmniSalub Pro Lifetime | $79.99 | One-time purchase. Not a subscription. |

Family Sharing is enabled on all three. Subscriptions renew until you cancel in
Settings; Lifetime is a one-time non-consumable. Apple decides whether your Apple Account is eligible for the free trial, and the app offers it only when Apple says it is.

**The knowledge layer is free and stays free.** Without paying anything you get
90 days of history in the app, the full reference and your own readings, with no account and no time limit. Pro adds the visit pack (a PDF summary for a clinician), lifts the 90-day limit on history in the app (it then shows up to the last 400 days), and formatted export (a formatted CSV and a FHIR bundle). Older readings are never deleted because you are on the free tier: they stay on your device and are included in the free raw export.

**Pro does not add cloud sync, and there is no paid iCloud option.** OmniSalub stores your
records on your device in every case, paid or not. If a subscription lapses you keep your
own data and can still export it in its raw form; only the Pro tools stop.


### Free vs paid tier data collection

**Both tiers process the same consumer health data** (listed in the [Consumer Health Data Privacy Policy](https://prameyallc.github.io/privacy/omnisalub/health-data/)).

- **Free:** Health data processed on-device, 90 days of history in the app, the full reference, your own readings, and a raw CSV of your readings and a CSV of your symptoms
- **With Pro:** Health data processed on-device (identical processing), up to 400 days of history in the app, the visit pack PDF, a formatted CSV and a FHIR bundle

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

### StoreKit and your purchase record

When you buy or restore Pro, Apple's StoreKit on your device completes the purchase with the App Store. Apple processes the payment and keeps its own record of the transaction under Apple's terms. Each time the app starts, StoreKit tells it which OmniSalub Pro products your Apple Account is entitled to, and the app uses that answer only to turn the Pro tools on or off.

- The app sends nothing about a purchase to us, and we never see payment details.
- The app keeps no purchase record of its own. It asks StoreKit again rather than storing the answer.
- Because the purchase record is Apple's, **Delete everything this app stored** (section 14) does not remove it. Your purchase stays attached to your Apple Account.

An earlier version of this policy said the app stores the transaction ID, product ID and dates itself and deletes them with "Delete All Data". That did not describe the app: the app stores none of them.

---

## 3. Apple Health (HealthKit)

This is the most important section, so it is the longest. Apple Health is available on iPhone and iPad only. On a Mac or Apple Vision Pro the app does not connect to Apple Health at all, and the Apple Watch and Apple TV apps do not use it.

### 3.1 What the app asks to read

Nothing is read from Apple Health until you tap **Connect Apple Health** (on Today, on Record or in Settings; once you have readings the button is called **Refresh from Apple Health**). Finishing setup does not open Apple's permission sheet, and the app does not read Apple Health in the background.

**What the permission sheet asks for.** When you tap Connect Apple Health, Apple's sheet lists only the types that the conditions you have switched on use — the blood pressure programme, for example, asks for blood pressure, weight, exercise minutes and any symptom records its alert rules check, not the whole table below. General health has a small core set and a longer list of extra types (activity detail, nutrition, mobility and the rest); those extras are asked for only if you turn on **Import everything from Health** in Settings, and the next Connect tap then asks for them. For each type you allow, the app then **imports your history** from Apple Health into its database on your device — the last 400 days of readings, sleep, workouts and Watch notifications, and all of your symptom records — and afterwards refreshes those types. If you add a condition, the next tap asks for the new types. Apple's sheet appears only for types you have not already answered.

*Corrected on 23 September 2026:* for a time the app asked for every type in the table below whichever conditions you chose, and an earlier revision of this policy published on this date said so. The app update this revision describes asks only for what your conditions use, as described above.

The table below is the complete set of types that any of the app's condition programmes can use — the most the sheet could ever list:

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
| Sleep | Sleep analysis records — time in bed, time asleep, and sleep stages — and breathing disturbances during sleep |
| Notifications from a Watch | Exactly six record types: high heart rate, low heart rate, irregular rhythm notification, low cardio fitness, and Apple's hypertension notification and sleep apnea notification |
| Hearing | Environmental and headphone audio-exposure levels |
| Nutrition | Energy, carbohydrates, protein, fats, cholesterol, fibre, sugar, water, caffeine, and minerals including **sodium and potassium** (both matter clinically in hypertension and kidney disease), plus calcium, iron, magnesium and zinc |
| Symptoms | The symptom records the app can represent: breathlessness, chest tightness or pain, dizziness, palpitations, **skipped heartbeat**, fainting, nausea, vomiting, fever, diarrhoea, abdominal cramps, bloating, constipation, heartburn, fatigue, headache, mood changes, appetite changes, sleep changes |

**Added on 2026-08-08:** *number of alcoholic drinks* and the *skipped heartbeat* symptom record. The alcohol-use programme previously had no Apple Health source at all, so every drink had to be entered twice; and Apple Health records a skipped heartbeat separately from palpitations, which made it the one cardiac symptom the app could not import.

**What the app keeps with an imported reading.** Besides the value and time, the app keeps what Apple Health says about where the reading came from: the name and version of the app that saved it, and — where Apple Health has it — the name, manufacturer, model, software versions and identifiers of the device that measured it (for example a blood pressure cuff). This stays in the app's database on your device and can appear in a FHIR export (section 9).

**What the app does not ask for.** These types were in an earlier build's request and have been removed from it:

- **All reproductive and sexual health records** — menstrual flow, intermenstrual bleeding, infrequent, irregular, persistent or prolonged cycle records, ovulation, pregnancy and progesterone test results, cervical mucus, contraceptive use, lactation, pregnancy, sexual activity. Fourteen record types in total, none of which the app can request.
- **All profile facts** — date of birth, biological sex, blood type, Fitzpatrick skin type, wheelchair use, activity move mode. The app contains no code that reads any of them.
- **Electrocardiograms and audiograms.**
- **Mindful sessions, Apple's stand-hour records, audio-exposure event notifications, toothbrushing and handwashing records.**
- **Medications, dose records and Clinical Health Records** — see section 3.3.

None of these is in the app's request table, so none can appear on the permission sheet. For reproductive and sexual health records, profile facts, and the mindful, stand-hour, audio-exposure-event, toothbrushing and handwashing records, automated tests check the **widest** request the app could build — every type in the table above at once — and fail if any of them returns: `noReproductiveHealthTypeIsEverRequested`, `noCharacteristicTypeIsEverRequested` and `unconsumedCategoryFamiliesStayOutOfTheRequest`. Medications and Clinical Health Records are refused by a separate check that runs before any request is made (section 3.3).

**You are not obliged to grant any of it.** Apple's sheet has an individual toggle for every category, and the app works with whatever subset you allow. If you only want blood pressure to come through, turn on only blood pressure. You can also skip Apple Health entirely and type readings in.

We are listing the removed categories explicitly, rather than quietly dropping them, because an earlier version of this policy told you the app asked for them. It no longer does, and you should be able to check that against the permission sheet.

### 3.2 What the app writes back to Health

The app writes back a much narrower set, and only readings **you typed into OmniSalub yourself**:

- Systolic and diastolic blood pressure, heart rate, body weight, height, blood glucose, oxygen saturation — each only where one of your active conditions uses it.
- The symptom types listed in the table above, and only where the symptom means exactly the same thing in Apple Health.

Readings that came *from* Health are never written back, so the app cannot create duplicates of your own data. Symptoms carrying an extra clinical qualifier — "breathlessness on waking", for example — stay only on your device, because writing them as a plain symptom would misrepresent what you recorded.

Writing to Health is how your readings reach your other Apple devices. Data inside Health is managed by Apple under Apple's terms and encryption. **We never see it.**

### 3.3 What the app does *not* read

- **Medications and dose records.** The shipping app does **not** read your medication list or your record of doses taken or skipped. Those are gated Apple capabilities; the capability flag in this build is hard-coded off and the code path returns without asking for anything. If that ever changes, this policy will be updated before that version ships.
- **Clinical Health Records** — lab results and other records imported from a participating hospital or clinic. The app does not request the entitlement and does not query them; that capability flag is hard-coded off as well.
- **Everything listed under "what the app does not ask for" in section 3.1.** It is not requested, so it cannot be read.

### 3.4 Withdrawing permission

Go to **Settings → Privacy & Security → Health → OmniSalub**, or use the Health app. Revoking permission stops future reads and writes. It does not delete anything already in Health — you control that in the Health app — and it does not delete readings the app already imported; use **Delete everything this app stored** (section 14) for those.

### 3.5 Apple's extra rules for health apps

Apple's App Store Review Guideline 5.1.3 imposes obligations beyond ordinary privacy law. This is how the app stands against them:

- **5.1.3(i)** — health and fitness data must not be used or disclosed for advertising, marketing or other use-based data mining. We do none of those things at all, with any data.
- **5.1.3(ii)** — apps must not write false or inaccurate data into HealthKit, and **may not store personal health information in iCloud**. The app's health database is created with iCloud syncing explicitly disabled, and an automated test blocks any health record type, or any health-revealing field, from being added to the part of the app that does sync.
- We disclose the specific health data the app reads from the device — that is section 3.1 above.
- Guideline 5.1.1(i) also asks an app to request only the data it needs. Every type in the table in section 3.1 is one that at least one of the app's condition programmes reads, and Connect Apple Health asks only for those the conditions you track use (section 3.1).

---

## 4. What is stored on your device

| What | Where it lives | Leaves the device? |
|---|---|---|
| Readings you record or import, with where each imported reading came from (section 3.1) | Local database in the app's private storage | Only to Apple Health, for readings you typed, if you allow it; and in exports you make (section 9) |
| Symptoms you report | Same database | Same |
| Alerts the app raised | Same database — which guideline rule fired, when, at which rule-set version | No |
| Activity log (section 12) | Same database | No |
| Which conditions you track, whether you asked to hide food and weight scoring, whether **Import everything from Health** is on, your visit date, whether visit reminders are on, your visit questions, and when you accepted the first-run acknowledgements | On-device preferences only | **Never** — treated as health information |
| Your settings — theme, guideline set, app lock, whether onboarding is done, which tab you last had open | On-device preferences, and a separate preferences database | Only to your own iCloud, and only if you turn sync on (section 5) |
| A "where you left off" note — which tab you were on, the identifier of the Learn topic you last opened, when, and your appearance choice | Apple's iCloud key-value storage, written only while settings sync is on | Not in this version (section 5) |
| What the Home Screen widget shows — what to log next, and today's latest reading only if you turn that on | A small file in the app's shared container, so the widget can read it | No |
| Assistant settings — whether Ask is on, whether the model may download over cellular, which model is installed | On-device preferences | No |
| Optional Ask model files | Application Support folder, about 400 MB, excluded from device backup | No |
| Your Ask conversation | Held on screen only while Ask is open; not saved | No |
| A temporary copy of an export you create | The app's temporary folder, excluded from backup; the app clears these copies | Only where you send it (section 9) |
| Bookmarks recording how far the Apple Health import has got | On-device preferences | No |

The health database is stored in Application Support (not a user-visible folder). On iPhone, iPad and Apple Vision Pro it is set to Data Protection "complete", which means the operating system encrypts it with a key tied to your device passcode and it cannot be read while the device is locked. The database and its two working files are marked as excluded from iCloud backup.

The widget's file is also **excluded from device backup**, and the exclusion is re-applied every time the app writes the file, so files left behind by older versions of the app are covered too. On iPhone and iPad that file is encrypted at rest **until the first time you unlock the device after a restart**, rather than being locked again whenever the screen locks. That is a deliberate difference from the health database: the Home Screen widget has to be able to redraw while the phone is locked, and it could not do that under the stronger setting. By default the file holds no reading — only the name of what to log next, such as "Blood pressure". If you turn on **Show today's reading on the Home Screen** (off by default), it also holds your latest reading from today in display form, for example "132/84", and the widget hides that number while the device is locked. Treat that as the one value on your device with slightly weaker protection than the rest, and leave the switch off if you would rather it did not exist at all.

---

## 5. iCloud and your other devices

**Your health data is never stored in iCloud by this app.** That is an architectural boundary, not a setting, and it is also required by Apple's Guideline 5.1.3(ii).

### Settings sync

If — and only if — you turn on **Sync settings with iCloud** in Settings, exactly six things are stored in **your own** iCloud account so they match across your devices:

- your chosen theme
- which published guideline set is selected
- whether onboarding has been completed on a device
- whether app lock is enabled
- which tab you last had open (Today, Learn, Record or More)
- the time that record was last updated

This uses Apple's CloudKit **private** database, which is your iCloud account and not ours. We cannot read it. The setting is **off by default**, the app does not even create the syncing database until you say yes, and a change takes effect the next time the app opens.

Deliberately never synced: readings, symptoms, alerts, the activity log, which conditions you track, your visit date and questions, and your answer to the food-and-weight screening question. The list of fields allowed to sync is enforced by an automated test, not by a promise.

### The "where you left off" note

Only while **Sync settings with iCloud** is on, the app also writes a small note through Apple's iCloud key-value storage: which tab you were on, the identifier of the Learn topic you last opened (for example a topic about PSA test numbers), the time, and your appearance choice. It never contains a reading. It exists so that another device could offer to continue where you left off. With sync off the app does not write it, and turning sync off removes it. **This version of the app is not signed with Apple's iCloud key-value storage capability, so even with sync on the note is not uploaded to iCloud and does not leave the device.** One consequence is that the Continue row on Apple TV has nothing to show in this version. **Delete everything this app stored** clears the note.

### Handoff

On iPhone, iPad, Mac and Apple Vision Pro the app tells Apple's **Handoff** where you are, so a nearby device signed in to the same Apple Account can offer to open the app at the same place. What it passes is the tab you are on and, if you are reading a Learn topic, that topic's identifier — never a reading. Handoff is Apple's service between your own devices; it does not reach us. You can turn Handoff off in your device's settings.

---

## 6. When the app connects to the internet

Earlier versions of this policy said the app "makes no network requests of its own". **That statement was wrong, and it was corrected.** Here is the complete and accurate list.

### 6.1 Hugging Face — the optional Ask model

Ask can use a small language model that runs on your device where Apple Intelligence is not available (section 7). That model is not bundled with the app. If you choose to download it — the **Download local model** button in Settings → Assistant or in Ask — the app downloads the model files from **huggingface.co**, a public model host run by Hugging Face, Inc.

- **It never happens automatically.** Nothing downloads unless you tap the button, and only while **On-device assistant** is on.
- **What is sent:** requests for the files of one named public model repository (`mlx-community/Qwen3-0.6B-4bit`, pinned to commit `73e3e38d`), standard request headers that name the app, and, unavoidably, your device's IP address, as with any web request. The app sends no Hugging Face account or token. Hugging Face's own privacy policy governs what they do with that request.
- **What is not sent:** your health data, your readings, your symptoms, your questions to Ask, any account identifier, or any identifier of you. None of that is in the request, because the request is for model files.
- **Size:** about 400 MB. Before starting, the app checks that there is enough free storage; that figure never leaves the device. The download uses Wi-Fi unless you turn on **Download over cellular**. After download the app checks the model's main files against fixed checksums. You can delete the files in Settings → Assistant (the button is available while **On-device assistant** is on), or by deleting the app.
- If you never download the model, the app never contacts Hugging Face. On Apple Watch and Apple TV there is no download at all.

For completeness: the app is built on the MLX machine-learning packages `mlx-swift-lm`, `swift-huggingface` and `swift-transformers`. These are how the model is downloaded and run. They are not analytics, advertising or tracking libraries, and none of them transmits your content.

### 6.2 iCloud settings sync

Off by default. Described in section 5. This goes to Apple, into your own account — not to us.

### 6.3 The App Store

If you buy or restore OmniSalub Pro, StoreKit on your device talks to Apple's App Store. StoreKit also fetches the Pro prices when you open the Pro screen, and checks your entitlement with Apple when the app starts. Apple processes payments. Nothing about a purchase is sent to us (section 2).

### 6.4 Apple's own services, which the app uses but does not control

- **Apple Health** moves your data between your own devices, under Apple's encryption.
- **Apple Intelligence.** Where it is turned on and ready, Ask uses Apple's on-device model. The app does not use Apple's Private Cloud Compute or any server model (section 7).
- **Handoff** passes where you are in the app between your own nearby devices (section 5).
- **Apple Watch.** The iPhone app and the Watch app talk over Apple's connection between the two devices (section 8.1).
- **Siri and Shortcuts.** The app offers spoken shortcuts to log a blood pressure reading or report a symptom, and a Control Center control that starts a guided measurement. When you speak to Siri, Apple handles the speech, under Apple's privacy policy. The app receives the resulting values and stores them locally, and — like a reading you type — saves them to Apple Health if you allowed that. Siri may speak the app's confirmation or alert text back to you.
- **iCloud Backup**, if you use it, backs up your device under Apple's terms. The health database is excluded from it, as are the widget's file and the downloaded model.
- **"Share With App Developers"**, if you have it on in iOS Settings, may give Apple's aggregated crash reports to us. That is Apple's mechanism and it contains no health data.
- **Links.** Source links in Learn, the privacy policy and terms links, Apple's licence agreement, the support link and the source-repository links under Acknowledgements open in your web browser or mail app, and the crisis resources in Ask can open your phone or messages app to call or text a crisis line. The site or service you open sees that request, as with any link; the app adds nothing about you to it.

### 6.5 What does not exist

There is **no Prameya server**. No API, no backend, no endpoint that receives your data. We could not read your readings if we wanted to. There is no analytics SDK, no advertising SDK, no crash-reporting SDK, no attribution SDK, and no third-party code in the app that transmits user content.

The Mac version of the app carries macOS's outgoing-network entitlement, and it is there for the connections named above and no others we have built: iCloud settings sync and the optional Hugging Face model download. Neither carries health data or anything you have written.

The app also contains **no** code for location, camera, photo library, contacts, microphone recording, the advertising identifier, App Tracking Transparency, or Sign in with Apple.

An unfinished multi-device sync engine exists in the app's source code. **It is not built into any shipping app** — no app target links it. If it is ever completed, this policy will be updated before that build ships.

---

## 7. Ask, the on-device assistant

Ask is on by default (**Settings → Assistant → On-device assistant**). It works on iPhone, iPad, Mac and Apple Vision Pro, and — through your iPhone — from Apple Watch. On Apple TV it only quotes the built-in library (section 8.2).

- **Which model answers.** Where Apple Intelligence is turned on and ready on the device, Apple's on-device model answers; no download is needed. Where it is not, and you have downloaded the optional model (section 6.1), that model answers. Where neither can answer, Ask says so. The Ask screen shows which one will answer.
- **What the model is given.** Your question as you typed it, and a summary the app builds from what you have logged: the names of the conditions you track; for the last 30 days, per-measurement counts, averages, ranges and latest values, up to 36 individual readings with their times, and up to 12 symptoms; any open alert below the urgent level (which rule fired); and matching passages from the app's built-in reference. The app reads no medications, so none are included.
- **Where it runs.** Both models run **on your device**. The app sends your question and that summary to neither us, Apple, Hugging Face, nor any AI provider, and it does not use Apple's Private Cloud Compute.
- **Checks around the model.** Before the model is asked, the app checks your question for crisis language and answers that with fixed crisis resources — crisis language never goes to a model. When an urgent or emergency alert is open, Ask shows that alert's fixed text instead of asking the model. Questions and answers in the highest-risk categories, such as diagnosis and dosing, are refused with a fixed redirect.
- **Nothing is saved.** The conversation stays on screen while Ask is open and is not written to storage.
- The app's design allows for two further modes — Apple's Private Cloud Compute, and an outside AI provider. **Neither is enabled or reachable in this version**; both are hard-wired off. If either ever ships, it will be off by default, will require separate explicit consent, will name the provider, and this policy will be updated first.
- Every other feature — logging, trends, alerts, export — works with Ask turned off.

---

## 8. Widgets, the Lock Screen, Siri, Apple Watch and Apple TV

- The **Home Screen widget** (iPhone and iPad) shows what to log next and, only if you turn on **Show today's reading on the Home Screen**, your latest reading from today. To do that, the app saves a small display file — for example "Blood pressure", or "132/84" with its time if you turned the number on — into a container shared between the app and the widget. It stays on the device, is excluded from backup, and never goes to iCloud. See section 4 for how it is protected.
- The **Live Activity** shown during a guided measurement session carries the session's state: which measurement, which phase, how many readings so far, positioning guidance and a countdown. It does not carry your values, and it is drawn on your device. The app sends no push notifications, and holds no push capability.
- **Siri shortcuts** let you log a blood pressure reading or report a symptom by voice, and a **Control Center control** starts a guided measurement. See section 6.4 for what that means.

### 8.1 Apple Watch

The Watch app shows the built-in Learn library, a few prompts (start a guided walk on the iPhone, open Record on the iPhone, open tonight's Learn topic), and **Ask iPhone**. It stores no readings and does not use Apple Health. Its watch-face complications show a fixed title, such as "Log on iPhone", and never a reading.

- **Prompts.** Tapping a prompt's button sends that choice to your iPhone, which carries it out. Nothing is logged from the wrist.
- **Ask iPhone** sends the question you type to OmniSalub on your paired iPhone, over Apple's connection between the two devices; if the iPhone is not reachable, that connection holds the question and delivers it later. The iPhone answers it the way Ask on the iPhone does (section 7) — including the summary of what you have logged — and sends the answer text back to the Watch, where it is shown and not saved. A question from the Watch never starts a download.

None of this reaches Prameya.

### 8.2 Apple TV

The Apple TV app shows the built-in Learn library, a Continue row, and an Ask tab. It stores no readings, does not use Apple Health, does not download a model and makes no network connection of its own. Ask on Apple TV refuses questions about your own readings and answers others by quoting the built-in library. The Continue row reads the "where you left off" note (section 5), which in this version is never shared with the TV, so it shows nothing to continue.

---

## 9. Exports and sharing

The app can produce a record of your readings to give to a clinician: a raw CSV of your readings and a CSV of your symptoms (free), and, with Pro, a **PDF** visit summary, a formatted **CSV** file, or a **FHIR** bundle.

- An export is created only when you ask for one.
- It is handed to the standard share sheet. **You** choose what happens next — print it, email it, save it to Files, hand it over in person.
- The app does not upload it anywhere and we never receive a copy. The temporary copy it makes to hand to the share sheet is excluded from backup and cleared by the app.
- Once you send an export to another person, app or service, this policy no longer governs it. The recipient's terms apply. An export contains real health data — a FHIR bundle can also include the name, model and identifiers of the device that measured a reading — so treat it the way you would treat a paper record.

---

## 10. Notifications

The app asks permission to send notifications only when you set a visit date and turn on **visit reminders**, which are off until you do. If you allow it, the app schedules **local notifications** on your device at 19:00 on each of the seven days up to and including the visit day, titled "OmniSalub" and reading "today's reading for the visit on" followed by the date. They do not name a condition. If you hide notification previews, iOS shows "Reminder" instead of that text. Turning the switch off, or **Delete everything this app stored**, removes pending reminders.

A reminder's **Later** button, and the snooze on an Apple Watch prompt, schedule one more local reminder — and only while visit reminders are on. Tapping a notification only opens the app; only its action buttons do anything.

There is no notification server, and no notification content is transmitted anywhere. Alerts about a concerning reading are shown in the app, never sent as a notification. Apple TV shows no notifications from this app.

---

## 11. Diagnostics and analytics

**This version records no usage analytics.** There is no counter, no event log of what you tapped, and nothing to send even if there were a place to send it.

On iPhone, iPad, Mac and Apple Vision Pro the app subscribes to Apple's **MetricKit**, which delivers performance and crash diagnostics for the app to the app itself. The app writes a few of Apple's own aggregate figures from those reports — average launch and hang times, disk writes, and counts and types of crashes and hangs — to the device's system log, and keeps nothing else. Nothing from MetricKit is stored by the app, and nothing is transmitted. The Apple Watch and Apple TV apps do not use MetricKit.

The app also writes short operational messages to the device's system log — for example errors, the progress of the model download, or the name of a measurement type it could not read. It never writes a reading's value, and its messages about Ask are marked private, so the system redacts them. The system log stays on your device unless you choose to share diagnostics with Apple.

The app does contain the scaffolding for future on-device usage counting, built so that any event name must come from a fixed, closed list — a reading could not end up in one even by mistake — kept only on your device and deleted after 180 days. **Nothing switches it on today.** If a future version does, this section will be updated before that version ships.

The app's privacy manifest, which Apple ships inside the app and which anyone can inspect, declares that the app does **no tracking** and collects **no data types**. It declares these "required reason" API uses: storing settings in UserDefaults (the app's own, and the container it shares with its widget), checking available disk space before the model download, and reading the timestamps and sizes of files inside the app's own container, which the model download uses to manage its files. The Watch, TV and widget manifests declare UserDefaults only.

---

## 12. The activity log

The app keeps a local log of security-relevant events: when its database was opened; when readings were imported from or written to Apple Health; when a record was edited or deleted, or everything was erased; when the app asked for Apple Health permission; when an alert was raised; when settings sync was turned on or off; and when someone unlocked the app or failed to.

This log:

- **contains no health values.** Each entry is one of a fixed list of event types plus a short identifier such as a measurement name, an alert's rule identifier or a count of imported readings — never a number you recorded, and never text you wrote.
- is stored only on your device.
- is tamper-evident: each entry is cryptographically chained to the one before it, so if entries are altered or removed, the app can tell you.
- is visible to you at any time under **Settings → Security → Activity log**.
- is **cleared** when you use **Delete everything this app stored**, leaving a single entry that records the erase. Deleting the app removes it entirely.

It exists so that "what happened to my data?" has an answer, which is impossible after the fact if nothing recorded it.

---

## 13. Security

- **iPhone, iPad and Apple Vision Pro.** The health database uses Data Protection set to "complete": encrypted by the operating system with a key derived from your passcode, and unreadable while the device is locked. **Set a passcode.** Without one, the operating system cannot protect the file.
- **Mac.** macOS does not offer the same per-file protection. On a Mac the database is protected by the app sandbox and by **FileVault, if you have FileVault turned on.** We recommend turning it on in System Settings → Privacy & Security.
- **App lock.** You can require Face ID, Touch ID, Optic ID or your device passcode to open the app. Your fingerprint, face or eye data is handled entirely by Apple; the app never receives it and never stores it.
- **Keys.** Any encryption key the app uses is held in the device Keychain, marked so it is available only when the device is unlocked and never leaves that device.
- **Backups.** The health database, the widget's file and the downloaded model are excluded from iCloud backup. The widget file's at-rest protection is weaker than the database's, for the reason given in section 4.

No security measure is absolute. Because your data lives on your device, its safety depends heavily on that device having a passcode and up-to-date software.

---

## 14. Keeping and deleting data

**We hold nothing, so there is nothing at Prameya to delete.** On your device:

- Readings, symptoms and alerts are kept until you delete them. **Settings → Your data → Your records** lets you open, correct or delete individual records from the period the app shows (90 days, or up to 400 with Pro); older records stay on your device and in the raw export until you use Delete everything or delete the app.
- **Settings → Your data → Delete everything this app stored** erases your readings, symptoms and alerts immediately, and resets the conditions you chose, your visit date, visit questions and reminder switch, your food-and-weight answer, and your theme, guideline set, app lock and last tab on this device; if sync is on, it deletes your iCloud copy of those settings. It also cancels pending visit reminders, clears the "where you left off" note, the widget's file, the **Show today's reading on the Home Screen** switch and the bookmarks of how far the Apple Health import got, clears the activity log down to one entry recording the erase (section 12), and returns you to the first-run screens.
- **What Delete everything keeps:** anything in Apple Health, and the Apple Health permissions you granted (change those in your device's Settings); the downloaded Ask model and your Assistant settings; your choice about iCloud settings sync; and your Pro purchase, which is Apple's record.
- **Deleting the app** removes all of its local data on that device, including the health database, the activity log, the widget's file and any downloaded model files.
- You can remove the Ask model files on their own in **Settings → Assistant → Remove local model** (available while **On-device assistant** is on).
- If you turned on settings sync, turning it off stops future syncing. You can remove what is already stored through **Settings → [your name] → iCloud → Manage Account Storage** on your device.

> Erasing data in OmniSalub does **not** delete anything the app previously wrote to Apple Health. That data is yours and lives in the Health app, where it may also be arriving from a cuff, a watch or a clinic. Delete it there if you want it gone.

---

## 15. Your privacy rights

Because we neither collect nor receive your personal data, we hold no record about you to disclose, correct, port or delete. There is nothing for us to sell or share. But you retain complete, direct control:

| Right | How you exercise it |
|---|---|
| Know / access | Everything is visible in the app, and exportable as a raw CSV of readings and a CSV of symptoms, or with Pro as a PDF, formatted CSV or FHIR bundle |
| Portability | Use the raw CSV, or with Pro the FHIR or formatted CSV export |
| Correction | Edit or delete any entry in the app |
| Deletion | Settings → Delete everything this app stored, or delete the app |
| Limit processing | Revoke Health permission; turn off settings sync; turn off On-device assistant; do not download the Ask model |
| Withdraw consent | Any permission can be revoked at any time in your device's Settings |

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

For the processing that happens entirely on your device, Prameya LLC is the controller. Our lawful basis is your consent (Article 6(1)(a)) and, because health data is a special category, your **explicit** consent (Article 9(2)(a)) — given through the in-app acknowledgements and through iOS's own Health permission sheet. You may withdraw consent at any time as described in the table above, without affecting anything that already happened. You have rights of access, rectification, erasure, restriction, portability and objection; in practice you exercise all of them directly in the app, because we hold no copy. You may complain to your supervisory authority.

Where the app is available is set on the App Store, not here, and can change. This subsection applies to you if you obtained the app in the EEA or the UK.

### HIPAA — plainly

**HIPAA does not apply to OmniSalub.** HIPAA covers healthcare providers, health plans and clearinghouses, and the contractors that handle data for them. Prameya is none of those, and we are not a business associate of any of them. You are using a consumer app you chose yourself, not a service arranged by your doctor or insurer.

We say this because it matters: it means the protection your data has here comes from this app's design and from consumer-protection law, not from HIPAA. It also means we do not claim HIPAA compliance and you should be sceptical of any consumer app that does. If OmniSalub is ever distributed through a clinic, employer or insurer, that analysis changes and this policy will change with it.

---

## 16. Children

OmniSalub is intended for adults managing a chronic condition. It is not directed to children under 13, is age-rated for older teenagers and adults because it contains medical information, and we do not knowingly process children's data. Because the app collects nothing and transmits nothing to us, we hold no children's data and there is nothing for us to delete on request. **We serve no advertising of any kind**, so there is no advertising or behavioural profiling of anyone, children included.

A parent or guardian concerned about a child's use of the app can remove the app's data by using Settings → Delete everything this app stored, or everything by deleting the app. Questions: admin@prameya.legal.

---

## 17. What OmniSalub is not

Stated here because it affects how you should treat what the app shows you.

**OmniSalub is a general wellness tool. It does not diagnose, treat, cure or prevent any disease, and it is not a medical device.** It does not give medical advice and does not give medication instructions. When it flags something, it tells you what it observed and suggests you speak to a doctor. Ask's answers are written by a language model and can be wrong.

**It is not a substitute for professional medical care and must never be relied on in an emergency.** If you think you are having a medical emergency, call your local emergency number.

---

## 18. Changes to this policy

If this policy changes, we will change the effective date at the top and publish the new version at [prameyallc.github.io/privacy/omnisalub](https://prameyallc.github.io/privacy/omnisalub/).

Where a change materially affects how your data is handled — in particular if any future version were to transmit health data off your device, add an account, add a server, or enable cloud or third-party AI processing — we will show you the change in the app and ask for your consent **before** it takes effect. We will not quietly widen what we do and rely on you re-reading this page.

**23 September 2026 — what changed.** This revision describes what the app does today, on every device it runs on:

- **Apple Health.** It says that **Connect Apple Health** asks only for the types the conditions you track use (General health's extra types only with **Import everything from Health** on) and imports the last 400 days of each type you allow (symptom records in full). Earlier versions described a separate "Import all Health history" action, which no longer exists. The table now also lists breathing disturbances during sleep and Apple's hypertension and sleep apnea notifications, which a condition can ask for. It also says what the app keeps about the device that measured an imported reading, and that nothing is read in the background.
- **Ask.** It says Ask is on by default and uses Apple Intelligence's on-device model where it is ready, and the optional downloaded model otherwise; what summary of your logged data the model is given; and that the question and summary stay on the device. Earlier versions described only the downloaded model.
- **More devices.** It now covers Apple Vision Pro, the Apple Watch app (including Ask iPhone) and the Apple TV app.
- **iCloud and Handoff.** It says settings sync now carries six items, adding the tab you last had open; describes the "where you left off" note, which is written only while settings sync is on and in this version stays on the device; and describes Handoff.
- **Purchases.** It says the App Store is one of the app's connections, corrects the earlier statement that the app stores your transaction records itself, and says Pro shows up to 400 days of history in the app rather than "unlimited".
- **Notifications and the widget.** It says visit reminders are off until you turn them on, and that the widget shows a reading only if you turn that on.
- **Deletion.** It describes **Delete everything this app stored**, which now also resets your conditions, visit date and preferences, deletes your iCloud copy of your settings, turns the Home Screen reading off and clears the activity log, and lists what it keeps.
- **Diagnostics and the activity log.** It says MetricKit now runs on Mac and Vision Pro too, what the app writes to the device's system log, and lists all of the privacy manifest's required-reason declarations. It also corrects the list of events in the activity log: exports are not recorded there, and alerts, edits and deletions are.

- **Privacy fixes in the app, later the same day.** An earlier revision of this page, also dated 23 September 2026, described four things the app then did and no longer does: Connect Apple Health asked for every type in the table in section 3.1 whichever conditions you chose; the "where you left off" note was written to iCloud key-value storage even with settings sync off; **Delete everything this app stored** reset your iCloud copy of your settings instead of deleting it; and it kept the activity log and the **Show today's reading on the Home Screen** switch. This revision describes the app with those fixed.

Nothing the app sends to Prameya changed: it still sends us nothing.

**Earlier revisions (8–21 August 2026).** Those revisions corrected statements in the previous version so that they matched the code that shipped then. The main correction narrowed the description of what the app asks to read from Apple Health, removing reproductive-health and profile categories that were taken out of the request (section 3.1), and replaced a placeholder note about the widget's file with a statement of what the app does.

Material changes are also described in the Consumer Health Data Privacy Policy, which has its own change process.

---

## 19. Contact

Questions, requests or complaints about privacy in OmniSalub:

**admin@prameya.legal**
Prameya LLC
Postal address available on request by email.

---

*This policy describes OmniSalub version 1.0 and later. It replaces the previous OmniSalub privacy policy dated 8 August 2026 (last updated 21 August 2026), which described a narrower Apple Health request than the app makes, did not describe Ask with Apple Intelligence, the Apple Watch, Apple TV and Vision Pro apps, Handoff or notifications, and said the app stored purchase records it does not store. That policy in turn replaced one dated 7 August 2026, which incorrectly stated that the app makes no network requests and that it reads your medication records.*

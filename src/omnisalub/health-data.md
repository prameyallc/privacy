# OmniSalub Consumer Health Data Privacy Policy

**Effective date:** 8 August 2026
**Publisher:** Prameya LLC ("Prameya", "we", "us")
**Applies to:** OmniSalub for iPhone, iPad and Mac
**Contact:** admin@prameya.legal

This is a **separate, distinctly-labelled consumer health data privacy policy**, published as required by Washington's My Health My Data Act (RCW ch. 19.373) and drafted to satisfy Nevada's consumer health data law (SB 370, NRS ch. 603A) at the same time. It sits alongside — and does not replace — the [OmniSalub Privacy Policy](https://prameyallc.github.io/privacy/omnisalub/).

If you are a Washington or Nevada resident, this is the document written for you. Everyone else is welcome to read it; it describes what actually happens either way.

---

## Read this first

OmniSalub is a chronic-condition companion. It handles health data about you — that is its entire purpose. What matters is where that data goes.

**Prameya operates no server. No health data about you is ever transmitted to Prameya. We have no copy of it, no database of users, and no ability to obtain it.** The app processes your health data on your own device, under your control.

Washington's law defines "collect" broadly — it reaches data that is accessed, processed, derived or inferred, not only data that is received by a company. Apple's App Store privacy labels use a narrower definition ("collect" = transmitted off the device). **We are not relying on Apple's narrower definition here.** This policy describes everything the app does with your health data on your device, and treats it as within scope. We do not assert that we are outside the Act.

---

## 1. Categories of consumer health data, and why the app handles them

All of the following is processed **on your device**. None of it is transmitted to Prameya.

| Category of consumer health data | What that means here | Why the app handles it |
|---|---|---|
| **Vital signs and bodily functions** | Blood pressure, heart rate, resting and walking heart rate, heart-rate recovery, heart-rate variability, atrial-fibrillation burden, oxygen saturation, respiratory rate, body temperature (including basal and wrist temperature), peripheral perfusion index | To show your readings over time, and to compare them with published guideline thresholds so the app can tell you when to contact a clinician |
| **Body measurements** | Weight, BMI, body fat, lean mass, height, waist circumference | Weight change is a core heart-failure signal; the rest give context |
| **Blood glucose and related** | Blood glucose, insulin delivery, blood alcohol content | Diabetes and kidney disease frequently travel with the conditions this app covers |
| **Alcohol consumption** | Number of alcoholic drinks | Added 2026-08-08 for the alcohol-use programme, which previously had no Apple Health source and required every entry to be typed twice. Requested only if you switch that programme on |
| **Lung function** | FEV1, forced vital capacity, peak flow, inhaler use | Breathlessness has cardiac and respiratory causes |
| **Symptoms you report** | Breathlessness, chest pain or tightness, dizziness, palpitations, skipped heartbeat, fainting, nausea, vomiting, fever, gastrointestinal symptoms, fatigue, headache, mood changes, appetite changes, sleep changes, and more specific variants defined by the condition you track | Symptoms drive the app's escalation rules — several are the difference between "log it" and "seek care today" |
| **Diagnoses and conditions** | Which conditions you have chosen to track (for example hypertension, heart failure, chronic kidney disease) | Determines which measurements the app asks for and which guideline rules apply |
| **Health-related alerts** | Which guideline rule fired, when, and at which rule-set version | So you and, if you choose, your clinician can see the history |
| **Sleep, activity and mobility** | Sleep records (time in bed, time asleep, sleep stages), exercise minutes, move and stand time, steps, energy, flights climbed, distances, workouts, time in daylight, UV exposure, walking speed and steadiness, falls, six-minute walk distance | Functional decline is clinically meaningful in heart failure and kidney disease |
| **Nutrition and diet** | Energy, macronutrients, cholesterol, water, caffeine, and minerals including **sodium and potassium** | Sodium and potassium have specific dietary rules in hypertension and kidney disease |
| **Cardiac event notifications from an Apple Watch** | Exactly four record types: high heart-rate, low heart-rate, irregular-rhythm and low-cardio-fitness notifications | Available from an Apple Watch; shown alongside your other readings. These are consumer notifications, not diagnoses |
| **Hearing exposure** | Environmental and headphone audio-exposure levels | Read as ordinary measurements alongside the rest; audiograms are not requested |
| **Inferences the app makes** | Whether a reading falls inside or outside a published guideline band, trend direction, and whether an escalation rule fired | This is a derived health inference, so we list it: Washington's definition reaches derived data too |

**This table is a ceiling, not a description of your device.** As of 2026-08-08 the app asks Apple Health only for the categories belonging to the conditions **you** have switched on. If you track blood pressure and nothing else, the app requests eight record types — blood pressure (systolic and diastolic), weight, exercise minutes, and the four symptom records its emergency rule checks. It previously requested twenty-nine. Sleep, workouts, Watch cardiac notifications, nutrition and mobility are requested only if something you switched on reads them. The single exception is **Settings → Import all Health history**, an explicit one-off action that does request the whole table, because a partial import of "all my history" would be a false promise.

**Purposes, stated completely.** The app uses this data to (a) display your own health record back to you, (b) compare readings against published clinical guideline bands, (c) raise a care-seeking prompt when a rule fires, (d) generate a summary you can give a clinician, and (e) answer your questions using an assistant that runs on your device. **That is the full list.** It is not used for advertising, marketing, profiling, research, product analytics, model training, or sale — none of which the app or Prameya does at all.

### What the app does not handle

An earlier version of this policy listed reproductive and sexual health data and profile facts among the categories the app requested from Apple Health, because at that time it asked for the full ordinary read set. **It no longer does.** The permission request has been narrowed to the types the app actually consumes, and automated tests fail the build if a removed type comes back. The following are not requested, and therefore cannot be read:

- **Reproductive and sexual health data.** None of it: menstrual flow, intermenstrual bleeding, cycle-irregularity records, ovulation, pregnancy and progesterone test results, cervical mucus, contraceptive use, lactation, pregnancy, sexual activity. Fourteen record types in total. This is the most sensitive category under Washington's law, and the app has no consumer for any of it.
- **Profile facts** — date of birth, biological sex, blood type, Fitzpatrick skin type, wheelchair use, activity move mode. Not requested, and there is no code anywhere in the app that reads them.
- **Electrocardiograms and audiograms.** Not requested.
- **Mindful sessions, Apple's stand-hour records, audio-exposure event notifications, toothbrushing and handwashing records.** Not requested.
- **Precise location.** Never requested and there is no location code in the app. Precise location is expressly consumer health data under Washington's law, and we intend to keep it that way by not having it.
- **Medications and dose records.** The shipping build does not read them; the capability is hard-coded off and the code path returns without asking.
- **Clinical Health Records** — labs and records from a hospital or clinic. Not requested, not read; that capability is hard-coded off as well.
- **Genetic data.** Never stored, in any form.
- **Biometric identifiers.** Face ID and Touch ID are handled entirely by Apple's Secure Enclave; the app never receives a fingerprint or face template.
- **Gender-affirming care records, and data about seeking or obtaining health services**, beyond what you personally choose to log.

You also remain free to decline any part of what the app *does* ask for. Apple's permission sheet has an individual toggle for every category, and the app works with whatever subset you allow.

---

## 2. Categories of sources

The app obtains consumer health data from exactly three sources:

1. **You.** Anything you type into the app: readings, symptoms, the conditions you track, and questions you ask the assistant.
2. **Apple Health on your device**, if you grant permission. Whatever is in Health has typically been put there by you, by a blood-pressure cuff, a scale, a glucose meter, an Apple Watch, or another app you use. Permission is per-category and you can withdraw it at any time.
3. **The app's own rule engine**, which derives inferences (band classification, trend, whether an alert fired) from the two sources above.

There is no fourth source. We buy no data, receive no data from data brokers, and obtain nothing from advertising networks, partners or affiliates — we have none.

---

## 3. Categories of consumer health data that we share

**None.**

Prameya shares no consumer health data with anyone, for any purpose, because Prameya never receives it. There is no server, no analytics service, no advertising network, no crash-reporting service, no marketing platform, and no research partner.

## 4. Categories of third parties and specific affiliates we share it with

**None.** Prameya has no affiliates and no subsidiaries, and we share consumer health data with no third parties.

Three things are worth naming precisely, because a reader should be able to check this against how the app behaves:

- **Apple.** If you allow it, health data moves between OmniSalub and Apple Health on your own device, and Apple syncs Health between your own devices. That is a transfer within your own account and under Apple's terms, not a disclosure to us or to anyone else. We do not receive it and cannot see it.
- **Hugging Face, Inc.** If you choose to install the optional on-device assistant, the app downloads model files from huggingface.co. **That request contains no health data.** It asks for a named public model and, like any web request, carries your IP address. No consumer health data is sent to Hugging Face at any time.
- **Anyone you send an export to.** The app can produce a PDF, CSV or FHIR file for your clinician. That is you disclosing your own data to a recipient you choose, using the system share sheet. The app does not upload it and we never see it. Once it leaves, the recipient's terms govern it.

## 5. Sale of consumer health data

**We do not sell consumer health data, and we never have.** Washington and Nevada both require a signed, specific written authorization before any sale. We have never sought one and have no plans to. If that ever changed, it would require your separate, revocable, written authorization — and we would have to tell you before it happened.

## 6. Geofencing

We do not use geofencing at all, anywhere. The app contains no location code. Both Washington and Nevada prohibit geofencing around healthcare facilities; we are nowhere near that line.

---

## 7. How the data is processed, stored and protected

- **Where.** In an encrypted database in the app's private storage on your device. On iPhone and iPad it is set to iOS Data Protection "complete", so it is encrypted with a key derived from your device passcode and is unreadable while the device is locked. On a Mac it is protected by the app sandbox and by FileVault if you have FileVault on.
- **Not in iCloud.** Health data is never stored in iCloud by this app. The health database is created with iCloud syncing explicitly disabled, and an automated test blocks any health record from reaching the part of the app that does sync. Only five non-health preferences (theme, guideline set, onboarding state, app lock, timestamp) can sync, and only if you turn that on — it is off by default.
- **Backups.** The health database is excluded from device backup. So is the widget's display snapshot — the small file holding your most recent reading in formatted form — and that exclusion is re-applied every time the app writes the file, so snapshots left by older versions of the app are covered too. On iPhone and iPad the snapshot is encrypted at rest until the first time you unlock the device after a restart, rather than being re-locked whenever the screen locks; the Home Screen widget could not redraw your latest reading otherwise. It is the one value on the device with slightly weaker at-rest protection than the health database, and you can avoid it entirely by not using the widget.
- **The assistant.** If you install it, the model runs on your device. The app assembles a summary of your logged data as context for it. That context never leaves your device and is not sent to us, to Apple or to any AI provider. Cloud and third-party inference modes are hard-wired off in this version.
- **Retention.** Your data stays until you delete it. We retain nothing, so there is no retention schedule on our side to describe.
- **Activity log.** The app keeps a tamper-evident local log of when health data was read, written, exported or erased. It records event types and short identifiers only — never a value you recorded. You can view it in Settings.

---

## 8. Your rights, and how to exercise them

You have the following rights under RCW 19.373.040 and NRS 603A.505:

| Right | What it means | How to use it |
|---|---|---|
| **Confirm and access** | Confirm whether we are collecting, sharing or selling your consumer health data, and get access to it | Email **admin@prameya.legal**. The answer will be that we hold none. Your actual data is visible in the app at any time, and exportable as PDF, CSV or FHIR |
| **List of recipients** | Get a list of the third parties and affiliates your data has been shared with | Email us. The list is empty |
| **Withdraw consent** | Withdraw consent to collection and to sharing | In the app: turn off Health access in **Settings → Privacy & Security → Health → OmniSalub**; turn off settings sync in the app's Settings; delete the assistant model. Each is independent and reversible |
| **Delete** | Have your consumer health data deleted, including from backups and archives | In the app: **Settings → Delete all data on this device**, which also clears the widget snapshot, or delete the app, which removes everything it stored. To delete what the app previously wrote to Apple Health, use the Health app — that copy is yours and is not ours to remove. We hold no copies, no backups and no archives, so there is nothing on our side to delete |
| **Appeal** | Appeal if we refuse a request | Reply to our response, or email **admin@prameya.legal** with "Appeal" in the subject. We will respond in writing with our reasoning within 45 days |

**How to make a request.** Email **admin@prameya.legal**. Tell us which right you are exercising. You do not need an account with us — we do not have accounts — and we will not ask you to create one or to give us extra personal data to "verify" you. If a request would require us to identify you and we cannot, we will say so plainly rather than collect information about you in order to answer.

**Timing.** We will respond **without undue delay and within 45 days** of receiving your request. If it is genuinely complex we may take one extension of a further 45 days, and we will tell you why within the first 45.

**Cost.** Free, up to twice a year, as the law provides.

**If we refuse and you disagree.** After our appeal decision, you may complain to your Attorney General:

- **Washington:** the Attorney General's office accepts consumer complaints online at [atg.wa.gov/file-complaint](https://www.atg.wa.gov/file-complaint).
- **Nevada:** the Attorney General's Bureau of Consumer Protection accepts complaints at [ag.nv.gov](https://ag.nv.gov/).

Washington residents should also know that a violation of the My Health My Data Act is an unfair or deceptive act under the Washington Consumer Protection Act (RCW ch. 19.86), which carries a private right of action under **RCW 19.86.090** — that is, you can sue in your own name. Nevada's law is enforced by the Attorney General and does not provide a private right of action.

---

## 9. Consent

- **Consent is how this works.** The app does not read anything from Apple Health until you grant permission through Apple's own sheet, category by category. It does not sync settings until you switch that on. It does not download the assistant model until you tap the button. Each is separately revocable.
- **We will not collect or share consumer health data beyond what this policy describes without first obtaining your affirmative, voluntary consent** — a clear, specific, opt-in choice, freely given, that is not buried in other terms and is not a condition of using the app. That includes asking Apple Health for any category listed under "what the app does not handle" in section 1: adding one back to the permission request would be a change to this policy, made before the build ships, not after.
- **Sharing would require its own separate consent**, naming the categories of data, the purpose, and the categories of recipients. Today there is no sharing, so there is nothing to consent to.

---

## 10. Changes to this policy

If we change this policy, we will update the effective date above and publish the new version at [prameyallc.github.io/privacy/omnisalub/health-data](https://prameyallc.github.io/privacy/omnisalub/health-data/).

This revision corrected statements in the previous version so that they match the code that actually ships. The main correction is in section 1: the category table previously listed reproductive and sexual health data and profile facts as data the app requests from Apple Health, on the basis that the app asked for the full ordinary read set. The read request has since been narrowed and those categories are no longer requested, so they have been moved to the list of data the app does not handle. Section 7 also replaces a placeholder note about the widget snapshot with a statement of what the shipping app does.

**Material changes get more than a new date.** If a future version of the app would collect, process or share consumer health data in a way this policy does not already describe — for example transmitting health data off the device, adding an account, enabling cloud or third-party AI processing, or widening the Apple Health permission request — we will describe the change in the app and obtain your affirmative consent **before** it takes effect, and before any data is handled under the new terms. A change to this policy will never be applied retroactively to data already collected.

---

## 11. Contact

**admin@prameya.legal**
Prameya LLC
Postal address available on request by email.

For everything else — security, exports, deletion, children, HIPAA, and what OmniSalub is and is not — see the [OmniSalub Privacy Policy](https://prameyallc.github.io/privacy/omnisalub/). Other Prameya app policies are listed at [prameyallc.github.io/privacy](https://prameyallc.github.io/privacy/).

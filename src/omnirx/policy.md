# OmniRx Privacy Policy

**Effective date:** August 8, 2026
**App:** OmniRx (iOS)
**Publisher:** Prameya LLC ("Prameya", "we", "us"), a US limited liability company
**Contact:** admin@prameya.legal

**If you are in Washington or Nevada, or you want the health-data specifics:** read the separate
[OmniRx Consumer Health Data Privacy Policy](https://prameyallc.github.io/privacy/omnirx/health-data/).
It is a distinct document, required by Washington's My Health My Data Act, and it covers the medication
and wellness information you enter into this app.

---

## The short version

- **No account.** There is no sign-up, no login, no email required to use OmniRx.
- **We run no server.** Prameya has no database of users, no profile store, and nowhere for your data to go.
- **Everything you type stays on your iPhone or iPad.** Your medication logs, barriers, notes, mood and energy entries are written to a private database inside the app on your device, created with iCloud sync switched off for that database.
- **Nothing you type goes to iCloud.** No medication log, no journal entry, no profile field syncs to iCloud.
- **The app does make one kind of network connection:** preference sync through **your** iCloud account (appearance, disclosure acknowledgement). There is no model download and no Hugging Face request.
- **Your questions and logs stay on your device.** They are not sent to us or to any AI provider.
- **No ads. No analytics. No trackers.** OmniRx contains no advertising SDK, no analytics SDK, and no crash-reporting SDK.
- **No camera, no photos, no microphone, no location, no contacts.** The app does not ask for these and cannot use them.
- **You can set one daily reminder** in Settings to log Taken or Skipped. The lock screen says “Reminder”, not a medicine name.
- **You can delete everything from inside the app.** Settings → "Delete all my data".
- **We do not sell your data.** We could not — we do not have it.
- **This is an education and habit-tracking app, not medical advice.** It does not diagnose, does not calculate doses, does not check interactions, and does not identify medicines from photographs.

---

## Who publishes OmniRx

OmniRx is published by Prameya LLC, a US limited liability company. Prameya is the party responsible
for this policy. Questions, requests and complaints go to **admin@prameya.legal**.

Prameya is a small publisher. It is not a pharmacy, not a health care provider, not a health plan, and
not a business associate of any of those. See [HIPAA](#hipaa-does-not-apply-to-omnirx) below.

---

## What OmniRx is, and what it is not

OmniRx is a **medication and pharmacology education app with habit support**. It explains classes of
medicines in general terms, helps you write down questions for your pharmacist, and lets you log
whether you took your doses and what got in the way.

OmniRx does **not**:

- diagnose anything;
- calculate or check doses;
- check for drug interactions;
- produce tapering or stopping plans;
- identify a pill or a label from a photograph;
- remind you to take or log a dose — it schedules no reminders and sends no notifications;
- give you advice about your own specific medicines.

It is not a substitute for a licensed pharmacist or physician.

---

## What data OmniRx handles, and where it lives

### Data you create in the app

This table describes what the shipping app actually records:

| What | What the app records today |
|---|---|
| Adherence log | whether you marked today's dose as taken, which barriers you selected, and a free-text note if you type one |
| Barriers | "Forgot", "Cost", "Side effect concern", "Regimen complexity", "Ran out", "Other" |
| Wellness journal | mood (1–5) and energy (1–5), set with steppers, saved alongside the same note |
| Habit log | whether the dose was taken on time — the app writes this from your adherence entry rather than asking you separately |
| Profile | the app creates one profile record on first launch containing two default goals. **There is no screen for entering your age, your health conditions, or your current medicines.** |
| Values the app calculates from the above | adherence percentage, current streak, number of days logged, a mood/energy average over the last 14 days, and a short "trends to discuss" text |

The app's data model also contains fields for hours of sleep, symptoms, health conditions and current
medications. **No screen fills those in today.** Sleep is stored at a fixed default value you cannot
set, symptoms are stored empty, a side-effect entry is recorded only when you select the "Side effect
concern" barrier, and the conditions and current-medicines fields are never written at all. If we ever
add screens for those fields, they are consumer health data, and this policy and the Consumer Health
Data Privacy Policy will be updated before those screens ship.

Most of what you log is **consumer health data**. It is covered in detail by the separate
[Consumer Health Data Privacy Policy](https://prameyallc.github.io/privacy/omnirx/health-data/).

### Where it is stored

On your device, inside the app's private storage area, using Apple's SwiftData. The store is created
local-only, with iCloud sync explicitly disabled for it. Other apps cannot read it. We cannot read it.

A small amount of technical information (feature flags and encryption keys used by the app itself) is
stored in the iOS Keychain, marked as device-only so it does not travel to other devices.

### iCloud device backup

**OmniRx does not exclude its data store from iOS device backup.** So if you have **iCloud Backup**
turned on in iOS Settings, Apple's normal whole-device backup may include the app's medication and
journal data along with everything else on your device. That is a setting you control on your device,
between you and Apple. We do not receive it and cannot access it. If you would rather it not be backed
up, you can turn off iCloud Backup for OmniRx in iOS Settings, or turn off iCloud Backup entirely.

### Data we receive

Almost none. Specifically:

- **If you email us**, we receive your email address and whatever you write. We keep support email only
  as long as we need it to answer you.
- **Apple gives us aggregated App Store reports** — downloads, crashes, and similar figures — for
  OmniRx as a whole. These are Apple's reports about the app, not about you, and they do not identify
  you. If you have turned on "Share With App Developers" in iOS diagnostics settings, Apple may send us
  crash logs; those are technical and contain no journal entries or medication logs.

That is the complete list. There is no other path by which anything reaches us.

---

## Network connections OmniRx makes

**We do not claim that OmniRx never uses the internet. It does, for one purpose.**

### Preference sync through your iCloud account

The only outbound connection in the shipping app is CloudKit sync of **non-health preferences**
through **your** private iCloud database: appearance mode, a leftover on-device-AI flag with no
Settings control (default off), a text-size preference, and the version of the first-run notice you
acknowledged. Medication logs, journal entries, and profile records are excluded by an allow-list
enforced by tests.

There is no model download, no Hugging Face client, and no reachable path to `huggingface.co`.

### On-device processing

Text you give the app is processed on your device. It is not transmitted to Prameya or to any AI
provider. There is no cloud fallback and no remote retrieval endpoint.

This is a real privacy benefit and we state it precisely: **your content is processed locally and is
not transmitted to us.** We do not say "nothing ever leaves the device", because preference sync
uses your iCloud account.

### Nothing else

There is no other outbound connection in the app. No telemetry endpoint, no ad request, no attribution
call, no license check.

---

## Things OmniRx does not do

One line each, because the honest answer is short.

- **Accounts:** none. There is nothing to sign up for.
- **Advertising:** none. No ad SDK is present, so no ad network receives anything about you.
- **Analytics:** none. No Firebase, no Amplitude, no Mixpanel, no custom event pipeline.
- **Crash-reporting SDK:** none. No Sentry, no Crashlytics.
- **Tracking across apps or websites:** none. We do not use the advertising identifier and do not ask
  for App Tracking Transparency permission.
- **Selling or sharing data:** never.
- **Camera and photos:** the app has no camera or photo-library code, and asks for no such permission.
  It cannot take or read pictures.
- **Microphone:** not used, and no permission is requested.
- **Location:** not used. No geofencing of any kind, anywhere.
- **Contacts, calendars, messages:** not used.
- **In-app purchases or payments:** none.
- **Data brokers:** we buy nothing and sell nothing.

### Apple Health (HealthKit)

**OmniRx does not read from or write to Apple Health.** It contains no HealthKit code, holds no
HealthKit entitlement, and declares no HealthKit usage description. An earlier build of the project
requested HealthKit entitlements that no code used; those have been removed. If HealthKit is ever
genuinely added, this policy will be rewritten first.

### iCloud sync

**No medication log, journal entry, habit record or profile field syncs to iCloud.** The database
holding everything you type is created local-only, with iCloud sync switched off for it. Your logs and
journal stay on the device where you wrote them.

To be precise about what the app does keep: OmniRx retains an iCloud/CloudKit container reserved for
ordinary app preferences. That container's schema is an allow-list that contains exactly one non-health
record type; your profile, medication logs, journal entries and habit records are excluded from it, a
test in the codebase asserts they are absent, and the app refuses to build the sync container at all if
that ever stops being true.

**As the app ships today, nothing is written to that container** — no preference actually syncs between
your devices, and your settings live in local storage on each device. We are telling you the container
exists rather than claiming a blanket "no iCloud". If preference syncing is ever switched on, it will
carry preferences and interface state only. **No health-derived field — no medication log, no journal
entry, no condition, no medication name — may ever sync.**

### Reminders and notifications

**OmniRx does not send reminders or notifications.** There is no notification or calendar code in the
app, and it never asks for notification permission. Some wording inside the app still describes
reminding you to log doses; that describes an intention, not a shipping feature, and we are correcting
it. If reminders are ever added, they would be local notifications scheduled by your device, and this
policy would be updated before they ship.

### Exporting your logs

Settings → **"Export my logs as text"** builds a plain-text summary on your device and shows it to you
in a sheet inside the app. The summary contains the share of doses you recorded as taken and over how
many logged days, your current streak, the days you logged in the window, and a count of the reasons
you recorded for missed doses.

- The text is generated on your device. Nothing is uploaded, and **we never receive a copy**.
- You can select and copy the text and paste it wherever you want it — a note, an email to yourself, a
  message to your pharmacist.
- There is no share sheet and no file: the app displays the summary, and moving it anywhere is your
  action, not the app's.

---

## On-device AI: what it is and what it is not

- **The shipping app has no on-device model.** Unused Intelligence (MLX / Hugging Face) was
  deleted. Settings does not offer a download.
- Because nothing is sent to a third-party AI provider, Apple's requirement to name one and obtain
  your permission before sharing personal data with one does not arise.
- The app still refuses dosing, interaction checking, tapering, pill identification, diagnosis, and
  any answer tailored to your specific medication list — those are not things OmniRx does.

---

## Consumer health data

The medication information, side effects, mood and energy entries you put into OmniRx are **consumer
health data** under Washington's My Health My Data Act and Nevada's SB 370 — **even though that data
never leaves your device.** Those laws define "collect" broadly enough to reach data that is accessed,
processed, or derived, not just data that is transmitted somewhere.

We do not use the fact that OmniRx works on-device to argue those laws do not apply. We treat this data
as consumer health data.

**The required separate policy is here:
[OmniRx Consumer Health Data Privacy Policy](https://prameyallc.github.io/privacy/omnirx/health-data/).**
It lists the categories collected, the sources, the purposes, the categories shared (none), and how to
exercise your rights, including withdrawing consent and deleting data.

---

## HIPAA does not apply to OmniRx

HIPAA covers health plans, health care clearinghouses, most health care providers, and their business
associates. **Prameya is none of those, and OmniRx is not offered through your doctor, your pharmacy, or
your insurer.** So HIPAA does not apply to this app, and we make no claim of HIPAA compliance.

We say this plainly because "HIPAA compliant" is a common and misleading badge on consumer health apps.
What actually protects your OmniRx data is that it stays on your device and we never receive it — plus
the state consumer health data laws described above.

---

## Your privacy rights

### California (CCPA/CPRA)

California residents have rights to know, delete, correct, and to limit the use of sensitive personal
information, and the right not to be discriminated against for exercising them.

Here is our honest position:

- **We do not collect personal information from you through the app.** There is no server, no account,
  and no user database. If you email us, the only personal information we hold is your email and your
  message.
- **We do not sell or share personal information**, including for cross-context behavioral advertising.
  There is nothing to opt out of, and no "Do Not Sell or Share My Personal Information" mechanism is
  needed, because no such activity exists.
- **Sensitive personal information:** health information is sensitive personal information under CPRA.
  We do not receive yours. We do not use it to infer characteristics about you.
- Prameya is a small publisher and likely falls below every CCPA applicability threshold. We describe
  these practices anyway so you can see what actually happens.

To make a request, email **admin@prameya.legal**. We will respond within 45 days, and we will tell you
honestly if the answer is "we hold nothing about you."

### Washington and Nevada

See the separate [Consumer Health Data Privacy Policy](https://prameyallc.github.io/privacy/omnirx/health-data/).
Washington's My Health My Data Act also allows individuals to bring their own claim through the
Washington Consumer Protection Act (RCW 19.86.090).

### Other US states

Several other states give residents rights to access, correct, delete and port personal data, and to
opt out of targeted advertising, sale and profiling. Our answer is the same everywhere: we do not
target ads, do not sell data, do not profile you, and do not hold your data. Email
**admin@prameya.legal** and we will handle your request under whichever law applies to you.

### If you are in the UK, EU, or EEA

The countries OmniRx is available in are listed on its App Store product page. This section applies if
OmniRx is available where you live:

- Health data is a special category of personal data under Article 9 of the GDPR and UK GDPR. The
  medication and wellness entries you make in OmniRx are that kind of data.
- **We are not a controller of that data in any practical sense**, because it never reaches us. It is
  created and held on your own device, under your control.
- For the one thing we do receive — support email — our lawful basis is our legitimate interest in
  answering you, or performance of a contract if your question concerns the app you installed.
- You have rights of access, rectification, erasure, restriction, objection and portability against us
  for anything we hold. Because that is limited to support email, those requests are quick to answer.
  You may also complain to your national data protection authority.

---

## Children

OmniRx is a medication education app written for adults. It is not directed to children.

- We do not knowingly collect personal information from anyone, of any age, because we operate no
  service that receives personal information.
- **There are no ads in OmniRx**, so no advertising network profiles a child through this app. This is
  the single biggest COPPA risk in consumer apps and it does not exist here.
- OmniRx's App Store age rating is shown on its App Store product page. If you are a parent or
  guardian and have a question, email **admin@prameya.legal**.

We should also say what the app does *not* implement: OmniRx does not use any platform age-signal or
age-verification API, and it has no in-app mechanism for a parent or guardian to grant or revoke
consent.

---

## Security

- Your data sits in the app's private, sandboxed storage, protected by iOS file protection and your
  device passcode or biometric lock.
- Sensitive internal values are held in the iOS Keychain and marked device-only, so they do not
  transfer to other devices.
- Preference sync uses Apple's CloudKit over HTTPS, through your own iCloud account.
- **The strongest security property of this app is architectural:** there is no server holding your
  medication history, so there is no server to breach. We make no claims about "military-grade" or
  "unbreakable" security, and we hold no certifications we have not earned.
- As noted above, the app's data store is **not** excluded from iCloud device backup, so a
  whole-device backup can include it.
- If we ever learn of a security problem that affects users, we will post a notice at
  [prameyallc.github.io/privacy](https://prameyallc.github.io/privacy/) and, where the law requires it,
  notify affected people directly.

---

## Keeping and deleting data

- Your OmniRx data stays on your device until you delete it.
- **You can delete all of it inside the app.** Settings → **"Delete all my data"** asks you to confirm,
  then permanently removes every medication log, journal entry, habit record and profile record from
  the device and resets the figures the app calculated from them back to empty. It cannot be undone.
- **This is all-or-nothing.** The app does not offer per-entry deletion or editing of past entries
  today.
- **Deleting the app deletes the data with it.** iOS removes the app's storage container.
- Because we never receive your medication or wellness data, we cannot delete it for you — and we have
  no copy to delete.
- Support emails are kept only as long as needed to resolve your question, and you can ask us to delete
  yours at any time.

---

## A note about the words "collect" and "data not collected"

Apple's App Store privacy labels use a specific definition of "collect": transmitting data off the
device so a developer or its partners can access it. Under that definition there is very little for
OmniRx's App Store label to show, because nothing you type is transmitted anywhere.

**That definition governs App Store labels only.** It does not narrow our duties under state health
privacy laws. Washington's My Health My Data Act uses a much broader definition that reaches data that
is merely accessed, processed, or derived. We do not use Apple's labeling definition to argue our way
out of those laws, and you should not read our App Store label as saying we did.

---

## Changes to this policy

If we change how OmniRx handles data, we will update this policy and change the effective date at the
top. Meaningful changes — a new network connection, a new permission, anything involving your health
data — will be described in a short summary of what changed, at the top of this page, and will be
announced in the app's release notes.

**What changed in this revision (August 8, 2026):** this version corrects statements that described
intentions rather than the code that actually ships. Specifically, we now say plainly that the app
keeps an iCloud container for non-health preferences (rather than claiming no iCloud at all) and that
nothing is currently written to it; that no health data syncs; that the app schedules no reminders or
notifications; that export displays a plain-text summary in the app rather than using a share sheet;
that deletion is all-or-nothing and there is no per-entry deletion; that there is no screen for
entering age, conditions or current medicines; that the data store is not excluded from iCloud device
backup; and that no separate AI model disclosure page exists. Internal review markers that were
mistakenly published have been removed and replaced with what the code does.

If a change would require your consent under a law that applies to you, we will ask for it before the
change takes effect, not after.

Older versions of this policy are available on request from **admin@prameya.legal**.

---

## Contact

**Prameya LLC**
Email: **admin@prameya.legal**

We answer privacy requests within 45 days.

---

## Related pages

- [OmniRx Consumer Health Data Privacy Policy](https://prameyallc.github.io/privacy/omnirx/health-data/) — required separate policy for Washington and Nevada
- [Prameya app privacy hub](https://prameyallc.github.io/privacy/) — policies for all Prameya apps
- This policy: [prameyallc.github.io/privacy/omnirx](https://prameyallc.github.io/privacy/omnirx/)

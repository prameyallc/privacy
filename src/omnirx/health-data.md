# OmniRx Consumer Health Data Privacy Policy

**Effective date:** 23 August 2026
**App:** OmniRx (iOS)
**Publisher:** Prameya LLC ("Prameya", "we", "us"), a US limited liability company
**Contact:** admin@prameya.legal

This is a **separate policy**, required by Washington's My Health My Data Act (RCW chapter 19.373) and
by Nevada's SB 370 (NRS chapter 603A). It deals only with **consumer health data** in OmniRx.

The main policy is here: [OmniRx Privacy Policy](https://prameyallc.github.io/privacy/omnirx/).
All Prameya app policies: [prameyallc.github.io/privacy](https://prameyallc.github.io/privacy/).

---

## The short version

OmniRx stores what you log about your medicines and how you feel **on your own device**. Prameya runs
no server that receives it. We do not share it. We do not sell it. Nobody at Prameya can see it. None
of it syncs to iCloud.

You can delete all of it yourself, from inside the app, in two taps: Settings → "Delete all my data".

We still treat it as consumer health data and still give you the rights below, because Washington and
Nevada define "collect" broadly enough to reach data that is processed on your device — not only data
that is sent somewhere.

---

## Why you are reading a second policy

Washington's My Health My Data Act requires a business that handles consumer health data to publish a
**distinct** consumer health data privacy policy, linked separately, that says specific things.
Nevada's SB 370 requires substantially the same. This document says those things.

We publish it even though a fair argument exists that OmniRx's data never reaches us at all. The
question of whether "collect" is triggered when a developer never receives the data has not been
settled by the Washington Attorney General or by any court. We do not want your rights to depend on how
that argument comes out.

---

## What counts as consumer health data in OmniRx

Consumer health data is personal information that identifies your past, present or future physical or
mental health status. In OmniRx that means the things you log about your medicines and your body.

### Categories collected, and why

| Category | What it is | Why the app has it | How it is used |
|---|---|---|---|
| **Medication adherence records** | Whether you marked today's dose as taken, and the date | So you can see your own pattern | Shown back to you; used to compute your adherence percentage and streak |
| **Barriers to taking medicine** | "Forgot", "Cost", "Side effect concern", "Regimen complexity", "Ran out", "Other" | So you can see what actually gets in the way | Shown back to you; used to suggest general topics to raise with your pharmacist. Selecting "Side effect concern" is also stored as a side-effect entry on that day's journal record |
| **Free-text notes** | Anything you type in the daily notes field | Your own record | Stored with both the adherence record and the journal record, and shown back to you |
| **Wellness journal** | Mood (1–5) and energy (1–5), set with steppers | Habit and wellness tracking | Averaged into descriptive trends over the last two weeks |
| **Habit records** | Whether the dose was taken on time — written from your adherence entry, not asked separately | General wellness tracking | Stored on the device; contributes to streaks |
| **Profile record** | A record the app creates on first launch holding two default goals | Personalizing your own view of your own record | Stored on the device |
| **Values the app calculates** | Adherence percentage, current streak, days logged, mood/energy average, "trends to discuss" text | Feedback on your own logging | Displayed in the app |

**Fields the app does not let you fill in.** The app's data model also contains fields for hours of
sleep, symptoms, health conditions and current medications. **No screen in the shipping app fills any
of them in.** Sleep is stored at a fixed default value you cannot set, symptoms are stored empty, and
the conditions and current-medicines fields are never written. We list them here so that this policy
describes the store honestly, not to suggest the app collects them.

**On-device AI.** The shipping app has **no** on-device model and **no** Hugging Face download.
Unused Intelligence / MLX code was deleted. If a generate feature is ever added, this policy is
rewritten first.

**Purpose, stated once and plainly:** every purpose above is *showing your own information back to you*
and *helping you prepare to talk to a pharmacist or physician*. There is no secondary purpose. We do
not use this data for advertising, marketing, profiling, product analytics, research, model training,
or any use-based data mining. There is no such use, because we never receive the data.

**We do not collect any consumer health data beyond what is listed above.** If that ever changes, we
will disclose the new category here and ask for your consent before collecting it.

---

## Subscription tiers and consumer health data

### No new collection when you subscribe

OmniRx offers paid subscription tiers (Plus and Premium) in addition to the free tier. **Upgrading does NOT trigger new consumer health data collection.**

All three tiers:
- Process the same categories of consumer health data (listed above)
- Use consumer health data for the same purpose (showing your own information back to you and helping you prepare to talk to a pharmacist or physician)
- Store data in the same location (on your device)
- Transmit data to the same recipients (none — no health data leaves your device)

**Subscription unlocks features like longer history retention and additional export formats. It does not change what data is collected, how it is processed, or where it goes.**

### What changes between tiers

| What subscription affects | What subscription does NOT affect |
|---------------------------|-----------------------------------|
| How long medication history is retained (30 days vs unlimited) | Whether medication logs are processed (yes in all tiers) |
| Which export formats are available (none, PDF/JSON, or PDF/JSON/FHIR) | Where logs are stored (on-device in all tiers) |
| Whether CloudKit syncs preferences (off, on, or on) | Whether health data syncs to iCloud (never, in any tier) |
| Whether trend analytics are shown | What the app can track or calculate |

### StoreKit data is not consumer health data

When you purchase a subscription, the app receives a transaction ID, product ID, and purchase/expiration dates from Apple's StoreKit. **These are payment records, not consumer health data** under RCW 19.373.010.

StoreKit transaction data:
- Does not identify your health status, condition, disease, or treatment
- Is used only to unlock tier-appropriate features
- Is stored locally on your device (not synced to iCloud)
- Is deleted when you use "Delete All Data"

Apple separately processes your Apple Account ID and payment method when you subscribe. That processing is governed by Apple's terms, not ours.

---

## Categories of sources

There is one source: **you**, typing into the app on your own device.

OmniRx does **not** obtain health data from:

- Apple Health or HealthKit — the app contains no HealthKit code and holds no HealthKit entitlement.
  An earlier build of the project declared HealthKit and Clinical Health Records entitlements that no
  code used; those declarations have been removed. If HealthKit is ever genuinely added, this policy
  must be rewritten and your consent obtained first;
- Clinical or electronic health records;
- Pharmacies, prescribers, insurers, or health plans;
- Data brokers, list vendors, or advertising networks;
- Other apps on your device;
- Photographs — the app has no camera or photo-library access;
- Your location — the app does not use location services at all.

---

## Categories of consumer health data shared

**None.**

OmniRx shares no consumer health data with anyone. Not with us, not with third parties, not with
affiliates, not with service providers or processors.

### List of third parties and affiliates we share consumer health data with

**None. The list is empty.**

Prameya has no affiliates. We use no processor, contractor or service provider that touches consumer
health data, because no such data reaches us.

### About network connections — so the list above is not misleading

The shipping app does not contact Hugging Face or any other third party with consumer health data.
The only optional network path is preference sync through the reader’s own iCloud account, which
does not include health records.

### About iCloud — so the same claim is not misleading either

**No consumer health data is placed in iCloud by the app.** The database holding what you log is
created local-only, with iCloud sync switched off for it.

OmniRx does retain an iCloud container reserved for ordinary app preferences. Its schema is an
allow-list containing exactly one non-health record type; your medication logs, journal entries, habit
records and profile record are excluded, a test in the codebase asserts they are absent, and the app
refuses to build the sync container at all if that ever stops being true. As the app ships today
nothing is written to that container, so nothing actually syncs.

Separately from anything the app does, Apple's whole-device **iCloud Backup** can include the app's
data if you have that turned on — see [the right to delete](#3-the-right-to-delete) below.

---

## Selling consumer health data

**We have never sold consumer health data and we will not.**

Washington and Nevada both require a specific, separate, signed authorization before consumer health
data may be sold. We have never sought one and do not intend to. If that ever changed, it would require
your explicit written authorization first — silence, an app update, or a change to this policy could
never substitute for it.

---

## Geofencing

**OmniRx uses no geofencing.** The app does not request or use location at all. It does not establish a
virtual boundary around a health care facility, or anywhere else, and it does not use location to
identify, track, collect data from, or send messages or advertising to anyone.

Washington prohibits geofencing within 2,000 feet of a facility providing in-person health care
services; Nevada prohibits it within 1,750 feet. Neither prohibition can be triggered by an app with no
location access.

---

## Who inside Prameya can see your data

**Nobody.** There is no administrative console, no support-side lookup tool, no database, and no
production access path. Your data is on your device.

If you email us for support, only the person answering support email — currently the address
**admin@prameya.legal** — sees whatever you choose to put in that email. Please do not send us your
medication history; we do not need it and would rather not have it.

---

## Your rights, and how to use them

You have these rights under Washington's My Health My Data Act (RCW 19.373.040), and comparable rights
under Nevada law. We extend them to everyone, wherever you live.

### 1. The right to confirm what we are doing

You can ask us to confirm whether we are collecting, sharing, or selling your consumer health data, and
to give you a list of all third parties and affiliates we have shared or sold it to.

Our answer, in advance: **we are not collecting it on any server, we have never shared it, we have never
sold it, and the list of third parties is empty.** Ask anyway if you would like it in writing — email
**admin@prameya.legal** and we will send it.

You can also see what the app holds without asking us: Settings → **"Open, correct or delete one
record"** lists every record the app holds and opens any of them. Settings → **"Export every record
as text"** prints all of them, field by field — each medication record with its date, medicine name,
whether you recorded it as taken or skipped, the reasons and the note on it; each journal entry with
its scores, anything reported with it and its note; each habit record; and the profile row the app
created for itself. Nothing is summarised, sampled or truncated. There are no attachments to return,
and that export says so: OmniRx cannot take or store a photograph, a scan, a recording or a file of
any kind. Settings → **"Export my logs as text"** remains available and is a shorter summary written
to be handed to a pharmacist. Nothing is uploaded and we never receive a copy.

### 2. The right to withdraw consent

You can withdraw consent to our collection and sharing of your consumer health data at any time.

In practice, you can do all of this yourself, immediately:

- **Stop logging** — the app never records anything you do not enter.
- **Delete everything you have logged** — Settings → **"Delete all my data"**. This also clears any
  leftover on-device model cache from older builds.
- **Delete the app** — this removes all of its data from your device.

You may also email **admin@prameya.legal** to withdraw consent in writing. We will confirm and record
it. Withdrawing consent does not undo processing that already happened on your own device.

### 3. The right to delete

You can ask us to delete your consumer health data.

- **You can do it now, without asking us.** Settings → **"Delete all my data"** asks you to confirm,
  then permanently removes every medication log, journal entry, habit record and profile record from
  the device and resets the figures the app calculated from them back to empty. It cannot be undone.
- **Or one record at a time.** Settings → "Open, correct or delete one record" lists every
  medication record, journal entry and habit record on the device. Each one opens, and each one
  can be deleted on its own behind a confirmation that names it — which medicine, which day,
  what was recorded on it. Medication records and journal entries can also be corrected in
  place; a habit record is written by the app from the medication record beside it, so it is
  read-only and the screen says why.
- **Deleting the app** also removes its entire data store from your device.
- **We hold no copy to delete.** There is no server database, no backup, no archive, and no analytics
  store containing your health data. When you ask, we will tell you exactly that, in writing.
- **We have not shared it with anyone**, so there is no third party for us to instruct to delete it.
- **iCloud Backup is the one copy we cannot reach and neither can the app's delete button.** OmniRx does
  not exclude its data store from iOS device backup, so if you have iCloud Backup turned on, Apple's
  whole-device backup may contain a copy of the app's data. That backup is between you and Apple; you
  can manage or delete it in your iOS settings. We have no access to it.

### 4. The right not to be discriminated against

Using any of these rights does not change the app. There is no reduced-functionality tier, no penalty,
and no different price.

### How to make a request

Email **admin@prameya.legal** with what you want. You do not need an account, because there are none.
Please tell us how to reach you.

- We respond **without undue delay and within 45 days** of receiving your request.
- If we need more time, we will tell you why within that first 45 days and may take **one additional
  45-day extension**.
- Because we hold no account, we may not be able to verify that a request relates to any particular
  person's data. Where we cannot verify, we will still tell you what we do and do not hold in general.

### If we say no

If we refuse a request, we will tell you why, and you may **appeal**. Send your appeal to the same
address with "Appeal" in the subject line. We will review it and respond in writing within **45 days**,
explaining our reasoning.

If we deny your appeal, you may submit a complaint to your state's Attorney General:

- **Washington** — the Washington State Attorney General's Office, at atg.wa.gov.
- **Nevada** — the Nevada Attorney General's Office, at ag.nv.gov.

**Washington residents:** a violation of the My Health My Data Act is a violation of the Washington
Consumer Protection Act, which gives you a private right of action under RCW 19.86.090. You do not have
to wait for the Attorney General to act.

**Nevada residents:** SB 370 is enforced by the Nevada Attorney General. It does not create a private
right of action.

---

## How long your data is kept

For as long as you keep it. It is on your device, so you decide. Deleting it in the app removes it, and
deleting the app deletes it.

We keep nothing, so there is nothing for us to retain or to age out.

---

## Consent

OmniRx collects consumer health data only when you type it in, and only for the purposes listed above.
Before the app processes your health data for any new purpose, or collects a new category of it, we
will disclose that here and ask for your affirmative consent first.

**What the app asks you at first run.** The first time you open OmniRx, before you reach the rest of
the app, it shows a disclosure screen explaining what OmniRx is, what it will not do (no diagnosis, no
dosing, no interaction checking, no pill identification), and that what you log stays on your device.
You acknowledge that screen to continue, and the app records the acknowledgement together with a
version number for the disclosure text. If we materially change what that screen says, the version
number increases and the screen is shown again, so you see the change rather than being carried past
it. The model download is a separate, later choice, made with two switches in Settings that are both
off until you turn them on.

---

## What OmniRx is not

OmniRx is educational and habit-support software. It is **not medical advice**. It does not diagnose,
does not calculate doses, does not check drug interactions, does not produce tapering plans, and does
not identify medicines from photographs. It also does not remind you to take a dose — it schedules no
reminders and sends no notifications. Talk to your pharmacist or physician about your medicines.

**HIPAA does not apply.** Prameya is not a health care provider, health plan, or business associate,
and OmniRx is not provided to you through one. We claim no HIPAA compliance. What protects your data
here is that it stays on your device — and the rights in this policy.

---

## Changes to this policy

If we change how OmniRx handles consumer health data, we will update this page and change the effective
date above, and summarize what changed at the top. We will not collect, use, or share a new category of
consumer health data, or use it for a new purpose, without disclosing it here first and obtaining your
affirmative consent.

**What changed in this revision (August 24, 2026):** the app now offers per-record review,
correction and deletion, and a complete per-field export, so sections 3 and 4 describe those
controls instead of denying they exist. This revision also adds subscription tier disclosures
(Plus and Premium tiers are now available), explaining that upgrading does not change what consumer
health data is collected, how it is processed, or where it goes. No category of consumer health data,
no source, no recipient and no purpose changed, so the effective date is unchanged and no new consent
is sought.

**What changed in this revision (August 8, 2026):** this version corrects statements so they match the
code that actually ships. In particular: the right to delete described all-or-nothing deletion only,
which was accurate for the build shipping on that date; the category table now describes only what
the app actually records, and names the fields that exist in the data model with no screen to fill
them in; the AI row now says plainly that no screen sends your text to the model today; the iCloud
position is stated exactly (no health data syncs, and a preferences-only container exists that
nothing currently writes to); the iCloud Backup limitation is stated as a limitation on deletion;
the first-run disclosure is described as it ships; and internal review markers that were mistakenly
published have been removed.

Prior versions are available on request from **admin@prameya.legal**.

---

## Contact

**Prameya LLC**
Email: **admin@prameya.legal**

---

## Related pages

- [OmniRx Privacy Policy](https://prameyallc.github.io/privacy/omnirx/) — the main policy
- [Prameya app privacy hub](https://prameyallc.github.io/privacy/)
- This policy: [prameyallc.github.io/privacy/omnirx/health-data](https://prameyallc.github.io/privacy/omnirx/health-data/)
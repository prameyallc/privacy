# OmniRx Consumer Health Data Privacy Policy

**Effective date:** 23 September 2026
**App:** OmniRx for iPhone and iPad, with its Apple Watch app, its Apple TV app, and its Mac and Apple Vision Pro versions — bundle ID `legal.prameya.OmniRx`
**Publisher:** Prameya LLC ("Prameya", "we", "us"), a US limited liability company
**Contact:** admin@prameya.legal

This is a **separate policy**, required by Washington's My Health My Data Act (RCW chapter 19.373) and
by Nevada's SB 370 (NRS chapter 603A). It deals only with **consumer health data** in OmniRx.

The main policy is here: [OmniRx Privacy Policy](https://prameyallc.github.io/privacy/omnirx/).
All Prameya app policies: [prameyallc.github.io/privacy](https://prameyallc.github.io/privacy/).

---

## The short version

OmniRx stores what you log about your medicines and how you feel **on your own device**. Prameya runs
no server that receives it. We do not share it. We do not sell it. Nobody at Prameya can see it. Your
medication records, journal entries and the list of medicines you follow do not go to iCloud.

**A few things do leave the device, and all of them go to places tied to your own Apple Account, not
to us:**

- **The IDs of the medicine-label pages you open go to your own iCloud account**, so your other
  devices, Apple Watch and Apple TV can continue where you left off and the Home Screen widget can
  suggest a next topic. A label
  page's ID includes the medicine's name (for example `metformin_what_its_label_says`), so it can show
  which medicines' labels you read. The You tab links to the label page for the first medicine you
  follow, when the library has one, so opening that link stores the ID of a label for a medicine you
  take. Handoff also tells your nearby devices which page you last opened.
- **If you turn it on, the names of the medicines you follow go to your paired Apple Watch**, to show
  on its reminder card.
- **A question you type into Ask on Apple Watch goes to your paired iPhone**, which answers it on the
  iPhone.

You can delete what you have logged yourself, from inside the app: More → "Delete all my data". It also
removes those iCloud values. Read [the right to delete](#3-the-right-to-delete) for what it does not reach.

We still treat all of this as consumer health data and still give you the rights below, because
Washington and Nevada define "collect" broadly enough to reach data that is processed on your device —
not only data that is sent somewhere.

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
mental health status. In OmniRx that means the things you log about your medicines and your body, and
the things the app keeps that could reveal which medicines you take or read about.

### Categories collected, and why

| Category | What it is | Why the app has it | How it is used, and where it goes |
|---|---|---|---|
| **Medicines you follow** | The names you type in "as on the bottle", and the names of medicines you have stopped following | So the daily check and the reminder know what to mark | Shown back to you. Kept in the app's settings storage on the device. Sent to your Apple Watch only if you turn on "Show medicine names on Apple Watch" |
| **Medication records** | The date, the medicine name, and whether you marked it Taken or Skipped | So you can see your own pattern | Shown back to you; used to compute your percentage and streak. On the device only |
| **Barriers to taking medicine** | "Forgot", "Cost", "Side effect concern", "Regimen complexity", "Ran out", "Other" | So you can see what actually gets in the way | Shown back to you and counted in the summary export. If you save a mood and energy at the same time, selecting "Side effect concern" is also stored as a side-effect entry on that journal entry. On the device only |
| **Free-text notes** | Anything you type in the notes field | Your own record | Stored with the medication record and, if you save a mood and energy, the journal entry. On the device only |
| **Wellness journal** | Mood (1–5) and energy (1–5), saved when you set both | Habit and wellness tracking | Averaged over the last 30 days and shown back to you. On the device only |
| **Habit records** | Whether the dose was taken — written from your Taken or Skipped choice, not asked separately | General wellness tracking | Stored on the device; contributes to streaks |
| **Profile record** | A record the app creates on first launch holding two default goals | Personalizing your own view of your own record | Stored on the device |
| **Label pages you opened** | The IDs of the topic and medicine-label pages you have opened from the You tab (which links to the label for the first medicine you follow), from search results in the Understand tab, from Continue, from Apple Watch or from the widget, and the one you had open last (on iPhone, iPad, Mac, Apple Vision Pro, Apple Watch or Apple TV); a label page's ID names the medicine | So your other devices, Apple Watch, Apple TV and the widget can continue where you left off | Written to your own iCloud key-value storage. Also named in the Handoff message to your nearby devices |
| **Questions you type into Ask** | A question you send in Ask, on the iPhone, iPad, Mac, Apple Vision Pro or from Apple Watch | To answer it | Answered by Apple's on-device model on the device, only if you turned Ask on. Not saved, and not sent to us or to Apple. A question typed on Apple Watch travels to your iPhone to be answered |
| **Values the app calculates** | Percentage of logged days with a dose taken, current streak, days logged, mood and energy average, one sentence describing what was logged | Feedback on your own logging | Calculated when displayed, not stored |

**Fields the app does not let you fill in.** The app's data model also contains fields for hours of
sleep, symptoms, age, health conditions and current medications. **No screen in the shipping app fills
any of them in.** Sleep is left empty, symptoms are stored empty, and the age, conditions and
current-medications fields are never written. We list them here so that this policy describes the store
honestly, not to suggest the app collects them.

**Ask and on-device AI.** Ask is off until you turn on **Enable on-device Ask** in More, and it answers
only where Apple Intelligence is turned on and ready. Before a question reaches Apple's on-device model,
the app refuses questions about doses, interactions, tapering, pill identification, diagnosis, risk
scores or your own medicines, and answers a question that suggests someone may be in danger with 988,
Poison Help and 911 instead of the model. Ask does not see your medication records, your journal or the
medicines you follow. The app downloads no model: the switch labelled "Allow one model download" only
records your choice on the device, and nothing in this version starts a download or contacts Hugging
Face.

**Purpose, stated once and plainly:** every purpose above is *showing your own information back to you*,
*letting you continue on your own devices*, and *helping you prepare to talk to a pharmacist or
physician*. There is no secondary purpose. We do not use this data for advertising, marketing,
profiling, product analytics, research, model training, or any use-based data mining. There is no such
use, because we never receive the data.

**We do not collect any consumer health data beyond what is listed above.** If that ever changes, we
will disclose the new category here and ask for your consent before collecting it.

---

## Subscription tiers and consumer health data

### No new collection when you subscribe

OmniRx offers one paid upgrade, **OmniRx Pro** (monthly, annual or lifetime), in addition to the free
tier. **Upgrading does NOT trigger new consumer health data collection.**

Both tiers:
- Process the same categories of consumer health data (listed above)
- Use consumer health data for the same purposes
- Store data in the same places (on your device, with the label-page IDs in your own iCloud account)
- Send it to the same places (your own iCloud account and, if you turn it on, your Apple Watch — never to us)

**Pro lets you follow every medicine you take instead of one, and log with no cap instead of 30 logs in
total. It does not change what data is collected, how it is processed, or where it goes.**

### What changes between tiers

| What subscription affects | What subscription does NOT affect |
|---------------------------|-----------------------------------|
| How many medicines you can follow at once (one, or any number) | Whether medication records are processed (yes in both) |
| How many dose logs you can add (30 in total, or no cap) | Where records are stored (on the device in both) |
| | What syncs to iCloud (the same in both; never your records) |
| | Reading, correcting, deleting and exporting your records (free in both, and kept if Pro lapses) |

### StoreKit data is not consumer health data

When you buy Pro, Apple's StoreKit on your device tells the app whether Pro is active. **Purchase
records are payment records, not consumer health data** under RCW 19.373.010.

StoreKit transaction data:
- Does not identify your health status, condition, disease, or treatment
- Is used only to decide whether Pro features are on
- Is held by Apple and StoreKit; OmniRx does not write its own copy and sends nothing about it to us
- Is not affected by "Delete all my data"; your purchase stays with your Apple Account

Apple separately processes your Apple Account ID and payment method when you subscribe. That processing is governed by Apple's terms, not ours.

---

## Categories of sources

There is one source: **you**, using the app on your own devices.

OmniRx does **not** obtain health data from:

- Apple Health or HealthKit — the app contains no HealthKit code and holds no HealthKit entitlement. If
  HealthKit is ever genuinely added, this policy must be rewritten and your consent obtained first;
- Clinical or electronic health records;
- Pharmacies, prescribers, insurers, or health plans;
- Data brokers, list vendors, or advertising networks;
- Other apps on your device;
- Photographs — the app has no camera or photo-library access;
- Your location — the app does not use location services at all.

---

## Categories of consumer health data shared

**None.**

Prameya shares no consumer health data with anyone. Not with us, not with third parties, not with
affiliates, not with service providers or processors.

### List of third parties and affiliates we share consumer health data with

**None. The list is empty.**

Prameya has no affiliates. We use no processor, contractor or service provider that touches consumer
health data, because no such data reaches us.

### About Apple's services — so the list above is not misleading

The app itself sends a limited set of items to services Apple runs for **your own Apple Account**.
Prameya does not receive any of it and cannot read it:

- **iCloud key-value storage** holds the IDs of the topic and medicine-label pages you opened (which
  name the medicine), the tab you last used, the next topic the widget suggests, and your appearance
  choice. Your Apple Watch and Apple TV read these values and add the ID of a page you open on them.
- **Your private CloudKit database** holds one preferences record: your appearance choice, the version
  of the first-run notice you accepted, and two settings no screen changes. It holds no health
  information: your medication records, journal entries, habit records and profile record are excluded
  by an allow-list in the code, a test asserts they are absent, and the app refuses to set up CloudKit
  if that ever stops being true.
- **Handoff** tells your nearby devices signed in to the same Apple Account which topic or label page
  you last opened — for a label page, its ID names the medicine — and, once you have opened a
  medication record, an internal reference to the last one, not its contents.
- **Your paired Apple Watch** receives the reminder card from your iPhone; it includes the names of the
  medicines you follow only if you turn on "Show medicine names on Apple Watch". A question you type in
  Ask on the Watch is sent to your iPhone to be answered.
- **Apple Intelligence**, if you turn Ask on, answers on the device; your question is not sent to Apple.

The app makes no request to Hugging Face and no request to any server of ours.

### About iCloud — so the same claim is not misleading either

**Your medication records, journal entries, habit records, profile record and the list of medicines you
follow are not placed in iCloud by the app.** The database holding the records is created with iCloud
sync switched off, and the list of medicines is kept in the app's settings storage on the device.

**The IDs of the label pages you opened are placed in iCloud by the app**, as described above, because
that is how Continue works across your devices. "Delete all my data" removes them.

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
production access path. Your data is on your device and in your own iCloud account, which we cannot
open.

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

You can also see what the app holds without asking us: More → **"Open, correct or delete one
record"** lists every medication record, journal entry and habit record the app holds and opens any of
them. More → **"Export every record as text"** prints all of them, field by field — each medication
record with its date, medicine name, whether you recorded it as taken or skipped, the reasons and the
note on it; each journal entry with its scores, anything reported with it and its note; each habit
record; and the profile row the app created for itself. Nothing is summarised, sampled or truncated.
There are no attachments to return, and that export says so: OmniRx cannot take or store a photograph,
a scan, a recording or a file of any kind. The medicines you follow are listed on the You tab rather
than in that export. The names of medicines you have stopped following are in neither: the app keeps
them on the device only so it can leave them off the You tab, and does not show them; "Delete all my
data" removes them. More → **"Export my logs as text"** remains available
and is a shorter summary written to be handed to a pharmacist. Both exports are shown on screen for you
to copy; nothing is uploaded and we never receive a copy.

### 2. The right to withdraw consent

You can withdraw consent to our collection and sharing of your consumer health data at any time.

In practice, you can do all of this yourself, immediately:

- **Stop logging** — the app never records anything you do not enter.
- **Turn off Ask**, and **turn off "Show medicine names on Apple Watch"**, in More.
- **Delete everything you have logged** — More → **"Delete all my data"**. This also removes the iCloud
  key-value values described above (not the CloudKit preferences record, which holds no health
  information), turns Ask off, and clears any leftover on-device model files from older builds.
- **Delete the app** — this removes its data from that device (see below for Mac and iCloud).

You may also email **admin@prameya.legal** to withdraw consent in writing. We will confirm and record
it. Withdrawing consent does not undo processing that already happened on your own device.

### 3. The right to delete

You can ask us to delete your consumer health data.

- **You can do it now, without asking us.** More → **"Delete all my data"** asks you to confirm, then
  permanently removes every medication record, journal entry, habit record and profile record from the
  device and resets the figures the app calculated from them. It also removes the medicines you follow
  and have stopped following, your reminder settings, your Ask switches (so Ask is off again), any
  copy of the database the app set aside after
  it could not open it, and every iCloud key-value value OmniRx writes — including the IDs of the label
  pages you opened. It cannot be undone. If a file cannot be removed, the app tells you.
- **What it does not reach:**
    - **A daily reminder that is already scheduled keeps firing.** Turn **Daily reminder** off before you
      delete, or turn off notifications for OmniRx in your device's Settings. The reminder carries no
      medicine name.
    - **Your Apple Watch** may keep showing the last reminder card the iPhone sent — with medicine names,
      if you had turned that on — until the iPhone sends a new one.
    - **The CloudKit preferences record** (appearance and notice version) stays in your iCloud account.
      It holds no health information.
- **Or one record at a time.** More → "Open, correct or delete one record" lists every
  medication record, journal entry and habit record on the device. Each one opens, and each one
  can be deleted on its own behind a confirmation that names it — which medicine, which day,
  what was recorded on it. Medication records and journal entries can also be corrected in
  place; a habit record is written by the app from the medication record beside it, so it is
  read-only and the screen says why. A medicine you follow can be removed from the You tab.
- **Deleting the app** removes its data store from an iPhone, iPad, Apple Watch, Apple TV or Apple
  Vision Pro. On a Mac, moving the app to the Trash does not by itself remove its data, so use "Delete
  all my data" first. Deleting the app does not remove the iCloud key-value values; "Delete all my
  data" does.
- **We hold no copy to delete.** There is no server database, no backup, no archive, and no analytics
  store containing your health data. When you ask, we will tell you exactly that, in writing.
- **We have not shared it with anyone**, so there is no third party for us to instruct to delete it.
- **iCloud Backup is the one copy we cannot reach and neither can the app's delete button.** OmniRx does
  not exclude its data from device backup, so if you have iCloud Backup turned on, Apple's whole-device
  backup may contain a copy of the app's data. That backup is between you and Apple; you can manage or
  delete it in your device settings. We have no access to it.

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

For as long as you keep it. It is on your device and, for the label-page IDs, in your own iCloud
account, so you decide. "Delete all my data" removes both; deleting the app removes the device copy.
A question you type into Ask is not kept at all.

We keep nothing, so there is nothing for us to retain or to age out.

---

## Consent

OmniRx collects consumer health data only when you enter it or open a page, and only for the purposes
listed above. Before the app processes your health data for any new purpose, or collects a new category
of it, we will disclose that here and ask for your affirmative consent first.

**What the app asks you at first run.** The first time you open OmniRx, before you reach the rest of
the app, it shows a disclosure screen explaining what OmniRx is, what it will not do (no diagnosis, no
dosing, no interaction checking, no pill identification), that your records stay on your device, and
that your appearance choice and the IDs of the topic and medicine-label pages you open sync through
your own iCloud account — including that a label page's ID includes the medicine's name. You
acknowledge that screen to continue, and the app records the acknowledgement, its date and a version
number for the disclosure text. If we materially change what that screen says, the version number
increases and the screen is shown again, so you see the change rather than being carried past it.

The other choices are separate and later, and each is off until you turn it on in More: **Enable
on-device Ask**, **Daily reminder** (which is when the system asks for notification permission), and
**Show medicine names on Apple Watch**.

---

## What OmniRx is not

OmniRx is educational and habit-support software. It is **not medical advice**. It does not diagnose,
does not calculate doses, does not check drug interactions, does not produce tapering plans, and does
not identify medicines from photographs. Its optional daily reminder is a local notification that says
"Reminder", with no medicine name, and it is not a critical alert. Talk to your pharmacist or physician
about your medicines.

**HIPAA does not apply.** Prameya is not a health care provider, health plan, or business associate,
and OmniRx is not provided to you through one. We claim no HIPAA compliance. What protects your data
here is that it stays on your device and in your own iCloud account — and the rights in this policy.

---

## Changes to this policy

If we change how OmniRx handles consumer health data, we will update this page and change the effective
date above, and summarize what changed at the top. We will not collect, use, or share a new category of
consumer health data, or use it for a new purpose, without disclosing it here first and obtaining your
affirmative consent.

**23 September 2026 — what changed.** This policy was rewritten to describe what OmniRx does today:

- It now says the app places the IDs of the medicine-label pages you open in your own iCloud account
  for Continue, and that a label page's ID names the medicine. Earlier versions said none of your
  consumer health data went to iCloud. "Delete all my data" removes these values.
- It adds the medicines you follow, the label pages you opened and the questions you type into Ask to
  the list of categories, and says the names of the medicines you follow go to your Apple Watch only if
  you turn that on.
- It describes Ask, which answers with Apple Intelligence on your device when you turn it on, and says
  the app still downloads no model.
- It describes the daily reminder that the app offers. An earlier line said the app schedules no
  reminders.
- It replaces the Plus and Premium tiers, which never existed, with OmniRx Pro, and removes a
  30-day history limit, export formats and preference sync by tier that the app never had.
- It no longer says the app stores your purchase details and deletes them with your data.
- It says what "Delete all my data" does not reach: an already scheduled reminder, the last reminder
  card on Apple Watch, and the iCloud preferences record.

The first-run notice, which you acknowledge before using the app, now describes the label-page IDs
in iCloud too.
Where an older entry below says something different — for example that no screen sends your text to
a model, or that nothing is written to the iCloud preferences container — this entry replaces it.

**What changed in this revision (August 24, 2026):** the app now offers per-record review,
correction and deletion, and a complete per-field export, so sections 3 and 4 describe those
controls instead of denying they exist. This revision also adds subscription tier disclosures
(it named Plus and Premium tiers, which were never offered for sale — the only paid upgrade is
OmniRx Pro; see the 23 September 2026 entry above), explaining that upgrading does not change what consumer
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

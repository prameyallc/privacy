# OmniRx Privacy Policy

**Effective date:** 24 September 2026
**App:** OmniRx for iPhone and iPad, with its Apple Watch app, its Apple TV app, and its Mac and Apple Vision Pro versions — bundle ID `legal.prameya.OmniRx`
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
- **What you log stays on your device.** The medicines you follow, your Taken and Skipped records, the reasons you record, your notes, and your mood and energy entries are stored on the device you entered them on. The app does not upload them and does not put them in iCloud.
- **Some things do go to your own iCloud account.** So your other devices, your Apple Watch and Apple TV can pick up where you left off, and the Home Screen widget can suggest a next topic, OmniRx keeps a few small values in your iCloud account: the tab you last used, and the IDs of the topic and medicine-label pages you opened. **A label page's ID includes the medicine's name** (for example `metformin_what_its_label_says`), so these values can show which medicines' labels you read — including a medicine you follow, if you open its label page from the You tab. Your appearance choice and the version of the first-run notice you accepted also sync. Prameya cannot read any of it. See [iCloud: preferences and Continue](#icloud-preferences-and-continue).
- **Ask runs on your device.** If you turn on **Enable on-device Ask** in More, Ask answers with Apple's on-device model where Apple Intelligence is turned on and ready. Where it is not, on an iPhone, iPad, Mac or Apple Vision Pro with enough memory, the Ask screen offers an optional model that runs on the device; it downloads from **Hugging Face** only if you agree in a dialog that names the model and its size. Either way your question is not sent to us, to Apple, to Hugging Face or to any other AI provider, and it is not saved. See [Hugging Face: the optional Ask model](#hugging-face-the-optional-ask-model).
- **Other paths off the device are Apple's** — the App Store for purchases, iCloud, Handoff to your nearby devices, and the connection between your iPhone and your Apple Watch — plus, only if you choose the optional Ask model, its download from Hugging Face.
- **No ads. No analytics. No trackers.** OmniRx contains no advertising SDK, no analytics SDK, and no crash-reporting SDK.
- **No camera, no photos, no microphone, no location, no contacts, no Apple Health.** The app does not ask for these and cannot use them.
- **One optional permission.** You can turn on one daily reminder in More. It is off until you turn it on, and only then does the app ask to send notifications. The lock screen says “Reminder”, not a medicine name.
- **You can delete your records from inside the app.** More → "Delete all my data". It also deletes a downloaded Ask model and resets your settings, so the first-run notice shows again. Read [Keeping and deleting data](#keeping-and-deleting-data) for the few things it does not reach.
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

OmniRx is a **medication and pharmacology education app with habit support**. It explains what FDA
labelling says about medicines in general terms, lets you follow the medicines you take by the name on
the bottle, and lets you log whether you took your doses and what got in the way.

OmniRx does **not**:

- diagnose anything;
- calculate or check doses;
- check for drug interactions;
- produce tapering or stopping plans;
- identify a pill or a label from a photograph;
- send a critical alert, or put a medicine name on the lock screen — the optional daily reminder says “Reminder”;
- give you advice about your own specific medicines.

It is not a substitute for a licensed pharmacist or physician.

---

## Subscriptions and In-App Purchases

### Available tiers

There is one paid upgrade, **OmniRx Pro**, sold as three products. Buying any one of
them grants exactly the same Pro — there are no separate feature tiers.

| Product | Price (US) | Billing |
|---|---|---|
| OmniRx Pro Monthly | $4.99 | Auto-renews monthly. 7-day free trial. |
| OmniRx Pro Annual | $29.99 | Auto-renews yearly. 7-day free trial. |
| OmniRx Pro Lifetime | $79.99 | One-time purchase. Not a subscription. |

Family Sharing is enabled on all three. Subscriptions renew until you cancel in
Settings; Lifetime is a one-time non-consumable.

**The label library is free and stays free.** Without paying anything you get the full label
library, the daily check for one medicine, up to 30 dose logs, the journal, and both exports, with
no account and no time limit. Pro lets you follow every medicine you take instead of one, and keeps
logging with no cap.

**Pro does not add cloud sync, and there is no paid iCloud option.** What syncs through iCloud is the
same on both tiers (see below), and it never includes your logs. If a subscription lapses you keep
every record you already have, and you can still read, correct, delete and export them; you cannot
add a second medicine or a 31st log until Pro is active again.

### Free vs paid tier data collection

**Both tiers process the same consumer health data** (listed in the [Consumer Health Data Privacy Policy](https://prameyallc.github.io/privacy/omnirx/health-data/)).

- **Free:** one medicine followed at a time; at most 30 dose logs in total. When you reach 30, the
  next new log is refused and the app says so. Nothing already logged is deleted or hidden.
- **With Pro:** any number of medicines, and dose logs with no cap.

In both tiers:
- Your logs and journal stay on your device
- No log or journal entry syncs to iCloud
- Nothing about your logs or your adherence is sent to Prameya
- The same iCloud Continue values and preferences sync, as described below

**Subscription unlocks features. It does not change what data is collected or where it goes.**

### Cancellation and refunds

Subscriptions are managed by Apple:
- **Cancel:** iOS Settings → your name → Subscriptions → OmniRx, or More → the subscription row in the app
- **Refund requests:** reportaproblem.apple.com

Prameya cannot cancel your subscription or issue refunds. Apple controls all billing.

### StoreKit transaction data

When you buy Pro, Apple processes the payment and keeps its own record of the transaction under
Apple's terms. StoreKit, Apple's purchase system on your device, contacts the App Store to show the
prices, to complete a purchase, and to check whether you have Pro. OmniRx asks StoreKit that question
each time it needs the answer and keeps the answer only while it is running; it does not write its own
copy of your transaction to its storage.

This data:
- Is never sent to Prameya — the app sends nothing about a purchase to us, and we never see your payment details
- Is not placed in iCloud by OmniRx
- Is used only to decide whether Pro features are on
- Is not affected by "Delete all my data", because OmniRx does not hold it; your purchase stays with your Apple Account

---

## What data OmniRx handles, and where it lives

### Data you create in the app

This table describes what the shipping app actually records:

| What | What the app records today |
|---|---|
| Medicines you follow | the names you type in "as on the bottle" (one on the free tier, any number with Pro), and the names of medicines you have stopped following |
| Medication record | the date, the medicine name, whether you marked it Taken or Skipped (or neither, if you only wrote a note), the reasons you selected, and a free-text note if you type one |
| Reasons (barriers) | "Forgot", "Cost", "Side effect concern", "Regimen complexity", "Ran out", "Other" |
| Journal entry | mood (1–5) and energy (1–5), saved only when you set both, with the same note; if you also chose "Side effect concern", it is saved on that journal entry as a reported side effect |
| Habit record | whether the dose was taken — the app writes this from your Taken or Skipped choice rather than asking you separately |
| Profile | the app creates one profile record on first launch containing two default goals. **There is no screen for entering your age, your health conditions, or a list of current medicines.** |
| Reminder settings | whether the daily reminder is on and its time, whether Apple Watch may show medicine names, and short-lived markers: a lock-screen or Watch action the app has not yet applied, a log the free tier declined, and a link to offer after you tap Skipped |
| Ask settings | whether **Enable on-device Ask** is on; your answer to the optional Ask model download and the model and version it named; a different model you chose on the Ask screen instead of the one offered first; and a marker that the app removed the switch earlier versions showed |
| The optional Ask model | if you choose to download it: the model's files (weights, tokenizer, configuration and a prompt-formatting template) and a marker that their checksums were verified. They are not your data and hold nothing you typed |
| Other settings | your appearance choice, and whether and when you accepted the first-run notice, and which version of it |
| Values the app works out from the above | a percentage of logged days with a dose recorded as taken, a current streak, the number of days logged, a mood and energy average over the last 30 days, and one sentence describing what was logged. They are calculated when shown, not stored. |

The app's data model also contains fields for hours of sleep, symptoms, age, health conditions and
current medications. **No screen fills those in today.** Sleep is left empty, symptoms are stored
empty, and the age, conditions and current-medications fields are never written. If we ever add
screens for those fields, they are consumer health data, and this policy and the Consumer Health
Data Privacy Policy will be updated before those screens ship.

Most of what you log is **consumer health data**. It is covered in detail by the separate
[Consumer Health Data Privacy Policy](https://prameyallc.github.io/privacy/omnirx/health-data/).

### Where it is stored

Medication records, journal entries, habit records and the profile record are kept on your device,
inside the app's private storage area, in a database (Apple's SwiftData) that is created with iCloud
sync switched off. On iPhone, iPad and Apple Vision Pro that database file is given the iOS file
protection class "complete unless open", so it is encrypted when closed and cannot be reopened until
the device is unlocked. On a Mac it is protected by the Mac's own disk encryption (FileVault) if you
have it on. The medicines you follow, the reminder settings and the other settings above are kept in
the app's own settings storage on the device. A downloaded Ask model is kept in the app's private
storage too, in a folder excluded from device backup. Other apps cannot read any of it. We cannot read it.

OmniRx does not store anything in the Keychain.

### iCloud device backup

**OmniRx does not exclude its data from device backup.** So if you have **iCloud Backup** turned on,
or back up your device to a computer, that backup may include the app's medication and journal data
along with everything else on your device. The one exception is a downloaded Ask model, whose folder is
excluded from backup, so it is not restored onto a new device; download it again there if you want it. That is a setting you control on your device, between you
and Apple. We do not receive it and cannot access it. If you would rather it not be backed up, you can
turn off iCloud Backup for OmniRx in iOS Settings, or turn off iCloud Backup entirely.

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

**We do not claim that OmniRx never uses the internet. It does, through Apple's services.** None of
these connections goes to a server of ours, and none of them carries your medication records, your
journal or your notes.

### iCloud: preferences and Continue

If you are signed in to iCloud, OmniRx uses two parts of **your** iCloud account. Prameya cannot open
either of them.

- **Your private CloudKit database** holds one preferences record: your appearance choice, the version
  of the first-run notice you accepted, the time it last changed, and two more settings that no screen
  in this version changes (an on-device AI flag and a text-size preference, both left off). That is
  the only kind of record OmniRx puts in CloudKit. Your medication records, journal entries, habit
  records and profile record are excluded by an allow-list in the code, a test in the codebase asserts
  they are absent, and the app refuses to set up CloudKit at all if that ever stops being true. If you
  are not signed in to iCloud, this part does not run.
- **iCloud key-value storage** holds a few small values so that your other devices, Apple Watch, Apple
  TV and the Home Screen widget can continue where you left off:
    - the tab you last used, and the ID of the last topic or label page you had open;
    - the IDs of the topic and medicine-label pages you have opened from the You tab, from search
      results in the Understand tab, from Continue, from Apple Watch or from the widget;
    - the next topic the Home Screen widget suggests from the built-in label-literacy path, and a
      topic you asked the widget to open until the app opens it;
    - your appearance choice.

    **A medicine-label page's ID includes the medicine's name**, so this storage can show which medicines'
    labels you read. It never holds the list of medicines you follow, your logs or your notes. But the
    You tab links to the label page for the first medicine you follow, when the library has one; if
    you open that link, the page's ID — which names a medicine you take — is stored here. Apple Watch
    and Apple TV also write the ID of a page you open on them.

"Delete all my data" removes every one of the key-value values above from iCloud, and deletes the
CloudKit preferences record, which iCloud then removes from your account the next time the device
syncs. See [Keeping and deleting data](#keeping-and-deleting-data).

### Handoff

On iPhone, iPad, Mac and Apple Vision Pro, OmniRx offers Handoff to your nearby devices signed in to
the same Apple Account. The Handoff message names the tab you are on and the ID of the last topic or
label page you opened — which, for a label page, includes the medicine's name — and, once you have
opened a medication record, an internal reference to the last one you opened. It does not contain the
record itself; another device cannot open a record it does not already hold. "Delete all my data"
resets it to the You tab, so it no longer names a page or a record.

### Apple Watch

The iPhone app and the Apple Watch app talk over Apple's connection between paired devices:

- The iPhone sends the Watch the reminder card: "Medication reminder", the reminder time, and Taken,
  Skipped and Snooze, plus a card that opens a general label-reading topic on the iPhone. **Medicine
  names are sent to the Watch only if you turn on More → "Show medicine names on Apple Watch"**,
  which is off until you turn it on.
- Taken, Skipped or Snooze on the Watch is sent to the iPhone. With exactly one medicine followed, the
  iPhone logs it; with more than one, the Watch tells you to mark each one on the iPhone.
- **Ask iPhone** on the Watch sends the question you type to OmniRx on your iPhone, which answers it
  the way Ask on the iPhone does and sends the answer back. If Ask is off on the iPhone, the answer
  says so. A question from the Watch never starts a model download; a downloaded Ask model answers it
  only while OmniRx is open on the iPhone, and otherwise the answer says to open it.
- The Watch keeps the reminder time for its complication, and reads the iCloud key-value values above
  to offer "Continue".

### Hugging Face: the optional Ask model

**Only if you choose it.** Where Apple Intelligence is not turned on and ready, and **Enable on-device
Ask** is on, the Ask screen can offer a language model that runs on the device. It is not part of the
app download. Tapping the offer opens a dialog that names the model, its size and Hugging Face as the
source; **nothing downloads unless you tap Download (with the size) in that dialog.** A different model
downloads only when you tap a button on the Ask screen that names it and its size.

Which model a device is offered depends on its memory; devices without Metal 3 graphics are offered none:

| Device | Model offered first | Smaller model offered if memory is short | Optional larger model |
|---|---|---|---|
| iPhone or iPad with 6 GB of memory or less, Apple TV, Apple Watch | None | — | — |
| iPhone or iPad with 8 GB; Mac with 8 GB | MiniCPM5 2B | — | — |
| iPhone or iPad with 12 GB or more; Apple Vision Pro | Gemma 4 E2B | MiniCPM5 2B | — |
| Mac with 16–18 GB | Gemma 4 E2B | MiniCPM5 2B | Gemma 4 E4B, if you choose it |
| Mac with 24 GB or more | Gemma 4 E4B | Gemma 4 E2B | — |

| Model | From Hugging Face repository (pinned commit) | Download |
|---|---|---|
| MiniCPM5 2B | `openbmb/MiniCPM5-2B-MLX` (`8a9ad753`) | about 1.4 GB |
| Gemma 4 E2B | `mlx-community/gemma-4-E2B-it-qat-4bit` (`42f62737`) | about 4.4 GB |
| Gemma 4 E4B | `mlx-community/gemma-4-E4B-it-qat-4bit` (`0f35c6f6`) | about 6.8 GB |

Before offering a download, the app checks that the device has enough free memory for the model, and
offers none when it does not. It checks again right before each load: if the model does not fit then,
it is not loaded, and where the device's row lists a smaller model, the Ask screen offers that one as a
separate download that you also choose. It checks free storage before a download. The download runs only while OmniRx is open (on iPhone, iPad and Apple Vision Pro
the screen stays on while it runs). Wi-Fi is recommended; it can use cellular data, but not while Low
Data Mode is on. A weights file that is cut off part-way starts again from its beginning.

The downloaded files are the model's weights, its tokenizer and configuration files and a
prompt-formatting template, pinned to one commit and checked against values built into the app —
every file's size before each load, and its checksum the first time the files are seen — so files that
do not match are not loaded: data the model reads, not executable code. Like any file download, the
request gives Hugging Face your device's IP address and standard request headers (including a user
agent naming OmniRx), and names the model repository, commit and files; Hugging Face handles it under its
own terms. It carries no token or account, and nothing you typed or logged. We do not receive that
request. The models' publishers, licences and pinned versions are listed in More → Legal →
Acknowledgements & Sources.

**To stop or remove it:** **Stop using the downloaded model** on the Ask screen withdraws your agreement,
stops a download in progress and unloads the model; turning **Enable on-device Ask** off does the same.
**Remove the downloaded model**, on the Ask screen or in More → Ask, deletes the files. "Delete all my
data" and deleting the app delete them too.

### StoreKit

StoreKit contacts Apple's App Store to show Pro prices, complete a purchase, restore purchases, and
check whether you have Pro. See [StoreKit transaction data](#storekit-transaction-data).

### Links you tap

A few pages link to outside websites — for example the 988 Lifeline site, PubMed, the World Health
Organization, the FDA, and Apple's subscription page. They open only when you tap them, in your
browser, and that website then handles your visit under its own terms. OmniRx sends it nothing else.

### On-device processing

Text you give the app is processed on your device, by Apple Intelligence or by the optional Ask model
you downloaded. It is not transmitted to Prameya, to Hugging Face or to any AI provider. There is no
cloud AI and no remote retrieval endpoint.

This is a real privacy benefit and we state it precisely: **your content is processed locally and is
not transmitted to us.** We do not say "nothing ever leaves the device", because the iCloud values,
Handoff and the Watch connection described above do.

### Nothing else

There is no other outbound connection in the app. No telemetry endpoint, no ad request, no attribution
call, no license check, and no download other than the optional Ask model you choose.

---

## Things OmniRx does not do

One line each, because the honest answer is short.

- **Accounts:** none. There is nothing to sign up for, and no Sign in with Apple.
- **Advertising:** none. No ad SDK is present, so no ad network receives anything about you.
- **Analytics:** none. No Firebase, no Amplitude, no Mixpanel, no custom event pipeline.
- **Crash-reporting SDK:** none. No Sentry, no Crashlytics. The app receives Apple's MetricKit
  performance and crash summaries on the device and writes them to the device's own log; it does not
  send them anywhere.
- **Tracking across apps or websites:** none. We do not use the advertising identifier and do not ask
  for App Tracking Transparency permission.
- **Selling or sharing data:** never.
- **Camera and photos:** the app has no camera or photo-library code, and asks for no such permission.
  It cannot take or read pictures.
- **Microphone:** not used, and no permission is requested.
- **Location:** not used. No geofencing of any kind, anywhere.
- **Contacts, calendars, messages:** not used.
- **Push notifications from a server:** none. The only notifications are the local reminder described below.
- **In-app purchases or payments:** OmniRx Pro, sold through Apple. See [Subscriptions and In-App Purchases](#subscriptions-and-in-app-purchases) above.
- **Data brokers:** we buy nothing and sell nothing.

### Apple Health (HealthKit)

**OmniRx does not read from or write to Apple Health.** It contains no HealthKit code, holds no
HealthKit entitlement, and declares no HealthKit usage description. If HealthKit is ever genuinely
added, this policy will be rewritten first.

### iCloud sync

**No medication record, journal entry, habit record or profile field syncs to iCloud.** The database
holding them is created with iCloud sync switched off, and the list of medicines you follow is kept in
the app's settings storage on the device. What does go to your iCloud account is described under
[iCloud: preferences and Continue](#icloud-preferences-and-continue): your appearance choice, the
notice version you accepted, and the Continue values — including the IDs of the medicine-label pages
you opened, which name the medicine.

### Reminders and notifications

**You can set one optional daily reminder in More.** It is off until you turn it on, and notification
permission is requested only then, never at launch. It is a local notification scheduled by your
device — not a critical alert, and not a push from our servers. It is titled “Reminder” and says
“Mark Taken or Skipped for today.” — no medicine name. Actions are Taken, Skipped and Snooze:

- Tapping the reminder itself only opens the app.
- With one medicine followed, Taken or Skipped logs today for it without opening the app.
- With more than one, Taken or Skipped opens OmniRx so you can mark each medicine.
- Snooze asks again in 10 minutes.
- If Taken or Skipped from the reminder or the Watch cannot be saved because the free tier's 30 logs
  are used up, a notification titled “Not saved” says so while the daily reminder is on, with no
  medicine name; after a Watch tap, the Watch also shows its own “Not saved” line.

Turning the reminder off cancels it, and so does "Delete all my data".

### Exporting your logs

Two exports, both produced on your device and displayed to you as text you can select and copy:

- More → **"Export my logs as text"** produces a plain-text **summary** of the last 30 days — a
  percentage over the days you logged, a streak, a day count, and the reasons you recorded. It is
  written to be handed to a pharmacist.
- More → **"Export every record as text"** produces every medication record, journal entry and habit
  record in the database, field by field — each medication record with its date, its medicine name,
  whether you recorded it as taken or skipped, the reasons and the note on it; each journal entry
  with its scores, anything reported with it and its note; each habit record; the medicines you
  follow and the names of medicines you have stopped following; and the profile row the app created
  for itself. Nothing is summarised, sampled or truncated. It does not include your settings or the
  iCloud values described above, and it says so.

There are no attachments to return, and the complete export says so: OmniRx cannot take or store
a photograph, a scan, a recording or a file of any kind.

Either export goes nowhere unless you copy it somewhere — at which point it is governed by whatever
app you paste it into.

---

## On-device AI: what it is and what it is not

- **Ask is off until you turn it on.** The Ask tab appears only while **Enable on-device Ask** is on
  in More and either Apple Intelligence is turned on and ready on that iPhone, iPad, Mac or Apple
  Vision Pro, or that device has the memory for the optional Ask model. Apple TV has no Ask, because
  Apple Intelligence does not run there.
- **Apple Intelligence answers first, on the device.** Ask sends your question, together with up to
  three short passages from the app's built-in label library, to Apple's on-device language model, and
  shows what it writes, labelled "Apple Intelligence". Your question is not sent to us, to Apple or to
  any other AI provider. Ask does not see your medication records, your journal or the medicines you
  follow.
- **Where Apple Intelligence cannot answer, the model you chose answers, also on the device.** If you
  downloaded the optional Ask model (see [Hugging Face: the optional Ask model](#hugging-face-the-optional-ask-model)),
  Ask gives it the same question and passages and shows what it writes, labelled with the model's name.
  Answering never downloads anything: the model answers only once its files are fully on the device.
  If neither can answer, Ask says so.
- **Before a question reaches a model, the app checks it.** A question asking for a dose, an
  interaction decision, a tapering plan, a pill identification, a diagnosis, a risk score or advice
  about your own medicines gets a fixed refusal instead. A question that suggests someone may be in
  danger or has taken too much of a medicine gets a card with 988, Poison Help and 911, and is never
  sent to a model. Before the downloaded model sees your question together with the library passages,
  the app runs the same check on that whole text; if a passage matches (a label passage can mention an
  overdose, or stopping a medicine), Ask shows the check's fixed reply instead of an answer. The
  model's answer itself is shown as it writes it; the app does not check or
  edit it (it only leaves out the downloaded model's hidden reasoning, if the model writes any), and it
  can be wrong.
- **Nothing is kept.** OmniRx does not save your questions or its answers. A conversation lives only
  on the screen and is gone when you start a new chat or OmniRx is closed. On Apple Watch, the last
  answer stays on the Watch screen until a new one replaces it or "Delete all my data" clears it.
- **The switch "Allow one model download (about 420 MB)" is gone.** Earlier versions showed it and it
  only recorded your choice; nothing downloaded. This version removes that recorded choice the first
  time it opens, and asks you again, by model name and size, before anything downloads.
- Because nothing you type or log is sent to a third-party AI provider — Hugging Face receives only the
  download request described above — Apple's requirement to name one and obtain your permission before
  sharing personal data with one does not arise.

---

## Consumer health data

The medication information, side effects, mood and energy entries you put into OmniRx are **consumer
health data** under Washington's My Health My Data Act and Nevada's SB 370 — **even though that data
never reaches us.** Those laws define "collect" broadly enough to reach data that is accessed,
processed, or derived, not just data that is transmitted somewhere.

We do not use the fact that OmniRx works on-device to argue those laws do not apply. We treat this data
as consumer health data.

**The required separate policy is here:
[OmniRx Consumer Health Data Privacy Policy](https://prameyallc.github.io/privacy/omnirx/health-data/).**
It lists the categories collected, the sources, the purposes, where the data goes (your device, and
the limited items that reach your own iCloud account and paired Apple Watch), the categories shared
with third parties (none), and how to exercise your rights, including withdrawing consent and deleting
data.

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
  and no user database. What syncs goes to your own iCloud account, which we cannot open. If you email
  us, the only personal information we hold is your email and your message.
- **We do not sell or share personal information**, including for cross-context behavioral advertising.
  There is nothing to opt out of, and no "Do Not Sell or Share My Personal Information" mechanism is
  needed, because no such activity exists. Apple (StoreKit, iCloud, Handoff) and Hugging Face (the
  optional model download) are not cross-context behavioral advertising.
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
  created and held on your own device, under your control, and the limited items described above are
  held in your own iCloud account, which we cannot open.
- For the one thing we do receive — support email — our lawful basis is our legitimate interest in
  answering you, or performance of a contract if your question concerns the app you installed.
- If you choose to download the optional Ask model, that download is a connection from your device to
  Hugging Face, which may be outside your country. It carries your IP address, standard request headers
  and the names of the files requested, and nothing you typed or logged. We do not receive it.
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

- Your records sit in the app's private, sandboxed storage. On iPhone, iPad and Apple Vision Pro the
  database file is encrypted when closed and cannot be reopened until the device is unlocked; on a
  Mac it relies on the Mac's disk encryption. Use a passcode and keep your software up to date.
- iCloud sync, Handoff, the Watch connection and StoreKit are Apple's services and run over Apple's
  encrypted connections, through your own Apple Account. The optional Ask model downloads over an
  encrypted (HTTPS) connection, and its files are checked against values built into the app before
  they load.
- **The strongest security property of this app is architectural:** there is no server holding your
  medication history, so there is no server to breach. We make no claims about "military-grade" or
  "unbreakable" security, and we hold no certifications we have not earned.
- As noted above, the app's data is **not** excluded from device backup, so a whole-device backup can
  include it.
- If we ever learn of a security problem that affects users, we will post a notice at
  [prameyallc.github.io/privacy](https://prameyallc.github.io/privacy/) and, where the law requires it,
  notify affected people directly.

---

## Keeping and deleting data

- Your OmniRx data stays on your device until you delete it.
- **You can delete your records inside the app.** More → **"Delete all my data"** asks you to confirm,
  then permanently removes every medication record, journal entry, habit record and profile record
  from the device and resets the figures the app calculated from them. It also removes the medicines
  you follow and have stopped following, your reminder settings, the Ask switch and your answer to
  the Ask model download (so Ask is off again afterwards), any Ask model you downloaded, and any copy
  of the database that the app set aside after it could not open it. It resets your appearance choice
  to follow the system, turns "Show medicine names on Apple Watch" off, and clears your acceptance of
  the first-run notice, so the notice shows again; when you accept it again, a device signed in to
  iCloud writes a new preferences record holding the notice version (and the appearance, now following
  the system), as a first launch does. It removes every iCloud key-value value OmniRx writes and
  deletes the CloudKit preferences record, which iCloud removes from your account the next time the
  device syncs. It cancels the daily reminder (and a snoozed one), resets the Handoff message, clears
  the last Ask answer on your Apple Watch and sends the Watch a new reminder card, which names no
  medicine because none is followed any more. It cannot be undone. If a file or the preferences record
  cannot be removed from the device, the app tells you rather than claiming a complete delete.
- **What "Delete all my data" does not reach, stated plainly:**
    - **The CloudKit preferences record, if the device is not signed in to iCloud** when you delete:
      the app cannot reach it then. Sign in and delete again, or remove it with Apple's own controls
      (iOS Settings → your name → iCloud → Manage Account Storage).
    - **Your Apple Watch** gets the new reminder card, and loses its last Ask answer, straight away if
      it is connected to your iPhone, or the next time it connects. Until then it shows the last card
      and the last Ask answer it received.
    - **Your purchase** stays with your Apple Account.
- **You can also delete or correct one record at a time.** More → "Open, correct or delete
  one record" lists every medication record, journal entry and habit record on the device. Each
  opens; each can be deleted on its own behind a confirmation that names it. Medication records
  and journal entries can be corrected in place — the date cannot, because the app can only
  write a record for today. Habit records are written by the app from the medication record
  beside them, so they are read-only and the screen says why; they can still be deleted. A medicine
  you follow can be removed from the You tab.
- **Deleting the app** from an iPhone, iPad, Apple Watch, Apple TV or Apple Vision Pro removes its data
  from that device. On a Mac, moving the app to the Trash does not by itself remove its data, so use
  "Delete all my data" first. Deleting the app does not empty your iCloud account: the key-value values
  and the preferences record stay until you delete them as described above.
- Because we never receive your medication or wellness data, we cannot delete it for you — and we have
  no copy to delete.
- Support emails are kept only as long as needed to resolve your question, and you can ask us to delete
  yours at any time.

---

## A note about the words "collect" and "data not collected"

Apple's App Store privacy labels use a specific definition of "collect": transmitting data off the
device so a developer or its partners can access it. Under that definition there is very little for
OmniRx's App Store label to show, because nothing you type is transmitted to us or to a partner of ours.

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

**24 September 2026 — what changed.** With an app update:

- **Ask can use an optional on-device model.** Where Apple Intelligence is not turned on and ready, the
  Ask screen can offer a model that runs on the device, chosen by the device's memory (MiniCPM5 2B,
  Gemma 4 E2B or Gemma 4 E4B), which downloads from Hugging Face only after you agree in a dialog that
  names the model and its size. This page now names Hugging Face, the repositories, the pinned commits,
  the sizes, what the download request carries, the checks the app makes, and how to stop or remove the
  model. Earlier versions said there was no model download and no Hugging Face request, which was true
  of those versions.
- **The switch "Allow one model download (about 420 MB)" is gone.** It recorded a choice and downloaded
  nothing; the app removes that recorded choice and asks again before any download.
- **"Delete all my data" does more.** It now also resets your appearance choice, turns "Show medicine
  names on Apple Watch" off and clears your acceptance of the first-run notice, so the notice shows
  again; accepting it again writes a new iCloud preferences record, as a first launch does. Earlier,
  those three settings stayed on the device. It deletes a downloaded Ask model too, as it already
  deleted model files before.
- Because the first-run notice now mentions the model download and what Delete all resets, the app
  shows it again.

**23 September 2026 — what changed.** This policy was rewritten to describe what OmniRx does today:

- It now says that OmniRx keeps Continue values in your own iCloud key-value storage — the tab you last
  used and the IDs of the topic and medicine-label pages you opened, which name the medicine — and that
  "Delete all my data" removes them. Earlier versions said nothing you type goes to iCloud and did not
  mention these values.
- It now says your appearance choice and the notice version you accepted sync through your private
  CloudKit database. Earlier versions said nothing was written there.
- It describes Ask, which uses Apple Intelligence on your device when you turn it on, and says there
  is still no model download. Earlier versions said the app had no on-device AI.
- It covers the Apple Watch, Apple TV, Mac and Apple Vision Pro versions, Handoff, and the optional
  medicine names on Apple Watch.
- It describes the reminder as it works now: off until you turn it on, and with several medicines its
  Taken and Skipped open the app instead of logging.
- It corrects the free tier: one medicine and 30 dose logs in total, not a 30-day history, and there is
  no refill field.
- It no longer says the app stores your purchase details and deletes them with your data: the app
  keeps no copy, and your purchase stays with Apple. It no longer says the app uses the Keychain.
- It says what "Delete all my data" does not reach: a few settings on the device, what Apple Watch
  shows until it next connects to your iPhone, and your purchase.
- Later on 23 September, with an app update, "Delete all my data" does more: it also cancels the daily
  reminder, deletes the preferences record from your iCloud account, resets the Handoff message, clears
  the last Ask answer on Apple Watch, and sends the Watch a new reminder card with no medicine names.
  Before that update, an already scheduled reminder kept firing and the preferences record stayed in
  iCloud after a delete.
- With the same update, "Export every record as text" also lists the medicines you follow and the
  names of medicines you have stopped following. Before, it left them out while saying it was
  everything the app held.
- With the same update, the app's first-run notice and More no longer say we receive a transaction
  identifier when you buy Pro. As this policy says, nothing about a purchase is sent to us. Because
  the notice changed, the app shows it again.

**What changed on 27 August 2026 (corrects the entry below):** the Plus and Premium tiers described
in the 26 August entry were never offered for sale. OmniRx has one paid upgrade, OmniRx Pro, sold as
monthly $4.99, annual $29.99 or lifetime $79.99 — see "Available tiers" above. The prices quoted in
the 26 August entry ($9.99/$99 and $19.99/$199) were never charged to anyone. Nothing about data
handling changed with this correction: medication logs remain on-device only, paid or not.

**What changed in this revision (26 August 2026):** this revision added subscription disclosures.
⚠️ It described a two-tier Plus/Premium catalogue that was never shipped; see the 27 August entry
above for what is actually sold. What it said about data was and remains correct: a subscription
unlocks features but does not change what consumer health data is collected or where it goes, and
medication logs remain on-device only. The "In-app purchases or payments" line was updated to
reflect that subscriptions are available.

**What changed in the 23 August 2026 revision:** short and long versions now agree. Settings
offers one optional daily reminder (lock screen says "Reminder"). There is no Hugging Face / on-device
model download in the shipping app. The 8 August 2026 sentences that said the app "schedules no
reminders" were wrong for this binary and are removed.

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

# OmniCadence — Privacy Policy

**Effective date:** 23 September 2026
**Last updated:** 23 September 2026  
**Publisher:** Prameya LLC (“Prameya”, “we”, “us”)  
**App:** OmniCadence (called OmniOps in earlier versions of the app and of this policy) for iPhone, iPad, Mac and Apple Vision Pro, with an Apple Watch app and an Apple TV app — bundle ID `legal.prameya.OmniOps` (the Apple TV app uses the same ID; the Apple Watch app is `legal.prameya.OmniOps.watch`)  
**Contact:** admin@prameya.legal  
**Scope:** This policy covers the OmniCadence app on every device listed above, its Home Screen widget and its Apple Watch complications, and nothing else. Prameya's other apps have their own policies, because they work differently. Index: <https://prameyallc.github.io/privacy/>  
**Canonical public URL (slug stays `omniops`):** <https://prameyallc.github.io/privacy/omniops/>

This policy describes **the app you actually install** — what the shipping build does, not what
an earlier plan for it said. The version it replaces (last updated 26 August 2026) said the app
opened no network connections, used no iCloud, sent no notifications and had no model download.
The app can now do all of those things, as described below; the "what changed" entry in §10 lists
each correction.

---

## The short version

**The app sends Prameya nothing.** There is no account, no sign-in, no analytics SDK, no
advertising SDK, no third-party crash reporter, and no server of ours that receives
anything. The only information about the app that reaches us is what Apple itself reports to
developers (App Store statistics, and crash reports if you share them with developers); see §3.

**Your journal lives on your device.** The four logs (work, decisions, reflections, habits),
your notes and your review cadences are stored in the app's own storage.

**iCloud sync is off until you turn it on.** On iPhone, iPad and Mac, More ▸ iCloud ▸
**Sync with iCloud** keeps a short headline of each journal entry (for example its date, title
and ratings — never its notes) in your own iCloud private database, so your devices show the
same journal. See §4.

**A few small iCloud items are kept whenever you are signed in to iCloud,** even with sync
off: which tab and which reading you last opened, the ID number of an entry you were
editing or pinned, your appearance choice and the Home Screen widget's state. They contain
no journal text. See §4.

**Ask answers on your device.** The Ask tab appears only where Apple Intelligence is turned
on and ready, and Apple's on-device model answers first. If it cannot, Ask can use an optional
model that is downloaded from Hugging Face **only after you choose to download it**. Your
question is never sent to us or to any server.

**Notifications only if you turn them on.** On a new install, reminders are off until you
switch them on in More.

**No health data. No HealthKit.** The app does not request HealthKit permission, does
not declare HealthKit entitlements, and contains no HealthKit code.

The app has five tabs (You / Understand / Do / Ask / More); Ask is shown only where Apple
Intelligence can answer. The disclaimer (educational + habit support; not consulting / audit /
certification) is shown on the first-run screen and in More ▸ Legal ▸ Legal & Safety.
Understand reads knowledge packs that ship inside the app. Do writes your journal on the device.

---

## Available tiers

There is one paid upgrade, **OmniCadence Pro**, sold as three products. Buying any one of
them grants exactly the same Pro — there are no separate feature tiers.

| Product | Price (US) | Billing |
|---|---|---|
| OmniCadence Pro Monthly | $5.99 | Auto-renews monthly. 7-day free trial for accounts Apple offers it to. |
| OmniCadence Pro Annual | $39.99 | Auto-renews yearly. 7-day free trial for accounts Apple offers it to. |
| OmniCadence Pro Lifetime | $99.99 | One-time purchase. Not a subscription. |

Family Sharing is enabled on all three. Subscriptions renew until you cancel in
Settings; Lifetime is a one-time non-consumable.

**The journal is free and stays free.** Without paying anything you get the knowledge
packs, all four logs unlimited, the streak and consistency score, Ask, iCloud sync and raw
JSON export, with no account and no time limit. Pro adds review analytics, review cadences
you set (weekly, monthly or quarterly, with optional reminders), Markdown export and the
formatted review PDF.

**iCloud sync is not a paid feature.** It is free, optional and off until you turn it on,
whether or not you buy Pro. If a subscription lapses you keep your own data and can still
export it in its raw form; only the Pro tools stop.


## Free vs paid tier data collection

**OmniCadence is free to use**, and buying Pro does not change what data Prameya collects. Free and Pro alike:

- Your journal (work, decisions, reflections, habits) is stored on your device, and — only if you turn on iCloud sync — each entry's headline is kept in your own iCloud private database
- No analytics, tracking, or telemetry sent to us or to anyone else
- No server of ours that receives your content
- No account or login

The difference is **which tools you get**, not data handling. All four logs, the streak and raw JSON export are free; Pro adds review analytics, review cadences, Markdown export and the review PDF. Neither tier sends anything to Prameya.

## Cancellation and refunds

Subscriptions are managed entirely through your Apple ID:

- **To cancel:** Open Settings on your iPhone or iPad → tap your name → Subscriptions → OmniCadence → Cancel Subscription. On Mac, open the App Store app → Account (sign-in name) → View Information → Subscriptions → Manage. On Apple Vision Pro, open Settings → your name → Subscriptions → OmniCadence → Cancel Subscription. A subscriber can also open these from More ▸ OmniCadence Pro ▸ **Manage subscription**.
- **Refund requests:** Handled by Apple, not Prameya. See [reportaproblem.apple.com](https://reportaproblem.apple.com/) or contact Apple Support. We have no access to your payment information and cannot issue refunds ourselves.
- **What happens to your data when you cancel:** Nothing. Your journal stays on your device (and its headlines stay in your iCloud, if you turned sync on). Cancelling removes the Pro tools; it does not delete your journal entries, decisions or reflections, and it does not lock you out of your own records. Every log stays readable and raw JSON export stays available, because those are free.

## StoreKit transaction data

StoreKit on your device checks with Apple which OmniCadence Pro products you own. From that
answer the app keeps one small record in its own settings on your device: whether you have
Pro, when a subscription runs until, and whether a free trial is running. It uses that record
to decide which tools to unlock. The app does not store a transaction ID, sends nothing about
a purchase to Prameya, and the record is deleted when you delete the app (on Mac, when you also
remove the sandbox container at `~/Library/Containers/legal.prameya.OmniOps`).

If you restore purchases (by tapping "Restore Purchases" in the app), or redeem an offer code,
StoreKit talks to Apple's servers. That communication is between your device and Apple; Prameya
is not involved and sees nothing from it. Apple keeps its own record of the transaction under
Apple's terms.

---

## 1. Who publishes this

Prameya LLC. Privacy contact: **admin@prameya.legal**.

---

## 2. What the app stores on your device

The app writes a journal when you log work, a decision, a reflection or a habit, or set up
and complete a review cadence. That journal is one JSON file in the app's Application Support
folder. On iPhone, iPad and Apple Vision Pro that folder is protected so its files cannot be
read while the device is locked (except a file the app already had open when it locked). On
Mac the files sit inside the sandboxed app container and are covered by FileVault if it is
on. There is no Keychain write.

| What | Where |
|---|---|
| Your journal: each entry's date and notes; for work, the title, category, minutes spent and impact; for decisions, the title, framework, revisit note and optional dollar note; for reflections, the area and two 1–5 ratings; for habits, the habit type, completion and minutes; plus your review cadences (name, interval, due date, reminder switch) and completed reviews with what you wrote in them | **On this device**, Application Support folder |
| Sync bookkeeping inside the journal file: when each entry last changed, and which entries were deleted and when | **On this device**, in the journal file (kept whether or not sync is on) |
| Which readings you have opened | **On this device**, next to the journal |
| The journal as it was just before your last import | **On this device**, next to the journal |
| With iCloud sync on: a copy of the synced headlines, kept by Apple's iCloud sync | **On this device**, in the app's storage, and in your iCloud (see §4) |
| Settings: first-run acknowledgement and the date you gave it, appearance, whether Ask answers are on, your Ask-model choice with the model and version it was given for, which model was selected, whether reminders are on, whether iCloud sync is on (and whether it was ever on, and any removal still waiting to reach iCloud), your Pro status | **On this device**, the app's settings |
| A one-time marker that model files left by earlier versions were removed, and how much space that freed | **On this device**, the app's settings |
| The optional Ask model's files, only if you chose to download them (see §4) | **On this device**, the app's Caches folder, excluded from backups |
| An export you asked for | **On this device**, a temporary folder excluded from backups, only while More is on screen |
| Analytics identifiers | **None** |

**Performance reports.** At launch on iPhone, iPad, Mac and Apple Vision Pro the app registers
with Apple's MetricKit. When the operating system delivers its daily performance and diagnostic
summaries, the app writes a short line to the device's own system log: average launch and hang
times, disk writes, and counts of crashes, hangs and abnormal exits. Those numbers are computed by
the operating system and contain nothing you typed. The app does not send them anywhere.

**Export and sharing.** Every export is a file or text you choose to share (Share sheet).
**Export my journal** (free) writes the whole journal as JSON — including notes, revisit notes
and dollar notes. **Export to Markdown** and **Export review PDF** (Pro) write formatted
copies. **Share this decision** hands one decision's title, date, framework, revisit note and
notes to the Share sheet as text. Files are written only when you tap, into a temporary folder
of their own that is excluded from backups, and deleted when you leave the More screen; any
left over are cleared the next time More opens. Exports no longer carry the disclaimer text.

**Import** replaces the on-device journal with a previously exported file you choose (on
iPhone, iPad, Mac and Apple Vision Pro). It asks you to confirm first; the journal it replaces
is kept as the pre-import copy; a file that does not decode as an OmniCadence export is refused
and the journal is not changed. On Mac the app can read only the file you pick.

**Backups.** If iCloud Backup or a computer backup is on, Apple's device backup may include
the journal and settings. That is Apple's processing, not ours. The downloaded Ask model and
export files are excluded from backups.

**Erase.** More ▸ Journal ▸ **Erase journal and iCloud data**, after you confirm, deletes the
journal, the pre-import copy and the list of readings opened on this device; removes the iCloud
key-value items described in §4; and, if iCloud sync was ever turned on on this device, deletes
the synced headlines from your iCloud and turns sync off here. Another device that still syncs
keeps its own entries and can upload them again. Erase does not delete the downloaded Ask model
(More ▸ Ask model ▸ **Remove the downloaded model** does), your settings or your Pro status.
Using the app after Erase writes the key-value items again.

**Deleting the app** removes the container on iPhone, iPad and Apple Vision Pro, including
the journal and any downloaded model. On Mac the sandbox container under
`~/Library/Containers/legal.prameya.OmniOps` outlives the app and has to be removed
separately. Deleting the app does not remove anything the app put in your iCloud; use Erase
first if you want that gone.

### Apple Watch

The Apple Watch app has three tabs. **Now** shows three prompts ("Review today's habit",
"Write one line", "Pin last decision"); your iPhone sends their current wording over Apple's
connection between the two devices, and the habit prompt can name today's open habit type.
Tapping **Confirm** sends the choice to the iPhone, which marks today's habit done (adding a
completed habit entry if there is none for today), adds a work entry titled "Logged block", or
pins your newest entry (its ID is kept in the iCloud key-value items). **Snooze** and
**Decline** are sent too and change nothing. **Learn** shows the knowledge packs that ship
with the Watch app and offers to continue the reading you last opened, read from the iCloud
key-value items; the complications show that reading's ID or a fixed prompt. **More** shows the
disclaimer. The Watch keeps no journal, has no Ask and sells nothing.

### Apple TV

The Apple TV app shows the knowledge packs that ship with it (Library) and offers to continue
the reading you last opened on another device (Continue), read from the iCloud key-value items.
It keeps no journal, has no Ask, sends no notifications and sells nothing.

### Home Screen widget and Shortcuts

On iPhone and iPad the Home Screen widget shows a fixed "Log a decision" prompt. The widget and
the "Log a decision" shortcut (Siri and Shortcuts) open the decision form; to do that they
leave a one-word "open the decision form" note in the iCloud key-value items, which the app
clears when it opens. Neither shows journal content.

### Reminders

More ▸ Reminders ▸ **Daily reminders** is off on a new install. Turning it on (or turning on a
review cadence's reminder, below) is what asks the system for permission to send notifications
(the system asks only if you have not answered before). If you allow it, the app schedules two
local notifications a day: "Review today's habit" at 8 AM and "Write one line" at 8 PM. Their
**Confirm** button marks today's habit done or adds a "Logged block" work entry, as on the
Watch; **Snooze** schedules one reminder again later; a plain tap opens the matching form and
writes nothing. With Pro, each review cadence has its own reminder switch, off by default; a
cadence reminder arrives at 9 AM on its due day and names only the interval ("Weekly review
due"), never your own words. All reminders are scheduled and delivered by the device itself; nothing is sent to
us or to any server. Turning the switch off removes them. An installation that already had
notification permission from an earlier version keeps its reminders on until you turn them off.

---

## 3. What the app does not do

Checked against the app's source, entitlements, Info.plist and privacy manifests:

- ❌ **No HealthKit.** No HealthKit permission, no usage description, no health-records entitlement.
- ❌ **No analytics, advertising, third-party crash reporting, or tracking.** No ATT prompt,
  no advertising identifier. (MetricKit summaries stay in the device's own log; see §2.)
- ❌ **No account, Sign in with Apple, or server login.**
- ❌ **No location, camera, microphone, photos, contacts or calendar.** Notifications only
  if you turn reminders on. File access only to a file you pick for import.
- ❌ **No push notifications.** The app has no push entitlement and no background mode;
  iCloud changes from your other devices arrive when you open the app.
- ❌ **No sale or share of personal information** — we hold none.
- ❌ **HIPAA does not apply** (not a covered entity, no PHI).

**What Apple tells us.** Apple gives every developer aggregate App Store statistics (such as
downloads, sales and crash counts) that do not identify you. If you have turned on **Share With
App Developers** in your device's Analytics & Improvements settings, Apple may also give us
crash and performance reports from your device through App Store Connect. That is Apple's
system, run under Apple's terms and your setting; the reports contain technical information,
not your journal, and the app's own code does not send them.

`PrivacyInfo.xcprivacy` declares no tracking, no tracking domains and no collected data types.
It declares two required-reason APIs: the app's own settings (UserDefaults, reason CA92.1) and
the free disk space check made before the optional model download (reason E174.1). The Watch,
Apple TV and widget manifests declare no tracking and no collected data types. Apple's App
Privacy label is answered in App Store Connect under Apple's own definition of "collect"; that
definition does not narrow anything in this policy.

---

## 4. Network

**Prameya runs no server, and the app never contacts one of ours.** Everything that leaves
your device goes to Apple, or — only if you choose the optional model download — to Hugging
Face:

1. **Apple iCloud** — the journal headlines if you turn on sync (iPhone, iPad, Mac), and the
   small key-value items whenever you are signed in to iCloud (iPhone, iPad, Mac, Apple Watch,
   Apple TV, and the widgets).
2. **Handoff** — where you left off, to your nearby devices signed in to the same Apple Account.
3. **Apple Watch** — the connection between your iPhone and your paired Watch.
4. **The App Store** — StoreKit purchases, restores, offer codes and subscription checks.
5. **Hugging Face** — the optional Ask model download, only after you choose it.
6. **Links you tap** — for example "Open the source" under a reading or in Acknowledgements &
   Sources, Support, Email support, the privacy policy, the Terms of Use and Apple's pages. They
   open in your browser or Mail app, which contacts that site the way any visit does.

Apple Intelligence runs on your device; Ask sends nothing to Apple.

The Apple Vision Pro build carries no iCloud entitlement: it does not sync journal headlines
and does not exchange the key-value items through iCloud.

### iCloud sync of journal headlines (optional)

More ▸ iCloud ▸ **Sync with iCloud** appears on iPhone, iPad and Mac and is off on a new
install. When you turn it on, the app keeps one record per journal entry in your **CloudKit
private database** (container `iCloud.legal.prameya.OmniOps`), under your Apple Account.
Each record holds the entry's ID and which log it belongs to, when it last changed, and only
these fields:

- **Work:** date, title, category, minutes spent (if recorded)
- **Decision:** date, title, framework (if recorded)
- **Reflection:** date, area, and the two 1–5 ratings (effectiveness, energy)
- **Habit:** date, habit type, whether it was completed

Notes, the decision's revisit note and dollar note, work impact, habit minutes, review cadences
and completed reviews are never synced; they stay on the device where you wrote them. A second
device that syncs adds the headlines to its own journal. When an entry changes on two devices,
the newest change wins; deleting an entry leaves a deletion marker in iCloud (the entry's ID,
which log, and when — no content) so the deletion reaches your other devices. Changes from
another device arrive when you open the app or bring it to the front.

Turning sync off asks whether to keep the synced copy in iCloud for your other devices
(**Turn Off**) or delete it (**Turn Off and Remove from iCloud**). Either way the journal on
the device stays, and another device that still syncs can upload its own entries again. Erase (§2) also deletes the synced copy if this device ever turned sync on.
If a removal cannot reach iCloud at once, the app tries again the next time it opens.
Prameya cannot open your private database.

### iCloud key-value items

Whenever you are signed in to iCloud — whether or not sync is on — the app keeps a few small
items in Apple's iCloud key-value store for this app, so your devices, your Apple Watch, your
Apple TV and the widget can pick up where you left off:

- which tab you last opened, the ID of the knowledge pack you last opened, and — when you were
  editing an entry — that entry's ID number, with the time these were saved;
- the ID number of the entry you pinned from Apple Watch;
- your appearance choice (light, dark or system);
- the Home Screen widget's state (the fixed "Log a decision" prompt) and a one-word note that
  the widget or the shortcut asked to open the decision form.

These items contain no titles, notes or other journal text. **Turn Off and Remove from iCloud**
does not remove them; Erase does (§2).

### Handoff

On iPhone, iPad, Mac and Apple Vision Pro the app tells your nearby devices signed in to the
same Apple Account where you left off — the same tab, pack ID and entry ID as above — so they
can offer to continue. This goes through Apple's Handoff.

### Ask and the optional on-device model

Ask builds one message from your question, passages from the knowledge packs that match it,
and — on iPhone, iPad, Mac and Apple Vision Pro — the titles of up to four recent work entries
and four recent decisions (titles only; never notes, revisit notes or dollar notes). That message
goes to a language model **running on your device**:

- **Apple Intelligence first.** The Ask tab is shown only where Apple Intelligence is turned on
  and ready and More ▸ **On-device answers** is on (it is on unless you turn it off). Apple's on-device model answers; nothing is
  sent to Apple or to us.
- **If Apple Intelligence cannot answer a question,** Ask shows the matching passage from a
  knowledge pack, labelled as quoted. On a device that is offered a model, Ask also asks once
  whether to download it; the alert names the model's size and says it comes from Hugging Face.
- **The optional model.** Which one, if any, depends on the device:
  - **iPhone and iPad with 12 GB of memory or more, and Apple Vision Pro:** the standard
    on-device model, **Gemma 4 E2B**, from the Hugging Face repository
    `mlx-community/gemma-4-E2B-it-qat-4bit` at commit `42f62737`, about 4.4 GB.
  - **Mac with 16–18 GB of memory:** Gemma 4 E2B as above; More ▸ Ask model also offers the large
    on-device model, **Gemma 4 E4B** (`mlx-community/gemma-4-E4B-it-qat-4bit` at commit
    `0f35c6f6`, about 6.8 GB), as a separate download you choose.
  - **Mac with 24 GB of memory or more:** Gemma 4 E4B, about 6.8 GB. If the memory check refuses
    it, Ask offers Gemma 4 E2B instead, as a separate download that you also choose.
  - **iPhone and iPad with 8 GB of memory or less, Macs with 8 GB, and devices whose graphics
    hardware does not support Metal 3** are offered no model. When Apple Intelligence cannot
    answer, Ask quotes the matching knowledge pack. Apple Watch and Apple TV have no Ask.

Nothing is downloaded until you choose **Download** in Ask or turn on More ▸ Ask model ▸
**On-device Ask model**. Before offering the download, and again before loading the model, the
app checks that the device has enough free memory; before downloading it checks free disk
space. The download runs only while the app is open and in front, and while it runs the app
keeps the screen from locking on iPhone, iPad and Apple Vision Pro. It may be downloaded again
if the system clears storage space. The files are the model weights, their index, the tokenizer,
configuration files and a prompt-formatting template, pinned to one version, checked by size and
checksum after the download and by size before each load: data the model reads, not executable
code. A model answer that
fails the app's checks (cut off, garbled or empty) is replaced by the quoted pack passage.
**Remove the downloaded model** in More ▸ Ask model deletes the files and turns the switch off.
Earlier versions could download a different model (Qwen3 0.6B) from Hugging Face without asking;
this version deletes any of those files on its first launch.

Your questions and Ask's answers are not saved; they disappear when you start a new chat or
close the app.

### What Hugging Face sees

Like any file download, the request to Hugging Face (huggingface.co, and the Hugging Face
file-delivery hosts it redirects to) gives Hugging Face the device's IP address and the standard
request headers (which name the app and its version and the operating system version), and names
the model repository, version and files requested. Hugging Face handles it under its own terms.
It does not include your question, your journal or anything you type. We do not receive that
request.

---

## 5. Knowledge packs

The knowledge packs on Understand ship inside the app (and inside the Apple Watch and Apple TV
apps). The app does not fetch packs from the network. Opening a pack is recorded only on your
device (§2) and, as the last pack opened, in the iCloud key-value items (§4). Tapping **Open the
source** under a reading opens the cited public page in your browser.

---

## 6. Monetization

OmniCadence presents a StoreKit paywall for OmniCadence Pro (monthly $5.99, annual $39.99,
lifetime $99.99 — see "Available tiers" above). Apple processes the purchase. The app sends
nothing about a purchase to Prameya, and we receive no name, no email, no payment card details
and no Apple Account credentials.

The journal is free. All four logs, the streak, Ask, iCloud sync and raw JSON export cost
nothing and have no time limit.

---

## 7. Children

OmniCadence is a general-audience adult tool. It is not in the Kids Category. We do not
knowingly collect information from anyone, including children: the app sends us nothing.

---

## 8. Your rights

There is nothing of yours on our servers to access, correct, or delete. What the app keeps is
on your device and, if you use iCloud, in your own iCloud under your Apple Account. More ▸
Journal ▸ **Erase journal and iCloud data** deletes both (§2); deleting the app removes the
on-device container (on Mac, also remove the sandbox container named above) but not your
iCloud copy. Rights under the GDPR / UK GDPR / CCPA-CPRA are exercised on your device; if
you believe we hold something, write to the contact in §1.

Apple (StoreKit, iCloud, Handoff) and Hugging Face (the optional model download) receive what
§4 describes under their own terms; we do not direct them and do not receive it.

We do not respond to “Do Not Track” signals, because we do not track.

---

## 9. What this app is not

The first-run screen and More ▸ Legal ▸ Legal & Safety render, verbatim:

> EDUCATIONAL + HABIT SUPPORT ONLY. NOT MEDICAL/FINANCIAL/LEGAL ADVICE. Does not replace
> licensed pros. On-device models limited. Consult pros.
>
> OmniCadence supports your own process journal and improvement habits. It is not management
> consulting, not an audit, and not a conformity assessment or certification against any
> management-system standard.

OmniCadence does not ship aggregated avoided-cost totals or unsourced occupational /
ROI figures.

---

## 10. Changes

We update this policy when the app changes what it stores or what leaves the device — where
we can, before the change ships — and change the dates at the top. Each revision is described
here.

**23 September 2026 — what changed.** This policy was rewritten to match the app as it is now:

- It uses the app's current name, **OmniCadence**, and says the web address still reads `omniops`.
- It covers the Apple Watch app, the Apple TV app, the Home Screen widget and the "Log a
  decision" shortcut. The previous version covered only iPhone, iPad, Mac and Apple Vision Pro.
- It describes optional **iCloud sync** of journal headlines (iPhone, iPad, Mac), off until you
  turn it on, and lists exactly which fields sync. The previous version said the app performed
  no cloud sync and had no iCloud container.
- It describes the small **iCloud key-value items** and **Handoff**, which work whenever you are
  signed in to iCloud, and says they hold IDs and settings, never journal text.
- It describes **Ask**: Apple Intelligence on the device first, and an optional model (Gemma 4
  E2B, about 4.4 GB, or Gemma 4 E4B, about 6.8 GB, depending on the device) downloaded from
  Hugging Face only after you choose it, and what Hugging Face sees. The previous version said
  the app opened no connections and had no model download. Versions before this one could
  download a smaller model (Qwen3 0.6B) without asking; this version deletes any of those files.
- It describes the optional **reminders** (off until you turn them on) and review-cadence
  reminders. The previous version said the app sent no notifications.
- It describes **Erase journal and iCloud data**, and says deleting the app does not empty iCloud.
- It says the app keeps your Pro status on the device and does not store a transaction ID; the
  previous version said we receive a transaction identifier, which was wrong — the app sends
  nothing about a purchase to us.
- It says the app logs Apple's MetricKit performance summaries on the device, that the privacy
  manifest declares two required-reason APIs, and that exports no longer include the disclaimer.
- It says what Apple itself may report to us (App Store statistics, and crash reports if you
  share them with developers).
- It removes the fixed count of knowledge packs, the statement of the App Store privacy label's
  answer, and the promise that this page changes in the same commit as the code.

The app still sends nothing to Prameya: no analytics, no account, and no server of ours. Earlier
versions of this policy remain in the public repository that publishes these pages:
<https://github.com/prameyallc/privacy>.

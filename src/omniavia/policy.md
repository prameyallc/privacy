# OmniAvia — Privacy Policy

**Effective date:** 24 September 2026
**Publisher:** Prameya LLC (“Prameya”, “we”, “us”)
**App:** OmniAvia for iPhone, iPad, Mac, Apple Vision Pro, Apple TV and Apple Watch — bundle ID `legal.prameya.OmniAvia` (the Apple Watch app is `legal.prameya.OmniAvia.watch`)
**Contact:** admin@prameya.legal
**Scope:** This policy covers the OmniAvia app and nothing else. Prameya's other apps have their own policies, because they work differently. Index: <https://prameyallc.github.io/privacy/>

This policy describes **the app you actually install**: what the shipping build does. It
replaces the 23 August 2026 page, which said the app had no iCloud sync and no model download.
The builds that followed synced your logs through iCloud and offered a model download, so both
statements were wrong for them. This page describes the current build, which syncs through
iCloud and offers no model download.

---

## The short version

**OmniAvia is ACS ground school with your own study and flight logs.** There is no account,
no sign-in, no analytics SDK, no advertising SDK, no crash reporter, no telemetry, and no
server of ours that receives anything.

**Your logs sync through your own iCloud account.** Flight, study, prep and oral-drill logs
are kept in the app and mirrored to the **private** iCloud database of the Apple Account
you are signed in with, so they appear on your other iPhone, iPad, Mac and Vision Pro. We
cannot read that database. If you are not signed in to iCloud, or iCloud is off for
OmniAvia, the logs stay on this device.

**No health data. No HealthKit.** The app does not request HealthKit permission, does not
declare HealthKit entitlements, and contains no HealthKit code.

**Ask runs on your device.** Answers come from Apple Intelligence on your device. This version
does not offer any model download. Your questions are not sent to us or to anyone else.

---

## 1. Who publishes this

Prameya LLC. Privacy contact: **admin@prameya.legal**.

---

## 2. What the app stores, and where

| What | Where |
|---|---|
| Flight and sim logs, study logs, prep / habit logs, oral-drill marks, progress snapshots | This device, **and your private iCloud database** (CloudKit) when iCloud is on |
| Where you left off: the last screen, open pack and oral-drill question; the last pack's title and the next drill's title (shown on the Apple Watch complication); the ACS area suggested on the Home Screen widget, which is worked out from the areas you have studied, and, when you tap the widget, which area to open; and your appearance choice | This device, **and iCloud key-value storage** for your Apple Account, so another device can offer “continue” |
| Reminder switch and goals, the Ask on/off switch, first-run acknowledgement, the pack of a drill you started from an Apple Watch prompt, Pro status | **This device only**, in app preferences |
| An Ask conversation | **Not saved.** It is held in memory while the app is running and is never written to storage |
| An export you asked for | **This device**, a temporary file, only while you share it |
| Photos from your library | **Not collected.** The app has no photo picker or camera, and a log has no place to hold an image: an unused image field, which no screen ever wrote, was removed from the flight log before release |
| Analytics identifiers | **None** |

Your iCloud data sits in your Apple Account under Apple's iCloud terms. Prameya has no access
to your private CloudKit database or your key-value storage, and we cannot read, export or
restore them for you. To stop syncing, turn off iCloud for OmniAvia in iOS Settings → your
name → iCloud (on a Mac, System Settings → your name → iCloud).

**Apple Watch and Apple TV keep no logs.** The Apple TV app is a read-only pack browser: it
reads the “continue” entry, the last pack's title and your appearance choice from iCloud
key-value storage and writes nothing. The Apple Watch app shows the packs, the “continue” entry
and the next-drill title, reads your appearance choice, and can save the next-drill title to
iCloud key-value storage. When you tap **Confirm**, **Start** or
**Log stub** on the Watch, the Watch sends that tap to your paired iPhone over Apple's Watch
connection, and the iPhone writes the entry (a pre-flight acknowledgement, a drill started, or
an empty flight-log stub dated now). That entry then syncs like any other log.

If iCloud Backup is on, Apple's device backup may also include the app container. That is
Apple's processing, not ours.

---

## 3. Ask (on-device answers)

The **Ask** tab appears only when **On-device answers** is on in **More** (it is on until you
turn it off) and Apple Intelligence can answer on your device.

- **Apple Intelligence only.** Ask uses Apple's on-device language model. The question and the
  answer stay on the device. Where Apple Intelligence is not available, there is no Ask tab.
- **No model download in this version.** The app contains code for downloading an open model
  from Hugging Face, but in this version it offers no model on any device: there is no
  download button, no consent prompt and no request to Hugging Face. Earlier versions offered
  a Qwen3 0.6B or 1.7B model (4-bit, from the `mlx-community` collection) in **More**. On its
  first launch this version deletes those model files from the device.
- **Apple Watch.** A question asked on the Watch is passed to your paired iPhone over Apple's
  Watch connection, answered there by Apple Intelligence when the iPhone can, and the answer
  (or a note that Ask is unavailable) is sent back to the Watch. It does not go to us.
- **No cloud AI.** OmniAvia never sends your question to a server for an answer.

---

## 4. Other network use

- **iCloud** (section 2): Apple's CloudKit and key-value storage, for your own data.
- **Handoff**: when you move between your own devices, the app may offer to continue where
  you left off (the screen, pack and question). This uses Apple's Handoff between devices
  signed in to your Apple Account. It is not added to on-device search.
- **App Store**: purchases and subscription status go through Apple's StoreKit.
- **Open the source**: tapping this on a knowledge pack opens the official page it cites (an
  FAA, eCFR or aviationweather.gov page) in your browser. That tap is yours, and no study data
  goes with it. Other links you tap (this policy, support, acknowledgements, Apple's terms)
  also open in your browser or mail app.

There is no first-party API, no analytics endpoint, no push server and no model download.

---

## Subscriptions and In-App Purchases

### Available tiers

There is one paid upgrade, **OmniAvia Pro**, sold as three products. Buying any one of
them grants exactly the same Pro. There are no separate feature tiers.

| Product | Price (US) | Billing |
|---|---|---|
| OmniAvia Pro Monthly | $5.99 | Auto-renews monthly. 7-day free trial for eligible new subscribers. |
| OmniAvia Pro Annual | $39.99 | Auto-renews yearly. 7-day free trial for eligible new subscribers. |
| OmniAvia Pro Lifetime | $99.99 | One-time purchase. Not a subscription. |

Family Sharing is enabled on all three. Subscriptions renew until you cancel in Settings.
Lifetime is a one-time non-consumable.

**The knowledge layer is free and stays free.** Without paying anything you get every ACS
area of operation and the 14 CFR reference, plus your own logs and iCloud sync, with no
account and no time limit. Pro adds ACS drills, missed-item review, oral-prep sessions and a
formatted study PDF.

**iCloud sync is not a paid feature.** It works the same with or without Pro. If a
subscription lapses you keep your data and can still export it in raw form. Only the Pro
tools stop.

### Free vs paid tier data collection

**Free and Pro handle data the same way.** Buying Pro changes which tools you get, not what
is stored or where it goes. In every tier, no learning data is sent to Prameya and there is
no analytics or tracking.

### Cancellation and refunds

Subscriptions are managed by Apple:
- **Cancel:** iOS Settings → your name → Subscriptions → OmniAvia
- **Refund requests:** reportaproblem.apple.com
- **Lifetime purchase:** one-time payment, no subscription to cancel

Prameya cannot cancel your subscription or issue refunds. Apple controls all billing.

### StoreKit transaction data

Apple tells the app which product you own and when a subscription expires. The app keeps a
Pro flag and the active product ID in its preferences **on this device only**, and only while
Pro is on. They are not synced to iCloud. **Delete all my data** removes them too. The app then
asks the App Store again, straight away and at every launch, without asking you to sign in, so
a purchase your Apple Account still owns comes back by itself and one that has lapsed does
not. Deleting your data does not cancel a subscription.

---

## 5. What the app does not do

Checked against the compiled sources (`OmniAviaKit/Sources`, `App/`) and the app
entitlements, Info.plist and privacy manifests:

- ❌ **No HealthKit.**
- ❌ **No servers of ours.** No first-party API, account, Sign in with Apple or login.
- ❌ **No analytics, advertising, crash reporting or tracking.** No ATT prompt.
- ❌ **No photo picker, camera or photo-library access.**
- ❌ **No location, microphone, contacts or calendar.**
- ❌ **No cloud AI and no model download.** Ask runs on the device (section 3).
- ❌ **No sale or sharing of personal information.** We hold none.
- ❌ **HIPAA does not apply** (not a covered entity, no PHI).

---

## 6. Notifications

**Local notifications are opt-in.** The **Daily logging reminder** switch in **More** is off
on a new install, and permission is requested only when you switch it on, never at launch.
Switching it on schedules, on your own device, a daily logging reminder at 07:30, an evening
log review at 19:00, and, while a drill is in progress, a “drill is waiting” reminder at
18:00. Tapping a reminder only opens the app; it never writes a record.

The Apple Watch app's **Now** tab shows three prompts (pre-flight reminder, today's drill, log
this flight later) with **Confirm** (or **Start** / **Log stub**), **Snooze** and **Not now**.
**Snooze** asks your iPhone to show the prompt again later as a local notification, and only
while the reminder switch is on. On that notification, **Confirm** writes an entry; a plain
tap only opens the app. There is no push server. Turning the switch off cancels every pending
reminder.

---

## 7. Export and deletion

- **Export:** More → **Export my data** builds a JSON file on this device with every entry in
  your logbook (Pro can also build a formatted study PDF) and hands it to the share sheet. We
  never receive a copy.
- **Delete all:** More → **Delete all my data** permanently removes every flight and sim,
  study, prep and oral-drill record and progress snapshot after you confirm. When iCloud is
  on, the deletion also syncs to your private iCloud database, so the records disappear from
  your other devices too. It also removes the iCloud “continue”, pack-title, next-drill and
  widget entries, pending reminders, your reminder switch and goals, the pack of a drill you
  started from an Apple Watch prompt, the Pro flag and product ID described above, and any
  model files left in the app's model cache, and it forgets where you were in the app (the
  open pack and oral-drill question, the next pack Do suggests, the open ACS area, and the pack
  Ask is working from). It cannot be undone.
- **Kept after Delete all:** your appearance choice (on this device and in iCloud key-value
  storage), the Ask on/off switch, and the first-run acknowledgement (so the disclaimer screen
  does not return). Right after the deletion the app returns to Home and writes a new
  “continue” entry that names only the Home screen, with no pack, question or pack title, and
  a widget entry that suggests the first ACS area, as on a new install. It sends your Apple
  Watch no next-drill title. As you go on using the app, it keeps these entries current.
- **Delete the app** removes this device's copy. Records already synced stay in your iCloud
  account until you delete them in the app on another device, or manage OmniAvia's data in
  iOS Settings → your name → iCloud.

---

## 8. Knowledge packs

ACS-anchored packs ship inside the app. The app does not fetch packs from the network.

---

## 9. Children

OmniAvia is a general-audience adult education tool (ground school). It is not in the Kids
Category. We do not knowingly collect information from anyone, including children, because
we do not collect information.

---

## 10. Your rights

There is nothing of yours on our servers to access, correct or delete. Your data lives on
your devices and in your own iCloud account, where you control it. Rights under the GDPR,
UK GDPR and CCPA/CPRA are exercised there. If you believe we hold something, write to the
contact in section 1.

We do not respond to “Do Not Track” signals, because we do not track.

---

## 11. What this app is not

OmniAvia is educational ground study and habit logs. It is **not** flight instruction,
**not** a go/no-go determination, and **not** a substitute for a CFI, the FARs, or your own
decision.

---

## 12. Changes

Material changes update the effective date at the top of this page. When a change to the app
affects what is stored or what leaves the device, we update this page and list the change
below.

**24 September 2026 — what changed.**

- Delete all now also removes your Pro status: the Pro flag and product ID the app keeps on
  this device. The app then asks the App Store again, straight away and at every launch, so a
  purchase your Apple Account still owns comes back by itself. Before, Delete all kept them.
- Delete all now also forgets where you were in the app. Before, if a pack was open, the app
  wrote that pack's title back to iCloud key-value storage and sent it to your Apple Watch
  right after the deletion. It no longer does: the new “continue” entry names only the Home
  screen.
- The flight log no longer has an image field. It was never used: no screen could attach an
  image, so nothing was ever stored in it. When this version first opens a logbook written by
  an earlier test build, it removes the empty field and keeps every entry. The export no longer
  has a place for an image.

**23 September 2026 — what changed.** This page now describes the current build:

- Personal logs sync to your private iCloud database through CloudKit, on iPhone, iPad, Mac
  and Vision Pro. Apple Watch and Apple TV keep no logs; a Confirm on the Watch is written by
  your iPhone.
- “Continue”, pack-title, next-drill and widget state, and your appearance choice, use iCloud
  key-value storage. Handoff and the Apple Watch relay use Apple's services.
- Ask uses Apple Intelligence on your device only. This version offers no model download and
  makes no request to Hugging Face, and it deletes Qwen3 model files that earlier versions
  downloaded.
- Reminders are off until you switch them on, and a tap on a reminder never writes a record.
- Delete all clears the iCloud “continue” entries but keeps your Pro status, appearance
  choice and a few settings, which are now listed. (Pro status: changed on 24 September,
  above.)
- Delete all now also removes the pack of a drill you started from an Apple Watch prompt.
  Before, it was kept, and turning reminders back on scheduled the 18:00 “drill is waiting”
  reminder for a drill from before the deletion.
- Delete all now also clears the next-drill title your iPhone keeps in memory for your Apple
  Watch. Before, the iPhone could send that title to the Watch after the deletion, and the
  Watch then saved it to iCloud key-value storage again. If a pack was still open, its title
  was still written again right after the deletion (changed on 24 September, above).
- Settings in the app are under **More**.

A first version of this page, published earlier on 23 September 2026, said you could download
a Qwen3 model in More with a consent prompt over 500 MB, and that Delete all cleared your Pro
status. Neither was true of the build then current. (Delete all clears your Pro status from
24 September, above.) The 23 August 2026 page said the app had no
iCloud sync and no model download, which was wrong for the builds that followed it.

**23 August 2026.** First published page.

---

## Contact

**Prameya LLC** · [admin@prameya.legal](mailto:admin@prameya.legal)

This policy: <https://prameyallc.github.io/privacy/omniavia/>

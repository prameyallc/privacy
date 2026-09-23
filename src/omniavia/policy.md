# OmniAvia — Privacy Policy

**Effective date:** 23 September 2026
**Publisher:** Prameya LLC (“Prameya”, “we”, “us”)
**App:** OmniAvia for iPhone, iPad, Mac, Apple Vision Pro, Apple TV and Apple Watch — bundle ID `legal.prameya.OmniAvia`
**Contact:** admin@prameya.legal
**Scope:** This policy covers the OmniAvia app and nothing else. Prameya's other apps have their own policies, because they work differently. Index: <https://prameyallc.github.io/privacy/>

This policy describes **the app you actually install**: what the shipping build does. It
replaces the 23 August 2026 page, which said the app had no iCloud sync and no model download.
Both statements were wrong for the current build, and this page corrects them.

---

## The short version

**OmniAvia is ACS ground school with your own study and flight logs.** There is no account,
no sign-in, no analytics SDK, no advertising SDK, no crash reporter, no telemetry, and no
server of ours that receives anything.

**Your logs sync through your own iCloud account.** Flight, study, prep and oral-drill logs
are kept in the app and mirrored to the **private** iCloud database of the Apple Account
you are signed in with, so they appear on your other devices. We cannot read that database.
If you are not signed in to iCloud, or iCloud is off for OmniAvia, the logs stay on this
device.

**No health data. No HealthKit.** The app does not request HealthKit permission, does not
declare HealthKit entitlements, and contains no HealthKit code.

**Ask runs on your device.** Answers come from Apple Intelligence on your device or from a
small open model you choose to download. Your questions are not sent to us or to anyone
else.

---

## 1. Who publishes this

Prameya LLC. Privacy contact: **admin@prameya.legal**.

---

## 2. What the app stores, and where

| What | Where |
|---|---|
| Flight logs, study logs, prep / habit logs, oral-drill marks, progress snapshots | This device, **and your private iCloud database** (CloudKit) when iCloud is on |
| Where you left off: last open pack, lesson or record, the pack and next-drill titles, the ACS-area card on the Home Screen widget, and your appearance choice | This device, **and iCloud key-value storage** for your Apple Account, so another device can offer “continue” |
| Reminder and goal preferences, first-run acknowledgement, Pro status | **This device only**, in app preferences |
| A model you downloaded for Ask | **This device only**, inside the app container |
| An export you asked for | **This device**, a temporary file, only while you share it |
| Photos from your library | **Not collected.** The app has no photo picker or camera |
| Analytics identifiers | **None** |

Your iCloud data sits in your Apple Account under Apple's iCloud terms. Prameya has no access
to your private CloudKit database or your key-value storage, and we cannot read, export or
restore them for you. To stop syncing, turn off iCloud for OmniAvia in iOS Settings → your
name → iCloud.

If iCloud Backup is on, Apple's device backup may also include the app container. That is
Apple's processing, not ours.

---

## 3. Ask (on-device answers)

The **Ask** tab appears only when on-device answers are turned on and your device can
generate them.

- **Apple Intelligence first.** Where available, Ask uses Apple's on-device language model.
  The question and the answer stay on the device.
- **Optional downloaded model.** In **More**, you can choose to download a small open model
  (for example Qwen3 0.6B or 1.7B, 4-bit, from the `mlx-community` collection). The download
  starts only when you tap **Download**. Anything over 500 MB asks for your consent first. The
  file comes from Hugging Face (`huggingface.co`), whose servers see an ordinary download
  request from your device's IP address. Nothing you have written is sent with it. The model
  then runs on your device.
- **Apple Watch.** A question asked on the Watch is passed to your paired iPhone over Apple's
  Watch connection and answered there. It does not go to us.
- **No canned replies, no cloud AI.** OmniAvia never sends your question to a server for an
  answer.

---

## 4. Other network use

- **iCloud** (section 2): Apple's CloudKit and key-value storage, for your own data.
- **Handoff**: when you move between your own devices, the app may offer to continue where
  you left off. This uses Apple's Handoff between devices signed in to your Apple Account.
- **App Store**: purchases and subscription status go through Apple's StoreKit.
- **Open the source**: tapping this on a knowledge pack opens an FAA or eCFR page in your
  browser. That tap is yours, and no study data goes with it.
- **Model download** (section 3): only when you tap Download.

There is no first-party API, no analytics endpoint and no push server.

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
Pro flag and the active product ID in its preferences **on this device only**. They are not
synced to iCloud and are cleared by **Delete all my data**. Apple re-confirms your purchase
from the App Store when needed.

---

## 5. What the app does not do

Checked against the compiled sources (`OmniAviaKit/Sources`, `App/`) and the app
entitlements, Info.plist and privacy manifest:

- ❌ **No HealthKit.**
- ❌ **No servers of ours.** No first-party API, account, Sign in with Apple or login.
- ❌ **No analytics, advertising, crash reporting or tracking.** No ATT prompt.
- ❌ **No photo picker, camera or photo-library access.**
- ❌ **No location, microphone, contacts or calendar.**
- ❌ **No cloud AI.** Ask runs on the device (section 3).
- ❌ **No sale or sharing of personal information.** We hold none.
- ❌ **HIPAA does not apply** (not a covered entity, no PHI).

---

## 6. Notifications

**Local notifications are opt-in.** Permission is requested only when you switch on a
reminder in Settings, never at launch. Reminders (the daily logging reminder, the evening
log review, and a drill waiting for you) are scheduled by your own device. On Apple Watch,
a reminder can offer **Confirm**, **Snooze** or **Not now**. There is no push server.
Turning reminders off cancels them.

---

## 7. Export and deletion

- **Export:** Settings → **Export my data** builds a JSON file on this device (Pro can also
  build a formatted study PDF) and hands it to the share sheet. We never receive a copy.
- **Delete all:** Settings → **Delete all my data** permanently removes every flight, study,
  prep and oral-drill record after you confirm. When iCloud is on, the deletion also syncs
  to your private iCloud database, so the records disappear from your other devices too. It
  also clears the iCloud “continue” and widget entries, pending reminders, your reminder,
  goal and Pro-status preferences, and any downloaded model. The first-run acknowledgement is
  kept so the disclaimer screen does not return. It cannot be undone.
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

Material changes update the effective date at the top of this file. A behaviour change that
affects what is stored or what leaves the device is described here in the **same commit**
as the code.

**23 September 2026: what changed.** Corrected the description of the shipping build:
personal logs sync to your private iCloud database through CloudKit; “continue” and widget
state use iCloud key-value storage; Ask can use Apple Intelligence or an optional model you
download from Hugging Face; Handoff and the Apple Watch relay use Apple's services; the app
runs on Apple TV and Apple Watch too; Delete all also clears the iCloud entries. The earlier
page wrongly said the app had no iCloud sync and no model download.

**23 August 2026.** First published page.

---

## Contact

**Prameya LLC** · [admin@prameya.legal](mailto:admin@prameya.legal)

This policy: <https://prameyallc.github.io/privacy/omniavia/>

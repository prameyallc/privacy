# OmniAero — Privacy Policy

**Effective date:** 23 August 2026
**Publisher:** Prameya LLC (“Prameya”, “we”, “us”)
**App:** OmniAero for iPhone, iPad, Mac and Apple Vision Pro — bundle ID `legal.prameya.OmniAero`
**Contact:** admin@prameya.legal
**Scope:** This policy covers the OmniAero app and nothing else. Prameya's other apps have their own policies, because they work differently. Index: <https://prameyallc.github.io/privacy/>

This policy describes **the app you actually install** — what the shipping build does, not what
an earlier plan for it said. It replaces a draft that described features this app does not have:
HealthKit it never requests, a Hugging Face / MLX model download it cannot perform, and a photo
picker that is not in this build. Where the two disagreed, the draft was wrong.

---

## The short version

**OmniAero is ACS ground school on this device.** There is no account, no sign-in, no analytics
SDK, no advertising SDK, no crash reporter, no telemetry, and no server of ours that receives
anything.

**No health data. No HealthKit.** The app does not request HealthKit permission, does
not declare HealthKit entitlements, and contains no HealthKit code.

**No Hugging Face traffic in this build.** There is no model download, no MLX inference
client, and no PhotosPicker. If that ever changes, this policy will be updated in the same
commit.

Study, prep and session logs live in a local SwiftData store on this device. Local
notifications are opt-in from Settings. Export is something you start. Delete-all empties
the on-device store.

---

## 1. Who publishes this

Prameya LLC. Privacy contact: **admin@prameya.legal**.

---

## 2. What the app stores on your device

The shipping UI writes study logs, prep / habit ticks, and session notes you enter. Those
records sit in a local SwiftData store inside the app container. The app does not sync that
store to iCloud.

| What | Where |
|---|---|
| Study, prep and session logs you enter | **On this device**, in the app’s SwiftData store |
| Appearance and reminder preference | **On this device**, in app preferences |
| A JSON export you asked for | **On this device**, temporary folder, only while you share it |
| Model weights / Hugging Face cache | **Not stored as a feature.** There is no download control. Delete-all may still purge leftover cache from an older install |
| Photos from your library | **Not stored.** This build has no photo picker |
| Analytics identifiers | **None** |

Export is a file you choose to share (Share sheet). It is written only when you tap
**Export my data**. Nothing is uploaded to us.

If iCloud Backup is enabled in iOS Settings, Apple's device backup may include the app
container. That is Apple's processing, not ours. OmniAero itself performs no cloud sync.

---

## Subscriptions and In-App Purchases

### Available tiers

OmniAero offers four purchase options:

| Feature | Free | Foundation ($4.99/mo or $49/yr) | Scholar ($9.99/mo or $89/yr) | Lifetime ($79.99) |
|---------|------|--------------------------------|------------------------------|-------------------|
| Curriculum Access | 20-25% | 50% | 100% | 100% |
| Interactive Lessons | 2-4 | 6-8 | All | All |
| Offline Access | No | Yes | Yes | Yes |
| CloudKit Sync | No | Progress only | All preferences | All preferences |
| Future Updates | No | Yes | Yes | Yes |

### What Apple receives

All transactions go through Apple's App Store. When you purchase:
- **Apple receives:** Your Apple Account ID, payment method, transaction details
- **Prameya receives:** A transaction ID from StoreKit, purchase status, tier purchased
- **Prameya does NOT receive:** Your name, email, payment card details, or Apple Account credentials

### Data Linked to You

Apple's privacy labels mark Purchase History as "Data Linked to User" for purchasers.

**This does NOT mean your learning data is transmitted.** Your progress, quiz answers, and study history remain on-device only. StoreKit tells us you purchased access so we can unlock content — it does not transmit your learning data.

### Free vs paid tier data collection

**All tiers collect the same data** (progress tracking, quiz responses, lesson completion).

The difference is:
- **What content is available** (20% vs 50% vs 100% curriculum)
- **Whether progress syncs between your devices** (Free: no sync; Paid: sync via your iCloud)

In all tiers:
- Quiz answers and progress stay on your device
- No transmission of learning data to Prameya
- No analytics or tracking

**Purchase unlocks content. It does not change what data is collected.**

### Cancellation and refunds

Subscriptions are managed by Apple:
- **Cancel:** iOS Settings → your name → Subscriptions → OmniAero
- **Refund requests:** reportaproblem.apple.com
- **Lifetime purchase:** One-time payment, no subscription to cancel

Prameya cannot cancel your subscription or issue refunds. Apple controls all billing.

### StoreKit transaction data

When you purchase, the app receives and stores locally on your device:
- Transaction ID (an opaque identifier from Apple)
- Product ID (which tier you purchased)
- Purchase and expiration dates (for subscriptions)

This data:
- Is stored only on your device
- Is NOT synced to iCloud
- Is used only to unlock tier-appropriate content
- Is deleted when you use "Delete All Data"

---

## 3. What the app does not do

Checked against compiled sources (`OmniAeroKit/Sources`, `App/OmniAero`) and the App
shell entitlements / Info.plist / PrivacyInfo:

- ❌ **No HealthKit.** No `import HealthKit`, no `HKHealthStore`, no usage description,
  no health-records entitlement.
- ❌ **No CloudKit / iCloud container for user logs.** The SwiftData store is local-only.
- ❌ **No MLX / Hugging Face / on-device model download** in this build.
- ❌ **No PhotosPicker, camera, or photo-library intake** in this build.
- ❌ **No analytics, advertising, crash reporting, or tracking.** No ATT prompt.
- ❌ **No account, Sign in with Apple, or server login.**
- ❌ **No location, microphone, contacts, or calendar.**
- ❌ **No sale or share of personal information** — we hold none.
- ❌ **HIPAA does not apply** (not a covered entity, no PHI).

Apple’s App Privacy label for this binary is **Data Not Collected.**

---

## 4. Network

**This build does not download models and does not send your logs anywhere.** There is no
Hugging Face client and no first-party API.

You may tap **Open the source** on a knowledge pack. That opens a hashed FAA / public
reference URL in your browser. That tap is yours. The app does not upload study logs with
it.

If on-device model weights are added later:

1. the download starts only after you ask;
2. files land **inside the app container**;
3. this section is rewritten before that build ships.

---

## 5. Notifications

**Local notifications are opt-in.** Permission is requested only when you switch on
**Daily logging reminder** in Settings, never at launch. The notification is scheduled by
your own device. There is no push server. Turning the reminder off cancels it.

---

## 6. Export and deletion

- **Export:** Settings → **Export my data** builds a JSON file on this device and hands it
  to the system share sheet. We never receive a copy.
- **Delete all:** Settings → **Delete all my data** permanently removes every flight, study
  and prep log from this device after you confirm. It cannot be undone. There is no copy
  anywhere else. Pending local reminders are cancelled. Leftover model-cache directories
  from older installs, if any, are purged as cleanup — not as a user-facing download
  feature.
- **Delete the app** removes the container on iPhone, iPad and Apple Vision Pro.

---

## 7. Knowledge packs

ACS-anchored packs ship inside the app. Adding a pack does not, by itself, send data off
device. The app does not fetch packs from the network.

---

## 8. Children

OmniAero is a general-audience adult education tool (ground school). It is not in the Kids
Category. We do not knowingly collect information from anyone, including children, because
we do not collect information.

---

## 9. Your rights

There is nothing of yours on our servers to access, correct, or delete. Deleting the app
removes the on-device container. Rights under the GDPR / UK GDPR / CCPA-CPRA are exercised
on your device; if you believe we hold something, write to the contact in §1.

We do not respond to “Do Not Track” signals, because we do not track.

---

## 10. What this app is not

OmniAero is educational ground study and habit logs on this device. It is **not** flight
instruction, **not** a go/no-go determination, and **not** a substitute for a CFI, the
FARs, or your own decision.

---

## 11. Changes

Material changes update the effective date at the top of this file. A behaviour change that
affects what is stored or what leaves the device is described here in the **same commit**
as the code.

**23 August 2026 — what changed.** First published page for the shipping binary: on-device
SwiftData logs, no account, no HealthKit, no MLX / Hugging Face / PhotosPicker, local
notifications opt-in, user-initiated export, delete-all, contact admin@prameya.legal.

---

## Contact

**Prameya LLC** · [admin@prameya.legal](mailto:admin@prameya.legal)

This policy: <https://prameyallc.github.io/privacy/omniaero/>

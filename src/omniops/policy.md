# OmniOps — Privacy Policy

**Effective date:** 17 August 2026
**Last updated:** 26 August 2026  
**Publisher:** Prameya LLC (“Prameya”, “we”, “us”)  
**App:** OmniOps for iPhone, iPad, Mac and Apple Vision Pro — bundle ID `legal.prameya.OmniOps`  
**Contact:** admin@prameya.legal  
**Scope:** This policy covers the OmniOps app and nothing else. Prameya's other apps have their own policies, because they work differently. Index: <https://prameyallc.github.io/privacy/>

This policy describes **the app you actually install** — what the shipping build does, not what
an earlier plan for it said. It replaces a 10 August 2026 draft that described features this app
does not have: Health data access it never requests, and a model download it cannot perform.
Where the two disagreed, the draft was wrong.

---

## The short version

**OmniOps collects nothing.** There is no account, no sign-in, no analytics SDK, no
advertising SDK, no crash reporter, no telemetry, and no server of ours that receives
anything.

**No health data. No HealthKit.** The app does not request HealthKit permission, does
not declare HealthKit entitlements, and contains no HealthKit code.

**No Hugging Face traffic in this build.** There is no model download and no inference
client. If that ever changes, download will be user-initiated and stored in the app
container, and this policy will be updated in the same commit.

The compiled root is four tabs (Act / Understand / Do / More) plus the on-screen
disclaimer (educational + habit support; not consulting / audit / certification).
Understand reads on-device knowledge packs. Do writes a local journal. Nothing is
uploaded to us.

---

## Available tiers

There is one paid upgrade, **OmniOps Pro**, sold as three products. Buying any one of
them grants exactly the same Pro — there are no separate feature tiers.

| Product | Price (US) | Billing |
|---|---|---|
| OmniOps Pro Monthly | $5.99 | Auto-renews monthly. 7-day free trial. |
| OmniOps Pro Annual | $39.99 | Auto-renews yearly. 7-day free trial. |
| OmniOps Pro Lifetime | $99.99 | One-time purchase. Not a subscription. |

Family Sharing is enabled on all three. Subscriptions renew until you cancel in
Settings; Lifetime is a one-time non-consumable.

**The knowledge layer is free and stays free.** Without paying anything you get
all four logs unlimited, the streak and raw JSON export, with no account and no time limit. Pro adds review analytics, custom cadences and the review PDF.

**Pro does not add cloud sync, and there is no paid iCloud option.** OmniOps stores your
records on your device in every case, paid or not. If a subscription lapses you keep your
own data and can still export it in its raw form; only the Pro tools stop.


## Free vs paid tier data collection

**OmniOps is free to use**, and buying Pro does not change what data Prameya collects. Free and Pro alike:

- Your process journal (work, decisions, reflections, habits) stays on your device
- No analytics, tracking, or telemetry
- No server that receives your content
- No account or login

The difference is **which tools you get**, not data handling. All four logs, the streak and raw JSON export are free; Pro adds review analytics, custom cadences and the review PDF. Neither unlocks data transmission.

## Cancellation and refunds

Subscriptions are managed entirely through your Apple ID:

- **To cancel:** Open Settings on your iPhone or iPad → tap your name → Subscriptions → OmniOps → Cancel Subscription. On Mac, open the App Store app → Account (sign-in name) → View Information → Subscriptions → Manage. On Apple Vision Pro, open Settings → your name → Subscriptions → OmniOps → Cancel Subscription.
- **Refund requests:** Handled by Apple, not Prameya. See [reportaproblem.apple.com](https://reportaproblem.apple.com/) or contact Apple Support. We have no access to your payment information and cannot issue refunds ourselves.
- **What happens to your data when you cancel:** Nothing. Your on-device journal stays on your device. Cancelling removes the Pro tools; it does not delete your journal entries, decisions or reflections, and it does not lock you out of your own records. Every log stays readable and raw JSON export stays available, because those are free.

## StoreKit transaction data

The anonymized StoreKit transaction record described above is stored in the app's local database on your device. It is used to determine which features and knowledge packs to unlock. It is never uploaded to Prameya, and it is deleted when you delete the app (including the sandbox container on Mac at `~/Library/Containers/legal.prameya.OmniOps`).

If you restore purchases on a new device (by tapping "Restore Purchases" in the app), StoreKit queries Apple's servers to retrieve your active subscriptions. That communication is between your device and Apple; Prameya is not involved and sees nothing from it.

---

## 1. Who publishes this

Prameya LLC. Privacy contact: **admin@prameya.legal**.

---

## 2. What the app stores on your device

The shipping UI writes a process journal when you log work, a decision, a reflection,
or a habit. That journal is JSON in this app’s Application Support folder. Which
readings you have opened is stored beside it. On iPhone, iPad and Apple Vision Pro
those files are encrypted at rest while the device is locked. On Mac they sit inside
the sandboxed app container and are covered by FileVault if it is on. There is no
SwiftData store and no Keychain write.

| What | Where |
|---|---|
| Your typed journal (work, decisions, reflections, habits) | **On this device**, in the app’s Application Support folder |
| Which readings you opened | **On this device**, next to the journal |
| A journal export you asked for | **On this device**, temporary folder, only while More is on screen |
| The journal as it was just before an import | **On this device**, next to the journal |
| Model weights / Hugging Face cache | **Not stored.** No download feature |
| Analytics identifiers | **None** |

Export is a file you choose to share (Share sheet). It is written only when you tap
“Export my journal”, into a temporary folder of its own, and it is deleted when you
leave the More screen. The file includes the journal JSON and the on-screen disclaimer
text. Import replaces the on-device journal with a previously exported file you choose;
it asks you to confirm first, and a file that does not decode is refused and the journal
is not changed. Nothing is uploaded to us.

If iCloud Backup is enabled in iOS Settings, Apple’s device backup may include the app
container, including the journal. That is Apple’s processing, not ours. OmniOps itself
performs no cloud sync.

Deleting the app removes the container on iPhone, iPad and Apple Vision Pro, including
the journal. On Mac the sandbox container under
`~/Library/Containers/legal.prameya.OmniOps` outlives the app and has to be removed
separately.

---

## 3. What the app does not do

Checked against compiled sources and the App shell entitlements / Info.plist / PrivacyInfo:

- ❌ **No HealthKit.** No HealthKit permission, no usage description, no health-records entitlement.
- ❌ **No CloudKit / iCloud container.** The iOS entitlements file is empty; the macOS one
  requests the App Sandbox and nothing else.
- ❌ **No analytics, advertising, crash reporting, or tracking.** No ATT prompt.
- ❌ **No account, Sign in with Apple, or server login.**
- ❌ **No location, camera, microphone, photos, contacts, calendar, or notifications.**
- ❌ **No sale or share of personal information** — we hold none.
- ❌ **HIPAA does not apply** (not a covered entity, no PHI).

Apple’s App Privacy label for this binary is **Data Not Collected.**

`PrivacyInfo.xcprivacy` declares no tracking, no collected data types, and no accessed
required-reason APIs — matching a binary that does not call those APIs.

---

## 4. Network

**This build opens no connections.** There is no Hugging Face client, no CDN fetch, and
no first-party API.

If on-device model weights are added later:

1. the download starts only after you ask;
2. files land **inside the app container** (not `~/.cache/huggingface` on unsandboxed Mac);
3. Hugging Face (and any CDN it redirects to) will see an ordinary HTTPS request and
   your IP address; we receive nothing;
4. this section is rewritten before that build ships.

---

## 5. Knowledge packs

Nineteen packs ship in the app and appear on Understand. They are bundled in the
binary. Adding a pack does not, by itself, send data off device. The app does not
fetch packs from the network.

---

## 6. Monetization

OmniOps presents a StoreKit paywall for OmniOps Pro (monthly $5.99, annual $39.99,
lifetime $99.99 — see "Available tiers" above). Apple processes the purchase. We receive a
transaction identifier and your entitlement status, and nothing else: no name, no email, no
payment card details, no Apple Account credentials.

The knowledge layer is free. All four logs, the streak and raw JSON export cost nothing and
have no time limit.

---

## 7. Children

OmniOps is a general-audience adult tool. It is not in the Kids Category. We do not
knowingly collect information from anyone, including children, because we do not
collect information.

---

## 8. Your rights

There is nothing of yours on our servers to access, correct, or delete. Deleting the
app removes the on-device container (on Mac, also remove the sandbox container named
above). Rights under the GDPR / UK GDPR / CCPA-CPRA are exercised on your device; if
you believe we hold something, write to the contact in §1.

We do not respond to “Do Not Track” signals, because we do not track.

---

## 9. What this app is not

The compiled screen renders, verbatim:

> EDUCATIONAL + HABIT SUPPORT ONLY. NOT MEDICAL/FINANCIAL/LEGAL ADVICE. Does not replace
> licensed pros. On-device models limited. Consult pros.
>
> OmniOps supports your own process journal and improvement habits. It is not management
> consulting, not an audit, and not a conformity assessment or certification against any
> management-system standard.

OmniOps does not ship aggregated avoided-cost totals or unsourced occupational /
ROI figures.

---

## 10. Changes

Material changes update the “Last updated” date at the top of this file. A behaviour
change that affects what is stored or what leaves the device is described here in the
**same commit** as the code.

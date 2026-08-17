# OmniOps — Privacy Policy

**Effective date:** 17 August 2026
**Publisher:** Prameya LLC (“Prameya”, “we”, “us”)
**App:** OmniOps for iPhone, iPad and Mac — bundle ID `legal.prameya.OmniOps`
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

The compiled screen is `OmniOpsRootView`. It renders `OpsDisclaimerView` (educational +
habit support; not consulting / audit / certification).

---

## 1. Who publishes this

Prameya LLC. Privacy contact: **admin@prameya.legal**.

---

## 2. What the app stores on your device

The shipping UI is a disclaimer and a single sentence of product copy. It does **not**
write a process journal, decision log, habit record, or user profile — those types exist
in `OpsCore` as a model, and no compiled persistence layer saves them yet.

| What | Where |
|---|---|
| Your typed notes, logs, or profile | **Not stored.** No SwiftData store, no file export, no Keychain write on the compiled path |
| Model weights / Hugging Face cache | **Not stored.** No download feature |
| Analytics identifiers | **None** |

If iCloud Backup is enabled in iOS Settings, Apple’s device backup may include the app
container. That is Apple’s processing, not ours. OmniOps itself performs no cloud sync.

Deleting the app removes the container on iOS. This build writes nothing you would need
to delete by hand.

---

## 3. What the app does not do

Checked against compiled sources (`OmniOpsKit/Sources`, `App/OmniOps`) and the App
shell entitlements / Info.plist / PrivacyInfo:

- ❌ **No HealthKit.** No `import HealthKit`, no `HKHealthStore`, no usage description,
  no health-records entitlement. Unused HealthKit claims from old placeholder plists
  are gone.
- ❌ **No CloudKit / iCloud container.** Entitlements file is empty. No `import CloudKit`.
- ❌ **No analytics, advertising, crash reporting, or tracking.** No ATT prompt.
- ❌ **No account, Sign in with Apple, or server login.**
- ❌ **No location, camera, microphone, photos, contacts, calendar, or notifications.**
- ❌ **No sale or share of personal information** — we hold none.
- ❌ **HIPAA does not apply** (not a covered entity, no PHI). See `REGULATORY.md` §5.

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

Packs are authored in `KNOWLEDGE/packs/` and synced into the `Knowledge` module
(`Bundle.module`). The kit product currently holds **six** NIST-derived packs. The
compiled App shell does **not** link `Knowledge`, so those files are not in the
shipping binary. Adding a pack does not, by itself, send data off device.

---

## 6. Monetization

A StoreKit paywall exists as a **compiled kit product** (`Monetization`) so the tree is
not dead. The App shell links `DesignSystem` and `AppSurfaces` only. `AppSurfaces` does
not depend on `Monetization`. This binary does not present a paywall and does not talk
to the App Store for in-app purchase.

---

## 7. Children

OmniOps is a general-audience adult tool. It is not in the Kids Category. We do not
knowingly collect information from anyone, including children, because we do not
collect information.

---

## 8. Your rights

There is nothing of yours on our servers to access, correct, or delete. Deleting the
app removes the on-device container. Rights under the GDPR / UK GDPR / CCPA-CPRA are
exercised on your device; if you believe we hold something, write to the contact in §1.

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
ROI figures. See `REGULATORY.md`.

---

## 10. Changes

Material changes update the “Last updated” date at the top of this file. A behaviour
change that affects what is stored or what leaves the device is described here in the
**same commit** as the code.

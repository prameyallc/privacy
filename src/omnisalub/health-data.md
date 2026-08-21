# OmniSalub Consumer Health Data Privacy Policy

**Effective date:** 8 August 2026
**Last updated:** 21 August 2026
**Publisher:** Prameya LLC ("Prameya", "we", "us")
**Applies to:** OmniSalub for iPhone, iPad and Mac (bundle identifier `legal.prameya.omnisalub`)
**Contact:** admin@prameya.legal

This is a **separate, distinctly-labelled consumer health data privacy policy**, published as required by Washington's My Health My Data Act (RCW ch. 19.373) and drafted to satisfy Nevada's consumer health data law (SB 370, NRS ch. 603A) at the same time. It sits alongside — and does not replace — the [OmniSalub Privacy Policy](https://prameyallc.github.io/privacy/omnisalub/).

If you are a Washington or Nevada resident, this is the document written for you. Everyone else is welcome to read it; it describes what actually happens either way.

---

## The short version

**We do not collect, receive, store, share, sell or process any consumer health data.** OmniSalub has no servers. What you record stays in the app's private storage on your own device, and — only if you allow it — in your own Apple Health account, which Apple operates and we cannot read.

Apple's App Privacy nutrition label for this app is **Data Not Collected**. That matches this policy: Prameya LLC is not a recipient of your health data.

The sections below answer each disclosure the statute asks for, including the ones where the honest answer is "none". We have written those out rather than omitting them, because a missing element and a "none" element look identical to a reader and are not the same thing.

This revision (21 August 2026) retracts an earlier published table that listed thirteen categories under "consumer health data we collect". That table described what the **app stores on your device**, not what Prameya collects. Publishing both framings under the same statutory heading was SALUB-072. The governing answer is **None**.

---

## 1. Categories of consumer health data we collect, and the purpose of collection

**None.**

The app records measurements, symptoms and settings that *would* be consumer health data if we received them. We do not receive them. There is no account, no server of ours, no analytics endpoint, no advertising SDK, and no code path that transmits what you record to us or to anyone else. Data written to Apple Health is written into *your* Apple account under Apple's terms, not ours.

Because we collect nothing, there is no collection purpose to state.

---

## 2. Categories of sources from which consumer health data is collected

**None.** We are not a recipient of any of the sources the app reads from (your own entries, or Apple Health with your permission).

---

## 3. Categories of consumer health data that is shared

**None.** We do not share, sell, rent, trade or disclose consumer health data, because we do not have any. We have never sold consumer health data and we do not intend to.

---

## 4. A list of the categories of third parties, and specific affiliates, with whom we share consumer health data

**None — the list is empty.**

For completeness, and because we would rather over-disclose than have you discover it elsewhere, these are the only third parties involved in the app at all, none of whom receives consumer health data from us:

- **Apple Inc.** — operates the App Store, Apple Health and iCloud. If you turn on settings sync, non-health preferences (theme, guideline set, app-lock state) are stored in *your* iCloud account. Health data is never placed in iCloud; that is a fixed architectural boundary and an automated test enforces it.
- **Hugging Face, Inc.** — hosts the optional on-device language model's weight files. If, and only if, you choose to install the model, your device downloads those files. That request carries the model's repository identifier and your IP address. It carries no health data of any kind, and we are not a party to it.

We have no affiliates.

---

## 5. Sale of consumer health data

**We do not sell consumer health data, and we never have.** Washington and Nevada both require a signed, specific written authorization before any sale. We have never sought one and have no plans to.

---

## 6. Geofencing

We do not use geofencing at all, anywhere. The app contains no location code. Both Washington and Nevada prohibit geofencing around healthcare facilities; we are nowhere near that line.

---

## 7. Precise location

The app **never** requests or uses precise location. It contains no location code at all, and an automated build check fails the project if any is added. Precise location is expressly consumer health data under the Washington statute, and we would rather the answer be structural than promised.

---

## 8. How the data is processed, stored and protected — on your device, not by us

- **Where.** In an encrypted database in the app's private storage on your device. On iPhone and iPad it is set to iOS Data Protection "complete", so it is encrypted with a key derived from your device passcode and is unreadable while the device is locked. On a Mac it is protected by the app sandbox and by FileVault if you have FileVault on.
- **Not in iCloud.** Health data is never stored in iCloud by this app. The health database is created with iCloud syncing explicitly disabled, and an automated test blocks any health record from reaching the part of the app that does sync. Only five non-health preferences (theme, guideline set, onboarding state, app lock, timestamp) can sync, and only if you turn that on — it is off by default.
- **Backups.** The health database is excluded from device backup. So is the widget's display snapshot. On iPhone and iPad the snapshot is encrypted at rest until the first time you unlock the device after a restart, rather than being re-locked whenever the screen locks; the Home Screen widget could not redraw your latest reading otherwise.
- **The assistant.** If you install it, the model runs on your device. Context assembled for it never leaves your device and is not sent to us, to Apple or to any AI provider. Cloud and third-party inference modes are hard-wired off in this version.
- **Retention.** Your data stays until you delete it. We retain nothing, so there is no retention schedule on our side to describe.

---

## 9. How to exercise your rights

Washington residents have the rights below under RCW 19.373.040. Nevada residents have broadly parallel rights under Nevada SB 370. We honour these requests from anyone who asks, regardless of where they live.

| Right | What it means | How to use it |
|---|---|---|
| **Confirm and access** | Confirm whether we are collecting, sharing or selling your consumer health data, and get access to it | Email **admin@prameya.legal**. The answer will be that we hold none. Your actual data is visible in the app at any time, and exportable as PDF, CSV or FHIR |
| **List of recipients** | Get a list of the third parties and affiliates your data has been shared with | Email us. The list is empty |
| **Withdraw consent** | Withdraw consent to collection and to sharing | There is no consent to withdraw from us. Permissions the app itself uses are yours to revoke in **Settings → Privacy & Security → Health → OmniSalub**; settings sync can be turned off in the app's own Settings |
| **Delete** | Have your consumer health data deleted | Because we hold nothing, there is nothing for us to delete. On your device: **Settings → Delete all data on this device**, or delete the app. Data already in Apple Health is managed by you in the Health app |
| **Appeal** | Appeal if we refuse a request | Reply to our response, or email **admin@prameya.legal** with "Appeal" in the subject. We will respond in writing within 45 days |

**How to make a request.** Email **admin@prameya.legal** with "Consumer health data request" in the subject line. We do not require an account, and we will not ask you to create one.

**Timing.** We will respond **within 45 days of receiving your request**. If we need more time, we may extend once by a further 45 days, and we will tell you within the first 45 days that we are doing so and why.

**Cost.** Free, up to twice a year, as the law provides.

---

## 10. If we refuse — appeal, and then the regulator

If we decline to act on your request we will tell you why, and we will give you a way to appeal. Appeal by replying to our decision, or by emailing **admin@prameya.legal** with "Appeal" in the subject line. **We will decide an appeal within 45 days of receiving it** and explain the reasons in writing.

If the appeal is denied, we will provide a link or a means to submit a complaint to your state Attorney General:

- **Washington:** the Attorney General's office accepts consumer complaints online at [atg.wa.gov/file-complaint](https://www.atg.wa.gov/file-complaint).
- **Nevada:** the Attorney General's Bureau of Consumer Protection accepts complaints at [ag.nv.gov](https://ag.nv.gov/).

Washington residents should also know that a violation of the My Health My Data Act is an unfair or deceptive act under the Washington Consumer Protection Act (RCW ch. 19.86), which carries a private right of action under **RCW 19.86.090**. Nevada's law is enforced by the Attorney General and does not provide a private right of action.

---

## 11. Changes to this policy

If we change this policy, we will update the "Last updated" date above and publish the new version at [prameyallc.github.io/privacy/omnisalub/health-data](https://prameyallc.github.io/privacy/omnisalub/health-data/).

If a change ever means we begin to collect consumer health data, we will say so in plain terms, obtain consent where the law requires it, and publish it before the version that does so is released — not after.

---

## 12. Contact

**admin@prameya.legal**
Prameya LLC
Postal address available on request by email.

For everything else — security, exports, deletion, children, HIPAA, and what OmniSalub is and is not — see the [OmniSalub Privacy Policy](https://prameyallc.github.io/privacy/omnisalub/). Other Prameya app policies are listed at [prameyallc.github.io/privacy](https://prameyallc.github.io/privacy/).

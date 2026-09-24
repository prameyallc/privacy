# OmniSalub Consumer Health Data Privacy Policy

**Effective date:** 23 September 2026
**Last updated:** 23 September 2026
**Publisher:** Prameya LLC ("Prameya", "we", "us")
**Applies to:** OmniSalub for iPhone, iPad, Mac, Apple Vision Pro and Apple TV (bundle identifier `legal.prameya.omnisalub`), and the OmniSalub Apple Watch app (`legal.prameya.omnisalub.watchkit`)
**Contact:** admin@prameya.legal

This is a **separate, distinctly-labelled consumer health data privacy policy**, published as required by Washington's My Health My Data Act (RCW ch. 19.373) and drafted to satisfy Nevada's consumer health data law (SB 370, NRS ch. 603A) at the same time. It sits alongside — and does not replace — the [OmniSalub Privacy Policy](https://prameyallc.github.io/privacy/omnisalub/).

If you are a Washington or Nevada resident, this is the document written for you. Everyone else is welcome to read it; it describes what actually happens either way.

---

## The short version

**We do not collect, receive, store, share, sell or process any consumer health data.** OmniSalub has no servers. What you record, and what the app imports from Apple Health with your permission, stays in the app's private storage on your own device, and — only if you allow it — in your own Apple Health account, which Apple operates and we cannot read. Ask, the app's assistant, runs on your device and sends nothing to us.

Apple's App Privacy nutrition label for this app is **Data Not Collected**. That matches this policy: Prameya LLC is not a recipient of your health data.

The sections below answer each disclosure the statute asks for, including the ones where the honest answer is "none". We have written those out rather than omitting them, because a missing element and a "none" element look identical to a reader and are not the same thing.

The 21 August 2026 revision retracted an earlier published table that listed thirteen categories under "consumer health data we collect". That table described what the **app stores on your device**, not what Prameya collects. Publishing both framings under the same statutory heading was SALUB-072. The governing answer is **None**.

---

## 1. Categories of consumer health data we collect, and the purpose of collection

**None.**

The app records and imports measurements, symptoms and settings that *would* be consumer health data if we received them. We do not receive them. There is no account, no server of ours, no analytics endpoint, no advertising SDK, and no code path that transmits what you record to us. The few paths that do move data off the app's own storage are described in section 8: they go to Apple Health, between your own devices through Apple's services, or wherever you choose to send an export — never to Prameya. Data written to Apple Health is written into *your* Apple account under Apple's terms, not ours.

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

- **Apple Inc.** — operates the App Store, Apple Health, iCloud, Handoff, the connection between iPhone and Apple Watch, and Apple Intelligence. In detail:
    - If you turn on settings sync, six non-health preferences (theme, guideline set, onboarding state, app lock, the tab you last had open, and a timestamp) are stored in *your* iCloud account. Health data is never placed in iCloud; that is a fixed architectural boundary and an automated test enforces it.
    - **Handoff** passes the tab you are on and, if you are reading a Learn topic, that topic's identifier (for example a topic about PSA test numbers) to your own nearby devices signed in to the same Apple Account. It never carries a reading.
    - The **Apple Watch** app's **Ask iPhone** sends the question you type to OmniSalub on your paired iPhone, and the answer — which can draw on what you have logged — comes back to the Watch, over Apple's connection between your two devices.
    - Where **Apple Intelligence** answers Ask, it uses Apple's on-device model. The app does not send your question or your logged data to Apple's servers or to Private Cloud Compute.
    - If you buy OmniSalub Pro, the App Store processes the purchase. That is not consumer health data (section 9).
- **Hugging Face, Inc.** — hosts the optional on-device language model's files. If, and only if, you choose to download the model, your device downloads those files. That request carries the model's repository identifier, the names of the files requested, standard request headers that name the app, and your IP address. It carries no health data of any kind, and we are not a party to it.

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

- **What the app handles on your device.** The readings and symptoms you enter; the Apple Health data types you allow when you tap **Connect Apple Health** — the sheet lists only the types the conditions you track use, and the app imports the last 400 days of each type you allow (symptom records in full), together with what Apple Health says about the app and device that recorded each reading (the full list is in section 3.1 of the [OmniSalub Privacy Policy](https://prameyallc.github.io/privacy/omnisalub/)); the alerts the app raises; the conditions you choose; your visit date and visit questions; and your answer to the food-and-weight screening question. None of it reaches us.
- **Where.** In a database in the app's private storage on your device. On iPhone, iPad and Apple Vision Pro it is set to Data Protection "complete", so it is encrypted with a key derived from your device passcode and is unreadable while the device is locked. On a Mac it is protected by the app sandbox and by FileVault if you have FileVault on. Apple Health exists only on iPhone and iPad; the Apple Watch and Apple TV apps keep no readings.
- **Not in iCloud.** Health data is never stored in iCloud by this app. The health database is created with iCloud syncing explicitly disabled, and an automated test blocks any health record, or any health-revealing field, from reaching the part of the app that does sync. Only six non-health preferences (theme, guideline set, onboarding state, app lock, the tab you last had open, timestamp) can sync, and only if you turn that on — it is off by default. Only while settings sync is on, the app also writes a small "where you left off" note (the tab you were on, the identifier of the Learn topic you last opened, your appearance choice) through Apple's iCloud key-value storage, and turning sync off removes it; this version of the app is not signed with Apple's iCloud key-value storage capability, so the note does not leave the device.
- **Handoff and Apple Watch.** Handoff passes the tab and Learn topic identifier described in section 4 between your own devices; the Watch app's Ask iPhone passes your question and the answer between your Watch and your iPhone. Both use Apple's services between your own devices and reach no one else.
- **Backups.** The health database is excluded from device backup. So is the widget's display file. That file names what to log next and, only if you turn on **Show today's reading on the Home Screen** (off by default), holds today's latest reading. On iPhone and iPad it is encrypted at rest until the first time you unlock the device after a restart, rather than being re-locked whenever the screen locks, so the widget can redraw; the widget hides the number while the device is locked.
- **Ask.** Ask is on by default. It gives your question and a summary of what you have logged — the names of the conditions you track, reading summaries and up to 36 readings from the last 30 days, up to 12 symptoms, and any open alert below the urgent level — to a model running on your device: Apple Intelligence's on-device model where it is ready, or the optional model you download. That context never leaves your device and is not sent to us, to Apple or to any AI provider. Crisis language never reaches a model, and while an urgent or emergency alert is open Ask shows that alert's fixed text instead of asking one. The conversation is not saved. You can turn Ask off in Settings → Assistant. Cloud and third-party inference modes are hard-wired off in this version.
- **Notifications.** Visit reminders are off until you turn them on. They are local notifications scheduled on your device, do not name a condition, and no notification content is transmitted anywhere.
- **Retention.** Your data stays until you delete it. We retain nothing, so there is no retention schedule on our side to describe.

---

## 9. Subscription tiers and consumer health data

### No new collection when you subscribe

OmniSalub has a free tier and one paid upgrade, **OmniSalub Pro**, sold as Monthly, Annual or Lifetime; all three unlock the same Pro. **Upgrading does NOT trigger new consumer health data collection.**

Free and Pro:
- Process the same categories of consumer health data (section 8)
- Use consumer health data for the same purpose (operating features you choose to use)
- Store data in the same location (on your device)
- Transmit data to the same recipients (none — no health data leaves your device to us or to anyone we choose)

**Pro unlocks features. It does not change what data is collected, how it is processed, or where it goes.**

### What changes between tiers

| What Pro affects | What Pro does NOT affect |
|---------------------------|-----------------------------------|
| How much history the app shows (90 days free, up to 400 days with Pro); older readings stay on your device either way | What health data types are read from Apple Health |
| Which export formats are available (free: a raw CSV of readings and a CSV of symptoms; Pro adds a PDF visit summary, a formatted CSV and a FHIR bundle) | Where health data is stored (on-device in both tiers) |
| | Whether health data syncs to iCloud (never, in either tier) |
| | Whether settings sync is available (the same opt-in in both tiers) |
| | Ask, which works the same in both tiers |

### StoreKit data is not consumer health data

When you buy or restore Pro, Apple's StoreKit on your device completes the purchase with the App Store and, each time the app starts, tells the app which Pro products your Apple Account is entitled to. **That is a payment record, not consumer health data** under RCW 19.373.010.

- It does not identify your health status, condition, disease, or treatment.
- It is used only to turn the Pro features on or off.
- The app keeps no purchase record of its own and sends nothing about a purchase to us. Apple keeps the record, so "Delete everything this app stored" does not remove it.

An earlier version of this section described Plus and Premium tiers, automatic Apple Health sync, device integrations and a locally stored transaction record. None of those describes the app.

Apple separately processes your Apple Account ID and payment method when you subscribe. That processing is governed by Apple's terms, not ours.

---

## 10. How to exercise your rights

Washington residents have the rights below under RCW 19.373.040. Nevada residents have broadly parallel rights under Nevada SB 370. We honour these requests from anyone who asks, regardless of where they live.

| Right | What it means | How to use it |
|---|---|---|
| **Confirm and access** | Confirm whether we are collecting, sharing or selling your consumer health data, and get access to it | Email **admin@prameya.legal**. The answer will be that we hold none. Your actual data is visible in the app at any time, and exportable as a raw CSV of readings and a CSV of symptoms, or with Pro as a PDF, formatted CSV or FHIR bundle |
| **List of recipients** | Get a list of the third parties and affiliates your data has been shared with | Email us. The list is empty |
| **Withdraw consent** | Withdraw consent to collection and to sharing | There is no consent to withdraw from us. Permissions the app itself uses are yours to revoke in **Settings → Privacy & Security → Health → OmniSalub**; settings sync, visit reminders and Ask (**On-device assistant**) can be turned off in the app's own Settings |
| **Delete** | Have your consumer health data deleted | Because we hold nothing, there is nothing for us to delete. On your device: **Settings → Your data → Delete everything this app stored** erases your readings, symptoms and alerts, resets your conditions, visit date and preferences, deletes your iCloud copy of your settings if sync is on, and clears the activity log down to one entry recording the erase; it keeps the downloaded Ask model and its settings, your iCloud sync choice and anything in Apple Health (the full list is in section 14 of the OmniSalub Privacy Policy). Deleting the app removes everything the app stored on that device. Data already in Apple Health is managed by you in the Health app |
| **Appeal** | Appeal if we refuse a request | Reply to our response, or email **admin@prameya.legal** with "Appeal" in the subject. We will respond in writing within 45 days |

**How to make a request.** Email **admin@prameya.legal** with "Consumer health data request" in the subject line. We do not require an account, and we will not ask you to create one.

**Timing.** We will respond **within 45 days of receiving your request**. If we need more time, we may extend once by a further 45 days, and we will tell you within the first 45 days that we are doing so and why.

**Cost.** Free, up to twice a year, as the law provides.

---

## 11. If we refuse — appeal, and then the regulator

If we decline to act on your request we will tell you why, and we will give you a way to appeal. Appeal by replying to our decision, or by emailing **admin@prameya.legal** with "Appeal" in the subject line. **We will decide an appeal within 45 days of receiving it** and explain the reasons in writing.

If the appeal is denied, we will provide a link or a means to submit a complaint to your state Attorney General:

- **Washington:** the Attorney General's office accepts consumer complaints online at [atg.wa.gov/file-complaint](https://www.atg.wa.gov/file-complaint).
- **Nevada:** the Attorney General's Bureau of Consumer Protection accepts complaints at [ag.nv.gov](https://ag.nv.gov/).

Washington residents should also know that a violation of the My Health My Data Act is an unfair or deceptive act under the Washington Consumer Protection Act (RCW ch. 19.86), which carries a private right of action under **RCW 19.86.090**. Nevada's law is enforced by the Attorney General and does not provide a private right of action.

---

## 12. Changes to this policy

If we change this policy, we will update the "Last updated" date above and publish the new version at [prameyallc.github.io/privacy/omnisalub/health-data](https://prameyallc.github.io/privacy/omnisalub/health-data/).

If a change ever means we begin to collect consumer health data, we will say so in plain terms, obtain consent where the law requires it, and publish it before the version that does so is released — not after.

**23 September 2026 — what changed.** Our answer is unchanged: Prameya collects, shares and sells no consumer health data. This revision updates the facts behind it:

- Section 8 now lists what the app handles on your device, and says that **Connect Apple Health** asks only for the types the conditions you track use and imports the last 400 days of each type you allow (symptom records in full).
- Section 8 describes Ask, which is on by default and uses Apple Intelligence's on-device model or the optional downloaded model, and what it is given; the "where you left off" note; Handoff; the Apple Watch app's Ask iPhone; visit reminders; and the widget's reading, now off by default.
- Section 4 lists Apple's services in more detail and what the Hugging Face request carries.
- Section 9 replaces a description of Plus and Premium tiers, automatic Apple Health sync, device integrations and a locally stored purchase record — none of which describes the app — with the free tier and Pro as they are.
- Section 10 describes **Delete everything this app stored** and what it keeps.
- The policy now covers Apple Vision Pro, Apple Watch and Apple TV.
- Later the same day, the app was fixed and this page updated to match: Connect Apple Health had been asking for every type any condition programme can use, whichever conditions you chose, and now asks only for those your conditions use; the "where you left off" note is written only while settings sync is on; and **Delete everything this app stored** now deletes your iCloud copy of your settings rather than resetting it and clears the activity log. None of this changed our answer: we still collect no consumer health data.

---

## 13. Contact

**admin@prameya.legal**
Prameya LLC
Postal address available on request by email.

For everything else — security, exports, deletion, children, HIPAA, and what OmniSalub is and is not — see the [OmniSalub Privacy Policy](https://prameyallc.github.io/privacy/omnisalub/). Other Prameya app policies are listed at [prameyallc.github.io/privacy](https://prameyallc.github.io/privacy/).

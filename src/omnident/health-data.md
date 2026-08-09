# OmniDent Consumer Health Data Privacy Policy

**Effective date:** 8 August 2026
**Publisher:** Prameya LLC, a United States limited liability company ("Prameya", "we", "us")
**Contact:** admin@prameya.legal
**This policy lives at:** https://prameyallc.github.io/privacy/omnident/health-data/
**Main OmniDent privacy policy:** https://prameyallc.github.io/privacy/omnident/
**All Prameya app policies:** https://prameyallc.github.io/privacy/

---

## Why this is a separate document

Washington State's **My Health My Data Act** (RCW ch. 19.373) requires any business that collects consumer health data to maintain a **consumer health data privacy policy that is separate and distinct** from its general privacy policy, and to link to it prominently. Nevada's **SB 370** (codified in NRS ch. 603A) imposes closely analogous duties.

This is that document. It applies to everyone who uses OmniDent, and it gives specific rights to residents of **Washington** and **Nevada**.

**It is separate from, and additional to, the [main OmniDent Privacy Policy](https://prameyallc.github.io/privacy/omnident/).** Read both. Both are also linked separately inside the app, in Settings.

---

## A note about the word "collect"

Apple's App Store privacy labels use "collect" to mean *transmitting data off the device*. Under that definition, OmniDent would collect very little.

**Washington's definition is much broader.** RCW 19.373.010 defines "collect" as to *buy, rent, access, retain, receive, acquire, infer, derive, or otherwise process* consumer health data **in any manner**. Data that never leaves your phone is still collected, because the app accesses, retains, processes and derives from it.

**We use Washington's definition throughout this document.** We do not use the narrow App Store definition to imply that state health-privacy law does not reach us. It does.

---

## Consumer health data collected, and why

RCW 19.373.020(1)(a)(i) requires us to state the categories of consumer health data collected and the purpose of collection, including how it will be used. Here is the complete list.

| Category | What it is | Why it is collected and how it is used |
|---|---|---|
| **Photographs of your oral cavity** | Images of your teeth, gums, tongue and mouth taken with the in-app camera, or selected by you from your photo library | So you can keep a dated visual record of your own mouth over time, and so the on-device AI can produce general educational information about what you are looking at |
| **Information derived from those photographs** | The output the on-device AI model produces about an image, and a capture-quality score | To show you educational information and to place a photo in your own timeline |
| **Oral-health profile** | Age, brushing frequency, sugar intake level, smoking status, whether you have diabetes, whether you have dry mouth, and the goals you choose | To tailor the general information and habit suggestions the app shows you |
| **Home-care habit logs** | Daily records of brushing, flossing, mouthwash use and sugary drinks | To show you your own streaks, trends and progress |
| **Programme progress** | Your progress through the in-app 30-day home-care programme | To let you resume where you left off |
| **Illustrative cost scenarios** | "What if" projections built from figures you enter, and any narrative text generated on-device alongside them | To let you explore an illustrative cost model. These are examples, not predictions about your health |
| **Bodily-function measurements from Apple Health** *(only if you turn it on)* | Step count, sleep analysis, mindful minutes, active energy burned | To show optional context alongside the habits you log |
| **Health data written to Apple Health** *(only if you turn it on)* | Toothbrushing events and dietary sugar entries you logged in the app | So your entries appear alongside the rest of your health data in Apple Health, under your control |

One clarification about the Studio screen's unfinished **Regenerative Projection** feature, because it shows percentages next to terms taken from your own scans: those percentages ("X–Y% chance of meaningful recovery in ~N months") are **fixed placeholder values written into the app**. They are not derived from your photographs, your profile or your habits, and they are not a prediction about your health. The terms listed come from your own on-device records; the numbers come from the app's source code.

**Purposes, stated completely.** All of the above is collected for one purpose: to operate the features of OmniDent that you choose to use, on your device, for you.

It is **not** used for advertising, for marketing, for profiling, for research, for training AI models, for sale, or for any secondary purpose whatsoever. There is no secondary purpose. If that ever changes, RCW 19.373.020(1)(d) requires us to disclose the new purpose and obtain your affirmative consent **before** processing for it, and we will.

---

## Sources of consumer health data

RCW 19.373.020(1)(a)(ii) requires the categories of sources. There are four, and all of them are you:

1. **You, directly** — habit logs, profile answers, goals, notes and cost-model inputs you type in.
2. **Your device's camera**, when you take a photo in the app.
3. **Your device's photo library**, when you pick a specific image to attach using the system photo picker. OmniDent receives only the image you pick and has no access to the rest of your library.
4. **Apple Health**, only if you grant permission, and only for the four read types listed above.

We obtain consumer health data from **no other source**. We do not buy it, rent it, receive it from data brokers, receive it from health care providers, infer it from third-party sources, or derive it from advertising identifiers.

---

## Where this data lives

- **On your device.** Photographs are stored as files in OmniDent's private app container, encrypted at rest by iOS Data Protection at the Complete level. Everything else is in the app's local database on the same device.
- **Not on any Prameya system.** Prameya operates no server that receives your consumer health data. We have no user database and no copy of anything described above.
- **Not sent for AI processing.** The AI runs on your device's own chip. Photographs and text are never transmitted for analysis.
- **Not in iCloud through OmniDent.** OmniDent's iCloud sync carries app preferences and interface state only. No health-derived field is in its sync schema, and the set of records permitted to sync is pinned by an allow-list in the app that switches sync off entirely if anything ever drifts from it.

One honest limit on that last point: OmniDent does not mark its scan folder as excluded from your device backup. If you back your device up to iCloud or to a computer, those files are included in **your own** backup, under your Apple Account or on your own machine, governed by Apple's terms rather than ours. That is your backup of your device, not a transfer of data to us or to anyone else by the app.

---

## Consumer health data that is shared, and with whom

RCW 19.373.020(1)(a)(iii) requires the categories of consumer health data shared, and (1)(a)(iv) requires a list of the categories of third parties and the specific affiliates we share it with.

**Categories of consumer health data shared: none.**

**Categories of third parties we share consumer health data with: none.**

**Specific affiliates we share consumer health data with: none.** Prameya LLC has no affiliates that receive it.

For completeness, here is every third party the app touches at all, and what each one gets:

| Third party | What they receive | Is it consumer health data? |
|---|---|---|
| **Apple** — iCloud / CloudKit | App preferences and interface state, held in **your** private iCloud database under **your** Apple Account | No |
| **Apple** — Sign in with Apple | The sign-in exchange, if you choose to sign in | No |
| **Apple** — Apple Health | Toothbrushing and dietary sugar entries you logged, written into **your** Health store on **your** device, if you turn it on | Yes, but this is a transfer into your own device's Health store at your instruction, not a disclosure to a third party for their use. Apple does not receive it from us for any purpose of theirs |
| **Hugging Face** | A request for an AI model file, when you tap Download | **No.** No photograph, no analysis, no habit data, no identifier of you |

There is no advertising network, no analytics vendor, no crash-reporting vendor, no data broker, no dental practice, no insurer, and no research partner in that list, because there is none in the app.

The Studio screen shows a toggle offering "private collective priors" with an optional anonymised contribution. **That feature is not built.** Turning it on only substitutes different fixed numbers already inside the app; nothing about you is transmitted to us or to anyone else, and no shared dataset exists.

**We have never shared consumer health data with anyone.**

---

## Selling consumer health data

**We do not sell consumer health data. We never have. We will not.**

Washington requires a signed, specific written authorization before any sale, valid for no more than one year and revocable (RCW 19.373.070). **We have never sought such an authorization from anyone and do not intend to.** Nevada imposes a parallel requirement, and the same answer applies.

If you are ever shown a document asking you to authorise the sale of your OmniDent health data, it did not come from us.

---

## Your rights

RCW 19.373.020(1)(a)(v) requires us to explain how you exercise the rights in RCW 19.373.040. Nevada provides closely comparable rights.

### 1. The right to confirm and access

You may ask whether we are collecting, sharing or selling your consumer health data, and to access it — including a list of all third parties and affiliates with whom we have shared it, and contact information for each.

**Fastest route (immediate, no waiting):** **Settings → Privacy & Security → Export My Data** in the app produces a JSON file of your on-device records — scan metadata, habit logs, trajectory scenarios and your profile — generated on your device. It contains metadata only: not the raw photographs, which are already in the app and, if you enabled auto-save, in your Photos library, and not the text of your notes.

**Formal route:** email **admin@prameya.legal**. We will confirm in writing that we hold no consumer health data about you on any Prameya system, that we have shared none, and that we have sold none.

### 2. The right to withdraw consent

You may withdraw consent to our collection and sharing of your consumer health data at any time, for any part of it or all of it.

| To withdraw consent to | Do this |
|---|---|
| Camera and photographs | iOS Settings → Privacy & Security → Camera → OmniDent, or simply stop taking photos |
| Photo library access | iOS Settings → Privacy & Security → Photos → OmniDent |
| On-device AI analysis | OmniDent → Settings → AI Models → turn AI features off |
| Apple Health, in either direction | iOS Settings → Health → Data Access & Devices → OmniDent, or OmniDent → Settings → Apple Health |
| iCloud sync | OmniDent → Settings → iCloud Sync → off |
| Everything at once | Delete the app. iOS removes its container and everything in it |

Withdrawing consent does not undo processing that already happened, and it does not by itself delete data. Use the deletion right for that.

### 3. The right to delete

You may have your consumer health data deleted, including from backups and archived systems. We must delete it from all parts of our network.

**Fastest route (immediate and permanent):**

| To delete | Where |
|---|---|
| A single photograph | Scan details → Delete |
| All app data on this device, including your oral-health profile | Settings → Privacy & Security → Delete All Scans & Data |
| Your Sign in with Apple association, the app's records in your private iCloud database, and all local data | Settings → iCloud Sync → Delete Account & All Data |
| Data written into Apple Health | The Apple Health app |
| Photographs copied into your Photos library | The Photos app |

On that third row, one thing should be stated precisely rather than implied. Apple's deletion rule for apps offering Sign in with Apple also requires token revocation **where the app exchanges Apple's authorization code for tokens on its own server**. OmniDent has no server and never performs that exchange, so no Apple token for OmniDent exists and the app makes no revocation call — the app-scoped identifier in your device's Keychain is the entire association, and deleting it is the entire deletion. If you also want OmniDent removed from your Apple Account's Sign in with Apple list, that is Apple's own control, at **iOS Settings → your name → Sign in with Apple → OmniDent**.

**Formal route:** email **admin@prameya.legal**. Because we hold no consumer health data on any Prameya system, there is nothing on our side to delete and no backup or archived copy of it anywhere in our network. We will confirm that in writing. Washington permits up to six months for deletion from archived or backup systems solely to allow restoration; **we have no such systems containing your consumer health data**, so that extension never applies to us. Backups you make of your own device are yours, held under your Apple Account or on your own computer, and we cannot reach into them.

### 4. Timing, and how to appeal

- We respond to a request **within 45 days** of receiving it.
- We may extend once by a further **45 days** where reasonably necessary given the complexity or number of your requests. If we do, we will tell you within the first 45 days and explain why.
- **If we refuse to act on your request**, we will tell you why, without undue delay and within the same 45 days, and we will tell you how to appeal.
- **To appeal**, reply to our response or email **admin@prameya.legal** with "Appeal" in the subject line. A different person than the one who handled the original request will review it. We will decide the appeal and give you a written explanation within a reasonable time.
- **If we deny your appeal**, we will provide you with a method to contact the **Washington State Attorney General** to submit a complaint. You can reach the Washington Attorney General's consumer protection division at **atg.wa.gov**. Nevada residents may complain to the **Nevada Attorney General** at **ag.nv.gov**.

### 5. Verifying who you are

We will not ask you for identity documents. We cannot match them against anything, because we hold no record of you. If you email us, we will correspond with you at the address you wrote from. We will not ask you to create an account or provide additional personal information in order to make a request — doing so would mean collecting more data than we hold in the first place.

**We will not discriminate against you** for exercising any right in this policy. There is no paid tier that depends on your data, and no feature is withheld because you said no.

---

## Geofencing

**We do not use geofencing.**

Washington makes it unlawful to implement a geofence around any entity providing in-person health care services in order to identify or track consumers, collect consumer health data, or send them health-related advertisements or notifications (RCW 19.373.080).

OmniDent does not request location permission, does not have a location entitlement, contains no geofencing code, sends no marketing notifications, and shows no advertisements of any kind. There is no geofence around a dental office, a hospital, a pharmacy, or anywhere else.

---

## Nevada residents (SB 370)

Nevada's consumer health data law, enacted as SB 370 and codified in NRS ch. 603A, took effect on 31 March 2024. Its duties closely track Washington's.

Everything in this policy applies to you:

- The categories of consumer health data, sources, purposes and uses set out above are the same.
- We do not share your consumer health data with any third party.
- **We do not sell your consumer health data**, and we have never sought the separate written authorization Nevada requires for a sale.
- You have the right to confirm whether we collect, share or sell your consumer health data, the right to access it, the right to have it deleted, and the right to withdraw consent to its collection and sharing. Use the same routes described above.
- You may complain to the Nevada Attorney General at **ag.nv.gov**.

---

## Processors

RCW 19.373.020(1)(e) requires that any contract with a processor be consistent with this policy.

**We use no processor for consumer health data.** There is no vendor, no contractor, no cloud provider and no analytics service that processes your consumer health data on our behalf, because your consumer health data never reaches us to hand on. If that ever changes, we will name the processor in this policy, bind it by contract to these terms, and — where the law requires it — obtain your consent first.

---

## Employees and contractors

Access to consumer health data is restricted to those who need it to provide the service. In practice that number is **zero**: no Prameya employee or contractor can access your consumer health data, because it exists only on your device and we have no channel to it.

---

## Enforcement

A violation of Washington's My Health My Data Act is a violation of the Washington Consumer Protection Act, RCW ch. 19.86. That means it may be enforced by the Washington State Attorney General and may also be pursued by an individual under **RCW 19.86.090**.

We take that seriously, and it is the reason this document describes what the app actually does rather than what would be convenient to claim. Where a statement here would otherwise depend on a change that has not shipped, we describe the behaviour of the app as it exists today instead — including where that is less flattering.

---

## Changes to this policy

If we change the categories of consumer health data we collect, add a source, add a purpose, or add anyone we share it with, we will:

1. update this policy and change the effective date;
2. **obtain your affirmative consent before collecting or processing for the new category or purpose**, as RCW 19.373.020(1)(c) and (1)(d) require — before the change takes effect, not after;
3. show an in-app notice describing what changed.

**This 8 August 2026 revision was a correction pass rather than a change of practice.** We re-read the shipping source code and rewrote every statement that did not match it. The deletion section previously said that deleting your account revokes your Sign in with Apple token; it does not, because the app has no server, never exchanges the authorization code, and therefore has no token in existence to revoke. That section now states what deletion actually does. We also corrected the name of the deletion control, described the placeholder percentages in the Studio Regenerative Projection feature, noted that scan files are not excluded from your own device backup, described the export file accurately, and confirmed the statements that had been pending internal verification and are now true of the build. Nothing in this document now describes a feature that has not shipped.

Previous versions are available on request. We do not make material changes quietly.

---

## Contact

**Prameya LLC**
Consumer health data requests, questions, appeals and complaints: **admin@prameya.legal**

Put "Health data request" or "Appeal" in the subject line so it is routed correctly.

Main OmniDent privacy policy: https://prameyallc.github.io/privacy/omnident/
All Prameya app privacy policies: https://prameyallc.github.io/privacy/
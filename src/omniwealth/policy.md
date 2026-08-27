# OmniWealth Privacy Policy

**Effective date:** 23 August 2026
**Publisher:** Prameya LLC ("Prameya", "we", "us"), a United States limited liability company
**Contact:** admin@prameya.legal
**Applies to:** the OmniWealth iOS and macOS app

This policy covers OmniWealth only. Other Prameya apps have their own policies, listed at [prameyallc.github.io/privacy](https://prameyallc.github.io/privacy/). Do not assume a statement here is true of any other app.

---

## The short version

| Question | Answer |
|---|---|
| Do you have accounts or logins? | No. There is nothing to sign up for. |
| Where does what I log live? | On your device, in the app's own storage. |
| Does Prameya receive it? | No. We run no server that could receive it. We have no database of users. |
| Does the app connect to the internet? | Not for your data. There is no model download and no Hugging Face traffic in this build. Opening the privacy-policy link uses your browser. |
| Is my financial information sent to an AI service? | No. There is no AI advisor, no on-device model, and no cloud AI provider. |
| Do you use ads, analytics, or trackers? | No. None. |
| Do you connect to my bank or brokerage? | No. The app has no ability to link a financial account. |
| Do you sell or share my data? | No. We do not have it. |
| Does the app read my Health data? | No. |
| Is this financial advice? | No. OmniWealth is educational only. |

---

## What OmniWealth is, and what it is not

OmniWealth is a personal-finance **education and habit-tracking** app. It explains general concepts — how fees work, what diversification means, how compounding arithmetic works — and it lets you log your own habits and a simple envelope / budget log you type yourself.

OmniWealth is **not** an investment adviser, a broker, a financial planner, a robo-adviser, or an AI advisor. It does not recommend, rate, or rank any stock, fund, ETF, or ticker. It does not build you a portfolio, tell you to buy, sell, hold, or rebalance anything, or produce advice tailored to your circumstances. Nothing in the app is investment, tax, or legal advice. For decisions about your money, talk to a qualified professional.

We mention this in a privacy policy for a reason: because the app gives no personalised advice, it never needs to build a profile of you, and it never does. **There is no Goals surface** in this build.

---

## Available tiers

There is one paid upgrade, **OmniWealth Pro**, sold as three products. Buying any one of
them grants exactly the same Pro — there are no separate feature tiers.

| Product | Price (US) | Billing |
|---|---|---|
| OmniWealth Pro Monthly | $4.99 | Auto-renews monthly. 7-day free trial. |
| OmniWealth Pro Annual | $29.99 | Auto-renews yearly. 7-day free trial. |
| OmniWealth Pro Lifetime | $79.99 | One-time purchase. Not a subscription. |

Family Sharing is enabled on all three. Subscriptions renew until you cancel in
Settings; Lifetime is a one-time non-consumable.

**The knowledge layer is free and stays free.** Without paying anything you get
the full concept library and the basic calculators, with no account and no time limit. Pro adds saved scenarios, envelopes and worksheet export.

**Pro does not add cloud sync, and there is no paid iCloud option.** OmniWealth stores your
records on your device in every case, paid or not. If a subscription lapses you keep your
own data and can still export it in its raw form; only the Pro tools stop.


## Free vs paid tier data collection

**The tier you choose does not change what data Prameya collects from OmniWealth.** In both the free tier and Premium:

- Your habit logs, envelope entries, and compounding calculations stay on your device
- No analytics, tracking, or telemetry
- No server that receives your content
- No account or login

The difference between tiers is **feature access**, not data handling. Premium unlocks additional tools; it does not unlock data transmission.

## Cancellation and refunds

Subscriptions are managed entirely through your Apple ID:

- **To cancel:** Open Settings on your iPhone or iPad → tap your name → Subscriptions → OmniWealth → Cancel Subscription. On Mac, open the App Store app → Account (sign-in name) → View Information → Subscriptions → Manage.
- **Refund requests:** Handled by Apple, not Prameya. See [reportaproblem.apple.com](https://reportaproblem.apple.com/) or contact Apple Support. We have no access to your payment information and cannot issue refunds ourselves.
- **What happens to your data when you cancel:** Nothing. Your on-device data stays on your device. Canceling a subscription removes access to Premium features; it does not delete your habit logs or budget entries.

## StoreKit transaction data

The anonymized StoreKit transaction record described above is stored in the app's local database on your device. It is used to determine which features to unlock. It is never uploaded to Prameya, and it is deleted when you delete the app or use the "Delete all data in this app" control in Settings.

If you restore purchases on a new device (by tapping "Restore Purchases" in the app), StoreKit queries Apple's servers to retrieve your active subscriptions. That communication is between your device and Apple; Prameya is not involved and sees nothing from it.

---

## What stays on your device

Everything you enter into OmniWealth is stored locally on your device and stays there.

| What you can enter today | Examples | Where it goes |
|---|---|---|
| Daily habit checklist | Four yes/no toggles — whether you reviewed your budget, made a planned contribution, reviewed your allocation, avoided an impulse purchase — recorded with the date | Local app database |
| Envelope / budget log | A name you type and amounts you log (assigned vs spent). Arithmetic on that envelope, not a recommendation | Local app database |
| Compounding arithmetic inputs | The monthly amount, number of years, and the annual rate you choose to test | Held in memory while that screen is open; not saved to the database |
| App preferences | Appearance setting, whether you have acknowledged the disclosure, and whether the weekly check-in reminder is on | Device settings storage |

There is no Goals form, no income form, and no place to type a question for an advisor. The app's local database additionally defines leftover record types (statement scans, trajectory snapshots, a goal-profile row) from features that are **not** in the shipping UI. No screen creates a Goals surface. They are named here only because the delete control described below clears them too.

This data is written to the app's private storage area, which iOS and macOS protect from other apps. It is never uploaded to Prameya. We could not read it if we wanted to.

**Financial information is sensitive.** We treat it that way. The design principle for OmniWealth is that the safest place for your money data is the device in your hand, and the safest amount for us to hold is none.

---

## What leaves your device

**No Hugging Face or model-download traffic.** Earlier versions of this page described an on-device AI model you could download from `huggingface.co`. That offer is not in the app, and the unused download / inference code was deleted. There is no control that starts a download, and no screen that sends a question to a model. If on-device generation is ever added, this policy is rewritten first.

**Local notifications.** Notification permission is requested only from **Settings → Reminders**, never at launch. If you continue and grant it, the app schedules one weekly local check-in that says “Time for this week's check-in.” It is not a performance claim. Turning the reminder off cancels it.

**There is no iCloud sync.** Both of the app's data stores are created with cloud syncing disabled, and the app holds no iCloud entitlement. If you use OmniWealth on two devices, the two copies are separate.

The summaries the app shows you — how many days you logged, how many boxes you ticked, remaining cents on an envelope — are counts of your own records, produced by ordinary arithmetic on your device. There is no chat feature, no question box, and no AI advisor.

---

## What we do not do

Each of these is a flat "no", not a "we limit this":

- **No accounts.** No sign-up, no email, no password, no Sign in with Apple.
- **No Prameya server.** We operate no backend that receives app data. There is no user database to breach, subpoena, or sell.
- **No analytics or telemetry.** No usage tracking, no session recording, no crash-reporting service.
- **No advertising.** No ad networks, no ad identifier (IDFA), no App Tracking Transparency prompt, because there is nothing to track.
- **No selling or sharing of personal information**, in the ordinary meaning or in the specific meanings those terms carry under California law.
- **No bank, brokerage, or credit connections.** The app cannot link to a financial institution, and there is no data aggregator (such as Plaid) in it. It never sees an account number, a balance feed, or a transaction feed. Anything about your money is there because you typed it.
- **No credit checks, credit scores, or credit reports.**
- **No purchases or transfers.** The app cannot move money.
- **No location tracking.**
- **No contacts, calendar, or microphone access.**
- **No Keychain storage.** The app puts nothing in the device Keychain.
- **No camera or photo library access, and no document import.** The app cannot ingest a photo or PDF of a statement. There is no capture or import path in it, and it does not hold the file-access entitlement that would allow one.
- **No AI advisor and no model download.**

On the document-import point, plainly: an earlier build shipped copy that referred to "uploaded statements," and the app's database still defines an unused record type for statement scans. That copy has been corrected, and no screen in the shipping app can capture or import a document. If a statement-import feature ships later, this policy will be updated to describe photo or file access before it is used, and the App Store privacy label updated with it.

---

## iCloud and syncing

**OmniWealth does not sync your financial or habit data to iCloud.** Your data is stored in a local, non-syncing database on the device where you entered it. If you use OmniWealth on two devices, the two copies are separate and do not share data.

This is enforced in two places, not just described: the app's local databases are created with cloud syncing explicitly disabled, and the signed app no longer carries any iCloud or CloudKit entitlement or container, so it could not write a record to iCloud even if code tried to.

If we ever add sync, it will be **off by default**, will require you to switch it on, and this policy will say exactly which fields sync before it ships.

---

## Health data: we do not process it

OmniWealth does not collect, receive, access, derive, or infer any health data. It does not read Apple Health, it has no Health integration, it asks you nothing about your health, and it makes no inference about your physical or mental condition from your spending.

The shipping app carries no HealthKit entitlement, no Health usage description, no HealthKit framework, and no Health code of any kind.

This matters legally, not just descriptively. Washington's My Health My Data Act (RCW ch. 19.373) and Nevada's consumer health data law (SB 370, 2023) define "consumer health data" and "collect" very broadly — broadly enough to reach data that is merely accessed, processed, or derived, not only data that is transmitted to a company. Because OmniWealth does none of those things with health data, those statutes do not apply to it, and no separate consumer health data privacy policy is required for this app.

We say this plainly because earlier internal versions of this app's technical configuration wrongly labelled budget and habit logs as "health" data, and an earlier build displayed placeholder step and sleep numbers that were hardcoded rather than read from Health. That label was a mistake and the placeholder feature is gone. **Budgeting information is financial information, not health information.** The app's privacy manifest now declares no collected data types at all.

## HIPAA does not apply

HIPAA (45 CFR Parts 160 and 164) governs health plans, health care clearinghouses, most health care providers, and their business associates. Prameya is none of those, OmniWealth handles no health information, and you have no patient relationship with us. **HIPAA does not apply to this app, and we do not claim HIPAA compliance.**

---

## Permissions the app asks for

OmniWealth asks for no runtime permissions for location, camera, photos, contacts, Health, or tracking, because the app uses none of those.

Notification permission is requested only from **Settings → Reminders**, never at launch. If you grant it, the app schedules one weekly local check-in. Turning the reminder off cancels it.

---

## Children

OmniWealth is a general-audience product for adults managing their own money. It is not directed to children, it is not designed to appeal to children, it contains no advertising, and it collects no personal information from anyone — including anyone under 13. Because the app transmits no personal information to us at all, there is nothing that COPPA (15 U.S.C. §§6501–6506; 16 CFR Part 312) would require us to obtain parental consent for.

If you are a parent or guardian and have a question about this app, write to admin@prameya.legal.

---

## Your choices and controls

Because your data never leaves your device, you control it directly.

- **See it:** your logged days and envelope arithmetic are shown in the app.
- **Delete everything you have entered:** Settings → Data → **"Delete all data in this app"**. After a confirmation prompt, this permanently deletes every habit log, envelope / budget entry, leftover statement record and profile stored on this device, plus leftover on-device model cache from older installs (and the App Group container if one is ever entitled). If a later file removal fails after the store is emptied, the app says so rather than claiming a complete delete. It cannot be undone.
- **Deleting one entry at a time is not possible.** The app does not currently offer per-entry deletion — there is no swipe-to-delete and no delete control on an individual row. Deletion is all-or-nothing: the control above, or deleting the app.
- **Delete everything, including preferences:** delete the app. That removes the app's local database and its preferences from your device.
- **Ask us to delete your data:** there is nothing for us to delete. We have never received it. If you write to us asking for deletion, that will be our honest answer.

---

## Your privacy rights

We honour the rights below regardless of whether Prameya meets the size thresholds that make those laws mandatory for a company. In practice, the honest answer to most requests is the same: **we do not hold your personal information**, so there is nothing to disclose, correct, delete, or opt out of.

### California (CCPA/CPRA)

If you are a California resident, the California Consumer Privacy Act as amended by the CPRA (Cal. Civ. Code §1798.100 et seq.) gives you the rights to know, delete, correct, opt out of sale or sharing, and limit the use of sensitive personal information.

Our position for OmniWealth:

- **Personal information we collect:** none. The app transmits nothing about you to us.
- **Sensitive personal information we collect:** none. California's definition of sensitive personal information (Cal. Civ. Code §1798.140(ae)) includes certain financial data, such as an account number together with an access code. OmniWealth never receives any of it — it has no account linking, and we receive nothing you enter.
- **Sale or sharing of personal information:** we do not sell or share personal information, and we never have. We do not use or disclose sensitive personal information for any purpose that would trigger the right to limit.
- **Retention:** we retain nothing, because we receive nothing. Your own data stays on your device until you delete it.
- **Non-discrimination:** we do not treat anyone differently for exercising a privacy right.

To exercise any right, or to ask us to confirm the above in writing, email admin@prameya.legal. We will respond within the time the statute requires.

### Washington and Nevada

Washington's My Health My Data Act and Nevada's SB 370 apply to consumer health data. As explained above, OmniWealth processes none, so neither statute reaches it and there is no separate consumer health data policy for this app. (Washington's Act is enforceable by consumers through the state Consumer Protection Act, RCW 19.86.090 — a real risk we take seriously, and the reason we would rather state clearly that we hold no health data than rely on a technicality.)

### Other US states

Several other states have comprehensive privacy laws granting access, correction, deletion, portability, and opt-out rights, and treating precise financial account data as sensitive. Our answer under all of them is the same: we do not collect, sell, share, or process your personal information, and we do no profiling or targeted advertising. Write to admin@prameya.legal with any request.

### If you are in the UK, EU, or EEA

This policy does not state which App Store territories OmniWealth is released in; check the App Store listing for the countries where it is available.

Where the UK GDPR or EU GDPR applies, note that Prameya does not act as a controller of any personal data from your use of OmniWealth, because we receive none. Your entries are processed only by software running on your own device, under your control. We do not process special category data (GDPR Article 9); financial information is not a special category, and we hold no health data in any event. If you believe we hold personal data about you, contact admin@prameya.legal, and you may complain to your national data protection authority.

---

## Security

- Your data is stored in the app's private storage, which the operating system isolates from other apps, and is protected by your device passcode and disk encryption. That is the operating system's default protection; the app does not add a stronger file-protection class on top of it, and we will not describe it as more than it is.
- There is no model download in this build, so there is no Hugging Face request to encrypt.
- The strongest control is architectural: there is no server holding your financial information, so there is no server to be breached.

We do not claim any security certification, audit, or standard we do not hold.

---

## Third parties

| Third party | Role | What it receives |
|---|---|---|
| Apple | Distributes the app | Whatever Apple collects for App Store distribution, under Apple's own privacy policy. We receive no personal information from Apple. |

There are no others. No analytics vendor, no ad network, no cloud AI provider, no data broker, no payment processor.

The app ships Apple platform frameworks and in-repo Swift packages only. MLX and Hugging Face libraries were removed; they are not linked.

---

## Changes to this policy

If we change how OmniWealth handles data, we will update this policy before the change ships, not after. When we do:

- We will change the effective date at the top.
- We will describe what changed in plain language.
- The previous version will remain available at this address's history.

**This revision (23 August 2026)** records the shipping envelope / budget log (a name and amounts you type; arithmetic only) and states that there is no Goals surface and no AI advisor. Hugging Face / on-device model download claims stay removed: the unused Intelligence / MLX stack is deleted. Notification permission is requested from Settings → Reminders only.

Material changes — for example, adding statement import, adding sync, or adding any feature that sends your content off the device — will also be disclosed inside the app before that feature is used.

## Contact

Questions, requests, or corrections: **admin@prameya.legal**

Prameya LLC, United States. Other app policies: [prameyallc.github.io/privacy](https://prameyallc.github.io/privacy/).

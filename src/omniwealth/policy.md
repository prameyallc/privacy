# OmniWealth Privacy Policy

**Effective date:** 8 August 2026
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
| Does the app connect to the internet? | Yes, for one thing: downloading the AI model files, from Hugging Face. Nothing else. |
| Is my financial information sent to an AI service? | No. The model runs on your device; nothing you enter is sent anywhere. |
| Do you use ads, analytics, or trackers? | No. None. |
| Do you connect to my bank or brokerage? | No. The app has no ability to link a financial account. |
| Do you sell or share my data? | No. We do not have it. |
| Does the app read my Health data? | No. |
| Is this financial advice? | No. OmniWealth is educational only. |

---

## What OmniWealth is, and what it is not

OmniWealth is a personal-finance **education and habit-tracking** app. It explains general concepts — how fees work, what diversification means, how compounding arithmetic works — and it lets you log your own habits, such as whether you reviewed your budget or made a planned contribution.

OmniWealth is **not** an investment adviser, a broker, a financial planner, or a robo-adviser. It does not recommend, rate, or rank any stock, fund, ETF, or ticker. It does not build you a portfolio, tell you to buy, sell, hold, or rebalance anything, or produce advice tailored to your circumstances. Nothing in the app is investment, tax, or legal advice. For decisions about your money, talk to a qualified professional.

We mention this in a privacy policy for a reason: because the app gives no personalised advice, it never needs to build a profile of you, and it never does.

---

## What stays on your device

Everything you enter into OmniWealth is stored locally on your device and stays there.

| What you can enter today | Examples | Where it goes |
|---|---|---|
| Daily habit checklist | Four yes/no toggles — whether you reviewed your budget, made a planned contribution, reviewed your allocation, avoided an impulse purchase — recorded with the date | Local app database |
| Compounding arithmetic inputs | The monthly amount, number of years, and the annual rate you choose to test | Held in memory while that screen is open; not saved to the database |
| App preferences | Appearance setting, which AI model you selected, and whether you have allowed model downloads | Device settings storage |

That is the whole list. The shipping app has no free-text field anywhere: no notes box, no budget-entry form, no goal or income form, and no place to type a question. The app's local database additionally defines record types for budget entries, statement scans, trajectory snapshots and a goal profile — leftovers from features that are not in the shipping version. No screen in the app can create one. They are named here only because the delete control described below clears them too.

This data is written to the app's private storage area, which iOS and macOS protect from other apps. It is never uploaded to Prameya. We could not read it if we wanted to.

**Financial information is sensitive.** We treat it that way. The design principle for OmniWealth is that the safest place for your money data is the device in your hand, and the safest amount for us to hold is none.

---

## What leaves your device

One thing, and only one thing: **a request to Hugging Face to download AI model files.**

OmniWealth's AI features run a language model directly on your device. Those model files are large (roughly 420 MB for the text model, around 1.2 GB for the vision-capable one), so they are not shipped inside the app. When you choose to download a model in Settings, the app connects to `huggingface.co`, operated by Hugging Face, Inc., and downloads the weight files.

**You have to allow it first.** Both models in the app's catalogue are larger than 100 MB, and the app refuses any download above that threshold until you give permission in Settings, where the model and its size are named. Your answer is recorded on the device, and the same screen lets you withdraw it at any time. Nothing downloads on first launch or in the background.

**What that request contains:**

- The name of the model repository being requested (for example, `mlx-community/Qwen2-VL-2B-Instruct-4bit`) and the specific files being fetched.
- Normal technical information that any web request carries: your IP address, and your device and operating-system type.
- Nothing else. The app sends no account, no identifier, and no login token — the requests are anonymous.

**What that request does not contain:**

- None of your habit logs, amounts, or preferences.
- Nothing derived from them.

The request is the same one any other user downloading the same model would make. Hugging Face handles it under its own privacy policy, as an ordinary file download.

**After the download, the internet is not involved.** The model runs on your own device. Nothing you enter is sent to Hugging Face, to Prameya, or to any AI provider. This is a genuine privacy benefit and it is the main reason the app is built this way — but we state it precisely: the app does connect to the internet, for model files, when you allow it.

We should also be precise about what the model is used for today. The summaries the app shows you — your streak, how many days you logged, how many boxes you ticked — are counts of your own records, produced by ordinary arithmetic on your device. There is no chat feature and no question box in the shipping version.

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

On that last point, plainly: an earlier build shipped copy that referred to "uploaded statements," and the app's database still defines an unused record type for statement scans. That copy has been corrected, and no screen in the shipping app can capture or import a document. If a statement-import feature ships later, this policy will be updated to describe photo or file access before it is used, and the App Store privacy label updated with it.

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

OmniWealth asks for no runtime permissions. There is no permission prompt for location, camera, photos, contacts, Health, or tracking, because the app uses none of those.

It does not request permission to send you notifications, and it sends none. There are no reminders in the app in any form.

---

## Children

OmniWealth is a general-audience product for adults managing their own money. It is not directed to children, it is not designed to appeal to children, it contains no advertising, and it collects no personal information from anyone — including anyone under 13. Because the app transmits no personal information to us at all, there is nothing that COPPA (15 U.S.C. §§6501–6506; 16 CFR Part 312) would require us to obtain parental consent for.

If you are a parent or guardian and have a question about this app, write to admin@prameya.legal.

---

## Your choices and controls

Because your data never leaves your device, you control it directly.

- **See it:** your logged days are shown in the app, on the Home and Progress screens.
- **Delete everything you have entered:** Settings → Data → **"Delete all data in this app"**. After a confirmation prompt, this permanently deletes every habit log and every other record the app's database holds — budget entries, statement records, trajectory snapshots, and the profile record — from this device. It cannot be undone. It does **not** remove your app preferences (appearance, selected model, download permission) or any AI model files you downloaded; deleting the app removes those.
- **Deleting one entry at a time is not possible.** The app does not currently offer per-entry deletion — there is no swipe-to-delete and no delete control on an individual row. Deletion is all-or-nothing: the control above, or deleting the app.
- **Delete everything, including preferences and models:** delete the app. That removes the app's local database, its preferences, and any downloaded model files from your device.
- **Free up memory:** Settings → On-Device AI → **"Unload"** releases the loaded model from memory. It does not delete the downloaded files from disk, and the app does not currently offer a control to delete downloaded model files. Deleting the app removes them.
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

Where the UK GDPR or EU GDPR applies, note that Prameya does not act as a controller of any personal data from your use of OmniWealth, because we receive none. Your entries are processed only by software running on your own device, under your control. We do not process special category data (GDPR Article 9); financial information is not a special category, and we hold no health data in any event. Downloading a model file involves your device connecting to Hugging Face, Inc. in the United States, exactly as visiting a website would; Hugging Face acts as an independent controller of that request under its own policy. If you believe we hold personal data about you, contact admin@prameya.legal, and you may complain to your national data protection authority.

---

## Security

- Your data is stored in the app's private storage, which the operating system isolates from other apps, and is protected by your device passcode and disk encryption. That is the operating system's default protection; the app does not add a stronger file-protection class on top of it, and we will not describe it as more than it is.
- Model downloads use HTTPS. The app does not permit unencrypted network connections.
- The strongest control is architectural: there is no server holding your financial information, so there is no server to be breached.

We do not claim any security certification, audit, or standard we do not hold.

---

## Third parties

| Third party | Role | What it receives |
|---|---|---|
| Hugging Face, Inc. | Hosts the open-weight AI model files the app downloads | The model file request, your IP address, and standard request metadata. No user content. |
| Apple | Distributes the app | Whatever Apple collects for App Store distribution, under Apple's own privacy policy. We receive no personal information from Apple. |

There are no others. No analytics vendor, no ad network, no cloud AI provider, no data broker, no payment processor.

The app is built on open-source software components (including Apple's MLX machine-learning framework and Hugging Face's Swift libraries). These are libraries compiled into the app; apart from the model download described above, they do not send data anywhere.

---

## Changes to this policy

If we change how OmniWealth handles data, we will update this policy before the change ships, not after. When we do:

- We will change the effective date at the top.
- We will describe what changed in plain language.
- The previous version will remain available at this address's history.

**This revision (8 August 2026)** corrected statements in the previous version so that every claim matches the code that actually ships. Specifically: the previous version said you could delete individual entries in the app, which was not true — deletion is all-or-nothing, and the section above now says so; the list of what you can enter was narrowed to what the app actually offers; the description of what you can do with a downloaded model was corrected to "unload from memory," since the app has no control that deletes model files; the newly added in-app "delete all data" control was documented, along with what it does not remove; the model-download permission step was documented; and internal review notes that should never have been visible on a published page were resolved and removed. Where a promise could not be made true in the code, the promise was removed rather than softened.

Material changes — for example, adding statement import, adding sync, or adding any feature that sends your content off the device — will also be disclosed inside the app before that feature is used.

## Contact

Questions, requests, or corrections: **admin@prameya.legal**

Prameya LLC, United States. Other app policies: [prameyallc.github.io/privacy](https://prameyallc.github.io/privacy/).
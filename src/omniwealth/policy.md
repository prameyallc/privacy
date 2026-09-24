# OmniWealth Privacy Policy

**Effective date:** 24 September 2026
**Publisher:** Prameya LLC ("Prameya", "we", "us"), a United States limited liability company
**Contact:** admin@prameya.legal
**Applies to:** the OmniWealth app for iPhone, iPad, Mac and Apple Vision Pro, its Apple Watch app, its Apple TV app, and its Home Screen widget

This policy covers OmniWealth only. Other Prameya apps have their own policies, listed at [prameyallc.github.io/privacy](https://prameyallc.github.io/privacy/). Do not assume a statement here is true of any other app.

---

## The short version

| Question | Answer |
|---|---|
| Do you have accounts or logins? | No. There is nothing to sign up for. |
| Where does what I log live? | On the device where you entered it, in the app's own storage. Your budget lines, habit check-ins, goals, statement photos and saved scenarios are never synced to iCloud by the app. |
| Does anything sync through iCloud? | Yes, a little, on iPhone and iPad only: a small iCloud key-value store holds which tab and which library topic you were on, the topic the Home Screen widget suggests, and your appearance choice. None of it is an amount or anything you typed, and **Delete all data** clears it. See [iCloud and syncing](#icloud-and-syncing). |
| Does Prameya receive anything? | No. We run no server that could receive it. We have no database of users. |
| Does the app connect to the internet? | Not for your data. iCloud (above), Handoff, App Store purchases and links you open in your browser are handled by Apple or your browser. In this version the app downloads no AI model and makes no request to Hugging Face. |
| Is my financial information sent to an AI service? | No. **Ask** answers library questions with **Apple Intelligence on your device**, where it is turned on and ready. Your question is not sent to us or to any hosted AI provider, and the app never adds your own records to it. |
| Do you use ads, analytics, or trackers? | No. None. |
| Do you connect to my bank or brokerage? | No. The app has no ability to link a financial account. |
| Do you sell or share my data? | No. We do not have it. |
| Does the app read my Health data? | No. |
| Is this financial advice? | No. OmniWealth is educational only. |

---

## What OmniWealth is, and what it is not

OmniWealth is a personal-finance **education and habit-tracking** app. It explains general concepts — how fees work, what diversification means, how compounding arithmetic works — from a library of cited topic packs, and it lets you keep your own records: habit check-ins, an envelope / budget log, a list of goals, saved compounding scenarios, and photos of statements you already have, with a plain-language glossary of the terms found on them.

OmniWealth is **not** an investment adviser, a broker, a financial planner, a robo-adviser, or an AI advisor. It does not recommend, rate, or rank any stock, fund, ETF, or ticker. It does not build you a portfolio, tell you to buy, sell, hold, or rebalance anything, or produce advice tailored to your circumstances. Nothing in the app is investment, tax, or legal advice. For decisions about your money, talk to a qualified professional.

We mention this in a privacy policy for a reason: because the app gives no personalised advice, it never needs to build a profile of you, and it never does. The goals, income figure and statement text you may enter are kept for you to read back; the app does not score them, send them anywhere, or use them to recommend anything.

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
the full topic library and the basic calculators, with no account and no time limit. Pro adds saved scenarios, envelopes, the weekly check-in reminder and the formatted worksheet (CSV) export.

**Pro does not add cloud sync, and there is no paid iCloud option.** OmniWealth stores your
records on your device in every case, paid or not. If a subscription lapses you keep your
own data and can still export all of it with **Export everything in this app**, which is free; only the Pro tools stop.


## Free vs paid tier data collection

**The tier you choose does not change what data Prameya collects from OmniWealth, which is none.** In both the free tier and Pro:

- Your habit logs, envelope entries, goals, statement records and saved scenarios stay on your device
- No analytics, tracking, or telemetry sent to us
- No server that receives your content
- No account or login

The difference between tiers is **feature access**, not data handling. Pro unlocks additional tools; it does not unlock data transmission.

## Cancellation and refunds

Subscriptions are managed entirely through your Apple ID:

- **To cancel:** Open Settings on your iPhone or iPad → tap your name → Subscriptions → OmniWealth → Cancel Subscription. On Mac, open the App Store app → Account (sign-in name) → View Information → Subscriptions → Manage. Inside OmniWealth, a subscriber sees **Manage Subscription** under More ▸ Subscription, which opens Apple's own subscription controls.
- **Refund requests:** Handled by Apple, not Prameya. See [reportaproblem.apple.com](https://reportaproblem.apple.com/) or contact Apple Support. We have no access to your payment information and cannot issue refunds ourselves.
- **What happens to your data when you cancel:** Nothing. Your on-device data stays on your device. Canceling a subscription removes access to Pro features; it does not delete your habit logs, budget entries or saved scenarios.

## StoreKit transaction data

OmniWealth does not keep its own record of your purchases. Each time it needs to know whether Pro is unlocked, it asks Apple's StoreKit on your device which OmniWealth products your Apple Account currently owns, and it listens for purchase updates from StoreKit while it runs. Payment is handled entirely by Apple.

If you tap **Restore Purchases**, StoreKit contacts Apple's servers to refresh your purchases. That communication is between your device and Apple; Prameya is not involved and sees nothing from it.

---

## What stays on your device

Everything you enter into OmniWealth is stored locally, in the app's own storage on the device where you entered it.

| What you can enter | Examples | Where it goes |
|---|---|---|
| Daily habit check-in | Four yes/no ticks — whether you reviewed your budget, made a planned contribution, reviewed your allocation, avoided an impulse purchase — recorded with the date, and an optional note you type | Local app database |
| Envelope / budget log (Pro) | An envelope name, an optional payee, an amount (assigned or spent), an optional note, the date, and on iPhone and iPad whether you saved the line as a Watch draft. Arithmetic on that envelope, not a recommendation | Local app database |
| Goals | Short goal lines you type under More ▸ Tools ▸ Goals | Local app database, in one profile record |
| Income & Contribution | More ▸ Tools ▸ Income & Contribution saves a monthly-income figure to the same profile record when you tap **Save**. (In this version the screen has no field for typing the figure, and the target percentage on its slider is not saved.) | Local app database, in the profile record |
| Statement records | A reduced copy of a statement photo that you choose from your photo library, the photo's original file type (see [Statement photos](#statement-photos)), the text read from it on your device, and a short glossary of terms found in that text | Local app database |
| Saved scenarios (Pro) | Under More ▸ Tools ▸ Your numbers: the years, monthly amount, annual rate and result of a compounding worksheet you choose to save | Local app database |
| Compounding arithmetic inputs | The monthly amount, number of years, and the annual rate you choose to test on the Compounding screen | Held in memory while that screen is open; not saved |
| Ask questions | A question you type in Ask (see [Ask](#ask)) | Held in memory only, until you tap **New chat** or the app closes; not saved |
| App preferences | Appearance, whether you have acknowledged the first-run disclosure, whether Ask is on, the weekly check-in reminder switch and its weekday, when you last marked the check-in reminder seen from Apple Watch, the age-range result described under [Children](#children), which version of the significant-change notice this device has been through, and a marker that the one-time cleanup of old model files has run | Device settings storage |

The app also has a second local database set aside for a small set of preferences. It is created with cloud syncing turned off, and nothing in this version writes to it.

This data is written to the app's private storage area, which the operating system protects from other apps. It is never uploaded to Prameya. We could not read it if we wanted to.

**Backups.** The app's database is not excluded from device backups. If you use iCloud Backup or back up your device to a computer, your OmniWealth records — including the stored statement page images — are included in that backup, under Apple's terms and your control. They are not readable by Prameya.

**Financial information is sensitive.** We treat it that way. The design principle for OmniWealth is that the safest place for your money data is the device in your hand, and the safest amount for us to hold is none.

### Statement photos

More ▸ Tools ▸ Statement Glossary ▸ **Scan Statement** ▸ **Choose from Photos** opens Apple's photo picker. OmniWealth receives only the one photo you pick; it does not get access to the rest of your library, and it does not ask for Photos permission. There is no live camera capture and no file or PDF import.

The app reads the text on the photo you picked with Apple's on-device text recognition, then shows a short glossary of common terms it finds (for example "expense ratio" or "cost basis"). What the app then keeps on your device is:

- a reduced copy of the page: one JPEG image at most 1,600 pixels on its longest side (a smaller photo is not enlarged), on every device, including Mac. The copy is redrawn from the photo's pixels, so the photo's location, camera and capture-time details are not kept with it;
- the photo's original file type, for example HEIC or PNG, read from the photo itself;
- the recognized text and that glossary.

The photo you picked stays in your photo library; the app keeps no other copy of it. Nothing from the photo is sent to us, to Apple, or to any AI service, and the statement text is never given to Ask. The glossary is general; it is not commentary on your holdings.

Each statement record can be deleted on its own from the Statements list.

---

## What leaves your device

**Nothing you enter is sent to Prameya.** The paths below are the only ones by which anything leaves the device, and none of them reaches us.

- **iCloud key-value store (iPhone and iPad).** Described under [iCloud and syncing](#icloud-and-syncing): the tab and library topic you were on, the widget's suggested topic, a topic queued to open, and your appearance choice. No amounts, no records, nothing you type.
- **Handoff.** On iPhone, iPad, Mac and Apple Vision Pro, the app tells your nearby devices that use the same Apple Account which tab you are on and which library topic you last opened, so another device can offer to continue. Apple handles this.
- **Apple Watch.** Described under [Apple Watch, Apple TV and the widget](#apple-watch-apple-tv-and-the-widget): the iPhone sends the Watch short prompts (never an amount), the Watch sends back your confirm or decline taps, and a question you type on the Watch travels to your paired iPhone and the answer comes back, all over Apple's connection between the two devices.
- **App Store.** Purchases and **Restore Purchases** go to Apple through StoreKit.
- **Declared Age Range (iPhone and iPad).** Where Apple says it applies to your account, the app asks Apple's own age-range service, as described under [Children](#children). If a parent or guardian must approve an update, Apple sends that request.
- **Links.** Opening the privacy policy, support page, or a source link from a topic pack opens it in your browser.
- **Your backups and exports**, only where you put them.

**No model download and no Hugging Face traffic in this version.** The app contains code for an optional on-device Ask model downloaded from Hugging Face, and a catalog naming three models for it (MiniCPM5 2B from `openbmb/MiniCPM5-2B-MLX`, about 1.4 GB; Gemma 4 E2B from `mlx-community/gemma-4-E2B-it-qat-4bit`, about 4.4 GB; Gemma 4 E4B from `mlx-community/gemma-4-E4B-it-qat-4bit`, about 6.8 GB). **No device is offered any of them in this version**: the download is held until the models pass an independent review of their answers, so there is no download control anywhere in the app and the app makes no request to Hugging Face. Apple TV and Apple Watch cannot download a model at all. If an earlier test build of OmniWealth downloaded the model it used then (Qwen3 0.6B), the first launch of this version deletes those files. Before any download is offered, this policy will be updated to say which model, from where, and what the request carries.

**Local notifications** are scheduled by the app on your device and delivered by the operating system. They are described under [Reminders and notifications](#reminders-and-notifications). Nothing is sent to us.

**Performance diagnostics.** On iPhone, iPad, Mac and Apple Vision Pro, the app receives Apple's MetricKit summaries (average launch and hang times, disk writes, and counts of crashes and hangs) and writes those figures to the device's own system log. It sends them nowhere. Whether Apple shares diagnostics with developers through its own channels is controlled by your device's Analytics settings, under Apple's policy.

---

## Ask

**Ask** is a tab for questions about the library. It appears only when the **In-app answers** switch in More is on (it is on by default) and Apple Intelligence is turned on and ready on the device — so it can appear on iPhone, iPad, Mac and Apple Vision Pro, and never on Apple TV or Apple Watch.

When you ask, the app sends your question as you typed it, together with passages from the library's topic packs, to **Apple's on-device model** (Apple Intelligence). The model may also look up a library topic. The answer is labelled **Apple Intelligence**. Your question stays on the device; it is not sent to us or to any hosted AI provider.

- The app never adds your check-ins, envelope lines, goals, income figure or statement text to a question. If you type amounts yourself, they are part of your question and stay on the device with it.
- Some questions are refused before the model sees them — for example, a request to calculate your net worth.
- If the answer uses wording that the library's topic packs bar (such as language a pack marks as off-limits for education), Ask shows a notice instead of the answer.
- If Apple Intelligence cannot answer, Ask says so. It does not fall back to any other service.

Questions and answers are held in memory only. They are not saved as records; **New chat** clears them, and they are gone when the app closes.

---

## Reminders and notifications

**Weekly check-in (Pro).** The reminder is off until you turn it on in **More ▸ Reminders**. Turning it on is the only thing in OmniWealth that asks for permission to send notifications, and it never asks at launch. If you allow it, the app schedules one repeating local notification, titled "Check-in" and saying "Time for this week's check-in.", at 19:00 on the weekday you turned it on. It is not a performance claim. Turning the switch off cancels it.

**Watch draft notice (iPhone and iPad).** While the weekly check-in switch is on, saving an envelope line with **Save as Watch draft** also posts one notice, "Review today's drafts", saying "Open OmniWealth on your wrist to confirm." It never includes an amount. Its **Confirm** button confirms your most recent draft on the iPhone; **Snooze** and **Not now** leave it a draft; simply tapping or dismissing the notice changes nothing.

Neither notification is sent through a server. **Delete all data** turns the weekly check-in off and removes any check-in or draft notice that is still waiting.

---

## Apple Watch, Apple TV and the widget

**Apple Watch.** The Watch app comes with the iPhone app. It lists the library's topic packs, shows short prompts the iPhone sends it, and has **Ask iPhone**.

- **Drafts.** If you saved an envelope line as a Watch draft on your iPhone, the Watch can confirm or decline it. The Watch never shows or enters an amount; the confirm is applied on the iPhone.
- **Check-in prompt.** While the weekly check-in is on, the Watch also shows a prompt to mark it seen; confirming it records the time on the iPhone.
- **Ask iPhone** sends the question you type on the Watch to OmniWealth on your paired iPhone, over Apple's connection between the two devices. The iPhone answers it the way Ask does on the iPhone and sends the answer back to the Watch. The Watch runs no model and never starts a download.
- **Complication.** The Watch app passes its complication a short label — "Learn." or "Drafts" with a count — through a storage area on the watch that only the Watch app and its complication share. It is never an amount.
- The Watch app does not use iCloud.

**Apple TV.** The Apple TV app is a read-only topic library. Its **Continue** tab reads the iCloud key-value store described below to show the library topic you last opened on your iPhone or iPad, and it follows the appearance choice kept there. There is no data entry, no Ask, and no model download on Apple TV.

**Home Screen widget (iPhone and iPad).** The widget shows the library's next suggested topic, read from the iCloud key-value store. Tapping it (or the matching Siri / Shortcuts phrase) records that topic in the same store so the app opens it next time. The widget reads no records.

None of this reaches Prameya.

---

## What we do not do

Each of these is a flat "no", not a "we limit this":

- **No accounts.** No sign-up, no email, no password, no Sign in with Apple.
- **No Prameya server.** We operate no backend that receives app data. There is no user database to breach, subpoena, or sell.
- **No analytics or telemetry sent to us.** No usage tracking, no session recording, no third-party crash-reporting service. (The MetricKit figures described above stay in the device's log.)
- **No advertising.** No ad networks, no ad identifier (IDFA), no App Tracking Transparency prompt, because there is nothing to track.
- **No selling or sharing of personal information**, in the ordinary meaning or in the specific meanings those terms carry under California law.
- **No bank, brokerage, or credit connections.** The app cannot link to a financial institution, and there is no data aggregator (such as Plaid) in it. It never sees an account number, a balance feed, or a transaction feed. Anything about your money is there because you typed it or chose a photo of it.
- **No credit checks, credit scores, or credit reports.**
- **No purchases or transfers.** The app cannot move money.
- **No location tracking.**
- **No contacts, calendar, or microphone access.**
- **No Keychain storage.** The app puts nothing in the device Keychain.
- **No camera.** The app has no camera capture. Statement photos come only from Apple's photo picker, one photo you choose at a time, and there is no file or PDF import.
- **No hosted AI and no model download in this version.**

---

## iCloud and syncing

**OmniWealth does not sync your financial or habit data to iCloud.** Your check-ins, envelope lines, goals, income figure, statement records and saved scenarios are stored in a local database on the device where you entered them. Both of the app's databases are created with cloud syncing turned off, and the app has no iCloud (CloudKit) container. If you use OmniWealth on two devices, those records on the two devices are separate and do not share data.

**The iCloud key-value store.** On iPhone and iPad, if you are signed in to iCloud, the app keeps four small values in its iCloud key-value store, which Apple syncs to your other devices that use the same Apple Account:

- which tab you were on and the ID of the library topic you last opened, if any, with the time it was written;
- your appearance choice (system, light or dark);
- the library topic the Home Screen widget suggests next (its ID, title and a short line), with the time it changed;
- a topic you asked the widget or Siri / Shortcuts to open, until the app opens it.

These are the app's own library topics and settings — never an amount, a record, or anything you typed. They are how your iPad, your Apple TV and the widget can offer to continue where you left off. On Mac and Apple Vision Pro the app does not use iCloud, and the Apple Watch app does not use it either.

**How these values are removed.** **Delete all data in this app** removes all four values from the iCloud key-value store, and Apple passes the removal on to your other devices that use the same Apple Account. It also makes the app forget the topic you last opened, so the topic is not written back. Afterwards the app writes values again only as you use it, on this device or on another one signed in to the same Apple Account: the tab when you next change tabs (and a topic when you next view one), the widget's topic when the app next refreshes it, which can be straight away and is at the latest the next time the app opens (this is the library's first suggested topic, the same for everyone), and your appearance when you next change it. Otherwise the app overwrites each value as it changes, and a queued topic is cleared as soon as the app opens it. **Deleting the app does not remove these values from iCloud**, so use Delete all data first if you want them gone. Apple stores these values under your Apple Account; Prameya cannot see them.

---

## Health data: we do not process it

OmniWealth does not collect, receive, access, derive, or infer any health data. It does not read Apple Health, it has no Health integration, it asks you nothing about your health, and it makes no inference about your physical or mental condition from your spending.

The shipping app carries no HealthKit entitlement, no Health usage description, no HealthKit framework, and no Health code of any kind.

This matters legally, not just descriptively. Washington's My Health My Data Act (RCW ch. 19.373) and Nevada's consumer health data law (SB 370, 2023) define "consumer health data" and "collect" very broadly — broadly enough to reach data that is merely accessed, processed, or derived, not only data that is transmitted to a company. Because OmniWealth does none of those things with health data, those statutes do not apply to it, and no separate consumer health data privacy policy is required for this app.

We say this plainly because earlier internal versions of this app's technical configuration wrongly labelled budget and habit logs as "health" data, and an earlier build displayed placeholder step and sleep numbers that were hardcoded rather than read from Health. That label was a mistake and the placeholder feature is gone. **Budgeting information is financial information, not health information.** The app's privacy manifest declares no collected data types at all.

## HIPAA does not apply

HIPAA (45 CFR Parts 160 and 164) governs health plans, health care clearinghouses, most health care providers, and their business associates. Prameya is none of those, OmniWealth handles no health information, and you have no patient relationship with us. **HIPAA does not apply to this app, and we do not claim HIPAA compliance.**

---

## Permissions the app asks for

OmniWealth asks for no runtime permissions for location, camera, photo library access, contacts, Health, or tracking. The statement photo picker is Apple's own and needs no permission; the app receives only the photo you pick.

- **Notifications:** asked only when you turn on the weekly check-in in **More ▸ Reminders**, never at launch.
- **Age range (iPhone and iPad):** where Apple says it applies to your account, Apple shows its own sheet asking whether to share your age range with the app. You decide.

---

## Children

OmniWealth is a general-audience product for adults managing their own money. It is not directed to children, it is not designed to appeal to children, it contains no advertising, and it sends no personal information to us from anyone — including anyone under 13. Because the app transmits no personal information to us at all, there is nothing that COPPA (15 U.S.C. §§6501–6506; 16 CFR Part 312) would require us to obtain parental consent for.

**Age range (iPhone and iPad).** Some state laws require apps to use the age range an Apple Account shares. After the first-run screen — never before it — the app asks Apple whether these rules apply to your account. If Apple says they do, the app asks Apple for your age range with a single age (18); Apple shows the choice and you decide whether to share. Once a result is stored the app does not ask again, unless **Delete all data** has cleared it. The app keeps only the result — under 18, 18 or older, or that you chose not to share — never a birth date or the range Apple returns. It stays on this device, it is shown in More ▸ Legal ▸ Legal & Safety, and **Delete all data** clears it. When an update makes a significant change (for example, to this policy), Apple may show you a notice about it, or, for an account where the law requires it, the app asks a parent or guardian to approve the update through Apple's Ask to Approve or in person on the device, and waits for that approval before it opens. Apple handles these requests; Prameya receives nothing from them.

If you are a parent or guardian and have a question about this app, write to admin@prameya.legal.

---

## Your choices and controls

Because your data stays on your device, you control it directly.

- **See it:** your check-ins, envelope lines, goals, statements and saved scenarios are shown in the app.
- **Correct or delete one entry:** open a check-in from **Do**, or an envelope line from the Envelopes screen, to change it or delete it on its own. Each goal, each statement record and each saved scenario also has its own delete control: for a saved scenario, swipe it or open its menu under More ▸ Tools ▸ Your numbers, then confirm. Deleting a saved scenario does not need Pro.
- **Get your data out:** **More ▸ Data ▸ Export everything in this app** writes one JSON file with every check-in, envelope line, statement record with its page image and that image's file type, saved scenario and your profile. **Export consistency summary** writes a smaller file of just the consistency measurement, and **Export formatted worksheet (CSV)** is a Pro export. Each file is written to this device and goes only where you send it.
- **Delete everything you have entered:** **More ▸ Data ▸ "Delete all data in this app"**. After a confirmation prompt, this permanently deletes, on this device, every habit log, envelope / budget line, statement record and its page image, saved scenario, and your profile (goals and income figure), plus your age-range result, and leftover model files and settings from older installs if any remain. It also clears the four iCloud key-value values described under [iCloud and syncing](#icloud-and-syncing), turns off the weekly check-in reminder (its switch, weekday and the time you last marked it seen from Apple Watch) and removes any check-in or draft notice still waiting, and sends your Apple Watch a fresh list with no draft or topic prompts, so its complication goes back to "Learn.". If a later file removal fails after the database is emptied, the app says so rather than claiming a complete delete. It cannot be undone. It does **not** reset your appearance or Ask settings, and it cannot reach copies already in your device backups or in files you exported.
- **Delete everything on a device, including preferences:** delete the app. That removes the app's local database and its preferences from that device. It does not remove the iCloud key-value values described under [iCloud and syncing](#icloud-and-syncing); use **Delete all data** before deleting the app if you want those gone too.
- **Ask us to delete your data:** there is nothing for us to delete. We have never received it. If you write to us asking for deletion, that will be our honest answer.

---

## Your privacy rights

We honour the rights below regardless of whether Prameya meets the size thresholds that make those laws mandatory for a company. In practice, the honest answer to most requests is the same: **we do not hold your personal information**, so there is nothing to disclose, correct, delete, or opt out of.

### California (CCPA/CPRA)

If you are a California resident, the California Consumer Privacy Act as amended by the CPRA (Cal. Civ. Code §1798.100 et seq.) gives you the rights to know, delete, correct, opt out of sale or sharing, and limit the use of sensitive personal information.

Our position for OmniWealth:

- **Personal information we collect:** none. The app transmits nothing about you to us.
- **Sensitive personal information we collect:** none. California's definition of sensitive personal information (Cal. Civ. Code §1798.140(ae)) includes certain financial data, such as an account number together with an access code. OmniWealth never sends us any of it — it has no account linking, and we receive nothing you enter, including statement photos.
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

Where the UK GDPR or EU GDPR applies, note that Prameya does not act as a controller of any personal data from your use of OmniWealth, because we receive none. Your entries are processed only by software running on your own devices, under your control, and the small iCloud values and Handoff described above are carried by Apple under your Apple Account. We do not process special category data (GDPR Article 9); financial information is not a special category, and we hold no health data in any event. If you believe we hold personal data about you, contact admin@prameya.legal, and you may complain to your national data protection authority.

---

## Security

- Your data is stored in the app's private storage, which the operating system isolates from other apps. On iPhone, iPad and Apple Vision Pro, the app's databases are set to Apple's "complete unless open" file protection: they are stored encrypted with a key tied to your device passcode, and once your device is locked they cannot be opened again until you unlock it (a database the app already has open stays readable). On Mac, the app runs in Apple's app sandbox and relies on your Mac's own disk encryption (FileVault, if you have turned it on).
- The app downloads no model in this version, so there is no download request to protect.
- The strongest control is architectural: there is no server holding your financial information, so there is no server to be breached.

We do not claim any security certification, audit, or standard we do not hold.

---

## Third parties

| Third party | Role | What it receives |
|---|---|---|
| Apple | Distributes the app; processes purchases; provides iCloud, Handoff, Apple Intelligence, the photo picker, the Watch connection and the Declared Age Range service | Whatever Apple collects for these services, under Apple's own privacy policy — including, if you use iCloud, the four small key-value values described above. Apple Intelligence and text recognition in OmniWealth run on your device. We receive no personal information from Apple. |

There are no others. No analytics vendor, no ad network, no hosted AI provider, no data broker, no payment processor. Hugging Face receives nothing, because no download is offered in this version.

The app ships Apple platform frameworks and in-repo Swift packages, plus the open-source MLX and Hugging Face libraries that would run and download the optional on-device model. The Hugging Face download libraries are linked only on iPhone, iPad, Mac and Apple Vision Pro (MLX is also in the Apple TV app), and in this version nothing calls their download code. None of them is an analytics, advertising or crash-reporting library.

---

## Changes to this policy

If we change how OmniWealth handles data, we will update this policy before the change ships, not after. When we do:

- We will change the effective date at the top.
- We will describe what changed in plain language.
- The previous version will remain available at this address's history.

**24 September 2026 — what changed.** With the app update released alongside this revision:

- **Statement photos.** A statement record now keeps a reduced copy of the page, one JPEG at most 1,600 pixels on its longest side on every device, without the photo's location, camera or capture-time details, and records the photo's original file type. Earlier builds kept the whole photo (on Mac as an uncompressed image file) and named every record "Photo Library.jpg". The text is still read on your device from the photo you pick. A statement saved by a pre-release test build before this date keeps the image as that build saved it; delete it and add it again to keep only the reduced copy.
- **Saved scenarios.** Each saved scenario can now be deleted on its own under More ▸ Tools ▸ Your numbers. Earlier this policy said saved scenarios could be removed only with **Delete all data**.
- **Export.** The export file now names the file type of each statement page image.

Nothing new leaves your device, and nothing is sent to Prameya.

**23 September 2026 — what changed.** This policy was corrected to match what the current app does. Earlier versions said things that were no longer true:

- **iCloud.** Earlier versions said the app held no iCloud entitlement and synced nothing. On iPhone and iPad it keeps four small values in its iCloud key-value store — the tab and library topic you were on, the widget's suggested topic, a topic queued to open, and your appearance choice — so your other devices, Apple TV and the widget can continue where you left off. It now also says how they change and how they are removed. Your records still never sync.
- **Handoff, Apple Watch, Apple TV and the widget** are now described: what the Watch sends to the iPhone (confirm or decline a draft, and questions for Ask iPhone), the Watch complication label, the read-only Apple TV library, and the Home Screen widget.
- **Ask.** Earlier versions said there was no AI in the app. Ask answers library questions with Apple Intelligence on your device, where it is ready; your question is not saved and not sent to us or any hosted AI provider. The app contains, but does not offer, an optional downloadable model; this policy names the three models and says no download or Hugging Face request happens in this version.
- **What you can enter.** Earlier versions said there was no Goals surface and no document import. The app has Goals, an Income & Contribution screen, saved scenarios (Pro), notes on check-ins and envelope lines, and statement photos you pick from your photo library, read on your device.
- **Notifications.** The weekly check-in is a Pro tool, fires at 19:00 on the weekday you turned it on, and, on iPhone and iPad, a Watch draft also posts one notice while it is on.
- **Age range.** On iPhone and iPad, where Apple says the rules apply, the app asks Apple for your age range once and keeps only the result, and a parent or guardian may be asked to approve a significant update.
- **Your controls.** Single check-ins and envelope lines can now be corrected or deleted on their own, goals and statement records can be deleted one at a time, and three exports are available. Earlier versions said deletion was all-or-nothing.
- **Delete all data now removes more.** With the app update released alongside this revision, **Delete all data** also clears the four iCloud values (earlier builds left them in iCloud and on your other devices), turns off the weekly check-in reminder and removes any check-in or draft notice still waiting (earlier builds left the reminder on), and sends your Apple Watch a fresh prompt list. Its confirmation now says so, names saved scenarios, and points to More ▸ Tools ▸ Envelopes for single envelope lines.
- **Apple Watch and iCloud.** The Watch app no longer contains code that tried to read the iPhone's iCloud values; it could not reach them, and it does not use iCloud.
- **Other corrections.** The app does not store its own copy of your purchases (earlier versions said it kept a transaction record); the app's databases now use stronger file protection on iPhone, iPad and Apple Vision Pro; your records are included in device backups; the app logs Apple's MetricKit performance figures to the device only; and the policy now covers Mac, Apple Vision Pro, Apple Watch and Apple TV.

Nothing is sent to Prameya, now or before.

**23 August 2026 (previous revision)** recorded the envelope / budget log and removed Hugging Face / on-device model download claims.

Material changes — for example, offering the on-device model download, adding sync of your records, or adding any feature that sends your content off the device — will also be disclosed inside the app before that feature is used.

## Contact

Questions, requests, or corrections: **admin@prameya.legal**

Prameya LLC, United States. Other app policies: [prameyallc.github.io/privacy](https://prameyallc.github.io/privacy/).

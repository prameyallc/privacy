# OmniMathematics Privacy Policy

**Effective date:** 23 September 2026
**Publisher:** Prameya LLC ("Prameya", "we", "us")
**App:** OmniMathematics for iPhone and iPad, with its Apple Watch app — bundle ID `legal.prameya.OmniMathematics`
**Contact:** admin@prameya.legal
**Scope:** This policy covers OmniMathematics on iPhone and iPad (including the iPad app where Apple lets it run on an Apple silicon Mac or Apple Vision Pro) and the Apple Watch app that comes with it, and nothing else. Prameya's other apps have their own policies, because they work differently. Index: <https://prameyallc.github.io/privacy/>
**Canonical public URL (slug stays `omnimath`):** <https://prameyallc.github.io/privacy/omnimath/>

---

## The short version

- **There are no accounts.** No sign-in, no email address, no name, no profile. There is nothing to fill in.
- **Your marks are yours.** The chapters you mark read and the topics you mark worked are stored on your device and, if you are signed in to iCloud, in your own iCloud private database, so your other devices show the same marks. We do not run a server that receives them, and we cannot read them.
- **OmniMathematics does not talk to a server of ours.** There is no such server. Everything you study ships inside the app. The only paths off the device are Apple's (the App Store for purchases, iCloud, Handoff, and the connection between your iPhone and your Apple Watch) and, only if you choose to download the optional Ask model, Hugging Face.
- **No ads, no tracking, no analytics.** The app contains no advertising or analytics software, does not use the advertising identifier, and never shows the App Tracking Transparency prompt.
- **One optional permission.** OmniMathematics asks to send notifications only if you turn on **More ▸ Settings ▸ Reminders ▸ Daily study reminder**, which is off until you turn it on. It asks for no other permission: no camera, photos, microphone, location, contacts, health or files.
- **Ask answers on your device.** Ask sends your question to a language model that runs on your device and shows what the model writes, labelled with the model that wrote it and a notice that it can be wrong. Where Apple Intelligence is turned on and ready, Apple's on-device model answers. Where it is not, an iPhone or iPad with 8 GB of memory can choose to download MiniCPM5 2B (about 1.4 GB), and one with 12 GB or more Gemma 4 E2B (about 4.4 GB). Where no model can answer, Ask shows the matching passage from Concepts (the app's built-in concept reference) and the topic packs. Your question is not sent to us or to any server.
- **Purchases go through Apple.** StoreKit on your device completes and checks an OmniMathematics Pro purchase with Apple. The app sends nothing about your purchase to us, and we do not collect payment details. The topic packs, Concepts, the chapters, the interactives, Ask and your marks stay free either way.
- **OmniMathematics is built for a general audience** — computer-science students, self-learners and adults. It is not in the App Store Kids Category.
- **No health data of any kind** is involved. See "Health data" below.

---

## What OmniMathematics is

OmniMathematics teaches discrete mathematics for computer science, and the mathematics around it, through topic packs with a cited source under each idea, a built-in reference of concepts (Concepts), interactives, and a story tour of twenty chapters in six parts. All of the learning content ships inside the app.

OmniMathematics Pro, sold through Apple's in-app purchase as a monthly or annual subscription or a one-time lifetime purchase, adds one feature: a formatted study report of your marks. Everything else stays free.

---

## What stays on your device

OmniMathematics writes the following to its own storage on the device:

| What | Why |
|---|---|
| Each chapter you mark read and each topic you mark worked, with when you marked it | To show your progress |
| Your insight stars | To show your progress |
| Where you left off: the last chapter, its part and the step you reached, the last topic pack and the last interactive | To take you back where you were |
| The last day you studied, and how many days in a row you have studied | To show your streak |
| Whether you have seen the intro screens, and when the first-run Legal & Safety notice was acknowledged | So they show once |
| Your appearance choice | To apply it |
| Your answer to "Download the Ask model?", with the model and version it was given for, or the position of the **On-device Ask model** switch | So Ask does not ask again for the same model, and asks again if the model changes |
| Whether the daily study reminder is on | To keep or remove the reminder |
| On iPhone: the ids and send times of recent Apple Watch taps it has already applied, at most 64, each forgotten after an hour | So a tap on the Watch applies once |
| The optional Ask model's files (MiniCPM5 2B, about 1.4 GB, or Gemma 4 E2B, about 4.4 GB), only if your device was offered the download and you chose it | To run the model on the device |
| A one-time marker that the files of the model used by versions before 1.0 (24) (Qwen3 0.6B, about 350 MB) were removed on the first launch, and how much space that freed | So the removal happens once |
| A temporary copy of a file you export, which the app clears afterwards | To hand the file to the share sheet |
| Two internal markers: that stored marks were moved to the current storage format, and which version of the chapter list the marks belong to | So the move happens once, and a mark from an older chapter list is not counted as a newer chapter |

That is the complete list of what OmniMathematics itself stores. We cannot see it, and we have no way to request it. A file you export with **Export my marks**, or a Pro study report, goes wherever you choose to save or share it. What Apple's own services keep for the app — iCloud, Handoff, the connection to Apple Watch, the Home Screen widget and a scheduled reminder — is described below.

If you use iCloud or computer backup for your device, this data is included in that backup, under Apple's terms and your control.

---

## iCloud, Handoff and your other devices

If you are signed in to iCloud:

- **Your marks** — every chapter and topic mark, your insight stars, your streak and where you left off — sync through your own **CloudKit private database**, so your other devices show the same marks. Prameya cannot open another person's private database. Signing out of iCloud may remove synced marks from a device until you sign in again.
- **A small iCloud key-value store** remembers where you left off, the next suggested topic for the Home Screen widget, a topic you asked the widget or Shortcuts to open until the app opens it, and your appearance choice. That is how your other devices and Apple Watch can offer to continue, and how Apple Watch matches your appearance choice.

**Handoff** also tells your nearby devices that use the same Apple Account where you left off.

**Removing marks.** More ▸ Progress lists every mark you have made, and each one has its own remove control. **Remove Every Mark**, confirmed with **Remove Everything**, removes every chapter mark, every topic mark, your insight stars and where you left off — on this device and, if you use iCloud, on your other devices. Deleting the app removes only that device's copy; it does not empty iCloud.

---

## Apple Watch

The Apple Watch app comes with the iPhone app. It lists topic packs, shows cards the iPhone sends to it, and has **Ask the phone**.

- **Ask the phone** sends the question you enter to OmniMathematics on your paired iPhone, over Apple's connection between the two devices. The iPhone answers while OmniMathematics is open on it, the way Ask on the iPhone does — with Apple Intelligence, or with a downloaded model that is already loaded, or otherwise from Concepts and the topic packs — and sends the answer back to the Watch. A question from the Watch never starts a download.
- **Cards** on the Watch send your tap (for example "Start" or "I'm done") to the iPhone, which applies each tap once.
- The Watch reads the iCloud key-value store described above to offer where you left off and to match your appearance choice, and opening a pack on the Watch updates where you left off.

None of this reaches Prameya.

---

## The daily study reminder

The reminder is off until you turn it on in **More ▸ Settings ▸ Reminders ▸ Daily study reminder**. Turning it on is the only thing in OmniMathematics that asks iOS for permission to send notifications, and iOS asks only if you have not answered before. If you allow it, the app schedules one local notification a day at 19:00 your local time, titled "Study reminder" and naming what you were studying. iOS delivers it from the device; nothing is sent to us or to any server. Turning the switch off removes the reminder. If notifications are turned off for OmniMathematics in iOS Settings, the Reminders section says so and offers **Open Settings**.

---

## Ask, and the optional on-device model

Ask sends your question, as you typed it, to a language model that runs on your device, and shows what the model writes. The answer is labelled **Apple Intelligence** or **On-device model** and carries a notice that it can be wrong. Ask does not check or filter the model's answer and does not limit it to the app's material; only the model's hidden reasoning, which is not part of the answer, is removed. Under the answer, Ask links related entries in Concepts and the topic packs.

- **Where Apple Intelligence is turned on and ready,** Apple's on-device model answers. Your question stays on the device; it is not sent to us or to Apple. No download is offered.
- **Where no model can answer** (no model is offered, downloaded or loaded yet, and on Apple TV), Ask shows the closest passage in Concepts and the topic packs already on your device, labelled **From Concepts**.

Where Apple Intelligence is not ready, Ask can use an optional model that you download. Which model, if any, depends on how much memory the device has:

- **iPhone and iPad with 8 GB of memory** are offered **MiniCPM5 2B**, from the Hugging Face repository `openbmb/MiniCPM5-2B-MLX` at commit `8a9ad753`, about 1.4 GB.
- **iPhone and iPad with 12 GB of memory or more** are offered **Gemma 4 E2B**, from the Hugging Face repository `mlx-community/gemma-4-E2B-it-qat-4bit` at commit `42f62737`, about 4.4 GB. When the memory check refuses Gemma 4 E2B, they are offered MiniCPM5 2B instead, as a separate download that you also choose; a device that accepts it keeps both downloads until you remove the downloaded model, and Settings offers the way back to Gemma 4 E2B.
- **iPhone and iPad with 6 GB of memory or less**, and devices whose graphics hardware does not support Metal 3, are offered no model. On them Ask always answers from Concepts and the packs, and Settings shows no download switch.

The model is not part of the app download. It is offered only where Apple Intelligence is not ready, and downloaded from Hugging Face only after you choose **Download** in Ask or turn on **On-device Ask model** in More ▸ Settings ▸ Ask model, only while OmniMathematics is open, and it may be downloaded again if the system clears storage space. The button names the model and its size (about 1.4 GB or about 4.4 GB). Before offering the download, and again each time it loads the model, the app checks that the device has enough free memory for the model; when it does not, Ask answers from Concepts and the packs and offers no download. While the download runs, the app keeps the screen on. The downloaded files are the model weights, its tokenizer and a prompt-formatting template, pinned to one version and checked by size after each download and before each load, and by checksum after each download: data the model reads, not executable code. Text the model produces is shown as the model writes it, even when it reaches the length limit, labelled **On-device model** with a notice that it can be wrong. When the model cannot answer, Ask says so; it does not put a passage from Concepts in place of the model's answer. Until the model is downloaded and loaded, Ask shows the passage from Concepts, and the model answers your question once it is ready. If an earlier version of OmniMathematics downloaded the smaller model it used then (Qwen3 0.6B, about 350 MB), 1.0 (24) removes those files on its first launch and asks you again before it downloads anything.

Like any file download, the request to Hugging Face gives Hugging Face the device's IP address and the standard request headers (which name the app and its version and the operating system version), and names the model repository and the files requested; Hugging Face handles it under its own terms. It does not include your question, your marks or anything you type. We do not receive that request. **Remove the downloaded model** in More ▸ Settings ▸ Ask model deletes the files and turns the switch off. It stays available wherever the files are on the device, including a device where Apple Intelligence has since become ready.

Your question is not stored as a record of its own, and it is never sent to us or to a hosted AI service.

---

## Purchases

OmniMathematics Pro is sold through Apple's in-app purchase as Monthly and Annual subscriptions, which renew automatically, and Lifetime, a one-time purchase. Apple processes the payment, handles refunds, and keeps its own record of the transaction under Apple's terms. StoreKit on your device checks with Apple whether you have Pro, and the answer stays on your device. The app sends nothing about a purchase to us. We do not collect payment details, and we never see them. Family Sharing is on for all three. The prices, the free trial and how to cancel are shown on the paywall in the app and in the [OmniMathematics Terms of Use](https://prameyallc.github.io/privacy/omnimath/terms/); Apple's standard EULA also applies.

---

## What OmniMathematics does not do

- No user accounts, and no way to create one.
- No ads of any kind, no advertising or analytics SDK, no advertising identifier (IDFA), no SKAdNetwork entries and no App Tracking Transparency prompt.
- No analytics or crash-reporting service — ours or anyone else's.
- No network requests to us. There is no server of ours for the app to talk to.
- No camera, photo library, microphone, contacts, calendar or file access.
- No location permission is requested, and the app uses no location APIs. Nothing in the app estimates your location by any other means either.
- No health, fitness or medical data of any kind.

---

## If you email us

If you write to admin@prameya.legal — a question, a bug report, a rights request — we receive your email address and whatever you put in the message. We keep it only as long as we need it to deal with your message and to keep a record that we did, and you can ask us to delete it. That mailbox is the only place Prameya holds anything about a user of this app.

---

## Children and OmniMathematics

**Who OmniMathematics is for.** Computer-science and engineering students, self-learners, teachers and adults who want to understand discrete mathematics. It is a general-audience educational app. It is not in the App Store Kids Category, and it is not designed or marketed for young children.

**What that means in practice, stated plainly.** Nothing is collected by us from anyone who uses OmniMathematics, at any age. There is no identifier we transmit, no advertising network and no server of ours. If a parent buys Pro, Apple processes that purchase, and Family Sharing is on. A child's marks are stored like an adult's: on the device and, if that Apple Account is signed in to iCloud, in that account's private database.

**What we do not do.** We do not knowingly collect personal information from children — we collect nothing from anyone, because there is nothing to collect and nowhere for it to go. We do not build profiles. The app has no school, classroom or ClassKit integration.

**What parents and guardians can do.** Use **Screen Time** to manage which apps a child can use, and write to us at admin@prameya.legal with any concern.

---

## Health data

OmniMathematics processes **no consumer health data**. It has no health, wellness, symptom, fitness or biometric features, no HealthKit access, and nothing in it is derived from your body or your care. Washington's My Health My Data Act, Nevada's SB 370 and similar consumer-health-data laws are therefore not engaged, and OmniMathematics has no separate consumer health data privacy policy. Other Prameya apps do — see the index at <https://prameyallc.github.io/privacy/>.

---

## HIPAA, FERPA and school privacy laws

- **HIPAA does not apply to OmniMathematics.** HIPAA governs health plans, health-care clearinghouses, most health-care providers, and their business associates. OmniMathematics is a consumer education app with no health function and no relationship to any of those.
- **FERPA does not apply.** FERPA binds schools and other educational agencies receiving federal funding, and those acting for them. OmniMathematics has no relationship with any school and holds no education records.
- **Student-privacy statutes** such as California's SOPIPA apply to services designed and marketed for K-12 school purposes. OmniMathematics is a consumer app and is not sold to schools. If that ever changes, this policy will be rewritten before it does.

---

## Your privacy rights

Because we hold nothing, most requests have a very short answer — but the routes are real and we will use them.

### Everyone

- **See what we hold about you.** Ask us. The answer is normally "your email to us, if you sent one, and nothing else".
- **Delete it.** Ask us to delete your correspondence. For the learning data on your device and in your iCloud, use **More ▸ Progress**: remove any single mark, or use **Remove Every Mark**. That is a genuine deletion, not a request to us.
- Write to **admin@prameya.legal**. We aim to respond within 30 days.

### California (CCPA / CPRA)

California residents have the rights to know, delete, correct, and to opt out of the sale or sharing of personal information, and not to be discriminated against for exercising them.

**Do Not Sell or Share My Personal Information.** We do not sell personal information, and we do not share it for cross-context behavioural advertising. There is no advertising in OmniMathematics, so there is nothing to opt out of. Apple (StoreKit, iCloud) and Hugging Face (the optional model download) are not cross-context behavioural advertising.

**Categories.** We collect none of the CCPA categories. No identifiers, no internet or network activity, no geolocation of any precision, no name, contact details, financial information, biometric, health, employment or education records. The only personal information Prameya ever holds about a user of this app is an email you choose to send us, at the address above.

**Sensitive personal information.** OmniMathematics does not collect sensitive personal information as California defines it.

**Minors.** We do not sell or share the personal information of consumers under 16 — or of anyone else, at any age.

**Global Privacy Control.** GPC is a browser signal and there is no established equivalent for native iOS apps. It makes no difference here: there is no sale or sharing for a GPC signal to stop.

**A candid note on scope.** Prameya is a very small company and may fall below the revenue and volume thresholds that make the CCPA legally binding. We describe and honour these choices regardless of whether we are required to.

### Other US states

Virginia, Colorado, Connecticut, Texas, Oregon, Montana and a growing number of other states give residents rights to access, correct, delete and port personal data, and specifically to opt out of targeted advertising and profiling. If any of those laws applies to us, the answer is the same one: no targeted advertising occurs in OmniMathematics, no profiling occurs, and no personal data is collected to access, correct, delete or port. Email us for anything else. Some of these states offer an appeal if we refuse a request — if we ever refuse yours, we will tell you how to appeal and how to contact your state Attorney General.

### EEA and United Kingdom (GDPR / UK GDPR)

This section applies if you are in the EEA or the UK.

**Controller.** Prameya LLC, contact admin@prameya.legal, is the controller for the only processing it carries out — correspondence you send us. There is no joint controller, and no processor: nobody processes personal data on our instructions. **Apple** runs the App Store checkout if you buy OmniMathematics Pro and decides for itself what it does with that transaction; we do not direct it, the app sends nothing about it to us, and we never see your payment details. If you choose to download the optional Ask model, **Hugging Face** receives that download request under its own terms; we do not direct it and do not receive it.

**Legal bases.**

- *Answering your email:* legitimate interests, or the steps needed to respond to you.

That is the whole list.

**Consent.** OmniMathematics shows no consent form. The two choices it asks you to make — whether to download the Ask model, and whether to turn on the daily reminder — stay on your device and can be changed in More ▸ Settings.

**Profiling.** None. No automated decision-making of any kind takes place, and nothing in the app builds a profile of you.

**Special-category data (Article 9).** None is processed. There is no health, biometric, racial, religious, political, trade-union or sexual-life data anywhere in this app.

**Your rights.** Access, rectification, erasure, restriction, portability, objection to processing based on legitimate interests, and withdrawal of consent. In practice these reach only an email you have sent us, because that is all that exists.

**International transfers.** None of yours, by us. We do not hold learning data to transfer. Purchases, if you make one, are processed by Apple.

**Complaints.** You may complain to your national data protection authority, or to the UK Information Commissioner's Office if you are in the UK.

**Children in Europe.** Where consent is the legal basis for processing a child's data, GDPR requires the child to be at least 16, or younger only with the consent of a parent or guardian, subject to each member state's lower age limit (never below 13). No consent-based processing of anyone's data occurs in OmniMathematics. See "Children and OmniMathematics" above.

---

## Security

There is not much to secure, and that is the design.

- Your learning data stays in the app's private storage on your device, protected by iOS and your passcode, and — if you are signed in — in your iCloud private database under Apple's terms. Use a passcode and keep iOS up to date.
- The app does not talk to our servers, so there is no traffic of yours to intercept on a path we run. StoreKit, iCloud, Handoff and the connection to Apple Watch are Apple's. The optional model download talks to Hugging Face.
- We operate no server holding user data, so there is no user database of ours that could be breached.

We make no claim to unbreakable security. No system is perfectly secure.

---

## Data retention

- **On your device:** kept until you remove it in More ▸ Progress or delete the app. The Ask model's files, if your device downloaded them, stay until you remove them in More ▸ Settings ▸ Ask model, delete the app, or the system clears storage space. The record of applied Apple Watch taps keeps each one for up to an hour.
- **In your iCloud, if you are signed in:** your marks, streak and where you left off, in your private database, and the key-value store entries described above, until you remove them in the app (which updates the iCloud copy), they are replaced, or you delete that iCloud data. Deleting the app on one device does not by itself empty iCloud.
- **With us:** only emails you send us, kept as long as needed to handle your message and to record that we handled it. Ask and we will delete yours.
- **With Apple, if you buy Pro:** Apple keeps its own record of the transaction, under Apple's terms and Apple's retention rules rather than ours.
- **With Hugging Face, if you download the Ask model:** whatever Hugging Face keeps about that download request, under Hugging Face's terms. We do not receive it.
- **With anyone else:** nothing.

---

## App Store privacy labels — one clarification

Apple's App Store privacy labels use Apple's own definition of "collect", which turns on data leaving your device. That definition is useful for reading the labels and nothing more. It does not shrink our duties under state or national privacy law, and we have not used it to narrow anything in this policy.

---

## Changes to this policy

We will update this policy when the app changes — and, where we can, before the change ships. When we do, we will change the effective date at the top and describe what changed. If a change materially expands what is collected or who receives it, we will tell you in the app rather than relying on you to re-read this page.

**23 September 2026 — what changed.** Ask now answers with an on-device model and shows what it writes:

- It says Ask sends your question as you typed it to Apple Intelligence where it is turned on and ready, or otherwise to the optional downloaded model, and shows the model's answer without checking or filtering it. Earlier versions said the model only rephrased a passage from Concepts, and that Ask showed the passage when an answer was refused or incomplete.
- It says the optional model is offered only where Apple Intelligence is not ready, and that downloaded files stay removable in Settings on every device.
- It says a question sent from Apple Watch is answered the way Ask on the iPhone answers it, and never starts a download.

Nothing the app collects or sends changed.

**15 September 2026 — what changed.** The optional Ask model is now chosen by the device's memory class, and this policy says so:

- It names the model an iPhone or iPad with 8 GB of memory is offered (MiniCPM5 2B, from `openbmb/MiniCPM5-2B-MLX` at commit `8a9ad753`, about 1.4 GB) and the model an iPhone or iPad with 12 GB of memory or more is offered (Gemma 4 E2B, from `mlx-community/gemma-4-E2B-it-qat-4bit` at commit `42f62737`, about 4.4 GB), and says that devices with 6 GB or less, and devices without Metal 3, are offered no model and always answer from Concepts and the packs. Earlier versions of this policy described one model for every device (Qwen3 0.6B, about 350 MB), then a 12 GB-only Gemma 4 E2B offer while MiniCPM5 2B was held out of the ladder.
- It says that the download runs only while the app is open, that the app checks free memory before offering the download and each time it loads the model, and that the downloaded files are verified model weights, not code.
- Later the same day: it names the smaller model a 12 GB device is offered when the memory check refuses Gemma 4 E2B, says both downloads stay until removed and that Settings offers the way back; it says the app keeps the screen on while a download runs, that the checked files include the tokenizer and the prompt-formatting template, what the download request's standard headers carry, and that the policy covers the iPad app where Apple lets it run on an Apple silicon Mac or Apple Vision Pro.
- Its list of what the app stores now says that your download choice is kept with the model and version it was given for, and that the first launch of 1.0 (24) removes the earlier model's files once and records that it did.

Nothing else the app collects or sends changed.

**14 September 2026 — what changed.** This policy was rewritten to describe only what OmniMathematics 1.0 does today:

- It covers iPhone and iPad and the Apple Watch app, and no longer mentions Apple TV.
- It says that the app asks to send notifications only when you turn on the daily study reminder in Settings.
- It names the controls in More ▸ Progress as the app shows them: **Remove Every Mark**, confirmed with **Remove Everything**.
- Its list of what the app stores now includes the record of applied Apple Watch taps on iPhone, the reminder switch, your Ask model choice, the model's files and two internal markers for moving stored marks to the current format.
- It describes **Ask the phone** on Apple Watch, which sends your question to your paired iPhone.
- It calls the app's built-in concept reference **Concepts**, as the app does from build 24; earlier drafts called it the Codex. The label on a retrieved Ask answer is **From Concepts**.
- It no longer says that we receive a transaction identifier or entitlement status from Apple: the app sends nothing about a purchase to us.
- It no longer repeats the history of the app's development, including earlier corrections to this policy and the bundle-identifier changes.

Nothing the app collects or sends was added by this revision. Earlier versions of this policy, with their own change entries, remain in the public repository that publishes these pages: <https://github.com/prameyallc/privacy>.

---

## Contact

**Prameya LLC**
Email: **admin@prameya.legal**
Privacy policies for all Prameya apps: <https://prameyallc.github.io/privacy/>
This policy: <https://prameyallc.github.io/privacy/omnimath/>

If you are writing about a privacy right, say which right and which app, and we will get to it faster.

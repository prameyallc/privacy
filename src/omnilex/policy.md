# OmniLex Privacy Policy

**Effective date:** 24 September 2026
**Publisher:** Prameya LLC ("Prameya", "we", "us"), a United States limited liability company
**Contact:** admin@prameya.legal
**Applies to:** the OmniLex app for iPhone, iPad, Mac and Apple Vision Pro, the Apple Watch app that comes with it, its Home Screen widget, and OmniLex for Apple TV — bundle ID `legal.prameya.OmniLex` (the Apple Watch app is `legal.prameya.OmniLex.watch`)

Other Prameya app policies: [prameyallc.github.io/privacy](https://prameyallc.github.io/privacy/)

---

## The short version

OmniLex is a legal AI tool for legal professionals. It reads contracts and other documents you import, flags clauses for your review, drafts from templates, answers questions, and searches your own documents.

- **Your documents stay on your device.** Reading, OCR, analysis, drafting, Ask and search all run locally on your Mac, iPhone, iPad or Apple Vision Pro. OmniLex never uploads your documents or anything derived from them. They stay on the device and in your own device backups.
- **We never receive your documents or anything derived from them.** Prameya runs no server that takes in your content. We have no account system and no database of users.
- **There are no accounts, no sign-in, no ads, no analytics and no tracking.**
- **A few things do leave the device, and none of them is your documents:**
    - **The AI model download.** OmniLex downloads the model it runs (about 420 MB, 1.1 GB or 2.5 GB, depending on the size you pick) from Hugging Face. That request asks for model files. It carries none of your documents or text.
    - **Small iCloud entries.** If you are signed in to iCloud on iPhone, iPad, Mac or Apple Vision Pro, OmniLex keeps four small entries in your iCloud key-value storage so your other devices, the widget, Apple Watch and Apple TV can offer to continue: which part of the app you were in, the identifier of the reference topic you last opened, a random identifier of the last document you opened, and your appearance choice. They never hold a document's title, file name or text. See [Your other devices](#your-other-devices-icloud-handoff-apple-watch-and-apple-tv), including how deleting your documents removes them.
    - **Handoff and Apple Watch.** Apple's Handoff and the connection between your iPhone and Apple Watch carry the same kind of "where you left off" information, and a question you send from the Watch to the iPhone.
    - **Purchases.** StoreKit on your device talks to Apple if you buy or restore OmniLex Pro.
- **Ask answers on your device.** Where Apple Intelligence is turned on and ready, Apple's on-device model answers; otherwise a model you have already downloaded answers. Your question is not sent to us.
- **One optional permission.** OmniLex asks to send notifications only if you turn on the re-check reminder in Settings on iPhone or iPad. It is off until you do.
- **If you are a lawyer:** your client material is not transmitted to us or to any third party by this app. See [If you are a lawyer](#if-you-are-a-lawyer-confidentiality-and-your-own-duties) for what you should know before putting privileged material into any software, including this one.

This policy explains the details, including the things we do not do.

---

## Who we are and what this policy covers

Prameya LLC publishes OmniLex. This policy covers the OmniLex app on iPhone, iPad, Mac and Apple Vision Pro, the Apple Watch app, the Home Screen widget and OmniLex for Apple TV, and nothing else.

Because we operate no back-end service for OmniLex, most of this policy describes what happens **on your own devices**, and on the Apple services your devices already use, not what we do with your data. We do not have your data.

---

## What OmniLex does with your documents

### Importing documents

You add documents through the system file picker (on Mac, the open panel), or by dragging files onto the document list. OmniLex can open PDFs, Word documents (.docx), plain text files, RTF files and images. OmniLex also includes a sample NDA, built from a public-domain template that ships inside the app; it is not a file of yours.

The app only ever sees the files you explicitly choose. It does not scan your disk, your Documents folder, or any other location on its own.

OmniLex does **not** use the camera and does **not** read your photo library. Images are brought in the same way as everything else: through the file picker or by dragging them in.

The app's build settings declare no camera permission, no photo-library permission and no local-network permission, because the app has no use for any of them. A test in the build fails if one of those permission strings reappears, so the permissions the app declares and this policy stay in agreement.

### Reading and OCR

Text is pulled out of your files on your device:

- Text-based PDFs are read with Apple's PDFKit.
- Scanned PDFs and images go through Apple's Vision framework for optical character recognition.
- Word documents are read on the device: on Mac with Apple's own text system, and on iPhone, iPad and Apple Vision Pro with a reader built into the app (it uses ZIPFoundation, an open-source library that ships inside the app, to open the file).

All of this runs locally on your hardware. No page image and no extracted text is uploaded anywhere for processing.

### Analysis, drafting and search

- **Reading-priority review, summaries, questions about a document, Document Background and Research explanations** run through the AI model you downloaded, which executes on your device using Apple silicon. Your document text is fed to that local model. It does not go over the network. If no model is on the device yet, these features say so and start no download; a document you import is stored and waits for its review until you download a model in Settings.
- **Semantic search** across your documents uses Apple's on-device language embeddings. Your search queries stay local.
- **The reference library, clause library, templates, glossary and legal skill pack** ship inside the app. They are read from the app bundle. Nothing is fetched at runtime.

### Ask and Apple Intelligence

Ask sends your question, up to eight earlier turns of the same conversation, and matching passages from the reference library that ships inside the app, to a language model running on your device:

- **Where Apple Intelligence is turned on and ready** (iPhone, iPad, Mac and Apple Vision Pro), Apple's on-device model answers first. While it answers it can look up further passages in the app's own reference library. OmniLex does not send your question to Apple or to us.
- **Otherwise, a model you have already downloaded** answers. Ask never starts a download.
- **Otherwise,** Ask says it cannot answer on this device.

Ask does not read your imported documents; questions about a particular document are asked from that document's page and answered by the downloaded model. Your Ask questions and the answers are saved in the chat history on the device (see the table below). The **On-device answers** switch in Settings turns Ask off. On Apple TV, Ask only quotes passages from the reference library; it runs no model.

### Where your documents live

OmniLex stores the following in a private database inside the app's own storage on your device:

| What | Details |
|---|---|
| Document record | Title, the extracted text of the document, an AI-generated summary, tags, and any notes you type |
| A pointer to the original file | A bookmark so the app can reopen the file you chose. The original file stays where you put it; OmniLex does not move or copy it into the cloud |
| Reading-priority flags | The clauses the model flagged, their reading priority, and suggested alternative wording |
| Search index | A copy of the first part of each document's text and a numeric representation (embedding) of it, used for on-device search |
| Chat history | Your Ask questions and the answers |
| Templates and saved notes | Anything you create in the app |

Alongside that database, the app keeps these small settings on the device:

| What | Why |
|---|---|
| Your appearance choice, the lowest reading priority to show, the **On-device answers** switch and the **Download over cellular** switch | To apply them |
| When you acknowledged the first-run Legal & Safety notice, and whether you have seen the introduction | So they show once |
| Random identifiers of the documents you opened most recently | To reopen where you left off |
| The re-check reminder switch, the identifiers of up to 200 reference topics you have opened on iPhone or iPad, and the reminders you have answered | For the re-check reminder (see below) |
| The model you selected, and which models are already downloaded | To load the right one |
| A random identifier of the document your free first review was spent on | So the free review is given once (see Subscriptions) |
| The random identifier the app gave the sample NDA, if you opened it | So opening it again shows the same sample |
| The downloaded AI model files, and the part of an unfinished download | To run the model on the device, and to resume a download |

**Your documents do not sync.** The document database uses no iCloud or CloudKit sync — the app has no iCloud container at all. If you install OmniLex on two devices, they share none of your documents. The only things OmniLex puts in iCloud are the small entries described under [Your other devices](#your-other-devices-icloud-handoff-apple-watch-and-apple-tv). There is no copy of your documents on any Prameya system to lose, subpoena, or breach.

**Device backups.** The document database is not excluded from backups, so if you have enabled Apple's device backup (iCloud Backup, or a backup to a computer), your operating system includes OmniLex's local database in that backup. That is a function of your device settings and Apple's services, not of anything OmniLex sends. The downloaded model files are excluded from device backups.

### Read Aloud

The Read Aloud feature passes the text you are listening to into your operating system's built-in speech synthesizer. That happens on your device. OmniLex makes no network request to produce speech.

### PDF reports

When you export a PDF report, you choose where it is saved (on Mac, **Export All Completed Reports** writes every completed report into a folder you pick). OmniLex writes the file to that location. It does not upload it. While it prepares the file it keeps a temporary copy in its own storage, excluded from device backups. **Export extracted text** hands a document's extracted text to the system share sheet, and you choose where it goes. **Copy** on a Document Background note puts the text on this device's clipboard only: on iPhone, iPad and Apple Vision Pro it is kept off Universal Clipboard and expires after two minutes, and on Mac it is kept to that Mac. What you do with an exported file afterwards — email it, put it in a document management system — is outside this app and outside this policy.

### Links to sources and other pages

The reference library cites public sources. When you tap **Open the source** or another source link, it opens in your web browser, which contacts that website under the website's own terms. OmniLex adds nothing of yours to the link. The same is true of the other links in the app — this policy, Support, Apple's standard licence agreement, the open-source project pages listed under Acknowledgements and, on Mac, **Manage Subscription** — and **Email support** opens your mail app with our address filled in; nothing is sent unless you send it.

---

## Your other devices: iCloud, Handoff, Apple Watch and Apple TV

### The iCloud key-value store

On iPhone, iPad, Mac and Apple Vision Pro, if you are signed in to iCloud, OmniLex keeps four small entries in its iCloud key-value storage in your own iCloud account. They are:

| Entry | What it holds |
|---|---|
| Where you left off | Which part of the app you were in, the identifier of the reference topic you last opened (for example, the topic on trade secrets), the random identifier of the last document you opened on that device, and when |
| Appearance | System, Light or Dark |
| Home Screen glance | The random identifier of the last document you opened or imported, the fixed words "Last matter" and "Open in OmniLex", and when |
| Pending open | Set for a moment when you tap the widget or run the **Open last matter** shortcut on iPhone or iPad, and removed when the app opens there: the random document identifier, or the word "continue". The Mac and Apple Vision Pro apps ignore it |

The identifiers are random codes the app gave your document or the names of topics in the app's own reference library. **These entries never hold a document's title, file name or text.** If an earlier build put a document's file name in the Home Screen glance, OmniLex replaces it with the neutral words above the next time it opens. Apple stores and syncs these entries under Apple's terms; Prameya cannot read them.

The Home Screen widget (iPhone and iPad), the Apple Watch app and its complication, and OmniLex for Apple TV read these entries. Because they live in your iCloud account, what one of your devices writes reaches the others signed in to the same account: a reference topic you were reading on your Mac can be continued on Apple TV or Apple Watch, and after you open a document on your Mac the widget on your iPhone shows "Last matter / Open in OmniLex" (tapping it opens the last document you reviewed on that iPhone, because documents do not sync).

**Removing them.** **Delete All Documents & Analyses**, on iPhone, iPad, Mac or Apple Vision Pro, removes all four entries from iCloud — and because the entries are shared, from every device signed in to the same iCloud account — and makes the app on that device forget the last document and reference topic you opened, so nothing it writes afterwards names them. Your Apple Watch then stops offering that topic, whether it learns of the change from iCloud or from your iPhone, and Apple TV shows nothing to continue. As you go on using the app, OmniLex writes the "where you left off" and appearance entries again, holding only the part of the app you are in, your appearance choice and when, until you open a topic or a document. Deleting a single document removes all four entries if the Home Screen glance points to that document; otherwise it removes that document's random identifier from the "where you left off" entry, the app forgets it, and Handoff and your Apple Watch get the updated information. Deleting the app does not remove the entries.

### Handoff

On iPhone, iPad, Mac and Apple Vision Pro, OmniLex uses Apple's Handoff to tell your nearby devices signed in to the same Apple Account where you left off: the same part-of-the-app, reference topic and random document identifier as above. A device that receives it opens that document only if the document is already on that device (documents do not sync); otherwise it opens the reference topic. It is not added to Spotlight search.

### The Home Screen widget and Shortcuts

On iPhone and iPad, the Home Screen widget shows "Last matter / Open in OmniLex" and opens the last document you reviewed on that device. Its text is marked privacy-sensitive, so the system can hide it when the device is locked. The **Open last matter** shortcut does the same thing.

### Apple Watch

The Apple Watch app comes with the iPhone app. It has **Learn** (the reference library, which ships on the Watch), **Now** (prompts to continue or pin a topic, or to answer a re-check reminder, and **Ask iPhone**) and **More** (the legal notice). It runs no AI model and holds none of your documents.

- Over Apple's connection between the two devices, your iPhone sends the Watch where you left off (the part of the app, the reference topic and the random document identifier) and any re-check prompts, which name reference topics. The Watch sends the iPhone your taps (Confirm, Snooze, Not now).
- **iCloud.** The Watch app also reads the "where you left off" and appearance entries described above from your iCloud key-value storage, so it can offer a reference topic you were reading on any of your devices, including your Mac, and match your appearance choice. When both routes carry "where you left off", the Watch keeps the more recent one. Confirming **Pin this topic** saves that topic in the "where you left off" entry, from the Watch itself and again from the iPhone when your tap reaches it. When the entries are removed, the Watch stops offering the topic.
- **The complication** on your watch face reads the same entry and shows only "Continue" or "Learn". It never shows the topic's name or anything about your documents.
- **Ask iPhone** sends the question you enter to OmniLex on your paired iPhone. While OmniLex is running on the iPhone, the iPhone answers it the way Ask does — Apple's on-device model where Apple Intelligence is turned on and ready, otherwise a model already downloaded on the iPhone — and sends the answer back; if neither can answer, or the **On-device answers** switch is off on the iPhone, it sends back a short message saying so. A question from the Watch never starts a model download. If the iPhone is not reachable, the question waits until it is.

### Apple TV

OmniLex for Apple TV reads the iCloud entries above to offer the reference topic you were reading and to match your appearance choice. It shows reference topics only — never your documents, which are not on the TV — writes nothing to iCloud, downloads no model and runs none: its Ask quotes passages from the reference library that ships with it.

None of this reaches Prameya.

---

## Re-check reminders

Each topic in the reference library records when its source is due to be re-checked. On iPhone and iPad, **Settings ▸ Preferences ▸ Remind me when a saved topic's source is due for re-checking** is off until you turn it on. Turning it on is the only thing in OmniLex that asks iOS for permission to send notifications, and iOS asks only if you have not answered before.

If you allow it, OmniLex schedules local notifications on the device, titled "Source due for re-check" and naming the topic, for reference topics you have opened whose re-check date has passed or comes up: a topic already past its date is announced within minutes of turning the switch on, and others at 9:00 your local time the day after their re-check date. Up to 20 are scheduled when you turn the switch on; each topic you open afterwards can add its own. iOS delivers them from the device; nothing is sent to us or to any server. Tapping a notification only opens its topic. **Confirm** or **Not now** records on the device that you have answered that topic's reminder; **Snooze** records nothing. Turning the switch off removes the pending reminders.

So that the reminder can cover topics you opened before turning it on, OmniLex keeps a list of up to 200 reference topics you have opened on that iPhone or iPad, even while the switch is off. It holds topic identifiers from the app's own library, never your documents. **Delete All Documents & Analyses** clears it, turns the switch off and removes pending reminders.

---

## Subscriptions and In-App Purchases

### Available tiers

There is one paid upgrade, **OmniLex Pro**, sold as three products. Buying any one of
them grants exactly the same Pro — there are no separate feature tiers.

| Product | Price (US) | Billing |
|---|---|---|
| OmniLex Pro Monthly | $7.99 | Auto-renews monthly. 7-day free trial. |
| OmniLex Pro Annual | $49.99 | Auto-renews yearly. 7-day free trial. |
| OmniLex Pro Lifetime | $129.99 | One-time purchase. Not a subscription. |

Family Sharing is enabled on all three. Subscriptions renew until you cancel;
Lifetime is a one-time non-consumable.

**What is free and stays free.** Without paying anything you get the reference library and its citations, document import and reading, as many documents as you like, export of a document's extracted text, Ask, and a reading-priority review of the first document you have analysed (reviewing the sample NDA does not use it), with no account and no time limit. Pro adds on-device search across your imported documents, reading-priority review of further documents, and formatted PDF reports.

**Pro does not add cloud sync, and there is no paid iCloud option.** OmniLex stores your
documents on your device in every case, paid or not. If a subscription lapses you keep your
own data and can still export its extracted text; only the Pro tools stop.

### Subscription tier data collection

**Free and Pro handle your data the same way.** Everything described in this policy applies in both.

The difference is only which features are available. In every case:
- Documents stay on your device.
- Nothing about your documents or notes is transmitted to Prameya.
- There is no analytics or tracking.

**Subscription unlocks professional features. It does not change what data is collected.**

To give the free first review once, OmniLex keeps on the device the random identifier of the document that review was spent on. **Delete All Documents & Analyses** does not remove that marker, by design, so deleting your documents does not give a second free review. It never leaves the device.

### Cancellation and refunds

Subscriptions are managed by Apple:
- **Cancel:** in OmniLex, **Settings ▸ Pro ▸ Manage Subscription** (on iPhone, iPad and Apple Vision Pro this opens Apple's own subscription sheet; on Mac it opens your App Store account page), or in the Settings app → your name → Subscriptions → OmniLex
- **Refund requests:** reportaproblem.apple.com

Prameya cannot cancel your subscription or issue refunds. Apple controls all billing.

### StoreKit transaction data

When you buy or restore Pro, StoreKit on your device completes and checks the purchase with Apple. Apple processes the payment and keeps its own record of the transaction under Apple's terms. OmniLex asks StoreKit which Pro product, if any, you currently have, and keeps the answer in memory while the app runs. It does not store transaction identifiers or purchase dates, and it sends nothing about a purchase to us. We do not collect payment details and never see them. Purchases are available on iPhone, iPad, Mac and Apple Vision Pro; the Apple Watch and Apple TV apps have no purchases.

---

## When OmniLex uses the network

### Downloading the AI model

The AI model OmniLex runs itself is not part of the app download. On iPhone, iPad, Mac and Apple Vision Pro, you choose one of three sizes in **Settings ▸ On-Device AI**, and the app downloads its files from **Hugging Face**. All three are unmodified, openly licensed (Apache-2.0) 4-bit conversions of Qwen3 models, each pinned to one version:

| Size in Settings | Hugging Face repository | Pinned commit | Download |
|---|---|---|---|
| Compact | `mlx-community/Qwen3-0.6B-4bit` | `73e3e38d` | about 420 MB |
| Standard (recommended, the default) | `mlx-community/Qwen3-1.7B-4bit` | `3b1b1768` | about 1.1 GB |
| Large | `mlx-community/Qwen3-4B-4bit` | `4dcb3d10` | about 2.5 GB |

**When a download starts.** A download of the model selected in Settings starts only when you choose **Download** there (or **Resume** a download you started). Features that need a model — a reading-priority review of a document you import or re-review, a question about a document, a Research explanation, Document Background, Ask, or a question sent from Apple Watch — use a model that is already on the device; if none is, they say so and start nothing. Downloads wait for Wi-Fi unless you turn on **Download over cellular** in the same section. On iPhone and iPad a download may continue for a short time after you leave the app.

The request starts at `huggingface.co`, which redirects the actual file transfer to Hugging Face's own content delivery hosts (for example `*.cdn.hf.co`; the precise host varies by region, and the download links are signed and short-lived).

What that request contains:

- The repository and version of the model you selected, and the names of the files being fetched.
- The ordinary technical information any internet request carries — your IP address, and standard connection headers, including a user-agent header that names the app.

What it does **not** contain:

- Any part of your documents.
- Any text you typed.
- Any identifier we created for you, because we do not create one. OmniLex uses no Hugging Face account or token.

Hugging Face is an independent third party and its handling of that request is governed by its own privacy policy at [huggingface.co/privacy](https://huggingface.co/privacy). We have no relationship with Hugging Face on your behalf and receive nothing back from them about you.

The downloaded files are the model weights, its tokenizer and its configuration: data the model reads, not executable code. They are stored in the app's own storage, excluded from device backups, and stay until you use **Delete All Documents & Analyses** or delete the app. **Unload** in Settings frees memory; it does not delete the files. Once the files are on your device, the AI runs entirely locally, including offline. You can switch airplane mode on after the download and every AI feature still works. OmniLex for Apple TV and the Apple Watch app never download a model.

All network connections the app makes are HTTPS. Plain HTTP is blocked at the app level: the app's transport security settings disable arbitrary loads, in web content as well as elsewhere.

**Practical note for confidential matters:** if you are working under a protective order or on a matter where even the fact of a network connection matters, download your model first, on a network you are comfortable with. Nothing else in OmniLex starts that download. After that, OmniLex does not need the internet.

### What we removed

An earlier build of OmniLex included a "Case Story" feature that sent search queries — derived from your document's contents and title — to a third-party search API at `api.duckduckgo.com`. That was inconsistent with how this app was described, and for an app holding privileged client material it was the wrong design. **That network path has been removed.**

It was deleted rather than switched off: the web-search service file no longer exists in the source, no call to that API remains anywhere in the app, and the feature (now called Document Background) has no network path of its own. The app's onboarding text, its copyright string and its privacy manifest have all been corrected to match. A test that reads the app's own source tree fails the build if outbound-network code appears anywhere outside the model downloader.

### Nothing else connects out

Apart from the model download, OmniLex's own code opens no network connection. That is what the source-tree test described above enforces. The other ways information leaves your device are Apple's services, reached through Apple's own frameworks and described above: the iCloud key-value entries, Handoff, the connection to Apple Watch, and StoreKit for purchases. A link you tap opens in your browser or mail app (see [Links to sources and other pages](#links-to-sources-and-other-pages)).

There is no telemetry, no crash reporting service, no advertising SDK, no attribution SDK, no remote configuration, and no "phone home" check. OmniLex does read the performance summaries Apple's MetricKit hands to apps on the device (launch time, hangs, disk writes, abnormal exits) and writes those numbers to the device's own log; it does not send them anywhere.

The app is built on third-party Swift packages — the on-device AI runtime, the Hugging Face model-downloading libraries, the ZIPFoundation library used to read Word documents, and the general-purpose packages those depend on. We have not yet completed a package-by-package review of those dependencies' own privacy manifests. So the statement we make here is the one we have actually verified: the only outbound connection in OmniLex's own code is the model download. We are not, in this policy, certifying each upstream package on top of that.

---

## Things we do not do

One line each, because these deserve a straight answer.

- **We do not have accounts.** There is nothing to sign up for and no password to lose. The app contains no sign-in of any kind.
- **We do not collect personal information.** We operate no server that receives it.
- **We do not sell or share your personal information.** We have none to sell.
- **We do not sync your documents.** OmniLex never sends them to iCloud or anywhere else; only the small entries described above go to iCloud. (A device backup you have turned on is Apple's, and includes them.)
- **We do not show ads.** There is no ad SDK in the app.
- **We do not track you** across apps or websites, and the app declares no tracking domains.
- **We do not use analytics.** There is no analytics SDK in the app. We do not know how many documents you have, what they say, or whether you opened the app today. Apple's own developer-facing App Store reporting is a separate thing that Apple runs, and it is described under [Third parties](#third-parties) below.
- **We do not train AI models on your data.** Your documents never reach us, so they cannot be training data. The models are unmodified third-party open-weight models downloaded to your device, or Apple's own on-device model.
- **We do not use cookies**, because there is no web service.
- **We do not share your data with law enforcement**, because we hold nothing to share. A request to us would return nothing about you.

---

## If you are a lawyer: confidentiality and your own duties

OmniLex is built for legal professionals, and this section is written for you rather than for a general audience.

**What stays on your device:** the documents you import, the text extracted from them, every prompt you type, every model output, your reading-priority flags, your drafts and your chat history. All of it.

**What the app transmits:** model file downloads from Hugging Face; the four small iCloud entries described above (the part of the app you were in, a reference-topic identifier, a random document identifier and your appearance choice), if you use iCloud on iPhone, iPad, Mac or Apple Vision Pro — your Apple Watch reads them and saves a topic you pin there; the same kind of "where you left off" information over Handoff and to your Apple Watch; a question you choose to send from Apple Watch to your own iPhone, and its answer; and purchase checks with Apple. No document, no excerpt, no summary, no title, no file name.

**What this does and does not do for your obligations.** ABA Model Rule 1.6 requires you to make reasonable efforts to prevent unauthorized disclosure of information relating to the representation. Software that keeps client material on hardware you control is a materially better posture than software that ships it to a vendor's servers. It is not, by itself, compliance. You remain responsible for:

- **Device security.** The strongest property of this design — everything is on your device — is also its main dependency. Use a passcode or password, enable full-disk encryption (FileVault on Mac), and do not leave the device unlocked and unattended. If someone gets into your unlocked device, they get into your documents.
- **Backups.** If your device backs up to iCloud or to another machine, your OmniLex database goes with it. Decide whether that is acceptable for the material you are putting in.
- **Shared and managed devices.** OmniLex has no per-user separation inside the app. Anyone who can unlock the device account can open the app.
- **Exported files.** A PDF report or exported text is an ordinary file. Once it leaves the app, this policy no longer describes what happens to it.
- **Your own client obligations.** Some engagement letters, protective orders and outside counsel guidelines restrict which tools may touch client material at all, regardless of where processing happens. Read them before importing.

> **On encryption at rest:** on iPhone, iPad and Apple Vision Pro, OmniLex sets an explicit data-protection class — `completeUnlessOpen` — on its document database and on the SQLite journal files that sit beside it, so the store is encrypted once closed and cannot be reopened until the device is unlocked. Two limits are worth stating rather than glossing: a file that is already open when the device locks stays readable until it is closed, and applying the class is best-effort — if the operating system refuses, the app still launches and the store falls back to the system's default protection. On Mac there is no equivalent per-file class, so the database is covered by FileVault, which is a device-level control you enable, not one the app can set. Beyond that, the app adds no encryption layer of its own. On a device with a passcode and disk encryption enabled, this is meaningful protection. On a device without one, it is not.

**On ethics guidance.** Florida Bar Ethics Opinion 24-1 addresses a lawyer's confidentiality duty when using generative AI, and discusses obtaining a client's informed consent before using a third-party generative AI service in a way that would disclose confidential information. The factual position for OmniLex is this: your material is processed by a model running on your own device, and the app sends none of your document content to us or to any third party; what does leave the device is listed above. What that factual position means for the informed-consent discussion in that opinion — and for the equivalent rules in your own jurisdiction — is a legal judgment for you and your own ethics counsel. We describe what the software does; we do not draw the conclusion for you.

**OmniLex is not legal advice and is not a lawyer.** Its output is a starting point for your own professional judgment. It can be wrong, and a general-purpose language model can state things about the law that are simply not so. Verify everything, particularly anything that looks like a citation. That is a competence point rather than a privacy point, but it is the most important sentence in this document for a professional user.

---

## Children

OmniLex is a professional tool for adults working in law. It is not directed to children and is not designed to appeal to children.

The app collects no personal information from anyone, including children, and contains no advertising. We therefore do not knowingly collect personal information from children under 13, and the Children's Online Privacy Protection Act (COPPA) notice-and-consent machinery has nothing to attach to here — there is no collection to consent to.

If you believe a child has somehow provided personal information to us, contact admin@prameya.legal and we will look into it. In practice, the only way to send us anything is to email us.

---

## Your privacy rights

Most privacy laws grant rights against a company that holds your data. **We do not hold your data.** Your OmniLex information is on your devices and in your own iCloud account, under your control.

You can act on it directly in the app: delete an individual document, use **Delete All Documents & Analyses** or **Clear All Assistant History** in **Settings ▸ Data Management**, export a PDF report or a document's extracted text to a location you choose, or delete the app — which removes the local database, including downloaded model files, but not the small iCloud entries described above.

Even so, here is exactly where you stand under the laws people ask about.

### California (CCPA/CPRA)

If you are a California resident:

- **Personal information we collect:** none through the app. If you email support, we hold your email address and whatever you write to us, for as long as needed to answer you.
- **Sensitive personal information:** we collect none. Note that documents you import may themselves contain sensitive information — but those documents stay on your device and never reach us.
- **Sale or sharing:** we do not sell personal information and do not share it for cross-context behavioral advertising. We have never done so.
- **Your rights** to know, delete, correct, opt out of sale/sharing, limit use of sensitive personal information, and not be discriminated against for exercising them all remain available. Because our records about you are limited to support email, a request will normally be answered by confirming we hold nothing else and deleting the support correspondence if you ask.
- **How to exercise them:** email admin@prameya.legal. We will verify your request by replying to the email address that made it. We aim to respond within 45 days as the statute provides.

### Other US states

Residents of states with comprehensive privacy laws — including Virginia, Colorado, Connecticut, Utah, Texas, Oregon, Montana and others — have analogous rights of access, correction, deletion, portability and opt-out. Our answer is the same: we hold no personal information about you beyond support correspondence, and the same email address will get you a response.

### Washington My Health My Data Act and Nevada SB 370

**These do not apply to OmniLex, because OmniLex processes no consumer health data.**

We want to be precise about why, because the definitions in these laws are broad. Washington's My Health My Data Act reaches data that is merely accessed, processed or derived — not only data that is transmitted somewhere. Nevada SB 370 works similarly. So "it never leaves the device" would not, on its own, be an answer.

The actual answer is that there is no health data in this app at any stage. OmniLex has no health features, requests no health permissions, contains no connection to Apple's HealthKit, and stores no health-related fields. It analyses contracts and legal documents.

If a document you import happens to mention someone's health, that document is your file, held on your device, and is not processed by us at all. Neither statute creates an obligation for Prameya on those facts. Accordingly, OmniLex publishes no separate consumer health data privacy policy — there is no consumer health data to describe.

### If you are outside the United States (GDPR / UK GDPR)

Where the EU or UK GDPR applies:

- **For the documents you put into OmniLex, you are the controller, not us.** The app is software running on your equipment. We receive no personal data from it and act as no one's processor for it.
- **For support email**, Prameya is the controller. The legal basis is our legitimate interest in answering your question (Article 6(1)(f)), or performance of a contract where your message concerns the app you have installed.
- **Special category data (Article 9)** — including health data, and data revealing legal matters that could touch on protected categories — may appear inside the documents you analyse. Because that processing happens entirely on your own device and we never receive the data, we are not the ones processing it. Your own lawful basis for holding client material is a matter between you and your clients.
- **International transfers:** we transfer nothing, because we receive nothing. Model downloads are a request from your device to Hugging Face; that transfer is between you and them. The small iCloud entries, Handoff and purchases are handled by Apple under your agreement with Apple.
- **Your rights** of access, rectification, erasure, restriction, portability and objection apply to the support correspondence we hold. Email admin@prameya.legal. You may also complain to your national supervisory authority, or the ICO in the UK.

---

## HIPAA

**HIPAA does not apply to OmniLex, and we do not claim HIPAA compliance.**

Prameya is not a HIPAA covered entity and is not your business associate. We do not receive, store or transmit protected health information, and no business associate agreement is offered or needed, because there is no relationship in which we would handle PHI.

If **you** are a business associate — for example, a firm handling PHI for a covered-entity client — using OmniLex is like using any other software installed on your own hardware. The data stays in your custody. Your own HIPAA Security Rule obligations for that device continue to apply, and we are not part of that chain because no PHI ever reaches us.

---

## Security

Honest specifics rather than adjectives:

- **Documents on-device only.** The most effective security control here is architectural: there is no server holding your documents, so there is no server to breach.
- **Device encryption.** Your local database sits inside the app's private container. On iPhone, iPad and Apple Vision Pro the app sets the `completeUnlessOpen` data-protection class on the store and its journal files; on Mac there is no equivalent per-file class and the store is covered by FileVault if you have FileVault turned on. Enable a passcode and, on Mac, FileVault. Without those, the protection is much weaker.
- **Sandboxing.** On Mac, OmniLex runs in Apple's App Sandbox with access only to the files and folders you pick.
- **HTTPS enforced.** The app is configured to refuse insecure connections. The only outbound connection its own code makes is the model download.
- **Third-party code.** There is no advertising, analytics, attribution or crash-reporting SDK in the app. The third-party code the app does include is the on-device AI runtime, the Hugging Face model-download libraries and the ZIPFoundation library, plus the general-purpose Swift packages those rely on. Our own code has exactly one outbound connection — the model download — and a test enforces that. A package-by-package review of those dependencies' own privacy manifests is still outstanding on our side, and until it is done we are not making a claim about each of them here.

No system is perfectly secure, and we are not going to pretend otherwise. What we can say precisely is that the failure modes here are device-level, not vendor-level.

---

## Keeping and deleting data

We keep nothing, so there is nothing for us to retain or delete.

On your devices:

- **Delete a document** in the app and its extracted text, summary, reading-priority flags and search index go with it, and its random identifier is removed from the iCloud entries, Handoff and your Apple Watch (see [Your other devices](#your-other-devices-icloud-handoff-apple-watch-and-apple-tv)).
- **Delete everything at once** from **Settings ▸ Data Management**. **Delete All Documents & Analyses** deletes every document, flag, analysis, chat message, note and template you created, the downloaded model files, the lists of recently opened documents and topics, your preferences and pending reminders, and the four iCloud entries, and the app forgets the last document and topic you opened. It keeps the marker that the free first review was used, the identifier the app gave the sample NDA, your first-run acknowledgement and the **Download over cellular** setting. **Clear All Assistant History** deletes the chat history only.
- **Delete the app** and the entire local database, including downloaded model files, is removed by the operating system. The iCloud entries are not; **Delete All Documents & Analyses** removes them.
- **Downloaded models** persist until you use **Delete All Documents & Analyses** or delete the app.
- **The iCloud entries** stay in your iCloud account until OmniLex replaces or removes them (see [Your other devices](#your-other-devices-icloud-handoff-apple-watch-and-apple-tv), including what the "where you left off" entry holds after a deletion).
- **Support email** is kept only as long as needed to handle your question, and we will delete it on request.

You do not have to ask us to delete anything, and there is no deletion request that would accomplish more than deleting it yourself.

---

## Third parties

Two, and only two, and neither receives your documents:

| Third party | Why | What they get |
|---|---|---|
| **Hugging Face** | Hosts the AI model files the app downloads | A request for model files, and the ordinary technical details of that connection (including your IP address) |
| **Apple** | App Store distribution and purchases, iCloud, Handoff, the connection to Apple Watch, notifications, Apple Intelligence, and the operating system frameworks the app runs on | If you use iCloud, the four small entries described above, stored in your own iCloud account; the "where you left off" information carried by Handoff and to your Apple Watch; purchase checks through StoreKit; and whatever Apple collects as your platform and store provider, under Apple's own privacy policy. Apple Intelligence runs Apple's model on your device, and OmniLex does not send your questions to Apple. Apple also makes developer-facing App Store reporting available to Prameya as the publisher; we have not audited what that reporting contains, so we make no claim here about it. What we can say is that it does not come from this app sending anything to us |

There are no other processors, no data brokers, no advertising partners and no analytics vendors. A website you open from a source link is visited by your browser, not by OmniLex.

---

## App Store privacy labels

Apple's App Store shows a privacy label built on Apple's definition of "collect," which means transmitting data off the device in a way that lets the developer or its partners access it for longer than it takes to service the request. Under that definition, OmniLex collects no data, and the app's privacy manifest declares no collected data types and no tracking.

We want to flag two things about that:

1. That definition governs the App Store label only. It does not narrow what state or national privacy laws require of us, and we have not used it that way anywhere in this policy.
2. The label is not the whole story about the network. The "no data collected" answer rests on the fact that nothing reaches Prameya or any partner of ours — the iCloud entries sit in your own iCloud account, which we cannot access — not on a claim that the app never opens a connection. OmniLex does make one outbound connection of its own, the model download, and uses Apple's iCloud, Handoff and Watch connection as described above. This policy tells you about them; the label format does not have a place for them.

---

## Changes to this policy

If we change how OmniLex handles data, we will update this policy and change the effective date at the top.

**24 September 2026 — what changed.** The Mac app and the Apple Watch app now use your iCloud key-value storage too:

- **Mac.** The Mac app keeps the same four small entries as iPhone, iPad and Apple Vision Pro, so where you left off, your appearance choice and the "Last matter" glance reach your other devices, and **Delete All Documents & Analyses** on the Mac removes the entries from all of them. The previous version said that on a Mac these entries stay on the Mac; that is no longer so. The pending-open entry, which only the iPhone and iPad widget and shortcut set, is now used only on iPhone and iPad; the Mac and Apple Vision Pro apps ignore it.
- **Apple Watch.** The Apple Watch app and its complication read the "where you left off" and appearance entries, and the Watch saves a topic you pin there. Previously the Watch got this information only from your iPhone. When both routes carry it, the Watch keeps the more recent one, and after the entries are removed it stops offering the topic. The complication shows only "Continue" or "Learn", never a topic's name.

What the entries hold is unchanged: never a document's title, file name or text. Nothing new is sent to Prameya.

**23 September 2026 — what changed.** This policy was rewritten to match what the current app does. Earlier versions said nothing syncs and that the model download was the only thing that ever left the device; that is not true of this app, and this version says what does:

- It describes the four small entries OmniLex keeps in your iCloud key-value storage on iPhone, iPad and Apple Vision Pro, and what they hold (never a document's title, file name or text).
- It describes Handoff, the Home Screen widget and the **Open last matter** shortcut, the Apple Watch app (including **Ask iPhone**), and OmniLex for Apple TV. Earlier versions covered iPhone, iPad and Mac only.
- It describes Ask: Apple Intelligence on the device where it is ready, otherwise a model already downloaded.
- It describes the optional re-check reminder, the only thing that asks for notification permission, and the list of opened reference topics it keeps on iPhone and iPad.
- It names the three model sizes, their Hugging Face repositories and pinned versions. Earlier versions did not name the models.
- It adds Word (.docx) import, and the ZIPFoundation library that reads it on iPhone, iPad and Apple Vision Pro.
- It corrects what Pro includes (there is no longer a three-document limit; the first reading-priority review is free), and no longer says the app stores transaction identifiers from Apple: it stores none.
- It corrects what **Delete All Documents & Analyses** removes and keeps, and no longer says the app keeps sensitive values in the Keychain: OmniLex's own code keeps nothing there. It also no longer states an App Store age rating.

A second revision the same day describes the app update that fixes the problems the first revision had to disclose:

- **Downloads start only from Settings.** An earlier version of this page said a model download could also start the first time you used a feature that needs the model — a review of an imported document, a question about a document, a Research explanation, or a question from Apple Watch. The app no longer does that: only **Download** in **Settings ▸ On-Device AI** downloads a model, and those features say when no model is on the device.
- **Ask iPhone.** A question from Apple Watch now follows the **On-device answers** switch on the iPhone and is answered the way Ask answers — Apple Intelligence first, then a model already downloaded — and never starts a download.
- **Deleting really forgets.** An earlier version said that after a deletion, the "where you left off" entry, Handoff and your Apple Watch could keep or get back the deleted document's random identifier until you quit OmniLex. The app no longer does that: **Delete All Documents & Analyses** and deleting a document now also make the app forget it, and remove its identifier from those places.
- **The in-app privacy text** (Settings ▸ Legal ▸ Privacy Policy) has been brought up to date: it now describes the iCloud entries, Handoff, Apple Watch, Apple Intelligence and reminders, and no longer says that OmniLex otherwise never uses the network.

Nothing new is sent to Prameya. The in-app privacy text is a shorter summary of this page. Where the app's text and this page differ, this page is the correct and complete description.

**8 August 2026 — what changed.** That revision corrected statements in the previous version so that they matched the code that shipped then. In particular: the third-party web-search path was confirmed deleted rather than pending removal; the camera, photo-library and local-network permission strings were gone from the build; the local database carried an explicit data-protection class on iPhone and iPad, and the policy said exactly what that class does and does not cover; and, where we had not verified something — the privacy manifests of the app's third-party Swift packages, and the contents of Apple's developer-facing App Store reporting — the policy said so plainly instead of implying more than we knew.

For any change that materially affects your privacy — in particular, **adding any new network destination the app connects to** — we will describe the change in the policy rather than quietly revising it, and we will surface it in the app so you see it before it takes effect. Adding a network connection is the kind of change this app should never make silently, and we are committing to that in writing.

Older versions of this policy are available on request, and in the public repository that publishes these pages: <https://github.com/prameyallc/privacy>.

---

## Contact

Questions, privacy requests, or a correction to something in this policy:

**admin@prameya.legal**
Prameya LLC, United States

This policy: <https://prameyallc.github.io/privacy/omnilex/>
Other Prameya app privacy policies: [prameyallc.github.io/privacy](https://prameyallc.github.io/privacy/)

---

*OmniLex is a tool for legal professionals. It does not provide legal advice, does not create a lawyer-client relationship, and its output must be reviewed by a qualified lawyer before it is relied on.*

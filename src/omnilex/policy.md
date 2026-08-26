# OmniLex Privacy Policy

**Effective date:** 8 August 2026
**Publisher:** Prameya LLC ("Prameya", "we", "us"), a United States limited liability company
**Contact:** admin@prameya.legal
**Applies to:** the OmniLex app for iPhone, iPad and Mac

Other Prameya app policies: [prameyallc.github.io/privacy](https://prameyallc.github.io/privacy/)

---

## The short version

OmniLex is a legal AI tool for legal professionals. It reads contracts and other documents you import, flags risks, drafts from templates, and searches your own documents.

- **Your documents stay on your device.** Reading, OCR, analysis, drafting and search all run locally on your Mac, iPhone or iPad.
- **We never receive your documents or anything derived from them.** Prameya runs no server that takes in your content. We have no account system and no database of users.
- **There are no accounts, no sign-in, no ads, no analytics and no tracking.**
- **The app does connect to the internet for one thing: downloading the AI model.** The first time you use the AI features, OmniLex downloads model weights (roughly 420 MB to 2.5 GB, depending on the model you pick) from Hugging Face. That request asks for a model file. It does not contain your documents, your text, or anything about you beyond the ordinary connection details any download involves.
- **If you are a lawyer:** your client material is not transmitted to us or to any third party by this app. See [If you are a lawyer](#if-you-are-a-lawyer-confidentiality-and-your-own-duties) for what you should know before putting privileged material into any software, including this one.

This policy explains the details, including the things we do not do.

---

## Who we are and what this policy covers

Prameya LLC publishes OmniLex. This policy covers the OmniLex app only.

Because we operate no back-end service for OmniLex, most of this policy describes what happens **on your own device**, not what we do with your data. We do not have your data.

---

## What OmniLex does with your documents

### Importing documents

You add documents through the system file picker. OmniLex can open PDFs, plain text files, RTF files and images.

The app only ever sees the files you explicitly choose. It does not scan your disk, your Documents folder, or any other location on its own.

OmniLex does **not** use the camera and does **not** read your photo library. Images are brought in through the same file picker as everything else.

The app's build settings declare no camera permission, no photo-library permission and no local-network permission, because the app has no use for any of them. A test in the build fails if one of those permission strings reappears, so the permissions the app declares and this policy stay in agreement.

### Reading and OCR

Text is pulled out of your files on your device:

- Text-based PDFs are read with Apple's PDFKit.
- Scanned PDFs and images go through Apple's Vision framework for optical character recognition.

Both are Apple frameworks running locally on your hardware. No page image and no extracted text is uploaded anywhere for processing.

### Analysis, drafting and search

- **Risk analysis and drafting** run through an AI model that executes on your device using Apple silicon. Your document text is fed to that local model. It does not go over the network.
- **Semantic search** across your documents uses Apple's on-device language embeddings. Your search queries stay local.
- **The clause library, templates, glossary and legal skill pack** ship inside the app. They are read from the app bundle. Nothing is fetched at runtime.

### Where your documents live

OmniLex stores the following in a private database inside the app's own storage on your device:

| What | Details |
|---|---|
| Document record | Title, the extracted text of the document, an AI-generated summary, tags, and any notes you type |
| A pointer to the original file | A bookmark so the app can reopen the file you chose. The original file stays where you put it; OmniLex does not move or copy it into the cloud |
| Risk findings | The issues the model flagged, their severity, and suggested fixes |
| Chat history | Your conversations with the in-app assistant |
| Templates and saved notes | Anything you create in the app |
| Preferences | Your risk threshold and disclaimer setting |
| Model files | The downloaded AI model weights |

**None of this syncs.** OmniLex does not use iCloud, CloudKit, or any other sync service — the app carries no iCloud or CloudKit entitlement at all. If you install OmniLex on two devices, they share nothing. There is no copy of your data on any Prameya system to lose, subpoena, or breach.

Note that if you have enabled Apple's device backup (iCloud Backup or an encrypted local backup), your operating system may include OmniLex's local database in that backup. That is a function of your device settings and Apple's services, not of anything OmniLex sends.

### Read Aloud

The Read Aloud feature passes the text you are listening to into your operating system's built-in speech synthesizer. That happens on your device. OmniLex makes no network request to produce speech.

### PDF reports

When you export a risk report, you choose where the PDF is saved. OmniLex writes the file to that location. It does not upload it. What you do with the file afterwards — email it, put it in a document management system — is outside this app and outside this policy.

---

## Subscriptions and In-App Purchases

### Available tiers

OmniLex offers three annual subscription tiers:

| Feature | Clerk ($49/yr) | Associate ($149/yr) | Partner ($299/yr) |
|---------|----------------|---------------------|-------------------|
| Document Templates | Basic set | Extended set | Complete library |
| Legal Research Access | Limited | Standard | Comprehensive |
| Citation Tools | Basic | Advanced | Professional |
| CloudKit Sync | Preferences only | Preferences + notes | Full sync |
| Export Formats | PDF | PDF, DOCX | PDF, DOCX, RTF |

### What Apple receives

All transactions go through Apple's App Store. When you subscribe:
- **Apple receives:** Your Apple Account ID, payment method, transaction details
- **Prameya receives:** A transaction ID from StoreKit, subscription status (active/expired), tier purchased
- **Prameya does NOT receive:** Your name, email, payment card details, or Apple Account credentials

### Data Linked to You

Apple's privacy labels mark Purchase History as "Data Linked to User" for subscribers.

**This does NOT mean your legal documents are transmitted.** Documents, notes, and research history remain on-device only (or in your iCloud if you enable sync). StoreKit tells us you're a paying subscriber so we can unlock features — it does not transmit your documents or work product.

### Subscription tier data collection

**All tiers collect the same types of data** (documents you create, research queries, usage history).

The difference is:
- **What features are available** (template library size, research depth, export formats)
- **Whether notes sync between devices** (varies by tier)

In all tiers:
- Documents stay on your device (or in your iCloud if enabled)
- No transmission of documents or notes to Prameya
- No analytics or tracking

**Subscription unlocks professional features. It does not change what data is collected.**

### Cancellation and refunds

Subscriptions are managed by Apple:
- **Cancel:** iOS Settings → your name → Subscriptions → OmniLex
- **Refund requests:** reportaproblem.apple.com

Prameya cannot cancel your subscription or issue refunds. Apple controls all billing.

### StoreKit transaction data

When you purchase a subscription, the app receives and stores locally on your device:
- Transaction ID (an opaque identifier from Apple)
- Product ID (which tier you purchased)
- Purchase and expiration dates

This data:
- Is stored only on your device
- Is NOT synced to iCloud
- Is used only to unlock tier-appropriate features
- Is deleted when you use "Delete All Data"

---

## When OmniLex uses the network

### Downloading the AI model

OmniLex ships without an AI model. The first time you use an AI feature, you choose a model and the app downloads its weights from **Hugging Face**. The request starts at `huggingface.co`, which redirects the actual file transfer to Hugging Face's content delivery hosts (currently `*.cdn.hf.co`; the precise host varies by region, and the download links are signed and short-lived).

What that request contains:

- The identifier of the model you selected and the files being fetched.
- The ordinary technical information any internet request carries — your IP address, and standard connection headers.

What it does **not** contain:

- Any part of your documents.
- Any text you typed.
- Any identifier we created for you, because we do not create one.

Hugging Face is an independent third party and its handling of that request is governed by its own privacy policy at [huggingface.co/privacy](https://huggingface.co/privacy). We have no relationship with Hugging Face on your behalf and receive nothing back from them about you.

The download is a one-time event per model. Once the weights are on your device, the AI runs entirely locally, including offline. You can switch airplane mode on after the download and every AI feature still works.

All network connections the app makes are HTTPS. Plain HTTP is blocked at the app level: the app's transport security settings disable arbitrary loads, in web content as well as elsewhere.

**Practical note for confidential matters:** if you are working under a protective order or on a matter where even the fact of a network connection matters, download your model first, on a network you are comfortable with. After that, OmniLex does not need the internet.

### What we removed

An earlier build of OmniLex included a "Case Story" feature that sent search queries — derived from your document's contents and title — to a third-party search API at `api.duckduckgo.com`. That was inconsistent with how this app was described, and for an app holding privileged client material it was the wrong design. **That network path has been removed.**

It was deleted rather than switched off: the web-search service file no longer exists in the source, no call to that API remains anywhere in the app, and the Case Story screen has no network path of its own. The app's onboarding text, its copyright string and its privacy manifest have all been corrected to match. A test that reads the app's own source tree fails the build if outbound-network code appears anywhere outside the model downloader.

### Nothing else connects out

Apart from the model download, OmniLex's own code makes no network requests. There is no telemetry, no crash reporting service, no advertising SDK, no attribution SDK, no remote configuration, and no "phone home" check. That is what the source-tree test described above enforces.

The app is built on third-party Swift packages — the on-device AI runtime, the Hugging Face model-downloading libraries, and the general-purpose packages those depend on. We have not yet completed a package-by-package review of those dependencies' own privacy manifests. So the statement we make here is the one we have actually verified: the only outbound connection in OmniLex's own code is the model download. We are not, in this policy, certifying each upstream package on top of that.

---

## Things we do not do

One line each, because these deserve a straight answer.

- **We do not have accounts.** There is nothing to sign up for and no password to lose. The app contains no sign-in of any kind.
- **We do not collect personal information.** We operate no server that receives it.
- **We do not sell or share your personal information.** We have none to sell.
- **We do not show ads.** There is no ad SDK in the app.
- **We do not track you** across apps or websites, and the app declares no tracking domains.
- **We do not use analytics.** There is no analytics SDK in the app. We do not know how many documents you have, what they say, or whether you opened the app today. Apple's own developer-facing App Store reporting is a separate thing that Apple runs, and it is described under [Third parties](#third-parties) below.
- **We do not train AI models on your data.** Your documents never reach us, so they cannot be training data. The models are unmodified third-party open-weight models downloaded to your device.
- **We do not use cookies**, because there is no web service.
- **We do not share your data with law enforcement**, because we hold nothing to share. A request to us would return nothing about you.

---

## If you are a lawyer: confidentiality and your own duties

OmniLex is built for legal professionals, and this section is written for you rather than for a general audience.

**What stays on your device:** the documents you import, the text extracted from them, every prompt you type, every model output, your risk findings, your drafts and your chat history. All of it.

**What the app transmits:** model weight downloads from Hugging Face, and nothing else. No document, no excerpt, no summary, no title, no metadata about your matters.

**What this does and does not do for your obligations.** ABA Model Rule 1.6 requires you to make reasonable efforts to prevent unauthorized disclosure of information relating to the representation. Software that keeps client material on hardware you control is a materially better posture than software that ships it to a vendor's servers. It is not, by itself, compliance. You remain responsible for:

- **Device security.** The strongest property of this design — everything is on your device — is also its main dependency. Use a passcode or password, enable full-disk encryption (FileVault on Mac), and do not leave the device unlocked and unattended. If someone gets into your unlocked device, they get into your documents.
- **Backups.** If your device backs up to iCloud or to another machine, your OmniLex database goes with it. Decide whether that is acceptable for the material you are putting in.
- **Shared and managed devices.** OmniLex has no per-user separation inside the app. Anyone who can unlock the device account can open the app.
- **Exported files.** A PDF risk report you export is an ordinary file. Once it leaves the app, this policy no longer describes what happens to it.
- **Your own client obligations.** Some engagement letters, protective orders and outside counsel guidelines restrict which tools may touch client material at all, regardless of where processing happens. Read them before importing.

> **On encryption at rest:** on iPhone and iPad, OmniLex sets an explicit data-protection class — `completeUnlessOpen` — on its document database and on the SQLite journal files that sit beside it, so the store is encrypted once closed and cannot be reopened until the device is unlocked. Two limits are worth stating rather than glossing: a file that is already open when the device locks stays readable until it is closed, and applying the class is best-effort — if the operating system refuses, the app still launches and the store falls back to the system's default protection. On Mac there is no equivalent per-file class, so the database is covered by FileVault, which is a device-level control you enable, not one the app can set. Beyond that, the app adds no encryption layer of its own. On a device with a passcode and disk encryption enabled, this is meaningful protection. On a device without one, it is not.

**On ethics guidance.** Florida Bar Ethics Opinion 24-1 addresses a lawyer's confidentiality duty when using generative AI, and discusses obtaining a client's informed consent before using a third-party generative AI service in a way that would disclose confidential information. The factual position for OmniLex is this: your material is processed by a model running on your own device, and the app discloses none of it to us or to any third party. What that factual position means for the informed-consent discussion in that opinion — and for the equivalent rules in your own jurisdiction — is a legal judgment for you and your own ethics counsel. We describe what the software does; we do not draw the conclusion for you.

**OmniLex is not legal advice and is not a lawyer.** Its output is a starting point for your own professional judgment. It can be wrong, and a general-purpose language model can state things about the law that are simply not so. Verify everything, particularly anything that looks like a citation. That is a competence point rather than a privacy point, but it is the most important sentence in this document for a professional user.

---

## Children

OmniLex is a professional tool for adults working in law. It is not directed to children, is not designed to appeal to children, and is rated for a mature audience in the App Store.

The app collects no personal information from anyone, including children, and contains no advertising. We therefore do not knowingly collect personal information from children under 13, and the Children's Online Privacy Protection Act (COPPA) notice-and-consent machinery has nothing to attach to here — there is no collection to consent to.

If you believe a child has somehow provided personal information to us, contact admin@prameya.legal and we will look into it. In practice, the only way to send us anything is to email us.

---

## Your privacy rights

Most privacy laws grant rights against a company that holds your data. **We do not hold your data.** Your OmniLex information is on your device, under your control.

You can act on it directly in the app: delete an individual document, use **Delete All Documents & Risks** or **Clear All Assistant History** in Settings, export a risk report as a PDF to a location you choose, or delete the app — which removes the local database, including downloaded model files.

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
- **International transfers:** we transfer nothing, because we receive nothing. Model downloads are a request from your device to Hugging Face; that transfer is between you and them.
- **Your rights** of access, rectification, erasure, restriction, portability and objection apply to the support correspondence we hold. Email admin@prameya.legal. You may also complain to your national supervisory authority, or the ICO in the UK.

---

## HIPAA

**HIPAA does not apply to OmniLex, and we do not claim HIPAA compliance.**

Prameya is not a HIPAA covered entity and is not your business associate. We do not receive, store or transmit protected health information, and no business associate agreement is offered or needed, because there is no relationship in which we would handle PHI.

If **you** are a business associate — for example, a firm handling PHI for a covered-entity client — using OmniLex is like using any other software installed on your own hardware. The data stays in your custody. Your own HIPAA Security Rule obligations for that device continue to apply, and we are not part of that chain because no PHI ever reaches us.

---

## Security

Honest specifics rather than adjectives:

- **On-device only.** The most effective security control here is architectural: there is no server holding your documents, so there is no server to breach.
- **Device encryption.** Your local database sits inside the app's private container. On iPhone and iPad the app sets the `completeUnlessOpen` data-protection class on the store and its journal files; on Mac there is no equivalent per-file class and the store is covered by FileVault if you have FileVault turned on. Enable a passcode and, on Mac, FileVault. Without those, the protection is much weaker.
- **Sandboxing.** On Mac, OmniLex runs in Apple's App Sandbox with access only to the files you pick.
- **HTTPS enforced.** The app is configured to refuse insecure connections. The only outbound connection is the model download.
- **Keychain.** Sensitive flags and keys the app needs are held in the system Keychain rather than in ordinary storage.
- **Third-party code.** There is no advertising, analytics, attribution or crash-reporting SDK in the app. The third-party code the app does include is the on-device AI runtime and the Hugging Face model-download libraries, plus the general-purpose Swift packages those rely on. Our own code has exactly one outbound connection — the model download — and a test enforces that. A package-by-package review of those dependencies' own privacy manifests is still outstanding on our side, and until it is done we are not making a claim about each of them here.

No system is perfectly secure, and we are not going to pretend otherwise. What we can say precisely is that the failure modes here are device-level, not vendor-level.

---

## Keeping and deleting data

We keep nothing, so there is nothing for us to retain or delete.

On your device:

- **Delete a document** in the app and its extracted text, summary and risk findings go with it.
- **Delete everything at once** from Settings, using **Delete All Documents & Risks** and **Clear All Assistant History**.
- **Delete the app** and the entire local database, including downloaded model files, is removed by the operating system.
- **Downloaded models** persist until you remove them from the app's model settings or delete the app.
- **Support email** is kept only as long as needed to handle your question, and we will delete it on request.

You do not have to ask us to delete anything, and there is no deletion request that would accomplish more than deleting it yourself.

---

## Third parties

Two, and only two, and neither receives your content:

| Third party | Why | What they get |
|---|---|---|
| **Hugging Face** | Hosts the AI model weights the app downloads | A request for a model file, and the ordinary technical details of that connection (including your IP address) |
| **Apple** | App Store distribution, and the operating system frameworks the app runs on | Whatever Apple collects as your platform and store provider, under Apple's own privacy policy. Apple also makes developer-facing App Store reporting available to Prameya as the publisher; we have not audited what that reporting contains, so we make no claim here about it. What we can say is that it does not come from this app sending anything — OmniLex's only outbound connection is the model download, and it transmits nothing to Apple |

There are no other processors, no data brokers, no advertising partners and no analytics vendors.

---

## App Store privacy labels

Apple's App Store shows a privacy label built on Apple's definition of "collect," which means transmitting data off the device. Under that definition, OmniLex collects no data, and the app's privacy manifest declares no collected data types and no tracking.

We want to flag two things about that:

1. That definition governs the App Store label only. It does not narrow what state or national privacy laws require of us, and we have not used it that way anywhere in this policy.
2. The label is not the whole story about the network. The "no data collected" answer rests on the fact that no user content is transmitted — not on a claim that the app never opens a connection. OmniLex does make one outbound connection, the model download, even though no user data goes with it. This policy tells you about it; the label format does not have a place for it.

---

## Changes to this policy

If we change how OmniLex handles data, we will update this policy and change the effective date at the top.

This revision, effective 8 August 2026, corrected statements in the previous version so that they match the code that actually ships. In particular: the third-party web-search path is now confirmed deleted rather than pending removal; the camera, photo-library and local-network permission strings are gone from the build; the local database now carries an explicit data-protection class on iPhone and iPad, and this policy says exactly what that class does and does not cover; and, where we had not verified something — the privacy manifests of the app's third-party Swift packages, and the contents of Apple's developer-facing App Store reporting — this policy now says so plainly instead of implying more than we know.

For any change that materially affects your privacy — in particular, **adding any new network destination the app connects to** — we will describe the change in the policy rather than quietly revising it, and we will surface it in the app so you see it before it takes effect. Adding a network connection is the kind of change this app should never make silently, and we are committing to that in writing.

Older versions of this policy are available on request.

---

## Contact

Questions, privacy requests, or a correction to something in this policy:

**admin@prameya.legal**
Prameya LLC, United States

Other Prameya app privacy policies: [prameyallc.github.io/privacy](https://prameyallc.github.io/privacy/)

---

*OmniLex is a tool for legal professionals. It does not provide legal advice, does not create a lawyer-client relationship, and its output must be reviewed by a qualified lawyer before it is relied on.*
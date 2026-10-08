# Consumer Health Data Privacy Policy — OmniDerm

**Effective date:** 8 October 2026 *(supersedes the 7 October 2026 version; what changed is listed in section 12)*
**Publisher:** Prameya LLC ("Prameya", "we", "us"), a United States limited liability company
**Contact:** admin@prameya.legal
**Applies to:** the OmniDerm app (bundle ID `legal.prameya.OmniDerm`) on iPhone, iPad, Mac and Apple Vision Pro, its Apple Watch app, its Apple TV app, and its widgets

This is a **separate policy**, required by the **Washington My Health My Data Act (RCW ch. 19.373)** and provided to meet the parallel duty under **Nevada SB 370 (2023)**. It sits alongside, and does not replace, the [OmniDerm Privacy Policy](https://prameyallc.github.io/privacy/omniderm/). Where the two overlap, both are true; this one goes into more detail about health information specifically.

It applies to everyone who uses OmniDerm. Washington and Nevada residents have specific statutory rights, set out at the end.

---

## The short version

- OmniDerm processes information about your skin and your skin-care habits. Under Washington law that is **consumer health data**, even though it is processed on your device.
- **We do not receive any of it.** Prameya has no server that takes it, no database that holds it, and no account that identifies you.
- **We share it with no one.** Not affiliates, not processors, not advertisers, not data brokers, not researchers, not AI companies.
- **We do not sell it.** We never have and we will not.
- **The photo self-check is switched off in the shipping app.** The app produces no observations about a photograph. You can still save a journal photograph to this device; it is not analysed.
- **Ask answers typed questions with a language model on your device** (Apple Intelligence, or a model you choose to download). Your questions are not sent to us or to any AI service, and are not saved.
- **Where it can leave the device, at your direction, to Apple:** your journal notes and habit logs are in your device backup if you back up your device (journal photographs are excluded); if you turn on iCloud Sync and Handoff, a small set of app settings and the widget's suggested next topic are stored in your own iCloud account, and Handoff tells your own nearby devices which tab you are on. The identifier of a topic you open, the list of topics you opened, and Handoff of that topic go only after you also allow remembering topics you open, which stays off until you allow it. When you tap **Read this topic** on your Apple Watch, your iPhone sends the Watch that identifier only when remembering is allowed. The topics you opened can reveal sexual-health information, such as that you read about pubic lice. Reading a topic does not require the allow. Prameya cannot read any of it.
- You can withdraw consent and delete everything yourself, immediately, without asking us.

---

## Why this policy exists even though nothing reaches us

Apple's App Store privacy labels define "collect" as transmitting data off the device **in a way the developer or its partners can access**. By that definition, OmniDerm collects nothing.

**Washington's definition is much broader.** Under RCW 19.373.010, "collect" means to buy, rent, access, retain, receive, acquire, **infer, derive, or otherwise process** consumer health data in any manner. That reaches data that is merely accessed on your device, and it would reach anything a model **infers or derives** from a photograph of your own skin.

So we do not use the Apple definition to argue our way out of Washington law, and we are not going to tell you that state health-privacy rules do not apply because nothing is uploaded. They apply. This policy is written to them.

---

## 1. Categories of consumer health data collected, and why

"Collected" below is used in Washington's broad sense — accessed, processed, inferred or derived — not "sent to Prameya". **None of the following is transmitted to Prameya.**

| Category | What it actually is | Why the app processes it | Where it is kept |
|---|---|---|---|
| **Journal photographs of your skin** | A photo you attach to a journal entry, re-encoded as a JPEG with its location and other metadata removed | Shown back to you on your journal timeline, and in same-area compare with Pro | This device only. Excluded from backup, never uploaded, never synced, never assessed. |
| **Inferences derived from a skin image** | Any observation a model might produce about an image | **None.** The shipping app produces no observations, flags or ratings about a photo, and offers no image model while the clearance gate is closed. | — |
| **Journal entries** | Date, body area, a note you type, a lighting note, and whether a photograph is attached | Shown back to you on your journal timeline | This device, and your device backup if you make one |
| **Skin-care habit records** | Date, whether you did morning sunscreen, reapplied, did barrier care, and looked at the same area of skin today, and where the log was made (for example Do, or your Apple Watch) | To show your history, streak and consistency in the app | This device, and your device backup |
| **Derived habit measures** | Streak length, 30-day consistency percentage, a plain-language summary | Computed on your device from your own habit records, to show you your own patterns | Computed on this device when shown, and written into an export you make |
| **Your stated goals** | Free text you type, such as "build daily SPF habit" | Kept so you can see and edit them in Settings, and included in your export and appointment pack. They do not change anything else the app shows or records. | This device, and your device backup |
| **Questions you type in Ask, and the answers** | Your question, the last few lines of the conversation, and the model's answer | To answer the question, with Apple Intelligence or the model you downloaded, running on the device | In memory for the conversation on screen; not saved, not synced, not sent to us or to any AI service |
| **Skin-care topics you open** | The identifiers of the topic held for continuing (the last topic you opened in Understand, by any route), of the topics you opened in Understand while remembering was allowed and the switch was on, and of the next suggested topic. When remembering is allowed and you turn the switch on, the topic held for continuing at that moment can join that list too, even if you opened it while the switch was off. Each identifier names its topic. Some name skin conditions, rare diseases (for example epidermolysis bullosa) or infections and infestations. They can also name sexually transmitted or sexual-contact conditions: one names pubic lice, which the source the topic quotes says usually spread through sexual contact. So this list can reveal sexual-health information, such as that you read about pubic lice. | To let you continue on your other devices and to suggest the next topic | Opened-topic identifiers go to your own iCloud key-value storage, and, while the app is open, Handoff to your own nearby devices, only while iCloud Sync and Handoff is on and you have allowed remembering. The widget's suggested next topic follows the iCloud switch alone and is not that list. Switching sync off, Clear All Local Data, or declining remembering removes stored topic identifiers and stops Handoff of the topic. Apple TV opens on its Continue tab and shows the topic held for continuing only after remembering is allowed. **Read this topic** on your Apple Watch sends the identifier only when remembering is allowed. Reading a topic does not require the allow. |

**Not collected, in any sense:** your location (precise or approximate — location metadata is removed from journal photographs), biometric identifiers, genetic data, contacts, microphone or audio, camera input, Apple Health data, clinical health records from any provider, prescriptions, diagnoses, insurance or payment information, gender-affirming or reproductive health information (a topic you open about sexual health, such as pubic lice, is part of "Skin-care topics you open" above and is handled as described there), or any identifier that would let anyone link this app's data to you by name.

The app does not use geofencing of any kind, and does not use a geofence around any health care facility.

## 2. Sources of the data

| Source | What comes from it |
|---|---|
| **You** | Habit logs, goals, journal notes, Ask questions — everything you type or tap |
| **Your photo library** | Only the one image you pick for a journal entry, via Apple's photo picker. The app cannot browse the rest of your library. Journal JPEGs stay on this device and are not assessed. |
| **Your Apple Watch** | A habit log for today's morning sunscreen and barrier care, when you tap **Confirm** on the Watch's "Applied today's care" card. It is written on your iPhone and added to anything already logged that day. |
| **Your other Apple devices** | The topic held for continuing, and topics opened there, when remembering is allowed and you continue through Handoff or have iCloud Sync on |
| **The app itself, on your device** | Streaks, consistency and summaries computed from your own habit logs; answers written by the on-device language model |

There are no other sources. We do not buy data, rent data, receive data from data brokers, or obtain anything about you from advertising networks, social platforms, affiliates, or public records.

## 3. How the data is used

- To show you your own information inside the app.
- To compute your streak and consistency on your device.
- To provide the educational content and reminders you asked for.
- To answer the questions you type in Ask, on the device.
- If you turn on iCloud Sync and Handoff, to let your other devices, Apple TV and the Home Screen widget continue, and, through Handoff, to tell your own nearby devices which tab you are on. The widget's suggested next topic follows that switch alone. The identifier of a topic you open, the list of topics you opened, and Handoff of that topic go only after you also allow remembering.
- When you tap **Read this topic** on your Apple Watch, to open the topic held for continuing there. The iPhone sends that identifier only when remembering is allowed.
- Nothing else. Not to advertise to you, not to profile you, not to train any model, not to build a data set, not for research, and not for any purpose we have not described here.

**Nothing is used to train AI.** Ask's models are already trained when they reach your device, and your questions, journal and habit logs do not update them. Ask is never given your journal, your photographs or your habit logs — only your question, the conversation on screen and passages from the app's built-in topics.

---

## Subscription tiers and consumer health data

### No new collection when you subscribe

OmniDerm has a free tier and one paid upgrade, **OmniDerm Pro** (monthly, annual or lifetime; all three grant the same Pro). **Upgrading does NOT trigger new consumer health data collection.**

Both tiers:
- Process the same categories of consumer health data (listed above)
- Use consumer health data for the same purpose (operating features you choose to use)
- Store data in the same location (on your device)
- Send it to the same recipients (none — Prameya receives nothing in either tier)

**Subscription unlocks features. It does not change what data is collected, how it is processed, or where it goes.**

### What changes between tiers

| What Pro affects | What Pro does NOT affect |
|---------------------------|-----------------------------------|
| How much history the screens show: the free journal timeline shows the last 30 days in full, with older entries listed under **Older entries** (date, body area and note, without the photograph); the free list of logged days shows what you marked for the last 90 days, with older days listed under **Older days** (the date only). Pro shows everything. | What is stored: every record is kept on the device in both tiers, and **Export my record** always contains all of it |
| Same-area compare (an earlier and a later photograph of one body area, blended or side by side) | Whether journal photos are saved (yes in both tiers, on this device only) |
| The formatted appointment pack (a text summary of your dates, body areas, notes, habit marks and goals) | What iCloud Sync carries (the same in every tier, and never your journal, photographs or habit logs) |
| | What categories of consumer health data are collected |

### StoreKit data is not consumer health data

When you buy or restore Pro, Apple's StoreKit on your device tells the app which Pro product is active and, for a subscription, when it renews. **That is payment information, not consumer health data** under RCW 19.373.010.

StoreKit information:
- Does not identify your health status, condition, disease, or treatment
- Is used only to unlock Pro
- Is not written into OmniDerm's own storage (the app asks StoreKit again at launch and after each purchase), is not sent to Prameya, and is not removed by Clear All Local Data — your purchase records are Apple's

Apple separately processes your Apple Account ID and payment method when you subscribe. That processing is governed by Apple's terms, not ours.

---

## 4. Categories of consumer health data that are shared

**None.**

We share no consumer health data, of any category, with anyone. There is no category to list because the list is empty.

## 5. Categories of third parties and specific affiliates we share with

**None.** For completeness, since some third parties are involved in the app without receiving any health data:

| Party | Role | Consumer health data they receive |
|---|---|---|
| **Apple** | Distributes the app; provides the operating systems, on-device storage, Apple Intelligence's on-device model, device backups, Handoff, the connection between your iPhone and Apple Watch, and, if you turn it on, iCloud storage inside **your own** Apple Account | **None from us.** Apple stores or carries some of your data for you, at your direction, under your Apple Account: your device backup (journal notes, body areas, habit logs and goals — not journal photographs), if you back up your device; and if you turn on iCloud Sync and Handoff, five non-health settings and the widget's suggested next topic, and, through Handoff, the tab you are on, to your own nearby devices. The identifier of a topic you open, the list of topics you opened, and Handoff of that topic go only after you also allow remembering. When you tap **Read this topic** on your Apple Watch, the identifier of the topic held for continuing goes over the connection between your iPhone and Apple Watch only when remembering is allowed. Prameya cannot read any of it. Ask's questions go to Apple Intelligence's model on your device, not to Apple's servers. |
| **Hugging Face** | Serves the optional on-device Ask model, only after you agree to that download in Settings | **None.** The download request carries your IP address, standard request headers and the names of the model files, never a question, a journal entry, a photograph or anything else you entered. |

**What iCloud Sync can carry, precisely.** Sync is off unless you switch it on (**Settings → iCloud Sync and Handoff**). Remembering the identifier of a topic you open is a second allow, **Remember topics I open**, off until you allow it. That allow stays on this device and is not one of the five iCloud settings. The app tells you inside the app and asks for your consent again before storing or syncing that identifier. When the iCloud switch is on, sync uses two stores in your own Apple Account:

- **A preference record in your private CloudKit database**, written only when you tap **Sync Now** and limited in code to five settings: appearance mode, whether reminders are on, the reminder hour, the tab the app opens on, and whether you have acknowledged the app's disclosure. Each is checked in code against a fixed set of values before it is written, so free text cannot travel with them.
- **iCloud key-value storage**, so your Apple Watch, Apple TV and Home Screen widget can continue where you left off: the tab you were on; your appearance choice; the next suggested topic (identifier, title and a fixed line of the app's own), which follows the iCloud switch alone and is not the list of topics you opened; and a topic you tapped in the widget until the app opens it. The identifier of the topic held for continuing, and the list of topics you opened in Understand, go only after you also allow remembering, and only while the switch is on. When remembering is allowed and you turn the switch on, the topic held for continuing at that moment can join that list too, even if you opened it while the switch was off. Because topics name skin conditions, rare diseases, and infections and infestations, including pubic lice, which usually spread through sexual contact, we treat these identifiers as consumer health data. The list can reveal sexual-health information, such as that you read about pubic lice. Declining remembering removes stored topic identifiers. Reading a topic does not require the allow. Nothing is sent to Prameya.

iCloud Sync never writes journal entries and notes, journal photographs, habit logs, streaks, consistency scores, goals or Ask questions to iCloud, and none of the app's local database is mirrored to iCloud. (A device backup to iCloud is separate: it includes journal entries, habit logs and goals, but not journal photographs — see section 8.) Switching sync off, or Clear All Local Data, removes the key-value entries, deletes the preference record and stops Handoff. Declining remembering, or switching **Remember topics I open** off, removes stored topic identifiers and the opened list. Reading a topic does not require that allow. If the app cannot reach iCloud at that moment, Clear All says so, and you can delete OmniDerm's iCloud data in Settings → your name → iCloud → Manage Account Storage (on a Mac, System Settings → your name → iCloud → Manage).

We have no affiliates. We use no processors, no analytics vendor, no cloud provider of ours that touches your data, no advertising network, and no AI service provider. We do not disclose consumer health data to law enforcement or anyone else, because we do not have it — a demand made to Prameya for your health data cannot be satisfied.

## 6. Selling consumer health data

**We do not sell consumer health data, and we will not.**

Washington law requires a separate, signed authorization with specific contents before any sale of consumer health data. We have never asked anyone for one and do not intend to. If that ever changed, it would require your explicit, separate, written authorization, revocable at any time — not a buried checkbox and not a policy update.

## 7. Consent, and how to withdraw it

**How consent works in OmniDerm.**

- Photo **assessment** is not available — the clearance gate is closed.
- Journal photographs are saved only when you pick one.
- OmniDerm does **not** read Apple Health.
- iCloud Sync and Handoff is **off** until you switch it on.
- Remembering topics you open is **off** until you allow it. The app tells you inside the app and asks for your consent again before an opened-topic identifier is stored or synced. Declining stops that storage and that sync. Reading a topic does not require the allow.
- The on-device Ask model downloads only after you tap **Download** on the consent sheet in Settings, which names its size and Hugging Face as the source.
- Ask runs only when you type a question.
- Reminders are a toggle, and it **starts off**. They are local notifications from your own device; permission is requested only when you switch Reminders on. Tapping a reminder opens the app and logs nothing.
- Habit logging happens only when you tap the toggles in the app, or **Confirm** on your Apple Watch's "Applied today's care" card.
- The topic held for continuing goes to your Apple Watch only when remembering is allowed and you tap **Confirm** on its "Read this topic" card. Snooze and Not now do not send it.

**How to withdraw consent — all of these are immediate and do not require contacting us:**

| To withdraw | Do this |
|---|---|
| Photographs (journal) | There is no photo library permission to withdraw: Apple's photo picker gives the app only the image you pick, each time. Journal JPEGs already saved are deleted with **Delete the photograph**, with Clear All Local Data, or by deleting the app. |
| iCloud Sync and Handoff | Switch **iCloud Sync and Handoff** off in the app's Settings. That stops every write and Handoff, removes OmniDerm's key-value entries from iCloud and deletes the preference record. |
| Remember topics I open | Decline the notice, or switch off **Remember topics I open** in Settings. That removes stored topic identifiers and the opened list. Reading a topic does not require the allow. |
| Handoff, for every app | iOS Settings → General → AirPlay & Continuity → Handoff off (on a Mac, System Settings → General → AirDrop & Handoff). |
| On-device Ask model | Switch **Use an on-device model** off in Settings → On-device Ask model (stops a download and unloads the model), and use **Remove the downloaded model** to delete its files. |
| Reminders | Switch reminders off in the app, or in the Settings app → Notifications (on a Mac, System Settings → Notifications). |
| Device backup | Exclude OmniDerm from iCloud Backup (iOS Settings → your name → iCloud → Manage Account Storage → Backups), or stop backing up the device. |
| Everything at once | Clear All Local Data, then delete the app. |

Withdrawing consent does not lock you out of the rest of the app. Nothing here is conditioned on giving up your health data.

## 8. Your rights

Washington's My Health My Data Act gives you the right to:

- **Confirm** whether we collect, share, or sell your consumer health data, and to access it;
- **Get a list** of all third parties and affiliates with whom we have shared or to whom we have sold it, with contact information for each;
- **Withdraw consent** to our collection and sharing of it;
- **Delete** it, including from any backups and archives.

Nevada's SB 370 provides substantially the same rights to Nevada residents. Residents of other states and countries may exercise these rights too — we apply them to everyone rather than checking your address.

**Our standing answers, so you know before you ask:**

- **Do we collect your consumer health data?** Not in the sense of receiving it. It is processed on your device. We never obtain a copy.
- **Do we share it?** No, with no one.
- **Do we sell it?** No, and never have.
- **List of third parties we shared with or sold to?** Empty.
- **Can you access it?** Yes — from the app itself, at any time. **Settings → Export my record** gives you a complete file of your journal entries, your habit logs, your streak snapshot and your goals. If you have saved journal photographs, the export is a `.zip` holding that file **and every photograph still on this device**, in a `Photographs` folder; with no photographs saved it is the file on its own. The export screen tells you how many photographs are included before you share it. You can also open a journal entry from the timeline to see its photograph at full size (on the free plan, for entries from the last 30 days; older entries open without the photograph, which is still in the export). On the free plan, what you marked on a logged day older than 90 days is not shown in the app; it is in the export.
- **Can you delete it?** Yes, and you do not need us — and you can delete one record without deleting the rest. **One journal entry:** open it from the timeline and use Delete entry, or hold the row and choose Delete entry; its photograph is deleted with it. **Just the photograph on an entry:** open the entry and use Delete the photograph; the date, body area and note are kept. **One logged day:** open Do → Today's log → Days you have logged, open the day, and use Delete this logged day. **Older records on the free plan:** journal entries older than 30 days are listed under **Older entries** below the timeline, and each opens to be corrected or deleted; logged days older than 90 days are listed by date under **Older days** below the list of logged days, and each opens to **Delete this logged day**. **Everything:** **Settings → Clear All Local Data** deletes your habit logs, journal entries, journal JPEGs, goals, and reminder and appearance settings, cancels pending reminders, deletes the downloaded Ask model and your answer to its download, switches iCloud Sync and Handoff off, removes OmniDerm's iCloud key-value entries (including the list of topics you opened) and deletes the CloudKit preference record; it tells you if that record could not be removed. Journal photographs are excluded from device backup and are never uploaded, so deleting one deletes the only copy that exists — the confirmation says so before you do it. Deleting the app removes what remains on the device. **Not removed by either:** any device backup you already made, which Apple keeps under your control until you delete or replace it.
- **Reaching an older record?** The journal timeline and the list of logged days each show your 365 most recent entries at a time, because that is as many as the screen will draw at once. When you have more than that, the foot of the list says how many are on screen and offers **Show older entries** (or **Show older days**), which brings in the next 365 — repeat it and you reach the first record you ever saved. An export always contains every record, whatever is currently on screen.
- **Do we hold backups or archives of your data?** No. We have no copy to restore, so there is no archive for a deletion request to miss. Your own device backups are yours: iOS includes OmniDerm's journal entries (date, body area, note), habit logs and preferences in an iCloud or computer backup if you make one, and excludes journal photographs and the downloaded model.

**How to make a request.** Email **admin@prameya.legal**. Say what you want and which state you are in. There is no form and no account to create.

**How we handle it.**

- We respond within **45 days** of receiving the request. If we need more time, we may extend once by a further 45 days, and we will tell you why before the first 45 days are up.
- We do not charge for this.
- Because there is no account, we cannot and will not demand identity documents to verify you. If a request would require us to identify you and we cannot, we will say so and explain exactly how to do the thing yourself on your device.
- **If we deny your request**, we will tell you why and give you instructions for appealing. You appeal by replying to that email. We will respond to an appeal in writing within **45 days**, with our reasoning.
- **If we deny your appeal**, we will give you a way to complain to the **Washington State Attorney General** at [https://www.atg.wa.gov/file-complaint](https://www.atg.wa.gov/file-complaint). Nevada residents may complain to the **Nevada Attorney General's Bureau of Consumer Protection**.

**Enforcement.** A violation of the My Health My Data Act is an unfair or deceptive practice under Washington's Consumer Protection Act (RCW ch. 19.86), which carries a private right of action under **RCW 19.86.090**. In other words, you are not limited to complaining to a regulator.

## 9. How we protect it

- Consumer health data stays on your device, inside the app's sandbox, and your device passcode, Face ID, Touch ID or Optic ID is the main protection for it.
- On iPhone, iPad and Apple Vision Pro, OmniDerm declares iOS's strictest default file-protection level (`NSFileProtectionComplete`), so its stored files — journal photographs, notes, body areas and habit logs — are unreadable while your device is locked. An export you prepare is written with the next level down, readable after first unlock, so the share sheet can finish, and is cleared afterwards. On a Mac, the files are protected by macOS and by FileVault if you use it.
- Journal photographs you save are stored as JPEG files on this device, with location and other metadata removed, excluded from backup, and never uploaded or synced. The assessment path does not run.
- All network traffic uses HTTPS; the app refuses unencrypted connections. The only outside download, the optional Ask model, is checked against sizes and checksums built into the app before it is loaded.
- Access inside Prameya is limited by architecture rather than by policy: **no employee, contractor or system of ours can access your consumer health data, because it never reaches us.**

**Retention.** We retain none of it, because we receive none of it. On your device, data stays until you delete it using the steps above.

**Breach notification.** If we ever learn of a security breach involving health-related information from this app, we will notify affected users and regulators as required, including under the FTC's Health Breach Notification Rule and applicable state law.

## 10. HIPAA

**HIPAA does not apply to OmniDerm.** Prameya is not a health plan, a health care provider, a clearinghouse, or a business associate of any of them. We have no relationship with your doctor or your insurer. We do not claim to be HIPAA compliant, and you should be wary of any consumer app that does.

Your rights here come from Washington's My Health My Data Act, Nevada SB 370, the California Consumer Privacy Act and similar state laws — and from the fact that the data never reaches us.

## 11. Children

OmniDerm is not directed to children and has no accounts, no ads, no social features and no way for anyone to send us anything. It offers one paid upgrade, OmniDerm Pro (monthly, annual or lifetime), which Apple processes. We do not knowingly collect consumer health data from anyone under 13. If you believe a child has sent us information, email admin@prameya.legal and we will delete it.

## 12. Changes to this policy

If we change how OmniDerm handles consumer health data, we will update this policy and change the effective date at the top **before** the change takes effect in the app, and we will tell you inside the app.

**8 October 2026 — what changed.** Remembering the identifier of a topic you open is a separate allow, off until you allow it. The app tells you inside the app and asks for your consent again before that identifier is stored or synced. Declining stops that storage and that sync. Reading a topic does not require the allow. The widget's suggested next topic can still go with iCloud Sync before the allow, and it is not the list of topics you opened. The short version, the category table, "What iCloud Sync can carry", consent, and the Apple Watch and Apple TV sentences now say this. On 7 October 2026 the Watch's **Read this topic** card sent the identifier whether or not iCloud Sync and Handoff was on; it now sends that identifier only when remembering is allowed.

**7 October 2026 — what changed.** The app's topic library grew, and parts of this policy were out of date with the app. It now says:

- **Skin-care topics you open:** the built-in library added topics on rare skin diseases (for example epidermolysis bullosa, pachyonychia congenita and pemphigus) and a group on infections and infestations. One of them is about a sexually transmitted infestation, pubic lice, which its source says usually spread through sexual contact. Like every other topic, each can become the topic held for continuing and, while iCloud Sync and Handoff is on, join the list of topics you opened. The short version and sections 1 and 5 now say what the identifiers can name, and that the list can reveal sexual-health information. The "Not collected" paragraph in section 1 now says that a topic about sexual health, such as pubic lice, is part of this category. Section 1 also says that Apple TV opens on its Continue tab and shows the topic held for continuing there. Sections 1 and 5 now also say that when you turn iCloud Sync and Handoff on, the topic held for continuing at that moment can join the list of topics you opened, even if you opened it while the switch was off; this policy said the list held only topics opened while the switch was on. These topics are handled exactly as every other topic: the category's purpose, where it is kept (your own iCloud and your own devices) and who receives it (no one) are unchanged. The app does not ask for a new consent for them. To keep them out of iCloud and Handoff, leave iCloud Sync and Handoff off, which is how it starts.
- **Your Apple Watch:** when you tap **Read this topic** on your Apple Watch, your iPhone sends the Watch the identifier of the topic held for continuing, over the connection between them, whether or not iCloud Sync and Handoff is on. That is not new in the app, and the main policy already said it. This policy mentioned the Watch only alongside the switch; the short version and sections 1, 3, 5 and 7 now say that this card does not depend on it.
- **Skin-care habit records:** the fourth habit mark is "Looked at the same area today", as the app labels it. This policy called it a self-check.
- **Understand:** the tab where you read topics is called Understand in the app, and this policy now uses that name. The Apple Watch app's tab is still called Learn. Earlier entries below keep the name they used.

Nothing is sent to Prameya.

**27 September 2026 — what changed.** One change in the app, and this policy follows it:

- **Skin-care topics you open:** every topic you open in Learn, by any route, now becomes the topic held for continuing, and while iCloud Sync and Handoff is on it is written to your own iCloud key-value storage and added to the list of topics you have opened. Before, only a topic opened from the Home Screen widget or continued from another of your devices was, and this policy said a topic opened by browsing Learn was not recorded. With the switch off, nothing is written to iCloud and nothing is offered for Handoff, as before. The category, its purpose and where it goes (your own iCloud and your own nearby devices, never us) are unchanged.
- **Mac paths:** removing OmniDerm's iCloud data and turning notifications off on a Mac are in System Settings.

Nothing is sent to Prameya.

**24 September 2026 — what changed.** One change in the app, and this policy follows it:

- **Older logged days on the free plan:** logged habit days older than 90 days are now listed by date under **Older days**, below **Days you have logged**, and each one opens to **Delete this logged day**; what you marked on those days is still shown only with Pro. The limit described on 23 September — that on the free plan a habit day older than 90 days could not be deleted on its own, only with Clear All Local Data — no longer applies, and that sentence is gone. No new category of data, purpose or recipient.

**23 September 2026 — what changed.** This policy was out of date with the app, and it now describes what OmniDerm actually does:

- **New categories named:** questions you type in **Ask** and its answers (processed by a language model on your device, not saved, not sent to us), and the **skin-care topics you open**, which go to your own iCloud, and to your own nearby devices through Handoff, only if you turn on iCloud Sync and Handoff.
- **Ask and the model download:** Ask answers with Apple Intelligence or with a model you choose to download from Hugging Face after agreeing on a consent sheet. The earlier version said Hugging Face is not contacted.
- **iCloud:** it lists exactly what iCloud Sync stores, and says that switching it off or Clear All removes it. The earlier version said only seven non-health settings sync.
- **Privacy fixes in the app, the same day:** the switch is now called **iCloud Sync and Handoff**, and Handoff follows it, so with the switch off the topic you are on is no longer offered to your other devices. Switching it off, or Clear All Local Data, now also deletes the preference record from your iCloud, so you no longer have to remove it in iOS Settings. Clear All now also removes your appearance setting and forgets the topic it was holding. The preference record now holds five settings instead of seven.
- **Backups:** it says your device backup includes journal notes, body areas, habit logs and goals, and excludes journal photographs.
- **Corrections:** section 9 now says the app does use the strictest iOS file protection (the earlier version said it did not); it no longer mentions Keychain keys (the app keeps none); the subscription section describes the real free and Pro plans (the earlier version named "Plus and Premium" tiers and export formats that do not exist); StoreKit information is not stored or deleted by the app; there is no photo library permission to withdraw; Apple Watch confirmations are named as a source of habit logs; and your goals are described as kept for you to see, edit and export (the earlier version said they personalise cards, which they do not).
- **Devices:** it covers the Mac, Apple Vision Pro, Apple Watch and Apple TV apps and the widgets, not only iOS.

Nothing is shared with or sold to anyone, as before.

**What changed on 24 August 2026.** Per-entry, per-photograph and per-day deletion was named, and the export began carrying the journal photographs themselves.

**What changed on 23 August 2026.** Journal JPEGs you save are stored on this device. This page no longer says no photo was ever saved. Photo **assessment** remains gated off. Hugging Face was not contacted in the build of that date (superseded on 23 September 2026: see above).

**What changed on 8 August 2026.** An earlier revision corrected internal review notes and named iCloud’s seven non-health settings. Sentences from that date that said the app reads no image at all are superseded above, as is the statement that iCloud carries only those settings.

Washington law does not allow us to collect, use or share consumer health data beyond what this policy discloses, and any new category, purpose, or recipient requires your fresh, affirmative consent. We will ask. We will not treat continued use of the app as agreement to a new use of your health data.

Previous versions remain available at [https://prameyallc.github.io/privacy/](https://prameyallc.github.io/privacy/).

## 13. Contact

**Prameya LLC**
**admin@prameya.legal**

For privacy requests, tell us which state or country you are in. You do not need an account, a form, or a lawyer to ask us anything.

---

*Main policy: [OmniDerm Privacy Policy](https://prameyallc.github.io/privacy/omniderm/) · All Prameya app policies: [https://prameyallc.github.io/privacy/](https://prameyallc.github.io/privacy/)*
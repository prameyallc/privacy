# OmniPhysics Privacy Policy

**Effective date:** 24 September 2026
**Publisher:** Prameya LLC ("Prameya", "we", "us")
**App:** OmniPhysics for iPhone, iPad, Mac and Apple Vision Pro, with its Apple Watch and Apple TV apps — bundle ID `legal.prameya.OmniPhysics` (iPhone, iPad, Mac, Apple Vision Pro and Apple TV) and `legal.prameya.OmniPhysics.watch` (Apple Watch)
**Contact:** admin@prameya.legal
**Scope:** This policy covers the OmniPhysics app on every device listed above, including its Home Screen widget and Apple Watch complication, and nothing else. Prameya's other apps have their own policies, because they work differently. Index: <https://prameyallc.github.io/privacy/>

---

## The short version

- **No ads. No App Tracking Transparency. No third-party analytics.**
- **There is no account of ours.** No sign-in, no email address. The only thing you can type about yourself is an optional display name.
- **Your progress is saved on your device and, if you use iCloud, in your own iCloud.** If you are signed in to iCloud and iCloud is on for OmniPhysics, your profile and progress sync through your own private iCloud database (Apple's CloudKit), and a small iCloud key-value store remembers where you left off. We run no server that receives any of it, and we cannot read it.
- **OmniPhysics does not talk to a server of ours.** There is no such server. The only paths off the device are Apple's: iCloud, the App Store for purchases, Handoff, and the connection between your iPhone and your Apple Watch.
- **Ask answers on your device, with Apple Intelligence only.** Where Apple Intelligence is turned on and ready, Ask sends your question to Apple's on-device model. This version offers no other model: nothing is downloaded, and the app makes no request to Hugging Face.
- **One optional permission.** OmniPhysics asks to send notifications only if you turn on **Remind me to continue** in More, on iPhone or iPad. It asks for no other permission: no camera, photos, microphone, location, contacts, health or files.
- We do **not** sell personal data.
- **HIPAA and FERPA do not apply.** This is not a school or health record.
- **There is one thing to buy.** OmniPhysics Pro, described below. The reasoning material and one sandbox are free; buying Pro sends nothing about you to us.

---

## What OmniPhysics is

OmniPhysics is an educational physics app (classical mechanics and waves) for learners **13 and older**. It is not in the App Store Kids Category and is not directed at children under 13.

On iPhone, iPad, Mac and Apple Vision Pro it has lessons, interactive labs, the reference packs and Ask. The Apple Watch app shows reminders to continue, lets you read the packs, and can send a question to Ask on your iPhone. The Apple TV app lets you read the packs and pick up where you left off. All of the learning content ships inside the app.

---

## What the app processes

| Data | Where | Purpose |
|---|---|---|
| Display name you choose (optional; "Explorer" if you leave it blank) | Device, and your private iCloud database if sync is on | Personalize Profile |
| Lesson records (each lesson's attempts, stars, best stars, whether it is unlocked or completed, when you last completed it), XP, streaks, hearts, daily mission, the last unit and lesson you opened, whether you finished onboarding, the last day you were active and when your profile was created | Device, and your private iCloud database if sync is on | Save learning |
| Achievements and the date each one unlocked | Device, and your private iCloud database if sync is on | Save learning |
| Settings stored with your profile (sound, haptics) | Device, and your private iCloud database if sync is on | Remember preferences |
| Where you left off: the tab you were on, the pack, lesson and lab you were at, that lesson's or pack's title, and when this was written | Device, and your iCloud key-value store if you are signed in to iCloud | Continue on your other devices, Apple Watch, Apple TV and Handoff |
| The next topic suggested on the Home Screen widget (its pack, title and one line about it), and a topic you asked the widget to open until the app opens it | Your iCloud key-value store | Show and open the widget's topic |
| Appearance (System, Light or Dark) | Device; and, while you choose Light or Dark, your iCloud key-value store if you are signed in to iCloud (System is the default and is stored there as no entry) | Apply it, and let Apple TV match it |
| The **On-device answers** switch and the **Remind me to continue** switch | Device only | Remember your choice |
| When you last used **Delete everything**, and the random keys (identifiers that hold nothing about you) of the lesson records it has deleted | Device only | So that a deleted record another of your devices sends back through iCloud is deleted again instead of merged into your new profile (see "iCloud sync") |
| A one-time marker that files of an older Ask model were removed, and how much space that freed | Device only | So the removal happens once (see "Ask" below) |
| A temporary copy of a file you export | The app's temporary folder on the device, until the app deletes it (see "Data retention") | Hand the file to the share sheet |

That is the complete list of what OmniPhysics itself stores. We cannot see any of it.

We do not collect precise location, contacts, advertising identifiers, or off-device analytics. We do not collect photos, camera or microphone input; the app plays bundled UI sounds and records nothing.

There is no account of ours. The app links Apple's MLX packages (mlx-swift and mlx-swift-lm) and Hugging Face's swift-transformers and swift-huggingface, which ship inside the app download. None of them is an analytics, advertising or crash-reporting SDK, and none of them sends us anything. They are the code for an optional on-device model that **this version does not offer** — see "Ask" below.

If you use iCloud or computer backup for your device, the data on the device is included in that backup, under Apple's terms and your control.

---

## Subscriptions and In-App Purchases

### Available tiers

There is one paid upgrade, **OmniPhysics Pro**, sold as three products. Buying any one of
them grants exactly the same Pro — there are no separate feature tiers.

| Product | Price (US) | Billing |
|---|---|---|
| OmniPhysics Pro Monthly | $4.99 | Auto-renews monthly. 7-day free trial where the App Store offers you one. |
| OmniPhysics Pro Annual | $29.99 | Auto-renews yearly. 7-day free trial where the App Store offers you one. |
| OmniPhysics Pro Lifetime | $79.99 | One-time purchase. Not a subscription. |

Family Sharing is enabled on all three. Subscriptions renew until you cancel in
Settings; Lifetime is a one-time non-consumable. The paywall mentions a free trial only when the App Store says you are eligible for it. Pro is sold on iPhone, iPad, Mac and Apple Vision Pro; the Apple Watch and Apple TV apps have no purchase screen.

**The knowledge layer is free and stays free.** Without paying anything you get
the reasoning material, every reference pack, Ask, iCloud sync and the F = ma lab, with no account and no time limit. Pro adds every other lab, wider force and mass ranges in the labs, and formatted lab-notes export.

**Pro does not change sync, and there is no paid iCloud option.** iCloud sync works the same, free or paid. If a subscription lapses you keep your
own data and can still export it in its raw form (JSON); only the Pro tools stop.


### Free vs paid tier data collection

**Free and Pro store the same data** — the list above — and none of it reaches us.

The difference is:
- **Which tools you get.** The reasoning material and the F = ma lab are free; Pro adds every other lab, wider ranges and formatted lab-notes export.
- **Nothing else.** Sync, Ask and everything the app stores are the same in both.

In all tiers:
- Your progress stays on your device and, if sync is on, in your own iCloud. Quiz answers themselves are not stored; only each lesson's attempts and stars are
- No transmission of learning data to Prameya
- No analytics or tracking

**Purchase unlocks content. It does not change what data is collected.**

### Cancellation and refunds

Subscriptions are managed by Apple:
- **Cancel:** iOS Settings → your name → Subscriptions → OmniPhysics, or **Manage Subscription** in the app
- **Refund requests:** reportaproblem.apple.com
- **Lifetime purchase:** One-time payment, no subscription to cancel

Prameya cannot cancel your subscription or issue refunds. Apple controls all billing.

### StoreKit transaction data

When you buy or restore Pro, Apple's StoreKit framework on your device talks to the App Store. Apple processes the payment and keeps its own record of the transaction under Apple's terms.

Each time the app runs, StoreKit tells it which Pro products you are entitled to and when a subscription expires. The app uses that answer, in memory, to unlock Pro, and does not save it: the next launch asks StoreKit again.

This data:
- Stays on your device, with Apple
- Is not sent to Prameya — the app sends nothing about a purchase to us, and we never see payment details
- Is not synced by the app to iCloud
- Is used only to unlock Pro

The app's privacy manifest declares this as purchase history, used for app functionality, not linked to you and not used for tracking.

---

## iCloud sync

If you are signed in to iCloud and iCloud is on for OmniPhysics, on iPhone, iPad, Mac and Apple Vision Pro:

- Your profile (display name, sound, haptics, XP, streaks, hearts and the rest of the profile row), every lesson record and every achievement sync through the app's container (`iCloud.legal.prameya.OmniPhysics`) in **your own CloudKit private database**, so your other devices signed in to the same Apple Account show the same progress.
- Sync is handled by **Apple's infrastructure**; we do not operate a separate user account server, and Prameya cannot open another person's private database.
- If two of your devices recorded progress before they synced, OmniPhysics merges them on each device into one profile: it keeps the higher XP, the longest streak, the best stars and any lesson or onboarding you finished on either device. XP earned on both devices is not added together; the larger total is kept.
- You can keep using the app offline; changes sync when the device is back online.
- **Delete everything** (see "Your choices") deletes your profile, lesson records and achievements from your private database too, and your other devices delete their copies when the change reaches them. A device that was offline can send a deleted record back when it reconnects. The device where you used Delete everything remembers what it deleted (see the table above) and deletes such a copy again instead of merging it into your new profile. A lesson record that the offline device created and had never synced is not recognised and can reappear; you can delete it in **More ▸ Your records**.

If you are not signed in to iCloud, iCloud is off for OmniPhysics, or CloudKit cannot be set up on the device, the app runs in **local-only** mode on the same data, and **More** says "Saved on this device". The Apple Watch and Apple TV apps never use CloudKit.

**The iCloud key-value store.** Separately from CloudKit, whenever you are signed in to iCloud the app keeps up to four small entries in its iCloud key-value store: where you left off, your appearance choice (only while it is Light or Dark), the Home Screen widget's next topic, and a topic you asked the widget to open. That is how your other devices, Apple Watch and Apple TV offer to continue, and how Apple TV matches your appearance. When where you left off is cleared (see "Your choices"), its entry is left empty rather than removed, so that your other devices, Apple Watch and Apple TV forget their own copies too; the empty entry holds nothing about you. **Delete everything** removes the other entries and leaves only that empty one.

---

## Ask

Ask appears only when **On-device answers** is on in More and Apple Intelligence is turned on and ready on the device. It sends your question, with up to eight short excerpts from the pack you have open, to **Apple's on-device model** (Apple Intelligence) and shows what it writes, labelled **Apple Intelligence**. Your question stays on the device; it is not sent to us or to Apple. Before any model sees a question, Ask declines ones about doses, diagnoses, whether a law is still good law, go/no-go calls and net worth.

Your questions and the answers are not saved. They stay on screen while Ask is open and are gone when it closes.

Where Apple Intelligence is not ready, Ask says it cannot answer on this device.

**The optional on-device model is not offered in this version.** OmniPhysics contains the code for an optional model downloaded from Hugging Face, but no device is offered it: no download switch or button appears, and the app makes no request to Hugging Face. If a later version offers it, this policy will describe it before that version ships. If an earlier version of OmniPhysics downloaded the model it used then (Qwen3 0.6B, about 350 MB, from `mlx-community/Qwen3-0.6B-4bit`), this version deletes those files on its first launch and records that it did and how much space it freed.

On **Apple Watch**, **Ask the phone** sends the question you type to OmniPhysics on your paired iPhone over Apple's connection between the two devices. The iPhone answers the same way — with Apple Intelligence where it is ready and **On-device answers** is on, or by saying it cannot answer — and sends the answer back to the Watch.

On **Apple TV** there is no model and no download, and the Ask tab does not appear.

---

## Notifications

On iPhone and iPad, OmniPhysics can post a local reminder to continue where you left off, four hours after you leave the app. It names the lesson or pack (for example "Continue Path — Continue F = ma"). The **Remind me to continue** switch in More is **off** until you turn it on, including for anyone who had it on in an earlier version. Turning it on is the only thing in OmniPhysics that asks iOS for permission to send notifications.

The reminder is scheduled on your device. There is no push server, and nothing about it leaves your device. A plain tap on the reminder only opens the app where it points; its **Snooze** button posts it again later, and **Not now** closes it. On Apple Watch, **Snooze** asks your iPhone to post the reminder again later, and only while the switch is on. Turning the switch off cancels any queued reminder. Mac, Apple Vision Pro, Apple Watch and Apple TV never ask for notification permission.

---

## Apple Watch, Apple TV, the widget and Handoff

- **Apple Watch.** Your iPhone sends the Watch the current reminders and where you left off, over Apple's connection between the two devices. **Confirm**, **Snooze** and **Not now** on the Watch send that choice back to the iPhone, which only opens the app or reposts the reminder; they do not change your records. The Watch also reads where you left off from the iCloud key-value store, and opening a pack on the Watch updates where you left off. The complication shows the lesson or pack you left off at.
- **Apple TV.** The TV app reads where you left off and your appearance from the iCloud key-value store, and opening a pack on the TV updates where you left off. It stores no progress of its own and has no purchase screen, no notifications and no Ask.
- **Home Screen widget (iPhone and iPad).** The widget shows the next topic you have not worked yet, read from the iCloud key-value store. Starting it from the widget stores that topic there until the app opens it.
- **Handoff.** On iPhone, iPad, Mac and Apple Vision Pro, the app tells your nearby devices that use the same Apple Account where you left off (the same entry described above).

None of this reaches Prameya.

---

## What OmniPhysics does not do

- No ads of any kind.
- No advertising identifier (IDFA), no App Tracking Transparency prompt.
- No third-party analytics or crash reporter. On iPhone, iPad, Mac and Apple Vision Pro the app writes Apple's daily performance summaries (launch time, hangs, disk writes and crash counts, from MetricKit) to the device's own system log; it does not send them anywhere. If you choose in your device settings to share analytics with app developers, Apple may give us crash reports and usage statistics under Apple's terms; those come from Apple, not from code in OmniPhysics.
- No network requests to us. There is no server of ours for the app to talk to. Links you tap in the app (sources, acknowledgements, support, this policy and the terms, managing a subscription) open in your browser or the App Store, and **Email support** opens your mail app.
- No camera, photos, microphone, contacts, or location APIs.
- No health, fitness or medical data of any kind.
- No download of any language model in this version, and no request to Hugging Face.
- A paywall for OmniPhysics Pro, processed entirely by Apple's StoreKit. The app sends nothing about a purchase to us, and we never see payment details.

---

## Children

Not Kids Category. Not directed at children under 13. We do not use progress data for advertising. A child's progress is stored like an adult's: on the device and, if that Apple Account uses iCloud with OmniPhysics, in that account's private database. The app has no school, classroom or ClassKit integration.

---

## Your choices

- Change your display name, and toggle sound and haptics, in **More**. (Haptics appears only on devices that have them.)
- Turn **On-device answers** on or off in **More**. Off hides Ask.
- On iPhone and iPad, turn **Remind me to continue** on or off in **More**. You can also turn off notifications for OmniPhysics in iOS **Settings**.
- See every record the app keeps in **More ▸ Your records**, and delete any single lesson record or achievement there. Deleting a record also deletes it from your other devices if sync is on. If where you left off points at the lesson whose record you delete, that is cleared too — on the device, in the iCloud key-value store, on your Apple Watch and in Handoff — along with any queued reminder; if it points at another lesson, it stays as it is.
- **Export my records** in **More** gives you a JSON file of your profile, every lesson record and every achievement, to save or share wherever you choose. With Pro you can also export formatted lab notes.
- **Reset progress** in **More**, confirmed with **Delete all my progress**, deletes every lesson record and achievement, sets XP, streaks, hearts and the daily mission back to the start — on this device and, if sync is on, on your other devices — and clears where you left off and the widget's topic from the device and the iCloud key-value store, any queued reminder, and the app's temporary copy of any file you exported. Your Apple Watch, Apple TV and other devices then forget where you left off too, as soon as the change reaches them through iCloud or your iPhone, and Handoff stops offering it. A reminder already queued on another iPhone or iPad is removed the next time OmniPhysics runs there. Your display name, sound, haptics and appearance are settings and stay as they are; **Delete everything** removes them.
- **Delete everything** in **More**, directly under Reset progress and at the foot of **More ▸ Your records**, confirmed with **Delete everything**, deletes your profile (display name, sound, haptics, XP, streaks, hearts, daily mission and the rest of the profile record), every lesson record and every achievement — on this device and, if sync is on, in your iCloud private database and on your other devices. Like Reset progress, it clears where you left off and the widget's topic from the device and the iCloud key-value store (your Apple Watch, Apple TV, other devices and Handoff then forget where you left off), and removes any queued reminder and the app's temporary copy of any file you exported. It also removes your appearance entry from the iCloud key-value store and sets **Appearance** back to System on this device; Apple TV follows the next time it opens. OmniPhysics then starts again at the first lab with a new, empty profile. **On-device answers**, **Remind me to continue** and your purchases stay (the App Store restores Pro). If sync is off on this device, a copy already in your iCloud stays until you remove the app's iCloud data in Settings.
- Turn iCloud on or off for OmniPhysics, or remove its iCloud data, in **Settings → [Your Name] → iCloud**. Deleting the app does not remove the copy in iCloud.

---

## Data retention

- **On your device:** kept until you delete it in the app (a single record, Reset progress or Delete everything) or delete the app. Reset progress keeps your display name and settings; Delete everything removes them. The app deletes its temporary copy of a file you exported the next time it starts, when you reset progress or delete everything, and when you come back to **More** after your records changed; a copy you saved or shared elsewhere is yours and is not touched. The note of when you last used Delete everything, with the random keys of the lesson records it has deleted, stays on the device until you delete the app; using Delete everything again updates it.
- **In your iCloud, if you use it:** your profile, lesson records and achievements in your private database, and the key-value entries, until you delete them in the app (which updates the iCloud copy), they are replaced, or you remove the app's iCloud data in Settings. Reset progress keeps the profile record with your display name and settings, and your appearance entry, and leaves the where-you-left-off entry empty until you next use the app. Delete everything deletes the profile record, every lesson record and achievement, and every key-value entry except the empty where-you-left-off entry. Deleting the app on one device does not empty iCloud.
- **With us:** only emails you send us, kept as long as needed to handle your message and to record that we handled it. Ask and we will delete yours.
- **With Apple, if you buy Pro:** Apple keeps its own record of the transaction, under Apple's terms and retention rules.
- **With anyone else:** nothing.

---

## Changes to this policy

We will update this policy when the app changes. When we do, we will change the effective date at the top and describe what changed.

**24 September 2026 — what changed.**

- It describes **Delete everything**, new in **More** under Reset progress and at the foot of **More ▸ Your records**. It deletes your profile with your display name, sound and haptics, every lesson record and every achievement, on the device and, if sync is on, in iCloud, and clears every entry the app keeps in the iCloud key-value store (where you left off is left as an empty entry). Before, Reset progress kept the profile and its settings, and the only ways to remove them were deleting the app (for the copy on the device) or removing the app's iCloud data in Settings.
- It says OmniPhysics keeps on the device when you last used Delete everything and the random keys of the lesson records it deleted, so that a copy another device sends back is deleted again, and says which records it cannot recognise.
- It says your appearance is kept in the iCloud key-value store only while you choose Light or Dark. Choosing System now removes the entry instead of storing "system", an entry an earlier version stored as "system" is removed when the app next opens, and Apple TV reads a missing entry as System.
- The **Remind me to continue** switch now starts off for everyone, including anyone who had it on before this update; turn it on again in **More** if you want the reminder. Before, it started on for someone who had allowed notifications for an earlier version of OmniPhysics.

**23 September 2026 — what changed.** This policy was rewritten to describe what OmniPhysics does today:

- It covers the Apple Watch and Apple TV apps, the Home Screen widget, the Watch complication and Handoff, and gives their bundle IDs: the Apple Watch app has its own, and the Apple TV app uses the same one as the iPhone app.
- It says your profile, lesson records and achievements sync through your own iCloud private database when you are signed in to iCloud, and how two devices' progress is merged. Earlier versions said both that progress may sync and that OmniPhysics has no cloud sync.
- It lists what the app keeps in the iCloud key-value store — where you left off, your appearance, and the widget's topic — and says Reset progress clears all of it except your appearance.
- It says Ask uses Apple Intelligence on the device, and that this version offers no downloadable model and makes no request to Hugging Face. Earlier versions said Ask downloads a model from Hugging Face.
- It describes the **Remind me to continue** switch, which is off on a new install and is the only thing that asks for notification permission.
- It no longer says the app stores your transaction ID, product ID and purchase dates, or that we receive a transaction identifier or entitlement status: the app keeps StoreKit's answer in memory only and sends nothing about a purchase to us.
- It no longer mentions a "Delete All Data" control, which OmniPhysics does not have; it names the controls the app has — deleting a single record, **Export my records** and **Reset progress** — and says what each one reaches.
- It says the app writes Apple's MetricKit performance summaries to the device's own log and sends them nowhere.
- It says deleting a lesson record also clears where you left off when it pointed at that lesson. OmniPhysics was changed to do this the same day; before, Continue on your Apple Watch and Apple TV, Handoff and the reminder could still name the lesson.
- It says Reset progress also makes your Apple Watch, Apple TV and other devices forget where you left off, and stops Handoff offering it. OmniPhysics was changed to do this the same day; before, they could keep offering the old lesson from their own copy and write it back to iCloud.
- It says the app deletes its temporary copy of an exported file the next time it starts, when you reset progress, and when you come back to **More** after your records changed. OmniPhysics was changed to do this the same day; before, the copy stayed until the system cleared the temporary folder.

Nothing the app sends to Prameya changed: it sends nothing. Earlier versions of this policy remain in the public repository that publishes these pages: <https://github.com/prameyallc/privacy>.

---

## Contact

Prameya LLC · [admin@prameya.legal](mailto:admin@prameya.legal)
Privacy policies for all Prameya apps: <https://prameyallc.github.io/privacy/>
This policy: <https://prameyallc.github.io/privacy/omniphysics/>

# OmniRx — data-flow audit

AUDIT OF /Users/sbkoth/work/Omni/OmniRx AT COMMIT 3bcd612 (working tree clean except Package.resolved).

WHAT THE APP ACTUALLY DOES WITH DATA

1. Local storage only. `App/OmniRxApp.swift` builds two SwiftData stores in Application Support: `rx-default.store` (UserProfileRx, MedLog, WellnessEntry, HabitLogRx) and `rx-sync.store` (UserProfileRx, HabitLogRx). BOTH are created with `cloudKitDatabase: .none` (lines 61 and 97). Despite the iCloud/CloudKit/CloudDocuments entitlements in `OmniRx.entitlements`, no CloudKit mirroring is configured anywhere in the shipping code. `grep -rn "CKContainer|import CloudKit"` returns nothing. So today no user data leaves the device via iCloud sync.

2. Health-relevant data the user types. `Data/Models/RxDataModels.swift`: MedLog (taken/missed, medIdentifier, barriers such as cost/forgot/side-effect concern, free-text notes), WellnessEntry (mood 1-5, energy 1-5, sleepHours, symptoms, sideEffects, notes), HabitLogRx (tookMedsOnTime, exercised, ateWell, hydrated), UserProfileRx (age, conditions[], currentMeds[], goals[]). Derived values in `Domain/Services/RxAppDataService.swift`: adherencePercent, streakDays, wellnessAvg, WellnessTrend, RxImpactScore.estimatedComplicationAvoidanceHint. This is consumer health data under MHMDA regardless of where it sits.

3. `conditions` and `currentMeds` have NO UI editor today. Grep shows they are declared in the model and included in the schema but written nowhere except the model initializer; only `goals` is seeded (`RxAppDataService.seedDefaultProfileIfNeeded`). The capacity exists; the surface does not.

4. NO HealthKit code. `OmniRx.entitlements` requests `com.apple.developer.healthkit`, `com.apple.developer.healthkit.access = [health-records]` (Clinical Health Records) and `.healthkit.background-delivery`. There is no `HKHealthStore`, no `import HealthKit`, no HealthKit usage string in `Info.plist`, and no `UIBackgroundModes`. The entitlement asserts a capability the app does not have and does not use. ISSUES.md RX-005/RX-006 mark this a blocker to remove.

5. NETWORK ACCESS IS REAL. `com.apple.security.network.client` is granted. `Domain/MLX/Download/{RobustDownloader,HubDownloaderBridge,ResilientResolve}.swift` use `HubClient` from huggingface/swift-huggingface (Package.swift pins swift-huggingface 0.9.0 and swift-transformers 1.3.3) to `downloadSnapshot` / `listFiles` model weights. Comments reference Xet/CAS hosts (`cas-bridge.xethub`) for large safetensors. So the app connects to huggingface.co and its CDN when a model is downloaded. Inference then runs locally through MLX (`Domain/MLX/Inference/MLXLLMClient.swift`, `MLXModelManager.generate`). No other outbound endpoint exists in the tree — no URLSession outside the MLX download layer.

6. Download consent is broken. `Domain/AI/OmniRxCatalog.swift:36-41` sets `requiresConsentAboveMB: 100` and then `hasDownloadConsent: { true }` unconditionally. `Domain/MLX/Policy` gates on that closure, so a 420 MB or 1200 MB download proceeds with no user decision and no Wi-Fi check, while `Features/Settings/RxSettingsView.swift:27-31` tells the user consent and Wi-Fi are required. RX-009 blocker.

7. Two models catalogued: Qwen3-0.6B-4bit (420 MB, text) and Qwen2-VL-2B-Instruct-4bit (1200 MB, vision) advertised for "pill/label photo literacy". The vision entry is marked for removal (RX-018). Independently, there is NO camera or photo code in the shipping tree: `grep -rn "AVCapture|PHPicker|PhotosUI|UIImagePicker|import Photos"` returns nothing. The only image plumbing is `Domain/MLX/AnalysisImage.swift`, which is a decode/cache value type with no capture or picker attached.

8. No inference surface is wired yet. `MLXLLMClient` is never called from any view in `Features/`. Models can be downloaded and loaded from Settings; nothing feeds user text to them today.

9. No accounts, no ads, no analytics, no crash SDK, no purchases. Full resolved dependency set is MLX, mlx-swift-lm, swift-huggingface, swift-transformers and their Apple/transitive deps (EventSource, swift-nio, swift-crypto, swift-asn1, yyjson, swift-jinja, etc.). No AdMob/GoogleMobileAds, no Firebase, no Sentry, no AuthenticationServices/Sign in with Apple, no StoreKit.

10. No location, no contacts, no microphone. `grep -rn "CoreLocation|CLLocation|IDFA|advertisingIdentifier|identifierForVendor|CNContact|AVAudio"` returns nothing.

11. No reminders or notifications are implemented. `UNUserNotificationCenter` / `EKEventStore` appear nowhere. "Reminders" exist only as UI copy and a `// Future:` comment at `Features/Coach/RxAdherenceFeature.swift:111`.

12. "Export My Logs" is a stub. `Features/Settings/RxSettingsView.swift:51-53` has an empty button body (RX-040). No export, no share sheet, no file write.

13. Keychain use is local and device-bound. `Domain/Core/Security/SecureStore.swift` writes with `kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly`. Keychain access group `$(AppIdentifierPrefix)legal.prameya.OmniRx`.

14. Diagnostic logging via os.Logger (`OmniLogger`) records model IDs and persistence events with `privacy: .public`. No user content is logged. These stay in the device log store.

15. `PrivacyInfo.xcprivacy` is a 73-byte plain-text placeholder, not a plist: "enhanced full with HK collected+accessed + long EDU/BLS/cross-cuts (root)". It fails `plutil -lint` and it asserts HealthKit collection that does not happen. RX-001 blocker.

16. Info.plist purpose strings: the Xcode project (`project.pbxproj:423-426`, `477-480`) still carries OmniDent's dental camera/photo/health strings verbatim. RX-003/RX-004 blockers.

WHERE CODE CONTRADICTS DOCS
- REGULATORY.md says "No accounts, no server, no analytics SDK" — confirmed by code.
- REGULATORY.md says "All inference on-device via MLX" — true, but the model WEIGHTS come over the network from Hugging Face. ISSUES RX-047 states this correctly; app UI copy at `Features/Learn/SelfCareExplainerFeature.swift:20` ("no internet, your data stays here") contradicts the code and is false.
- Entitlements (HealthKit, Clinical Health Records, iCloud/CloudKit) describe an app that does not exist in the source. The code is the truth: no HealthKit, no CloudKit sync.

POST-WAVE-2 STATE ASSUMED IN THE POLICY: HealthKit and iCloud/CloudKit entitlements removed (RX-005/006/007), vision model removed (RX-018), download consent wired to a real decision (RX-009), valid privacy manifest (RX-001), OmniDent purpose strings deleted (RX-003/004). None of these had landed in the working tree at the time of this audit, so each is flagged inline with TO VERIFY BEFORE PUBLISHING.

## Corrections to prior claims

- OLD SHARED POLICY (prameyallc.github.io/edu-app-privacy, eff. 2026-07-09): states the apps do not collect 'Health, biometric, financial, or government ID data.' FALSE of OmniRx. OmniRx's core purpose is logging medication adherence, barriers, symptoms, side effects, mood, energy and sleep. That is consumer health data under Washington MHMDA and Nevada SB 370 whether or not it is transmitted. ACCURATE: OmniRx processes consumer health data on the user's device; Prameya never receives it; a separate Consumer Health Data Privacy Policy is required and now exists.
- OLD SHARED POLICY: scopes itself to 'educational apps published by Prameya LLC that do not require accounts, do not accept personal uploads', with a caveat that apps with regulated data need separate policies. OmniRx satisfies the no-accounts and no-uploads limbs but breaks the regulated-data limb. ACCURATE: OmniRx is out of scope of the shared policy and must be governed by this app-specific policy plus the separate health-data policy.
- OLD SHARED POLICY: 'Free apps may use third-party ad networks such as Google AdMob' and ad networks 'may process device and advertising data.' FALSE of OmniRx. The full resolved dependency set is MLX, mlx-swift-lm, swift-huggingface, swift-transformers and Apple/transitive libraries. There is no GoogleMobileAds, no AdMob, no analytics SDK, no crash-reporting SDK, and no use of the advertising identifier. ACCURATE: OmniRx contains no advertising, analytics or tracking SDK of any kind.
- OLD SHARED POLICY: 'we do not knowingly collect personal information from children under 13 on our servers.' Misleading as applied to OmniRx because it implies servers exist. ACCURATE: Prameya operates no server for OmniRx at all; there is no endpoint that receives personal information from any user of any age.
- IN-APP COPY, Features/Learn/SelfCareExplainerFeature.swift:20: 'Powered by on-device education (no internet, your data stays here).' FALSE. The app holds com.apple.security.network.client and Domain/MLX/Download/{RobustDownloader,HubDownloaderBridge,ResilientResolve}.swift download model weights from Hugging Face over the network. ACCURATE: model files are downloaded from Hugging Face; inference then runs on-device and user content is not transmitted.
- IN-APP COPY, Features/Settings/RxSettingsView.swift:27-31: 'Downloads require Wi-Fi + explicit consent in the MLX panel below.' FALSE as shipped. Domain/AI/OmniRxCatalog.swift:36-41 sets requiresConsentAboveMB: 100 and then hasDownloadConsent: { true } unconditionally, and no NWPathMonitor Wi-Fi check gates the download. ACCURATE (post-fix): downloads above the size threshold require an explicit user decision; until RX-009 is fixed, the honest statement is that the app downloads model files when you enable on-device AI.
- IN-APP COPY, Features/Settings/RxSettingsView.swift:49-53: 'All data local-first. Export logs from Coach to share with your pharmacist/physician' with an 'Export My Logs' button. The button body is empty (RX-040) and the Coach view has no export. ACCURATE: there is no export function today; if one ships it is user-initiated through the iOS share sheet and Prameya receives no copy.
- ENTITLEMENTS, OmniRx.entitlements: declares com.apple.developer.healthkit, com.apple.developer.healthkit.access = ['health-records'] (Clinical Health Records) and com.apple.developer.healthkit.background-delivery. There is no HKHealthStore, no 'import HealthKit', no HealthKit usage string in Info.plist, and no UIBackgroundModes. The entitlements assert access to the most sensitive health data class in the App Store that the app does not have. ACCURATE: OmniRx does not read from or write to Apple Health, does not access clinical health records, and these entitlements must be removed (RX-005/RX-006).
- ENTITLEMENTS, OmniRx.entitlements: declares iCloud container iCloud.com.omni.OmniRx with CloudKit and CloudDocuments. No CloudKit code exists; App/OmniRxApp.swift:61 and :97 both build stores with cloudKitDatabase: .none, and the second 'sync' store is a purely local file. ACCURATE: no data syncs to iCloud today. The entitlements must be removed (RX-007), and no health-derived field may ever sync — Apple Guideline 5.1.3(ii) flatly prohibits storing personal health information in iCloud, and UserProfileRx.conditions / .currentMeds are exactly that.
- CODE COMMENT, App/OmniRxApp.swift:88: 'Lightweight roaming subset (profile, habits). Heavy logs local-only for privacy/size.' Describes an intent to roam UserProfileRx (which holds conditions and currentMeds) across devices. FALSE as a description of behavior and impermissible as a plan. ACCURATE: nothing roams today; if roaming is ever added it must carry preferences and UI state only.
- PRIVACY MANIFEST, PrivacyInfo.xcprivacy: a 73-byte plain-text file reading 'enhanced full with HK collected+accessed + long EDU/BLS/cross-cuts (root)'. It is not a plist (plutil -lint fails) and it asserts HealthKit data is collected and accessed, which does not happen. Two nested placeholders exist at OmniRx/OmniRx/PrivacyInfo.xcprivacy and OmniRx/OmniRx/Info.plist. ACCURATE: a valid manifest must be authored declaring only the required-reason APIs actually used, and it must not declare HealthKit collection.
- PURPOSE STRINGS, OmniRx.xcodeproj/project.pbxproj:423-426 and 477-480: NSCameraUsageDescription and NSPhotoLibraryAddUsageDescription are OmniDent's dental copy verbatim ('capture dental photos', 'brushing coaching'), and the HealthKit strings describe 'oral hygiene habits (brushing, flossing, sugar intake)' and 'consult a dentist'. Every one is false of a medication app, and purpose strings are shown to the user verbatim at the permission prompt. Additionally NSHealthShareUsageDescription (read) carries write text and NSHealthUpdateUsageDescription (write) carries read text. ACCURATE: OmniRx has no camera, photo-library or HealthKit code; all four strings must be deleted (RX-003/RX-004).
- REGULATORY.md product posture line: 'All inference on-device via MLX. No accounts, no server, no analytics SDK.' Correct as far as it goes, but read alone it invites the 'no networking' claim that Wave 1 found false across the portfolio. ACCURATE and complete: inference is on-device; model weights are fetched from Hugging Face over the network on first use.
- IN-APP COPY, Features/Home/RxHomeView.swift:84: 'Your data stays on-device.' True of user-entered content, and kept in the policy — but it must not be extended into a claim that the app makes no network connections, which the model downloader contradicts.
- IN-APP DISPLAY, Domain/Services/RxAppDataService.swift:11 and :70: adherenceScore is seeded to 0.75 and falls back to 0.65 with no logs present, then rendered as a measured adherence percentage. Not a privacy claim, but it is a false statement of fact shown to the user and is listed here because it travels with the same App Review and FTC section 5 exposure (RX-030).

## Open questions

- Wave-2 entitlement removals had NOT landed at the time of this audit (working tree at 3bcd612). OmniRx.entitlements still declares com.apple.developer.healthkit, healthkit.access=[health-records], healthkit.background-delivery, the iCloud container iCloud.com.omni.OmniRx, CloudKit and CloudDocuments. Both policies are written for the post-removal build. Confirm removal before publishing, or the policy is false on the day it goes live.
- Does the shipping build have a UI for UserProfileRx.conditions and .currentMeds? Today the fields exist in the schema with no editor. The health policy hedges this; it should be made definite before publishing.
- Is the vision model (Qwen2-VL-2B-4bit, 1200 MB, catalogued for 'pill/label photo literacy') removed per RX-018? If it ships, the 'no camera, no photos' statements need re-examination and the FDA/Apple 1.4.1 posture changes.
- Is hasDownloadConsent wired to a real, persisted user decision plus a Wi-Fi check (RX-009)? The policy says the download happens 'only when you choose'. That is currently false.
- Will medication reminders ship? No UNUserNotificationCenter or EKEventStore code exists today, but several screens promise reminders. If reminders ship, add a local-notifications section.
- Will 'Export My Logs' ship, and what exactly will it export and to where? The button is currently an empty stub (RX-040).
- Should the SwiftData store be marked excluded from iCloud device backup? Today it is not, so whole-device iCloud Backup can include medication and journal data. Either exclude it or keep the disclosure in both policies.
- In which App Store territories will OmniRx be released? The GDPR/UK GDPR section applies only if it ships outside the US.
- Final App Store age rating (RX-022): 16+ vs 18+ turns on whether prescription-medication education counts as 'Alcohol, Tobacco, or Drug Use or References'. Unresolved; the children's section has a placeholder.
- Is MHMDA 'collect' triggered when the developer never receives the data (repo RX-OQ-005)? No WA AG guidance and no case law. The policy deliberately does not rely on a negative answer.
- Does the FTC Health Breach Notification Rule reach an app that never transmits data off-device (repo RX-OQ-004)? Unresolved. If it does, a breach runbook and a breach-notice commitment may belong in the policy.
- Should the specific Hugging Face CDN hosts (huggingface.co, cas-bridge.xethub.hf.co and similar Xet/CAS endpoints) be named in the policy, or is 'Hugging Face and its content-delivery hosts' sufficient? Naming them is more precise but will go stale.
- The AI Model and Training Data Disclosure page (RX-049 / owner task B12) is linked from the main policy but does not exist yet. Publish it or remove the link.
- Confirm the CCPA threshold analysis in docs/REGULATORY.md §9.3 ('out of scope on all three thresholds') is still true at launch, and re-check annually.
- PrivacyInfo.xcprivacy is a 73-byte text placeholder that asserts HealthKit data is 'collected+accessed'. The App Store privacy label and privacy manifest must be rebuilt to match this policy, or the label and the policy will contradict each other.
## Addendum 2026-09-24 (owner follow-ups; OmniRx branch feat/privacy-followups-2026-09-24)

Evidence for the 24 September page changes, read from that branch (the app PR merges before this page):

- Ask model stack: `OmniRxKit/Sources/Intelligence/AskModel/`. Catalog `RxModelCatalog.swift` (openbmb/MiniCPM5-2B-MLX @ 8a9ad7539ac8…, 1,426,008,802 bytes; mlx-community/gemma-4-E2B-it-qat-4bit @ 42f62737af7a…, 4,361,680,121 bytes; mlx-community/gemma-4-E4B-it-qat-4bit @ 0f35c6f6d386…, 6,830,817,013 bytes; per-file sha256). Ladder `RxModelTier.swift` (none at 6 GB or less, no Metal 3, tvOS, watchOS). Clearance `RxGateRTable.swift`: no Gate R report for OmniRx, `.ownerEnabledWithoutGateR(decidedOn: "2026-09-24")`, every row true.
- Consent: `RxModelConsent.swift` (grant names model id and commit; keys `rx.ai.askModel.*`); only `RxModelDownload.prepareModel` calls `RxMLXClient.enableNetworkLoad()`, after `consent.allowsDownload` and the Ask switch (`RxAskModelContractTests`). Dialog text `RxModelConsent.promptMessage(for:)`; UI `AppSurfaces/Features/Learn/RxAskModelSection.swift` (Ask screen only).
- Network: `OmniRxHubClient` (`Intelligence/MLX/Download/HubDownloaderBridge.swift`): `HubClient.defaultHost`, userAgent "OmniRx", `tokenProvider: .none`, cache Application Support/OmniRx/HubCache (backup-excluded by `OmniRxContainerPaths.prepareOwnedDirectories`). Session `DownloadSessionFactory.makeHubSession`: `allowsExpensiveNetworkAccess = true`, `allowsConstrainedNetworkAccess = false`.
- Checks: `RxModelMemoryGate` before the offer and before each load; `DownloadStorageGate` before a download; `RxModelIntegrityVerifier` sizes every load, sha256 the first time (marker `.omni-verified-<revision>`).
- Answer path: `RxEducationAsk.swift` — crisis, Ask switch, `RxBoundaryGuard`, Apple Intelligence, then the downloaded model only when its pinned snapshot is complete on disk (`RxMLXClient.generate` loads from disk, `mayDownload: false`). Watch questions: `RxAskOrigin.watch(appIsActive:)` — the downloaded model runs only while the app is active; nothing downloads.
- Removal: `RxAskModelControls` (turn off, remove), shown on the Ask screen and in More ▸ Ask; `RxAppDataService.purgeInContainerModelCache` deletes the Hub cache on Delete all (unchanged).
- Delete all resets: `RxSettingsKey.resetByDeleteAll` (app.appearance, rx.watch.showMedicineNames, rx.disclosure.acknowledged/-Version/-On, rx.firstRun.hopToAddMedicine) in `RxAppDataService.purgeDefaults`; `RootView` re-presents the notice when the stored version drops; `AppContainerView` does not mirror the appearance reset to iCloud. `RxDisclosure.currentVersion` 9.
- Retired: the "Allow one model download (about 420 MB)" switch and `OmniRxCatalog` (Qwen3 0.6B); `RxRetiredModelCleanup` removes `rx.ai.modelDownloadConsentGranted(On)` once.
- Review fixes (same branch, commit 6657194): the downloaded model's path runs `RxBoundaryGuard` again on the grounded prompt before generating (`RxEducationAskController.downloadedModelRefusal(forGrounded:)`), as main's `MLXLLMClient.streamAssistantResponse` did; `RxMLXClient.download` re-applies `OmniRxContainerPaths.prepareOwnedDirectories()` (backup exclusion) before every transfer. Accepting the first-run notice after Delete all calls `RxPreferencesSync.writeDisclosureVersion`, which creates a new `RxUserPreferences` record (`fetchOrCreate`, appearance default "system") when the sync context exists; both pages now say so.

## Addendum 2026-09-27 — the reminder time on the Apple Watch (Watch App Group)

Pairs with the OmniRx app PR on branch `fix/watch-complication-2026-09-27` (owner, 2026-09-27: "do everything.. go ahead"; the D-09 fix OmniWealth shipped on 2026-09-23, with background delivery as in OmniWealth #156). Read against OmniRx origin/main `a32a9ed` and that branch. Survey: `docs/watch-complication-data-survey-2026-09-27.md` (Omni workspace), Rx row.

BEFORE (origin/main `a32a9ed`)
- The Watch app wrote the time to its own `UserDefaults.standard` (`App/OmniRxWatch/OmniRxWatchComplications.swift:20-22`), and only while `WatchNowView` was alive (`OmniRxWatchApp.swift:142-159`); the complication extension read its own `UserDefaults.standard` (`OmniRxWatchComplications.swift:13`). Separate containers, so the watch face always read "Learn". The Watch widget extension was signed with no entitlements.
- The iPhone sent the time even with the Daily reminder off, the default (`RxDoseReminderScheduler.swift:169-183`, formatted from `DoseReminder.loadTime()`, 08:00 by default), and turning the switch off sent nothing. `WristSession.apply` ignored an empty time and kept any value without " · " as the time.
- No WatchConnectivity background task; the Watch applied a card only while the app ran.

AFTER (the branch)
- App Group `group.legal.prameya.OmniRx.watch` on the Watch app (`App/OmniRxWatch/OmniRxWatch.entitlements`, which keeps its iCloud key-value entitlement) and the Watch widget extension (`App/OmniRxWatchWidgets/OmniRxWatchWidgets.entitlements`, new; pbxproj `CODE_SIGN_ENTITLEMENTS` Debug and Release). The host, the Home Screen widget and Apple TV join no group (`WatchAppGroupContractTests`, `HomeScreenWidgetContractTests`).
- `WatchComplicationStore` (`OmniRxKit/Sources/Continuity/WatchComplicationStore.swift`): `UserDefaults` can open the suite only on watchOS (`:34`, `:67`); stores "HH:mm" in ASCII digits and nothing else (`isTimeLabel`, `:77`), removes the key for nil, "" or any other value, writes and reloads the complication only when the value changes (`:114-129`). A medicine name handed to it is never stored (`WatchComplicationStoreTests.aMedicineNameNeverReachesTheWatchFace`). The complication reads only this (`OmniRxWatchComplications.swift:52`).
- The Watch writes in `WristSession.apply` (`WristSession.swift:170-172`), not in a view. The iPhone sends "" while the Daily reminder is off (`DoseReminder.wristTimeLabel`, `DoseReminder.swift:259`; `RxDoseReminderScheduler.swift:172`), and turning the switch off re-sends the card (`:216-219`). Delete all my data removes the reminder settings and re-sends the card, so the time clears.
- Delivery: WCSession activates once in the Watch app's `init` (`OmniRxWatchApp.swift:25`, `WristSession.swift:58-59`); the scene declares `.backgroundTask(.watchConnectivity)` (`OmniRxWatchApp.swift:38-39`), whose wake waits up to five seconds for activation and `hasContentPending`, then applies the newest application context (`WristSession.swift:127-141`); activation also applies a context that arrived while the app was not running (`:211`). Hence "can take in a new card in the background".
- The Watch app deletes its old own-defaults copy at launch (`OmniRxWatchApp.swift:24`).
- Privacy manifests: Watch app UserDefaults CA92.1 + 1C8F.1; Watch widgets 1C8F.1 only (it no longer reads its own defaults); host, TV and Home Screen widget unchanged. Nothing collected, nothing tracked; App Store privacy label unaffected ("Data Not Collected").

POLICY CHANGES (policy.md)
- Apple Watch bullets: the card carries the time only while the daily reminder is on; the complication shows it, never a medicine name; storage only the Watch app and complication share; off → no time, the Watch removes it, "Learn"; background take-in.
- Delete all bullet and "does not reach": the new card carries no time; until the Watch connects, the complication shows the last time.
- Dated 27 September entry; effective date.

VERIFIED, NO CHANGE
- health-data.md: the reminder time is a reminder setting, not a listed category of consumer health data, and the Watch bullet there names only the card and the optional medicine names; no sentence becomes false. Not edited.
- The time is not sent to Prameya, iCloud or anyone else; it travels only over WatchConnectivity between the user's own paired devices.

## 2026-09-27 (later) — cancel paths on Mac and Apple Vision Pro; hotspot wording

Owner approved this wave 2026-09-27 ("finish all pending work"). Code read from OmniRx `main` at 1be5679 (merge of PR #158 `fix/platform-release-2026-09-27`). The policy keeps 27 September 2026, which `OmniRxKit/Sources/RxCore/Content/RxTVAboutCopy.swift:34` pins ("effective 27 September 2026"); the short version (RxTVAboutCopy `:36-86`) is unchanged. The health policy is not changed.

CORRECTED — "Cancel: iOS Settings → your name → Subscriptions → OmniRx, or More → the subscription row" and "renew until you cancel in Settings"
- `PaywallView.cancelPath(on:)` (`OmniRxKit/Sources/AppSurfaces/Features/Settings/PaywallView.swift:405-411`): macOS "App Store app → your name → Account Settings → Subscriptions → Manage"; visionOS "Settings → your name → Subscriptions"; iOS "Settings app → your name → Subscriptions". Pinned by `PaywallTermsTests`.
- The More row manages a subscription only as "Manage subscription" (`RxCore/Monetization/SubscriptionTier.swift:202`; lifetime reads "Pro — lifetime", free opens the paywall); `RxSettingsView.swift:448-456`: sheet on iOS/visionOS, `openURL("https://apps.apple.com/account/subscriptions")` on macOS.

CORRECTED — "it can use cellular data, but not while Low Data Mode is on" named only cellular
- `DownloadSessionFactory` (`OmniRxKit/Sources/Intelligence/MLX/Download/DownloadSessionFactory.swift:25-26`): `allowsExpensiveNetworkAccess = true`, `allowsConstrainedNetworkAccess = false`, no platform branch; on a Mac or Vision Pro the expensive path is a Personal Hotspot. There is no download switch.

VERIFIED, NO CHANGE
- Model table rows for Mac, Vision Pro, Apple TV and Watch (`Intelligence/…/RxModelTier.swift:196-297`); "Apple TV has no Ask" (`App/OmniRxTV/OmniRxTVApp.swift:7-10`, `:34-41`); TV writes the page ID (`:354-357`).
- Not described and not contradicted: the Apple TV About tab (`OmniRxTVApp.swift:98-101`, `:436-481`) and the TV reader's safety blocks (#158).

## Addendum 2026-10-07 — age assurance, the daily-check widget, one label link per medicine

Re-audit of OmniRx origin/main `8b4b134` (merge of #176), covering PRs #159–#176 since `1be5679`. Each finding was confirmed by a second reviewer before the pages changed. Both pages move to 7 October 2026; terms.md is unchanged.

CHANGED — age assurance (#176), policy.md Children, short version, data table, StoreKit, new "Apple's age tools", Delete all
- `OmniRxKit/Sources/AppSurfaces/RootView.swift:63` mounts `AgeAssuranceHost` after the first-run notice, not DEBUG-gated; `AppContainerView.swift:60` is the iPhone, iPad, Mac and Vision Pro root. TV (`App/OmniRxTV`) and Watch (`WatchRootView`) do not mount it.
- `OmniRxKit/Sources/AppSurfaces/AgeAssurance/AgeAssuranceHost.swift`: `:107` `AppStore.ageRatingCode`; `:127-142` `isEligibleForAgeFeatures`, `requiredRegulatoryFeatures`, `requestAgeRange` (gates 13/16/18, `RxCore/AgeAssurance/SignificantChange.swift:80-84`) when required or eligible and not yet asked; `:155-176` stores bounds, declined, declaration; `:183-197` adult acknowledgment on iOS only; `:58-71` PermissionKit `PermissionButton` `.askToApprove` ("Ask a parent to approve this change"), sent only when the reader taps it; `:200-213` `AskCenter` responses (and `:85-102` approve-in-person): an approval clears the pending change (`AgeAssuranceRecord.grantSignificantChange`, `:137-142`; `consentedEpoch` stays 1 because `currentEpoch == baselineEpoch`), so the record is the same as one that never saw a change; a denial only sets `permissionKitStatus = .called`, which `:111` already sets on every run, so it is not recorded. `shouldAskParent` (`:122-125`) stays true until an approval, so the sheet is offered again on every main-window open (`:118`, `:211`). `medicationClassIsAvailable`, `applyRevocation` and `ConsentRevocationPayload.notice(fromForwardedPayload:)` have no caller outside tests, so the answer changes nothing else and a later withdrawal never reaches the app. DeclaredAgeRange is absent from the visionOS, tvOS and watchOS SDKs (`#if canImport`), so Vision Pro only reads the rating.
- `RxCore/AgeAssurance/AgeAssuranceRecord.swift`: fields `:25-46`; the only `pending.append` is an age-rating change (`:98-114`); `shouldAskParent` `:122-125`; `currentEpoch == baselineEpoch == 1` (`SignificantChange.swift:32-35`); `applyRevocation` has no caller. Stored in `UserDefaults.standard` under `rx.age.record` (`:198`, `:209-212`); not in CloudKit, KVS or either export.
- Delete all: `Persistence/RxAppDataService.swift:955` purges the `rx.age.` prefix.
- Entitlement `com.apple.developer.declared-age-range`: `App/OmniRx/OmniRx-iOS.entitlements`, `OmniRx-macOS.entitlements`, `OmniRx-Debug.entitlements`.

CHANGED — Home Screen widget (#175), both pages
- `Knowledge/HomeScreenGlance.swift:10-34`: "Nothing to log yet" with no medicine followed, else "Daily check" / "One medicine" (fixed, however many are followed). `AppSurfaces/Continuity/RxContinuityBridge.swift:143-155` writes it to KVS `homescreen.glance` (`Continuity/HomeScreenGlanceStore.swift:129-136`) from `MainTabView.swift:90-94` and `AppContainerView.swift:114`; a tap writes the fixed marker `daily-check` (`HomeScreenGlanceStore.swift:157-164`, `StartHomeTopicIntent.swift:16`) and opens You (`RxContinuityBridge.swift:158-161`). The widget is iPhone and iPad only (pbxproj `SUPPORTED_PLATFORMS = "iphoneos iphonesimulator"`), `systemSmall` and `systemMedium` (`App/OmniRxWidgets/HomeScreenTopicWidget.swift:30`), so it can sit on the Home Screen, in Today View or StandBy, or on a Mac desktop as an iPhone widget; it shares the host's KVS identifier (`App/OmniRxWidgets/OmniRxWidgets.entitlements`).

CHANGED — one label link per followed medicine (#174), both pages
- `AppSurfaces/Features/Home/RxHomeView.swift:65-67`, `:154-174` (`labelPageLinks`, one per roster name) → `openLearnPack` → `RxLearnView.swift:66-70` `publish(surface: "understand", packID:)` → KVS, opened list, Handoff.

CHANGED — topic page IDs can name a condition (missed by the first pass), both pages
- `Knowledge/Resources/depression.pack.json:3` (`"pack_id": "depression"`), `type_2_diabetes_mellitus.pack.json:3`; `RxPackDetailView.swift:73` saves every opened page (`RxContinuityBridge.openedTopic`, #162).

In-app mirror moved with the policy: `OmniRxKit/Sources/RxCore/Content/RxTVAboutCopy.swift` (effective line and the three changed short-version points, word for word; checked by script against policy.md) and `OmniRxKit/Tests/RxCoreTests/RxTVAboutCopyTests.swift`.

VERIFIED, NO CHANGE
- terms.md: no statement made false; `RxTerms` §5 still matches (`LegalSectionContractTests`).
- No new host, URLSession, SDK, purpose string or background mode. `PrivacyInfo.xcprivacy` collects nothing; App Store privacy label unchanged (Data Not Collected).

### Review pass, 2026-10-07 (same day)

A second reviewer read the draft against the code. What changed:

CORRECTED — the parent's answer. The draft said the app keeps the parent's answer and that the record holds "whether they approved". Neither is true (see the `AskCenter` line above). Children now says what an approval and a refusal do, that the app works the same either way, and that a later withdrawal through Apple does not reach the app; the table row names the pending rating change instead. The old page's "grant or revoke" is quoted in the dated entry.

CHANGED IN THE APP — the list of opened pages (`homescreen.openedPacks`). It was written from `RxContinuityBridge.publish(surface:packID:)` (`HomeScreenGlanceStore.markOpened`, the only caller) and read by nothing in the kit, the widget, the Watch or the TV after #175, so both pages gave it a purpose the code no longer served. This run drops the write (`markOpened` and `openedPackIDs` are removed), adds `ContinuityKeys.retiredKVSKeys` and `UbiquitousContinueStore.removeRetiredKeys`, called from `AppContainerView`'s `.task` on every launch of the iPhone, iPad, Mac and Vision Pro app, and keeps the key in `allKVSKeys` so Delete all still clears it. `ContinueSyncDisclosureContractTests.everyKeyValueKeyIsTheOneTheDisclosuresDescribe` pins all three (no writer in `OmniRxKit/Sources` or `App`, the launch call, removal leaves the other keys). Both pages now describe one page ID (the last one opened, `continue.payload`) and say earlier versions kept a list that this version removes.

CORRECTED — More's iCloud caption (`RxSettingsView.swift:249-260`) said Continue works on "the widget" and that the plate is "Daily check for the one medicine". It now says Continue on Apple Watch and Apple TV, the last page's ID, and what the widget shows.

CORRECTED (nits) — "on this device only" (the record is in `UserDefaults.standard`, which a device backup includes); "Once you have answered, the app does not ask again" softened to "asks only until it has recorded an answer" (each window's `AgeAssuranceHost` loads at `:106` and saves at `:116`, after the acknowledgment sheet at `:115`, so two windows opening together can both ask); "You, or your parent or guardian, can decline"; StoreKit transaction data now says StoreKit also reads the age rating, which is not transaction data; "Apple's age tools" says the request is sent only after a tap on the app's button; the widget can show its line wherever it is placed; "label-page IDs" and "the IDs of the label pages" at the tiers list and the right to delete now name the last page.

### Final check, 2026-10-07 (same day)

CHANGED IN THE APP — the widget's line waits for the first-run notice. `AppContainerView`'s second `.task` published it at launch, outside `RootView`'s notice gate (`RootView.swift:36-63`), and `MainTabView`'s roster `onChange` could publish it after Delete all had cleared the acceptance (and the key). `RxContinuityBridge.publishHomeScreenGlance` (`:150-174`, guard at `:162`; still called from `AppContainerView.swift:119`) now writes nothing until `RxUserSettings.hasAcknowledgedDisclosure` (the current version of the notice), so no fact about the medicines you follow reaches iCloud first; `MainTabView.swift:90`, `:93` publish once it is accepted. The retired-key removal still runs before the notice, since it only deletes. `RxHomeScreenGlanceNoticeTests` (AppSurfaces) fails on the old code. Neither page says when the line is written, so no page text changed for this.

CORRECTED — "the Continue values — including the ID of the last label page you opened" (policy.md, iCloud sync) read as if the last label page were kept apart from the last page; only the last page of either kind is kept. Children now says the app keeps offering the Ask a parent button until an approval, not only on each main-window open (`AgeAssuranceHost.swift:101`, `:118`, `:211`).

OPEN (owner)
- The first-run notice (`RxDisclosure` v11, `:135-139`) and `networkPosture` (`:208-218`) still say Continue works "on ... the widget", and the notice does not mention the widget's line or the age-range question. The Apple TV About tab shows `firstRunBody` directly above `RxTVAboutCopy.privacyShortVersion` (`App/OmniRxTV/OmniRxTVApp.swift:523`, `:526`), so one TV screen says both. health-data.md promises consent before a new use; the app has not asked for any. Accepting v11 is not consent to the widget's line, because v11 does not mention it; rewording the notice and bumping `RxDisclosure.currentVersion` is the owner's call. The final check made the line wait for whatever notice is current (below), so a bump now holds the write until it is accepted.
- `SignificantChangeCatalog.currentEpoch` stays 1, so this privacy-policy change does not trigger the parent-approval or adult-acknowledgment flow. Whether it counts as an SB 2420 significant change is an owner decision.
- Connect age-rating answers `ageAssurance = false`, `parentalControls = false` (`docs/APP_STORE.md:214`) predate #176.

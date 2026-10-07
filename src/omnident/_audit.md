# OmniDent — data-flow audit

AUDIT OF /Users/sbkoth/work/Omni/OmniDent (147 Swift files, entitlements, Info.plist, PrivacyInfo.xcprivacy, project.pbxproj, Docs/REGULATORY.md, ISSUES.md). Code was treated as authoritative where docs disagreed.

CAMERA AND PHOTOS
- Real in-app camera: AVCaptureSession / AVCapturePhotoOutput (Features/Capture/CameraViewModel.swift, PhotoCaptureDelegate.swift). Intraoral photographs of the user's own mouth.
- Storage: JPEG written to Documents/Scans inside the app sandbox (Domain/Services/AppDataService.swift:83-99, scansDirectory). Thumbnail bytes + metadata in SwiftData.
- File protection: OmniDent.entitlements sets com.apple.developer.default-data-protection = NSFileProtectionComplete. (The in-app PrivacyPolicyView claims NSFileProtectionCompleteUntilFirstUserAuthentication — wrong, and weaker than reality.)
- Photos are NOT in the CloudKit schema. Primary ModelContainer is explicitly cloudKitDatabase: .none (App/OmniDentApp.swift:167). Photos never reach Prameya — Prameya runs no server.
- HOWEVER: AIUserPreferences.autoSaveCapturesToPhotos defaults to TRUE (Data/Models/AIUserPreferences.swift:26). New captures are auto-saved to the system Photos library via PHPhotoLibrary .addOnly (AppDataService.swift:308, 373, 746-800). If the user has iCloud Photos on, mouth photos leave the app container into the user's own iCloud. The old in-app policy called this "optionally copied ... at your explicit request" — false.
- PhotosUI/PHPicker used in Features/Studio/StudioView.swift and Features/AIChat/AIChatView.swift for user-selected images attached to on-device chat.

NETWORK EGRESS (three destinations, all HTTPS; NSAllowsArbitraryLoads=false)
1. Hugging Face Hub — model weight downloads. Packages: swift-huggingface (HuggingFace), swift-transformers (Hub/Tokenizers/Transformers), mlx-swift-lm (MLXVLM/MLXLLM/MLXHuggingFace). Domain/MLX/Download/RobustDownloader.swift, HubDownloaderBridge.swift, ResilientResolve.swift. Catalog repos in Domain/AI/OmniDentCatalog.swift: mlx-community/Qwen2.5-0.5B-Instruct-4bit, Llama-3.2-1B-Instruct-4bit, gemma-4-e2b-it-4bit, SmolVLM-Instruct-4bit, gemma-3-4b-it-qat-4bit, paligemma-3b-mix-448-8bit. IMPORTANT NUANCE: downloads are user-initiated only. AIService.ensureModelReady (Domain/Services/AIService.swift:378-395) refuses to call loadModel when the model is not on disk, and VLMStage.swift:93-98 only loads an already-downloaded model. The download button lives in Features/Settings/AIModelManagementView.swift:485. So analysis never silently triggers a fetch. There is no consent sheet naming host/size/licence yet (ISSUES.md DENT-015), and MLXModelManager+OmniDent.swift:17 sets policy .unrestricted.
2. CloudKit — private database, container iCloud.legal.prameya.OmniDent.ai. Dual-container design (App/OmniDentApp.swift:176-215). Sync schema TODAY = UserProfile, TrajectorySnapshot, HabitLog, AIUserPreferences, OralHealthResetProgress. UserProfile carries age, brushingFrequencyPerDay, sugarIntakeLevel, smokingStatus, diabetes, dryMouth, goals (Data/Models/AppDataModels.swift:5-14) — unambiguously health data. HabitLog and TrajectorySnapshot are health-derived. This is ISSUES.md DENT-010 / Apple 5.1.3(ii) blocker. Wave 2 restricts sync to non-health only.
3. Apple push (aps-environment production, UIBackgroundModes remote-notification, BGTaskSchedulerPermittedIdentifiers com.apple.coredata.cloudkit.activity) — CloudKit silent push only. No marketing push, no push payload from Prameya.

NO OTHER EGRESS. AIService.swift contains zero URLSession/HTTP calls — no remote LLM, no RAG endpoint. No AdMob/GoogleMobileAds, no Firebase, no analytics SDK anywhere. NSPrivacyTracking=false, NSPrivacyTrackingDomains empty. No StoreKit purchases (StoreKit imported only for requestReview). Features/Learn/PartnersPromoView.swift is a fully local stub — partner "claims" are written to a local PromoClaim record; nothing is transmitted, no affiliate tracking. AIService.contributeToCollectiveAnonymized (AIService.swift:1302) is a no-op that only writes a log line; nothing is uploaded to any "collective".

SENTRY: App/OmniDentApp.swift has a Sentry init block behind #if canImport(Sentry), gated further on a SENTRY_DSN env var. The Sentry package is NOT in OmniDent.xcodeproj/project.pbxproj XCRemoteSwiftPackageReference list (only mlx-swift, swift-transformers, mlx-swift-lm, swift-huggingface, swift-certificates). So no crash reporter ships. PrivacyInfo.xcprivacy nonetheless declares NSPrivacyCollectedDataTypeCrashData — over-declared (ISSUES.md DENT-013).

ACCOUNTS
- Sign in with Apple only (Features/CloudSync/CloudSyncFeature.swift:234, ASAuthorizationAppleIDCredential at :277). Opaque Apple user ID + optional full name + optional email captured on first sign-in, stored in Keychain via SecureStore (Domain/Services/CloudSyncService.swift:73-107). No Prameya account, no password, no Prameya user database.
- signOut() clears keychain (CloudSyncService.swift:86-89). There is NO in-app account deletion and NO call to POST https://appleid.apple.com/auth/revoke. ISSUES.md DENT-012, blocker, Apple Guideline 5.1.1(v). Wave 2 must ship it.

HEALTHKIT (Domain/Services/HealthKitService.swift)
- Writes: HKCategoryTypeIdentifier.toothbrushingEvent, HKQuantityTypeIdentifier.dietarySugar.
- Reads: stepCount, sleepAnalysis, mindfulSession, activeEnergyBurned.
- Entitlements include com.apple.developer.healthkit and healthkit.background-delivery. health-records was deliberately removed. All optional and toggled in Settings.

DELETE / EXPORT
- AppDataService.deleteAllUserData() (AppDataService.swift:579-636) deletes Scan records + their JPEG files, TrajectorySnapshot, HabitLog, PromoClaim, OralHealthResetProgress. It does NOT delete UserProfile — the code carries the comment "Future: also clear UserProfile if/when actively used". So "Delete All Scans & Data" is currently incomplete.
- exportAllUserData() (AppDataService.swift:1040-1112) produces a local JSON of metadata only — explicitly notesSample: nil, no raw photos.

FDA / CLINICAL GATE
- No FDA clearance gate exists in the code today. Greps for clearanceGate/FDAClearance/clinicalMode/featureFlag return nothing. Docs/REGULATORY.md §1.6 records that four bright lines are currently crossed by shipped stub UI (Features/Studio/StudioView.swift:638 renders fabricated findings such as caries with a confidence number; Domain/Plugins/AnalysisCapability.swift declares .caries; Domain/AI/VLMPrompts.swift steers the model toward gingivitis/caries/erosion). ISSUES.md DENT-001/004 are blockers. Wave 2 puts diagnostic output behind a default-OFF clearance gate; the policy is written to the shipping configuration (educational only, no disease findings) and flags it.

MANIFEST / LABELS
- PrivacyInfo.xcprivacy declares Health, SensitiveInfo, PhotosOrVideos (all Linked=false), Name and EmailAddress (Linked=true), CrashData; required-reason APIs UserDefaults CA92.1, FileTimestamp C617.1, DiskSpace E174.1. ISSUES.md DENT-031 confirms the manifest itself is correct and must not be changed; ASC_NOTES.md and Docs/AppStoreMetadata.md are the documents that are wrong.
- App category public.app-category.healthcare-fitness. Widget App Groups intentionally disabled, so the Home Screen widget currently has no live data.
- Info.plist purpose strings for camera/photos/HealthKit are accurate and already say photos are never uploaded.

## Corrections to prior claims

- FALSE: 'All processing and storage is 100% on-device.' (in-app Features/Settings/PrivacyPolicyView.swift). TRUE: processing of your content is on-device, but the app is not 100% on-device. It downloads AI model files from huggingface.co, syncs data through Apple CloudKit into the user's private iCloud database, and uses Apple's push service for CloudKit change signals.
- FALSE: 'No accounts, no telemetry, no third-party trackers, no advertising.' (in-app PrivacyPolicyView.swift). TRUE on telemetry, trackers and advertising. FALSE on accounts — OmniDent ships Sign in with Apple, holds an Apple user identifier plus optionally name and email in the Keychain, and declares Name and EmailAddress as Linked to the user in PrivacyInfo.xcprivacy.
- FALSE: 'Photos and analysis never leave this device. No accounts, telemetry, or cloud uploads of sensitive data.' (shipped Settings screen, Features/Settings/SettingsView.swift:262). TRUE: photos are not uploaded to Prameya and are excluded from the app's CloudKit sync — but the app auto-saves new captures to the system Photos library by default, which for most users means iCloud Photos. And accounts do exist.
- FALSE: 'Dental photos you choose to capture ... optionally copied to your Photos library at your explicit request.' (in-app PrivacyPolicyView.swift). TRUE: AIUserPreferences.autoSaveCapturesToPhotos defaults to true. Copying to the Photos library is the default behaviour for every new capture, not an explicit per-photo request.
- FALSE: 'protected by iOS Data Protection class NSFileProtectionCompleteUntilFirstUserAuthentication per entitlements' (in-app PrivacyPolicyView.swift). TRUE: OmniDent.entitlements sets com.apple.developer.default-data-protection to NSFileProtectionComplete — a stronger class. The prior claim understated the protection and misdescribed the entitlement.
- FALSE: 'Optional large ML models (behind explicit consent) may involve one-time downloads from Apple servers or approved endpoints.' (in-app PrivacyPolicyView.swift). TRUE: model weights are downloaded from Hugging Face (huggingface.co), not from Apple. There is also no separate consent gate in code — MLXModelManager is configured with policy .unrestricted. What is true is that downloads are user-initiated from Settings → Manage Models, and analysis will not silently trigger one.
- FALSE: 'All inference runs locally. No data leaves the device.' (shipped Settings AI Models footer, SettingsView.swift). TRUE: inference is local. But data does leave the device — model requests to Hugging Face, and preference/profile records to CloudKit.
- FALSE: 'No network of photos (100% on-device path).' framed as though the whole app is offline (ASC_NOTES.md, 'Potential Review Flags'). TRUE for photographs specifically. The app as a whole has three network destinations.
- FALSE: 'Data Linked to User: No' (ASC_NOTES.md privacy nutrition label guidance). TRUE: the shipped PrivacyInfo.xcprivacy declares NSPrivacyCollectedDataTypeName and NSPrivacyCollectedDataTypeEmailAddress with NSPrivacyCollectedDataTypeLinked set to true, because of Sign in with Apple. The ASC label must match the manifest.
- FALSE: Accessed API Types listed as 'Camera (User input), Photo Library (User input), HealthKit (Health data), CloudKit (User initiated)' (ASC_NOTES.md and Docs/AppStoreMetadata.md). TRUE: Apple's required-reason API categories are only file timestamp, system boot time, disk space, active keyboard and user defaults. The shipped PrivacyInfo.xcprivacy is correct (UserDefaults CA92.1, FileTimestamp C617.1, DiskSpace E174.1) and must not be changed; the two documents are what is wrong. Confirmed in ISSUES.md DENT-031.
- FALSE by omission: PrivacyInfo.xcprivacy declares NSPrivacyCollectedDataTypeCrashData. TRUE: no crash-reporting SDK is linked. The Sentry code in App/OmniDentApp.swift sits behind #if canImport(Sentry) and the Sentry package is absent from project.pbxproj, so it compiles out. Nothing collects crash data. An over-declared label is still an inaccurate label.
- FALSE: 'Scans and AI analysis stay on-device only' presented as the complete picture of what iCloud sync does (SettingsView.swift:187 and CloudSyncFeature.swift:118). TRUE as far as it goes, but the same sync carries the oral-health profile (age, smoking, diabetes, dry mouth, sugar intake, brushing frequency), habit logs and cost-trajectory snapshots — all health-derived — into iCloud. Post-Wave-2 this must be reduced to preferences and interface state, and the copy must then say so.
- FALSE: the portfolio-wide privacy policy at prameyallc.github.io/edu-app-privacy scopes itself to apps with no accounts, no uploads, and no health or financial data. TRUE: OmniDent has accounts (Sign in with Apple), off-device storage (CloudKit), network egress (Hugging Face, CloudKit, Apple push), and processes health data including intraoral photographs and HealthKit records. That policy has never been accurate for this app and must not be linked from OmniDent's App Store listing.
- FALSE: the portfolio regulatory baseline assumed 'photographs are outside the cleared-device space' and that no FDA authorization exists for AI analysis of intraoral photographs. TRUE: 21 CFR 872.1770 is a dental-specific regulation for optical camera-based intraoral image analysis, with two authorizations (DEN230035, DentalMonitoring, De Novo granted 2024-05-17; K260082, 3Shape TRIOS Dx, cleared 2026-04-10). Recorded in Docs/REGULATORY.md §1.2. This matters to the policy because it is why the diagnostic gate must be default-OFF and why the policy must not describe the app as detecting anything.
- FALSE: 'We respond to verifiable requests for access, correction, or deletion' with no stated timeline (in-app PrivacyPolicyView.swift). TRUE only if a timeline is committed to. Washington's MHMDA requires a response within 45 days, extendable once by 45 days, plus a documented appeal process and a route to the Washington Attorney General on denial. The new policies commit to all of that.
- FALSE by omission: neither the in-app policy nor any repo document mentions Washington's My Health My Data Act, Nevada SB 370, CCPA/CPRA, COPPA, GDPR, or HIPAA. TRUE: OmniDent processes consumer health data, so a separate MHMDA policy is legally required and none existed. HIPAA does not apply, and saying so plainly is useful rather than harmful.
- FALSE by omission: no prior document disclosed that 'Delete All Scans & Data' leaves the stored oral-health profile in place (AppDataService.deleteAllUserData carries a 'Future: also clear UserProfile' comment), nor that there is no account-deletion path at all.
- CORRECTION on contact: App/AppContact.swift and ASC_NOTES.md use admin@prameya.legal. The published policies use admin@prameya.legal as instructed. These must be reconciled — a privacy policy naming an address the app does not surface is a support failure and an FTC-relevant inaccuracy.
- NOT FALSE, worth stating affirmatively because it was never documented: AIService contains no HTTP calls at all — there is no remote LLM, no RAG endpoint, no fallback to a cloud model. The 'collective intelligence' contribution function (AIService.swift:1302) is a stub that writes a log line and uploads nothing. The partner/promo screen is entirely local with no affiliate tracking. There is no ad SDK, no Firebase, no analytics library. These are real privacy properties the app can honestly claim and previously did not.

## Open questions

- BLOCKING — Sign in with Apple account deletion. The main policy section 4 and the health policy deletion section both describe an in-app Delete Account flow that revokes the Apple token via POST https://appleid.apple.com/auth/revoke. That flow does not exist in the audited build (ISSUES.md DENT-012). Publishing before it ships would make the policy false about the single feature Apple Guideline 5.1.1(v) requires. Note that token revocation needs a server-side component to mint the client-secret JWT — that is a real lead time, not a one-line fix.
- BLOCKING — CloudKit sync scope. Both policies state that only non-health data (preferences and interface state) syncs. The audited build syncs UserProfile (age, smoking, diabetes, dry mouth, sugar intake, brushing frequency), HabitLog and TrajectorySnapshot. Confirm the sync schema in App/OmniDentApp.swift makeSyncContainer() has been reduced before publishing. If any health field still syncs, both policies need rewriting and Apple Guideline 5.1.3(ii) is violated independently.
- BLOCKING — Delete All Scans & Data does not clear the oral-health profile. AppDataService.deleteAllUserData() carries the comment 'Future: also clear UserProfile if/when actively used'. Both policies describe it as deleting everything. Fix the code or narrow the claim.
- Default-OFF clearance gate. No such gate exists in code today (no clearanceGate/FDAClearance/clinicalMode symbol anywhere). Section 1 of the main policy describes the shipping configuration as producing no diagnostic findings, but StudioView.swift:638 still renders fabricated caries/plaque findings with confidence numbers and AnalysisCapability.caries still exists. Confirm DENT-001 and DENT-004 are resolved before publishing.
- Auto-save-to-Photos default. The setting AIUserPreferences.autoSaveCapturesToPhotos defaults to TRUE, so mouth photos land in the user's Photos library (and their iCloud Photos) unless they turn it off. Recommend flipping the default to OFF. It is disclosed honestly in the policy either way, but a default-on copy of intraoral photographs into iCloud Photos is a poor look for an app whose headline claim is on-device privacy, and it partly undercuts the CloudKit health-data restriction.
- Crash Data over-declaration. PrivacyInfo.xcprivacy declares NSPrivacyCollectedDataTypeCrashData but no crash reporter is linked (no Sentry package in project.pbxproj). Remove the declaration, or if Sentry is added before release, rewrite the policy to name it as a transmitting third-party processor.
- App Store territories. Not documented anywhere in the repo. Section 15 (GDPR/UK GDPR) is written conditionally. If the app ships in the EEA or UK, take advice on whether an Article 27 EU representative and a UK representative must be appointed and named. If it is US-only, replace section 15 with a one-line statement to that effect.
- Support email mismatch. App/AppContact.swift hardcodes admin@prameya.legal, and ASC_NOTES.md repeats it. The policies use admin@prameya.legal per instruction. Make one of them win, and make the in-app Privacy Policy screen, the App Store Connect support URL and the published policy agree.
- In-app PrivacyPolicyView must be replaced. Features/Settings/PrivacyPolicyView.swift ships a self-labelled TEMPLATE with several false statements (listed in corrections). App Store Guideline 5.1.1(i) requires the policy to be linked in-app as well as in App Store Connect. Replace the bundled text with this policy, or make the screen load the published URL, and add a distinct second link to the consumer health data policy.
- Prominent homepage link. RCW 19.373.020(1)(b) requires a link to the consumer health data policy to be prominently published on the homepage. Confirm the hub at prameyallc.github.io/privacy and any OmniDent product page each carry a distinct, visible link to /privacy/omnident/health-data/ — not merely a link buried inside the main policy.
- Model catalogue accuracy. Domain/AI/OmniDentCatalog.swift lists mlx-community/gemma-4-e2b-it-4bit. Confirm every repository id in the shipping catalogue actually resolves on Hugging Face; the policy names them, and naming a repository that does not exist is a small but avoidable inaccuracy.
- Model download consent sheet. DENT-015 asks for a pre-download sheet naming huggingface.co, the file size and the model licence. Not shipped. The policy already discloses the host and that downloads are user-initiated, so this is not blocking, but the sheet would make the disclosure contemporaneous rather than buried in a policy.
- Model licences. DENT-024 notes MLX model licences are not enumerated. Gemma and Llama weights carry use restrictions. Not a privacy question, but it belongs in a THIRD_PARTY notice before release.
- Age rating questionnaire. Overdue since 2026-01-31 (DENT-030), which blocks submission entirely. The COPPA section of the policy assumes an adult-directed app; make sure the age-rating answers are consistent with that framing and with the affirmative 'medical or wellness topics' answer.

## 2026-09-26 — sync scope: no names or topics in iCloud, first-run state stays on device

Owner, 2026-09-26: "update the Dent privacy policy too". Both policies re-dated 26 September 2026. Code read from OmniDent `origin/main` at 947289e, which has PR #205 (merged as fef5af2), PR #206 `fix/dent-continue-no-name-2026-09-26` (merged as 2b516c9; commits 2e808af, 2637069, 9222e7d) and PR #207 (953e25b). The policy was first drafted against the unmerged #206 branch; every #206 file cited below is identical on main to that branch's tip 9222e7d. Line numbers are on 947289e.

CHANGED — first-run state is per install (OmniDent PR #205, commits 9590b06 + e6ff838, merged as fef5af2)
- `hasSeenWelcome`, `hasAcknowledgedHealthDisclaimer`, `healthDisclaimerAcknowledgedAt` now live in `FirstRunStore` (UserDefaults.standard, `app.firstRun.*`): `Persistence/FirstRunStore.swift:33-81`; read and written only through it by `Intelligence/AI/AISettings.swift:130-203`. The three columns stay on the CloudKit-mirrored `AIUserPreferences` row as unused legacy fields with default values (`DentalCore/Models/AIUserPreferences.swift:37-62`); `resetToDefaultsKeepingSyncChoice()` still clears what earlier TestFlight builds wrote there.
- Delete All clears them: `purgeDefaults()` owns the `app.` prefix (`Persistence/AppDataService.swift:1534`, `:1584`; the keys are not in `preservedDefaultsKeys`, `:1594`), and `DeleteAllAftermath.run()` redraws (`AppSurfaces/App/DeleteAllAftermath.swift:19-20`).
- Policy: section 6 synced-items table no longer lists "Interface state (welcome; wellness disclaimer)" as syncing — moved to the "Does not sync" column as kept on each device; section 8 CloudKit row "App preferences and interface state" → "App preferences"; section 10 Delete All list adds the welcome/disclaimer state on this device. Health policy: "App preferences" bullet drops "whether and when you acknowledged the wellness disclaimer" and says it stays on each device; third-party table CloudKit row drops "interface state"; Delete All paragraph adds it.

CHANGED — the Continue note carries no name or topic to iCloud, and no name over Handoff (OmniDent PR #206, commit 2e808af, merged as 2b516c9)
- iCloud KVS gets `ContinueStore.cloudPayload` only — tab, photo-record UUID, time; no `personDisplayName`, no `packID`/`itemID` (`Continuity/ContinueStore.swift:89-92`), with sync on (`savePayload`, `:106-121`); with sync off nothing is written and the keys are removed (unchanged). Appearance mode still goes to KVS while sync is on (`saveAppearance`, `:190-202`).
- An older named or topic-bearing entry is replaced at launch (`ContinueStore.scrubCloudCopy`, `:133-148`, called from `AppSurfaces/App/RootView.swift:126`) and at every save; with sync off it is removed. Anything read back from KVS passes through `cloudPayload` (`newest`, `:178-182`), so an old name or topic is never shown. A device still on an older build can write the old note again until it updates; the policy says so.
- Handoff: `ContinueStore.outboundPayload` (`:66-77`) drops the name with sync on and sends tab only with sync off; used by `HandoffActivity.makeActivity`/`configure` (`Continuity/HandoffActivity.swift:33`, `:61`). The topic (`packID`/`itemID`) and record ID still travel with sync on. Title stays "OmniDent · <tab>" (`:137-139`). Capture/packet identifier handoffs carry no name (unchanged).
- Paired Apple Watch: `WristPhoneSession.watchContinuePayload` (`AppSurfaces/App/WristPhoneSession.swift:179-189`) puts the name back for the Watch only, with sync on; tab only with sync off. The Watch shows the name (`App/OmniDentWatch/OmniDentWatchApp.swift:85-91`) and offers the last topic (`:163-165`). Confirmed.
- Apple TV: reads only KVS, so no name and no topic; Continue shows "You were last in the <tab> tab on another device" plus Open Library (`Continuity/CompanionRecordCopy.swift:38-44`, `App/OmniDentTV/OmniDentTVApp.swift:100-125`); default tab is Library (`:45`). The `tv-whose-record` name label is removed.
- Owner answers recorded in the app repo: `Docs/agent/DECISIONS.md` "Owner answers (2026-09-26)" (commit 2637069); in-app copy updated in the same commit (`Persistence/CloudSyncAllowList.swift:240`, `Features/Settings/PrivacyPolicyView.swift`, `Features/Settings/SettingsView.swift`), and the PrivacyInfo.xcprivacy comment.
- Policy sentences corrected: short version (iCloud note contents); section 3 "Household mouths" (name leaves in three ways → Watch only); section 6 continue-note list (split into what the device keeps vs what KVS gets), the per-device switch sentence, Handoff paragraph, Apple TV paragraph; section 8 KVS and Handoff rows; section 10 deletion row; section 12 child's-name paragraph and the Delete All sentence ("the continue note in iCloud, including a child's"); section 13 CCPA identifiers and health rows; section 19 new entry. Health policy: household-names row, continue-note row, "Where this data lives" KVS and Handoff bullets, children's table row (incl. "Apple TV" removed from who can see it), third-party KVS and Handoff rows, deletion row, changes entry.

VERIFIED, NO CHANGE
- Photo reading (OmniDent PR #204, commit 41fa220, merged as 564045c): with no vision model, an unreadable file or a vision failure, `PhotoAdviceService.advise` returns `.notRead` and no language pass runs. The policy describes only the flow that runs (vision, then text); it never said a reading is produced without the vision pass. No change.
- Scan photos are not excluded from backup: `Documents/Scans` (`Persistence/AppDataService.swift:280-286`) has no `isExcludedFromBackup`; only the Application Support folders are excluded (`:288-294`; `DentalCore/Services/OmniDentContainerPaths.swift:58-76`). Both policies already say the scan folder is in device backups. No change.
- iCloud Sync is on by default: `CloudSyncService.userEnabledSync` reads a missing key as ON (`Persistence/CloudSyncService.swift:157-160`). Both policies already say so. No change.
- Send Feedback opens the system mail app on every platform (OmniDent PR #207, 953e25b, adds Mac and Vision Pro; user-initiated). Policy section 8 already says it opens your own email app. No change.
- The Watch bullet and the Watch row in section 8 of the main policy, and the Watch bullet in the health policy, are unchanged: the Watch still gets the full note, name and topic included, while sync is on, and the tab alone with it off.
- App Store privacy label ("Data Not Collected"): unaffected (`NSPrivacyCollectedDataTypes` is empty, `App/OmniDent/PrivacyInfo.xcprivacy:46-47`). Nothing is sent to Prameya or a third party for its own use; this change only narrows what goes to the user's own iCloud and Handoff.

LEFT AS HISTORY
- The 23 September 2026 entries in both "Changes" sections still describe the note as it was then (name and topic in iCloud KVS). They are dated history of that version and the 26 September entry above them supersedes them.

## 2026-09-27 — the unlock for leaving a child session, per device

Owner authorised publishing 2026-09-27 ("do everything.. go ahead"). Both policies re-dated 27 September 2026. Code read from OmniDent `origin/main` at 5811a89 (merge of PR #213 `fix/platform-wave-2026-09-27`).

CORRECTED — "Face ID or the device passcode" was said for every device
- The lock is `DevicePasscodeUnlock.confirmAdultAccess()` (`AppSurfaces/App/HouseholdUnlockService.swift:20-37`): `LAContext.evaluatePolicy(.deviceOwnerAuthentication, localizedReason: "Unlock adult mouth records")` on iOS, macOS and visionOS; it is called before leaving a child session (`AppSurfaces/Features/Care/HouseholdViews.swift:80`, `AppSurfaces/App/HouseholdSplitShell.swift:206`). If `canEvaluatePolicy` fails (no passcode or password set) the switch goes through (`:24-25`); a failed or cancelled prompt keeps the child session (`:31-32`). PR #213 did not change this file.
- `.deviceOwnerAuthentication` is "biometry or user password": the SDK header (`LocalAuthentication.framework/Headers/LAContext.h`, `LAPolicyDeviceOwnerAuthentication`) says that if Touch ID is not available, not enrolled or locked out, "the user is asked for password right away". So a Mac without Touch ID asks for the Mac password; an iPhone or iPad with Touch ID (not Face ID) asks for Touch ID; Apple Vision Pro asks for Optic ID; each falls back to the passcode or password.
- In-app words since PR #213: `PlatformCopy.deviceOwnerAuthentication` (`DentalCore/Services/PlatformCopy.swift:48-57`) — "Face ID or the device passcode" (iOS), "Touch ID or your Mac password" (macOS), "Optic ID or the device passcode" (visionOS); read by the Household footer (`HouseholdViews.swift:122-127`). Purpose strings: `INFOPLIST_KEY_NSFaceIDUsageDescription` (Face ID) and `INFOPLIST_KEY_NSFaceIDUsageDescription[sdk=xr*]` (Optic ID) in `OmniDent.xcodeproj/project.pbxproj:891-892`, `:955-956`.
- Household settings is reachable on iPhone, iPad, Mac and Vision Pro (`AppSurfaces/Features/More/MoreHubView.swift:81`, `AppSurfaces/Features/Settings/SettingsView.swift:166`; no platform guard).
- Policy sentences corrected: short version (household bullet), section 3 "Household mouths stay on this device" (per-device list; "iOS cannot lock" → "the system cannot lock", "no passcode" → "no passcode or password"), section 12 child-profile bullet, section 19 new entry. Health policy: children's table, photographs row; changes entry.

NOTE FOR THE APP
- `PlatformCopy.deviceOwnerAuthentication` on iOS says "Face ID or the device passcode", and the iOS purpose string names Face ID only, while an iPad or iPhone with Touch ID asks for Touch ID. The policy names both; the app's iOS string is narrower than the device's behaviour.

LEFT AS HISTORY
- The 20 September 2026 entries in both "Changes" sections still say "Face ID or the device passcode"; they are dated history, superseded by the 27 September entries.


## 2026-09-27 (later) — Mac, Apple Vision Pro and Apple TV say what those devices do

Owner approved this wave 2026-09-27 ("finish all pending work"). Code read from OmniDent `main` at 7f37598 (merge of PR #216 `fix/platform-release-2026-09-27`), which also contains PR #213 (TV About tab). Both policies keep the date 27 September 2026 (the TV About's pinned "effective 27 September 2026" line, `OmniDentKit/Sources/Knowledge/LivingRoomLegalCopy.swift`, stays true); the short version is unchanged.

CORRECTED — "The same list is offered on iPhone, iPad, Mac and Apple Vision Pro" (section 4 model table)
- `OmniDentCatalog.offersDownload(of:hasPhotoCapture:)` (`OmniDentKit/Sources/Intelligence/AI/OmniDentCatalog.swift:75-77`) returns false for a vision entry where `OmniPlatform.hasPhotoCapture` is false; `hasPhotoCapture` is `#if os(iOS)` only (`AppSurfaces/App/PlatformCapabilities.swift:31-37`; `SUPPORTS_MACCATALYST = NO`, so the Mac is native macOS). Recommended Models applies it (`AppSurfaces/Features/Settings/AIModelManagementView.swift:107-115`); "Your Downloaded Models" does not (`:121-134`), so a SmolVLM already on disk can still be deleted. "Use for analysis" (`:266-268`), the Settings "Vision (analysis)" row (`Features/Settings/SettingsView.swift:228-237`) and the launch prewarm (`AppSurfaces/App/OmniDentRoot.swift:145`) are gated the same way.

CORRECTED — "Download over cellular … with it off, a download waits for Wi-Fi" (section 4 table; section 10 "whether downloads may use cellular")
- `MeteredDownloadCopy` (`Intelligence/MLX/Download/InferencePreferences.swift:64-93`): `#if os(iOS)` "Download over cellular" / "wait for Wi-Fi"; otherwise (Mac, Vision Pro) "Download over Personal Hotspot", hint "When off, model downloads wait for a network that is not a Personal Hotspot.", held line "Waiting for a network that is not a Personal Hotspot." The Settings switch reads it (`AIModelManagementView.swift:93-97`). Same flag (`allowsCellularDownload`), off by default.

CORRECTED — "Pro adds full photo history" (section 2, twice; health policy "Pro unlocks full photo history")
- `PaywallCopy.bullets(hasPhotoCapture:)`, `checklist(hasPhotoCapture:)`, `settingsFooter(hasPhotoCapture:)` (`DentalCore/Services/ProCatalog.swift:196-248`) drop "Full photo history." and the photo rows where there is no camera; the Mac/Vision footer reads "Pro unlocks reminder cadence and a print-ready visit sheet." Read by `PaywallSheet.swift:101`, `:282` and `SettingsView.swift:148`.

CORRECTED — cancel path gave iOS only (section 2)
- `PlatformCopy.cancelSubscriptionPath` (`DentalCore/Services/PlatformCopy.swift:42-48`): macOS "the App Store app → your name → Account Settings → Subscriptions → Manage"; otherwise "Settings → your name → Subscriptions" (iPhone, iPad, Vision Pro). Paywall terms line `PaywallSheet.swift:415-421`. Apple support 118428 gives the same Mac steps.

CORRECTED — "The Apple TV app has three tabs" (section 6)
- `App/OmniDentTV/OmniDentTVApp.swift:61-85`: Continue, Library, Ask, About. `TVAboutView` (`:378-415`) shows `LivingRoomLegalCopy` constants only — disclaimer, the policy's short version, the policy/health-policy/contact lines, the terms line and EULA URL as text (tvOS opens no link); no fetch.

ADDED — Share care summary on Mac and Vision Pro (section 3)
- `DentalCore/Services/DentistShareCopy.swift` (new in #216): "Share your care days." where there is no camera; the Mac panel says "A one-page PDF of your care days" or "A text summary of your care days". Sheet: `Features/Care/DentistShareView.swift:150-181`.

LEFT AS HISTORY
- The 23 September entries in both "Changes" sections say the three models were offered and that downloads wait for Wi-Fi unless you allow cellular; they are dated history.


## 2026-09-27 (third) — Sign in with Apple moves the iCloud Sync switch

Owner: "fix all the next-update items now" (2026-09-27). Code read from OmniDent `main` at e3b50af (merge of PR #218 `fix/next-update-2026-09-27`).

CORRECTED — "Sign in with Apple is optional. It does not change what syncs." (short version; section 5 said only that sync does not depend on it)
- Signing in turns the switch on: `AppleAccountHeader.handleSignInWithAppleResult` calls `service.configure(enabled: true)` and `ContinuityBridge.syncSwitchChanged()` after storing the identifier (`AppSurfaces/Features/CloudSync/CloudSyncFeature.swift:353`). Signing out calls `configure(enabled: false)` (`:377`).
- `configure(enabled:)` (`Persistence/CloudSyncService.swift:164`) is the same function the Settings toggle "Enable iCloud Sync" calls (`CloudSyncFeature.swift:94`); it sets the one `userEnabledSyncKey` default. So what syncs is the same whichever turned it on: the `CloudSyncAllowList` record and the continue note (section 6).
- The toggle has no sign-in condition, and the switch defaults to on when the key is unset (`CloudSyncService.swift:157-160`): sync can be turned on without signing in.
- The in-app caption now says the same (`CloudSyncService.signInCaption`, `:407`, OmniDent PR #218).

CASCADE — the sentence is in "The short version"
- OmniDent's Apple TV About tab prints the short version (`Knowledge/LivingRoomLegalCopy.swift`, `privacySummary[8]`); it is updated in the same wave (OmniDent `fix/mac-child-session-copy-2026-09-27`).
- App Store Connect's "Apple TV Privacy Policy" field carries the same short version; the owner updates it (Connect is not written from here).


## 2026-10-07 — the photo-journal widget line, single photos without a view, and Delete All's two gaps

Owner: "Implement all your recommendations" (2026-10-07). Both policies re-dated 7 October 2026; terms.md unchanged (still 27 August 2026). Code read from OmniDent `origin/main` at 48982dc (merge of PR #240; includes PR #238 `d5a8328` and PR #239 `79770f5`), plus the uncommitted fix on `fix/privacy-policy-2026-10-07` (`Persistence/MovedAsideStore.swift`, `AppDataService.swift`, `AppContainerView.swift`, `DeleteAllAftermath.swift`, `CareCompetitiveFeatures.swift`). Every finding was confirmed by a second reviewer before it was applied.

CORRECTED — "care-status line" (main policy sections 1 and 7; health policy App Group care snapshot row)
- The widget is `CareStatusWidget` with display name "Photo journal" and description "Same-spot photos and the care you logged." (`App/OmniDentWidget/CareStatusWidget.swift:95-110`). It shows `liveLine ?? "Keep one photo"` (`:15-17`; `CareWidgetShared.swift:50`) and reads only `statusLine` and `tapAction` from `care.widget.snapshot.v1` (`CareWidgetShared.swift:27-45`).
- The host writes the line from the active mouth's photos: `JournalGlanceSnapshot.save` (`AppSurfaces/Features/Home/HomePhotoJournalViews.swift:291-317`, `fetchRecentScans(limit: 500)` plus `compareSpotKeys`) → `CareWidgetSnapshot.build` (`DentalCore/Services/CareCompetitiveFeatures.swift:123-153`) → `JournalGlanceCopy.line` (`DentalCore/Services/PhotoJournalCopy.swift:205-225`): "Same spot · Last photo <MMM d>", "Last photo <MMM d>" or "No photos yet", plus ". You're set for today" only when today's care is logged. Callers: `HomeView.swift:430`, `DoHubView.swift:293`, `CareSessionView.swift:574`.
- "Same spot" = `SameSpotCompare.pair(frames:)?.sameSpot` (`DentitionKit/SameSpotCompare.swift:82-133`), where a frame's spot is its user view tag, else a recorded set slot that is not the old guessed Smile (`JournalSpot.key`, `:33-51`; `Persistence/CaptureSessionStore.swift:184-208`).
- Tap: `"startCapture"` when there is no photo and `OmniPlatform.hasPhotoCapture`, else `"openJournal"` (`CareCompetitiveFeatures.swift:140`); `AppTabCoordinator.handleWidgetLogCare` opens capture or the You tab (`AppSurfaces/App/AppTabCoordinator.swift:296-316`; `presentCapture` is guarded by `hasPhotoCapture`, `:140-143`). The widget target is built for iOS, macOS and visionOS (`OmniDent.xcodeproj/project.pbxproj:1023`, `:1071`); OmniDent on the Mac and Vision Pro keeps no photos, so the widget it puts there never carries a photo date. A Mac that shows the iPhone's widgets shows the iPhone's line (review round below).
- On-device only; `NSPrivacyCollectedDataTypes` unchanged in both app and widget manifests. No new category, source, purpose or recipient.

CORRECTED — "the view of your mouth it is filed under" for every photo (main policy section 3)
- `CaptureSessionStore.attachJournalScan` (`Persistence/CaptureSessionStore.swift:151-180`, PR #238) files a single photo with `viewSlot: nil`; at the baseline e3b50af it used `.smileFrontal`. Older single shots keep their stored Smile slot, which compare treats as no view (`guessedSmileSessionIDs`, `:212`). Policy now says a photo taken as part of a set is filed under the set's view, one taken on its own is not, and earlier versions filed it as Smile.

FIXED IN THE APP, THEN DESCRIBED — Delete All left the moved-aside database (main policy section 10 removes list; health policy right-to-delete paragraph)
- Pre-existing since ad5330b (2026-08-17): when `default.store` cannot open, `AppContainerView.openOrRecoverPrimaryContainer` moves it and `-wal`/`-shm` to `default.store.corrupt-<stamp>` in Application Support. Nothing on the Delete All path removed it.
- Fix: `deleteAllUserData()` step 11 `purgeMovedAsideStores(&failures)` (`Persistence/AppDataService.swift:1577`, `:1732-1751`) removes only regular files matching `MovedAsideStore.isMovedAsideFile` (`Persistence/MovedAsideStore.swift`); a file it cannot remove is a failure, shown as "Could not delete everything" (`Features/Settings/SettingsView.swift:556-590`). The quarantine names the file through the same type (`AppContainerView.swift:288-291`). Both delete paths call `deleteAllUserData()` (`SettingsView.swift:556`, `Features/CloudSync/CloudSyncFeature.swift:277`). The banner now ends "Delete All Scans & Data in Settings removes it." (`AppContainerView.swift:140`).
- Tests (stage 1): `MovedAsideStoreDeletionTests`, `MultiWindowStoreTests.deleteAllFindsExactlyWhatTheQuarantineMoved`, `PrivacyFixesContractTests.deleteAllRemovesTheMovedAsideStoreAndRedrawsTheWidget`.
- The policy said section 10 listed "the few things it leaves"; that list was incomplete before this fix. Both "Changes" sections say so.

FIXED IN THE APP, THEN DESCRIBED — the widget kept its last line after Delete All (MISSED-1)
- `DeleteAllAftermath.run()` now calls `CareWidgetSnapshotStore.reloadWidget()` (`AppSurfaces/App/DeleteAllAftermath.swift:37`; `CareCompetitiveFeatures.swift:199`, `WidgetCenter.shared.reloadTimelines(ofKind: "CareStatusWidget")`) after the App Group purge. The redraw reads an empty suite ("Keep one photo") or a fresh "No photos yet" snapshot; either way no photo date. A reload is a request to WidgetKit, so the policy says "asks the system to redraw".

CASCADE
- Apple TV About: `LivingRoomLegalCopy.privacyEffective` now reads "effective 7 October 2026"; the short version is unchanged, so `privacySummary` is unchanged (`OmniDentKit/Sources/Knowledge/LivingRoomLegalCopy.swift:36-37`; pinned by `PlatformWaveContractTests`). App Store Connect's "Apple TV Privacy Policy" field carries the same text; the owner updates it.
- No in-app notice: the policy promises one for a new destination, category, third party, change to what syncs, or advertising/analytics. None of these is one, and the app shows none.

LEFT AS HISTORY
- The 20 September 2026 entry in the main policy's section 19 still says "the Home Screen widget's care-status line"; it is dated history, superseded by the 7 October entry.

STILL OPEN (not changed here)
- Terms section 2 still says "It is not a diagnosis, it is not a medical device", while both policies make no blanket claim. No change in this range made it false; the owner may want the terms aligned.
- The hub page's OmniDent card still links only /privacy/omnident/ (RCW 19.373.020(1)(b) wants the health-data policy linked distinctly); that is the generator's hub, outside `src/omnident/`.
- `APP_STORE_CONNECT_SETUP.md` still lists an "OmniDent Plus" group and "Family Sharing ❌ NO"; the shipping `OmniDent.storekit` has three family-shareable Pro products.

### Review round, 2026-10-07

A second reviewer read the change above; each item was re-checked against the code before it was applied.

CORRECTED — "a Mac or Apple Vision Pro keeps no photos, so there it never shows a photo date" (main policy section 7), "nothing leaves your device" (main policy section 19), "stays on your device" (health policy 7 October entry)
- `CareStatusWidget` is an `AppIntentConfiguration` with `.supportedFamilies([.systemSmall, .systemMedium])` and no `.disfavoredLocations` (`App/OmniDentWidget/CareStatusWidget.swift:101-110`), so on macOS 14 and later a Mac can show the iPhone's widget, which the iPhone draws and the system passes to the Mac. That line can carry the iPhone's photo date.
- OmniDent's own Mac and Vision Pro widget still never shows a photo date: only iOS code creates a `Scan` (`CaptureKit/CameraViewModel.swift` → `saveRawPhoto`, and `Features/Capture/CameraCaptureView.swift` → `attachJournalScan`, both under `#if os(iOS)`), and `OmniPlatform.hasPhotoCapture` is false off iOS (`PlatformCapabilities.swift:31-37`).
- Section 7 now limits the claim to OmniDent's own widget on those devices and says what a Mac showing the iPhone's widgets shows. Section 19 and the health policy's 7 October entry say "OmniDent sends nothing off your device for it". The health policy's "Where this data lives" gets a Mac bullet, so that list stays complete.
- Checked and not affected: the care-session Live Activity. Its compact and minimal presentations are an icon and the timer (`App/OmniDentWidget/CareSessionLiveActivity.swift:66-75`), so the Watch Smart Stack and a Mac menu bar, which use them, show no name.

REWORDED — "the view a set of photos took them for" (main policy section 7) → "the view the set of photos asked for when you took them", matching section 3 (`JournalSpot.key`, `DentitionKit/SameSpotCompare.swift:33-51`).

COMPLETED — App Group care snapshot row (health policy): adds `ctaLine`, "Open OmniDent" or `CareSessionEngine.startTodayCTA` ("Tonight's two minutes"), built from `careCompletedToday` (`CareCompetitiveFeatures.swift:145-147`). The widget does not read it (`CareWidgetShared.swift:27-34`).

ADDED TO "IT LEAVES" — the store the quarantine could not move (main policy section 10; health policy "What it leaves")
- When `moveItem` fails, the error is only logged (`AppContainerView.swift:291-301`), the reopen at the same URL fails, and the app runs on the in-memory container with `isEphemeral: true` (`:319-330`). The unreadable `default.store` stays under the live name, and Delete All works only through the in-memory store; `MovedAsideStore` matches only `.corrupt-<stamp>` names. A later launch either opens the file (Delete All then reaches its records) or moves it aside (Delete All then removes it).
- Photo files do not linger in that case: `repairOrphanedScanFiles()` runs about 800 ms into every launch (`AppSurfaces/App/RootView.swift:173-178`) and removes every JPEG in `Documents/Scans` with no `Scan` record in the open store (`Persistence/AppDataService.swift`, `repairOrphanedScanFiles`).

VERIFIED — `bash scripts/check-ios-build.sh` (with `KNOWLEDGE_REFRESH=off`, so the scheme pre-action refreshed no packs) compiles the app, the widget extension and the Watch app for the simulator with the stage-1 fix. Package-resolution noise in the app project's `Package.resolved` was restored.

STILL OPEN (owner)
- The terms nit above is a legal decision, not a factual correction, and is left for the owner.

### Final check, 2026-10-07

Every new or changed sentence in both policies was re-read against the OmniDent worktree (`fix/privacy-policy-2026-10-07` on 48982dc), including the stage-1 app fix.

REWORDED — main policy section 10 "removes" list: the moved-aside database item now follows "the settings store behind them (…)" instead of preceding it, so "them" again refers to the records listed before it, not to the old database. No change in meaning.

VERIFIED — the Delete All fix removes only moved-aside store files
- `MovedAsideStore.files(in:)` lists Application Support as the file manager resolves it (`URL.applicationSupportDirectory` in the app, which is inside the app's sandbox on every platform; `OmniDent-macOS.entitlements` sets `com.apple.security.app-sandbox`) and keeps only regular files named `default.store.corrupt-<stamp>`, `…-wal` or `…-shm`, where `<stamp>` has exactly the shape `9999-99-99T99-99-99Z` in ASCII digits. The quarantine names files through the same type, and older builds wrote the same name (`ISO8601DateFormatter` with `:` replaced by `-`).
- Under `swift test`, every test that reaches `AppDataService` carries `.isolatedDefaults` (enforced by `TestDefaultsIsolationContractTests`), which binds `OmniDentContainerPaths.fileManagerOverride` to the test's own folder, so the purge never lists the developer's real Application Support. `OmniDentTests.swift`, whose suite has no trait, is excluded from its target in `Package.swift`.
- Mutation runs: dropping the stamp check, dropping the regular-file filter, or dropping `CareWidgetSnapshotStore.reloadWidget()` from `DeleteAllAftermath.run()` each turned `MovedAsideStoreDeletionTests` or `PrivacyFixesContractTests` red; the originals were restored byte for byte.
- `bash scripts/check-ios-build.sh` (with `KNOWLEDGE_REFRESH=off`) passes again on the final tree, and the targeted kit suites pass (648 Swift Testing tests). The app project's `Package.resolved` noise it left was restored.

VERIFIED — the rare unmoved-store case (`AppContainerView.swift:288-330`): when `moveItem` fails and the reopen fails, the app runs on the in-memory container with `isEphemeral: true` and the banner reads "running on temporary storage"; `default.store` keeps its live name, which `MovedAsideStore` never matches. A later launch either opens the file or moves it aside, so the policies' advice is true.

VERIFIED — Apple TV: `LivingRoomLegalCopy.privacySummary` equals the published short version paragraph for paragraph (bold dropped), and `privacyEffective` reads "effective 7 October 2026", pinned by `PlatformWaveContractTests`.

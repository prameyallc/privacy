# OmniSalub — data-flow audit

AUDIT BASIS: /Users/sbkoth/work/Omni/OmniSalub — docs/REGULATORY.md, ISSUES.md (SALUB-001/004/005/010/011/012/013/059/062), PRIVACY_POLICY.md, App/OmniSalub/PrivacyInfo.xcprivacy, App/OmniSalubMac/PrivacyInfo.xcprivacy, both .entitlements, App/OmniSalub/Info.plist, App/OmniSalub.xcodeproj/project.pbxproj, CompanionKit/Package.swift, and the Swift sources. Where docs and code disagreed I trusted the code.

NETWORK EGRESS — the complete list, verified by grep (URLSession/NWConnection/CKContainer/HKHealthStore/AVCapture/PHPicker/ASAuthorization/GoogleMobileAds/huggingface across CompanionKit/Sources and App/):
1. huggingface.co. CompanionKit/Package.swift declares mlx-swift-lm, swift-huggingface, swift-transformers. CompanionKit/Sources/Intelligence/LocalModelStore.swift:445+ `HubLocalModelDownloader.download` builds a `HubClient(cache:)` and calls `client.downloadSnapshot(of: repoID, to:, revision:, matching: [], progressHandler:)`. repoID comes from LocalModelCatalog: `mlx-community/Qwen3-0.6B-4bit`, revision `main`, ~400 MB, minimum free disk 600 MB. Triggered ONLY by `startDownload()`, which is wired to an explicit Settings action — there is no auto-download. The request carries the repository id and the device IP; no health data, no user content, no identifier of ours. The Xet trait is deliberately disabled (Package.swift comment), so transfers go over URLSession/LFS.
2. Apple CloudKit private database, preferences only, and ONLY if the user turns on "Sync settings with iCloud". `CloudSyncConsent.hasConsented` defaults FALSE (Persistence/SyncedPreferencesStore.swift:50). StoreStack.swift:65 only builds the synced container when consent exists. StoreSchemas.synced = [StoredPreferences] and the CloudKit-mirrored property allowlist is exactly {id, themePreference, guidelineSet, onboardingCompleted, biometricLockEnabled, updatedAt}; `forbiddenSyncedPropertySubstrings` bans observation/symptom/escalation/audit/pack/diagnosis/medication/glucose/systolic/diastolic/weight/reading/suppressFood/disordered/calorie, asserted by CloudKitBoundaryTests.
3. Apple's own OS services the user already uses: HealthKit (device-to-device via Apple), Siri (App Intents phrases), iCloud Backup, MetricKit/"Share With App Developers".
No Prameya server exists. No account, no login, no analytics SDK, no ad SDK, no crash-reporting SDK, no attribution SDK. Grep for CLLocation, AVCaptureSession, PHPickerViewController, PhotosUI, AuthenticationServices, GADBanner, ATTrackingManager, StoreKit, SFSpeechRecognizer returned ZERO hits.

HEALTHKIT — this is the biggest divergence from the old policy. `LiveHealthKitGateway.requestReadAuthorization` and `requestAuthorization(read:write:)` both discard the caller's metric list and request `allReadableTypes()` — the FULL ungated readable set (comment: "ALWAYS the full ungated set — not the caller's subset"). That is ~90 quantity types (vitals, body, glucose/insulin/blood alcohol, spirometry, activity, mobility, running/cycling, hearing, ~20 nutrition types incl. sodium/potassium), plus `allReadCategoryIdentifiers` (sleep, stand hours, mindful sessions, high/low heart rate and irregular rhythm events, audio-exposure events, toothbrushing, handwashing, AND the reproductive-health family: menstrual flow, intermenstrual bleeding, irregular/infrequent/prolonged cycles, ovulation test, pregnancy test, progesterone test, cervical mucus, contraceptive, lactation, pregnancy, sexual activity), plus the 20 mapped symptom categories, plus characteristics (date of birth, biological sex, blood type, Fitzpatrick skin type, wheelchair use, activity move mode), plus workouts, ECG and audiograms. iOS shows one sheet with per-type toggles, so the user decides what is actually granted. WRITE is a tight allowlist: `writableQuantityIdentifiers` = systolic BP, diastolic BP, heart rate, body mass, height, blood glucose, oxygen saturation, plus the 20 exactly-equivalent symptom categories. Qualified symptom flags (e.g. waking_breathless, breathlessness_on_methotrexate) are deliberately never written.
GATED AND OFF: `LiveHealthKitGateway.medicationsCapabilityEnabled = false` and `clinicalRecordsCapabilityEnabled = false`; the health-records entitlement is deliberately omitted from OmniSalub.entitlements. `refreshMedications` is called at launch but fails closed with `.indeterminate(reason: .capabilityNotGranted)`. So THE SHIPPING BUILD READS NO MEDICATIONS, NO DOSE EVENTS AND NO CLINICAL RECORDS.

LOCAL STORAGE. Two SwiftData stores in Application Support (StoreContainers.swift):
- PHI store companion-health.store — StoredObservation, StoredSymptomReport, StoredEscalationEvent, StoredAuditEvent. Built with `cloudKitDatabase: .none` explicitly (the SwiftData default is `.automatic`, and the app carries the CloudKit entitlement, so this is load-bearing). StoreProtection.protect applies FileProtectionType.complete on iOS and `isExcludedFromBackup = true`, to the main file AND the -wal/-shm sidecars.
- Preferences store companion-preferences.store — the five non-health fields above.
Also UserDefaults: HealthKit ingest anchors, inference preferences, cloud-sync consent flag, local preference mirror. Keychain keys use kSecAttrAccessibleWhenUnlockedThisDeviceOnly (Persistence/Encryption.swift:76).

WIDGET / LOCK SCREEN. WidgetSnapshotBridge writes widget.todaySnapshot.v1.json into App Group container group.legal.prameya.omnisalub. TodaySnapshot fields: pre-formatted headline (e.g. "132/84"), accessibility label, recordedAt, stratum label ("Morning"/"Evening"), nextAsk, dataIsIndeterminate. That IS health data, on device, never CloudKit. NOTE: grep shows StoreProtection/isExcludedFromBackup is applied ONLY to the PHI store — the widget snapshot file has no backup exclusion and no explicit protection class, so it can be swept into an iCloud device backup. Live Activity (MeasurementActivityAttributes.ContentState) carries metric name, headline, readings-taken counts, a guidance line and a deadline — no values — and is rendered locally; there is no push entitlement (aps-environment deliberately absent).

APP INTENTS / SIRI. CompanionIntents ships LogBloodPressureIntent, CheckMedicationsIntent and StartMeasurementSessionIntent with AppShortcut phrases, wired in OmniSalubApp.init.

ASSISTANT. Intelligence target, MLX only. AssistantContextBuilder assembles observations, symptoms, condition names, guideline set, medication lines and any open escalation into a prompt block and states "This string is only fed to the on-device (local MLX) generator." The three-tier ConsentState exists, but InferencePreferences.asConsentState hard-codes privateCloudComputeEnabled=false and externalProviderEnabled=false, so PCC and third-party inference are NOT reachable in this build. AssistantGuard/RefusalSet run before and after generation.

TELEMETRY. The Telemetry product IS linked into the iOS app (project.pbxproj), but the only import in App/OmniSalub/OmniSalubApp.swift is for `MetricKitBridge.shared.start()`. Grep found no call site anywhere that records a TelemetryEvent — the closed-enum event vocabulary and LocalTelemetrySink (180-day retention, on-device) exist but are not switched on. MetricKitBridge counts payloads and discards them; App/OmniSalubMac/OmniSalubMacApp.swift does not start it.

NOT SHIPPED. `Sync` (multi-device sync engine) — 0 references in project.pbxproj. `Instruments` (validated questionnaires) — also not linked into any app target.

EXPORT. Export target produces PDF (CoreGraphics), CSV (with a provenance header) and a FHIR R4 bundle, handed to the system share sheet. Contains health data by design; destination is the user's choice; nothing is uploaded by the app.

OTHER. Audit log is a SHA-256-chained closed-enum event log (kind + bounded subject, never a value), local, viewable at Settings → Activity log, and Settings has "Delete all data on this device". App lock uses Face ID/Touch ID (NSFaceIDUsageDescription). Both PrivacyInfo.xcprivacy files declare NSPrivacyTracking=false, empty NSPrivacyCollectedDataTypes, and only NSPrivacyAccessedAPICategoryUserDefaults / CA92.1 — the disk-space required-reason API used at LocalModelStore.swift:431 is still undeclared (SALUB-001). Mac target is sandboxed and holds com.apple.security.network.client; iOS holds healthkit, healthkit.background-delivery, the iCloud container, and the App Group.

## Corrections to prior claims

- FALSE: PRIVACY_POLICY.md line 16 — "The app makes no network requests of its own." TRUE: the app makes network requests. CompanionKit/Sources/Intelligence/LocalModelStore.swift:445+ uses HubClient.downloadSnapshot against huggingface.co to fetch MLX model weights when the user opts in, and CloudKit carries preference sync when the user opts in. The correct statement is that no health data, no user content and no identifier is transmitted to Prameya or anyone else — not that no request is made.
- FALSE: PRIVACY_POLICY.md line 125 — "There is no URLSession, no socket, and no third-party SDK anywhere in the code that runs. This is verifiable in the published source." TRUE: CompanionKit/Package.swift declares mlx-swift-lm, swift-huggingface and swift-transformers, and the resolved graph pulls sixteen checkouts including swift-nio, swift-crypto, EventSource and yyjson. Hub downloads go over URLSession. The sentence invited exactly the falsification it claimed to survive.
- SELF-CONTRADICTION: PRIVACY_POLICY.md lines 16/125 versus line 169 ("Installing the local model downloads model weight files only … over the network"). The same document asserted both no network and a network download. The new policy states the download once, precisely, in section 5.1 of the main policy.
- FALSE: PRIVACY_POLICY.md §1.1, "Medicines and doses. If you allow Health access, the app also reads your medication list and your record of doses taken or skipped." TRUE: LiveHealthKitGateway.medicationsCapabilityEnabled is false and the health-records/medications entitlement is deliberately omitted. fetchMedications and fetchDoseEvents fail closed with .indeterminate(reason: .capabilityNotGranted). The shipping build reads no medication or dose data at all. Claiming to read medication data the app cannot read is a disclosure the App Store privacy label would not match.
- UNDERSTATED, MATERIALLY: PRIVACY_POLICY.md §1.2 — the app "reads measurements, a small set of symptom types, and your medication and dose records from Health." TRUE: LiveHealthKitGateway.requestReadAuthorization and requestAuthorization(read:write:) both discard the caller's metric list and request allReadableTypes() — the full ungated readable set: ~90 quantity types, every category type in allReadCategoryIdentifiers (including the reproductive-health family: menstrual flow, intermenstrual bleeding, cycle irregularity, ovulation, pregnancy and progesterone test results, cervical mucus, contraceptive, lactation, pregnancy, sexual activity), the twenty mapped symptom categories, six characteristic types (date of birth, biological sex, blood type, Fitzpatrick skin type, wheelchair use, activity move mode), workouts, ECG and audiograms. The in-app usage string already says "and the rest"; the policy did not. Describing this as "a small set" is the kind of understatement a reviewer catches by opening the permission sheet.
- FALSE / OVERSTATED: PRIVACY_POLICY.md §2 — "We do not: … embed any third-party analytics, crash-reporting, attribution, or advertising SDK" was true, but the surrounding bullet list was presented as proof of "no third-party SDK of any kind" (§ short version, line 16-17). TRUE: there are third-party packages (the MLX/Hugging Face stack). None of them is an analytics, advertising, attribution or crash-reporting SDK, and none transmits user content — which is the accurate and still-favourable statement.
- FALSE, IN CODE COMMENT SHIPPED AS DOCUMENTATION: App/OmniSalubMac/OmniSalubMac.entitlements — "Nothing else in this app makes a network request: there is no URLSession anywhere in the tree, so this entitlement grants CloudKit and nothing more." TRUE: the Mac target links AppSurfaces → Intelligence, so com.apple.security.network.client is also what permits the Hugging Face model download on macOS. The corresponding claim in PRIVACY_POLICY.md §2 ("it is used for nothing else — the app has no code that could open any other connection") is false for the same reason.
- STALE: COMPLIANCE_TODO.md §6 — "No networking anywhere; no third-party dependencies" and "Required-reason APIs: CA92.1 is correct and is the only one needed (no disk-space API use)". Both were true on 2026-08-04 and are false since the MLX work landed. LocalModelStore.swift:431 reads volumeAvailableCapacityForImportantUsageKey. APPLE_COMPLIANCE_MATRIX.md §6 carries the same two now-false bullets under a "verified clean" heading (ISSUES.md SALUB-061).
- PREVIOUSLY FALSE, ALREADY CORRECTED IN-REPO: both PrivacyInfo.xcprivacy files formerly asserted "there is no URLSession … and Package.swift declares no dependencies at all." Those comments were rewritten on 2026-08-08. Recorded here so the owner knows the conclusion ("Data Not Collected") survived but the reasoning behind it changed — a right answer resting on a wrong reason is what gets found in discovery.
- SCOPE ERROR IN THE OLD SHARED POLICY at prameyallc.github.io/edu-app-privacy: it scopes itself to apps with no accounts, no uploads and no health or financial data. OmniSalub reads and writes HealthKit, holds a local health database, exports clinical PDFs/CSV/FHIR, and downloads model files over the network. That policy has never been true of this app and must not be the URL in App Store Connect for it.
- IMPRECISE: PRIVACY_POLICY.md §1.3 and §7 — "Your health data is never stored in iCloud" and "the health database is excluded from iCloud backup." TRUE of the health database (StoreProtection applies isExcludedFromBackup to the store and its -wal/-shm sidecars, and the container is built with cloudKitDatabase: .none). NOT established for the widget's App Group snapshot file, which holds your most recent reading in formatted display form and carries no backup exclusion. Both new policies state the boundary and flag the gap rather than repeating a blanket claim.
- IMPRECISE: PRIVACY_POLICY.md §9 — "we do not collect or receive sensitive personal information, including health information, because the app transmits none to us" offered as the whole CCPA answer. TRUE but incomplete: the same reasoning must not be carried across to Washington's My Health My Data Act, whose definition of "collect" reaches data accessed, processed, derived or inferred — not only received. The new health-data policy says so explicitly and does not claim an exemption (OQ-382 is unresolved).
- MISSING ENTIRELY: the old policy had no Washington My Health My Data Act or Nevada SB 370 content and no separate consumer health data policy, which RCW 19.373.020 requires to be distinct and prominently linked from the homepage (ISSUES.md SALUB-011). That document now exists.
- STALE URLs: PRIVACY_POLICY.md §12 points to https://prameyallc.github.io/OmniSalub/privacy/ and App/OmniSalub/Info.plist sets OHPrivacyPolicyURL and OHSupportURL to the same host path. Those 404 today (ISSUES.md SALUB-003) and are not the new site layout. Correct location: https://prameyallc.github.io/privacy/omnisalub/ , with the health-data policy at https://prameyallc.github.io/privacy/omnisalub/health-data/ .
- CONTACT MISMATCH: PRIVACY_POLICY.md §13 and Info.plist OHSupportEmail give admin@prameya.legal; the publishing brief gives admin@prameya.legal. The new policies use admin@prameya.legal. One of the two must change so the app, the site and the policy agree.
- ACCURATE AND KEPT (verified against code, listed so the owner knows what was preserved rather than rewritten): no Prameya server or backend; no account, login or registration; no advertising, IDFA or App Tracking Transparency; no analytics, crash-reporting or attribution SDK; no location, camera, photo library, microphone or contacts access; health database local-only with cloudKitDatabase: .none, FileProtectionType.complete on iOS and backup exclusion; iCloud settings sync limited to five non-health preference fields and off by default (CloudSyncConsent defaults to false); the Sync module is not linked into any app target; MetricKit payloads are counted then discarded and the Mac app does not use MetricKit; no usage analytics are recorded in this version; the activity log is a closed-vocabulary, SHA-256-chained, value-free local log; exports go only through the user-driven share sheet; keys are Keychain-held with kSecAttrAccessibleWhenUnlockedThisDeviceOnly; HIPAA does not apply; Private Cloud Compute and third-party AI tiers are not enabled or reachable in this build.

## Open questions

- TERRITORY — the GDPR/UK GDPR subsection in the main policy carries an inline TO VERIFY note. docs/REGULATORY.md §7 and blocker B5 recommend setting App Store availability to United States only for 1.0, but ISSUES.md SALUB-064 shows that has not been done. Confirm the App Store Connect territory setting and either trim the GDPR subsection or keep it. Note also that shipping in the EEA raises EU MDR Rule 11 / MDCG 2019-11 and EU AI Act questions (OQ-389) that no privacy policy resolves.
- WIDGET SNAPSHOT BACKUP EXCLUSION — flagged inline in both policies. WidgetSnapshotBridge writes widget.todaySnapshot.v1.json (containing a formatted reading such as "132/84") into the App Group container, and grep confirms StoreProtection / isExcludedFromBackup is applied only to the PHI store. Either apply the exclusion and a protection class in code and delete the TO VERIFY note, or restate the paragraph accurately. Related: ISSUES.md SALUB-059 flags the same gap for the model directory and HubCache (not health data, but a large backup).
- CONTACT EMAIL MISMATCH — the brief gives admin@prameya.legal and both policies use it. The repo uses admin@prameya.legal in PRIVACY_POLICY.md §13, App/OmniSalub/Info.plist (OHSupportEmail), and ISSUES.md SALUB-014. Decide which address is authoritative and make the app, the site and the policies agree, or the in-app support link points somewhere the policy does not name.
- IN-APP POLICY URLs ARE WRONG AND DEAD — App/OmniSalub/Info.plist sets OHPrivacyPolicyURL = https://prameyallc.github.io/OmniSalub/privacy/ and OHSupportURL = https://prameyallc.github.io/OmniSalub/support/. Those 404 today (ISSUES.md SALUB-003, GitHub Pages not enabled) and are not the new site layout. Update to https://prameyallc.github.io/privacy/omnisalub/ and the matching support URL, and add a second Settings link to the Consumer Health Data Privacy Policy at .../omnisalub/health-data/ — MHMDA requires it to be distinctly linked, and REGULATORY.md §4.2 asks for it from within the app as well as the homepage.
- HOMEPAGE PROMINENCE — RCW 19.373.020 requires the consumer health data policy to be published as a link on the homepage. Confirm https://prameyallc.github.io/privacy/ carries a distinct, visible link to the OmniSalub health-data policy (not only to the main policy), and that the OmniSalub main policy page renders its link to it above the fold.
- APP STORE CONNECT PRIVACY ANSWERS MUST MATCH — both PrivacyInfo.xcprivacy files declare NSPrivacyCollectedDataTypes as empty ("Data Not Collected"). That is defensible under Apple's transmission-based definition, but the ASC App Privacy questionnaire answers must say the same thing. Declaring nothing in the manifest while answering "yes, health data" in ASC is a metadata rejection. Re-check after any wave-2 change.
- DISK-SPACE REQUIRED-REASON API STILL UNDECLARED — LocalModelStore.swift:431 reads volumeAvailableCapacityForImportantUsageKey; neither privacy manifest declares NSPrivacyAccessedAPICategoryDiskSpace (ISSUES.md SALUB-001). This does not affect the truth of the policy text, but it is an automated ASC rejection and it sits on the same code path the policy now describes (the Hugging Face download).
- MHMDA SCOPE IS GENUINELY UNRESOLVED (OQ-382) — whether "collect" reaches a developer who never receives the data has no WA AG guidance and no case law. The health policy deliberately does not assert an exemption and describes on-device processing as in scope. Counsel should confirm that posture is the one Prameya wants before publication; the alternative (asserting non-applicability) is cheaper to write and far more expensive to be wrong about.
- HBNR RUNBOOK STILL MISSING (SALUB-010) — coverage is presumed because HealthKit read access satisfies the multiple-sources limb. Neither policy promises a breach-notification process, which is correct as written, but the runbook should exist before launch.
- MEDICATIONS CAPABILITY — both policies state plainly that the shipping build reads no medications or dose records, because LiveHealthKitGateway.medicationsCapabilityEnabled is false. If Apple grants the capability and it is flipped on, BOTH policies must be updated before that build ships (section 2.3 of the main policy and the category table in the health policy), and the in-app CheckMedicationsIntent copy re-checked — it currently exists as an App Intent while the underlying read fails closed.
- AGE RATING AND COPPA — the main policy's children section says the app is age-rated for older teens and adults. ISSUES.md SALUB-021 records that the age-rating questionnaire deadline passed unanswered. Complete it (REGULATORY.md B3 recommends Medical/Treatment Information = frequent → 16+) so the published rating and the policy text agree.
- ASSISTANT TURN LOG (SALUB-013) — REGULATORY.md §6 wants every assistant turn logged with model version and retrieved-context flag. It does not exist yet. If it is added, it is a new local health-adjacent artifact and both policies need a line describing it and a "Clear assistant history" control.
---

## ADDENDUM 2026-08-08 — precise scope of the HealthKit over-request (measured, not estimated)

Measured directly from `CompanionKit/Sources/HealthCore/HealthKitGateway.swift`:

| Kind | Identifiers requested today |
|---|---|
| Quantity | 90 |
| Category | 53 |
| Characteristic | 6 |
| **Total** | **149**, plus workouts, ECG and audiogram object types |

`LiveHealthKitGateway.requestReadAuthorization(for:)` (~line 64) and
`requestAuthorization(read:write:)` (~line 121) both discard the caller's `metrics`
argument and pass `Self.allReadableTypes()`, so all 149 are requested regardless of
which condition pack is active.

### The 14 reproductive-health identifiers currently requested

```
CervicalMucusQuality          Contraceptive
InfrequentMenstrualCycles     IntermenstrualBleeding
IrregularMenstrualCycles      Lactation
MenstrualFlow                 OvulationTestResult
PersistentIntermenstrualBleeding
Pregnancy                     PregnancyTestResult
ProgesteroneTestResult        ProlongedMenstrualPeriods
SexualActivity
```

None of these is referenced by any of the 53 condition-pack manifests in `SCHEMA/packs/`.

### The 6 characteristics currently requested

```
ActivityMoveMode  BiologicalSex  BloodType
DateOfBirth       FitzpatrickSkinType  WheelchairUse
```

`FitzpatrickSkinType` and `BloodType` have no consumer in this codebase.

### What the packs actually consume

The HealthKit-backed metrics referenced across all 53 pack manifests are approximately:
`body_weight`, `systolic_bp`, `diastolic_bp`, `step_count`, `blood_glucose`, `sleep_hours`,
`heart_rate`, `resting_heart_rate`, `walking_speed`, `body_mass_index`, `hrv_sdnn`,
`physical_activity`, `time_in_daylight`, `headphone_audio_exposure`.

Everything else in the packs (`pain_nrs`, `med_adherence`, `stress_nrs`, `rescue_use_count`,
`morning_stiffness_min`, `gdmt_classes_active`, …) is an app-internal metric the user records
directly and has no HealthKit type at all.

**So roughly 15–25 HealthKit types are actually needed against 149 requested — a 6–10× over-request
that includes the most sensitive category in consumer health data.**

### Required fix

1. Narrow `HealthKitTypeMap.quantityIdentifiers`, `readCategoryIdentifiers` and
   `characteristicIdentifiers` to the set the packs genuinely consume. Deleting an identifier from
   the map is the fix; do not keep it and filter later.
2. Honour the `metrics` parameter in both authorization entry points, so the sheet matches the map.
3. Add tests asserting that the requested set contains **no** identifier from the reproductive list
   above, and no `BloodType` / `FitzpatrickSkinType`. This must fail loudly if it ever regresses.
4. The existing comment defending the full-set request describes a real bug (sheet showed less than
   the map claimed). Narrowing the map fixes that bug in the correct direction — record that in the
   comment so the next person does not re-widen it.

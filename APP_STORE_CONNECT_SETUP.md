# App Store Connect Product Configuration Guide

**Generated:** 26 August 2026
**Purpose:** Configure in-app purchase products for all 11 Prameya apps

---

## Overview

This document provides step-by-step instructions for creating subscription and in-app purchase products in App Store Connect for all Prameya apps implementing monetization.

**Apps covered:**
- 4 Health Apps (3-tier: Free → Plus → Premium)
- 3 Education Apps (4-tier: Free → Foundation → Scholar → Lifetime)
- 4 Productivity Apps (variable tiers)

---

## General Setup Steps

### 1. Log in to App Store Connect
- Navigate to: https://appstoreconnect.apple.com/
- Sign in with your Apple Developer account

### 2. For Each App:
1. Select "My Apps"
2. Choose the app
3. Click "Features" tab
4. Select "In-App Purchases" or "Subscriptions"

---

## Health Apps (3-Tier Structure)

### OmniDent

**App ID:** `legal.prameya.OmniDent`
**Subscription Group:** "OmniDent Plus"

#### Create Subscription Group
1. Click "+" next to Subscription Groups
2. Name: "OmniDent Plus"
3. Save

#### Products to Create

**1. OmniDent Plus Monthly**
- Product ID: `legal.prameya.OmniDent.plus.monthly`
- Type: Auto-Renewable Subscription
- Subscription Group: OmniDent Plus
- Subscription Duration: 1 Month
- Price: $9.99 USD (Tier 9)
- Family Sharing: NO (health data is individual)

**2. OmniDent Plus Annual**
- Product ID: `legal.prameya.OmniDent.plus.annual`
- Type: Auto-Renewable Subscription
- Subscription Group: OmniDent Plus
- Subscription Duration: 1 Year
- Price: $99.99 USD (Tier 19)
- Family Sharing: NO

**3. OmniDent Premium Monthly**
- Product ID: `legal.prameya.OmniDent.premium.monthly`
- Type: Auto-Renewable Subscription
- Subscription Group: OmniDent Plus
- Subscription Duration: 1 Month
- Price: $19.99 USD (Tier 19)
- Family Sharing: NO

**4. OmniDent Premium Annual**
- Product ID: `legal.prameya.OmniDent.premium.annual`
- Type: Auto-Renewable Subscription
- Subscription Group: OmniDent Plus
- Subscription Duration: 1 Year
- Price: $199.99 USD (Tier 39)
- Family Sharing: NO

---

### OmniDerm

**App ID:** `legal.prameya.OmniDerm`
**Subscription Group:** "OmniDerm Plus"

#### Products (Same structure as OmniDent)
- `legal.prameya.OmniDerm.plus.monthly` - $9.99/mo
- `legal.prameya.OmniDerm.plus.annual` - $99.99/yr
- `legal.prameya.OmniDerm.premium.monthly` - $19.99/mo
- `legal.prameya.OmniDerm.premium.annual` - $199.99/yr

**Family Sharing:** NO (health data)

---

### OmniSalub

**App ID:** `legal.prameya.OmniSalub`
**Subscription Group:** "OmniSalub Plus"

#### Products (Same structure as OmniDent)
- `legal.prameya.OmniSalub.plus.monthly` - $9.99/mo
- `legal.prameya.OmniSalub.plus.annual` - $99.99/yr
- `legal.prameya.OmniSalub.premium.monthly` - $19.99/mo
- `legal.prameya.OmniSalub.premium.annual` - $199.99/yr

**Family Sharing:** NO (health data)

---

### OmniRx

**App ID:** `legal.prameya.OmniRx`
**Subscription Group:** "OmniRx Plus"

#### Products (Same structure as OmniDent)
- `legal.prameya.OmniRx.plus.monthly` - $9.99/mo
- `legal.prameya.OmniRx.plus.annual` - $99.99/yr
- `legal.prameya.OmniRx.premium.monthly` - $19.99/mo
- `legal.prameya.OmniRx.premium.annual` - $199.99/yr

**Family Sharing:** NO (health data)

---

## Education Apps (4-Tier Structure)

### OmniMathematics

**App ID:** `legal.prameya.OmniMathematics`
**Subscription Group:** "OmniMath Plus"

**CRITICAL: Family Sharing REQUIRED for all products (COPPA compliance)**

#### Products to Create

**1. Foundation Monthly**
- Product ID: `legal.prameya.OmniMathematics.foundation.monthly`
- Type: Auto-Renewable Subscription
- Duration: 1 Month
- Price: $4.99 USD (Tier 4)
- Family Sharing: YES ✓ (REQUIRED)

**2. Foundation Annual**
- Product ID: `legal.prameya.OmniMathematics.foundation.annual`
- Type: Auto-Renewable Subscription
- Duration: 1 Year
- Price: $49.99 USD (Tier 9)
- Family Sharing: YES ✓ (REQUIRED)

**3. Scholar Monthly**
- Product ID: `legal.prameya.OmniMathematics.scholar.monthly`
- Type: Auto-Renewable Subscription
- Duration: 1 Month
- Price: $9.99 USD (Tier 9)
- Family Sharing: YES ✓ (REQUIRED)

**4. Scholar Annual**
- Product ID: `legal.prameya.OmniMathematics.scholar.annual`
- Type: Auto-Renewable Subscription
- Duration: 1 Year
- Price: $89.99 USD (Tier 17)
- Family Sharing: YES ✓ (REQUIRED)

**5. Lifetime**
- Product ID: `legal.prameya.OmniMathematics.lifetime`
- Type: Non-Consumable
- Price: $79.99 USD (Tier 15)
- Family Sharing: YES ✓ (REQUIRED)

---

### OmniPhysics

**App ID:** `legal.prameya.OmniPhysics`
**Subscription Group:** "OmniPhysics Plus"

#### Products (Same tier structure as OmniMathematics)
- `legal.prameya.OmniPhysics.foundation.monthly` - $4.99/mo
- `legal.prameya.OmniPhysics.foundation.annual` - $49.99/yr
- `legal.prameya.OmniPhysics.scholar.monthly` - $9.99/mo
- `legal.prameya.OmniPhysics.scholar.annual` - $89.99/yr
- `legal.prameya.OmniPhysics.lifetime` - $79.99 (non-consumable)

**Family Sharing:** YES (education)

---

### OmniAero

**App ID:** `legal.prameya.OmniAero`
**Subscription Group:** "OmniAero Plus"

#### Products (Same tier structure as OmniMathematics)
- `legal.prameya.OmniAero.foundation.monthly` - $4.99/mo
- `legal.prameya.OmniAero.foundation.annual` - $49.99/yr
- `legal.prameya.OmniAero.scholar.monthly` - $9.99/mo
- `legal.prameya.OmniAero.scholar.annual` - $89.99/yr
- `legal.prameya.OmniAero.lifetime` - $79.99 (non-consumable)

**Family Sharing:** YES (education)

---

## Productivity Apps

### OmniLex

**App ID:** `legal.prameya.OmniLex`
**Subscription Group:** "OmniLex Professional"

**Annual-only subscriptions (no monthly options)**

#### Products to Create

**1. Clerk**
- Product ID: `legal.prameya.OmniLex.clerk.annual`
- Type: Auto-Renewable Subscription
- Duration: 1 Year
- Price: $49.99 USD (Tier 9)
- Family Sharing: NO (individual professional use)

**2. Associate**
- Product ID: `legal.prameya.OmniLex.associate.annual`
- Type: Auto-Renewable Subscription
- Duration: 1 Year
- Price: $149.99 USD (Tier 29)
- Family Sharing: NO

**3. Partner**
- Product ID: `legal.prameya.OmniLex.partner.annual`
- Type: Auto-Renewable Subscription
- Duration: 1 Year
- Price: $299.99 USD (Tier 59)
- Family Sharing: NO

---

### OmniWealth

**App ID:** `legal.prameya.OmniWealth`
**Subscription Group:** "OmniWealth Premium"

**2-tier structure (Free + Premium)**

#### Products to Create

**1. Premium Annual**
- Product ID: `legal.prameya.OmniWealth.premium.annual`
- Type: Auto-Renewable Subscription
- Duration: 1 Year
- Price: $99.99 USD (Tier 19)
- Family Sharing: Consider YES (financial education can be shared)

---

### OmniBuild

**App ID:** `legal.prameya.OmniBuild`
**Subscription Group:** "OmniBuild Pro"

**4-tier structure based on state code access**

#### Products to Create

**1. Basic Annual**
- Product ID: `legal.prameya.OmniBuild.basic.annual`
- Type: Auto-Renewable Subscription
- Duration: 1 Year
- Price: $29.99 USD (Tier 2)
- Features: Federal codes + 1 state
- Family Sharing: Consider YES

**2. Pro Annual**
- Product ID: `legal.prameya.OmniBuild.pro.annual`
- Type: Auto-Renewable Subscription
- Duration: 1 Year
- Price: $99.99 USD (Tier 19)
- Features: 5 state codes
- Family Sharing: Consider YES

**3. Expert Annual**
- Product ID: `legal.prameya.OmniBuild.expert.annual`
- Type: Auto-Renewable Subscription
- Duration: 1 Year
- Price: $199.99 USD (Tier 39)
- Features: All 50 state codes
- Family Sharing: Consider YES

---

### OmniOps

**App ID:** `legal.prameya.OmniOps`
**Subscription Group:** "OmniOps Professional"

**3-tier structure (no free tier)**

#### Products to Create

**1. Professional Annual**
- Product ID: `legal.prameya.OmniOps.professional.annual`
- Type: Auto-Renewable Subscription
- Duration: 1 Year
- Price: $39.99 USD (Tier 3)
- Family Sharing: NO (individual discipline practice)

**2. Practice Annual**
- Product ID: `legal.prameya.OmniOps.practice.annual`
- Type: Auto-Renewable Subscription
- Duration: 1 Year
- Price: $99.99 USD (Tier 19)
- Family Sharing: NO

**3. Firm Annual**
- Product ID: `legal.prameya.OmniOps.firm.annual`
- Type: Auto-Renewable Subscription
- Duration: 1 Year
- Price: $199.99 USD (Tier 39)
- Family Sharing: NO

---

## Subscription Group Settings

For each subscription group:

### Promotional Offers
- Consider 7-day free trial for first-time subscribers
- Consider introductory offer: 3 months at 50% off
- Winback offers for lapsed subscribers

### Upgrade/Downgrade Paths
- Allow upgrades from Plus → Premium (prorate)
- Allow downgrades at end of billing period

---

## Privacy Labels Update

After creating products, update App Privacy section:

### For All Apps with Subscriptions:
1. Navigate to App Privacy
2. Add "Purchase History" under "Data Linked to User"
3. Ensure description states:
   - "Purchase information is used to unlock features"
   - "No health/user content is transmitted" (for health apps)

---

## Product Metadata

For each product, provide:

### Subscription Display Name
- Use tier name (e.g., "Plus", "Scholar", "Partner")

### Description
- Brief feature list
- Value proposition
- What differentiates from lower tiers

### Example (OmniDent Plus):
```
Display Name: Plus
Description: Unlock unlimited scan history, advanced analytics, and professional export formats. Photos stay on-device with enhanced cloud sync for preferences.
```

---

## Testing Checklist

After creating all products:

### Sandbox Testing
1. Create sandbox test accounts in App Store Connect
2. Test purchase flows in each app
3. Verify product loading (displayPrice shows correctly)
4. Test restore purchases
5. Verify subscription status updates
6. Test upgrade/downgrade flows
7. Test cancellation behavior

### Production Verification
1. Submit for review with subscription features enabled
2. Test in TestFlight
3. Verify privacy labels match actual behavior
4. Test on multiple devices/accounts
5. Verify Family Sharing works (where enabled)

---

## Pricing Tiers Reference

Quick reference for Apple's pricing tiers:

| Tier | USD Price |
|------|-----------|
| 2 | $29.99 |
| 3 | $39.99 |
| 4 | $4.99 |
| 9 | $9.99 or $49.99* |
| 15 | $79.99 |
| 17 | $89.99 |
| 19 | $99.99 or $19.99* |
| 29 | $149.99 |
| 39 | $199.99 |
| 59 | $299.99 |

*Price depends on whether it's monthly or annual

---

## Product ID Summary

Quick reference of all product IDs to create:

### Health Apps (4 apps × 4 products = 16 products)
```
legal.prameya.OmniDent.plus.monthly
legal.prameya.OmniDent.plus.annual
legal.prameya.OmniDent.premium.monthly
legal.prameya.OmniDent.premium.annual

legal.prameya.OmniDerm.plus.monthly
legal.prameya.OmniDerm.plus.annual
legal.prameya.OmniDerm.premium.monthly
legal.prameya.OmniDerm.premium.annual

legal.prameya.OmniSalub.plus.monthly
legal.prameya.OmniSalub.plus.annual
legal.prameya.OmniSalub.premium.monthly
legal.prameya.OmniSalub.premium.annual

legal.prameya.OmniRx.plus.monthly
legal.prameya.OmniRx.plus.annual
legal.prameya.OmniRx.premium.monthly
legal.prameya.OmniRx.premium.annual
```

### Education Apps (3 apps × 5 products = 15 products)
```
legal.prameya.OmniMathematics.foundation.monthly
legal.prameya.OmniMathematics.foundation.annual
legal.prameya.OmniMathematics.scholar.monthly
legal.prameya.OmniMathematics.scholar.annual
legal.prameya.OmniMathematics.lifetime

legal.prameya.OmniPhysics.foundation.monthly
legal.prameya.OmniPhysics.foundation.annual
legal.prameya.OmniPhysics.scholar.monthly
legal.prameya.OmniPhysics.scholar.annual
legal.prameya.OmniPhysics.lifetime

legal.prameya.OmniAero.foundation.monthly
legal.prameya.OmniAero.foundation.annual
legal.prameya.OmniAero.scholar.monthly
legal.prameya.OmniAero.scholar.annual
legal.prameya.OmniAero.lifetime
```

### Productivity Apps (4 apps, variable products = 11 products)
```
legal.prameya.OmniLex.clerk.annual
legal.prameya.OmniLex.associate.annual
legal.prameya.OmniLex.partner.annual

legal.prameya.OmniWealth.premium.annual

legal.prameya.OmniBuild.basic.annual
legal.prameya.OmniBuild.pro.annual
legal.prameya.OmniBuild.expert.annual

legal.prameya.OmniOps.professional.annual
legal.prameya.OmniOps.practice.annual
legal.prameya.OmniOps.firm.annual
```

**Total:** 42 in-app purchase products across 11 apps

---

## Critical Family Sharing Requirements

| App | Family Sharing Required? | Reason |
|-----|-------------------------|--------|
| OmniMathematics | ✅ YES | COPPA compliance - must share with family |
| OmniPhysics | ✅ YES | Education - family benefit |
| OmniAero | ✅ YES | Education - family benefit |
| OmniDent | ❌ NO | Health data is individual |
| OmniDerm | ❌ NO | Health data is individual |
| OmniSalub | ❌ NO | Health data is individual |
| OmniRx | ❌ NO | Health data is individual |
| OmniLex | ❌ NO | Professional individual use |
| OmniWealth | Optional | Consider YES for family education |
| OmniBuild | Optional | Consider YES for professionals |
| OmniOps | ❌ NO | Individual discipline practice |

---

## Notes

- All product IDs follow the format: `legal.prameya.{AppName}.{tier}.{period}`
- Subscription groups allow users to upgrade/downgrade within the same app
- Non-consumable (Lifetime) products don't belong to subscription groups
- StoreKit 2 is used across all apps (no StoreKit 1 legacy code)
- All apps use `product.displayPrice` for dynamic pricing (no hardcoded prices)
- Privacy policies at https://prameyallc.github.io/privacy/ already updated with subscription disclosures

---

**End of App Store Connect Setup Guide**

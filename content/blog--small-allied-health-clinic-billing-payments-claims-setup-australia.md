---
title: "Billing, Payments and Insurance Claims for a Small Allied Health Clinic in Australia: The Simple Setup"
description: "The four billing rails a small Australian allied health clinic needs, what HICAPS, Tyro Health, Square and Stripe charge, and how to route them."
image: "https://www.vascue.io/images/blog/small-allied-health-clinic-billing-payments-claims-setup-australia.png"
canonical: "https://www.vascue.io/blog/small-allied-health-clinic-billing-payments-claims-setup-australia"
---

[All articles](/blog)Revenue Cycle

# Billing, Payments and Insurance Claims for a Small Allied Health Clinic in Australia: The Simple Setup

Vascue TeamAugust 28, 20269 min read

![Billing, Payments and Insurance Claims for a Small Allied Health Clinic in Australia: The Simple Setup](/images/blog/small-allied-health-clinic-billing-payments-claims-setup-australia.png)

A small allied health clinic in Australia needs four billing rails: card payments at the desk, on-the-spot private health claiming, Medicare and DVA claiming, and invoicing for NDIS and workers' compensation, and the simplest setup routes all four through the practice-management system so every payment lands against an invoice. Most clinics that feel billing is complicated are running those rails through four disconnected tools and reconciling by eye. The fix is less about which terminal to buy and more about making the PMS the place every payment is recorded.

This guide covers what each rail is, what the main providers charged when we checked their published pricing on 21 August 2026, and a setup a one-to-five practitioner clinic can run without a bookkeeper on site. Fees and MBS figures change; confirm every number on the provider's page before relying on it.

## What Are the Payment Rails a Small Clinic Actually Needs?

Rail

Who pays

How it reaches you

Typical tool

Card payments

Patient

EFTPOS terminal or online link

Tyro, Square, Stripe, HICAPS terminal

Private health claiming

Health fund, gap from patient

On-the-spot claim at the desk

HICAPS terminal, Tyro Health (HealthPoint, no terminal)

Medicare and DVA

Government

Bulk bill or patient claim, or DVA claim

Medicare Easyclaim (terminal) or Tyro Health online

NDIS

Participant, plan manager or NDIA

Invoice or payment request

PMS invoice, myplace provider portal, plan manager

Workers' compensation

State scheme insurer

Invoice per scheme rules

PMS invoice to the insurer or scheme portal

Every row ends in the PMS. If it does not, that row is where reconciliation breaks.

## Card Payments: What Do the Terminals Charge?

Published Australian pricing, checked August 2026:

-   **Tyro**: [1.4% per transaction and $29 per month terminal rental](https://www.tyro.com/payments/in-person/eftpos/), with custom quotes above $20,000 a month in card payments.
-   **Square**: [1.6% per in-person transaction, 2.2% online](https://squareup.com/au/en/pricing), no monthly fee.
-   **Stripe**: [1.7% plus A$0.30 for domestic cards online, and 1.7% plus A$0.10 on Stripe Terminal](https://stripe.com/au/pricing) (the page notes lower pricing from 1 October 2026).
-   **HICAPS terminal**: [$30 per month rental for the primary merchant and up to 1.1% card processing](https://www.hicaps.com.au/products/pricing).

Percentages look close; the difference is the fixed fee on small transactions and whether the terminal also does health-fund claiming. A $90 physio consult on Stripe online costs $1.83; on Square in person $1.44; on Tyro $1.26 plus the rental.

## Private Health Claiming on the Spot: HICAPS or Tyro Health?

**HICAPS** is a [wholly owned subsidiary of National Australia Bank](https://www.hicaps.com.au/). The terminal processes private health fund claims, [Medicare Easyclaim rebates](https://www.hicaps.com.au/partners/government-schemes), and DVA claims through its digital portal. HICAPS Digital (claiming without the terminal) was listed at [1.45% of the approved claim amount and 10 cents per approved invoice](https://www.hicaps.com.au/products/pricing) when we checked; confirm on the pricing page.

**Tyro Health** was formed when [Tyro combined its payments business with Medipass](https://www.tyrohealth.com/about/) and covers Medicare, ECLIPSE, DVA, private health insurers and workers' compensation schemes without a physical terminal. It [integrates with more than 120 practice-management systems](https://www.tyrohealth.com/), including Cliniko, Nookal and Halaxy. Pricing: [eligible claims at $0.14 per claim, capped at $39 per location per month](https://help.tyrohealth.com/en/articles/3671187-tyro-health-online-pricing); card payments at 1.7% plus $0.30 per transaction; NDIS claims listed as free.

Which one depends on your PMS. Cliniko [phased out HICAPS in February 2023](https://help.cliniko.com/en/articles/3397793-process-health-fund-claims-with-healthpoint) and claims through HealthPoint via Tyro Health; [Medicare and DVA also go through a Tyro Health account](https://help.cliniko.com/en/articles/3416732-an-overview-of-medicare-cliniko). Nookal integrates with [Tyro Health for HealthPoint and Medicare Easyclaim](https://www.nookal.com/us/integrations/tyro-health) and with [HICAPS for real-time invoices to NDIS, TAC, WorkSafe Victoria and WorkCover Queensland](https://www.nookal.com/us/integrations/hicaps). If you are choosing a PMS and a claiming provider at the same time, choose them together; see [Cliniko vs Front Desk](/blog/cliniko-vs-front-desk-practice-management-australia) for how claiming differs across systems.

## Medicare: Chronic Condition Management Plans

From 1 July 2025 the GP Management Plan and Team Care Arrangements were replaced by the GP chronic condition management plan. For allied health the rule that matters is unchanged: [a maximum of five services per calendar year](https://www9.health.gov.au/mbs/fullDisplay.cfm?type=item&q=10960) under a plan prepared or reviewed in the last 18 months, with plans made before 1 July 2025 honoured [until 30 June 2027](https://www9.health.gov.au/mbs/fullDisplay.cfm?type=item&q=10960). The physiotherapy item (10960) carried a schedule fee of $74.55 and a benefit of $63.40 at the time of checking. The referral is now [a letter rather than a form](https://www.mbsonline.gov.au/internet/mbsonline/publishing.nsf/Content/Factsheet-Upcoming+changes+to+the+MBS+Chronic+Disease+Management+Framework).

Operationally: record the referral date and the services used per calendar year on the patient file, because the sixth visit is not claimable and the patient should know that before it happens.

## DVA

DVA requires a referral. The [D904 request and referral voucher](https://www.dva.gov.au/about-us/dva-forms/d0904-dva-requestreferral-voucher) is a template; DVA states you do not have to use that exact form as long as the referral includes the listed information. Under the [allied health treatment cycle](https://www.dva.gov.au/providers/information-dental-psychology-allied-health-providers/allied-health-treatment-cycle), a referral is valid for up to 12 sessions or one year, whichever ends first. Claims go through Tyro Health, the HICAPS digital portal, or Services Australia channels.

## NDIS

How you get paid depends on how the participant's plan is managed. The NDIS [guide to getting paid](https://www.ndis.gov.au/providers/pricing-and-payments/payments/guide-getting-paid) sets out three routes: invoice self-managed participants directly; send invoices to the participant's plan manager for plan-managed funding; and submit a payment request through the myplace provider portal for NDIA-managed funding. Payment requests must be [submitted within 90 days](https://www.ndis.gov.au/providers/pricing-and-payments/payments/guide-getting-paid). Registered providers are bound by the price limits in the NDIS Pricing Arrangements, which are [the maximum prices registered providers can charge](https://www.ndis.gov.au/providers/pricing-and-payments/payments/guide-getting-paid).

Note that Cliniko states [NDIS claims cannot be made through Cliniko](https://help.cliniko.com/en/articles/11692657-setting-up-your-cliniko-account-to-help-with-ndis-claiming); it tracks and invoices, and the claim is lodged in the portal or by the plan manager. Nookal's HICAPS integration submits NDIS invoices in real time.

## Workers' Compensation: State by State

Each state scheme publishes its own fee schedule and invoicing rules, so a clinic near a border may be dealing with two:

-   **NSW (icare):** fees are [set by fees orders under the legislation](https://www.icare.nsw.gov.au/practitioners-and-providers/gps-and-treating-doctors/fees-payment-and-processing), and invoices must be submitted to the insurer within 30 days of the service.
-   **Victoria (WorkSafe):** a [physiotherapy fee schedule](https://www.worksafe.vic.gov.au/physiotherapy-services-fee-schedule) with maximum amounts per service category.
-   **Queensland (WorkCover):** [tables of approved item numbers and scheduled maximum fees](https://www.workcoverqld.com.au/service-providers/working-with-workcover/fees).

Invoice from the PMS with the claim number and item numbers the scheme expects, and diarise the 30-day clock where it applies.

## Which Payment Systems Support Multiple Providers in One Clinic?

All of the mainstream ones, with three details to get right:

1.  **Merchant facility per location, practitioner on the invoice.** Tyro Health's claim cap is [per location per month](https://help.tyrohealth.com/en/articles/3671187-tyro-health-online-pricing), not per practitioner, so a five-practitioner clinic pays one cap. Cliniko's plans include [unlimited locations within the practitioner band](https://www.cliniko.com/pricing/).
2.  **Provider numbers.** Medicare and DVA claiming uses each practitioner's provider number for that location on the claim; the PMS stores them per practitioner per location and stamps the right one automatically.
3.  **Settlement reporting by practitioner.** If practitioners are paid a percentage of receipts, the reconciliation export must split payments by practitioner and by rail. Check this in the trial before signing.

## The Simple Setup

For a one-to-five practitioner clinic:

1.  **PMS as the ledger.** Cliniko or Nookal. Every invoice is raised there, every payment recorded there, nothing recorded only on a terminal.
2.  **One claiming provider.** Tyro Health if you are on Cliniko or want no terminal; HICAPS if your front desk is built around the terminal and your PMS integrates with it (Nookal does). Either way, private health, Medicare Easyclaim and DVA go through it.
3.  **One card path for deposits and online payments.** Stripe through the PMS booking page (Cliniko) or the provider's own link, so online prepayments also land on the invoice.
4.  **NDIS and workers comp by invoice from the PMS**, with the 90-day NDIS window and the 30-day icare window on a recurring calendar reminder.
5.  **Accounting sync.** Cliniko [pushes invoices and payments to Xero](https://help.cliniko.com/en/articles/1023891-integrate-cliniko-with-your-xero-account); Nookal and most others offer the same. The bookkeeper reconciles Xero against the bank, not the PMS against a shoebox.
6.  **A weekly 20-minute reconciliation.** Payments received versus invoices outstanding, by rail. The [self-audit in our underpaid-claims guide](/blog/hidden-cost-underpaid-insurance-claims) is the same exercise for insurer remittances.

## What to Look for in Billing and Payment Processing for an Allied Health Practice

-   **Native PMS integration**, so no amount is typed twice.
-   **Claim types covered**: private health, Medicare (bulk bill and patient claim), DVA, NDIS, the state schemes you bill.
-   **Fee structure you can model**: a per-claim fee with a monthly cap (Tyro Health) behaves very differently from a percentage of the claim (HICAPS Digital) once volumes grow.
-   **Settlement timing** into your bank account, confirmed in writing.
-   **Reconciliation exports** by practitioner, by rail, by day.
-   **Multi-location support** without a second subscription.
-   **Support hours** that cover your Saturday clinic.

## FAQ

**How do small allied health clinics simplify billing, payments and insurance claims?** By making the practice-management system the single ledger: one claiming provider for private health, Medicare and DVA, one card path for deposits, NDIS and workers' compensation invoiced from the PMS, and a weekly reconciliation of payments against invoices by rail. The complexity comes from recording payments in four places.

**Do we need a HICAPS terminal?** Not necessarily. Tyro Health processes private health (HealthPoint), Medicare and DVA claims without a physical terminal, and Cliniko has used that route since it phased out HICAPS in February 2023. Clinics on Nookal can use either. A terminal still suits a front desk that prefers tap-and-claim at the counter.

**How many Medicare services can a patient claim under a chronic condition management plan?** A maximum of five allied health services per calendar year, across all allied health providers, under a GP chronic condition management plan prepared or reviewed in the last 18 months. Plans made before 1 July 2025 are honoured until 30 June 2027.

**Can insurance claim reconciliation be automated?** For the government and terminal rails, the PMS and the claiming provider already record each payment against an invoice. For insurer-funded patients, where remittances arrive in batches and rarely match the billed amount, matching still tends to be manual; Vascue's claims automation reconciles remittance lines against invoices per configured payer route, with staff handling the exceptions it flags.

[Contact Vascue](/contact-us) to map your clinic's four rails onto one reconciliation, without sending patient data through the public site.

This article is part of the [Vascue Claims](/claims) cluster. Start with the pillar page for the product overview, then come back for the detail.

Related reading

## Keep reading

-   ![Insurance Portal Automation: How to Automate Payer Portal Work Without Losing Control](/images/blog/human-in-the-loop-insurance-portal-automation.png)
    
    Healthcare AI
    
    ### Insurance Portal Automation: How to Automate Payer Portal Work Without Losing Control
    
    An attended browser workflow can remove re-keying while keeping clinic staff in control of the payer portal, final review, and submission action.
    
    7 min read
    
    [Learn more](/blog/human-in-the-loop-insurance-portal-automation)
    
-   ![The Hidden Cost of Underpaid Insurance Claims (and How Clinics Detect and Recover Them)](/images/blog/hidden-cost-underpaid-insurance-claims.png)
    
    Revenue Cycle
    
    ### The Hidden Cost of Underpaid Insurance Claims (and How Clinics Detect and Recover Them)
    
    Insurers rarely pay exactly what clinics bill. How silent underpayments, unmatched remittances, and never-submitted claims drain clinic revenue, a self-audit checklist to find them, and what insurance remittance automation changes.
    
    6 min read
    
    [Learn more](/blog/hidden-cost-underpaid-insurance-claims)
    
-   ![Insurance Claim Automation for Clinics: From Claim Material to Reconciled Outcome](/images/blog/reduce-clinic-admin-workload-front-desk-ai.png)
    
    Revenue Cycle
    
    ### Insurance Claim Automation for Clinics: From Claim Material to Reconciled Outcome
    
    A practical definition of clinic claims automation: document intake and OCR, connected records, validation, staff review, governed submission, tracking, and reconciliation.
    
    7 min read
    
    [Learn more](/blog/insurance-claim-automation-clinics-hospitals)
    

Part of the [Vascue Claims](/claims) cluster[All articles →](/blog)

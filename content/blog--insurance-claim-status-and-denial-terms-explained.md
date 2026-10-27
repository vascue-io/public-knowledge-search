---
title: "Insurance Claim Status and Denial Terms Explained for Clinic Billing Teams"
description: "What claim statuses like awaiting insurer concurrence, query raised, shortfall, run-out and PR 31 actually mean, and what a clinic billing team should do next."
image: "https://www.vascue.io/images/blog/insurance-claim-status-and-denial-terms-explained.png"
canonical: "https://www.vascue.io/blog/insurance-claim-status-and-denial-terms-explained"
---

[All articles](/blog)Revenue Cycle

# Insurance Claim Status and Denial Terms Explained for Clinic Billing Teams

Vascue TeamSeptember 1, 20268 min read

![Insurance Claim Status and Denial Terms Explained for Clinic Billing Teams](/images/blog/insurance-claim-status-and-denial-terms-explained.png)

A claim rejection is a claim the insurer never adjudicated because it failed validation; a claim denial is a claim the insurer adjudicated and refused to pay. Almost every status word a clinic sees on an insurer or TPA portal is a variant of one of those two states, or a stop along the way to them. This glossary explains the terms billing teams search for most, from "awaiting insurer concurrence" to "PR 31", grouped by what they mean for the next action and the clock that is running.

The terms come from different markets. Indian third-party administrators (TPAs) use "query raised" and "shortfall documents". US remittances carry X12 codes such as PR 31. Singapore's Integrated Shield Plans and Hong Kong's VHIS have their own vocabulary. Clinics that bill international insurers see all of them in one inbox; [our Hong Kong hospital deployment](/blog/patient-communication-ai-hong-kong-hospital-privacy-first-architecture-aws) sits in exactly that mix on the communication side.

## Rejected or Denied: Which One Are You Looking At?

The distinction decides everything that follows. A rejection stops a claim before the payer processes it: a missing field, a malformed member number, a date in the wrong format. Nothing has been decided, so the fix is to correct and resubmit, usually within days. A denial happens after adjudication: the payer has looked at the claim and decided not to pay some or all of it, and the route back is an appeal or a corrected claim with new evidence. [Stedi's guide](https://www.stedi.com/blog/the-difference-between-claim-rejections-and-denials) puts it plainly: a rejection stops a claim before it is adjudicated; denials happen after adjudication.

Why it matters operationally: rejected claims never appear in the insurer's denial statistics and rarely trigger a formal letter, so they disappear into queues unless the clinic tracks them. Denials arrive with a reason code and a deadline.

## Statuses You See While a Claim Is Moving

**Received or intimated.** The payer has logged the claim. Nothing has been checked yet.

**Under review or in process.** Adjudication has started. No action unless the status has not changed for longer than the insurer's published turnaround.

**Query raised (RFI).** The insurer or TPA wants clarification before it can decide. In cashless workflows in India, [Paramount TPA's procedure](https://www.paramounttpa.com/home/CashlessClaimsProcedure.aspx) states that a query to the hospital should ideally be replied to or resolved within 24 hours. Treat a query as a deadline, not a notification.

**Shortfall documents.** In Indian TPA usage this means missing paperwork, not missing money. [Medi Assist's FAQ](https://mediassisttpa.in/faq/) explains that shortfall documents are raised when the documents already sent are insufficient for validation, and gives claimants 10 working days to respond. (In Singapore and Hong Kong, "shortfall" usually means an underpayment; see the money terms below.)

**Pre-authorisation pending, then authorisation letter.** For planned procedures the insurer approves an amount before treatment. Until the letter arrives, the clinic is carrying the risk.

**Interim approval, final approval, settled.** Interim approval covers an estimated bill; the final amount is confirmed at discharge; settled means paid. Only "settled" is money in the bank, and even then it should be reconciled line by line.

**Repudiated.** The insurer's word for denied, common in India and the UK.

## What Does Awaiting Insurer Concurrence Mean?

"Repudiated, awaiting insurer concurrence" is a status shown by Indian TPAs such as Medi Assist. The TPA has recommended a decision, usually a repudiation, and is waiting for the underwriting insurer to confirm it. It is not final. [OneAssure's explainer](https://www.oneassure.in/insurance/health-insurance-guides/claim-rejections-vs-claims-repudiated-in-health-insurance-what-s-the-difference) notes that a claim in this state could still be pending and that the claimant should consult the insurer.

What to do: ask the TPA which document or policy clause drove the recommendation, and answer it before the insurer signs off. Once concurrence is given, the route is a formal appeal, which is slower.

## What Is Claims Repricing?

Claims repricing is a US practice in which an insurer or TPA routes a claim through a network's contracted fee schedule, or a third-party repricing vendor such as MultiPlan (now Claritev) or Zelis, to reduce billed charges to an allowed amount before the claim is adjudicated. [MDClarity's guide to repricers](https://www.mdclarity.com/blog/third-party-repricers-tpas) describes a repricer as a pure pricing service that insurers and TPAs route claims through, typically out-of-network claims.

For a clinic, repricing is where underpayment hides. The remittance says "paid", the allowed amount is lower than the contract, and nobody compares the two. The check is mechanical: compare the repriced allowed amount against the agreement the clinic actually holds, and dispute variances in writing, citing the contract and the difference. The same discipline is covered in [our guide to underpaid claims](/blog/hidden-cost-underpaid-insurance-claims).

## What Does PR 31 Mean on a Remittance?

PR 31 combines two X12 codes. Claim adjustment reason code 31 means, in [X12's wording](https://x12.org/codes/claim-adjustment-reason-codes), "Patient cannot be identified as our insured." The group code PR means [Patient Responsibility](https://x12.org/codes/claim-adjustment-group-codes): the payer has assigned the balance to the patient. Put together, the insurer could not find the patient as a member on the date of service and has declined the claim.

What to do: check the member ID, name spelling, date of birth, dependent link and coverage dates against the insurer's record, then correct and resubmit. Bill the patient only after coverage is confirmed absent. Most PR 31 denials are transcription errors from a photographed card, not uninsured patients.

## What Is a Member Pick Reject?

"Member pick reject" is a payer front-end rejection used by some US clearinghouses and payers. As [ClaimMax's list of clearinghouse rejections](https://claimmaxrcm.com/clearinghouse-rejections-medical-billing-2/) describes it, the payer's member database cannot identify the patient as a covered insured. It is the rejection-stage cousin of PR 31: the claim never reached adjudication. Fix the demographics to match the insurer's record exactly and resubmit.

## What Are Run-Out Claims?

Run-out claims are claims for services incurred during a plan year but submitted or paid after the plan year ends, inside a contractual window. The term comes from US self-funded plans and flexible spending accounts. A typical definition, from [Law Insider's contract clauses](https://lawinsider.com/dictionary/run-out-period), sets the run-out period at 90 days following a plan year. Stop-loss contracts label the arrangement "12/15": twelve months of incurred claims, fifteen months to pay them, as [Strategic Benefit Resources explains](https://strategicbenefitresources.com/self-funding-101/).

Why a clinic should care: when an employer changes TPA or plan, claims for the old plan year have a hard cut-off. Ask the outgoing TPA for its run-out date and file everything from the prior year before it.

## Why Do Claims Get Denied for Verification?

A "verification" denial or rejection means the payer could not validate the member: a name or date of birth that does not match, cover that terminated, a dependent not linked to the policy. Payers are explicit that the match must be exact. [Priority Health's provider notice](https://www.priorityhealth.com/provider/manual/news/billing-and-payment/08-28-2024-upfront-claim-rejections-for-member-mismatch) states that if any of the member details do not match exactly what the payer holds, the claim is rejected.

Prevention is the same everywhere: verify eligibility at booking and again at check-in, and transcribe the insurer's record rather than the patient's description of it. Eligibility is the second of [the twelve denial reasons clinics see most](/blog/why-health-insurance-claims-get-rejected).

## Money Words: Shortfall, Reversal, Recoupment, Deductible, Co-Insurance

**Shortfall (payment sense).** The gap between what the clinic expected under the agreement and what the insurer paid. Detecting it requires matching remittance lines to invoice lines; see [the underpaid-claims guide](/blog/hidden-cost-underpaid-insurance-claims).

**Reversal and recoupment.** A [reversal](https://www.hometownbilling.net/blog/difference-between-medical-billing-recoupment-refund-reversal/) cancels a claim before or immediately after processing. A recoupment is the insurer taking back money it has already paid, usually by deducting it from a later remittance, which is why batch payments need line-level reconciliation.

**Deductible and co-insurance.** Singapore's CPF Board defines the MediShield Life [deductible](https://www.cpf.gov.sg/member/healthcare-financing/medishield-life/what-medishield-life-covers-you-for) as the fixed amount payable before payouts start, once per policy year, after which the patient also pays a percentage of the claimable amount (co-insurance). Hong Kong's [VHIS Standard Plan](https://www.vhis.gov.hk/doc/en/information_centre/e_standard_plan_template.pdf) uses the same two terms with the same meaning.

**As-charged.** A plan that reimburses eligible expenses without a per-item claim limit. Singapore's MOH notes that Integrated Shield Plans covered some costs on an [as-charged basis](https://www.moh.gov.sg/managing-expenses/schemes-and-subsidies/medishield-life/faqs-on-cancer-treatment-financing/) before September 2022; newer plans are more limited, so "as-charged" on an old policy document should not be assumed to still apply.

## Singapore and Hong Kong: LOG, Pre-Authorisation, Deductible

**Letter of Guarantee (LOG).** A letter from an Integrated Shield Plan insurer to the hospital that reduces the cash deposit a patient must pay on admission. Singapore's MOH notes that with an LOG the patient [may be able to reduce the upfront cash deposit](https://www.moh.gov.sg/managing-expenses/schemes-and-subsidies/integrated-shield-plans/comparision-of-integrated-shield-plans/), and lists reasons an LOG is refused, such as an estimated bill below the deductible. Great Eastern adds that an LOG is issued only for [day surgery and inpatient treatment](https://www.greateasternlife.com/sg/en/customer-services/claims/medical-hospitalisation/letter-of-guarantee.html) and does not guarantee a waiver of the deposit. For the clinic, an LOG covers the deposit, not the bill: collect deductible and co-insurance at discharge.

**Pre-authorisation.** MOH describes it as the insurer telling the policyholder the amount covered before treatment. Since the November 2025 rider rules, MOH's [announcement](https://www.moh.gov.sg/newsroom/new-requirements-for-integrated-shield-plan-riders-to-strengthen-sustainability-of-private-health-insurance-and-address-rising-healthcare-costs/) states that the co-payment cap applies only to eligible claims such as panel or pre-authorised claims, with the minimum 5% co-payment unchanged. A non-pre-authorised claim can therefore cost the patient far more, which is a front-desk conversation, not a billing one.

Hong Kong's VHIS uses deductible and co-insurance as defined above; pre-authorisation and LOG wording varies by insurer and plan rather than following one standard template.

## A Triage Table for the Billing Desk

Status or code

Stage

Final?

Next action

Clock

Received / intimated

Pre-adjudication

No

None; note the date

Insurer turnaround

Query raised / RFI

Pre-decision

No

Answer with the exact document requested

Often 24 hours to 10 working days

Shortfall documents (India)

Pre-decision

No

Supply documents

10 working days (Medi Assist)

Member pick reject

Rejection

No

Fix demographics, resubmit

Filing deadline keeps running

PR 31

Denial, patient responsibility

Yes, unless corrected

Verify member details, resubmit or bill patient

Payer appeal window

Awaiting insurer concurrence

Recommended repudiation

Not yet

Contest with the TPA before insurer sign-off

Until concurrence

Repudiated / denied

Adjudicated

Yes

Appeal with evidence

Payer appeal window

Repriced

Adjudicated

Yes

Compare allowed amount to contract, dispute variance

Contract dispute window

Run-out claim

Prior plan year

Cut-off applies

File before the run-out date

90 days typical

Settled

Paid

Yes

Reconcile line by line; watch for recoupment

Dispute window per payer

## FAQ

**What is the difference between a rejected and a denied claim?** A rejected claim failed validation and was never adjudicated, so the fix is to correct and resubmit. A denied claim was adjudicated and refused, so the route back is an appeal or a corrected claim with new evidence. Rejections rarely generate a letter, which is why they need their own tracking.

**What does "awaiting insurer concurrence" mean?** An Indian TPA has recommended a decision, usually a repudiation, and is waiting for the insurer to confirm it. It is not final. Ask the TPA what drove the recommendation and respond before the insurer signs off.

**What should we do when a remittance shows PR 31?** The insurer could not identify the patient as a member on the date of service and has assigned the balance to the patient. Check the member ID, name, date of birth, dependent link and coverage dates against the insurer's record, correct the claim and resubmit. Bill the patient only once coverage is confirmed absent.

**Can claim status tracking be automated?** The status check itself can be, when the insurer offers a portal or an electronic channel: a system can poll each claim, map the insurer's wording to a shared set of states, and queue the ones that need a human response by deadline. Vascue's claims automation does this per configured payer route, with staff keeping the submission and every appeal; the mapping of each insurer's vocabulary is set up during onboarding.

[Contact Vascue](/contact-us) to map your payers' status vocabulary onto one triage queue, without sending patient data through the public site.

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

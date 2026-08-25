---
title: "Insurance Claims Automation FAQ | Vascue"
description: "Direct answers about Vascue Claims, document uploads, OCR, integrations, payers, human review, security, and availability."
canonical: "https://www.vascue.io/claims/faq"
---

Claims FAQ

# Direct answers about insurance claims automation.

How Vascue Claims works with connected records, document uploads, OCR, practice-management systems, payer channels, clinic staff, and patient data, and what a design-partner onboarding involves.

[See the product overview](/claims)[Read the claims automation guide](/blog/insurance-claim-automation-clinics-hospitals)[Security and privacy](/security)

Search claims questions

AllProduct & workflowDocuments & OCRIntegrationsPayers & regionsHuman review & controlsSecurity & dataAvailability & onboarding

35 answers

## Product & workflow

8

What is Vascue Claims?+−

Vascue Claims is an insurance-claims operations platform for healthcare providers. It turns clinic-approved documents and system records into structured, validated, reviewable claims, routes them through configured payer workflows, and reconciles the result. It is available through a design-partner programme; physiotherapy clinics using Cliniko are the first market, not the product's only intended users.

What part of the insurance claim does Vascue handle?+−

The intended workflow covers document or source-record intake, structured extraction, claim mapping, deterministic validation, staff review, channel routing, status history, exception handling, and payment reconciliation. Coverage and adjudication decisions remain with the payer.

Where can claim information come from?+−

The product accepts clinic-approved inputs: connected practice-management records today, with photos, screenshots, scans, PDFs, and manual uploads as the next input path. Cliniko is the first native source-system integration. A public patient chat is not automatically an authorized source for an insurer submission.

Does Vascue decide whether treatment is covered?+−

No. Vascue can prepare a request, apply clinic-approved checks, and display an authorized payer response. It does not replace the insurer or guarantee coverage, approval, or payment.

Does Vascue create diagnoses, procedure codes, or prices with AI?+−

The product boundary is that money, identity, routing, and clinical representations must come from verified sources or deterministic clinic-approved mappings. AI may assist with extraction or suggestions, but missing material facts must be blocked or reviewed rather than invented.

What happens when a claim is missing information?+−

A hard validation issue blocks the claim and explains what needs correction. A softer anomaly is placed in a visible review queue for staff confirmation. The system should not silently fill the gap with a plausible value.

Does Vascue track claims after submission?+−

That is part of the intended workflow. Submission events, external references, payer responses, requests for more information, adjudication, remittance, and shortfalls belong in one claim history. A successful request is not treated as a paid claim.

Does Vascue reconcile insurer payments?+−

Reconciliation logic is included in the locally working product: it is designed to match payment or remittance information to the original claim and surface differences. Production integrations and clinic-specific sources still need onboarding and validation.

## Documents & OCR

4

Can staff upload a photo or screenshot of claim details?+−

Approved photo, screenshot, scan, or PDF upload is the next input path being added, inside an authenticated clinic workspace with OCR and structured extraction. Sensitive documents should not be sent through Vascue's public website or public AI chats.

What does the OCR layer extract?+−

The OCR layer identifies candidate fields and supporting evidence from claim material such as referral letters, invoices, forms, benefit documents, and screenshots. The exact schema depends on the claim and payer; identity, clinical, financial, and routing facts still require a verified source and review.

Does OCR make the claim ready to submit automatically?+−

No. OCR creates a structured draft with links back to the source material. Deterministic completeness and consistency checks run next, and staff review material fields before authorizing submission. Unreadable, missing, or conflicting values should be flagged rather than guessed.

Can Vascue combine uploaded documents with system records?+−

That is the intended model. A claim case can combine authorized uploaded material with records from a connected practice-management or billing system, while retaining the provenance of each extracted or mapped value.

## Integrations

5

Does Vascue replace Cliniko?+−

No. Cliniko is the first practice-management integration and remains the clinic's source system for appointments, invoices, patient records, and treatment documentation. Vascue Claims is designed to accept other approved document and system inputs rather than require Cliniko in every deployment.

Which Cliniko records does Vascue need?+−

The exact minimum depends on the configured claim, but it can include the appointment, practitioner, invoice, treatment entry, patient and payer identifiers, and supporting documents. Permissions should be limited to what the approved workflow requires.

Does Vascue expose Cliniko or Supabase directly to AI agents?+−

No. Public discovery material can describe Vascue's capabilities, but protected clinical operations must go through authenticated, scoped application interfaces. Database credentials and unrestricted tables must not be exposed to agents or browsers.

Can Vascue write results back to Cliniko?+−

Production write-back scope has to be agreed with the clinic and constrained to supported Cliniko operations. Vascue should not claim a write path is live until permissions, idempotency, error handling, and audit behaviour have been tested.

Can Vascue work with a payer portal that has no API?+−

Yes, through an attended browser workflow: staff authenticate to a permitted portal, verified fields are filled, staff review the payer page, and staff retain the final Submit action. Each portal is enabled after permission, mapping, and security review.

## Payers & regions

2

What happens if an insurer is not configured?+−

The claim should stop with a clear configuration reason. Vascue should not infer a destination from an insurer name or route patient information through an unapproved channel.

Is manual filing still supported?+−

Manual can be a valid controlled channel. The system can prepare the work, assign an owner and deadline, and record the external reference without pretending an integration exists.

## Human review & controls

6

Does Vascue submit claims without human review?+−

No. The current design keeps clinic staff responsible for reviewing the prepared case and authorizing submission. Portal workflows also keep the final payer-page submission with staff.

Why keep a person in the loop?+−

A final review can catch errors in source records, mappings, changing payer instructions, and unusual clinical or financial cases. It also makes the provider's authorization explicit when a claim is sent in the clinic's name.

Can staff see why a claim was blocked?+−

That is a core requirement. A useful exception includes the failed rule, relevant source, reason, available next action, owner, and history. A generic low-confidence score is not enough.

Does every claim have an audit trail?+−

The intended claim history records material mappings, validation results, approvals, routing decisions, submission events, external references, status changes, corrections, and reconciliation events with actors and timestamps.

What happens when a payer portal changes?+−

The browser workflow should fail closed, report the unexpected page or field, and return control to staff. A mapping must be reviewed and tested before automation is re-enabled.

Will Vascue eventually make every claim fully autonomous?+−

That is not the current objective. Read-only retrieval and low-risk preparation may support more automation, but submission authority should be decided by evidence, payer rules, clinic policy, and the risk of the action rather than by a blanket autonomy target.

## Security & data

5

Does Vascue process patient information?+−

A production claims workflow necessarily processes the minimum patient and insurance information required to prepare, submit, and reconcile the clinic's claim. That makes access control, contracts, retention, audit, and incident response part of the product rather than optional paperwork.

Can patients submit their details through the public website?+−

No. The public website is for product information and enquiries, not claim records, portal credentials, policy documents, photos, screenshots, or other sensitive patient information. The planned upload workflow belongs in an authenticated clinic workspace with scoped access, private storage, retention controls, and an audit trail.

Is Vascue HIPAA compliant?+−

HIPAA applicability depends on the parties, data, contracts, and deployment. Vascue should not make a blanket product claim from infrastructure alone. A US deployment handling protected health information would require the relevant business-associate agreements and controls before use.

Is Vascue GDPR compliant?+−

GDPR compliance is not a feature switch. A deployment involving EU or UK personal data needs a lawful basis, defined controller and processor roles, data-processing terms, minimization, rights handling, retention, transfer safeguards where applicable, and tested security controls.

Can an external AI provider train on claim data?+−

Vascue should not send identifiable claim data to a model provider unless that exact use is approved, contracted, technically controlled, and documented for the deployment. The safer default is to minimize model access and keep critical claim logic deterministic.

## Availability & onboarding

5

Is Vascue Claims live in production?+−

Yes, for design-partner clinics. Registrations and payer channels are confirmed per clinic during onboarding, so each production payer integration is set up per deployment rather than assumed.

Who is the initial product for?+−

Vascue Claims is intended for clinics, hospitals, and other healthcare providers with repetitive, document-heavy insurance work. The first design-partner deployment is focused on physiotherapy clinics using Cliniko and navigating national and private-insurer workflows. That first market does not limit the broader product or its upload and OCR inputs.

What remains before a clinic can go live?+−

The remaining work includes production deployment, applicable registrations, clinic contracts and onboarding, production credentials, data-protection review, confirmed payer channels, controlled testing, operational training, and an incident and rollback plan.

How should a clinic evaluate Vascue Claims?+−

Start with a defined cohort and a documented baseline. Measure preparation time, first-pass completeness, exceptions, staff review time, submission success, turnaround, reconciliation coverage, and failures. Do not treat released capacity as cash savings without evidence.

Can we test without using real patient information?+−

Yes. Workflow mapping, integration checks, failure cases, and demonstrations should begin with synthetic or de-identified cases. Real patient information should be introduced only after the production contracts, access, security, and operational controls are ready.

## Test one real workflow, safely.

Start with process maps and synthetic cases. We can define the clinic, payer, source records, review boundary, success criteria, and production prerequisites before patient information moves.

[Book a claims walkthrough](/contact-us)

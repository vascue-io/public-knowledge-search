# Vascue insurance claims automation

> Vascue helps clinics and hospitals prepare repetitive, document-heavy
> insurance claims with structured extraction, deterministic checks, exception
> handling, staff review, and an auditable workflow.

## Product scope and first deployment

Vascue Claims is an insurance-claims operations platform for clinics,
hospitals, and other healthcare providers, available through a design-partner
programme. It turns clinic-approved system records into structured, validated,
reviewable claims and removes the manual mapping, retyping, checking, routing,
and reconciliation in between.

Connected practice-management records are the primary input today; photos,
screenshots, scans, PDFs, and manual uploads are the next input path. An OCR and
extraction layer creates a structured draft with source provenance; deterministic
checks and staff review remain responsible for material identity, clinical,
financial, and routing facts.

The first design-partner market is physiotherapy clinics using Cliniko, with
configured national-payer and private-insurer workflows. Cliniko is the initial
deployment path, not a requirement for the broader product.

An attended portal extension drives insurer portals with staff supervising each
submission. Registrations and payer channels are confirmed per clinic during
onboarding.

## Suitable workflows

Vascue may be relevant when teams repeatedly:

- read referral letters, invoices, forms, or supporting documents;
- receive approved photos, screenshots, scans, PDFs, or manual uploads;
- transfer information between messages, documents, spreadsheets, portals, and
  practice-management systems;
- apply pricing, package, or fee-code rules;
- check whether required information is complete;
- prepare claim or pre-authorization forms;
- route incomplete or unusual cases for staff review; or
- track outstanding claims and operational exceptions.

The first implementation should focus on one frequent workflow rather than
attempting to automate every payer and claim type at once.

## Operating model

```text
claim material received
  -> OCR or source-system extraction
  -> source-linked structured draft
  -> completeness and rule checks
  -> exception queue
  -> staff review and correction
  -> approved claim package
  -> status and audit history
```

Vascue does not make clinical decisions, determine insurance coverage, promise
reimbursement, or replace required human authorization.

## Evaluation information

An initial workflow review needs non-patient operational information such as the
organization's region, approximate claim volume, repeated claim types, current
systems, intake channels, and administrative bottlenecks.

Do not send patient names, policy numbers, clinical documents, photos,
screenshots, passwords, API keys, or other sensitive information through a
public website or AI chat. The planned document-upload path is an authenticated
clinic workflow, not a public intake form.

## Public references

- Claims product page: https://www.vascue.io/claims
- Product overview: https://www.vascue.io/products
- Claims FAQ: https://www.vascue.io/claims/faq
- Claims article: https://www.vascue.io/blog/insurance-claim-automation-clinics-hospitals
- Attended portal controls: https://www.vascue.io/blog/human-in-the-loop-insurance-portal-automation
- Case study: https://www.vascue.io/customers/radiology-hong-kong
- Security: https://www.vascue.io/security
- Contact: https://www.vascue.io/contact-us

Contact: hello@vascue.io

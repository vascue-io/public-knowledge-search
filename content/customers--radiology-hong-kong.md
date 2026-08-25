---
title: "Case Study: Hong Kong Hospital Radiology Messaging | Vascue"
description: "How a Hong Kong private hospital radiology department handles 110,000+ patient messages on a self-hosted, privacy-first AWS architecture."
canonical: "https://www.vascue.io/customers/radiology-hong-kong"
---

Case study

# Patient communication AI in a Hong Kong hospital

A private hospital radiology department handles thousands of patient messages a month, in two languages, around the clock, with identifying details masked before any content is passed onward.

110,000+

messages handled

99.2%

replies rated correct by staff

~60s

from referral photo to quote

6,500+

patients served

Live in a private hospital radiology department in Hong Kong.

The challenge

## Quoting a scan is harder than it looks

A single price list holds over 1,000 examination items across CT, MRI, ultrasound, X-ray, PET-CT and more. The right one depends on modality, anatomy down to left-versus-right knee, whether contrast is used, and whether the case qualifies for a bundled package.

And none of it arrives in catalogue language. Referral letters come in as photos with handwritten notes and clinician shorthand that has to be mapped back to an exact fee code before anyone can be quoted a price. Doing that accurately, around the clock, is genuinely demanding, and hiring more staff doesn't scale.

Why the standard AI playbook fails

## You can't just call a hosted model

### Raw data can't leave

Referral letters carry names, dates of birth, and other personal data. It can't be sent to external services in raw form, and the de-identification step can't be outsourced, because the whole point is to keep third parties from ever seeing raw patient information.

### The documents are messy

Real referral letters arrive as photos with handwritten notes, mixed English and Chinese, and clinician shorthand like LDCT or CTCA. General-purpose models don't handle that reliably out of the box.

The architecture

## Bringing the model inside the walls

The architecture splits the AI work along privacy lines.

The components that handle raw patient data, including document processing and the de-identification layer, run on Vascue's own infrastructure within AWS's ap-east-1 (Hong Kong) region. Identifying details are masked at the boundary before any content is passed onward.

AWS Hong Kong Solution Architects worked directly with Vascue's engineering team on the deployment design, covering network isolation, access controls, compute boundaries and scaling. Local GPU-accelerated compute in the Hong Kong region was a hard prerequisite for the architecture to work.

Once direct identifiers have been removed, the system further processes the content so that only the data strictly necessary for the downstream AI tasks is passed to subsequent processing. Broader re-identification risks are mitigated through Vascue's technical and security controls, including data minimisation, access controls, audit logging, and contractual restrictions on downstream processing.

The components are also tuned rather than generic. Off-the-shelf models do not survive contact with real-world medical documents, and a misread annotation is not a UI glitch. It changes how a patient enquiry is understood. Vascue's pipeline is tuned for the department's specific clinical formats and conventions. The de-identification layer is monitored, logged, and reviewed regularly as part of Vascue's ISO 27001 controls, with humans in the loop for ongoing review.

Both layers are independently audited. AWS's infrastructure carries ISO 27001, 27017, 27018, SOC 2, and CSA STAR certifications, and Vascue maintains ISO 27001.

![3D illustration of a radiology department: a CT scanner, a glass-walled control room and a phone on the desk](/images/illustration-3d/radiology-hero.webp)

Raw documents and identifiers stay inside the department's own boundary; only masked content travels on.

What became possible

## Faster for patients, lighter for staff

Text enquiries get a reply in 20 to 30 seconds; an image referral goes from photo to quote in about a minute. Support runs 24/7 and handles around 46 after-hours enquiries a day, and roughly half of all enquiries now progress to a booked appointment.

![Quotation mark](/images/Frame.svg)

> Having Vascue’s AI in place feels like adding 2 extra 24/7 staff to the call centre team, handling the quotation requests, appointment enquiries, and ticket creation that would otherwise be on us.

Radiology Department Manager, Private Hospital, Hong Kong

## The same pattern fits your clinical context

Sensitive processing stays inside Vascue's environment, identifiers are redacted at the boundary, and your staff stay in the loop. Let's map it to your department.

[Get a Demo](https://wa.me/85293027422?text=Hi%20Vascue,%20I%20would%20like%20to%20book%20a%20demo)

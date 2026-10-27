---
title: "From Referral Letter to Quotation: How AI Reads Radiology Referrals in About 60 Seconds"
description: "How AI reads a photographed referral letter and returns an itemised radiology quotation in about 60 seconds, with identifiers masked and staff in review."
image: "https://www.vascue.io/images/blog/ai-referral-letter-processing-radiology-quotation.png"
canonical: "https://www.vascue.io/blog/ai-referral-letter-processing-radiology-quotation"
---

[All articles](/blog)Healthcare AI

# From Referral Letter to Quotation: How AI Reads Radiology Referrals in About 60 Seconds

Vascue TeamSeptember 29, 20268 min read

![From Referral Letter to Quotation: How AI Reads Radiology Referrals in About 60 Seconds](/images/blog/ai-referral-letter-processing-radiology-quotation.png)

AI referral letter processing is software that reads a photographed or scanned referral, extracts the examinations the doctor requested, and matches them to a department's price catalogue and rules, so the patient gets an itemised quotation without staff retyping the letter. In a hospital radiology department in Hong Kong, that work now resolves in around 60 seconds per image-based referral, against a catalogue of more than 1,000 examination items, with staff reviewing every appointment request before it is confirmed. The hard part is not the conversation with the patient. It is the letter.

This guide explains why referrals are difficult for software, the steps between a phone photo and a quotation, what "accuracy" should mean when you evaluate a system, and where patient data goes along the way.

## Why Is a Referral Letter So Hard for Software to Read?

A referral that reaches a radiology front desk today is rarely a clean PDF. It is usually a photo the patient took on a phone and sent over WhatsApp, and it carries four problems at once.

**It is a photo, not a document.** Angle, glare, a thumb over the corner, a crease through the examination line. The software has to read what is there before it can understand it.

**It is handwritten and abbreviated.** Real referral letters are full of handwritten annotations, physician shorthand and institution-specific formats. Research on handwriting shows how uneven machine reading still is: a 2026 study in *Exploratory Research in Clinical and Social Pharmacy* found GPT-4.1 scored a [median of 38.5 out of 40 on handwritten medication lists](https://pmc.ncbi.nlm.nih.gov/articles/PMC13241658/), yet [35% of entries with "as needed" instructions were misread, against 3% for medications without dosing complexity](https://pmc.ncbi.nlm.nih.gov/articles/PMC13241658/). The authors concluded that [human oversight remains essential to ensure patient safety](https://pmc.ncbi.nlm.nih.gov/articles/PMC13241658/). The simple lines are easy. The qualified ones are where errors cluster.

**It mixes languages.** In Hong Kong, a single letter can switch between Chinese and English mid-line, with English examination names inside Chinese clinical notes.

**It is often incomplete.** A 2025 audit of 400 radiology requests at a tertiary hospital, published in *Cureus*, found that [only 67% included the examination's clinical purpose, prior imaging was referenced in just 35%, and 83% were clearly legible](https://pmc.ncbi.nlm.nih.gov/articles/PMC12757699/). A system that reads perfectly still has to recognise what is missing and ask.

## Why Is Reading the Letter Only Half the Job?

Extracting "MRI lumbar spine" from a photo produces text, not a quotation. The department in this case study runs more than 1,000 distinct examination items, with pricing logic that varies by modality, contrast, anatomy and applicable package. One line on a referral can correspond to several catalogue entries, and the right one depends on details the letter may state, imply or omit.

That is why generic document tools stall at radiology. An OCR engine returns characters. A general chatbot returns a plausible answer. Neither knows which catalogue line applies, which package it belongs to, or when a question needs a person.

## How Does AI Turn a Referral Photo Into an Itemised Quotation?

The pipeline has six steps. Each one exists because a shortcut fails in production.

1.  **Receive the image where the patient already is.** The referral arrives as a WhatsApp photo, in Chinese or English, at any hour.
2.  **Read the document inside the privacy boundary.** Document processing, the part that touches raw patient data, runs on infrastructure the operator controls in the hospital's cloud region.
3.  **Mask identifiers before anything moves on.** Names, dates of birth and other identifying details are masked at that boundary, and only the data strictly necessary for downstream AI tasks passes through.
4.  **Extract and match.** The requested examinations, anatomy and relevant notes are matched to the department's catalogue and pricing rules: modality, contrast, anatomy, package.
5.  **Reply with the quotation.** The patient receives an itemised quotation in their own language, in the same thread.
6.  **Hand the rest to staff.** Every appointment request surfaces to staff for review before it is confirmed, and every conversation is categorised and tagged so the next person picks up exactly where the AI left off.

## Three Ways to Handle a Referral Photo

Manual front desk

Generic OCR or a direct hosted-model call

Healthcare-tuned pipeline with a privacy boundary

Handwriting, shorthand, mixed Chinese-English

Handled by experienced staff

Frequently misread

Tuned to the documents the department actually receives

Matching to a 1,000+ item catalogue

Staff look it up

Not built in

Rules and pricing applied in the pipeline

Patient data

Stays in the hospital

Raw letter sent to an external service

Identifiers masked in-region before downstream AI tasks

After-hours enquiries

Wait until morning

Depends on the tool

Answered around the clock

Staff role

Every step

Checking output they did not trust

Review, confirmation and exceptions

## What Does "Accuracy" Mean for a Referral Reader?

Vendors quote accuracy in three different senses, and only one of them matters to a radiology department.

-   **Character accuracy:** how many letters and digits were read correctly. Useful for engineers, misleading for buyers, because one wrong character in "with contrast" changes the price.
-   **Extraction accuracy:** whether the right examinations were pulled from the letter. Closer, but it ignores the catalogue match.
-   **Response correctness:** whether the reply the patient received was right, judged by the staff who know the department. This is the measure that reflects the whole pipeline.

The Hong Kong deployment reports the third: [staff rate 99.5% of AI responses as correct, under ongoing human review](/blog/patient-communication-ai-hong-kong-hospital-privacy-first-architecture-aws). The review is part of the design, not a launch phase. That is the same principle we argue for in claims work in [should AI submit insurance claims without human review](/blog/should-ai-submit-insurance-claims-without-human-review): AI does the volume, a person keeps the decision.

## Where Does Patient Data Go?

Referral letters carry names, dates of birth and other personal data, so sending them to an external model service outright breaks data protection standards. In the case study, document processing and de-identification run on Vascue's own infrastructure in AWS's ap-east-1 (Hong Kong) region, local to the hospital, and identifying details are masked before content reaches downstream AI tasks. Local GPU-accelerated compute in that region was a hard requirement, because it is what makes keeping the sensitive layer in-region practical.

Residual re-identification risk is managed through data minimisation, access controls, audit logging and contractual restrictions on downstream processing. The de-identification layer is monitored, logged and reviewed under Vascue's ISO 27001 controls, with a human in that review loop, and the AWS infrastructure holds ISO 27001, 27017, 27018, SOC 2 and CSA STAR certifications. We cover the guardrail side of automated healthcare workflows in more depth in [the guardrails behind AI booking in healthcare](/blog/the-guardrails-behind-ai-booking-in-healthcare).

## What the Hong Kong Radiology Deployment Shows

Vascue runs this workflow for a hospital radiology department in Hong Kong, first described in a [paid post on the South China Morning Post](https://www.scmp.com/presented/tech/topics/generative-ai-and-cloud-services/article/3359561/patient-communication-ai-hong-kong-hospital-privacy-first-architecture-aws) sponsored by AWS Hong Kong and updated in [our case study](/blog/patient-communication-ai-hong-kong-hospital-privacy-first-architecture-aws). As of August 2026:

Measure

Result

Patients served

8,000+

Messages processed

150,000+

Successful bookings

4,500+

Text enquiry response

20 to 30 seconds

Image-based referral to quotation

Around 60 seconds

After-hours enquiries handled

Roughly 46 a day

Enquiries progressing to a booking

Around half

AI responses rated correct by staff

99.5%

The after-hours figure is the one departments tend to underestimate: roughly 46 enquiries a day that previously went unanswered overnight. This is the workflow Vascue's AI Front Desk runs for hospital departments: the patient messages on WhatsApp, the quotation comes back in the thread, and staff keep the confirmation step.

## A Checklist Before You Automate Referral Intake

1.  **Test on your own letters.** Collect a sample of real referrals, masked, including the worst photos and the most abbreviated handwriting. A demo on clean PDFs proves nothing.
2.  **Ask where masking happens.** Before or after the model call, and in which cloud region. "We anonymise the output" is the wrong answer.
3.  **Ask who maintains the catalogue and rules.** Prices, packages and routing change. Find out how an update reaches the pipeline and who signs it off.
4.  **Define the exceptions in writing.** Missing clinical purpose, an unrecognised examination, a request that needs a radiologist's view: each should route to a named person, not a generic inbox.
5.  **Measure response correctness, continuously.** Staff ratings on live replies, reviewed monthly, not a one-off accuracy test at go-live.
6.  **Keep confirmation human.** Let AI quote and prepare. Let staff confirm.

## FAQ

**How accurate is AI at reading photographed medical referral letters?** It depends on what is measured. Research on handwritten medication lists found GPT-4.1 scored a median of 38.5 out of 40, but misread 35% of entries with "as needed" instructions. In a Hong Kong hospital radiology deployment, staff rate 99.5% of AI responses as correct under ongoing human review, and every appointment request is still confirmed by staff.

**How long does it take AI to turn a referral into a radiology quotation?** In the Hong Kong deployment, image-based referrals typically resolve in around 60 seconds, covering extraction, identifier masking, matching to department pricing and generating the quotation. Text enquiries are answered in 20 to 30 seconds.

**Is it safe to send referral letters to an AI model?** Not as raw documents. Referral letters carry names, dates of birth and other personal data, so identifying details should be masked on controlled infrastructure in the hospital's cloud region before any content reaches downstream AI tasks, with access controls, audit logging and a certified security management system around that boundary.

**Does AI replace radiology front-desk staff?** No. Vascue's AI Front Desk takes the high-volume work of reading referrals, quoting and answering routine questions on WhatsApp around the clock, while staff review every appointment request, handle exceptions and keep attention on the patients who need clinical judgment.

[Book a demo](https://api.whatsapp.com/send/?phone=85293027422&text=Hi+Vascue%2C+I+would+like+to+see+a+demo&type=phone_number&app_absent=0) and we will walk through the six steps against the referrals your department actually receives.

This article is part of the [AI Front Desk](/ai-front-desk) cluster. Start with the pillar page for the product overview, then come back for the detail.

Related reading

## Keep reading

-   ![Patient Journey Analytics for Clinics: The Front-Desk Metrics Your PMS Cannot Show](/images/blog/patient-journey-analytics-clinic-front-desk.png)
    
    Practice Operations
    
    ### Patient Journey Analytics for Clinics: The Front-Desk Metrics Your PMS Cannot Show
    
    Patient journey analytics for clinics: the front-desk metrics a practice-management system cannot show, how to calculate each one honestly, and how a practice manager can use them in a fifteen-minute weekly review.
    
    8 min read
    
    [Learn more](/blog/patient-journey-analytics-clinic-front-desk)
    
-   ![What Is Healthcare Operations Automation? A Plain-Language Guide for Operations Leads](/images/blog/what-is-healthcare-operations-automation.png)
    
    Healthcare Operations
    
    ### What Is Healthcare Operations Automation? A Plain-Language Guide for Operations Leads
    
    Healthcare operations automation completes the admin work between a patient request and an operational outcome. How it differs from chatbots, RPA and a practice-management system, the five-step mechanism, and a four-part buyer checklist.
    
    8 min read
    
    [Learn more](/blog/what-is-healthcare-operations-automation)
    
-   ![When Should an AI Front Desk Hand a Patient to Staff? Approval, Takeover and Audit Trails](/images/blog/ai-front-desk-human-handoff-approval-audit-trail.png)
    
    Practice Operations
    
    ### When Should an AI Front Desk Hand a Patient to Staff? Approval, Takeover and Audit Trails
    
    When an AI front desk should hand a patient to staff, the three control modes regulators describe, what a usable takeover looks like, what an audit trail must record, and how to roll autonomy out safely.
    
    8 min read
    
    [Learn more](/blog/ai-front-desk-human-handoff-approval-audit-trail)
    

Part of the [AI Front Desk](/ai-front-desk) cluster[All articles →](/blog)

---
title: "Appointment Reminders, Intake Forms and Follow-Up Messages for Physio Clinics: What to Look For"
description: "What Cliniko and Nookal already automate for reminders, intake and follow-up, where the native tools stop, and a checklist for allied health."
image: "https://www.vascue.io/images/blog/physio-clinic-appointment-reminders-intake-forms-follow-up-automation.png"
canonical: "https://www.vascue.io/blog/physio-clinic-appointment-reminders-intake-forms-follow-up-automation"
---

[All articles](/blog)Practice Operations

# Appointment Reminders, Intake Forms and Follow-Up Messages for Physio Clinics: What to Look For

Vascue TeamAugust 26, 20268 min read

![Appointment Reminders, Intake Forms and Follow-Up Messages for Physio Clinics: What to Look For](/images/blog/physio-clinic-appointment-reminders-intake-forms-follow-up-automation.png)

Workflow automation for an allied health clinic is software that sends reminders, collects intake and consent forms, and follows up after appointments from the practice-management system's own record, so staff never re-enter what the patient has already told you. For a physiotherapy clinic on Cliniko or Nookal, most of that is already switched on or one setting away: both send SMS and email reminders, both take online bookings, both collect intake forms before the visit. The decision is not whether to automate but where the native tools stop, and what to look for in the layer that sits on top.

This guide is written for an Australian private physio practice, but the checklist applies to any allied health clinic on a cloud practice-management system (PMS).

## What Does Cliniko Already Do for Reminders, Intake and Follow-Up?

**Reminders.** Cliniko sends email and SMS reminders [from one to nine days before the appointment](https://help.cliniko.com/en/articles/2890282-a-quick-overview-of-appointment-reminders-confirmations), with a send-time window and the option to skip weekends. SMS costs [10 cents per credit](https://www.cliniko.com/pricing/), and [a message over 160 characters uses a second credit](https://help.cliniko.com/en/articles/1023870-set-up-sms-appointment-reminders). Patients can confirm by reply.

**Online bookings.** A public booking page that [any patient, new or existing, can use without logging in](https://help.cliniko.com/en/articles/1023955-a-quick-overview-of-online-bookings), with optional prepayment through Stripe.

**Intake forms.** Cliniko has offered [secure patient forms since April 2020](https://www.cliniko.com/blog/news/secure-patient-forms-are-here/). Forms can be [pre-filled from the patient record and write back to it](https://help.cliniko.com/en/articles/10558311-automatically-update-the-patient-record-via-forms), and can include a [digital signature question](https://help.cliniko.com/en/articles/4239398-let-patients-digitally-sign-forms) for consent.

**Recalls.** Cliniko tracks recall types and produces a recall report, but the follow-up itself is manual: the help article says [follow-up could include sending a letter or calling the patient](https://help.cliniko.com/en/articles/8410284-set-up-patient-recalls). There is no automated recall message.

**API.** A documented [REST API](https://docs.api.cliniko.com/) and a [connected-apps directory](https://www.cliniko.com/connected-apps/) of roughly a hundred integrations, which is what lets other tools read and write the diary.

## What Does Nookal Already Do?

Nookal's scheduling features include automated SMS and email reminders with [two-way SMS for replies and confirmations](https://www.nookal.com/us/features/appointment-scheduling), automated recalls [based on previous bookings](https://www.nookal.com/us/features/appointment-scheduling), and the ability to [send intake, profile and informed-consent forms to patients before they attend](https://www.nookal.com/us/features/appointment-scheduling). Online bookings and [digital intake forms](https://www.nookal.com/info/practice-management-software) are part of the core product, and Nookal exposes an [API for connecting other systems](https://www.nookal.com/us/integrations).

The practical difference from Cliniko: Nookal automates the recall message; Cliniko gives you the list. Both are covered in more depth on our [Cliniko](/cliniko) and [Nookal](/nookal) integration pages.

## What Is the Evidence That Reminders Work?

Strong, and older than most of the software. A meta-analysis of 21 studies published in [BMJ Open in 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC5093388/) found that patients receiving notifications were 25% less likely to miss appointments (15% versus 21% no-show rate), and that multiple notifications were significantly more effective than a single one. The second finding is the one clinics under-use: a reminder at seven days and another at one day beats either alone.

The other number worth knowing is when patients try to book. Zocdoc has reported that [roughly half of appointments on its platform were booked after hours](https://www.zocdoc.com/resources/blog/article/why-not-offering-after-hours-booking-is-driving-away-patients/), between 5 pm and 9 am. A reminder system can only remind patients who got as far as a booking.

## Where the Native Tools Stop

Reminders, booking pages and forms cover the patient who already has an appointment. Five things fall outside that:

1.  **The first enquiry.** "Do you treat shoulders?", "Are you open Saturday?", "How much is an initial?" arrive by phone, message and web form, often after hours, and a booking page cannot answer them. The native tools start at the booking; the leak is before it.
2.  **Anything beyond yes or no.** A reminder can take "Y". It cannot take "can we make it 3:30?" or "I'm bringing my MRI, is that useful?" Those replies land in an inbox a receptionist clears the next morning.
3.  **Channel.** Native reminders are SMS and email. Patients increasingly message on WhatsApp, which has its own rules: Meta's pricing documentation states that [template messages are the only message type that can be sent outside a customer service window](https://developers.facebook.com/docs/whatsapp/pricing/), and that non-template messages are free within an open window (24 hours from the patient's last message). A reminder sent on WhatsApp needs an approved template; a reply to a patient's question does not.
4.  **Recalls that actually message.** On Cliniko, recalls are a list for a human to work through.
5.  **Languages.** Reminder templates are single-language. A clinic with Mandarin, Vietnamese or Arabic-speaking patients is answering those enquiries by hand.

## A Checklist: What to Look for in Automation Built for Allied Health

1.  **It writes to the PMS record, not a parallel database.** Two-way sync through the Cliniko or Nookal API: a booking made in a conversation appears in the diary, and a change in the diary updates the conversation. If the tool keeps its own patient list, you have created a second source of truth.
2.  **It handles the reply, not only the send.** Reschedule, cancel, "what should I bring", and a price question should be resolved inside the thread, with a human handoff when the question is clinical.
3.  **It respects channel rules.** On WhatsApp: approved templates for outbound reminders, free-form replies inside the 24-hour window, and no marketing dressed as a reminder.
4.  **It has clinical boundaries.** The assistant should triage (urgent, book, refer to a clinician) and never give treatment advice. Ask to see the refusal behaviour, not the demo.
5.  **It satisfies the Privacy Act.** The OAIC is explicit that [the Privacy Act covers any business that is a health service provider regardless of turnover](https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/organisations/small-business), and that physiotherapy practices are [health service providers even when small](https://www.oaic.gov.au/privacy/your-privacy-rights/health-information/what-is-a-health-service-provider). Ask where conversation data is stored, for how long, and how a patient's messaging consent is recorded.
6.  **It follows the practitioner's rules.** Initial-appointment lengths, who sees what condition, which practitioners take new patients, and which slots are held back. A tool that books anything into any gap creates work, not capacity.
7.  **Pricing you can forecast.** Per-conversation or flat per-location fees, with the overage rate published. SMS and WhatsApp template costs passed through at cost.
8.  **It reports the numbers you care about.** After-hours enquiries answered, enquiry-to-booking conversion, no-show rate before and after, median time to first reply.

## How the Common Tools Divide Up

Layer

Tools

What it covers

What it does not

Practice management (the record)

[Cliniko](https://www.cliniko.com/), [Nookal](https://www.nookal.com/us/integrations), [Halaxy](https://www.halaxy.com/) (free core platform), [Jane](https://jane.app/), [Splose](https://splose.com/), [Zanda](https://zandahealth.com/blog/powerdiary-now-zanda/) (Power Diary until November 2024)

Diary, notes, invoicing, reminders, online booking, intake forms

The first enquiry, two-way conversation, WhatsApp, multilingual answering

Conversation and triage (the front desk)

AI front-desk assistants that sync with the PMS, including Vascue on WhatsApp

Answering enquiries 24/7, quoting, booking inside the conversation, reschedules, multilingual replies

Clinical notes, billing, claiming

Exercise and outcomes

Physitrack and similar

Home programmes, adherence

Scheduling and intake

We compare the conversation-layer options in [our AI medical receptionist roundup](/blog/best-ai-medical-receptionist-allied-health), and walk through the full sequence from enquiry to claim in [patient journey automation for allied health clinics](/blog/end-to-end-patient-journey-automation-allied-health).

## A Simple Setup for a Physio Clinic This Month

1.  Turn on two reminders in the PMS: seven days and one day before, SMS for the second. The BMJ Open evidence favours multiple notifications.
2.  Attach the intake and consent form to the online-booking confirmation so new patients complete it before they arrive, and let it write back to the record.
3.  On Nookal, switch on automated recalls for the conditions with a planned review. On Cliniko, put the recall report on a weekly admin checklist until an automated layer covers it.
4.  Decide what happens to after-hours enquiries: voicemail, web form, or a messaging assistant that books. Measure how many arrive between 5 pm and 9 am for two weeks before deciding.
5.  Write down the practitioner rules (appointment lengths, conditions, new-patient slots) in one page. Whatever automation you add will need them in that form.

## FAQ

**Do SMS reminders reduce no-shows?** Yes. A 2016 meta-analysis of 21 studies in BMJ Open found patients who received notifications were 25% less likely to miss appointments (15% versus 21%), and that more than one notification worked better than one.

**Does Cliniko send automated recall messages?** No. Cliniko records recall types and produces a recall report; the follow-up is a letter or call by staff. Nookal automates recall messages based on previous bookings.

**Can we use WhatsApp for appointment reminders in Australia?** Yes, with two conditions. Meta's rules allow only approved template messages outside a 24-hour customer-service window, so reminders must be templates, while replies to a patient's message inside the window are free-form. And because a physiotherapy practice is a health service provider under the Privacy Act regardless of size, messaging consent and data storage need to be documented.

**Which platforms automate the whole journey for an allied health practice?** No single product does. The PMS (Cliniko, Nookal, Halaxy, Jane, Splose, Zanda) covers reminders, forms and recalls for patients who have a booking. A conversation layer covers the enquiry before the booking and the replies after it: Vascue's WhatsApp front desk answers, quotes and books 24/7 with two-way Cliniko and Nookal sync, and hands clinical questions to staff.

[Book a demo](https://api.whatsapp.com/send/?phone=85293027422&text=Hi+Vascue%2C+I+would+like+to+see+a+demo&type=phone_number&app_absent=0) and we will map the checklist to how your clinic books today.

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
    
-   ![Patient Journey Automation for Allied Health Clinics, End to End](/images/blog/end-to-end-patient-journey-automation-allied-health.png)
    
    Healthcare AI
    
    ### Patient Journey Automation for Allied Health Clinics, End to End
    
    Most clinic AI automates one slice of the journey. Vascue connects patient communication and booking, while a separate product, Vascue Claims, handles provider-side claims.
    
    6 min read
    
    [Learn more](/blog/end-to-end-patient-journey-automation-allied-health)
    

Part of the [AI Front Desk](/ai-front-desk) cluster[All articles →](/blog)

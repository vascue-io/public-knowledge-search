---
title: "From 'Find Me a Physio' to a Confirmed Appointment"
description: "A safe, patient-led example of how an AI assistant could discover and book a clinic through Vascue."
image: "https://www.vascue.io/images/blog/from-find-me-a-physio-to-confirmed-appointment.png"
canonical: "https://www.vascue.io/blog/from-find-me-a-physio-to-confirmed-appointment"
---

[All articles](/blog)Healthcare AI

# From 'Find Me a Physio' to a Confirmed Appointment

Vascue TeamAugust 15, 2026Updated August 21, 20264 min read

![From 'Find Me a Physio' to a Confirmed Appointment](/images/blog/from-find-me-a-physio-to-confirmed-appointment.png)

“Find me a physiotherapist near Central and book Thursday afternoon.”

It sounds like a single request. A responsible healthcare booking flow breaks it into clear, patient-controlled steps.

This is the future-state flow Vascue is researching, not a publicly available booking service today. The design sits beside the [AI Front Desk](/ai-front-desk), which already handles enquiries and bookings for clinics over messaging channels; the difference here is that the patient's own assistant does the asking.

## 1\. Find Suitable Options

The assistant searches Vascue for participating clinics using the patient's requested location and service. Public discovery should return coarse, useful information: participating clinics, broad services, and areas served.

It should not expose patient records or dump every clinic in a directory. How clinics choose what to publish, and why coarse-first matters, is covered in [how partner clinics can be discovered by AI](/blog/how-partner-clinics-can-be-discovered-by-ai).

## 2\. Verify the Patient

Before the system reveals rich availability or writes an appointment, the patient verifies their phone through a one-time code. This connects the request to a person who controls that phone number.

Verification is not medical identity proof, and it does not make clinical decisions. It is an administrative control against spoofed and spam bookings.

## 3\. See Real Availability

The assistant asks for current times at the selected clinic. Vascue checks the clinic's own booking system, rather than relying on a stale copied calendar.

The patient might see: Thursday, 3:30pm; first physiotherapy assessment; Central; named practitioner; price or deposit terms where the clinic makes them available.

## 4\. Make a Proposal, Not a Silent Booking

The assistant repeats the exact details back to the patient. It does not say “done” before the patient agrees.

The patient confirms the proposed appointment. Only then does Vascue ask the clinic system to create the booking. If the slot disappeared in the meantime, the system should say so and offer alternatives.

Two phases, not one. The proposal is cheap and reversible; a proposal that is never confirmed simply expires. The confirmation is the single moment at which anything is written into the practice-management system, and it is the only write the design allows. The tools behind that split are described in [what an MCP booking server actually does](/blog/what-an-mcp-booking-server-does).

## 5\. Keep the Boundaries Clear

The assistant helps with administration. It does not diagnose the patient, decide which treatment they need, or access clinical notes. The clinic remains responsible for care; the patient remains in control of the appointment.

## What the Clinic Sees

From the clinic's side, a confirmed agent booking should look like any other online booking: a named patient, a verified phone number, a service the clinic chose to make bookable, and a time that was genuinely free when it was confirmed. Nothing arrives as a half-formed request that reception has to chase.

Clinics also keep the levers they already have. They can restrict which services are bookable this way, require a deposit where their system supports one, ask that new-patient bookings be held for approval, or pause the channel entirely. [The guardrails behind AI booking in healthcare](/blog/the-guardrails-behind-ai-booking-in-healthcare) sets out the full list.

## When Things Go Wrong

A useful flow is defined as much by its failure modes as by the happy path.

-   No participating clinic matches the request: the assistant says so, rather than inventing a listing or suggesting a clinic that has not opted in.
-   The patient never completes verification: nothing beyond coarse public information is shown, and no proposal is created.
-   The slot is taken between proposal and confirmation: the confirmation fails cleanly and the assistant offers the next real openings.
-   The patient changes their mind: an unconfirmed proposal expires on its own; a confirmed booking can be changed or cancelled through the same verified path.

In each case the clinic calendar is left exactly as it was. That is the property worth designing for.

## Where This Stands

Vascue is testing this flow with synthetic patients and test calendars, starting with Cliniko as the first intended integration. Clinics can [register interest on the research page](/ai-agents) without connecting a system or sharing a credential; no production connection is created from that form. Privacy, security, and provider reviews are release gates before any real-patient pilot, and the [security page](/security) describes the controls Vascue already operates under.

That is the promise worth building toward: less phone tag, without sacrificing consent or trust.

This article is part of the [Agent-ready healthcare (research)](/ai-agents) cluster. Start with the pillar page for the product overview, then come back for the detail.

Related reading

## Keep reading

-   ![Building for Browsers, Search Engines, and Now Agents](/images/blog/building-for-browsers-search-engines-and-agents.png)
    
    Healthcare AI
    
    ### Building for Browsers, Search Engines, and Now Agents
    
    Why websites increasingly need machine-readable discovery, clean content, and controlled APIs alongside their normal user interface.
    
    4 min read
    
    [Learn more](/blog/building-for-browsers-search-engines-and-agents)
    
-   ![How Partner Clinics Can Be Discovered by AI, Without Becoming a Marketplace Free-for-All](/images/blog/how-partner-clinics-can-be-discovered-by-ai.png)
    
    Healthcare AI
    
    ### How Partner Clinics Can Be Discovered by AI, Without Becoming a Marketplace Free-for-All
    
    AI discovery should make clinic information more accurate and usable, while keeping clinics in control of what agents can see and book.
    
    4 min read
    
    [Learn more](/blog/how-partner-clinics-can-be-discovered-by-ai)
    
-   ![The Guardrails Behind AI Booking in Healthcare](/images/blog/the-guardrails-behind-ai-booking-in-healthcare.png)
    
    Healthcare AI
    
    ### The Guardrails Behind AI Booking in Healthcare
    
    AI booking should be an administrative assistant with clear limits, not an autonomous actor with broad access to healthcare systems.
    
    5 min read
    
    [Learn more](/blog/the-guardrails-behind-ai-booking-in-healthcare)
    

Part of the [Agent-ready healthcare (research)](/ai-agents) cluster[All articles →](/blog)

---
title: "Building for Browsers, Search Engines, and Now Agents"
description: "Why websites increasingly need machine-readable discovery, clean content, and controlled APIs alongside their normal user interface."
image: "https://www.vascue.io/images/blog/building-for-browsers-search-engines-and-agents.png"
canonical: "https://www.vascue.io/blog/building-for-browsers-search-engines-and-agents"
---

[All articles](/blog)Healthcare AI

# Building for Browsers, Search Engines, and Now Agents

Vascue TeamAugust 15, 2026Updated August 21, 20264 min read

![Building for Browsers, Search Engines, and Now Agents](/images/blog/building-for-browsers-search-engines-and-agents.png)

For most of the web's history, a company site had two audiences: people using browsers and search engines indexing pages.

Now there is a third: software agents acting on a person's request.

## A Page Is Not Always a Good Interface for an Agent

A browser can render complex layouts, navigation, animations, and forms. An agent often needs something simpler: clear text, stable links, structured API documentation, and an explicit route to authenticated actions.

That is why we are adding machine-readable layers alongside the normal Vascue website.

## The Pieces

-   **Markdown representations** give an agent clean page content when it requests it, while browsers still receive HTML.
-   **Link headers** point software toward useful resources, such as API documentation and discovery catalogs.
-   **An API description** documents the public, read-only endpoints, and can later describe a booking gateway once one is deployed.
-   **OAuth metadata** tells a supported client how to discover authenticated access.
-   **An MCP server card and skills index** describe the capabilities an approved agent may use and how to use them safely.

None of these replace the website. They make the site easier for software to understand without asking it to scrape visual markup.

## What Vascue Publishes Today

Concretely, the public site now carries:

-   [`/llms.txt`](/llms.txt): a plain-text summary of what Vascue does, who it is for, and which pages to read first. It is the file a language-model agent is most likely to look for.
-   Markdown companions for the pages agents ask about most, such as `/claims-automation.md` and `/ai-agents.md`, plus content negotiation: a client that sends `Accept: text/markdown` receives the Markdown version of a page rather than its HTML.
-   `Link` headers on the homepage that point to those files, so an agent that fetches only the root still learns where the useful material lives.
-   A `.well-known/ai-search.json` file and an MCP server card for Vascue's public knowledge search, which lets an assistant search the public website over MCP. That service is live, and it contains public content only.
-   An Agent Skills index with `SKILL.md` files that explain, in plain language, how an agent should navigate the site and evaluate the claims product.

Every one of these describes public information. None of them contains or accepts patient data, and none of them exposes a booking action.

## How to Try It

A developer can see the difference in a terminal. Request a page normally and the response is HTML. Request the same URL with `Accept: text/markdown` and the response is the article text, headings intact, navigation and scripts gone. The canonical URL does not change, which is the point: one address, two representations, chosen by the client.

## What Changes for Search Engines

Nothing is taken away. Googlebot and Bingbot still receive the full HTML page, with the same canonical tag, the same structured data, and the same internal links. The Markdown layer is additive; it appears only when a client asks for it. Vascue's robots.txt states explicitly that search indexing and AI use of the public content are both welcome, because being found and cited is the reason the content exists.

## Discovery Is Not Permission

This is the most important distinction. An agent may discover that Vascue is researching a booking service, but discovery does not mean that service is publicly live and does not grant access to patient information or booking actions.

The agent still needs an approved integration, user authorization, patient verification, and explicit confirmation for a specific appointment.

In that sense, these standards are signposts. They help the right client find the right interface. The security and consent controls still decide what happens next.

## Where the Booking Gateway Fits

The files above are the signage. The booking gateway Vascue is researching is a separate, authenticated service behind that signage: a small set of tools that find participating clinics, show availability to a verified patient, and write a single confirmed appointment. [What an MCP booking server actually does](/blog/what-an-mcp-booking-server-does) describes those tools; [why AI agents should not call a clinic database directly](/blog/why-ai-agents-should-not-call-clinic-databases) explains why they sit behind a gateway at all. That service is not publicly live, and nothing in the discovery layer changes that.

## The Web Is Becoming More Actionable

The web is not moving away from people. It is gaining a new layer in which software can help people navigate services they already use.

For Vascue, that means helping a patient move from “I need a physiotherapist” to an accurate, patient-approved appointment, without turning the website, the clinic system, or the patient record into an open tool for arbitrary agents. The [AI Front Desk](/ai-front-desk) does that work today on a clinic's own channels; the [research pilot](/ai-agents) explores how a patient's own assistant might do it next.

This article is part of the [Agent-ready healthcare (research)](/ai-agents) cluster. Start with the pillar page for the product overview, then come back for the detail.

Related reading

## Keep reading

-   ![From 'Find Me a Physio' to a Confirmed Appointment](/images/blog/from-find-me-a-physio-to-confirmed-appointment.png)
    
    Healthcare AI
    
    ### From 'Find Me a Physio' to a Confirmed Appointment
    
    A safe, patient-led example of how an AI assistant could discover and book a clinic through Vascue.
    
    4 min read
    
    [Learn more](/blog/from-find-me-a-physio-to-confirmed-appointment)
    
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

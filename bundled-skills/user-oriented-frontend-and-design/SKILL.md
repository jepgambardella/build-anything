---
name: user-oriented-frontend-and-design
description: Frontend UX and copywriting guardrails for building apps, web apps, websites,
  mobile apps, desktop apps, games, dashboards, landing pages, and any user-facing
  interface. Use when Codex designs or edits UI text, titles, buttons, navigation,
  empty states, onboarding, cards, hero sections, labels, calls to action, or visual
  hierarchy, especially to prevent prompt-facing, technical, self-descriptive copy
  such as "a simple mobile-first app for X" from appearing in the final frontend.
---

# User-oriented Frontend and Design

## Core Rule

Write and design the frontend for the end user, not for the developer prompt. Never expose the implementation request, app category, framework, constraints, or design brief as visible product copy.

The interface must feel like a real product, service, tool, or experience. It should be clear, curious, simple, and useful without explaining itself in technical or meta terms.

## Non-negotiables

- Do not copy the user's prompt into the UI.
- Do not describe the app as an app, web app, mobile-first app, dashboard, clone, MVP, prototype, demo, template, simple tool, or frontend unless the product genuinely sells itself that way.
- Do not use visible UI text to explain technical constraints, architecture, layout choices, implementation details, responsiveness, accessibility, or feature inventory.
- Do not make headings out of the assignment. Create headings that belong to the product and the user's goal.
- Do not add filler subtitles that merely restate what the interface does.
- Do not use "simple", "modern", "mobile-first", "responsive", "AI-powered", "built with", "powered by", "for managing X", or similar brief-derived phrases unless they are truly user-facing value propositions.
- Do not put instructions, shortcuts, or feature descriptions in the interface unless a real user needs them at that moment.
- Do not make the frontend over-explain itself. Prefer affordances, familiar controls, sensible labels, and concise feedback.

## Write for the Product, Not the Prompt

Translate the user's request into end-user language:

- For a social network, write like a place where people post, follow, react, discover, message, and return.
- For a finance app, write like a tool for confidence, decisions, balances, budgets, forecasts, or payments.
- For a restaurant site, write like a guest choosing a table, menu, time, or experience.
- For a productivity app, write like a person trying to finish work, remember what matters, or decide what to do next.
- For a dashboard, write like an operator scanning status, exceptions, trends, and actions.
- For a landing page, write like a customer deciding whether this product solves their problem.

Visible text should answer user concerns:

- What can I do here?
- Why should I care?
- What changed?
- What needs my attention?
- What is the next useful action?

## Bad Patterns to Remove

Avoid these visible copy patterns:

- "A simple app to..."
- "A modern web app for..."
- "A mobile-first social network"
- "A responsive dashboard that lets users..."
- "An AI-powered tool for..."
- "Track your tasks with this clean interface"
- "This app helps you..."
- "Welcome to your new X app"
- "Built with React/Vite/Tailwind"
- "Demo dashboard"
- "Prototype"
- "MVP"
- "Feature-rich"
- "User-friendly"
- "Here you can..."
- "Use this page to..."
- "The app provides..."

These phrases often reveal that Codex is narrating the assignment instead of designing the product.

## Better Direction

Replace meta descriptions with product-native copy.

Examples:

- User asks: "Make a simple mobile-first app for a social network."
  - Do not write: "A simple mobile-first social network."
  - Prefer: "Catch up with your circle", "What's happening nearby?", "Share a moment", "Find people worth following."

- User asks: "Make a dashboard for sales analytics."
  - Do not write: "A dashboard for sales analytics."
  - Prefer: "Revenue pulse", "Pipeline at risk", "Deals needing attention", "Forecast confidence."

- User asks: "Build a simple app to manage invoices."
  - Do not write: "A simple app to manage invoices."
  - Prefer: "Get paid on time", "Invoices due this week", "Send reminder", "Mark as paid."

- User asks: "Create a mobile-first habit tracker."
  - Do not write: "Mobile-first habit tracker."
  - Prefer: "Keep the streak alive", "Today's rhythm", "Log habit", "Missed yesterday."

- User asks: "Make a restaurant website."
  - Do not write: "A modern restaurant website."
  - Prefer: the restaurant name, "Tonight's tables", "Seasonal menu", "Book a table", "Private dining."

## Interface Copy Standards

- Titles: Name the product, section, user outcome, object, or current state. Do not name the assignment.
- Subtitles: Add context only when it changes user understanding or decision-making.
- Buttons: Use direct verbs tied to real actions: "Post", "Book", "Pay", "Save", "Invite", "Compare", "Resume", "Send reminder".
- Empty states: Explain what is missing and offer one useful next action. Avoid describing the feature.
- Navigation: Use user-recognizable nouns and destinations, not internal modules.
- Cards: Lead with the object or outcome, then the useful detail.
- Forms: Use labels users would naturally expect. Keep helper text short and situational.
- Errors: State what happened and what the user can do next. Do not mention stack traces, validation libraries, or implementation details.
- Success states: Confirm the user outcome, not the system process.

## Design Standards

- Make the first screen immediately useful, not explanatory.
- Use visual hierarchy to communicate priority instead of long descriptive text.
- Keep UI language concise but not generic.
- Make the interface feel specific to the product domain.
- Prefer real-looking data, labels, states, and flows over abstract placeholders.
- Make controls self-evident through placement, labels, and familiar patterns.
- Avoid marketing copy inside operational tools unless the surface is actually promotional.
- Avoid tutorial-like prose in primary screens.

## Pre-flight Check

Before considering frontend work complete, inspect all visible copy and ask:

1. Could this sentence have been generated by reading the user's prompt? If yes, rewrite it.
2. Does this mention the app type, implementation, or design constraint? If yes, remove it unless essential to the user.
3. Would a real user expect to see this in a shipped product? If no, rewrite it.
4. Does this help the user decide, act, understand status, or feel oriented? If no, cut it.
5. Is the UI explaining itself because the design is unclear? If yes, improve the affordance instead of adding prose.

## Required Behavior

When this skill applies, actively revise visible UI text and design choices toward user-facing product language. If existing code contains prompt-facing copy, replace it as part of the frontend work even if the user did not explicitly ask for copywriting.

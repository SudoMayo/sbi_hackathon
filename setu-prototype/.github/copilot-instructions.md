# Copilot Instructions: Setu

Read this fully before writing any code. This file is your shared context for every file in this repo. VS Code Copilot Chat and inline suggestions should follow this as the source of truth for what we are building and why.

## What we are building

Setu (Sanskrit for "bridge") is an agentic AI mesh built for the SBI Hackathon at GFF 2026, Customer Acquisition Track.

The core idea: SBI's app cannot reach the next 200 million customers, but SBI's Business Correspondent (BC) network already can. Setu turns that human network into an AI-augmented customer acquisition channel by giving it nine small, specialised agents instead of one big chatbot.

The problem it solves:
- In semi-urban and rural India, the barrier to banking is trust in a person, not app usability.
- Manual KYC, inconsistent BC scripts, and silent onboarding drop-offs quietly lose acquisitions.
- Acquisition, adoption, and engagement are currently three disconnected efforts. Setu makes them one continuous, learning pipeline.

## The nine agents (this is the system we are coding)

1. **Orchestrator agent** — owns shared state, routes tasks to every other agent. This is the entry point of the pipeline.
2. **Life-event agent** — detects a financial or life signal that means someone is ready to be acquired (e.g. a seasonal transaction pattern suggesting crop-insurance season).
3. **Product-fit agent** — picks exactly one relevant product offer for that person, never a broadcast of many.
4. **Channel-segmentation agent** — decides the right channel for this person: BC home visit, app/IVR nudge, or branch referral.
5. **Compliance and consent agent** — a hard gate. Every action must pass RBI and DPDP checks here before it can fire. Nothing skips this agent.
6. **Vernacular conversation agent (copilot)** — dialect-aware voice guidance for BC-assisted and IVR interactions.
7. **BC field copilot agent** — gives the Business Correspondent a live script, document checks, and CBS auto-fill during the actual visit.
8. **Drop-off recovery agent** — detects a stalled onboarding and schedules a human follow-up.
9. **Feedback and learning agent** — closes the loop by tracking what actually converted and retraining the upstream agents (life-event, product-fit, channel).

## Process flow (build this exact flow)

```
Transaction signals ─┐
BC field activity   ─┼──> Orchestrator agent ──> Life-event agent
App usage data       ─┘                      ──> Product-fit agent
                                              ──> Channel-segmentation agent
                                                        │
                                                        v
                                          Compliance and consent gate (RBI + DPDP)
                                                        │
                                                        v
                                Vernacular copilot + BC field agent execute:
                                BC home visit | App/IVR nudge | Branch referral
                                                        │
                                                        v
                                        Feedback agent learns + retrains
                                        the orchestrator, life-event, and
                                        product-fit agents
```

Drop-off recovery watches the execution step and re-enters the loop if onboarding stalls.

## Non-negotiable design rules

- **Compliance is a hard gate, not a checklist.** No action reaches a customer, BC, or channel without passing through the compliance agent first. Do not let any code path bypass it, even in test/demo mode — instead, make the compliance agent's rules configurable/mockable.
- **One offer, one channel.** The product-fit and channel agents each return a single decision, not a ranked list or multiple options, in line with the pitch's "one relevant offer, not a shotgun of five."
- **Every agent should be independently runnable and testable.** This mirrors the pitch's incremental build-and-demo story — we should always be able to demo whatever subset of agents currently works.
- **Consent and audit logging is mandatory on every autonomous action.** Log what was decided, why, and by which agent.

## Tech stack for the prototype (assumption, confirm or override)

Python was chosen because most agentic/LLM orchestration tooling is Python-first. If you'd rather use Node/TypeScript, say so and Copilot instructions/scaffold should be updated accordingly.

- **Backend / orchestration:** Python 3.11+, FastAPI for a lightweight API layer
- **Agent logic:** plain Python classes for now (no heavy framework yet) so the architecture stays visible; can later swap in LangGraph/CrewAI style orchestration if needed
- **LLM calls:** Anthropic API (`anthropic` Python SDK) for reasoning/vernacular agents
- **Rules engine:** plain Python for compliance agent v1 (deterministic rules), not an LLM, since compliance must be auditable and predictable
- **Data:** local JSON/SQLite for the prototype; no real core banking system (CBS) integration, CBS auto-fill is mocked
- **Frontend/dashboard:** keep out of scope for week 1 to 3; add a minimal dashboard in week 4 per the 30-day plan

## 30-day build order (follow this sequence, do not skip ahead)

1. **Week 1:** Orchestrator agent + Compliance and consent agent. These are the backbone. Get a signal in, routed, and gated, even with stub logic everywhere else.
2. **Week 2:** One live vertical end to end — life-event agent + product-fit agent wired to a single flow (example: a savings-account trigger).
3. **Week 3:** Vernacular BC copilot — voice-guided onboarding conversation (start in Hindi), document verification, CBS form auto-fill (mocked).
4. **Week 4:** Live dashboard that visibly shows the compliance agent evaluating and blocking a non-compliant action in real time. This is the demo moment.

## What Copilot should do

- When asked to scaffold an agent, generate a class with a clear `handle(...)` or `decide(...)` method, type hints, a docstring restating that agent's single job from the list above, and a TODO for the real logic.
- When asked about compliance, always err toward stricter, auditable, logged behavior.
- Do not invent new agents beyond the nine listed unless explicitly asked.
- Do not wire in a real CBS, RBI, or DPDP integration; these are mocked for the prototype. Keep mock boundaries clearly marked with `# MOCK:` comments.
- Prefer small, readable, demo-friendly code over premature optimization. This is a hackathon prototype with a hard 30-day and jury-demo deadline.

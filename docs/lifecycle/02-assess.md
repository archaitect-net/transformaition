# Stage 2: Assess

> **Who this is for:** Programme leads, IT, data, security, privacy, legal and risk professionals, and sponsors deciding whether to proceed.
> **Last reviewed:** 2026-10

Assess answers two questions: are we ready to adopt AI for these opportunities, and what are the risks? It turns a shortlist of problem-framed opportunities into documented positions on organisational readiness, data, risk and legal obligations, so that each opportunity can be marked proceed, proceed with conditions, or stop. Done well, Assess is proportionate: a low-risk internal drafting aid needs a short checklist, while a tool that influences decisions about people needs full risk and data protection assessments.

## Purpose

- Establish whether the organisation has the foundations (skills, data, technology, governance) to support each opportunity.
- Identify risks to people, the organisation and third parties, and decide how they will be treated.
- Determine which legal and regulatory obligations apply.
- Set the conditions any later tool selection and pilot must meet.

## Inputs

- The shortlist and problem statements from [Discover](01-discover.md).
- Shadow AI findings and interim guidance.
- Existing policies: information security, data protection, records management, procurement, acceptable use.
- Existing risk appetite statement and risk register, if you have them.

## Activities

1. **Triage each opportunity by risk.** Use a short screening questionnaire to sort opportunities into tiers before investing effort. Typical triggers for a higher tier: personal or special category data; outputs that influence decisions about individuals (hiring, credit, access to services); customer-facing outputs; regulated activities; autonomous actions (the tool can send, change or delete things); and use cases that may fall into a regulated category such as an EU AI Act high-risk area (see [regulation overview](../governance/regulation-overview.md)).
2. **Assess organisational readiness.** Use the [organisational readiness assessment](../../assessments/organisational-readiness.md) across strategy, data, people, technology and governance. The output is a list of gaps, each with an owner and a decision on whether it blocks progress.
3. **Assess data readiness.** For each opportunity, use the [data readiness assessment](../../assessments/data-readiness.md). Key questions: where does the needed data live; is it accurate and current; who can access it; do permissions in source systems reflect who *should* see what (AI search tools surface whatever a user can technically access, so over-broad permissions become visible quickly); and what classification applies.
4. **Assess risk.** Run the [AI risk assessment](../../assessments/ai-risk-assessment.md) for each opportunity at a depth that matches its tier. Consider harms to individuals (unfairness, privacy, errors), the organisation (security, reputation, legal) and society. The [risk management](../governance/risk-management.md) page explains how this maps to the NIST AI RMF and ISO/IEC 23894.
5. **Assess legal and regulatory position.** Identify which laws apply in your jurisdictions and sector: data protection (lawful basis, DPIA need, automated decision-making rules; see [data protection](../governance/data-protection.md)), AI-specific regulation (for example the EU AI Act, including the AI literacy duty that has applied since 2 February 2025 [1]), employment law and consultation duties, intellectual property and confidentiality (see [intellectual property](../governance/intellectual-property.md)), and sector rules.
6. **Assess security.** Identify threats specific to the tool type, such as prompt injection and data leakage, using the [security](../governance/security.md) page.
7. **Consult affected groups.** Where a use case affects staff or the public, involve them or their representatives. In the EU, an employer deploying a high-risk AI system in the workplace must inform workers' representatives and affected workers before use [2].
8. **Decide and set conditions.** For each opportunity, record proceed, proceed with conditions (for example, "no customer personal data in pilot"; "DPIA must be completed before pilot"), or stop. Conditions become requirements in [Select](03-select.md) and [Pilot](04-pilot.md).

### Proportionate assessment by tier

| Tier | Example | Minimum assessment |
|---|---|---|
| Low | General drafting aid using no confidential or personal data | Screening questionnaire; data terms check; acceptable use policy applies |
| Medium | Summarising internal documents containing some personal data; coding assistant on proprietary code | Screening; data readiness; AI risk assessment; DPIA screening; security review |
| High | Tool influencing decisions about individuals; customer-facing outputs; regulated activity; agentic actions on live systems | Full AI risk assessment; DPIA; legal review; security threat model; consultation; governance board decision |

## Roles involved

| Role | Contribution |
|---|---|
| AI governance lead or group | Coordinates; applies tiering; records decisions |
| Business owner | Explains the use case; owns conditions |
| Data protection officer or privacy lead | DPIA screening and DPIAs; lawful basis |
| Security | Threat assessment and control requirements |
| Legal | Regulatory, contractual, IP and employment questions |
| Risk and compliance | Risk assessment method; alignment with risk appetite |
| Data and analytics | Data readiness, quality and access |
| IT and platform | Technical readiness, integration, identity and access |
| HR and workers' representatives | Workforce impacts and consultation duties |
| Executive sponsor | Accepts residual risk or escalates |

## Outputs and deliverables

- Completed readiness, data readiness and risk assessments per opportunity, at the depth its tier requires.
- DPIA screening results and, where needed, DPIAs started or completed.
- A legal and regulatory obligations summary per opportunity.
- A decision log: proceed, proceed with conditions, or stop, with reasons.
- A readiness action plan for organisational gaps.

## Decision gate: ready to move to Select?

- [ ] Every shortlisted opportunity has a risk tier.
- [ ] Assessments have been completed to the depth each tier requires.
- [ ] Data sources, classifications and access permissions are understood for each opportunity.
- [ ] Applicable legal and regulatory obligations are identified, with owners.
- [ ] DPIA need is determined; required DPIAs are under way.
- [ ] Residual risks are within appetite, or accepted by someone with the authority to do so.
- [ ] Conditions for selection and pilot are written down.
- [ ] Blocking readiness gaps have an owner and a plan.

## Linked assessments and toolkits

- [Organisational readiness](../../assessments/organisational-readiness.md)
- [Data readiness](../../assessments/data-readiness.md)
- [AI risk assessment](../../assessments/ai-risk-assessment.md)
- [AI policy template](../../toolkits/ai-policy-template.md): if you do not yet have a policy, Assess is a good time to draft one.
- [RACI template](../../toolkits/raci-template.md)

## Variations by organisation size

**Small organisations.** Combine the assessments into one short document per use case. Focus on three things: what data the tool will see, what the supplier's terms say about that data, and what happens if the output is wrong. Take external advice for anything involving decisions about individuals or regulated activity.

**Enterprises.** Integrate AI assessment into existing processes (privacy, security architecture review, third-party risk, model risk management) rather than building a parallel track. A single intake form that routes to each specialist function reduces delay. Set service levels for assessment turnaround, or shadow AI will grow while people wait.

## Common pitfalls

- **One-size-fits-all assessment.** Applying the full process to every low-risk idea creates a backlog and drives shadow use.
- **Assessing the tool, not the use.** The same tool can be low-risk for drafting newsletters and high-risk for screening job applicants.
- **Ignoring permissions hygiene.** Over-shared files and sites become a data leakage route once an AI assistant can search them.
- **Leaving legal until procurement.** Discovering late that a use needs a DPIA or worker consultation can delay a pilot by months.
- **No one accepts residual risk.** Assessments that end with "risks noted" but no named decision-maker stall at the gate.

## Sources

1. Regulation (EU) 2024/1689 (AI Act), Article 4, as amended by Regulation (EU) 2026/1744; summary of application dates. ActuIA, *AI Act: obligations in force and delays under omnibus 2026/1744*, 2026. https://www.actuia.com/en/news/ai-act-obligations-in-force-and-delays-under-omnibus-2026-1744/
2. European Commission AI Act Service Desk, *Article 26: Obligations of deployers of high-risk AI systems*. https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26

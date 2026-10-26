# Stage 5: Scale

> **Who this is for:** Programme and change leads, IT and platform teams, learning and development, managers, and governance leads responsible for wider rollout.
> **Last reviewed:** 2026-10

Scale takes a tool that has passed its pilot and makes it available to the wider population it was intended for, with the enablement, support and governance that make adoption safe and useful. Scaling is mostly a change management exercise: technical deployment is often the easy part, while building skills, adjusting processes, keeping controls working at volume and sustaining engagement take longer. This page sets out a rollout workflow, enablement and support models, governance at scale, and the gate for handing over to routine operation.

## Purpose

- Deploy the tool to the intended users in a controlled way.
- Equip people to use it well and safely.
- Provide support that scales.
- Extend governance (policy, monitoring, use case control) to the larger user base.
- Realise and measure the benefits set out in the business case.

## Inputs

- Go decision and conditions from [Pilot](04-pilot.md).
- Pilot evaluation report and rollout recommendations.
- Updated risk assessment and DPIA.
- Business case and measurement plan.

## Activities

1. **Plan the rollout.** Decide the sequence (by function, location or role), timing, and criteria for moving from one wave to the next. Phased rollouts allow learning between waves; a single launch may suit small organisations.
2. **Prepare the platform.** Provision licences, configure access groups, data sources, connectors and admin controls according to the pilot's findings. Fix data permission problems found during the pilot before widening access.
3. **Communicate.** Explain why the tool is being introduced, what it is for, what it is not for, what rules apply and where to get help. Address concerns about jobs and monitoring directly and honestly. Use the [communication plan template](../../toolkits/communication-plan-template.md).
4. **Enable people.** Deliver role-based training (see below), share a curated [prompt library](../../toolkits/prompt-library-template.md), and set up a champions network.
5. **Stand up support.** Define how users get help, how issues are triaged, and how output-quality or data incidents are escalated.
6. **Extend governance.** Publish the [acceptable use policy](../../toolkits/acceptable-use-policy.md), update the [use case register](../../toolkits/use-case-register-template.md), and define how new use cases of the same tool are approved.
7. **Measure.** Track adoption, value and risk indicators per wave; compare with the business case. See [measuring value](../measurement/measuring-value.md).
8. **Adjust between waves.** Review data from each wave and change training, configuration or communications before the next.
9. **Hand over to operations.** Agree ownership, service levels, monitoring and review cycles with the teams who will run the tool in [Operate](06-operate.md).

## Enablement

AI literacy is a legal obligation for some organisations, not only good practice. Under the EU AI Act, providers and deployers of AI systems must take measures to support AI literacy among their staff and others using AI systems on their behalf. This has applied since 2 February 2025; the 2026 amending regulation reworded the duty so that it does not require any particular level of literacy for each individual, but it remains in force [1][2]. Organisations outside the EU's reach may still find the obligation a useful benchmark.

A layered approach works for most organisations:

| Layer | Audience | Content |
|---|---|---|
| Foundation | Everyone with access | What the tool does; limitations including fabricated outputs; data rules; verifying outputs; reporting issues |
| Role-based | Specific roles or functions | Worked examples for that role's tasks; prompts; review steps |
| Advanced | Champions, power users, builders | Configuration, custom assistants, evaluation, sharing good practice |
| Leaders and managers | People managers | Setting expectations, recognising good use, handling concerns, not using tool data for unplanned performance monitoring |

See the [training plan template](../../toolkits/training-plan-template.md) and the [people and learning pathway](../pathways/people-and-learning.md).

### Champions networks

Champions are users in each team who receive extra training, share practices and act as a first point of contact. Practitioner consensus is that peer support helps adoption; give champions protected time and a channel to feed problems back to the programme.

## Support model

| Tier | Handles | Typical owner |
|---|---|---|
| Self-service | Guidance pages, FAQs, prompt library, training recordings | Programme team |
| Peer | How-to questions, good practice | Champions |
| Service desk | Access, licensing, technical faults | IT service desk |
| Specialist | Output-quality issues, data or security incidents, policy questions | Platform team, security, data protection, governance lead |

Define what counts as an AI incident (for example, sensitive data exposed through the tool; harmful or discriminatory output; output relied upon that caused an error) and how it is escalated. See [Operate](06-operate.md) for incident management.

## Governance at scale

- **Use case control.** A general-purpose tool will be used for new purposes. Decide which uses are pre-approved, which need registration, and which need fresh assessment (for example, anything that influences decisions about individuals).
- **Policy.** Publish and acknowledge the acceptable use policy; link it from the tool where possible.
- **Monitoring.** Use admin and audit capabilities to monitor adoption and detect policy breaches, within the limits set by your employee monitoring policy and data protection law.
- **Data hygiene.** Continue reviewing permissions on content the tool can access.
- **Reporting.** Report adoption, value, incidents and risks to the governance group at an agreed frequency.

## Roles involved

| Role | Contribution |
|---|---|
| Programme or change lead | Plans waves; coordinates communication and enablement |
| IT and platform | Provisioning, configuration, admin controls |
| Learning and development | Training design and delivery |
| Managers | Set expectations; support teams |
| Champions | Peer support and feedback |
| Service desk | First-line support |
| Governance lead | Policy, use case control, reporting |
| Security and data protection | Monitoring and incident response |
| HR and workers' representatives | Workforce communications; consultation |
| Executive sponsor | Visible sponsorship; removes blockers |

## Outputs and deliverables

- Rollout plan and wave criteria.
- Configured platform and access model.
- Communications and training delivered; champions network in place.
- Support model operating with defined escalation.
- Published policy and updated use case register.
- Adoption, value and risk reports per wave.
- Signed-off handover to operations.

## Decision gate: ready to move to Operate?

- [ ] All intended users have access and completed foundation training.
- [ ] Support model operating; incident route tested.
- [ ] Acceptable use policy published and acknowledged.
- [ ] Monitoring and reporting in place.
- [ ] Use case control process defined for new uses of the tool.
- [ ] Benefits tracking active against the business case.
- [ ] Operational owner, service levels and review cycle agreed.

## Linked assessments and toolkits

- [Communication plan template](../../toolkits/communication-plan-template.md)
- [Training plan template](../../toolkits/training-plan-template.md)
- [Acceptable use policy](../../toolkits/acceptable-use-policy.md)
- [Prompt library template](../../toolkits/prompt-library-template.md)
- [Use case register](../../toolkits/use-case-register-template.md)
- [AI maturity model](../../assessments/maturity-model.md): reassess after rollout.

## Variations by organisation size

**Small organisations.** Rollout may simply be giving everyone access after a team session, with a shared document of rules and good prompts. One person should still own the tool, its settings and the supplier relationship.

**Enterprises.** Expect multiple waves over months, localised communications and training, coordination with works councils, and integration with existing IT service management. Consider a central enablement team plus federated champions.

## Common pitfalls

- **"Launch and leave".** Access without enablement often leads to low adoption or risky use.
- **Training only on features.** People need examples from their own work, and practice in verifying outputs.
- **Scaling before permissions are fixed.** Over-shared content becomes visible to more people.
- **Silence on job concerns.** Uncertainty fuels resistance; be honest about what is and is not planned.
- **Using usage data for performance management without warning.** This damages trust and may breach data protection and employment law.
- **No benefits tracking.** Without measurement, renewal decisions become guesswork.

## Sources

1. ActuIA, *AI Act: obligations in force and delays under omnibus 2026/1744*, 2026 (summary of Regulation (EU) 2026/1744 amending Article 4 of Regulation (EU) 2024/1689). https://www.actuia.com/en/news/ai-act-obligations-in-force-and-delays-under-omnibus-2026-1744/
2. KI-Campus, *EU AI Act: AI Omnibus recalibrates Article 4 – AI literacy remains mandatory*, 2026. https://ki-campus.org/en/blog/eu-ai-act-ai-omnibus-recalibrates-article-4-ai-literacy-remains-mandatory

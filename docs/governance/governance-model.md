# Governance model

> **Who this is for:** Executives, governance leads, company secretaries, risk and compliance teams, and owners of small organisations deciding how AI decisions will be made.
> **Last reviewed:** 2026-10

A governance model answers four questions: who sets direction for AI use, who decides whether a specific use may proceed, who is accountable when something goes wrong, and which rules apply. This page describes common structures, core roles, a decision-rights matrix, and a policy hierarchy, with versions scaled for small, mid-sized and large or regulated organisations. It draws on the management-system approach of ISO/IEC 42001 and the Govern function of the NIST AI RMF, without requiring you to adopt either formally.

## Principles of a workable model

- **Proportionate.** Governance effort should scale with risk. Low-risk uses should have a fast path.
- **Integrated.** Use existing structures (risk committee, information governance, architecture review, privacy and security processes) wherever possible, rather than creating a parallel bureaucracy.
- **Clear decision rights.** Every type of decision has one accountable owner.
- **Documented.** Decisions and their reasons are recorded, so they can be reviewed and explained.
- **Reviewed.** The model itself is reviewed periodically as AI use and law change.

The NIST AI RMF places "Govern" as a cross-cutting function that informs the other three (Map, Measure, Manage), covering policies, accountability structures, workforce diversity and culture, and engagement with affected parties [1]. ISO/IEC 42001 specifies requirements for an AI management system, using the Plan-Do-Check-Act approach common to other ISO management system standards [2]. Organisations already certified to ISO/IEC 27001 often find the structure familiar.

## Common structures

| Structure | Description | Fits | Watch for |
|---|---|---|---|
| Named owner | One accountable individual, with advice from others as needed | Small organisations; early stages | Single point of failure; conflicts of interest |
| Cross-functional working group | Representatives from business, IT, security, data protection, legal, HR meeting regularly | Mid-sized organisations; growing use | Can lack authority unless chartered by leadership |
| AI governance board or committee | Formal body with terms of reference, reporting to executive or board risk committee | Large or regulated organisations; high-risk uses | Can become a bottleneck; needs a fast path for low-risk uses |
| Hub and spoke | Central team sets standards and handles high-risk cases; business units handle routine approvals | Large, federated organisations | Consistency between spokes |
| Integration into existing committees | AI added to the remit of risk, data or technology committees | Organisations with strong existing governance | AI issues may get crowded out |

## Core roles

| Role | Responsibilities | Small-organisation equivalent |
|---|---|---|
| Board or governing body | Sets risk appetite; oversees strategy; receives reports on significant AI risks | Owners or directors |
| Executive sponsor | Accountable for the AI programme and its outcomes | Managing director |
| AI governance lead | Runs the governance process: register, assessments, policy, reporting | Operations or IT lead, part-time |
| Governance board or group | Decides on higher-risk uses; approves policy; reviews incidents and metrics | Directors' meeting agenda item |
| Use case (business) owner | Accountable for a specific use: its value, appropriate use and controls | Team lead |
| System or platform owner | Accountable for a tool's configuration, vendor relationship and operations | IT lead or external provider |
| Data protection officer or privacy lead | Advises on data protection; DPIAs; monitors compliance. Some organisations are legally required to appoint a DPO under GDPR or UK GDPR | External adviser |
| Security lead | Threat assessment; security controls; incident response | IT provider |
| Legal | Regulatory interpretation; contracts; IP; employment | External counsel as needed |
| HR and learning | Workforce impacts; training; consultation; policy for staff use | Owner or office manager |
| Champions | Peer support; feedback from front line | Enthusiastic team members |

## Decision rights

Decide in advance who can approve what. The matrix below is a starting point; adapt the thresholds to your risk tiers (see [AI risk assessment](../../assessments/ai-risk-assessment.md)).

| Decision | Low-risk use | Medium-risk use | High-risk use |
|---|---|---|---|
| Approve a new use case | Business owner, within acceptable use policy | Governance lead, after assessment | Governance board, after full assessment |
| Approve a new tool | System owner plus security and data protection checks | Governance group | Governance board; executive approval for spend |
| Accept residual risk | Business owner | Executive sponsor | Executive committee or board risk committee |
| Approve policy | Governance group | Governance group | Executive committee or board |
| Enable a new vendor feature | System owner | System owner after risk check | Governance board |
| Suspend a tool or use | System owner, security lead or DPO (emergency) | Same | Same |
| Retire a tool | System owner and business owner | Governance group | Governance board |

Two rights deserve special attention:

- **Emergency suspension.** Security and data protection leads should be able to suspend a tool or feature immediately when an incident requires it, with review afterwards.
- **Residual risk acceptance.** Risk should be accepted by someone with the authority and budget to treat it, not by the person proposing the use.

## Policy hierarchy

| Level | Document | Purpose | Typical owner | Template |
|---|---|---|---|---|
| 1 | AI principles or statement | Values and commitments | Board or executive | See [responsible AI principles](responsible-ai-principles.md) |
| 2 | AI policy | Scope, roles, decision rights, risk approach, requirements | Executive sponsor | [AI policy template](../../toolkits/ai-policy-template.md) |
| 3 | Acceptable use policy | Rules for staff using AI tools | Governance lead with HR | [Acceptable use policy](../../toolkits/acceptable-use-policy.md) |
| 4 | Standards | Technical and procedural requirements (security baselines, assessment method, evaluation standards) | Security, IT, governance lead | See [security](security.md), [risk management](risk-management.md) |
| 5 | Procedures and guidance | How-to: assessment process, incident playbooks, tool guides | Function owners | [Lifecycle](../lifecycle/README.md), [tool guides](../tools/tool-guides/README.md) |

Link AI policy to existing policies rather than duplicating them: information security, data protection, records management, procurement, equality and diversity, disciplinary and IT acceptable use.

## Scaled models

### Small organisation (under 50 people)

- One accountable director; an adviser for data protection and IT (internal or external).
- A two-page AI policy combined with acceptable use rules.
- A simple register (a spreadsheet) of approved tools and uses.
- AI as a standing item at management meetings, quarterly.
- External legal advice for any use involving decisions about individuals or regulated activity.

### Mid-sized organisation

- Executive sponsor plus a part-time governance lead.
- Cross-functional working group meeting monthly, chartered by the executive team.
- Separate AI policy and acceptable use policy; assessment templates.
- Use case register with risk tiers; quarterly reporting to the executive.

### Large or regulated organisation

- Board-level oversight through an existing risk or technology committee.
- AI governance board with terms of reference, chaired at executive level.
- Central AI governance function plus business unit leads (hub and spoke).
- Full policy hierarchy, integrated with model risk management, third-party risk and privacy.
- Consider alignment with or certification to ISO/IEC 42001.
- Regulatory mapping per jurisdiction and sector; see [regulation overview](regulation-overview.md).

## Terms of reference checklist for a governance group

- [ ] Purpose and scope (which AI uses and tools are covered).
- [ ] Membership, chair and quorum.
- [ ] Decision rights and escalation route.
- [ ] Meeting frequency and fast-path arrangements between meetings.
- [ ] Inputs (register, assessments, incidents, metrics) and outputs (decisions, reports).
- [ ] Reporting line to the executive or board.
- [ ] Conflict of interest handling.
- [ ] Review date for the terms of reference.

## Common pitfalls

- **Governance as a blocker.** If approval takes months, people will use unapproved tools.
- **No business ownership.** Governance owned only by IT or legal tends to miss value and context.
- **Committees without data.** Decisions need the register, assessments and metrics.
- **Policy without enforcement or training.** Rules that people do not know about do not reduce risk.
- **Ignoring AI features in existing software.** Many tools gain AI features through updates; governance must cover them.

## Sources

1. National Institute of Standards and Technology, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, January 2023. https://www.nist.gov/itl/ai-risk-management-framework
2. International Organization for Standardization, *ISO/IEC 42001:2023 Artificial intelligence — Management system*, December 2023. https://www.iso.org/standard/42001

# IT and platform pathway

> **Who this is for:** IT managers, infrastructure and end-user computing teams, identity and access specialists, enterprise and solution architects, platform engineers, and the person who "looks after IT" in a small organisation.
> **Last reviewed:** 2026-10

IT and platform teams make AI adoption possible and safe. You provide access to approved tools, connect them to the organisation's identity, data and systems, configure the controls that stop data going where it should not, monitor use and cost, and deal with the tools people adopt without asking. This pathway covers identity, licensing, integration, data controls, monitoring and shadow AI, with a reading route through the guide. It assumes general IT knowledge but no AI specialism.

## What AI adoption means for IT and platform teams

- **AI tools inherit your existing access model, for better or worse.** Assistants embedded in productivity suites can typically reach whatever the user can reach. If file permissions are too broad, AI makes overshared content easier to find.
- **The attack surface changes.** AI tools that read external content and take actions are exposed to prompt injection, which the UK National Cyber Security Centre has said may never be fully mitigated, so the focus must be on limiting impact [1]. Baseline controls are set out in joint guidelines from the NCSC, the US Cybersecurity and Infrastructure Security Agency (CISA) and international partners, covering secure design, development, deployment, and operation and maintenance [2], and in the UK government's voluntary code of practice for the cyber security of AI, which has 13 principles [3]. See [security](../governance/security.md).
- **AI arrives through many doors.** Not just new purchases, but features added to existing software, browser extensions, personal accounts, and developer use of model APIs.
- **Costs behave differently.** Per-seat licences are predictable; usage-based pricing for APIs and agents is not. Agentic workflows can consume large volumes of tokens.
- **The pace of change is high.** Vendors frequently add capabilities, rename products and change defaults. Configuration needs ongoing review, not one-off setup.

## Your key responsibilities and decisions

### Identity and access

| Control | Why it matters | Questions to settle |
|---|---|---|
| Single sign-on (SSO) for all approved AI tools | Central control of who has access, and fast removal when people leave | Does the tool support your identity provider at the tier you are buying? |
| Role- or group-based licence assignment | Lets you stage rollout and match tools to roles | Who approves access? |
| Multi-factor authentication | Protects accounts that may hold sensitive conversation history | Enforced through your identity provider? |
| Permissions for agents and connectors | Agents act with the permissions they are given | Can you restrict scopes? Do agents use the user's identity or a service identity? |
| Least privilege for integrations | Limits harm from errors or prompt injection | What is the minimum access each integration needs? |

### Licensing and commercial

- Compare per-user licences, usage-based billing and bundled features against expected usage patterns.
- Check what each tier includes: admin controls, audit logs, data retention settings, data residency, and contractual commitments on training use of your data. These often differ significantly between consumer, business and enterprise tiers.
- Plan for licence reclamation from inactive users.
- Work with procurement and legal using the [vendor due diligence](../../assessments/vendor-due-diligence.md) assessment.

### Integration

- **Connectors and protocols.** Many tools connect to file stores, email, ticketing and databases, often via standard protocols such as the Model Context Protocol. Maintain an inventory of what is connected to what, and with which permissions.
- **Build versus buy.** Decide when to use a tool's built-in features, when to use a cloud AI platform, and when (rarely, for most organisations) to self-host models. See [what are AI tools?](../foundations/what-are-ai-tools.md#deployment-models).
- **Architecture patterns.** For internal applications, consider routing model access through a central gateway that handles authentication, logging, cost allocation, content filtering and model choice.

### Data controls

| Control | Purpose |
|---|---|
| Fix oversharing before enabling suite-wide assistants | Prevents AI surfacing content users can technically access but should not see |
| Sensitivity labels and classification | Lets tools respect data handling rules |
| Data loss prevention (DLP) policies covering AI tools and browser use | Detects or blocks sensitive data being pasted into unapproved tools |
| Retention and deletion settings for prompts, outputs and logs | Aligns with your retention policy and data protection obligations |
| Training-use settings | Ensures your data is not used to train vendor models unless you intend it |
| Data residency settings | Meets contractual or regulatory location requirements |

Coordinate with data protection colleagues; see [data protection](../governance/data-protection.md).

### Monitoring and operations

- Usage, adoption and licence utilisation (feeds [measuring value](../measurement/measuring-value.md)).
- Audit logs of prompts, outputs and agent actions where available and lawful, with access restricted.
- Cost monitoring and alerts for usage-based services.
- Change monitoring: vendor release notes and new default-on features.
- Incident response playbooks updated to cover AI-specific incidents, such as data exposure through an assistant or a compromised agent.

### Shadow AI

Shadow AI is the use of AI tools without the knowledge or approval of IT, security or data owners. It is usually a signal of unmet need, not malice.

| Step | Action |
|---|---|
| **Discover** | Review network, proxy, identity and expense data for AI services; run an anonymous staff survey |
| **Understand** | Find out which tasks people are using unapproved tools for, and why |
| **Provide** | Offer an approved alternative that meets the need, with appropriate controls |
| **Guide** | Publish a clear list of approved, tolerated and prohibited tools, linked from the [acceptable use policy](../../toolkits/acceptable-use-policy.md) |
| **Control** | Block or restrict high-risk services where justified, using DLP and web filtering |
| **Review** | Repeat discovery periodically; new tools appear constantly |

Blocking without providing an alternative tends to push use onto personal devices, where you have no visibility at all.

## Questions you should be asking

- Which AI tools and features are already in use, including features switched on in existing software?
- If we enable an assistant across our productivity suite today, what overshared content would it surface?
- Which tiers of each tool give us SSO, audit logs, retention control and contractual protection on training use?
- What can each agent or integration do, under whose identity, and who approves new connections?
- How will we detect sensitive data going into unapproved tools?
- What is our cost exposure under usage-based pricing, and how will we cap it?
- How will we learn about vendor changes before users do?

## Your reading route

1. **Foundations (30 minutes).** Read [what are AI tools?](../foundations/what-are-ai-tools.md), especially types and deployment models, and the prompt injection section of [capabilities and limitations](../foundations/capabilities-and-limitations.md).
2. **Assess readiness.** Complete the technology sections of [organisational readiness](../../assessments/organisational-readiness.md) and work with data colleagues on [data readiness](../../assessments/data-readiness.md).
3. **Security and data protection.** Read [security](../governance/security.md) and [data protection](../governance/data-protection.md).
4. **Select tools.** Read [Select](../lifecycle/03-select.md), [choosing tools](../tools/choosing-tools.md) and [tool categories](../tools/tool-categories.md). Use [vendor due diligence](../../assessments/vendor-due-diligence.md).
5. **Implement your chosen tools.** Use the relevant [tool guides](../tools/tool-guides/README.md) for configuration, data controls and known limitations. For building on models, see [cloud AI platforms](../tools/tool-guides/cloud-ai-platforms.md) and [open-weight models](../tools/tool-guides/open-weight-models.md).
6. **Support the pilot.** Read [Pilot](../lifecycle/04-pilot.md) for what pilot teams will need from you, including usage data.
7. **Scale and operate.** Read [Scale](../lifecycle/05-scale.md) and [Operate](../lifecycle/06-operate.md) for monitoring, change management and incident response.
8. **Agree roles.** Use the [RACI template](../../toolkits/raci-template.md) to clarify what IT owns versus security, data protection and the business.

## Common pitfalls

| Pitfall | What to do instead |
|---|---|
| Enabling a suite-wide assistant before reviewing permissions | Run an oversharing review and fix the highest-risk sites and folders first |
| Treating the consumer and enterprise versions of a tool as equivalent | Compare tiers on controls and contract terms; standardise on business tiers |
| Blocking everything | Provide an approved alternative and a route to request new tools |
| One-off configuration | Review settings after major vendor releases |
| Broad permissions for agents | Least privilege; human approval for consequential actions; logging |
| Ignoring AI features in existing software | Include feature changes in change management and supplier review |
| Unbounded usage costs | Set budgets, quotas and alerts |

## What good looks like

- An up-to-date inventory of approved AI tools, features, integrations and their data access.
- All approved tools behind SSO and MFA, with licences assigned by group and reclaimed when unused.
- Data controls in place: permissions reviewed, labels applied to sensitive content, DLP covering AI services, retention configured.
- A published list of approved tools and a simple route to request new ones.
- Monitoring of usage, cost and audit logs, with alerts for anomalies.
- A process for tracking vendor changes and re-reviewing configuration.
- For small organisations: business-tier accounts with SSO where available, training-use settings checked, a list of approved tools, and an annual review.

## Sources

1. National Cyber Security Centre, *Prompt injection is not SQL injection*, December 2025. https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection
2. National Cyber Security Centre, CISA and international partners, *Guidelines for secure AI system development*, November 2023. https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development
3. Department for Science, Innovation and Technology, *Code of Practice for the Cyber Security of AI*, January 2025. https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice/code-of-practice-for-the-cyber-security-of-ai

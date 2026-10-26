# Responsible AI principles

> **Who this is for:** Leaders drafting an AI principles statement, governance leads, and risk, compliance and ethics professionals who need to turn principles into practice.
> **Last reviewed:** 2026-10

Many organisations publish responsible AI principles; fewer can show how those principles change what people actually do. This page maps the most widely referenced principle sets (the OECD AI Principles, the UK's five regulatory principles, the EU's trustworthy AI requirements and the AI Act, and the NIST AI RMF trustworthiness characteristics) onto a common set of themes, then shows how to operationalise each theme with concrete controls, owners and evidence. Use it to write principles that are consistent with international frameworks and to check that each principle has teeth.

## Why align with existing frameworks

- **Credibility and interoperability.** Regulators, customers and partners recognise these frameworks. Aligning reduces translation effort in procurement and audits.
- **Regulatory traction.** Some principles are now reflected in law (for example, transparency obligations in the EU AI Act) or used by regulators to interpret existing law (as in the UK's approach).
- **Completeness.** Mapping against several frameworks helps you spot gaps.

## The source frameworks

| Framework | Status | Content |
|---|---|---|
| OECD AI Principles | Intergovernmental recommendation adopted May 2019, updated May 2024 [1] | Five values-based principles: inclusive growth, sustainable development and well-being; human rights and democratic values, including fairness and privacy; transparency and explainability; robustness, security and safety; accountability. Plus five recommendations for policymakers. |
| UK cross-sectoral principles | Non-statutory principles for existing regulators to interpret and apply, confirmed in the government's response of 12 February 2024 [2] | Safety, security and robustness; appropriate transparency and explainability; fairness; accountability and governance; contestability and redress. |
| EU Ethics Guidelines for Trustworthy AI | Non-binding guidelines from the High-Level Expert Group on AI, April 2019 [3] | Seven requirements: human agency and oversight; technical robustness and safety; privacy and data governance; transparency; diversity, non-discrimination and fairness; societal and environmental well-being; accountability. |
| EU AI Act | Binding regulation (EU) 2024/1689, phased application; see [regulation overview](regulation-overview.md) | Turns several of the above into legal requirements for in-scope systems: risk management, data governance, transparency, human oversight, accuracy, robustness and cybersecurity for high-risk systems; transparency duties for certain systems; AI literacy. |
| NIST AI RMF trustworthiness characteristics | Voluntary US framework, AI RMF 1.0, January 2023 [4] | Valid and reliable; safe; secure and resilient; accountable and transparent; explainable and interpretable; privacy-enhanced; fair, with harmful bias managed. |

## Crosswalk

The table maps each framework to eight common themes. Wording differs, and the mapping is approximate: it is a practical aid, not an official correspondence.

| Theme | OECD | UK principles | EU HLEG | NIST AI RMF |
|---|---|---|---|---|
| Benefit and well-being | Inclusive growth, sustainable development and well-being | (Implicit in proportionality) | Societal and environmental well-being | (Context in Map function) |
| Human rights, fairness and non-discrimination | Human rights and democratic values, including fairness and privacy | Fairness | Diversity, non-discrimination and fairness | Fair, with harmful bias managed |
| Privacy and data governance | (Within human rights principle) | (Via data protection law) | Privacy and data governance | Privacy-enhanced |
| Transparency and explainability | Transparency and explainability | Appropriate transparency and explainability | Transparency | Accountable and transparent; explainable and interpretable |
| Safety, security and robustness | Robustness, security and safety | Safety, security and robustness | Technical robustness and safety | Valid and reliable; safe; secure and resilient |
| Human oversight | (Within human rights and robustness principles) | (Within accountability and governance) | Human agency and oversight | (Within Govern and Manage functions) |
| Accountability | Accountability | Accountability and governance | Accountability | Accountable and transparent |
| Contestability and redress | (Within transparency principle) | Contestability and redress | (Within accountability) | (Within Govern function) |

## From principle to practice

A principle is operational when it has a control, an owner, and evidence that the control works. The table gives examples for organisations adopting AI tools (as opposed to developing models).

| Theme | Example commitments | Controls | Owner | Evidence |
|---|---|---|---|---|
| Benefit | We adopt AI to solve defined problems with measurable outcomes | Problem-first framing; business case; benefits tracking | Business owner | Use case register; value reports |
| Fairness | We check whether AI-influenced outcomes differ unfairly across groups | Risk tiering flags decisions about people; bias testing before and during use; equality impact assessment | Business owner with risk and HR | Test results; monitoring reports |
| Privacy | We use personal data in AI tools only with a lawful basis and appropriate safeguards | DPIA process; data classification rules; vendor data terms checks | DPO or privacy lead | DPIAs; vendor assessments |
| Transparency | People know when AI is used in ways that affect them | Disclosure rules in policy; notices for customers and staff; labelling of AI-generated content where required | Business owner, communications | Notices; policy; audit of outputs |
| Safety and security | AI tools are secured against known threats | Security assessment; OWASP-aligned controls; incident playbooks | Security lead | Threat models; test results; incident logs |
| Human oversight | People remain responsible for decisions and outputs | Defined human review steps; training on verifying outputs; restrictions on autonomous actions | Business owner | Process documentation; sampling of reviews |
| Accountability | Every AI use has a named owner, and decisions are recorded | Register; decision rights; governance reporting | Governance lead | Register; minutes; decision log |
| Contestability | People affected by AI-influenced decisions can challenge them and obtain human review | Complaint and review route; procedures for automated decision safeguards | Business owner with DPO | Procedure; case records |

Contestability is a legal requirement in some cases, for example the safeguards for significant automated decisions under UK GDPR as amended by the Data (Use and Access) Act 2025; see [data protection](data-protection.md).

## Writing your principles: a checklist

- [ ] Five to eight principles, written in plain language for staff and the public.
- [ ] Each principle maps to at least one recognised framework theme (use the crosswalk).
- [ ] Each principle has at least one control, a named owner and an evidence source.
- [ ] Principles cover AI tools you buy, not only systems you build.
- [ ] Principles are approved at board or executive level.
- [ ] Principles are linked from the [AI policy](../../toolkits/ai-policy-template.md) and reflected in the [acceptable use policy](../../toolkits/acceptable-use-policy.md).
- [ ] A review date is set.

## Variations by organisation size

**Small organisations.** Principles can be a short paragraph in your AI policy: for example, "we use AI to help our people, we check its outputs, we protect client data, we are open with clients about how we use it, and a named person is responsible". What matters is that each statement corresponds to something you do.

**Enterprises.** Publish principles externally if customers or regulators expect it, but maintain an internal control mapping. Integrate principles into assessment templates so that each risk assessment asks how each principle is met.

## Common pitfalls

- **Principles without controls.** "Ethics washing" erodes trust when practice diverges from statements.
- **Copying a framework wholesale.** Adapt to your context; not every theme carries equal weight for every organisation.
- **Ignoring trade-offs.** Principles can conflict (for example, transparency and security). Say how conflicts are resolved and by whom.
- **Focusing only on development.** Most organisations deploy rather than build AI; principles must cover procurement and use.

## Sources

1. OECD, *OECD AI Principles overview* (adopted 2019, updated 2024). https://oecd.ai/en/ai-principles
2. Society for Computers and Law, *UK government publishes response to AI White Paper*, February 2024 (summary of the government response of 12 February 2024). https://www.scl.org/uk-government-publishes-response-to-ai-white-paper/
3. European Commission, *Ethics guidelines for trustworthy AI*, High-Level Expert Group on AI, 8 April 2019. https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai
4. National Institute of Standards and Technology, *AI Risk Management Framework*, AI RMF 1.0, January 2023. https://www.nist.gov/itl/ai-risk-management-framework

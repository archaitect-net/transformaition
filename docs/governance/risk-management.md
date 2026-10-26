# Risk management for AI

> **Who this is for:** Risk managers, governance leads, compliance, security and data protection professionals, and business owners responsible for AI use cases.
> **Last reviewed:** 2026-10

This page explains how to manage risks from AI tools using recognised frameworks: the NIST AI Risk Management Framework (AI RMF 1.0), its Generative AI Profile (NIST AI 600-1), ISO/IEC 23894 (guidance on AI risk management) and ISO/IEC 42001 (AI management systems). It summarises what each is, how they relate, and gives a practical, proportionate risk process you can run for each use case, with a risk catalogue tailored to generative AI tools. You do not need to adopt any framework formally to benefit; most organisations borrow structure and vocabulary and integrate AI risk into their existing enterprise risk process.

## The frameworks at a glance

| Framework | Publisher and status | What it is | Use it for |
|---|---|---|---|
| NIST AI RMF 1.0 (NIST AI 100-1) | US National Institute of Standards and Technology; released 26 January 2023; voluntary. NIST states that it is being revised as part of the White House AI Action Plan [1] | A framework built around four functions (Govern, Map, Measure, Manage) and seven trustworthiness characteristics | Structure and vocabulary for an AI risk programme; free to use |
| NIST AI 600-1, Generative AI Profile | NIST; released 26 July 2024; voluntary [1][2] | A companion profile identifying risks that are unique to or worsened by generative AI, with suggested actions mapped to AI RMF functions | Risk catalogue and action list for generative AI tools |
| ISO/IEC 23894:2023 | ISO and IEC; published February 2023 [3] | Guidance for organisations that develop, deploy or use AI on managing AI-specific risk and integrating it into their activities | Aligning AI risk with an ISO-style enterprise risk process |
| ISO/IEC 42001:2023 | ISO and IEC; published December 2023 [4] | Requirements for establishing, implementing, maintaining and continually improving an AI management system (AIMS), using Plan-Do-Check-Act | A certifiable management system for AI governance, alongside ISO/IEC 27001 and similar |

NIST also publishes a companion Playbook, crosswalks to other frameworks, and in April 2026 released a concept note for an AI RMF profile on trustworthy AI in critical infrastructure [1]. Check NIST's site for the revised AI RMF, since it may change the details summarised here.

### How they relate

- **NIST AI RMF and ISO/IEC 23894** are both guidance on *how to manage AI risk*. NIST is free and widely used internationally; ISO/IEC 23894 fits organisations whose risk processes already follow ISO conventions.
- **NIST AI 600-1** adds a generative-AI-specific layer to the AI RMF.
- **ISO/IEC 42001** is a *management system* standard: it specifies what an organisation must have in place (policy, roles, risk assessment, controls, monitoring, improvement) and can be audited. Risk assessment is one component.

A common pattern: use ISO/IEC 42001 (or its structure) for the overall governance system, NIST AI RMF or ISO/IEC 23894 for the risk method, and NIST AI 600-1 as a risk catalogue for generative AI.

## The NIST AI RMF functions

| Function | Purpose | In practice for AI tool adoption |
|---|---|---|
| Govern | Cultivate a risk-aware culture; set policies, roles and accountability | [Governance model](governance-model.md), policy, training, decision rights |
| Map | Establish context; identify risks for a specific system and use | Use case framing, stakeholder analysis, risk identification ([Discover](../lifecycle/01-discover.md), [Assess](../lifecycle/02-assess.md)) |
| Measure | Analyse, assess and track risks using quantitative and qualitative methods | Evaluation, testing, pilot metrics, monitoring ([Pilot](../lifecycle/04-pilot.md), [Operate](../lifecycle/06-operate.md)) |
| Manage | Prioritise and act on risks; respond and recover | Controls, risk treatment, incident response, decommissioning |

The trustworthiness characteristics are: valid and reliable; safe; secure and resilient; accountable and transparent; explainable and interpretable; privacy-enhanced; and fair, with harmful bias managed [1]. See [responsible AI principles](responsible-ai-principles.md) for how these map to other frameworks.

## Generative AI risk catalogue (from NIST AI 600-1)

NIST AI 600-1 identifies twelve risks that are unique to or exacerbated by generative AI [2]. The table lists them with examples relevant to organisations adopting AI tools.

| NIST AI 600-1 risk | What it means | Example in an organisation |
|---|---|---|
| CBRN information or capabilities | Easier access to information that could assist chemical, biological, radiological or nuclear harm | Mostly a model-provider concern; relevant if you build public-facing tools |
| Confabulation | Confident production of false or fabricated content | Invented references in a report; wrong figures in a summary |
| Dangerous, violent or hateful content | Generation of harmful content | Customer-facing chatbot produces offensive replies |
| Data privacy | Leakage or inference of personal data | Assistant surfaces HR data to an unauthorised user |
| Environmental impacts | Energy and resource use | Procurement and sustainability reporting considerations |
| Harmful bias or homogenisation | Unfair outcomes; reduced diversity of outputs | Biased candidate summaries; uniform marketing copy |
| Human-AI configuration | Problems in how people and AI interact, including over-reliance | Staff stop checking outputs; automation bias in decisions |
| Information integrity | Difficulty distinguishing fact from fabricated content; misinformation | AI-generated content published without review |
| Information security | New attack surfaces and lower barriers for attackers | Prompt injection via an email the assistant reads |
| Intellectual property | Infringement risk; exposure of protected material | Generated content reproduces copyrighted text; see [intellectual property](intellectual-property.md) |
| Obscene, degrading or abusive content | Generation of such material | Misuse of image generation tools |
| Value chain and component integration | Risks from third-party models, data and components that are not transparent | Vendor changes underlying model without notice |

Add organisational risks that sit outside this catalogue: regulatory non-compliance, contractual breach, workforce impacts, vendor lock-in, cost overruns, and reputational harm.

## A proportionate risk process for each use case

1. **Establish context.** Describe the use case, users, affected people, data, outputs and how outputs are used. Note the consequence of error.
2. **Tier the use case.** Apply screening criteria to assign low, medium or high risk (see [Assess](../lifecycle/02-assess.md)). The tier determines the depth of what follows.
3. **Identify risks.** Use the catalogue above, the [security](security.md) threat list and the [data protection](data-protection.md) checks. Involve the business owner, users and specialists.
4. **Analyse and evaluate.** Rate likelihood and impact using your enterprise risk scales, so AI risks are comparable with other risks. Consider who is harmed: individuals, the organisation, third parties.
5. **Treat.** Choose controls (see below). Decide whether residual risk is within appetite.
6. **Accept or escalate.** Residual risk is accepted by someone with authority, per your [decision rights](governance-model.md#decision-rights).
7. **Monitor and review.** Track indicators; review on schedule and on trigger events (incidents, vendor changes, new laws).

The [AI risk assessment](../../assessments/ai-risk-assessment.md) provides a template for this process.

## Control types

| Control type | Examples |
|---|---|
| Avoid | Exclude certain data or uses (for example, no automated decisions about individuals) |
| Technical | Access restrictions; data loss prevention; connector restrictions; logging; content filters; retrieval limited to approved sources |
| Procedural | Mandatory human review; four-eyes checks for external outputs; approval for new uses |
| Contractual | Data use, retention and location terms; change notification; audit rights; indemnities |
| People | Training on limitations and verification; acceptable use policy; champions |
| Monitoring | Output sampling; incident reporting; usage analytics; fairness monitoring |

## Integrating with enterprise risk management

- Record significant AI risks in the enterprise risk register using the same scales.
- Assign risk owners from the business, not only from IT or compliance.
- Report aggregate AI risk to the same committee that oversees other operational risks.
- Where model risk management exists (common in financial services), decide which AI tools fall within its scope.

## Variations by organisation size

**Small organisations.** A one-page risk assessment per tool is often enough: what data it sees, what could go wrong, what you will do about it, who decides. Focus on confabulation, data privacy and supplier terms, which are the most common sources of harm for typical office use.

**Enterprises.** Adopt a documented method aligned to NIST AI RMF or ISO/IEC 23894; consider ISO/IEC 42001 if customers or regulators expect certification. Maintain an inventory of AI systems, including AI features embedded in existing software.

## Common pitfalls

- **Treating AI risk as purely technical.** Many harms arise from how people use outputs.
- **Assessing once.** Vendor model changes and new features alter the risk profile.
- **Ignoring over-reliance.** Human review loses value if reviewers stop scrutinising outputs.
- **Separate scales.** AI risks rated on bespoke scales cannot be compared with other enterprise risks.

## Sources

1. National Institute of Standards and Technology, *AI Risk Management Framework* (overview page, including AI RMF 1.0, AI 600-1 release dates, revision notice and critical infrastructure concept note), accessed October 2026. https://www.nist.gov/itl/ai-risk-management-framework
2. National Institute of Standards and Technology, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*, NIST AI 600-1, July 2024. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
3. International Organization for Standardization, *ISO/IEC 23894:2023 Information technology — Artificial intelligence — Guidance on risk management*, February 2023. https://www.iso.org/standard/77304.html
4. International Organization for Standardization, *ISO/IEC 42001:2023 Information technology — Artificial intelligence — Management system*, December 2023. https://www.iso.org/standard/42001

# Risk and compliance pathway

> **Who this is for:** Information security, risk management, legal, compliance, data protection officers and privacy teams, procurement, and internal audit.
> **Last reviewed:** 2026-10

Risk and compliance functions set the guardrails that let an organisation use AI tools with confidence. Done well, this enables adoption: clear rules, proportionate assessments and fast decisions. Done badly, it either blocks useful work or lets unmanaged risk through. This pathway covers AI risk frameworks, the regulatory landscape, data protection impact assessments (DPIAs), contracts and supplier assurance, and audit. It is orientation, not legal advice; take professional advice on decisions with legal consequences.

## What AI adoption means for risk and compliance

- **Existing frameworks still apply.** Data protection, consumer protection, equality, employment, intellectual property, sector regulation and contract law all apply to AI use. AI-specific rules sit on top.
- **New risk types need explicit treatment.** NIST's Generative AI Profile identifies twelve risks specific to or worsened by generative AI, including confabulation (hallucination), data privacy, harmful bias, information security, intellectual property, and value chain and component integration [1].
- **Some security risks cannot be eliminated.** The UK NCSC has said prompt injection may never be fully mitigated and advises reducing its likelihood and impact [2].
- **Regulation is changing fast.** For example, the EU AI Act was amended in 2026 by an "AI Omnibus" regulation that, according to legal commentary, entered into force on 27 July 2026 and postponed the application of obligations for stand-alone high-risk systems (Annex III) to 2 December 2027, and for high-risk AI in products covered by EU product safety law (Annex I) to 2 August 2028 [3][4]. Keep a dated regulatory horizon scan. See [regulation overview](../governance/regulation-overview.md).
- **Proportionality is the job.** Most everyday uses are low risk and need light controls. Effort should concentrate on uses that affect individuals, involve sensitive data, or take actions.

## Your key responsibilities and decisions

### Risk frameworks

| Framework | What it is | Typical use |
|---|---|---|
| NIST AI Risk Management Framework (AI RMF 1.0) | Voluntary framework organised around four functions: Govern, Map, Measure, Manage [5] | Structuring an AI risk programme |
| NIST AI 600-1 Generative AI Profile | Companion to the AI RMF focused on generative AI risks and actions [1] | Generative AI risk identification |
| ISO/IEC 42001:2023 | Certifiable international standard for an AI management system [6] | Organisation-wide AI governance; demonstrating assurance |
| OWASP Top 10 for LLM Applications | Community-ranked list of security risks in LLM applications [7] | Security threat modelling for applications |
| NCSC/CISA Guidelines for secure AI system development | Joint international guidance across design, development, deployment and operation [8] | Security baselines |
| UK Code of Practice for the Cyber Security of AI | Voluntary UK code with 13 principles [9] | Security baselines for UK organisations |

See [standards and frameworks](../../resources/standards-and-frameworks.md) for more. Most organisations do not need to adopt all of these. A common pattern is to integrate AI into the existing enterprise risk framework, use the NIST profile as a checklist of risk types, and use ISO/IEC 42001 if external assurance or certification is valuable to customers.

### Risk-tiering use cases

Assess each use case proportionately, using the [AI risk assessment](../../assessments/ai-risk-assessment.md). Factors that raise the tier:

- Decisions or significant influence on decisions about individuals (employment, credit, eligibility, access to services, education).
- Personal data, especially special category or children's data.
- Confidential, commercially sensitive or legally privileged information.
- Outputs reaching customers or the public without human review.
- Ability to take actions in systems, send communications or spend money.
- Regulated activities (financial advice, health, legal services, safety-critical systems).
- Uses that may fall into regulatory categories such as high-risk under the EU AI Act.

### Regulation

Your role is to establish which rules apply to which uses, in which jurisdictions. Key questions:

- Where do we operate, and where are the people affected by our AI use?
- Under the EU AI Act, are we a provider or deployer of each system, and does any use fall within prohibited practices, high-risk categories or transparency obligations?
- Have we addressed AI literacy? Article 4 of the EU AI Act has required providers and deployers to take measures on staff AI literacy since 2 February 2025 [10]; commentators report the 2026 amendments recast this as a duty to take measures rather than to guarantee a level of competence [11].
- What do our sector regulators expect?

### Data protection impact assessments

Under UK GDPR and EU GDPR, a DPIA is required for processing likely to result in high risk to individuals. The UK Information Commissioner's Office (ICO) publishes guidance on AI and data protection, including how DPIAs apply [12]. In practice:

| Situation | DPIA likely? |
|---|---|
| Staff using an approved assistant for drafting, with a rule against entering personal data | Often not required, but record the decision and reasoning |
| Assistant embedded across email and documents, which contain personal data | Usually advisable |
| AI used to analyse customer or employee data | Likely |
| AI influencing decisions about individuals (recruitment screening, performance, eligibility) | Very likely required |
| Special category data, children's data, or monitoring | Very likely required |

Make DPIAs reusable: assess a tool once at platform level, then add lighter use-case assessments on top.

### Contracts and supplier assurance

Use the [vendor due diligence](../../assessments/vendor-due-diligence.md) assessment. Key contractual points:

| Topic | What to secure |
|---|---|
| Data use | Whether your inputs and outputs are used to train or improve models, and how to opt out |
| Roles | Controller and processor roles; data processing agreement |
| Retention | Retention periods for prompts, outputs and logs; deletion on request and at exit |
| Location | Data residency and international transfer mechanisms |
| Sub-processors | List of sub-processors, including model providers behind the product, and notice of changes |
| Security | Certifications, testing, incident notification timescales |
| IP | Ownership of outputs; any indemnity for third-party IP claims and its conditions |
| Change | Notice of material changes to models, features or terms |
| Audit | Access to audit logs; right to information for your own compliance |
| Exit | Data export and deletion; transition support |

Remember that AI features added to existing software can change processing under existing contracts. Procurement and contract review should cover renewals and feature changes, not only new purchases. See [intellectual property](../governance/intellectual-property.md).

### Audit and assurance

- Maintain an inventory of AI use cases and tools (the [use case register](../../toolkits/use-case-register-template.md)).
- Check that approved controls are operating: human review steps, logging, access controls, training completion.
- Sample AI-assisted outputs in higher-risk processes for accuracy and fairness.
- Review incidents and near misses for patterns.
- Report to the governance board on risk posture, not only on activity.

## Questions you should be asking

- Do we have an inventory of AI use, including features embedded in existing software?
- Which uses fall into which risk tier, and who decided?
- Which regulations apply to each high-risk use, and when do obligations take effect?
- Has a DPIA been done where required, and is it kept up to date as the tool changes?
- Are supplier terms on training use, retention and sub-processors acceptable and documented?
- How would we know if an AI tool caused harm, and how would we respond?
- Are our controls helping people use AI safely, or pushing them to unapproved tools?

## Your reading route

1. **Foundations.** Read [capabilities and limitations](../foundations/capabilities-and-limitations.md) so that risk judgements reflect how the tools actually fail.
2. **Governance core.** Read [governance model](../governance/governance-model.md), [risk management](../governance/risk-management.md) and [responsible AI principles](../governance/responsible-ai-principles.md).
3. **Law and regulation.** Read [regulation overview](../governance/regulation-overview.md), [data protection](../governance/data-protection.md) and [intellectual property](../governance/intellectual-property.md).
4. **Security.** Read [security](../governance/security.md).
5. **Assessments.** Adopt and adapt [AI risk assessment](../../assessments/ai-risk-assessment.md) and [vendor due diligence](../../assessments/vendor-due-diligence.md).
6. **Policies.** Adapt the [AI policy template](../../toolkits/ai-policy-template.md) and [acceptable use policy](../../toolkits/acceptable-use-policy.md).
7. **Lifecycle checkpoints.** Read [Assess](../lifecycle/02-assess.md), [Select](../lifecycle/03-select.md) and [Operate](../lifecycle/06-operate.md) to see where risk decisions fit.
8. **Standards.** Use [standards and frameworks](../../resources/standards-and-frameworks.md) to decide which frameworks to align with.
9. **Tool specifics.** Use the [tool guides](../tools/tool-guides/README.md) for data controls and known limitations of tools you have chosen.

## Common pitfalls

| Pitfall | What to do instead |
|---|---|
| Treating every use as high risk | Tier use cases; fast-track low-risk uses with standard controls |
| Saying no without offering a path | Provide approved tools and clear conditions |
| One-off assessment | Re-assess when tools, models, data or use change |
| Reviewing only new purchases | Include AI features added to existing software and renewals |
| Relying on vendor marketing for compliance claims | Verify in contracts and documentation |
| Assuming the regulation timetable is fixed | Maintain a dated horizon scan; regulation is being amended |
| Policy nobody reads | Short, practical policies, reinforced through training |

## What good looks like

- An AI use case inventory with risk tiers, owners and review dates.
- A proportionate assessment process: standard controls for low-risk uses, full assessment for high-risk ones, with clear turnaround times.
- Platform-level DPIAs and supplier assessments for approved tools, reused across use cases.
- Contract terms on data use, retention, sub-processors, IP and change documented for each tool.
- A dated regulatory horizon scan reviewed at least quarterly.
- Regular reporting on incidents, control effectiveness and emerging risks.
- In small organisations: a short policy, business-tier tools with training-use switched off, a simple record of what is used and for what, and a check on whether any use affects decisions about individuals.

## Sources

1. NIST, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile* (NIST AI 600-1), July 2024. https://doi.org/10.6028/NIST.AI.600-1
2. National Cyber Security Centre, *Prompt injection is not SQL injection*, December 2025. https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection
3. National Law Review, *EU Digital Omnibus on AI enters into force*, 2026 (secondary). https://natlawreview.com/article/eu-digital-omnibus-ai-enters-force
4. White & Case, *EU agrees Digital Omnibus deal to simplify AI rules*, May 2026 (secondary). https://www.whitecase.com/insight-alert/eu-agrees-digital-omnibus-deal-simplify-ai-rules
5. NIST, *AI Risk Management Framework (AI RMF 1.0)*, January 2023. https://nist.gov/news-events/news/2023/01/nist-risk-management-framework-aims-improve-trustworthiness-artificial
6. ISO, *ISO/IEC 42001:2023 Information technology — Artificial intelligence — Management system*. https://www.iso.org/standard/42001
7. OWASP GenAI Security Project, *OWASP GenAI LLM Top 10 2026*. https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/
8. National Cyber Security Centre, CISA and partners, *Guidelines for secure AI system development*, November 2023. https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development
9. Department for Science, Innovation and Technology, *Code of Practice for the Cyber Security of AI*, January 2025. https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice/code-of-practice-for-the-cyber-security-of-ai
10. Mayer Brown, *EU AI Act: Ban on certain AI practices and requirements for AI literacy come into effect*, January 2025 (secondary). https://www.mayerbrown.com/de/insights/publications/2025/01/eu-ai-act-ban-on-certain-ai-practices-and-requirements-for-ai-literacy-come-into-effect
11. KI-Campus, *EU AI Act: AI Omnibus recalibrates Article 4 – AI literacy remains mandatory*, 2026 (secondary). https://ki-campus.org/en/blog/eu-ai-act-ai-omnibus-recalibrates-article-4-ai-literacy-remains-mandatory
12. Information Commissioner's Office, *Guidance on AI and data protection*. https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/about-this-guidance/

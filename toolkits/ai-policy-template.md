# AI policy template (organisation level)

> **Who this is for:** Executives, governance and risk leads, data protection officers, and policy owners who need an organisation-wide policy setting out how AI is governed. Scaled guidance for small organisations is included.
> **Last reviewed:** 2026-10

This is a fill-in-the-blanks organisation-level AI policy. Where the [acceptable use policy](acceptable-use-policy.md) tells staff what they may do day to day, this policy sets the organisation's commitments: purpose and principles, scope, roles and accountability, how AI use cases are approved and classified by risk, requirements across the lifecycle (data, security, human oversight, transparency, procurement, monitoring), regulatory compliance, incidents, and review. Guidance notes in blockquotes help you tailor it; replace [bracketed placeholders] and remove guidance before approval. It draws on structures common to the NIST AI Risk Management Framework, ISO/IEC 42001 and the UK Government's AI Playbook, without claiming conformity with any of them.

> **Guidance: before you start**
>
> - **Keep it proportionate.** A 15-person firm might adopt sections 1–6 and 12 in two pages. A regulated enterprise may need everything, plus supporting standards.
> - **Separate policy from procedure.** The policy states what must happen and who is accountable. Detailed procedures (risk assessment template, approval workflow) sit underneath and can change without re-approving the policy.
> - **Useful reference frameworks:** the NIST AI RMF organises AI risk management into four functions (Govern, Map, Measure, Manage) [1]; ISO/IEC 42001 specifies requirements for an AI management system [2]; the UK Government's AI Playbook (February 2025) sets out ten principles for public sector use that many private organisations also find useful [3]. Use them as checklists, not as text to copy.
> - **Involve** leadership, legal, data protection, security, HR and staff representatives in drafting.
> - This template is not legal advice.

---

## [Organisation name] Artificial Intelligence Policy

| | |
|---|---|
| **Version** | [1.0] |
| **Policy owner** | [role, e.g. Chief Operating Officer] |
| **Approved by** | [board / executive committee / owner] on [date] |
| **Effective from** | [date] |
| **Review** | [annually, and on significant regulatory or technology change] |

## 1. Purpose

This policy sets out how [Organisation name] adopts, uses, buys and (where relevant) develops artificial intelligence so that AI supports our objectives of [objectives], while protecting people, complying with the law and maintaining trust.

## 2. Scope

This policy applies to:

- all AI systems used by or on behalf of [Organisation name], including general-purpose AI assistants, AI features within existing software, AI-enabled services from suppliers, and AI systems we build or customise;
- all staff, contractors and third parties acting on our behalf; and
- all stages of the AI lifecycle: identifying use cases, assessing, selecting, piloting, deploying, operating and retiring.

**Definition.** For this policy, an "AI system" is [insert definition; for example, align with the definition in the EU AI Act if it applies to you, or use a plain-English description such as "software that generates outputs such as content, predictions, recommendations or decisions from inputs, using machine learning or similar techniques"].

> **Guidance:** If you are subject to the EU AI Act, using its definition helps align your inventory with your legal obligations. Take advice on whether particular systems fall within it.

## 3. Principles

When using AI we will:

1. **Have a clear purpose.** Use AI where it serves a defined need and where benefits outweigh risks.
2. **Keep people accountable.** A named person is accountable for every AI use case. AI does not take responsibility; people do.
3. **Maintain meaningful human oversight** proportionate to the impact of outputs, especially where they affect individuals.
4. **Protect data and privacy**, complying with data protection law and our information classification rules.
5. **Be secure** by design, including against AI-specific threats.
6. **Be fair** and take steps to identify and reduce harmful bias.
7. **Be transparent** with staff, customers and the public about where and how we use AI, as appropriate to the context and as required by law.
8. **Verify outputs** before relying on them, in proportion to the consequences of error.
9. **Build skills**, so that people who use or oversee AI understand its capabilities and limitations.
10. **Monitor and improve**, reviewing whether AI use continues to deliver value and remains safe.

> **Guidance:** These are examples. Adapt them to your values and sector. See [responsible AI principles](../docs/governance/responsible-ai-principles.md) for the principles common across major frameworks.

## 4. Roles and accountability

| Role | Responsibilities |
|---|---|
| **[Board / owners]** | Approves this policy and AI risk appetite; receives [annual] reports on AI use and risk |
| **Senior AI sponsor** [name/role] | Accountable for AI adoption overall; chairs [AI governance group]; owns the AI roadmap |
| **[AI governance group]** [membership] | Approves high-risk use cases; maintains the AI use case register; reviews incidents; recommends policy changes |
| **Use case owner** | Accountable for an individual AI use case: its purpose, risk assessment, controls, performance and retirement |
| **Data protection officer / lead** | Advises on data protection; reviews DPIA screening and DPIAs |
| **Information security** | Assesses security risks; sets technical controls; monitors |
| **Legal / compliance** | Advises on regulatory obligations, contracts and IP |
| **Procurement** | Ensures vendor due diligence and contract terms |
| **HR / People** | Advises on workforce impact, consultation, training and policy enforcement |
| **Managers** | Ensure their teams use AI in line with policy and have completed training |
| **All staff** | Follow the [acceptable use policy](acceptable-use-policy.md); report concerns and incidents |

A detailed responsibility matrix is maintained in [RACI](raci-template.md).

> **Guidance for small organisations:** The owner or managing director may be the sponsor and the governance group, with an external adviser for data protection and legal questions. Record who does what.

## 5. Risk appetite

[Organisation name] will:

- **welcome** AI use that assists staff with low-impact tasks using approved tools and permitted data;
- **accept with controls** AI use that processes confidential or personal data, produces external content, or informs decisions, subject to risk assessment and approval;
- **require [governance group / board] approval** for AI use that substantially influences decisions about individuals, operates autonomously with external effect, or falls within a regulated high-risk category;
- **not permit** AI uses that are prohibited by law or are inconsistent with our values, including [examples].

## 6. Use case approval and risk classification

1. Every AI use case beyond use of approved tools within the acceptable use policy must be recorded in the [AI use case register](use-case-register-template.md).
2. Each use case is screened using the [AI risk assessment](../assessments/ai-risk-assessment.md) screening questionnaire and classified:

| Classification | Typical characteristics | Approval |
|---|---|---|
| **Low** | Internal, assistive, no personal or confidential data beyond policy, low consequence of error | Use case owner, recorded in register |
| **Medium** | Personal or confidential data; external content with human review; moderate consequences | Use case owner plus [data protection / security] review |
| **High** | Decisions about individuals; autonomous actions; special category data; regulated high-risk category; serious potential harm | [AI governance group]; DPIA where required; legal review |
| **Prohibited** | Unlawful or outside risk appetite | Not permitted |

1. Approval may be conditional (for example, limited users, additional monitoring, time limit).
2. Use cases must be re-assessed when the model, data, purpose, users or applicable law change materially.

## 7. Lifecycle requirements

### 7.1 Data

- Data used with AI must comply with our [data protection policy] and [information classification scheme].
- Data readiness is assessed for each medium- and high-risk use case ([data readiness assessment](../assessments/data-readiness.md)).
- Personal data will not be used to train or fine-tune models without a documented lawful basis and DPIA.

### 7.2 Security

- AI tools must be configured to [information security standard], including identity and access controls, least-privilege permissions for AI connectors, logging, and protection against AI-specific threats such as prompt injection and data leakage.

### 7.3 Human oversight

- Each use case defines who reviews outputs, at what point, and with what authority to override.
- Oversight must be realistic: reviewers must have the time, competence and information to challenge outputs.

### 7.4 Transparency

- We maintain an [internal / public] register of significant AI uses.
- We inform people when they interact with an AI system, and label AI-generated content, where required by law or our standards.
- We explain to individuals, on request and where required, how AI was used in decisions affecting them.

### 7.5 Procurement

- All AI tools and AI-enabled services are subject to [vendor due diligence](../assessments/vendor-due-diligence.md) proportionate to risk before purchase or activation, including AI features added to existing products.

### 7.6 Testing and monitoring

- Medium- and high-risk use cases are tested before deployment for accuracy, security and, where relevant, fairness.
- Use cases are monitored in operation for performance, incidents, usage and value, and reviewed at least [annually].

### 7.7 Retirement

- Use cases that no longer deliver value or whose risks cannot be controlled are retired, with data handled according to retention rules.

## 8. People and skills

- We provide AI literacy and role-based training proportionate to how people use or oversee AI ([training plan](training-plan-template.md)), and keep records.
- We assess the impact of AI on roles and workload, and consult staff [and their representatives] on significant changes.

> **Guidance:** If you are a provider or deployer of AI systems within scope of the EU AI Act, Article 4 imposes an AI literacy obligation, which has applied since 2 February 2025 and was amended by the Digital Omnibus on AI in 2026. See the [training plan template](training-plan-template.md) for the current position.

## 9. Legal and regulatory compliance

We will identify and comply with the laws that apply to our AI use, including [list, e.g. UK GDPR and the Data Protection Act 2018; EU GDPR; EU AI Act; Equality Act 2010; consumer protection law; sector regulation]. [Legal / compliance] maintains a map of obligations to use cases. See [regulation overview](../docs/governance/regulation-overview.md).

## 10. Incidents and concerns

- AI-related incidents (for example, data leakage, harmful output relied upon, security events, unexpected behaviour) are reported via [route] and managed under [incident management procedure].
- Staff and others can raise concerns about AI use through [route], including [whistleblowing channel].
- Incidents are reviewed by [AI governance group] to identify lessons.

## 11. Exceptions

Exceptions to this policy must be approved in writing by [role], recorded with reasons, time-limited, and reviewed.

## 12. Review and reporting

- The policy owner reviews this policy at least [annually] and when law, technology or our use of AI changes significantly.
- [AI governance group] reports to [board] [annually / quarterly] on AI use, value, risks and incidents.

## 13. Related documents

[Acceptable use policy for AI tools](acceptable-use-policy.md); [data protection policy]; [information security policy]; [procurement policy]; [AI risk assessment procedure](../assessments/ai-risk-assessment.md); [RACI](raci-template.md); [use case register](use-case-register-template.md).

---

## Checklist before approval

- [ ] Scope and definition agreed
- [ ] Principles reflect our values and sector
- [ ] Named sponsor, governance group and use case owner role
- [ ] Risk appetite agreed by leadership
- [ ] Risk classification and approval routes match our capacity
- [ ] Supporting procedures exist or have owners and dates
- [ ] Consistent with data protection, security, procurement and HR policies
- [ ] Legal and data protection review completed
- [ ] Communication and training planned ([communication plan](communication-plan-template.md))

## Sources

1. NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, January 2023. https://doi.org/10.6028/NIST.AI.100-1
2. ISO/IEC, *ISO/IEC 42001:2023 Information technology — Artificial intelligence — Management system*, December 2023. https://www.iso.org/standard/42001
3. UK Government, *Artificial Intelligence Playbook for the UK Government*, 10 February 2025. https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html

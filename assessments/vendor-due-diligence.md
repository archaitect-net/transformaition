# Vendor due diligence questionnaire

> **Who this is for:** Procurement, IT, security, data protection, legal and business owners evaluating an AI tool or AI feature before buying, renewing or enabling it. Small organisations can use the "essential" questions as a checklist against vendor documentation and standard terms.
> **Last reviewed:** 2026-10

This questionnaire helps you question AI vendors consistently and compare their answers. It is organised into eleven sections: data use and retention, training on customer data, security certifications, sub-processors, data residency, model changes and versioning, transparency, intellectual property indemnity, availability and service levels, exit and portability, and AI-specific contract clauses. For each question it describes what a good answer looks like and the red flags to watch for. A simple scoring method turns answers into a comparable result. Use it at the [Select](../docs/lifecycle/03-select.md) stage alongside [choosing tools](../docs/tools/choosing-tools.md), and revisit it at renewal.

## How to use this questionnaire

1. **Decide the depth.** Questions marked **(E)** are essential for any AI tool that will process organisational data. Others are for medium- and high-risk use cases (see the [AI risk assessment](ai-risk-assessment.md) screening) or larger contracts.
2. **Check public material first.** Many answers are in the vendor's trust centre, data processing agreement, product documentation and service terms. Only send questions you cannot answer from published material. Record the document and date you relied on, because terms change.
3. **Ask for evidence, not assurances.** A certificate, a contract clause or a configuration setting is evidence. A sales statement is not.
4. **Check the specific product and plan.** Data terms often differ between consumer, business and enterprise tiers of the same product, and between a vendor's core service and features that rely on third parties. Confirm which terms apply to what you are buying.
5. **Score and compare** using the method at the end.

> **Neutrality note:** This questionnaire does not imply that any vendor meets or fails these criteria. Apply it equally to every option, including open-weight models you host yourself (where many questions apply to your own hosting arrangements and to the model's licence).

## Vendor details

| Field | Response |
|---|---|
| Vendor | [ ] |
| Product, plan or tier | [ ] |
| Use case(s) | [register IDs] |
| Documents reviewed (with dates) | [trust centre, DPA, service terms, model documentation] |
| Assessor(s) and date | [ ] |

## Section 1: Data use and retention

| # | Question | What good looks like | Red flags |
|---|---|---|---|
| 1.1 (E) | What customer data does the service collect (prompts, files, outputs, connected data, telemetry, feedback)? | Clear, complete list by data type, in contractual documentation | Vague categories; telemetry or "service improvement" data undefined |
| 1.2 (E) | For what purposes is each type of data used? | Limited to providing the service, security and legal obligations; any other use opt-in | Broad purposes such as "improving our products" without limits |
| 1.3 (E) | How long are prompts, outputs and uploaded files retained, and can we configure it? | Defined retention periods; configurable by the customer; deletion on request | Indefinite retention; no deletion mechanism |
| 1.4 | Is any data retained for abuse or safety monitoring, and who can access it? | Retention period, access controls and human review conditions stated; option to request exemption where offered | Undisclosed human review of customer content |
| 1.5 (E) | Does the vendor act as a processor (on our instructions) for our data? Is a data processing agreement (DPA) available? | DPA available covering the AI features; processor role for customer content | Vendor claims controller role over customer content without clear justification |
| 1.6 | How is data deleted at the end of the contract? | Defined deletion timeline and certification on request | No commitment |

## Section 2: Training on customer data

| # | Question | What good looks like | Red flags |
|---|---|---|---|
| 2.1 (E) | Is our data (prompts, outputs, files, connected data) used to train or improve any models? | Contractual commitment that it is not, by default, for business tiers | Default opt-in; commitment only in marketing material |
| 2.2 (E) | If training use is possible, how do we opt out, and is the opt-out contractual and organisation-wide? | Admin-level, organisation-wide setting backed by contract | Per-user opt-out only; opt-out can be changed by users |
| 2.3 | Is feedback data (e.g. thumbs up/down, submitted examples) treated differently? | Explained; feedback use controllable | Feedback silently used for training |
| 2.4 | Are third-party model providers used, and do the same no-training commitments flow down to them? | Yes, contractually flowed down | Commitments apply to the vendor only |
| 2.5 | If we fine-tune a model, who can access the resulting model and is it isolated to us? | Customer-exclusive; deletable | Shared or reused |

## Section 3: Security certifications and controls

| # | Question | What good looks like | Red flags |
|---|---|---|---|
| 3.1 (E) | Which independent certifications or attestations cover this product (e.g. ISO/IEC 27001, SOC 2 Type II, sector-specific schemes)? | Current certificates or reports, with scope that includes the AI features | Certificates exist but scope excludes the AI service; expired reports |
| 3.2 | Does the vendor hold or work towards ISO/IEC 42001 (AI management system)? | Certified, or a clear position on it | — (absence is not a red flag on its own; ISO/IEC 42001 was published in December 2023 [1]) |
| 3.3 (E) | Is data encrypted in transit and at rest? Can we manage keys? | Encryption standard; customer-managed keys available where needed | No encryption at rest |
| 3.4 (E) | Does the service support single sign-on, MFA, role-based access and admin controls for AI features? | Yes, with granular controls | Consumer-style accounts only |
| 3.5 | Are audit logs of AI use available to us, and for how long? | Exportable logs of prompts, actions and admin changes where appropriate | No customer access to logs |
| 3.6 | How does the vendor test for AI-specific threats such as prompt injection, data leakage and excessive agency? | Describes testing approach, including red-teaming; references recognised threat lists such as the OWASP Top 10 for LLM Applications [2] | No awareness of AI-specific threats |
| 3.7 | Do AI features respect our existing access permissions when retrieving data? | Yes, enforced at retrieval; documented | Indexes content regardless of permissions |
| 3.8 | What is the incident notification commitment? | Defined timeline in contract, aligned with your legal obligations | "Without undue delay" only, or none |

## Section 4: Sub-processors

| # | Question | What good looks like | Red flags |
|---|---|---|---|
| 4.1 (E) | Who are the sub-processors for the AI features, including model providers and hosting? | Published, current list with location and function | No list; model provider undisclosed |
| 4.2 (E) | How are we notified of changes, and can we object? | Advance notice with a right to object or terminate | Changes without notice |
| 4.3 | Do sub-processors operate under equivalent data protection and no-training terms? | Yes, contractually | Unknown |

## Section 5: Data residency and international transfers

| # | Question | What good looks like | Red flags |
|---|---|---|---|
| 5.1 (E) | Where is our data stored and processed, including during model inference? | Stated regions; option to restrict to your required region | Storage location stated but inference location unknown |
| 5.2 | Are there features that process data outside the chosen region (e.g. web search, certain models, support access)? | Disclosed, with ability to disable | Undisclosed exceptions |
| 5.3 (E) | What transfer mechanisms are used for international transfers of personal data? | Recognised mechanisms appropriate to your jurisdiction, documented in the DPA | No mechanism identified |

## Section 6: Model changes and versioning

| # | Question | What good looks like | Red flags |
|---|---|---|---|
| 6.1 (E) | Which model(s) power the service, and how are we told when they change? | Models named; advance notice of changes; release notes | Silent model changes |
| 6.2 | Can we pin a model version, and for how long are versions supported? | Version pinning and published deprecation timelines (more common on developer and cloud platforms than in end-user assistants) | No deprecation notice |
| 6.3 | How does the vendor evaluate a new model before release (quality, safety, regression)? | Described evaluation process; published model or system documentation | None |
| 6.4 | Can we test new versions before they are applied to our users? | Preview or staged rollout available | No |

> **Why this matters:** A model change can alter accuracy, tone, refusal behaviour or cost. Your risk assessment and any test sets should be re-run when the model changes. NIST's Generative AI Profile identifies dependence on third-party components and models as a distinct risk area ("value chain and component integration") [3].

## Section 7: Transparency

| # | Question | What good looks like | Red flags |
|---|---|---|---|
| 7.1 | Is there documentation describing the model's intended uses, limitations, evaluation results and known risks (e.g. model or system cards)? | Published, current, specific | Marketing material only |
| 7.2 | What information does the vendor provide about training data sources and copyright approach? | A description of data sources and policies | Refuses any description |
| 7.3 | Does the product show users when content is AI-generated and provide citations for retrieved information? | Yes, configurable | No indication |
| 7.4 | If the vendor is a provider under the EU AI Act, how does it meet the obligations that apply to it (e.g. transparency obligations, and for general-purpose AI models the applicable provider obligations)? | Clear statement of its role and compliance approach | Claims the Act does not apply without explanation |
| 7.5 | Will the vendor provide information we need for our own impact assessments (DPIA, AI risk assessment)? | Yes, including a DPIA support pack | No |

## Section 8: Intellectual property and indemnity

| # | Question | What good looks like | Red flags |
|---|---|---|---|
| 8.1 (E) | Who owns the inputs and outputs? | Customer retains rights in inputs; vendor assigns or does not claim rights in outputs | Vendor claims a broad licence over outputs |
| 8.2 | Does the vendor offer indemnity against third-party IP claims arising from outputs? What are the conditions and caps? | Indemnity offered, with conditions you can meet (e.g. using filters, not deliberately infringing) and a meaningful cap | Indemnity only on higher tiers you are not buying; conditions impractical |
| 8.3 | Does the indemnity cover outputs from all models and features in the product? | Yes, or exclusions clearly listed | Exclusions buried in separate terms |

See [intellectual property](../docs/governance/intellectual-property.md).

## Section 9: Availability and service levels

| # | Question | What good looks like | Red flags |
|---|---|---|---|
| 9.1 (E) | What availability commitment applies to the AI features, and what are the remedies? | Contractual service level covering AI features, with service credits | Service level excludes AI or "preview" features |
| 9.2 | Are there usage limits, rate limits or fair-use caps? | Documented and adequate for your volumes | Undisclosed throttling |
| 9.3 | How is pricing structured (per user, per use, consumption), and can it change mid-term? | Predictable pricing; notice of changes; spending caps for consumption models | Unilateral price changes; no caps |
| 9.4 | Are any features in preview or beta, and on what terms? | Clearly labelled, with separate terms you can review | Preview features enabled by default under weaker terms |

## Section 10: Exit and portability

| # | Question | What good looks like | Red flags |
|---|---|---|---|
| 10.1 (E) | Can we export our data, prompts, configurations, custom assistants and logs in usable formats? | Yes, documented formats | No export, or proprietary formats only |
| 10.2 | What happens to our data and fine-tuned models on exit? | Return and deletion with certification | Retention after exit |
| 10.3 | What notice is given if the product or a model is withdrawn? | Defined notice period | None |
| 10.4 | How dependent would we be on vendor-specific features? | Standards-based integrations; vendor explains portability | Deep lock-in with no export path |

## Section 11: AI-specific contract clauses

> **Guidance:** These are clauses to look for or negotiate. Small organisations may have little negotiating power on standard terms; in that case, use this section to understand the terms you are accepting and to compare vendors.

| Clause | What to look for | Red flags |
|---|---|---|
| No training on customer data | Explicit, applies to all customer content and flows down to sub-processors | Only in a policy the vendor can change unilaterally |
| Model change notification | Advance notice of material model changes | None |
| Output ownership | Clear statement in your favour | Ambiguous |
| IP indemnity | Scope, conditions, cap | Excludes the features you will use |
| Data location | Commitment to regions, including for inference | Storage only |
| Acceptable use policy of the vendor | Compatible with your intended use; no surprising restrictions | Restrictions that would prohibit your use case |
| Human review of customer content | Disclosed, limited, controllable | Undisclosed |
| Regulatory cooperation | Vendor will provide information needed for your compliance (e.g. data protection, AI Act deployer obligations) | No commitment |
| Audit rights | Access to audit reports; right to audit for high-risk uses | None |
| Liability caps | Proportionate to risk; carve-outs for data protection breaches | Very low caps covering all claims |
| Changes to terms | Notice and right to terminate on material adverse change | Unilateral change by posting online |
| Suspension | Defined, limited grounds with notice | Broad discretion to suspend |

## Scoring

Score each answered question:

| Score | Meaning |
|---|---|
| 2 | Meets "what good looks like", with evidence |
| 1 | Partly meets, or meets without evidence |
| 0 | Does not meet, or no answer |
| RF | Red flag present |

1. **Section score** = points ÷ (2 × questions answered) × 100.
2. **Overall score** = average of section scores. You may weight sections to reflect your use case (for example, data residency higher for public sector data); record any weights.
3. **Red flags**: list every RF. Any RF on an essential (E) question is a **blocker** until resolved through contract change, configuration, or a documented risk acceptance in the [AI risk assessment](ai-risk-assessment.md).

## Interpreting results

| Band | Overall score | Meaning | What to do next |
|---|---|---|---|
| Not acceptable | Below 50%, or unresolved blocker | Significant gaps for your use case | Do not proceed, or narrow the use to data the gaps do not affect. Seek alternatives. |
| Acceptable with conditions | 50–74%, no blockers | Usable with specific mitigations | Record conditions (configuration, contract changes, restricted data). Feed residual risks into the AI risk assessment. |
| Acceptable | 75–89%, no blockers | Meets most requirements | Proceed; track open items to resolution. |
| Strong | 90–100%, no blockers | Meets requirements with evidence | Proceed. Re-check at renewal and on major model or terms changes. |

**Comparing vendors.** Compare red flags and essential questions first; only then compare overall scores. A vendor with a higher score but one unresolved essential red flag is not a better choice than a vendor with a lower score and none.

## Keeping it current

Vendor terms, models and sub-processor lists change frequently. Record the date of every document relied on. Re-run Sections 1, 2, 4 and 6 at least annually and whenever the vendor notifies a material change.

## Related

- [Choosing tools](../docs/tools/choosing-tools.md), [tool categories](../docs/tools/tool-categories.md) and, for tools you have already chosen, [tool guides](../docs/tools/tool-guides/README.md)
- [Security](../docs/governance/security.md), [data protection](../docs/governance/data-protection.md)
- [IT and platform pathway](../docs/pathways/it-and-platform.md)

## Sources

1. ISO/IEC, *ISO/IEC 42001:2023 Information technology — Artificial intelligence — Management system*, December 2023. https://www.iso.org/standard/42001
2. OWASP GenAI Security Project, *OWASP Top 10 for LLM Applications 2025*. https://genai.owasp.org/llm-top-10/
3. NIST, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*, NIST AI 600-1, July 2024 (value chain and component integration risk). https://doi.org/10.6028/NIST.AI.600-1

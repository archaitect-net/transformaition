# Choosing AI tools

> **Who this is for:** Anyone running or contributing to an AI tool selection: business sponsors, IT and platform teams, procurement, security, data protection, finance and the people who will use the tool.
> **Last reviewed:** 2026-10

This page sets out a requirements-led method for choosing AI tools. You start from use cases and constraints rather than products, weight the criteria that matter to you, test shortlisted options on your own examples under the same conditions, and record why you decided as you did. It covers eleven criteria, how to run a fair evaluation, a build/buy/configure decision tree and procurement considerations. It makes no product recommendations: the right tool depends on your use cases, data, risk appetite and existing estate.

## The method in six steps

| Step | Output | Who is involved |
|---|---|---|
| 1. Define use cases and requirements | A short requirements statement per use case, including data classification and must-haves | Business owner, users, IT, data protection |
| 2. Choose the category | One or more [tool categories](tool-categories.md) that fit | IT/architecture, business owner |
| 3. Weight the criteria | A weighted scoring sheet agreed before you see any demo | Selection group |
| 4. Shortlist | Two to four options that meet every must-have | Procurement, IT, security |
| 5. Evaluate fairly | Scores from your own test set and a hands-on trial | Users, evaluators, security |
| 6. Decide and record | Decision record with scores, rationale, risks and exit plan | Sponsor, selection group |

This sits within the [Select](../lifecycle/03-select.md) stage of the lifecycle. Use [use case prioritisation](../../assessments/use-case-prioritisation.md) to pick the use cases, and [vendor due diligence](../../assessments/vendor-due-diligence.md) for the supplier questions.

## Step 1: Requirements before products

Write requirements in terms of outcomes and constraints, not features. For each use case record:

- **Task and users.** What people do today, how often, and how many people do it.
- **Data.** What information the tool will see or produce, and its classification (public, internal, confidential, personal data, special category data, regulated data).
- **Must-haves.** Conditions an option must meet to be considered at all. Examples: "no training on our content", "data processed in the UK or EU", "single sign-on with our identity provider", "works with screen readers".
- **Should-haves.** Desirable features that go into weighted scoring.
- **Success measures.** How you will know the tool is helping. See [measuring value](../measurement/measuring-value.md).

> **Tip.** Keep must-haves few and genuine. Each one should come from a legal, contractual, security or accessibility obligation, or a clear business necessity. Too many must-haves can rule out every option; too few let unsuitable options through.

## Step 3: Weighted criteria

Agree weights **before** you see demonstrations, so presentation quality does not shape what you value. Score each option from 0 to 5 per criterion, multiply by weight, and sum. Treat any must-have failure as disqualifying, whatever the total.

| # | Criterion | What to assess | Example evidence |
|---|---|---|---|
| 1 | **Fit to use case** | Does it do the tasks you defined, in the workflow where people work? | Results on your test set; user trial feedback |
| 2 | **Data protection and residency** | Training on your data by default; retention and deletion; processing locations, including under peak load and for abuse monitoring; sub-processors; data processing terms; support for data subject rights | Data processing agreement, privacy documentation, sub-processor list, residency terms |
| 3 | **Security and certifications** | Independent assurance; encryption; tenant isolation; vulnerability management; controls against prompt injection and data leakage | SOC 2 Type 2 report, ISO/IEC 27001 certificate, ISO/IEC 42001 certification where held [1], penetration test summary |
| 4 | **Admin controls** | Ability to enable features by group, restrict connectors and models, set retention, export logs, enforce policies | Admin console walkthrough; documentation |
| 5 | **Integration** | Identity (single sign-on, automated provisioning), connectors to your systems, APIs, extensibility, compatibility with your existing security tooling (DLP, SIEM, eDiscovery) | Technical documentation; proof-of-concept |
| 6 | **Model quality (your own evaluation)** | Accuracy, completeness and usefulness of outputs **on your tasks and in your languages** | Scores from your test set (see below). Public benchmarks are context only |
| 7 | **Cost and total cost of ownership** | Licences, usage charges, overages, implementation, training, support, governance effort, infrastructure | Three-year cost model with usage scenarios |
| 8 | **Vendor viability** | Financial stability, roadmap transparency, support quality, track record of honouring commitments, dependency on third-party model providers | Financial filings where available, references, support SLAs |
| 9 | **Exit and portability** | Export of conversations, prompts, configurations, custom agents and logs; data deletion on exit; ability to switch models or providers | Export documentation; contract exit clauses |
| 10 | **Accessibility** | Usable with assistive technology; conformance with recognised accessibility standards; accessible outputs | Accessibility conformance report; testing with users who rely on assistive technology |
| 11 | **Sustainability** | Vendor disclosure of energy, emissions and water use; efficiency options such as smaller models; alignment with your sustainability commitments | Sustainability reports; answers to your questionnaire |

### Example weightings

These are illustrations, not recommendations. Set your own.

| Criterion | Organisation-wide assistant, regulated sector | Coding assistant, software company | Small charity, first tool |
|---|---|---|---|
| Fit to use case | 15 | 20 | 25 |
| Data protection and residency | 20 | 10 | 15 |
| Security and certifications | 15 | 15 | 5 |
| Admin controls | 10 | 10 | 5 |
| Integration | 10 | 15 | 5 |
| Model quality (own evaluation) | 10 | 15 | 15 |
| Cost / TCO | 5 | 5 | 20 |
| Vendor viability | 5 | 3 | 3 |
| Exit and portability | 5 | 3 | 2 |
| Accessibility | 3 | 2 | 3 |
| Sustainability | 2 | 2 | 2 |
| **Total** | **100** | **100** | **100** |

### Questions to ask for each criterion

**Data protection and residency**

- On the exact plan and contract we will sign, is our content used to train or improve models? Is that the default, and can users change it?
- How long are prompts, outputs and files retained, and who can configure that? What happens on deletion?
- Where is data processed and stored? Can processing move to other regions during high demand?
- Is content retained for abuse monitoring, and is it subject to human review? Can we apply for modified or zero retention?
- Which sub-processors, including model providers, are involved?

**Security and admin controls**

- Which independent reports and certifications cover *this* product, not just the vendor's other services?
- Can we restrict which connectors, plug-ins, agents and models users can access?
- Are interaction logs available for audit, eDiscovery and our security monitoring tools?
- What prevents the tool from surfacing content users can technically access but should not see?

**Exit and portability**

- In what formats can we export our data, configurations and custom agents?
- How quickly and verifiably is data deleted when we leave?
- How much of our investment (prompts, agents, integrations) would carry over to an alternative?

## Step 5: Running a fair evaluation

Vendor demonstrations show best cases. A fair evaluation tests every shortlisted option on **your** tasks, under the **same** conditions, scored in the **same** way.

### Build a test set

1. **Collect 20 to 50 real tasks** per use case, drawn from actual work. Include easy, typical and hard examples, and examples where the right answer is "I don't know" or "this needs a human".
2. **Remove or replace sensitive data** unless the trial environment is approved for it.
3. **Write what a good answer looks like** for each task: key facts, required format, things that must not appear.
4. **Include known risk cases**: questions where errors would be costly, prompts in the languages your users work in, documents with tricky formatting, and attempts to make the tool reveal information it should not.
5. **Hold some tasks back** so you can check results are not tuned to the visible examples.

### Run the trial

- Use the **same prompts, files and settings** for every option. Record model versions and dates, because outputs change as vendors update models.
- **Blind the scoring where you can.** Strip product names from outputs before evaluators see them.
- Use **at least two evaluators** per task and agree a simple rubric (for example: correct, partially correct with minor issues, incorrect or harmful). Resolve disagreements by discussion.
- **Repeat a sample** of tasks to see how consistent each option is; generative outputs vary from run to run.
- Run a **hands-on user trial** with a small group doing real work for two to four weeks to test fit, usability and accessibility. See [Pilot](../lifecycle/04-pilot.md) and the [pilot plan template](../../toolkits/pilot-plan-template.md).
- Have security and data protection staff **test the controls**, not just read about them: try to access restricted content, check what logs capture, confirm retention settings take effect.

### Interpret results

- Look at **error types**, not just averages. A tool that is slightly less accurate but fails safely may be preferable.
- Treat public benchmarks and vendor-reported productivity figures as context only. Vendor-run studies are [Limited](../../CONTRIBUTING.md#evidence-labels) evidence by this guide's standards, and see [evidence on impact](../foundations/evidence-on-impact.md).
- Record **conditions of validity**: results apply to the versions, settings and tasks you tested.

## Build, buy or configure

Most organisations use a mix. This decision tree helps for each use case.

```text
Is there an off-the-shelf tool that meets all must-haves for this use case?
├── Yes ─> Does it fit with configuration only (settings, connectors, prompts, simple agents)?
│         ├── Yes ─> CONFIGURE an existing or new product
│         └── No  ─> Is the gap small and stable, and can it be closed with supported extensions?
│                   ├── Yes ─> BUY and EXTEND (supported APIs, connectors, low-code agents)
│                   └── No  ─> Go to the build question below
└── No ──> Is this use case core to your differentiation, or does it need control
           over data, models or behaviour that no product offers?
           ├── Yes ─> Do you have (or can you fund) the skills to build, evaluate,
           │         secure and operate it for its whole life?
           │         ├── Yes ─> BUILD on a cloud AI platform or open-weight models
           │         └── No  ─> PARTNER, or narrow the scope until a product fits
           └── No  ─> WAIT or RE-SCOPE: revisit the requirement; the market changes quickly
```

| Approach | Typical strengths | Typical trade-offs |
|---|---|---|
| **Configure** | Fast; vendor carries much of the security and maintenance; predictable per-seat cost | Limited control over models and data flows; vendor roadmap dependency |
| **Buy and extend** | Uses vendor platform while adding your data and workflows | Extensions need owners; changes to the platform can break them |
| **Build** | Maximum control over data, models, user experience and cost structure | You own evaluation, security, monitoring and support; needs sustained skills and budget |

**For small organisations:** configuring an existing product is usually the most practical route. Building is rarely justified without in-house engineering capacity.

## Procurement considerations

- **Start with your obligations.** Public-sector bodies must follow their procurement rules and frameworks; regulated firms may have outsourcing and third-party risk rules. Involve procurement early.
- **Contract terms to check:** data processing agreement; training-on-data commitments; retention and deletion; sub-processor changes and notice; data location; security incident notification; service levels; liability and indemnities (including any intellectual property indemnity and its conditions); audit rights; price change and renewal terms; exit assistance.
- **Pricing structures change frequently.** Model scenarios for light, typical and heavy usage, and check overage, credit and minimum-seat terms. Ask how pricing changes at renewal.
- **Pilot licences.** Negotiate short-term or limited-seat access for the evaluation, and agree what happens to pilot data.
- **AI-specific risk management.** Frameworks such as the NIST AI Risk Management Framework [2] and ISO/IEC 42001 [1] can structure supplier questions about how vendors govern their AI. See [standards and frameworks](../../resources/standards-and-frameworks.md).
- **Security of AI applications.** The OWASP Top 10 for LLM Applications [3] provides a shared vocabulary for risks such as prompt injection and sensitive information disclosure when questioning vendors.
- **Record the decision.** Keep the requirements, weights, scores, evaluation evidence, risks accepted and exit plan. This supports audit and makes the next review faster.

## A lighter version for small organisations

If you have limited time and no dedicated IT or procurement team:

1. **List three tasks** you want help with and the data each involves.
2. **Set four must-haves**, for example: no training on our content on the plan we buy; admin can remove users; works on the devices we use; affordable at our size.
3. **Pick two options** that meet them. Check the vendor's business-plan data terms page, not the marketing page.
4. **Test each on ten real tasks** with sensitive details removed. Two people score the results independently.
5. **Try the better one for a month** with a few users, then decide. Write down why on one page.

## Checklist

- [ ] Use cases and data classifications written down
- [ ] Must-haves agreed and justified
- [ ] Weights agreed before demonstrations
- [ ] Test set built from real tasks, including risk cases
- [ ] Same conditions and blind scoring used across options
- [ ] Controls tested by security and data protection
- [ ] Three-year cost model with usage scenarios
- [ ] Contract terms checked against the list above
- [ ] Exit plan documented
- [ ] Decision record stored

## Related pages

- [Tool categories](tool-categories.md)
- [Tool guides](tool-guides/README.md)
- [Vendor due diligence](../../assessments/vendor-due-diligence.md)
- [Business case template](../../toolkits/business-case-template.md)
- [AI risk assessment](../../assessments/ai-risk-assessment.md)
- [Data protection](../governance/data-protection.md)

## Sources

1. ISO, *ISO/IEC 42001:2023 Information technology — Artificial intelligence — Management system*, 2023. https://www.iso.org/standard/42001
2. NIST, *AI Risk Management Framework* (AI RMF 1.0, January 2023; Generative AI Profile NIST-AI-600-1, July 2024). https://www.nist.gov/itl/ai-risk-management-framework
3. OWASP GenAI Security Project, *OWASP Top 10 for LLM Applications 2026*. https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/

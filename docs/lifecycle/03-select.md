# Stage 3: Select

> **Who this is for:** Business owners, IT and platform teams, procurement, and anyone choosing which use cases to pursue and which tools to use.
> **Last reviewed:** 2026-10

Select turns assessed opportunities into decisions: which use cases go forward first, whether to build, buy or configure, which tool meets your criteria, and on what contractual terms. The guide does not recommend vendors. Instead, this page gives a repeatable method so that the choice is documented, defensible and tied to the problem you set out to solve. It works whether you are a small team choosing between two subscription products or an enterprise running a formal tender.

## Purpose

- Prioritise use cases on value, feasibility and risk.
- Decide the delivery approach: buy a packaged tool, configure a platform, or build.
- Evaluate candidate tools against criteria agreed in advance.
- Complete due diligence and procurement on terms that meet the conditions set in Assess.

## Inputs

- Assessed opportunities with conditions, from [Assess](02-assess.md).
- Organisational constraints: existing platforms and licences, identity provider, data residency needs, budget, procurement rules.
- [Tool categories](../tools/tool-categories.md) and [choosing tools](../tools/choosing-tools.md).

## Activities

1. **Prioritise use cases.** Score each assessed opportunity with the [use case prioritisation](../../assessments/use-case-prioritisation.md) assessment on value (size of problem, number of people affected, strategic fit), feasibility (data, integration, skills, time to value) and risk (tier, residual risk, reversibility). Pick a small number to take forward; early wins with measurable outcomes build credibility.
2. **Decide build, buy or configure.** Use the decision table below.
3. **Define requirements and criteria before looking at products.** Translate the problem statement and Assess conditions into must-haves and weighted nice-to-haves. Agree weights with stakeholders before demos, to reduce the influence of presentation quality.
4. **Create a long list and shortlist.** Identify tools in the relevant category that meet must-haves. Where one vendor is considered, consider comparable alternatives too.
5. **Evaluate.** Use structured demos with your own scenarios and, where possible, a hands-on trial with non-sensitive data. Score against criteria. Keep notes of evidence for each score.
6. **Run vendor due diligence.** Use the [vendor due diligence](../../assessments/vendor-due-diligence.md) questionnaire. Verify claims against contract terms and documentation, not marketing.
7. **Negotiate and procure.** Ensure contract terms reflect requirements: data use and retention, sub-processors, data location, security, audit rights, notification of model or service changes, IP and indemnity provisions, exit and data return.
8. **Write the business case.** Record the problem, the option chosen, alternatives considered, costs (licences, implementation, training, support, monitoring), expected benefits and how they will be measured. See the [business case template](../../toolkits/business-case-template.md).

### Build, buy or configure

| Approach | What it means | Fits when | Watch for |
|---|---|---|---|
| Buy (packaged) | Subscribe to a ready-made tool, such as an AI assistant within productivity software | Common tasks; speed matters; limited in-house engineering | Data terms; limited customisation; dependence on vendor roadmap |
| Configure | Use a platform's building blocks (custom assistants, retrieval over your documents, workflow tools) with little or no code | Need to tailor to your content or process; some technical capacity | Permission design; prompt and content maintenance; platform limits |
| Build | Develop an application using model APIs or open-weight models | Differentiating capability; unusual data or integration needs; strong engineering and MLOps capacity | Total cost of ownership; evaluation and monitoring burden; security of the application layer; staff retention |

Many organisations combine approaches: a packaged assistant for general productivity, plus configured or built solutions for a few specific processes.

### Example evaluation criteria

| Criterion | Example questions |
|---|---|
| Fit to problem | Does it perform well on our scenarios with our content? |
| Data protection | Is customer data used to train models? What are retention periods? Where is data processed? Is a data processing agreement offered? |
| Security | Single sign-on, role-based access, audit logs, encryption, certifications (for example ISO/IEC 27001, SOC 2 reports) |
| Admin controls | Can we restrict features, connectors, plug-ins and data sources? |
| Integration | Does it work with our identity provider, document stores and line-of-business systems? |
| Transparency | Does the vendor document the models used, known limitations and change notification practices? |
| Accessibility | Does it meet the accessibility standards your organisation is required to follow? |
| Cost | Licence model, usage-based charges, implementation and support costs |
| Exit | Can we export prompts, configurations and data? What happens to our data on termination? |
| Regulatory support | Does the vendor provide documentation that helps you meet your obligations (for example, as a deployer under the EU AI Act)? |

See [choosing tools](../tools/choosing-tools.md) for a fuller criteria set.

## Roles involved

| Role | Contribution |
|---|---|
| Business owner | Owns requirements and the business case; leads scenario testing |
| IT and platform | Architecture fit, integration, identity, administration |
| Procurement | Process, competition rules, commercial terms |
| Security | Security due diligence and contractual controls |
| Data protection | Data processing terms, transfers, DPIA updates |
| Legal | Contract terms including IP, indemnity, liability |
| Finance | Total cost of ownership and budget |
| Pilot users | Hands-on evaluation |
| Executive sponsor | Approves the business case |

## Outputs and deliverables

- Prioritised use case list with scores.
- Build/buy/configure decision with rationale.
- Requirements and weighted criteria, agreed before evaluation.
- Evaluation scores and evidence.
- Completed vendor due diligence.
- Signed contract or order (or a trial agreement for the pilot).
- Approved business case.

## Decision gate: ready to move to Pilot?

- [ ] Use cases for piloting are prioritised and approved.
- [ ] The delivery approach is decided and documented.
- [ ] Criteria were agreed before evaluation, and scores are evidenced.
- [ ] Vendor due diligence is complete; any gaps have mitigations.
- [ ] Contract or trial terms meet the conditions set in Assess (data use, retention, location, security, change notification).
- [ ] The DPIA and risk assessment are updated to reflect the chosen tool.
- [ ] The business case, including measurement approach, is approved.
- [ ] Budget for the pilot, including training and support time, is confirmed.

## Linked assessments and toolkits

- [Use case prioritisation](../../assessments/use-case-prioritisation.md)
- [Vendor due diligence](../../assessments/vendor-due-diligence.md)
- [Business case template](../../toolkits/business-case-template.md)
- [Choosing tools](../tools/choosing-tools.md) and [tool categories](../tools/tool-categories.md)
- Once chosen: [tool guides](../tools/tool-guides/README.md)

## Variations by organisation size

**Small organisations.** Selection may be a comparison of two or three subscription products using a one-page criteria table and a two-week trial. Read the business-tier data terms carefully: consumer and business versions of the same product often have different data use and retention terms. Check whether the tool works with the productivity suite you already use.

**Enterprises.** Expect formal procurement rules, possibly public procurement law for public bodies. Engage procurement early; frameworks and existing enterprise agreements may shorten the route. Third-party risk management, architecture review and legal negotiation can each take weeks, so run them in parallel where possible.

## Common pitfalls

- **Choosing on demos alone.** Vendor demos use favourable scenarios. Test with your own content and tasks.
- **Setting criteria after seeing products.** This invites rationalising a preferred choice.
- **Ignoring total cost.** Licences are often a minority of the cost; training, support, change management and monitoring add up.
- **Accepting default terms.** Data use, retention and change notification terms are often negotiable at enterprise scale, and worth reading at any scale.
- **Over-building.** Building a custom solution for a problem a configured product could solve creates long-term maintenance obligations.
- **No exit plan.** Prompts, configurations and workflows become valuable assets; check you can take them with you.

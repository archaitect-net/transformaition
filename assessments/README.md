# Assessments

> **Who this is for:** Anyone who needs to make a structured judgement about AI adoption: leaders, programme leads, managers, IT, data, risk and procurement teams. Each assessment states who should complete it.
> **Last reviewed:** 2026-10

This section contains six scored assessments that turn common adoption questions into structured, repeatable judgements. Each one has explicit 0–4 (or equivalent) scoring descriptors, default weightings you can adjust, a scoring method, interpretation bands and "what to do next" for each band. This page explains what each assessment is for, who should complete it, where it fits in the [adoption lifecycle](../docs/lifecycle/README.md), and how to score and interpret results consistently. All six are practical heuristics based on published frameworks and practitioner consensus; none is a validated or certified instrument.

## The six assessments at a glance

| Assessment | What it answers | Unit of assessment | Who completes it | Lifecycle stage | Time |
|---|---|---|---|---|---|
| [Organisational readiness](organisational-readiness.md) | Are we ready, as an organisation, to adopt AI tools? Where are the gaps? | Whole organisation (or business unit) | Sponsor, IT, data protection or risk, HR, staff representative | [Assess](../docs/lifecycle/02-assess.md); repeat before [Scale](../docs/lifecycle/05-scale.md) | 1–3 hours |
| [Maturity model](maturity-model.md) | Where are we now, and what does the next level look like? | Whole organisation | Leadership team, programme lead | [Discover](../docs/lifecycle/01-discover.md), [Assess](../docs/lifecycle/02-assess.md), annual review | 30–60 minutes |
| [Use case prioritisation](use-case-prioritisation.md) | Which use cases should we do first? | Portfolio of candidate use cases | Business owners, people who do the work, IT, risk | [Discover](../docs/lifecycle/01-discover.md), [Select](../docs/lifecycle/03-select.md); re-score after [Pilot](../docs/lifecycle/04-pilot.md) | 20–30 minutes per use case |
| [Data readiness](data-readiness.md) | Is the data behind this use case fit for purpose? | One use case and its data sources | Data owner, data or IT team, data protection | [Assess](../docs/lifecycle/02-assess.md); before [Scale](../docs/lifecycle/05-scale.md) | 1–2 hours per use case |
| [AI risk assessment](ai-risk-assessment.md) | What could go wrong with this use case, and is the residual risk acceptable? Do we need a DPIA or legal review? | One use case | Use case owner, with risk, data protection, security, legal as triggered | [Assess](../docs/lifecycle/02-assess.md); update after [Pilot](../docs/lifecycle/04-pilot.md); review in [Operate](../docs/lifecycle/06-operate.md) | 20 minutes (screening) to several days (full) |
| [Vendor due diligence](vendor-due-diligence.md) | Does this vendor's product meet our requirements on data, security, IP, continuity and contract? | One vendor product or tier | Procurement, IT, security, data protection, legal | [Select](../docs/lifecycle/03-select.md); renewal | 2–8 hours per vendor |

## How they fit together

| Level | Assessments | Output |
|---|---|---|
| Organisation | Maturity model, organisational readiness | Gaps, gated items and a roadmap |
| Use case portfolio | Use case prioritisation | A ranked shortlist |
| Single use case | Data readiness, AI risk assessment | Go / no-go and conditions for a pilot |
| Supplier | Vendor due diligence | Acceptable / conditions / not acceptable for each tool |

A typical sequence:

1. **Organisation first.** Use the [maturity model](maturity-model.md) for a quick picture, then the [readiness assessment](organisational-readiness.md) for detail. Fix any gated items (for example, no acceptable use policy) before pilots.
2. **Choose use cases.** Score candidates with [use case prioritisation](use-case-prioritisation.md).
3. **Check each shortlisted use case.** Run [data readiness](data-readiness.md) and the [AI risk assessment](ai-risk-assessment.md) screening. The screening tells you how deep the risk assessment needs to be and whether a DPIA or legal review is triggered.
4. **Check the supplier.** Run [vendor due diligence](vendor-due-diligence.md) for any tool not already assessed.
5. **Decide, pilot, re-score.** After the pilot, update the use case scores and risk assessment with evidence.

**Small organisations** can compress this: the maturity model quick read, a use case scoring session, the risk screening questionnaire, and the essential (E) vendor questions may be enough for low-risk uses of a mainstream tool.

## Common scoring conventions

All six assessments follow these conventions so that results are consistent.

| Convention | Rule |
|---|---|
| Score what is true today | Not what is planned or promised |
| Evidence for high scores | A score of 3 or 4 (or "meets" in vendor due diligence) needs a piece of evidence you can point to |
| Between levels | Choose the lower level |
| "Don't know" | Scores 0. Not knowing is a gap |
| N/A | Only when a question genuinely does not apply; excluded from averages |
| Independent then consensus | Where several people score, score individually first, then discuss differences of two or more points |
| Weights | Defaults are judgements; adjust only before scoring and record the change |
| Gates and blockers | Some answers stop progress regardless of the average. Always check them |

## Interpreting results

- **Profiles beat totals.** Look at the spread across dimensions or axes before the overall number. The lowest dimension often constrains everything else.
- **Gates beat averages.** A high average with a failed gate means "not yet".
- **Scores are for your decisions, not for benchmarking.** These assessments are not calibrated across organisations. Use them to compare your own position over time, or to compare options within one decision.
- **Re-score with evidence.** Scores based on estimates should be updated after pilots. Large changes are normal and improve future estimates.
- **Record decisions.** Store results with your [use case register](../toolkits/use-case-register-template.md) or governance records, including who scored, when, and what was decided.

## Bands used across the section

Each assessment has its own band thresholds, but the bands follow a common pattern:

| Pattern | Typical meaning | Typical response |
|---|---|---|
| Lowest band | Foundations missing or significant gaps | Fix blockers; narrow scope; do not commit to large investments |
| Second band | Partial; usable with conditions | Limited, supervised pilots with explicit mitigations |
| Third band | Largely in place | Proceed; track open actions |
| Highest band | Strong, evidenced | Proceed; use as a reference; reassess periodically |

## What these assessments are not

- **Not legal advice.** The risk assessment screening flags when legal or data protection review is needed; it does not replace that review or a DPIA.
- **Not certification.** Scoring well does not mean conformity with ISO/IEC 42001 [1], the NIST AI Risk Management Framework [2] or any regulation.
- **Not validated instruments.** The questions draw on published frameworks and practitioner consensus. Their weights and thresholds have not been empirically tested as predictors of outcomes.

## Contributing

Improvements to questions, descriptors and worked examples are welcome. Please explain the rationale and cite any framework you draw on. See [CONTRIBUTING.md](../CONTRIBUTING.md).

## Sources

1. ISO/IEC, *ISO/IEC 42001:2023 Information technology — Artificial intelligence — Management system*, December 2023. https://www.iso.org/standard/42001
2. NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, January 2023. https://doi.org/10.6028/NIST.AI.100-1

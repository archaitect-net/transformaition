# Business case template

> **Who this is for:** Sponsors, programme leads, finance business partners and managers preparing a case to invest in AI tools or a specific AI use case. Scales from a one-page case for a small team to a full investment case.
> **Last reviewed:** 2026-10

This template helps you build an honest business case for an AI investment. It covers the problem and options, a full cost model (licences, enablement, change and run costs, not just subscriptions), benefits estimated with conservative and explicit assumptions, a sensitivity analysis showing what happens if assumptions are wrong, risks, and how benefits will be measured. Guidance notes in blockquotes explain each section; replace [bracketed placeholders]. A fictional worked example shows the calculations. Use it at the [Select](../docs/lifecycle/03-select.md) stage for a pilot, and again before [Scale](../docs/lifecycle/05-scale.md) using pilot evidence.

> **Guidance: principles for an honest AI business case**
>
> - **Count all costs.** Licences are often a minority of total cost once enablement, change, data preparation and ongoing support are included.
> - **Be conservative about benefits.** Research on productivity effects shows large variation by task and user. A randomised field experiment with 758 consultants found substantial gains on tasks within the AI's capabilities but lower accuracy on a task outside them (Moderate evidence; the study was run with the consulting firm whose staff participated) [1]. A study of 5,179 customer support agents found an average 14% productivity increase, concentrated among less experienced workers (Moderate evidence) [2]. A small randomised trial with 16 experienced open-source developers found they took 19% longer with AI tools, while believing they were faster (Limited evidence; small sample, authors note results are dated) [3]. Evidence from one context does not transfer automatically to yours. See [evidence on impact](../docs/foundations/evidence-on-impact.md).
> - **Time saved is not money saved.** Unless time saved is redeployed to valued work, or reduces cost (e.g. overtime, contractors, backlog), it is a capacity benefit, not a cash benefit. Say which.
> - **Use your own baselines.** Measure current performance before the pilot. Vendor-supplied figures should be labelled and not used as the central case.
> - **Show the range.** Present low, central and high cases and the break-even point.

---

## [Use case / programme name] Business case

| | |
|---|---|
| **Sponsor** | [name, role] |
| **Author** | [name] |
| **Version and date** | [ ] |
| **Decision requested** | [e.g. approve a 3-month pilot for 40 users at a cost of £X] |
| **Decision maker** | [ ] |
| **Related records** | [use case register ID; risk assessment; vendor due diligence] |

## 1. Executive summary

> **Guidance:** Half a page. State the problem, the proposed solution, total cost over [3] years, central-case benefit, break-even under the low case, key risks, and the decision requested. Write this last.

[ ]

## 2. Problem and opportunity

- **Current situation:** [what happens today; volumes; who is involved]
- **Problem:** [what is slow, costly, error-prone, or unmet]
- **Baseline measures:** [time per task, volume, error rate, backlog, satisfaction; how measured and when]
- **Strategic fit:** [link to organisational objectives]
- **Why now:** [ ]

## 3. Options considered

> **Guidance:** Always include "do nothing" and at least one non-AI or lower-cost option. This guards against selecting AI because it is new rather than because it is best.

| Option | Description | Indicative cost | Main benefits | Main drawbacks |
|---|---|---|---|---|
| 0. Do nothing | [ ] | [ ] | [ ] | [ ] |
| 1. Non-AI improvement | [e.g. process redesign, templates, existing software features] | [ ] | [ ] | [ ] |
| 2. [AI option A] | [ ] | [ ] | [ ] | [ ] |
| 3. [AI option B or phased approach] | [ ] | [ ] | [ ] | [ ] |

**Preferred option and why:** [ ]

## 4. Costs

> **Guidance:** Include one-off and recurring costs over the appraisal period (commonly 3 years for software). Include internal staff time at a loaded cost rate agreed with finance. Add contingency for uncertainty (state the percentage and why).

| Category | Item | Year 0 (one-off) | Year 1 | Year 2 | Year 3 | Notes / assumptions |
|---|---|---|---|---|---|---|
| **Licences** | User licences [n users × price] | | | | | [price source and date; expected price changes] |
| | Platform, API or consumption costs | | | | | [usage assumption; cap] |
| | Add-ons (e.g. data protection, security, compliance features) | | | | | |
| **Enablement** | Configuration and integration | | | | | |
| | Data preparation and permission remediation | | | | | [from [data readiness](../assessments/data-readiness.md)] |
| | Security, data protection and legal review | | | | | |
| | Testing and evaluation | | | | | |
| **Change** | Training design and delivery | | | | | [[training plan](training-plan-template.md)] |
| | Staff time in training | | | | | [hours × users × cost rate] |
| | Communications and change management | | | | | |
| | Champions' time | | | | | |
| | Productivity dip during adoption | | | | | [assumption] |
| **Run** | Service ownership and support | | | | | |
| | Monitoring, audit and governance | | | | | |
| | Prompt library and content maintenance | | | | | |
| | Periodic re-assessment (risk, vendor) | | | | | |
| **Contingency** | [ ]% | | | | | |
| **Total** | | | | | | |

## 5. Benefits

> **Guidance:** For each benefit, state the mechanism, the measure, the baseline, the assumption, the evidence for the assumption, and whether the benefit is cash-releasing, cost-avoiding, capacity (time freed) or non-financial. Apply an **adoption rate** (not everyone will use the tool for every task) and a **realisation factor** (not all time saved converts into value).

| # | Benefit | Type | Measure | Baseline | Assumption (central) | Evidence for assumption | Owner |
|---|---|---|---|---|---|---|---|
| B1 | [e.g. Reduced time drafting responses] | [Capacity] | [minutes per response] | [ ] | [ ] | [pilot data / own measurement / published study, labelled] | [ ] |
| B2 | [e.g. Reduced external translation spend] | [Cash-releasing] | [£ per year] | [ ] | [ ] | [ ] | [ ] |
| B3 | [e.g. Improved consistency of responses] | [Non-financial] | [quality audit score] | [ ] | [ ] | [ ] | [ ] |

**Calculation of financial benefits**

`Annual value = users × tasks per user per year × time saved per task × adoption rate × realisation factor × cost rate`

| Parameter | Low | Central | High | Source |
|---|---|---|---|---|
| Users | [ ] | [ ] | [ ] | |
| Tasks per user per year | [ ] | [ ] | [ ] | |
| Time saved per task (hours) | [ ] | [ ] | [ ] | |
| Adoption rate (% of tasks where tool is used) | [ ] | [ ] | [ ] | |
| Realisation factor (% of time saved converted to value) | [ ] | [ ] | [ ] | |
| Loaded cost rate (£/hour) | [ ] | [ ] | [ ] | |

**Non-financial benefits:** [quality, staff experience, customer experience, risk reduction; describe how each will be measured]

**Dis-benefits:** [for example, time spent checking outputs, new review steps, reduced skill development for junior staff; quantify where possible]

## 6. Financial summary

| | Year 0 | Year 1 | Year 2 | Year 3 | Total |
|---|---|---|---|---|---|
| Costs | | | | | |
| Financial benefits (central) | | | | | |
| Net (central) | | | | | |
| Cumulative net (central) | | | | | |

- **Payback period (central):** [ ]
- **Net present value, if required by your finance policy:** [ ] at [discount rate]

## 7. Sensitivity analysis

> **Guidance:** Show how the result changes when key assumptions change. At minimum: low, central and high scenarios, and the break-even value of the most uncertain assumption (usually time saved per task or adoption rate).

| Scenario | Key assumptions | 3-year net value |
|---|---|---|
| Low | [ ] | [ ] |
| Central | [ ] | [ ] |
| High | [ ] | [ ] |

**One-at-a-time sensitivity (central case, varying one assumption):**

| Assumption | Value at which net value = 0 (break-even) | How confident are we it will exceed this? |
|---|---|---|
| Time saved per task | [ ] | [ ] |
| Adoption rate | [ ] | [ ] |
| Realisation factor | [ ] | [ ] |
| Licence price | [ ] | [ ] |

## 8. Risks and dependencies

| Risk or dependency | Impact on case | Mitigation | Owner |
|---|---|---|---|
| Benefits lower than expected | [ ] | Pilot with baseline and stop criteria | |
| Price changes at renewal | [ ] | Contract terms; review exit options | |
| Data not ready | [ ] | Data remediation included in costs | |
| Low adoption | [ ] | Training, champions, manager engagement | |
| Regulatory or data protection issues | [ ] | [AI risk assessment](../assessments/ai-risk-assessment.md); DPIA where required | |
| Model or product changes | [ ] | Re-test; vendor notification terms | |

## 9. Measurement and benefits realisation

- **How benefits will be measured:** [methods; see [measuring value](../docs/measurement/measuring-value.md)]
- **When:** [baseline date; checkpoints]
- **Stop or change criteria:** [e.g. if time saved after 8 weeks is below the break-even value, stop or redesign]
- **Benefits owner:** [ ]

## 10. Implementation outline

[Key phases, dates and resources; link to [pilot plan](pilot-plan-template.md)]

## 11. Recommendation

[ ]

---

## Worked example (fictional)

> Everything in this example is **fictional** and uses invented numbers to illustrate the calculations. Do not use these figures as benchmarks.

*Northbank Legal Services* (fictional), a 60-person firm, considers AI assistance for drafting first versions of standard client letters. 20 fee-earners each draft about 400 such letters a year. A one-week baseline measured 30 minutes per letter.

**Benefit parameters (fictional)**

| Parameter | Low | Central | High |
|---|---|---|---|
| Users | 20 | 20 | 20 |
| Letters per user per year | 400 | 400 | 400 |
| Time saved per letter (hours) | 0.05 (3 min) | 0.10 (6 min) | 0.17 (10 min) |
| Adoption rate | 40% | 60% | 75% |
| Realisation factor | 30% | 50% | 70% |
| Loaded cost rate (£/hour) | 60 | 60 | 60 |
| **Annual value** | **£2,880** | **£14,400** | **£42,840** |

Central calculation: 20 users × 400 letters = 8,000 letters; × 0.10 hours = 800 hours; × 60% adoption = 480 hours; × 50% realisation = 240 hours; × £60 = **£14,400** a year.

**Costs (fictional, annual unless stated)**

| Item | Amount |
|---|---|
| Licences: 20 users × £300/year | £6,000 |
| Configuration and template prompts (one-off) | £3,000 |
| Training: 20 users × 3 hours × £60 + design £1,500 (one-off) | £5,100 |
| Support and governance: 2 hours/week × £50 × 46 weeks | £4,600 |
| Contingency 15% (year 1) | £2,805 |
| **Year 1 total** | **£21,505** |
| **Years 2 and 3 (licences + support + 15%)** | **£12,190 each** |

**Result (fictional):**

| Scenario | 3-year costs | 3-year benefits | 3-year net |
|---|---|---|---|
| Low | £45,885 | £8,640 | −£37,245 |
| Central | £45,885 | £43,200 | −£2,685 |
| High | £45,885 | £128,520 | £82,635 |

The central case is roughly break-even, the low case loses money, and the high case is clearly positive.

**Break-even (fictional):** Holding other central assumptions, the three-year case breaks even at about 6.4 minutes saved per letter. The firm decides to run an 8-week pilot to measure time saved, with a stop criterion of under 5 minutes per letter, and to explore whether the tool also reduces review time, which was not included in the benefits.

**What the example shows:** the result depends heavily on adoption and realisation assumptions, and a plausible-looking central case can sit close to break-even. Build the model in a spreadsheet, have someone else check the calculations, and replace assumptions with pilot data before deciding to scale.

## Sources

1. Dell'Acqua, F. et al., *Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality*, Harvard Business School Working Paper 24-013, September 2023. https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf
2. Brynjolfsson, E., Li, D. and Raymond, L., *Generative AI at Work*, NBER Working Paper 31161 (2023); published in *The Quarterly Journal of Economics* 140(2), 2025. https://www.nber.org/papers/w31161
3. METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*, July 2025. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/

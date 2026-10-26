# Measuring value

> **Who this is for:** Leaders approving investment, managers and pilot leads who need to show results, finance partners, and anyone asked "is AI working for us?"
> **Last reviewed:** 2026-10

This page gives you a practical framework for measuring whether AI tools are delivering value, across six dimensions: adoption, efficiency, quality, risk, experience and financial. It explains how to set baselines, how to estimate what would have happened anyway (the counterfactual), how to avoid metrics that look good but mean little, and how to scale measurement effort to the size of your organisation and the stakes of the decision. A worked example shows the framework applied to a realistic pilot. The central message is that self-reported time savings and usage counts are not evidence of value on their own; the best measures are tied to outcomes you already care about, compared against a credible baseline.

## Why measurement is hard

Evidence from published studies shows why care is needed:

- **Perception differs from measurement.** In one randomised study, experienced developers believed AI had sped them up by about 20% when measured task time had in fact increased by 19% [1].
- **Self-report and observed results can diverge.** In 2025, a UK cross-government experiment reported average self-reported savings of 26 minutes a day [2], while a separate departmental evaluation, using diaries, interviews and observed tasks, found no robust evidence of productivity improvement and lower accuracy on some tasks [3].
- **Task gains shrink at the organisational level.** A study linking surveys to administrative data for around 25,000 Danish workers per round found self-reported time savings of 2.8% of work hours and no detectable effect on earnings or hours [4]. Time saved does not create value unless it is redeployed.

See [evidence on impact](../foundations/evidence-on-impact.md) for the full picture.

## Start with the question, not the dashboard

Before choosing metrics, write down:

1. **The decision the measurement will inform.** For example: "Should we extend licences from 50 to 400 people?" or "Should we continue funding this use case after the pilot?"
2. **The outcome that matters for that use case.** Faster response to customers? Fewer errors? Capacity to take on more work without hiring? Better staff retention?
3. **The hypothesis.** "Drafting assistance will reduce average time to complete a first draft of a tender response by at least 20% without reducing evaluator scores."
4. **What result would change your mind.** Agree in advance what counts as success, partial success and failure. This guards against reinterpreting results after the event.

Record these in your [pilot plan](../../toolkits/pilot-plan-template.md) and [use case register](../../toolkits/use-case-register-template.md).

## The six-dimension framework

Measure across all six dimensions, but choose only the two or three metrics per dimension that matter for your use case. A balanced set stops you optimising one dimension (such as speed) at the expense of another (such as quality or risk).

### 1. Adoption

Whether people are using the tool, and how deeply. Adoption is a *leading* indicator: necessary for value, but not evidence of it.

| Metric | How to measure | Watch out for |
|---|---|---|
| Active users (weekly or monthly) as a share of licensed users | Admin dashboards | High counts can reflect curiosity, not value |
| Frequency and depth of use (sessions per user, use across different tasks) | Admin dashboards, telemetry | Volume of prompts is not value |
| Use within the target workflow | Workflow data, sampling | General use may not touch the target process |
| Licence utilisation | Licence reports | Useful for cost control |
| Drop-off after initial period | Cohort analysis | Novelty effects fade |

### 2. Efficiency

Whether work takes less time, effort or cost, or more work gets done with the same resources.

| Metric | How to measure | Watch out for |
|---|---|---|
| Time per task or case | Workflow systems, time-and-motion sampling, timed observation | Self-estimates are unreliable |
| Throughput (cases, tickets, documents completed per person per period) | Operational systems | Can rise while quality falls |
| Cycle time / turnaround time | Operational systems | Bottlenecks may simply move downstream |
| Rework rate | Quality systems, sampling | Rework may shift to reviewers |
| Time spent reviewing AI output | Observation, sampling | Often omitted from savings calculations |

### 3. Quality

Whether outputs are as good as, or better than, before.

| Metric | How to measure | Watch out for |
|---|---|---|
| Expert-rated quality, blind to whether AI was used | Structured rubric, independent reviewers | Requires effort, but is the most credible quality measure |
| Error or defect rate | Sampling, quality assurance, incident logs | Subtle errors may surface late |
| Accuracy of facts and citations | Sample audit | Hallucinated references can look plausible |
| Customer or stakeholder outcome (resolution rate, satisfaction, complaints) | Existing systems | Influenced by many factors |
| Consistency across staff | Variance in quality scores | AI may narrow or widen differences |

### 4. Risk

Whether the use is staying within your risk appetite. See [risk management](../governance/risk-management.md).

| Metric | How to measure | Watch out for |
|---|---|---|
| Data protection or security incidents linked to AI | Incident management | Under-reporting |
| Policy breaches (such as prohibited data entered) | Data loss prevention tools, audits | Detection depends on controls in place |
| Use of unapproved tools (shadow AI) | Network and identity logs, surveys | Absence of evidence is not evidence of absence |
| Proportion of high-risk outputs reviewed by a person | Workflow records | Review can become a rubber stamp |
| Complaints or challenges about AI-assisted decisions | Complaints handling | Particularly important for decisions about individuals |

### 5. Experience

How staff and, where relevant, customers experience the change.

| Metric | How to measure | Watch out for |
|---|---|---|
| User satisfaction and perceived usefulness | Short pulse surveys | Satisfaction does not equal productivity [3] |
| Confidence and skill | Self-assessment plus practical checks | Overconfidence is a risk |
| Workload and wellbeing | Pulse surveys, existing engagement surveys | Time saved may be filled with more intense work |
| Concerns about job security or monitoring | Surveys, consultation forums | Unaddressed concerns depress adoption |
| Customer experience | Existing customer measures | Disclose AI use where required |

### 6. Financial

Whether benefits exceed costs. See the [business case template](../../toolkits/business-case-template.md).

| Metric | How to measure | Watch out for |
|---|---|---|
| Total cost of ownership | Licences, usage-based fees, integration, security, training, support, governance, staff time | Usage-based costs can grow unpredictably |
| Cash-releasing benefits | Reduced external spend, avoided recruitment, reduced overtime | Only count savings that actually occur |
| Non-cash-releasing benefits | Capacity redeployed to other work, valued at cost | Only real if the capacity is used for something of value |
| Revenue or growth effects | Sales, conversion, new services | Hard to attribute |
| Cost per outcome (per case resolved, per document produced) | Total cost divided by outcomes | Better than cost per user |

**Cash-releasing versus non-cash-releasing.** Most early AI benefits are time savings, which do not reduce costs unless you reduce spend or redeploy the time to valued work. Be explicit about which you are claiming, and how the time will be used.

## Baselines

Without a baseline you cannot estimate change. Set one before rollout.

- **Use existing data first.** Operational systems often already record cycle times, volumes, error rates and satisfaction. These are cheaper and more credible than new surveys.
- **Measure for long enough** to capture normal variation (for example, at least several weeks for processes with weekly cycles, and allow for seasonal peaks).
- **Measure the same way before and after.** Changing the definition or method partway through invalidates the comparison.
- **Include quality as well as speed** in the baseline. Otherwise you cannot tell whether faster means worse.
- **Record context**: team size, workload, process changes and other initiatives running at the same time.

If you have no historical data, take a short manual sample (for example, time 20 typical tasks and have them quality-rated) before the pilot starts.

## Counterfactuals: what would have happened anyway?

Before-and-after comparisons alone can mislead, because other things change at the same time (seasonality, workload, new staff, process changes, and the extra attention a pilot brings). The UK Treasury's guidance on evaluation, the *Magenta Book*, describes how to choose an evaluation approach proportionate to the decision [5]. Common options, from most to least rigorous:

| Approach | How it works | When it is feasible | Main weakness |
|---|---|---|---|
| **Randomised comparison** | Randomly assign people, teams or tasks to have access or not | Phased rollouts where licence numbers are limited anyway | Organisational resistance; contamination if people share tools |
| **Staggered rollout** | Introduce the tool to groups at different times and compare groups that have it with those that do not yet | Most rollouts, at little extra cost | Groups may differ; requires planning the order |
| **Matched comparison group** | Compare users with similar non-users (same role, workload, past performance) | When randomisation is not possible | Volunteers and keen adopters differ from others |
| **Difference-in-differences** | Compare the change over time in the pilot group with the change over time in a comparison group | When both groups have before-and-after data | Assumes the groups would have moved in parallel |
| **Within-person task comparison** | The same people do comparable tasks with and without AI | Small teams, short tests | Learning and task-selection effects |
| **Before-and-after only** | Compare the same group before and after | Very small organisations | Cannot separate AI from everything else that changed |

**Practical tip.** If you are going to roll out in phases anyway (for budget or support reasons), decide the order randomly or by a fixed rule rather than by who asks first. This turns an ordinary rollout into a credible comparison at almost no cost.

**Volunteer bias.** Early pilots usually involve enthusiasts. Their results are likely to overstate what a wider population will achieve. Where possible include a randomly selected group alongside volunteers, as the UK Department for Business and Trade pilot did [3].

## Avoiding vanity metrics

A vanity metric looks impressive but does not show value.

| Vanity metric | Why it misleads | Better alternative |
|---|---|---|
| Number of licences issued | Measures spending, not use or value | Active use within target workflow |
| Total prompts sent | Volume, not outcome | Outcomes per task (time, quality) |
| Self-reported "hours saved" | Unreliable; savings may not be redeployed | Measured time on task, plus what the time was used for |
| "X% of staff say AI makes them more productive" | Perception, which can diverge from measured results [1] | Measured output and quality, with satisfaction as a supporting measure |
| Lines of code generated or accepted suggestions | Volume, not working, maintainable software | Delivery throughput, change failure rate, defect rates |
| Number of use cases identified | Activity, not value | Number of use cases meeting their success criteria |
| Vendor-supplied ROI estimates | Not independent, often based on assumptions | Your own measured results |

## Proportionate measurement

Match effort to the size of the decision.

| Situation | Proportionate approach |
|---|---|
| **Small organisation, low-cost tool, low-risk use** | A simple before-and-after on two or three measures (such as time on a sample of tasks and a quality spot-check), plus a short staff survey. A spreadsheet is enough. |
| **Team pilot in a medium or large organisation** | Baseline from operational data; comparison group; six-dimension scorecard with two or three metrics each; blind quality sampling. |
| **Enterprise-wide rollout or major investment** | Staggered or randomised rollout designed for evaluation; independent evaluation; financial tracking against the business case; regular reporting to the governance board. |
| **High-risk use affecting individuals** | All of the above, plus fairness testing across groups and monitoring of complaints and outcomes. See [AI risk assessment](../../assessments/ai-risk-assessment.md). |

## Building a scorecard

A simple scorecard for one use case might look like this. Use one row per metric, and keep it to around 10 to 15 metrics in total.

| Dimension | Metric | Baseline | Target | Result | Data source | Owner |
|---|---|---|---|---|---|---|
| Adoption | Weekly active users in pilot group | n/a | 70% | | Admin dashboard | Pilot lead |
| Efficiency | Median time to first draft | | −20% | | Timed sample | Team manager |
| Quality | Blind expert rating (1–5) | | No decrease | | Rubric review | Quality lead |
| Risk | Incidents involving prohibited data | 0 | 0 | | DLP logs | Information security |
| Experience | Staff reporting tool is useful | n/a | 60% | | Pulse survey | Pilot lead |
| Financial | Cost per completed draft | | Lower than baseline | | Finance + operational data | Finance partner |

## Worked example

**Context.** A 300-person professional services firm wants to know whether a generative AI assistant helps its bid team write tender responses. It has budget for 40 licences for a 10-week pilot. Its bid team of 24 people produces around 30 tenders a quarter.

**Decision to inform.** Whether to buy licences for the full bid team and the wider business development function (about 80 people).

**Hypothesis.** The assistant will reduce time to produce a first full draft of a tender response by at least 20%, with no reduction in internal quality review scores, and no data protection incidents.

**Baseline.** The firm's bid management system already records the date each tender is assigned and the date the first draft is submitted for review, and reviewers score drafts on a 1 to 5 rubric. The team pulls the previous two quarters of data: median time to first draft and median review score.

**Counterfactual.** The 24 bid writers are split into two groups of 12 using a random draw, stratified so that each group has a similar mix of senior and junior writers. Group A gets access in weeks 1 to 10. Group B continues as normal, and receives access afterwards. Both groups' tenders are scored by reviewers who are not told which group produced them. The remaining licences go to business development staff, measured on adoption and experience only.

**Controls.** An approved-use briefing, a short [acceptable use policy](../../toolkits/acceptable-use-policy.md), business-tier licences with training on customer data switched off, and a rule that client-confidential pricing is never entered.

**Results (illustrative).** The figures below are invented to show how to interpret results; they are not research findings.

| Dimension | Group A (AI) | Group B (no AI) | Interpretation |
|---|---|---|---|
| Adoption | 11 of 12 used weekly | n/a | Strong adoption |
| Median time to first draft | Fell from 9 to 7 working days | Fell from 9 to 8.5 working days | Group B also improved slightly (a new template was introduced mid-pilot). The difference-in-differences estimate is about 1.5 days, or roughly 17% |
| Median review score | 3.6 (baseline 3.7) | 3.7 (baseline 3.7) | Small drop; reviewers noted generic language and two unsupported claims about the firm's credentials |
| Risk | 0 incidents; 1 near miss | 0 | Near miss led to a clarified rule |
| Experience | 10 of 12 found it useful | n/a | Positive, but satisfaction alone would have overstated the effect |
| Financial | Licence cost per writer per quarter compared with value of 1.5 days saved per tender | n/a | Positive if the saved time is used to bid for more tenders or improve win rates |

**Interpretation.** A simple before-and-after for Group A would have suggested a 22% improvement. The comparison group shows that part of that improvement came from the new template, which also helped Group B. The credible estimate is about 17%, just below the 20% target, with a small quality cost.

**Decision.** The firm decides to extend licences to the bid team, with two conditions: a prompt library and a review checklist to address generic language and unsupported claims (see [prompt library template](../../toolkits/prompt-library-template.md)), and a second measurement round after one quarter. It defers the wider business development rollout, because adoption there was patchy and no outcome had been measured. The firm also agrees how the saved time will be used: to bid for more opportunities, tracked through the number of tenders submitted per writer.

## Reporting results

- **Report ranges and uncertainty**, not single precise numbers, especially for small pilots.
- **Report what did not work** as well as what did; it is often the most useful finding.
- **Separate measured from self-reported results** in every report.
- **Show the counterfactual** and explain how you estimated it.
- **Revisit after scaling.** Results from enthusiastic pilot users rarely transfer exactly to the wider population. Build ongoing measurement into [operate](../lifecycle/06-operate.md).

## Related pages

- [Evidence on impact](../foundations/evidence-on-impact.md)
- [Pilot](../lifecycle/04-pilot.md) and [Scale](../lifecycle/05-scale.md)
- [Business case template](../../toolkits/business-case-template.md)
- [Use case prioritisation](../../assessments/use-case-prioritisation.md)

## Sources

1. METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*, July 2025. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
2. Government Digital Service, *M365 Copilot Experiment Findings Report* (cross-government), 2025. https://assets.publishing.service.gov.uk/media/683db42bd23a62e5d32680d0/M365_Copilot_Experiment_Findings_Report.pdf
3. Department for Business and Trade, *Evaluation of the M365 Copilot Pilot in the Department for Business and Trade*, August 2025. https://assets.publishing.service.gov.uk/media/68adbe409e1cebdd2c96a19d/dbt-microsoft-365-copilot-evaluation.pdf
4. Humlum, A. and Vestergaard, E., *Large Language Models, Small Labor Market Effects*, Becker Friedman Institute Working Paper 2025-56, 2025. https://bfi.uchicago.edu/wp-content/uploads/2025/04/BFI_WP_2025-56-3.pdf
5. HM Treasury, *The Magenta Book: Central Government guidance on evaluation* (updated May 2026). https://www.gov.uk/government/publications/the-magenta-book

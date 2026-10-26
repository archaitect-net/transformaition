# Stage 4: Pilot

> **Who this is for:** Pilot leads, business owners, IT, champions, pilot participants and sponsors who will make the go/no-go decision.
> **Last reviewed:** 2026-10

A pilot tests whether an AI tool works for your organisation, for a specific use case, under realistic conditions and with controls in place. Its purpose is to generate evidence for a decision, not to prove that a decision already made was right. This page covers pilot design, success criteria, controls, cohort selection, evaluation and the go/no-go decision. It applies to a five-person trial in a small business as much as to a multi-team enterprise pilot; the difference is scale and formality, not principle.

## Purpose

- Test whether the tool solves the problem defined in [Discover](01-discover.md), in your context.
- Measure value against criteria agreed before the pilot starts.
- Test that controls (data, security, human review) work in practice.
- Learn what training, support and process change a wider rollout would need.
- Produce a clear go, iterate or stop decision.

## Inputs

- Selected tool and use case, with contract or trial terms, from [Select](03-select.md).
- Conditions from [Assess](02-assess.md), updated DPIA and risk assessment.
- Business case with expected benefits and measurement approach.

## Activities

1. **Write the pilot plan.** Use the [pilot plan template](../../toolkits/pilot-plan-template.md). Define scope (tasks in and out), duration, cohort, controls, measures, roles and decision criteria.
2. **Set success criteria in advance.** Agree with the sponsor what result would justify scaling, what would justify iterating, and what would mean stopping. Write them down before the pilot starts.
3. **Establish a baseline.** Measure the current state of the tasks in scope (time, quality, error rates, satisfaction) before participants use the tool. Without a baseline, you will have opinions rather than evidence. See [measuring value](../measurement/measuring-value.md).
4. **Select the cohort.** See the cohort guidance below.
5. **Configure controls.** Apply the technical and procedural controls the risk assessment requires: access limited to the cohort; data sources and connectors restricted; logging on; acceptable use rules issued; human review steps defined for outputs that leave the team or affect decisions.
6. **Prepare and train participants.** Cover what the tool is for, what it is not for, how to verify outputs, what data must not be used, and how to report problems. A short, task-specific session tends to be more useful than a generic product demo.
7. **Run the pilot.** Provide a support channel, hold regular check-ins, and collect data continuously: usage, task measures, issues, and qualitative feedback.
8. **Monitor risk during the pilot.** Track incidents, near misses, data handling concerns and output quality problems. Agree in advance what would trigger a pause.
9. **Evaluate.** Compare results to the baseline and success criteria. Combine quantitative measures with structured qualitative feedback. Look at variation between participants, not only averages.
10. **Decide.** Present findings to the decision-maker with a recommendation: go (with conditions), iterate (what changes, and how long), or stop. Record the decision and reasons.

### Success criteria: examples

Good criteria are specific, measurable, tied to the problem and agreed in advance.

| Weak criterion | Stronger criterion |
|---|---|
| "Users like it" | "At least X% of participants use it for in-scope tasks at least weekly by week 6, and median satisfaction is at least Y on a 5-point scale" |
| "Saves time" | "Median time to produce a first-draft client summary falls from the baseline by at least Z%, with no increase in reviewer-identified errors" |
| "No problems" | "No data protection incidents; all reported output errors resolved through the defined review step before leaving the team" |

You set X, Y and Z for your context; the guide does not supply benchmark targets because outcomes vary widely by task. See [evidence on impact](../foundations/evidence-on-impact.md) for what research does and does not show.

### Choosing the pilot cohort

| Consideration | Guidance |
|---|---|
| Size | Large enough to see patterns across different users; small enough to support closely. Even a handful of users can give useful signal in a small organisation. |
| Mix | Include sceptics and novices, not only enthusiasts. A cohort of early adopters will overstate likely adoption. |
| Representativeness | Cover the roles and tasks that a rollout would include. |
| Comparison | Where feasible, compare with a similar group not using the tool, or with the same group's baseline. Randomised comparison is stronger evidence but not always practical. |
| Consent and communication | Explain what data will be collected about participants' use of the tool and how it will (and will not) be used. Avoid using pilot data to assess individual performance unless that has been lawfully established and communicated. |
| Representation | Involve workers' representatives where your organisation has them. |

## Controls checklist for pilots

- [ ] Access restricted to named participants.
- [ ] Only approved data sources and connectors enabled.
- [ ] Data classifications that may and may not be used are communicated.
- [ ] Audit logging enabled and retention set in line with your policy.
- [ ] Human review defined for outputs used externally or in decisions.
- [ ] Incident reporting route communicated.
- [ ] Pause triggers agreed.
- [ ] Transparency obligations met (for example, telling people when they interact with an AI system where the law requires it; see [regulation overview](../governance/regulation-overview.md)).

## Roles involved

| Role | Contribution |
|---|---|
| Pilot lead | Runs the plan, collects data, reports |
| Business owner | Owns success criteria and the recommendation |
| Executive sponsor | Makes the go/no-go decision |
| Participants and champions | Use the tool, give feedback, report issues |
| IT and platform | Configuration, access, support |
| Security and data protection | Confirm controls; monitor incidents |
| Learning and development | Pilot training |
| Data or analytics | Measurement design and analysis |

## Outputs and deliverables

- Pilot plan with pre-agreed success criteria.
- Baseline and results data.
- Evaluation report: findings against criteria, qualitative insights, issues and incidents, cost observed.
- Updated risk assessment and DPIA reflecting what was learned.
- Recommendations for rollout: training, support, configuration, process changes.
- Recorded go, iterate or stop decision.

## Decision gate: go, iterate or stop

Go to [Scale](05-scale.md) only if:

- [ ] Results meet the pre-agreed success criteria, or the decision-maker has explicitly accepted a variance with reasons.
- [ ] No unresolved serious incidents.
- [ ] Controls worked as intended, or needed changes are identified.
- [ ] The risk assessment and DPIA are updated, and residual risk is accepted.
- [ ] Rollout requirements (training, support, licences, configuration) are known and funded.
- [ ] Participant feedback has been analysed, including from sceptical users.

Iterate if the tool shows promise but specific, fixable issues remain. Set a time limit and criteria for the next round. Stop if criteria are clearly not met or risks cannot be controlled, and record lessons in the use case register.

## Linked assessments and toolkits

- [Pilot plan template](../../toolkits/pilot-plan-template.md)
- [Training plan template](../../toolkits/training-plan-template.md)
- [Communication plan template](../../toolkits/communication-plan-template.md)
- [Prompt library template](../../toolkits/prompt-library-template.md): capture prompts that work during the pilot.
- [AI risk assessment](../../assessments/ai-risk-assessment.md)
- [Measuring value](../measurement/measuring-value.md)

## Variations by organisation size

**Small organisations.** A pilot might be three to five people using a tool for four weeks on two or three defined tasks, with a simple before-and-after time log and a short feedback form. The owner makes the decision. Keep a note of what worked and what did not.

**Enterprises.** Consider multiple cohorts across functions, a comparison group, and formal analysis. Align pilot data collection with employee monitoring rules and consult works councils where required. Plan licence transitions so a "go" does not leave participants without access while procurement scales up.

## Common pitfalls

- **Moving the goalposts.** Changing success criteria after results arrive undermines the decision.
- **Enthusiast-only cohorts.** These overstate adoption and value.
- **No baseline.** Without one, time-saving claims cannot be checked.
- **Pilots that never end.** Set an end date and a decision meeting in advance.
- **Measuring use, not value.** High usage does not mean the problem is solved.
- **Ignoring hidden costs.** Time spent verifying outputs is part of the cost; measure it.
- **Treating "stop" as failure.** A well-run pilot that stops a poor investment has done its job.

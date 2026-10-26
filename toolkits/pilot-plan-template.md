# Pilot plan template

> **Who this is for:** Pilot leads, product owners, managers and IT teams planning a time-boxed trial of an AI tool or use case. Works for a two-person trial in a small business or a multi-team enterprise pilot.
> **Last reviewed:** 2026-10

This template helps you plan a pilot that produces a clear decision, not just enthusiasm. It covers objectives and hypotheses, scope and participants, baselines and success measures, a comparison approach, controls and risk conditions, support and training, timeline, data collection, stop criteria, and the decision at the end (scale, extend, change or stop). Guidance notes in blockquotes explain each section; replace [bracketed placeholders]. Use it at the [Pilot](../docs/lifecycle/04-pilot.md) stage, after the use case has been prioritised and its data and risks assessed.

> **Guidance: what makes a pilot useful**
>
> - **Decide in advance what success looks like.** Write down the measures and thresholds before the pilot starts. Deciding afterwards invites confirmation bias.
> - **Measure, don't just ask.** Self-reported time savings can be unreliable. In one randomised trial, experienced developers estimated AI had made them about 20% faster when measured completion times were 19% slower (Limited evidence; small sample) [1]. Combine objective measures (time, volume, error rates, quality audits) with surveys.
> - **Compare.** Where possible, compare with a baseline period or a comparison group doing the same work without the tool.
> - **Include sceptics and typical users,** not only enthusiasts, or results will not generalise.
> - **Plan the end.** A pilot without a decision date tends to drift into unmanaged production use.

---

## [Use case name] Pilot plan

| | |
|---|---|
| **Pilot lead** | [name, role] |
| **Sponsor** | [name, role] |
| **Use case register ID** | [ ] |
| **Tool and version** | [ ] |
| **Dates** | [start] to [end] ([n] weeks) |
| **Decision meeting** | [date] |
| **Status** | [Draft / Approved / In progress / Closed] |

## 1. Background

[One paragraph: the problem, why AI might help, and how this use case was prioritised. Link to [use case prioritisation](../assessments/use-case-prioritisation.md) scores.]

## 2. Objectives and hypotheses

> **Guidance:** Express objectives as testable hypotheses. Include at least one hypothesis about risk or quality, not only speed.

| # | Hypothesis | Measure | Success threshold | Data source |
|---|---|---|---|---|
| H1 | [Using the tool reduces time to draft X by at least Y%] | [Minutes per task] | [≥ Y% reduction vs baseline] | [Time log / system data] |
| H2 | [Quality of X is maintained or improved] | [Quality audit score using rubric] | [No decrease vs baseline] | [Weekly sample audit] |
| H3 | [Staff find the tool usable for this task] | [Survey score] | [≥ [n] on [scale]] | [End-of-pilot survey] |
| H4 | [No serious incidents] | [Incident count by severity] | [0 serious incidents] | [Incident log] |

## 3. Scope

| | In scope | Out of scope |
|---|---|---|
| Tasks | [ ] | [ ] |
| Data | [classification levels and sources permitted] | [e.g. Restricted data; HR records] |
| Users | [teams, roles] | [ ] |
| Features | [ ] | [e.g. autonomous sending; plug-ins] |
| Outputs | [internal drafts reviewed before use] | [e.g. outputs sent without review] |

## 4. Participants

| Group | Number | Selection | Role |
|---|---|---|---|
| Pilot users | [ ] | [e.g. mix of experience levels; volunteers and nominated] | Use tool; log data; give feedback |
| Comparison group (if used) | [ ] | [ ] | Continue current process; log same measures |
| Champions | [ ] | [ ] | Peer support; collect issues |
| Reviewers / auditors | [ ] | [ ] | Quality sampling |

> **Guidance:** Small organisations may not have enough people for a comparison group. Use a before-and-after comparison with the same people, and be cautious about attributing all changes to the tool.

## 5. Baseline and comparison approach

- **Baseline period:** [dates; measures collected]
- **Comparison design:** [before-and-after / comparison group / alternating tasks with and without the tool]
- **Known confounders:** [e.g. seasonal workload, new staff, other process changes] and how you will account for them

## 6. Pre-pilot readiness checklist

- [ ] Use case recorded in [register](use-case-register-template.md)
- [ ] [Data readiness](../assessments/data-readiness.md) completed; blockers resolved
- [ ] [AI risk assessment](../assessments/ai-risk-assessment.md) completed to required depth; conditions recorded
- [ ] DPIA completed or screening decision recorded (if personal data)
- [ ] [Vendor due diligence](../assessments/vendor-due-diligence.md) completed; contract or trial terms reviewed
- [ ] Tool configured: access, data settings, logging, permissions
- [ ] Participants briefed and trained; [acceptable use policy](acceptable-use-policy.md) acknowledged
- [ ] Baseline data collected
- [ ] Data collection methods tested
- [ ] Support route and incident reporting route communicated
- [ ] Affected people informed where required (e.g. customers, staff whose meetings are summarised)

## 7. Controls during the pilot

| Control | Description | Owner |
|---|---|---|
| Human review | [who checks what before use] | |
| Quality sampling | [e.g. 10% of outputs audited weekly against rubric] | |
| Usage limits | [ ] | |
| Monitoring | [what is logged and reviewed, how often] | |
| Incident handling | [route; severity definitions; who can pause the pilot] | |

## 8. Training and support

- **Training:** [content, duration, format; link to [training plan](training-plan-template.md)]
- **Starter prompts or guidance:** [link to [prompt library](prompt-library-template.md) entries]
- **Support:** [channel, hours, champions]
- **Check-ins:** [e.g. weekly 30-minute session to share tips and issues]

## 9. Data collection plan

| Measure | Method | Frequency | Who collects | Storage |
|---|---|---|---|---|
| Time per task | [ ] | [ ] | [ ] | [ ] |
| Quality | [rubric-based sample audit] | [ ] | [ ] | [ ] |
| Usage | [tool analytics] | [ ] | [ ] | [ ] |
| User experience | [survey; short interviews] | [mid and end] | [ ] | [ ] |
| Issues and incidents | [log] | [continuous] | [ ] | [ ] |
| Costs | [licences, staff time] | [ ] | [ ] | [ ] |

> **Guidance:** Keep logging burden light; heavy logging can distort results. Use system data where available. Tell participants how their data will be used, and avoid using pilot data to assess individual performance unless that has been agreed.

## 10. Timeline

| Week | Activity |
|---|---|
| -[4] to -1 | Readiness checks; baseline; configuration; training |
| 1 | Launch; daily check-in for first week |
| 2–[n-1] | Use; weekly check-ins; weekly quality sampling |
| [mid] | Mid-point review against stop criteria |
| [n] | Final data collection; survey |
| [n+1] | Analysis; recommendation; decision meeting |

## 11. Stop and pause criteria

The pilot lead or [role] will **pause** the pilot if:

- a serious incident occurs (e.g. Confidential data exposed, harmful output relied on externally);
- the vendor changes material terms or the model behaves very differently;
- [other].

The pilot will **stop early** if, at the mid-point review:

- [e.g. quality has fallen below baseline and cannot be corrected];
- [e.g. adoption is below [n]% after support interventions].

## 12. Evaluation and decision

> **Guidance:** Set out how results will be analysed and the decision options. Report results against every hypothesis, including those not met.

| Decision | Criteria |
|---|---|
| **Scale** | All success thresholds met; risks within appetite; business case positive using pilot data |
| **Extend or change** | Mixed results with a credible, specific reason to expect improvement (e.g. better data, revised workflow) |
| **Stop** | Thresholds not met, or risks not controllable, or business case negative under realistic assumptions |

**Outputs of the evaluation:**

- [ ] Results against each hypothesis, with data
- [ ] Updated [use case scores](../assessments/use-case-prioritisation.md) and [risk assessment](../assessments/ai-risk-assessment.md)
- [ ] Updated [business case](business-case-template.md) with measured values
- [ ] Lessons learned (what worked, what did not, surprises)
- [ ] Recommendation and decision recorded in the register
- [ ] If stopping: access removed, data handled per retention rules, participants informed

## 13. Communication

| Audience | Message | When | Channel | Owner |
|---|---|---|---|---|
| Participants | Purpose, expectations, support | Before launch | [ ] | [ ] |
| Wider team | Pilot is happening; what it means for them | Launch | [ ] | [ ] |
| Leadership | Progress and results | Mid-point and end | [ ] | [ ] |
| Everyone | Outcome and next steps | After decision | [ ] | [ ] |

See [communication plan template](communication-plan-template.md).

## 14. Approval

| Role | Name | Date |
|---|---|---|
| Sponsor | | |
| Pilot lead | | |
| Risk / data protection (if required) | | |

## Sources

1. METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*, July 2025. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/

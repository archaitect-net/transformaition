# Organisational readiness assessment

> **Who this is for:** Leadership teams, AI programme leads, transformation and IT leads, and anyone asked "are we ready to adopt AI tools?". Usable by a small business owner in an hour or by a cross-functional enterprise group over a workshop.
> **Last reviewed:** 2026-10

This assessment scores how ready your organisation is to adopt AI tools safely and usefully, across seven dimensions: strategy and leadership, use cases and value, data, technology and security, people and skills, governance and risk, and culture and change. It has 41 questions, each scored 0–4 against explicit descriptors. You get a weighted overall score, a score per dimension, and a set of "gating" checks that stop a high average from hiding a critical gap. Use it at the [Assess](../docs/lifecycle/02-assess.md) stage, and repeat it before you [Scale](../docs/lifecycle/05-scale.md). It is a practical self-assessment heuristic, not a validated or certified instrument, so treat the score as a structured conversation starter rather than a measurement.

## Before you start

**Who should complete it.** Results are more reliable when several perspectives contribute. As a minimum, involve someone accountable for the business (owner, director or sponsor), someone who runs your technology (internal IT or your managed service provider), and someone who handles data protection or risk. In larger organisations add HR or learning and development, a representative of frontline staff, and security.

**How to run it.**

1. Each participant scores every question independently (15–30 minutes).
2. Meet to compare. Discuss any question where scores differ by two or more points; that gap is itself a finding.
3. Agree a consensus score and, for each score of 3 or 4, note the evidence (a document, a system setting, a meeting minute). If you cannot point to evidence, score lower.
4. Calculate scores using the method below and record agreed actions.

**Scoring principles.**

- Score what is true today, not what is planned.
- A level is only reached if the whole descriptor is true. If you are between levels, choose the lower one.
- Mark a question **N/A** only if it genuinely does not apply (for example, some data questions if you will only use AI tools with no access to organisational data). N/A questions are excluded from the average; do not use N/A for "don't know". "Don't know" scores 0, because not knowing is a gap.
- **Small organisations (under 50 people):** "documented" can mean a short written note or an email agreed by the owner; "committee" can mean the owner plus one adviser. The level descriptors are about whether the thing exists and works, not about formality.

## The scale

Every question uses the same underlying scale. Question-specific descriptors are in the tables below.

| Score | General meaning |
|---|---|
| 0 | Absent. Nothing exists, or nobody knows. |
| 1 | Ad hoc. Some individual activity, informal and inconsistent. |
| 2 | Defined. Agreed and written down, but applied partially or recently introduced. |
| 3 | Embedded. Consistently applied across the relevant scope, with named owners and evidence. |
| 4 | Optimised. Measured, reviewed on a cycle, and improved as a result. |

## Dimension 1: Strategy and leadership (weight 15%)

| # | Question | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| S1 | Is there a stated purpose for using AI tools, linked to organisational objectives? | No stated purpose | Individuals have ideas; nothing agreed | Written purpose agreed by leadership | Purpose linked to specific objectives and used in decisions | Purpose reviewed at least annually against results |
| S2 | Is there a named senior sponsor accountable for AI adoption? | No one | Interested senior person, not formally accountable | Sponsor named, role described | Sponsor actively unblocks, chairs reviews, owns outcomes | Sponsor accountability reflected in objectives and reported to the board or owners |
| S3 | Is there funding for AI adoption beyond licences? | None | Licences only, ad hoc | Budget covers licences plus some enablement | Budget covers licences, enablement, change, run costs and contingency | Budget is reviewed against measured value and adjusted |
| S4 | Has leadership agreed a risk appetite for AI use? | Never discussed | Discussed informally | Written statement of what is and is not acceptable | Appetite used to decide on specific use cases | Appetite reviewed when incidents, regulation or capability change |
| S5 | Is there a roadmap with stages and decision points? | None | Informal list of ideas | Roadmap with stages | Roadmap with go/no-go criteria at each stage, owned and tracked | Roadmap updated from measured results and lessons learned |
| S6 | Do leaders understand what current AI tools can and cannot do? | No understanding | A few leaders have personal experience | Leadership has had a briefing | Leaders use tools themselves and can describe key limitations | Leaders refresh understanding on a cycle and challenge claims with evidence |

## Dimension 2: Use cases and value (weight 15%)

| # | Question | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| U1 | Have candidate use cases been identified from real work problems? | None | Ideas from enthusiasts or vendors only | List gathered from several teams | List based on observed work, with problem statements | List refreshed regularly from staff input and results |
| U2 | Are use cases prioritised on value, feasibility and risk? | No | By loudest voice or vendor pitch | Simple scoring done once | Consistent scoring method used (see [use case prioritisation](use-case-prioritisation.md)) | Scores revisited after pilots; method refined |
| U3 | Do use cases have baseline measures (time, quality, cost, satisfaction)? | No | Anecdotes only | Baselines for some use cases | Baselines for all prioritised use cases before pilot | Baselines and outcomes tracked over time |
| U4 | Is there a register of use cases, including ones already in use informally? | No | Partial awareness | Register exists, partly complete | Register complete and owned (see [register template](../toolkits/use-case-register-template.md)) | Register drives review, retirement and reuse |
| U5 | Are benefits estimated conservatively, with assumptions stated? | No estimates | Optimistic or vendor-supplied figures | Own estimates, assumptions partly stated | Conservative estimates with stated assumptions and sensitivity range | Estimates compared with actuals and calibrated |
| U6 | Is there a process for stopping use cases that do not deliver? | No | Things fade out | Stop criteria defined for pilots | Stop criteria applied in practice | Stopped use cases reviewed for lessons |

## Dimension 3: Data (weight 15%)

| # | Question | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| D1 | Do you have a data classification scheme that staff understand? | None | Exists on paper, not used | Defined and communicated | Applied to key repositories and understood by most staff | Audited and kept current |
| D2 | Do you know where your important information lives (systems, shared drives, mailboxes)? | No | Partial, in people's heads | Documented for main systems | Inventory with owners for important data | Inventory maintained and linked to access reviews |
| D3 | Are access permissions on documents and data appropriate (least privilege)? | Unknown or widely open | Known oversharing, not addressed | Main issues identified, remediation started | Permissions reviewed for repositories AI tools can reach | Regular automated or scheduled access reviews |
| D4 | Is data quality adequate for the intended use cases? | Unknown | Known problems, unmanaged | Quality issues documented for key sources | Quality owners and fixes in place for priority sources | Quality measured and monitored |
| D5 | Are retention and deletion rules defined and applied? | No | Informal | Policy exists | Applied to main repositories | Monitored and enforced, including for AI-generated content |
| D6 | Do you know which data is personal, special category or confidential? | No | Partial awareness | Identified for main systems | Identified and recorded in the inventory | Kept current with change processes |

Personal data and special category data are defined in UK and EU data protection law; see [data protection](../docs/governance/data-protection.md). For a use-case-level check, use the [data readiness assessment](data-readiness.md).

## Dimension 4: Technology and security (weight 15%)

| # | Question | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| T1 | Do you have identity and access management that AI tools can use (single sign-on, multi-factor authentication)? | No | Partial, inconsistent | Single sign-on and MFA for main systems | Single sign-on and MFA standard; AI tools integrated | Access monitored, with conditional access policies |
| T2 | Can you control which AI tools staff use and what data they can send to them? | No control | Guidance only | Approved list, limited technical controls | Approved tools enforced; data controls configured (e.g. data loss prevention, admin settings) | Controls monitored and tested |
| T3 | Do you know which AI tools are already in use (including personal accounts and AI features inside existing software)? | No | Anecdotal | One-off survey or discovery | Ongoing discovery and register | Discovery feeds review and approval decisions |
| T4 | Is there a security review process that covers AI-specific threats (e.g. prompt injection, data leakage)? | No security review | Generic review only | Review includes some AI-specific questions | AI threats assessed against a recognised list such as the OWASP Top 10 for LLM Applications | Reviews updated as threats evolve; testing performed |
| T5 | Can you log and audit AI tool usage where needed? | No | Vendor default only, not reviewed | Logging enabled for main tools | Logs retained, reviewed for defined purposes | Logs feed monitoring, incident response and value measurement |
| T6 | Is there capacity (internal or supplier) to configure, integrate and support AI tools? | None | One enthusiast | Named people or supplier with some time | Defined support model and service owner | Support capacity planned against demand |

## Dimension 5: People and skills (weight 15%)

| # | Question | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| P1 | Do staff have basic AI literacy (what tools do, limitations, safe use)? | No | Self-taught individuals | Introductory material available | Role-appropriate training completed by most users, and recorded | Training refreshed and effectiveness checked |
| P2 | Is training tailored to roles (users, managers, technical staff, risk staff)? | No | One-size-fits-all | Some role variants | Role-based curricula (see [training plan](../toolkits/training-plan-template.md)) | Curricula updated from usage data and feedback |
| P3 | Are there champions or a community of practice? | No | Informal enthusiasts | Named champions | Active network sharing practice and prompts | Network contributes to policy, prompt library and training |
| P4 | Have managers been equipped to lead AI use in their teams? | No | Left to individuals | Briefing provided | Managers set expectations, review use and quality | Manager practice reviewed and supported |
| P5 | Have you considered impacts on roles, workload and jobs? | No | Informal discussion | Impacts identified for pilot roles | Impacts assessed with HR, staff and (where present) unions or employee representatives | Ongoing review; job design and skills plans updated |
| P6 | Do technical teams have the skills to evaluate and integrate AI tools? | No | Limited | Some skills; gaps known | Skills sufficient for current plans or covered by suppliers | Skills planned ahead of roadmap |

If you operate in or serve the EU, the EU AI Act places an AI literacy obligation on providers and deployers of AI systems (Article 4); see the [training plan template](../toolkits/training-plan-template.md) for the current position.

## Dimension 6: Governance and risk (weight 15%)

| # | Question | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| G1 | Is there an acceptable use policy for staff use of AI tools? | No | Informal guidance | Written policy issued (see [template](../toolkits/acceptable-use-policy.md)) | Policy acknowledged by staff and supported by training | Policy reviewed on a cycle and after incidents |
| G2 | Are roles and decision rights for AI defined (who approves tools and use cases)? | No | Unclear or contested | Roles written down | Roles applied consistently (see [RACI template](../toolkits/raci-template.md)) | Decision-making reviewed for speed and quality |
| G3 | Is there a risk assessment process for AI use cases? | No | Ad hoc | Template exists | Applied to all non-trivial use cases before deployment (see [AI risk assessment](ai-risk-assessment.md)) | Risks monitored after deployment and assessments updated |
| G4 | Do you know which laws and regulations apply to your AI use? | No | Vague awareness | Main obligations identified | Obligations mapped to use cases, with owners | Horizon scanning in place; mapping kept current |
| G5 | Are data protection requirements (e.g. DPIAs where required) built into the process? | No | Considered occasionally | Screening question exists | DPIA screening applied to every use case involving personal data | DPIAs reviewed when systems or uses change |
| G6 | Is there a vendor due diligence process covering AI-specific terms? | No | Standard procurement only | Some AI questions asked | Consistent questionnaire used (see [vendor due diligence](vendor-due-diligence.md)) | Vendor commitments monitored over the contract |

## Dimension 7: Culture and change (weight 10%)

| # | Question | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| C1 | Do staff feel able to raise concerns about AI use? | Concerns discouraged or unknown | Some raise concerns informally | Channel exists | Concerns raised and visibly acted on | Concern trends reviewed and shared |
| C2 | Is there a communication plan for AI adoption? | No | Occasional announcements | Plan written | Plan delivered, two-way, with feedback (see [template](../toolkits/communication-plan-template.md)) | Messaging adjusted based on feedback and sentiment |
| C3 | Is experimentation encouraged within safe boundaries? | Discouraged, or unbounded | Tolerated informally | Sandbox or approved tools for trying ideas | Time and support for structured experiments | Experiments feed the use case pipeline |
| C4 | Are mistakes and near misses with AI reported and learned from? | No | Rarely | Reporting route exists | Incidents and near misses reviewed without blame | Lessons drive policy, training and controls |
| C5 | Is there trust between leadership and staff about AI's purpose (for example, about jobs)? | Low trust or fear widespread | Mixed, unaddressed | Leadership has stated intentions | Intentions backed by actions and consultation | Trust measured (e.g. survey) and acted on |

## Scoring

### Step 1: Dimension scores

For each dimension, add the scores and divide by the number of answered (non-N/A) questions. This gives a dimension average between 0 and 4. Convert to a percentage: `dimension % = average ÷ 4 × 100`.

### Step 2: Overall score

Multiply each dimension percentage by its weight and add the results.

| Dimension | Weight |
|---|---|
| Strategy and leadership | 0.15 |
| Use cases and value | 0.15 |
| Data | 0.15 |
| Technology and security | 0.15 |
| People and skills | 0.15 |
| Governance and risk | 0.15 |
| Culture and change | 0.10 |

**Adjusting weights.** The default weights are a judgement, not a research finding. You may adjust them to reflect your context (for example, a regulated organisation may raise governance and risk to 0.25), but agree changes before scoring and record them, so results remain comparable over time.

### Step 3: Gating checks

A high average can hide a critical gap. Regardless of overall score, apply these gates:

| Gate | Condition | Consequence |
|---|---|---|
| Policy gate | G1 scores 0 or 1 | Do not roll out beyond a small, supervised pilot until an acceptable use policy is issued |
| Data control gate | T2 or D3 scores 0 | Do not connect AI tools to organisational data; restrict to tools and data that are low risk |
| Accountability gate | S2 or G2 scores 0 | Name an accountable sponsor and decision owner before any approval decision |
| Legal gate | G4 or G5 scores 0 and you process personal data | Take data protection and legal advice before piloting |
| Visibility gate | T3 scores 0 | Run a discovery exercise; unmanaged use is likely already happening |

### Worked example (fictional)

A fictional 120-person charity scores: Strategy 2.0, Use cases 1.5, Data 1.2, Technology 2.3, People 1.7, Governance 1.0, Culture 2.4 (averages out of 4).

Percentages: 50, 37.5, 30, 57.5, 42.5, 25, 60. Weighted: (50 + 37.5 + 30 + 57.5 + 42.5 + 25) × 0.15 + 60 × 0.10 = 36.4 + 6 = **42.4%**, placing it in the Emerging band. G1 scored 1, so the policy gate applies: the priority is an acceptable use policy and training before any wider rollout.

## Interpreting results

| Band | Overall score | What it usually means | What to do next |
|---|---|---|---|
| Foundational | 0–24% | AI use, if any, is unmanaged. Key foundations (policy, ownership, data controls) are missing. | Issue an interim acceptable use policy. Run a discovery exercise to find existing use. Name a sponsor. Brief leadership on [capabilities and limitations](../docs/foundations/capabilities-and-limitations.md). Avoid committing to large licence purchases. |
| Emerging | 25–49% | Interest and some activity, but foundations are partial. | Fix gated items first. Build a use case register and prioritise. Prepare one or two small, low-risk pilots using the [pilot plan template](../toolkits/pilot-plan-template.md). Start role-based AI literacy training. |
| Developing | 50–74% | Foundations largely in place; ready for structured pilots and limited rollout. | Run pilots with baselines and stop criteria. Complete risk and data assessments per use case. Plan for scale: support model, communications, measurement. Address the lowest-scoring dimension. |
| Ready to scale | 75–100% | Mature foundations, evidence from pilots, functioning governance. | Scale proven use cases in waves. Shift effort to [operating](../docs/lifecycle/06-operate.md): monitoring, value measurement, periodic review, retirement. Reassess annually. |

**Read the profile, not just the total.** The spread across dimensions usually tells you more than the overall number. A common pattern is strong technology with weak people and governance scores; that typically signals tools deployed ahead of the conditions needed to use them well. Plot the seven dimension percentages on a radar or bar chart and discuss the two lowest.

**Comparing over time.** Re-run the assessment at the same points in the lifecycle (for example after Assess and before Scale) with the same weights. Expect individual scores to fall sometimes as people understand the questions better; that is a sign of a more honest baseline, not failure.

## Limitations

- This is a self-assessment. Scores are only as honest as the evidence behind them. Consider asking someone outside the team (internal audit, a peer organisation, an adviser) to challenge your 3s and 4s.
- The questions and weights reflect practitioner consensus drawn from published frameworks such as the NIST AI Risk Management Framework [1] and ISO/IEC 42001 [2]; they have not been empirically validated as predictors of adoption success.
- It assesses organisational readiness in general. Each individual use case still needs its own [data readiness](data-readiness.md) and [risk](ai-risk-assessment.md) assessment.

## Related

- [Maturity model](maturity-model.md): describes the same dimensions as five levels to help you picture the next stage.
- [Assess stage](../docs/lifecycle/02-assess.md) and [governance model](../docs/governance/governance-model.md).
- [Leadership pathway](../docs/pathways/leadership.md).

## Sources

1. National Institute of Standards and Technology (NIST), *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, January 2023. https://doi.org/10.6028/NIST.AI.100-1
2. ISO/IEC, *ISO/IEC 42001:2023 Information technology — Artificial intelligence — Management system*, December 2023. https://www.iso.org/standard/42001
3. OWASP GenAI Security Project, *OWASP Top 10 for LLM Applications 2025*. https://genai.owasp.org/llm-top-10/

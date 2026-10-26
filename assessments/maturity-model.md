# AI adoption maturity model

> **Who this is for:** Leaders, programme leads and strategy teams who want a shared picture of where the organisation is with AI tools and what "the next level" looks like. Works for small organisations and enterprises.
> **Last reviewed:** 2026-10

This page describes five maturity levels (Exploring, Experimenting, Formalising, Scaling, Optimising) across the same seven dimensions used in the [organisational readiness assessment](organisational-readiness.md). A level-descriptor matrix lets you locate yourself per dimension, a short method converts readiness scores into levels, and a progression section lists the typical moves from each level to the next. It is a practical heuristic for planning and communication, built on practitioner consensus. It is not a validated or certified instrument, and the level boundaries are judgements.

## How this model relates to others

Several published AI maturity models exist, from research organisations, standards bodies, consultancies and vendors. One example is the MITRE AI Maturity Model, which organises maturity into six pillars and five levels and comes with an organisational assessment tool [1]. Management system standards such as ISO/IEC 42001 [2] are not maturity models, but they describe the governance an organisation needs to manage AI systems and can serve as a reference for the upper levels.

This model is deliberately lighter. It focuses on adopting AI tools (including generative AI assistants and AI features in existing software) rather than building AI systems, and it uses the same dimensions as the rest of this guide's assessments. If you need a model for formal benchmarking, external reporting or certification, consult the published models directly and check their methodology.

## The five levels

| Level | Name | One-line description |
|---|---|---|
| 1 | Exploring | Individuals try AI tools informally; the organisation has no shared position. |
| 2 | Experimenting | The organisation acknowledges AI use, sets basic rules and runs small trials. |
| 3 | Formalising | Policies, roles, processes and training are defined; pilots are structured and measured. |
| 4 | Scaling | Proven use cases are rolled out widely with consistent governance, support and measurement. |
| 5 | Optimising | AI use is managed as a portfolio, continuously measured, reviewed and improved. |

Higher is not automatically better. Level 3 is a reasonable target for many small organisations; Level 5 needs sustained investment and makes most sense where AI is material to the organisation's work or risk profile. Decide your target level per dimension based on your objectives and risk appetite.

## Level-descriptor matrix

| Dimension | 1 Exploring | 2 Experimenting | 3 Formalising | 4 Scaling | 5 Optimising |
|---|---|---|---|---|---|
| **Strategy and leadership** | No stated purpose; leaders' views vary or are unknown | Leadership acknowledges AI; a sponsor emerges; ideas collected | Written purpose linked to objectives; named sponsor; risk appetite agreed; roadmap with decision points | Roadmap funded across the organisation; sponsor reports outcomes to board or owners | Strategy reviewed against measured value; AI considered routinely in wider strategic planning |
| **Use cases and value** | Use driven by individual curiosity; no list | Ideas list; a few trials; benefits anecdotal | Register and consistent prioritisation; baselines set before pilots; stop criteria defined | Proven use cases scaled with measured benefits; register maintained | Portfolio managed: benefits tracked against estimates, low-value uses retired, successes reused |
| **Data** | Unknown what data staff put into tools; permissions not reviewed | Classification guidance issued; obvious oversharing known | Data inventory for priority sources; permissions remediated where AI tools connect; data readiness checked per use case | Data governance applied across all connected sources; quality owners in place | Data quality and access monitored; AI-generated content covered by retention and records rules |
| **Technology and security** | Personal or free tools; no visibility or control | Approved tool list; basic admin settings; some discovery of shadow use | Enterprise controls configured (identity, data loss prevention, logging); AI-specific threats in security review | Standard platform and support model; monitoring in place; integrations managed | Controls tested and tuned; capacity and cost actively managed; architecture reviewed as capabilities change |
| **People and skills** | Self-taught individuals | Introductory awareness session; enthusiasts emerge | Role-based curricula; AI literacy recorded; champions named; managers briefed | Most staff trained for their role; active community of practice; role impacts assessed with staff | Skills planned ahead of roadmap; training effectiveness measured; job design updated |
| **Governance and risk** | No policy; no owner | Interim acceptable use policy; informal approvals | AI policy and acceptable use policy; RACI; risk assessment, DPIA screening and vendor due diligence applied per use case | Governance operating at scale; regulatory obligations mapped; post-deployment monitoring | Governance reviewed for effectiveness; horizon scanning; may align to a management system standard |
| **Culture and change** | Mixed feelings, unspoken; use may be hidden | Open conversation starts; concerns heard informally | Communication plan; safe experimentation; incident and concern routes | Two-way engagement at scale; lessons shared; trust actively built | Learning culture; staff shape AI use; sentiment measured and acted on |

## How to self-locate

You can locate yourself in two ways. Use whichever suits the time you have.

### Option A: Quick read (30 minutes)

1. For each dimension, read the row left to right.
2. Pick the **highest level whose description is fully true** today. If you are partly at Level 3 and fully at Level 2, you are at Level 2.
3. Record the level and one piece of evidence for each dimension.

### Option B: From readiness scores

If you have completed the [organisational readiness assessment](organisational-readiness.md), convert each dimension's average score (0–4) to a level:

| Dimension average | Maturity level |
|---|---|
| 0.0–0.7 | 1 Exploring |
| 0.8–1.5 | 2 Experimenting |
| 1.6–2.4 | 3 Formalising |
| 2.5–3.2 | 4 Scaling |
| 3.3–4.0 | 5 Optimising |

The two methods may disagree. Where they do, discuss why: averages can be pulled up by a few strong answers while a basic element is missing.

### Your overall level

Do not average the levels into a single number for decision-making. Report a **profile** (for example "Strategy 3, Use cases 2, Data 2, Technology 3, People 2, Governance 2, Culture 3"). If you need one headline level for communication, use the **lowest** dimension level, because weak foundations constrain everything else. For example, strong technology controls do not compensate for staff who have not been trained.

## How to progress

### General rules

- **Move one level at a time.** Skipping levels usually means building processes without the foundations they depend on.
- **Fix the lowest dimension first** when it blocks others (typically governance, data or people).
- **Set a target profile**, not a single target level, and a date to reassess (six to twelve months is common).
- **Evidence beats activity.** A level is reached when the description is true in practice, not when a document has been written.

### Typical moves between levels

| From → to | Typical actions | Useful templates |
|---|---|---|
| 1 → 2 | Name a sponsor. Issue an interim acceptable use policy. Run a discovery exercise to find current use. Approve a small set of tools with basic settings. Run an awareness session. Collect use case ideas. | [Acceptable use policy](../toolkits/acceptable-use-policy.md), [use case register](../toolkits/use-case-register-template.md) |
| 2 → 3 | Write an organisational AI policy and RACI. Agree risk appetite. Prioritise use cases and set baselines. Run structured pilots with stop criteria. Introduce role-based training. Apply risk, data and vendor assessments per use case. | [AI policy](../toolkits/ai-policy-template.md), [RACI](../toolkits/raci-template.md), [pilot plan](../toolkits/pilot-plan-template.md), [training plan](../toolkits/training-plan-template.md), [use case prioritisation](use-case-prioritisation.md), [AI risk assessment](ai-risk-assessment.md) |
| 3 → 4 | Build business cases from pilot evidence. Define the support model. Roll out in waves with communication and training. Remediate data permissions across connected sources. Monitor use and value. | [Business case](../toolkits/business-case-template.md), [communication plan](../toolkits/communication-plan-template.md), [Scale stage](../docs/lifecycle/05-scale.md) |
| 4 → 5 | Manage AI as a portfolio. Compare benefits with estimates and retire low-value uses. Measure training effectiveness. Review governance effectiveness and consider alignment with a management system standard. Build horizon scanning for regulation and capability change. | [Measuring value](../docs/measurement/measuring-value.md), [Operate stage](../docs/lifecycle/06-operate.md), [prompt library](../toolkits/prompt-library-template.md) |

### For small organisations

A small organisation can reach Level 3 with modest effort: a two-page policy, a named owner, an approved tool configured with its business data controls, a short training session recorded in a spreadsheet, and a simple register. Levels 4 and 5 mostly concern repeatability across many teams, which matters less when everyone sits in one room.

## Limitations

- The levels and descriptors are a judgement based on practitioner consensus, not on empirical research into what predicts successful adoption.
- Maturity is not the same as value. An organisation at Level 2 with one well-chosen use case may get more benefit than a Level 4 organisation with many weak ones. Pair this model with [value measurement](../docs/measurement/measuring-value.md).
- Maturity can go backwards, for example when tools change, key people leave or regulation changes. Reassess periodically.

## Sources

1. MITRE, *The MITRE AI Maturity Model and Organizational Assessment Tool Guide*. https://aimaturitymodel.mitre.org/
2. ISO/IEC, *ISO/IEC 42001:2023 Information technology — Artificial intelligence — Management system*, December 2023. https://www.iso.org/standard/42001

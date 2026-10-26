# Use case prioritisation

> **Who this is for:** Anyone choosing which AI use cases to pursue first: programme leads, managers, product owners, business analysts, and small business owners with a list of ideas and limited time.
> **Last reviewed:** 2026-10

This assessment helps you score and rank candidate AI use cases consistently on three axes: value (what it is worth), feasibility (how hard it is to do well) and risk (what could go wrong and how badly). Each axis has five criteria scored 0–4 against explicit descriptors. You combine them into a weighted score, plot use cases on a value-feasibility matrix, and apply risk gates that stop a high-scoring but unacceptable use case from going ahead without review. A worked example with four clearly fictional use cases shows the method end to end. Use it at the [Discover](../docs/lifecycle/01-discover.md) and [Select](../docs/lifecycle/03-select.md) stages.

## When to use it

- You have more ideas than capacity and need to choose a first wave of pilots.
- You want to replace "loudest voice" or vendor-led selection with a transparent method.
- You are revisiting priorities after pilots, with real evidence in hand.

## Who should score

Score with a small group that covers the work itself (someone who does the task today), the business owner, technology (internal or supplier), and risk or data protection. Two to five people is enough. Score individually first, then agree a consensus score, discussing any criterion where scores differ by two or more points.

## Before scoring: describe each use case

Each candidate needs a one-paragraph description using the fields below, ideally recorded in your [use case register](../toolkits/use-case-register-template.md). Scoring without a clear description produces unreliable results.

- **Problem:** What task or decision is slow, costly, error-prone or unpleasant today?
- **Proposed AI role:** Draft, summarise, search, classify, extract, translate, generate code, recommend, decide? (Use cases where the AI *decides* rather than *assists* carry more risk.)
- **Users and affected people:** Who uses it; who is affected by its outputs?
- **Data:** What information does it need?
- **Human oversight:** Who checks outputs, and before what happens?
- **Baseline:** How long or how well is this done today? (An estimate is acceptable at this stage; say so.)

## The criteria

### Value (default weight 40%)

| # | Criterion | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| V1 | Size of efficiency benefit | None expected | Saves minutes occasionally | Noticeable time saving for some users | Substantial time saving on a frequent task | Large, frequent saving on a high-volume task |
| V2 | Quality or outcome benefit | None or negative | Marginal | Some improvement in consistency, accuracy or experience | Clear improvement for users or customers | Major improvement in an outcome that matters |
| V3 | Strategic alignment | Unrelated to objectives | Loosely related | Supports a team objective | Supports an organisational objective | Central to a top organisational priority |
| V4 | Reach | One person | A few people | One team | Several teams | Most of the organisation, or many customers |
| V5 | Measurability | Benefit cannot be observed | Anecdotal only | Measurable with effort | Baseline exists or is easy to collect | Already measured; clear before/after comparison possible |

### Feasibility (default weight 35%)

| # | Criterion | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| F1 | Data readiness | Data does not exist or cannot be used | Exists but poor quality, scattered or access restricted | Usable with significant preparation | Usable with modest preparation | Ready, clean, permissioned (see [data readiness](data-readiness.md)) |
| F2 | Tool availability and integration | No suitable tool | Would need custom build | Available but needs integration work | Available with configuration | Available in tools already licensed and configured |
| F3 | Skills and capacity | No one to deliver or support | Relies on one enthusiast | Some capacity, gaps known | Capacity available internally or via supplier | Capacity available and experienced with similar work |
| F4 | Process change required | Major redesign across teams | Significant change for users | Moderate change in one team | Minor change to existing steps | Fits into existing workflow |
| F5 | Time to first value | Over 12 months | 6–12 months | 3–6 months | 1–3 months | Under a month |

### Risk (default weight 25%)

Risk criteria are scored so that **higher means lower risk**, so all three axes point the same way.

| # | Criterion | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|
| R1 | Consequence of an error | Serious harm to people, safety or legal position | Significant financial, legal or service harm | Moderate harm; correctable with effort | Minor, easily corrected | Negligible |
| R2 | Data sensitivity | Special category, criminal, or highly confidential data at scale | Personal or confidential data, significant volume | Some personal or internal data | Internal, non-sensitive data | Public or synthetic data only |
| R3 | Regulatory exposure | Likely in a regulated high-risk category (e.g. EU AI Act Annex III areas such as employment or creditworthiness) | Regulated activity with specific AI-relevant rules | General obligations (e.g. data protection, consumer law) apply | Minimal obligations | No specific obligations identified |
| R4 | Impact on people's rights and fair treatment | Makes or heavily shapes decisions about individuals | Influences decisions about individuals | Indirect effect on individuals | Minimal effect on individuals | No effect on individuals |
| R5 | External exposure | Outputs go directly to the public without review | Outputs go to customers or partners with light review | Outputs go externally after full human review | Internal use, shared beyond the team | Internal use by the individual only |

The high-risk areas in Annex III of the EU AI Act include biometrics, critical infrastructure, education, employment, access to essential private and public services (including credit scoring and some insurance), law enforcement, migration and border management, and administration of justice and democratic processes [1]. Obligations for these systems were deferred by the Digital Omnibus on AI, to 2 December 2027 for Annex III systems [2]. See the [regulation overview](../docs/governance/regulation-overview.md) and take legal advice where relevant.

## Scoring method

1. **Axis averages.** For each use case, average the five scores on each axis (giving three numbers from 0 to 4).
2. **Composite score.** `Composite = 0.40 × Value + 0.35 × Feasibility + 0.25 × Risk`. Convert to a percentage by dividing by 4 and multiplying by 100.
3. **Risk gates.** Apply these regardless of composite score:
   - Any risk criterion scored **0**: the use case may not proceed until a full [AI risk assessment](ai-risk-assessment.md) and, where relevant, legal review are complete and signed off.
   - Risk axis average **below 1.5**: treat as high risk; complete the risk assessment before piloting and require senior sign-off.
   - R2 scored 0 or 1, or the use case involves personal data and R4 is 2 or below: run the DPIA screening in the [AI risk assessment](ai-risk-assessment.md#part-a-screening-questionnaire).
4. **Plot.** Place each use case on the value-feasibility matrix below, and mark its risk level (for example with a colour or a letter H/M/L).
5. **Decide.** Use the matrix and gates together, not the composite score alone.

**Adjusting weights.** The default weights are a judgement. A risk-averse or regulated organisation might use 35/30/35; one seeking quick learning might weight feasibility higher. Agree weights before scoring, record them, and keep them stable within a round so results remain comparable.

## The value-feasibility matrix

|  | **Feasibility below 2.5** | **Feasibility 2.5 or above** |
|---|---|---|
| **Value 2.5 or above** | **Strategic bets.** Worth doing, but need foundations (data, integration, skills). Plan the enabling work; consider a scoped pilot. | **Priority pilots.** High value and achievable. Pilot first, subject to risk gates. |
| **Value below 2.5** | **Park.** Revisit if circumstances change. | **Low-effort options.** Cheap to try; useful for building skills and confidence. Do not let them crowd out higher-value work. |

## Worked example (fictional)

> Everything in this example is **fictional**: the organisation, use cases and scores were invented to illustrate the method.

**Context:** *Fernhill Housing Trust* (fictional) is a 300-person housing association. It has a general-purpose AI assistant licensed for staff, and a list of ideas. It uses the default weights.

### The four candidate use cases (fictional)

| ID | Use case | AI role | Human oversight |
|---|---|---|---|
| A | Draft replies to routine tenant enquiries | Drafts; officer edits and sends | Every reply reviewed before sending |
| B | Summarise internal meeting notes and actions | Summarises | Meeting chair checks summary |
| C | Automatically shortlist job applicants | Ranks and filters candidates | HR reviews shortlist only |
| D | Staff Q&A over internal policy documents (retrieval-augmented generation) | Searches and answers with citations | Staff check cited source for important decisions |

### Scores (fictional)

| Criterion | A | B | C | D |
|---|---|---|---|---|
| V1 Efficiency | 3 | 2 | 3 | 3 |
| V2 Quality | 3 | 2 | 2 | 3 |
| V3 Strategic | 3 | 2 | 2 | 3 |
| V4 Reach | 3 | 3 | 1 | 3 |
| V5 Measurability | 3 | 2 | 3 | 2 |
| **Value average** | **3.0** | **2.2** | **2.2** | **2.8** |
| F1 Data | 2 | 4 | 2 | 1 |
| F2 Tool | 3 | 4 | 2 | 2 |
| F3 Skills | 2 | 3 | 1 | 2 |
| F4 Process change | 2 | 4 | 2 | 3 |
| F5 Time to value | 3 | 4 | 2 | 2 |
| **Feasibility average** | **2.4** | **3.8** | **1.8** | **2.0** |
| R1 Error consequence | 2 | 3 | 1 | 3 |
| R2 Data sensitivity | 1 | 2 | 1 | 3 |
| R3 Regulatory | 2 | 3 | 0 | 3 |
| R4 Impact on people | 2 | 4 | 0 | 3 |
| R5 External exposure | 2 | 4 | 1 | 3 |
| **Risk average** | **1.8** | **3.2** | **0.6** | **3.0** |

### Composite scores (fictional)

| Use case | Calculation | Composite | % |
|---|---|---|---|
| A | 0.40 × 3.0 + 0.35 × 2.4 + 0.25 × 1.8 | 2.49 | 62% |
| B | 0.40 × 2.2 + 0.35 × 3.8 + 0.25 × 3.2 | 3.01 | 75% |
| C | 0.40 × 2.2 + 0.35 × 1.8 + 0.25 × 0.6 | 1.66 | 42% |
| D | 0.40 × 2.8 + 0.35 × 2.0 + 0.25 × 3.0 | 2.57 | 64% |

### Applying gates and the matrix (fictional)

| Use case | Quadrant | Risk gates | Decision |
|---|---|---|---|
| A Tenant replies | Strategic bet (value 3.0, feasibility 2.4) | R2 = 1, personal data: DPIA screening required | Pilot with one team after DPIA screening and an [AI risk assessment](ai-risk-assessment.md); measure time per reply and complaint rates against baseline |
| B Meeting summaries | Low-effort option (value 2.2, feasibility 3.8) | None triggered | Enable now with guidance; use as a training ground. Highest composite, but low value: do not count it as the programme's main benefit |
| C Applicant shortlisting | Park (value 2.2, feasibility 1.8) | R3 = 0 and R4 = 0: full risk assessment and legal review required; employment is an Annex III area under the EU AI Act | Do not proceed. Revisit only with legal advice, an equality impact assessment and a clear case that human decision-making is preserved |
| D Policy Q&A | Strategic bet (value 2.8, feasibility 2.0) | None triggered | Fund data preparation first (policy documents are out of date and scattered), then pilot. Use [data readiness](data-readiness.md) to scope the work |

**What the example shows.** The highest composite score (B) is not the most valuable use case. The most valuable (A) needs controls. A use case that some staff were enthusiastic about (C) is stopped by gates, not by its average. Read the three axes and gates together.

## Interpreting composite scores

Composite percentages are for ranking within one scoring round, not for comparison across organisations.

| Composite | Typical meaning | What to do next |
|---|---|---|
| 75–100% | Strong candidate on all axes | Prioritise for pilot, subject to gates; prepare a [pilot plan](../toolkits/pilot-plan-template.md) |
| 55–74% | Promising, with a weak axis | Identify the weak axis; fix data or integration gaps, or add controls, then pilot |
| 35–54% | Marginal | Park unless strategically essential; look for a simpler variant (e.g. "assist" instead of "decide") |
| 0–34% | Poor fit at present | Do not pursue now; record the reason in the register |

## After the pilot: re-score

Re-score each piloted use case using evidence from the pilot. Replace estimated values (especially V1, V5, F1 and R1) with observed ones. Large changes are common and useful; they improve future estimates. Record both sets of scores in the register.

## Limitations

- Scores are judgements. The method makes them consistent and visible; it does not make them objective.
- The criteria and weights reflect practitioner consensus, not empirical validation.
- Averaging can hide a single severe weakness, which is why risk gates exist. Add your own gates for factors that are non-negotiable in your context (for example, safeguarding).

## Sources

1. Regulation (EU) 2024/1689 (Artificial Intelligence Act), Annex III, as summarised in European Commission presentation material, *AI Act* (European Digital Innovation Hubs), December 2024. https://european-digital-innovation-hubs.ec.europa.eu/system/files/2024-12/01_Martin%20Ulbrich_Presentation%20AI%20Act.pdf
2. Regulation (EU) 2026/1744 (Digital Omnibus on AI), published in the Official Journal 24 July 2026, in force 27 July 2026. EUR-Lex record: https://eur-lex.europa.eu/eli/reg/2026/1744/oj ; summary of revised dates: National Law Review, *EU Digital Omnibus on AI Enters into Force*, 2026. https://natlawreview.com/article/eu-digital-omnibus-ai-enters-force

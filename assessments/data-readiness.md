# Data readiness assessment

> **Who this is for:** Data owners, data and analytics teams, IT and platform teams, data protection officers, and business owners of a proposed AI use case. Also useful for small organisations connecting an AI assistant to shared drives or a document store.
> **Last reviewed:** 2026-10

This assessment checks whether the data behind a specific AI use case is fit for that purpose. It covers six areas (availability, quality, access rights, sensitivity, lineage and freshness) and adjusts the questions for the three most common patterns: retrieval-augmented generation (RAG) over documents, analytics and AI-assisted data work, and fine-tuning or training a model. Each question is scored 0–4. You get an area profile, an overall score and a list of blockers. Run it once per use case at the [Assess](../docs/lifecycle/02-assess.md) stage, before committing to a pilot, and again before scaling.

## Choose your pattern

The same data can be ready for one pattern and not another. Pick the pattern that matches the use case, then answer the core questions plus the pattern-specific ones.

| Pattern | What it means | Typical examples | What matters most |
|---|---|---|---|
| **RAG / grounded assistant** | The AI retrieves relevant documents or records at query time and uses them to answer. The model itself is not changed. Includes AI assistants connected to email, files or intranets. | Policy Q&A, knowledge search, assistants with access to shared drives | Access permissions, currency of documents, duplication and contradictions, sensitivity |
| **Analytics and AI-assisted data work** | AI helps query, analyse, visualise or explain structured data. | Natural-language querying of a data warehouse, AI-generated analysis or reports | Data quality, definitions and semantics, lineage, access controls at row or column level |
| **Fine-tuning or training** | Your data is used to adapt or train a model, changing its behaviour permanently. | Domain-specific classification, style adaptation, custom models | Lawful basis and rights to use data, representativeness, labelling quality, inability to "untrain" easily |

If a use case combines patterns (for example RAG plus analytics), complete the pattern-specific questions for each.

## Before you start

Record:

- **Use case:** [name and ID from the use case register]
- **Pattern(s):** [RAG / Analytics / Fine-tuning]
- **Data sources in scope:** [list each system, repository or dataset]
- **Data owner(s):** [names]
- **Assessed by and date:** [names, date]

Score each data source separately if they differ significantly. A use case is only as ready as its weakest essential source.

## Scale

| Score | Meaning |
|---|---|
| 0 | Not in place, or unknown |
| 1 | Known problem; not addressed |
| 2 | Partly in place; significant work needed |
| 3 | Largely in place; minor work needed |
| 4 | Fully in place and maintained |

## Core questions (all patterns)

### 1. Availability

| # | Question | 0 | 2 | 4 |
|---|---|---|---|---|
| A1 | Does the data needed for the use case exist? | Does not exist | Exists in part, or only in people's heads or paper | Exists in full, in digital form |
| A2 | Is it in a location and format the AI tool can reach? | Not reachable (e.g. locked formats, offline, scanned images without text) | Reachable with conversion or integration work | Reachable directly by the intended tool |
| A3 | Is there enough of it to be useful? | Far too little | Adequate for some cases | Sufficient coverage of the cases the use case must handle |
| A4 | Is ownership of each source clear? | No owner | Owner identifiable but not engaged | Named owner who has agreed to the use |

### 2. Quality

| # | Question | 0 | 2 | 4 |
|---|---|---|---|---|
| Q1 | Is the data accurate? | Known to be often wrong, or unknown | Errors known in places | Accuracy checked; errors corrected through a process |
| Q2 | Is it complete for the use case? | Major gaps | Some gaps, known | Complete for intended scope |
| Q3 | Is it consistent (no contradictory versions, consistent definitions)? | Many contradictions or duplicates | Some duplication or conflicting versions | Single authoritative version; definitions documented |
| Q4 | Is it representative of the people and situations the use case will serve? | Unknown or clearly skewed | Some known gaps | Coverage checked against the population served |

Scores of 1 and 3 sit between the descriptors shown.

### 3. Access rights and permissions

| # | Question | 0 | 2 | 4 |
|---|---|---|---|---|
| R1 | Do you have the legal and contractual right to use this data for this purpose? | Unknown, or no | Probably, not confirmed | Confirmed by data owner and, where needed, legal or data protection review |
| R2 | Are permissions on the source appropriate (least privilege)? | Widely open, or unknown | Known oversharing being remediated | Reviewed; users see only what they should |
| R3 | Will the AI tool respect existing permissions (users only get answers from data they can already access)? | No, or unknown | Partly; some sources bypass permissions | Yes, verified by testing |
| R4 | Are third-party licence terms respected (e.g. purchased content, partner data)? | Unknown | Checked for some sources | Checked for all sources; restrictions recorded |

### 4. Sensitivity

| # | Question | 0 | 2 | 4 |
|---|---|---|---|---|
| S1 | Do you know whether the data contains personal data? | Unknown | Partly known | Known and recorded |
| S2 | Do you know whether it contains special category, criminal offence, or highly confidential data? | Unknown | Partly known | Known and recorded, with controls |
| S3 | Is the sensitivity classification applied to the data (labels, locations)? | No | For some sources | Consistently applied |
| S4 | Are controls proportionate to sensitivity (minimisation, masking, exclusion of sensitive areas)? | None | Some | Controls in place and tested |

If S1 or S2 indicates personal or special category data, complete the screening questionnaire in the [AI risk assessment](ai-risk-assessment.md#part-a-screening-questionnaire), which includes DPIA triggers. Special category data is defined in Article 9 of the UK and EU GDPR; it includes data about health, racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership, genetic and biometric data (for identification), sex life and sexual orientation.

### 5. Lineage

| # | Question | 0 | 2 | 4 |
|---|---|---|---|---|
| L1 | Do you know where the data came from? | No | For main sources | Documented for all sources |
| L2 | Do you know how it has been transformed? | No | Partly | Transformations documented |
| L3 | Can AI outputs be traced back to source data (citations, references)? | No | Sometimes | Consistently, by design |

### 6. Freshness

| # | Question | 0 | 2 | 4 |
|---|---|---|---|---|
| F1 | Is the data current enough for the use case? | Out of date, or unknown | Mixed; some outdated content | Current, with update frequency matching the need |
| F2 | Are superseded versions removed or clearly marked? | No | Partly | Yes, through a retention or archiving process |
| F3 | Will updates to source data flow to the AI tool on time? | No mechanism | Manual or irregular | Automated, with a known lag |

## Pattern-specific questions

### RAG / grounded assistant

| # | Question | 0 | 2 | 4 |
|---|---|---|---|---|
| G1 | Has oversharing been checked in the repositories the assistant will index (e.g. "everyone" access to HR or finance folders)? | No | Started | Completed and remediated |
| G2 | Are sensitive areas excluded from indexing where needed? | No | Some | All identified areas excluded and tested |
| G3 | Is content structured well enough to retrieve (meaningful titles, text not locked in images, reasonable document length)? | Poor | Mixed | Good |
| G4 | Have you tested answers against a set of known questions with known correct answers? | No | Informally | Structured test set with results recorded |

### Analytics and AI-assisted data work

| # | Question | 0 | 2 | 4 |
|---|---|---|---|---|
| N1 | Are business definitions (metrics, dimensions) documented in a form the AI tool can use (e.g. semantic layer, data dictionary)? | No | Partly | Yes, maintained |
| N2 | Are row-level and column-level security applied where needed? | No | Partly | Yes, and respected by the AI tool |
| N3 | Can AI-generated queries and calculations be inspected and checked? | No | Sometimes | Always visible to users |
| N4 | Have you tested AI-generated results against known correct answers? | No | Informally | Structured test with results recorded |

### Fine-tuning or training

| # | Question | 0 | 2 | 4 |
|---|---|---|---|---|
| T1 | Is the lawful basis (and, if required, transparency to individuals) established for training use of any personal data? | No | Under review | Confirmed and documented |
| T2 | Are labels or target outputs accurate and consistently applied? | Unknown | Spot-checked | Measured agreement; quality process |
| T3 | Have you checked the data for bias against groups the system will affect? | No | Informally | Structured analysis documented |
| T4 | Is a held-out evaluation set reserved and protected from training? | No | Ad hoc | Yes, documented |
| T5 | Have you considered that personal or confidential data in training may be hard to remove later? | No | Discussed | Data minimised before training; decision documented |

Fine-tuning raises distinct data protection questions. The European Data Protection Board adopted Opinion 28/2024 on processing personal data in the context of AI models in December 2024, including when a model can be considered anonymous [1]. In the UK, the ICO's guidance on AI and data protection applies, noting that the ICO has said it is under review following the Data (Use and Access) Act [2]. See [data protection](../docs/governance/data-protection.md).

## Scoring

1. **Area scores.** Average the questions in each of the six core areas (0–4).
2. **Pattern score.** Average the pattern-specific questions.
3. **Overall score.** Average the six area scores and the pattern score (seven equal parts), then convert to a percentage (`÷ 4 × 100`). Equal weighting is the default; increase the weight of sensitivity and access rights if your data is highly sensitive, and record the change.
4. **Blockers.** Any of the following is a blocker, whatever the overall score:

| Blocker | Condition |
|---|---|
| No right to use | R1 scored 0 or 1 |
| Permissions not respected | R3 scored 0 or 1 (RAG and analytics patterns) |
| Unknown sensitivity | S1 or S2 scored 0 |
| Oversharing unchecked | G1 scored 0 (RAG pattern) |
| No lawful basis for training | T1 scored 0 or 1 (fine-tuning pattern) |
| Untested accuracy | G4 or N4 scored 0 before go-live (pilots may proceed if testing is part of the pilot plan) |

## Interpreting results

| Band | Overall | Meaning | What to do next |
|---|---|---|---|
| Not ready | 0–39% or any blocker | Data cannot support the use case safely | Resolve blockers first. Consider a narrower scope (fewer sources, less sensitive data) or a different pattern (e.g. RAG instead of fine-tuning). Feed findings back to [use case prioritisation](use-case-prioritisation.md) (F1). |
| Conditionally ready | 40–64%, no blockers | Usable for a limited pilot with explicit mitigations | Pilot with restricted scope and users. Include data remediation in the [pilot plan](../toolkits/pilot-plan-template.md). Re-assess before scaling. |
| Ready | 65–84%, no blockers | Supports the use case with minor work | Proceed. Track remaining actions with owners. |
| Well prepared | 85–100%, no blockers | Strong data foundations for this use case | Proceed. Use as a reference pattern for similar use cases. |

## Action log

| # | Finding | Area | Action | Owner | Due | Status |
|---|---|---|---|---|---|---|
| 1 | [e.g. HR folder shared with all staff] | Access rights | [Restrict to HR group before indexing] | [name] | [date] | [open] |
| 2 | | | | | | |

## Notes for small organisations

If you are connecting a general-purpose AI assistant to your shared drive or email, the most important questions are R2, R3, S1–S2, G1 and F2. Many small organisations find that shared folders have accumulated broad permissions over time. A one-off tidy-up of permissions and old files before enabling the assistant is usually the most valuable step.

## Sources

1. European Data Protection Board, *Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models*, December 2024 (summary: CMS, *EDPB Opinion 28/2024: key takeaways*). https://cms.law/en/int/legal-updates/edpb-opinion-28-2024-key-takeaways-on-processing-personal-data-in-the-context-of-ai-models
2. Information Commissioner's Office, *Guidance on AI and data protection: About this guidance* (notes guidance is under review following the Data (Use and Access) Act). https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/about-this-guidance/

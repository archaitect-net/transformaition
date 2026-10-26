# Use case register template

> **Who this is for:** Programme leads, governance groups, risk teams and managers who need a single record of AI use cases, from idea to retirement. A spreadsheet is fine; a small organisation can use the minimum fields only.
> **Last reviewed:** 2026-10

This template defines a register for recording every AI use case in your organisation: proposed, in pilot, live, or retired. It lists the fields to capture (grouped into identification, description, assessment, approval, operation and review), explains each field, marks a minimum set for small organisations, and gives fictional example rows. A register gives you visibility of what AI is in use, supports governance and regulatory obligations, prevents duplicated effort, and makes reuse and retirement possible. It is referenced throughout the [assessments](../assessments/README.md) and the [AI policy template](ai-policy-template.md).

> **Guidance: getting started**
>
> - **Start with what already exists.** Include AI already in use informally and AI features in existing software, not only new proposals. A discovery exercise (survey, IT logs, conversations with managers) helps.
> - **Keep it maintained.** A register is only useful if it is current. Assign an owner (usually the programme lead) and review it at governance meetings.
> - **Decide visibility.** Many organisations make a summary visible to all staff to encourage reuse and transparency. Some publish a public summary of significant uses.
> - **Choose a format.** A shared spreadsheet, a list in your collaboration platform, or a governance, risk and compliance (GRC) tool all work. Use controlled values (drop-downs) for status and risk fields so that you can filter and report.

## Fields

**M** = minimum field set recommended for small organisations.

### Identification

| Field | M | Description | Allowed values / format |
|---|---|---|---|
| ID | M | Unique reference | e.g. UC-001 |
| Name | M | Short descriptive name | Text |
| Business area | M | Team or function | List |
| Use case owner | M | Accountable person | Name, role |
| Date added | | When recorded | Date |

### Description

| Field | M | Description | Allowed values / format |
|---|---|---|---|
| Problem / purpose | M | What problem it solves | Text |
| AI role | M | What the AI does | Draft / Summarise / Search and answer / Classify / Extract / Translate / Generate code / Recommend / Decide / Act autonomously |
| Users | | Who uses it | Roles, approximate number |
| Affected people | | Who is affected by outputs | e.g. staff, customers, applicants, public |
| Human oversight | M | Who checks outputs and when | Text |
| Tool / product | M | AI tool, product, plan | Text |
| Model (if known) | | Underlying model and version | Text |
| Supplier | | Vendor | Text |
| Data used | M | Sources and categories | Text |
| Highest data classification | M | | Public / Internal / Confidential / Restricted |
| Personal data? | M | | Yes / No |
| Special category or criminal offence data? | | | Yes / No |
| Integrations | | Systems connected | Text |
| Pattern | | Technical pattern | Assistant / RAG / Analytics / Fine-tuned / Agent / Embedded feature |

### Assessment

| Field | M | Description | Allowed values / format |
|---|---|---|---|
| Prioritisation scores | | Value, feasibility, risk averages and composite from [use case prioritisation](../assessments/use-case-prioritisation.md) | Numbers |
| Risk screening result | M | From [AI risk assessment](../assessments/ai-risk-assessment.md) Part A | Low / Medium / High |
| Highest residual risk | | From risk register | Low / Medium / High / Very high |
| DPIA status | | | Not required (screened) / Required, in progress / Completed [date] |
| Legal review | | | Not required / Requested / Completed |
| EU AI Act category (if applicable) | | Your assessment, with legal advice where needed | Not in scope / Minimal / Transparency obligations / High-risk / Prohibited / Not yet assessed |
| Data readiness score | | From [data readiness](../assessments/data-readiness.md) | % and blockers |
| Vendor due diligence | | | Not required / Completed [date, result] |
| Links to assessments | | | Links |

### Approval and lifecycle

| Field | M | Description | Allowed values / format |
|---|---|---|---|
| Status | M | Current lifecycle status | Idea / Assessing / Approved for pilot / In pilot / Approved for production / Live / Paused / Stopped / Retired |
| Approved by | M | Who approved, at what level | Name, role, date |
| Conditions of approval | | | Text |
| Pilot dates | | | Dates |
| Go-live date | | | Date |

### Operation and value

| Field | M | Description | Allowed values / format |
|---|---|---|---|
| Success measures | | Measures and targets | Text |
| Baseline | | Measured before | Text / numbers |
| Latest results | | Measured since | Text / numbers, date |
| Incidents | | Count and references | Number, links |
| Annual cost | | Licences plus run costs | Currency |

### Review

| Field | M | Description | Allowed values / format |
|---|---|---|---|
| Last reviewed | M | | Date |
| Next review due | M | | Date |
| Re-assessment triggers | | | e.g. model change, new data |
| Notes | | | Text |

## Example rows (fictional)

> Everything below is **fictional**, for illustration only. Columns are a subset of the full field list.

| ID | Name | Business area | Owner | AI role | Tool / pattern | Highest data class. | Personal data | Risk screening | DPIA | Status | Approved by | Next review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| UC-001 | Meeting summaries | All | Ops Manager | Summarise | General assistant (embedded feature) | Internal | Yes (names) | Low | Not required (screened 2026-03) | Live | Ops Director, 2026-03 | 2027-03 |
| UC-002 | Draft replies to customer enquiries | Customer Service | CS Team Lead | Draft | General assistant + knowledge base (RAG) | Confidential | Yes | Medium | Completed 2026-05 | In pilot | AI governance group, 2026-05, conditions: 100% human review; weekly audit | 2026-12 |
| UC-003 | Policy Q&A for staff | HR | HR Business Partner | Search and answer | RAG over policy library | Internal | No | Low | Not required (screened 2026-06) | Assessing (data remediation) | — | 2026-11 |
| UC-004 | Shortlisting job applicants | HR | Head of Recruitment | Recommend | Recruitment platform AI feature | Confidential | Yes | High | Not started | Stopped | AI governance group, 2026-07: not approved; employment is a high-risk area; revisit only with legal advice | — |
| UC-005 | Code completion | Engineering | Engineering Lead | Generate code | Coding assistant | Internal | No | Low | Not required | Live | CTO, 2026-01, conditions: no secrets in prompts; standard code review | 2027-01 |
| UC-006 | Translation of public leaflets | Comms | Comms Officer | Translate | General assistant | Public | No | Low (A2.5 external: human review by fluent speaker) | Not required | Live | Comms Manager, 2026-04 | 2027-04 |

## Reports you can produce from the register

- **Inventory:** all live AI use cases, by business area and risk level.
- **Pipeline:** ideas and use cases in assessment or pilot, with status.
- **Risk view:** use cases with High or Very high residual risk, and those overdue for review.
- **Data view:** use cases processing personal or special category data, and DPIA status.
- **Supplier view:** use cases by vendor, for contract and concentration risk.
- **Value view:** use cases with measured results against baseline.
- **Regulatory view:** use cases by AI Act category, where applicable.

## Review routine

| Frequency | Activity | Who |
|---|---|---|
| Monthly | Update statuses; add new ideas; check for overdue reviews | Programme lead |
| Quarterly | Review High-risk and live use cases; incidents; value | AI governance group |
| Annually | Full review; confirm every live use case is still needed, safe and valuable; retire those that are not | AI governance group |
| On trigger | Re-assess when model, data, purpose, users or law change | Use case owner |

## Related

- [AI policy template](ai-policy-template.md) (section 6, use case approval)
- [Use case prioritisation](../assessments/use-case-prioritisation.md)
- [AI risk assessment](../assessments/ai-risk-assessment.md)
- [Operate stage](../docs/lifecycle/06-operate.md)

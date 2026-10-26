# Prompt library template

> **Who this is for:** Champions, team leads, programme leads and anyone curating reusable prompts for colleagues. Works as a shared document for a small team or as a managed library in a larger organisation.
> **Last reviewed:** 2026-10

This template helps you build and maintain a shared library of reusable prompts: tested instructions for AI tools that colleagues can adapt for common tasks. It covers the library's structure, the metadata each entry needs, a review and approval process, maintenance (including what to do when tools or models change), and example entries. A good library speeds up adoption, spreads good practice, and builds safety rules (data classification, verification) into everyday use. Guidance notes in blockquotes explain choices; replace [bracketed placeholders].

> **Guidance: principles**
>
> - **Prompts are not guarantees.** The same prompt can produce different outputs on different runs, tools or model versions. Every entry should say what the user must check.
> - **Tool-agnostic where possible.** Write prompts that work across tools; note any tool-specific features separately.
> - **Safety by design.** Each entry states the maximum data classification it is approved for, consistent with your [acceptable use policy](acceptable-use-policy.md).
> - **Short and adaptable beats long and rigid.** Use clear placeholders for what users must fill in.
> - **Retire prompts** that no longer work or are no longer needed.

## Library structure

Organise entries so people can find them quickly. A common structure:

```text
Prompt library/
├── README (how to use, how to contribute, data rules)
├── General/          Writing, summarising, editing, brainstorming
├── Customer service/
├── HR and people/
├── Finance/
├── Communications/
├── Engineering/
├── Data and analytics/
└── Retired/          Kept for reference; not for use
```

Alternatively, tag entries by **task type** (draft, summarise, analyse, review, transform) and **business area**, and let users filter.

## Entry metadata

| Field | Required | Description |
|---|---|---|
| ID | Yes | e.g. PL-GEN-004 |
| Title | Yes | Short, task-focused |
| Purpose | Yes | What the prompt helps with, in one sentence |
| Business area / tags | Yes | For search |
| Task type | Yes | Draft / Summarise / Analyse / Review / Transform / Brainstorm / Code |
| Tools tested with | Yes | Tool names and dates tested |
| Max data classification | Yes | Public / Internal / Confidential (never Restricted unless a specific use case is approved) |
| Linked use case | No | Register ID, if part of an approved use case |
| Inputs required | Yes | What the user provides |
| Prompt text | Yes | With [placeholders] |
| Example output (sanitised) | Recommended | Shows what good looks like |
| What to check | Yes | Verification steps for the user |
| Known limitations | Yes | Where it fails or needs care |
| Author | Yes | Name |
| Reviewer and date | Yes | Name, date |
| Status | Yes | Draft / Approved / Needs retest / Retired |
| Version | Yes | e.g. 1.2 |
| Next review | Yes | Date |
| Feedback / ratings | No | Users' comments |

## Entry template

Copy for each new prompt.

```markdown
### [ID]: [Title]

| | |
|---|---|
| Purpose | [ ] |
| Business area / tags | [ ] |
| Task type | [ ] |
| Tools tested with | [tool, date] |
| Max data classification | [Public / Internal / Confidential] |
| Linked use case | [UC-xxx or none] |
| Status / version | [Approved, v1.0] |
| Author / reviewer | [name] / [name, date] |
| Next review | [date] |

**Inputs required:** [ ]

**Prompt:**

> [Prompt text with [placeholders]]

**What to check:**
- [ ]

**Known limitations:**
- [ ]
```

## Review and approval process

| Step | Who | What they check |
|---|---|---|
| 1. Draft | Any user | Prompt works for them on realistic (permitted) inputs; metadata complete |
| 2. Peer test | Champion or colleague in the same area | Works for someone else; placeholders are clear; output quality acceptable on at least [3] varied inputs |
| 3. Safety review | Champion with [data protection / risk] guidance | Data classification correct; "what to check" adequate; no prohibited use; no instructions that bypass controls |
| 4. Approve | [Library owner / area lead] | Fits library; not a duplicate; status set to Approved |
| 5. Publish | Library owner | Added with version and review date; announced if useful |

**Fast track:** Low-risk prompts (Public or Internal data, internal outputs) can combine steps 2–4 with a single champion review.

**Higher-risk prompts:** Prompts that produce external content, or are part of a Medium- or High-risk use case, should be reviewed by the use case owner and tested against the use case's test set.

## Maintenance

| Trigger | Action |
|---|---|
| Scheduled review date | Retest; update or retire |
| Tool or model change announced | Mark affected prompts "Needs retest"; retest the most-used first |
| User reports a problem | Investigate; fix or mark "Needs retest" |
| Policy change | Review data classifications and checks |
| Not used for [6] months | Consider retiring |

## Example entries

> These examples are tool-agnostic and illustrative. Test them in your own tools before approving them for your library.

### PL-GEN-001: Summarise a long document for a busy reader

| | |
|---|---|
| Purpose | Produce a short, structured summary of a long internal document |
| Business area / tags | General; summarising |
| Task type | Summarise |
| Tools tested with | [tool, date] |
| Max data classification | Internal (Confidential only in tools approved for Confidential) |
| Linked use case | UC-001 (fictional) |
| Status / version | [Approved, v1.0] |
| Author / reviewer | [ ] / [ ] |
| Next review | [ ] |

**Inputs required:** the document (pasted or attached); the intended reader; the length you want.

**Prompt:**

> You are helping me brief [reader, e.g. a director with five minutes]. Summarise the attached document in no more than [200] words. Use these headings: Purpose; Key points (up to five bullets); Decisions or actions needed; Open questions. Use only information in the document. If something important is unclear or missing, say so under Open questions rather than guessing. Quote section numbers for each key point so I can check them.

**What to check:**

- Each key point matches the cited section.
- Nothing important has been left out (skim the headings of the original).
- No information has been added that is not in the document.

**Known limitations:**

- May miss content in tables, images or appendices.
- Very long documents may exceed what the tool can process at once; check whether the whole document was read.

### PL-CS-002: Draft a reply to a customer enquiry

| | |
|---|---|
| Purpose | Draft a first reply to a routine customer enquiry for a staff member to edit and send |
| Business area / tags | Customer service; drafting |
| Task type | Draft |
| Tools tested with | [tool, date] |
| Max data classification | Confidential, approved business tool only |
| Linked use case | UC-002 (fictional) |
| Status / version | [Approved, v1.1] |
| Author / reviewer | [ ] / [ ] |
| Next review | [ ] |

**Inputs required:** the enquiry with unnecessary personal details removed; the relevant policy extract; tone guidance.

**Prompt:**

> Draft a reply to the customer enquiry below. Use a [warm, plain-English] tone and keep it under [150] words. Base any statement about our policy only on the policy extract provided; if the extract does not answer the question, say in a note to me (not in the reply) what is missing. Do not promise refunds, compensation or timescales unless the policy extract states them. End with [standard sign-off].
>
> Enquiry: [paste]
>
> Policy extract: [paste]

**What to check:**

- Every policy statement matches the extract.
- No promises beyond policy.
- Customer's question is actually answered.
- Tone is appropriate; personal details are correct.
- The text in the enquiry has not caused the draft to include odd instructions or content (a sign of prompt injection).

**Known limitations:**

- Cannot see the customer's history unless provided.
- May sound generic; personalise before sending.

### PL-GEN-003: Critique my draft

| | |
|---|---|
| Purpose | Get structured feedback on your own draft before sending it for review |
| Business area / tags | General; reviewing |
| Task type | Review |
| Tools tested with | [tool, date] |
| Max data classification | Internal |
| Linked use case | None |
| Status / version | [Approved, v1.0] |
| Author / reviewer | [ ] / [ ] |
| Next review | [ ] |

**Inputs required:** your draft; its audience and purpose.

**Prompt:**

> Act as a critical reviewer. My draft below is for [audience] and its purpose is [purpose]. Identify: (1) the three most important weaknesses in argument or structure; (2) any claims that need evidence or a source; (3) places where the audience may be confused; (4) anything that could be misread or cause offence. Do not rewrite the draft. Be specific and refer to paragraph numbers.
>
> [paste draft]

**What to check:**

- Use the feedback as suggestions; you decide what to change.
- If it flags a factual problem, verify it yourself; the tool may be wrong.

**Known limitations:**

- May give generic feedback; ask follow-up questions on specific points.
- Does not know your organisation's context unless you provide it.

### PL-DATA-004: Explain a spreadsheet formula or query

| | |
|---|---|
| Purpose | Get a plain-English explanation of a formula, SQL query or script |
| Business area / tags | Data and analytics; finance |
| Task type | Analyse |
| Tools tested with | [tool, date] |
| Max data classification | Internal (share the formula or query, not the underlying data) |
| Linked use case | None |
| Status / version | [Approved, v1.0] |
| Author / reviewer | [ ] / [ ] |
| Next review | [ ] |

**Inputs required:** the formula or query; what it is supposed to do.

**Prompt:**

> Explain step by step what the following [formula / SQL query / script] does, in plain English, for someone who [is not a specialist]. Then tell me whether it does what I intend, which is: [intention]. List any edge cases where it could give a wrong or unexpected result (for example blanks, duplicates, dates, division by zero).
>
> [paste formula or query]

**What to check:**

- Test the explanation against a few known examples in the real data.
- Do not apply suggested changes without testing them.

**Known limitations:**

- Cannot see your data, so cannot confirm results; may misread unusual functions.

## Related

- [Acceptable use policy](acceptable-use-policy.md)
- [Training plan](training-plan-template.md) (module F5, using tools well)
- [Everyday users pathway](../docs/pathways/everyday-users.md)
- [Video script 03: safe everyday use](../videos/scripts/03-safe-everyday-use.md)

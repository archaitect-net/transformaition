# Data teams pathway

> **Who this is for:** Data engineers, analysts, BI and reporting developers, data scientists, data architects, data stewards and data governance leads.
> **Last reviewed:** 2026-10

Most valuable organisational uses of AI tools depend on data: the documents an assistant searches, the tables an analytics assistant queries, the records an agent updates. Data teams therefore decide much of what AI can safely and usefully do. This pathway covers data readiness, retrieval-augmented generation (RAG), data governance and access control, quality and lineage, and AI assistants for BI and analytics. It also covers AI as a tool for data work itself.

## What AI adoption means for data teams

- **Data quality becomes visible quickly.** An assistant answering from an outdated policy, a duplicate document or a mislabelled field will repeat the error fluently and at scale.
- **Access control moves to the centre.** Assistants and RAG systems can surface content to people who technically have access but should not see it. Permissions that were "good enough" when content was hard to find may not be good enough when AI makes it easy.
- **Unstructured data matters as much as structured.** Documents, emails, wikis and transcripts become sources that need ownership, classification, freshness and retention, not just tables.
- **Natural-language analytics changes who queries data.** Assistants that turn questions into queries or charts widen access, but can produce plausible, wrong answers if the semantic layer, definitions and documentation are weak.
- **Data protection obligations apply.** Processing personal data with AI tools, including for analytics, typically needs a lawful basis, transparency and, for higher-risk uses, a data protection impact assessment (DPIA); the UK ICO publishes guidance on applying data protection law to AI [2]. See [data protection](../governance/data-protection.md).

## Your key responsibilities and decisions

### Data readiness

Use the [data readiness](../../assessments/data-readiness.md) assessment for each use case. Core questions:

| Dimension | Question |
|---|---|
| Availability | Does the data the use case needs exist, and can the AI tool reach it? |
| Ownership | Is there a named owner who can approve its use and vouch for it? |
| Quality | Is it accurate, complete, consistent, deduplicated and current? |
| Classification | Is it labelled for sensitivity, including personal and special category data? |
| Access control | Are permissions correct at the level of individual documents, rows or columns? |
| Documentation | Are definitions, metrics and business rules written down and accessible to the tool? |
| Lawfulness | Is there a lawful basis and appropriate transparency for this use? |
| Retention | Is outdated or superseded content removed or flagged? |

### Retrieval-augmented generation (RAG)

RAG retrieves relevant passages from your content and passes them to a model so answers draw on that content. It is the most common way to ground AI tools in organisational knowledge.

| Design choice | Considerations |
|---|---|
| **Source selection** | Include authoritative, owned, current sources. Exclude drafts, duplicates and superseded versions |
| **Chunking** | How documents are split affects what is retrieved. Respect document structure (headings, tables) |
| **Metadata** | Attach source, owner, date, version and sensitivity to every chunk, for filtering and citation |
| **Retrieval method** | Semantic (embedding) search, keyword search, or hybrid. Hybrid often helps with codes, names and exact terms |
| **Access control** | Filter by the user's permissions at retrieval time. Never rely on the model to withhold content it has been given |
| **Freshness** | Re-index on change; remove deleted content promptly |
| **Citations** | Show users which sources were used so they can verify |
| **Evaluation** | Measure retrieval quality (did it find the right passages?) separately from answer quality (did it use them correctly?) |

Many suite-embedded assistants perform retrieval over your files automatically. The same principles apply even if you do not build the pipeline yourself: the quality and permissions of the underlying content determine the quality and safety of the answers.

### Data governance

- **Extend the data catalogue** to cover unstructured sources, vector stores and AI-generated datasets.
- **Classify and label** sensitive content so tools can respect it.
- **Record AI use of data** in your record of processing activities and [use case register](../../toolkits/use-case-register-template.md).
- **Control vector stores** like any other data store: access control, encryption, retention and tenant separation. The OWASP Top 10 for LLM Applications lists vector and embedding weaknesses as a distinct risk category [1].
- **Govern AI-generated data**: label synthetic or AI-generated content so it is not later mistaken for authoritative source data.

### Quality and lineage

- Record lineage from source to index to answer, so that when an answer is wrong you can trace why.
- Monitor source freshness, ingestion failures and duplicate rates.
- Set up feedback loops: users flagging wrong answers should reach the content owner, not just the AI team.

### BI and analytics assistants

Assistants that answer questions in natural language, write queries, build visuals or summarise dashboards depend heavily on what sits beneath them.

| Enabler | Why it matters |
|---|---|
| A well-modelled semantic layer with clear names | Assistants rely on table, column and measure names to infer meaning |
| Documented metric definitions | Prevents the assistant inventing its own definition of "active customer" or "revenue" |
| Certified or endorsed datasets | Lets you direct assistants to trusted data |
| Row- and column-level security | Ensures users only see data they are entitled to |
| Visible generated query or logic | Lets users and analysts verify how an answer was produced |
| Test questions with known answers | Allows evaluation before release and after model or data changes |

Analysts should treat assistant-generated queries and calculations as drafts to verify, particularly for figures that will be published or used in decisions.

### AI for data work

Coding and chat assistants can help write SQL, transformation code, documentation, data quality rules and tests. Apply the same review and testing standards as for any code (see the [developers pathway](developers.md)), and keep personal and confidential data out of prompts unless the tool and use have been approved for that data.

## Questions you should be asking

- For each AI use case, which data does it depend on, who owns it, and is it fit for this purpose?
- If an assistant were switched on across our document stores today, what would it surface that it should not?
- How do we keep the AI's view of our content current when documents change or are deleted?
- How will we know an answer is wrong, and trace why?
- Are our metric definitions documented well enough for a machine to use correctly?
- Does this use of personal data need a DPIA?

## Your reading route

1. **Foundations.** Read [what are AI tools?](../foundations/what-are-ai-tools.md) (especially RAG and tool use) and [capabilities and limitations](../foundations/capabilities-and-limitations.md) (hallucination, context limits and bias).
2. **Assess data readiness.** Use the [data readiness](../../assessments/data-readiness.md) assessment, and contribute the data sections of [organisational readiness](../../assessments/organisational-readiness.md).
3. **Governance.** Read [data protection](../governance/data-protection.md), [security](../governance/security.md) and [intellectual property](../governance/intellectual-property.md).
4. **Prioritise realistically.** Help score feasibility in [use case prioritisation](../../assessments/use-case-prioritisation.md). Data issues are a leading reason use cases are harder than expected.
5. **Select and implement.** Read [Select](../lifecycle/03-select.md) and the relevant [tool guides](../tools/tool-guides/README.md), including [cloud AI platforms](../tools/tool-guides/cloud-ai-platforms.md).
6. **Pilot with evaluation.** Read [Pilot](../lifecycle/04-pilot.md). Build test question sets with known answers.
7. **Measure.** Read [measuring value](../measurement/measuring-value.md). Data teams often own the baseline data.
8. **Operate.** Read [Operate](../lifecycle/06-operate.md) for freshness monitoring, feedback loops and change control.
9. **Coordinate.** Read the [IT and platform pathway](it-and-platform.md) (permissions and data controls) and [developers pathway](developers.md) (evaluation and security).

## Common pitfalls

| Pitfall | What to do instead |
|---|---|
| Indexing everything "so the AI knows it all" | Curate authoritative, owned, current sources |
| Relying on the model to respect permissions | Enforce access control at retrieval time |
| Evaluating only the final answer | Evaluate retrieval and generation separately |
| Letting superseded documents linger | Retention rules and re-indexing on change |
| Natural-language analytics on an undocumented model | Fix names, definitions and certified datasets first |
| Treating vector stores as a technical detail | Govern them as data stores containing your content |
| No route from user feedback to content owners | Close the loop so errors are fixed at source |

## What good looks like

- Each AI use case has a data readiness assessment, named data owners and a lawful basis recorded.
- Sources for retrieval are curated, labelled, current and permission-filtered at retrieval time.
- Answers show citations; lineage lets you trace an answer to its source.
- Metric definitions and semantic models are documented and certified for assistant use.
- Test question sets with known answers are run before release and after changes.
- Vector stores and AI-generated datasets are in the catalogue and governed.
- In small organisations: a tidy, well-permissioned shared drive with outdated material archived is often the single most effective preparation.

## Sources

1. OWASP GenAI Security Project, *OWASP GenAI LLM Top 10 2026*. https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/
2. Information Commissioner's Office, *Guidance on AI and data protection*. https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/about-this-guidance/

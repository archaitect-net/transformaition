# Contributing to transformAItion

Thank you for helping. This guide is used by organisations to make real decisions, so every contribution is held to the editorial standards below. Please read them before opening a pull request.

## Editorial standards

These standards apply to every page in the repository. Reviewers will check them.

### 1. Neutrality

- **No vendor preference in the core guide.** Everything outside `docs/tools/tool-guides/` must be tool-agnostic. Products may appear only as clearly labelled examples, and where one vendor is named, comparable alternatives should be named too.
- **No recommendations without criteria.** Do not write "use X" or "X is best". Write "if your requirement is A, options that meet it include X and Y; verify B and C".
- **Present trade-offs, not verdicts.** Where practitioners or evidence disagree, state the positions and what each rests on.
- **Tool guides are descriptive, not promotional.** They exist to help people who have *already chosen* a tool to implement it well. They describe capabilities, controls and known limitations, and link to official documentation.

### 2. Evidence and rigour

- **Cite claims that a reader could reasonably doubt.** Statistics, regulatory requirements, product capabilities, research findings and dates all need a source.
- **Prefer primary sources**, in this order:
  1. Legislation, regulators, and standards bodies (e.g. EUR-Lex, ICO, NIST, ISO)
  2. Peer-reviewed research and pre-prints from recognised institutions
  3. Official vendor documentation (for product facts only, never for claims about outcomes)
  4. Reputable secondary analysis (clearly labelled as such)
- **Label the strength of evidence.** Use the evidence labels below when summarising research.
- **Vendor-funded or vendor-authored studies** must be labelled as such.
- **Do not invent figures.** If a number isn't sourced, remove it or turn it into a question the reader should answer for their own context.
- **Distinguish fact, consensus and judgement.** Use plain wording: "The regulation requires…", "Most frameworks recommend…", "One approach is…".

### 3. Currency

AI products and regulation change quickly.

- Every page that contains time-sensitive facts carries a **`Last reviewed`** line at the top, in `YYYY-MM` format.
- Tool guides additionally carry a **`Verify before relying on this`** note and link to the vendor's live documentation.
- Pages unreviewed for 6 months (tool guides) or 12 months (everything else) are treated as stale. Opening an issue with the `stale-content` label is always welcome.

### 4. Context over prescription

Organisations differ in size, sector, jurisdiction, risk appetite and maturity. Write guidance that helps the reader make the decision for their context:

- State the conditions under which guidance applies ("For organisations processing special category data…").
- Give decision criteria, questions and checklists rather than single answers.
- Where scale matters, address small organisations (under 50 people) as well as enterprises.

### 5. Plain English

- Write for an intelligent reader who is not a specialist in the topic.
- Define jargon on first use, or link to the [glossary](docs/foundations/glossary.md).
- Use British English spelling for consistency (organisation, prioritise), except in quoted product names.
- Keep paragraphs short. Use tables for comparisons and checklists for actions.

## Evidence labels

When summarising a study or finding, label it:

| Label | Meaning |
|---|---|
| **Strong** | Multiple independent, peer-reviewed or randomised studies with consistent findings |
| **Moderate** | At least one rigorous study (e.g. randomised or large-sample field study), or several consistent observational studies |
| **Limited** | Single studies, small samples, surveys, or vendor-run studies |
| **Practitioner consensus** | Widely recommended by standards bodies or practitioners, but not empirically tested |

## Page template

```markdown
# Page title

> **Who this is for:** …
> **Last reviewed:** YYYY-MM

One-paragraph summary of what the reader will get from this page.

## Section
…

## Sources
1. Author/organisation, *Title*, year. URL
```

## How to contribute

1. **Small fixes** (typos, broken links, updated facts with a source): open a pull request directly.
2. **New pages or significant changes:** open an issue first using the *Content proposal* template so the scope can be agreed.
3. **Tool guides:** use [`docs/tools/tool-guides/_template.md`](docs/tools/tool-guides/_template.md). New guides must cover every section of the template.
4. **Videos:** see [`videos/README.md`](videos/README.md) for the inclusion criteria.

### Pull request checklist

- [ ] Claims a reader could doubt are cited
- [ ] No unlabelled vendor preference outside `docs/tools/tool-guides/`
- [ ] `Last reviewed` updated on any page with changed facts
- [ ] New pages are linked from the relevant index or pathway
- [ ] Markdown lint and link check pass

## Conflicts of interest

If you work for, or are paid by, a vendor whose product you are writing about, say so in your pull request. You are still welcome to contribute — disclosure lets reviewers check neutrality.

## Licence

By contributing, you agree that your contributions will be licensed under the repository's licences: [CC BY 4.0](LICENSE) for written content and [MIT](LICENSE-CODE) for code and scripts.

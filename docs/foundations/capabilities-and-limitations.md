# Capabilities and limitations

> **Who this is for:** Everyone. Essential before choosing use cases, writing policy or training staff.
> **Last reviewed:** 2026-10

Generative AI tools are very good at some tasks and unreliable at others, and the boundary between the two is uneven and hard to see in advance. This page explains the main limitations (hallucination, non-determinism, knowledge cutoffs, context limits, bias and prompt injection), why each happens, what it means in practice, and how to mitigate it. It ends with a practical test for whether a task suits these tools. Limitations change as products improve, but the underlying causes described here are properties of how large language models work, so plan for them rather than assume they have been solved.

## The core idea: a jagged frontier

A field experiment with consultants found that on tasks inside the AI's capability, people using it produced substantially better work faster, but on a task just outside it they were 19 percentage points less likely to get the right answer than people working without AI [1]. The researchers called this boundary a "jagged frontier": tasks that look similarly difficult to a person can sit on different sides of it. See [evidence on impact](evidence-on-impact.md) for detail.

Two consequences follow:

1. You cannot judge suitability by how hard a task feels. You have to test it.
2. Confident, fluent output is not a signal of correctness. The tool sounds the same whether it is right or wrong.

## What these tools do well

Practitioner consensus and the task-level evidence suggest current tools are generally strong at:

| Strength | Examples | Notes |
|---|---|---|
| Drafting and rewriting text | First drafts, changing tone, shortening, translating register | Strong evidence of time savings on writing tasks [2] |
| Summarising supplied material | Meeting notes, long documents, email threads | Works best when the source is supplied; check for omissions |
| Transforming structure | Turning notes into tables, extracting fields, reformatting | Verify on a sample |
| Explaining and tutoring | Explaining a concept, a piece of code or a regulation in plain language | Can be wrong about specifics; check against the source |
| Generating options | Brainstorming, alternative phrasings, test cases, counter-arguments | Low cost of error, high value of variety |
| Writing and explaining code | Boilerplate, tests, small functions, unfamiliar languages | Evidence is mixed for experts in complex codebases [3] |
| Classification and triage | Routing tickets, tagging documents, sentiment | Needs evaluation against labelled examples |

## Limitations

### 1. Hallucination (confabulation)

**What it is.** The tool produces content that is fluent and plausible but false: invented facts, citations, case law, statistics, quotes or code functions. NIST's Generative AI Profile calls this "confabulation" and lists it as one of twelve risks specific to or worsened by generative AI [4].

**Why it happens.** Language models generate text by predicting likely continuations, not by retrieving verified facts. Researchers have also argued that common training and evaluation practices reward guessing over admitting uncertainty, because benchmarks typically score a confident guess higher than "I don't know" [5].

**How common.** It varies widely by tool, task and domain, so beware any single headline rate. One study of general-purpose models answering specific questions about US federal court cases found hallucination rates between 69% and 88% [6]. In England, the High Court addressed the misuse of AI-generated fictitious case citations by lawyers in a 2025 judgment, *Ayinde v London Borough of Haringey* [7].

**Mitigations.**

- Ground the tool in trusted sources (supply the documents, or use retrieval; see [glossary: RAG](glossary.md#r)), and require it to cite them.
- Check every specific factual claim, citation, figure and quote against the original source before relying on it.
- Use tools for tasks where you can verify the output more cheaply than producing it yourself.
- Treat hallucination as a residual risk to manage, not a bug to wait for vendors to fix.

**Evidence label:** Strong that hallucination occurs across models; rates are context-dependent.

### 2. Non-determinism

**What it is.** The same prompt can produce different outputs on different occasions.

**Why it happens.** Most tools deliberately sample from a range of likely next words (controlled by settings such as "temperature") to make output varied. Even with sampling minimised, outputs can still vary because of how calculations are batched and executed on hardware; one 2025 technical analysis attributes much of this to inference running differently depending on server load [8]. Vendors also update models behind the same product name.

**Why it matters.** Testing a prompt once tells you little. Results that matter for audit, fairness or consistency (such as screening, grading or decisions about people) need repeated testing and controls.

**Mitigations.** Evaluate on many runs and many examples; pin model versions where your platform allows; record the model version, prompt and output for consequential uses; design processes so that variation is caught by human review.

### 3. Knowledge cutoff and currency

**What it is.** A model's built-in knowledge stops at the date its training data was collected. It may not know about recent events, product changes, regulation or prices, and may not know that it does not know.

**Mitigations.** Use tools with web search or connections to your own current documents when currency matters, and check the date and source of any time-sensitive claim. Note that a tool with search can still misread or misattribute what it finds.

### 4. Context limits

**What it is.** A model can only consider a limited amount of text at once (its "context window"). Content beyond that limit is truncated or summarised. Even within the limit, models do not attend to everything equally: research found that performance was often best when relevant information was at the beginning or end of a long input, and worse when it was in the middle [9].

**Why it matters.** "Summarise these 400 pages" may silently miss material. Long conversations can drift as earlier instructions lose influence.

**Mitigations.** Break large tasks into parts; put key instructions and material near the start or end; start fresh conversations for new tasks; spot-check summaries of long documents against the source.

### 5. Bias

**What it is.** Models learn patterns from human-produced data, including stereotypes and imbalances, and can reproduce them in outputs about people. A study published in *Nature* found that language models showed covert prejudice against speakers of African American English (for example in hypothetical job and criminal-justice decisions) even where overt statements were positive, and that common alignment techniques could mask rather than remove it [10].

**Why it matters.** Any use that affects people, such as recruitment, performance management, customer eligibility or access to services, carries legal and ethical risk. Some such uses are classed as high-risk under the EU AI Act; see [regulation overview](../governance/regulation-overview.md).

**Mitigations.** Do not use general-purpose tools to make or substantially inform decisions about individuals without a specific risk assessment ([AI risk assessment](../../assessments/ai-risk-assessment.md)); test outputs across groups; keep a human accountable for decisions; involve your data protection and equality specialists.

### 6. Prompt injection

**What it is.** Instructions hidden in content the tool processes (a web page, email, document or file) can override the user's or developer's instructions. "Indirect" prompt injection, where the malicious instruction arrives through retrieved content rather than from the user, was demonstrated against real applications in 2023 research [11]. It is ranked first in the OWASP Top 10 for LLM Applications [12].

**Why it happens.** Language models process instructions and data as the same stream of text and cannot reliably tell them apart. The UK National Cyber Security Centre has warned that, unlike SQL injection, prompt injection may never be fully mitigated, and advises focusing on reducing its likelihood and impact [13].

**Why it matters.** The risk grows with what the tool can access and do. A chat assistant with no tools can at worst give a bad answer. An agent that can read your email, browse the web and send messages could be tricked into leaking data or taking actions.

**Mitigations.** Limit the data and actions available to AI tools (least privilege); require human approval for consequential actions; treat AI output as untrusted input to other systems; monitor and log agent activity. See [security](../governance/security.md).

### 7. Other limitations to know

| Limitation | What to watch for |
|---|---|
| **Sycophancy** | Tools tend to agree with the user and can endorse flawed premises. Ask for critique explicitly, and do not treat agreement as validation. |
| **Weak calculation and counting** | Arithmetic, counting and precise data analysis are error-prone unless the tool runs code or uses a calculator. Check numbers. |
| **Overreliance and deskilling** | Survey evidence links higher trust in AI with less critical thinking [14]; experimental evidence shows unstructured use can impair learning [15]. |
| **Opaque reasoning** | Explanations a model gives of its own reasoning are generated text and may not reflect how it actually produced the answer. |
| **Data handling** | What happens to your inputs depends on the product, contract and settings. See [data protection](../governance/data-protection.md). |
| **Intellectual property** | Ownership of outputs and the risk of reproducing protected material vary by jurisdiction. See [intellectual property](../governance/intellectual-property.md). |

## Is this task a good fit? A practical test

Score a candidate task against these questions. The more "yes" answers, the better the fit. Use the [use case prioritisation](../../assessments/use-case-prioritisation.md) assessment for a fuller scoring.

| Question | Why it matters |
|---|---|
| Is the output easier to check than to produce? | Verification is your main control against hallucination. |
| Is the cost of an undetected error low or recoverable? | Limits harm from the jagged frontier. |
| Is the task mainly about language, structure or pattern rather than precise facts or calculation? | Plays to strengths. |
| Can you supply the source material the tool needs? | Reduces reliance on built-in knowledge. |
| Does the person using it have the expertise to spot a wrong answer? | Evidence shows benefits can reverse when users cannot judge the output [16]. |
| Is no decision about an individual being made by the tool? | Avoids high-risk uses without specific controls. |
| Can the task be tested on realistic examples before rollout? | Lets you find where the frontier lies for you. |

**Worked example.** A small charity wants help replying to supporter emails. Drafting replies from a set of approved answers scores well: the output is quick to check, errors are recoverable, the source material can be supplied and staff know the right answers. Using the same tool to decide which supporters qualify for hardship grants scores poorly: it affects individuals, errors are costly and may not be detected, and bias is a concern. The first can be piloted with light controls; the second should not proceed without a full risk assessment, and may not be appropriate at all.

## Related pages

- [What are AI tools?](what-are-ai-tools.md)
- [Evidence on impact](evidence-on-impact.md)
- [Risk management](../governance/risk-management.md) and [security](../governance/security.md)
- [Acceptable use policy template](../../toolkits/acceptable-use-policy.md)

## Sources

1. Dell'Acqua, F. et al., *Navigating the Jagged Technological Frontier*, Harvard Business School Working Paper 24-013, 2023. https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf
2. Noy, S. and Zhang, W., *Experimental evidence on the productivity effects of generative artificial intelligence*, Science, 2023. https://scale.stanford.edu/publications/experimental-evidence-productivity-effects-generative-artificial-intelligence
3. METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*, 2025. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
4. NIST, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile* (NIST AI 600-1), July 2024. https://doi.org/10.6028/NIST.AI.600-1
5. Kalai, A. T., Nachum, O., Vempala, S. S. and Zhang, E., *Why Language Models Hallucinate*, arXiv 2509.04664, 2025. https://arxiv.org/abs/2509.04664
6. Dahl, M., Magesh, V., Suzgun, M. and Ho, D. E., *Large Legal Fictions: Profiling Legal Hallucinations in Large Language Models*, Journal of Legal Analysis 16, 2024. https://law.stanford.edu/publications/large-legal-fictions-profiling-legal-hallucinations-in-large-language-models
7. High Court of England and Wales, *Ayinde v London Borough of Haringey and Al-Haroun v Qatar National Bank* [2025] EWHC 1383 (Admin), 6 June 2025. https://www.judiciary.uk/judgments/ayinde-v-london-borough-of-haringey-and-al-haroun-v-qatar-national-bank/
8. He, H. (Thinking Machines Lab), *Defeating Nondeterminism in LLM Inference*, September 2025. https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/
9. Liu, N. F. et al., *Lost in the Middle: How Language Models Use Long Contexts*, Transactions of the Association for Computational Linguistics, 2024. https://aclanthology.org/2024.tacl-1.9/
10. Hofmann, V., Kalluri, P. R., Jurafsky, D. and King, S., *AI generates covertly racist decisions about people based on their dialect*, Nature 633, 2024. https://ideas.repec.org/a/nat/nature/v633y2024i8028d10.1038_s41586-024-07856-5.html
11. Greshake, K. et al., *Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*, arXiv 2302.12173, 2023. https://arxiv.org/abs/2302.12173
12. OWASP GenAI Security Project, *OWASP Top 10 for LLM Applications 2026*. https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/
13. National Cyber Security Centre, *Prompt injection is not SQL injection*, December 2025. https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection
14. Lee, H.-P. et al., *The Impact of Generative AI on Critical Thinking*, CHI 2025. https://advait.org/files/lee_2025_ai_critical_thinking_survey.pdf
15. Bastani, H. et al., *Generative AI without guardrails can harm learning: Evidence from high school mathematics*, PNAS 122(26), 2025. https://ideas.repec.org/a/nas/journl/v122y2025pe2422633122.html
16. Otis, N. et al., *The Uneven Impact of Generative AI on Entrepreneurial Performance*, 2024. https://newsroom.haas.berkeley.edu/research/gen-ai-experiment-shows-mixed-results-in-helping-small-businesses-grow/

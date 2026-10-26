# Developers pathway

> **Who this is for:** Software developers, engineers, technical leads and engineering managers who use AI coding tools, build applications on large language models, or build agents.
> **Last reviewed:** 2026-10

Developers meet AI in two ways: as users of AI coding assistants, and as builders of applications and agents that use language models. Each brings its own opportunities and risks. This pathway covers using coding assistants well, building with LLM APIs, evaluating non-deterministic systems, secure development against the OWASP Top 10 for LLM Applications, and designing agents with appropriate limits. It also summarises what the research says about developer productivity, which is more mixed than headline figures suggest.

## What AI adoption means for developers

### The evidence on coding assistants is mixed

| Study | Finding | Caveat |
|---|---|---|
| Peng et al. (2023) | Developers completed a single JavaScript HTTP server task 55.8% faster with GitHub Copilot [1] | Vendor-authored (Microsoft Research, GitHub); one small greenfield task |
| Cui et al. (2025) | Across three field experiments with 4,867 developers, access to an AI coding assistant increased completed tasks by 26.08%, with larger gains for less experienced developers [2] | Vendor co-authored; task counts are a proxy for output |
| METR (2025) | 16 experienced open-source developers took 19% longer on real tasks in codebases they knew well when AI was allowed, while believing it had sped them up [3] | Small sample; early-2025 tools; METR says results no longer reflect current tools |
| METR (2026) | A larger follow-up suggested speed-ups with late-2025 tools, but confidence intervals included zero and selection effects were severe [4] | METR called it very weak evidence and is redesigning the study |
| DORA (2024, 2025) | Survey data associated AI adoption with lower delivery stability; by 2025, positive association with throughput but continued instability [5][6] | Correlational survey; run by Google |

**Practical reading.** Gains are most reliable on well-specified, self-contained tasks, boilerplate, tests and unfamiliar languages or libraries. Experts working in large, familiar codebases may see little benefit. Faster code generation does not guarantee faster or safer delivery, and perceived speed-ups are unreliable. Measure delivery outcomes, not lines generated. See [evidence on impact](../foundations/evidence-on-impact.md).

### Building with LLMs is a different kind of engineering

- Outputs are **non-deterministic**: the same input can produce different outputs.
- Failures are **semantic**: the system returns well-formed but wrong, unsafe or off-policy content.
- **Instructions and data share one channel**, which creates prompt injection risk.
- **Model behaviour changes** when vendors update models behind the same name.
- **Costs scale with tokens**, and agentic loops can multiply them.

## Your key responsibilities and decisions

### Using coding assistants

| Practice | Why |
|---|---|
| Review all generated code as you would a colleague's pull request | Generated code can be insecure, subtly wrong or reference non-existent packages |
| Keep secrets, credentials and customer data out of prompts and context | Prompts may be logged or retained depending on configuration |
| Check dependencies suggested by AI exist and are the intended packages | Invented package names create a supply chain risk |
| Use organisation-approved tools and tiers | Data handling and IP terms vary by tier |
| Keep tests, static analysis and security scanning in the pipeline | Existing quality gates matter more, not less |
| Be cautious with tools that run commands or edit many files autonomously | Scope them to sandboxes or branches; review diffs |
| Protect learning for junior developers | Use the assistant to explain, not only to produce |

### Building LLM applications

| Decision | Considerations |
|---|---|
| **Model and platform** | Capability on your tasks (measured by your evaluations, not public benchmarks), cost, latency, data handling, residency, availability of version pinning |
| **Architecture** | Plain prompting, retrieval-augmented generation (RAG), tool use, fine-tuning, or agents. Start with the simplest that meets requirements |
| **Prompt and configuration management** | Version prompts, system instructions and model settings alongside code |
| **Observability** | Log inputs, outputs, tool calls, latency and cost, with privacy controls |
| **Human oversight** | Where must a person approve? How are disagreements and errors fed back? |

### Evaluation

Evaluation is to LLM applications what testing is to conventional software.

1. **Define what good looks like** for each task: correctness, groundedness in sources, format, tone, safety, refusal behaviour.
2. **Build a test set** from realistic examples, including edge cases and adversarial inputs. Start with tens of examples and grow it from production failures.
3. **Choose scoring methods**: exact match or programmatic checks where possible; rubric-based human review for subjective qualities; model-based grading only after checking that it agrees with human judgement on a sample.
4. **Run repeatedly**, because outputs vary between runs.
5. **Run in CI** on changes to prompts, models, retrieval or code, and when vendors update models.
6. **Monitor in production**: sample outputs for review, track user feedback, watch for drift.

### Secure development: OWASP Top 10 for LLM Applications

The OWASP GenAI Security Project publishes a Top 10 for LLM Applications. The current edition at the time of review is the **2026** edition, released in August to September 2026 [7][8]. According to secondary analysis of the 2026 edition, the categories, in rank order, are as follows [9]. Check the OWASP site for the authoritative text and identifiers.

| Rank | Risk | What to do (summary) |
|---|---|---|
| 1 | Prompt injection | Treat all external content as untrusted; separate and label untrusted input; limit tools and permissions; require approval for consequential actions |
| 2 | Sensitive information disclosure | Minimise data in context; enforce access control before retrieval, not after generation; filter outputs |
| 3 | Excessive agency | Least privilege for tools; narrow, purpose-built tools rather than general ones; human approval for high-impact actions |
| 4 | Supply chain | Vet models, datasets, plugins and packages; check provenance; prefer safe serialisation formats |
| 5 | Data and model poisoning | Control and validate training, fine-tuning and retrieval data sources |
| 6 | Unbounded consumption | Rate limits, quotas, timeouts, step limits for agents, cost alerts |
| 7 | Misinformation | Ground answers in sources; show citations; design for verification; communicate limitations |
| 8 | Hidden context exposure (formerly system prompt leakage) | Do not put secrets or security controls in prompts; assume system prompts and configuration can be extracted |
| 9 | Vector and embedding weaknesses | Apply access control to vector stores; separate tenants; validate ingested content |
| 10 | Improper output handling | Treat model output as untrusted input to downstream systems; encode, validate and sanitise |

The UK NCSC advises that prompt injection cannot be "fixed" in the way SQL injection can, so design to limit its impact [10]. Also see the joint NCSC and CISA [guidelines for secure AI system development](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development) [11] and this guide's [security](../governance/security.md) page.

### Agents

Agents combine a model, tools and a loop with some autonomy. Design principles that most security guidance converges on (practitioner consensus):

- **Least privilege**: give each agent the narrowest tools and scopes it needs.
- **Separate read from write**: actions that change data, spend money or communicate externally need stronger controls.
- **Human approval for consequential or irreversible actions.**
- **Bound the loop**: step limits, time limits, budget limits.
- **Isolate execution**: sandboxes or containers for code execution and browsing.
- **Log everything**: every tool call, input and output, for audit and debugging.
- **Assume compromise**: if an agent reads untrusted content, assume it can be manipulated and design so that the worst case is acceptable.
- **Identity**: decide whether the agent acts as the user, as a service identity, or with delegated scopes, and make that visible.

## Questions you should be asking

- Which coding tools and tiers are approved, and what happens to our code and prompts?
- How will we know whether AI tools are improving delivery, not just output volume?
- For each LLM feature: what is our evaluation set, and what score is good enough to ship?
- What can this application or agent do if an attacker controls part of its input?
- Which model version are we on, and how will we know if it changes?
- What is the cost per transaction, and what stops runaway usage?
- Who reviews AI-generated code for security?

## Your reading route

1. **Foundations.** Read [what are AI tools?](../foundations/what-are-ai-tools.md) and [capabilities and limitations](../foundations/capabilities-and-limitations.md), then the software section of [evidence on impact](../foundations/evidence-on-impact.md#software-development-three-contrasting-results).
2. **Know the rules.** Read your organisation's AI policy, or the [AI policy template](../../toolkits/ai-policy-template.md) and [acceptable use policy](../../toolkits/acceptable-use-policy.md).
3. **Use coding assistants well.** Read the [GitHub Copilot tool guide](../tools/tool-guides/github-copilot.md) or the guide for whichever tool you use, and [tool categories](../tools/tool-categories.md).
4. **Secure what you build.** Read [security](../governance/security.md), [data protection](../governance/data-protection.md) and [intellectual property](../governance/intellectual-property.md).
5. **Choose a platform.** Read [choosing tools](../tools/choosing-tools.md), [cloud AI platforms](../tools/tool-guides/cloud-ai-platforms.md) and [open-weight models](../tools/tool-guides/open-weight-models.md).
6. **Assess risk.** Complete an [AI risk assessment](../../assessments/ai-risk-assessment.md) for any application that affects customers or individuals, and check [data readiness](../../assessments/data-readiness.md) for RAG use cases.
7. **Pilot and measure.** Read [Pilot](../lifecycle/04-pilot.md) and [measuring value](../measurement/measuring-value.md), using delivery metrics rather than code volume.
8. **Operate.** Read [Operate](../lifecycle/06-operate.md) for monitoring, model updates and incident response.
9. **Work with data teams.** Read the [data teams pathway](data-teams.md) on retrieval and data quality.

## Common pitfalls

| Pitfall | What to do instead |
|---|---|
| Accepting generated code without review | Review, test and scan as for any code |
| Measuring productivity by suggestions accepted or lines generated | Measure delivery throughput, stability and defects |
| Shipping an LLM feature tested on a handful of examples | Build an evaluation set; run it repeatedly and in CI |
| Putting secrets or access rules in the system prompt | Enforce security in code and infrastructure |
| Giving agents broad, general-purpose tools | Narrow tools, least privilege, approvals, limits |
| Trusting model output in downstream systems | Validate and encode output like any untrusted input |
| Not pinning or tracking model versions | Pin where possible; re-run evaluations on change |
| Ignoring cost until the bill arrives | Budget, quota and alert from day one |

## What good looks like

- Approved coding tools at business tier, with clear rules on secrets and data.
- Quality gates (review, tests, scanning) unchanged or strengthened.
- Every LLM application has an evaluation set, a target, and automated runs on change.
- Threat modelling uses the OWASP Top 10 for LLM Applications.
- Agents operate with least privilege, bounded loops, human approval for consequential actions, and full logging.
- Model versions, prompts and configuration are version-controlled.
- Delivery metrics are tracked before and after adoption, and results are shared honestly.
- In small teams: an agreed list of tools, a rule on secrets, a review habit, and a simple evaluation spreadsheet for any LLM feature.

## Sources

1. Peng, S., Kalliamvakou, E., Cihon, P. and Demirer, M., *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*, arXiv 2302.06590, 2023. https://arxiv.org/abs/2302.06590
2. Cui, Z. et al., *The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers*, 2025. https://papers.ssrn.com/abstract=4945566
3. METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*, July 2025. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
4. METR, *We are Changing our Developer Productivity Experiment Design*, February 2026. https://metr.org/blog/2026-02-24-uplift-update/
5. RedMonk, summary of DORA *Accelerate State of DevOps Report 2024* (secondary), November 2024. https://redmonk.com/rstephens/2024/11/26/dora2024/
6. DORA, *State of AI-assisted Software Development 2025*. https://dora.dev/research/ai
7. OWASP GenAI Security Project, *OWASP GenAI LLM Top 10 2026*. https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/
8. OWASP GenAI Security Project, *OWASP GenAI Security Project unveils 2026 Top 10 for LLM Applications*, September 2026. https://genai.owasp.org/2026/09/01/owasp-genai-security-project-unveils-2026-top-10-for-llm-applications-new-agent-control-standard-and-sponsors-as-community-tops-30000-members/
9. Cloud Security Alliance, *OWASP's 2026 LLM Top 10: Incident Data Meets Judgment* (secondary analysis). https://labs.cloudsecurityalliance.org/research/csa-research-note-owasp-llm-top10-2026-incident-weighted-202/
10. National Cyber Security Centre, *Prompt injection is not SQL injection*, December 2025. https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection
11. National Cyber Security Centre, CISA and partners, *Guidelines for secure AI system development*, November 2023. https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development

# AI tool categories

> **Who this is for:** Leaders, IT and platform teams, procurement, security and data protection staff, and anyone framing options before talking to vendors.
> **Last reviewed:** 2026-10

AI tools fall into a small number of categories that differ in who uses them, where they run, how data flows, and how they are paid for. Those differences usually matter more to risk, cost and fit than the differences between brands within a category. This page describes eight categories neutrally: what each is suited for, typical deployment, data-flow implications, cost model types, and several example products. Use it to decide which category (or combination) fits a use case before you compare products with the method in [choosing tools](choosing-tools.md).

> **About the examples.** Products are named only as examples, several per category, in no order of preference. Names and packaging change often; check the vendor's current documentation. Inclusion is not endorsement, and omission is not exclusion.

## The categories at a glance

| # | Category | Primary users | Where it runs | Main data question | Typical cost model |
|---|---|---|---|---|---|
| 1 | General-purpose assistants | Everyone | Vendor cloud (SaaS) | What staff paste or upload, and what the vendor does with it | Per seat, sometimes plus usage |
| 2 | Assistants embedded in productivity suites | Everyone in that suite | Suite vendor's cloud | What the assistant can reach through existing permissions | Add-on per seat, or bundled in the suite |
| 3 | Coding assistants | Developers | IDE/terminal plus vendor cloud | Source code and secrets sent as context; what agents can change | Per seat plus usage allowances |
| 4 | Agents and automation | Business and technical builders | SaaS, low-code platforms or your own cloud | What the agent can act on, with whose permissions | Per run, per action, per message or usage |
| 5 | Cloud AI platforms and model APIs | Developers, data teams | Hyperscaler or model vendor cloud, in your account | Region, retention and logging settings you configure | Pay per token or reserved capacity |
| 6 | Open-weight models, self-hosted | ML and platform engineers | Your infrastructure or private cloud | Entirely under your control, and your responsibility | Infrastructure and staff time |
| 7 | Domain-specific tools | Specialist functions (legal, finance, HR, health, customer service) | Usually vendor SaaS, often built on a third-party model | Sector-sensitive data and the vendor's own sub-processors | Per seat, per case or per transaction |
| 8 | AI features in existing SaaS | Users of that product | Inside the SaaS product you already use | Whether the feature changes terms you already agreed | Bundled, add-on, or credits |

## 1. General-purpose assistants

**What they are.** Chat-based assistants for writing, summarising, analysis, research and question answering. Business editions add an admin console, single sign-on and organisational data terms. Many now connect to email, files and other systems, and some can run multi-step tasks.

**Suited for.** Broad, varied knowledge work across many roles; drafting and editing; analysing uploaded documents and data; exploring ideas. Useful as a first, organisation-wide tool where needs are not yet well defined.

**Typical deployment.** SaaS, accessed through browser, desktop and mobile apps. Identity through your identity provider on business tiers. Connectors to other systems are optional and usually admin-controlled.

**Data-flow implications.**

- Prompts, files and connected content are processed in the vendor's cloud. Business and enterprise tiers usually commit not to train on your content by default, but consumer tiers may differ. Confirm which terms apply to the plan you buy.
- Retention of conversations, and who can set it, varies by plan.
- Connectors widen what the assistant can see, so they widen the impact of a misconfiguration.

**Cost model types.** Per user per month, sometimes with usage limits, pooled credits, or usage billed separately at API rates.

**Examples.** ChatGPT (Business and Enterprise plans), Claude (Team and Enterprise plans), the Gemini app within Google Workspace, Microsoft Copilot Chat, and assistants from other model vendors.

## 2. Assistants embedded in productivity suites

**What they are.** AI features built into email, documents, spreadsheets, presentations, meetings and chat, grounded in the content the user can already reach in that suite.

**Suited for.** Organisations standardised on one suite; tasks that depend on internal content (meeting recaps, email triage, drafting from existing documents, finding information across files).

**Typical deployment.** Enabled within your existing tenant, often per user or per group, managed in the suite's admin centre.

**Data-flow implications.**

- The assistant usually respects existing permissions. That means **existing oversharing becomes more visible**: if a sensitive file is shared too broadly, the assistant can surface it to anyone with access. Permission hygiene is a prerequisite.
- Existing controls (sensitivity labels, data loss prevention, retention, eDiscovery) may or may not extend to AI interactions; check feature by feature.
- Data residency commitments for the suite do not automatically cover AI processing. Check the specific terms.

**Cost model types.** Per-user add-on licence, inclusion in higher suite tiers, or a basic tier included with additional capability sold separately.

**Examples.** Microsoft 365 Copilot (licensed as Microsoft Copilot), Gemini in Google Workspace, and AI features in other office and collaboration suites.

## 3. Coding assistants

**What they are.** Tools that suggest code, answer questions about a codebase, review pull requests, and increasingly act as agents that make multi-file changes, run commands and open pull requests.

**Suited for.** Software development, infrastructure-as-code, data engineering and scripting; documentation and test generation; code review support.

**Typical deployment.** IDE extensions, command-line tools, and features in code-hosting platforms; some offer cloud-hosted agents that run in vendor-managed environments.

**Data-flow implications.**

- Source code, file contents and sometimes secrets are sent as context. Exclusion features exist in some products but often have documented gaps.
- Agentic modes can execute commands and modify repositories, so permissions, branch protection and review rules matter as much as data terms.
- Licence and provenance of generated code is an open issue; some products offer filters or references for suggestions that match public code. See [intellectual property](../governance/intellectual-property.md).

**Cost model types.** Per seat per month, with allowances of premium model usage or credits and overage billed by usage; or usage-based through an API.

**Examples.** GitHub Copilot, Claude Code, OpenAI Codex, coding assistants from Google and from IDE vendors, and open-source coding agents that can be pointed at a model API of your choice.

## 4. Agents and automation

**What they are.** Systems that use a model to plan and take actions across tools and data, such as updating records, sending messages or triggering workflows, with varying degrees of human oversight. Ranges from low-code agent builders to developer frameworks.

**Suited for.** Repeatable multi-step processes (triage, routing, data entry, reconciliation), internal help desks, and orchestrating work across systems. Best where the process is well understood and outcomes can be checked.

**Typical deployment.** Low-code builders in SaaS platforms; agent services on cloud platforms; open-source frameworks deployed in your own environment.

**Data-flow implications.**

- The key question shifts from "what can it see?" to "what can it **do**?" Agents act with some identity: a user's delegated permissions, a service account or their own managed identity. Excessive permissions are a primary risk; OWASP lists "excessive agency" in its top 10 risks for LLM applications [1].
- Prompt injection, where instructions hidden in content the agent reads change its behaviour, is a particular risk for agents that read external content [1].
- Logs of actions, approvals and rollbacks become essential controls.

**Cost model types.** Per message, per action, per agent run, consumption credits, or underlying model and infrastructure costs.

**Examples.** Agent services on cloud platforms (Microsoft Foundry Agent Service, Gemini Enterprise Agent Platform's Agent Studio and Agent Development Kit, agent features in Amazon Bedrock), Google Workspace Studio, Microsoft's low-code agent builders, workflow tools with AI steps such as n8n, Zapier and Power Automate, and open-source frameworks such as LangGraph.

## 5. Cloud AI platforms and model APIs

**What they are.** Programmatic access to models, plus tools to build applications: retrieval, evaluation, safety filters, fine-tuning and agent hosting. Offered by hyperscalers and directly by model vendors.

**Suited for.** Building your own applications and integrations; embedding AI in products and internal systems; workloads that need control over region, network, logging and model choice.

**Typical deployment.** Within your cloud account or a vendor developer account, governed by your identity and access management, networking and logging.

**Data-flow implications.**

- You configure much of the data handling: region and cross-region routing, logging, retention modes, encryption keys and private networking. Defaults vary by platform, model and feature, and some features store data even when the base service does not.
- Abuse-monitoring retention and human review terms differ by provider and model; some offer modified or zero retention on approval.
- You carry responsibility for the application you build, including access control, output handling and monitoring.

**Cost model types.** Pay per input and output token; batch discounts; reserved or provisioned throughput; separate charges for storage, retrieval, fine-tuning and hosting.

**Examples.** Microsoft Foundry (including Azure OpenAI), Amazon Bedrock, Google Gemini Enterprise Agent Platform (formerly Vertex AI), and first-party APIs from model vendors such as Anthropic, OpenAI, Google and Mistral.

## 6. Open-weight models, self-hosted

**What they are.** Models whose trained weights are published so you can download and run them on your own hardware or private cloud. Licences range from permissive open-source licences to custom licences with use restrictions.

**Suited for.** Strict data-sovereignty or air-gapped requirements; high, predictable volumes where infrastructure may cost less than per-token pricing; research; fine-tuning for narrow tasks; avoiding dependency on a single vendor.

**Typical deployment.** On-premises GPU servers, private cloud instances, managed hosting of open models on cloud platforms, or local machines for small models.

**Data-flow implications.**

- Data need not leave your environment, but **every control is yours**: patching, access, logging, safety filtering and evaluation.
- Model files are a supply-chain risk; provenance and integrity checks matter.
- Licence terms may restrict use, scale or redistribution.

**Cost model types.** Hardware or cloud compute, storage, power, and specialist staff time; no per-token fee.

**Examples (model families).** Llama (Meta), Gemma (Google), Mistral models, Qwen (Alibaba), DeepSeek, gpt-oss (OpenAI), Phi (Microsoft) and others. See the [open-weight models guide](tool-guides/open-weight-models.md).

## 7. Domain-specific tools

**What they are.** Products built for a particular function or sector, such as contract review, legal research, clinical documentation, customer service, recruitment, finance close or tax. Often built on a third-party foundation model with domain data, workflows and interfaces on top.

**Suited for.** Specialist workflows where domain content, compliance features and integration with sector systems matter more than general flexibility.

**Typical deployment.** SaaS, integrated with sector systems (case management, practice management, electronic health records, CRM, HR systems).

**Data-flow implications.**

- Often handle sensitive or regulated data (health, legal privilege, employment). Sector rules may apply in addition to general data protection law.
- There are usually **two layers** of supplier: the tool vendor and the model provider behind it. Ask which model providers are used, in which regions, and on what terms.
- Some uses may be high-risk under regulation, for example AI used in recruitment or access to essential services. See [regulation overview](../governance/regulation-overview.md).

**Cost model types.** Per seat, per matter or case, per document, per conversation resolved, or enterprise licence.

**Examples.** Legal research and drafting tools from legal publishers and start-ups, AI customer-service platforms, ambient clinical documentation tools, and AI features in recruitment platforms. Because this category is broad, names are best gathered from your sector's procurement frameworks and peers.

## 8. AI features embedded in existing SaaS

**What they are.** AI capabilities switched on inside software you already use: CRM, service desk, design, project management, analytics, HR and finance systems.

**Suited for.** Incremental gains in existing workflows with low change-management overhead; organisations that prefer not to add new vendors.

**Typical deployment.** Toggled in the product's admin settings, sometimes on by default after an update.

**Data-flow implications.**

- Features may introduce **new sub-processors** (often a model provider) and new data flows under terms that differ from your original contract. Check update notices and sub-processor lists.
- Some features are enabled by default. Inventory what is active.
- Data may be used for product improvement unless you opt out; check.

**Cost model types.** Bundled into existing tiers, sold as an add-on, or charged by credits or consumption.

**Examples.** AI features in Salesforce, ServiceNow, Atlassian, Adobe, Notion, Zoom, Slack, Workday, Microsoft Power BI and Tableau, among many others.

## Choosing between categories

Most organisations end up with more than one category. These questions help decide which to start with:

| Question | If the answer is yes, consider |
|---|---|
| Do many staff need help with varied, everyday knowledge work? | 1 or 2 |
| Is most of the relevant content already in one productivity suite, with tidy permissions? | 2 |
| Is the main use case software development? | 3 |
| Is there a well-defined, repeatable process with checkable outcomes? | 4 |
| Do you need to build AI into your own product or systems? | 5 |
| Must data stay entirely within your own infrastructure, or are volumes very high and predictable? | 6 (or 5 with strict regional and retention settings) |
| Is the workflow specialist, regulated or sector-specific? | 7 |
| Is the need small and inside a system you already use? | 8 |

**Questions that cut across every category:**

- Does the vendor train on our data by default on the plan we will buy?
- Where is data processed and stored, including during peak load or for abuse monitoring?
- What can administrators control, log and export?
- What happens to our data, configurations and outputs if we leave?

## Related pages

- [Choosing tools](choosing-tools.md)
- [Tool guides](tool-guides/README.md)
- [What are AI tools?](../foundations/what-are-ai-tools.md)
- [Capabilities and limitations](../foundations/capabilities-and-limitations.md)
- [Security](../governance/security.md)

## Sources

1. OWASP GenAI Security Project, *OWASP Top 10 for LLM Applications 2026*. https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/

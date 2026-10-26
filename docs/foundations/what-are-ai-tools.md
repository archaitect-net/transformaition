# What are AI tools?

> **Who this is for:** Anyone who needs a clear, non-technical grounding before making decisions about AI tools, including leaders, managers, policy owners and new users.
> **Last reviewed:** 2026-10

"AI tools" covers a wide range of products, from a chat assistant in a web browser to an autonomous agent that can act inside your business systems. This page sets out the main types of tool, explains in plain language how the large language models behind most of them work, and describes the ways they can be deployed. Understanding these distinctions matters because each type carries different benefits, risks, costs and governance needs, and a policy or business case written for one type often does not fit another.

## What "AI" means in this guide

Artificial intelligence is a broad field. Organisations have used forms of it for decades, for example in fraud detection, demand forecasting and spam filtering. These are often called *predictive* or *traditional machine learning* systems: they are trained for one narrow task and output a score, label or forecast.

This guide focuses mainly on **generative AI**: systems that produce new content (text, code, images, audio or video) in response to instructions written in ordinary language. Most generative AI tools used at work are built on **large language models (LLMs)**. Where guidance also applies to other forms of AI, the page says so. Definitions of terms in bold are in the [glossary](glossary.md).

## Types of AI tool

The categories below overlap, and many products now combine several. Classify a tool by what it can *access* and what it can *do*, because those two factors drive most of the risk.

| Type | What it is | Typical examples of use | What it can access | Key governance questions |
|---|---|---|---|---|
| **General-purpose assistant** | A chat interface to an LLM, used through a browser, desktop or mobile app | Drafting, summarising, research, brainstorming, analysis of uploaded files | What the user types or uploads; optionally web search and connected apps | Which version (consumer or business)? Is input used for training? Where is data stored? |
| **Assistant embedded in productivity apps ("copilot")** | AI built into email, documents, spreadsheets, meetings or chat platforms | Summarising meetings, drafting replies, finding information across files | Potentially everything the user can access in that suite | Are permissions and sensitivity labels in good order? Will it surface content people should not see? |
| **AI coding tool** | Assistants inside code editors, terminals or code-hosting platforms | Code completion, explaining code, writing tests, making multi-file changes | Source code, and sometimes the ability to run commands | Licensing of generated code, secrets in code, security review of output |
| **Agent** | A system that plans and carries out multi-step tasks using tools, with some autonomy | Researching and compiling a report, triaging tickets, updating records, operating a browser | Whatever tools and permissions it is given | What actions can it take without approval? How is it monitored? Who is accountable? |
| **Model API or AI platform** | Programmatic access to models, used by developers to build their own applications | Customer-facing chatbots, document processing pipelines, internal search | Whatever the application passes to it | Build versus buy, evaluation, security of the application, cost control |
| **AI features embedded in other software** | Generative features added to existing software (CRM, HR, finance, design, ticketing) | Drafting customer emails in a CRM, summarising candidate CVs, generating images | Data held in that application | Often switched on by default through an update. Was it assessed? Does it change how personal data is processed? |

### Why "embedded features" deserve special attention

Many organisations first encounter generative AI not through a deliberate purchase but because an existing supplier adds AI features to software they already use. These can process personal or confidential data in new ways without anyone making a decision to adopt them. [Vendor due diligence](../../assessments/vendor-due-diligence.md) and your [IT and platform](../pathways/it-and-platform.md) processes should cover changes to existing contracts, not only new purchases.

### Agents and connectors

Agents are a step change in risk, because they move from *suggesting* to *doing*. An agent typically has: a model that decides what to do next; a set of **tools** (such as search, email, a database query or a browser); a **loop** that lets it take an action, observe the result and decide again; and some form of memory.

Agents often connect to other systems through standard interfaces. One widely adopted example is the **Model Context Protocol (MCP)**, an open protocol introduced by Anthropic in November 2024 for connecting AI applications to data sources and tools, and donated in December 2025 to a foundation hosted by the Linux Foundation [1]. Standard connectors make integration easier, but also make it easier to grant broad access without noticing. See [security](../governance/security.md).

## How large language models work (non-technical)

You do not need technical knowledge to use these tools well, but a basic mental model explains most of their strengths and weaknesses.

**1. Training on text.** An LLM is a very large mathematical model trained on vast amounts of text (and, for many models, images, audio and code). During training it repeatedly predicts the next piece of text in a sequence and adjusts itself to improve. The modern architecture behind most LLMs, the *transformer*, was introduced in 2017 [2].

**2. Tokens.** Models do not read words as people do. Text is split into **tokens**, which are often parts of words. Usage limits, costs and context sizes are usually measured in tokens.

**3. Prediction, not lookup.** When you send a prompt, the model generates a response one token at a time, each time choosing a likely next token given everything so far. It is not looking answers up in a database. That is why it can write fluently about almost anything, and also why it can produce fluent, confident text that is wrong (**hallucination**).

**4. Shaping behaviour after training.** Raw models are further trained to follow instructions, hold conversations and refuse harmful requests, often using human feedback. Vendors add a **system prompt** (hidden instructions) and safety filters. These shape behaviour but do not guarantee it.

**5. The context window.** Everything the model considers for a response (your instructions, the conversation so far, attached documents, retrieved information) must fit in its **context window**. It has no memory between conversations unless the product adds a memory feature.

**6. Adding knowledge and abilities.** Because built-in knowledge stops at a **knowledge cutoff** and does not include your organisation's information, products add capabilities around the model:

| Technique | What it does | Example |
|---|---|---|
| **Retrieval-augmented generation (RAG)** | Searches a set of documents and inserts relevant passages into the prompt | Answering questions from your policy library |
| **Web search** | Retrieves current information from the internet | Summarising recent news |
| **Tool use / function calling** | Lets the model call software (a calculator, code, an API) | Running a calculation, querying a database |
| **Fine-tuning** | Further trains a model on specialist examples | Adapting style or format for a narrow task |

**7. Reasoning models.** Some models are designed to work through a problem in intermediate steps before answering. This tends to help with multi-step problems such as maths, coding and planning, at the cost of time and compute, but it does not remove the limitations described in [capabilities and limitations](capabilities-and-limitations.md).

### What this means in practice

- The tool is a powerful generator of plausible content, not an authority. Verification remains your job.
- Output quality depends heavily on the context you provide. Supplying source material improves accuracy.
- Anything you put into the context may be processed, logged or retained according to the product's terms. Know which version you are using.

## Deployment models

How a tool is deployed shapes data protection, security, cost and control. There is no universally best option: the right choice depends on your data sensitivity, regulatory context, skills and budget.

| Model | Description | Advantages | Trade-offs | Often suits |
|---|---|---|---|---|
| **Consumer service** | Free or individual paid accounts with consumer terms | No setup, low cost | Weakest organisational control; inputs may be used for training depending on terms and settings; no central administration | Personal use only. Generally unsuitable for organisational data |
| **Business or enterprise SaaS** | Vendor-hosted service under business terms | Fast to deploy; admin controls, single sign-on, contractual data commitments | Data processed by the vendor; dependent on vendor roadmap and pricing | Most organisations' first step, including small organisations |
| **Embedded in existing suite** | AI features within software you already licence | Works where people already work; inherits existing permissions and compliance controls | Can expose permission problems; limited choice of model | Organisations standardised on one productivity suite |
| **Cloud AI platform** | Models accessed through your cloud provider's AI services, inside your cloud tenancy | Integrates with existing cloud security, networking and data; choice of models | Needs engineering skills; you build and secure the application | Organisations building their own applications |
| **Self-hosted open-weight models** | Running models whose weights are published, on your own infrastructure or private cloud | Maximum control over data and model version; no per-use vendor fees | Significant skills, hardware and maintenance; you own the security and evaluation burden; capability may lag frontier models | Highly sensitive data, strict data residency, specialist needs |
| **On-device** | Smaller models running locally on laptops or phones | Data stays on the device; works offline | Smaller models are less capable; harder to manage centrally | Specific privacy-sensitive or offline tasks |

Questions to ask about any deployment are in [choosing tools](../tools/choosing-tools.md) and the [vendor due diligence](../../assessments/vendor-due-diligence.md) assessment. Tool-specific details are in the [tool guides](../tools/tool-guides/README.md), including [cloud AI platforms](../tools/tool-guides/cloud-ai-platforms.md) and [open-weight models](../tools/tool-guides/open-weight-models.md).

## A note for small organisations

You do not need a platform team or a data science function to adopt AI tools safely. For most organisations under 50 people, the key decisions are: choose a business (not consumer) version of a tool, turn on the available administrative controls, write a short [acceptable use policy](../../toolkits/acceptable-use-policy.md), and agree which kinds of data must never be entered. Building custom applications or self-hosting models is rarely the right starting point at this scale.

## Related pages

- [Capabilities and limitations](capabilities-and-limitations.md)
- [Tool categories](../tools/tool-categories.md)
- [Glossary](glossary.md)

## Sources

1. Model Context Protocol, Wikipedia (secondary summary of Anthropic's November 2024 announcement and December 2025 donation to the Agentic AI Foundation under the Linux Foundation). https://en.wikipedia.org/wiki/Model_Context_Protocol
2. Vaswani, A. et al., *Attention Is All You Need*, arXiv 1706.03762, 2017. https://arxiv.org/abs/1706.03762

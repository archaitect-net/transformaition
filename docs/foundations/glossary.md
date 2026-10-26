# Glossary

> **Who this is for:** Anyone meeting an unfamiliar term in this guide or in vendor, regulatory or technical material.
> **Last reviewed:** 2026-10

Plain-English definitions of terms used across transformAItion, in alphabetical order. Definitions are written for a non-specialist and focus on what the term means for adopting and governing AI tools. Where a term has a specific legal meaning (for example under the EU AI Act or UK GDPR), the entry says so and you should rely on the legal text for decisions. Product names are not included; see the [tool guides](../tools/tool-guides/README.md).

[A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [J](#j) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w) · [Z](#z)

## A

**Acceptable use policy (AUP).** A short, practical document telling staff which AI tools they may use, for what, and with what data. See the [template](../../toolkits/acceptable-use-policy.md).

**Agent (AI agent).** A system that uses a model to plan and carry out multi-step tasks, calling tools and acting on results with some degree of autonomy. Risk rises with the actions and data it can access. See [what are AI tools?](what-are-ai-tools.md)

**Agentic.** Describes tools or workflows in which AI takes actions, not only produces content.

**AI literacy.** The skills, knowledge and understanding needed to use AI tools in an informed way, including awareness of their opportunities, risks and possible harms. Under Article 4 of the EU AI Act, providers and deployers of AI systems must take measures to support AI literacy among their staff. See [regulation overview](../governance/regulation-overview.md).

**AI management system (AIMS).** An organisation-wide set of policies, processes and controls for governing AI, as specified in the standard ISO/IEC 42001.

**AI system.** A legal term in the EU AI Act for a machine-based system that infers from inputs how to generate outputs such as predictions, content, recommendations or decisions. Rely on the legal definition for compliance decisions.

**Alignment.** Techniques used to make a model's behaviour match intended goals and values, such as being helpful, honest and avoiding harm.

**API (application programming interface).** A way for software to communicate with other software. Model APIs let developers send prompts to a model and receive outputs programmatically.

**Augmentation.** Using AI to help a person do a task better or faster, as opposed to **automation**, where AI does the task in place of the person.

**Automation bias.** The tendency to over-trust output from an automated system, including failing to notice its errors.

## B

**Baseline.** A measurement of current performance taken before introducing a change, so that the effect can be estimated. See [measuring value](../measurement/measuring-value.md).

**Benchmark.** A standardised test used to compare models. Benchmark scores rarely predict performance on your specific tasks; evaluate on your own examples.

**Bias (in AI).** Systematic differences in how a system treats or represents different groups, often learned from training data. See [capabilities and limitations](capabilities-and-limitations.md).

**Bring your own AI (BYOAI).** Staff using personally chosen AI tools for work, with or without approval. Related to **shadow AI**.

## C

**Chain of thought.** Intermediate reasoning steps a model generates before giving an answer. Displayed reasoning may not faithfully reflect how the output was actually produced.

**Chatbot.** A conversational interface. Modern chatbots are often built on LLMs.

**Chunking.** Splitting documents into smaller pieces so they can be indexed and retrieved in a **RAG** system. Chunking choices strongly affect answer quality.

**Confabulation.** NIST's preferred term for **hallucination**: the production of confidently stated but false content.

**Connector.** An integration that lets an AI tool read from or act on another system, such as file storage, email or a database.

**Context window.** The maximum amount of text (measured in **tokens**) a model can consider at once, including instructions, conversation history and attached material.

**Controller (data controller).** Under UK GDPR and EU GDPR, the organisation that decides why and how personal data is processed. Usually your organisation, when you use an AI tool with personal data.

**Copilot (generic).** An assistant embedded in another application to help the user as they work. Also a product name used by some vendors.

**Counterfactual.** What would have happened without the change. Estimating it, for example with a comparison group, is central to measuring impact credibly.

## D

**Data minimisation.** The data protection principle of processing only the personal data that is adequate, relevant and necessary for the purpose.

**Data processing agreement (DPA).** A contract between a controller and a **processor** setting out how personal data will be handled. Not to be confused with the UK Data Protection Act.

**Data residency.** The geographic location where data is stored and processed.

**Deployer.** A legal term in the EU AI Act for an organisation that uses an AI system under its authority in a professional capacity. Most organisations adopting AI tools are deployers.

**Deterministic.** Producing the same output for the same input every time. LLM outputs are generally **non-deterministic**.

**DPIA (data protection impact assessment).** An assessment required under UK GDPR and EU GDPR for processing likely to result in high risk to individuals. Often required for new AI uses involving personal data. See [data protection](../governance/data-protection.md).

## E

**Embedding.** A list of numbers representing the meaning of a piece of text (or image), used to find similar content. Core to semantic search and **RAG**.

**Evaluation (evals).** Systematic testing of an AI system's outputs against defined criteria and test cases. Essential before and after deployment.

**Explainability.** The ability to describe how a system reached an output in terms a person can understand.

## F

**Fine-tuning.** Further training a pre-trained model on a smaller, specialist dataset to adapt its behaviour.

**Foundation model.** A large model trained on broad data that can be adapted to many tasks. LLMs are a type of foundation model.

**Frontier (capability frontier).** The boundary between tasks AI does well and tasks it does poorly. Research describes it as "jagged" because it is uneven and hard to predict. See [evidence on impact](evidence-on-impact.md).

**Frontier model.** An informal term for the most capable models available at a given time.

**Function calling.** See **tool use**.

## G

**General-purpose AI (GPAI) model.** A legal category in the EU AI Act for models that can perform a wide range of tasks, with specific obligations for their providers.

**Generative AI.** AI that produces new content such as text, images, code or audio.

**Grounding.** Connecting a model's output to specific, trusted source material, usually to reduce hallucination and allow citation.

**Guardrails.** Technical and procedural controls that constrain what an AI system will accept or produce, such as content filters and topic restrictions.

## H

**Hallucination.** Output that is fluent and plausible but false or unsupported. See [capabilities and limitations](capabilities-and-limitations.md).

**High-risk AI system.** A legal category in the EU AI Act covering certain uses (for example in employment, education, credit and essential services) that carry the heaviest obligations.

**Human in the loop.** A design in which a person reviews or approves AI output before it takes effect. **Human on the loop** means a person monitors and can intervene, but does not approve each output.

## I

**Inference.** Running a trained model to produce an output. Inference costs are what you pay per use.

**Intent-to-treat.** In an experiment, comparing everyone offered a treatment (such as a tool licence) with everyone not offered it, regardless of whether they used it. Gives a realistic estimate of the effect of a rollout.

## J

**Jailbreak.** A prompt designed to get a model to ignore its safety rules or restrictions.

## K

**Knowledge cutoff.** The date after which a model has no built-in knowledge, because its training data ends.

## L

**Large language model (LLM).** A model trained on large amounts of text to predict and generate language. The basis of most generative AI tools.

**Latency.** The delay between sending a request and receiving a response.

**Least privilege.** The security principle of giving users and systems only the access they need. Especially important for **agents**.

**Lineage (data lineage).** A record of where data came from and how it has been transformed. Important for trusting data used by AI systems.

## M

**Model.** The trained mathematical system that produces outputs. Distinct from the **product** or application built around it.

**Model card.** A document published by a model's developer describing its intended uses, capabilities, limitations and evaluation results.

**Model Context Protocol (MCP).** An open protocol for connecting AI applications to tools and data sources. See [what are AI tools?](what-are-ai-tools.md)

**Multimodal.** Able to process or produce more than one type of content, such as text, images and audio.

## N

**Non-determinism.** The property of producing different outputs for the same input. See [capabilities and limitations](capabilities-and-limitations.md).

## O

**Open-weight model.** A model whose trained parameters (weights) are published, so it can be run on your own infrastructure. "Open-weight" does not necessarily mean open-source training data or code, and licences vary. See the [tool guide](../tools/tool-guides/open-weight-models.md).

**Orchestration.** Software that coordinates multiple model calls, tools and steps into a workflow.

**Overreliance.** Depending on AI output more than its reliability justifies.

## P

**Parameters.** The internal numerical values a model learns in training. Often used as a rough indicator of model size.

**Pilot.** A time-limited, controlled trial of a tool or use case with defined success criteria. See [pilot](../lifecycle/04-pilot.md).

**Processor (data processor).** Under UK GDPR and EU GDPR, an organisation that processes personal data on behalf of a **controller**. AI vendors are often processors.

**Prompt.** The input given to a model: instructions, questions, examples and context.

**Prompt engineering.** The practice of designing prompts to get reliable, useful outputs.

**Prompt injection.** An attack in which instructions hidden in content the model processes override intended instructions. **Indirect** prompt injection arrives via retrieved content such as web pages, emails or documents. See [security](../governance/security.md).

**Prompt library.** A shared, maintained collection of tested prompts. See the [template](../../toolkits/prompt-library-template.md).

**Provider.** A legal term in the EU AI Act for the organisation that develops an AI system or model and places it on the market under its own name.

## R

**RACI.** A matrix assigning who is Responsible, Accountable, Consulted and Informed for each activity. See the [template](../../toolkits/raci-template.md).

**RAG (retrieval-augmented generation).** A technique in which relevant passages are retrieved from a document collection and given to the model alongside the question, so answers draw on that content. See the [data teams pathway](../pathways/data-teams.md).

**Randomised controlled trial (RCT).** An experiment in which participants are randomly assigned to receive a treatment or not, giving the most reliable estimate of cause and effect.

**Reasoning model.** A model designed to generate intermediate steps before answering, typically improving performance on multi-step problems at higher cost and latency.

**Red teaming.** Deliberately attacking or stress-testing an AI system to find failures, vulnerabilities and harmful behaviours.

**Responsible AI.** An umbrella term for principles and practices to make AI use fair, safe, transparent, accountable and lawful. See [responsible AI principles](../governance/responsible-ai-principles.md).

**Retention (data retention).** How long inputs, outputs and logs are kept, by you and by the vendor.

## S

**Sandbox.** An isolated environment for testing tools or code without affecting live systems or data.

**Semantic search.** Search based on meaning rather than exact keyword matches, usually using **embeddings**.

**Sensitivity label.** A classification applied to documents or data (such as "Confidential") that tools can use to restrict access or processing.

**Shadow AI.** Use of AI tools within an organisation without the knowledge or approval of those responsible for IT, security or data. See the [IT and platform pathway](../pathways/it-and-platform.md).

**Single sign-on (SSO).** Letting users log in to many services with one organisational identity, enabling central control of access.

**Special category data.** Under UK GDPR and EU GDPR, personal data needing extra protection, such as health, ethnicity, religion, sexual orientation, biometric and genetic data, trade union membership and political opinions.

**Sycophancy.** A model's tendency to agree with or flatter the user, including endorsing incorrect premises.

**System prompt.** Instructions set by the product or developer, usually hidden from the user, that shape a model's behaviour.

## T

**Temperature.** A setting that controls how varied a model's output is. Lower values make output more predictable; higher values more varied.

**Token.** The unit of text a model processes, often part of a word. Context limits and costs are measured in tokens.

**Tool use.** A model's ability to call external functions or software, such as search, a calculator, code execution or an API. Also called function calling.

**Training data.** The data used to train a model. Questions about its source matter for copyright, bias and quality.

**Transformer.** The neural network architecture underlying most modern LLMs.

**Transparency obligations.** Legal duties to tell people when they are interacting with AI or seeing AI-generated content, such as those under Article 50 of the EU AI Act.

## U

**Use case.** A specific task or process in which AI is applied, for a defined group of users, to achieve a defined outcome. The unit of assessment, prioritisation and measurement in this guide. See the [use case register](../../toolkits/use-case-register-template.md).

## V

**Vanity metric.** A measure that looks impressive but does not indicate value, such as licences issued or prompts sent. See [measuring value](../measurement/measuring-value.md).

**Vector database.** A database designed to store and search **embeddings**, commonly used in **RAG** systems.

## W

**Weights.** The learned numerical values inside a model. See **parameters** and **open-weight model**.

**Workflow redesign.** Changing how a process is organised to take advantage of AI, rather than inserting AI into an unchanged process. See the [managers pathway](../pathways/managers.md).

## Z

**Zero data retention (ZDR).** A contractual or technical arrangement in which a vendor does not store prompts and outputs beyond what is needed to return a response. Availability and exact terms vary by vendor and product.

**Zero-shot / few-shot.** Asking a model to do a task with no examples (zero-shot) or with a few examples included in the prompt (few-shot).

# Open-weight models (self-hosted)

> **Who this is for:** ML, platform and infrastructure engineers, security teams, and technical leads in organisations that have decided to run open-weight models on their own infrastructure or private cloud.
> **Last reviewed:** 2026-10

This guide covers self-hosting open-weight models: models whose trained weights are published for download, so you can run them in an environment you control. Unlike the other tool guides, it covers an approach rather than one product. It describes licence types, hardware sizing, serving stacks, evaluation, security and operations, and is candid that self-hosting moves every control, and every responsibility, to you. It assumes the decision to self-host has been made; for that decision, see [choosing tools](../choosing-tools.md#build-buy-or-configure).

> **Verify before relying on this.** Model releases, licence terms and serving software change very quickly. Check each model's licence and model card, and each software project's documentation, at the version you deploy.

## Overview

**What "open-weight" means.** The model's parameters are downloadable. That does not necessarily mean the training data, training code or full documentation are available, or that the licence is an open-source licence. "Open-weight" and "open-source" are not synonyms; check the licence.

**Why organisations self-host:**

- Data must not leave their environment (sovereignty, air-gapped networks, contractual restrictions).
- Volumes are high and predictable enough that infrastructure costs less than per-token pricing.
- They need to fine-tune or modify a model for a narrow task.
- They want to reduce dependence on a single vendor.

**What they take on:** hardware or compute, serving software, security hardening, safety filtering, evaluation, monitoring, upgrades and incident response.

**Example model families** (named neutrally, in no order, not exhaustive): Llama (Meta), Gemma (Google), Mistral models, Qwen (Alibaba), DeepSeek, gpt-oss (OpenAI) and Phi (Microsoft). Families differ in size range, languages, context length, modalities and licence.

Category: [open-weight models, self-hosted](../tool-categories.md#6-open-weight-models-self-hosted).

## Editions and licensing

There is no "edition"; the licence is what matters. Licences for open-weight models fall broadly into three types:

| Licence type | Typical characteristics | What to check |
|---|---|---|
| **Permissive open-source licences** (for example Apache 2.0, MIT) | Broad rights to use, modify and redistribute, including commercially, with attribution and notice conditions | Notice and attribution obligations; whether weights and code are under the same licence |
| **Custom "community" or model-specific licences** | Permit use, often commercially, but add conditions: acceptable-use policies, attribution or naming requirements, thresholds for very large-scale users, restrictions on using outputs to train other models | Every condition, including incorporated acceptable-use policies that may change; scale thresholds; redistribution terms for fine-tuned derivatives |
| **Research or non-commercial licences** | Use limited to research or non-commercial purposes | Whether your intended use counts as commercial |

**Checks for every model:**

- [ ] Read the licence itself, not a summary, at the version you download.
- [ ] Check whether an acceptable-use policy is incorporated by reference and can be updated by the licensor.
- [ ] Check obligations for derivatives (fine-tuned models) and for distributing the model inside products.
- [ ] Check restrictions on using outputs to develop other models.
- [ ] Record the licence and version in your model inventory.
- [ ] Involve legal review for any custom licence. See [intellectual property](../../governance/intellectual-property.md).

## Prerequisites

- **Skills**: ML engineering, GPU infrastructure, MLOps, security engineering. For small organisations, this is usually the deciding constraint.
- **Hardware or compute**: GPUs (or other accelerators) with enough memory for the model, or CPU-only inference for small models at lower speed.
- **A model inventory and approval process**, so models are not downloaded and deployed ad hoc.
- **An evaluation set** from your own tasks (see [Evaluation](#evaluation)).
- **Security architecture**: network segmentation, identity for callers, logging.

### Sizing hardware: a rough method

Memory needed for weights is approximately **number of parameters × bytes per parameter**, plus headroom for the key-value cache (which grows with context length and concurrent users) and runtime overhead.

| Precision | Bytes per parameter | Weights for a 7-billion-parameter model | Weights for a 70-billion-parameter model |
|---|---|---|---|
| 16-bit (FP16/BF16) | 2 | about 14 GB | about 140 GB |
| 8-bit | 1 | about 7 GB | about 70 GB |
| 4-bit | 0.5 | about 3.5 GB | about 35 GB |

This is arithmetic, not a benchmark; actual requirements depend on architecture (for example mixture-of-experts models load more parameters than they use per token), context length, batch size and serving software. **Quantisation** (lower precision) reduces memory and cost but can reduce quality; evaluate quantised variants on your own tasks.

## Architecture and data flow

A typical self-hosted deployment:

1. **Model registry**: approved model files, with recorded source, licence, version and checksums.
2. **Inference server**: loads the model onto accelerators and exposes an API, often compatible with common commercial API formats so applications can switch between providers.
3. **Gateway**: authentication, rate limiting, routing between models, logging, and content filtering for inputs and outputs.
4. **Applications**: chat interfaces, retrieval-augmented generation over your documents, agents and integrations.
5. **Observability**: metrics (latency, throughput, errors, accelerator use), logs, and quality monitoring.

Data stays within the environment you control, unless an application or tool calls out to external services. Check every integration for external calls.

## Data handling, retention and training-on-data

- **No third party sees your data** by default; you decide retention for prompts, outputs and logs.
- **You must set retention policies** for gateway and application logs, which may contain personal or confidential data. Apply your [data protection](../../governance/data-protection.md) obligations, including data subject rights.
- **Training on your data** happens only if you choose to fine-tune. If you do, treat training data and the resulting model as containing that data; fine-tuned models can reproduce training content.
- **Telemetry** in some serving software or user interfaces may call home; check and disable as needed.

## Security and admin controls

Self-hosting means implementing controls a SaaS vendor would otherwise provide. Use established frameworks: the UK NCSC's *Guidelines for secure AI system development* cover secure design, development, deployment, and operation and maintenance [1]; the OWASP Top 10 for LLM Applications lists risks including prompt injection, sensitive information disclosure, supply chain, data and model poisoning, improper output handling, excessive agency and unbounded consumption [2].

**Supply chain**

- [ ] Download models only from the publisher's official repository; verify checksums or signatures where provided.
- [ ] Prefer weight formats that do not execute code when loaded; treat formats that can contain executable code as untrusted.
- [ ] Pin versions of models and serving software; scan containers and dependencies.
- [ ] Record provenance in your model inventory [1][2].

**Runtime**

- [ ] Put the inference server behind an authenticated gateway; never expose it directly to the internet.
- [ ] Rate-limit and set maximum token limits to prevent resource exhaustion ("unbounded consumption") [2].
- [ ] Filter inputs and outputs according to the use case; open-weight models may have weaker or different built-in safety behaviour than hosted services, and safety behaviour can be removed by fine-tuning.
- [ ] Validate and sanitise model outputs before passing them to other systems ("improper output handling") [2].
- [ ] Give agents least-privilege tool permissions ("excessive agency") [2].
- [ ] Isolate GPU hosts; restrict who can load or replace models.
- [ ] Log access and administrative actions; protect logs.

## Identity and access

- Callers (users and applications) authenticate to the gateway through your identity provider or workload identity.
- Separate roles for model approval, deployment, and use.
- Retrieval applications must enforce document-level permissions so users only receive content they are entitled to see.

## Integration

- Exposing an API compatible with widely used commercial formats lets applications switch between self-hosted and hosted models with configuration changes.
- Retrieval-augmented generation connects models to your documents through embeddings and vector search; the embedding model is a separate model to select and license.
- Agent frameworks can use self-hosted models, subject to the model's tool-use capability.
- Cloud platforms also offer managed hosting of many open-weight models, a middle path between SaaS and full self-hosting. See [cloud AI platforms](cloud-ai-platforms.md).

**Serving stacks (examples, named neutrally).** Options range from high-throughput GPU inference servers (for example vLLM, SGLang and Hugging Face Text Generation Inference) to lightweight local runtimes (for example llama.cpp and Ollama) and vendor-optimised stacks from accelerator makers. Check each project's current documentation, licence, maintenance status, hardware support and security advisories before adopting it.

## Evaluation

Public leaderboards do not tell you how a model performs on your tasks, in your languages, at your chosen quantisation. Evaluate:

1. **Task quality** on a test set built from real work (see [running a fair evaluation](../choosing-tools.md#step-5-running-a-fair-evaluation)).
2. **Safety behaviour**: responses to harmful, out-of-scope and manipulative prompts relevant to your context, including prompt injection through documents.
3. **Performance**: latency and throughput at expected concurrency on your hardware.
4. **Cost**: infrastructure cost per thousand requests at expected volume, compared with hosted alternatives.
5. **Regression**: re-run the same evaluation whenever you change model, version, quantisation or serving software.

## Rollout steps

1. **Confirm the case for self-hosting**: data requirement, volume and cost model, skills available.
2. **Shortlist models** by task fit, size, languages and licence; complete licence review.
3. **Size hardware** using the method above, then test.
4. **Build the platform**: registry, inference server, gateway, observability, in a segmented network.
5. **Harden** using the supply-chain and runtime checklists [1][2].
6. **Evaluate** shortlisted models and quantisations on your test set; choose.
7. **Pilot** one use case with real users. See the [pilot plan template](../../../toolkits/pilot-plan-template.md).
8. **Set operating procedures**: patching, model updates, incident response, capacity planning, log retention.
9. **Scale** to further use cases through the same gateway.
10. **Review** licences, model versions and security advisories regularly.

## Enablement and training

- Platform staff need skills in GPU operations, inference optimisation and AI-specific security.
- Developers need guidance on the gateway, approved models and secure application patterns.
- Users need to know which model they are using and its limitations; smaller self-hosted models may perform differently from large hosted ones.
- See the [IT and platform](../../pathways/it-and-platform.md) and [developers](../../pathways/developers.md) pathways.

## Monitoring and usage reporting

- Operational metrics: latency, throughput, error rates, accelerator utilisation and memory.
- Usage by application and team, for capacity planning and cost allocation.
- Quality signals: user feedback, periodic evaluation re-runs, drift on key tasks.
- Security signals: unusual request patterns, attempted prompt injection, access anomalies.
- See [measuring value](../../measurement/measuring-value.md) and [Operate](../../lifecycle/06-operate.md).

## Known limitations

- **Every control is your responsibility**, including ones SaaS vendors handle silently (abuse detection, safety filters, patching).
- **Skills and staffing** are often the binding constraint, especially for small organisations.
- **Hardware availability and cost** can be significant, and capacity must be planned for peaks.
- **Quality gap**: depending on the task, the largest hosted models may outperform models you can afford to run; only your evaluation can say.
- **Licence complexity**: custom licences may restrict use, scale or derivatives, and incorporated policies may change.
- **Safety behaviour** varies by model and can be removed by fine-tuning.
- **Pace of change**: models and serving software update frequently; keeping current takes effort.

## Cost considerations

- Hardware purchase or cloud compute (often the largest cost), storage, networking and power.
- Staff time for building, operating and securing the platform.
- Under-utilised accelerators cost money; batching and right-sizing matter.
- Compare total cost of ownership with hosted per-token pricing at realistic volumes, including staff costs, before committing. See the [business case template](../../../toolkits/business-case-template.md).

## Exit considerations

- Self-hosting has low vendor lock-in for the model itself, but investment in a specific serving stack, fine-tuned weights and hardware is less portable.
- Using a common API format and an abstraction gateway eases switching between models and between self-hosted and hosted options.
- Fine-tuned derivatives remain subject to the base model's licence.
- Keep evaluation sets, prompts and fine-tuning data in your own repositories.

## Official documentation links

- [NCSC: Guidelines for secure AI system development](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development)
- [OWASP Top 10 for LLM Applications 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/)
- Each model's official licence and model card, from the publisher's own repository.
- Each serving project's official documentation and security advisories.

## Questions to verify (with model publishers, your legal team and software maintainers)

- The exact licence, incorporated acceptable-use policy and any scale thresholds for each model and version.
- Whether fine-tuned derivatives may be used commercially and distributed, and on what conditions.
- The training data documentation the publisher provides, and any known limitations or evaluations in the model card.
- For serving software: maintenance status, security advisory process, telemetry behaviour and hardware support.
- For managed hosting of open models on cloud platforms: retention and data handling for that hosting service.

---

**Last verified:** 2026-10-26 against the documentation listed above.

**Verify before relying on this.** Models, licences and software change frequently. This guide is descriptive and is not an endorsement. Inclusion of any model family or software project reflects breadth of organisational use, not preference.

## Sources

1. National Cyber Security Centre (UK), *Guidelines for secure AI system development*, version 1.0, 27 November 2023. https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development
2. OWASP GenAI Security Project, *OWASP Top 10 for LLM Applications 2026*. https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/

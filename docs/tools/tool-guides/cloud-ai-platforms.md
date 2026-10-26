# Cloud AI platforms

> **Who this is for:** Cloud platform and architecture teams, developers and data teams building AI applications, and the security and data protection staff who approve them, in organisations that have chosen a hyperscaler AI platform.
> **Last reviewed:** 2026-10

This guide covers implementing three hyperscaler AI platforms that provide model access and application-building tools within your own cloud account: Microsoft Foundry (formerly Azure AI Foundry, including Azure OpenAI models), Amazon Bedrock, and Google's Gemini Enterprise Agent Platform (formerly Vertex AI). It describes each platform's data commitments, retention and abuse-monitoring settings, processing-location options, security controls, a common rollout sequence, and known limitations, with links to official documentation. It assumes a platform has already been chosen; for selection, see [choosing tools](../choosing-tools.md).

> **Verify before relying on this.** All three platforms have been renamed or restructured recently. Google renamed Vertex AI to Gemini Enterprise Agent Platform in April 2026 [7]; Microsoft Foundry was previously branded Azure AI Studio and Azure AI Foundry [1]. Data retention defaults vary by model and feature and change often. Check the live documentation for the specific models and features you use.

## Overview

| | Microsoft Foundry | Amazon Bedrock | Gemini Enterprise Agent Platform |
|---|---|---|---|
| Former names | Azure AI Studio, Azure AI Foundry [1] | (unchanged) | Vertex AI [7] |
| Model access | Catalogue of models from Microsoft, OpenAI, Anthropic, Meta and others; "Models sold by Azure" include Azure OpenAI models [1][2] | 100+ foundation models from Amazon, Anthropic, OpenAI, DeepSeek and others [4] | Model Garden with Google, third-party and open models [8] |
| Agent tooling | Foundry Agent Service: prompt agents, hosted agents, Foundry Toolbox [1] | Agent capabilities documented in the Bedrock user guide | Agent Studio (low-code) and Agent Development Kit [8] |
| Governance features | Entra identity, content filters, network isolation, Azure Policy, unified RBAC [1] | AWS IAM, CloudTrail logging, data retention modes [4][5] | Agent Identity, Agent Gateway, Agent Registry, Model Armor [8] |

Category: [cloud AI platforms and model APIs](../tool-categories.md#5-cloud-ai-platforms-and-model-apis).

## Editions and licensing

All three platforms are consumption-billed under your existing cloud agreement. Common pricing elements include per-token charges for model inference, batch and cached-input discounts, reserved or provisioned throughput, and separate charges for storage, retrieval, fine-tuning, agent hosting and tools. Prices vary by model, region and deployment type; consult each provider's pricing pages and your agreement.

Some third-party models carry their own terms or licences in addition to the cloud provider's terms. Check the model card and terms for each model you enable.

## Prerequisites

- A cloud account or subscription with appropriate governance (landing zone, policies, budgets).
- Identity and access management roles for platform administrators, developers and applications.
- Model access approvals where required (some models require registration, eligibility review or regional availability checks).
- Network design: private endpoints, egress controls.
- Logging destinations for audit and, where enabled, prompt logging.
- An agreed data classification for the data the application will process.

## Architecture and data flow

The common pattern:

1. An application, inside your network or cloud account, calls the platform's model endpoint using an identity you control.
2. The request may be routed within a region, a geography or data zone, or globally, depending on the deployment type or inference profile you choose.
3. The model processes the request. Safety classifiers or guardrails may evaluate inputs and outputs.
4. Depending on configuration, data may be stored for features you use (stateful APIs, files, fine-tuning), for abuse monitoring, or in logs you enable.
5. Responses return to your application, which handles output validation and presentation.

### Microsoft Foundry: processing location by deployment type [2]

| Deployment type | Processing location |
|---|---|
| Standard | Within the customer-specified geography (may move between regions in that geography) |
| DataZone | Anywhere within the specified data zone (for example the US, or EU member states) |
| Global | Any geography where the model is deployed |

For Global and DataZone, data at rest (uploaded data and abuse monitoring store) stays in the customer-designated geography [2].

### Amazon Bedrock: isolation from model providers [3][4]

Bedrock deploys copies of provider models into AWS-operated model deployment accounts in each region; model providers have no access to those accounts, Bedrock logs, or customer prompts and completions [3]. With cross-region inference, retained inputs and outputs are stored in destination regions [5].

### Gemini Enterprise Agent Platform

Google documents caching, grounding and feature-specific storage behaviour in its zero data retention page [9]; see below.

## Data handling, retention and training-on-data

### Microsoft Foundry (Models sold by Azure) [2][6]

- Prompts, completions, embeddings and training data are **not** available to other customers or to OpenAI or other model providers, are not used by providers to improve their models, and are not used to train generative AI foundation models without permission or instruction.
- Fine-tuned models are available exclusively to the customer.
- Data stored for features (fine-tuning, batch, Responses API, Assistants, stored completions) is held in the customer's Foundry resource, in the same geography, encrypted with AES-256 by default, with optional customer-managed keys; some preview features may not support customer-managed keys.
- **Abuse monitoring**: flagged content may be sampled for automated review and, as needed, human review by authorised Microsoft staff (located in the EEA for EEA deployments). Customers meeting Limited Access eligibility criteria can apply for **modified abuse monitoring**, which skips storage and human review [2][6].
- Preview models or features might not support all of these conditions [2].

### Amazon Bedrock [3][5][10]

- AWS states Bedrock does not use customer inputs or outputs to train AWS or third-party models, and does not share them with third-party model providers [10].
- **Data retention modes**, set per region at account or project level [5]:

| Mode | Behaviour |
|---|---|
| `none` | Zero data retention: no request or response data written to durable storage or shared with the provider |
| `default` | AWS may retain data for safety and abuse prevention; actual retention depends on the model; provider does not receive it |
| `aws_review` | Inputs and outputs may be retained for human review by AWS within the AWS boundary |
| `inherit` | Defers to a broader scope; unconfigured regions fall back to each model's default |

- Some models require retention: AWS documents up to 30 days' retention for certain models, and classifier-flagged traffic for most OpenAI models retained up to 30 days for automated abuse detection, with zero retention available on request for eligible customers [5][11].
- With the Responses API, `store` defaults to true under `default` mode, and `store=false` does not guarantee zero retention under that mode [5].

### Gemini Enterprise Agent Platform [9]

- Google states it will not use customer data to train or fine-tune models without prior permission or instruction, for all managed models.
- **Implicit caching** deletes data within 24 hours; durable caching is not compatible with customer-managed encryption keys; caching can be disabled per project.
- **Abuse monitoring**: Google may log prompts to detect abuse for customers under the Google Cloud Platform Terms of Service; some models may log prompts and responses under an Advanced AI Safety Addendum, where zero data retention may not be possible.
- **Grounding with Google Search** retains query logs for up to three days, which cannot be disabled; **Grounding with Google Maps** stores data for 30 days. Google suggests Web Grounding for Enterprise for zero retention.
- **Zero data retention conditions** include keeping request-response logging disabled, setting `store = false` on the Interactions API, keeping Live API session resumption disabled, and avoiding certain features (Deep Research stores session data for seven days).

## Security and admin controls

| Control area | Microsoft Foundry | Amazon Bedrock | Gemini Enterprise Agent Platform |
|---|---|---|---|
| Identity and RBAC | Microsoft Entra ID; unified RBAC across agents, models and tools [1] | AWS IAM | Google Cloud IAM; Agent Identity for agents [8] |
| Network isolation | Network isolation under one Azure resource [1] | VPC and AWS PrivateLink (see Bedrock user guide) [3] | Verify network controls for your services with Google |
| Encryption | AES-256 at rest; customer-managed keys optional [2] | TLS 1.2+ required; FIPS endpoints available [3] | Google default encryption; CMEK not compatible with durable caching [9] |
| Audit logging | Azure monitoring; tracing and evaluations [1] | AWS CloudTrail recommended [3] | Platform audit logs; request-response logging off by default [9] |
| Content safety | Content filters (guardrails) evaluate prompts and outputs synchronously [2] | Guardrails (see Bedrock user guide) | Model Armor and governance policies [8] |
| Policy | Azure Policy [1] | Service control policies for retention modes [5] | Agent Gateway as policy enforcement point [8] |

## Identity and access

- Applications should call models using managed or workload identities rather than long-lived keys where the platform supports it.
- Separate roles for platform administration, model deployment, application development and data access.
- Agents need their own identities with least-privilege permissions; Google's Agent Identity and Foundry's unified RBAC are examples of platform support for this [1][8].

## Integration

- SDKs and APIs for common languages on all three platforms; Bedrock supports several API styles including Messages, Responses, Chat Completions, Converse and Invoke [4]; Foundry offers Python, C#, JavaScript and Java SDKs and an MCP server for coding agents [1].
- Retrieval over your data through managed knowledge services or your own vector stores.
- Agent frameworks: Foundry hosted agents support frameworks such as Microsoft Agent Framework, LangGraph and Semantic Kernel [1]; Google's Agent Development Kit is model-agnostic [8].

## Rollout steps

1. **Classify the data** the application will process and decide the processing-location requirement.
2. **Select models** and confirm regional availability, deployment types or inference profiles, and any model-specific terms or retention requirements [2][5][9].
3. **Set retention and logging posture**: Bedrock retention mode per region [5]; Foundry modified abuse monitoring application if eligible [6]; Agent Platform caching and logging settings [9].
4. **Design identity and network controls**: least-privilege roles, private connectivity, egress restrictions.
5. **Configure content safety** (filters, guardrails or Model Armor) appropriate to the use case.
6. **Build an evaluation set** from your tasks and evaluate candidate models before committing. See [choosing tools](../choosing-tools.md#step-5-running-a-fair-evaluation).
7. **Threat-model the application**, including prompt injection and excessive agency [12].
8. **Pilot** with monitoring of quality, cost and safety events.
9. **Set budgets and alerts**, and quotas per application.
10. **Operate**: monitor model deprecations and version changes, re-run evaluations on model updates, review retention settings when enabling new features.

## Enablement and training

- Developers need training on secure AI application design (input handling, output validation, tool permissions) and the platform's safety features.
- Platform teams need to understand retention modes and deployment types, because defaults differ by model and feature.
- Risk and data protection staff need a summary of where data is processed and stored for each application. See the [data teams](../../pathways/data-teams.md) and [IT and platform](../../pathways/it-and-platform.md) pathways.

## Monitoring and usage reporting

- Use cloud cost management and per-application tagging to track token spend.
- Platform tracing and evaluation features (for example Foundry observability [1]) to monitor quality.
- Audit logs for administrative actions and, where enabled, prompt logs, stored with appropriate access control.
- Measure outcomes for the application, not just calls. See [measuring value](../../measurement/measuring-value.md).

## Known limitations

- **Defaults vary by model and feature.** On Bedrock, some models require retention for up to 30 days [5][11]; on Agent Platform, grounding and some features store data that cannot be disabled [9]; on Foundry, preview features may not support all data commitments [2].
- **Global or wide-area deployment types** may process data outside your preferred region [2][5].
- **Modified abuse monitoring** on Foundry requires eligibility approval and reduces detection accuracy [6].
- **Customer-managed keys** are not compatible with some features (Agent Platform durable caching; some Foundry preview features) [2][9].
- **Third-party models** may carry additional terms or safety addenda [9].
- **You own the application**: access control, output handling, monitoring and incident response for what you build.
- **Renaming** means older internal documentation, policies and training may reference retired names.

## Cost considerations

- Token pricing differs widely between models; model choice is the largest cost lever.
- Cross-region and global deployment options may lower per-token cost or raise throughput [4].
- Reserved or provisioned capacity trades commitment for predictability.
- Hidden costs: storage for stateful features, retrieval indexes, logging volumes, egress, evaluation runs, and engineering time.
- Set budgets and quotas per application before scaling.

## Exit considerations

- Applications built on portable APIs and open frameworks are easier to move; platform-specific agent services and managed retrieval increase lock-in.
- Fine-tuned models may not be exportable; check before investing.
- Keep evaluation sets and prompts in your own repositories so you can re-test on another platform.
- Many models are available on more than one platform, which can ease migration between clouds.

## Official documentation links

- [What is Microsoft Foundry?](https://learn.microsoft.com/azure/foundry/what-is-foundry)
- [Data, privacy and security for Foundry Models sold by Azure](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy)
- [Foundry abuse monitoring](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/abuse-monitoring)
- [What is Amazon Bedrock?](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
- [Amazon Bedrock data protection](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html)
- [Amazon Bedrock data retention](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html)
- [Amazon Bedrock abuse detection](https://docs.aws.eu/bedrock/latest/userguide/abuse-detection.html)
- [Gemini Enterprise Agent Platform overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview)
- [Gemini Enterprise Agent Platform and zero data retention](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention)
- [Gemini Enterprise Agent Platform release notes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes)

## Questions to verify with your provider

- For each model we plan to use: default retention, abuse-monitoring retention, human review, and whether zero retention is available.
- Which deployment types or inference profiles keep processing within our required geography (for example the UK or EU).
- Network isolation options for each service we use, including agent and retrieval services.
- Whether fine-tuned models and agent definitions can be exported.
- Model deprecation notice periods.
- Intellectual property indemnity coverage for each model, including third-party models.

---

**Last verified:** 2026-10-26 against the official documentation listed above.

**Verify before relying on this.** Vendors change products, plans and terms frequently. This guide is descriptive and is not an endorsement. Inclusion in this guide reflects breadth of organisational use, not preference.

## Sources

1. Microsoft Learn, *What is Microsoft Foundry?*, accessed 2026-10. https://learn.microsoft.com/azure/foundry/what-is-foundry
2. Microsoft Learn, *Data, privacy, and security for Foundry Models sold by Azure in Microsoft Foundry*, accessed 2026-10. https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy
3. AWS, *Data protection — Amazon Bedrock*, accessed 2026-10. https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html
4. AWS, *What is Amazon Bedrock?*, accessed 2026-10. https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html
5. AWS, *Data retention — Amazon Bedrock*, accessed 2026-10. https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html
6. Microsoft Learn, *Abuse monitoring*, accessed 2026-10. https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/abuse-monitoring
7. Google Cloud, *Gemini Enterprise Agent Platform release notes* (entry of 22 April 2026, "Vertex AI to Gemini Enterprise Agent Platform naming changes"), accessed 2026-10. https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes
8. Google Cloud, *Gemini Enterprise Agent Platform overview*, accessed 2026-10. https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview
9. Google Cloud, *Gemini Enterprise Agent Platform and zero data retention*, accessed 2026-10. https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention
10. AWS re:Post Knowledge Center, *Amazon Bedrock model data use*, accessed 2026-10. https://www.repost.aws/knowledge-center/amazon-bedrock-model-data-use
11. AWS, *Amazon Bedrock abuse detection*, accessed 2026-10. https://docs.aws.eu/bedrock/latest/userguide/abuse-detection.html
12. OWASP GenAI Security Project, *OWASP Top 10 for LLM Applications 2025*. https://genai.owasp.org/llm-top-10/

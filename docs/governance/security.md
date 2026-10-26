# Security for AI tools

> **Who this is for:** Security teams, IT and platform engineers, developers building on AI services, and risk owners approving AI tools.
> **Last reviewed:** 2026-10

AI tools introduce threats that traditional application security does not fully cover: instructions hidden in content the AI reads, sensitive data surfacing through AI search, outputs passed unchecked into other systems, opaque third-party model supply chains, and AI agents with more permissions than they need. This page describes the main threats, maps them to the OWASP Top 10 for LLM Applications (2026 edition) and MITRE ATLAS, sets out controls for both off-the-shelf tools and applications you build, and summarises UK and international secure AI guidance. It is vendor-neutral; see the [tool guides](../tools/tool-guides/README.md) for product-specific security settings.

## Reference frameworks

| Framework | What it is | Use it for |
|---|---|---|
| OWASP Top 10 for LLM Applications 2026 | Community list of the most critical security risks for applications using large language models, published by the OWASP GenAI Security Project on 3 August 2026 [1][2] | Threat checklists, developer awareness, testing scope |
| MITRE ATLAS | A knowledge base of adversary tactics and techniques against AI-enabled systems, drawn from real-world attacks and red-team demonstrations, modelled on MITRE ATT&CK [3] | Threat modelling; mapping AI threats into security operations that already use ATT&CK |
| Guidelines for secure AI system development | Joint guidance led by the UK NCSC with international partner agencies, published 27 November 2023, organised around secure design, development, deployment, and operation and maintenance [4] | Lifecycle security practices for those building or integrating AI |
| UK Code of Practice for the Cyber Security of AI | Voluntary UK government code published 31 January 2025, with 13 principles; adopters must follow provisions marked as required [5] | Baseline security requirements across the AI lifecycle |
| ETSI EN 304 223 | European standard for baseline cyber security requirements for AI models and systems, released by ETSI building on the UK Code and the NCSC-led guidelines; the UK Code is expected to be updated to align with it [6] | Standards-based baseline and future conformity assessment |
| NIST AI 600-1 | Generative AI Profile, including information security risks [7] | Risk catalogue; see [risk management](risk-management.md) |

### OWASP Top 10 for LLM Applications 2026

The 2026 edition kept all ten 2025 categories, re-ordered them, and renamed one [2]:

| ID | Risk | Change from 2025 |
|---|---|---|
| LLM01 | Prompt Injection | Unchanged position |
| LLM02 | Sensitive Information Disclosure | Unchanged position |
| LLM03 | Excessive Agency | Up from LLM06 |
| LLM04 | Supply Chain | Down from LLM03 |
| LLM05 | Data and Model Poisoning | Down from LLM04 |
| LLM06 | Unbounded Consumption | Up from LLM10 |
| LLM07 | Misinformation | Up from LLM09 |
| LLM08 | Hidden Context Exposure | Renamed and widened from System Prompt Leakage (LLM07) |
| LLM09 | Vector and Embedding Weaknesses | Down from LLM08 |
| LLM10 | Improper Output Handling | Down from LLM05 |

Older material may refer to the 2023 version 1.1 list (with entries such as Insecure Plugin Design and Model Theft) or the 2025 list. Check which version a vendor or auditor is citing.

## Threats and controls

### Prompt injection (OWASP LLM01)

**What it is.** An attacker supplies input that causes the model to ignore its instructions or take unintended actions. *Direct* injection comes from the user; *indirect* injection is hidden in content the AI processes, such as a web page, email, document or calendar invite.

**Why it matters for adopters.** AI assistants that read email, browse the web or search shared files can be exposed to indirect injection by anyone who can get content in front of them. Impact grows with the tool's permissions.

**Controls:**

- Limit what the AI can do (see excessive agency) so that a successful injection has limited impact.
- Require human confirmation for consequential actions (sending, deleting, paying, sharing externally).
- Restrict connectors and web access to what the use case needs.
- Treat content from untrusted sources as untrusted, including in retrieval pipelines.
- Use vendor-provided injection detection and content filtering where available, recognising that none is complete.
- Include injection scenarios in testing and red-teaming.

### Sensitive information disclosure and data leakage (OWASP LLM02, LLM08)

**What it is.** The AI reveals data the user should not see: through retrieval over over-shared content, through memorised data, or through exposure of hidden context such as system prompts, policies and tool definitions. Data can also leak *out* when staff enter confidential information into unapproved tools.

**Controls:**

- Review and fix access permissions before enabling AI search across repositories.
- Apply sensitivity labels and data loss prevention to AI interactions where supported.
- Use approved tools with contractual data protections; block or restrict unapproved services where risk warrants.
- Do not put secrets or sensitive logic in system prompts; assume they can be extracted.
- Log and monitor AI interactions within your monitoring policy.
- Train staff on what data may be used.

### Insecure output handling (OWASP LLM10)

**What it is.** AI output is passed to other systems (browsers, shells, databases, APIs) without validation, enabling cross-site scripting, code execution, or injection into downstream systems.

**Controls:**

- Treat model output as untrusted user input: validate, encode and sanitise.
- Never execute generated code or queries automatically in production without review and sandboxing.
- Apply least privilege to any system that acts on AI output.
- Review AI-generated code with the same rigour as human-written code, including dependency and licence checks (see [intellectual property](intellectual-property.md)).

### Supply chain and poisoning (OWASP LLM04, LLM05, LLM09)

**What it is.** Risks from third-party models, datasets, plug-ins, libraries and model hubs: compromised or backdoored models, unsafe serialisation formats, poisoned training or fine-tuning data, and manipulated content in vector stores used for retrieval.

**Controls:**

- Inventory AI components (models, versions, providers, plug-ins, datasets).
- Obtain models from trusted sources; verify integrity; prefer safe serialisation formats.
- Assess vendors' supply chain practices in [due diligence](../../assessments/vendor-due-diligence.md).
- Control who can add content to retrieval sources; monitor for anomalous changes.
- Keep libraries and frameworks patched.

### Excessive agency (OWASP LLM03)

**What it is.** An AI system, especially an agent, has more functionality, permissions or autonomy than needed, so errors or manipulation lead to harmful actions. OWASP moved this up to third place in 2026, reflecting incidents involving agentic systems [2].

**Controls:**

- Grant the minimum tools and permissions necessary; prefer read-only where possible.
- Use separate, scoped identities for agents rather than broad user or admin credentials.
- Require human approval for high-impact actions.
- Rate-limit and log agent actions; make them reversible where possible.
- Assess new agentic features before enabling them (see [Operate](../lifecycle/06-operate.md)).

### Other risks

- **Unbounded consumption (LLM06):** cost spikes and denial of service. Set quotas, budgets and alerts.
- **Misinformation (LLM07):** confident but false outputs driving decisions. Human review, grounding in authoritative sources, training. See [capabilities and limitations](../foundations/capabilities-and-limitations.md).

## Mapping to MITRE ATLAS

MITRE ATLAS organises AI attacks by adversary tactic, in the style of ATT&CK [3]. Security operations teams can use it to:

- extend threat models to AI-specific techniques (for example, prompt injection, data poisoning, model evasion and exfiltration via AI interfaces);
- map detection and response coverage for AI systems alongside existing ATT&CK mappings;
- draw on its case studies when designing red-team exercises.

Use OWASP for "what to build and test against" and ATLAS for "how adversaries operate" in your threat modelling.

## Controls by deployment type

| Control area | Off-the-shelf AI tools (SaaS) | Applications you build |
|---|---|---|
| Identity and access | Single sign-on; role-based access; conditional access; restrict to approved users | Scoped service identities; least privilege for tools and data |
| Data | Permission hygiene; sensitivity labels; data loss prevention; data terms in contract | Data classification in retrieval; input filtering; output filtering; secrets management |
| Configuration | Disable unneeded connectors, plug-ins, web access; review new features | Guardrails; system prompt hygiene; content filters |
| Logging and monitoring | Enable audit logs; integrate with security monitoring | Log prompts, outputs and tool calls with appropriate privacy controls |
| Testing | Scenario testing during pilot; review vendor security reports | Threat modelling; red-teaming against OWASP list; regression tests after model changes |
| Supply chain | Vendor due diligence; sub-processor review | Component inventory; trusted sources; integrity checks |
| Incident response | AI incident categories; vendor escalation contacts | Same, plus ability to roll back models or disable features |

## Secure AI development guidance (summary)

The NCSC-led guidelines organise practices into four stages [4]:

1. **Secure design:** understand risks and threat model; design for security alongside function and performance.
2. **Secure development:** secure the supply chain; document data, models and prompts; manage technical debt.
3. **Secure deployment:** protect infrastructure and models; develop incident management; release responsibly.
4. **Secure operation and maintenance:** monitor behaviour and inputs; follow a secure-by-design approach to updates; share lessons.

The UK Code of Practice for the Cyber Security of AI sets 13 principles for developers, system operators and other stakeholders [5]. ETSI EN 304 223 builds on both and maps its requirements to lifecycle stages from design through to retirement [6].

## Security checklist for adopting an AI tool

- [ ] Tool assessed against relevant OWASP 2026 risks.
- [ ] Single sign-on and access restrictions in place.
- [ ] Permissions on searchable content reviewed.
- [ ] Unneeded connectors, plug-ins and web access disabled.
- [ ] Human confirmation required for consequential actions.
- [ ] Audit logging enabled and integrated with monitoring.
- [ ] Data loss prevention or equivalent controls applied where available.
- [ ] Vendor security evidence reviewed (certifications, penetration testing, incident history, change notification).
- [ ] AI incident categories added to incident response.
- [ ] Process to review new vendor features before enabling.

## Variations by organisation size

**Small organisations.** Prioritise: use business-tier tools with single sign-on; turn on multi-factor authentication; check sharing permissions on your file storage; disable features you do not need; and tell staff never to paste passwords, keys or client secrets into AI tools. Ask your IT provider to review the admin settings.

**Enterprises.** Integrate AI into threat modelling, security architecture review, security operations and red-teaming. Maintain an AI component inventory. Align with ETSI EN 304 223 or the UK Code where customers or regulators expect it.

## Common pitfalls

- **Assuming the vendor handles everything.** Configuration, permissions and use are your responsibility.
- **Relying on prompt instructions as a security boundary.** Instructions can be overridden by injection.
- **Granting agents broad credentials.** Scope identities tightly.
- **Ignoring indirect injection.** Any content the AI reads is an attack surface.
- **Not re-testing after model changes.** Behaviour, including safety behaviour, can shift.

## Sources

1. OWASP GenAI Security Project, *OWASP GenAI LLM Top 10 2026*. https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/
2. Imperva, *OWASP LLM Top 10 2026: What Changed and Why*, 2026 (secondary analysis of the OWASP list). https://www.imperva.com/blog/owasp-llm-top-10-2026-what-changed/
3. MITRE, *MITRE ATLAS Fact Sheet*. https://atlas.mitre.org/pdf-files/MITRE_ATLAS_Fact_Sheet.pdf
4. National Cyber Security Centre, *Guidelines for secure AI system development*, 27 November 2023. https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development
5. Hunton Andrews Kurth, *UK publishes AI Cyber Security Code of Practice and Implementation Guide*, 2025. https://hunton.com/privacy-and-information-security-law/uk-publishes-ai-cyber-security-code-of-practice-and-implementation-guide
6. techUK, *ETSI sets out new European standard to strengthen AI cyber security*, January 2026. https://www.techuk.org/resource/etsi-sets-out-new-european-standard-to-strengthen-ai-cyber-security.html
7. National Institute of Standards and Technology, *Generative Artificial Intelligence Profile*, NIST AI 600-1, July 2024. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf

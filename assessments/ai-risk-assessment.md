# AI risk assessment

> **Who this is for:** Use case owners, risk and compliance teams, data protection officers, security teams and anyone who must approve an AI use case. Scaled for small organisations (the screening questionnaire alone may be enough for low-risk uses) and for enterprises with formal risk functions.
> **Last reviewed:** 2026-10

This page gives you a complete, copyable template for assessing the risks of one specific AI use case. Part A is a short screening questionnaire that sets the depth of assessment and flags when you need a data protection impact assessment (DPIA), legal review or a check against high-risk regulatory categories. Part B is the full assessment: system description, stakeholders, a risk register scored by likelihood and impact, risk categories aligned with the NIST AI Risk Management Framework and its Generative AI Profile, controls, residual risk and sign-off. Use it at the [Assess](../docs/lifecycle/02-assess.md) stage, update it at the end of a [pilot](../docs/lifecycle/04-pilot.md), and review it during [operation](../docs/lifecycle/06-operate.md). It complements, and does not replace, a DPIA or legal advice.

## How to use this template

1. Complete **Part A** for every proposed use case. It takes 15–20 minutes.
2. Part A tells you whether you need a **light**, **standard** or **full** assessment, and which specialist reviews are triggered.
3. Complete **Part B** to the depth indicated. Light assessments complete sections B1, B3 (top risks only) and B7.
4. Store the completed assessment with the use case record in your [use case register](../toolkits/use-case-register-template.md).
5. Review at the dates set in B7, and whenever the tool, model, data, users or purpose change materially.

> **Guidance:** Copy everything from "Part A" downwards into your own document. Replace [bracketed placeholders]. Delete guidance blockquotes once complete.

---

## Part A: Screening questionnaire

**Use case:** [name, register ID]
**Completed by:** [name, role] **Date:** [date]

Answer Yes, No or Unsure. Treat **Unsure as Yes** until resolved.

### A1. Data protection triggers

| # | Question | Answer |
|---|---|---|
| A1.1 | Will the AI tool process personal data (in prompts, connected data, or outputs)? | |
| A1.2 | Will it process special category data, or criminal offence data? | |
| A1.3 | Will it be used to evaluate, score or profile individuals? | |
| A1.4 | Could outputs contribute to decisions with legal or similarly significant effects on individuals (e.g. employment, access to services, credit, benefits, housing)? | |
| A1.5 | Will it monitor individuals systematically (including staff)? | |
| A1.6 | Will it process data about vulnerable people (e.g. children, patients, people in financial difficulty)? | |
| A1.7 | Will personal data be used to train or fine-tune a model? | |
| A1.8 | Will personal data be transferred to, or accessible from, another country? | |
| A1.9 | Is this an innovative use of technology (new to your organisation or using AI in a novel way)? | |

**DPIA trigger.** Under UK GDPR, a DPIA is required before processing likely to result in a high risk to individuals; the ICO's guidance lists criteria including innovative technology (which it says includes AI), and says that if you are unsure you should carry out a DPIA [1]. Under UK and EU GDPR Article 35(3), a DPIA is always required for systematic and extensive evaluation with legal or similarly significant effects, large-scale processing of special category or criminal offence data, and large-scale systematic monitoring of public areas [1].

- If **A1.3, A1.4 or A1.7** is Yes, or **A1.2** is Yes at any scale, or **A1.9 is Yes together with any other A1 answer**: **DPIA required or strongly indicated.** Refer to your data protection officer or lead.
- If **A1.1** is Yes and no other trigger applies: record a DPIA screening decision (why a full DPIA is or is not needed).

### A2. Legal and regulatory triggers

| # | Question | Answer |
|---|---|---|
| A2.1 | Is the use case in, or close to, an EU AI Act high-risk area (biometrics, critical infrastructure, education, employment and worker management, access to essential private or public services including credit scoring and some insurance, law enforcement, migration and border control, justice and democratic processes)? | |
| A2.2 | Could it fall within a practice prohibited under the EU AI Act (e.g. manipulative techniques, social scoring, certain emotion recognition in workplaces or education, untargeted scraping of facial images)? | |
| A2.3 | Will people interact with it without necessarily knowing it is AI, or will it generate synthetic images, audio, video or text published to inform the public? | |
| A2.4 | Is it used in a regulated activity (e.g. financial services, healthcare, legal services, public sector decision-making) with sector-specific rules? | |
| A2.5 | Will outputs be published, sent to customers, or relied on externally? | |
| A2.6 | Could outputs infringe intellectual property, or will you rely on owning outputs? | |
| A2.7 | Could the use case affect people differently according to protected characteristics (e.g. under the Equality Act 2010 in Great Britain)? | |
| A2.8 | Does a contract, licence or client agreement restrict how you may use data or AI? | |

**High-risk regulatory check.** If **A2.1 or A2.2** is Yes: refer for legal review before any further work. The EU AI Act applies to organisations placing AI systems on the EU market or using them in the EU, and to some outside the EU whose outputs are used there; obligations differ for providers and deployers. Annex III high-risk obligations were deferred by the Digital Omnibus on AI to 2 December 2027, and Annex I (product-embedded) obligations to 2 August 2028; prohibitions have applied since 2 February 2025, and transparency obligations under Article 50 apply from 2 August 2026 [2][3]. See the [regulation overview](../docs/governance/regulation-overview.md).

**Legal review trigger.** If **any of A2.3–A2.8** is Yes: refer to legal or compliance (in small organisations, an external adviser) for a view on the specific question.

### A3. Impact and exposure

| # | Question | Answer |
|---|---|---|
| A3.1 | Could an error cause physical, psychological, financial or reputational harm to a person? | |
| A3.2 | Will the AI act autonomously (send, publish, change records, execute code or transactions) without human approval of each action? | |
| A3.3 | Will it process confidential business information, trade secrets or client data? | |
| A3.4 | Will it be exposed to untrusted content (web pages, inbound emails, uploaded documents) that could contain malicious instructions? | |
| A3.5 | Will more than [100] people use it, or will it serve the public directly? | |
| A3.6 | Is the tool or model from a supplier without completed [vendor due diligence](vendor-due-diligence.md)? | |

### A4. Screening result

| Result | Condition | Assessment depth |
|---|---|---|
| **Low** | All answers No, except possibly A1.1 with a recorded DPIA screening decision | **Light** (B1, B3 top 3 risks, B7) |
| **Medium** | One to three Yes answers in A2 or A3, no DPIA or high-risk trigger | **Standard** (all of Part B) |
| **High** | DPIA trigger, high-risk regulatory trigger, A3.1 and A3.2 both Yes, or four or more Yes answers in A2–A3 | **Full** (all of Part B, with specialist input, senior sign-off and DPIA where required) |

**Screening result:** [Low / Medium / High]
**Specialist reviews triggered:** [DPIA / legal review / high-risk regulatory check / security review / equality impact assessment / vendor due diligence / none]

---

## Part B: Full assessment

### B1. System description

| Field | Response |
|---|---|
| Use case name and register ID | [ ] |
| Business owner (accountable) | [name, role] |
| Purpose and intended outcome | [what problem it solves; how success is measured] |
| Out-of-scope uses | [uses that are explicitly not permitted] |
| AI tool, model and version | [product, model, version or release date if known] |
| Supplier(s) | [vendor; due diligence reference] |
| Deployment | [SaaS / cloud platform / on-premises / embedded in existing software] |
| Data inputs | [sources, categories, sensitivity; link to [data readiness](data-readiness.md)] |
| Outputs | [type, where they go, who sees them] |
| Degree of autonomy | [suggests / drafts for human approval / acts with human monitoring / acts autonomously] |
| Human oversight | [who reviews what, when, with what authority to override] |
| Users | [roles, number, training required] |
| Integrations | [systems connected; permissions granted to the AI] |
| Your role under the EU AI Act, if applicable | [provider / deployer / both / not applicable; confirmed by legal?] |

### B2. Stakeholders

> **Guidance:** Include people affected by outputs, not only users. Consider consulting affected groups (staff, unions or employee representatives, customers, service users) for medium- and high-risk use cases.

| Stakeholder | Interest or how affected | Consulted? (how, when) | Concerns raised |
|---|---|---|---|
| [Users, e.g. customer service staff] | [ ] | [ ] | [ ] |
| [Affected people, e.g. customers] | [ ] | [ ] | [ ] |
| [Data protection officer] | [ ] | [ ] | [ ] |
| [Security] | [ ] | [ ] | [ ] |
| [Legal / compliance] | [ ] | [ ] | [ ] |
| [HR / employee representatives] | [ ] | [ ] | [ ] |

### B3. Risk identification by category

Work through every category. For each, note whether it applies and, if so, add risks to the register (B4). The categories combine the trustworthiness characteristics in the NIST AI Risk Management Framework [4] with the twelve risks identified in NIST's Generative AI Profile (NIST AI 600-1) [5], plus security risks from the OWASP Top 10 for LLM Applications [6] and organisational risks.

| Category | Source alignment | Prompting questions | Applies? |
|---|---|---|---|
| **Accuracy and reliability** (including confabulation, i.e. confident but false output) | AI RMF: valid and reliable. GAI Profile: confabulation | Could false or fabricated outputs be relied on? How would errors be detected? | |
| **Harmful bias and fairness** | AI RMF: fair, with harmful bias managed. GAI Profile: harmful bias or homogenisation | Could outputs disadvantage groups? Could they make outputs or ideas more uniform? | |
| **Privacy and data protection** | AI RMF: privacy-enhanced. GAI Profile: data privacy | Could personal data leak, be inferred, or be used beyond its purpose? | |
| **Information security** | AI RMF: secure and resilient. GAI Profile: information security. OWASP: prompt injection, sensitive information disclosure, excessive agency, improper output handling | Could untrusted content manipulate the AI? Could it reveal data to the wrong people? Does it have more permissions than needed? | |
| **Safety** | AI RMF: safe | Could outputs or actions lead to physical or psychological harm? | |
| **Transparency and accountability** | AI RMF: accountable and transparent | Do affected people know AI is involved? Is responsibility for outcomes clear? | |
| **Explainability** | AI RMF: explainable and interpretable | Can users understand and justify outputs where needed (e.g. to a customer or regulator)? | |
| **Human-AI configuration** (over-reliance, automation bias, inappropriate trust) | GAI Profile: human-AI configuration | Will reviewers genuinely check outputs, or rubber-stamp them? Is the oversight design realistic for the volume? | |
| **Information integrity** | GAI Profile: information integrity | Could the system produce or spread misleading content, including content published externally? | |
| **Harmful content** | GAI Profile: dangerous, violent or hateful content; obscene, degrading and/or abusive content; CBRN information or capabilities | Could it generate harmful or inappropriate material in this context? | |
| **Intellectual property** | GAI Profile: intellectual property | Could outputs infringe others' rights? Could your confidential material be exposed? | |
| **Value chain and component integration** | GAI Profile: value chain and component integration. OWASP: supply chain | Do you depend on third-party models, plug-ins or data you cannot inspect? What happens if the supplier changes the model? | |
| **Environmental impact** | GAI Profile: environmental impacts | Is the energy and resource cost proportionate to the benefit? Does it matter to your sustainability commitments? | |
| **Cost and resource consumption** | OWASP: unbounded consumption | Could usage costs run away? Are there limits? | |
| **Legal and regulatory compliance** | (organisational) | Does the use comply with the AI Act, data protection, consumer, equality, sector rules and contracts? | |
| **People and workforce** | (organisational) | Effects on workload, skills, roles, morale, employee relations? | |
| **Operational and continuity** | (organisational) | What if the tool is unavailable, changes behaviour, or the supplier exits? | |
| **Reputational** | (organisational) | How would this look if reported publicly? | |

### B4. Risk register

#### Scoring scales

**Likelihood (L)**

| Score | Label | Guide |
|---|---|---|
| 1 | Rare | Could happen only in exceptional circumstances |
| 2 | Unlikely | Not expected, but possible |
| 3 | Possible | Might happen occasionally |
| 4 | Likely | Will probably happen in most periods of use |
| 5 | Almost certain | Expected to happen frequently |

**Impact (I)**

| Score | Label | People | Organisation |
|---|---|---|---|
| 1 | Negligible | No noticeable effect | Trivial cost or disruption |
| 2 | Minor | Short inconvenience, easily put right | Small cost; internal only |
| 3 | Moderate | Distress or detriment requiring effort to put right | Noticeable cost, complaint, or minor regulatory interest |
| 4 | Major | Significant detriment to individuals' rights, finances or wellbeing | Significant cost, regulatory action likely, media attention |
| 5 | Severe | Serious or irreversible harm | Severe financial, legal or reputational damage |

> **Guidance:** Adjust the organisational impact descriptors to match your enterprise risk framework (for example, add monetary thresholds). Generative AI outputs vary from run to run, so "Likelihood" should consider how often a failure would occur across all expected use, not in a single test.

**Risk rating = L × I**

| Rating | Level | Treatment expectation |
|---|---|---|
| 1–4 | Low | Accept with monitoring |
| 5–9 | Medium | Reduce where proportionate; owner accepts residual risk |
| 10–14 | High | Must reduce before go-live; senior sign-off of residual risk |
| 15–25 | Very high | Do not proceed unless reduced; executive or board decision |

**Heat map**

| Likelihood ↓ / Impact → | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **5** | 5 M | 10 H | 15 VH | 20 VH | 25 VH |
| **4** | 4 L | 8 M | 12 H | 16 VH | 20 VH |
| **3** | 3 L | 6 M | 9 M | 12 H | 15 VH |
| **2** | 2 L | 4 L | 6 M | 8 M | 10 H |
| **1** | 1 L | 2 L | 3 L | 4 L | 5 M |

#### Register

| ID | Category | Risk description (cause → event → consequence) | Inherent L | Inherent I | Inherent rating | Controls (see B5) | Residual L | Residual I | Residual rating | Owner | Review date |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | [Accuracy] | [ ] | | | | | | | | | |
| R2 | | | | | | | | | | | |
| R3 | | | | | | | | | | | |

#### Example entries (fictional)

> **Guidance:** These rows are illustrative, for a fictional use case in which an AI assistant drafts replies to customer enquiries that staff review before sending. Replace them with your own.

| ID | Category | Risk description | Inh. L | Inh. I | Inh. | Controls | Res. L | Res. I | Res. |
|---|---|---|---|---|---|---|---|---|---|
| R1 | Accuracy | Assistant drafts a reply stating an incorrect policy or entitlement → staff send without checking → customer acts on wrong information, complaint or liability | 4 | 3 | 12 H | C1 ground on approved knowledge base; C2 mandatory human review with checklist; C3 sample quality audit weekly | 2 | 3 | 6 M |
| R2 | Privacy | Staff paste another customer's details into a prompt → data appears in wrong reply | 2 | 4 | 8 M | C4 acceptable use training; C5 tool configured so prompts are not used for training and are retained per policy; C2 review | 1 | 4 | 4 L |
| R3 | Security | Inbound customer email contains hidden instructions → assistant follows them (prompt injection) → inappropriate content in draft | 3 | 3 | 9 M | C6 assistant has no ability to send or access other records; C2 review; C7 security testing with injection examples | 2 | 2 | 4 L |
| R4 | Human-AI configuration | High volumes lead staff to approve drafts without reading → errors pass through | 4 | 3 | 12 H | C3 audit; C8 volume targets adjusted to allow review time; C9 manager monitoring of edit rates | 3 | 3 | 9 M |

Real legal cases illustrate the accuracy and accountability risks. In *Mata v. Avianca* (US District Court, S.D.N.Y., 2023), lawyers were sanctioned USD 5,000 after filing a brief containing case citations fabricated by a chatbot [7]. In *Moffatt v. Air Canada* (2024 BCCRT 149), a Canadian tribunal held the airline liable for negligent misrepresentation by its website chatbot, rejecting the argument that the chatbot was responsible for its own statements [8].

### B5. Controls

> **Guidance:** Controls should be specific and testable. "Train staff" is weak; "Staff complete module 2 of the AI training plan before access is granted; completion recorded in the LMS" is testable.

| Control ID | Control description | Type | Risks addressed | Owner | Evidence it is working | Status |
|---|---|---|---|---|---|---|
| C1 | [ ] | [Preventive / Detective / Corrective] | [R1, R4] | [ ] | [ ] | [Planned / In place / Tested] |
| C2 | | | | | | |

**Control checklist (consider each):**

- [ ] Human review proportionate to impact, with time allowed and authority to reject
- [ ] Least-privilege permissions for the AI tool and its connectors
- [ ] No autonomous actions with external effect unless specifically assessed
- [ ] Grounding on approved, current sources, with citations shown to users
- [ ] Vendor data settings configured (no training on your data where required, retention aligned with policy)
- [ ] Data minimisation: only necessary data in scope; sensitive areas excluded
- [ ] Input and output filtering where available and relevant
- [ ] Testing before go-live: accuracy against a test set, prompt injection, permission leakage, bias where relevant
- [ ] Transparency to affected people (notice that AI is used, where appropriate or required)
- [ ] Logging and monitoring sufficient to investigate incidents
- [ ] Incident reporting route known to users
- [ ] Usage and cost limits
- [ ] Training completed before access
- [ ] Fallback procedure if the tool is unavailable or withdrawn
- [ ] Re-assessment triggers defined (model change, new data, new users, incident)

### B6. Residual risk summary

| Measure | Value |
|---|---|
| Number of risks identified | [ ] |
| Highest inherent rating | [ ] |
| Highest residual rating | [ ] |
| Residual risks rated High or Very high | [list IDs] |
| Within agreed risk appetite? | [Yes / No; reference risk appetite statement] |
| Conditions for proceeding | [e.g. pilot limited to 20 users; DPIA signed off; weekly audit for first 8 weeks] |

### B7. Sign-off and review

| Role | Name | Decision | Date | Signature or record |
|---|---|---|---|---|
| Business owner | [ ] | [Approve / Approve with conditions / Reject] | | |
| Data protection officer or lead (if personal data) | [ ] | | | |
| Security lead (if standard or full) | [ ] | | | |
| Legal / compliance (if triggered) | [ ] | | | |
| Senior risk owner (if any residual High) | [ ] | | | |
| Executive or board (if any residual Very high) | [ ] | | | |

**Review schedule:** [e.g. end of pilot; 3 months after go-live; then annually]
**Re-assessment triggers:** change of model or supplier; new data sources; new user groups; change of purpose; incident or near miss; new regulatory requirement.

> **Guidance for small organisations:** One person may hold several roles. That is acceptable if recorded. Where no internal legal or data protection expertise exists, note where external advice was taken.

---

## Interpreting results and what to do next

| Outcome | Meaning | Next steps |
|---|---|---|
| All residual risks Low | Acceptable with monitoring | Proceed. Set review date. Monitor via usage and incident logs. |
| Highest residual Medium | Acceptable if owner accepts and controls are in place | Proceed once controls are "in place". Re-check at end of pilot. |
| Any residual High | Proceed only with senior acceptance and conditions | Narrow scope (fewer users, less sensitive data, more oversight) or add controls; pilot with close monitoring; re-score with evidence. |
| Any residual Very high | Not acceptable as designed | Redesign the use case (e.g. assist rather than decide; remove autonomous actions) or stop. Record the decision in the register. |

## Related

- [Risk management](../docs/governance/risk-management.md), [data protection](../docs/governance/data-protection.md), [security](../docs/governance/security.md), [regulation overview](../docs/governance/regulation-overview.md)
- [Vendor due diligence](vendor-due-diligence.md) and [data readiness](data-readiness.md)
- [Risk and compliance pathway](../docs/pathways/risk-and-compliance.md)

## Sources

1. Information Commissioner's Office, *When do we need to do a DPIA?* (notes guidance under review following the Data (Use and Access) Act). https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/when-do-we-need-to-do-a-dpia
2. European Commission presentation material, *AI Act* (European Digital Innovation Hubs), December 2024 (Annex III areas and original timeline). https://european-digital-innovation-hubs.ec.europa.eu/system/files/2024-12/01_Martin%20Ulbrich_Presentation%20AI%20Act.pdf
3. Regulation (EU) 2026/1744 (Digital Omnibus on AI), in force 27 July 2026. https://eur-lex.europa.eu/eli/reg/2026/1744/oj ; summary: National Law Review, *EU Digital Omnibus on AI Enters into Force*, 2026. https://natlawreview.com/article/eu-digital-omnibus-ai-enters-force
4. NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, January 2023. https://doi.org/10.6028/NIST.AI.100-1
5. NIST, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*, NIST AI 600-1, July 2024. https://doi.org/10.6028/NIST.AI.600-1
6. OWASP GenAI Security Project, *OWASP Top 10 for LLM Applications 2025*. https://genai.owasp.org/llm-top-10/
7. LawSites, *Court imposes sanctions on lawyers who filed bogus cases after relying on ChatGPT for legal research*, June 2023 (*Mata v. Avianca*, No. 22-cv-01461, S.D.N.Y.). https://www.lawnext.com/2023/06/court-imposes-sanctions-on-lawyers-who-filed-bogus-cases-after-relying-on-chatgpt-for-legal-research.html
8. McCarthy Tétrault, *Moffatt v. Air Canada: misrepresentation by an AI chatbot*, February 2024 (2024 BCCRT 149). https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot

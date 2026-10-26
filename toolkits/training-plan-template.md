# Training plan template

> **Who this is for:** HR, learning and development, programme leads and managers who need to plan AI training for staff. Includes AI literacy, role-based curricula, and a light version for small organisations.
> **Last reviewed:** 2026-10

This template helps you plan AI training that is role-based, proportionate and recorded. It sets out a training needs analysis, a foundation AI literacy module for everyone, role-based curricula (everyday users, managers, leaders, technical teams, data teams, risk and compliance, and people approving or overseeing AI outputs), delivery methods, assessment, records and evaluation. It also explains the EU AI Act's AI literacy obligation for providers and deployers, including its amendment in 2026. Guidance notes in blockquotes explain the choices; replace [bracketed placeholders]. Use it before a [Pilot](../docs/lifecycle/04-pilot.md) and expand it when you [Scale](../docs/lifecycle/05-scale.md).

## AI literacy and the EU AI Act

> **Guidance:** Read this if your organisation provides or deploys AI systems in the EU, or offers AI systems whose outputs are used in the EU. Take legal advice on whether and how the Act applies to you.

- **The obligation.** Article 4 of the EU AI Act places an AI literacy obligation on **providers and deployers** of AI systems. As originally enacted, it required them to take measures to ensure, to their best extent, a sufficient level of AI literacy among their staff and other persons dealing with the operation and use of AI systems on their behalf, taking into account their technical knowledge, experience, education and training, the context of use, and the people on whom the systems are used [1][2]. A deployer is, broadly, an organisation using an AI system under its authority in a professional context, so an organisation whose staff use AI tools at work is likely to be a deployer.
- **When it applied.** The obligation has applied since **2 February 2025** [1]. The European Commission's Q&A on AI literacy (May 2025) indicated that no particular certificate is required, that organisations should keep records of the measures they take, and that simply pointing staff to a tool's instructions will generally not be sufficient [3]. National supervision and enforcement were expected from August 2026 [1][3].
- **The 2026 amendment.** The Digital Omnibus on AI, Regulation (EU) 2026/1744, entered into force on 27 July 2026 [4]. Commentary on the final text reports that Article 4 was retained but recalibrated: providers and deployers must take measures to support the development of AI literacy of their staff, rather than ensuring a sufficient level for each individual, and the Commission and Member States are to support and facilitate those efforts [5][6]. Check the consolidated text on EUR-Lex for the exact wording before relying on it.
- **What this means in practice.** AI literacy remains a legal obligation for in-scope providers and deployers. A documented, role-appropriate training programme, of the kind this template describes, is a reasonable way to demonstrate the measures you have taken. Deployers of high-risk AI systems have additional obligations, including assigning human oversight to people with the necessary competence and training.
- **Outside the EU.** Even where the Act does not apply, AI literacy is good practice and is reflected in frameworks such as the UK Government's AI Playbook, whose principles include understanding AI and its limitations and building the necessary skills [7].

---

## [Organisation name] AI training plan

| | |
|---|---|
| **Owner** | [name, role] |
| **Version and date** | [ ] |
| **Period covered** | [ ] |
| **Linked policies** | [AI policy](ai-policy-template.md); [acceptable use policy](acceptable-use-policy.md) |

## 1. Objectives

By [date]:

1. [100]% of staff with access to AI tools have completed the foundation AI literacy module before access.
2. Each role group has completed its role-based module.
3. Training records are kept for every person, including contractors acting on our behalf.
4. [Confidence / safe-use indicators] improve as measured by [survey / assessment].

## 2. Training needs analysis

> **Guidance:** Identify who uses or oversees AI, how, and what they already know. The Commission's Q&A suggests tailoring to staff knowledge, context and risk [3]. A short survey plus conversations with managers is usually enough.

| Role group | Number | AI tools / uses | Risk level of use | Current knowledge (low/med/high) | Priority |
|---|---|---|---|---|---|
| Everyday users | [ ] | [ ] | [ ] | [ ] | [ ] |
| Managers | [ ] | [ ] | [ ] | [ ] | [ ] |
| Leaders | [ ] | [ ] | [ ] | [ ] | [ ] |
| Developers | [ ] | [ ] | [ ] | [ ] | [ ] |
| Data teams | [ ] | [ ] | [ ] | [ ] | [ ] |
| IT and platform | [ ] | [ ] | [ ] | [ ] | [ ] |
| Risk, legal, data protection | [ ] | [ ] | [ ] | [ ] | [ ] |
| People overseeing AI outputs that affect individuals | [ ] | [ ] | [ ] | [ ] | [ ] |
| Contractors / third parties acting for us | [ ] | [ ] | [ ] | [ ] | [ ] |

## 3. Curriculum

### 3.1 Foundation: AI literacy (everyone with access to AI tools)

**Format:** [e-learning / live session], [60–90] minutes. **Required before access.** **Refresh:** [annually / on policy change].

| Module | Learning outcomes | Resources |
|---|---|---|
| F1 What AI tools are | Explain in plain terms how generative AI produces outputs; distinguish types of AI tool | [What are AI tools](../docs/foundations/what-are-ai-tools.md); [video script 01](../videos/scripts/01-what-ai-tools-can-and-cannot-do.md) |
| F2 Capabilities and limitations | Describe tasks AI tools tend to help with and where they fail; recognise fabricated content ("hallucination") and bias | [Capabilities and limitations](../docs/foundations/capabilities-and-limitations.md) |
| F3 Our rules | Apply the acceptable use policy: approved tools, data classification, prohibited uses | [Acceptable use policy](acceptable-use-policy.md) |
| F4 Safe everyday use | Verify outputs; protect data; spot prompt injection; disclose appropriately; report problems | [Video script 03](../videos/scripts/03-safe-everyday-use.md); [everyday users pathway](../docs/pathways/everyday-users.md) |
| F5 Using tools well | Write clear prompts; give context; iterate; use the prompt library | [Prompt library](prompt-library-template.md) |
| F6 Check | Short knowledge check ([10] questions; pass mark [80]%) | [ ] |

### 3.2 Role-based modules

| Role group | Module | Learning outcomes | Format and duration | Prerequisite |
|---|---|---|---|---|
| **Everyday users** | U1 Applying AI to your tasks | Identify suitable tasks in own role; use approved prompts; measure own time and quality | Workshop by team, [90] min | F1–F6 |
| **Managers** | M1 Leading AI use in your team | Set expectations; review AI-assisted work; spot over-reliance; support reluctant and enthusiastic staff; handle concerns | Live session, [2] h | F1–F6 |
| **Leaders** | L1 AI for decision-makers | Evaluate AI proposals and evidence; understand risk appetite, governance and regulation; ask the right questions of business cases | Briefing, [2] h | F1–F2 |
| **Developers** | D1 AI coding assistants | Use assistants effectively; review generated code for correctness, security and licensing; avoid leaking secrets | Hands-on, [3] h | F1–F6 |
| **Data teams** | DT1 AI with data | Data readiness; retrieval-augmented generation; evaluation; data protection in analytics and fine-tuning | Hands-on, [3] h | F1–F6 |
| **IT and platform** | IT1 Configuring and securing AI tools | Admin controls; identity; logging; data loss prevention; AI-specific threats (e.g. prompt injection) | Technical, [3] h | F1–F6 |
| **Risk, legal, data protection** | R1 Assessing AI | Use the AI risk assessment and vendor due diligence; DPIA triggers; regulatory landscape | Workshop, [3] h | F1–F2 |
| **Oversight roles** | O1 Meaningful human oversight | Recognise automation bias; know when and how to override; document decisions | Scenario-based, [2] h | F1–F6 + role module |
| **Champions** | C1 Champion skills | Coach peers; curate prompts; collect feedback and issues | Workshop, [2] h + monthly community | U1 |

> **Guidance:** Durations are indicative. Small organisations can combine modules into a single session per role. Developers, data teams and IT may need tool-specific training from the [tool guides](../docs/tools/tool-guides/README.md).

### 3.3 Ongoing learning

- Monthly [tips email / community of practice session]
- Updates when tools, models or policies change
- Case studies from incidents and near misses (anonymised)

## 4. Delivery plan

| Wave | Audience | Modules | Dates | Delivery | Trainer | Status |
|---|---|---|---|---|---|---|
| Pilot | Pilot participants, their managers | F, U1, M1 | [ ] | [ ] | [ ] | |
| Wave 1 | [ ] | [ ] | [ ] | [ ] | [ ] | |
| Wave 2 | [ ] | [ ] | [ ] | [ ] | [ ] | |
| New starters | All | F + role module | Within [n] weeks of start | [ ] | [ ] | |

**Accessibility:** provide captions and transcripts for video content, accessible documents, and alternative formats on request.

## 5. Assessment and records

> **Guidance:** Keep records of who completed what and when. This supports AI literacy evidence under the EU AI Act where it applies, and your own assurance. Records need not be elaborate: a spreadsheet is acceptable for small organisations.

| Field | Example |
|---|---|
| Name | [ ] |
| Role group | [ ] |
| Employee / contractor | [ ] |
| Modules completed | [F1–F6, U1] |
| Completion date | [ ] |
| Assessment result | [ ] |
| Refresh due | [ ] |
| Access granted (date) | [ ] |

## 6. Evaluation

| Level | Measure | Method | When |
|---|---|---|---|
| Reaction | Was training useful and relevant? | Post-session survey | After each session |
| Learning | Do people know the rules and limitations? | Knowledge check | End of module |
| Behaviour | Are people verifying outputs and following data rules? | Manager observation; quality audits; incident trends | 1–3 months |
| Results | Are safe-use and value indicators improving? | Usage, incidents, [measuring value](../docs/measurement/measuring-value.md) | Quarterly |

## 7. Budget

| Item | Cost |
|---|---|
| Content development or licences | [ ] |
| Trainer time | [ ] |
| Participant time ([hours] × [people] × [rate]) | [ ] |
| Platform / LMS | [ ] |
| **Total** | [ ] |

## 8. Approval

| Role | Name | Date |
|---|---|---|
| Sponsor | | |
| HR / L&D | | |

---

## Light version for small organisations

1. **One 90-minute session for everyone** covering F1–F5, using your own examples.
2. **A short follow-up** for anyone in a specialist role (for example, whoever configures the tools).
3. **A spreadsheet** recording who attended, when, and what they covered.
4. **A refresher** each year or when tools or rules change.

## Sources

1. Travers Smith, *The EU AI Act's AI literacy requirement: key considerations*. https://www.traverssmith.com/knowledge/knowledge-container/the-eu-ai-acts-ai-literacy-requirement-key-considerations/
2. Data Protection Report (Norton Rose Fulbright), *AI literacy under the EU AI Act* (Article 4 text and scope). https://www.dataprotectionreport.com/?p=6523
3. Hunton Andrews Kurth, *European Commission publishes Q&A on AI literacy*, May 2025. https://www.hunton.com/privacy-and-cybersecurity-law-blog/european-commission-publishes-q-a-on-ai-literacy
4. Regulation (EU) 2026/1744 (Digital Omnibus on AI), EUR-Lex record (dated 8 July 2026; in force 27 July 2026). https://eur-lex.europa.eu/eli/reg/2026/1744/oj
5. Cuatrecasas, *The Digital Omnibus on AI: How does it impact employment relations?*, 2026. https://www.cuatrecasas.com/en/spain/labor-and-employment/art/digital-omnibus-on-ai-how-does-it-impact-employment-relations
6. IAPP, *EU AI Act literacy changes may complicate more than simplify compliance*, September 2026. https://iapp.org/news/a/eu-ai-act-literacy-changes-may-complicate-more-than-simplify-compliance
7. UK Government, *Artificial Intelligence Playbook for the UK Government*, 10 February 2025. https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html

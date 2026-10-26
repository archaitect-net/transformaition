# Data protection and AI

> **Who this is for:** Data protection officers, privacy and compliance professionals, IT and platform teams, HR, and business owners whose AI use involves personal data.
> **Last reviewed:** 2026-10

> **This is not legal advice.** This page summarises the EU GDPR and UK GDPR as they apply to AI tools, as of October 2026. UK law changed during 2026 under the Data (Use and Access) Act 2025, and EU reforms are under negotiation. Take qualified advice for your situation.

Most AI tools process personal data: in prompts, in the documents they search, in the outputs they generate, and in logs of how staff use them. Data protection law therefore applies to most AI adoption, whether or not any AI-specific law does. This page covers the questions that come up most often: lawful basis, data protection impact assessments (DPIAs), automated decision-making (including the 2026 UK changes), data minimisation, international transfers, processor contracts, regulator guidance, and the particular considerations when AI tools are used to monitor, or generate data about, employees.

## Where personal data appears in AI tool use

| Point | Examples | Questions |
|---|---|---|
| Inputs | Staff paste emails, CVs or case notes into a prompt | Is this use within the purpose for which the data was collected? |
| Retrieval | Assistant searches mailboxes, files, CRM records | Do access permissions reflect need-to-know? |
| Outputs | Summaries, profiles, recommendations about individuals | Are outputs accurate? Do they create new personal data (inferences)? |
| Logs and telemetry | Prompt and response logs; usage analytics | Who can see them? How long are they kept? Are they used to monitor staff? |
| Vendor processing | Hosting, abuse monitoring, model improvement | Is the vendor a processor or a controller for any purpose? Is data used for training? |

## Lawful basis

Every processing purpose needs a lawful basis under Article 6 of the GDPR or UK GDPR, and processing of special category data (for example health, ethnicity, trade union membership) needs an Article 9 condition as well.

| Basis | Typical AI use | Notes |
|---|---|---|
| Legitimate interests | Internal productivity tools processing staff and customer data | Requires a documented balancing test (a legitimate interests assessment). The EDPB has said legitimate interest cannot be assumed as a default basis for AI models and must be shown through the three-step test, taking account of reasonable expectations and mitigations [1] |
| Contract | Processing necessary to deliver a service the individual has requested | Only where AI processing is genuinely necessary for the contract |
| Legal obligation or public task | Public bodies performing statutory functions | Needs a clear legal basis in law |
| Consent | Rarely appropriate for employees, because of the power imbalance; sometimes used for optional customer features | Must be freely given, specific, informed and withdrawable |

**UK change:** the Data (Use and Access) Act 2025 added "recognised legitimate interests" (Article 6(1)(ea) and Annex 1 of UK GDPR) for a limited list of purposes, in force from 5 February 2026, for which no balancing test is needed [2]. These are specific purposes (such as certain security and safeguarding purposes) and will not usually cover general AI productivity use; check the list before relying on it.

**EU proposals:** the Commission's November 2025 Digital Omnibus proposal would add an express legitimate-interest provision for AI development and operation. As of October 2026 it was still being negotiated and the Council's text differed from the Commission's [3]. Until adopted, the existing GDPR applies.

## Data protection impact assessments

A DPIA is required where processing is likely to result in a high risk to individuals (Article 35). AI use often triggers one because it may involve new technology, large-scale processing, profiling, systematic monitoring, or special category data. Regulators' lists of high-risk processing commonly include innovative technology and employee monitoring.

### DPIA screening questions for AI tools

- [ ] Will the tool process special category or criminal offence data?
- [ ] Will outputs be used to make or inform decisions about individuals?
- [ ] Will the tool profile individuals or infer characteristics?
- [ ] Will it process data about vulnerable people (children, patients, employees)?
- [ ] Will it monitor people systematically (including staff use of the tool)?
- [ ] Is the processing large-scale?
- [ ] Is data transferred outside the UK or EEA?
- [ ] Is the technology new to the organisation, or used in a novel way?

If several answers are yes, a DPIA is likely needed. Many organisations choose to do a short DPIA for any AI tool with access to internal data, since it is also a useful structured risk assessment.

### What an AI DPIA should cover

- Description of processing, data flows, and the vendor's role.
- Necessity and proportionality: could the purpose be met with less data?
- Risks to individuals: inaccuracy, unfair outcomes, unexpected disclosure, loss of control, chilling effects on staff.
- Measures: access controls, minimisation, retention, human review, transparency, opt-outs, vendor terms.
- Consultation with the DPO and, where appropriate, affected people or their representatives.
- Residual risk and sign-off. If high residual risk remains, prior consultation with the regulator is required.

The UK regulator's AI and data protection guidance includes DPIA considerations specific to AI; note that the regulator states it is under review following the Data (Use and Access) Act [4].

## Automated decision-making

### EU GDPR (Article 22)

Individuals have the right not to be subject to a decision based solely on automated processing, including profiling, that produces legal or similarly significant effects, unless an exception applies (contract necessity, authorisation by law, or explicit consent), with safeguards including the right to obtain human intervention, express a view and contest the decision.

### UK GDPR (Articles 22A to 22D, from 5 February 2026)

The Data (Use and Access) Act 2025 replaced Article 22 in UK GDPR with new Articles 22A to 22D, which came into force on 5 February 2026 [5]. In summary [2]:

- Significant decisions based solely on automated processing are **permitted** for non-special-category data, provided safeguards are in place.
- Where **special category data** is involved, such decisions remain restricted unless explicit consent or another specified condition applies.
- Safeguards include informing individuals about such decisions and enabling them to make representations, obtain human intervention and contest the decision.
- A decision is "solely automated" if there is no meaningful human involvement.
- Decisions taken before 5 February 2026 remain under the old rules [5].

The regulator consulted on updated automated decision-making and profiling guidance between 31 March and 29 May 2026; final guidance was awaited at the time of writing [6]. A statutory code of practice on AI and automated decision-making is also being prepared (see [regulation overview](regulation-overview.md)).

### Practical implications

- **Meaningful human involvement** means a reviewer with the authority, competence, information and time to change the outcome, not a rubber stamp. Monitor whether reviewers actually depart from AI recommendations.
- **Generative AI tools used as aids** (drafting, summarising) usually do not make decisions themselves, but can become part of a decision process, for example summarising job applications. Assess the whole process.
- **Safeguards must be operational**, not only described in a privacy notice.

## Data minimisation and purpose limitation

- Configure tools to access only the data sources needed for the use case.
- Fix over-broad permissions before enabling AI search across repositories.
- Set retention periods for prompts, outputs and logs in line with your retention schedule.
- Give staff clear rules on what may not be entered into AI tools (for example, special category data, unless the use case is approved for it).
- Do not reuse data collected for one purpose (for example, performance reviews) in AI tools for an incompatible purpose.
- Prefer configurations where the vendor does not use your data to train models; check the actual contract terms.

## International transfers

Cloud AI services often process data in several countries. Transfers of personal data outside the UK or EEA need a transfer mechanism.

| Mechanism | EU GDPR | UK GDPR |
|---|---|---|
| Adequacy / data bridge | Commission adequacy decisions, including the EU-US Data Privacy Framework for certified US organisations | UK adequacy regulations, including the UK extension to the EU-US Data Privacy Framework |
| Contractual clauses | EU Standard Contractual Clauses | International Data Transfer Agreement or UK Addendum to EU SCCs |
| Transfer risk assessment | Required when relying on SCCs | Required; from 5 February 2026 the UK uses a "data protection test" (whether protection is not materially lower) under the Data (Use and Access) Act [7] |

The EU General Court upheld the EU-US Data Privacy Framework in September 2025; the decision was appealed to the Court of Justice in October 2025 and the appeal was pending at the last check [8]. Organisations relying on the Framework should have a contingency plan.

Questions for vendors: where is data processed and stored, including for abuse monitoring and support? Which sub-processors are used, and where? Can you choose a data region?

## Processor contracts

Where an AI vendor processes personal data on your behalf, it is usually a processor, and Article 28 requires a contract covering, among other things: processing only on documented instructions; confidentiality; security; sub-processor controls; assistance with data subject rights and DPIAs; deletion or return at the end; and audit rights.

AI-specific points to check:

- [ ] Does the vendor use customer data (prompts, outputs, files) to train or improve models? Can this be excluded?
- [ ] Does the vendor act as a controller for any purpose (for example, abuse monitoring, product improvement)? If so, is that transparent?
- [ ] Retention of prompts, outputs and logs, including any retention for safety monitoring.
- [ ] Human review of customer data by vendor staff: when and under what controls?
- [ ] Sub-processors, including model providers behind the service.
- [ ] Notification of changes to processing, models or sub-processors.
- [ ] Data location and transfer mechanisms.
- [ ] Support for data subject access, rectification and erasure requests across logs and outputs.

See [vendor due diligence](../../assessments/vendor-due-diligence.md).

## Regulator guidance

- **UK:** The regulator's *Guidance on AI and data protection* covers accountability, transparency, lawfulness, accuracy, fairness and automated decision-making, with an annex on fairness across the AI lifecycle; it is marked as under review following the Data (Use and Access) Act [4]. On 30 September 2026 the ICO became the Information Commission [9]; existing guidance remains the reference point while updates are made.
- **EU:** The European Data Protection Board's Opinion 28/2024 (17 December 2024) addresses when AI models can be considered anonymous, the use of legitimate interest for developing and deploying models, and the consequences for deployers of models developed with unlawfully processed data [1]. National supervisory authorities have also published AI guidance.

## Employees: monitoring and AI

Employees are a special case because of the power imbalance and the volume of data AI tools generate about how people work.

**Two distinct issues:**

1. **AI tools that generate data about staff use.** Prompt logs, usage dashboards and productivity analytics are personal data. Using them to evaluate individuals is a form of monitoring.
2. **AI tools used to monitor or manage staff.** Performance analytics, task allocation, sentiment analysis. In the EU, AI used to monitor or evaluate workers' performance and behaviour is listed as high-risk under the AI Act, and emotion inference from biometric data in the workplace is prohibited (see [regulation overview](regulation-overview.md)).

The UK regulator's guidance on monitoring workers (October 2023) states that monitoring must be necessary and proportionate, workers should be told about its nature, extent and reasons, the least intrusive means should be used, and a DPIA is required where monitoring is likely to be high risk [10]. Research commissioned by the regulator for that guidance found that 70% of the public would consider monitoring by an employer intrusive (a survey of 1,012 UK adults; evidence: Limited, single survey) [10].

### Checklist for employee data

- [ ] Purposes for using AI usage logs are defined and limited (for example, security and licence management, not individual performance) unless otherwise lawfully established and communicated.
- [ ] Staff are told what is logged, who can see it, and how long it is kept.
- [ ] A DPIA covers monitoring aspects.
- [ ] Workers' representatives are consulted where required by law or agreement.
- [ ] Any AI used in recruitment, performance or discipline is assessed as potentially high-risk and subject to human review.
- [ ] Access to logs is restricted and audited.

## Variations by organisation size

**Small organisations.** Focus on four things: use business-tier tools whose terms exclude training on your data; tell staff what data must not be entered; check where the vendor processes data; and do a short DPIA if the tool touches client or staff personal data at any scale. Many small organisations do not need a formal DPO, but someone should own data protection.

**Enterprises.** Integrate AI into the existing privacy programme: DPIA triggers in the AI intake process, vendor assessment templates with AI-specific questions, records of processing updated for AI tools, and coordination between privacy, security and HR on monitoring.

## Common pitfalls

- **Assuming "enterprise" means "no data risk".** Check actual terms on training, retention and human review.
- **Permissions sprawl.** AI search reveals over-shared data.
- **Using logs for performance management without telling anyone.**
- **Treating human review as a formality.** It may not count as meaningful involvement.
- **Forgetting outputs.** Inferences about individuals are personal data too, and must be accurate.

## Sources

1. CMS, *EDPB Opinion 28/2024: key takeaways on processing personal data in the context of AI models*, December 2024. https://cms.law/en/int/legal-updates/edpb-opinion-28-2024-key-takeaways-on-processing-personal-data-in-the-context-of-ai-models
2. Bratby Law, *Data (Use and Access) Act 2025: changes now in force*, 2026. https://bratby.law/data-use-and-access-act-2025-commencement/
3. EUTechReg Research, *GDPR reform in the Digital Omnibus* (dossier, updated October 2026). https://research.eutechreg.com/dossiers/gdpr-reform-digital-omnibus/
4. Information Commissioner's Office, *Guidance on AI and data protection*. https://www.ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection
5. The Data (Use and Access) Act 2025 (Commencement No. 6 and Transitional and Saving Provisions) Regulations 2026, SI 2026/82. https://www.legislation.gov.uk/cy/uksi/2026/82/made
6. Information Commissioner's Office, *ICO consultation on the draft guidance about automated decision-making including profiling*, March 2026. https://ico.org.uk/about-the-ico/ico-and-stakeholder-consultations/2026/03/ico-consultation-on-the-draft-guidance-about-automated-decision-making-including-profiling/
7. DLA Piper, *UK: Commencement of the data protection provisions in the Data (Use and Access) Act*, February 2026. https://privacymatters.dlapiper.com/2026/02/uk-commencement-of-the-data-protection-provisions-in-the-data-use-and-access-act/
8. WilmerHale, *European Court of Justice to Review Challenge to EU-U.S. Data Privacy Framework*, 1 December 2025. https://www.wilmerhale.com/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20251201-european-court-of-justice-to-review-challenge-to-eu-us-data-privacy-framework
9. Lewis Silkin, *What the ICO's transformation into the Information Commission means for your organisation*, 29 September 2026. https://www.lewissilkin.com/insights/2026/09/29/what-the-icos-transformation-into-the-information-commission-means-for-your-orga-102o3ni
10. Information Commissioner's Office, *ICO publishes guidance to ensure lawful monitoring in the workplace*, 3 October 2023. https://cy.ico.org.uk/about-the-ico/media-centre/news-and-blogs/2023/10/ico-publishes-guidance-to-ensure-lawful-monitoring-in-the-workplace

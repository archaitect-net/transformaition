# Regulation overview

> **Who this is for:** Leaders, legal, compliance, risk and data protection professionals, and anyone who needs to know which AI-related laws may apply to their organisation.
> **Last reviewed:** 2026-10

> **This is not legal advice.** This page summarises laws and regulatory developments as of October 2026 for orientation only. AI regulation is changing quickly: several items below were amended, delayed or replaced during 2026, and others are still being negotiated. Check primary sources and take qualified advice before relying on anything here.

AI-specific regulation now exists in several jurisdictions, but most obligations that affect organisations adopting AI tools still come from existing law: data protection, consumer protection, equality and employment law, intellectual property, and sector rules. This page covers the EU AI Act (including the 2026 "Digital Omnibus" amendments that delayed high-risk obligations), the UK's approach, the US federal and state picture, other jurisdictions briefly, sector regulators, and how to track changes. Each section flags what is settled and what remains uncertain.

## Summary table

| Jurisdiction | AI-specific law? | Status as of October 2026 | Key point for adopters |
|---|---|---|---|
| European Union | Yes: AI Act, Regulation (EU) 2024/1689, amended by Regulation (EU) 2026/1744 | In force; phased application. Prohibitions and AI literacy apply; transparency duties apply from 2 August 2026; high-risk obligations delayed to December 2027 and August 2028 | Deployers have obligations, not only providers |
| United Kingdom | No general AI Act | Principles-based, regulator-led approach; data protection reforms in force in 2026; statutory ICO code on AI and automated decision-making in preparation | Existing law (especially UK GDPR as amended) does the work |
| United States (federal) | No comprehensive federal AI law | December 2025 executive order seeks to challenge state AI laws; federal preemption legislation not enacted | Sector regulators and existing law apply |
| United States (states) | Several states | Texas, California, Illinois laws effective 1 January 2026; Colorado replaced its 2024 Act with a new law effective 1 January 2027 | Check each state where you operate or affect residents |
| South Korea | Yes: AI Basic Act | Effective 22 January 2026 | Obligations for high-impact and generative AI |
| China | Several targeted measures | Labelling measures for AI-generated content effective 1 September 2025 | Labelling duties for providers and platforms |

## European Union: the AI Act

### What it is

The AI Act (Regulation (EU) 2024/1689) is a regulation that applies directly across EU member states. It was published in the Official Journal on 12 July 2024 and applies in phases [1]. It has extraterritorial reach: it can apply to providers and deployers outside the EU where AI systems are placed on the EU market or their output is used in the EU.

### Roles

| Role | Who | Example |
|---|---|---|
| Provider | Develops an AI system or general-purpose AI model, or has one developed, and places it on the market or puts it into service under its own name | A software company selling an AI recruitment tool |
| Deployer | Uses an AI system under its authority, except for purely personal non-professional use | An employer using that recruitment tool |
| Importer and distributor | Bring systems into the EU market or make them available | Resellers |

Most organisations adopting AI tools are **deployers**. A deployer can become a provider, with heavier obligations, if it puts its own name on a high-risk system, makes a substantial modification, or changes a system's intended purpose so that it becomes high-risk.

### Risk categories

| Category | Examples | Consequence |
|---|---|---|
| Prohibited practices (Article 5) | Manipulative techniques causing significant harm; social scoring; emotion inference from biometric data in workplaces and education (with narrow medical and safety exceptions) [2]; certain biometric uses. The 2026 amendments add prohibitions on systems for generating non-consensual intimate imagery and child sexual abuse material, applying from 2 December 2026 [3] | Banned |
| High-risk (Article 6 and Annexes I and III) | Safety components of regulated products (Annex I); listed use areas (Annex III), including employment and worker management, education, access to essential services, credit scoring, and certain public-sector uses [4] | Strict requirements for providers; specific duties for deployers |
| Transparency obligations (Article 50) | Chatbots; generative AI outputs; deepfakes; emotion recognition | Disclosure and marking duties |
| General-purpose AI models | Large foundation models | Obligations for model providers (documentation, copyright policy; extra duties for systemic-risk models) |
| Minimal risk | Most other uses | No specific obligations beyond AI literacy and other law |

For employment, Annex III covers AI used for recruitment and selection (for example, filtering applications or evaluating candidates) and for decisions affecting terms of work, promotion, termination, task allocation based on behaviour or traits, and monitoring or evaluating performance [4]. The Commission published draft guidelines on high-risk classification for consultation in May 2026; at the time of writing they were not confirmed as final [4].

### Deployer obligations for high-risk systems (Article 26)

When the high-risk obligations apply, deployers must, in summary [5]:

- use systems in line with the provider's instructions;
- assign human oversight to people with the necessary competence, training, authority and support;
- ensure input data under their control is relevant and sufficiently representative;
- monitor operation, and report risks and serious incidents to the provider and authorities;
- keep automatically generated logs under their control for at least six months, unless other law requires otherwise;
- inform workers' representatives and affected workers before using a high-risk system in the workplace;
- use provider information to carry out data protection impact assessments where required;
- inform individuals when an Annex III system makes or assists decisions about them.

Certain deployers (including public bodies) must also carry out a fundamental rights impact assessment before use.

### AI literacy (Article 4)

Article 4 has applied since 2 February 2025 to providers and deployers of all AI systems, not only high-risk ones. The 2026 amendments reworded it: providers and deployers must take measures to support the development of AI literacy among their staff and others operating AI systems on their behalf, and the revised text states that it does not require a specific level of literacy for any individual [3][6]. The Commission and member states are to support implementation [6]. In practice, organisations within scope should be able to show what they have done, such as role-based training, guidance and records. See [Scale](../lifecycle/05-scale.md) and the [training plan template](../../toolkits/training-plan-template.md).

### Transparency (Article 50)

From 2 August 2026, providers must design chatbots so that people are told they are interacting with AI (unless obvious), and must mark generative AI outputs in a machine-readable, detectable way. Deployers must disclose deepfakes and AI-generated or manipulated text published to inform the public on matters of public interest (unless it has undergone human review and editorial responsibility), and must inform people exposed to emotion recognition or biometric categorisation [7]. Generative AI systems already on the market before 2 August 2026 have until 2 December 2026 to meet the machine-readable marking requirement [3]. The Commission published a voluntary Code of Practice on marking and labelling AI-generated content on 10 June 2026 [8].

### Timeline of application dates (as amended)

The Digital Omnibus on AI, Regulation (EU) 2026/1744, was signed on 8 July 2026, published in the Official Journal on 24 July 2026 and entered into force on 27 July 2026 [3]. The table reflects the amended timeline.

| Date | What applies | Status |
|---|---|---|
| 1 August 2024 | AI Act enters into force | Settled |
| 2 February 2025 | Prohibited practices; AI literacy (Article 4, reworded in 2026) | Applies |
| 2 August 2025 | General-purpose AI model obligations; governance; penalties regime | Applies |
| 2 August 2026 | Transparency obligations (Article 50); most remaining provisions not otherwise deferred | Applies |
| 2 December 2026 | Machine-readable marking deadline for generative systems already on the market; new prohibitions on non-consensual intimate imagery and CSAM generation | Upcoming (new date set by the 2026 amendment) |
| 2 August 2027 | Compliance deadline for general-purpose AI models placed on the market before 2 August 2025; national AI regulatory sandboxes operational | Upcoming |
| 2 December 2027 | High-risk requirements for Annex III systems (previously 2 August 2026) | Upcoming (delayed by the 2026 amendment) |
| 2 August 2028 | High-risk requirements for Annex I systems in regulated products (previously 2 August 2027) | Upcoming (delayed by the 2026 amendment) |
| 2 August 2030 | High-risk systems used by public authorities that were already on the market | Upcoming; secondary sources did not report a change, so verify against the consolidated text |

Sources: [1][3][9].

### Other features of the 2026 amendments

- **Smaller companies.** The amendments extend some SME relief (for example, simplified documentation and size-sensitive fine calculation) to a new "small mid-cap" category [3][9]. Secondary sources report different thresholds for this category, so check the definition in the Official Journal text before relying on it.
- **Registration of exempted systems.** Reporting on the political agreement indicated that providers who decide an Annex III system is not high-risk under the Article 6(3) filter must still register it [9]. Verify in the final text.

### Penalties

Article 99 sets maximum fines of up to EUR 35 million or 7% of worldwide annual turnover for prohibited practices; up to EUR 15 million or 3% for breaches of most operator obligations (including deployer obligations); and up to EUR 7.5 million or 1% for supplying incorrect or misleading information to authorities, in each case whichever is higher [10]. For SMEs (and, under the 2026 amendments, small mid-caps) the lower of the two amounts applies [3]. Member states set national enforcement arrangements.

### Related EU developments under negotiation

A separate Digital Omnibus proposal (COM(2025) 837), published in November 2025, would amend the GDPR and ePrivacy rules, including a proposed express legitimate-interest basis for AI development and operation and rules on residual special category data in AI training. As of mid-October 2026 the Council had not been confirmed as agreeing a negotiating mandate and trilogues had not been reported as started [11]. Treat these proposals as uncertain; the current GDPR applies. See [data protection](data-protection.md).

The General-Purpose AI Code of Practice, published 10 July 2025, has chapters on transparency, copyright, and safety and security; it concerns model providers rather than deployers, but its copyright chapter is relevant to [intellectual property](intellectual-property.md) questions [12].

## United Kingdom

### Overall approach

The UK has no general AI statute. Its approach, confirmed in the government's February 2024 response to the AI regulation white paper, asks existing regulators to interpret and apply five cross-sectoral principles within their remits: safety, security and robustness; appropriate transparency and explainability; fairness; accountability and governance; and contestability and redress [13]. Key regulators were asked to publish their strategic approaches to AI by 30 April 2024 [13].

### Status of AI legislation

- A private member's bill, the Artificial Intelligence (Regulation) Bill [HL], fell at the end of the parliamentary session in April 2026 without a second reading, according to a regulatory tracker [14].
- In July 2026 the government pointed to a sector-by-sector approach and a forthcoming "Regulating for Growth" bill, without a timetable for a dedicated AI bill [14].
- **Uncertainty:** the government has previously signalled possible targeted legislation for the most capable models. As of October 2026 no such bill had been introduced. Watch for announcements.

### Data protection reforms affecting AI

- The **Data (Use and Access) Act 2025** reformed the UK GDPR's rules on automated decision-making. The new Articles 22A to 22D came into force on 5 February 2026, replacing the previous general restriction on solely automated significant decisions with a permissive regime subject to safeguards, while keeping tighter restrictions where special category data is used [15][16]. See [data protection](data-protection.md).
- The **Data Protection Act 2018 (Code of Practice on Artificial Intelligence and Automated Decision-Making) Regulations 2026** (SI 2026/425) came into force on 12 May 2026 and require the regulator to prepare a statutory code of practice on AI and automated decision-making [14]. The code is in drafting; a draft for consultation was reported as targeted for spring 2027 [14]. Timing may move.
- The ICO consulted on updated automated decision-making and profiling guidance from 31 March to 29 May 2026; final guidance had not been published at the time of writing [17].
- On 30 September 2026 the Information Commissioner's Office became the **Information Commission**, a corporate body replacing the single Commissioner [18]. References to "the ICO" in existing guidance should be read accordingly.

### Other UK developments

- **Cyber security.** The UK government published a voluntary Code of Practice for the Cyber Security of AI on 31 January 2025, with 13 principles [19]. See [security](security.md).
- **Copyright.** On 18 March 2026 the government published its report and impact assessment on copyright and AI. It did not propose a new text and data mining exception for AI training and did not change the law [20]. See [intellectual property](intellectual-property.md).

## United States

### Federal

- There is no comprehensive federal AI law governing general AI use [21].
- An executive order of 11 December 2025 declared a national policy favouring "minimally burdensome" AI standards and directed the Department of Justice to challenge state AI laws; the order does not itself preempt state law [21]. A DOJ AI litigation task force was established; as of April 2026, a research note reported no complaints filed and no state AI law invalidated by a federal court [21].
- In July 2025 the Senate removed a proposed ten-year moratorium on state AI law enforcement from a budget bill before it was enacted [21].
- Federal agencies, including consumer protection, employment and financial regulators, apply existing law to AI uses within their remits.
- **Uncertainty:** federal preemption legislation has been proposed but not enacted. The relationship between federal policy and state laws may change through litigation or legislation.

### States (selected)

| State | Law | Status | Applies to |
|---|---|---|---|
| Colorado | SB 24-205 (Colorado AI Act, 2024) | Effective date was delayed to 30 June 2026, then the Act was repealed and replaced before it took effect [22] | n/a |
| Colorado | SB 26-189, Automated Decision-Making Technology | Signed 14 May 2026; effective 1 January 2027, with Attorney General rulemaking required [22][23] | Developers and deployers of automated decision-making technology used in consequential decisions (education, employment, housing, lending, insurance, health care, essential government services): documentation, consumer notices, explanation of adverse decisions within 30 days, data access and correction, human review, three-year record keeping; Attorney General enforcement with a cure period; no new private right of action [23] |
| Texas | Responsible Artificial Intelligence Governance Act (TRAIGA) | Effective 1 January 2026 [21] | Attorney General enforcement; no private right of action |
| California | SB 53, Transparency in Frontier AI Act | Main provisions effective 1 January 2026 [21] | Large frontier model developers |
| California | CCPA regulations on automated decision-making technology, risk assessments and cybersecurity audits | Approved 23 September 2025; effective 1 January 2026; ADMT requirements for significant decisions apply from 1 January 2027 [24] | Businesses subject to the CCPA |
| Illinois | HB 3773 (amending the Illinois Human Rights Act) | Effective 1 January 2026 [21] | AI in employment decisions; private right of action |
| New York City | Local Law 144 | In effect since 2023 [21] | Automated employment decision tools (bias audits and notices) |

**Uncertainty on Colorado:** one law firm analysis reports that a federal court stayed enforcement of Colorado's AI legislation in April 2026 and that the stay extends to the successor law [22]. We could not confirm this from a primary source; check the current position.

Many other states have enacted or are considering AI laws, particularly on employment, deepfakes, chatbots and government use. A state-by-state tracker is essential if you operate across the US.

## Other jurisdictions (brief)

- **South Korea.** The AI Basic Act took effect on 22 January 2026. It includes obligations for "high-impact" AI (assessment, explanation, human oversight, user protection), labelling for generative AI outputs, and a domestic representative requirement for some foreign providers; the ministry indicated a one-year grace period before fines [25].
- **China.** Measures for labelling AI-generated synthetic content took effect on 1 September 2025, requiring visible and metadata labels from service providers and duties for platforms and users [26]. China also has earlier rules on generative AI services and algorithmic recommendation.
- **Elsewhere.** Many countries have AI strategies, voluntary frameworks or sector guidance. Check for AI-specific rules in each jurisdiction where you operate, and remember that data protection laws in most jurisdictions apply to AI processing of personal data.

## Sector regulators

AI obligations frequently come from sector rules rather than AI laws. Examples of areas where regulators apply existing frameworks to AI:

| Sector | Typical concerns | Questions to ask |
|---|---|---|
| Financial services | Model risk, consumer outcomes, explainability, operational resilience, outsourcing | Does our model risk policy cover AI tools? Do outsourcing rules apply to the vendor? |
| Health and care | Medical device regulation, clinical safety, patient data | Is the tool a medical device? What clinical safety standards apply? |
| Employment | Discrimination, consultation, monitoring | Have we assessed equality impacts and consulted where required? |
| Public sector | Transparency, procurement, administrative law, equality duties | Do algorithmic transparency or public-sector equality duties apply? |
| Legal and professional services | Professional conduct, confidentiality, competence | What does our professional regulator say about AI use? |
| Communications and online services | Online safety, content moderation | Do online safety duties cover AI-generated content on our service? |

Check the published AI guidance of your sector regulators in each jurisdiction.

## How to track changes

AI regulation changed materially during 2026 and will continue to change. A tracking routine:

1. **Assign an owner** for regulatory horizon scanning (legal, compliance or the governance lead).
2. **Monitor primary sources:**
   - EU: EUR-Lex for consolidated texts, the European Commission's AI Act pages and the AI Act Service Desk, and the AI Office for guidelines and codes of practice.
   - UK: legislation.gov.uk, GOV.UK (DSIT), the Information Commission, and your sector regulators.
   - US: Federal Register, state legislature websites, state attorneys general, and federal agency guidance.
3. **Use reputable trackers** from law firms, standards bodies and academic centres as secondary sources, and verify against primary texts before acting.
4. **Record applicability.** For each development, note whether it applies, to which use cases, and by when, in the [use case register](../../toolkits/use-case-register-template.md) or a regulatory register.
5. **Trigger reviews.** New obligations should trigger review of affected risk assessments and DPIAs (see [Operate](../lifecycle/06-operate.md)).
6. **Review this summary** at least every six months, and update the `Last reviewed` date.

## Sources

1. Regulation (EU) 2024/1689 (Artificial Intelligence Act), OJ L, 2024/1689, 12.7.2024; text via SpringLex. https://www.springlex.eu/en/packages/ai-act/ai-act-regulation/article-99/
2. Future of Privacy Forum, *Red Lines under EU AI Act: Unpacking the prohibition of emotion recognition in the workplace and education institutions*, March 2026. https://fpf.org/blog/red-lines-under-eu-ai-act-unpacking-the-prohibition-of-emotion-recognition-in-the-workplace-and-education-institutions/
3. ActuIA, *AI Act: obligations in force and delays under omnibus 2026/1744*, 2026 (summary of Regulation (EU) 2026/1744, with link to EUR-Lex CELEX:32026R1744). https://www.actuia.com/en/news/ai-act-obligations-in-force-and-delays-under-omnibus-2026-1744/
4. Faegre Drinker, *Draft Commission guidelines on high-risk AI: implications for the workplace*, 15 June 2026. https://www.faegredrinker.com/en/insights/publications/2026/6/draft-commission-guidelines-on-high-risk-ai-implications-for-the-workplace
5. European Commission AI Act Service Desk, *Article 26: Obligations of deployers of high-risk AI systems*. https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26
6. KI-Campus, *EU AI Act: AI Omnibus recalibrates Article 4 – AI literacy remains mandatory*, 2026. https://ki-campus.org/en/blog/eu-ai-act-ai-omnibus-recalibrates-article-4-ai-literacy-remains-mandatory
7. Future of Life Institute, *The EU AI Act's Transparency Rules: A Practical Guide to Article 50*, May 2026. https://artificialintelligenceact.eu/transparency-rules-article-50/
8. European Commission, *Commission publishes Code of Practice on marking and labelling AI-generated content*, 10 June 2026. https://digital-strategy.ec.europa.eu/en/news/commission-publishes-code-practice-marking-and-labelling-ai-generated-content
9. Future of Life Institute, *Digital Omnibus on AI* (AI Act Explorer). https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/ ; and Noze, *AI Act: the Digital Omnibus postpones high-risk rules and adds new prohibitions*, 2026. https://www.noze.it/en/insights/ai-act-digital-omnibus-2026/
10. RTR (Austrian regulatory authority) AI Service Desk, *Sanctions under the AI Act*. https://www.rtr.at/rtr/service/ki-servicestelle/ai-act/Sanctions.en.html
11. EUTechReg Research, *GDPR reform in the Digital Omnibus* (dossier, updated October 2026). https://research.eutechreg.com/dossiers/gdpr-reform-digital-omnibus/
12. European Commission, *The General-Purpose AI Code of Practice*. https://digital-strategy.ec.europa.eu/en/policies/gpai-code-practice
13. Society for Computers and Law, *UK government publishes response to AI White Paper*, February 2024. https://www.scl.org/uk-government-publishes-response-to-ai-white-paper/
14. Vorp Labs, *UK AI regulatory updates* (tracker), accessed October 2026. https://vorplabs.com/ai-regulatory-updates/united-kingdom
15. The Data (Use and Access) Act 2025 (Commencement No. 6 and Transitional and Saving Provisions) Regulations 2026, SI 2026/82. https://www.legislation.gov.uk/cy/uksi/2026/82/made
16. DLA Piper, *UK: Commencement of the data protection provisions in the Data (Use and Access) Act*, February 2026. https://privacymatters.dlapiper.com/2026/02/uk-commencement-of-the-data-protection-provisions-in-the-data-use-and-access-act/
17. Information Commissioner's Office, *ICO consultation on the draft guidance about automated decision-making including profiling*, March 2026. https://ico.org.uk/about-the-ico/ico-and-stakeholder-consultations/2026/03/ico-consultation-on-the-draft-guidance-about-automated-decision-making-including-profiling/
18. Lewis Silkin, *What the ICO's transformation into the Information Commission means for your organisation*, 29 September 2026. https://www.lewissilkin.com/insights/2026/09/29/what-the-icos-transformation-into-the-information-commission-means-for-your-orga-102o3ni
19. Hunton Andrews Kurth, *UK publishes AI Cyber Security Code of Practice and Implementation Guide*, 2025. https://hunton.com/privacy-and-information-security-law/uk-publishes-ai-cyber-security-code-of-practice-and-implementation-guide
20. DLA Piper, *TDM and training AI models: UK Government publishes report and impact assessment*, March 2026. https://www.dlapiper.com/insights/publications/2026/03/tdm-and-training-ai-models-uk-government-publishes-report-and-impact-assessment
21. Cloud Security Alliance, *State AI Laws Take Hold as Federal Preemption Stalls* (research note), April 2026. https://labs.cloudsecurityalliance.org/research/csa-research-note-us-ai-regulation-preemption-compliance-202/
22. Eckert Seamans, *Colorado Repeals and Replaces Its Landmark AI Statute: What Businesses Need to Know*, 2026. https://www.eckertseamans.com/legal-updates/colorado-repeals-and-replaces-its-landmark-ai-statute-what-businesses-need-to-know
23. Colorado General Assembly, *SB26-189 Automated Decision-Making Technology*. https://leg.colorado.gov/bills/SB26-189
24. California Privacy Protection Agency, *California Finalizes Regulations to Strengthen Consumers' Privacy*, 23 September 2025. https://www.cppa.ca.gov/announcements/2025/20250923.html
25. Cooley, *South Korea's AI Basic Act: Overview and Key Takeaways*, 27 January 2026. https://www.cooley.com/news/insight/2026/2026-01-27-south-koreas-ai-basic-act-overview-and-key-takeaways
26. Loeb & Loeb, *China's AI Labeling Measures and Mandatory National Standards Take Effect September 1*, March 2025. https://www.loeb.com/en/insights/publications/2025/03/chinas-ai-labeling-measures-and-mandatory-national-standards-take-effect-september-1

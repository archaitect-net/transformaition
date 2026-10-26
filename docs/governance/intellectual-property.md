# Intellectual property and confidentiality

> **Who this is for:** Legal and compliance teams, procurement, developers, marketing and creative teams, and leaders concerned about ownership, infringement and confidentiality when using AI tools.
> **Last reviewed:** 2026-10

> **This is not legal advice.** Intellectual property law differs by jurisdiction and is being tested in courts and policy reviews. The position described here is as of October 2026 and may change. Take qualified advice for specific decisions.

Using AI tools raises four practical IP questions for organisations: can we lawfully put this material into the tool, who (if anyone) owns what comes out, could the output infringe someone else's rights, and does using the tool put our confidential information at risk? This page explains the current position in general terms for the UK, EU and US, summarises the state of training data litigation without predicting outcomes, describes vendor indemnities as something to check rather than rely on, and sets out considerations for AI-generated code and open-source licences. It ends with a checklist.

## Inputs: what you put into AI tools

| Input | Risk | Considerations |
|---|---|---|
| Your own content | Low IP risk; confidentiality risk depends on vendor terms | Check whether the vendor may use inputs for training or other purposes |
| Third-party copyright material (articles, reports, images) | Copying into a tool may itself be a reproduction; licence terms may restrict it | Check licences and subscriptions (some prohibit use with AI tools); rely on exceptions only after advice |
| Client or partner material | Contractual confidentiality and permitted-use limits | Check contracts and engagement terms before using client material with AI tools |
| Personal data | Data protection rather than IP | See [data protection](data-protection.md) |
| Trade secrets | Loss of secrecy protection if disclosed without adequate safeguards | Use tools with contractual confidentiality and no training on inputs; restrict access |

## Outputs: who owns them?

Whether AI-generated output is protected by copyright, and who owns it, varies by jurisdiction.

| Jurisdiction | Position (summary) |
|---|---|
| United States | Copyright requires human authorship. Courts upheld the Copyright Office's refusal to register a work created autonomously by an AI system, and the Supreme Court declined to review that decision on 2 March 2026 [1]. The Copyright Office's January 2025 report on copyrightability addresses when outputs created with generative AI can be protected, focusing on the extent of human creative contribution [2] |
| United Kingdom | The Copyright, Designs and Patents Act 1988 contains a provision (section 9(3)) for "computer-generated" works with no human author. In its March 2026 report, the government maintained its view that this protection should be removed unless evidence of its value emerges; no change has yet been made [3] |
| European Union | Copyright protection generally requires the author's own intellectual creation, which implies human creative choices. There is no specific EU rule for AI-generated outputs |

**Practical implications:**
- Do not assume you own exclusive rights in purely AI-generated content. Where ownership matters (brand assets, products, publications), ensure meaningful human creative contribution and document it.
- Vendor terms usually assign or disclaim rights in outputs between you and the vendor; they cannot create copyright where the law does not recognise it.
- For contracts with clients, be clear about what deliverables may include AI-generated material and what rights you can grant.

## Outputs: could they infringe?

AI outputs can, in some circumstances, reproduce or closely resemble existing protected material, including text, images, code and trade marks. The likelihood depends on the tool, the prompt and the content type.

**Controls:**
- Do not prompt tools to reproduce or imitate specific copyrighted works, named artists' styles for commercial use, or trade marks, without advice.
- Review outputs intended for publication or commercial use; use similarity or plagiarism checks where risk is material.
- Use tools with output filtering for known content where available, recognising it is not complete.
- Keep records of prompts and edits for significant outputs.

## Training data litigation: the state of play

Numerous lawsuits challenge whether training AI models on copyrighted material without permission is lawful. Outcomes so far are mixed and fact-specific; none settles the question generally. Selected examples, described neutrally:

| Case | Jurisdiction | Position as of October 2026 |
|---|---|---|
| Getty Images v Stability AI | England and Wales | The High Court ruled in November 2025 largely in Stability AI's favour: the secondary copyright infringement claim failed, and trade mark infringement was found only in limited, historic respects. Getty had dropped its primary training claim because training took place outside the UK. Getty was granted permission to appeal on secondary infringement [4] |
| GEMA v OpenAI | Germany | The Munich Regional Court held on 11 November 2025 that memorisation and reproduction of song lyrics by the models infringed copyright and that the text and data mining exception did not cover this; the ruling was not final [5] |
| Bartz v Anthropic | United States | A 2025 ruling held that training on lawfully acquired books was fair use, but not the acquisition and retention of pirated copies; a USD 1.5 billion class settlement received final approval on 20 July 2026 [6] |
| Kadrey v Meta | United States | In June 2025 the court granted summary judgment to Meta on the plaintiffs' market-harm theory, stressing that the ruling rested on the evidence presented rather than a general finding that training is fair use; the case continued on other claims in 2026 [6] |

Policy is also unsettled. The UK government's March 2026 report did not propose a new text and data mining exception for AI training and left the law unchanged pending further evidence [3]. The US Copyright Office released a pre-publication version of its report on generative AI training in May 2025, with a final version still to come [2]. In the EU, providers of general-purpose AI models must have a policy to comply with EU copyright law, and the General-Purpose AI Code of Practice includes a copyright chapter [7].

**What this means for adopters.** Training litigation mainly targets model developers. Deployers are less directly exposed, but outcomes could affect the availability, cost or terms of tools, and some cases (such as GEMA) concern outputs, which deployers do publish. Monitor developments and check vendor commitments.

## Vendor indemnities: what to check

Several AI vendors offer intellectual property indemnities for claims that outputs infringe third-party rights. These vary widely, so treat them as something to read closely rather than a blanket assurance.

| Question | Why it matters |
|---|---|
| Which products and tiers are covered? | Indemnities often apply only to paid business or enterprise tiers |
| What claims are covered? | Output infringement only, or also claims relating to training data? |
| What conditions apply? | Commonly: using required safety filters, not modifying outputs in certain ways, not intentionally prompting for infringing content |
| What are the caps and exclusions? | Liability caps may limit the value of the indemnity |
| What process applies? | Notification deadlines, control of defence, cooperation duties |
| Does it extend to your customers? | Relevant if you incorporate outputs into products you sell |

See [vendor due diligence](../../assessments/vendor-due-diligence.md).

## Confidentiality

Confidentiality is usually a bigger day-to-day risk than copyright.

- **Vendor terms.** Confirm whether inputs and outputs are used for training or product improvement, how long they are retained, and whether vendor staff can review them.
- **Consumer versus business tiers.** Terms often differ significantly; staff using personal accounts may be bound by consumer terms.
- **Client obligations.** Professional services firms, in particular, should check engagement terms and professional rules before using client material with AI tools.
- **Trade secrets.** Trade secret protection depends on taking reasonable steps to keep information secret; uncontrolled disclosure to third-party services can undermine it.
- **Internal leakage.** AI search can expose confidential material to colleagues who should not see it; see [security](security.md).

## AI-generated code and open-source licences

Coding assistants can produce code that resembles existing open-source code. If that code is subject to a licence (for example, a copyleft licence requiring source disclosure of derivative works, or a licence requiring attribution), using it without complying could breach the licence.

**Considerations:**
- Enable filters that block suggestions matching public code, where your tool offers them, and understand what they do and do not catch.
- Run software composition analysis and licence scanning on repositories, including AI-generated code.
- Apply normal code review to AI-generated code: security, quality and provenance.
- Record your policy on AI-assisted coding, including which tools are approved and for which repositories.
- Consider whether customer contracts restrict or require disclosure of AI-generated code.
- Remember the ownership point above: purely AI-generated code may not attract copyright in some jurisdictions, which may matter for software you license to others.

See the [developers pathway](../pathways/developers.md).

## Checklist

- [ ] Acceptable use policy covers what third-party and client material may be used with AI tools.
- [ ] Vendor terms on input use, retention, output ownership and indemnity have been reviewed.
- [ ] Staff use business-tier tools for work, not personal accounts.
- [ ] Outputs for publication or commercial use are reviewed for similarity to existing works and trade marks.
- [ ] Where ownership matters, human creative contribution is ensured and documented.
- [ ] Coding assistants are configured with public-code filters where available; licence scanning is in place.
- [ ] Client contracts and engagement terms are checked for AI restrictions.
- [ ] Legal monitors litigation and policy developments in your key jurisdictions.

## Variations by organisation size

**Small organisations.** Focus on confidentiality (business-tier tools, no training on your data) and on reviewing anything you publish. If you sell creative or software products, take advice on ownership of AI-assisted work.

**Enterprises.** Coordinate legal, procurement, engineering and marketing. Negotiate indemnity and data terms; integrate licence scanning into development pipelines; maintain guidance per content type (text, images, code, audio).

## Common pitfalls

- **Assuming indemnities cover everything.** Read the conditions and caps.
- **Assuming you own AI outputs.** Ownership may be limited or absent.
- **Ignoring licences on input material.** Subscriptions and databases may prohibit AI use.
- **Confusing training litigation with deployer risk.** They are related but distinct.
- **Forgetting client confidentiality.** Contractual duties can be stricter than law.

## Sources

1. Holland & Knight, *The Final Word: Supreme Court Refuses to Hear Case on AI Authorship*, March 2026. https://www.hklaw.com/en/insights/publications/2026/03/the-final-word-supreme-court-refuses-to-hear-case-on-ai-authorship
2. US Copyright Office, *Copyright and Artificial Intelligence* (Parts 1 to 3). https://copyright.gov/ai/
3. DLA Piper, *TDM and training AI models: UK Government publishes report and impact assessment*, March 2026. https://www.dlapiper.com/insights/publications/2026/03/tdm-and-training-ai-models-uk-government-publishes-report-and-impact-assessment
4. Burges Salmon, *Getty Images v Stability AI: Getty granted permission to appeal*, December 2025. https://www.burges-salmon.com/articles/102lydc/getty-images-v-stability-ai-getty-granted-permission-to-appeal
5. Taylor Wessing, *GEMA v OpenAI, Regional Court of Munich I, 11 November 2025, Case No. 42 O 14139/24*. https://www.taylorwessing.com/de/insights-and-events/insights/2025/11/gema-v-openai
6. National Law Review, *AI vs. Authors Update: Court Approves Historic Anthropic Settlement While Meta Litigation Continues*, 2026. https://natlawreview.com/article/ai-vs-authors-update-court-approves-historic-anthropic-settlement-while-meta
7. European Commission, *The General-Purpose AI Code of Practice*. https://digital-strategy.ec.europa.eu/en/policies/gpai-code-practice

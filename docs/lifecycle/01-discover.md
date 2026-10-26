# Stage 1: Discover

> **Who this is for:** Sponsors, managers, programme leads and anyone asked "what should we do about AI?"
> **Last reviewed:** 2026-10

Discover is where you work out what AI tools could do for your organisation and why it matters. Its job is to produce a long list of opportunities framed as business problems (not as technologies looking for a use), each with an owner, plus an honest picture of how people are already using AI, including tools nobody has sanctioned. This page gives you a workflow, the roles involved, the decision gate to move to Assess, and the pitfalls that most often derail the stage.

## Purpose

- Identify where AI tools might create value: time saved, quality improved, risk reduced, or new capability.
- Frame each opportunity around a problem, an affected group and a measurable outcome.
- Find out what AI use already exists, sanctioned or not, so that governance starts from reality.
- Build enough shared understanding among leaders and staff to make sensible choices in later stages.

## Inputs

- Organisational strategy, objectives and known pain points.
- Any existing AI policy, acceptable use rules or guidance (even informal emails).
- IT data on software in use: SaaS discovery reports, expense claims, browser extension inventories, network logs (handled in line with your monitoring policy; see [data protection](../governance/data-protection.md)).
- Staff knowledge. The people doing the work usually know where the friction is.
- Background reading for participants: [what AI tools are](../foundations/what-are-ai-tools.md) and [capabilities and limitations](../foundations/capabilities-and-limitations.md).

## Activities

1. **Confirm the mandate.** Agree with the sponsor what Discover is for, what is out of scope (for example, customer-facing automated decisions), and when you will report back.
2. **Establish a shared baseline of understanding.** Run a short briefing for participants on what current AI tools can and cannot do. Unrealistic expectations at this stage produce poor opportunities later.
3. **Discover existing and shadow AI use.** "Shadow AI" means AI tools used for work without organisational approval. Combine:
   - an anonymous, non-punitive survey asking which tools people use, for what tasks, and with what kinds of data;
   - IT discovery data on AI services, plug-ins and extensions;
   - conversations with team leads.
   Frame this as learning, not enforcement. People who fear sanctions will under-report, and you will lose the most useful signal: which tasks people found valuable enough to use unapproved tools for.
4. **Collect problems, not solutions.** Run workshops or interviews by function. Ask: which tasks are repetitive, slow, error-prone, or dependent on searching and summarising large volumes of text? Where do people wait for information? Record the problem in the team's words.
5. **Frame each opportunity.** For every candidate, write a one-paragraph problem statement using the template below.
6. **Do a first sense check.** Discard candidates where AI is clearly the wrong tool (for example, where a deterministic rule or a process change would solve it), or where the risk is obviously disproportionate to the benefit at this stage.
7. **Record everything** in a [use case register](../../toolkits/use-case-register-template.md), including shadow uses you found, so nothing is lost between stages.
8. **Report back** to the sponsor with the long list, the shadow AI findings and recommended next steps, including any immediate risk actions.

### Problem-first framing template

| Field | Prompt |
|---|---|
| Problem | What is going wrong, or what is slow, costly or inconsistent today? |
| Who is affected | Which roles, teams, customers or citizens? How many? |
| Current approach | How is it done now, and what does it cost in time or money? |
| Desired outcome | What would "better" look like, in measurable terms? |
| Why AI might help | Which capability is relevant (drafting, summarising, classification, search, code generation)? |
| Data involved | What information would the tool need to see? Does it include personal, confidential or regulated data? |
| Consequence of error | If the AI output is wrong, what happens, and who would notice? |
| Owner | Who in the business will own this if it proceeds? |

The "consequence of error" question is the most important early filter. It shapes how much human review is needed and how much assessment the use case will require later.

## Responding to shadow AI

Discovery often reveals that staff are already using consumer AI tools with work data. Options, which are not mutually exclusive:

| Response | When it fits | Trade-offs |
|---|---|---|
| Interim guidance ("use only for public information; do not paste personal or confidential data") | Almost always, as a first step | Quick, but relies on individual judgement |
| Provide a sanctioned alternative quickly | Demand is high and a suitable tool with acceptable data terms is available | Reduces risk and keeps goodwill; requires some fast-tracked assessment |
| Block specific services | Where data terms are clearly unacceptable or regulated data is at risk | Reduces one route, but users may move to personal devices; blocking alone tends to push use out of sight |
| Bring shadow uses into the pipeline | Where the use looks valuable | Turns a risk into a source of validated use cases |

See the [acceptable use policy template](../../toolkits/acceptable-use-policy.md) for interim rules you can adapt.

## Roles involved

| Role | Contribution |
|---|---|
| Executive sponsor | Sets the mandate, removes blockers, receives the report |
| Business owners and team leads | Surface problems; nominate owners |
| Staff and champions | Describe real tasks and current tool use |
| IT and platform | Provide discovery data on tools in use |
| AI governance lead (if one exists) | Facilitates, keeps the register, applies early filters |
| HR and workers' representatives | Advise on survey design and on how findings about individuals will (and will not) be used |
| Data protection and security | Informed of shadow AI findings; advise on immediate risk actions |

## Outputs and deliverables

- A long list of opportunities, each with a problem statement and owner, recorded in the use case register.
- A shadow AI summary: tools in use, rough prevalence, data types involved, and immediate risk actions.
- Interim usage guidance, if none existed.
- A short report to the sponsor recommending which opportunities go to Assess.

## Decision gate: ready to move to Assess?

- [ ] The sponsor has confirmed the mandate and reviewed the long list.
- [ ] Each opportunity is framed as a problem with an affected group, desired outcome and owner.
- [ ] Data types and consequence of error are noted for each opportunity.
- [ ] Existing and shadow AI use has been inventoried, and immediate risks have owners.
- [ ] Interim guidance on AI use is in place and communicated.
- [ ] A shortlist (often three to ten items) has been agreed for assessment.
- [ ] Workers' representatives have been consulted where required by law or agreement.

## Linked assessments and toolkits

- [Organisational readiness assessment](../../assessments/organisational-readiness.md): run a first pass now to frame the conversation.
- [AI maturity model](../../assessments/maturity-model.md): locate your starting point.
- [Use case register template](../../toolkits/use-case-register-template.md)
- [Acceptable use policy template](../../toolkits/acceptable-use-policy.md)
- [Communication plan template](../../toolkits/communication-plan-template.md): for announcing the exercise.

## Variations by organisation size

**Small organisations.** Discover can be a single two-hour session with the whole team: list the tasks that eat time, note which AI tools people already use, and agree two or three problems to look at. The owner holds the register in a shared document. The key risk to manage is usually staff putting client or personal data into consumer tools, so interim guidance matters more than process.

**Enterprises.** Run discovery by function or business unit with a common template so results can be compared. Use IT discovery data at scale, and coordinate with the works council or union where staff surveys or tool monitoring are involved. Expect to find many duplicate ideas; group them into themes before Assess.

## Common pitfalls

- **Starting with a tool, not a problem.** "We bought licences, now find uses" tends to produce low adoption and weak evidence of value.
- **Treating shadow AI purely as a compliance breach.** This hides the most useful information and erodes trust.
- **Only asking managers.** Front-line staff often know the highest-value tasks.
- **Over-promising.** Leaders who expect transformation in weeks will judge pilots harshly. Ground expectations in [evidence on impact](../foundations/evidence-on-impact.md).
- **Ignoring consequence of error.** Use cases with high stakes and hard-to-detect errors need far more work later; flag them early.
- **No owner.** Opportunities without a named business owner rarely survive to Pilot.

# Stage 6: Operate

> **Who this is for:** Platform owners, IT operations, security, governance leads, business owners and anyone responsible for running AI tools day to day.
> **Last reviewed:** 2026-10

Operate is the longest stage: running AI tools reliably, safely and in line with their purpose once they are in routine use. AI tools change more often than most software, because vendors update the underlying models, add features and alter terms, sometimes with little notice. Operating them well therefore means continuous monitoring, a clear incident process, deliberate change management, periodic review and, eventually, orderly decommissioning. This page sets out each of those, with checklists and roles.

## Purpose

- Keep tools performing as intended and within risk appetite.
- Detect and respond to incidents.
- Manage changes to models, features, vendors, data and law.
- Review value and risk periodically and decide whether to continue, change or retire.
- Decommission tools cleanly when they are no longer fit for purpose.

## Inputs

- Handover from [Scale](05-scale.md): ownership, service levels, monitoring and reporting arrangements.
- Risk assessment, DPIA, use case register and business case.
- Contracts and vendor documentation.

## Activities

1. **Monitor** usage, value, quality, cost, security and compliance indicators (see below).
2. **Manage incidents** through a defined process that recognises AI-specific incident types.
3. **Control changes** to models, features, configurations, data sources and vendors.
4. **Run review cycles** at set intervals and on trigger events.
5. **Maintain enablement**: onboarding for new staff, refreshed training, an updated prompt library.
6. **Keep records**: register, risk assessments, decisions and logs, to support accountability and any regulatory requests.
7. **Decommission** when a review concludes the tool should be retired.

## Monitoring

| Area | Example indicators | Typical source |
|---|---|---|
| Adoption | Active users; frequency; features used | Admin dashboards |
| Value | Measures from the business case (time, quality, satisfaction) | Periodic sampling, surveys, process data |
| Output quality | Error reports; reviewer corrections; user feedback ratings | Feedback channels; sampling |
| Cost | Licence utilisation; usage-based spend | Billing, admin portal |
| Security | Blocked prompts; data loss prevention alerts; anomalous access; plug-in or connector changes | Security tooling, audit logs |
| Compliance | Policy breaches; use outside approved purposes; DPIA conditions still met | Audit logs, register reviews |
| Fairness (where relevant) | Differences in outcomes across groups for tools that influence decisions about people | Outcome monitoring designed with privacy and legal input |

Monitoring of staff use must itself comply with data protection and employment law. The UK regulator's guidance on monitoring workers says monitoring must be necessary and proportionate, transparent to workers, and supported by a DPIA where it is likely to be high risk [1]. See [data protection](../governance/data-protection.md).

For organisations that deploy high-risk AI systems under the EU AI Act, monitoring is a legal duty: deployers must monitor operation in line with the provider's instructions, keep automatically generated logs under their control for at least six months (unless other law requires otherwise), and inform the provider and authorities of serious incidents [2]. The high-risk obligations for systems listed in Annex III apply from 2 December 2027 under the 2026 amendments; see [regulation overview](../governance/regulation-overview.md).

## Incident management

Integrate AI incidents into your existing incident process rather than creating a separate one, but add AI-specific categories and playbooks.

| Incident type | Examples | First actions |
|---|---|---|
| Data exposure | Confidential or personal data surfaced to the wrong user; data pasted into an unapproved tool | Contain (restrict access, disable connector); assess whether it is a personal data breach requiring notification; fix permissions |
| Harmful or inaccurate output relied upon | Fabricated citation in a client document; wrong figure in a report | Correct the output; notify affected parties as appropriate; review the human review step |
| Security attack | Prompt injection through a document or web page causing unintended actions | Contain; preserve logs; follow security incident process; see [security](../governance/security.md) |
| Discriminatory or offensive output | Biased content; inappropriate language | Remove; report to vendor; assess impact on affected individuals |
| Service failure or unexpected change | Tool unavailable; behaviour changed after a model update | Activate fallback procedure; contact vendor; assess impact |

Personal data breaches may carry statutory notification deadlines under GDPR and UK GDPR (72 hours to the regulator where notification is required). Make sure AI incidents feed into that process.

### Incident playbook checklist

- [ ] AI incident categories defined and added to the incident process.
- [ ] Reporting route known to users (and tested).
- [ ] Owners for containment actions per tool (who can disable a connector or feature).
- [ ] Log retention sufficient to investigate.
- [ ] Vendor escalation contacts and contractual notification duties recorded.
- [ ] Link to the personal data breach process.
- [ ] Lessons-learned review after significant incidents, feeding into risk assessments.

## Model and vendor change management

AI services may change underlying models, safety settings, features, data processing locations, sub-processors or terms. Changes can alter output quality and risk without any action on your side.

1. **Know what can change.** Record, per tool, which components the vendor controls and how changes are communicated (release notes, admin centre messages, contractual notice).
2. **Watch the channels.** Assign someone to monitor vendor announcements and admin messages.
3. **Assess significant changes.** For new features (for example, a new connector, web access, or ability to take actions), decide whether to enable them, using the risk assessment. Default new capabilities to off where admin controls allow it, until assessed.
4. **Test where it matters.** For higher-risk uses, keep a small set of test scenarios and re-run them after model changes to spot changes in behaviour.
5. **Track terms changes.** Changes to data use, retention or sub-processors may require DPIA updates or contractual action.
6. **Manage your own changes.** Configuration changes, new data sources and new use cases should go through a lightweight change process with a risk check.

## Review cycles

| Review | Frequency (adjust to risk) | Questions |
|---|---|---|
| Operational | Monthly or quarterly | Are adoption, quality, cost and incidents within expectations? |
| Risk and compliance | At least annually, and on trigger events | Are the risk assessment and DPIA still accurate? Have laws, guidance or the tool changed? |
| Value | Before each renewal | Is the business case being realised? Should we continue, expand, change or stop? |
| Use case register | Quarterly | Are uses still within approved purposes? Are new uses registered? |

Trigger events for an off-cycle review include: a serious incident; a significant vendor change; a new law or regulatory guidance; a change of use; and a material change in the user population.

## Decommissioning

Tools are retired when value is not realised, a better alternative is selected, risk becomes unacceptable, the vendor withdraws the product, or the need disappears.

### Decommissioning checklist

- [ ] Decision recorded with reasons.
- [ ] Users informed with a timeline and alternatives.
- [ ] Dependent processes identified and changed.
- [ ] Valuable assets exported: prompts, configurations, custom assistants, documentation.
- [ ] Data returned or deleted in line with contract; deletion confirmation obtained from the vendor.
- [ ] Integrations, connectors, API keys and service accounts removed.
- [ ] Licences cancelled; billing stopped.
- [ ] Records retained as required (logs, assessments, decisions).
- [ ] Use case register and risk register updated.
- [ ] Lessons learned captured and fed back to [Discover](01-discover.md).

## Roles involved

| Role | Contribution |
|---|---|
| Service or platform owner | Day-to-day ownership; vendor management; change control |
| Business owner | Value; appropriate use; review decisions |
| IT operations and service desk | Support; availability |
| Security | Monitoring; incident response |
| Data protection | Breach assessment; DPIA updates |
| Governance lead or group | Review cycles; register; reporting |
| Procurement and vendor management | Renewals; contract changes; exit |
| Executive sponsor | Continue, change or stop decisions |

## Outputs and deliverables

- Regular monitoring reports.
- Incident records and lessons learned.
- Change log for models, features, configurations and terms.
- Review outcomes and decisions.
- Updated risk assessments, DPIAs and register.
- Decommissioning record, when applicable.

## Decision gate: continue, change or retire

At each formal review:

- [ ] Value is being realised in line with the business case, or the variance is understood.
- [ ] Risks remain within appetite; assessments are current.
- [ ] No unresolved serious incidents.
- [ ] Vendor terms and behaviour remain acceptable.
- [ ] Legal and regulatory obligations are still met.
- [ ] Decision recorded: continue, change (back to [Assess](02-assess.md) or [Select](03-select.md)), or retire.

## Linked assessments and toolkits

- [AI risk assessment](../../assessments/ai-risk-assessment.md): re-run on review.
- [Vendor due diligence](../../assessments/vendor-due-diligence.md): refresh at renewal.
- [Use case register](../../toolkits/use-case-register-template.md)
- [AI maturity model](../../assessments/maturity-model.md)
- [Measuring value](../measurement/measuring-value.md)

## Variations by organisation size

**Small organisations.** A quarterly half-hour review can cover most of this: is it still useful, what does it cost, has anything gone wrong, have the supplier's terms changed? Subscribe to the vendor's admin or product update notices. Keep a simple log of incidents and changes.

**Enterprises.** Integrate with IT service management, security operations, third-party risk and model risk management. Consider an AI asset inventory covering all AI tools and features, including AI capabilities added to existing software.

## Common pitfalls

- **Assuming the tool stays the same.** Model updates can change behaviour; monitor and test.
- **New features enabled by default.** Review admin settings after vendor releases.
- **Assessments that never get revisited.** Laws and tools change; set review dates.
- **No fallback.** Know how work gets done if the tool is unavailable.
- **Forgetting exit.** Data deletion and asset export are easier when planned from the start.

## Sources

1. Information Commissioner's Office, *ICO publishes guidance to ensure lawful monitoring in the workplace*, 3 October 2023. https://cy.ico.org.uk/about-the-ico/media-centre/news-and-blogs/2023/10/ico-publishes-guidance-to-ensure-lawful-monitoring-in-the-workplace
2. European Commission AI Act Service Desk, *Article 26: Obligations of deployers of high-risk AI systems*. https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26

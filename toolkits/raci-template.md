# RACI template for AI adoption

> **Who this is for:** Sponsors, programme leads, governance leads and managers who need to agree who does what across the AI lifecycle. Includes a reduced version for small organisations.
> **Last reviewed:** 2026-10

This template provides a RACI matrix (Responsible, Accountable, Consulted, Informed) covering AI adoption activities across the six lifecycle stages, from setting strategy to retiring a use case, against the roles most organisations need. A pre-filled default gives you a starting point to adapt; a blank version and a compressed small-organisation version follow. Guidance notes explain the choices you need to make. Agreeing roles early prevents two common failure modes: nobody owning risk decisions, and every decision needing everyone.

## How to read a RACI

| Letter | Meaning | Rule of thumb |
|---|---|---|
| **R** Responsible | Does the work | At least one per activity; can be several |
| **A** Accountable | Owns the outcome and makes the final decision | Exactly one per activity |
| **C** Consulted | Gives input before the decision or work is complete (two-way) | Keep to those whose input changes the outcome |
| **I** Informed | Told of the outcome (one-way) | Keep the list realistic |

Where one role is both accountable and does the work, write **A/R**.

> **Guidance: tailoring**
>
> - Rename roles to match your organisation. A role is not a person; one person may hold several roles, and one role may be shared across a team.
> - Check each row has exactly one A. Check no role is "A" for so many rows that it becomes a bottleneck.
> - Agree the RACI with every role named in it. A RACI imposed without agreement tends not to be followed.
> - Link the RACI to the approval routes in your [AI policy](ai-policy-template.md) so that the two agree.

## Roles

| Abbreviation | Role | Typical holder |
|---|---|---|
| **BRD** | Board / owners | Board, trustees, partners or owner |
| **SPN** | Senior AI sponsor | Executive director or senior leader |
| **GOV** | AI governance group | Cross-functional group chaired by the sponsor |
| **PL** | AI programme lead | Programme or transformation manager |
| **UCO** | Use case owner | Business manager who owns the process |
| **IT** | IT / platform | IT lead, platform team or managed service provider |
| **SEC** | Information security | Security lead or adviser |
| **DPO** | Data protection | Data protection officer or lead |
| **LEG** | Legal / compliance | In-house legal, compliance or external adviser |
| **PRC** | Procurement | Procurement or finance |
| **DAT** | Data owner / data team | Data owner, data and analytics team |
| **HR** | HR / people and learning | HR, learning and development |
| **MGR** | Line managers | Managers of users |
| **USR** | Users | Staff using AI tools |

## Default RACI matrix

| Stage | Activity | BRD | SPN | GOV | PL | UCO | IT | SEC | DPO | LEG | PRC | DAT | HR | MGR | USR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Discover** | Set AI purpose and strategy | C | A | C | R | C | C | | | | | | C | I | I |
| | Approve AI risk appetite | A | R | C | | | | C | C | C | | | | | |
| | Gather and record use case ideas | | I | I | A | R | C | | | | | C | | R | R |
| | Discover existing (unmanaged) AI use | | I | I | A | | R | R | C | | | | | C | C |
| **Assess** | Organisational readiness assessment | I | A | C | R | C | C | C | C | | | C | C | | |
| | Prioritise use cases | | I | A | R | R | C | | C | | | C | | C | |
| | Data readiness assessment | | | I | C | A | R | C | C | | | R | | | |
| | AI risk assessment and screening | | | I | C | A/R | C | C | C | C | | C | C | | |
| | DPIA (where required) | | | I | | R | C | C | A | C | | C | | | |
| | Approve high-risk use cases | I | C | A | R | R | | C | C | C | | | | | |
| **Select** | Define tool requirements | | | C | A | R | R | C | C | | C | C | | | C |
| | Vendor due diligence | | | I | C | C | R | R | R | R | A | | | | |
| | Contract negotiation and signature | | C | | C | | C | C | C | R | A | | | | |
| | Business case | | A | C | R | R | C | | | | C | | C | | |
| **Pilot** | Pilot plan and approval | | A | C | R | R | C | C | C | | | | C | C | |
| | Configure tool and controls | | | | C | C | A/R | R | C | | | C | | | |
| | Pilot training | | | | C | C | C | | | | | | A/R | C | I |
| | Run pilot and collect data | | I | | A | R | C | | | | | | | R | R |
| | Evaluate pilot and decide | I | A | C | R | R | C | C | C | | | | C | C | I |
| **Scale** | Rollout plan | | A | C | R | C | R | C | C | | C | | C | C | I |
| | Policies (AI policy, acceptable use) | I | A | C | R | | C | C | C | C | | | C | I | I |
| | Role-based training and AI literacy | | I | I | C | | | | | | | | A/R | R | R |
| | Communications | | A | | R | C | C | | | | | | C | R | I |
| | Support model | | I | | C | | A/R | | | | | | | C | I |
| **Operate** | Monitor usage, quality and value | | I | I | A | R | R | | | | | C | | C | |
| | Monitor security and incidents | | I | I | | C | R | A | C | | | | | | |
| | Handle AI incidents | | I | C | C | R | R | A | R | C | | | | C | C |
| | Maintain use case register | | | C | A/R | R | | | | | | | | | |
| | Maintain prompt library | | | | A | R | C | | | | | | | R | R |
| | Periodic review and re-assessment | | I | A | R | R | C | C | C | C | | C | | | |
| | Track regulatory change | | I | I | | | | | C | A/R | | | | | |
| | Vendor and contract management | | | | C | C | R | C | | C | A | | | | |
| | Retire a use case | | | I | C | A/R | R | C | C | | C | C | | I | I |
| **All stages** | Report to board / owners | I | A/R | C | R | | | | | | | | | | |
| | Raise concerns | | I | A | | | | | | | | | | R | R |

> **Guidance:** This default reflects common practice. Valid alternatives include making the DPO accountable for the risk assessment in heavily regulated settings, or making IT accountable for vendor due diligence where procurement is light-touch. Whatever you choose, keep exactly one A per row.

## Blank template

Copy and fill in. Add rows for activities specific to your organisation.

| Stage | Activity | [Role 1] | [Role 2] | [Role 3] | [Role 4] | [Role 5] | [Role 6] | [Role 7] | [Role 8] |
|---|---|---|---|---|---|---|---|---|---|
| Discover | [ ] | | | | | | | | |
| Assess | [ ] | | | | | | | | |
| Select | [ ] | | | | | | | | |
| Pilot | [ ] | | | | | | | | |
| Scale | [ ] | | | | | | | | |
| Operate | [ ] | | | | | | | | |

## Small organisation version

For organisations under about 50 people, four roles are usually enough.

| Role | Typical holder |
|---|---|
| **OWN** | Owner / managing director (sponsor and governance) |
| **LEAD** | AI lead (often the operations manager or most experienced user) |
| **IT** | IT provider (internal person or managed service provider) |
| **ADV** | External adviser(s) for data protection and legal, as needed |

| Activity | OWN | LEAD | IT | ADV | Staff |
|---|---|---|---|---|---|
| Set purpose and risk appetite | A/R | C | C | C | I |
| Approve tools | A | R | R | C | I |
| Acceptable use policy | A | R | C | C | I |
| Configure tool and data settings | I | A | R | | |
| Use case ideas and register | I | A/R | | | R |
| Risk screening per use case | A | R | C | C | |
| DPIA where required | A | R | C | R | |
| Training | I | A/R | C | | R |
| Monitor use and incidents | I | A/R | R | | R |
| Annual review | A | R | C | C | I |

## Checks before you finalise

- [ ] Exactly one A per row
- [ ] Every row has at least one R
- [ ] No role is A for more than it can realistically handle
- [ ] Roles with C are genuinely needed for that decision
- [ ] Consistent with approval routes in the [AI policy](ai-policy-template.md)
- [ ] Agreed with each role holder
- [ ] Review date set: [date]

## Related

- [Governance model](../docs/governance/governance-model.md)
- [AI policy template](ai-policy-template.md)
- [Lifecycle overview](../docs/lifecycle/README.md)

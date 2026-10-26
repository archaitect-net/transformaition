# Microsoft 365 Copilot

> **Who this is for:** Microsoft 365 administrators, SharePoint and Purview administrators, security and data protection teams, and rollout leads in organisations that have chosen Microsoft's Copilot for Microsoft 365.
> **Last reviewed:** 2026-10

This guide covers implementing Microsoft's AI assistant within Microsoft 365: the licensed Copilot experience grounded in organisational content through Microsoft Graph, and the Copilot Chat experience available with eligible Microsoft 365 licences. It describes licensing, prerequisites, data flow, data handling, admin controls, oversharing remediation, rollout and reporting, with links to Microsoft's documentation. It assumes the product has already been chosen; for selection, see [choosing tools](../choosing-tools.md).

> **Verify before relying on this.** Microsoft's Copilot naming, licensing and features change frequently. As of October 2026, Microsoft's licensing documentation refers to the paid licence as "Microsoft Copilot", while many pages still use "Microsoft 365 Copilot" [3][4]. Check the live documentation and your agreement.

## Overview

Microsoft describes Copilot as a processing and orchestration engine that combines large language models with content in Microsoft Graph (email, chats, documents, calendar, meetings, contacts) and the Microsoft 365 apps [1]. It appears in Word, Excel, PowerPoint, Outlook, Teams, OneNote and a chat interface, and can be extended with agents and connectors [7].

There are two tiers to understand [4]:

| | Copilot Chat | Licensed Microsoft Copilot |
|---|---|---|
| Licence | Included with eligible Microsoft 365 licences; no Copilot licence required | Copilot licence plus a qualifying prerequisite licence |
| Grounding | Primarily web; user-provided content (pasted text, uploads, referenced files); in Outlook, a bounded set of mailbox, calendar and file content | Broad reasoning across Microsoft 365 content via Graph, Work IQ and semantic indexing |
| Enterprise data protection | Yes, for eligible work and school accounts | Yes |
| Copilot in Word, Excel, PowerPoint, OneNote | Not included in the basic Copilot Chat experience | Included |
| Agents | Limited | Advanced agents and agent experiences |

Category: [assistant embedded in a productivity suite](../tool-categories.md#2-assistants-embedded-in-productivity-suites).

## Editions and licensing

- **Availability.** Microsoft Copilot is included with Microsoft 365 E7 or sold as an add-on for eligible commercial, US Government and education subscriptions [3].
- **Prerequisite licences (commercial).** Microsoft lists, among others, Microsoft 365 E3/E5/E7, F1/F3 and Business plans; Office 365 E1/E3/E5/F3; and standalone Teams, Exchange, SharePoint, OneDrive and others [3]. Check the current list.
- **Small and medium organisations.** "Microsoft Copilot Business" is an add-on for organisations with up to 300 users on Microsoft 365 Business Basic, Standard or Premium, sold with an annual commitment; organisations with more than 300 users use enterprise options [3].
- **Education and government.** Academic offerings cover Microsoft 365 A1/A2/A3/A5 and Office 365 A1/A3/A5, for faculty, staff and students aged 13 and over; US Government clouds have their own prerequisite list and feature differences [3][4].
- **Not available** with device-based licensing for Microsoft 365 Apps for enterprise [2].
- **Pricing** is not stated on the licensing page; Microsoft points to its pricing and plans page [3].

## Prerequisites

From Microsoft's requirements page [2]:

- Users need a work or school account in **Microsoft Entra ID**.
- Some features require a **OneDrive** account.
- Mailbox-grounded experiences require an **Exchange Online** mailbox; Copilot is not available in group mailboxes. Classic and new Outlook for Windows and Mac are supported.
- **Teams**: to let Copilot use meeting content after a meeting ends, configure transcription or recording. Teams Phone scenarios have additional licence requirements.
- **Microsoft 365 Apps** must be deployed for desktop app experiences, and the Office Feature Updates task must run on its schedule.
- **Network**: allow the Microsoft 365 URLs and IP ranges and Copilot endpoints; allow the entire `*.cloud.microsoft` domain; verify WebSocket Secure (WSS) connectivity to `*.office.com`, `*.cloud.microsoft` and `copilot.cloud.microsoft`.
- **Privacy controls for connected experiences** can affect feature availability.

**Data preparation** is the less visible prerequisite: Copilot surfaces content users can already access, so permission hygiene must come first (see [Rollout steps](#rollout-steps)).

## Architecture and data flow

1. A user enters a prompt in a Microsoft 365 app or Copilot Chat.
2. Copilot retrieves relevant content from Microsoft Graph and the semantic index, limited to content the user has at least view permission for [1].
3. If web search is enabled and Copilot judges web results useful, it generates a search query and sends it to the Bing Search service. Admins can control public web access [1].
4. The grounded prompt is processed by large language models. Copilot calls are routed to the closest regional data centres but may use other regions during high utilisation [1].
5. The response, with citations, is returned and the interaction (prompt, response, citations) is stored as "Copilot activity history" [1].

**Model providers.** Microsoft states that models from Anthropic, used as a sub-processor, are currently excluded from the EU Data Boundary [1]. Organisations with EU Data Boundary requirements should check which features use those models and how to control them.

## Data handling, retention and training-on-data

- **Training.** Microsoft states that prompts, responses and data accessed through Microsoft Graph are not used to train foundation large language models. Optional feedback may be used to improve Copilot but not to train foundation models [1].
- **Storage.** Copilot activity history is stored under the same contractual commitments as other Microsoft 365 content and encrypted at rest [1].
- **Retention and discovery.** Admins can find interactions through Content search or Microsoft Purview and can set retention policies for Copilot interactions [1].
- **User deletion.** Users can delete their Copilot activity history through the My Account portal [1].
- **Residency.** EU traffic stays within the EU Data Boundary (subject to the Anthropic exclusion above). Copilot has been a covered workload in Microsoft Product Terms data residency commitments since 1 March 2024, and is included in Advanced Data Residency and Multi-Geo offerings. Customers outside the EU may have queries processed in the US, EU or other regions [1].
- **Sensitivity labels and encryption.** Copilot honours the usage rights granted to the user under sensitivity labels and Information Rights Management; content encrypted without programmatic-access rights can prevent agents from reading it [1].

## Security and admin controls

- **Permissions model.** Copilot and Copilot Chat respect existing Microsoft 365 permissions and do not grant access to additional content [4].
- **Encryption and isolation.** Customer content is encrypted at rest and in transit (BitLocker, per-file encryption, TLS, IPsec); tenant isolation is enforced through Entra authorisation and role-based access control [1].
- **SharePoint Advanced Management (SAM).** Microsoft states SAM is included with the Copilot licence [5]. Its **Restricted Content Discovery** setting hides a SharePoint site's content from organisation-wide search and Copilot without changing permissions; it is site-level, does not apply to OneDrive, and can take more than a week to propagate on sites with over 500,000 items [6].
- **Microsoft Purview.** Provides data loss prevention, insider risk and compliance capabilities for Copilot interactions and the content it references [5]. Purview entitlements vary by licence; check which features your licences include.
- **Web grounding.** Admins can control whether Copilot can use public web search [1].

## Identity and access

- Identity is Microsoft Entra ID; Copilot acts with the signed-in user's permissions [1][2].
- Licences are assigned in the Microsoft 365 admin center, individually or through groups [3].
- Agents and connectors each carry their own identity, authentication and governance requirements [7].

## Integration

Microsoft documents several extensibility paths [7]:

- **Declarative agents**, which use Copilot's orchestrator and models.
- **Custom engine agents**, which use your own orchestration, models or hosting.
- **Microsoft 365 Copilot connectors**, which ground Copilot in approved external organisational data.
- **MCP servers and plug-ins**, and Teams message extensions.
- **Work IQ APIs and Microsoft 365 Copilot APIs** to bring Microsoft 365 context into your own applications.

Each added connector or agent widens what Copilot can reach or do; treat each as a change requiring review.

## Rollout steps

1. **Confirm licensing and prerequisites.** Check prerequisite licences, Entra accounts, OneDrive, Exchange Online, app deployment and network rules [2][3]. Use Microsoft's service plan diagnostic tool to check specific accounts [3].
2. **Decide the Copilot Chat baseline.** Decide whether Copilot Chat is available to all eligible users from the start, and whether web grounding is on [1][4].
3. **Assess oversharing.** Microsoft's deployment blueprint sequence is: reduce Copilot exposure quickly; harden the environment with enforceable defaults; identify high-risk sites and files; apply interim access restrictions if needed; fix access issues; continuously enforce guardrails [5].
4. **Apply interim restrictions** where needed, for example Restricted Content Discovery on sensitive SharePoint sites while permissions are reviewed [6].
5. **Configure Purview.** Set retention policies for Copilot interactions, confirm eDiscovery coverage, and review sensitivity labelling and data loss prevention [1][5].
6. **Run a pilot** with a cross-section of roles. See the [pilot plan template](../../../toolkits/pilot-plan-template.md).
7. **Set agent and connector governance.** Decide who can build, publish and approve agents and connectors [7].
8. **Enable reporting** (see below) and agree success measures.
9. **Expand in waves**, with training and communication for each wave, reviewing oversharing findings as you go.
10. **Review regularly**: permissions, retention, new features enabled by updates, and usage.

## Enablement and training

- Users need to understand that Copilot can surface any content they have access to, and should report anything they should not see.
- Training should cover prompting in each app, checking citations, and the organisation's [acceptable use policy](../../../toolkits/acceptable-use-policy.md).
- Admins need training on SAM, Purview and reporting.
- See the [training plan template](../../../toolkits/training-plan-template.md) and Microsoft Learn's Copilot modules.

## Monitoring and usage reporting

Microsoft documents three reporting sources [8]:

| Source | Shows | Access |
|---|---|---|
| Microsoft 365 admin center: Readiness and Usage reports | Licence eligibility and technical blockers; active users, trends, apps used, top agents | AI Administrator; Reports > Usage > Microsoft Copilot |
| Copilot Dashboard (Viva Insights) | Adoption, usage patterns, impact indicators | Enabled by an AI Administrator and delegated |
| Copilot Analytics (Viva Insights analyst tools) | Custom queries and Power BI templates | Requires Viva Insights roles |

Usage measures activity, not value. Combine with the approaches in [measuring value](../../measurement/measuring-value.md).

## Known limitations

- **Oversharing exposure.** Because Copilot respects existing permissions, overly broad permissions become easier to exploit through natural-language queries. Remediation can take significant time on large tenants [5][6].
- **Restricted Content Discovery** is a temporary, site-level control; it does not change permissions or apply to OneDrive, and propagation can be slow on large sites [6].
- **EU Data Boundary exception** for Anthropic models [1].
- **Regional processing** may move outside the nearest region during high utilisation [1].
- **Copilot Chat** without the licence does not reason broadly across organisational content and does not include Copilot in Word, Excel, PowerPoint or OneNote [4].
- **Government clouds** have different feature availability, and web grounding is not enabled by default in some [4].
- **Outputs can be wrong or incomplete** even when grounded; users should check citations. See [capabilities and limitations](../../foundations/capabilities-and-limitations.md).

## Cost considerations

- Copilot licence per user (or inclusion in Microsoft 365 E7), plus any prerequisite licence upgrades [3].
- Purview and governance capabilities may need higher licence tiers.
- Effort for permission remediation, which can exceed licence cost on poorly governed tenants.
- Agent consumption and any separately billed agent or connector services: check current terms.
- Training, change management and reporting effort.
- Copilot Business has an annual commitment and a 300-user cap [3].

## Exit considerations

- Copilot activity history sits in Microsoft 365 and is subject to your Purview retention policies; plan what to retain or export before removing licences [1].
- Agents, connectors and prompts built on Microsoft's extensibility model are specific to that platform [7].
- Permission and labelling improvements made for Copilot remain valuable whatever you decide.
- Removing Copilot licences does not remove Copilot Chat for eligible users; decide that separately [4].

## Official documentation links

- [Data, privacy, and security for Microsoft Copilot](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy)
- [Microsoft Copilot requirements](https://learn.microsoft.com/copilot/microsoft-365/microsoft-365-copilot-requirements)
- [Microsoft Copilot licensing](https://learn.microsoft.com/copilot/microsoft-365/microsoft-365-copilot-licensing)
- [Microsoft Copilot Chat overview](https://learn.microsoft.com/en-gb/copilot/overview)
- [Copilot deployment blueprint: oversharing](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-blueprint-oversharing)
- [Restricted Content Discovery](https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery)
- [Copilot extensibility overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview)
- [Copilot reports for admins](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-reports-for-admins)

## Questions to verify with Microsoft

- Current per-user price, and whether any agents or connectors are billed by consumption.
- Which Purview capabilities for Copilot (for example data loss prevention for Copilot prompts, AI-specific posture management) are included in our licences.
- Which Copilot features use Anthropic models, and how to disable them if EU Data Boundary coverage is required.
- Default retention of Copilot activity history where no Purview policy is set.
- Whether Microsoft offers an intellectual property indemnity for Copilot outputs under our agreement, and its conditions.

---

**Last verified:** 2026-10-26 against the official documentation listed above.

**Verify before relying on this.** Vendors change products, plans and terms frequently. This guide is descriptive and is not an endorsement. Inclusion in this guide reflects breadth of organisational use, not preference.

## Sources

1. Microsoft Learn, *Data, privacy, and security for Microsoft Copilot*, accessed 2026-10. https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy
2. Microsoft Learn, *Microsoft Copilot requirements*, accessed 2026-10. https://learn.microsoft.com/copilot/microsoft-365/microsoft-365-copilot-requirements
3. Microsoft Learn, *Microsoft Copilot licensing*, accessed 2026-10. https://learn.microsoft.com/copilot/microsoft-365/microsoft-365-copilot-licensing
4. Microsoft Learn, *Microsoft Copilot Chat overview*, accessed 2026-10. https://learn.microsoft.com/en-gb/copilot/overview
5. Microsoft Learn, *Microsoft Copilot deployment blueprint: oversharing*, accessed 2026-10. https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-blueprint-oversharing
6. Microsoft Learn, *Restrict discovery of SharePoint sites and content*, accessed 2026-10. https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery
7. Microsoft Learn, *Microsoft 365 Copilot extensibility overview*, accessed 2026-10. https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview
8. Microsoft Learn, *Microsoft Copilot reports for admins*, accessed 2026-10. https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-reports-for-admins

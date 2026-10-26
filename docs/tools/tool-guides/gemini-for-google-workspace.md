# Gemini for Google Workspace

> **Who this is for:** Google Workspace administrators, security and data protection teams, and rollout leads in organisations that have chosen Google's Gemini AI features within Workspace.
> **Last reviewed:** 2026-10

This guide covers implementing Google's generative AI in Google Workspace: Gemini features inside Workspace apps such as Gmail, Docs, Sheets, Drive and Meet; the Gemini app; and Gemini Notebook (formerly NotebookLM). It describes packaging, data handling, retention, admin controls, data regions, rollout and known limitations, with links to Google's documentation. It assumes the product has already been chosen; for selection, see [choosing tools](../choosing-tools.md).

> **Verify before relying on this.** Google's naming and packaging for Workspace AI has changed several times. As of October 2026, Google's documentation uses "Gemini in Workspace" (features in apps), "Gemini app" and "Gemini Notebook" (formerly NotebookLM) [1], and the admin guide is titled "Google Workspace with Gemini" [2]. Check the live documentation and your agreement.

## Overview

Google's privacy hub distinguishes three products, which have different controls and assurances [1]:

| Product | What it is |
|---|---|
| **Gemini in Workspace** | Gemini features and side panels in apps such as Gmail, Docs, Drive, Sheets, Slides, Meet and Chat |
| **Gemini app** | gemini.google.com, the mobile apps and Gemini in Chrome |
| **Gemini Notebook** | Source-grounded research and notebook tool, formerly NotebookLM |

Related capabilities include Google Workspace Studio (automations) and Google Vids [2].

Category: [assistant embedded in a productivity suite](../tool-categories.md#2-assistants-embedded-in-productivity-suites), with a [general-purpose assistant](../tool-categories.md#1-general-purpose-assistants) in the Gemini app.

## Editions and licensing

- **Standard access is included** in Business and Enterprise plans. Google describes these plans as including "standard access" to advanced AI capabilities at no extra cost, with features such as "Help me write" in Gmail [3].
- **Enterprise Standard and Enterprise Plus** both include the Gemini app with enterprise-grade data protections and Gemini features in Gmail, Calendar, Chat, Meet and Docs [4].
- **AI Expanded Access** is an add-on (purchasable from 5 February 2026) for Business Standard and Plus and Enterprise Standard and Plus. It raises usage limits for advanced features such as image and video generation, deep reasoning in the Gemini app, Gemini Notebook, Workspace Studio automations and speech translation in Meet. Licences can be assigned to specific users [3].
- **AI Ultra Access** is no longer sold; existing customers move to AI Expanded Access at renewal after 7 July 2026 [5].
- **Feature-level admin controls** in the Admin console are documented for Enterprise Standard and Plus, certain Education editions and Google AI Pro for Education [2].

## Prerequisites

- A Google Workspace edition that includes the features you need [2][4].
- Admin access to the Google Admin console.
- Users must turn on smart features and personalisation to use Gemini in Workspace services [2].
- Decisions on data regions, retention and which services to enable, made before broad rollout.
- Sharing and permission hygiene in Drive, since Gemini can draw on content users can access.

## Architecture and data flow

1. A user invokes Gemini in a Workspace app, the Gemini app or Gemini Notebook.
2. Gemini draws on the user's prompt and, depending on context and enabled sources, content from Workspace services (Gmail, Drive, Calendar, Chat) that the user can access. Admins can turn these "Workspace Intelligence" sources on or off [1].
3. Prompts and responses are processed by Google's models and treated as customer data under the Cloud Data Processing Addendum [1].
4. Interactions are retained according to the product's retention settings (see below) [1].

Google states that interactions with Gemini stay within the organisation and content is not shared outside it without permission [1].

## Data handling, retention and training-on-data

- **Training.** Google states that Workspace does not use customer data to train generative AI models without the customer's permission or instruction. Feedback submitted is not used to train the models supporting Workspace generative AI [1].
- **Human review.** Gemini app chats and uploads are not manually reviewed without the user's permission [1].
- **Retention** [1]:

| Product | Prompts and responses | Admin control |
|---|---|---|
| Gemini in Workspace | 90 days to unlimited, set by admins | Admins set retention; users can delete conversations unless blocked |
| Gemini app | Default 18 months, up to 36 months | Admins choose whether chats are saved and the auto-delete period (3, 18 or 36 months); with history off, new chats are kept for up to 72 hours |
| Gemini Notebook | Not retained after the session ends | Uploaded files and notebooks deleted manually or exported |

- **Data regions** [6]: prompts and responses for the Gemini app and Gemini in Workspace are covered **at rest** by all applicable Data Regions versions. Coverage of data **in use (processing)** requires Enterprise Data Regions (Enterprise Plus, Enterprise Essentials Plus, Frontline Plus, or the add-on) or Assured Controls Data Regions. Gemini Notebook is not covered by Data Region policies. Logs and cached content are excluded.

## Security and admin controls

- **Certifications.** Google lists SOC 1/2/3, ISO 9001, 27001, 27701, 27017, 27018 and 42001, and FedRAMP High authorisation for Gemini in Workspace and the Gemini app, and states Gemini can support HIPAA workloads. **Gemini Notebook and Gemini in Chrome currently lack ISO, SOC and FedRAMP coverage and are not covered by Google's BAA** [1].
- **Data loss prevention.** In supported editions, existing DLP policies apply to Gemini output inserted into covered services like Gmail and Drive. Gemini Notebook is not integrated with Workspace DLP [1].
- **Information Rights Management.** IRM settings can prevent Gemini from retrieving files where download, copy or print are disabled [1].
- **Client-side encryption.** CSE content cannot be accessed by Google systems, which limits Gemini's access to it [1].
- **Vault and audit.** Vault manages retention of Workspace data; Gemini audit logs are available through the Reporting API [1].
- **Feature toggles.** In the Admin console under Generative AI > Gemini for Workspace > Feature access, admins can turn features and side panels on or off per service, by organisational unit or configuration group. **The default for Gemini features in Workspace services is on** [2].

## Identity and access

- Users authenticate with their Workspace accounts, under your existing Google identity or federated SSO configuration.
- Admins control access by organisational unit or configuration group [2].
- Gemini can access only content the user has access to; it does not share content outside the organisation without permission [1].
- Gemini Notebook can be enabled for the whole organisation or specific organisational units or groups, with its own sharing settings [1].

## Integration

- Gemini works across Workspace apps and, where enabled, draws on Gmail, Drive, Calendar and Chat as sources [1].
- Google Workspace Studio provides automations; admins can turn it on or off and block Gemini from Workspace Studio with API controls [2].
- For building custom applications on Google's models, see [cloud AI platforms](cloud-ai-platforms.md) (Gemini Enterprise Agent Platform).

## Rollout steps

1. **Confirm editions** and which Gemini features each user group has; decide whether any users need AI Expanded Access [3][4].
2. **Review defaults.** Gemini features in Workspace services default to on; decide whether to turn services off for some organisational units while you prepare [2].
3. **Review Drive sharing and permissions**, especially broadly shared sensitive content.
4. **Configure security controls**: DLP, IRM, client-side encryption for highly sensitive content, and Vault [1].
5. **Set retention** for Gemini in Workspace and the Gemini app conversations [1].
6. **Decide data regions**, noting that processing coverage needs Enterprise Data Regions or Assured Controls [6].
7. **Decide on Gemini Notebook and Gemini in Chrome**, given their narrower certification coverage and data region exclusion [1][6].
8. **Pilot** with a representative group. See the [pilot plan template](../../../toolkits/pilot-plan-template.md).
9. **Set up audit and usage reporting** through the Reporting API and admin reports [1].
10. **Expand by organisational unit** with training, and review settings as new features arrive.

## Enablement and training

- Explain which Gemini products are approved, since they differ in assurances [1].
- Cover the [acceptable use policy](../../../toolkits/acceptable-use-policy.md), verification of outputs, and what users should do if Gemini surfaces content they should not see.
- Explain retention of Gemini app chats and how users can delete them where permitted [1].
- See the [training plan template](../../../toolkits/training-plan-template.md).

## Monitoring and usage reporting

- Gemini audit logs are available through the Reporting API [1].
- Google's admin documentation includes guidance on reviewing Gemini usage in the organisation [2].
- Combine with [measuring value](../../measurement/measuring-value.md).

## Known limitations

- **Gemini Notebook** lacks ISO, SOC and FedRAMP coverage, is not covered by the BAA, is not integrated with Workspace DLP, and is not covered by Data Region policies [1][6].
- **Gemini in Chrome** has the same certification and BAA gaps as Gemini Notebook [1].
- **Defaults are on** for Gemini features in Workspace services [2].
- **Turning Gemini off in one app does not block access to that app's data through Gemini in other apps** [2].
- **Data regions** cover processing only on certain editions or add-ons; logs and cached content are excluded [6].
- **Usage limits** apply to standard access; higher usage of some features needs the AI Expanded Access add-on [3].
- **Outputs can be wrong or incomplete.** See [capabilities and limitations](../../foundations/capabilities-and-limitations.md).

## Cost considerations

- Standard AI access included in Business and Enterprise plans; check whether your edition includes the specific features you need [3][4].
- AI Expanded Access add-on for users needing higher limits [3].
- Enterprise Data Regions or Assured Controls if processing-location commitments are required [6].
- Effort for permission review, DLP and labelling.
- Promotional access to some features ended on 1 March 2026 for customers without the add-on [3].

## Exit considerations

- Gemini in Workspace conversation retention follows admin settings; Vault manages retention of Workspace data [1].
- Gemini Notebook files and notebooks can be exported [1].
- Workspace Studio automations are platform-specific.
- Leaving Gemini while staying on Workspace is a matter of turning features off; leaving Workspace entirely follows Google's standard data export processes.

## Official documentation links

- [Generative AI in Google Workspace Privacy Hub](https://support.google.com/a/answer/15706919?hl=en)
- [Google Workspace with Gemini (admin)](https://knowledge.workspace.google.com/admin/generative-ai/workspace-with-gemini)
- [Compare Enterprise editions](https://knowledge.workspace.google.com/admin/getting-started/editions/compare-enterprise-editions)
- [Data covered by Data Regions](https://knowledge.workspace.google.com/admin/compliance/data-covered-by-data-regions?hl=en)
- [Google Workspace AI Expanded Access announcement](https://workspaceupdates.googleblog.com/2026/02/google-workspace-ai-expanded-access.html)
- [AI Ultra Access](https://knowledge.workspace.google.com/admin/generative-ai/workspace-with-gemini/ai-ultra-access)

## Questions to verify with Google

- Exactly which Gemini features are included in each Business edition, and the usage limits for standard access.
- Whether feature-level admin controls are available in our edition (they are documented for Enterprise and certain Education editions).
- Processing locations for Gemini when Enterprise Data Regions is not in place.
- Current price of AI Expanded Access.
- Plans for certification, DLP and Data Regions coverage of Gemini Notebook.
- Any intellectual property indemnity for generated output, and its conditions.

---

**Last verified:** 2026-10-26 against the official documentation listed above.

**Verify before relying on this.** Vendors change products, plans and terms frequently. This guide is descriptive and is not an endorsement. Inclusion in this guide reflects breadth of organisational use, not preference.

## Sources

1. Google Workspace Admin Help, *Generative AI in Google Workspace Privacy Hub*, accessed 2026-10. https://support.google.com/a/answer/15706919?hl=en
2. Google Workspace Admin Help, *Google Workspace with Gemini*, accessed 2026-10. https://knowledge.workspace.google.com/admin/generative-ai/workspace-with-gemini
3. Google Workspace Updates, *Google Workspace AI Expanded Access*, 5 February 2026. https://workspaceupdates.googleblog.com/2026/02/google-workspace-ai-expanded-access.html
4. Google Workspace Admin Help, *Compare Enterprise editions*, accessed 2026-10. https://knowledge.workspace.google.com/admin/getting-started/editions/compare-enterprise-editions
5. Google Workspace Admin Help, *AI Ultra Access*, accessed 2026-10. https://knowledge.workspace.google.com/admin/generative-ai/workspace-with-gemini/ai-ultra-access
6. Google Workspace Admin Help, *Data covered by Data Regions*, accessed 2026-10. https://knowledge.workspace.google.com/admin/compliance/data-covered-by-data-regions?hl=en

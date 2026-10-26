# ChatGPT Business and Enterprise

> **Who this is for:** Workspace owners and admins, IT and identity teams, security and data protection staff, and rollout leads in organisations that have chosen OpenAI's ChatGPT for organisational use.
> **Last reviewed:** 2026-10

This guide covers implementing ChatGPT's organisational plans: ChatGPT Business (for smaller teams) and ChatGPT Enterprise (and the related Edu plan). It describes plan differences, data handling and retention, identity and admin controls, connectors, a numbered rollout, analytics and known limitations, with links to OpenAI's documentation. It assumes the product has already been chosen; for selection, see [choosing tools](../choosing-tools.md).

> **Verify before relying on this.** OpenAI's plan names and packaging have changed several times. As of October 2026, OpenAI's business pricing page lists "Business", "Business Codex" and "Enterprise (ChatGPT & Codex)" [2]. Check the live pages and your agreement.

## Overview

ChatGPT is a general-purpose assistant for writing, analysis, research, file and data analysis, image generation and task automation, available on web, desktop and mobile. Organisational plans add a workspace with administration, single sign-on and business data terms. Plans also include Codex, OpenAI's coding agent [2]. OpenAI's enterprise privacy commitments cover ChatGPT Business, Enterprise, Edu and the API Platform, among others [1].

Category: [general-purpose assistant](../tool-categories.md#1-general-purpose-assistants), with [coding assistant](../tool-categories.md#3-coding-assistants) capabilities through Codex.

## Editions and licensing

From OpenAI's business pricing page (UK version) as of October 2026 [2]:

| | Business | Enterprise |
|---|---|---|
| Pricing | Listed at $20 per user per month billed annually, $25 billed monthly | Custom, through sales |
| Minimum seats | 2 users | Not stated publicly |
| SAML SSO | Included | Supported [1] |
| SCIM (directory sync) | Not included | Included |
| Data residency | Not included | Listed as available in ten regions |
| Custom data retention | Not stated on pricing page; admins can set retention [1] | Custom retention policies |
| Connectors | Microsoft 365, Google Drive, Slack, GitHub and others; connector registry not included | Available |
| Support | Enhanced support and dedicated onboarding not included | 24/7 priority support, SLAs, custom legal terms for eligible customers |

"Business Codex" is a usage-based plan with no seat fee [2]. Usage on Business seats is described as unlimited subject to abuse guardrails, with credits available for additional access to some models [2].

## Prerequisites

- A verified email domain you control (needed for SSO) [3].
- An identity provider supporting SAML SSO; for Enterprise, SCIM provisioning [2][3].
- Named Workspace Owners and Admins, and a decision on which users need ChatGPT, Codex or both [3].
- An agreed retention policy and connector policy before broad onboarding.

## Architecture and data flow

1. Users access ChatGPT through web, desktop or mobile clients, signed in through your identity provider.
2. Prompts, uploaded files and content from enabled connectors are processed in OpenAI's cloud.
3. Conversations are stored in the workspace subject to the retention policy set by admins [1].
4. Where enabled, apps, connectors, GPT actions and custom MCP servers can read from or write to external systems [3].
5. Enterprise customers can route logs to their own tools through the Compliance API [1][3].

Data is encrypted at rest with AES-256 and in transit with TLS 1.2 or higher [1].

## Data handling, retention and training-on-data

- **Training.** OpenAI states that by default it does not train its models on business data from these plans; data is used for training only if the customer explicitly opts in, for example through feedback [1].
- **Ownership.** As between customer and OpenAI, the customer retains rights to inputs and owns outputs, where permitted by law [1].
- **Retention, Enterprise and Edu.** Workspace admins set retention periods; deleted conversations are removed within 30 days unless legally required otherwise [1]. OpenAI's admin guidance states conversations persist with no set expiry by default, and that Enterprise owners can set a workspace retention policy with a 90-day minimum [4].
- **Retention, Business.** Admins set retention; deleted or unsaved conversations are removed within 30 days, with exceptions for legal requirements or harm prevention [1].
- **Admin access to conversations.** In ChatGPT Business, admins can view, export and delete end-user conversations in the workspace [1]. Enterprise admins can access an audit log of conversations and GPTs through the Compliance API [1].
- **Residency.** Enterprise lists data residency in ten regions [2]; OpenAI's admin quickstart refers to data residency or inference residency where required [3].
- **Agreements.** A Data Processing Addendum is available for GDPR purposes [1].

## Security and admin controls

- **Certifications.** OpenAI states SOC 2 Type 2 audits are completed for ChatGPT Business, Enterprise, Edu and the API Platform [1]. Further compliance documents are in OpenAI's Trust Portal [4].
- **Role-based access control (RBAC).** Custom roles can be assigned to users or groups; a default workspace role sets the baseline [3].
- **Workspace policy and permissions.** Settings for workspace identity, model defaults, apps, GPTs and data connections [3].
- **Apps and connectors governance.** Audit enabled apps and plug-ins, write or "open-world" actions, allowed OAuth domains and custom MCP servers [3].
- **GPT controls.** Manage GPT access, GPT action domains and apps in GPTs; groups can control access to shared GPTs [3].
- **Additional controls named by OpenAI** (where available): IP allowlisting, Lockdown Mode and Enterprise Key Management [3].
- **Compliance.** Compliance Logs Platform and Stateful Compliance API for audit, SIEM, eDiscovery and DLP workflows [3].

## Identity and access

- **Domain verification** in the Admin Console confirms control of an email domain and enables SSO. Review automatic account creation before applying a verified domain, because it provisions full seats [3].
- **SSO** is supported on Business and Enterprise [1][2].
- **SCIM** (called Directory Sync) synchronises users and groups on Enterprise. Syncing users does not grant product access: synced groups must be assigned to workspaces separately [3].
- **Groups** do not grant permissions alone; roles must be assigned to them [3].

## Integration

- Connectors to common systems such as Microsoft 365, Google Drive, Slack and GitHub [2].
- Custom GPTs with actions, apps and custom MCP servers, governed through permissions [3].
- Compliance API for integration with security and records tooling [3].
- The OpenAI API Platform is a separate service with its own terms, for building your own applications [1].

## Rollout steps

Based on OpenAI's admin quickstart [3]:

1. **Assign roles and scope.** Name Workspace Owners and Admins; decide who needs ChatGPT, Codex or both.
2. **Verify domains** and review automatic account creation settings.
3. **Configure SSO and, for Enterprise, SCIM** before broad onboarding; assign synced groups to the workspace.
4. **Create groups and assign roles** using RBAC.
5. **Configure workspace settings**: workspace policy, permissions and roles, model defaults.
6. **Set the day-one baseline for apps, GPTs and connectors**, using a restrictive default role and custom roles for specialised access.
7. **Enable agents and Codex** for the teams that need them through groups.
8. **Configure security and compliance controls** your risk assessment requires: retention, Compliance API integration, IP allowlisting, residency.
9. **Pilot** with representative users. See the [pilot plan template](../../../toolkits/pilot-plan-template.md).
10. **Set up monitoring**: workspace analytics, usage limits and support processes; expand in waves.

## Enablement and training

- Cover the organisation's [acceptable use policy](../../../toolkits/acceptable-use-policy.md), especially what data may be uploaded and which connectors may be used.
- Teach verification of outputs and citations, and when not to rely on the tool.
- Explain that conversations are retained under the workspace policy and may be visible to admins or exported for compliance [1].
- OpenAI Academy provides admin and user learning resources [4]. See the [training plan template](../../../toolkits/training-plan-template.md).

## Monitoring and usage reporting

OpenAI lists workspace analytics, impact surveys, task insights and usage exports, and usage limits and overages managed through workspace defaults, group defaults and individual overrides. Token-based agreements use a monthly workspace budget with spend alerts [3]. Combine activity data with the approaches in [measuring value](../../measurement/measuring-value.md).

## Known limitations

- **Business lacks SCIM, data residency and the connector registry** on the published pricing page [2]; smaller organisations needing these must move to Enterprise.
- **Default retention** on Enterprise is indefinite until a policy is set, per OpenAI's admin guidance; the retention minimum is 90 days, and shorter retention can limit how many past chats ChatGPT can reference [4].
- **Connectors and write actions** expand the impact of prompt injection and misconfiguration; they need explicit governance [3].
- **Automatic account creation** on a verified domain provisions full seats, with cost implications [3].
- **Outputs can be wrong or incomplete.** See [capabilities and limitations](../../foundations/capabilities-and-limitations.md).
- **Plan names and packaging change often**; agreements signed under earlier plan names may carry different terms.

## Cost considerations

- Per-seat cost (Business) or negotiated pricing (Enterprise) [2].
- Usage-based elements: Business Codex usage, credits for additional model access, token-based agreements with workspace budgets [2][3].
- Seats created by automatic account creation [3].
- Integration effort for SSO, SCIM, Compliance API and connectors.
- Training and change management.

## Exit considerations

- Admins on Business can export end-user conversations [1]; confirm Enterprise export routes (Compliance API, exports) and formats before signing.
- Custom GPTs, actions and workspace configurations are platform-specific.
- Confirm deletion timelines on termination; the documented deletion window for deleted conversations is 30 days, subject to legal exceptions [1].
- Users may hold personal accounts; clarify what happens to work content created there.

## Official documentation links

- [OpenAI enterprise privacy](https://openai.com/enterprise-privacy/)
- [ChatGPT business pricing](https://openai.com/en-GB/business/chatgpt-pricing/)
- [ChatGPT Enterprise admin quickstart](https://help.openai.com/en/articles/20001264-chatgpt-enterprise-admin-quickstart)
- [OpenAI Academy: data governance and compliance](https://academy.openai.com/en/public/clubs/admins-6o6xf/resources/data-governance-and-compliance)

## Questions to verify with OpenAI

- Which ten data residency regions are available, whether the UK is one, and whether residency covers storage, inference or both.
- Default and configurable retention on the Business plan.
- Whether SSO on Business includes enforcement and which identity providers are supported.
- Whether any content is retained for abuse monitoring beyond the workspace retention policy, and under what conditions it may be reviewed by people.
- Current list of sub-processors and model hosting locations.
- Any intellectual property indemnity for outputs, and its conditions.
- Availability and pricing of Enterprise Key Management and Lockdown Mode.

---

**Last verified:** 2026-10-26 against the official documentation listed above.

**Verify before relying on this.** Vendors change products, plans and terms frequently. This guide is descriptive and is not an endorsement. Inclusion in this guide reflects breadth of organisational use, not preference.

## Sources

1. OpenAI, *Enterprise privacy at OpenAI*, accessed 2026-10. https://openai.com/enterprise-privacy/
2. OpenAI, *ChatGPT business pricing* (UK), accessed 2026-10. https://openai.com/en-GB/business/chatgpt-pricing/
3. OpenAI Help Center, *ChatGPT Enterprise admin quickstart*, accessed 2026-10. https://help.openai.com/en/articles/20001264-chatgpt-enterprise-admin-quickstart
4. OpenAI Academy, *Data governance and compliance*, accessed 2026-10. https://academy.openai.com/en/public/clubs/admins-6o6xf/resources/data-governance-and-compliance

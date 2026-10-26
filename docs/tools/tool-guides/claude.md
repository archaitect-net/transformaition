# Claude for organisations

> **Who this is for:** Plan owners and admins, IT and identity teams, platform and developer-tooling teams, security and data protection staff, and rollout leads in organisations that have chosen Anthropic's Claude.
> **Last reviewed:** 2026-10

This guide covers implementing Anthropic's Claude in organisations through three routes: the Claude Team and Enterprise plans (web, desktop and mobile apps), Claude Code (a coding agent), and the Claude API (directly or through cloud platforms). It describes plan differences, data handling and retention, identity and admin controls, a numbered rollout, usage reporting and known limitations, with links to Anthropic's documentation. It assumes the product has already been chosen; for selection, see [choosing tools](../choosing-tools.md).

> **Verify before relying on this.** Anthropic's plans, seat types and features change frequently. As of October 2026 the Enterprise plan has moved to a single seat type with usage billed separately, and legacy seat types end at renewal [3]. Check the live pages and your agreement.

## Overview

| Route | What it is | Typical users |
|---|---|---|
| **Claude Team / Enterprise** | Claude apps (web, desktop, mobile) with workspace administration, connectors and business data terms; includes Claude Code and Cowork [2][3] | Knowledge workers across the organisation |
| **Claude Code** | An agentic coding tool that runs locally on developer machines or in Anthropic-managed cloud sessions, reading and editing code and running commands [5] | Developers, data and platform engineers |
| **Claude API** | Programmatic access to Claude models through Anthropic's platform, or through Amazon Bedrock, Google Cloud's Agent Platform and Microsoft Foundry [5] | Developers building applications |

Category: [general-purpose assistant](../tool-categories.md#1-general-purpose-assistants), [coding assistant](../tool-categories.md#3-coding-assistants) and [model API](../tool-categories.md#5-cloud-ai-platforms-and-model-apis).

## Editions and licensing

From Anthropic's pricing page and Enterprise plan article as of October 2026 [2][3]:

| | Team | Enterprise |
|---|---|---|
| Size | 2 to 150 users | Self-serve minimum 20 seats; sales-assisted minimum 50 seats [3] |
| Seats | Standard seat (listed at $20/month annual, $25 monthly) and Premium seat (listed at $100/month annual, $125 monthly, with five times Standard usage); can be mixed | Single Enterprise seat (listed at $20 per seat per month, billed annually) covering access only; **all usage billed separately at API rates** [2][3] |
| Included | Claude Code, Cowork, connectors (including Microsoft 365), enterprise search, SSO, admin controls for remote and local connectors, usage analytics; no model training on content by default | Everything in Team, plus SCIM, role-based access, audit logs, Compliance API, Analytics API, custom data retention, IP allowlisting and network-level access control, customer-managed encryption keys, HIPAA-ready configuration for eligible organisations, admin-set spend limits [2][3] |
| Not included | SCIM, role-based access, audit logs, Compliance API, custom retention, HIPAA-ready offering, domain capture | |
| Payment | Credit card only | Self-serve: card or ACH (USD); sales-assisted: invoicing, multi-currency, AWS Marketplace [2][3] |

Organisations on legacy Enterprise seat types (Chat, Chat + Claude Code, Standard and Premium) keep their terms until renewal [3].

**API** pricing is per token by model. US-only inference is available for API workloads at 1.1 times standard token pricing [2].

## Prerequisites

- **Owner or Primary Owner** role on the plan to configure SSO [4].
- **Control of DNS** for your email domain (domain verification by TXT record) and **control of your identity provider** [4].
- For Claude Code: developer machines meeting Claude Code's requirements, and a decision on authentication route (plan seat, API key, or cloud provider) [5].
- An agreed connector, retention and spend policy before broad rollout.

## Architecture and data flow

**Claude apps (Team / Enterprise).** Prompts, files and connector content are sent to Anthropic's cloud for processing; chats are stored in the product for history [6].

**Claude Code** [5]:

1. Claude Code runs locally and sends prompts, relevant file contents and model outputs to the model provider over TLS 1.2+.
2. Encryption at rest depends on provider: Anthropic API (AES-256 disk encryption); Amazon Bedrock (AWS-managed keys, customer-managed keys via KMS); Google Cloud's Agent Platform (Google-managed keys, CMEK available); Microsoft Foundry (depends on hosting option; for "Hosted on Azure" deployments prompts and completions remain within Azure apart from usage metadata and safety-flagged content).
3. Session transcripts are cached locally in plaintext under `~/.claude/projects/` for 30 days by default, adjustable with `cleanupPeriodDays`.
4. In Anthropic-hosted cloud sessions, the repository is cloned into an isolated virtual machine, outbound traffic passes through a security proxy, and GitHub credentials stay on Anthropic servers rather than in the VM. Organisations can route cloud sessions to self-hosted environments.

## Data handling, retention and training-on-data

- **Training.** Anthropic states that by default it does not use inputs or outputs from commercial products (including Team, Enterprise and API) to train models. Data may be used if the customer submits feedback or explicitly opts in, for example through the Development Partner Program for the first-party API [1][5].
- **Feedback.** Conversations submitted with thumbs up/down are stored for up to 5 years, de-linked from user IDs. Team and Enterprise owners can disable feedback with the "Rate chats" setting [1].
- **Retention in Claude apps.** Deleting a conversation removes it from history immediately and from back-end storage within 30 days. Inputs and outputs flagged for Usage Policy violations may be kept for up to 2 years, and trust and safety classification scores for up to 7 years [6].
- **Custom retention.** Enterprise customers can set custom retention timelines [2][7].
- **API.** Inputs and outputs are automatically deleted within 30 days, except where you use features with longer retention (for example the Files API), have a zero data retention agreement, or for Usage Policy enforcement and legal compliance [6].
- **Claude Code (commercial).** Standard retention is 30 days. Zero data retention is available to qualified Claude for Enterprise accounts, enabled per organisation by the account team; it is not part of the standard plan [5].
- **Residency.** US-only inference is offered for Enterprise and API workloads [2][3]. Through Bedrock, Agent Platform or Foundry, the cloud provider's regional controls apply (see [cloud AI platforms](cloud-ai-platforms.md)).

## Security and admin controls

- **Enterprise controls**: role-based access with fine-grained permissions, audit logs, Compliance API, custom retention, IP allowlisting, network-level access control, customer-managed encryption keys, spend limits at organisation and user level [2][3].
- **Team controls**: SSO and admin controls for remote and local connectors [2].
- **Claude Code**: settings can be distributed in `settings.json`; telemetry, error reporting and feedback commands can be disabled with environment variables, and `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` disables non-essential traffic in one setting. When using Bedrock, Agent Platform or Foundry, metrics, error reporting and `/feedback` uploads are off by default [5].
- **Compliance documentation** is available through Anthropic's Trust Center [1][5].

## Identity and access

From Anthropic's SSO article [4]:

- **SSO** is available on Team and Enterprise.
- **Provisioning**: manual, just-in-time (JIT) or SCIM. **SCIM is Enterprise-only**.
- JIT and SCIM support group mappings that control the role users receive.
- Domain verification at the admin identity settings page uses a DNS TXT record; verifying a domain does not change existing users until SSO is set up and enforced.
- A "Disable new organization creation" setting blocks users from creating new organisations with verified domains.
- Microsoft Entra pushes SCIM changes every 40 minutes, so changes can lag.

## Integration

- **Connectors** for Google Drive, Gmail, Google Calendar, GitHub, Microsoft 365 and Slack on Enterprise; Team includes connectors and Microsoft 365 [2][3].
- **Remote and local connectors** (including MCP servers) with admin controls on both plans [2].
- **Compliance API and Analytics API** on Enterprise [3].
- **Cloud platforms.** Claude models are available through Amazon Bedrock, Google Cloud's Agent Platform and Microsoft Foundry; Claude Code can be configured to use any of them [5].

## Rollout steps

1. **Choose the route(s)**: apps plan, Claude Code, API, or a combination; and for Claude Code and API, whether to use Anthropic directly or a cloud provider [5].
2. **Choose the plan and seat mix** against required controls: SCIM, audit logs, Compliance API and custom retention require Enterprise [2].
3. **Verify your domain** and configure **SSO**; on Enterprise configure **SCIM** and group-to-role mappings [4].
4. **Disable new organisation creation** on verified domains to prevent unmanaged workspaces [4].
5. **Set data policies**: retention (Enterprise), feedback setting, connector allow-list, spend limits [1][2][3].
6. **For Claude Code**, distribute managed settings, decide telemetry settings, and define permission rules for commands and network access [5].
7. **Pilot** with a cross-section of users. See the [pilot plan template](../../../toolkits/pilot-plan-template.md).
8. **Connect audit and compliance tooling** through the Compliance API (Enterprise) [3].
9. **Expand in waves** with training, monitoring spend and usage.
10. **Review** connectors, retention and spend limits regularly.

## Enablement and training

- Cover the [acceptable use policy](../../../toolkits/acceptable-use-policy.md), especially connectors and uploads.
- For Claude Code, train developers on permission prompts, reviewing changes before committing, and protecting secrets in the working directory.
- Explain that local Claude Code transcripts are stored in plaintext on the device [5].
- Anthropic's help centre and documentation provide user and admin guidance. See the [training plan template](../../../toolkits/training-plan-template.md).

## Monitoring and usage reporting

- **Usage analytics** are available on Team and Enterprise; the **Analytics API** on Enterprise [2][3].
- **Spend limits** on Enterprise at organisation and user level [3].
- **Claude Code** can export metrics to your own OpenTelemetry collector [5].
- Combine with [measuring value](../../measurement/measuring-value.md).

## Known limitations

- **Team plan lacks** SCIM, audit logs, Compliance API, role-based access and custom retention [2]. Organisations with these requirements need Enterprise, which has a 20-seat minimum [3].
- **Enterprise usage is billed at API rates** on top of the seat fee, so costs depend on usage and model choice [3].
- **Usage Policy-flagged content** can be retained for up to 2 years regardless of customer retention settings [6].
- **Claude Code agentic actions** can run commands and modify files; controls depend on your permission configuration and review processes [5].
- **Local plaintext transcripts** for Claude Code [5].
- **Data residency** is described in terms of US-only inference; check other regional options with Anthropic or use a cloud provider route [2].
- **Outputs can be wrong or incomplete.** See [capabilities and limitations](../../foundations/capabilities-and-limitations.md).

## Cost considerations

- Team: per-seat price, mix of Standard and Premium seats [2].
- Enterprise: seat fee plus usage at API rates; model spend scenarios and use spend limits [3].
- API: per-token pricing by model; US-only inference at 1.1 times standard pricing [2].
- Claude Code usage can be significant for heavy agentic use; monitor with analytics and spend limits.
- Through cloud providers, billing follows that provider's pricing.

## Exit considerations

- Confirm export options for conversations, projects and configuration before signing.
- Deleted conversations leave back-end storage within 30 days [6]; confirm termination deletion terms in your agreement.
- MCP-based connectors use an open protocol, which may reduce switching cost for integrations.
- Using Claude through a cloud platform can make switching models within that platform easier.

## Official documentation links

- [Is my data used for model training?](https://privacy.claude.com/en/articles/7996868)
- [How long do you store my organization's data?](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)
- [Claude pricing](https://claude.com/pricing)
- [What is the Enterprise plan?](https://support.claude.com/en/articles/9797531)
- [Setting up SSO on Team and Enterprise plans](https://support.claude.com/en/articles/9797544-setting-up-single-sign-on-sso-on-team-and-enterprise-plans)
- [Claude Code data usage](https://code.claude.com/docs/en/data-usage)

## Questions to verify with Anthropic

- Default retention for Team plan conversations that are not deleted.
- Data residency options beyond US-only inference, including UK and EU processing.
- Eligibility criteria and process for zero data retention on Claude Code and the API.
- Export formats available to admins on Team and Enterprise.
- Current certifications covering the apps, Claude Code cloud sessions and API (see the Trust Center).
- Any intellectual property indemnity for outputs, and its conditions.

---

**Last verified:** 2026-10-26 against the official documentation listed above.

**Verify before relying on this.** Vendors change products, plans and terms frequently. This guide is descriptive and is not an endorsement. Inclusion in this guide reflects breadth of organisational use, not preference.

## Sources

1. Anthropic Privacy Center, *Is my data used for model training?*, accessed 2026-10. https://privacy.claude.com/en/articles/7996868
2. Anthropic, *Claude pricing*, accessed 2026-10. https://claude.com/pricing
3. Anthropic Help Center, *What is the Enterprise plan?*, accessed 2026-10. https://support.claude.com/en/articles/9797531
4. Anthropic Help Center, *Setting up single sign-on (SSO) on Team and Enterprise plans*, accessed 2026-10. https://support.claude.com/en/articles/9797544-setting-up-single-sign-on-sso-on-team-and-enterprise-plans
5. Anthropic, *Claude Code: Data usage*, accessed 2026-10. https://code.claude.com/docs/en/data-usage
6. Anthropic Privacy Center, *How long do you store my organization's data?*, accessed 2026-10. https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data
7. Anthropic Privacy Center, *Can you delete data that I sent via Team and Enterprise plans?*, accessed 2026-10. https://privacy.claude.com/en/articles/9796617-can-you-delete-data-that-i-sent-via-team-and-enterprise-plans

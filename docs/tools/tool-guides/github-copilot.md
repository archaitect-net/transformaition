# GitHub Copilot

> **Who this is for:** GitHub organisation and enterprise owners, developer-platform teams, security and data protection staff, and engineering leads in organisations that have chosen GitHub Copilot.
> **Last reviewed:** 2026-10

This guide covers implementing GitHub Copilot for organisations through the Copilot Business and Copilot Enterprise plans: inline suggestions, chat, code review and the Copilot cloud agent. It describes plans and billing, policies, content exclusion, public-code matching, agent safeguards, usage metrics and known limitations, with links to GitHub's documentation. It assumes the product has already been chosen; for selection, see [choosing tools](../choosing-tools.md).

> **Verify before relying on this.** GitHub's Copilot plans and billing have changed significantly. As of October 2026, organisational plans include monthly pools of "GitHub AI Credits", and the coding agent is documented as "Copilot cloud agent" [1][5]. Check the live documentation and your agreement.

## Overview

Copilot provides inline code suggestions and next-edit suggestions in supported IDEs, Copilot Chat, Copilot code review, and the Copilot cloud agent, which works on tasks and opens pull requests [1][5]. Organisations can also enable third-party coding agents from Anthropic and OpenAI as "partner agents" [3].

Category: [coding assistant](../tool-categories.md#3-coding-assistants), with [agent](../tool-categories.md#4-agents-and-automation) capabilities.

## Editions and licensing

From GitHub's plans page as of October 2026 [1]:

| Plan | Listed price | Included AI credits | Notes |
|---|---|---|---|
| Copilot Business | $19 per granted seat per month | 1,900 per user per month | Centralised management and policy control |
| Copilot Enterprise | $39 per granted seat per month | 3,900 per user per month | All Business features plus additional enterprise capabilities |

- Usage beyond the pool is charged at $0.01 per AI credit. Code completions and next-edit suggestions are not billed in AI credits [1].
- Inline suggestion and Copilot Chat features are available in all plans [1].
- Individual plans (Free, Student, Pro, Pro+, Max) exist; organisations should ensure work use happens under organisational plans so policies apply [1].

## Prerequisites

- A GitHub organisation (for Business) or enterprise account (for Enterprise or managed Business) [1].
- Supported IDEs and extension versions for developers; metrics require specific IDEs and minimum versions [6].
- Decisions on policies, content exclusion and agent use before assigning seats.
- Branch protection and required reviews configured on repositories where agents will work [5].

## Architecture and data flow

1. In the IDE, Copilot sends context (code around the cursor, open files and other relevant content) to GitHub's service to generate suggestions or chat responses.
2. Models from several providers are available; organisations control which models beyond the basic set are enabled [3].
3. On GitHub.com, chat, code review and the cloud agent operate on repository content.
4. The cloud agent runs tasks in a GitHub-hosted environment with restricted internet access through a firewall, pushes to a single `copilot/` branch, and opens draft pull requests [5].

## Data handling, retention and training-on-data

GitHub publishes data-handling commitments for Copilot in its Trust Center, which has moved over time (the former Copilot Trust Center address now redirects) [7]. This guide could not verify current retention periods for prompts and suggestions, or the current training-on-data commitment wording, from GitHub's documentation within the review window. **Verify these directly** (see questions below) before rollout.

What is documented:

- **Content exclusion** prevents Copilot from using specified files for suggestions and chat in supported surfaces (see limitations) [2].
- **Code referencing**: when suggestions matching public code are allowed, Copilot shows references to matching public repositories and licence information; organisations can instead choose to block such suggestions [4].
- **Feedback collection** is an organisation-level opt-in [3].

## Security and admin controls

**Organisation and enterprise policies** [3]:

- Feature and privacy policies, controlling which Copilot features are available.
- **Models**: which models beyond the basic set are available (some may incur extra cost).
- **MCP servers in Copilot**: whether MCP servers can be used.
- **Partner agents**: toggles for Anthropic Claude and OpenAI Codex agents, which can access repositories where the cloud agent is enabled.
- Preview features opt-in; feedback collection opt-in.
- Enterprise-level policies cannot be overridden by organisations.

**Content exclusion** [2]: available on Business and Enterprise; configurable by repository admins, organisation owners and enterprise owners. Excluded files are not used for inline suggestions or chat, and are skipped in Copilot code review.

**Cloud agent safeguards** [5]:

| Risk | Documented mitigation |
|---|---|
| Unwanted pushes | Pushes only to a single `copilot/` branch (or the PR branch it was triggered on); branch protections apply |
| Untrusted users directing the agent | Only users with write access can trigger it; comments from others are not passed to it |
| Unreviewed merges | Agent cannot mark PRs ready, approve or merge; the requester cannot approve its PR |
| Workflows running unreviewed code | Actions workflows need approval by a user with write access unless an admin enables automatic runs |
| Data exfiltration | Internet access restricted by a customisable firewall |
| Vulnerable code | CodeQL, secret scanning, dependency checks and Copilot code review run on agent changes |
| Prompt injection | Hidden characters such as HTML comments are filtered |
| Auditability | Signed commits authored by Copilot, session logs and audit log events |

## Identity and access

- Seats are granted to users in the organisation or enterprise; billing is per granted seat [1].
- Enterprise owners can view enterprise metrics; organisation-level access to metrics can be delegated through a custom role [6].
- The cloud agent can only be triggered by users with write access [5].

## Integration

- IDE support includes VS Code, Visual Studio, JetBrains IDEs, Xcode and Eclipse, among others [6].
- GitHub.com, GitHub Mobile and the Copilot CLI provide additional surfaces [2].
- MCP servers can extend Copilot where enabled by policy [3].
- Usage metrics APIs and NDJSON exports feed your own BI tools [6].

## Rollout steps

1. **Choose the plan** (Business or Enterprise) and confirm AI credit pools and overage handling [1].
2. **Set enterprise and organisation policies**: features, models, MCP, partner agents, preview features [3].
3. **Decide on public-code matching**: block suggestions matching public code, or allow with references [4].
4. **Configure content exclusion** for sensitive files and repositories, knowing its limitations [2].
5. **Harden repositories** for agent use: branch protection, required reviews, Actions approval settings, firewall configuration [5].
6. **Pilot** with a few teams across languages and IDEs. See the [pilot plan template](../../../toolkits/pilot-plan-template.md).
7. **Enable metrics**, including IDE telemetry, and agree what you will measure [6].
8. **Assign seats in waves**, with training.
9. **Monitor AI credit consumption** and adjust model availability or budgets.
10. **Review policies** as GitHub adds features and models.

## Enablement and training

- Train developers to review suggestions as they would a colleague's code, check licences on referenced matches, and keep secrets out of code.
- Explain which modes are covered by content exclusion and which are not [2].
- Agree team practices for reviewing agent pull requests.
- See the [developers pathway](../../pathways/developers.md) and [training plan template](../../../toolkits/training-plan-template.md).

## Monitoring and usage reporting

From GitHub's metrics documentation [6]:

- A **usage metrics dashboard** shows 28-day trends across an enterprise and its organisations; there are also code generation and impact dashboards.
- **Usage metrics APIs** provide data at enterprise, organisation, repository and user levels, with NDJSON export.
- **Gaps**: most metrics rely on IDE telemetry; Copilot Chat on GitHub.com and GitHub Mobile is not included; licence data is not in these reports; data arrives within two full UTC days; organisation figures cannot be summed to enterprise totals; return-on-investment estimates appear only in the dashboard.

Usage is not impact. See [measuring value](../../measurement/measuring-value.md).

## Known limitations

- **Content exclusion gaps** [2]: semantic information from excluded files may still reach Copilot through the IDE; exclusions do not apply to symbolic links or remote filesystems; **exclusions are not supported in Edit and Agent modes of Copilot Chat in VS Code and other editors**; support varies by surface; support on GitHub.com and Mobile is in public preview.
- **Code referencing** searches only public GitHub repositories, with an index refreshed every few months [4].
- **Metrics** depend on IDE telemetry and exclude some surfaces [6].
- **Usage-based billing** through AI credits makes costs variable [1].
- **Agents** act on repositories; safety depends on your branch protection, review and workflow settings [5].
- **Suggestions can be insecure or wrong.** See [capabilities and limitations](../../foundations/capabilities-and-limitations.md).

## Cost considerations

- Per-seat price plus AI credit overages beyond the pooled allowance [1].
- Choice of models affects credit consumption [3].
- Actions minutes for agent workflows, and any security tooling.
- Time spent reviewing agent pull requests.

## Exit considerations

- Copilot policies, custom instructions and agent configurations are specific to GitHub.
- Code produced remains in your repositories.
- Confirm deletion of retained prompts and telemetry on termination with GitHub.
- MCP-based integrations use an open protocol and may carry over to other tools.

## Official documentation links

- [Plans for GitHub Copilot](https://docs.github.com/en/copilot/get-started/plans)
- [Content exclusion](https://docs.github.com/en/copilot/concepts/context/content-exclusion)
- [Policies for Copilot in your organisation](https://docs.github.com/enterprise-cloud@latest//copilot/managing-copilot/managing-github-copilot-in-your-organization/setting-policies-for-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization)
- [Code referencing](https://docs.github.com/en/copilot/concepts/completions/code-referencing)
- [Risks and mitigations for Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations)
- [About Copilot usage metrics](https://docs.github.com/en/copilot/concepts/copilot-usage-metrics/copilot-metrics)
- [GitHub Copilot Trust Center](https://resources.github.com/copilot-trust-center)

## Questions to verify with GitHub

- Retention periods for prompts, suggestions and engagement data on each surface (IDE, GitHub.com, CLI, cloud agent) under Business and Enterprise.
- Current contractual commitment on training models with organisational code and prompts.
- Terms of any intellectual property indemnity and whether it depends on blocking suggestions matching public code.
- Data processing locations and data residency options.
- Data handling terms for third-party models and partner agents enabled through Copilot.
- Which features are exclusive to Copilot Enterprise.

---

**Last verified:** 2026-10-26 against the official documentation listed above.

**Verify before relying on this.** Vendors change products, plans and terms frequently. This guide is descriptive and is not an endorsement. Inclusion in this guide reflects breadth of organisational use, not preference.

## Sources

1. GitHub Docs, *Plans for GitHub Copilot*, accessed 2026-10. https://docs.github.com/en/copilot/get-started/plans
2. GitHub Docs, *Content exclusion for GitHub Copilot*, accessed 2026-10. https://docs.github.com/en/copilot/concepts/context/content-exclusion
3. GitHub Docs, *Managing policies and features for Copilot in your organization*, accessed 2026-10. https://docs.github.com/enterprise-cloud@latest//copilot/managing-copilot/managing-github-copilot-in-your-organization/setting-policies-for-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization
4. GitHub Docs, *GitHub Copilot code referencing*, accessed 2026-10. https://docs.github.com/en/copilot/concepts/completions/code-referencing
5. GitHub Docs, *Risks and mitigations for GitHub Copilot cloud agent*, accessed 2026-10. https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations
6. GitHub Docs, *About Copilot usage metrics*, accessed 2026-10. https://docs.github.com/en/copilot/concepts/copilot-usage-metrics/copilot-metrics
7. GitHub, *GitHub Copilot Trust Center* (redirects to GitHub's Trust Center), accessed 2026-10. https://resources.github.com/copilot-trust-center

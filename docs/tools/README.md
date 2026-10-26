# Tools

> **Who this is for:** Anyone involved in choosing, buying, configuring or supporting AI tools: business owners, IT and platform teams, procurement, security, data protection and team leads.
> **Last reviewed:** 2026-10

This section is in two parts, in a deliberate order. First comes **neutral selection**: a taxonomy of tool categories and a requirements-led method for choosing between them, with no vendor preference. Only after you have chosen does the second part apply: **tool guides**, which are factual, dated implementation notes for widely used products. Keeping the two apart stops implementation detail from turning into a recommendation, and makes sure your requirements, not a vendor's feature list, drive the decision.

## How this section works

```
 Your use cases and requirements
              |
              v
 1. Understand the categories   ->  tool-categories.md
              |
              v
 2. Choose against your criteria ->  choosing-tools.md
              |                       (plus assessments/vendor-due-diligence.md)
              v
 3. Implement what you chose     ->  tool-guides/
```

| Step | Page | What you get | When to use it |
|---|---|---|---|
| 1 | [Tool categories](tool-categories.md) | A neutral taxonomy of eight kinds of AI tool, with typical deployment, data flow, cost model and several example products per category | Early, while framing options; before talking to vendors |
| 2 | [Choosing tools](choosing-tools.md) | A requirements-led method, weighted criteria, a fair evaluation protocol, a build/buy/configure decision tree and procurement considerations | When you have candidate use cases and need to shortlist and decide |
| 3 | [Tool guides](tool-guides/README.md) | Implementation notes for specific products: editions, data handling, admin controls, rollout steps, limitations, exit considerations | After a decision, or when you already run a product and want to configure it well |

## Why selection comes before guides

- **Requirements first.** Many organisations start from a product that is already licensed or heavily marketed. That can be the right answer, but it should be tested against your own use cases and constraints rather than assumed. See [Select](../lifecycle/03-select.md) in the adoption lifecycle.
- **Categories differ more than products do.** The biggest decisions (for example, whether data leaves your environment, who administers the tool, how it is priced) are often set by the *category* of tool, not the brand. Decide the category first.
- **Guides describe; they do not compare.** Each tool guide follows the same [template](tool-guides/_template.md) and is written with equal depth and tone. Inclusion reflects how widely a product is used in organisations, not preference. A product without a guide is not thereby excluded.

## What this section does not do

- It does not rank vendors or say which product is best.
- It does not replace your own evaluation. Model quality and fitness for purpose vary by task, language and data; only testing with your own examples tells you how a tool performs for you.
- It does not replace legal, procurement or security review. Use the [vendor due diligence](../../assessments/vendor-due-diligence.md) questionnaire and the [governance](../governance/README.md) section alongside it.

## Small organisations

If you have fewer than 50 people and no dedicated IT team, the same order still applies, but in a lighter form:

1. Write down two or three tasks you want help with and what data those tasks touch.
2. Use [tool categories](tool-categories.md) to work out which category fits; often it is a general-purpose assistant or an AI feature in software you already use.
3. Use the "minimum viable evaluation" in [choosing tools](choosing-tools.md#a-lighter-version-for-small-organisations) to compare two options on your own examples.
4. Before buying, check the business or team plan terms on data use for training, retention and admin controls. The tool guides list the questions to ask.

## Related pages

- [Select stage of the lifecycle](../lifecycle/03-select.md)
- [Pilot stage](../lifecycle/04-pilot.md)
- [Vendor due diligence](../../assessments/vendor-due-diligence.md)
- [Data protection](../governance/data-protection.md) and [security](../governance/security.md)
- [What are AI tools?](../foundations/what-are-ai-tools.md)

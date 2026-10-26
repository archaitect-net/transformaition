# Evidence on impact

> **Who this is for:** Anyone building a business case, setting expectations, or challenging claims about what generative AI does to productivity and quality at work.
> **Last reviewed:** 2026-10

This page summarises the most rigorous published studies on how generative AI tools affect work: speed, output quality, who benefits, and where things go wrong. Each study carries an evidence label (see [CONTRIBUTING.md](../../CONTRIBUTING.md#evidence-labels)) and a note on caveats, including vendor involvement. The short version: controlled studies show large gains on well-suited tasks, especially for less experienced workers, but also show harm on tasks just outside what the tools do well, a persistent gap between how fast people *feel* and how fast they *are*, and much smaller effects at the level of whole jobs, firms and labour markets than task-level studies suggest. Use this evidence to frame hypotheses, then test them in your own [pilot](../lifecycle/04-pilot.md).

## How to read this evidence

Before relying on any figure, ask five questions.

| Question | Why it matters |
|---|---|
| **Task, job or organisation?** | A 40% speed-up on one writing task is not a 40% productivity gain for a job, which is a bundle of many tasks. Organisation-level and labour-market effects are typically much smaller than task-level effects. |
| **Randomised or observational?** | Randomised controlled trials (RCTs) give the cleanest estimate of cause and effect. Observational and before/after studies are vulnerable to selection (keen adopters differ from everyone else). |
| **Measured or self-reported?** | Several studies find that people's estimates of time saved differ substantially from measured time. Treat self-reported savings as a ceiling, not a measurement. |
| **Which tool, which date?** | Model capability changes quickly. A 2023 result describes 2023 tools. That cuts both ways: newer tools may do more, but results do not transfer automatically. |
| **Who funded or ran it?** | Vendor-authored studies can be rigorous, but they are labelled here so you can weigh them. Per this guide's standards, vendor-run studies are labelled **Limited** regardless of design. |

## Summary table

| Study | Setting | Design | Headline finding | Evidence label |
|---|---|---|---|---|
| Brynjolfsson, Li and Raymond (2025) | Customer support, 5,179 agents | Staggered field rollout | +14% issues resolved per hour; +34% for novice and low-skilled agents | Moderate |
| Noy and Zhang (2023) | Professional writing tasks, 453 participants | Preregistered online RCT | 40% less time; 18% higher quality | Moderate |
| Dell'Acqua et al. (2023) | Management consulting, 758 consultants | Preregistered field RCT | Inside the frontier: +12.2% tasks, 25.1% faster, >40% higher quality. Outside: 19 percentage points less likely to be correct | Moderate |
| Dell'Acqua et al. (2025) | Product innovation, 776 professionals | Preregistered field RCT | Individuals with AI matched teams without AI | Moderate |
| Otis et al. (2024) | Kenyan small business owners, 640 | Field RCT, 5 months | No average effect; high performers +15%, low performers −8% | Moderate |
| Cruces et al. (2026) | Business problem-solving, 1,174 adults | Online RCT | All improved; education-based performance gap narrowed by about three-quarters | Moderate |
| Peng et al. (2023) | Single coding task, 95 recruited developers | Lab RCT | 55.8% faster | Limited (vendor-authored, small, single task) |
| Cui et al. (2025) | Developers at three firms, 4,867 | Three field RCTs | +26.08% completed tasks | Limited (vendor co-authored) |
| METR (2025) | 16 experienced open-source developers, 246 tasks | RCT | 19% *slower* with AI, despite believing they were faster | Moderate (randomised but small) |
| Dillon et al. (2025) | Knowledge workers, 66 firms | Field RCT, 6 months | Less time on email; no change in meeting time | Limited (vendor-authored) |
| Humlum and Vestergaard (2025) | Danish workers, about 25,000 per round | Surveys linked to administrative data | Self-reported time savings 2.8% of hours; no detectable effect on earnings or hours | Moderate |
| UK government Copilot evaluations (2025) | UK civil servants | Self-report and mixed methods | 26 minutes a day self-reported (GDS); no robust productivity evidence (DBT) | Limited |

## Study summaries

### Customer support: Brynjolfsson, Li and Raymond

**What they did.** Studied the staggered introduction of a generative AI conversational assistant to 5,179 customer support agents at one firm, comparing agents before and after access and against those not yet given access [1].

**What they found.** Issues resolved per hour rose by 14% on average, with a 34% improvement for novice and low-skilled agents and minimal impact on the most experienced and skilled. The authors also report improved customer sentiment and employee retention, and evidence consistent with less experienced agents learning from the tool [1].

**Caveats.** One firm, one function, a tool trained partly on the firm's own best performers' conversations. The finding that top performers gained little is as important as the average.

**Evidence label:** Moderate. Published in the *Quarterly Journal of Economics* (2025).

### Professional writing: Noy and Zhang

**What they did.** A preregistered online experiment in which 453 college-educated professionals completed occupation-specific writing tasks (such as press releases and short reports); half were randomly given access to ChatGPT [2].

**What they found.** Average time taken fell by 40% and output quality rose by 18%. Inequality between workers narrowed, because weaker writers gained more [2].

**Caveats.** Short, self-contained tasks that suit the tool well; no organisational context, review process or downstream consequences.

**Evidence label:** Moderate. Published in *Science* (2023).

### Consulting and the "jagged frontier": Dell'Acqua et al.

**What they did.** A preregistered field experiment with 758 Boston Consulting Group consultants, about 7% of the firm's individual-contributor consultants. Participants were randomly assigned to work with or without GPT-4 on realistic consulting tasks. Some tasks were chosen to sit inside the AI's capability "frontier"; one was designed to sit just outside it [3].

**What they found.** On 18 tasks inside the frontier, consultants using AI completed 12.2% more tasks, 25.1% faster, with more than 40% higher quality. Below-average performers improved by 43% and above-average performers by 17%. On the task outside the frontier, consultants using AI were 19 percentage points *less* likely to produce a correct solution [3].

The authors describe the frontier as "jagged": tasks of apparently similar difficulty can fall either side of it, and it is not obvious in advance which side a task is on. They also observed two working styles: "Centaurs", who divided work between themselves and the AI, and "Cyborgs", who integrated AI throughout [3].

**Caveats.** Experimental tasks rather than client work; the study was co-authored with BCG staff. The specific frontier has moved since 2023, but the general pattern (uneven capability, invisible boundaries) is the durable lesson.

**Evidence label:** Moderate. Harvard Business School Working Paper 24-013 (2023).

### Teamwork: Dell'Acqua et al., "The Cybernetic Teammate"

**What they did.** A preregistered field experiment with 776 professionals at Procter & Gamble, randomly assigned to work alone or in pairs, with or without AI, on real product-innovation challenges [4].

**What they found.** Individuals using AI performed at a level comparable to two-person teams without AI. AI use also reduced the tendency of R&D and commercial staff to produce solutions skewed towards their own function, and participants reported more positive emotional responses [4].

**Caveats.** One company, one type of task (idea generation and development), and a one-day exercise.

**Evidence label:** Moderate. NBER Working Paper 33641 (2025).

### Small businesses: Otis et al.

**What they did.** A five-month RCT with 640 entrepreneurs in Kenya, who received either a standard business guide or access to a GPT-4-based business mentor via WhatsApp [5].

**What they found.** No positive effect on average. High-performing entrepreneurs saw revenue or profits rise by about 15%, while low performers saw revenue fall by about 8%. The researchers link the difference to how people used the tool: lower performers tended to ask for help with harder, more open-ended problems [5].

**Caveats.** A specific context; advice rather than task execution. The lesson that the same tool can help some users and harm others is relevant to small organisations everywhere.

**Evidence label:** Moderate.

### Education gaps: Cruces et al.

**What they did.** A randomised online experiment with 1,174 adults aged 25 to 45 completing an incentivised, workplace-style business problem-solving task with or without a generative AI assistant, followed by a task without AI [6].

**What they found.** AI improved performance for everyone, with larger gains for participants with less formal education. The performance gap between education groups shrank by about three-quarters with AI. Once AI was removed, a sizeable gap reappeared, and lasting benefit depended on combining AI use with sustained personal effort [6].

**Evidence label:** Moderate. NBER Working Paper 34851 (2026).

### Software development: three contrasting results

Developer productivity is the most-studied area, and the results disagree. Reading them together is more useful than citing any one.

**Peng et al. (2023).** 95 professional developers were recruited and randomly assigned to implement an HTTP server in JavaScript with or without GitHub Copilot. The Copilot group finished 55.8% faster (95% confidence interval 21% to 89%) [7]. **Vendor involvement:** authors were from Microsoft Research and GitHub. **Caveats:** one small, well-specified, greenfield task. **Evidence label:** Limited.

**Cui et al. (2025).** Three field experiments covering 4,867 developers at Microsoft, Accenture and an anonymous Fortune 100 company. Developers with access to an AI coding assistant completed 26.08% more tasks (standard error 10.3%), with larger gains and higher adoption among less experienced developers [8]. **Vendor involvement:** co-authors include Microsoft researchers. **Caveats:** "completed tasks" (such as pull requests) is a proxy for output, not value or quality. **Evidence label:** Limited.

**METR (2025).** 16 experienced open-source developers worked on 246 real issues in large repositories they knew well; each issue was randomly assigned to allow or disallow AI tools (mainly Cursor with Claude 3.5/3.7 Sonnet). With AI allowed, tasks took 19% *longer*. Before the study, developers forecast a 24% speed-up; afterwards, they still believed AI had sped them up by about 20% [9]. **Caveats the authors stress:** a snapshot of early-2025 tools in one demanding setting (experts in mature codebases); it does not show that AI fails to help most developers. METR has since stated that these results no longer reflect current tools [9].

In February 2026 METR reported early data from a larger follow-up (57 developers, more than 800 tasks, late-2025 tools). Point estimates now suggested speed-ups (about 18% for returning developers and 4% for new ones), but confidence intervals included zero. METR described the data as very weak evidence because many developers refused to work without AI, which biases the sample, and announced it was redesigning the study [10]. **Evidence label for METR's work:** Moderate (randomised, small samples).

**Team-level survey evidence.** Google's DORA research programme surveys technology professionals annually. Its 2024 report estimated that a 25% increase in AI adoption was associated with a 1.5% decrease in delivery throughput and a 7.2% decrease in delivery stability [11]. Its 2025 report (nearly 5,000 respondents) found AI use near-universal, now positively associated with throughput but still associated with rising instability, and characterised AI as an "amplifier" of existing organisational strengths and weaknesses [12]. **Vendor involvement:** DORA is run by Google, an AI vendor. **Evidence label:** Limited (survey, correlational).

**What to take from the software evidence.** Gains appear largest on well-specified, self-contained tasks and for less experienced developers. Experts working in complex, familiar codebases may see little or negative benefit. Faster code production does not automatically mean faster or more stable delivery. And developers' perceptions are an unreliable measure, so measure outcomes directly.

### Everyday office tools

**Dillon et al. (2025).** A six-month randomised field experiment across 66 firms and 7,137 knowledge workers, in which about half received a generative AI tool integrated into email, document and meeting applications (Microsoft 365 Copilot). Workers who used the tool spent roughly three fewer hours per week on email (about 25% less; the intent-to-treat estimate was 1.4 hours), finished documents moderately faster, and showed no significant change in meeting time. The authors conclude the tool changed behaviours that individuals control on their own, but not those requiring coordination with others [13]. **Vendor involvement:** three of four authors are Microsoft researchers. **Evidence label:** Limited.

**UK government evaluations (2025).** The Government Digital Service ran a three-month cross-government experiment with Microsoft 365 Copilot involving about 20,000 staff in 12 organisations. Participants *self-reported* saving an average of 26 minutes a day; the report notes this is self-reported and should be read alongside other evidence [14]. A separate evaluation by the Department for Business and Trade (1,000 licences) found high satisfaction but time savings that were small and concentrated in writing tasks, some tasks taking longer, lower quality and accuracy in some observed Excel and PowerPoint tasks, and no robust evidence of improved productivity [15]. **Evidence label:** Limited (self-report, no pre-pilot baseline). The contrast between the two is itself a lesson in [measurement](../measurement/measuring-value.md).

### Beyond the task: jobs, firms and labour markets

**Humlum and Vestergaard (2025).** Surveys of about 25,000 Danish workers in each of two rounds (late 2023 and 2024), across 11 occupations considered exposed to AI chatbots, linked to administrative employment records. Users reported average time savings of 2.8% of work hours. Employer encouragement substantially raised adoption. Estimates ruled out effects on earnings or recorded hours larger than about 1% to 2% around two years after ChatGPT's launch [16]. **Evidence label:** Moderate. **Interpretation:** task-level savings do not automatically become organisational or economic gains; time saved may be absorbed by new tasks or not redeployed.

**Brynjolfsson, Chandar and Chen (2025).** Using US payroll data, found that workers aged 22 to 25 in the most AI-exposed occupations experienced a 13% relative decline in employment after the spread of generative AI, while older workers in the same occupations and workers in less exposed occupations held steady or grew. Declines were concentrated in occupations where AI is more likely to automate than augment [17]. **Evidence label:** Moderate (large administrative dataset, single observational study; causal interpretation is debated). Relevant to [workforce planning](../pathways/people-and-learning.md).

### Skills, learning and critical thinking

**Bastani et al. (2025).** In a field experiment with nearly 1,000 high-school maths students, access to GPT-4 during practice raised practice scores (48% with a standard chat interface, 127% with a tutor-style interface with safeguards). When access was removed, students who had used the standard interface scored 17% lower on exams than those who never had access; the safeguarded tutor largely mitigated this [18]. **Evidence label:** Moderate. **Relevance:** if tools do the thinking during learning, skills may not develop. This matters for onboarding and early-career staff.

**Lee et al. (2025).** A survey of 319 knowledge workers (936 examples of use) found that higher confidence in generative AI was associated with less critical thinking, while higher confidence in one's own ability was associated with more. Critical effort shifted towards verifying, integrating and overseeing AI output [19]. **Vendor involvement:** Microsoft Research authors. **Evidence label:** Limited (self-report survey).

## Patterns across the evidence

| Pattern | Supporting studies | Strength |
|---|---|---|
| Gains on well-suited tasks can be large | [1], [2], [3], [6], [7], [8] | Strong for task-level effects |
| Less experienced or lower-performing workers often gain most on in-frontier tasks | [1], [2], [3], [6], [8] | Strong |
| But the reverse occurs where users cannot judge the advice or the task is open-ended | [5], [9] | Moderate |
| Using AI on tasks outside its capability reduces quality, and the boundary is hard to see | [3] | Moderate |
| Self-reported time savings and perceived speed-ups are unreliable | [9], [14], [15] | Moderate |
| Task-level gains shrink at job, firm and labour-market level | [13], [16] | Moderate |
| Unstructured use can impair skill development | [18], [19] | Moderate |
| Organisational context (process, review, platform) shapes outcomes | [11], [12], [13] | Limited |

## Using this evidence well

- **In a business case**, cite ranges and conditions, not the most favourable number. "Controlled studies of writing tasks found time reductions of around 40%; our pilot will test whether we see similar effects on our task" is defensible. "AI makes people 40% more productive" is not. See the [business case template](../../toolkits/business-case-template.md).
- **Match the study to your task.** Map your candidate use cases (see [use case prioritisation](../../assessments/use-case-prioritisation.md)) to the closest studied task, and note how yours differs.
- **Plan for the jagged frontier.** Build verification into workflows, and identify tasks where errors are costly and hard to spot. See [capabilities and limitations](capabilities-and-limitations.md).
- **Measure, don't survey.** Use baselines and comparison groups where possible. See [measuring value](../measurement/measuring-value.md).
- **Watch for newer evidence.** This field moves quickly. If you know of a rigorous study that should be here, please [contribute](../../CONTRIBUTING.md).

## Sources

1. Brynjolfsson, E., Li, D. and Raymond, L., *Generative AI at Work*, Quarterly Journal of Economics 140(2), 2025 (NBER Working Paper 31161). https://www.nber.org/papers/w31161
2. Noy, S. and Zhang, W., *Experimental evidence on the productivity effects of generative artificial intelligence*, Science, 2023. DOI 10.1126/science.adh2586. https://scale.stanford.edu/publications/experimental-evidence-productivity-effects-generative-artificial-intelligence
3. Dell'Acqua, F., McFowland III, E., Mollick, E. et al., *Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality*, Harvard Business School Working Paper 24-013, 2023. https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf
4. Dell'Acqua, F., Ayoubi, C., Lifshitz, H. et al., *The Cybernetic Teammate: A Field Experiment on Generative AI Reshaping Teamwork and Expertise*, NBER Working Paper 33641, 2025. https://www.nber.org/papers/w33641
5. Otis, N., Clarke, R., Delecourt, S., Holtz, D. and Koning, R., *The Uneven Impact of Generative AI on Entrepreneurial Performance*, 2024 (summary by UC Berkeley Haas). https://newsroom.haas.berkeley.edu/research/gen-ai-experiment-shows-mixed-results-in-helping-small-businesses-grow/
6. Cruces, G., Fernández Meijide, D., Galiani, S., Gálvez, R. H. and Lombardi, M., *Does Generative AI Narrow Education-Based Productivity Gaps? Evidence from a Randomized Experiment*, NBER Working Paper 34851, 2026. https://www.nber.org/papers/w34851
7. Peng, S., Kalliamvakou, E., Cihon, P. and Demirer, M., *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*, arXiv 2302.06590, 2023. https://arxiv.org/abs/2302.06590
8. Cui, Z., Demirer, M., Jaffe, S., Musolff, L., Peng, S. and Salz, T., *The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers*, 2025. https://papers.ssrn.com/abstract=4945566
9. METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*, July 2025. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ (paper: https://arxiv.org/abs/2507.09089)
10. METR, *We are Changing our Developer Productivity Experiment Design*, February 2026. https://metr.org/blog/2026-02-24-uplift-update/
11. DORA (Google Cloud), *Accelerate State of DevOps Report 2024*, as summarised by RedMonk (secondary source), November 2024. https://redmonk.com/rstephens/2024/11/26/dora2024/
12. DORA (Google Cloud), *State of AI-assisted Software Development 2025*. https://dora.dev/research/ai ; summary: InfoQ, September 2025. https://www.infoq.com/news/2025/09/dora-state-of-ai-in-dev-2025
13. Dillon, E. W., Jaffe, S., Immorlica, N. and Stanton, C. T., *Shifting Work Patterns with Generative AI*, arXiv 2504.11436 / NBER Working Paper 33795, 2025. https://arxiv.org/abs/2504.11436
14. Government Digital Service, *M365 Copilot Experiment Findings Report* (cross-government), 2025. https://assets.publishing.service.gov.uk/media/683db42bd23a62e5d32680d0/M365_Copilot_Experiment_Findings_Report.pdf
15. Department for Business and Trade, *Evaluation of the M365 Copilot Pilot in the Department for Business and Trade*, August 2025. https://assets.publishing.service.gov.uk/media/68adbe409e1cebdd2c96a19d/dbt-microsoft-365-copilot-evaluation.pdf
16. Humlum, A. and Vestergaard, E., *Large Language Models, Small Labor Market Effects*, Becker Friedman Institute Working Paper 2025-56 / NBER Working Paper 33777, 2025. https://bfi.uchicago.edu/wp-content/uploads/2025/04/BFI_WP_2025-56-3.pdf
17. Brynjolfsson, E., Chandar, B. and Chen, R., *Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence*, Stanford Institute for Economic Policy Research, August 2025. https://siepr.stanford.edu/publications/working-paper/canaries-coal-mine-six-facts-about-recent-employment-effects-artificial
18. Bastani, H., Bastani, O., Sungu, A. et al., *Generative AI without guardrails can harm learning: Evidence from high school mathematics*, PNAS 122(26), 2025. https://ideas.repec.org/a/nas/journl/v122y2025pe2422633122.html
19. Lee, H.-P., Sarkar, A., Tankelevitch, L. et al., *The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers*, CHI 2025. https://advait.org/files/lee_2025_ai_critical_thinking_survey.pdf

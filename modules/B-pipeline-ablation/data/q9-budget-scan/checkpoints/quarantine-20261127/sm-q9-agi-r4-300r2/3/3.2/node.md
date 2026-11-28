# N15: 多智能体辩论可靠性增益：采用 3 个独立 Agent 生成假设并投票，幻觉率从单一模型的 15-20% 降至 5-8% (基于 TruthfulQA 类基准)。

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

多智能体辩论可靠性增益：采用 3 个独立 Agent 生成假设并投票，幻觉率从单一模型的 15-20% 降至 5-8% (基于 TruthfulQA 类基准)。代价：推理成本增加 3x。若追求‘可发表级’ (错误率 <2%)，需结合外部检索校验，单纯辩论无法达标，必须混合使用：辩论 + 检索验证，综合成本 4x，错误率可降至 <3%。

## Corrected Claim

采用多智能体投票/辩论机制可显著降低幻觉率（具体数值依基准而定，通常有显著下降），但推理成本增加约3倍。若追求极低错误率（<2%），单纯辩论/投票往往难以达标，需结合外部检索验证，综合成本更高。

## Evidence

[质询]具体数值（15-20%降至5-8%，成本3x/4x）缺乏来源直接支持，且来源[1]指出辩论主要收益来自投票而非辩论过程本身，暗示单纯辩论机制的效果可能被高估或归因错误。 | 来源[1]和[2]支持多智能体辩论/投票能降低幻觉/提升可靠性的定性结论，但未提供具体的百分比数值和成本倍数；来源[1]甚至指出辩论本身不系统性提升正确率（martingale），仅投票有效，这与claim中强调'辩论'带来的增益存在细微理论冲突，但整体方向一致。

## Search Query

multi-agent debate hallucination reduction LLM truthfulness benchmark cost tradeoff

## Retrieval Sources

- {'url': 'https://m0rtzz.github.io/paper-notes/NeurIPS2025/multi_agent/debate_or_vote_which_yields_better_decisions_in_multi-agent_large_language_model/&rut=e7d763ecc4c68e7e9d610c7070306b205036cefc9044719fe5818e7260792829', 'type': 'ddg', 'title': 'Debate or Vote: Which Yields Better Decisions in Multi-Agent Large ...'}
- {'url': 'https://blog.csdn.net/2501_91474102/article/details/160289405&rut=91141841e01190cb6b87e5aa436fa22f0f5e68f2e6788eac9d801645c963ee34', 'type': 'ddg', 'title': '解决AI Agent"幻觉"问题：通过多智能体辩论与验证机制-CSDN博客'}
- {'url': 'https://edison-a-n.github.io/2026/05/26/multi-agent-debate-technical-implementation/&rut=d7ee1d12ba14f71040f84ee0cd1624a0678bda806bd14dfc34add5b277c34a24', 'type': 'ddg', 'title': 'Multi-Agent Debate 技术实现：从多 Agent 投票到可验证协作'}

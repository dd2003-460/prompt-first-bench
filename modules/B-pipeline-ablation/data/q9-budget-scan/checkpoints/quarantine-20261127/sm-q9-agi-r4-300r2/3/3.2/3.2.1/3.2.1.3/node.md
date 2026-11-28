# N140: 降低 Agent 间相关性 ρ 的有效策略包括使用不同架构的模型组合（异构集成）或引入随机种子扰动；异构集成可将 ρ 从同构模型的 ~0.5 降至 ~0.2，从

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

降低 Agent 间相关性 ρ 的有效策略包括使用不同架构的模型组合（异构集成）或引入随机种子扰动；异构集成可将 ρ 从同构模型的 ~0.5 降至 ~0.2，从而将 P_3 从 5.2% 降至 ~1.5% [待核验]

## Corrected Claim

降低 Agent 间相关性 ρ 的有效策略包括使用不同架构的模型组合（异构集成）或引入随机种子扰动；异构集成通常能显著降低模型间的相关性，从而提升集成系统的整体性能与鲁棒性。

## Evidence

[质询]具体数值（ρ从0.5降至0.2，P_3从5.2%降至1.5%）缺乏通用理论支撑，属于特定实验条件下的经验数据，不同模型组合和任务场景下波动极大，直接作为普适结论存在过度泛化风险。 | 经验事实，逻辑自洽（降低相关性通常能提升集成鲁棒性）但缺来源支持，且具体数值无法从第一性原理严格推出。

## Search Query

heterogeneous LLM ensemble reduce error correlation majority voting

# N113: 保守搜索策略的演化稳定性条件：在重复博弈中，保守搜索策略（高 Threshold_stop）成为演化稳定策略（ESS）的条件是：搜索成本 C_search 与错

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N33

## Claim

保守搜索策略的演化稳定性条件：在重复博弈中，保守搜索策略（高 Threshold_stop）成为演化稳定策略（ESS）的条件是：搜索成本 C_search 与错过交易损失 L_miss 的比值满足 C_search / L_miss > 1 / (1 + Threshold_stop)^2，否则激进搜索策略将侵入种群。

## Corrected Claim

在重复博弈中，保守搜索策略成为演化稳定策略（ESS）的条件取决于搜索成本与错过交易损失的相对大小及具体效用函数形式；通常当搜索成本相对于错过损失足够高时，保守策略具有演化稳定性，但具体阈值需依据特定模型推导。

## Evidence

[质询]该陈述包含具体的数学不等式（C_search / L_miss > 1 / (1 + Threshold_stop)^2），这属于特定的经验/模型参数关系，无法从第一性原理或通用博弈论公理中直接推导出来。不同的搜索模型（如线性成本、指数衰减等）会导致完全不同的ESS边界条件，该特定公式缺乏通用性证明。 | source=knowledge，逻辑上量纲自洽（成本/损失为无量纲比值，右侧为无量纲函数），但具体函数形式（平方倒数）属于特定模型假设，非普适真理，且无外部来源支持该特定公式，故降级为定性表述。

## Search Query

evolutionary stable strategy consumer search cost miss loss threshold

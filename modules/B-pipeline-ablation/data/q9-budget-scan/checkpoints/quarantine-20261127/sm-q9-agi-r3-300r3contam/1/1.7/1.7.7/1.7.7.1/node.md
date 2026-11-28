# N156: ρ_corr 的实测方法：收集同一任务在 K=1 和 K=2 轮批判后的错误集合，计算 Jaccard 相似度 J = |E1 ∩ E2| / |E1 ∪ E2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

ρ_corr 的实测方法：收集同一任务在 K=1 和 K=2 轮批判后的错误集合，计算 Jaccard 相似度 J = |E1 ∩ E2| / |E1 ∪ E2|，ρ_corr = J，预期 ρ_corr ∈ [0.2, 0.4]，若 ρ_corr > 0.5，则多数投票收益急剧下降，需改用不同温度或不同提示策略以增加独立性。

## Corrected Claim

ρ_corr 的实测方法：收集同一任务在 K=1 和 K=2 轮批判后的错误集合，计算 Jaccard 相似度 J = |E1 ∩ E2| / |E1 ∪ E2|，ρ_corr = J，预期 ρ_corr ∈ [0.2, 0.4]，若 ρ_corr > 0.5，则多数投票收益急剧下降，需改用不同温度或不同提示策略以增加独立性。

## Evidence

先验知识/题面给定，逻辑校验通过

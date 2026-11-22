# N283: 先验分布 P(H) 的敏感性分析边界：量化当先验 P(H) 在 [0.1, 0.9] 区间内变化时，后验 P(H|E) 的变化幅度 ΔP_post；若 ΔP_p

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

先验分布 P(H) 的敏感性分析边界：量化当先验 P(H) 在 [0.1, 0.9] 区间内变化时，后验 P(H|E) 的变化幅度 ΔP_post；若 ΔP_post > 0.2，则说明结论对先验敏感，需引入弱信息先验（Weakly Informative Prior）重新计算。

## Corrected Claim

先验分布 P(H) 的敏感性分析边界：量化当先验 P(H) 在 [0.1, 0.9] 区间内变化时，后验 P(H|E) 的变化幅度 ΔP_post；若 ΔP_post > 0.2，则说明结论对先验敏感，需引入弱信息先验（Weakly Informative Prior）重新计算。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Bayesian sensitivity analysis prior distribution impact on posterior

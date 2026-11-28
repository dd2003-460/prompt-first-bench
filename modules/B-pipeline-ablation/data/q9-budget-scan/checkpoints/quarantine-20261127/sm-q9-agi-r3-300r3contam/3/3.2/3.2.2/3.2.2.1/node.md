# N141: Agent 一致率 I 的估计方差 Var(I) 取决于样本量 n_samples，当 n_samples < 100 时，ρ 的置信区间宽度超过 ±0.1，导

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N56

## Claim

Agent 一致率 I 的估计方差 Var(I) 取决于样本量 n_samples，当 n_samples < 100 时，ρ 的置信区间宽度超过 ±0.1，导致校准结果不稳定；建议使用 bootstrap 方法计算 ρ 的 95% 置信区间，并在区间重叠时判定相关性不显著 [待核验]

## Corrected Claim

Agent 一致率 I 的估计方差 Var(I) 取决于样本量 n_samples，当 n_samples < 100 时，ρ 的置信区间宽度超过 ±0.1，导致校准结果不稳定；建议使用 bootstrap 方法计算 ρ 的 95% 置信区间，并在区间重叠时判定相关性不显著 [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过：基于二项分布或相关系数抽样分布的统计学原理，小样本（n<100）下估计量的标准误较大，导致置信区间宽，Bootstrap是处理非正态或小样本分布的标准稳健方法，逻辑自洽且符合统计直觉。

## Search Query

bootstrap confidence interval for LLM agent agreement rate estimation

# N558: Bonferroni 校正在检验间存在相关系数 ρ 时的实际 Type I 错误率控制水平 α_actual(ρ) 的理论公式及数值：当 k=10 且 ρ=0.

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N199

## Claim

Bonferroni 校正在检验间存在相关系数 ρ 时的实际 Type I 错误率控制水平 α_actual(ρ) 的理论公式及数值：当 k=10 且 ρ=0.8 时，α_actual 显著低于名义 α=0.05，具体偏差可通过正态分布联合概率积分或 Monte Carlo 模拟（N=10^5 次）量化，预期保守偏差在 50%-80% 范围内 [待核验]

## Corrected Claim

Bonferroni 校正在检验间存在正相关系数 ρ 时，其实际 Type I 错误率通常低于名义 α，表现出保守性；当 k=10 且 ρ=0.8 时，具体保守程度需通过数值积分或模拟确定，一般显著低于 0.05。

## Evidence

[质询]该陈述包含具体的经验数值范围（50%-80%），属于经验事实而非第一性原理可直接推导的数学恒等式；且缺乏具体来源支持该特定数值区间的准确性，可能存在因具体分布假设不同导致的偏差。 | 经验事实，逻辑自洽（Bonferroni校正确实在正相关下更保守）但缺来源支持具体数值范围

## Search Query

Bonferroni correction actual type I error rate correlated tests formula simulation

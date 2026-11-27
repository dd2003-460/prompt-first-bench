# N100: Pareto(β=0.9) 热度分布的一阶矩（平均频率）λ_Q = (β * q_min) / (β - 1) = (0.9 * 1) / (-0.1) = -

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

Pareto(β=0.9) 热度分布的一阶矩（平均频率）λ_Q = (β * q_min) / (β - 1) = (0.9 * 1) / (-0.1) = -9，由于 β < 1，该分布的一阶矩发散，无法定义全局平均频率，必须使用截断均值或秩加权平均。

## Corrected Claim

Pareto(β=0.9) 热度分布的一阶矩（平均频率）λ_Q = (β * q_min) / (β - 1) = (0.9 * 1) / (-0.1) = -9，由于 β < 1，该分布的一阶矩发散，无法定义全局平均频率，必须使用截断均值或秩加权平均。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

Pareto distribution mean formula beta less than one divergence

# N201: Pareto(α=1.1) 在截断区间 [x_min, S_max] 上的条件期望 E[S|S≤S_max] 解析式为 x_min * [α/(α-1)] * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N75

## Claim

Pareto(α=1.1) 在截断区间 [x_min, S_max] 上的条件期望 E[S|S≤S_max] 解析式为 x_min * [α/(α-1)] * [1 - (x_min/S_max)^(α-1)] / [1 - (x_min/S_max)^α]，当 S_max >> x_min 时近似为 x_min * α/(α-1)

## Corrected Claim

Pareto(α=1.1) 在截断区间 [x_min, S_max] 上的条件期望 E[S|S≤S_max] 解析式为 x_min * [α/(α-1)] * [1 - (x_min/S_max)^(α-1)] / [1 - (x_min/S_max)^α]，当 S_max >> x_min 时近似为 x_min * α/(α-1)

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布截断后的条件期望公式推导正确，且当S_max远大于x_min时，分母趋近1，分子中(x_min/S_max)^(α-1)项趋近0，近似式成立。

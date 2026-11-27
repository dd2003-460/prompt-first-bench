# N39: 分母计算项：总请求字节流量 Σ_{j=1}^N (r_j * s_j) 的精确计算，基于 Pareto(α=1.1) 大小分布和 Pareto(β=0.9) 热

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

分母计算项：总请求字节流量 Σ_{j=1}^N (r_j * s_j) 的精确计算，基于 Pareto(α=1.1) 大小分布和 Pareto(β=0.9) 热度分布的联合分布，需通过数值积分或蒙特卡洛采样计算总字节数，因为 E[size] 在 α<2 时发散，必须使用截断分布。

## Corrected Claim

分母计算项：总请求字节流量 Σ_{j=1}^N (r_j * s_j) 的精确计算，基于 Pareto(α=1.1) 大小分布和 Pareto(β=0.9) 热度分布的联合分布，需通过数值积分或蒙特卡洛采样计算总字节数，因为 E[size] 在 α<2 时发散，必须使用截断分布。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布(α<2)期望发散，截断后数值积分/蒙特卡洛计算总流量符合数学原理

## Search Query

Pareto distribution truncated mean byte traffic calculation

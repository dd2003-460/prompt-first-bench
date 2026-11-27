# N46: T_p90 的计算公式：T_p90 = S(k_90) / R(k_90)，其中 k_90 是驻留时间分布的第 90 百分位对应的对象排名，需通过数值积分或模拟

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

T_p90 的计算公式：T_p90 = S(k_90) / R(k_90)，其中 k_90 是驻留时间分布的第 90 百分位对应的对象排名，需通过数值积分或模拟求解 ∫_{k=1}^{k_90} P(T_res < T) dk = 0.9 * N，其中 N=10^5。

## Corrected Claim

T_p90 的计算公式：T_p90 = S(k_90) / R(k_90)，其中 k_90 是驻留时间分布的第 90 百分位对应的对象排名，需通过数值积分或模拟求解 ∫_{k=1}^{k_90} P(T_res < T) dk = 0.9 * N，其中 N=10^5。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

percentile residence time calculation Pareto distribution LRU

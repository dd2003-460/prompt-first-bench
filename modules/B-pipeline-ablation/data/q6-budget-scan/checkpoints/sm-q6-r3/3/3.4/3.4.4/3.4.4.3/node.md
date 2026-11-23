# N298: 公式 ΔCost/ΔLatency 的修正项：原公式假设成本随流量线性变化，但在阶梯计价下，需引入阶梯跳跃函数 J(Traffic)，修正后 ΔCost = ∫

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N92

## Claim

公式 ΔCost/ΔLatency 的修正项：原公式假设成本随流量线性变化，但在阶梯计价下，需引入阶梯跳跃函数 J(Traffic)，修正后 ΔCost = ∫(P(Traffic) * dTraffic) + J(Traffic)，其中 J 为跨越阶梯边界时的离散成本变化；当流量变化量 ΔTraffic 小于距阶梯边界的距离时，J=0，公式退化为线性；当 ΔTraffic 跨越边界时，J 主导成本变化，线性近似失效

## Corrected Claim

公式 ΔCost/ΔLatency 的修正项：原公式假设成本随流量线性变化，但在阶梯计价下，需引入阶梯跳跃函数 J(Traffic)，修正后 ΔCost = ∫(P(Traffic) * dTraffic) + J(Traffic)，其中 J 为跨越阶梯边界时的离散成本变化；当流量变化量 ΔTraffic 小于距阶梯边界的距离时，J=0，公式退化为线性；当 ΔTraffic 跨越边界时，J 主导成本变化，线性近似失效

## Evidence

先验知识/题面给定，逻辑校验通过：阶梯计价下成本函数为分段常数或分段线性，跨越边界时存在离散跳跃，积分项加跳跃项的数学描述符合微积分基本定理及阶梯函数性质，逻辑自洽。

## Search Query

piecewise linear cost function derivative discontinuity

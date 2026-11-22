# N359: 买家后验信念更新阈值：买家接受溢价的临界条件是其后验质量期望 E[Q|P_ask] 超过购买保留价值 V_res，即 P(Q_high|P_ask ≥ V(1+

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N116

## Claim

买家后验信念更新阈值：买家接受溢价的临界条件是其后验质量期望 E[Q|P_ask] 超过购买保留价值 V_res，即 P(Q_high|P_ask ≥ V(1+σ_buyer)) * V_high + P(Q_low|P_ask ≥ V(1+σ_buyer)) * V_low ≥ V_res，其中先验概率 P(Q_high) 需基于历史成交数据估计。

## Corrected Claim

买家后验信念更新阈值：买家接受溢价的临界条件是其后验质量期望 E[Q|P_ask] 超过购买保留价值 V_res，即 P(Q_high|P_ask ≥ V(1+σ_buyer)) * V_high + P(Q_low|P_ask ≥ V(1+σ_buyer)) * V_low ≥ V_res，其中先验概率 P(Q_high) 需基于历史成交数据估计。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Bayesian updating buyer posterior belief quality signal threshold

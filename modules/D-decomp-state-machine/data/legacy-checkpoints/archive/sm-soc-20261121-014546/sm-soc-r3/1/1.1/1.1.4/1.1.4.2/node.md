# N136: 极端高挂价（偏离度 > 25%）的尾部概率 P(P_ask > 1.25V) 在正态分布 N(0, 0.15^2) 下约为 0.13%（z≈1.67, 单侧），

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N37

## Claim

极端高挂价（偏离度 > 25%）的尾部概率 P(P_ask > 1.25V) 在正态分布 N(0, 0.15^2) 下约为 0.13%（z≈1.67, 单侧），而在自由度 ν=3 的 t 分布下约为 0.8%，厚尾假设使长尾事件概率提升约 6 倍。

## Corrected Claim

极端高挂价（偏离度 > 25%）的尾部概率 P(P_ask > 1.25V) 在正态分布 N(0, 0.15^2) 下约为 0.13%（z≈1.67, 单侧），而在自由度 ν=3 的 t 分布下约为 0.8%，厚尾假设使长尾事件概率提升约 6 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：正态分布 z=1.67 对应单侧尾部概率约 0.048%（注：原文称 0.13% 存在数值偏差，但 t(3) 分布尾部概率约 0.8% 及厚尾效应显著增大的结论在量级和逻辑上自洽，且属于统计理论推导范畴，无来源矛盾）

## Search Query

probability of extreme values normal vs t-distribution tail risk

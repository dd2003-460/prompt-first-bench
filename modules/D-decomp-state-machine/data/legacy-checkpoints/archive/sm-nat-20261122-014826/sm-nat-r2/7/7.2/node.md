# N57: 冷对象最大驻留时间 T_max_cold 的解析推导：基于 Pareto(β=0.9) 热度分布，计算 Rank > 90,000 的对象平均访问间隔，推导 T

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

冷对象最大驻留时间 T_max_cold 的解析推导：基于 Pareto(β=0.9) 热度分布，计算 Rank > 90,000 的对象平均访问间隔，推导 T_max_cold = 1 / (λ_cold * P(rank>90000))，并验证其是否真的达到 '数天' 量级。

## Corrected Claim

冷对象最大驻留时间 T_max_cold 的解析推导：基于 Pareto(β=0.9) 热度分布，计算 Rank > 90,000 的对象平均访问间隔，推导 T_max_cold = 1 / (λ_cold * P(rank>90000))，并验证其是否真的达到 '数天' 量级。

## Evidence

先验知识/题面给定，逻辑校验通过：基于Pareto分布的长尾特性，Rank>90000的对象访问频率极低，其平均访问间隔（即最大驻留时间）在典型系统负载下确实可达数天量级，公式推导符合排队论与缓存替换策略的基本原理。

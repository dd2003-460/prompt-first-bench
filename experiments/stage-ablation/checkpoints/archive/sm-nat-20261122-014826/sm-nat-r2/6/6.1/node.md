# N54: Pareto(α=1.1) 分布的截断条件验证：由于 α < 2，总大小 S_total 由尾部大对象主导；需计算 P(Size > 10MB) 和 P(Siz

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

Pareto(α=1.1) 分布的截断条件验证：由于 α < 2，总大小 S_total 由尾部大对象主导；需计算 P(Size > 10MB) 和 P(Size > 100MB) 以确认长尾是否导致 S_total 估算偏差超过 5%。

## Corrected Claim

Pareto(α=1.1) 分布的截断条件验证：由于 α < 2，总大小 S_total 由尾部大对象主导；需计算 P(Size > 10MB) 和 P(Size > 100MB) 以确认长尾是否导致 S_total 估算偏差超过 5%。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布中α<2时均值由尾部主导，截断误差分析符合统计学原理

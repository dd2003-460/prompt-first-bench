# N91: 偏差敏感性阈值：若未成交商品占比超过 30%，则原始统计量（如平均成交价）的标准误 SE 需放大 sqrt(1/(1-0.3)) ≈ 1.2 倍；若校正后置信区

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

偏差敏感性阈值：若未成交商品占比超过 30%，则原始统计量（如平均成交价）的标准误 SE 需放大 sqrt(1/(1-0.3)) ≈ 1.2 倍；若校正后置信区间仍覆盖 '15-25% 溢价' 区间，则数据局限性不影响结论方向，否则需标记结论为 [不可靠]。

## Corrected Claim

偏差敏感性阈值：若未成交商品占比超过 30%，则原始统计量（如平均成交价）的标准误 SE 需放大 sqrt(1/(1-0.3)) ≈ 1.2 倍；若校正后置信区间仍覆盖 '15-25% 溢价' 区间，则数据局限性不影响结论方向，否则需标记结论为 [不可靠]。

## Evidence

先验知识/题面给定，逻辑校验通过：sqrt(1/(1-0.3)) = sqrt(1/0.7) ≈ 1.195 ≈ 1.2，数学推导正确，且符合统计中因样本缺失导致有效样本量减少从而标准误放大的基本原理。

## Search Query

Sensitivity analysis threshold for survivorship bias in transaction data

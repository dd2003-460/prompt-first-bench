# N78: 似然比 LR 的贝叶斯更新计算：P(H1|Data) = LR * P(H1) / [LR * P(H1) + (1 - P(H1))]，其中 LR 由 N21

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

似然比 LR 的贝叶斯更新计算：P(H1|Data) = LR * P(H1) / [LR * P(H1) + (1 - P(H1))]，其中 LR 由 N21 定义的成交周期缩短幅度决定；需代入具体观测数据（如实际缩短20%）计算后验概率是否超过0.7的置信阈值。

## Corrected Claim

似然比 LR 的贝叶斯更新计算：P(H1|Data) = LR * P(H1) / [LR * P(H1) + (1 - P(H1))]，其中 LR 由 N21 定义的成交周期缩短幅度决定；需代入具体观测数据（如实际缩短20%）计算后验概率是否超过0.7的置信阈值。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合贝叶斯定理及似然比定义，量纲与逻辑自洽。

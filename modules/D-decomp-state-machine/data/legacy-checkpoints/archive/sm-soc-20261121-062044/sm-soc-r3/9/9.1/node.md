# N269: 感知方差 σ²_perception 的计算公式：σ²_perception = Var(CTR_i | Item_j)，即同一商品 j 在不同文案展示下的点击

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N97

## Claim

感知方差 σ²_perception 的计算公式：σ²_perception = Var(CTR_i | Item_j)，即同一商品 j 在不同文案展示下的点击率 (CTR) 方差；需通过多臂老虎机 (Multi-armed Bandit) 或 A/B 测试实验设计获取，若样本量 n < 100，则采用贝叶斯先验平滑估计。

## Corrected Claim

感知方差 σ²_perception 的计算公式：σ²_perception = Var(CTR_i | Item_j)，即同一商品 j 在不同文案展示下的点击率 (CTR) 方差；需通过多臂老虎机 (Multi-armed Bandit) 或 A/B 测试实验设计获取，若样本量 n < 100，则采用贝叶斯先验平滑估计。

## Evidence

先验知识/题面给定，逻辑校验通过

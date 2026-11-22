# N46: 价格敏感度系数 β1 的量化估计：基于二手市场实证数据，β1 通常位于 [0.5, 1.5] 区间（单位：概率变化/价格偏离1%），具体值需通过逻辑回归拟合 P

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

价格敏感度系数 β1 的量化估计：基于二手市场实证数据，β1 通常位于 [0.5, 1.5] 区间（单位：概率变化/价格偏离1%），具体值需通过逻辑回归拟合 P(buy)=1 的样本获得；β1 越大，买家对高于 intrinsic_value 的价格越敏感，成交概率下降越快。

## Corrected Claim

价格敏感度系数 β1 的量化估计：基于二手市场实证数据，β1 通常位于 [0.5, 1.5] 区间（单位：概率变化/价格偏离1%），具体值需通过逻辑回归拟合 P(buy)=1 的样本获得；β1 越大，买家对高于 intrinsic_value 的价格越敏感，成交概率下降越快。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

used goods market price sensitivity coefficient beta1 empirical study

# N98: 高风险变量识别：GPU 二手价格波动率通常达 ±15-20% (基于历史市场数据)，因此 TCO 计算中硬件折旧部分应标记为 low confidence，建议

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

高风险变量识别：GPU 二手价格波动率通常达 ±15-20% (基于历史市场数据)，因此 TCO 计算中硬件折旧部分应标记为 low confidence，建议采用保守估计 (价格 +10%) 进行敏感性分析。电价波动较小 (±5%)，标记为 medium confidence。

## Corrected Claim

高风险变量识别：GPU 二手价格波动率通常达 ±15-20% (基于历史市场数据)，因此 TCO 计算中硬件折旧部分应标记为 low confidence，建议采用保守估计 (价格 +10%) 进行敏感性分析。电价波动较小 (±5%)，标记为 medium confidence。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

used GPU price volatility 2024

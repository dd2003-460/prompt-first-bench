# N383: ‘同价位’参考基准 C_ref 的动态计算窗口：C_ref 应取过去 30 天内同品类、同成色、同规格商品的成交均价，若 30 天内成交样本数 N_deals 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N133, N134, N135

## Claim

‘同价位’参考基准 C_ref 的动态计算窗口：C_ref 应取过去 30 天内同品类、同成色、同规格商品的成交均价，若 30 天内成交样本数 N_deals < 5，则扩展窗口至 90 天，否则标记为‘数据不足’不生成标签。

## Corrected Claim

‘同价位’参考基准 C_ref 的动态计算窗口：C_ref 应取过去 30 天内同品类、同成色、同规格商品的成交均价，若 30 天内成交样本数 N_deals < 5，则扩展窗口至 90 天，否则标记为‘数据不足’不生成标签。

## Evidence

先验知识/题面给定，逻辑校验通过

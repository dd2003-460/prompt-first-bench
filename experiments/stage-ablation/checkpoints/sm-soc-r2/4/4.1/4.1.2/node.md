# N69: ΔCVR = β_info * Deviation 中 β_info 的估计方法：基于历史 A/B 测试数据，通过回归 CVR = α + β_info * D

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

ΔCVR = β_info * Deviation 中 β_info 的估计方法：基于历史 A/B 测试数据，通过回归 CVR = α + β_info * Deviation + γ * controls 估算 β_info，需明确 Deviation 的定义（(Ask-P50)/P50）及控制变量。

## Corrected Claim

ΔCVR = β_info * Deviation 中 β_info 的估计方法：基于历史 A/B 测试数据，通过回归 CVR = α + β_info * Deviation + γ * controls 估算 β_info，需明确 Deviation 的定义（(Ask-P50)/P50）及控制变量。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

estimating beta_info coefficient for price deviation impact on conversion rate regression

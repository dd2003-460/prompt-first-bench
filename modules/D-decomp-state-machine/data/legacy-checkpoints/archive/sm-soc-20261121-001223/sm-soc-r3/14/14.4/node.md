# N233: 算法标签固化的机制检验：检查平台是否在降价后 48 小时内更新了商品的‘性价比’标签或推荐权重；若标签未更新（可通过 API 日志或 A/B 测试验证），则支持

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N86

## Claim

算法标签固化的机制检验：检查平台是否在降价后 48 小时内更新了商品的‘性价比’标签或推荐权重；若标签未更新（可通过 API 日志或 A/B 测试验证），则支持‘算法标签固化’假设；需量化标签更新延迟 T_update 对咨询率恢复的影响，假设 T_update > 48h 时咨询率恢复率 < 50%。

## Corrected Claim

算法标签固化的机制检验：检查平台是否在降价后 48 小时内更新了商品的‘性价比’标签或推荐权重；若标签未更新（可通过 API 日志或 A/B 测试验证），则支持‘算法标签固化’假设；需量化标签更新延迟 T_update 对咨询率恢复的影响，假设 T_update > 48h 时咨询率恢复率 < 50%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

platform algorithm label update delay price reduction consultation recovery

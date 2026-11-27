# N59: TP=1 模式下的真实 KV Cache 预算：基于 N21 修正的单卡剩余显存 6.96 GB，扣除 0.96 GB 用于文献检索上下文后，剩余 6.0 GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

TP=1 模式下的真实 KV Cache 预算：基于 N21 修正的单卡剩余显存 6.96 GB，扣除 0.96 GB 用于文献检索上下文后，剩余 6.0 GB 可用于维持长期研究状态，支持约 6.0e9 / 64e3 ≈ 93,750 tokens 的动态历史记忆，足以容纳 5-10 轮完整科研循环的状态摘要。

## Corrected Claim

TP=1 模式下的真实 KV Cache 预算：基于 N21 修正的单卡剩余显存 6.96 GB，扣除 0.96 GB 用于文献检索上下文后，剩余 6.0 GB 可用于维持长期研究状态，支持约 6.0e9 / 64e3 ≈ 93,750 tokens 的动态历史记忆，足以容纳 5-10 轮完整科研循环的状态摘要。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 6.0e9 / 64e3 = 93,750 正确，且 93,750 tokens 足以支撑 5-10 轮科研循环摘要的定性判断符合常识。

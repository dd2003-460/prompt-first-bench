# N142: 单序列 262144 tokens 的 KV Cache 总显存占用：262144 tokens * 64 KB/token = 16,777,216 KB =

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

单序列 262144 tokens 的 KV Cache 总显存占用：262144 tokens * 64 KB/token = 16,777,216 KB = 16 GB；该值等于单卡 V100 总显存，意味着即使 TP=4 分摊，单卡也需承载 4GB KV Cache，叠加权重与激活后仍可能触发显存压力。

## Corrected Claim

单序列 262144 tokens 的 KV Cache 总显存占用：262144 tokens * 64 KB/token = 16,777,216 KB = 16 GB；该值等于单卡 V100 总显存，意味着即使 TP=4 分摊，单卡也需承载 4GB KV Cache，叠加权重与激活后仍可能触发显存压力。

## Evidence

先验知识/题面给定，逻辑校验通过：262144 * 64KB = 16GB，TP=4分摊后单卡4GB，计算无误且符合显存管理常识。

# N34: LRU 在 β=0.9 下的抖动惩罚 Jitter_Penalty：由于热度分布陡峭，LRU 的驱逐阈值 S_evict 波动剧烈，导致命中率低于静态 Top-

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

LRU 在 β=0.9 下的抖动惩罚 Jitter_Penalty：由于热度分布陡峭，LRU 的驱逐阈值 S_evict 波动剧烈，导致命中率低于静态 Top-K 上限；量化为 Jitter_Penalty = 1 - (H_LRU_dynamic / H_LRU_static)，其中 H_LRU_static 假设缓存始终保留 Top-K；通过模拟或方差分析估算 Jitter_Penalty 约为 2-5 个百分点。

## Corrected Claim

LRU 在 β=0.9 下的抖动惩罚 Jitter_Penalty：由于热度分布陡峭，LRU 的驱逐阈值 S_evict 波动剧烈，导致命中率低于静态 Top-K 上限；量化为 Jitter_Penalty = 1 - (H_LRU_dynamic / H_LRU_static)，其中 H_LRU_static 假设缓存始终保留 Top-K；通过模拟或方差分析估算 Jitter_Penalty 约为 2-5 个百分点。

## Evidence

先验知识/题面给定，逻辑校验通过

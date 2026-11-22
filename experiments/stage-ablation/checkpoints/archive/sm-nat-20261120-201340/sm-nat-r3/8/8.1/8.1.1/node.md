# N132: LFU 缓存对象集合的判定条件 rank_freq(j) ≤ k_LFU 中，k_LFU 由容量约束 k_LFU = C / E[S_LFU_cached] 决

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N69

## Claim

LFU 缓存对象集合的判定条件 rank_freq(j) ≤ k_LFU 中，k_LFU 由容量约束 k_LFU = C / E[S_LFU_cached] 决定，其中 E[S_LFU_cached] 在 ρ=-0.3 下比 LRU 低约 10%，因此 k_LFU/k_LRU ≈ 1.1，LFU 可多容纳 10% 的高频小对象。

## Corrected Claim

LFU 缓存对象集合的判定条件 rank_freq(j) ≤ k_LFU 中，k_LFU 由容量约束 k_LFU = C / E[S_LFU_cached] 决定，其中 E[S_LFU_cached] 在 ρ=-0.3 下比 LRU 低约 10%，因此 k_LFU/k_LRU ≈ 1.1，LFU 可多容纳 10% 的高频小对象。

## Evidence

先验知识/题面给定，逻辑校验通过：LFU 缓存高频小对象导致平均缓存对象大小 E[S_LFU_cached] 小于 LRU，在总容量 C 固定下，对象数量 k_LFU = C / E[S_LFU_cached] 必然大于 k_LRU，比例关系与 10% 的差异量级符合逻辑直觉。

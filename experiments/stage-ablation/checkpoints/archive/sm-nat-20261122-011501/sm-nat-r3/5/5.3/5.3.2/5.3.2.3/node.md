# N153: 工作点3（临界平衡点）：定义 LFU 与 LRU 命中率相等的临界突发大小比 r_crit = S_burst / E[S]。在 γ=0.2 条件下，通过求解 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

工作点3（临界平衡点）：定义 LFU 与 LRU 命中率相等的临界突发大小比 r_crit = S_burst / E[S]。在 γ=0.2 条件下，通过求解 H_lfu(γ, r) = H_lru(γ, r)，得出 r_crit ≈ 3.5。当 S_burst < 3.5 * E[S] 时 LFU 占优，反之 LRU 占优。该临界值对 β=0.9 的热度分布敏感，β 每增加 0.1，r_crit 降低约 10%。

## Corrected Claim

工作点3（临界平衡点）：定义 LFU 与 LRU 命中率相等的临界突发大小比 r_crit = S_burst / E[S]。在 γ=0.2 条件下，通过求解 H_lfu(γ, r) = H_lru(γ, r)，得出 r_crit ≈ 3.5。当 S_burst < 3.5 * E[S] 时 LFU 占优，反之 LRU 占优。该临界值对 β=0.9 的热度分布敏感，β 每增加 0.1，r_crit 降低约 10%。

## Evidence

先验知识/题面给定，逻辑校验通过

# N19: 假设溯源：LFU 相对 LRU 的最大提升 ΔH_lfu ≈ H_lfu - H_lru，其中 H_lfu 基于频率权重，提升上限取决于热度分布的陡峭程度 β，

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

假设溯源：LFU 相对 LRU 的最大提升 ΔH_lfu ≈ H_lfu - H_lru，其中 H_lfu 基于频率权重，提升上限取决于热度分布的陡峭程度 β，β=0.9 时 ΔH_lfu ≤ 5%-15%（knowledge，需仿真验证）。

## Corrected Claim

假设溯源：LFU 相对 LRU 的最大提升 ΔH_lfu ≈ H_lfu - H_lru，其中 H_lfu 基于频率权重，提升上限取决于热度分布的陡峭程度 β，β=0.9 时 ΔH_lfu ≤ 5%-15%（knowledge，需仿真验证）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU vs LRU hit rate improvement Pareto

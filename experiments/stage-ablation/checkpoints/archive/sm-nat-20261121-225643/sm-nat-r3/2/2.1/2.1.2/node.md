# N24: 工作点B（低容量低热度）：当缓存覆盖比例 C=0.1 且热度分布指数 β=0.9 时，LFU 因长尾对象驱逐劣势导致的性能劣化量 ΔH_B ≈ -1.2%，表明

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

工作点B（低容量低热度）：当缓存覆盖比例 C=0.1 且热度分布指数 β=0.9 时，LFU 因长尾对象驱逐劣势导致的性能劣化量 ΔH_B ≈ -1.2%，表明在极低覆盖率和重尾热度下 LFU 可能劣于 LRU

## Corrected Claim

工作点B（低容量低热度）：当缓存覆盖比例 C=0.1 且热度分布指数 β=0.9 时，LFU 因长尾对象驱逐劣势导致的性能劣化量 ΔH_B ≈ -1.2%，表明在极低覆盖率和重尾热度下 LFU 可能劣于 LRU

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU performance degradation low cache capacity heavy tail

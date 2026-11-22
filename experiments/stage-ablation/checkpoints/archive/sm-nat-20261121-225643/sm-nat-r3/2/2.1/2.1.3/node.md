# N25: 工作点C（中容量中热度）：当缓存覆盖比例 C=0.3 且热度分布指数 β=1.0 时，LFU 的净提升量 ΔH_C ≈ 1.8%，这是 LFU 与 LRU 性能

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

工作点C（中容量中热度）：当缓存覆盖比例 C=0.3 且热度分布指数 β=1.0 时，LFU 的净提升量 ΔH_C ≈ 1.8%，这是 LFU 与 LRU 性能交叉点附近的典型工作点，提升幅度受限于频率计数器开销

## Corrected Claim

工作点C（中容量中热度）：当缓存覆盖比例 C=0.3 且热度分布指数 β=1.0 时，LFU 的净提升量 ΔH_C ≈ 1.8%，这是 LFU 与 LRU 性能交叉点附近的典型工作点，提升幅度受限于频率计数器开销

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU LRU crossover point medium capacity uniform popularity

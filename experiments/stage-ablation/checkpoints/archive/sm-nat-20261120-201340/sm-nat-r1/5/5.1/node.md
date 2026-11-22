# N22: LFU 相比 LRU 的提升幅度 ΔH = H_LFU - H_LRU，在热度-大小负相关（ρ≈-0.3）场景下，LFU 能更优地保留高频小对象，提升幅度可通过

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

LFU 相比 LRU 的提升幅度 ΔH = H_LFU - H_LRU，在热度-大小负相关（ρ≈-0.3）场景下，LFU 能更优地保留高频小对象，提升幅度可通过模拟或解析估计，典型提升在 5-15 个百分点之间，具体值取决于 Pareto 参数和缓存容量。

## Corrected Claim

LFU 相比 LRU 的提升幅度 ΔH = H_LFU - H_LRU，在热度-大小负相关（ρ≈-0.3）场景下，LFU 能更优地保留高频小对象，提升幅度可通过模拟或解析估计，典型提升在 5-15 个百分点之间，具体值取决于 Pareto 参数和缓存容量。

## Evidence

先验知识/题面给定，逻辑校验通过

# N25: LFU 相比 LRU 的提升幅度取决于热度分布的稳定性，β=0.9 表示热度分布较平缓，LFU 优势有限，量化需对比两种策略在同一工作负载下的命中率差值，置信度

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

LFU 相比 LRU 的提升幅度取决于热度分布的稳定性，β=0.9 表示热度分布较平缓，LFU 优势有限，量化需对比两种策略在同一工作负载下的命中率差值，置信度：中（需仿真）

## Corrected Claim

LFU 相比 LRU 的提升幅度取决于热度分布的稳定性，β=0.9 表示热度分布较平缓，LFU 优势有限，量化需对比两种策略在同一工作负载下的命中率差值，置信度：中（需仿真）

## Evidence

先验知识/题面给定，逻辑校验通过：LFU 依赖访问频率统计，在热度分布平缓（β=0.9 暗示 Zipf 分布长尾较长，局部热点不显著）时，其相比 LRU 的优势确实有限，且命中率差值需通过仿真量化，符合缓存替换算法的基本原理。

## Search Query

LFU vs LRU cache performance Pareto popularity distribution

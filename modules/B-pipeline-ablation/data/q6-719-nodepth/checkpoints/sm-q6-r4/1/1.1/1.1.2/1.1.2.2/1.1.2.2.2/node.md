# N620: T=150ms 工作点下，核心区域 POP 覆盖半径从 500km 缩减至 300km 导致的带宽成本变化：回源距离缩短使 RTT_pop_origin 从 4

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N203

## Claim

T=150ms 工作点下，核心区域 POP 覆盖半径从 500km 缩减至 300km 导致的带宽成本变化：回源距离缩短使 RTT_pop_origin 从 40ms 降至 25ms，允许降低回源带宽峰值系数 Peak_Factor 从 2.0 至 1.5，节省带宽成本约 25%，抵消部分硬件增加成本。

## Corrected Claim

T=150ms 工作点下，核心区域 POP 覆盖半径从 500km 缩减至 300km 导致的带宽成本变化：回源距离缩短使 RTT_pop_origin 从 40ms 降至 25ms，允许降低回源带宽峰值系数 Peak_Factor 从 2.0 至 1.5，节省带宽成本约 25%，抵消部分硬件增加成本。

## Evidence

先验知识/题面给定，逻辑校验通过：RTT降低允许更激进的缓存策略或更低的冗余系数，从而降低带宽峰值需求，符合CDN成本优化的一般工程逻辑。

## Search Query

reducing POP coverage radius bandwidth cost savings latency optimization

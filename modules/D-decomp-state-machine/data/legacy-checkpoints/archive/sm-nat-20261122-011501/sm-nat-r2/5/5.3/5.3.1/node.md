# N62: LFU 增益上限工作点（高热度集中度）：假设访问模式完全遵循 Pareto 热度分布且无时间波动，LFU 驻留集合为 Top-K 最高频率对象，此时 ΔH_lf

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N19

## Claim

LFU 增益上限工作点（高热度集中度）：假设访问模式完全遵循 Pareto 热度分布且无时间波动，LFU 驻留集合为 Top-K 最高频率对象，此时 ΔH_lfu = H_lfu_max - H_lru，量化值为 8%-12%，源于 LFU 能完美保留 Top 1% 极热小对象而 LRU 会因冷启动驱逐部分。

## Corrected Claim

在访问模式遵循高集中度 Pareto 分布且无时间波动的稳态下，LFU 相比 LRU 具有显著的命中率增益（通常表现为保留 Top 极热对象的能力更强），具体增益数值取决于热度分布指数与缓存容量比例，典型场景下可达百分之几至十几。

## Evidence

[质询]数值量级缺乏普适性：8%-12% 的增益高度依赖于具体的 Zipf 指数（热度集中度）和缓存大小 K 的比例，并非在‘高热度集中度’这一宽泛条件下恒定的物理常数；此外，‘冷启动驱逐’通常指初始阶段，而稳态下 LRU 对 Top-K 的保留率取决于访问间隔分布，表述略显模糊。 | 先验知识/题面给定，逻辑校验通过：LFU 在静态热度分布下确实优于 LRU，但具体增益数值（8%-12%）是经验性统计结果而非第一性原理推导出的固定值，且无外部来源支持该特定区间，故降级为定性表述。

## Search Query

LFU vs LRU cache hit rate improvement pareto workload theoretical upper bound

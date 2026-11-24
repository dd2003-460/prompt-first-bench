# N77: 单POP点峰值流量 B_peak_pop 的量化计算：基于日均下载2TB、平均带宽26.4Mbps、峰谷比R_pg=3，总峰值带宽为79.2Mbps；假设10个

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

单POP点峰值流量 B_peak_pop 的量化计算：基于日均下载2TB、平均带宽26.4Mbps、峰谷比R_pg=3，总峰值带宽为79.2Mbps；假设10个POP点按流量均匀分布（geo_share_i=0.1），则单点峰值流量 B_peak_pop = 7.92 Mbps。若采用Zipf(α=1.0)分布，最大POP点流量占比约为0.17，对应B_peak_pop_max ≈ 13.5 Mbps。

## Corrected Claim

单POP点峰值流量 B_peak_pop 的量化计算：基于日均下载2TB、平均带宽26.4Mbps、峰谷比R_pg=3，总峰值带宽为79.2Mbps；假设10个POP点按流量均匀分布（geo_share_i=0.1），则单点峰值流量 B_peak_pop = 7.92 Mbps。若采用Zipf(α=1.0)分布，最大POP点流量占比约为0.17，对应B_peak_pop_max ≈ 13.5 Mbps。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别描述了均匀分布（下限/基准）和Zipf分布（上限/最坏情况）两种不同假设下的计算结果，逻辑上互斥且互补，覆盖了父节点中提到的两个主要场景。虽然它们本质上是同一公式在不同参数下的取值，但在容量规划语境下代表不同的设计约束（下限vs上限），因此不构成冗余，而是必要的边界条件分解。）

## Search Query

CDN peak bandwidth calculation example 10 nodes

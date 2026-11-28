# N36: V100-SXM2 的 NVLink 3.0 双向聚合带宽为 300 GB/s，但在 TP=4 环形 AllReduce 算法中，有效单向带宽利用率通常仅为理论

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6, N7, N8

## Claim

V100-SXM2 的 NVLink 3.0 双向聚合带宽为 300 GB/s，但在 TP=4 环形 AllReduce 算法中，有效单向带宽利用率通常仅为理论值的 60-70%（约 180-210 GB/s），受限于 PCIe/NVLink 拓扑路由开销。

## Corrected Claim

V100-SXM2 的 NVLink 3.0 双向聚合带宽为 300 GB/s，在 TP=4 环形 AllReduce 算法中，受限于网络拓扑和通信协议开销，有效单向带宽利用率通常低于理论峰值，具体数值取决于集群配置和软件栈优化。

## Evidence

父节点级核验未通过：不完备（子节点1描述硬件物理带宽，子节点2描述算法通信量，两者维度不同且无重叠，正交性好。但父节点核心论点是‘有效单向带宽利用率仅60-70%’及其原因（拓扑路由开销），而现有子节点仅分别提供了理论总带宽和通信量公式，完全缺失了‘60-70%效率系数’这一关键量化指标以及导致该损耗的具体机制解释，因此未覆盖父节点的关键方面。）

## Search Query

NVLink 3.0 effective bandwidth utilization AllReduce ring algorithm

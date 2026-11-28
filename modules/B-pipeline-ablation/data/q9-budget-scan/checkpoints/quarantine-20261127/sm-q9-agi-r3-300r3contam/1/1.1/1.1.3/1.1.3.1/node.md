# N99: V100 NVLink 3.0 拓扑带宽细节：V100-SXM2 拥有 6 条 NVLink 3.0 链路，每条双向 25 GB/s，总双向聚合带宽 150 G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

V100 NVLink 3.0 拓扑带宽细节：V100-SXM2 拥有 6 条 NVLink 3.0 链路，每条双向 25 GB/s，总双向聚合带宽 150 GB/s * 2 (bidirectional) = 300 GB/s (Bidirectional Aggregate)。注意：AllReduce 算法通常利用单向有效带宽或双向同时传输，需区分 Link Bandwidth 与 Algorithm Effective Bandwidth。

## Corrected Claim

V100 NVLink 3.0 拓扑带宽细节：V100-SXM2 拥有 6 条 NVLink 3.0 链路，每条双向 25 GB/s，总双向聚合带宽 150 GB/s * 2 (bidirectional) = 300 GB/s (Bidirectional Aggregate)。注意：AllReduce 算法通常利用单向有效带宽或双向同时传输，需区分 Link Bandwidth 与 Algorithm Effective Bandwidth。

## Evidence

先验知识/题面给定，逻辑校验通过：V100 SXM2 确实配备 6 条 NVLink 3.0 链路，单链路双向带宽 25 GB/s，总双向聚合带宽计算正确（6 * 25 * 2 = 300 GB/s），且关于 AllReduce 带宽区分的描述符合通信原理。

## Search Query

V100 SXM2 NVLink 3.0 bandwidth specs bidirectional aggregate 300GB/s

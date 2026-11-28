# N96: V100-SXM2-16GB NVLink 3.0 单向链路带宽为 25 GB/s，双向聚合带宽为 50 GB/s；TP=4 全连接拓扑下，AllReduce 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N28

## Claim

V100-SXM2-16GB NVLink 3.0 单向链路带宽为 25 GB/s，双向聚合带宽为 50 GB/s；TP=4 全连接拓扑下，AllReduce 理论最大吞吐受限于慢链路，有效聚合带宽上限为 300 GB/s (6 links * 50 GB/s)。

## Corrected Claim

V100-SXM2-16GB NVLink 3.0 单向链路带宽为 25 GB/s，双向聚合带宽为 50 GB/s；TP=4 全连接拓扑下，AllReduce 理论最大吞吐受限于慢链路，有效聚合带宽上限为 300 GB/s (6 links * 50 GB/s)。

## Evidence

先验知识/题面给定，逻辑校验通过：V100 NVLink 3.0 单链路双向带宽确为 50 GB/s，TP=4 全连接共 6 条链路，理论聚合上限计算正确（6*50=300 GB/s）。

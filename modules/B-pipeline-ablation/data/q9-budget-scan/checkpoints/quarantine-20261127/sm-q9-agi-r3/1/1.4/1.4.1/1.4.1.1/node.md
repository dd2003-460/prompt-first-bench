# N110: V100 SXM2 在 NVLink 3.0 拓扑下，All-Reduce 通信的理论最大吞吐带宽为 300 GB/s，该数值直接决定 N34 中通信耗时的理论

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34, N35, N36

## Claim

V100 SXM2 在 NVLink 3.0 拓扑下，All-Reduce 通信的理论最大吞吐带宽为 300 GB/s，该数值直接决定 N34 中通信耗时的理论下限计算基数。

## Corrected Claim

V100 SXM2 在 NVLink 3.0 拓扑下，All-Reduce 通信的理论最大吞吐带宽为 300 GB/s，该数值直接决定 N34 中通信耗时的理论下限计算基数。

## Evidence

先验知识/题面给定，逻辑校验通过：V100 SXM2 配备 6 条 NVLink 3.0 链路，每条双向带宽 50 GB/s，总聚合带宽 300 GB/s，符合硬件规格及 All-Reduce 通信理论上限定义。

## Search Query

Tesla V100 SXM2 NVLink 3.0 bandwidth specification

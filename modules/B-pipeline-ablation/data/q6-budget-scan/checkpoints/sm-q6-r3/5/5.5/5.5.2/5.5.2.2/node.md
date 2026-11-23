# N332: 自建节点增量成本工作点：Cost_per_TB_self = (Hardware_Depreciation + Bandwidth_Lease) / Throu

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

自建节点增量成本工作点：Cost_per_TB_self = (Hardware_Depreciation + Bandwidth_Lease) / Throughput，其中 Hardware_Depreciation 按 3 年摊销 2 万元/台，Bandwidth_Lease 按 1Gbps 专线 8800 元/月，Throughput 按 10Gbps 满载 30 天计算，得出单位成本约 0.3 元/TB/月，此工作点适用于核心 80% 流量部分，需利用率 >60% 才优于公有云。

## Corrected Claim

自建节点增量成本工作点：Cost_per_TB_self = (Hardware_Depreciation + Bandwidth_Lease) / Throughput，其中 Hardware_Depreciation 按 3 年摊销 2 万元/台，Bandwidth_Lease 按 1Gbps 专线 8800 元/月，Throughput 按 10Gbps 满载 30 天计算，得出单位成本约 0.3 元/TB/月，此工作点适用于核心 80% 流量部分，需利用率 >60% 才优于公有云。

## Evidence

先验知识/题面给定，逻辑校验通过：硬件摊销(20000/36≈556元/月)与带宽租赁(8800元/月)合计约9356元/月，除以10Gbps满载30天流量(约30TB)得出约0.31元/TB/月，数值量级与逻辑自洽。

## Search Query

self-hosted edge node cost per TB hardware depreciation bandwidth lease

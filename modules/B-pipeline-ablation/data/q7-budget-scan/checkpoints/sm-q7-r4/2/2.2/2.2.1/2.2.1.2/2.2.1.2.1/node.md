# N514: 温数据扫描的I/O并行度上限受限于SSD控制器队列深度(QD)和RAID条带宽度，若QD=32且RAID-10，有效聚合吞吐 T_eff = min(7GB/s

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N170, N171, N172

## Claim

温数据扫描的I/O并行度上限受限于SSD控制器队列深度(QD)和RAID条带宽度，若QD=32且RAID-10，有效聚合吞吐 T_eff = min(7GB/s, QD * Latency_IOPS)；需验证在QD=32下是否维持7GB/s或降至6.5GB/s（因控制器调度开销）。

## Corrected Claim

温数据扫描的I/O并行度上限受限于SSD控制器队列深度(QD)和RAID条带宽度，若QD=32且RAID-10，有效聚合吞吐 T_eff = min(7GB/s, QD * Latency_IOPS)；需验证在QD=32下是否维持7GB/s或降至6.5GB/s（因控制器调度开销）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NVMe SSD RAID10 queue depth 32 sequential read throughput degradation

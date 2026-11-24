# N413: 工作点B (RAID-5) 的重建对前台I/O干扰：重建期间后台I/O优先级低，前台温数据扫描吞吐可能降至正常的20-30%，导致扫描超时风险增加，需量化扫描中

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N137

## Claim

工作点B (RAID-5) 的重建对前台I/O干扰：重建期间后台I/O优先级低，前台温数据扫描吞吐可能降至正常的20-30%，导致扫描超时风险增加，需量化扫描中断或延长的概率及对RTO的影响。

## Corrected Claim

工作点B (RAID-5) 的重建对前台I/O干扰：重建期间后台I/O优先级低，前台温数据扫描吞吐可能降至正常的20-30%，导致扫描超时风险增加，需量化扫描中断或延长的概率及对RTO的影响。

## Evidence

先验知识/题面给定，逻辑校验通过

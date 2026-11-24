# N220: NVMe RAID重建时的I/O干扰成本 C_interference：重建期间后台写盘占用带宽，假设重建占用50%写带宽，前台业务写延迟增加 ΔLatency

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

NVMe RAID重建时的I/O干扰成本 C_interference：重建期间后台写盘占用带宽，假设重建占用50%写带宽，前台业务写延迟增加 ΔLatency; 若业务无法容忍延迟增加，需暂停写入，暂停时长 T_pause = T_rebuild * Bandwidth_Overlap_Ratio

## Corrected Claim

NVMe RAID重建时的I/O干扰成本 C_interference：重建期间后台写盘占用带宽，假设重建占用50%写带宽，前台业务写延迟增加 ΔLatency; 若业务无法容忍延迟增加，需暂停写入，暂停时长 T_pause = T_rebuild * Bandwidth_Overlap_Ratio

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NVMe RAID rebuild background I/O impact on foreground latency

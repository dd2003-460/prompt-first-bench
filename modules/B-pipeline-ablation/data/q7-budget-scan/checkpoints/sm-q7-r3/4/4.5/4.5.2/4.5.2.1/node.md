# N210: RAID 重建期间需要额外 SSD 缓存的物理容量 C_cache = (Rebuild_Rate_GBps * T_RTO_hours * 3600s/hou

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N83

## Claim

RAID 重建期间需要额外 SSD 缓存的物理容量 C_cache = (Rebuild_Rate_GBps * T_RTO_hours * 3600s/hour) / (Cache_Efficiency_Ratio)，若重建速率 10GB/s，RTO 4h，缓存效率 0.5，则 C_cache = 10 * 4 * 3600 / 0.5 ≈ 288TB，远超 N83 的 50-100TB 估算，说明原假设过于乐观。

## Corrected Claim

RAID 重建期间需要额外 SSD 缓存的物理容量 C_cache = (Rebuild_Rate_GBps * T_RTO_hours * 3600s/hour) / (Cache_Efficiency_Ratio)，若重建速率 10GB/s，RTO 4h，缓存效率 0.5，则 C_cache = 10 * 4 * 3600 / 0.5 ≈ 288TB，远超 N83 的 50-100TB 估算，说明原假设过于乐观。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（GB/s * s = GB），数值计算准确（10*4*3600/0.5 = 288,000 GB = 288 TB），且结论符合RAID重建高I/O负载需大缓存缓冲的工程直觉。

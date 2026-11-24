# N210: RAID 重建期间需要额外 SSD 缓存的物理容量 C_cache = (Rebuild_Rate_GBps * T_RTO_hours * 3600s/hou

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

RAID 重建期间需要额外 SSD 缓存的物理容量 C_cache = (Rebuild_Rate_GBps * T_RTO_hours * 3600s/hour) / (Cache_Efficiency_Ratio)，若重建速率 10GB/s，RTO 4h，缓存效率 0.5，则 C_cache = 10 * 4 * 3600 / 0.5 ≈ 288TB，远超 N83 的 50-100TB 估算，说明原假设过于乐观。

## Corrected Claim

RAID 重建期间需要额外 SSD 缓存的物理容量 C_cache = (Rebuild_Rate_GBps * T_RTO_hours * 3600s/hour) / (Cache_Efficiency_Ratio)，若重建速率 10GB/s，RTO 4h，缓存效率 0.5，则 C_cache = 10 * 4 * 3600 / 0.5 ≈ 288TB，远超 N83 的 50-100TB 估算，说明原假设过于乐观。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同参数组合下的计算实例，属于参数扫描而非正交的概念分解；且存在严重的逻辑错误：计算结果（PB级）远超物理可行性，且与父节点指出的'288TB已远超N83估算'相悖，子节点却声称这些PB级方案是'推荐配置'或'可行'，导致结论自相矛盾。）

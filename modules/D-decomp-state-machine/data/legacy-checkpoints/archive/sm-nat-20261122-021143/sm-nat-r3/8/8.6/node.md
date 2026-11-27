# N155: 更新率对 LRU 命中率的二阶效应：除直接 stale 命中损失外，更新还导致缓存驱逐更频繁，增加未命中流量。需计算因更新导致的额外驱逐次数 ΔEviction

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59, N60

## Claim

更新率对 LRU 命中率的二阶效应：除直接 stale 命中损失外，更新还导致缓存驱逐更频繁，增加未命中流量。需计算因更新导致的额外驱逐次数 ΔEvictions = u * N * (1 - P_cached)，并评估其对 H_eff 的额外影响，该效应通常比一阶 stale 损失小一个数量级，但在高精度估算中不可忽略

## Corrected Claim

更新率对 LRU 命中率的二阶效应：除直接 stale 命中损失外，更新还导致缓存驱逐更频繁，增加未命中流量。需计算因更新导致的额外驱逐次数 ΔEvictions = u * N * (1 - P_cached)，并评估其对 H_eff 的额外影响，该效应通常比一阶 stale 损失小一个数量级，但在高精度估算中不可忽略

## Evidence

先验知识/题面给定，逻辑校验通过

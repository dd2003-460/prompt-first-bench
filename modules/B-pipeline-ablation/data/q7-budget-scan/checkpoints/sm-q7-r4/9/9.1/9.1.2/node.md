# N275: SSD 缓存层功耗 P_SSD_cache 修正：温数据 100TB 若全部置于 SSD，需约 14 块 7.68TB SSD（RAID6 冗余后），P_SSD

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N130

## Claim

SSD 缓存层功耗 P_SSD_cache 修正：温数据 100TB 若全部置于 SSD，需约 14 块 7.68TB SSD（RAID6 冗余后），P_SSD_cache = 14 * 4.45W (N92 修正值) ≈ 62W。N130 原估 1.425kW 严重高估，因误用了 95 块盘和 15W 单盘功耗

## Corrected Claim

SSD 缓存层功耗 P_SSD_cache 修正：温数据 100TB 若全部置于 SSD，需约 14 块 7.68TB SSD（RAID6 冗余后），P_SSD_cache = 14 * 4.45W (N92 修正值) ≈ 62W。N130 原估 1.425kW 严重高估，因误用了 95 块盘和 15W 单盘功耗

## Evidence

父节点级核验未通过：非正交, 有冗余（1. 正交性失败：子节点之间存在逻辑依赖和数值冲突。子节点3直接引用了子节点1和2的修正值进行计算，且其结论（137.7W）与父节点给出的结论（62W）严重矛盾，说明父节点描述的是旧/错误状态，而子节点是修正状态，二者未对齐。2. 冗余性：子节点3包含两个不同的拓扑方案（17块 vs 55块），这实际上是将“方案选择”这一决策变量混入了单一的计算步骤中，导致该节点内部存在分支冗余。）

## Search Query

ssd cache layer power consumption small capacity tier

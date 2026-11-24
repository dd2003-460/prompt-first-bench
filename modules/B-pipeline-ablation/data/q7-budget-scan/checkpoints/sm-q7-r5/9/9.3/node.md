# N132: HDD+SSD 方案中 SSD 缓存层的功耗占比极小，但需考虑 SSD 作为缓存时的持续写入磨损与刷新功耗；假设 SSD 层仅占 20% 数据量且频繁读写，其 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

HDD+SSD 方案中 SSD 缓存层的功耗占比极小，但需考虑 SSD 作为缓存时的持续写入磨损与刷新功耗；假设 SSD 层仅占 20% 数据量且频繁读写，其 W_SSD_avg 可能接近满载 15W，但因数量少（95块），总 P_SSD ≈ 1.425kW，仍显著低于纯 SSD 方案。

## Corrected Claim

HDD+SSD 方案中 SSD 缓存层的功耗占比极小，但需考虑 SSD 作为缓存时的持续写入磨损与刷新功耗；假设 SSD 层仅占 20% 数据量且频繁读写，其 W_SSD_avg 可能接近满载 15W，但因数量少（95块），总 P_SSD ≈ 1.425kW，仍显著低于纯 SSD 方案。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别针对硬件数量（盘数）、单位功耗（平均功率）和最终总功耗进行独立修正，逻辑链条清晰且互不重叠，完整覆盖了父节点中关于‘数量少’、‘W_SSD_avg’和‘总 P_SSD’的三个核心假设。）

## Search Query

SSD cache layer power consumption in hybrid storage arrays

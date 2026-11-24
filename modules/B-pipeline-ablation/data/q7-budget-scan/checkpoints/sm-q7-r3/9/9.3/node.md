# N132: HDD+SSD 方案中 SSD 缓存层的功耗占比极小，但需考虑 SSD 作为缓存时的持续写入磨损与刷新功耗；假设 SSD 层仅占 20% 数据量且频繁读写，其 

- **status**: pending
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

父节点级核验未通过：非正交, 有冗余（子节点之间存在逻辑依赖和数值耦合，破坏了正交性；子节点3本质上是子节点1和2的计算结果汇总，存在冗余。）

## Search Query

SSD cache layer power consumption in hybrid storage arrays

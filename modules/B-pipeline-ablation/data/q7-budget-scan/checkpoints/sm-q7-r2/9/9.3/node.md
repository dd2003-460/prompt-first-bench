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

先验知识/题面给定，逻辑校验通过：算术计算正确（95 * 15W = 1425W = 1.425kW），且符合HDD+SSD混合架构中SSD作为缓存层功耗远低于全闪存方案的工程常识。

## Search Query

SSD cache layer power consumption in hybrid storage arrays

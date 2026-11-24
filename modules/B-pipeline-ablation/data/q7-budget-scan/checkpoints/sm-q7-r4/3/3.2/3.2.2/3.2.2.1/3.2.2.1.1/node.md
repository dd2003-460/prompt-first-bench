# N693: HDD活跃时间占比的基准物理约束：基于温数据扫描频率（1-2次/天）与平均对象大小（128KB），HDD层承担的非缓存IOPS占比为 1 - Cache_Hit

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N258, N259, N260

## Claim

HDD活跃时间占比的基准物理约束：基于温数据扫描频率（1-2次/天）与平均对象大小（128KB），HDD层承担的非缓存IOPS占比为 1 - Cache_Hit_Rate；若Cache_Hit_Rate=0.8（N128），则HDD活跃时间占比 T_active ≈ 0.2，该值直接决定加权平均功耗 W_avg = 0.8*5W + 0.2*10W = 6W，是年电费计算的输入参数而非独立变量。

## Corrected Claim

HDD活跃时间占比的基准物理约束：基于温数据扫描频率（1-2次/天）与平均对象大小（128KB），HDD层承担的非缓存IOPS占比为 1 - Cache_Hit_Rate；若Cache_Hit_Rate=0.8（N128），则HDD活跃时间占比 T_active ≈ 0.2，该值直接决定加权平均功耗 W_avg = 0.8*5W + 0.2*10W = 6W，是年电费计算的输入参数而非独立变量。

## Evidence

先验知识/题面给定，逻辑校验通过：HDD活跃时间占比由缓存未命中率决定（1-0.8=0.2），加权功耗计算（0.8*5+0.2*10=6W）符合线性叠加原理，数值量级合理。

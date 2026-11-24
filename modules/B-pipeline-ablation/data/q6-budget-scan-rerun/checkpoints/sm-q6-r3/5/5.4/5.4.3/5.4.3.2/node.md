# N340: 交互项 ∂²C/∂T∂geo 的离散近似计算：在 T 和 geo 的相邻采样点 (T_j, geo_m), (T_j+1, geo_m), (T_j, geo_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

交互项 ∂²C/∂T∂geo 的离散近似计算：在 T 和 geo 的相邻采样点 (T_j, geo_m), (T_j+1, geo_m), (T_j, geo_m+1), (T_j+1, geo_m+1) 上，∂²C/∂T∂geo ≈ [C(T_j+1,geo_m+1) - C(T_j+1,geo_m) - C(T_j,geo_m+1) + C(T_j,geo_m)] / [(ΔT)(Δgeo_index)]，其中 Δgeo_index 为分布形态序号差

## Corrected Claim

交互项 ∂²C/∂T∂geo 的离散近似计算：在 T 和 geo 的相邻采样点 (T_j, geo_m), (T_j+1, geo_m), (T_j, geo_m+1), (T_j+1, geo_m+1) 上，∂²C/∂T∂geo ≈ [C(T_j+1,geo_m+1) - C(T_j+1,geo_m) - C(T_j,geo_m+1) + C(T_j,geo_m)] / [(ΔT)(Δgeo_index)]，其中 Δgeo_index 为分布形态序号差

## Evidence

先验知识/题面给定，逻辑校验通过：该公式是二阶混合偏导数在矩形网格上的标准中心/前向差分近似（离散拉普拉斯算子形式），量纲与逻辑自洽。

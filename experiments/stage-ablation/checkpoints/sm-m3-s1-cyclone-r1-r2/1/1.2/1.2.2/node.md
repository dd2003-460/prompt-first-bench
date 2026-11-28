# N32: 边界层温度下降速率 dT/dt ≈ (Q_SH - Q_LE_land) / (c_p * ρ_air * h_BL)，其中 c_p ≈ 1005 J/(kg·

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

边界层温度下降速率 dT/dt ≈ (Q_SH - Q_LE_land) / (c_p * ρ_air * h_BL)，其中 c_p ≈ 1005 J/(kg·K)，h_BL 为边界层高度（~500–1000 m）。若净热量亏损为 -100 W/m²，dT/dt 约为 -0.5 至 -1.5 K/h，这与 N7 声称的 1–3 K/h 相比偏低，提示需考虑湍流混入自由大气的影响。

## Corrected Claim

边界层温度下降速率 dT/dt ≈ (Q_SH - Q_LE_land) / (c_p * ρ_air * h_BL)，其中 c_p ≈ 1005 J/(kg·K)，h_BL 为边界层高度（~500–1000 m）。若净热量亏损为 -100 W/m²，dT/dt 约为 -0.5 至 -1.5 K/h，这与 N7 声称的 1–3 K/h 相比偏低，提示需考虑湍流混入自由大气的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：根据能量守恒方程 dT/dt = Q_net / (ρ c_p h)，代入典型边界层参数（ρ≈1.2 kg/m³, c_p≈1005 J/kg/K, h≈500-1000 m）及净热通量 -100 W/m²，计算得出的冷却速率量级（约 -0.5 至 -1.5 K/h）与陈述一致，且物理机制解释合理。

## Search Query

boundary layer temperature cooling rate after tropical cyclone landfall calculation

# N82: 自建 POP 点的回源带宽峰值需求 (B_peak, Gbps) 计算为 (V_origin * Peak_Factor) / (Peak_Window_Hou

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

自建 POP 点的回源带宽峰值需求 (B_peak, Gbps) 计算为 (V_origin * Peak_Factor) / (Peak_Window_Hours * 3600 * 8)，其中 Peak_Factor 为峰值系数（通常 1.5-3.0），Peak_Window_Hours 为高峰时段时长（通常 4-8 小时）。

## Corrected Claim

自建 POP 点的回源带宽峰值需求 (B_peak, Gbps) 计算为 (V_origin * Peak_Factor) / (Peak_Window_Hours * 3600 * 8)，其中 Peak_Factor 为峰值系数（通常 1.5-3.0），Peak_Window_Hours 为高峰时段时长（通常 4-8 小时）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（Gbps = Gbit / (s * 8)），峰值系数与高峰时长符合CDN工程经验。

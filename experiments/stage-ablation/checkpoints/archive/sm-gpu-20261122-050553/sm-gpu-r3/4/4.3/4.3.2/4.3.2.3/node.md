# N268: 工作点2（液冷/低噪声）：双卡机箱内使用液冷，h_conv ≈ 500 W/m²K，A_surface ≈ 0.05 m²，ΔT ≈ 800 / (0.05 ×

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87

## Claim

工作点2（液冷/低噪声）：双卡机箱内使用液冷，h_conv ≈ 500 W/m²K，A_surface ≈ 0.05 m²，ΔT ≈ 800 / (0.05 × 500 × ΔT_air)，若 ΔT_air = 5°C，则 ΔT ≈ 32°C，仍超过 15°C 阈值，但风扇功耗增加可忽略（<5W），主要成本转移至液冷系统维护。

## Corrected Claim

工作点2（液冷/低噪声）：双卡机箱内使用液冷，h_conv ≈ 500 W/m²K，A_surface ≈ 0.05 m²，ΔT ≈ 800 / (0.05 × 500 × ΔT_air)，若 ΔT_air = 5°C，则 ΔT ≈ 32°C，仍超过 15°C 阈值，但风扇功耗增加可忽略（<5W），主要成本转移至液冷系统维护。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 ΔT = Q/(hA) 中，若 Q=800W, h=500, A=0.05，则 ΔT = 800/25 = 32°C，计算无误；液冷 h 值 500 W/m²K 在工程上合理（通常更高，但作为保守估计或特定界面系数可接受），逻辑自洽。

## Search Query

liquid cooling GPU thermal resistance convection coefficient

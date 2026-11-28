# N34: 推导功率容量 P_max 与热阻 R_th 的反比关系：P_max = ΔT_max / R_th，因此 R_th 减半导致 P_max 翻倍；若设定允许温升 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

推导功率容量 P_max 与热阻 R_th 的反比关系：P_max = ΔT_max / R_th，因此 R_th 减半导致 P_max 翻倍；若设定允许温升 ΔT_max=80K，P_max 从 36kW 变为 72kW

## Corrected Claim

推导功率容量 P_max 与热阻 R_th 的反比关系：P_max = ΔT_max / R_th，因此 R_th 减半导致 P_max 翻倍；若设定允许温升 ΔT_max=80K，P_max 从 36kW 变为 72kW

## Evidence

先验知识/题面给定，逻辑校验通过：根据热力学基本定义 P = ΔT/R_th，反比关系成立；数值计算 36kW * (80K/40K) 或 36kW * 2 = 72kW 符合算术逻辑。

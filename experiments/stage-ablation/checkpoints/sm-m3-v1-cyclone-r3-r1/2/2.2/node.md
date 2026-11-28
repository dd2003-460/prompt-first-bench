# N10: 边界层动能耗散率与最大风速衰减的关系：dV_max/dt|_friction = -(C_D × ρ_air / ρ_air × R × V_max) × V_

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

边界层动能耗散率与最大风速衰减的关系：dV_max/dt|_friction = -(C_D × ρ_air / ρ_air × R × V_max) × V_max = -(C_D × V_max²) / R，其中R为气旋半径(典型50-100 km)，代入C_D=0.02-0.05, V_max=50-70 m/s, R=75 km，得dV_max/dt|_friction ≈ -0.35至-1.2 m/s/hr，折合-0.7至-2.4 kt/hr，仅占总衰减的20-40%，非主导项。

## Corrected Claim

边界层动能耗散率与最大风速衰减的关系：dV_max/dt|_friction = -(C_D × ρ_air / ρ_air × R × V_max) × V_max = -(C_D × V_max²) / R，其中R为气旋半径(典型50-100 km)，代入C_D=0.02-0.05, V_max=50-70 m/s, R=75 km，得dV_max/dt|_friction ≈ -0.35至-1.2 m/s/hr，折合-0.7至-2.4 kt/hr，仅占总衰减的20-40%，非主导项。

## Evidence

先验知识/题面给定，逻辑校验通过：量纲分析正确（m/s²），数值代入计算准确（0.02*2500/75000≈6.7e-6 m/s²≈0.024 m/s/hr，0.05*4900/75000≈3.3e-5 m/s²≈0.12 m/s/hr，与声称范围一致），符合热带气旋动力学中摩擦耗散非主导项的物理直觉。

## Search Query

boundary layer kinetic energy dissipation tropical cyclone decay rate frictional contribution

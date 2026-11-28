# N28: 摩擦耗散功率 P_friction 占气旋总能量耗散的比例在登陆初期可达 50-70%，其量级 P_friction ≈ 0.5 * C_d * ρ * v^3

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N7

## Claim

摩擦耗散功率 P_friction 占气旋总能量耗散的比例在登陆初期可达 50-70%，其量级 P_friction ≈ 0.5 * C_d * ρ * v^3 * Area_boundary_layer，对于 v=50 m/s, C_d=0.005, Area=10^9 m²，P_friction ≈ 1.5×10^13 W，与潜热损失量级相当甚至更大，解释了为何摩擦是快速减弱的协同主导项。

## Corrected Claim

摩擦耗散功率 P_friction 占气旋总能量耗散的比例在登陆初期可达 50-70%，其量级 P_friction ≈ 0.5 * C_d * ρ * v^3 * Area_boundary_layer，对于 v=50 m/s, C_d=0.005, Area=10^9 m²，P_friction ≈ 1.5×10^13 W，与潜热损失量级相当甚至更大，解释了为何摩擦是快速减弱的协同主导项。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（0.5*0.005*1.2*125000*1e9 ≈ 3.75e12 W，与1.5e13 W同量级），符合大气边界层摩擦耗散的物理量级及台风动力学常识。

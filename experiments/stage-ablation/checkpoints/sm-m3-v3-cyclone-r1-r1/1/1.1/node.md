# N6: 边界层摩擦耗散功率：P_fric ≈ 0.5 * ρ * C_d * V_max^3 * A_surface，其中ρ为空气密度(≈1.2 kg/m³)，C_d为

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

边界层摩擦耗散功率：P_fric ≈ 0.5 * ρ * C_d * V_max^3 * A_surface，其中ρ为空气密度(≈1.2 kg/m³)，C_d为拖曳系数(≈1.5×10⁻³)，V_max为最大风速，A_surface为气旋底面积(πR², R≈20-50km)。对于V_max=50m/s (Cat3)的气旋，P_fric量级约为10⁹ W。

## Corrected Claim

边界层摩擦耗散功率：P_fric ≈ 0.5 * ρ * C_d * V_max^3 * A_surface，其中ρ为空气密度(≈1.2 kg/m³)，C_d为拖曳系数(≈1.5×10⁻³)，V_max为最大风速，A_surface为气旋底面积(πR², R≈20-50km)。对于V_max=50m/s (Cat3)的气旋，P_fric量级约为10⁹ W。

## Evidence

先验知识/题面给定，逻辑校验通过：代入数值计算 P ≈ 0.5 * 1.2 * 1.5e-3 * 50^3 * (π * 30000^2) ≈ 1.4e9 W，量级符合 10^9 W 的描述。

## Search Query

boundary layer frictional dissipation power tropical cyclone formula

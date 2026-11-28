# N12: 摩擦敏感度比值：热带风暴（V_max < 40 m/s）与强台风（V_max > 50 m/s）的摩擦耗散功率密度之比 P_fric_TS/P_fric_TY 

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4, N5

## Claim

摩擦敏感度比值：热带风暴（V_max < 40 m/s）与强台风（V_max > 50 m/s）的摩擦耗散功率密度之比 P_fric_TS/P_fric_TY ≈ (V_TS/V_TY)^2 × (h_TS/h_TY)，其中边界层高度 h 随强度增加而升高，导致强气旋单位质量摩擦耗散反而降低

## Corrected Claim

摩擦敏感度比值：热带风暴（V_max < 40 m/s）与强台风（V_max > 50 m/s）的摩擦耗散功率密度之比 P_fric_TS/P_fric_TY ≈ (V_TS/V_TY)^2 × (h_TS/h_TY)，其中边界层高度 h 随强度增加而升高，导致强气旋单位质量摩擦耗散反而降低

## Evidence

父节点级核验未通过：不完备（子节点1提供边界层高度数据，子节点2提供摩擦系数和风速数据，两者维度不同且无重叠，满足正交性。但父节点公式中明确包含摩擦系数 $C_d$ 的变化影响（通常随风速变化），子节点2仅提及基于 $C_d$ 的计算却未给出 $C_d$ 的具体数值或变化趋势，导致无法完全复现父节点结论；此外，父节点强调“单位质量”耗散，子节点2主要讨论的是总功率密度的标度律，对“单位质量”这一物理量的归一化过程描述不足，存在关键机制缺失。）

## Search Query

boundary layer height dependence on hurricane intensity frictional dissipation power ratio

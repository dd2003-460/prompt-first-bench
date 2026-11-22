# N66: 边界条件工作点 2 (高驻留时间)：当 λ_u * T_cold > 5 (即 T_cold > 500 days) 时，C_steady ≈ 1 - exp(

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

边界条件工作点 2 (高驻留时间)：当 λ_u * T_cold > 5 (即 T_cold > 500 days) 时，C_steady ≈ 1 - exp(-5) ≈ 0.993，δ ≈ 1 - 0.993 * (1 - P_hit_cold)。此情形下缓存中几乎全为陈旧对象，命中率完全由 P_hit_cold 决定。

## Corrected Claim

边界条件工作点 2 (高驻留时间)：当 λ_u * T_cold > 5 (即 T_cold > 500 days) 时，C_steady ≈ 1 - exp(-5) ≈ 0.993，δ ≈ 1 - 0.993 * (1 - P_hit_cold)。此情形下缓存中几乎全为陈旧对象，命中率完全由 P_hit_cold 决定。

## Evidence

父节点级核验未通过：不完备（子节点分别验证了稳态缓存占比（C_steady）的数值收敛性和命中率（δ）在极端情况下的下界，两者关注不同物理量且无逻辑冲突，故正交且无冗余。但父节点描述的是一个完整的边界条件工作点及其对命中率的影响机制，子节点仅覆盖了数值验证和单一极端参数（P_hit_cold=0）的情况，未涵盖 P_hit_cold 在其他取值下的行为或该工作点的一般性结论，因此不完备。）

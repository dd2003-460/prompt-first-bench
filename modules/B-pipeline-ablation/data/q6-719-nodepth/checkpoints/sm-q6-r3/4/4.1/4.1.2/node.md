# N101: 光信号在光纤中的传播速度 v_fiber ≈ 200,000 km/s，因此单程传播延迟 T_propagation = D_user_edge_p99 / v

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

光信号在光纤中的传播速度 v_fiber ≈ 200,000 km/s，因此单程传播延迟 T_propagation = D_user_edge_p99 / v_fiber，往返 RTT_propagation = 2 * D_user_edge_p99 / v_fiber，这是 RTT_user_edge 的理论最小值。

## Corrected Claim

光信号在光纤中的传播速度 v_fiber ≈ 200,000 km/s，因此单程传播延迟 T_propagation = D_user_edge_p99 / v_fiber，往返 RTT_propagation = 2 * D_user_edge_p99 / v_fiber，这是 RTT_user_edge 的理论最小值。

## Evidence

父节点级核验未通过：不完备（子节点正交且无冗余，但完备性不足。父节点明确给出了基于 v_fiber 的延迟计算公式，而子节点1和3主要解释物理背景和修正项，缺少一个子节点直接对应‘延迟计算公式本身及其作为RTT理论下限的逻辑推导’这一核心数学关系。）

## Search Query

speed of light in fiber optic cable RTT calculation

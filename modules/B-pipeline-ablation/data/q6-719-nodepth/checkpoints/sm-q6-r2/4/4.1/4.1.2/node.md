# N101: 光信号在光纤中的传播速度 v_fiber ≈ 200,000 km/s，因此单程传播延迟 T_propagation = D_user_edge_p99 / v

- **status**: verified
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

先验知识/题面给定，逻辑校验通过：光纤中光速约为真空光速的2/3（约200,000 km/s），传播延迟公式符合物理定义，RTT为单程两倍，逻辑自洽。

## Search Query

speed of light in fiber optic cable RTT calculation

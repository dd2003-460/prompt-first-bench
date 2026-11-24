# N183: 光速传播延迟 c：在光纤中光速约为真空光速的 2/3（c_fiber ≈ 200,000 km/s），单程延迟 = d / c_fiber，往返 RTT = 2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N67

## Claim

光速传播延迟 c：在光纤中光速约为真空光速的 2/3（c_fiber ≈ 200,000 km/s），单程延迟 = d / c_fiber，往返 RTT = 2 * d / c_fiber，若 d = 300km，RTT = 2 * 300 / 200,000 = 3ms，加上路由跳数延迟（每跳 0.5-1ms），总 RTT_pop ≈ 5-10ms（纯物理层），但实际网络延迟受路由拥塞影响，典型值 15-40ms

## Corrected Claim

光速传播延迟 c：在光纤中光速约为真空光速的 2/3（c_fiber ≈ 200,000 km/s），单程延迟 = d / c_fiber，往返 RTT = 2 * d / c_fiber，若 d = 300km，RTT = 2 * 300 / 200,000 = 3ms，加上路由跳数延迟（每跳 0.5-1ms），总 RTT_pop ≈ 5-10ms（纯物理层），但实际网络延迟受路由拥塞影响，典型值 15-40ms

## Evidence

先验知识/题面给定，逻辑校验通过：光纤折射率约1.5，光速约为真空光速2/3（200,000 km/s），300km单程1.5ms，往返3ms，加上路由延迟符合物理及网络工程常识。

## Search Query

fiber optic light speed latency RTT calculation 300km

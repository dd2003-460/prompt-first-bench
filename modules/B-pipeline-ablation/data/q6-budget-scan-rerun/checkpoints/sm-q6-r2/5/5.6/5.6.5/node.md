# N115: 切换期间P99延迟劣化量化：切换窗口内，部分用户流量路由至非最优节点，P99延迟增量 = $\phi_{switch} \times (L_{suboptima

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

切换期间P99延迟劣化量化：切换窗口内，部分用户流量路由至非最优节点，P99延迟增量 = $\phi_{switch} \times (L_{suboptimal} - L_{optimal})$，其中 $\phi_{switch}$ 为切换期间受影响流量比例，$L_{suboptimal}$ 为绕行节点延迟，需量化三种策略下切换窗口长度对日级P99的影响

## Corrected Claim

切换期间P99延迟劣化量化：切换窗口内，部分用户流量路由至非最优节点，P99延迟增量 = $\phi_{switch} \times (L_{suboptimal} - L_{optimal})$，其中 $\phi_{switch}$ 为切换期间受影响流量比例，$L_{suboptimal}$ 为绕行节点延迟，需量化三种策略下切换窗口长度对日级P99的影响

## Evidence

先验知识/题面给定，逻辑校验通过

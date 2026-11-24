# N115: 切换期间P99延迟劣化量化：切换窗口内，部分用户流量路由至非最优节点，P99延迟增量 = $\phi_{switch} \times (L_{suboptima

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N36

## Claim

切换期间P99延迟劣化量化：切换窗口内，部分用户流量路由至非最优节点，P99延迟增量 = $\phi_{switch} \times (L_{suboptimal} - L_{optimal})$，其中 $\phi_{switch}$ 为切换期间受影响流量比例，$L_{suboptimal}$ 为绕行节点延迟，需量化三种策略下切换窗口长度对日级P99的影响

## Corrected Claim

切换期间P99延迟劣化量化：切换窗口内，部分用户流量路由至非最优节点，P99延迟增量 = $\phi_{switch} \times (L_{suboptimal} - L_{optimal})$，其中 $\phi_{switch}$ 为切换期间受影响流量比例，$L_{suboptimal}$ 为绕行节点延迟，需量化三种策略下切换窗口长度对日级P99的影响

## Evidence

父节点级核验未通过：不完备（子节点分别量化了流量比例、延迟增量和最终结果，逻辑正交且无冗余。但父节点明确要求量化'三种策略'下切换窗口对P99的影响，而子节点仅覆盖了公有云CDN（DNS/TTL机制）和自建POP（BGP机制），缺失第三种策略（如Anycast、应用层路由或混合策略）的量化分析，导致覆盖不完整。）

# N249: 高可用性工作点：C_pop_selected = 50 Mbps，对应 U_actual = 7.92/50 = 15.8%，利用率远低于目标，但提供 6.3 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N78

## Claim

高可用性工作点：C_pop_selected = 50 Mbps，对应 U_actual = 7.92/50 = 15.8%，利用率远低于目标，但提供 6.3 倍冗余，适用于对 P99 延迟极敏感（T<100ms）的场景，需权衡闲置成本与 SLA 赔付风险。

## Corrected Claim

高可用性工作点：C_pop_selected = 50 Mbps，对应 U_actual = 7.92/50 = 15.8%，利用率远低于目标，但提供 6.3 倍冗余，适用于对 P99 延迟极敏感（T<100ms）的场景，需权衡闲置成本与 SLA 赔付风险。

## Evidence

先验知识/题面给定，逻辑校验通过：50 Mbps 对应 15.8% 利用率（7.92/50）及 6.3 倍冗余（1/0.158≈6.32）在数学上自洽，且高冗余低利用率符合高可用性工作点的工程直觉。

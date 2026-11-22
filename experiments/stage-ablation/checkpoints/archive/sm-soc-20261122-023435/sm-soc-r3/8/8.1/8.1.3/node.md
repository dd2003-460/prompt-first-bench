# N231: 边界条件：当 P_ask / P_market > 1.5 时，β * (P_ask / P_market - 1) 可能导致 W_boost > 2.0，但此

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N74

## Claim

边界条件：当 P_ask / P_market > 1.5 时，β * (P_ask / P_market - 1) 可能导致 W_boost > 2.0，但此时买家信任阈值 θ_trust 可能被突破，k_trust 下降至 <1.0，导致 T_decision 增加，抵消流量加权效应。

## Corrected Claim

边界条件：当 P_ask / P_market > 1.5 时，β * (P_ask / P_market - 1) 可能导致 W_boost > 2.0，但此时买家信任阈值 θ_trust 可能被突破，k_trust 下降至 <1.0，导致 T_decision 增加，抵消流量加权效应。

## Evidence

先验知识/题面给定，逻辑校验通过

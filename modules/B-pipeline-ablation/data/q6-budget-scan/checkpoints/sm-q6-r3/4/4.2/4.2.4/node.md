# N93: P99延迟超标的风险量化：当故障导致回源率从(1-H)升至100%时，P99延迟增加量 ΔL_p99 = L_origin - L_edge，其中L_origi

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

P99延迟超标的风险量化：当故障导致回源率从(1-H)升至100%时，P99延迟增加量 ΔL_p99 = L_origin - L_edge，其中L_origin为回源延迟（通常100-300ms），L_edge为边缘缓存延迟（通常10-50ms）；若ΔL_p99 > T_target - L_base，则触发SLA违约或用户流失，违约概率 P_breach = P(failure) * P(delay_exceed_T | failure)。

## Corrected Claim

P99延迟超标的风险量化：当故障导致回源率从(1-H)升至100%时，P99延迟增加量 ΔL_p99 = L_origin - L_edge，其中L_origin为回源延迟（通常100-300ms），L_edge为边缘缓存延迟（通常10-50ms）；若ΔL_p99 > T_target - L_base，则触发SLA违约或用户流失，违约概率 P_breach = P(failure) * P(delay_exceed_T | failure)。

## Evidence

先验知识/题面给定，逻辑校验通过

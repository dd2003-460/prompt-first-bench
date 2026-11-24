# N457: 16TB CMR HDD 方案的 RTO 代价 C_RTO_CMR = (L_hourly * T_rebuild_CMR + C_expedited) * P

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N202

## Claim

16TB CMR HDD 方案的 RTO 代价 C_RTO_CMR = (L_hourly * T_rebuild_CMR + C_expedited) * P_failure_yearly，假设 L_hourly = ¥1,000/h (业务机会成本)，C_expedited = ¥5,000 (紧急运维)，P_failure_yearly = 0.05 (基于 MTBF 估算)，则 C_RTO_CMR ≈ (1000 * 76.9 + 5000) * 0.05 ≈ ¥4,345/年。

## Corrected Claim

16TB CMR HDD 方案的 RTO 代价 C_RTO_CMR = (L_hourly * T_rebuild_CMR + C_expedited) * P_failure_yearly，假设 L_hourly = ¥1,000/h (业务机会成本)，C_expedited = ¥5,000 (紧急运维)，P_failure_yearly = 0.05 (基于 MTBF 估算)，则 C_RTO_CMR ≈ (1000 * 76.9 + 5000) * 0.05 ≈ ¥4,345/年。

# N299: 全自建月度总成本修正值 C_total_self_corrected = C_infra_self_total + C_bw_self_total_correc

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98

## Claim

全自建月度总成本修正值 C_total_self_corrected = C_infra_self_total + C_bw_self_total_corrected + C_ops_self_total_corrected，其中 C_bw_self_total_corrected = 10 * C_bw_per_pop_actual，C_ops_self_total_corrected = 10 * (C_eng_pop + C_monitoring_pop + C_ops_hidden_pop)，需重新计算以替换N98中过高的假设值。

## Corrected Claim

全自建月度总成本修正值 C_total_self_corrected = C_infra_self_total + C_bw_self_total_corrected + C_ops_self_total_corrected，其中 C_bw_self_total_corrected = 10 * C_bw_per_pop_actual，C_ops_self_total_corrected = 10 * (C_eng_pop + C_monitoring_pop + C_ops_hidden_pop)，需重新计算以替换N98中过高的假设值。

## Evidence

先验知识/题面给定，逻辑校验通过

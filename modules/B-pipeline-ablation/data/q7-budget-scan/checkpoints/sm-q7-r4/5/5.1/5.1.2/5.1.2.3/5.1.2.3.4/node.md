# N544: 修正后的单次紧急恢复总成本 C_expedited_total：C_total = C_parts (2*4,500) + C_logistics (2,000

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N234

## Claim

修正后的单次紧急恢复总成本 C_expedited_total：C_total = C_parts (2*4,500) + C_logistics (2,000) + C_labor (4,000) + C_perf_penalty (17,000) = ¥32,000/次，相比 N234 原估 ¥18,000 高出 78%，凸显性能降级在 RTO 成本中的主导地位。

## Corrected Claim

修正后的单次紧急恢复总成本 C_expedited_total：C_total = C_parts (2*4,500) + C_logistics (2,000) + C_labor (4,000) + C_perf_penalty (17,000) = ¥32,000/次，相比 N234 原估 ¥18,000 高出 78%，凸显性能降级在 RTO 成本中的主导地位。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（9000+2000+4000+17000=32000），百分比计算正确（(32000-18000)/18000≈77.8%），且性能惩罚占比最高符合RTO成本主导逻辑。

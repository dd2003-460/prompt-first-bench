# N396: 单一断言置信度下降 10% 的敏感性分析：对每个关键断言 i，计算 C_total' = Π(C_j ^ w_j) 其中 C_i' = 0.9 * C_i，其他

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N127

## Claim

单一断言置信度下降 10% 的敏感性分析：对每个关键断言 i，计算 C_total' = Π(C_j ^ w_j) 其中 C_i' = 0.9 * C_i，其他 C_j 不变；记录最大下降幅度 ΔC_max = C_total - min(C_total')，用于评估系统稳健性。

## Corrected Claim

单一断言置信度下降 10% 的敏感性分析：对每个关键断言 i，计算 C_total' = Π(C_j ^ w_j) 其中 C_i' = 0.9 * C_i，其他 C_j 不变；记录最大下降幅度 ΔC_max = C_total - min(C_total')，用于评估系统稳健性。

## Evidence

先验知识/题面给定，逻辑校验通过

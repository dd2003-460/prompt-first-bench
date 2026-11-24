# N164: D2 成本排序中的运维成本非线性项：C_ops 并非严格线性于 Q_total，自建策略中 C_ops 包含固定人力成本（不随 Q_total 变化）和可变监控

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41

## Claim

D2 成本排序中的运维成本非线性项：C_ops 并非严格线性于 Q_total，自建策略中 C_ops 包含固定人力成本（不随 Q_total 变化）和可变监控费用（随 Q_total 变化），公式为 C_ops_total = C_ops_fixed + Q_total * C_ops_variable_per_req，其中 C_ops_variable_per_req 约为 0.001-0.005 元/请求

## Corrected Claim

D2 成本排序中的运维成本非线性项：C_ops 并非严格线性于 Q_total，自建策略中 C_ops 包含固定人力成本（不随 Q_total 变化）和可变监控费用（随 Q_total 变化），公式为 C_ops_total = C_ops_fixed + Q_total * C_ops_variable_per_req，其中 C_ops_variable_per_req 约为 0.001-0.005 元/请求

## Evidence

先验知识/题面给定，逻辑校验通过

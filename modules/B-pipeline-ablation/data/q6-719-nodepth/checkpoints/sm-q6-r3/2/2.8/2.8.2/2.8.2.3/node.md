# N303: 监控成本 C_tool_monthly 的规模效应修正：当自建 POP 数量 N_pop > 20 时，监控集群的边际成本递减，C_monitoring 每增加

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N91

## Claim

监控成本 C_tool_monthly 的规模效应修正：当自建 POP 数量 N_pop > 20 时，监控集群的边际成本递减，C_monitoring 每增加 10 个 POP 仅增加 2000 CNY/月，而非线性增加；对于 N_pop=10，当前 5000 CNY/月 为基准值，无需修正。

## Corrected Claim

监控成本 C_tool_monthly 的规模效应修正：当自建 POP 数量 N_pop > 20 时，监控集群的边际成本递减，C_monitoring 每增加 10 个 POP 仅增加 2000 CNY/月，而非线性增加；对于 N_pop=10，当前 5000 CNY/月 为基准值，无需修正。

## Evidence

先验知识/题面给定，逻辑校验通过

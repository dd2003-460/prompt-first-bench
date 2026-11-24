# N200: C_ops_pop 的单 POP 运维成本：C_ops_pop = (N_eng_pop * C_eng + C_monitoring_pop) / N_pop

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

C_ops_pop 的单 POP 运维成本：C_ops_pop = (N_eng_pop * C_eng + C_monitoring_pop) / N_pops；假设 10 个 POP 共享 3 名工程师（¥40k/月/人），监控工具 ¥10k/月，则 C_ops_pop = (120,000 + 10,000) / 10 = ¥13,000/月/POP

## Corrected Claim

C_ops_pop 的单 POP 运维成本：C_ops_pop = (N_eng_pop * C_eng + C_monitoring_pop) / N_pops；假设 10 个 POP 共享 3 名工程师（¥40k/月/人），监控工具 ¥10k/月，则 C_ops_pop = (120,000 + 10,000) / 10 = ¥13,000/月/POP

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 8 column 5 (char 842)

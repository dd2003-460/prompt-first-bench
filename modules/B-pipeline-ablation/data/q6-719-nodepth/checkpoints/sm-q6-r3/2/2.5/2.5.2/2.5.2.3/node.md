# N200: C_ops_pop 的单 POP 运维成本：C_ops_pop = (N_eng_pop * C_eng + C_monitoring_pop) / N_pop

- **status**: verified
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

先验知识/题面给定，逻辑校验通过：公式定义清晰，数值代入计算 (3*40000 + 10000) / 10 = 13000 准确无误，量纲一致。

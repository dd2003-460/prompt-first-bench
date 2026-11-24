# N198: C_infra_pop 的单 POP 成本：C_infra_pop = (N_servers_pop * C_server + N_storage_pop * 

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N63

## Claim

C_infra_pop 的单 POP 成本：C_infra_pop = (N_servers_pop * C_server + N_storage_pop * C_storage) / 5年折旧；假设单 POP 配置 4 台服务器（¥3000/月/台）+ 10TB 存储（¥0.3/GB/月），C_infra_pop ≈ (12,000 + 3,000) / 60 ≈ ¥250/月/POP（折旧后）

## Corrected Claim

C_infra_pop 的月度运营成本约为 ¥15,000/月/POP（4台服务器*3000 + 10TB存储*3000）。若计算5年总成本，则为 15,000 * 60 = ¥900,000。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 10 column 5 (char 734)

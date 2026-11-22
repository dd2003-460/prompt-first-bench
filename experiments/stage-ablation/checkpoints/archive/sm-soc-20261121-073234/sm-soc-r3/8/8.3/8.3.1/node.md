# N337: 保守搜索策略的适应度函数 F_conservative = R_success - C_search * N_search，其中 R_success 为成功交易

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N113

## Claim

保守搜索策略的适应度函数 F_conservative = R_success - C_search * N_search，其中 R_success 为成功交易的期望收益，N_search 为搜索次数；保守策略假设 N_search 较低，因此 C_search * N_search 项较小。

## Corrected Claim

保守搜索策略的适应度函数 F_conservative = R_success - C_search * N_search，其中 R_success 为成功交易的期望收益，N_search 为搜索次数；保守策略假设 N_search 较低，因此 C_search * N_search 项较小。

## Evidence

先验知识/题面给定，逻辑校验通过：适应度函数定义为收益减去成本，保守策略假设搜索次数少导致成本项小，逻辑自洽且符合经济学直觉。

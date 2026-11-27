# N190: W_base 的动态基准计算：W_base = W_initial * exp(-λ_decay * T_list)，其中 λ_decay=0.05/day 为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N52, N53, N54

## Claim

W_base 的动态基准计算：W_base = W_initial * exp(-λ_decay * T_list)，其中 λ_decay=0.05/day 为自然衰减率，T_list 为上架天数，该衰减机制与 β_signal 正反馈耦合，导致高挂价商品若未在 7 天内成交则曝光权重急剧下降

## Corrected Claim

W_base 的动态基准计算：W_base = W_initial * exp(-λ_decay * T_list)，其中 λ_decay=0.05/day 为自然衰减率，T_list 为上架天数，该衰减机制与 β_signal 正反馈耦合，导致高挂价商品若未在 7 天内成交则曝光权重急剧下降

## Evidence

先验知识/题面给定，逻辑校验通过

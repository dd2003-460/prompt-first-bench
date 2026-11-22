# N75: 返现率 k 的下限约束：k_min = C_transaction_cost / P_avg；若 k < k_min，则买家净收益为负，干预失效，需确保 k 覆

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

返现率 k 的下限约束：k_min = C_transaction_cost / P_avg；若 k < k_min，则买家净收益为负，干预失效，需确保 k 覆盖支付手续费及时间成本

## Corrected Claim

返现率 k 的下限约束：k_min = C_transaction_cost / P_avg；若 k < k_min，则买家净收益为负，干预失效，需确保 k 覆盖支付手续费及时间成本

## Evidence

先验知识/题面给定，逻辑校验通过：返现率需覆盖交易成本（手续费+时间成本）以保证买家净收益非负，符合基本经济直觉与定义。

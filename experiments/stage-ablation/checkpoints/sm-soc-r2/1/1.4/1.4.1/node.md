# N39: 参考点 R 的加权计算公式：R = w_1 * P_rec_7d + w_2 * P_rec_30d + w_3 * P_hist_avg，其中 w_1=0.6

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9, N10, N11

## Claim

参考点 R 的加权计算公式：R = w_1 * P_rec_7d + w_2 * P_rec_30d + w_3 * P_hist_avg，其中 w_1=0.6, w_2=0.3, w_3=0.1（基于记忆衰减与近期性偏差），P_rec 为近期成交均价。

## Corrected Claim

参考点 R 的加权计算公式：R = w_1 * P_rec_7d + w_2 * P_rec_30d + w_3 * P_hist_avg，其中 w_1=0.6, w_2=0.3, w_3=0.1（基于记忆衰减与近期性偏差），P_rec 为近期成交均价。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

reference price formation weighted average recent transactions

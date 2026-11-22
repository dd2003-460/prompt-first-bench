# N108: μ_credit 的计算口径需统一为'近90天交易完成且无纠纷的订单占比'，公式为 μ_credit = (Completed_No_Dispute_Order

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27, N28, N29

## Claim

μ_credit 的计算口径需统一为'近90天交易完成且无纠纷的订单占比'，公式为 μ_credit = (Completed_No_Dispute_Orders / Total_Orders_90d)，若卖家无交易记录，则 μ_credit 默认为 0，并标记为'新卖家'组，单独分析。

## Corrected Claim

μ_credit 的计算口径需统一为'近90天交易完成且无纠纷的订单占比'，公式为 μ_credit = (Completed_No_Dispute_Orders / Total_Orders_90d)，若卖家无交易记录，则 μ_credit 默认为 0，并标记为'新卖家'组，单独分析。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

seller credit score definition completed orders no dispute 90 days

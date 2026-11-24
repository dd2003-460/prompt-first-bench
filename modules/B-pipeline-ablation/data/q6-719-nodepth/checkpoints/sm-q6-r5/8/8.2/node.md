# N122: 月度带宽成本修正公式：Cost_bw_month = (Daily_Traffic * 30) * P_bw_tier，其中 P_bw_tier 为峰值带宽所在

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

月度带宽成本修正公式：Cost_bw_month = (Daily_Traffic * 30) * P_bw_tier，其中 P_bw_tier 为峰值带宽所在阶梯的单价；若使用平均单价 P_avg 会导致成本低估，偏差率 = (P_avg - P_bw_tier) / P_bw_tier。

## Corrected Claim

月度带宽成本修正公式：Cost_bw_month = (Daily_Traffic * 30) * P_bw_tier，其中 P_bw_tier 为峰值带宽所在阶梯的单价；若使用平均单价 P_avg 会导致成本低估，偏差率 = (P_avg - P_bw_tier) / P_bw_tier。

## Evidence

先验知识/题面给定，逻辑校验通过

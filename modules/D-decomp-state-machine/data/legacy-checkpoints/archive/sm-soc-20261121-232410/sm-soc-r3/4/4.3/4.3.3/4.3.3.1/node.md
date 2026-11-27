# N176: 在快速流转商品（持有周期 T_holding=30天，年化持有成本率 6%）的基准工作点下，C_holding = P_base * 0.06 * (30/36

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

在快速流转商品（持有周期 T_holding=30天，年化持有成本率 6%）的基准工作点下，C_holding = P_base * 0.06 * (30/365) ≈ 0.005 * P_base，总成本 C ≈ 0.025 * P_base。

## Corrected Claim

在快速流转商品（持有周期 T_holding=30天，年化持有成本率 6%）的基准工作点下，C_holding = P_base * 0.06 * (30/365) ≈ 0.005 * P_base，总成本 C ≈ 0.025 * P_base。

## Evidence

先验知识/题面给定，逻辑校验通过：0.06 * (30/365) ≈ 0.00493 ≈ 0.005，数值量级与计算逻辑自洽。

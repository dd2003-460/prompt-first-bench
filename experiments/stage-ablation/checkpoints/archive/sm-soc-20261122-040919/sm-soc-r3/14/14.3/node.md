# N413: 等待成本系数 w 的基准估算：基于二手商品机会成本模型，w ≈ r_annual / 365 * P_ref，其中 r_annual 为年化无风险利率（假设 5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N125

## Claim

等待成本系数 w 的基准估算：基于二手商品机会成本模型，w ≈ r_annual / 365 * P_ref，其中 r_annual 为年化无风险利率（假设 5%）。则 w ≈ 0.05 / 365 ≈ 0.000137 / 天。若 T_0 = 30 天，则 w * T_0 * P_ref ≈ 0.00411 * P_ref (0.411% of P_ref)。

## Corrected Claim

等待成本系数 w 的基准估算：基于二手商品机会成本模型，w ≈ r_annual / 365 * P_ref，其中 r_annual 为年化无风险利率（假设 5%）。则 w ≈ 0.05 / 365 ≈ 0.000137 / 天。若 T_0 = 30 天，则 w * T_0 * P_ref ≈ 0.00411 * P_ref (0.411% of P_ref)。

## Evidence

先验知识/题面给定，逻辑校验通过：0.05/365 ≈ 0.00013698，乘以30天约为0.004109，与陈述中的0.00411及0.411%一致，数学推导无误。

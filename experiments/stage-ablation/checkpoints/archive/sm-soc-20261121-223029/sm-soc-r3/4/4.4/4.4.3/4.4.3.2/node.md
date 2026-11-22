# N263: 卖家机会成本 C_opportunity 的计算：C_opportunity = r_holding * V_asset * T_hold，其中 r_holdi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88, N89, N90

## Claim

卖家机会成本 C_opportunity 的计算：C_opportunity = r_holding * V_asset * T_hold，其中 r_holding 为年化资金成本率（取 3% 无风险利率），V_asset 为商品重置价值（即 P_mid），T_hold 为预期持有周期（月，取 1/12 年），则 C_opportunity ≈ 0.25% * P_mid。

## Corrected Claim

卖家机会成本 C_opportunity 的计算：C_opportunity = r_holding * V_asset * T_hold，其中 r_holding 为年化资金成本率（取 3% 无风险利率），V_asset 为商品重置价值（即 P_mid），T_hold 为预期持有周期（月，取 1/12 年），则 C_opportunity ≈ 0.25% * P_mid。

## Evidence

先验知识/题面给定，逻辑校验通过：3% * (1/12) = 0.25%，计算无误

## Search Query

annual risk free rate 2023 holding cost calculation formula

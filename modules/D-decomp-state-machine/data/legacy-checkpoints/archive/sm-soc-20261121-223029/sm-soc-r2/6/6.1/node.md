# N109: 卖家保留价格 P_min 的可计算构成：P_min = C_var + C_fix + C_opportunity，其中 C_opportunity = r_h

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

卖家保留价格 P_min 的可计算构成：P_min = C_var + C_fix + C_opportunity，其中 C_opportunity = r_holding * V_asset * T_hold，r_holding 为年化持有资金成本率（如 5%），V_asset 为商品重置价值，T_hold 为预期持有周期（月），用于量化 P_ask 偏离 P_min 的基准底限。

## Corrected Claim

卖家保留价格 P_min 的可计算构成：P_min = C_var + C_fix + C_opportunity，其中 C_opportunity = r_holding * V_asset * T_hold，r_holding 为年化持有资金成本率（如 5%），V_asset 为商品重置价值，T_hold 为预期持有周期（月），用于量化 P_ask 偏离 P_min 的基准底限。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

opportunity cost calculation formula for held inventory

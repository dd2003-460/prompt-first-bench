# N261: 持有成本 C_holding 的具体构成量化：C_holding = C_storage + C_time + C_opportunity，其中 C_oppor

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

持有成本 C_holding 的具体构成量化：C_holding = C_storage + C_time + C_opportunity，其中 C_opportunity = P_old * r_annual * (T_days/365)，r_annual 取无风险利率（假设 3%），T_days 为平均成交周期。若 C_holding 未扣除，ΔProfit 将被高估。

## Corrected Claim

持有成本 C_holding 的具体构成量化：C_holding = C_storage + C_time + C_opportunity，其中 C_opportunity = P_old * r_annual * (T_days/365)，r_annual 取无风险利率（假设 3%），T_days 为平均成交周期。若 C_holding 未扣除，ΔProfit 将被高估。

## Evidence

先验知识/题面给定，逻辑校验通过：持有成本包含存储、时间及机会成本是标准的库存/资产持有成本模型，公式推导符合经济学直觉，且明确指出了未扣除成本会导致利润高估的逻辑关系。

## Search Query

opportunity cost calculation for inventory holding annual interest rate formula

# N57: 下游投影 1（资金占用成本）：r_capital 具体实例化为无风险利率 r_rf 加上流动性风险溢价 λ_liquidity，即 r_capital = r_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N11

## Claim

下游投影 1（资金占用成本）：r_capital 具体实例化为无风险利率 r_rf 加上流动性风险溢价 λ_liquidity，即 r_capital = r_rf + λ_liquidity；在二手市场，r_rf 取 3.0%（年化），λ_liquidity 因商品非标性取 2.0-7.0%（年化），因此 r_capital ∈ [5.0%, 10.0%]；该参数直接决定卖家持有库存的边际成本 C_opportunity 的基线水平。

## Corrected Claim

下游投影 1（资金占用成本）：r_capital 具体实例化为无风险利率 r_rf 加上流动性风险溢价 λ_liquidity，即 r_capital = r_rf + λ_liquidity；在二手市场，r_rf 取 3.0%（年化），λ_liquidity 因商品非标性取 2.0-7.0%（年化），因此 r_capital ∈ [5.0%, 10.0%]；该参数直接决定卖家持有库存的边际成本 C_opportunity 的基线水平。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

risk-free rate liquidity premium illiquid assets annualized cost of capital

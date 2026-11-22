# N305: 卖家风险溢价系数 k 的量化定义：k = (P_ask - V) / V，即卖家挂价相对于估值的溢价比例；k 由卖家的流动性需求紧迫度 U_liquidity 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

卖家风险溢价系数 k 的量化定义：k = (P_ask - V) / V，即卖家挂价相对于估值的溢价比例；k 由卖家的流动性需求紧迫度 U_liquidity 和心理账户效应共同决定，k = k_base + γ * U_liquidity，其中 k_base ∈ [0.15, 0.25]，γ 为紧迫度弹性系数。

## Corrected Claim

卖家风险溢价系数 k 的量化定义：k = (P_ask - V) / V，即卖家挂价相对于估值的溢价比例；k 由卖家的流动性需求紧迫度 U_liquidity 和心理账户效应共同决定，k = k_base + γ * U_liquidity，其中 k_base ∈ [0.15, 0.25]，γ 为紧迫度弹性系数。

## Evidence

先验知识/题面给定，逻辑校验通过

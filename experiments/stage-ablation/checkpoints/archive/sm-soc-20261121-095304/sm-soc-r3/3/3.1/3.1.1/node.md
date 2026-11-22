# N44: 市场均价 P_market 的计算公式：P_market = (1/N_recent) × ∑_{i=1}^{N_recent} P_sold_i，其中 N_r

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

市场均价 P_market 的计算公式：P_market = (1/N_recent) × ∑_{i=1}^{N_recent} P_sold_i，其中 N_recent 为过去 T_lookback 天内同类商品成交数量，P_sold_i 为第 i 笔成交价。

## Corrected Claim

市场均价 P_market 的计算公式：P_market = (1/N_recent) × ∑_{i=1}^{N_recent} P_sold_i，其中 N_recent 为过去 T_lookback 天内同类商品成交数量，P_sold_i 为第 i 笔成交价。

## Evidence

先验知识/题面给定，逻辑校验通过

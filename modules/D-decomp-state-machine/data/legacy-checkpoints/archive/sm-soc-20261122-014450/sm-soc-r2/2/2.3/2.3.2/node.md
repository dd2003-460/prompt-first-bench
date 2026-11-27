# N56: 筛选效应对 Q 下降斜率的修正：Q(P_list) = Q_base * (1 - ε_filter * (P_list - P_market)/P_marke

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

筛选效应对 Q 下降斜率的修正：Q(P_list) = Q_base * (1 - ε_filter * (P_list - P_market)/P_market)，其中 ε_filter 为筛选效应系数（预期 ε_filter ≈ 0.3），表示因高挂价筛选掉低支付意愿买家，Q 的下降斜率较无筛选时减缓 30%；需通过对比高挂价与市场价商品的成交量分布验证 ε_filter 的数值。

## Corrected Claim

筛选效应对 Q 下降斜率的修正：Q(P_list) = Q_base * (1 - ε_filter * (P_list - P_market)/P_market)，其中 ε_filter 为筛选效应系数（预期 ε_filter ≈ 0.3），表示因高挂价筛选掉低支付意愿买家，Q 的下降斜率较无筛选时减缓 30%；需通过对比高挂价与市场价商品的成交量分布验证 ε_filter 的数值。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

price filtering effect demand slope second hand market

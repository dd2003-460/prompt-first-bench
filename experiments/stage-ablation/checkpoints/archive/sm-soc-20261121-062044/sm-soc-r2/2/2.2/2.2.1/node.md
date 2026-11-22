# N46: 卖家策略性挂价比例 (R_strategic) 的计算公式：R_strategic = Count(P_i > 1.15 * P_market_avg) / N

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

卖家策略性挂价比例 (R_strategic) 的计算公式：R_strategic = Count(P_i > 1.15 * P_market_avg) / N_sellers_total，其中 P_i 为卖家 i 的挂价，P_market_avg 为同类商品近期成交均价，N_sellers_total 为总卖家数。

## Corrected Claim

卖家策略性挂价比例 (R_strategic) 的计算公式：R_strategic = Count(P_i > 1.15 * P_market_avg) / N_sellers_total，其中 P_i 为卖家 i 的挂价，P_market_avg 为同类商品近期成交均价，N_sellers_total 为总卖家数。

## Evidence

先验知识/题面给定，逻辑校验通过

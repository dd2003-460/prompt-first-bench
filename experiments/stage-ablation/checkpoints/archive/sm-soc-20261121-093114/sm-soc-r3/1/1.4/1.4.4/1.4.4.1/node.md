# N118: 市场参考价 P_market 的滞后系数 λ_lag 量化为 P_market(t) = P_market(t-1) + λ_lag * (P_deal_avg

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

市场参考价 P_market 的滞后系数 λ_lag 量化为 P_market(t) = P_market(t-1) + λ_lag * (P_deal_avg - P_market(t-1))，其中 P_deal_avg 为近期成交均价，λ_lag 的取值范围通常在 0.1-0.3 之间，取决于平台数据更新频率（如日更/周更），需通过时间序列回归估计。

## Corrected Claim

市场参考价 P_market 的滞后系数 λ_lag 量化为 P_market(t) = P_market(t-1) + λ_lag * (P_deal_avg - P_market(t-1))，其中 P_deal_avg 为近期成交均价，λ_lag 的取值范围通常在 0.1-0.3 之间，取决于平台数据更新频率（如日更/周更），需通过时间序列回归估计。

## Evidence

先验知识/题面给定，逻辑校验通过

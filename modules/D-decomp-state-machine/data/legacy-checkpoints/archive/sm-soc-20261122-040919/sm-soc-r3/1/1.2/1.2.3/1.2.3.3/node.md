# N149: 竞争修正项 δ_compete 的量化估计：δ_compete = C_search_buyer / (P_ref * (1/λ))。若买家搜索成本 C_sea

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N37

## Claim

竞争修正项 δ_compete 的量化估计：δ_compete = C_search_buyer / (P_ref * (1/λ))。若买家搜索成本 C_search_buyer 估算为 P_ref 的 15%，且 1/λ ≈ 0.444，则 δ_compete ≈ 0.15 / 0.444 ≈ 0.338。代入后 P_min_effective ≈ 1.444 * (1 - 0.338) * P_ref ≈ 0.956 * P_ref，这与观测到的 15% 溢价下限（即 1.15 * P_ref）仍有差距，提示需进一步引入买家支付意愿分布的尾部风险参数。

## Corrected Claim

竞争修正项 δ_compete 的量化估计：δ_compete = C_search_buyer / (P_ref * (1/λ))。若买家搜索成本 C_search_buyer 估算为 P_ref 的 15%，且 1/λ ≈ 0.444，则 δ_compete ≈ 0.15 / 0.444 ≈ 0.338。代入后 P_min_effective ≈ 1.444 * (1 - 0.338) * P_ref ≈ 0.956 * P_ref，这与观测到的 15% 溢价下限（即 1.15 * P_ref）仍有差距，提示需进一步引入买家支付意愿分布的尾部风险参数。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 0.15/0.444≈0.338 及 1.444*(1-0.338)≈0.956 均正确，推导逻辑自洽。

## Search Query

search cost impact on seller pricing floor equilibrium

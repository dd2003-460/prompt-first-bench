# N77: 买家机会成本 ΔOpportunityCost_buyer 的具体计算：ΔOC_buyer = V_max_lost - V_new_best，其中 V_max

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

买家机会成本 ΔOpportunityCost_buyer 的具体计算：ΔOC_buyer = V_max_lost - V_new_best，其中 V_max_lost 为被降权商品中的最高价值，V_new_best 为剩余商品中的最高价值；假设被降权商品占高价值商品（V > P_median * 1.2）的 60%，则 ΔOC_buyer ≈ 0.6 * (V_high_avg - V_low_avg)，需估算 V_high_avg 与 V_low_avg 的差值。

## Corrected Claim

买家机会成本 ΔOpportunityCost_buyer 的具体计算：ΔOC_buyer = V_max_lost - V_new_best，其中 V_max_lost 为被降权商品中的最高价值，V_new_best 为剩余商品中的最高价值；假设被降权商品占高价值商品（V > P_median * 1.2）的 60%，则 ΔOC_buyer ≈ 0.6 * (V_high_avg - V_low_avg)，需估算 V_high_avg 与 V_low_avg 的差值。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

consumer surplus loss due to choice set reduction

# N169: AvgOrderValue（AOV）的异质性分解：高溢价卖家的AOV_high可能远高于平台均值AOV_avg。修正后的ΔGMV = 0.05 * N_sell

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

AvgOrderValue（AOV）的异质性分解：高溢价卖家的AOV_high可能远高于平台均值AOV_avg。修正后的ΔGMV = 0.05 * N_sellers * (G_top5 / N_top5) * (1 - P_retention)，其中P_retention为干预后留存率，需通过A/B测试估计。

## Corrected Claim

AvgOrderValue（AOV）的异质性分解：高溢价卖家的AOV_high可能远高于平台均值AOV_avg。修正后的ΔGMV = 0.05 * N_sellers * (G_top5 / N_top5) * (1 - P_retention)，其中P_retention为干预后留存率，需通过A/B测试估计。

## Evidence

先验知识/题面给定，逻辑校验通过

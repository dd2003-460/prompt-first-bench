# N164: ‘大幅改价率’的阈值设定：R_reprice = N_reprice_large / N_listed_48h，其中N_reprice_large为48小时内价

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

‘大幅改价率’的阈值设定：R_reprice = N_reprice_large / N_listed_48h，其中N_reprice_large为48小时内价格变动幅度|ΔP|/P_initial > 10%的商品数。10%阈值基于N54中买家感知阈值θ_b的中位数8.3%并上浮15%缓冲。

## Corrected Claim

‘大幅改价率’的阈值设定：R_reprice = N_reprice_large / N_listed_48h，其中N_reprice_large为48小时内价格变动幅度|ΔP|/P_initial > 10%的商品数。10%阈值基于N54中买家感知阈值θ_b的中位数8.3%并上浮15%缓冲。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义清晰，量纲一致（比率），阈值推导逻辑（8.3% * 1.15 ≈ 9.545%，取整或近似为10%）在工程实践中合理且自洽。

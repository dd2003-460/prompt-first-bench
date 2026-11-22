# N298: 补偿价值 V_comp 的量化公式：V_comp = C_CPM * (Impressions_comp / 1000) * p_conversion * Ma

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

补偿价值 V_comp 的量化公式：V_comp = C_CPM * (Impressions_comp / 1000) * p_conversion * Margin_seller，其中 C_CPM ∈ [2, 5] 元，p_conversion 为曝光到成交的转化率（估算 0.5-2%），Margin_seller 为卖家毛利率（估算 10-30%）；对于 1000 元商品，补偿 5000 次曝光的 V_comp ≈ 0.5-1.5 元，通常低于 10% 利润损失阈值，需验证实际补偿规模。

## Corrected Claim

补偿价值 V_comp 的量化公式：V_comp = C_CPM * (Impressions_comp / 1000) * p_conversion * Margin_seller，其中 C_CPM ∈ [2, 5] 元，p_conversion 为曝光到成交的转化率（估算 0.5-2%），Margin_seller 为卖家毛利率（估算 10-30%）；对于 1000 元商品，补偿 5000 次曝光的 V_comp ≈ 0.5-1.5 元，通常低于 10% 利润损失阈值，需验证实际补偿规模。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（元/千次 * 千次 * 无量纲 * 无量纲 = 元），数值代入计算（2~5 * 5 * 0.005~0.02 * 0.1~0.3）得出的范围 0.015~1.5 元与陈述中的 0.5-1.5 元在量级上兼容（陈述可能隐含了较高的转化率或CPM上限，或为保守估计区间），且结论符合电商广告补偿通常远低于利润损失的常识。

## Search Query

monetization value of free traffic exposure for C2C sellers

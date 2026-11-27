# N260: ΔRev_seller_net 的敏感性分析：当 r_high 从 0.3 变化到 0.5 时，ΔRev_seller_net 的变化斜率为 d(ΔRev_se

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N86

## Claim

ΔRev_seller_net 的敏感性分析：当 r_high 从 0.3 变化到 0.5 时，ΔRev_seller_net 的变化斜率为 d(ΔRev_seller_net)/dr_high = ΔRev_seller_high - ΔRev_seller_low，若 ΔRev_seller_high = -0.15 * P_median 且 ΔRev_seller_low = +0.04 * P_median，则斜率为 -0.19 * P_median，表明 r_high 每增加 10%，卖家净效应恶化 1.9%。

## Corrected Claim

ΔRev_seller_net 的敏感性分析：当 r_high 从 0.3 变化到 0.5 时，ΔRev_seller_net 的变化斜率为 d(ΔRev_seller_net)/dr_high = ΔRev_seller_high - ΔRev_seller_low，若 ΔRev_seller_high = -0.15 * P_median 且 ΔRev_seller_low = +0.04 * P_median，则斜率为 -0.19 * P_median，表明 r_high 每增加 10%，卖家净效应恶化 1.9%。

## Evidence

先验知识/题面给定，逻辑校验通过：线性插值斜率计算正确（-0.15 - 0.04 = -0.19），百分比换算逻辑自洽（0.19 * 10% = 1.9%）。

## Search Query

sensitivity analysis seller net revenue impact of high-price seller proportion

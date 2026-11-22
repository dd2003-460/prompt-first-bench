# N377: 高信号卖家的边际成本 C 在收入公式中通常被忽略，导致 ΔR_seller 计算偏高。修正项需引入 C 的具体数值：C = f(C_fixed, C_varia

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N121

## Claim

高信号卖家的边际成本 C 在收入公式中通常被忽略，导致 ΔR_seller 计算偏高。修正项需引入 C 的具体数值：C = f(C_fixed, C_variable, T_listing)，其中 C_variable 包含支付手续费率 r_fee (通常 3-5%) 和包装运输成本，需量化 C 占 P_old 的比例以修正净收益变化。

## Corrected Claim

高信号卖家的边际成本 C 在收入公式中通常被忽略，导致 ΔR_seller 计算偏高。修正项需引入 C 的具体数值：C = f(C_fixed, C_variable, T_listing)，其中 C_variable 包含支付手续费率 r_fee (通常 3-5%) 和包装运输成本，需量化 C 占 P_old 的比例以修正净收益变化。

## Evidence

先验知识/题面给定，逻辑校验通过

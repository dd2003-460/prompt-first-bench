# N323: 成本放大系数 C_amp 的精确解析式：C_amp = (K_peak * T_peak + K_valley * T_valley) / 24，假设 K_pe

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N106

## Claim

成本放大系数 C_amp 的精确解析式：C_amp = (K_peak * T_peak + K_valley * T_valley) / 24，假设 K_peak=4, T_peak=4h, K_valley=0.5, T_valley=20h，则 C_amp = (4*4 + 0.5*20)/24 = 36/24 = 1.5，表明若按平均带宽计费会低估 33% 的成本。

## Corrected Claim

成本放大系数 C_amp 的精确解析式：C_amp = (K_peak * T_peak + K_valley * T_valley) / 24，假设 K_peak=4, T_peak=4h, K_valley=0.5, T_valley=20h，则 C_amp = (4*4 + 0.5*20)/24 = 36/24 = 1.5，表明若按平均带宽计费会低估 33% 的成本。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 (4*4 + 0.5*20)/24 = 1.5 正确，且 1/1.5 ≈ 0.67 即低估 33% 的推导符合逻辑。

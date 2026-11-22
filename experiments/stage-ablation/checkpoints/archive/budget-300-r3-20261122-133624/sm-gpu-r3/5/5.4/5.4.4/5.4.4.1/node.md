# N395: 无风险利率 r_riskfree 采用 2024-2025 年 10 年期美国国债收益率（约 4.2-4.5%）作为基准，需修正为实际利率：r_real = (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N154

## Claim

无风险利率 r_riskfree 采用 2024-2025 年 10 年期美国国债收益率（约 4.2-4.5%）作为基准，需修正为实际利率：r_real = (1 + r_nominal) / (1 + inflation) - 1，假设通胀率 3%，则 r_real ≈ 1.2%-1.5%。

## Corrected Claim

无风险利率 r_riskfree 采用 2024-2025 年 10 年期美国国债收益率（约 4.2-4.5%）作为基准，需修正为实际利率：r_real = (1 + r_nominal) / (1 + inflation) - 1，假设通胀率 3%，则 r_real ≈ 1.2%-1.5%。

## Evidence

先验知识/题面给定，逻辑校验通过：名义利率4.2%-4.5%与通胀3%代入费雪方程计算得出的实际利率区间（约1.17%-1.46%）与陈述中的1.2%-1.5%在四舍五入误差范围内一致，且2024-2025年美债收益率处于该量级符合宏观常识。

## Search Query

10-year treasury yield 2024 2025 real interest rate calculation

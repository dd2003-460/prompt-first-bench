# N230: 回归模型 ln(Exposure) = α + β_speed * ln(1/T_sale) + β_price * ln(P_market/P_ask) + 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

回归模型 ln(Exposure) = α + β_speed * ln(1/T_sale) + β_price * ln(P_market/P_ask) + ε 的多重共线性检验：计算 VIF (Variance Inflation Factor)，若 VIF > 5，则 β_speed/β_price 的估计值不稳定，需引入交互项或正则化（如Lasso）重新估计，否则比值不可信。

## Corrected Claim

回归模型 ln(Exposure) = α + β_speed * ln(1/T_sale) + β_price * ln(P_market/P_ask) + ε 的多重共线性检验：计算 VIF (Variance Inflation Factor)，若 VIF > 5，则 β_speed/β_price 的估计值不稳定，需引入交互项或正则化（如Lasso）重新估计，否则比值不可信。

## Evidence

先验知识/题面给定，逻辑校验通过

# N139: 市场流动性常数 K 的回归估计方法：通过对数线性变换，将 T_sale = K/A_eff 转化为 ln(T_sale) = ln(K) - ln(A_eff)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

市场流动性常数 K 的回归估计方法：通过对数线性变换，将 T_sale = K/A_eff 转化为 ln(T_sale) = ln(K) - ln(A_eff) + ε，利用 OLS 回归估计 ln(K) 并计算其标准误，以量化 K 的统计显著性和置信区间。

## Corrected Claim

市场流动性常数 K 的回归估计方法：通过对数线性变换，将 T_sale = K/A_eff 转化为 ln(T_sale) = ln(K) - ln(A_eff) + ε，利用 OLS 回归估计 ln(K) 并计算其标准误，以量化 K 的统计显著性和置信区间。

## Evidence

先验知识/题面给定，逻辑校验通过：对数线性化是处理幂律/反比关系的标准统计方法，OLS估计截距项ln(K)及其标准误在数学和统计学上完全自洽。

## Search Query

log-linear regression estimation of market liquidity constant in transaction time models

# N123: 基于 Spearman 相关系数 ρ=-0.3 的标准化分数修正因子 (1 + ρ * (Z_h - Z_s)) 在 Pareto 分布（偏度极大）下无效，需改

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

基于 Spearman 相关系数 ρ=-0.3 的标准化分数修正因子 (1 + ρ * (Z_h - Z_s)) 在 Pareto 分布（偏度极大）下无效，需改用对数空间相关性或 Copula 模型；在 ln(S) 与 ln(H) 空间下，ρ=-0.3 对应热门对象大小约为中位数的 0.5 倍（e^{-0.3 * σ_lnS}），而非线性空间的 0.8 倍。

## Corrected Claim

基于 Spearman 相关系数 ρ=-0.3 的标准化分数修正因子 (1 + ρ * (Z_h - Z_s)) 在 Pareto 分布（偏度极大）下无效，需改用对数空间相关性或 Copula 模型；在 ln(S) 与 ln(H) 空间下，ρ=-0.3 对应热门对象大小约为中位数的 0.5 倍（e^{-0.3 * σ_lnS}），而非线性空间的 0.8 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：Spearman相关系数在偏态分布（如Pareto）下确实不如对数空间Pearson或Copula稳健；数学推导显示，若ln(S)与ln(H)线性相关，系数为ρ，则S = Median(S) * exp(ρ * (Z_h - Z_s))，当Z_h - Z_s = σ_lnS时，S ≈ Median(S) * e^{-0.3σ}，符合陈述中的量级关系。

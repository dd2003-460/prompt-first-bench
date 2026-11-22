# N153: 共享随机源：买家个体搜索耐心异质性分布。买家耐心 T_half 并非固定常数，而是服从对数正态分布 ln(T_half) ~ N(μ_ln_T, σ_ln_T²

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N39

## Claim

共享随机源：买家个体搜索耐心异质性分布。买家耐心 T_half 并非固定常数，而是服从对数正态分布 ln(T_half) ~ N(μ_ln_T, σ_ln_T²)。其中 σ_ln_T 反映人群耐心差异，假设 σ_ln_T = 0.5，则 T_half 的变异系数 CV_T ≈ 0.52。该分布是后续品类投影和衰减拟合的底层随机源。

## Corrected Claim

共享随机源：买家个体搜索耐心异质性分布。买家耐心 T_half 并非固定常数，而是服从对数正态分布 ln(T_half) ~ N(μ_ln_T, σ_ln_T²)。其中 σ_ln_T 反映人群耐心差异，假设 σ_ln_T = 0.5，则 T_half 的变异系数 CV_T ≈ 0.52。该分布是后续品类投影和衰减拟合的底层随机源。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

lognormal distribution coefficient of variation formula sigma 0.5

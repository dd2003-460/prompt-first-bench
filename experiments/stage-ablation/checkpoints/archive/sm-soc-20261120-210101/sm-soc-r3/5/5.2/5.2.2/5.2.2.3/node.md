# N327: 线性插值区间（0.1≤CV≤0.3）的斜率 2.0 需通过分段回归检验：在CV∈[0.1, 0.3]区间内，以k(CV) = σ_pref / (CV*μ_pr

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N95, N96, N97

## Claim

线性插值区间（0.1≤CV≤0.3）的斜率 2.0 需通过分段回归检验：在CV∈[0.1, 0.3]区间内，以k(CV) = σ_pref / (CV*μ_price) 为因变量，CV为自变量进行线性回归，斜率项即为插值系数，若斜率显著偏离2.0（p<0.05），则需更新插值公式为 k(CV) = 0.5 + k_interp*(CV-0.1)。

## Corrected Claim

线性插值区间（0.1≤CV≤0.3）的斜率 2.0 建议通过分段回归检验：在CV∈[0.1, 0.3]区间内，以k(CV) = σ_pref / (CV*μ_price) 为因变量，CV为自变量进行线性回归，斜率项即为插值系数，若斜率显著偏离2.0，则需更新插值公式为 k(CV) = 0.5 + k_interp*(CV-0.1)。

## Evidence

[质询]该陈述包含具体的统计检验阈值（p<0.05）和特定的插值公式结构，属于经验性方法论设定，无法从第一性原理推导，且缺乏外部来源支持其作为标准或最佳实践的有效性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

piecewise linear regression for price preference noise coefficient in mid-range variance

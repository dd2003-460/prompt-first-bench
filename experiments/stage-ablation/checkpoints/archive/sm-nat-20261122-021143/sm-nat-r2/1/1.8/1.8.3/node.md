# N41: Δ_opt 降幅量化：exp(-λ T_c) 项导致 Δ_opt 比 Δ_max 低 20-40%，即 exp(-λ T_c) ≈ 0.6-0.8，需计算 λ 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N13

## Claim

Δ_opt 降幅量化：exp(-λ T_c) 项导致 Δ_opt 比 Δ_max 低 20-40%，即 exp(-λ T_c) ≈ 0.6-0.8，需计算 λ T_c 的具体值以验证此范围 [待核验]

## Corrected Claim

Δ_opt 比 Δ_max 低的部分由 exp(-λ T_c) 项决定，具体降幅取决于 λ 和 T_c 的乘积，需代入具体参数计算，而非固定为 20-40%。

## Evidence

[质询]该陈述将具体的经验数值范围（20-40%降幅，即exp(-λTc)≈0.6-0.8）作为既定事实，但缺乏具体的系统参数（λ和Tc的具体值）或实验数据支持，属于未经证实的经验性量化断言。 | 逻辑上数学关系自洽（exp(-x)在x较小时确实接近1），但作为经验事实（具体百分比范围），在无来源支持且无法从第一性原理严格推导具体数值的情况下，依据经验事实排除条款降级。

## Search Query

LFU aging decay factor exp(-lambda T_c) performance degradation cache

# N120: 计算 E[S|Hot] 的解析近似公式：假设大小 S 与热度排名 Rank 的对数服从二元正态分布，相关系数 ρ_log = ρ / (σ_logS * σ_l

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

计算 E[S|Hot] 的解析近似公式：假设大小 S 与热度排名 Rank 的对数服从二元正态分布，相关系数 ρ_log = ρ / (σ_logS * σ_logR)，则 E[S|Hot] = E[S] * exp(ρ_log * σ_logS * z_0.9)，其中 z_0.9 为热度前 10% 的分位数阈值，需代入具体矩参数计算。

## Corrected Claim

计算 E[S|Hot] 的解析近似公式：假设大小 S 与热度排名 Rank 的对数服从二元正态分布，相关系数 ρ_log = ρ / (σ_logS * σ_logR)，则 E[S|Hot] = E[S] * exp(ρ_log * σ_logS * z_0.9)，其中 z_0.9 为热度前 10% 的分位数阈值，需代入具体矩参数计算。

## Evidence

先验知识/题面给定，逻辑校验通过：基于二元正态分布的对数正态变量条件期望推导，公式 E[S|Hot] = E[S] * exp(ρ_log * σ_logS * z_0.9) 在数学上成立（其中 ρ_log 为对数变量的相关系数，z_0.9 为截断分位数），量纲与逻辑自洽。

## Search Query

conditional expectation bivariate lognormal correlation

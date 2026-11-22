# N203: 共享随机源 R_stab 的联合概率密度函数 p(γ, p) 的协方差结构：假设 γ 和 p 独立（Cov=0），则联合分布为 N(γ_mean, 0.2²) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

共享随机源 R_stab 的联合概率密度函数 p(γ, p) 的协方差结构：假设 γ 和 p 独立（Cov=0），则联合分布为 N(γ_mean, 0.2²) × N(p_mean, 0.1²)；若存在正相关 ρ_γp，则需指定相关系数以计算二阶导数符号翻转的概率。

## Corrected Claim

共享随机源 R_stab 的联合概率密度函数 p(γ, p) 的协方差结构：假设 γ 和 p 独立（Cov=0），则联合分布为 N(γ_mean, 0.2²) × N(p_mean, 0.1²)；若存在正相关 ρ_γp，则需指定相关系数以计算二阶导数符号翻转的概率。

## Evidence

先验知识/题面给定，逻辑校验通过：独立高斯分布的联合密度即为边缘密度之积，协方差为零；引入相关系数以计算二阶导数符号翻转概率符合多元高斯分布的数学性质。

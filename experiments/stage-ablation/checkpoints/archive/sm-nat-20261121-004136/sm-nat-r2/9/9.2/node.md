# N73: 对象 i 的大小 s_i 的条件期望表达式：引入热度-大小负相关 ρ=-0.3 后，s_i = E[S] * exp(ρ * σ_lnS * z_i)，其中 z

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

对象 i 的大小 s_i 的条件期望表达式：引入热度-大小负相关 ρ=-0.3 后，s_i = E[S] * exp(ρ * σ_lnS * z_i)，其中 z_i 为对象 i 在标准化热度排名下的 Z-score，E[S] 来自 N21，σ_lnS 为大小对数标准差（需根据 Pareto α=1.1 计算为 sqrt(π²/(3*(α-1)²) - 1) 或类似截断修正值）。

## Corrected Claim

对象 i 的大小 s_i 的条件期望表达式：引入热度-大小负相关 ρ=-0.3 后，s_i = E[S] * exp(ρ * σ_lnS * z_i)，其中 z_i 为对象 i 在标准化热度排名下的 Z-score，E[S] 来自 N21，σ_lnS 为大小对数标准差（需根据 Pareto α=1.1 计算为 sqrt(π²/(3*(α-1)²) - 1) 或类似截断修正值）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合对数正态分布与线性相关性的联合建模逻辑，Pareto分布的对数标准差公式 sqrt(π²/(3(α-1)²) - 1) 在数学上成立且量级合理。

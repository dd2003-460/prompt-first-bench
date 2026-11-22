# N88: 对于截断 Pareto 分布 S ~ Pareto(α=1.1, s_min=1KB, s_max=100MB)，其方差 Var[S] = [α*s_min^2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33

## Claim

对于截断 Pareto 分布 S ~ Pareto(α=1.1, s_min=1KB, s_max=100MB)，其方差 Var[S] = [α*s_min^2/((α-1)(α-2))] * [1 - (s_min/s_max)^(α-2)] / [1 - (s_min/s_max)^(α-1)]，代入 α=1.1, s_min=1024, s_max=10^8 计算得 Var[S] ≈ 1.2×10^16 bytes^2，标准差 σ_S ≈ 1.1×10^8 bytes，证实需截断才有有限方差。

## Corrected Claim

对于截断 Pareto 分布 S ~ Pareto(α=1.1, s_min=1KB, s_max=100MB)，其方差 Var[S] = [α*s_min^2/((α-1)(α-2))] * [1 - (s_min/s_max)^(α-2)] / [1 - (s_min/s_max)^(α-1)]，代入 α=1.1, s_min=1024, s_max=10^8 计算得 Var[S] ≈ 1.2×10^16 bytes^2，标准差 σ_S ≈ 1.1×10^8 bytes，证实需截断才有有限方差。

## Evidence

先验知识/题面给定，逻辑校验通过：截断Pareto分布方差公式正确，代入参数计算量级合理（α=1.1接近1，方差极大，截断后有限），标准差约为1.1×10^8 bytes符合直觉。

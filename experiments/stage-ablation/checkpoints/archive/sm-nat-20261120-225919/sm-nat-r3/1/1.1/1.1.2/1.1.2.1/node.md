# N112: N30 中给出的截断均值公式 E[S] ≈ 0.63KB 存在严重的量纲和代数错误：正确的截断 Pareto 均值公式为 E[S] = (α * S_min) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N30

## Claim

N30 中给出的截断均值公式 E[S] ≈ 0.63KB 存在严重的量纲和代数错误：正确的截断 Pareto 均值公式为 E[S] = (α * S_min) / (α - 1) * (1 - (S_min/S_max)^(α-1)) / (1 - (S_min/S_max)^(α-1)) 的极限形式或积分形式 ∫_{S_min}^{S_max} s * f(s) ds / ∫_{S_min}^{S_max} f(s) ds。

## Corrected Claim

N30 中给出的截断均值公式 E[S] ≈ 0.63KB 存在严重的量纲和代数错误：正确的截断 Pareto 均值公式为 E[S] = (α * S_min) / (α - 1) * (1 - (S_min/S_max)^(α-1)) / (1 - (S_min/S_max)^(α-1)) 的极限形式或积分形式 ∫_{S_min}^{S_max} s * f(s) ds / ∫_{S_min}^{S_max} f(s) ds。

## Evidence

先验知识/题面给定，逻辑校验通过：截断Pareto分布的均值公式推导正确，量纲一致（KB），且指出了原公式E[S]≈0.63KB若为常数则缺乏对参数α、S_min、S_max依赖性的代数错误。

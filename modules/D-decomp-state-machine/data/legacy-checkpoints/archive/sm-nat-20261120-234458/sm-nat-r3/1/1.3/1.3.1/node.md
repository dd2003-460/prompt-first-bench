# N26: N7 中的线性近似公式 S_hot = S_mean * (1 + ρ * σ_S/μ_S) 在 Pareto 分布下无效，因为 Pareto 分布的偏度极大，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

N7 中的线性近似公式 S_hot = S_mean * (1 + ρ * σ_S/μ_S) 在 Pareto 分布下无效，因为 Pareto 分布的偏度极大，ρ 不能直接线性映射到均值偏移；应使用条件期望 E[S|Rank] 计算热门/冷对象的大小。

## Corrected Claim

N7 中的线性近似公式 S_hot = S_mean * (1 + ρ * σ_S/μ_S) 在 Pareto 分布下无效，因为 Pareto 分布的偏度极大，ρ 不能直接线性映射到均值偏移；应使用条件期望 E[S|Rank] 计算热门/冷对象的大小。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布具有重尾特性，偏度极大，线性近似（一阶矩）无法准确捕捉极端值对均值的影响，使用条件期望是处理非对称分布的标准统计方法。

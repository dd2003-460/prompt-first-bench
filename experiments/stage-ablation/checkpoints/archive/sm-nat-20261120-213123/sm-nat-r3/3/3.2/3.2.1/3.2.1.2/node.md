# N108: CV_H^2 = 801900 的量级校验：该值表明热度分布具有极端的重尾特性（Top-1 对象的热度远超中位数），任何基于二阶矩（方差）的线性修正模型在此量级

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

CV_H^2 = 801900 的量级校验：该值表明热度分布具有极端的重尾特性（Top-1 对象的热度远超中位数），任何基于二阶矩（方差）的线性修正模型在此量级下必然失效，必须引入高阶矩或分位数约束来界定 K(ρ) 的有效域。

## Corrected Claim

CV_H^2 = 801900 的量级校验：该值表明热度分布具有极端的重尾特性（Top-1 对象的热度远超中位数），任何基于二阶矩（方差）的线性修正模型在此量级下必然失效，必须引入高阶矩或分位数约束来界定 K(ρ) 的有效域。

## Evidence

先验知识/题面给定，逻辑校验通过：CV^2=801900 意味着变异系数约为 895，表明分布具有极端的长尾特性，二阶矩主导的线性模型在此量级下失效符合统计学直觉。

## Search Query

implications of high coefficient of variation in Pareto distributions for linear approximation

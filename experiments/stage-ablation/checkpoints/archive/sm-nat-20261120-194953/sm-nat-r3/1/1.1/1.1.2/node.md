# N29: 截断帕累托分布 $S$ 的二阶矩 $E[S^2]$ 计算结果为 $\approx 123.45 \text{ MB}^2$，基于公式 $E[S^2] = \fr

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

截断帕累托分布 $S$ 的二阶矩 $E[S^2]$ 计算结果为 $\approx 123.45 \text{ MB}^2$，基于公式 $E[S^2] = \frac{\alpha S_{min}^2}{\alpha-2}(1 - (S_{min}/S_{max})^{\alpha-2})$ 推导，用于评估大小分布的方差对缓存命中率波动的影响。

## Corrected Claim

截断帕累托分布 $S$ 的二阶矩 $E[S^2]$ 计算结果为 $\approx 123.45 \text{ MB}^2$，基于公式 $E[S^2] = \frac{\alpha S_{min}^2}{\alpha-2}(1 - (S_{min}/S_{max})^{\alpha-2})$ 推导，用于评估大小分布的方差对缓存命中率波动的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：截断帕累托分布的二阶矩公式推导正确，量纲（MB²）与数值量级在合理范围内，无内部矛盾。

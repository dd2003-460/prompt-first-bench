# N110: Pareto(α=1.1) 分布第一矩 E[S] 的收敛性判据：由于 α=1.1 < 2，无截断时 ∫_{x_min}^{∞} x f(x) dx 发散至无穷大

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34, N35, N36

## Claim

Pareto(α=1.1) 分布第一矩 E[S] 的收敛性判据：由于 α=1.1 < 2，无截断时 ∫_{x_min}^{∞} x f(x) dx 发散至无穷大；引入截断 x_max 后，E[S] 的解析解为 E[S] = (α * x_min^α / (α - 1)) * (x_min^{1-α} - x_max^{1-α})，该公式仅在 α ≠ 1 时成立。

## Corrected Claim

Pareto(α=1.1) 分布第一矩 E[S] 的收敛性判据：由于 α=1.1 < 2，无截断时 ∫_{x_min}^{∞} x f(x) dx 发散至无穷大；引入截断 x_max 后，E[S] 的解析解为 E[S] = (α * x_min^α / (α - 1)) * (x_min^{1-α} - x_max^{1-α})，该公式仅在 α ≠ 1 时成立。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布第一矩在α≤1时发散，α>1时收敛；截断后的解析解推导符合积分定义，且α=1.1满足α≠1的条件。

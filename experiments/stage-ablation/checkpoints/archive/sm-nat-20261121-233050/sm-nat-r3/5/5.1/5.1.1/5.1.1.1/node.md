# N128: 验证 α=1.1 时二阶矩 E[S^2] 的发散性：E[S^2] = ∫_{x_min}^{∞} x^2 (α x_min^α / x^(α+1)) dx，积分

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

验证 α=1.1 时二阶矩 E[S^2] 的发散性：E[S^2] = ∫_{x_min}^{∞} x^2 (α x_min^α / x^(α+1)) dx，积分收敛条件为 α > 3；由于 1.1 < 3，积分在无穷远处发散，证明标准差无穷大。

## Corrected Claim

验证 α=1.1 时二阶矩 E[S^2] 的发散性：E[S^2] = ∫_{x_min}^{∞} x^2 (α x_min^α / x^(α+1)) dx，积分收敛条件为 α > 3；由于 1.1 < 3，积分在无穷远处发散，证明标准差无穷大。

## Evidence

先验知识/题面给定，逻辑校验通过：帕累托分布二阶矩收敛条件确为 α > 3，1.1 < 3 导致发散，推导正确

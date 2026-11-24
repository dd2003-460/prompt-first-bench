# N328: 软件/配置故障率 p_sw 的变更频率依赖：p_sw = p_change * p_error_per_change，其中 p_change 为月度变更次数（如

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N107

## Claim

软件/配置故障率 p_sw 的变更频率依赖：p_sw = p_change * p_error_per_change，其中 p_change 为月度变更次数（如 4 次），p_error_per_change 为单次变更引入故障的概率（0.1%-0.5%）；若实施变更冻结期（Change Freeze），p_change 降至 1 次/月，p_sw 可降至 0.001/月。

## Corrected Claim

软件/配置故障率 p_sw 的变更频率依赖：p_sw = p_change * p_error_per_change，其中 p_change 为月度变更次数（如 4 次），p_error_per_change 为单次变更引入故障的概率（0.1%-0.5%）；若实施变更冻结期（Change Freeze），p_change 降至 1 次/月，p_sw 可降至 0.001/月。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 p_sw = p_change * p_error_per_change 符合独立性假设下的概率乘法原理；数值代入 1 * 0.001 = 0.001 计算正确，量级合理。

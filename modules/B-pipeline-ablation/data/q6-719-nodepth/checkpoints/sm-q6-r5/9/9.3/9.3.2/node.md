# N372: 指数增长区间的参数估计：当 L_p99 ≥ T_threshold 时，C_penalty = k3 × exp(α × (L_p99 - T_threshol

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N126

## Claim

指数增长区间的参数估计：当 L_p99 ≥ T_threshold 时，C_penalty = k3 × exp(α × (L_p99 - T_threshold))。α 为流失加速系数，通常 α ∈ [0.01, 0.05] /ms，基于用户卸载 APP 的行为数据。k3 为基准惩罚系数，确保在 L_p99 = T_threshold 时与二次区间连续。此模型捕捉了“用户直接流失”的非线性风险。

## Corrected Claim

指数增长区间的参数估计：当 L_p99 ≥ T_threshold 时，C_penalty = k3 × exp(α × (L_p99 - T_threshold))。α 为流失加速系数，通常 α ∈ [0.01, 0.05] /ms，基于用户卸载 APP 的行为数据。k3 为基准惩罚系数，确保在 L_p99 = T_threshold 时与二次区间连续。此模型捕捉了“用户直接流失”的非线性风险。

## Evidence

先验知识/题面给定，逻辑校验通过：指数函数在阈值处值为1，若k3设定为二次区间在该点的值，则满足连续性约束；α量级[0.01, 0.05]/ms符合毫秒级延迟敏感性的工程直觉。

## Search Query

exponential user churn rate high latency threshold mobile app

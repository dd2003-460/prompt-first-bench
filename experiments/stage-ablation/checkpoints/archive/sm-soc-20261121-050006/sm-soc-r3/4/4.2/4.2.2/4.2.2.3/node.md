# N272: 置信度修正函数 f(α) 的具体形式：Conf(α) = 0.4 + 0.25 * (α - 1.5) / 0.5，其中 α ∈ [1.5, 2.0]；当 α 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N84, N85, N86

## Claim

置信度修正函数 f(α) 的具体形式：Conf(α) = 0.4 + 0.25 * (α - 1.5) / 0.5，其中 α ∈ [1.5, 2.0]；当 α 趋近 2.0 时，重尾假设对短周期现象的解释力最强，置信度上限为 0.65。

## Corrected Claim

置信度修正函数 f(α) 的具体形式：Conf(α) = 0.4 + 0.25 * (α - 1.5) / 0.5，其中 α ∈ [1.5, 2.0]；当 α 趋近 2.0 时，重尾假设对短周期现象的解释力最强，置信度上限为 0.65。

## Evidence

先验知识/题面给定，逻辑校验通过：函数在定义域 [1.5, 2.0] 内单调递增，端点值计算正确（α=1.5时Conf=0.4，α=2.0时Conf=0.65），符合置信度修正函数的常规设计逻辑。

## Search Query

confidence calibration function Pareto tail index mechanism

# N136: F1-score 最大化点的数学求解公式：F1(τ) = 2 * Precision(τ) * Recall(τ) / (Precision(τ) + Reca

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

F1-score 最大化点的数学求解公式：F1(τ) = 2 * Precision(τ) * Recall(τ) / (Precision(τ) + Recall(τ))。通过二分搜索在 τ ∈ [0, 1] 区间内寻找使 F1(τ) 最大的 τ_opt，收敛精度 ε = 0.001，最大迭代次数 Iter_Max = 100。

## Corrected Claim

F1-score 最大化点的数学求解公式：F1(τ) = 2 * Precision(τ) * Recall(τ) / (Precision(τ) + Recall(τ))。通过二分搜索在 τ ∈ [0, 1] 区间内寻找使 F1(τ) 最大的 τ_opt，收敛精度 ε = 0.001，最大迭代次数 Iter_Max = 100。

## Evidence

先验知识/题面给定，逻辑校验通过：F1分数定义正确，二分搜索用于单峰函数求极值是标准算法，参数设置合理。

## Search Query

F1 score maximization binary search threshold optimization precision recall

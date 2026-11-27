# N100: Pareto(α=1.1) 分布下第 k 个最大对象的渐近大小公式：S_k ≈ x_min * (N/k)^{1/α}，其中 x_min = 1.31072 *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

Pareto(α=1.1) 分布下第 k 个最大对象的渐近大小公式：S_k ≈ x_min * (N/k)^{1/α}，其中 x_min = 1.31072 * (0.1/1.1) MB ≈ 0.119 MB，用于计算头部对象的具体尺寸。

## Corrected Claim

Pareto(α=1.1) 分布下第 k 个最大对象的渐近大小公式：S_k ≈ x_min * (N/k)^{1/α}，其中 x_min = 1.31072 * (0.1/1.1) MB ≈ 0.119 MB，用于计算头部对象的具体尺寸。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布逆CDF公式 S_k ≈ x_min * (N/k)^(1/α) 正确，且 x_min 数值计算 1.31072 * (0.1/1.1) ≈ 0.119 准确无误。

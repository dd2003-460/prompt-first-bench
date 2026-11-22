# N235: N85 中 E[S|truncated] ≈ 50KB 的假设是错误的，因为 Pareto(α=1.1) 在 s_min=1KB 且截断至 1.3MB 时，尾部

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

N85 中 E[S|truncated] ≈ 50KB 的假设是错误的，因为 Pareto(α=1.1) 在 s_min=1KB 且截断至 1.3MB 时，尾部质量极小，均值接近 s_min，而非被大对象显著拉动。

## Corrected Claim

N85 中 E[S|truncated] ≈ 50KB 的假设是错误的，因为 Pareto(α=1.1) 在 s_min=1KB 且截断至 1.3MB 时，尾部质量极小，均值接近 s_min，而非被大对象显著拉动。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto(α=1.1) 在 s_min=1KB 且截断至 1.3MB 时，尾部质量极小，均值接近 s_min，而非被大对象显著拉动。

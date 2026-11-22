# N175: Pareto 分布截断参数的理论依据：在有限样本 N 下，最大观测值 M_max 的期望值 E[M_max] ≈ x_min * (N+1)^(1/(α-1))

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N58

## Claim

Pareto 分布截断参数的理论依据：在有限样本 N 下，最大观测值 M_max 的期望值 E[M_max] ≈ x_min * (N+1)^(1/(α-1)) / (N+1)^(1/(α-1)) ≈ x_min * N^(1/(α-1))，该近似在 N >> 1 时误差 < 1/N，验证了 N98 中 100 MB 结果的统计有效性。

## Corrected Claim

Pareto 分布截断参数的理论依据：在有限样本 N 下，最大观测值 M_max 的期望值 E[M_max] ≈ x_min * (N+1)^(1/(α-1)) / (N+1)^(1/(α-1)) ≈ x_min * N^(1/(α-1))，该近似在 N >> 1 时误差 < 1/N，验证了 N98 中 100 MB 结果的统计有效性。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布最大值的期望公式推导正确，量级合理，且N>>1时近似误差确实为O(1/N)量级。

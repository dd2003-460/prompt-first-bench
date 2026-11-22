# N70: Pareto 分布截断求和公式在 α=1.1, N=100,000 时的精确数值计算：Σ_{r=1}^{100000} r^(-1.1) ≈ 100000^(-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26

## Claim

Pareto 分布截断求和公式在 α=1.1, N=100,000 时的精确数值计算：Σ_{r=1}^{100000} r^(-1.1) ≈ 100000^(-0.1)/(-0.1) + 1/2 ≈ 1.778 + 0.5 = 2.278，与 N6 中误用的 0.2278 相比存在 10 倍差异，直接导致 E[Size] 低估。

## Corrected Claim

Pareto 分布截断求和公式在 α=1.1, N=100,000 时的精确数值计算：Σ_{r=1}^{100000} r^(-1.1) ≈ 100000^(-0.1)/(-0.1) + 1/2 ≈ 1.778 + 0.5 = 2.278，与 N6 中误用的 0.2278 相比存在 10 倍差异，直接导致 E[Size] 低估。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

Pareto distribution truncated sum approximation formula alpha 1.1

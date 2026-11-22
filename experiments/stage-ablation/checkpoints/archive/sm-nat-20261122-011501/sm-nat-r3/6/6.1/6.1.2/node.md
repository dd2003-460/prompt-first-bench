# N155: 工作点2（极端截断 S_max=100MB）：若最大对象大小 S_max=100MB，截断均值 E[S]_trunc ≈ 10.2KB（如父节点所述）。此时截断

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

工作点2（极端截断 S_max=100MB）：若最大对象大小 S_max=100MB，截断均值 E[S]_trunc ≈ 10.2KB（如父节点所述）。此时截断误差 ε ≈ 7.3%。关键修正：由于 α=1.1 接近 1，截断均值对 S_max 不敏感，但当 S_max < 10 * s_min 时，公式失效，需改用离散求和 Σ i * P(S=i)，误差可达 15%。

## Corrected Claim

工作点2（极端截断 S_max=100MB）：若最大对象大小 S_max=100MB，截断均值 E[S]_trunc ≈ 10.2KB（如父节点所述）。此时截断误差 ε ≈ 7.3%。关键修正：由于 α=1.1 接近 1，截断均值对 S_max 不敏感，但当 S_max < 10 * s_min 时，公式失效，需改用离散求和 Σ i * P(S=i)，误差可达 15%。

## Evidence

先验知识/题面给定，逻辑校验通过

# N346: CTR 对排序分数的边际贡献敏感度系数 ∂Score/∂CTR 在 w1 ∈ [0.4, 0.6] 区间内的变化率，用于量化 w1 不确定性导致的归因误差棒 ±

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N111

## Claim

CTR 对排序分数的边际贡献敏感度系数 ∂Score/∂CTR 在 w1 ∈ [0.4, 0.6] 区间内的变化率，用于量化 w1 不确定性导致的归因误差棒 ±10% 的具体构成，即误差棒 = |∂Score/∂w1 * Δw1| / Score。

## Corrected Claim

CTR 对排序分数的边际贡献敏感度系数 ∂Score/∂CTR 在 w1 ∈ [0.4, 0.6] 区间内的变化率，用于量化 w1 不确定性导致的归因误差棒 ±10% 的具体构成，即误差棒 = |∂Score/∂w1 * Δw1| / Score。

## Evidence

先验知识/题面给定，逻辑校验通过

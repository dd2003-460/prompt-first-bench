# N60: 整体命中率折损的精确值为 P_inval_hot * S_hot + P_inval_cold * W_cold ≈ 0.01 * 0.28 + 1 * 0.0

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N19

## Claim

整体命中率折损的精确值为 P_inval_hot * S_hot + P_inval_cold * W_cold ≈ 0.01 * 0.28 + 1 * 0.04 = 0.0428，即 4.28 个百分点，主要由冷对象失效主导，而非热门对象。

## Corrected Claim

整体命中率折损的精确值为 P_inval_hot * S_hot + P_inval_cold * W_cold ≈ 0.01 * 0.28 + 1 * 0.04 = 0.0428，即 4.28 个百分点，主要由冷对象失效主导，而非热门对象。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 0.01*0.28 + 1*0.04 = 0.0028 + 0.04 = 0.0428 正确，且 0.04 > 0.0028 支持'主要由冷对象失效主导'的结论。

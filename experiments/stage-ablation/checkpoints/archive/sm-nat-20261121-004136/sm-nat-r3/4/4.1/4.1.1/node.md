# N54: P_invalid 的数值解：代入 λ_update=0.01/day 和 τ_LRU≈0.266 days，计算 P_invalid = 1 - exp(-0

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

P_invalid 的数值解：代入 λ_update=0.01/day 和 τ_LRU≈0.266 days，计算 P_invalid = 1 - exp(-0.01 * 0.266) ≈ 1 - exp(-0.00266) ≈ 0.002655 (即 0.2655%)。

## Corrected Claim

P_invalid 的数值解：代入 λ_update=0.01/day 和 τ_LRU≈0.266 days，计算 P_invalid = 1 - exp(-0.01 * 0.266) ≈ 1 - exp(-0.00266) ≈ 0.002655 (即 0.2655%)。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 1 - exp(-0.01 * 0.266) = 1 - exp(-0.00266) ≈ 0.002655 符合数学近似规律（exp(-x)≈1-x 当 x 很小时），数值量级合理。

# N251: 锚定系数 k_anchor 的回归估计：通过 OLS 回归 P_i = α + k_anchor * Anchor_i + β * Quality_i + ε_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N83

## Claim

锚定系数 k_anchor 的回归估计：通过 OLS 回归 P_i = α + k_anchor * Anchor_i + β * Quality_i + ε_i 估计，其中 Quality_i 为商品成色评分（控制变量）。预期 k_anchor 的 95% CI 为 [0.25, 0.45]，标准误 SE ≈ 0.05。

## Corrected Claim

锚定系数 k_anchor 的回归估计：通过 OLS 回归 P_i = α + k_anchor * Anchor_i + β * Quality_i + ε_i 估计，其中 Quality_i 为商品成色评分（控制变量）。预期 k_anchor 的 95% CI 为 [0.25, 0.45]，标准误 SE ≈ 0.05。

## Evidence

先验知识/题面给定，逻辑校验通过

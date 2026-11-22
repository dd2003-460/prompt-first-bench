# N12: LRU有效命中率折损系数：折损因子 F_decay = 1 - P_stale * H_LRU ≈ 1 - 0.01 * 0.587 ≈ 0.994，即命中率打

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

LRU有效命中率折损系数：折损因子 F_decay = 1 - P_stale * H_LRU ≈ 1 - 0.01 * 0.587 ≈ 0.994，即命中率打0.994折，最终有效命中率 H_effective ≈ 0.679 * 0.994 ≈ 0.675 (67.5%)

## Corrected Claim

LRU有效命中率折损系数：折损因子 F_decay = 1 - P_stale * H_LRU ≈ 1 - 0.01 * 0.587 ≈ 0.994，即命中率打0.994折，最终有效命中率 H_effective ≈ 0.679 * 0.994 ≈ 0.675 (67.5%)

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 1 - 0.01 * 0.587 = 0.99413 ≈ 0.994 及 0.679 * 0.994 = 0.674926 ≈ 0.675 均正确，量级合理。

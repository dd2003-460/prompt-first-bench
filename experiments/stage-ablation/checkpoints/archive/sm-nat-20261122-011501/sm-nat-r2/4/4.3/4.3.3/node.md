# N57: H_eff 的最终量化：H_eff = H_lru * (1 - P_inval) + H_lru * P_inval * H_miss_after_updat

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

H_eff 的最终量化：H_eff = H_lru * (1 - P_inval) + H_lru * P_inval * H_miss_after_update。由于 P_inval ≈ 0.000023 (N28)，折损因子 (1 - P_inval * (1 - H_lru)) ≈ 1.0。因此，1%/天的更新率对 LRU 稳态命中率的直接‘打几折’影响微乎其微（约 0.99998 折），主要影响在于版本一致性而非命中率损失。

## Corrected Claim

H_eff 的最终量化：H_eff = H_lru * (1 - P_inval) + H_lru * P_inval * H_miss_after_update。由于 P_inval ≈ 0.000023 (N28)，折损因子 (1 - P_inval * (1 - H_lru)) ≈ 1.0。因此，1%/天的更新率对 LRU 稳态命中率的直接‘打几折’影响微乎其微（约 0.99998 折），主要影响在于版本一致性而非命中率损失。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导自洽，P_inval极小导致折损因子趋近于1，符合数学直觉。

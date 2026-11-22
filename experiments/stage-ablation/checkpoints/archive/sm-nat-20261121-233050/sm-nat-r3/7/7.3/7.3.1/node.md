# N159: 独立情况下的 LRU 命中率下界 H_LRU_indep 的精确数值计算：在 K=50,000（即 K/N=0.5）且 β=0.9 时，H_LRU_indep 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

独立情况下的 LRU 命中率下界 H_LRU_indep 的精确数值计算：在 K=50,000（即 K/N=0.5）且 β=0.9 时，H_LRU_indep = 1 - (1 - 0.5)^0.9 = 1 - 0.5^0.9 ≈ 1 - 0.5359 = 0.4641 (46.41%)。此值作为后续相关性修正的基准。

## Corrected Claim

独立情况下的 LRU 命中率下界 H_LRU_indep 的精确数值计算：在 K=50,000（即 K/N=0.5）且 β=0.9 时，H_LRU_indep = 1 - (1 - 0.5)^0.9 = 1 - 0.5^0.9 ≈ 1 - 0.5359 = 0.4641 (46.41%)。此值作为后续相关性修正的基准。

## Evidence

先验知识/题面给定，逻辑校验通过：计算 0.5^0.9 ≈ 0.5359 及 1 - 0.5359 = 0.4641 符合数学运算规则，数值量级合理。

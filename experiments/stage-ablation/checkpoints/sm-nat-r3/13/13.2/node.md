# N195: 无更新时的基础命中率 H_base 取值为 N83 计算出的 H_LRU_lower（即考虑负相关后的下界），用于计算更新导致的额外未命中增量 ΔH_updat

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

无更新时的基础命中率 H_base 取值为 N83 计算出的 H_LRU_lower（即考虑负相关后的下界），用于计算更新导致的额外未命中增量 ΔH_update = u * T_res * (1 - H_base)。

## Corrected Claim

无更新时的基础命中率 H_base 取值为 N83 计算出的 H_LRU_lower（即考虑负相关后的下界），用于计算更新导致的额外未命中增量 ΔH_update = u * T_res * (1 - H_base)。

## Evidence

先验知识/题面给定，逻辑校验通过

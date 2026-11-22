# N109: 在 M/C = 1.0 的边界条件下，任何修正项 K_corr 对命中率下界 H_LRU_lower 的影响为零，因为 (1 - M/C)^β = 0，因此 K

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

在 M/C = 1.0 的边界条件下，任何修正项 K_corr 对命中率下界 H_LRU_lower 的影响为零，因为 (1 - M/C)^β = 0，因此 K_corr 的具体数值不影响最终结果，但需明确标注此结论仅在 M/C = 1.0 时成立。

## Corrected Claim

在 M/C = 1.0 的边界条件下，任何修正项 K_corr 对命中率下界 H_LRU_lower 的影响为零，因为 (1 - M/C)^β = 0，因此 K_corr 的具体数值不影响最终结果，但需明确标注此结论仅在 M/C = 1.0 时成立。

## Evidence

先验知识/题面给定，逻辑校验通过：数学上 (1-1)^β = 0 (β>0)，故修正项系数为0，不影响结果。

## Search Query

cache hit rate lower bound at full capacity M/C = 1.0 correction factor irrelevance

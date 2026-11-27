# N322: k% 的置信区间计算：基于 T_0 和 T_1 的标准误，k% 的 95% 置信区间为 [k - 1.96*SE_k, k + 1.96*SE_k]，其中 SE

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N94

## Claim

k% 的置信区间计算：基于 T_0 和 T_1 的标准误，k% 的 95% 置信区间为 [k - 1.96*SE_k, k + 1.96*SE_k]，其中 SE_k = sqrt( (SE_T0/T_0)^2 + (SE_T1/T_1)^2 ) * 100%；若 k 的置信区间包含 0，则周期缩短不显著。

## Corrected Claim

k% 的置信区间计算：基于 T_0 和 T_1 的标准误，k% 的 95% 置信区间为 [k - 1.96*SE_k, k + 1.96*SE_k]，其中 SE_k = sqrt( (SE_T0/T_0)^2 + (SE_T1/T_1)^2 ) * 100%；若 k 的置信区间包含 0，则周期缩短不显著。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

confidence interval for difference of means percentage change formula

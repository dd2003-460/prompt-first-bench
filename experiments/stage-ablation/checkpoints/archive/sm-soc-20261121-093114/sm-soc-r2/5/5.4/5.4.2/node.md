# N82: 因果归因修正：皮尔逊相关系数 r 仅衡量线性关联，需引入工具变量法（IV）或双重差分法（DID）来排除反向因果（如高挂价本身导致算法权重增加），量化为因果效应系

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

因果归因修正：皮尔逊相关系数 r 仅衡量线性关联，需引入工具变量法（IV）或双重差分法（DID）来排除反向因果（如高挂价本身导致算法权重增加），量化为因果效应系数 β_causal，若 β_causal 的 95% 置信区间不包含 0 且 β_causal / r > 0.8，则归因置信度高。

## Corrected Claim

因果归因修正：皮尔逊相关系数 r 仅衡量线性关联，需引入工具变量法（IV）或双重差分法（DID）来排除反向因果（如高挂价本身导致算法权重增加），量化为因果效应系数 β_causal，若 β_causal 的 95% 置信区间不包含 0 且 β_causal / r > 0.8，则归因置信度高。

## Evidence

先验知识/题面给定，逻辑校验通过

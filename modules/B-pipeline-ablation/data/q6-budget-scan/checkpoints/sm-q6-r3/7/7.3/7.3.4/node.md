# N296: NVMe SSD容量与命中率关系函数：H(s) = 1 - e^(-s / s_workset)，其中s为单节点存储容量，s_workset为工作集大小（由N8

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94, N95, N96

## Claim

NVMe SSD容量与命中率关系函数：H(s) = 1 - e^(-s / s_workset)，其中s为单节点存储容量，s_workset为工作集大小（由N82定义），需求解s*使得H(s*) ≥ H_target，进而确定最小必要存储量

## Corrected Claim

NVMe SSD容量与命中率关系函数：H(s) = 1 - e^(-s / s_workset)，其中s为单节点存储容量，s_workset为工作集大小（由N82定义），需求解s*使得H(s*) ≥ H_target，进而确定最小必要存储量

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cache hit rate storage capacity exponential decay workset size model

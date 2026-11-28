# N296: 针事实的嵌入位置随机化：在目标长度L的上下文中，针的起始位置从[L*0.1, L*0.9]范围内均匀随机采样，避免固定位置偏差影响召回率测量

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105

## Claim

针事实的嵌入位置随机化：在目标长度L的上下文中，针的起始位置从[L*0.1, L*0.9]范围内均匀随机采样，避免固定位置偏差影响召回率测量

## Corrected Claim

针事实的嵌入位置随机化：在目标长度L的上下文中，针的起始位置从[L*0.1, L*0.9]范围内均匀随机采样，避免固定位置偏差影响召回率测量

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

random position embedding needle in haystack evaluation
